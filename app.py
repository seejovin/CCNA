"""CCNA Practice: original questions and durable, browser-local study history."""
import json
from copy import deepcopy
from uuid import uuid4

import pandas as pd
import streamlit as st

from browser_storage import storage_request_id, sync_storage
from collection_storage import read_collection_progress
from analytics import build_report
from progress_store import empty_progress, record_answer, restart_attempt, restore_progress
from quiz_core import DOMAIN_COUNTS, DOMAIN_NAMES, SET_NUMBERS, document_path, is_correct, load_bank, response_error
from results_ui import render_breakdown, table_rows

st.set_page_config(page_title="CCNA Practice V2 · 10 sets", page_icon="📘", layout="centered")
st.markdown("""<style>
[data-testid="stMainBlockContainer"] {max-width: 960px; padding-top: 5.5rem; padding-bottom: 4rem;}
h1 {letter-spacing: -0.045em; font-weight: 750 !important;}
h2,h3 {letter-spacing: -0.025em;}
[data-testid="stSidebar"] {border-right: 1px solid #e4eaf4;}
[data-testid="stMetric"] {background: #f3f6fb; border-radius: 12px; padding: 14px 18px;}
[data-testid="stForm"] {border-radius: 14px; padding: 1.4rem;}
.eyebrow {font-size: .78rem; line-height: 1.6; letter-spacing: .16em; font-weight: 700; color: #2455d6; margin-bottom: .5rem;}
.footnote {font-size: .8rem; color: #63718a; margin-top: 2rem;}
</style>""", unsafe_allow_html=True)


@st.cache_data
def get_bank(set_number):
    return load_bank(set_number)


def clear_answer_widgets(prefix=""):
    for key in list(st.session_state):
        if key.startswith(tuple(f"{prefix}{kind}_" for kind in ("single", "multi", "match"))):
            del st.session_state[key]


if "active_set" not in st.session_state:
    try:
        selected = int(st.query_params.get("set", "1"))
    except (ValueError, TypeError):
        selected = 1
    st.session_state.active_set = selected if selected in SET_NUMBERS else 1
if "pending_view" in st.session_state:
    st.session_state.view = st.session_state.pop("pending_view")
set_number = st.session_state.active_set
bank = get_bank(set_number)
questions = bank["questions"]
by_id = {q["id"]: q for q in questions}

st.markdown(f'<div class="eyebrow">CCNA 200-301 v1.1 / SET {set_number:02d}</div>', unsafe_allow_html=True)
st.title("Know the network.")
st.write(f"Set {set_number:02d} of 10 · 100 questions per set · 1,000 questions to build understanding.")

# Read first: an empty server session must never overwrite existing browser history.
loaded = st.session_state.get("memory_loaded", False)
save_disabled = st.session_state.get("save_disabled", "")
pending_restore = st.session_state.get("pending_restore")
if pending_restore:
    candidate = pending_restore["progress"]
    replacement_id = pending_restore["replacement_id"]
    event = sync_storage(candidate, bank_id=bank["metadata"]["set_id"],
                         replacement_id=replacement_id,
                         expected_baseline=pending_restore["expected_baseline"])
    expected_request = storage_request_id(candidate, replacement_id=replacement_id)
    if event.get("request_id") == expected_request and event.get("status") == "saved":
        # Only commit the import after this exact replacement is durable.
        st.session_state.progress = candidate
        st.session_state.storage_baseline_id = event["baseline_id"]
        st.session_state.pop("save_disabled", None)
        st.session_state.pop("pending_restore", None)
        clear_answer_widgets()
        clear_answer_widgets("review_")
        st.session_state.review_responses = {}
        for key in ("current", "jump", "review_current", "review_question", "final_answer_id",
                    "pending_question", "switch_backup_confirmed"):
            st.session_state.pop(key, None)
        st.session_state.domain = 0
        st.session_state.view = "Results & downloads"
        st.session_state.restore_notice = True
        st.rerun()
    failed = event.get("status") == "error" and event.get("request_id") == expected_request
    if failed:
        st.error(f'Backup was not restored: {event.get("error", "Browser storage is unavailable.")}')
        st.caption("Your current session is unchanged. If another tab changed this set, cancel and reload before trying again.")
        if st.button("Retry saving this backup"):
            pending_restore["replacement_id"] = uuid4().hex
            st.rerun()
    else:
        st.info("Restoring your backup… Keep this tab open until saving is confirmed.")
    st.download_button("Back up my current session", json.dumps(st.session_state.progress, ensure_ascii=False, indent=2),
                       f"ccna-set-{set_number:02d}-progress.json", "application/json")
    if failed and st.button("Cancel restore"):
        st.session_state.pop("pending_restore", None)
        st.rerun()
    st.stop()

