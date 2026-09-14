"""Rebuild human-readable exports and objective coverage from the JSON source."""
import argparse
import json
from collections import Counter
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from quiz_core import DOMAIN_NAMES, SET_NUMBERS, OBJECTIVE_COUNTS, LEAF_OBJECTIVES, document_path, load_bank, validate_bank


def build_set(set_number):
    bank = load_bank(set_number)
    validate_bank(bank)
    questions = bank["questions"]
    lines = [f"# CCNA Practice — Set {set_number:02d}", "", "100 original questions aligned to CCNA 200-301 v1.1. No interactive labs.", "",
             "Answers and explanations follow each question. For an unrevealed attempt, use the Streamlit app.", "",
             f'Content review date: {bank["metadata"]["reviewed_on"]}.', ""]
    for q in questions:
        lines += [f'## {q["id"]} · {DOMAIN_NAMES[q["domain"]]}', "", f'Objectives: {", ".join(q["objectives"])} · {q["type"]} · {q["difficulty"]}', "", q["prompt"], ""]
        e = q.get("exhibit")
        if e and e["kind"] == "code":
            lines += ["```text", e["content"], "```", ""]
        elif e and e["kind"] == "table":
            lines += ["| " + " | ".join(e["headers"]) + " |", "| " + " | ".join(["---"] * len(e["headers"])) + " |"]
            lines += ["| " + " | ".join(str(x).replace("|", "\\|") for x in row) + " |" for row in e["rows"]]
            lines += [""]
        if q.get("diagram"):
            lines += ["```mermaid", "flowchart TD"]
            lines += [f'{n["id"]}[{json.dumps(n["label"])}]' for n in q["diagram"]["nodes"]]
            lines += [f'{e["from"]} ---|{json.dumps(e.get("label", ""))}| {e["to"]}' for e in q["diagram"]["edges"]]
            lines += ["```", ""]
        if q["type"] == "matching":
            lines += [f'{p["id"]}. {p["text"]}' for p in q["pairs"]] + [""]
        for c in q["choices"]:
            if "\n" in c["text"]:
                lines += [f'**Configuration {c["id"]}**', "", "```text", c["text"], "```", ""]
            else:
                lines += [f'- **{c["id"]}.** {c["text"]}']
        lines += [""]
        key = "; ".join(f'{p["id"]} → {p["answer"]}' for p in q["pairs"]) if q["type"] == "matching" else ", ".join(q["answer"])
        lines += [f'**Answer: {key}**', "", q["explanation"], "", "**Option explanations**", ""]
        lines += [f'- **{c["id"]}:** {c["explanation"]}' for c in q["choices"]] + ["", "**Further reading**", ""]
        lines += [f'- [{r["title"]}]({r["url"]}) — {r["section"]}' for r in q["references"]] + ["", "---", ""]
    document_path(set_number).write_text("\n".join(lines), encoding="utf-8")

    types = Counter(q["type"] for q in questions)
    difficulty = Counter(q["difficulty"] for q in questions)
    counts = Counter(q["domain"] for q in questions)
    cover = [f"# Set {set_number:02d} coverage", "", "This set follows the requested CCNA 200-301 v1.1 allocation. Question count and scoring are practice design choices.", "",
             "[Cisco v1.1 exam blueprint](https://learningcontent.cisco.com/documents/marketing/exam-topics/200-301-CCNA-v1.1.pdf)", "",
             "| Domain | Questions |", "| --- | ---: |"]
    cover += [f"| {name} | {counts[d]} |" for d, name in DOMAIN_NAMES.items()]
    cover += ["", f'Types: {types["single"]} single-answer, {types["multiple"]} multiple-answer, {types["matching"]} matching.', "",
              "Matching uses accessible dropdowns. Code and table exhibits are constructed scenarios; there is no executable device lab.", "",
              "Difficulty labels are author estimates, not learner-calibrated measurements: " + ", ".join(f"{k} {v}" for k, v in difficulty.items()) + ".", "",
              "## Objective map", "", "Each row shows questions tagged to a top-level objective, including its tagged subtopics. A tag indicates assessment relevance; it does not mean every skill variation has been tested. Configuring and verifying live devices requires separate hands-on practice.", "",
              "| Objective | Question numbers | Subtopic tags used |", "| --- | --- | --- |"]
    for d, max_n in {1: 13, 2: 9, 3: 5, 4: 9, 5: 10, 6: 7}.items():
        for n in range(1, max_n + 1):
            o = f"{d}.{n}"
            subset = [q for q in questions if any(t == o or t.startswith(o + ".") for t in q["objectives"])]
            tags = sorted({t for q in subset for t in q["objectives"] if t.startswith(o + ".")})
            cover.append(f'| {o} | {", ".join(str(int(q["id"].split("-")[-1])) for q in subset) or "Not assessed"} | {", ".join(tags) or "—"} |')
    # Leaf IDs from the linked v1.1 blueprint; other objectives have no lettered children.
    leaf_counts = {"1.1": 8, "1.2": 6, "1.3": 2, "1.9": 4, "1.11": 4, "1.13": 4, "2.1": 3, "2.2": 3, "2.5": 4, "3.1": 7, "3.2": 3, "3.3": 4, "3.4": 4, "6.3": 2}
    expected = {f"{parent}.{chr(97 + i)}" for parent, count in leaf_counts.items() for i in range(count)}
    tagged = {o for q in questions for o in q["objectives"]}
    missing = sorted(expected - tagged, key=lambda x: [int(t) if t.isdigit() else t for t in x.split(".")])
    cover += ["", "Lettered blueprint subtopics without a direct question tag: " + (", ".join(missing) if missing else "none") + ".", "",
              "## Sources and review", "", "Questions are original. Technical references point to primary documentation; none is represented as a recalled or official exam question. Authors checked platform assumptions, keys and distractors against the cited sources. Automated checks validate counts, schema and scoring, not technical truth. Peer review findings and corrections are recorded in the repository's review notes.", "",
              "One point is awarded only when the entire answer is correct. Multiple-answer and matching questions receive no partial credit. The app records the first submitted answer per question until restart. These rules do not reproduce Cisco scoring. This practice set is not psychometrically calibrated and does not predict an exam result.", "",
              "Version scope: v1.1. Cisco states that v1.1 remains available through February 2, 2027, with the refreshed exam beginning February 3, 2027. [Cisco transition announcement](https://blogs.cisco.com/learning/stay-on-track-get-certified-before-the-ccna-refresh)", ""]
    document_path(set_number, coverage=True).write_text("\n".join(cover), encoding="utf-8")
    print(f"Set {set_number:02d} exports: {len(questions)} questions; {dict(types)}; untagged lettered subtopics: {missing}")


