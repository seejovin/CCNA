"""Restore integration through the real Python bridge and delayed browser events.

Only the JS callback and uploaded-file object are modeled. Tests submit the
actual restore form; no pending-restore/session candidate is injected.
Browser raw-value comparison and event delivery are distinct operations here.
The actual JS implementation has its own concurrency/readback tests.
"""
from copy import deepcopy
import json
from pathlib import Path

import pytest
import streamlit as st
from streamlit.testing.v1 import AppTest

import browser_storage
from progress_store import empty_progress, record_answer, restore_progress
from quiz_core import load_bank


ROOT = Path(__file__).resolve().parents[1]


class Upload:
    def __init__(self, payload):
        self.body = payload if isinstance(payload, bytes) else json.dumps(payload).encode()
        self.size = len(self.body)

    def getvalue(self):
        return self.body


class RestoreFrontend:
    def __init__(self):
        self.raw = {}
        self.commands = {}
        self.pending = {}
        self.events = {}
        self.states = {}
        self.writes = []
        self.executed = []
        self.sequence = 0

    def component(self, *, data, **kwargs):
        identity = (data["session_id"], data["storage_key"])
        command = (data["operation"], data["request_id"])
        if self.commands.get(identity) != command:
            self.commands[identity] = command
            self.pending[identity] = deepcopy(data)
        return {"event": deepcopy(self.events.get(identity))}

    def baseline(self, state, raw):
        self.sequence += 1
        state.update(raw=raw, baseline_id=f"observation-{self.sequence}")

    def execute(self, identity, request):
        key = request["storage_key"]
        state = self.states.setdefault(identity, {"ready": False, "tokens": set()})
        event = {"request_id": request["request_id"]}
        if request["operation"] == "load":
            raw = self.raw.get(key)
            self.baseline(state, raw)
            event["baseline_id"] = state["baseline_id"]
            try:
                payload = None if raw is None else json.loads(raw)
                if raw is not None and not isinstance(payload, dict):
                    raise ValueError
            except ValueError:
                state["ready"] = False
                return dict(event, status="error", code="corrupt", error="Saved browser data could not be read.")
            state["ready"] = True
            return dict(event, status="loaded", payload=payload)
        event["baseline_id"] = state.get("baseline_id")
        replacing = request["operation"] == "replace"
        if replacing:
            token = request["replacement_id"]
            if token in state["tokens"]:
                return dict(event, status="error", code="replayed", error="Replacement already attempted.")
            state["tokens"].add(token)
            if request["expected_baseline"] != state.get("baseline_id"):
                return dict(event, status="error", code="stale_replacement", error="Replacement baseline changed.")
        elif not state["ready"]:
            return dict(event, status="error", code="uninitialized", error="A read is required.")
        current = self.raw.get(key)
        serialized = request["serialized"]
        if current != state.get("raw") and (replacing or current != serialized):
            return dict(event, status="error", code="conflict", error="Another tab changed saved progress.")
        payload = json.loads(serialized)
        assert payload["bank_id"] == f"ccna-200-301-v1.1-set-{key.split(':')[3][4:]}"
        if current != serialized:
            self.raw[key] = serialized
            self.writes.append((key, deepcopy(payload)))
        self.baseline(state, serialized)
        state["ready"] = True
        return dict(event, status="saved", baseline_id=state["baseline_id"])

    def deliver(self):
        pending, self.pending = self.pending, {}
        for identity, request in pending.items():
            self.executed.append(deepcopy(request))
            self.events[identity] = self.execute(identity, request)

    def replacement(self):
        matches = [(i, r) for i, r in self.pending.items() if r["operation"] == "replace"]
        assert len(matches) == 1
        return matches[0]

    def publish_wrong_ack(self, request_id):
        identity, _ = self.replacement()
        self.events[identity] = {"status": "saved", "request_id": request_id,
                                 "baseline_id": "unrelated-observation"}

    def fail_replacement(self, code="quota", changed_raw=None):
        identity, request = self.replacement()
        state = self.states[identity]
        state["tokens"].add(request["replacement_id"])
        self.pending.pop(identity)
        if changed_raw is not None:
            self.raw[request["storage_key"]] = changed_raw
        self.events[identity] = {"status": "error", "request_id": request["request_id"],
                                 "baseline_id": state["baseline_id"], "code": code,
                                 "error": "Another tab changed saved progress." if code == "conflict" else "Storage is full."}

    def settle(self, at):
        for _ in range(10):
            if not self.pending:
                return
            self.deliver()
            run(at)
        raise AssertionError("Storage failed to settle.")


@pytest.fixture
def frontend(monkeypatch):
    model = RestoreFrontend()
    monkeypatch.setattr(browser_storage, "_component", model.component)
    return model


