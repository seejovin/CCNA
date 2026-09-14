# Results and subsection analysis

The app now automatically opens the selected set's results after the 100th submitted answer. The final question's answer and explanation remain accessible from that report. The separate Overall results workspace combines the latest saved attempts in all ten sets and their retained wrong-answer histories.

## Data and scoring

- `data/objectives.json` gives names to all 53 parent objectives and 58 lettered subsections, verified against the linked Cisco v1.1 blueprint. No question bank was changed.
- `analytics.py` calculates unique-question overall scores, per-set scores, domains and objective evidence. A parent and child tag on one question do not count twice in that parent. Parent-only tags do not manufacture child-level evidence.
- Accuracy excludes unanswered questions. The all-or-nothing multiple-answer and matching rules remain unchanged. Overall accuracy is weighted by submitted question counts, not the average of individual set percentages.
- First-submission errors and retained mistakes are separate. A successful retry changes review status, not the original score. Restarting replaces the current attempt while retaining its mistake history. The existing schema does not archive every completed test score.
- Priorities show the most specific available tags, while keeping parent-only misses visible. Full objective metrics and the particular questions responsible for each priority are available together. Multi-topic items identify related study areas rather than diagnosing an isolated skill failure.

## Study signals

| Submitted questions | Accuracy or condition | Signal |
| --- | --- | --- |
| 0 | Unresolved historical mistake | Review from history |
| 0 | No unresolved historical mistake | Not assessed |
| 1–2 | At least one current mistake | Review · limited evidence |
| 1–2 | No current mistakes | Limited evidence |
| 3 or more | Below 70% | Priority review |
| 3 or more | 70% to below 85% | Review |
| 3 or more | At least 85% | On track |

An objective with no questions in the selected scope is shown as Not sampled. Pending historical review remains a separate count even when the current attempt's accuracy is high. These thresholds are study heuristics, not Cisco pass marks, human SME judgments, or statistically calibrated mastery measures.

## Browser storage

`collection_storage.py` and `collection_storage.js` provide a read-only snapshot of the ten existing keys. Reads do not alter progress, other sets, or the active write bridge's conflict baseline. Each refresh/session has its own request identity; stale events are ignored. A bad or inaccessible record does not prevent good records from being read, and every record is validated against its question bank before analysis.

The active set's session replaces its snapshot entry once, so a pending save neither omits nor double-counts a submission. Missing records mean unstarted sets; unreadable records produce a visible warning and are excluded. If the open set has a storage problem, its available session can still be reported with that limitation shown. Snapshots are refreshed on entering Overall results or pressing Refresh; the ten reads are not an atomic transaction across simultaneous writes by other tabs.

## Validation

77 Python tests and 18 Node tests passed. Coverage includes weighted scores, thresholds and limited samples, objective parent/child attribution, multiple/matching scoring, cross-set recurrence, final-submission navigation and final-answer visibility, unopened saved sets, cross-set question links, history after restart, successful review without rescoring, pending reads, unsaved active work, corrupted records, refresh behavior, read-only snapshots, stale request handling, and the existing save bridge's conflict and quota handling.

Streamlit AppTest exercises actual Python UI behavior with simulated browser acknowledgements. Node tests exercise the JavaScript bridges with simulated localStorage. This is not a claim of full browser end-to-end testing or learner outcome validation.
