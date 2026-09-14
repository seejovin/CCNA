"""Describe current test performance and retained mistake history without writes.

``build_report(banks, progresses)`` accepts question banks and already validated
progress records keyed by bank ID. Missing records are empty attempts. Current
scores use each question's first submission, with the same all-or-nothing
scoring as the quiz. Review answers never replace those submissions. Restarting
an attempt therefore clears its current score while retaining mistake history;
these reports are not an archive of every completed attempt.

Objective tags identify the skills a question assesses, not a diagnosis of
which part of a multi-objective question caused an error. Parent rows include
explicit children once per question, but parent tags never imply that every
child was assessed. Objective rows can overlap and must not be summed to obtain
an overall score. Fewer than three answers are labelled as limited evidence;
the percentage thresholds are study heuristics, not Cisco passing standards or
validated predictions of exam readiness.
"""

from quiz_core import DOMAIN_NAMES, LEAF_OBJECTIVES, OBJECTIVE_COUNTS, is_correct


def _objective_key(objective):
    parts = objective.split(".")
    return int(parts[0]), int(parts[1]), parts[2:]


def _row(identifier, domain):
    return {
        "id": identifier,
        "domain": domain,
        "questions": 0,
        "answered": 0,
        "correct": 0,
        "incorrect": 0,
        "history_questions": 0,
        "wrong_attempts": 0,
        "pending_review": 0,
        "question_ids": [],
        "history_question_ids": [],
        "_missed_set_ids": set(),
    }


def _observe(row, question, bank_id, answered, correct, mistake):
    row["questions"] += 1
    if answered:
        row["answered"] += 1
        if correct:
            row["correct"] += 1
        else:
            row["incorrect"] += 1
            row["question_ids"].append(question["id"])
            row["_missed_set_ids"].add(bank_id)
    if mistake is not None:
        row["history_questions"] += 1
        row["wrong_attempts"] += mistake["wrong_count"]
        if mistake["reviewed_at"] is None:
            row["pending_review"] += 1
            row["history_question_ids"].append(question["id"])


def _finish(row):
    row["unanswered"] = row["questions"] - row["answered"]
    row["accuracy"] = (
        100 * row["correct"] / row["answered"] if row["answered"] else None
    )
    row["missed_set_ids"] = sorted(row.pop("_missed_set_ids"))
    row["missed_sets"] = len(row["missed_set_ids"])
    if not row["answered"]:
        row["status"] = "Review from history" if row["pending_review"] else "Not assessed"
    elif row["answered"] < 3:
        row["status"] = "Review · limited evidence" if row["incorrect"] else "Limited evidence"
    elif row["accuracy"] < 70:
        row["status"] = "Priority review"
    elif row["accuracy"] < 85:
        row["status"] = "Review"
    else:
        row["status"] = "On track"
    return row


def build_report(banks, progresses):
    """Return totals, set/domain/objective rows, and ranked review priorities.

    Rows expose current ``question_ids`` (incorrect first submissions) separately
    from ``history_question_ids`` (unresolved retained mistakes). The
    ``history_questions`` count includes resolved and unresolved records, while
    ``wrong_attempts`` counts their recorded wrong submissions and retries.
    ``missed_sets`` counts distinct sets with current errors; ``missed_set_ids``
    exposes those IDs. Accuracy has an answered-question denominator, not the
    whole bank, and is None when nothing has been answered.

    Priorities retain the most specific explicit tag for each missed or pending
    question. An ancestor is suppressed for a particular question when a child
    is tagged, but a separate parent-only miss still produces a parent priority.
    Priority metrics are the corresponding full objective aggregate;
    ``focus_question_ids`` identifies the exact questions that nominated that
    priority. These lists and objective aggregates may overlap. Resolving a
    review removes its history signal but does not remove an original test miss.

    Neither input is mutated. Duplicate bank/question IDs and progress keyed to
    the wrong bank raise ValueError instead of silently double-counting scores.
    Progress records for banks outside the requested report scope are ignored.
    """
    banks = list(banks)
    domains = {domain: _row(domain, domain) for domain in DOMAIN_NAMES}
    parent_ids = {
        f"{domain}.{number}"
        for domain, count in OBJECTIVE_COUNTS.items()
        for number in range(1, count + 1)
    }
    objectives = {
        identifier: _row(identifier, int(identifier.split(".")[0]))
        for identifier in sorted(parent_ids | LEAF_OBJECTIVES, key=_objective_key)
    }
    total = _row("overall", None)
    set_rows = []
    seen_banks, seen_questions = set(), set()
    priority_questions = {}

    for bank in banks:
        bank_id = bank["metadata"]["set_id"]
        if bank_id in seen_banks:
            raise ValueError(f"Duplicate question set in analytics: {bank_id}.")
        seen_banks.add(bank_id)
        progress = progresses.get(bank_id)
        if progress is not None and progress["bank_id"] != bank_id:
            raise ValueError("Analytics progress belongs to a different question set.")
        submissions = progress["submissions"] if progress is not None else {}
        mistakes = progress["wrong_answers"] if progress is not None else {}
        set_row = _row(bank_id, None)
        set_row["set_number"] = int(bank_id.rsplit("-", 1)[1])

        for question in bank["questions"]:
            qid = question["id"]
            if qid in seen_questions:
                raise ValueError(f"Duplicate question in analytics: {qid}.")
            seen_questions.add(qid)
            answered = qid in submissions
            correct = is_correct(question, submissions[qid]) if answered else False
            mistake = mistakes.get(qid)
            explicit = set(question["objectives"])
            assessed = explicit | {".".join(tag.split(".")[:2]) for tag in explicit}
            for row in [total, set_row, domains[question["domain"]]]:
                _observe(row, question, bank_id, answered, correct, mistake)
            for identifier in assessed:
                _observe(objectives[identifier], question, bank_id, answered, correct, mistake)

            pending = mistake is not None and mistake["reviewed_at"] is None
            if (answered and not correct) or pending:
                parents_with_children = {
                    ".".join(tag.split(".")[:2]) for tag in explicit if tag.count(".") > 1
                }
                for identifier in sorted(explicit - parents_with_children, key=_objective_key):
                    priority_questions.setdefault(identifier, []).append(qid)

        set_row["completed"] = (
            set_row["questions"] > 0 and set_row["answered"] == set_row["questions"]
        )
        set_row["started"] = set_row["answered"] > 0
        set_rows.append(_finish(set_row))

    _finish(total)
    total["completed_sets"] = sum(row["completed"] for row in set_rows)
    total["started_sets"] = sum(row["started"] for row in set_rows)
    total["sets"] = len(set_rows)
    domain_rows = [_finish(row) for row in domains.values()]
    objective_rows = [_finish(row) for row in objectives.values()]
    priorities = [
        {**objectives[identifier], "focus_question_ids": list(qids)}
        for identifier, qids in priority_questions.items()
    ]
    priorities.sort(key=lambda row: (
        -row["incorrect"],
        -row["pending_review"],
        row["accuracy"] if row["accuracy"] is not None else float("inf"),
        _objective_key(row["id"]),
    ))
    return {
        "totals": total,
        "sets": set_rows,
        "domains": domain_rows,
        "objectives": objective_rows,
        "priorities": priorities,
    }