def run(at):
    at.run()
    assert not at.exception, [(e.message, e.stack_trace) for e in at.exception]
    return at


def click(at, label):
    button = next(b for b in at.button if b.label == label)
    assert not button.disabled
    button.click()
    return run(at)


def start(frontend, number=1, raw="{broken"):
    key = browser_storage.storage_key(f"ccna-200-301-v1.1-set-{number:02d}")
    if raw is not None:
        frontend.raw[key] = raw
    at = AppTest.from_file(ROOT / "app.py", default_timeout=30)
    at.query_params["set"] = str(number)
    run(at)
    frontend.settle(at)
    return at, key


def backup(number):
    bank = load_bank(number)
    p = empty_progress(bank)
    q = next(q for q in bank["questions"] if q["type"] == "single")
    wrong = [next(c["id"] for c in q["choices"] if c["id"] not in q["answer"])]
    record_answer(p, q, wrong, now="2026-09-14T12:00:00+00:00")
    record_answer(p, q, q["answer"], review=True, now="2026-09-15T12:00:00+00:00")
    p["flags"] = [q["id"]]
    return p


def submit_import(at, monkeypatch, candidate, *, confirmed=True):
    monkeypatch.setattr(st, "file_uploader", lambda *args, **kwargs: Upload(candidate))
    at.radio(key="view").set_value("Results & downloads")
    run(at)
    next(c for c in at.checkbox if c.label == "Replace my current progress with this backup").set_value(confirmed)
    return click(at, "Restore backup")


@pytest.mark.parametrize("number", range(1, 11))
def test_corrupt_storage_restore_commits_only_exact_ack_then_normal_saves(frontend, monkeypatch, number):
    at, key = start(frontend, number)
    original = deepcopy(at.session_state["progress"])
    candidate = backup(number)
    other_key = browser_storage.storage_key(f"ccna-200-301-v1.1-set-{number % 10 + 1:02d}")
    frontend.raw[other_key] = "other-set-do-not-touch"
    observed = at.session_state["storage_baseline_id"]
    assert "save_disabled" in at.session_state
    assert not frontend.writes
    submit_import(at, monkeypatch, candidate)
    staged = at.session_state["pending_restore"]
    assert staged["progress"] == candidate
    assert staged["expected_baseline"] == observed
    assert at.session_state["progress"] == original
    assert frontend.raw[key] == "{broken"
    assert not any("restored and saved" in x.value for x in at.success)
    # A write may finish before its event reaches Python, so cancellation must
    # not promise rollback while this operation's result remains unknown.
    assert "Cancel restore" not in [b.label for b in at.button]
    frontend.deliver()
    assert json.loads(frontend.raw[key]) == candidate
    assert at.session_state["progress"] == original
    run(at)
    assert at.session_state["progress"] == candidate
    assert "pending_restore" not in at.session_state
    assert "save_disabled" not in at.session_state
    assert at.session_state["view"] == "Results & downloads"
    assert at.session_state["domain"] == 0
    assert at.session_state["review_responses"] == {}
    assert any("Backup restored and saved" in x.value for x in at.success)
    assert frontend.raw[other_key] == "other-set-do-not-touch"
    frontend.settle(at)
    assert any("Saved in this browser" in x.value for x in at.caption)
    at.radio(key="view").set_value("Practice")
    run(at)
    target = next(q["id"] for q in load_bank(number)["questions"] if q["id"] not in candidate["flags"])
    at.selectbox(key="jump").set_value(target)
    run(at)
    click(at, "Flag for review")
    frontend.settle(at)
    assert len(json.loads(frontend.raw[key])["flags"]) == 2
    assert restore_progress(frontend.raw[key], load_bank(number))["wrong_answers"] == candidate["wrong_answers"]


@pytest.mark.parametrize("raw", ['{"schema_version":2}', '{"bank_id":"wrong-set"}', '[]'])
def test_other_invalid_records_also_recover_after_confirmed_backup(frontend, monkeypatch, raw):
    at, key = start(frontend, raw=raw)
    assert "save_disabled" in at.session_state
    submit_import(at, monkeypatch, backup(1))
    assert frontend.raw[key] == raw
    frontend.settle(at)
    assert at.session_state["progress"] == backup(1)
    assert "save_disabled" not in at.session_state


