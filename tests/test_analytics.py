"""Evidence-focused reporting tests using the real submission/history contract."""

from copy import deepcopy

import pytest

from analytics import build_report
from progress_store import empty_progress, record_answer, restart_attempt, restore_progress
from quiz_core import LEAF_OBJECTIVES, OBJECTIVE_COUNTS


NOW = "2026-09-14T12:00:00+00:00"


def bank(number=1, count=1, *, tags=None, domain=1):
    return {
        "metadata": {"set_id": f"ccna-200-301-v1.1-set-{number:02d}"},
        "questions": [
            {
                "id": f"CCNA{number}-{index:03d}",
                "domain": domain,
                "objectives": list(tags if tags is not None else ["1.1.a"]),
                "type": "single",
                "choices": [{"id": letter} for letter in "ABC"],
                "answer": ["A"],
            }
            for index in range(1, count + 1)
        ],
    }


def progress_for(question_bank, correct=0, answered=None):
    progress = empty_progress(question_bank)
    if answered is None:
        answered = len(question_bank["questions"])
    for index, question in enumerate(question_bank["questions"][:answered]):
        record_answer(progress, question, ["A"] if index < correct else ["B"], now=NOW)
    return restore_progress(progress, question_bank)


def report_for(banks, records=()):
    return build_report(banks, {record["bank_id"]: record for record in records})


def objective(report, identifier):
    return next(row for row in report["objectives"] if row["id"] == identifier)


def test_overall_uses_question_weighting_and_keeps_unanswered_separate():
    first, second, untouched = bank(1, 10), bank(2, 2), bank(3, 5)
    report = report_for([first, second, untouched], [progress_for(first, correct=10), progress_for(second)])
    total = report["totals"]
    assert total["questions"] == 17
    assert total["answered"] == 12
    assert total["correct"] == 10
    assert total["incorrect"] == 2
    assert total["unanswered"] == 5
    assert total["accuracy"] == pytest.approx(100 * 10 / 12)
    assert total["accuracy"] != 50  # An average of set percentages would mislead.
    assert (total["sets"], total["started_sets"], total["completed_sets"]) == (3, 2, 2)
    assert report["sets"][2]["accuracy"] is None
    assert report["sets"][2]["status"] == "Not assessed"
    assert report["sets"][2]["set_number"] == 3


def test_partial_attempt_is_not_a_completed_test_or_an_unanswered_failure():
    question_bank = bank(count=100)
    report = report_for([question_bank], [progress_for(question_bank, correct=2, answered=3)])
    assert report["totals"]["accuracy"] == pytest.approx(200 / 3)
    assert report["totals"]["incorrect"] == 1
    assert report["totals"]["unanswered"] == 97
    assert report["totals"]["completed_sets"] == 0
    assert report["totals"]["started_sets"] == 1
    assert report["sets"][0]["completed"] is False


@pytest.mark.parametrize("answered,correct,expected", [
    (0, 0, "Not assessed"),
    (1, 0, "Review · limited evidence"),
    (1, 1, "Limited evidence"),
    (2, 1, "Review · limited evidence"),
    (2, 2, "Limited evidence"),
    (3, 2, "Priority review"),
    (10, 7, "Review"),
    (20, 16, "Review"),
    (20, 17, "On track"),
    (20, 20, "On track"),
])
def test_status_thresholds_do_not_overstate_tiny_samples(answered, correct, expected):
    question_bank = bank(count=max(1, answered))
    report = report_for([question_bank], [progress_for(question_bank, correct, answered)])
    assert report["totals"]["status"] == expected
    assert objective(report, "1.1.a")["status"] == expected


def test_all_domains_and_objectives_exist_even_before_assessment():
    report = report_for([bank(tags=["1.1"])])
    assert len(report["domains"]) == 6
    assert len(report["objectives"]) == sum(OBJECTIVE_COUNTS.values()) + len(LEAF_OBJECTIVES)
    assert all(row["accuracy"] is None for row in report["objectives"])
    assert report["priorities"] == []
    assert report["totals"]["accuracy"] is None


