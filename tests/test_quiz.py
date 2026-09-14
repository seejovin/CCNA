from copy import deepcopy
from pathlib import Path

import pytest
import browser_storage
import collection_storage

from streamlit.testing.v1 import AppTest
from quiz_core import is_correct, load_bank, response_error, summarize, validate_bank

ROOT = Path(__file__).resolve().parents[1]


@pytest.fixture(autouse=True)
def saved_browser(monkeypatch):
    # AppTest has no JS runtime. Model browser acknowledgements here; exercise
    # the actual frontend protocol separately in test_browser_storage.mjs.
    storage = {"payload": None, "ready": True, "writes": 0, "sets": {}}

    def sync(payload, *, bank_id=browser_storage.DEFAULT_BANK_ID):
        if payload is None:
            data = storage["payload"] if bank_id == browser_storage.DEFAULT_BANK_ID else storage["sets"].get(bank_id)
            return {"status": "loaded", "payload": deepcopy(data)} if storage["ready"] else {}
        storage["writes"] += 1
        storage["sets"][bank_id] = deepcopy(payload)
        if bank_id == browser_storage.DEFAULT_BANK_ID:
            storage["payload"] = deepcopy(payload)
        return {"status": "saved", "request_id": browser_storage.storage_request_id(payload)}

    monkeypatch.setattr(browser_storage, "sync_storage", sync)
    def snapshot(token):
        records = {bank_id: deepcopy(storage["sets"].get(bank_id)) for bank_id in collection_storage.BANK_IDS}
        records[browser_storage.DEFAULT_BANK_ID] = deepcopy(storage["payload"])
        return {"status": "loaded", "records": records, "errors": {}}
    monkeypatch.setattr(collection_storage, "read_collection_progress", snapshot)
    return storage


def test_bank_structure_and_exact_distribution():
    assert validate_bank(load_bank())


def test_scoring_rejects_partial_extra_duplicate_and_incomplete_answers():
    bank = load_bank()["questions"]
    single = next(q for q in bank if q["type"] == "single")
    assert is_correct(single, single["answer"])
    assert not is_correct(single, [])
    assert not is_correct(single, [single["answer"][0], single["answer"][0]])
    multiple = next(q for q in bank if q["type"] == "multiple")
    assert is_correct(multiple, list(reversed(multiple["answer"])))
    assert not is_correct(multiple, multiple["answer"][:1])
    wrong = next(c["id"] for c in multiple["choices"] if c["id"] not in multiple["answer"])
    assert not is_correct(multiple, multiple["answer"] + [wrong])
    assert not is_correct(multiple, [wrong, *multiple["answer"][1:]])
    matching = next(q for q in bank if q["type"] == "matching")
    response = {p["id"]: p["answer"] for p in matching["pairs"]}
    assert is_correct(matching, response)
    incomplete = deepcopy(response)
    incomplete.pop(next(iter(incomplete)))
    assert response_error(matching, incomplete)
    first = next(iter(response))
    response[first] = next(c["id"] for c in matching["choices"] if c["id"] != response[first])
    assert not is_correct(matching, response)


def click(at, label):
    next(b for b in at.button if b.label == label).click().run()
    assert not at.exception
    return at


def start():
    at = AppTest.from_file(ROOT / "app.py", default_timeout=20).run()
    assert not at.exception
    return at


def jump(at, q):
    at.selectbox(key="jump").set_value(q["id"]).run()
    assert not at.exception


def test_submission_reveal_navigation_and_reset():
    q = next(q for q in load_bank()["questions"] if q["type"] == "single")
    at = start()
    jump(at, q)
    assert not any(q["explanation"] in m.value for m in at.markdown)
    click(at, "Submit answer")
    assert len(at.warning) == 1 and not at.session_state["progress"]["submissions"]
    wrong = next(c["id"] for c in q["choices"] if c["id"] not in q["answer"])
    at.radio(key=f'single_{q["id"]}').set_value(wrong)
    click(at, "Submit answer")
    assert at.session_state["progress"]["submissions"][q["id"]] == [wrong]
    assert len(at.error) == 1
    assert any(q["explanation"] in m.value for m in at.markdown)
    for c in q["choices"]:
        assert any(c["explanation"] in m.value for m in at.markdown)
    click(at, "Next →")
    jump(at, q)
    assert at.radio(key=f'single_{q["id"]}').value == wrong
    assert at.radio(key=f'single_{q["id"]}').disabled
    assert next(b for b in at.button if b.label == "Submitted").disabled
    at.checkbox(key="confirm_reset").check().run()
    click(at, "Restart")
    assert not at.session_state["progress"]["submissions"]
    assert not at.session_state["progress"]["flags"]