@pytest.mark.parametrize("ack", ["normal-save", "other-replacement", "same-token-old-content"])
def test_unrelated_or_stale_acknowledgements_cannot_commit(frontend, monkeypatch, ack):
    at, key = start(frontend)
    original = deepcopy(at.session_state["progress"])
    candidate = backup(1)
    submit_import(at, monkeypatch, candidate)
    pending = deepcopy(at.session_state["pending_restore"])
    ack_id = {
        "normal-save": browser_storage.storage_request_id(candidate),
        "other-replacement": browser_storage.storage_request_id(candidate, replacement_id="b" * 32),
        "same-token-old-content": browser_storage.storage_request_id(empty_progress(load_bank()), replacement_id=pending["replacement_id"]),
    }[ack]
    frontend.publish_wrong_ack(ack_id)
    run(at)
    assert at.session_state["pending_restore"] == pending
    assert at.session_state["progress"] == original
    assert at.session_state["storage_baseline_id"] == pending["expected_baseline"]
    assert frontend.raw[key] == "{broken"
    assert not at.success
    frontend.settle(at)
    assert at.session_state["progress"] == candidate


def test_failed_restore_and_cancel_preserve_corrupt_raw_and_current_session(frontend, monkeypatch):
    at, key = start(frontend)
    original = deepcopy(at.session_state["progress"])
    submit_import(at, monkeypatch, backup(1))
    frontend.fail_replacement()
    run(at)
    assert any("Storage is full" in e.value for e in at.error)
    assert at.session_state["progress"] == original
    assert "save_disabled" in at.session_state
    assert frontend.raw[key] == "{broken"
    click(at, "Cancel restore")
    frontend.settle(at)
    assert "pending_restore" not in at.session_state
    assert "save_disabled" in at.session_state
    assert at.session_state["progress"] == original
    assert frontend.raw[key] == "{broken"
    assert not frontend.writes


def test_retry_uses_new_token_and_same_baseline_without_early_session_commit(frontend, monkeypatch):
    at, key = start(frontend)
    original = deepcopy(at.session_state["progress"])
    submit_import(at, monkeypatch, backup(1))
    first = deepcopy(at.session_state["pending_restore"])
    frontend.fail_replacement()
    run(at)
    click(at, "Retry saving this backup")
    retry = at.session_state["pending_restore"]
    assert retry["replacement_id"] != first["replacement_id"]
    assert retry["expected_baseline"] == first["expected_baseline"]
    assert at.session_state["progress"] == original
    assert frontend.raw[key] == "{broken"
    frontend.settle(at)
    assert at.session_state["progress"] == backup(1)
    assert len(frontend.writes) == 1


def test_other_tab_change_rejects_import_and_retry_without_adopting_new_baseline(frontend, monkeypatch):
    at, key = start(frontend)
    submit_import(at, monkeypatch, backup(1))
    before = deepcopy(at.session_state["pending_restore"])
    newer = empty_progress(load_bank())
    newer["flags"] = ["CCNA1-010"]
    frontend.raw[key] = json.dumps(newer)
    frontend.deliver()
    run(at)
    assert any("Another tab changed" in e.value for e in at.error)
    click(at, "Retry saving this backup")
    assert at.session_state["pending_restore"]["expected_baseline"] == before["expected_baseline"]
    frontend.deliver()
    run(at)
    assert any("Another tab changed" in e.value for e in at.error)
    assert json.loads(frontend.raw[key]) == newer
    assert not frontend.writes


def test_ambiguous_readback_conflict_cancel_cannot_overwrite_newer_browser_record(frontend, monkeypatch):
    original = empty_progress(load_bank())
    original["flags"] = ["CCNA1-004"]
    at, key = start(frontend, raw=json.dumps(original))
    assert "save_disabled" not in at.session_state
    submit_import(at, monkeypatch, backup(1))
    newer = empty_progress(load_bank())
    newer["flags"] = ["CCNA1-020"]
    frontend.fail_replacement("conflict", changed_raw=json.dumps(newer))
    run(at)
    assert at.session_state["progress"] == original
    click(at, "Cancel restore")
    frontend.settle(at)
    assert at.session_state["progress"] == original
    assert json.loads(frontend.raw[key]) == newer
    assert any("Automatic saving is paused" in x.value for x in at.warning)
    assert not any("Saved in this browser" in x.value for x in at.caption)


@pytest.mark.parametrize("kind", ["invalid-json", "wrong-bank", "inconsistent-history", "unconfirmed"])
def test_restore_form_rejects_bad_or_unconfirmed_import_before_staging(frontend, monkeypatch, kind):
    at, key = start(frontend)
    candidate = backup(1)
    if kind == "invalid-json":
        candidate = b"{bad"
    elif kind == "wrong-bank":
        candidate = backup(2)
    elif kind == "inconsistent-history":
        candidate["wrong_answers"] = {}
    submit_import(at, monkeypatch, candidate, confirmed=kind != "unconfirmed")
    assert "pending_restore" not in at.session_state
    assert at.session_state["progress"] == empty_progress(load_bank())
    assert frontend.raw[key] == "{broken"
    assert not frontend.writes
    assert at.error if kind != "unconfirmed" else at.warning