def test_explicit_children_roll_up_once_and_parent_only_does_not_assess_children():
    question_bank = bank(count=3)
    question_bank["questions"][0]["objectives"] = ["1.1", "1.1.a", "1.1.a", "1.1.b"]
    question_bank["questions"][1]["objectives"] = ["1.1"]
    question_bank["questions"][2]["objectives"] = ["1.1.b"]
    progress = progress_for(question_bank)
    report = report_for([question_bank], [progress])
    assert objective(report, "1.1")["answered"] == 3
    assert objective(report, "1.1.a")["answered"] == 1
    assert objective(report, "1.1.b")["answered"] == 2
    assert objective(report, "1.1.c")["questions"] == 0
    assert objective(report, "1.1.c")["status"] == "Not assessed"
    priorities = {row["id"]: row for row in report["priorities"]}
    assert set(priorities) == {"1.1", "1.1.a", "1.1.b"}
    assert priorities["1.1"]["focus_question_ids"] == ["CCNA1-002"]
    assert priorities["1.1.a"]["focus_question_ids"] == ["CCNA1-001"]
    assert priorities["1.1.b"]["focus_question_ids"] == ["CCNA1-001", "CCNA1-003"]
    assert report["totals"]["incorrect"] == 3


def test_child_miss_does_not_produce_redundant_parent_priority():
    question_bank = bank(tags=["1.1", "1.1.a", "1.1.b"])
    report = report_for([question_bank], [progress_for(question_bank)])
    assert {row["id"] for row in report["priorities"]} == {"1.1.a", "1.1.b"}
    assert objective(report, "1.1")["incorrect"] == 1


def test_parent_only_miss_never_invents_a_child_weakness():
    question_bank = bank(tags=["1.1"])
    report = report_for([question_bank], [progress_for(question_bank)])
    assert [row["id"] for row in report["priorities"]] == ["1.1"]
    assert all(
        row["answered"] == 0 and row["questions"] == 0
        for row in report["objectives"] if row["id"].startswith("1.1.")
    )


def test_recurring_misses_count_distinct_sets_not_retry_events():
    first, second, third = bank(1), bank(2), bank(3)
    p1, p2, p3 = progress_for(first), progress_for(second), progress_for(third, correct=1)
    record_answer(p1, first["questions"][0], ["B"], review=True, now=NOW)
    report = report_for([first, second, third], [p1, p2, p3])
    row = objective(report, "1.1.a")
    assert (row["answered"], row["incorrect"], row["missed_sets"]) == (3, 2, 2)
    assert row["history_questions"] == 2
    assert row["wrong_attempts"] == 3
    assert row["pending_review"] == 2
    assert row["missed_set_ids"] == [p1["bank_id"], p2["bank_id"]]
    assert row["question_ids"] == ["CCNA1-001", "CCNA2-001"]
    assert row["history_question_ids"] == row["question_ids"]


def test_multiple_choice_and_matching_use_all_or_nothing_scoring():
    question_bank = bank(count=3)
    multiple, matching, single = question_bank["questions"]
    multiple.update(type="multiple", answer=["A", "B"])
    matching.update(type="matching", pairs=[{"id": "row1", "answer": "A"}, {"id": "row2", "answer": "B"}])
    progress = empty_progress(question_bank)
    record_answer(progress, multiple, ["A", "C"], now=NOW)
    record_answer(progress, matching, {"row1": "A", "row2": "C"}, now=NOW)
    record_answer(progress, single, ["A"], now=NOW)
    report = report_for([question_bank], [restore_progress(progress, question_bank)])
    assert report["totals"]["correct"] == 1
    assert report["totals"]["incorrect"] == 2
    assert report["totals"]["accuracy"] == pytest.approx(100 / 3)
    assert report["totals"]["question_ids"] == [multiple["id"], matching["id"]]