def test_multiple_and_matching_forms_and_results():
    qs = load_bank()["questions"]
    at = start()
    multi = next(q for q in qs if q["type"] == "multiple")
    jump(at, multi)
    at.checkbox(key=f'multi_{multi["id"]}_{multi["answer"][0]}').check()
    click(at, "Submit answer")
    assert len(at.warning) == 1 and not at.session_state["progress"]["submissions"]
    for answer in multi["answer"]:
        at.checkbox(key=f'multi_{multi["id"]}_{answer}').check()
    click(at, "Submit answer")
    assert len(at.success) == 1
    matching = next(q for q in qs if q["type"] == "matching")
    jump(at, matching)
    click(at, "Submit answer")
    assert len(at.warning) == 1
    for pair in matching["pairs"]:
        at.selectbox(key=f'match_{matching["id"]}_{pair["id"]}').set_value(pair["answer"])
    click(at, "Submit answer")
    assert len(at.success) == 1
    click(at, "Flag for review")
    assert matching["id"] in at.session_state["progress"]["flags"]
    at.radio(key="view").set_value("Results & downloads").run()
    assert not at.exception
    rows = summarize(qs, at.session_state["progress"]["submissions"])
    assert sum(r["Correct"] for r in rows) == 2
    assert sum(r["Submitted"] for r in rows) == 2
    assert sum(r["Questions"] for r in rows) == 100


def test_domain_navigation_and_completed_set():
    qs = load_bank()["questions"]
    at = start()
    at.selectbox(key="domain").set_value(3).run()
    assert at.session_state["current"] == "CCNA1-041"
    assert len(at.selectbox(key="jump").options) == 25
    at.session_state["progress"]["submissions"] = {
        q["id"]: ({p["id"]: p["answer"] for p in q["pairs"]} if q["type"] == "matching" else q["answer"])
        for q in qs
    }
    at.radio(key="view").set_value("Results & downloads").run()
    assert not at.exception
    assert any("100/100" in s.value for s in at.success)
    assert next(b for b in at.button if b.label == "Go to first unanswered").disabled


def test_wrong_history_survives_new_session_restart_and_correct_retry(saved_browser):
    q = next(q for q in load_bank()["questions"] if q["type"] == "single")
    qid = q["id"]
    wrong = next(c["id"] for c in q["choices"] if c["id"] not in q["answer"])
    at = start()
    jump(at, q)
    at.radio(key=f"single_{qid}").set_value(wrong)
    click(at, "Submit answer")
    assert saved_browser["payload"]["wrong_answers"][qid]["last_response"] == [wrong]

    # New Python/WebSocket session restores the actual saved payload.
    at = start()
    assert at.session_state["progress"]["submissions"][qid] == [wrong]
    at.checkbox(key="confirm_reset").check().run()
    click(at, "Restart")
    assert not saved_browser["payload"]["submissions"]
    assert saved_browser["payload"]["wrong_answers"][qid]["wrong_count"] == 1
    at.radio(key="view").set_value("Wrong-answer review").run()
    assert not at.exception
    assert at.selectbox(key="review_question").value == qid
    at.radio(key=f"review_single_{qid}").set_value(q["answer"][0])
    click(at, "Submit answer")
    assert saved_browser["payload"]["wrong_answers"][qid]["reviewed_at"]
    assert saved_browser["payload"]["wrong_answers"][qid]["last_response"] == [wrong]
    assert not saved_browser["payload"]["submissions"]
    assert any("marked reviewed" in s.value for s in at.success)
    click(at, "Retry this question")
    assert at.radio(key=f"review_single_{qid}").value is None
    at.radio(key=f"review_single_{qid}").set_value(wrong)
    click(at, "Submit answer")
    assert saved_browser["payload"]["wrong_answers"][qid]["wrong_count"] == 2
    assert saved_browser["payload"]["wrong_answers"][qid]["reviewed_at"] is None
    at = start()
    assert at.session_state["progress"]["wrong_answers"][qid]["wrong_count"] == 2


def test_waits_for_load_and_preserves_invalid_browser_data(saved_browser):
    saved_browser["ready"] = False
    at = start()
    assert not at.radio
    assert saved_browser["writes"] == 0
    assert any("Loading your saved progress" in item.value for item in at.info)
    saved_browser["ready"] = True
    saved_browser["payload"] = {"schema_version": 99, "existing_history": "keep"}
    at.run()
    assert not at.exception
    assert saved_browser["writes"] == 0
    assert saved_browser["payload"]["existing_history"] == "keep"
    assert any("Automatic saving is paused" in item.value for item in at.warning)
    assert at.radio(key="view").value == "Practice"


