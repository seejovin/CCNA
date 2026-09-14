"""Regressions for delayed browser events that synchronous AppTest misses.

The actual Python storage bridge runs here; only its JavaScript component
callback is modeled. Each load/save must cross a separate AppTest run before
its acknowledgment becomes available. JavaScript storage/conflict behavior is
covered separately by test_browser_storage.mjs.
"""

from copy import deepcopy
import json
from pathlib import Path

import pytest
from streamlit.testing.v1 import AppTest

import browser_storage
from progress_store import empty_progress, record_answer
from quiz_core import load_bank


ROOT = Path(__file__).resolve().parents[1]


class DeferredFrontend:
    def __init__(self):
        self.records = {}
        self.commands = {}
        self.pending = {}
        self.events = {}
        self.writes = []

    def component(self, *, data, **kwargs):
        identity = (data["session_id"], data["storage_key"])
        command = (data["operation"], data["request_id"])
        if self.commands.get(identity) != command:
            self.commands[identity] = command
            self.pending[identity] = deepcopy(data)
        return {"event": deepcopy(self.events.get(identity))}

    def deliver(self):
        pending, self.pending = self.pending, {}
        for identity, request in pending.items():
            key = request["storage_key"]
            event = {"request_id": request["request_id"], "baseline_id": f"baseline:{key}"}
            if request["operation"] == "load":
                event.update(status="loaded", payload=deepcopy(self.records.get(key)))
            else:
                assert request["operation"] == "save", "Replacement has separate recovery tests."
                payload = json.loads(request["serialized"])
                expected = f"ccna-200-301-v1.1-set-{key.split(':')[3][4:]}"
                assert payload["bank_id"] == expected, "Cross-set write attempted."
                self.records[key] = payload
                self.writes.append((key, deepcopy(payload)))
                event["status"] = "saved"
            self.events[identity] = event

    def settle(self, at):
        for _ in range(12):
            if not self.pending:
                return
            self.deliver()
            run(at)
        raise AssertionError("Storage did not settle within 12 event deliveries.")


@pytest.fixture
def frontend(monkeypatch):
    bridge = DeferredFrontend()
    monkeypatch.setattr(browser_storage, "_component", bridge.component)
    return bridge


def run(at):
    at.run()
    assert not at.exception, [(e.message, e.stack_trace) for e in at.exception]
    return at


def start(number):
    at = AppTest.from_file(ROOT / "app.py", default_timeout=30)
    at.query_params["set"] = str(number)
    return run(at)


def click(at, label):
    button = next(b for b in at.button if b.label == label)
    assert not button.disabled
    button.click()
    return run(at)


def correct_response(q):
    return {p["id"]: p["answer"] for p in q["pairs"]} if q["type"] == "matching" else deepcopy(q["answer"])


def wrong_response(q):
    response = correct_response(q)
    if q["type"] == "matching":
        first = next(iter(response))
        response[first] = next(c["id"] for c in q["choices"] if c["id"] != response[first])
    else:
        response[0] = next(c["id"] for c in q["choices"] if c["id"] not in response)
        response = [c["id"] for c in q["choices"] if c["id"] in response]
    return response


def fill(at, q, response, *, review=False):
    prefix = "review_" if review else ""
    if q["type"] == "single":
        at.radio(key=f'{prefix}single_{q["id"]}').set_value(response[0])
    elif q["type"] == "multiple":
        for c in q["choices"]:
            at.checkbox(key=f'{prefix}multi_{q["id"]}_{c["id"]}').set_value(c["id"] in response)
    else:
        for p in q["pairs"]:
            at.selectbox(key=f'{prefix}match_{q["id"]}_{p["id"]}').set_value(response[p["id"]])


def visible_label(widget):
    # widget.value reads Python session state and can conceal F-01. Inspect
    # the instruction actually sent to the frontend for the visible selection.
    proto = widget.proto
    return proto.raw_value if proto.set_value else proto.options[proto.default]


def assert_set(at, number):
    assert at.session_state["progress"]["bank_id"] == f"ccna-200-301-v1.1-set-{number:02d}"
    assert at.session_state["current"].startswith(f"CCNA{number}-")
    assert visible_label(at.selectbox(key="set_number")) == f"Set {number:02d} · 100 questions"
    assert any(f"SET {number:02d}" in m.value for m in at.markdown)


def inject_wire_label(at, key, label):
    states = at._tree.get_widget_states()
    widget_id = at.selectbox(key=key).proto.id
    state = next(s for s in states.widgets if s.id == widget_id)
    state.string_value = label
    at._run(states)
    assert not at.exception, [(e.message, e.stack_trace) for e in at.exception]


@pytest.mark.parametrize("number", range(1, 11))
def test_direct_set_url_after_deferred_load_has_matching_visible_selector(frontend, number):
    at = start(number)
    assert not at.selectbox
    assert not frontend.writes
    # First delivery loads data; the second is the distinct durable-save ack.
    frontend.deliver()
    run(at)
    assert_set(at, number)
    assert at.selectbox(key="set_number").disabled
    frontend.settle(at)
    assert not at.selectbox(key="set_number").disabled
    inject_wire_label(at, "set_number", visible_label(at.selectbox(key="set_number")))
    click(at, "Next →")
    assert_set(at, number)
    q = next(q for q in load_bank(number)["questions"] if q["id"] == at.session_state["current"])
    fill(at, q, correct_response(q))
    click(at, "Submit answer")
    assert at.selectbox(key="set_number").disabled
    frontend.settle(at)
    assert_set(at, number)
    assert any(q["explanation"] in m.value for m in at.markdown)
    key = browser_storage.storage_key(f"ccna-200-301-v1.1-set-{number:02d}")
    assert frontend.records[key]["submissions"][q["id"]] == correct_response(q)


