"""Tests for the durable data contract, independent of a browser or server."""
from copy import deepcopy
from datetime import datetime, timezone
import json

import pytest

from progress_store import empty_progress, record_answer, restart_attempt, restore_progress
from quiz_core import load_bank


BANK = load_bank()
SINGLE = next(q for q in BANK["questions"] if q["type"] == "single")
MATCHING = next(q for q in BANK["questions"] if q["type"] == "matching")
T1 = "2026-09-14T12:00:00+00:00"
T2 = "2026-09-15T12:00:00+00:00"
T3 = "2026-09-16T12:00:00+00:00"


def wrong_answer(question=SINGLE):
    if question["type"] == "matching":
        response = {pair["id"]: pair["answer"] for pair in question["pairs"]}
        first = question["pairs"][0]
        response[first["id"]] = next(c["id"] for c in question["choices"] if c["id"] != first["answer"])
        return response
    return [next(c["id"] for c in question["choices"] if c["id"] not in question["answer"])]


def saved_mistake():
    progress = empty_progress(BANK)
    record_answer(progress, SINGLE, wrong_answer(), now=T1)
    return progress


def test_fresh_restore_and_round_trip_are_independent():
    progress = restore_progress(None, BANK)
    assert progress == empty_progress(BANK)
    assert restore_progress(json.dumps(progress), BANK) == progress
    progress["flags"].append(SINGLE["id"])
    assert not empty_progress(BANK)["flags"]


def test_restart_and_json_restore_preserve_wrong_response_and_count():
    progress = saved_mistake()
    progress["flags"].append(SINGLE["id"])
    record_answer(progress, SINGLE, wrong_answer(), review=True, now=T2)
    restart_attempt(progress)
    restored = restore_progress(json.dumps(progress), BANK)
    assert restored["submissions"] == {}
    assert restored["flags"] == []
    assert restored["wrong_answers"][SINGLE["id"]] == {
        "last_response": wrong_answer(), "wrong_count": 2,
        "last_wrong_at": T2, "reviewed_at": None,
    }


def test_correct_review_resolves_then_later_mistake_reopens_without_changing_score():
    progress = saved_mistake()
    original = deepcopy(progress["submissions"])
    record_answer(progress, SINGLE, SINGLE["answer"], review=True, now=T2)
    mistake = progress["wrong_answers"][SINGLE["id"]]
    assert mistake["reviewed_at"] == T2
    assert mistake["last_response"] == wrong_answer()
    assert mistake["wrong_count"] == 1
    assert progress["submissions"] == original
    record_answer(progress, SINGLE, wrong_answer(), review=True, now=T3)
    assert progress["wrong_answers"][SINGLE["id"]]["reviewed_at"] is None
    assert progress["wrong_answers"][SINGLE["id"]]["wrong_count"] == 2
    assert progress["submissions"] == original


def test_review_cannot_add_score_and_normal_submission_keeps_first_answer():
    progress = empty_progress(BANK)
    record_answer(progress, SINGLE, wrong_answer(), review=True, now=T1)
    assert progress["submissions"] == {}
    record_answer(progress, SINGLE, SINGLE["answer"], now=T2)
    assert progress["wrong_answers"][SINGLE["id"]]["reviewed_at"] == T2
    record_answer(progress, SINGLE, wrong_answer(), now=T3)
    assert progress["submissions"][SINGLE["id"]] == SINGLE["answer"]


def test_response_and_restored_data_never_alias_caller_objects():
    response = wrong_answer(MATCHING)
    progress = empty_progress(BANK)
    record_answer(progress, MATCHING, response, now=T1)
    response.clear()
    qid = MATCHING["id"]
    assert progress["submissions"][qid] == wrong_answer(MATCHING)
    progress["submissions"][qid].clear()
    assert progress["wrong_answers"][qid]["last_response"] == wrong_answer(MATCHING)
    progress["submissions"][qid] = wrong_answer(MATCHING)
    restored = restore_progress(progress, BANK)
    progress["wrong_answers"][qid]["last_response"].clear()
    assert restored["wrong_answers"][qid]["last_response"] == wrong_answer(MATCHING)


