"""Validate portable practice progress and retain a separate mistake history.

Storage is supplied by the caller. These helpers never write to disk or share
progress between users; they operate on one decoded browser or backup record.
"""
from copy import deepcopy
from datetime import datetime, timezone
import json

from quiz_core import is_correct, response_error


SCHEMA_VERSION = 1
PROGRESS_FIELDS = {
    "schema_version", "bank_id", "submissions", "flags", "wrong_answers"
}
MISTAKE_FIELDS = {
    "last_response", "wrong_count", "last_wrong_at", "reviewed_at"
}


def empty_progress(bank):
    """Return a new, independent empty record for this question set."""
    return {
        "schema_version": SCHEMA_VERSION,
        "bank_id": bank["metadata"]["set_id"],
        "submissions": {},
        "flags": [],
        "wrong_answers": {},
    }


def _timestamp(value):
    """Require an explicit time zone and produce a UTC ISO 8601 timestamp."""
    try:
        if isinstance(value, str) and len(value) <= 64:
            value = datetime.fromisoformat(value.replace("Z", "+00:00"))
        if not isinstance(value, datetime) or value.tzinfo is None or value.utcoffset() is None:
            raise ValueError
        return value.astimezone(timezone.utc).isoformat()
    except (ValueError, TypeError, OverflowError):
        raise ValueError("Progress timestamps must include a valid date, time and time zone.") from None


def _response(question, response):
    """Check JSON response shapes before the quiz scorer uses sets on them."""
    if question["type"] == "matching":
        safe_shape = isinstance(response, dict) and all(
            isinstance(key, str) and isinstance(value, str)
            for key, value in response.items()
        )
    else:
        safe_shape = isinstance(response, list) and all(isinstance(value, str) for value in response)
    if not safe_shape or response_error(question, response):
        raise ValueError(f'Invalid saved answer for {question["id"]}.')
    return deepcopy(response)


def _question_mapping(value, questions, label):
    if not isinstance(value, dict) or len(value) > len(questions):
        raise ValueError(f"Saved {label} must be a question mapping.")
    if any(not isinstance(qid, str) or qid not in questions for qid in value):
        raise ValueError(f"Saved {label} contains an unknown question.")


def restore_progress(raw, bank):
    """Validate a saved JSON string/dict and return an independent safe record.

    A missing record (None) starts a new attempt. An existing unsupported or
    malformed record raises ValueError so the caller can preserve it instead of
    accidentally replacing saved history with an empty record.
    """
    if raw is None:
        return empty_progress(bank)
    if isinstance(raw, str):
        try:
            raw = json.loads(raw)
        except (ValueError, RecursionError):
            raise ValueError("Saved progress is not valid JSON.") from None
    if not isinstance(raw, dict) or set(raw) != PROGRESS_FIELDS:
        raise ValueError("Saved progress has missing or unsupported fields.")
    if type(raw["schema_version"]) is not int or raw["schema_version"] != SCHEMA_VERSION:
        raise ValueError("This saved progress uses an unsupported version.")
    if raw["bank_id"] != bank["metadata"]["set_id"]:
        raise ValueError("This saved progress belongs to a different question set.")

    questions = {question["id"]: question for question in bank["questions"]}
    result = empty_progress(bank)
    _question_mapping(raw["submissions"], questions, "submissions")
    for qid, response in raw["submissions"].items():
        result["submissions"][qid] = _response(questions[qid], response)

    flags = raw["flags"]
    if not isinstance(flags, list) or len(flags) > len(questions) or any(
        not isinstance(qid, str) or qid not in questions for qid in flags
    ):
        raise ValueError("Saved flags must contain valid question IDs.")
    if len(set(flags)) != len(flags):
        raise ValueError("Saved flags contain duplicate questions.")
    result["flags"] = list(flags)

    _question_mapping(raw["wrong_answers"], questions, "mistakes")
    for qid, mistake in raw["wrong_answers"].items():
        if not isinstance(mistake, dict) or set(mistake) != MISTAKE_FIELDS:
            raise ValueError(f"Saved mistake for {qid} has missing or unsupported fields.")
        response = _response(questions[qid], mistake["last_response"])
        if is_correct(questions[qid], response):
            raise ValueError(f"Saved mistake for {qid} must contain an incorrect answer.")
        count = mistake["wrong_count"]
        if type(count) is not int or count < 1:
            raise ValueError(f"Saved mistake count for {qid} must be a positive integer.")
        reviewed = mistake["reviewed_at"]
        result["wrong_answers"][qid] = {
            "last_response": response,
            "wrong_count": count,
            "last_wrong_at": _timestamp(mistake["last_wrong_at"]),
            "reviewed_at": None if reviewed is None else _timestamp(reviewed),
        }
    # Every incorrect first submission created by v1 recorded a mistake in the
    # same operation. A later correct review may resolve it, but never deletes
    # its history. Reject partial imports instead of silently losing the review
    # queue or inventing an unobserved last_wrong_at timestamp.
    for qid, response in result["submissions"].items():
        if not is_correct(questions[qid], response) and qid not in result["wrong_answers"]:
            raise ValueError(f"Saved incorrect answer for {qid} is missing its mistake history.")
    return result


def record_answer(progress, question, response, *, review=False, now=None):
    """Record one validated submission or review without replacing first scores.

    Every invocation represents an actual submitted response. The UI must lock
    an answered form until the user explicitly starts a new review or attempt.
    A correct retry resolves a mistake while preserving the last wrong answer.
    """
    response = _response(question, response)
    timestamp = _timestamp(datetime.now(timezone.utc) if now is None else now)
    qid = question["id"]
    if not review and qid not in progress["submissions"]:
        progress["submissions"][qid] = deepcopy(response)
    if is_correct(question, response):
        if qid in progress["wrong_answers"]:
            progress["wrong_answers"][qid]["reviewed_at"] = timestamp
    else:
        previous = progress["wrong_answers"].get(qid)
        progress["wrong_answers"][qid] = {
            "last_response": deepcopy(response),
            "wrong_count": previous["wrong_count"] + 1 if previous else 1,
            "last_wrong_at": timestamp,
            "reviewed_at": None,
        }


def restart_attempt(progress):
    """Clear the current score and flags, preserving all mistake history."""
    progress["submissions"] = {}
    progress["flags"] = []
