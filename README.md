# CCNA Practice V2 · 10 sets

A Streamlit study app with **1,000 original CCNA 200-301 v1.1 questions in ten sets of 100**, option-by-option explanations and primary-source reading references. The existing Set 01 question bank is preserved unchanged.

**Version 2.0.0.** This release corrects delayed-loading navigation, backup recovery, review-count labels, and 23 questions or reference locators. See [changes](CHANGELOG.md), [validation evidence](VALIDATION.md), and [question corrections](docs/v2-content-corrections.md).

Every set follows this allocation:

| Domain | Questions per set |
| --- | ---: |
| Network Fundamentals | 20 |
| Network Access | 20 |
| IP Connectivity | 25 |
| IP Services | 10 |
| Security Fundamentals | 15 |
| Automation and Programmability | 10 |

## Study experience

- Select **Set 01–10** in the sidebar. Each set has independent answers, flags, score and saved wrong-answer history.
- Select an answer and submit to reveal the correct answer, reasoning and explanations for every option.
- Single-answer, select-multiple and dropdown matching questions, including configuration and table exhibits.
- Navigate by domain or question, flag questions and review domain results.
- The final submission opens the set results automatically, with domain and named curriculum-subsection breakdowns and a link to the final answer explanation.
- **Overall results** combines the latest saved attempt in all ten sets and identifies recurring subsection errors, including saved sets you have not opened in the current session.
- Review priorities link to the supporting missed questions and their further-reading resources. Export either report as CSV.
- Download the full JSON bank and Markdown study guide from **Results & downloads**.
- Answers, flags and wrong-answer history save automatically in the same browser. The sidebar confirms when saving is complete.
- **Wrong-answer review** keeps the last incorrect response, number of incorrect attempts and review status for each missed question. Retry with full explanations and references; a correct retry marks it reviewed without changing the first-attempt score.
- **Restart this set** clears the current attempt and flags while keeping wrong-answer history.
- **Back up my progress** exports a portable JSON file. Restore it under **Results & downloads → Restore a progress backup**.

There are no interactive labs in this release. Each fully correct response earns one point, including multiple-answer and matching questions; there is no partial credit. This is a study score, not Cisco's scoring model or a prediction of an exam result.

## Results and review priorities

**Results & downloads** shows the selected set's score, six domain summaries, and all 111 named curriculum entries: 53 parent objectives plus 58 lettered subsections. **Overall results** uses the same breakdown across all ten sets. Both views show submitted questions, correct and incorrect answers, accuracy, available question coverage, and unresolved review history. A topic with no submitted answers is not treated as a weakness; a topic absent from a set is marked Not sampled.

With at least three submitted questions in an area, accuracy below 70% is **Priority review**, 70% to below 85% is **Review**, and 85% or higher is **On track**. Smaller samples carry a limited-evidence label. These are transparent study heuristics, not Cisco cutoffs or measured mastery. Questions with several tags contribute once to each relevant topic; one failed question cannot isolate which of those skills caused the error. Parent rows include tagged children without inventing evidence for untagged children.

Overall accuracy divides the total correct answers by total submitted answers, rather than averaging set percentages. Each set contributes its latest saved attempt, including partial attempts; this is not a chronological archive of every completed test. Restarting a set clears its current score while retaining mistakes, and unresolved historical mistakes remain actionable. Review retries can clear pending-review status without changing first-submission scores.

The overall view reads the existing browser records without writing to other sets. The active set uses its current session so an in-flight save cannot omit the latest response. Use **Refresh overall results** after work in another tab. Invalid saved records are preserved and excluded with a visible incomplete-report warning; they are never silently treated as empty results. See [results implementation and validation](docs/results-review.md).

## Saved progress

Progress is stored in a separate `localStorage` key per set under this app's origin, separate from Streamlit's temporary server session. It survives browser refreshes, closing and reopening the app, and app server restarts. Each browser profile has its own history; there is no account login or automatic cross-device synchronization. People sharing a browser profile share its saved progress. Clearing site data or private browsing can remove it, so keep a backup when moving browsers or devices.

Set 01 retains its original storage key, so existing saved progress remains available at the same app URL. The selected set is recorded in the `?set=` URL parameter; refreshing a set link opens that set. Switches wait for the current save to be acknowledged.