event = sync_storage(st.session_state.progress if loaded and not save_disabled else None, bank_id=bank["metadata"]["set_id"])
if event.get("baseline_id"):
    st.session_state.storage_baseline_id = event["baseline_id"]
if not loaded:
    if event.get("status") not in {"loaded", "error"}:
        st.info("Loading your saved progress…")
        st.stop()
    try:
        if event["status"] == "error":
            raise ValueError(event.get("error", "Browser storage is unavailable."))
        progress = restore_progress(event.get("payload"), bank)
        # Preserve an active attempt when this update reaches an already-open app.
        if event.get("payload") is None and st.session_state.get("submissions"):
            for qid, response in st.session_state.submissions.items():
                if qid in by_id and not response_error(by_id[qid], response):
                    record_answer(progress, by_id[qid], response)
            progress["flags"] = [qid for qid in st.session_state.get("flags", []) if qid in by_id]
    except ValueError as exc:
        progress = empty_progress(bank)
        st.session_state.save_disabled = str(exc)
    st.session_state.progress = progress
    st.session_state.memory_loaded = True
    st.rerun()

progress = st.session_state.progress
submissions = progress["submissions"]
history = progress["wrong_answers"]
flagged_ids = set(progress["flags"])
correct_total = sum(is_correct(by_id[qid], answer) for qid, answer in submissions.items())
save_error = save_disabled or (event.get("error", "Could not save progress.") if event.get("status") == "error" else "")
saved = not save_error and event.get("status") == "saved" and event.get("request_id") == storage_request_id(progress)
for key, initial in {"current": questions[0]["id"], "review_responses": {}}.items():
    if key not in st.session_state:
        st.session_state[key] = initial
if "pending_question" in st.session_state:
    st.session_state.current = st.session_state.pop("pending_question")
    st.session_state.jump = st.session_state.current
    st.session_state.domain = 0
    target = st.session_state.current
    if target not in submissions and target in history:
        st.session_state.view = "Wrong-answer review"
        st.session_state.review_current = target
        st.session_state.review_responses[target] = deepcopy(history[target]["last_response"])


def go(qid):
    st.session_state.current = qid
    st.session_state.jump = qid


def change_set():
    """Only enabled after a save acknowledgement (or an explicit backup notice)."""
    chosen = st.session_state.set_number
    if chosen not in SET_NUMBERS:
        st.session_state.set_number = st.session_state.active_set
        return
    st.session_state.active_set = chosen
    st.query_params["set"] = str(chosen)
    for key in list(st.session_state):
        if key != "active_set":
            del st.session_state[key]


def refresh_overall():
    st.session_state.overall_refresh = uuid4().hex


def view_changed():
    if st.session_state.view == "Overall results":
        refresh_overall()


def show_overall():
    st.session_state.view = "Overall results"
    refresh_overall()


def open_result_question(target_set, qid):
    if target_set != set_number:
        st.session_state.set_number = target_set
        change_set()
    st.session_state.pending_question = qid
    st.session_state.pending_view = "Practice"


def domain_changed():
    domain = st.session_state.domain
    go(next(q["id"] for q in questions if domain == 0 or q["domain"] == domain))


def jump_changed():
    chosen = st.session_state.jump
    if chosen in by_id:
        st.session_state.current = chosen
    else:
        st.session_state.jump = st.session_state.current


def review_changed():
    chosen = st.session_state.review_question
    if chosen in history and chosen in by_id:
        st.session_state.review_current = chosen
    else:
        st.session_state.review_question = st.session_state.get("review_current")


def question_label(qid):
    # Streamlit sends formatted labels over the wire. Keep them stable while
    # answers, flags and review status change; show mutable status separately.
    return f'Question {int(qid.split("-")[-1]):02d}'


def restart():
    restart_attempt(st.session_state.progress)
    clear_answer_widgets()
    clear_answer_widgets("review_")
    st.session_state.review_responses = {}
    st.session_state.pop("final_answer_id", None)
    st.session_state.confirm_reset = False
    st.session_state.domain = 0
    st.session_state.view = "Practice"
    go(questions[0]["id"])


