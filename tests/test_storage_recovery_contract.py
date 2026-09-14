"""The Python boundary validates candidates before issuing browser operations."""
from copy import deepcopy
import json

import pytest

import browser_storage
from progress_store import empty_progress, record_answer
from quiz_core import load_bank


TOKEN = "a" * 32
BASELINE = "opaque-browser-observation"
BANK = load_bank()


@pytest.fixture
def bridge(monkeypatch):
    calls = []
    monkeypatch.setattr(browser_storage.st, "session_state", {})

    def component(**kwargs):
        calls.append(kwargs)
        return {"event": {"status": "saved", "request_id": kwargs["data"]["request_id"],
                          "baseline_id": "new-observation"}}

    monkeypatch.setattr(browser_storage, "_component", component)
    return calls


def test_replacement_has_unique_content_specific_ack_and_preserves_candidate(bridge):
    candidate = empty_progress(BANK)
    original = deepcopy(candidate)
    event = browser_storage.sync_storage(candidate, replacement_id=TOKEN, expected_baseline=BASELINE)
    request = bridge[0]["data"]
    assert request["operation"] == "replace"
    assert request["replacement_id"] == TOKEN
    assert request["expected_baseline"] == BASELINE
    assert json.loads(request["serialized"]) == candidate == original
    assert event["request_id"] == browser_storage.storage_request_id(candidate, replacement_id=TOKEN)
    assert event["request_id"] != browser_storage.storage_request_id(candidate)
    assert event["request_id"] != browser_storage.storage_request_id(candidate, replacement_id="b" * 32)
    assert browser_storage.storage_request_id(dict(reversed(list(candidate.items()))), replacement_id=TOKEN) == event["request_id"]


@pytest.mark.parametrize("mutate", [
    lambda p: p.update(bank_id="ccna-200-301-v1.1-set-02"),
    lambda p: p.update(schema_version=2),
    lambda p: p.update(submissions=[]),
    lambda p: p.pop("wrong_answers"),
    lambda p: p.update(flags=["unknown"]),
])
def test_invalid_replacement_never_reaches_browser(bridge, mutate):
    candidate = empty_progress(BANK)
    mutate(candidate)
    original = deepcopy(candidate)
    with pytest.raises(ValueError):
        browser_storage.sync_storage(candidate, replacement_id=TOKEN, expected_baseline=BASELINE)
    assert bridge == []
    assert candidate == original


def test_inconsistent_incorrect_submission_never_reaches_browser(bridge):
    candidate = empty_progress(BANK)
    question = next(q for q in BANK["questions"] if q["type"] == "single")
    answer = [next(c["id"] for c in question["choices"] if c["id"] not in question["answer"])]
    record_answer(candidate, question, answer)
    candidate["wrong_answers"] = {}
    with pytest.raises(ValueError, match="missing its mistake history"):
        browser_storage.sync_storage(candidate, replacement_id=TOKEN, expected_baseline=BASELINE)
    assert bridge == []


@pytest.mark.parametrize("payload,kwargs", [
    (None, {"replacement_id": TOKEN, "expected_baseline": BASELINE}),
    ({}, {"replacement_id": TOKEN, "expected_baseline": BASELINE}),
    (empty_progress(BANK), {"replacement_id": TOKEN}),
    (empty_progress(BANK), {"replacement_id": "reused human label", "expected_baseline": BASELINE}),
    (empty_progress(BANK), {"expected_baseline": BASELINE}),
])
def test_replacement_requires_complete_explicit_contract(bridge, payload, kwargs):
    with pytest.raises(ValueError):
        browser_storage.sync_storage(payload, **kwargs)
    assert bridge == []


@pytest.mark.parametrize("number", range(1, 11))
def test_replacements_remain_isolated_to_the_destination_bank(bridge, number):
    candidate = empty_progress(load_bank(number))
    bank_id = candidate["bank_id"]
    browser_storage.sync_storage(candidate, bank_id=bank_id, replacement_id=TOKEN,
                                 expected_baseline=BASELINE)
    assert bridge[0]["data"]["storage_key"] == browser_storage.storage_key(bank_id)


def test_normal_load_and_save_contracts_remain_compatible(bridge):
    browser_storage.sync_storage(None)
    candidate = empty_progress(BANK)
    browser_storage.sync_storage(candidate)
    assert bridge[0]["data"]["operation"] == "load"
    assert bridge[0]["data"]["request_id"] == "load"
    assert bridge[1]["data"]["operation"] == "save"
    assert bridge[1]["data"]["request_id"] == browser_storage.storage_request_id(candidate)
    assert "replacement_id" not in bridge[1]["data"]