def test_correct_review_does_not_rescore_and_restart_retains_only_history_signal():
    question_bank = bank()
    question = question_bank["questions"][0]
    progress = progress_for(question_bank)
    record_answer(progress, question, ["A"], review=True, now=NOW)
    report = report_for([question_bank], [progress])
    assert report["totals"]["incorrect"] == 1
    assert report["totals"]["history_questions"] == 1
    assert report["totals"]["pending_review"] == 0
    assert report["totals"]["history_question_ids"] == []
    assert len(report["priorities"]) == 1  # Original scored miss remains visible.

    restart_attempt(progress)
    report = report_for([question_bank], [progress])
    assert report["totals"]["accuracy"] is None
    assert report["totals"]["history_questions"] == 1
    assert report["totals"]["pending_review"] == 0
    assert report["priorities"] == []

    record_answer(progress, question, ["B"], review=True, now=NOW)
    report = report_for([question_bank], [progress])
    row = objective(report, "1.1.a")
    assert row["answered"] == 0
    assert row["wrong_attempts"] == 2
    assert row["pending_review"] == 1
    assert row["missed_sets"] == 0
    assert row["question_ids"] == []
    assert row["history_question_ids"] == [question["id"]]
    assert row["status"] == "Review from history"
    assert report["priorities"][0]["focus_question_ids"] == [question["id"]]

    record_answer(progress, question, ["A"], now=NOW)
    report = report_for([question_bank], [progress])
    assert report["totals"]["accuracy"] == 100
    assert report["totals"]["history_questions"] == 1
    assert report["totals"]["pending_review"] == 0
    assert report["priorities"] == []


def test_priorities_sort_current_misses_then_pending_then_accuracy():
    question_bank = bank(count=7)
    tags = ["1.1.a", "1.1.a", "1.1.a", "1.1.b", "1.1.b", "1.1.c", "1.1.d"]
    for question, tag in zip(question_bank["questions"], tags):
        question["objectives"] = [tag]
    progress = empty_progress(question_bank)
    for index, question in enumerate(question_bank["questions"]):
        if index < 6:
            record_answer(progress, question, ["A"] if index == 0 else ["B"], now=NOW)
        else:
            record_answer(progress, question, ["B"], review=True, now=NOW)
    # A and B tie on misses and pending; B has lower accuracy. C has one miss.
    # D is a pending historical error with no current scored answer.
    report = report_for([question_bank], [progress])
    assert [row["id"] for row in report["priorities"]] == ["1.1.b", "1.1.a", "1.1.c", "1.1.d"]
    record_answer(progress, question_bank["questions"][3], ["A"], review=True, now=NOW)
    report = report_for([question_bank], [progress])
    assert [row["id"] for row in report["priorities"]][:2] == ["1.1.a", "1.1.b"]


def test_report_does_not_mutate_inputs_or_mix_out_of_scope_progress():
    first, second = bank(1), bank(2)
    p1, p2 = progress_for(first), progress_for(second)
    banks = [first]
    progresses = {p1["bank_id"]: p1, p2["bank_id"]: p2}
    before = deepcopy((banks, progresses))
    report = build_report(banks, progresses)
    assert (banks, progresses) == before
    assert report["totals"]["answered"] == 1
    assert report["totals"]["history_questions"] == 1
    report["objectives"][0]["question_ids"].clear()
    assert (banks, progresses) == before


def test_duplicate_inputs_and_miskeyed_progress_are_rejected():
    first, second = bank(1), bank(2)
    with pytest.raises(ValueError, match="Duplicate question set"):
        report_for([first, first])
    second["questions"][0]["id"] = first["questions"][0]["id"]
    with pytest.raises(ValueError, match="Duplicate question in analytics"):
        report_for([first, second])
    with pytest.raises(ValueError, match="different question set"):
        build_report([first], {first["metadata"]["set_id"]: empty_progress(bank(2))})