def retry(qid):
    st.session_state.review_responses.pop(qid, None)
    for key in list(st.session_state):
        if key.startswith((f"review_single_{qid}", f"review_multi_{qid}_", f"review_match_{qid}_")):
            del st.session_state[key]


def render_question(q, record, *, review=False):
    """Use the same input validation and explanation UI in practice and review."""
    qid = q["id"]
    locked = record is not None
    prefix = "review_" if review else ""
    st.divider()
    st.caption(f'{DOMAIN_NAMES[q["domain"]].upper()} · {q["difficulty"]} · Objective {", ".join(q["objectives"])}')
    st.subheader(f'Question {int(qid.split("-")[-1]):02d} / 100', anchor=False)
    st.markdown(q["prompt"])
    exhibit = q.get("exhibit")
    if exhibit:
        if exhibit["kind"] == "code":
            st.code(exhibit["content"], language="text", wrap_lines=True)
        elif exhibit["kind"] == "table":
            st.table(pd.DataFrame(exhibit["rows"], columns=exhibit["headers"]))
    diagram = q.get("diagram")
    if diagram:
        graph = ["digraph G {", 'rankdir="TB"; node [shape=box, style=rounded];']
        for node in diagram["nodes"]:
            graph.append(f'{json.dumps(node["id"])} [label={json.dumps(node["label"])}];')
        for edge in diagram["edges"]:
            graph.append(f'{json.dumps(edge["from"])} -> {json.dumps(edge["to"])} [label={json.dumps(edge.get("label", ""))},dir=none];')
        st.graphviz_chart("\n".join(graph + ["}"]))
    choices = {c["id"]: c for c in q["choices"]}
    ids = list(choices)

    def label(cid):
        text = choices[cid]["text"]
        return f"{cid}. Configuration {cid} (shown above)" if "\n" in text else f"{cid}. {text}"

    for choice in q["choices"]:
        if "\n" in choice["text"]:
            st.markdown(f'**Configuration {choice["id"]}**')
            st.code(choice["text"], language="text", wrap_lines=True)
    with st.form(f"{prefix}answer_{qid}", enter_to_submit=False):
        if q["type"] == "single":
            selected = st.radio("Select one answer", ids, index=ids.index(record[0]) if locked else None, format_func=label, key=f"{prefix}single_{qid}", disabled=locked)
            response = [selected] if selected else []
        elif q["type"] == "multiple":
            st.caption(f'Select exactly {len(q["answer"])} answers.')
            response = [cid for cid in ids if st.checkbox(label(cid), value=locked and cid in record, key=f"{prefix}multi_{qid}_{cid}", disabled=locked)]
        else:
            st.caption("Match each row using the dropdowns. Every row must be correct to earn the point.")
            response = {}
            for pair in q["pairs"]:
                response[pair["id"]] = st.selectbox(pair["text"], ids, index=ids.index(record[pair["id"]]) if locked else None, format_func=label, placeholder="Choose a match", key=f'{prefix}match_{qid}_{pair["id"]}', disabled=locked)
        submitted = st.form_submit_button("Submitted" if locked else "Submit answer", type="primary", disabled=locked, width="stretch")
    if submitted:
        error = response_error(q, response)
        if error:
            st.warning(error)
        else:
            record_answer(progress, q, response, review=review)
            if review:
                st.session_state.review_responses[qid] = deepcopy(response)
            elif len(submissions) == len(questions):
                st.session_state.final_answer_id = qid
                st.session_state.pending_view = "Results & downloads"
            st.rerun()
    if not locked:
        st.caption("Submit before moving to another question to save your answer.")
        return
    if is_correct(q, record):
        st.success("Correct · marked reviewed. Your set score is unchanged." if review else "Correct · 1 point")
    else:
        st.error("Incorrect · kept in your review queue. Review the reasoning below." if review else "Incorrect · 0 points — review the reasoning below.")
    if q["type"] == "matching":
        st.markdown("**Correct matches**")
        st.table(pd.DataFrame([{"Item": p["text"], "Your answer": label(record[p["id"]]), "Correct match": label(p["answer"])} for p in q["pairs"]]))
    else:
        st.markdown(f'**Your answer: {", ".join(record)}**')
        st.markdown(f'**Correct answer{ "s" if len(q["answer"]) > 1 else ""}: {", ".join(q["answer"])}**')
    st.markdown(q["explanation"])
    st.markdown("#### Why each option fits—or does not")
    for choice in q["choices"]:
        verdict = "Mapping" if q["type"] == "matching" else ("Correct" if choice["id"] in q["answer"] else "Incorrect")
        if "\n" in choice["text"]:
            st.markdown(f'**Configuration {choice["id"]}** · {verdict}')
            st.code(choice["text"], language="text", wrap_lines=True)
        else:
            st.markdown(f'**{choice["id"]}. {choice["text"]}** · {verdict}')
        st.markdown(choice["explanation"])
    st.markdown("#### Read further")
    for ref in q["references"]:
        st.markdown(f'- [{ref["title"]}]({ref["url"]}) — {ref["section"]}')


