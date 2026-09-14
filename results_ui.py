"""Readable curriculum evidence and actionable study priorities."""
import json
from functools import lru_cache

import pandas as pd
import streamlit as st

from quiz_core import DOMAIN_NAMES, ROOT


@lru_cache(maxsize=1)
def objective_names():
    return json.loads((ROOT / "data/objectives.json").read_text(encoding="utf-8"))["objectives"]


def objective_label(objective):
    return f"{objective} · {objective_names()[objective]}"


def table_rows(rows, level):
    result = []
    for row in rows:
        label = (DOMAIN_NAMES[row["id"]] if level == "domain" else
                 f'Set {row["set_number"]:02d}' if level == "set" else objective_label(row["id"]))
        result.append({
            "Area": label,
            "Answered / available": f'{row["answered"]} / {row["questions"]}',
            "Correct": row["correct"],
            "Incorrect": row["incorrect"],
            "Accuracy": "—" if row["accuracy"] is None else f'{row["accuracy"]:.1f}%',
            "Study signal": "Not sampled" if not row["questions"] else row["status"],
            "Pending review": row["pending_review"],
            "Sets with errors": row["missed_sets"],
        })
    return result


def render_breakdown(report, banks, *, prefix, on_open_question, can_switch, current_set, overall=False):
    """Render counts, then the evidence behind each recommended review topic."""
    st.subheader("Where to focus")
    st.caption("Accuracy uses submitted answers only. Unanswered questions are not counted as mistakes. "
               "Your attempt score stays fixed; successful retries reduce pending review.")
    tabs = st.tabs(["Review priorities", "Domains", "Subsections"])
    with tabs[0]:
        priorities = report["priorities"]
        if not priorities:
            st.info("No review priorities in the available results yet. Keep answering to build evidence across the curriculum.")
        else:
            st.dataframe(pd.DataFrame(table_rows(priorities, "objective")), hide_index=True, width="stretch")
            labels = {row["id"]: objective_label(row["id"]) for row in priorities}
            key = f"{prefix}_priority"
            if st.session_state.get(key) not in labels:
                st.session_state[key] = next(iter(labels))
            selected = st.selectbox("Explore a review subsection", list(labels), format_func=labels.__getitem__, key=key)
            row = next(r for r in priorities if r["id"] == selected)
            st.markdown(f'**{objective_label(selected)}**')
            st.write(f'{row["incorrect"]} incorrect out of {row["answered"]} submitted; '
                     f'{row["pending_review"]} question(s) still awaiting a successful review.')
            if overall:
                st.caption(f'Current-attempt errors occur in {row["missed_sets"]} set(s). '
                           f'{row["wrong_attempts"]} incorrect submission(s) are recorded in the retained history for this topic.')
            questions = {q["id"]: q for bank in banks for q in bank["questions"]}
            qids = row["focus_question_ids"]
            qlabels = {qid: f'Set {int(qid.split("-")[0][4:]):02d} · Question {int(qid.split("-")[1]):03d}' for qid in qids}
            qkey = f"{prefix}_evidence_question"
            if st.session_state.get(qkey) not in qlabels:
                st.session_state[qkey] = qids[0]
            qid = st.selectbox("Related missed question", qids, format_func=qlabels.__getitem__, key=qkey)
            question = questions[qid]
            st.write(question["prompt"])
            target_set = int(qid.split("-")[0][4:])
            st.button("Open question and explanation", key=f"{prefix}_open_question", on_click=on_open_question,
                      args=(target_set, qid), disabled=target_set != current_set and not can_switch)
            st.markdown("**Read before retrying**")
            for ref in question["references"]:
                st.markdown(f'- [{ref["title"]}]({ref["url"]}) — {ref["section"]}')
    with tabs[1]:
        st.dataframe(pd.DataFrame(table_rows(report["domains"], "domain")), hide_index=True, width="stretch")
    with tabs[2]:
        selected_domain = st.selectbox("Subsection domain", [0, *DOMAIN_NAMES],
                                      format_func=lambda d: "All domains" if d == 0 else DOMAIN_NAMES[d], key=f"{prefix}_domain")
        rows = [r for r in report["objectives"] if not selected_domain or r["domain"] == selected_domain]
        st.dataframe(pd.DataFrame(table_rows(rows, "objective")), hide_index=True, width="stretch")
        st.caption("Parent rows include their tagged children. A parent-only question does not establish evidence for each child. "
                   "Questions with several tags contribute once to each related topic, so topic counts must not be added together.")
    with st.expander("How study signals are calculated"):
        st.write("With at least three submitted questions: below 70% is Priority review, 70% to below 85% is Review, "
                 "and 85% or higher is On track. Fewer than three questions is limited evidence. "
                 "An unresolved mistake from a previous attempt remains a Review from history signal even after restarting.")
        st.write("These are study thresholds, not Cisco pass marks or proof of mastery. A question tagged to several "
                 "subsections points to related review areas; it cannot identify which individual skill caused the error. "
                 "Priorities show the most specific available tags, with parent-only mistakes retained separately.")
    export = []
    for level, rows in (("set", report["sets"]), ("domain", report["domains"]), ("objective", report["objectives"])):
        export.extend({"Level": level, **row} for row in table_rows(rows, level))
    st.download_button("Download results breakdown · CSV", pd.DataFrame(export).to_csv(index=False).encode("utf-8-sig"),
                       f'ccna-{"overall" if overall else f"set-{current_set:02d}"}-results.csv', "text/csv", key=f"{prefix}_report_csv")