def test_save_failure_is_not_reported_as_saved(monkeypatch):
    from progress_store import empty_progress
    def failing_save(payload, **kwargs):
        return {"status": "loaded", "payload": empty_progress(load_bank())} if payload is None else {"status": "error", "error": "Browser storage is full."}
    monkeypatch.setattr(browser_storage, "sync_storage", failing_save)
    at = start()
    assert any("Automatic saving is paused" in item.value for item in at.warning)
    assert not any("✓ Saved" in item.value for item in at.caption)
    assert any(button.label == "Back up my progress" for button in at.get("download_button"))


def test_switch_sets_keeps_scores_wrong_history_and_flags_separate(saved_browser):
    at = start()
    first = next(q for q in load_bank(1)["questions"] if q["type"] == "single")
    jump(at, first)
    wrong = next(c["id"] for c in first["choices"] if c["id"] not in first["answer"])
    at.radio(key=f'single_{first["id"]}').set_value(wrong)
    click(at, "Submit answer")
    click(at, "Flag for review")
    original = deepcopy(saved_browser["payload"])

    at.selectbox(key="set_number").set_value(2).run()
    assert not at.exception
    assert at.query_params["set"] == ["2"]
    assert at.session_state["progress"]["bank_id"].endswith("set-02")
    assert not at.session_state["progress"]["submissions"]
    assert not at.session_state["progress"]["wrong_answers"]
    assert not at.session_state["progress"]["flags"]
    second = next(q for q in load_bank(2)["questions"] if q["type"] == "single")
    jump(at, second)
    at.radio(key=f'single_{second["id"]}').set_value(second["answer"][0])
    click(at, "Submit answer")
    at.radio(key="view").set_value("Results & downloads").run()
    assert not at.exception
    assert sum(r["Correct"] for r in summarize(load_bank(2)["questions"], at.session_state["progress"]["submissions"])) == 1
    assert saved_browser["payload"] == original

    at.selectbox(key="set_number").set_value(10).run()
    assert not at.exception
    assert at.session_state["current"].startswith("CCNA10-")
    assert any("SET 10" in item.value for item in at.markdown)
    at.radio(key="view").set_value("Results & downloads").run()
    assert not at.exception
    at.selectbox(key="set_number").set_value(1).run()
    assert not at.exception
    assert at.session_state["progress"] == original
    at.radio(key="view").set_value("Wrong-answer review").run()
    assert at.selectbox(key="review_question").value == first["id"]

    at.selectbox(key="set_number").set_value(2).run()
    assert at.session_state["progress"]["submissions"] == {second["id"]: second["answer"]}


def test_set_link_loads_the_requested_set_and_invalid_links_fall_back():
    at = AppTest.from_file(ROOT / "app.py", default_timeout=20)
    at.query_params["set"] = "10"
    at.run()
    assert not at.exception
    assert at.selectbox(key="set_number").value == 10
    assert at.session_state["current"] == "CCNA10-001"
    at = AppTest.from_file(ROOT / "app.py", default_timeout=20)
    at.query_params["set"] = "invalid"
    at.run()
    assert not at.exception
    assert at.selectbox(key="set_number").value == 1


def test_set_switch_waits_for_save_acknowledgement(monkeypatch):
    def pending(payload, **kwargs):
        if payload is None:
            return {"status": "loaded", "payload": None}
        return {"status": "saved", "request_id": "older-payload"}
    monkeypatch.setattr(browser_storage, "sync_storage", pending)
    at = start()
    assert at.selectbox(key="set_number").disabled
    assert any("Saving progress" in item.value for item in at.caption)


def right_answer(q):
    return {p["id"]: p["answer"] for p in q["pairs"]} if q["type"] == "matching" else q["answer"]


def test_last_submission_opens_results_with_named_subsection_and_final_explanation():
    qs = load_bank()["questions"]
    final = next(q for q in qs if q["type"] == "single" and q["domain"] == 3)
    at = start()
    at.session_state["progress"]["submissions"] = {q["id"]: right_answer(q) for q in qs if q["id"] != final["id"]}
    jump(at, final)
    wrong = next(c["id"] for c in final["choices"] if c["id"] not in final["answer"])
    at.radio(key=f'single_{final["id"]}').set_value(wrong)
    click(at, "Submit answer")
    assert at.radio(key="view").value == "Results & downloads"
    assert any("99/100" in item.value for item in at.success)
    assert any(final["explanation"] in item.value for item in at.markdown)
    table = next(frame.value for frame in at.dataframe if "Area" in frame.value.columns and any(str(v).startswith("3.") for v in frame.value["Area"]))
    assert any(" · " in label for label in table["Area"])
    assert at.selectbox(key="set_results_evidence_question").value == final["id"]