The app loads and validates saved data before enabling writes. It confirms a save only after browser acknowledgement. If storage is blocked/full, existing data is incompatible, or another tab has saved newer work, the app shows a warning and keeps the current session available for backup. Reload to read the latest saved state. Use one active tab for studying; browsers supporting Web Locks serialize writes, while older browsers use a stale-value check.

The review history stores one latest incorrect response per question plus an aggregate incorrect count and review timestamp. It is not a full chronological log of every attempt. Backup imports replace the current saved state only after explicit confirmation, schema validation, and acknowledgment of that exact replacement from the browser. This also recovers from unreadable or incompatible saved data when browser storage is accessible. If another tab changes the stored record during restoration, replacement is rejected. Incomplete backups that contain an incorrect submission without its mistake history are rejected. No answer history is committed to this repository or stored in a shared server file.

## Deploy to Streamlit Community Cloud

The repository contains everything the app needs, including all ten banks and their study guides. No secrets, paid APIs or external database are required.

1. Open your [Streamlit workspace](https://share.streamlit.io/user/seejovin), sign in and choose **Create app**.
2. Choose an existing GitHub app/repository and use these settings:

   | Setting | Value |
   | --- | --- |
   | Repository | `seejovin/CCNA` |
   | Branch | `main` |
   | Main file path | `app.py` |
   | Python version | `3.12` |

3. Choose **Deploy**. Streamlit installs `requirements.txt` and starts the app.

See the [official Streamlit deployment instructions](https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app/deploy) if the interface differs. Later pushes to this branch update the deployed app.

## Run locally

Use Python 3.12:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m streamlit run app.py
```

On Windows, activate with `.venv\Scripts\activate` instead.

## Content and maintenance

`data/questions.json` is the unchanged Set 01 bank. `data/sets/set-02.json` through `set-10.json` contain the additional sets. Each question records its set-specific ID, domain, objective tags, type, estimated difficulty, choices, key, explanations and references.

- [All ten study guides and set coverage](docs/collection.md)
- [Coverage across all sets](docs/objective-matrix.md)
- [Primary references](docs/references.md)
- [Expansion review](docs/expansion-review.md)
- [Set 01 study guide with answers](docs/question-bank.md)
- [Objective coverage and scoring](docs/coverage.md)
- [Review notes](docs/review-notes.md)
- [Cisco v1.1 exam blueprint](https://learningcontent.cisco.com/documents/marketing/exam-topics/200-301-CCNA-v1.1.pdf)

These questions were authored for this project. They are not official Cisco questions or recalled exam content. References support the technical concepts; Cisco has not endorsed or validated this bank. Difficulty labels are author estimates, and the collection has not been calibrated using learner performance.

After editing the bank, regenerate exports and run the tests:

```bash
python -m pip install -r requirements-dev.txt
python scripts/build_docs.py
python -m pytest -q
node --test tests/test_browser_storage.mjs tests/test_collection_storage.mjs
```

The tests check all ten 100-question allocations, objective tags, unchanged Set 01 bytes, scoring, forms and explanations, navigation, separate saved state for each set, restoration into a fresh app session, retention after restart, review without score changes, and blocked or conflicting browser writes. V2 also tests delayed initial loads for every set, all 90 directed set switches, stale selector events, and confirmed backup recovery for all ten sets. AppTest models browser acknowledgements; Node tests exercise the actual storage component with a simulated browser store. Node is only required for the JavaScript tests, not deployment. Technical correctness also needs content review against the cited sources.

## Updating an existing local copy

Back up study progress from the current app, then replace the project files with this V2 package, including `data/sets` and `docs/sets`. Keep any private deployment settings. Run `python -m pip install -r requirements.txt` to match the tested Streamlit 1.55.0 and PyArrow 24.0.0 versions, then `python -m streamlit run app.py`. PyArrow was already a Streamlit dependency; V2 pins the tested version rather than allowing dependency drift.

All ten sets retain their existing browser storage keys and backup schema. At the same app origin, existing history remains available without migration. A different host, port or app URL has a separate browser store; use progress backups to transfer it. A backup from one set must be restored while that same set is selected; imports for another set are rejected. A corrected explanation does not rescore an existing attempt; all answer keys are unchanged.