@pytest.mark.parametrize("mutate", [
    lambda p: p.update(schema_version=2),
    lambda p: p.update(schema_version=True),
    lambda p: p.update(bank_id="another-set"),
    lambda p: p.update(unrecognized="must not be discarded"),
    lambda p: p.pop("flags"),
    lambda p: p.update(flags=[SINGLE["id"], SINGLE["id"]]),
    lambda p: p.update(flags=[[]]),
    lambda p: p.update(flags=["CCNA1-999"]),
    lambda p: p.update(submissions=[]),
    lambda p: p["submissions"].update({"CCNA1-999": ["A"]}),
    lambda p: p["submissions"].update({SINGLE["id"]: [[]]}),
    lambda p: p["submissions"].update({SINGLE["id"]: ["missing-choice"]}),
    lambda p: p.update(wrong_answers=[]),
    lambda p: p.update(wrong_answers={}),
    lambda p: p["wrong_answers"].update({"CCNA1-999": {}}),
    lambda p: p["wrong_answers"][SINGLE["id"]].update(wrong_count=0),
    lambda p: p["wrong_answers"][SINGLE["id"]].update(wrong_count=True),
    lambda p: p["wrong_answers"][SINGLE["id"]].update(wrong_count=1.5),
    lambda p: p["wrong_answers"][SINGLE["id"]].update(last_response=SINGLE["answer"]),
    lambda p: p["wrong_answers"][SINGLE["id"]].update(last_wrong_at="2026-09-14"),
    lambda p: p["wrong_answers"][SINGLE["id"]].update(last_wrong_at=123),
    lambda p: p["wrong_answers"][SINGLE["id"]].update(reviewed_at="not-a-time"),
    lambda p: p["wrong_answers"][SINGLE["id"]].update(extra="unknown"),
])
def test_restore_rejects_malformed_or_unsupported_data_without_mutating_it(mutate):
    raw = saved_mistake()
    mutate(raw)
    before = deepcopy(raw)
    with pytest.raises(ValueError):
        restore_progress(raw, BANK)
    assert raw == before


@pytest.mark.parametrize("raw", ["{", "null", "[]", [], 1, True])
def test_restore_rejects_non_records(raw):
    with pytest.raises(ValueError):
        restore_progress(raw, BANK)


def test_invalid_new_response_or_naive_timestamp_is_atomic():
    progress = saved_mistake()
    before = deepcopy(progress)
    for response, timestamp in [([], T2), ([[]], T2), (wrong_answer(), datetime(2026, 9, 14))]:
        with pytest.raises(ValueError):
            record_answer(progress, SINGLE, response, now=timestamp)
        assert progress == before


def test_aware_timestamp_normalizes_to_utc_and_default_is_aware():
    progress = empty_progress(BANK)
    record_answer(progress, SINGLE, wrong_answer(), now="2026-09-14T20:00:00+08:00")
    assert progress["wrong_answers"][SINGLE["id"]]["last_wrong_at"] == T1
    raw = saved_mistake()
    raw["wrong_answers"][SINGLE["id"]]["last_wrong_at"] = "2026-09-14T12:00:00Z"
    assert restore_progress(raw, BANK)["wrong_answers"][SINGLE["id"]]["last_wrong_at"] == T1
    record_answer(progress, SINGLE, wrong_answer())
    timestamp = datetime.fromisoformat(progress["wrong_answers"][SINGLE["id"]]["last_wrong_at"])
    assert timestamp.tzinfo == timezone.utc


def test_missing_mistake_history_rejects_partial_import_without_fabricating_timestamps():
    raw = saved_mistake()
    raw["wrong_answers"] = {}
    before = deepcopy(raw)
    with pytest.raises(ValueError, match="missing its mistake history"):
        restore_progress(json.dumps(raw), BANK)
    assert raw == before


def test_real_v1_export_states_remain_compatible_including_reviewed_first_errors():
    progress = saved_mistake()
    assert restore_progress(json.dumps(progress), BANK) == progress
    record_answer(progress, SINGLE, SINGLE["answer"], review=True, now=T2)
    assert progress["submissions"][SINGLE["id"]] == wrong_answer()
    assert progress["wrong_answers"][SINGLE["id"]]["reviewed_at"] == T2
    assert restore_progress(json.dumps(progress), BANK) == progress
    restart_attempt(progress)
    assert restore_progress(json.dumps(progress), BANK) == progress
    record_answer(progress, SINGLE, SINGLE["answer"], now=T3)
    assert restore_progress(json.dumps(progress), BANK) == progress


def test_correct_first_answer_without_mistake_history_is_valid():
    progress = empty_progress(BANK)
    record_answer(progress, SINGLE, SINGLE["answer"], now=T1)
    assert not progress["wrong_answers"]
    assert restore_progress(json.dumps(progress), BANK) == progress