with st.sidebar:
    st.markdown("### CCNA Practice")
    st.caption(f"200-301 v1.1 · SET {set_number:02d}")
    allow_unsaved_switch = False
    if save_error:
        allow_unsaved_switch = st.checkbox("I have backed up my unsaved progress before switching sets", key="switch_backup_confirmed")
    # Reassert the canonical value when the widget first appears after the
    # asynchronous storage handshake, so the browser receives set_value too.
    st.session_state.set_number = set_number
    st.selectbox("Question set", SET_NUMBERS, format_func=lambda n: f"Set {n:02d} · 100 questions", key="set_number", on_change=change_set, disabled=not (saved or allow_unsaved_switch))
    st.caption("Each set has its own answers, score and saved review history.")
    st.session_state.view = st.session_state.get("view", "Practice")
    view = st.radio("Workspace", ["Practice", "Wrong-answer review", "Results & downloads", "Overall results"], key="view", on_change=view_changed)
    st.divider()
    st.progress(len(submissions) / 100, text=f"{len(submissions)} of 100 submitted")
    st.caption(f"{correct_total} correct · {len(submissions) - correct_total} incorrect first answers")
    st.caption(f'Pending review: {sum(entry["reviewed_at"] is None for entry in history.values())}')
    st.session_state.domain = st.session_state.get("domain", 0)
    domain = st.selectbox("Domain", [0, *DOMAIN_NAMES], format_func=lambda d: "All domains · 100 questions" if d == 0 else f"{DOMAIN_NAMES[d]} · {DOMAIN_COUNTS[d]}", key="domain", on_change=domain_changed)
    available = [q["id"] for q in questions if domain == 0 or q["domain"] == domain]
    if st.session_state.current not in available:
        go(available[0])
    st.session_state.jump = st.session_state.current
    st.selectbox("Question", available, format_func=question_label, key="jump", on_change=jump_changed)
    current_id = st.session_state.current
    if current_id in submissions:
        st.caption("First answer: correct" if is_correct(by_id[current_id], submissions[current_id]) else "First answer: incorrect")
    if current_id in flagged_ids:
        st.caption("Flagged for review")
    remaining = [qid for qid in available if qid not in submissions]
    st.button("Go to first unanswered", disabled=not remaining, on_click=go, args=(remaining[0] if remaining else available[0],), width="stretch")
    st.divider()
    st.caption("Submit to reveal the reasoning. Your first submitted answer counts until you restart the set.")
    if save_error:
        st.warning(f"Automatic saving is paused. {save_error} Download a backup before reloading or closing this tab.")
    elif saved:
        st.caption("✓ Saved in this browser")
    else:
        st.caption("Saving progress… Please keep this tab open until saved.")
    st.caption("Answers, flags and wrong-answer history survive refreshes in this browser. Use a backup to move to another browser. Clearing site data or using private browsing can remove saved progress.")
    st.download_button("Back up my progress", json.dumps(progress, ensure_ascii=False, indent=2), f"ccna-set-{set_number:02d}-progress.json", "application/json", width="stretch")
    with st.expander("Restart this set"):
        st.caption("Wrong-answer history is kept for future review.")
        confirm = st.checkbox("Clear all answers and flags", key="confirm_reset")
        st.button("Restart", disabled=not confirm, key="restart", on_click=restart)