TRANSITIONS = [(origin, destination) for origin in range(1, 11) for destination in range(1, 11) if origin != destination]


@pytest.mark.parametrize("origin,destination", TRANSITIONS)
def test_all_directed_set_switches_with_deferred_loads_and_saves(frontend, origin, destination):
    for number in range(1, 11):
        bank = load_bank(number)
        p = empty_progress(bank)
        q = bank["questions"][0]
        record_answer(p, q, wrong_response(q))
        p["flags"] = [q["id"]]
        frontend.records[browser_storage.storage_key(p["bank_id"])] = p
    before = deepcopy(frontend.records)
    at = start(origin)
    frontend.settle(at)
    assert_set(at, origin)
    at.selectbox(key="set_number").set_value(destination)
    run(at)
    assert not at.selectbox  # Destination has no load acknowledgment yet.
    frontend.deliver()
    run(at)
    assert_set(at, destination)
    frontend.settle(at)
    click(at, "Next →")
    q = next(q for q in load_bank(destination)["questions"] if q["id"] == at.session_state["current"])
    fill(at, q, correct_response(q))
    click(at, "Submit answer")
    assert at.selectbox(key="set_number").disabled
    frontend.settle(at)
    assert_set(at, destination)
    destination_key = browser_storage.storage_key(f"ccna-200-301-v1.1-set-{destination:02d}")
    for key, record in before.items():
        if key != destination_key:
            assert frontend.records[key] == record
    assert frontend.records[destination_key]["submissions"][q["id"]] == correct_response(q)
    assert frontend.records[destination_key]["wrong_answers"] == before[destination_key]["wrong_answers"]
    assert frontend.records[destination_key]["flags"] == before[destination_key]["flags"]


@pytest.mark.parametrize("number,index,correct,filtered", [(1, 73, True, False), (1, 1, False, False), (2, 1, True, False), (10, 73, False, True)])
def test_submission_and_flags_keep_question_after_stale_selector_events(frontend, number, index, correct, filtered):
    q = load_bank(number)["questions"][index]
    at = start(number)
    frontend.settle(at)
    if filtered:
        at.selectbox(key="domain").set_value(q["domain"])
        run(at)
    at.selectbox(key="jump").set_value(q["id"])
    run(at)
    stable = visible_label(at.selectbox(key="jump"))
    response = correct_response(q) if correct else wrong_response(q)
    fill(at, q, response)
    click(at, "Submit answer")
    # Repeat the actual pre-submit label while the acknowledgment is pending.
    inject_wire_label(at, "jump", stable)
    frontend.settle(at)
    assert at.session_state["current"] == q["id"]
    assert visible_label(at.selectbox(key="jump")) == stable
    assert any(q["explanation"] in m.value for m in at.markdown)
    click(at, "Flag for review")
    frontend.settle(at)
    assert visible_label(at.selectbox(key="jump")) == stable
    # Also ignore legacy labels or malformed values from an older render.
    for old in [f"{stable} · Review", f"{stable} · Correct · Flagged", "obsolete question"]:
        inject_wire_label(at, "jump", old)
        frontend.settle(at)
        assert at.session_state["current"] == q["id"]
        assert visible_label(at.selectbox(key="jump")) == stable
        assert any(q["explanation"] in m.value for m in at.markdown)
    assert at.session_state["progress"]["submissions"][q["id"]] == response
    assert q["id"] in at.session_state["progress"]["flags"]


@pytest.mark.parametrize("number", range(1, 11))
def test_review_retains_question_after_stale_labels_and_reports_pending_count(frontend, number):
    bank = load_bank(number)
    qs = [q for q in bank["questions"] if q["type"] == "single"][:2]
    p = empty_progress(bank)
    for q in qs:
        record_answer(p, q, wrong_response(q))
    # One older error has already been reviewed. The new retry clears the last.
    record_answer(p, qs[0], correct_response(qs[0]), review=True)
    frontend.records[browser_storage.storage_key(p["bank_id"])] = p
    at = start(number)
    frontend.settle(at)
    at.radio(key="view").set_value("Wrong-answer review")
    run(at)
    q = qs[1]
    at.selectbox(key="review_question").set_value(q["id"])
    run(at)
    stable = visible_label(at.selectbox(key="review_question"))
    fill(at, q, correct_response(q), review=True)
    click(at, "Submit answer")
    for old in [stable, f"{stable} · To review · Missed 1 time(s)", "obsolete review question"]:
        inject_wire_label(at, "review_question", old)
        frontend.settle(at)
        assert at.selectbox(key="review_question").value == q["id"]
        assert visible_label(at.selectbox(key="review_question")) == stable
        assert any(q["explanation"] in m.value for m in at.markdown)
    assert {m.label: m.value for m in at.metric}["Still to review"] == "0"
    assert at.session_state["progress"]["submissions"] == p["submissions"]
    assert all(entry["reviewed_at"] for entry in at.session_state["progress"]["wrong_answers"].values())
    assert any(c.value == "Pending review: 0" for c in at.caption)
    assert any("Reviewed" in c.value for c in at.caption)
    assert not any("2 to review" in c.value for c in at.caption)
    assert not any(" · Review" in label for label in at.selectbox(key="jump").options)
    at.radio(key="view").set_value("Results & downloads")
    run(at)
    labels = [e.label for e in at.expander]
    assert "Questions to review · 2" not in labels
    assert any("Incorrect first" in label and "2" in label for label in labels)
