"""Acceptance checks for the complete ten-set collection."""
from collections import Counter
from hashlib import sha256
import json
import re

from browser_storage import DEFAULT_BANK_ID, STORAGE_KEY, storage_key
from progress_store import empty_progress, record_answer, restore_progress
from quiz_core import DOMAIN_COUNTS, OBJECTIVE_COUNTS, LEAF_OBJECTIVES, ROOT, SET_NUMBERS, document_path, load_bank, validate_bank


# Set 01 is the user's existing, published bank; its questions must not change.
ORIGINAL_SET_01_SHA256 = "c0d9ce89219f4ddd788452560c56438ed3829ec7b26b0ad05178ea93237d4b7d"


def test_complete_collection_allocations_coverage_and_unique_questions():
    prompts, identities, leaves = set(), set(), set()
    total = Counter()
    expected_parents = {f"{domain}.{n}" for domain, count in OBJECTIVE_COUNTS.items() for n in range(1, count + 1)}
    for number in SET_NUMBERS:
        bank = load_bank(number)
        assert validate_bank(bank)
        assert bank["metadata"]["question_count"] == 100
        assert bank["metadata"]["domain_counts"] == {str(k): v for k, v in DOMAIN_COUNTS.items()}
        parents = {".".join(tag.split(".")[:2]) for q in bank["questions"] for tag in q["objectives"]}
        assert expected_parents <= parents, (number, expected_parents - parents)
        for q in bank["questions"]:
            leaves.update(q["objectives"])
            normalized = re.sub(r"\s+", " ", q["prompt"].strip().casefold())
            # Shared generic matching instructions can recur if the actual
            # matching tasks differ, but fully identical items cannot recur.
            identity = json.dumps([normalized, q.get("exhibit"), [c["text"] for c in q["choices"]], q.get("pairs")], sort_keys=True)
            assert identity not in identities, q["id"]
            identities.add(identity)
            prompts.add(normalized)
            total[q["domain"]] += 1
        assert document_path(number).is_file()
        assert document_path(number, coverage=True).is_file()
    assert len(identities) == 1000
    assert LEAF_OBJECTIVES <= leaves
    assert total == {d: n * 10 for d, n in DOMAIN_COUNTS.items()}
    assert sha256((ROOT / "data/questions.json").read_bytes()).hexdigest() == ORIGINAL_SET_01_SHA256


def test_storage_keys_and_backup_scope_preserve_set01():
    assert storage_key(DEFAULT_BANK_ID) == STORAGE_KEY
    keys = {storage_key(load_bank(n)["metadata"]["set_id"]) for n in SET_NUMBERS}
    assert len(keys) == 10
    import pytest
    with pytest.raises(ValueError):
        storage_key("ccna-200-301-v1.1-set-11")
    first, second = load_bank(1), load_bank(2)
    progress = empty_progress(first)
    q = first["questions"][0]
    response = {p["id"]: p["answer"] for p in q["pairs"]} if q["type"] == "matching" else q["answer"]
    record_answer(progress, q, response)
    with pytest.raises(ValueError, match="different question set"):
        restore_progress(progress, second)