if view == "Results & downloads":
    st.subheader(f"Set {set_number:02d} results")
    if st.session_state.pop("restore_notice", False):
        st.success("Backup restored and saved in this browser.")
    a, b, c = st.columns(3)
    a.metric("Submitted", f"{len(submissions)} / 100")
    b.metric("Correct", f"{correct_total} / 100")
    c.metric("Accuracy on submitted", f"{correct_total / len(submissions):.0%}" if submissions else "—")
    if len(submissions) == 100:
        st.success(f"Set complete. Your practice score is {correct_total}/100. Use the review list to work through gaps.")
    else:
        st.info("This is an in-progress practice result. Unanswered questions have not been assessed.")
    st.button("See overall results across all sets", on_click=show_overall)
    report = build_report([bank], {bank["metadata"]["set_id"]: progress})
    render_breakdown(report, [bank], prefix="set_results", on_open_question=open_result_question,
                     can_switch=saved or allow_unsaved_switch, current_set=set_number)
    final_id = st.session_state.get("final_answer_id")
    if final_id in submissions:
        with st.expander("Your final answer and explanation"):
            render_question(by_id[final_id], submissions[final_id])
    review = [q for q in questions if q["id"] in submissions and not is_correct(q, submissions[q["id"]])]
    flagged = [q for q in questions if q["id"] in flagged_ids]
    for label, items in [("Incorrect first answers", review), ("Flagged questions", flagged)]:
        with st.expander(f"{label} · {len(items)}", expanded=bool(items)):
            if not items:
                st.caption("Nothing here yet.")
            for q in items:
                st.markdown(f'**Question {int(q["id"].split("-")[-1])}** · {DOMAIN_NAMES[q["domain"]]} · {", ".join(q["objectives"])}')
                st.write(q["prompt"])
    st.subheader("Keep studying")
    st.caption("Use Wrong-answer review for saved mistakes from every attempt. The following study downloads contain answer keys and explanations.")
    a, b = st.columns(2)
    a.download_button("Download question bank · JSON", json.dumps(bank, ensure_ascii=False, indent=2), f"ccna-set-{set_number:02d}.json", "application/json", width="stretch")
    b.download_button("Download study guide · Markdown", document_path(set_number).read_text(encoding="utf-8"), f"ccna-set-{set_number:02d}.md", "text/markdown", width="stretch")
    with st.expander("Restore a progress backup"):
        st.caption(f"Restore a progress JSON file for Set {set_number:02d}. This replaces this set's current attempt and wrong-answer history. Other sets are kept.")
        with st.form("restore_backup"):
            uploaded = st.file_uploader("Progress backup", type=["json"], max_upload_size=1)
            replace = st.checkbox("Replace my current progress with this backup")
            restore_clicked = st.form_submit_button("Restore backup")
        if restore_clicked:
            if not uploaded or not replace:
                st.warning("Choose a backup and confirm replacement first.")
            else:
                try:
                    if uploaded.size > 1_000_000:
                        raise ValueError("The backup must be smaller than 1 MB.")
                    restored = restore_progress(uploaded.getvalue().decode("utf-8"), bank)
                except (ValueError, UnicodeError) as exc:
                    st.error(f"Backup was not restored: {exc}")
                else:
                    baseline = st.session_state.get("storage_baseline_id")
                    if not baseline:
                        st.error("Backup was not restored: browser storage has not been read successfully. Allow browser storage, reload, and try again.")
                    else:
                        st.session_state.pending_restore = {
                            "progress": restored,
                            "replacement_id": uuid4().hex,
                            "expected_baseline": baseline,
                        }
                        st.rerun()
    with st.expander("Curriculum coverage & scoring"):
        st.markdown(document_path(set_number, coverage=True).read_text(encoding="utf-8"))
