# V2 release validation

**Version:** 2.0.0 · **Date:** 2026-09-14

The release addresses every confirmed application/content/reference defect in the preceding audit, plus its nine wording/source-fit concerns. No further confirmed failure was found in the checks below. This is evidence of the exercised behavior, not a guarantee against all possible defects.

## Automated acceptance results

| Check | Observed result |
| --- | --- |
| Final regression suite | 242 Python tests passed; 28 JavaScript tests passed. |
| Entire bank | 1,000 questions validated in ten sets of 100; 815 single-answer, 144 multiple-answer and 41 matching questions. |
| Functional exercise | 8,061 recorded AppTest runs covering every question's blank rejection, wrong submission, feedback, references, flags, correct review and correct submission after restart. |
| Exhibits | All 62 table and 131 code exhibits exercised in AppTest. |
| Scoring | 26,289 response combinations checked against the stored keys, with exactly one fully correct response per question. |
| Wrong-answer history | 1,000 wrong → wrong retry → correct retry → wrong retry cycles; original score retained, pending review closes and reopens appropriately. |
| Storage stress | Actual JavaScript bridge: 1,000 incremental history saves and 1,010 fresh-component loads, with ten-set isolation and complete collection snapshot. |
| Backup/restart | 20 full-set backup round trips; ten fresh-session restores and restarts; all 90 wrong-set import combinations rejected. |
| Delayed UI events | 114 regressions: all ten direct set URLs, all 90 directed set transitions, stale practice/review labels and corrected review counts. |
| Backup recovery | 24 restore integration tests, including each set's actual import-form branch, exact acknowledgments, corrupt/incompatible saved data, retries, cancellation after failure, and conflict protection. |
| Collection totals | Ten completed sets, 1,000 submitted, 100% correctness and zero pending after the synthetic full-correct run. |
| Reproducibility | Generated study documents reproduced byte-for-byte; installed dependencies have no conflicts. |

The final standard suite ran with Python 3.12.14, Streamlit 1.55.0 and PyArrow 24.0.0. Runtime requirements pin Streamlit and PyArrow; development requirements pin pytest 9.1.1.

## Live browser checks

Tested the packaged app on an isolated local origin, `http://127.0.0.1:8502`, through a real browser:

- A direct `?set=10` load displayed Set 10 in both the selector and app, with saving acknowledged.
- An incorrect Set 10 answer stayed on its own question and entered review history.
- A correct review retry kept the same question, showed its own feedback, reduced pending review to zero, and retained the incorrect first-answer score.
- Switching Set 10 → Set 01 opened separate, empty Set 01 progress without a bank mismatch or crash.
- Set 01 Question 74, previously observed jumping to Question 01 after submission, retained Question 74 and its correct configuration feedback.
- Refresh retained the saved Set 01 answer and score.
- A real JSON file upload replaced Set 01 with a different validated attempt, including its wrong answer and flag; the browser acknowledged saving, and the restored mistake history remained after refresh.
- The review layout was visually inspected at 1280×720. Dynamic question-heading anchors were removed after observing that Streamlit retained an earlier question's fragment during navigation; the final heading has no misleading anchor.

These checks used synthetic test progress. No deployment or production progress modification was part of V2 implementation.

## Content and references

Exactly 23 questions changed: 14 confirmed content/reference issues and nine wording or source-fit concerns. All 1,000 question IDs, choice IDs, answer keys and matching mappings are preserved. Set 01 remains byte-identical to the supplied source. The affected study guides and reference index were regenerated from the corrected JSON. See [per-question corrections](docs/v2-content-corrections.md).

The source audit checked all 171 original unique URLs; each was reachable through direct retrieval, the web reader or live-browser verification. V2 has 178 unique URLs across 1,282 reference uses. Its ten new exact URL strings were checked against primary-source pages; seven are additions to the distinct inventory after three replaced URLs disappeared. The remaining unchanged URLs reuse that same-day audit evidence. A reachable URL alone does not establish that every sentence is supported; corrected citation locators were reviewed for subject and section fit.

## Evidence and repeatability

The `validation/` directory includes portable exhaustive scripts, recorded JSON evidence and commands. The `tests/` directory contains the standard regression suite, including delayed-event and restore-form tests. See [repeatable validation](validation/README.md).

AppTest runs application and form logic without pixel rendering. Its component acknowledgments are modeled; the actual JavaScript storage implementation is tested separately with simulated `localStorage` and Web Locks. Targeted live checks join those layers in a real browser. Scoring enumeration checks consistency with the key; it does not independently prove the technical truth of every answer.

The release does not claim a 1,000-question pixel-by-pixel inspection, a mobile/cross-browser matrix, production heap/leak profiling, device configuration labs or packet-level validation. Progress persistence is browser-local, and Web Locks are required for serialized multi-tab writes; older browsers retain the documented stale-value check and single-active-tab recommendation. External pages can change after verification.