def test_overall_results_include_unopened_sets_without_double_counting_active_set(saved_browser):
    from progress_store import empty_progress, record_answer
    b2 = load_bank(2)
    p2 = empty_progress(b2)
    q2 = next(q for q in b2["questions"] if q["type"] == "single")
    wrong = next(c["id"] for c in q2["choices"] if c["id"] not in q2["answer"])
    record_answer(p2, q2, [wrong])
    saved_browser["sets"][b2["metadata"]["set_id"]] = p2
    at = start()
    q1 = next(q for q in load_bank()["questions"] if q["type"] == "single")
    jump(at, q1)
    at.radio(key=f'single_{q1["id"]}').set_value(q1["answer"][0])
    click(at, "Submit answer")
    at.radio(key="view").set_value("Overall results").run()
    assert not at.exception
    metrics = {m.label: m.value for m in at.metric}
    assert metrics["Submitted overall"] == "2 / 1,000"
    assert metrics["Accuracy overall"] == "50.0%"
    assert metrics["Pending review"] == "1"
    assert at.selectbox(key="overall_results_evidence_question").value == q2["id"]
    click(at, "Open question and explanation")
    assert at.selectbox(key="set_number").value == 2
    assert at.radio(key="view").value == "Practice"
    assert any(q2["explanation"] in item.value for item in at.markdown)
    assert saved_browser["payload"]["submissions"] == {q1["id"]: q1["answer"]}


def test_overall_excludes_corrupt_other_set_and_refreshes_new_saved_work(saved_browser):
    from progress_store import empty_progress, record_answer
    b2 = load_bank(2)
    bid = b2["metadata"]["set_id"]
    saved_browser["sets"][bid] = {"schema_version": 99}
    at = start()
    at.radio(key="view").set_value("Overall results").run()
    assert not at.exception
    assert any("report may be incomplete" in item.value for item in at.warning)
    assert any("9 of 10 sets" in item.value for item in at.markdown)
    assert saved_browser["sets"][bid] == {"schema_version": 99}
    p2 = empty_progress(b2)
    q = b2["questions"][0]
    record_answer(p2, q, right_answer(q))
    saved_browser["sets"][bid] = p2
    old_token = at.session_state["overall_refresh"]
    click(at, "Refresh overall results")
    assert at.session_state["overall_refresh"] != old_token
    assert {m.label: m.value for m in at.metric}["Submitted overall"] == "1 / 1,000"
    assert not at.warning


def test_results_keep_restart_history_actionable_and_correct_review_does_not_rescore():
    q = next(q for q in load_bank()["questions"] if q["type"] == "single")
    at = start()
    jump(at, q)
    wrong = next(c["id"] for c in q["choices"] if c["id"] not in q["answer"])
    at.radio(key=f'single_{q["id"]}').set_value(wrong)
    click(at, "Submit answer")
    at.checkbox(key="confirm_reset").check().run()
    click(at, "Restart")
    at.radio(key="view").set_value("Results & downloads").run()
    assert not at.exception
    assert any("Review from history" in frame.value.to_string() for frame in at.dataframe)
    click(at, "Open question and explanation")
    assert at.radio(key="view").value == "Wrong-answer review"
    assert any(q["explanation"] in item.value for item in at.markdown)
    click(at, "Retry this question")
    at.radio(key=f'review_single_{q["id"]}').set_value(q["answer"][0])
    click(at, "Submit answer")
    at.radio(key="view").set_value("Overall results").run()
    assert not at.exception
    metrics = {m.label: m.value for m in at.metric}
    assert metrics["Submitted overall"] == "0 / 1,000"
    assert metrics["Pending review"] == "0"


def test_overall_waits_for_read_and_includes_unsaved_current_work(monkeypatch):
    monkeypatch.setattr(collection_storage, "read_collection_progress", lambda token: {})
    at = start()
    at.radio(key="view").set_value("Overall results").run()
    assert not at.exception
    assert any("Reading saved results" in item.value for item in at.info)
    assert not at.metric
    monkeypatch.setattr(collection_storage, "read_collection_progress", lambda token: {
        "status": "loaded", "records": {bid: None for bid in collection_storage.BANK_IDS}, "errors": {}})
    monkeypatch.setattr(browser_storage, "sync_storage", lambda payload, **kw: {"status": "error", "error": "Storage is full."})
    q = load_bank()["questions"][0]
    at.session_state["progress"]["submissions"] = {q["id"]: right_answer(q)}
    at.run()
    assert not at.exception
    assert {m.label: m.value for m in at.metric}["Submitted overall"] == "1 / 1,000"
    assert any("current session's work" in item.value for item in at.caption)
