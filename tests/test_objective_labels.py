"""The weakness report must name every supported Cisco v1.1 objective."""
import json

from quiz_core import LEAF_OBJECTIVES, OBJECTIVE_COUNTS, ROOT, SET_NUMBERS, load_bank


def test_objective_labels_cover_exact_blueprint_and_question_tags():
    catalog = json.loads((ROOT / "data/objectives.json").read_text(encoding="utf-8"))
    labels = catalog["objectives"]
    parents = {
        f"{domain}.{number}"
        for domain, count in OBJECTIVE_COUNTS.items()
        for number in range(1, count + 1)
    }
    assert len(parents) == 53
    assert set(labels) == parents | LEAF_OBJECTIVES
    assert all(isinstance(label, str) and label == label.strip() and label for label in labels.values())
    assert all(label != objective for objective, label in labels.items())
    assert catalog["metadata"]["version"] == "1.1"
    assert catalog["metadata"]["source_url"] == (
        "https://learningcontent.cisco.com/documents/marketing/exam-topics/"
        "200-301-CCNA-v1.1.pdf"
    )
    for number in SET_NUMBERS:
        for question in load_bank(number)["questions"]:
            assert set(question["objectives"]) <= set(labels), question["id"]


def test_labels_distinguish_adjacent_and_repeated_objective_concepts():
    labels = json.loads((ROOT / "data/objectives.json").read_text(encoding="utf-8"))["objectives"]
    assert "IPv4" in labels["1.6"] and "IPv6" in labels["1.8"]
    assert labels["3.1.e"] != labels["3.2.b"]
    assert labels["3.1.f"] != labels["3.2.c"]
    assert "AI/ML" in labels["6.4"]
    assert "Ansible" in labels["6.6"] and "Terraform" in labels["6.6"]
