"""Question loading and deterministic, all-or-nothing practice scoring."""
from collections import Counter
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent
DOMAIN_NAMES = {
    1: "Network Fundamentals", 2: "Network Access", 3: "IP Connectivity",
    4: "IP Services", 5: "Security Fundamentals", 6: "Automation and Programmability",
}
DOMAIN_COUNTS = {1: 20, 2: 20, 3: 25, 4: 10, 5: 15, 6: 10}
SET_NUMBERS = tuple(range(1, 11))
OBJECTIVE_COUNTS = {1: 13, 2: 9, 3: 5, 4: 9, 5: 10, 6: 7}
LEAF_COUNTS = {"1.1": 8, "1.2": 6, "1.3": 2, "1.9": 4, "1.11": 4, "1.13": 4,
               "2.1": 3, "2.2": 3, "2.5": 4, "3.1": 7, "3.2": 3, "3.3": 4, "3.4": 4, "6.3": 2}
LEAF_OBJECTIVES = {f"{parent}.{chr(97 + i)}" for parent, count in LEAF_COUNTS.items() for i in range(count)}


def load_bank(set_number=1):
    if type(set_number) is not int or set_number not in SET_NUMBERS:
        raise ValueError("Choose a set from 1 to 10.")
    path = ROOT / ("data/questions.json" if set_number == 1 else f"data/sets/set-{set_number:02d}.json")
    return json.loads(path.read_text(encoding="utf-8"))


def document_path(set_number, *, coverage=False):
    if set_number == 1:
        return ROOT / ("docs/coverage.md" if coverage else "docs/question-bank.md")
    return ROOT / f'docs/sets/set-{set_number:02d}{"-coverage" if coverage else ""}.md'


def validate_bank(bank):
    match = re.fullmatch(r"ccna-200-301-v1\.1-set-(\d{2})", bank["metadata"]["set_id"])
    assert match and int(match[1]) in SET_NUMBERS, "Unknown set identifier"
    set_number = int(match[1])
    questions = bank["questions"]
    assert len(questions) == 100, "Set must contain exactly 100 questions"
    assert Counter(q["domain"] for q in questions) == DOMAIN_COUNTS
    assert [q["id"] for q in questions] == [f"CCNA{set_number}-{n:03d}" for n in range(1, 101)]
    assert len({q["prompt"].strip().lower() for q in questions}) == 100
    for q in questions:
        ids = [c["id"] for c in q["choices"]]
        assert len(ids) == len(set(ids)) >= 3, q["id"]
        assert len({c["text"] for c in q["choices"]}) == len(ids), q["id"]
        assert q["objectives"] and all(o.startswith(f'{q["domain"]}.') for o in q["objectives"])
        assert all(re.fullmatch(r"[1-6]\.\d+(\.[a-h])?", o) and 1 <= int(o.split(".")[1]) <= OBJECTIVE_COUNTS[q["domain"]] for o in q["objectives"]), q["id"]
        assert all(o.count(".") == 1 or o in LEAF_OBJECTIVES for o in q["objectives"]), q["id"]
        assert q["explanation"].strip() and all(c["explanation"].strip() for c in q["choices"])
        assert q["difficulty"] in {"Foundation", "Applied", "Challenge"}
        assert q["references"] and all(r["url"].startswith("https://") and r["title"] and r["section"] for r in q["references"])
        if q["type"] == "matching":
            assert q["pairs"] and all(p["answer"] in ids for p in q["pairs"])
            assert len({p["id"] for p in q["pairs"]}) == len(q["pairs"])
        else:
            assert q["type"] in {"single", "multiple"}
            assert set(q["answer"]) <= set(ids)
            assert len(q["answer"]) == len(set(q["answer"]))
            assert len(q["answer"]) == 1 if q["type"] == "single" else len(q["answer"]) >= 2
    return True


def response_error(q, response):
    ids = {c["id"] for c in q["choices"]}
    if q["type"] == "matching":
        if not isinstance(response, dict) or set(response) != {p["id"] for p in q["pairs"]}:
            return "Choose an answer for every row."
        if any(value not in ids for value in response.values()):
            return "Choose an answer for every row."
    else:
        if not isinstance(response, list) or len(response) != len(q["answer"]) or not set(response) <= ids or len(set(response)) != len(response):
            return "Choose one answer." if q["type"] == "single" else f'Choose exactly {len(q["answer"])} answers.'
    return None


def is_correct(q, response):
    if response_error(q, response):
        return False
    if q["type"] == "matching":
        return response == {p["id"]: p["answer"] for p in q["pairs"]}
    return set(response) == set(q["answer"])


def summarize(questions, submissions):
    rows = []
    for domain, name in DOMAIN_NAMES.items():
        subset = [q for q in questions if q["domain"] == domain]
        answered = [q for q in subset if q["id"] in submissions]
        correct = sum(is_correct(q, submissions[q["id"]]) for q in answered)
        rows.append({"Domain": name, "Questions": len(subset), "Submitted": len(answered),
                     "Correct": correct, "To review": len(answered) - correct})
    return rows
