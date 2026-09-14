# Version 2.0.0 — 2026-09-14

## Navigation and display

- Keep the active question set separate from its dropdown. Reassert the displayed selection after asynchronous browser loading so a direct Set 10 link cannot show Set 01 or mix progress with another bank.
- Give practice and saved-review question selectors stable labels. Delayed labels from older renders cannot reset the selected question or attach another question's feedback.
- Show answer, flag and review status separately from question selectors.
- Remove automatically generated question-heading anchors, which retained the preceding question's fragment after navigation and did not restore a question when followed.
- Distinguish incorrect first answers from unresolved review history. A successful review clears the pending count without changing the original score.

## Saved progress and recovery

- Stage confirmed backup imports until the browser acknowledges the exact replacement. Keep the current session available for backup while saving is pending or fails.
- Recover unreadable or incompatible saved data through a confirmed, validated backup replacement; resume automatic saving after success.
- Compare replacement against the exact previously observed browser record, serialize writes with Web Locks when available, reject stale/replayed replacements, and verify the written value before acknowledging success.
- Reject inconsistent imports that omit mistake history for an incorrect submission. Genuine V1 exports, including reviewed mistakes from earlier attempts, remain compatible.
- Preserve all ten storage keys, question IDs, answer keys and matching maps. No score migration is required.

## Question content and references

Corrected 23 questions: three confirmed explanation/prompt defects, eleven confirmed reference defects, and nine wording or source-fit concerns. Regenerated the affected study guides and reference index. See [the per-question changes](docs/v2-content-corrections.md).

## Reproducibility

Added asynchronous navigation, restore-form and storage recovery regressions. Pinned PyArrow 24.0.0 alongside Streamlit 1.55.0 to match the tested runtime. See [validation](VALIDATION.md) for observed coverage and limits.