def build_collection():
    banks = [load_bank(n) for n in SET_NUMBERS]
    lines = ["# CCNA Practice — ten-set collection", "", "1,000 original non-lab questions for CCNA 200-301 v1.1: ten sets of 100. Set 01 is the original bank; Sets 02–10 add 900 questions.", "",
             "Every set uses 20 Network Fundamentals, 20 Network Access, 25 IP Connectivity, 10 IP Services, 15 Security Fundamentals and 10 Automation and Programmability questions.", "",
             "| Set | Questions | Single answer | Multiple answer | Matching | Study guide | Coverage |",
             "| --- | ---: | ---: | ---: | ---: | --- | --- |"]
    for number, bank in zip(SET_NUMBERS, banks):
        types = Counter(q["type"] for q in bank["questions"])
        guide = document_path(number).relative_to(ROOT / "docs")
        coverage = document_path(number, coverage=True).relative_to(ROOT / "docs")
        lines.append(f'| {number:02d} | 100 | {types["single"]} | {types["multiple"]} | {types["matching"]} | [Answers & explanations]({guide}) | [Objective map]({coverage}) |')
    lines += ["", "[Coverage across all ten sets](objective-matrix.md) · [Primary reading references](references.md) · [Expansion review notes](expansion-review.md)", "",
              "## Using the collection", "", "Select a set in the app sidebar. Complete an attempt, revisit missed questions through Wrong-answer review, and use the cited resources to repair gaps. Repeat a missed question from its underlying reasoning before moving to another set. Scores apply to one selected set; each set keeps separate browser progress.", "",
              "Multiple-answer and matching items require the whole response to be correct for one point. Matching uses accessible dropdowns. CLI and table exhibits are written scenarios; they do not run devices. None of these sets includes interactive labs.", "",
              "The sets share curriculum objectives while varying cases, evidence and decisions. They are original practice material, not official exam papers. Labels such as Challenge are author judgments, not measured item difficulty; results have not been calibrated to predict Cisco exam outcomes.", ""]
    (ROOT / "docs/collection.md").write_text("\n".join(lines), encoding="utf-8")
    matrix = ["# Objective coverage across all sets", "", "Each cell counts questions tagged to the objective or one of its children. A question may assess multiple objectives, so column totals across objectives can exceed 100. Tags record assessed relevance, not proof of hands-on mastery.", "",
              "| Objective | " + " | ".join(f"Set {n:02d}" for n in SET_NUMBERS) + " |",
              "| --- | " + " | ".join(["---:"] * 10) + " |"]
    for d, count in OBJECTIVE_COUNTS.items():
        for n in range(1, count + 1):
            objective = f"{d}.{n}"
            counts = [sum(any(t == objective or t.startswith(objective + ".") for t in q["objectives"]) for q in b["questions"]) for b in banks]
            matrix.append(f'| {objective} | ' + ' | '.join(map(str, counts)) + ' |')
    leaves = {o for b in banks for q in b["questions"] for o in q["objectives"]}
    matrix += ["", "Lettered blueprint subtopics without an assessment tag anywhere in the collection: " + (", ".join(sorted(LEAF_OBJECTIVES - leaves)) or "none") + ".", ""]
    (ROOT / "docs/objective-matrix.md").write_text("\n".join(matrix), encoding="utf-8")
    refs = {}
    for b in banks:
        for q in b["questions"]:
            for ref in q["references"]:
                entry = refs.setdefault(ref["url"], {"title": ref["title"], "questions": set()})
                entry["questions"].add(q["id"])
    readings = ["# Primary reading references", "", f"{len(refs)} distinct reference URLs across the collection. Each question links to its relevant section; this index shows where each resource is used.", ""]
    for url, ref in sorted(refs.items(), key=lambda item: item[1]["title"].casefold()):
        readings += [f'## [{ref["title"]}]({url})', "", ", ".join(sorted(ref["questions"], key=lambda q: (int(q.split('-')[0][4:]), int(q.split('-')[1])))), ""]
    (ROOT / "docs/references.md").write_text("\n".join(readings), encoding="utf-8")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--set", type=int, choices=SET_NUMBERS, dest="set_number")
    args = parser.parse_args()
    (ROOT / "docs/sets").mkdir(parents=True, exist_ok=True)
    for number in ([args.set_number] if args.set_number else SET_NUMBERS):
        build_set(number)
    if not args.set_number:
        build_collection()


if __name__ == "__main__":
    main()