elif view == "Overall results":
    st.subheader("Overall results · all ten sets")
    st.caption("Combined results use the latest saved attempt in each set, including unfinished attempts. "
               "Wrong-answer history includes earlier attempts. Restarting a set replaces its attempt score; review retries do not rescore it.")
    st.button("Refresh overall results", on_click=refresh_overall)
    if "overall_refresh" not in st.session_state:
        refresh_overall()
    snapshot = read_collection_progress(st.session_state.overall_refresh)
    if snapshot.get("status") != "loaded":
        st.info("Reading saved results from all ten sets…")
    else:
        banks = [get_bank(n) for n in SET_NUMBERS]
        records = snapshot.get("records", {})
        issues = dict(snapshot.get("errors", {}))
        combined = {}
        for other_bank in banks:
            bank_id = other_bank["metadata"]["set_id"]
            if bank_id in issues:
                continue
            if bank_id not in records:
                issues[bank_id] = "No storage result was returned for this set."
                continue
            try:
                combined[bank_id] = restore_progress(records[bank_id], other_bank)
            except ValueError as exc:
                issues[bank_id] = str(exc)
        # Current session is newer than its browser snapshot during an in-flight
        # save. Replacing this one mapping avoids counting it twice.
        combined[bank["metadata"]["set_id"]] = progress
        if issues:
            st.warning("Some saved results could not be read. Affected sets are excluded, except the open set uses its current session. "
                       "Stored data has been left unchanged; this overall report may be incomplete.")
            with st.expander("Unavailable saved results"):
                for bank_id, message in issues.items():
                    st.write(f'Set {bank_id[-2:]}: {message}')
        if not saved:
            st.caption(f"Set {set_number:02d} includes the current session's work while saving is pending or paused.")
        usable_banks = [b for b in banks if b["metadata"]["set_id"] in combined]
        report = build_report(usable_banks, combined)
        totals = report["totals"]
        a, b, c, d = st.columns(4)
        a.metric("Completed sets", f'{totals["completed_sets"]} / 10')
        b.metric("Submitted overall", f'{totals["answered"]} / 1,000')
        c.metric("Accuracy overall", "—" if totals["accuracy"] is None else f'{totals["accuracy"]:.1f}%')
        d.metric("Pending review", totals["pending_review"])
        st.write(f'{totals["correct"]} correct · {totals["incorrect"]} incorrect · '
                 f'{len(usable_banks)} of 10 sets available for this report.')
        st.dataframe(pd.DataFrame(table_rows(report["sets"], "set")), hide_index=True, width="stretch")
        render_breakdown(report, usable_banks, prefix="overall_results", on_open_question=open_result_question,
                         can_switch=saved or allow_unsaved_switch, current_set=set_number, overall=True)
elif view == "Wrong-answer review":
    st.subheader("Your saved wrong answers")
    pending = sum(entry["reviewed_at"] is None for entry in history.values())
    a, b = st.columns(2)
    a.metric("Questions in history", len(history))
    b.metric("Still to review", pending)
    st.caption("History is kept across attempts. A correct retry marks the question reviewed; your original set score stays the same.")
    review_ids = [qid for qid in available if qid in history]
    if not review_ids:
        st.info("No saved wrong answers in this domain yet. Incorrect submissions will appear here automatically.")
    else:
        if st.session_state.get("review_current") not in review_ids:
            st.session_state.review_current = review_ids[0]
        st.session_state.review_question = st.session_state.review_current
        qid = st.selectbox("Saved question", review_ids, format_func=question_label, key="review_question", on_change=review_changed)
        entry = history[qid]
        q = by_id[qid]
        st.caption(f'{"To review" if entry["reviewed_at"] is None else "Reviewed"} · Missed {entry["wrong_count"]} time(s)')
        st.caption(f'Last incorrect attempt: {entry["last_wrong_at"].replace("T", " ")}')
        with st.expander("My last wrong answer"):
            texts = {c["id"]: c["text"] for c in q["choices"]}
            if q["type"] == "matching":
                st.table(pd.DataFrame([{"Item": p["text"], "Selected answer": texts[entry["last_response"][p["id"]]]} for p in q["pairs"]]))
            else:
                for cid in entry["last_response"]:
                    st.write(f"{cid}. {texts[cid]}")
        render_question(q, st.session_state.review_responses.get(qid), review=True)
        if qid in st.session_state.review_responses:
            st.button("Retry this question", on_click=retry, args=(qid,))
else:
    qid = st.session_state.current
    render_question(by_id[qid], submissions.get(qid))
    index = available.index(qid)
    st.divider()
    a, b, c = st.columns(3)
    a.button("← Previous", disabled=index == 0, on_click=go, args=(available[max(0, index - 1)],), width="stretch")
    if b.button("Unflag" if qid in flagged_ids else "Flag for review", width="stretch"):
        if qid in flagged_ids:
            progress["flags"].remove(qid)
        else:
            progress["flags"].append(qid)
        st.rerun()
    c.button("Next →", disabled=index == len(available) - 1, on_click=go, args=(available[min(len(available) - 1, index + 1)],), width="stretch")

st.markdown('<div class="footnote">Original practice material · No interactive labs in this set · One point per fully correct response. Practice scores do not reproduce Cisco exam scoring or predict an exam result.</div>', unsafe_allow_html=True)
