# Reproduce the full question-bank checks

Run these commands from the CCNA-V2 directory using Python 3.12 and Node.js. Install the development dependencies first, preferably in a virtual environment:

```sh
python -m pip install -r requirements-dev.txt
python -m pytest -q
node --test tests/*.mjs
python validation/exhaustive_core.py
node validation/exhaustive_storage.mjs
python validation/exhaustive_functional.py
```

Run the core script before the storage script: it generates the synthetic progress fixture consumed by JavaScript. Each script resolves the application relative to its own location, so it also works when called by absolute path from another directory. Fresh results and fixtures go into `validation/generated/`; the recorded evidence is kept separately and is never overwritten by these commands.

The full functional run normally takes several minutes. Its optional integer argument limits the run to the first N sets for debugging, for example `python validation/exhaustive_functional.py 1`. Omit the argument to cover all 1,000 questions. Any failed assertion produces a nonzero exit status; the functional script also records the failure in its result JSON.

## Recorded coverage

The `evidence/` directory contains these observed results from the V2 verification:

| Evidence | Scope |
| --- | --- |
| `functional-results.json` | All 1,000 questions; 8,061 recorded AppTest runs; blank, wrong and correct submissions; explanation/reference emission; 62 table and 131 code exhibits; flags, review history, restart, fresh-session restore, backup validation and overall totals. |
| `core-results.json` | 26,289 possible response combinations across all 1,000 questions, plus wrong → wrong retry → correct retry → wrong retry history cycles. Includes each question's coverage. |
| `storage-results.json` | Actual JavaScript storage code with 1,000 incremental saves, 1,010 fresh-component loads, ten-set isolation and the complete collection snapshot. |
| `async-results.json` | A compact extract of the observed JUnit results: all 114 tests in `tests/test_v2_async.py` passed, covering ten direct set URLs, all 90 directed set transitions, stale question-selector events and pending-review labels. |

All three packaged harnesses were executed successfully. The final packaged functional harness completed all 1,000 questions and 8,061 recorded app runs after the last application edit; its recorded results are included here. The packaged core and JavaScript results matched their earlier observed evidence. Additional files record the final 242 Python/28 JavaScript regression results, content validation, and targeted live-browser observations.

## What these checks establish

The recorded full AppTest and async runs used Streamlit 1.55.0 and PyArrow 24.0.0. AppTest executes the application and Streamlit's form/render logic without a pixel-rendered browser. The full functional harness models synchronous browser acknowledgments. The 114 async regressions run the actual Python bridge and defer its modeled component events across separate app runs; they inspect the selector values emitted to the frontend, including the failure paths missed by synchronous testing.

The JavaScript harness executes the actual storage modules under Node.js with an in-memory `localStorage`. The standard JavaScript suite separately tests errors, conflicts and confirmed replacement. These are simulations of browser storage, not access to a learner's saved data or a deployed site. The scripts do not open the live site or modify real browser progress.

Grader enumeration proves consistency with the stored answer keys, not the independent technical truth of every key. Reference emission checks prove that the expected URLs appear in the rendered output; they do not fetch or revalidate external pages. These scripts do not measure responsive pixel layout, production latency, browser heap leaks or cross-device behavior. Refer to the root validation report for the broader release checks.
