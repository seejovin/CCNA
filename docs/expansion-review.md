# Sets 02–10: authoring and review record

Scope: 900 additional original questions for CCNA 200-301 v1.1, combined with the unchanged 100-question Set 01. The requested per-set allocation is 20 / 20 / 25 / 10 / 15 / 10. This is a non-lab study collection, including single-answer, multiple-answer, matching, and written CLI/table exhibits.

## Content method

Domain authors used the v1.1 blueprint to assign relevant objectives, consulted primary Cisco, IETF and product documentation, wrote new cases and option explanations, and reviewed their keys. Existing questions were inspected to avoid direct reuse. Cases vary evidence, fault conditions, constraints and decisions; repeated curriculum objectives are intentional. The new sets were not created by shuffling the original 100 questions or simply substituting addresses into one common exam template.

Each set assesses all 53 top-level objectives. Lettered subtopics rotate through the sets; coverage tags indicate what a question assesses, not that every practical variation of an objective has been demonstrated. See the individual coverage guides and the collection matrix for the actual assignments.

The answer positions are varied deterministically during authoring, with keys and matching mappings changed together. Difficulty is an author estimate. There is no commercial exam-dump source or claim that these are recalled Cisco questions.

## Corrections and checks

- Corrected an inter-VLAN troubleshooting exhibit whose initial addresses did not support the claimed wrong-mask behavior; made proxy ARP assumptions explicit.
- Corrected the wireless rate-limiting case to use upstream traffic on one AP radio, matching the documented scope of the configured limits.
- Replaced abbreviated `::1` references with the full intended IPv6 server address to avoid confusing it with loopback.
- Changed an FHRP maintenance question to distinguish keeping gateway service from retaining tolerance to another gateway failure during maintenance.
- Corrected cost-only OSPF tags to the parent objective instead of the neighbor-adjacency child.
- Added feature-specific DAI and port-security reading references to a matching item initially citing only DHCP snooping.
- Clarified ACL ingress direction and server destination ports so packet-filtering questions specify the intended traffic unambiguously.
- Clarified an empty-JSON-array question and a nested-object question; replaced one repetitive AI question with a distinct model-evaluation case.
- Recalculated addressing, wildcard, IPv6 and route-cost cases with independent checks. Static routes, candidate selection, installed prefixes and forwarding decisions are distinguished explicitly.
- Screened the collection for exact item reuse and high textual similarity, followed by content review. Similarity screening is a review aid and cannot establish semantic uniqueness or technical correctness.

Domain author notes are in `docs/authoring-notes`. Additional independent reviews focused on the final 50 IP Connectivity questions, Network Access protocol/configuration cases, Network Fundamentals numerical/addressing cases, and all 27 new ACL questions. The application changes also received a separate state-isolation review.

## App and storage behavior

Each set loads its own JSON bank and uses separate question IDs, browser storage, attempt score, flags and wrong-answer history. The original Set 01 data file and browser storage key are retained. An already-open Set 01 session keeps its established storage baseline during the upgrade. Switching waits for a save acknowledgement; a storage error requires the user to acknowledge backing up unsaved work before switching.

Saved progress is browser-local at the same app origin. It is not account-based cloud synchronization. Each backup belongs to one set, and importing it into another set is rejected. Restarting an attempt keeps that set’s wrong-answer history. A correct review retry does not change the initial attempt score.

## Validation limits

Automated checks enforce counts, IDs, tags, keys, response validation, set isolation, storage failure handling, and the original Set 01 file hash. AppTest runs the actual Streamlit UI logic with simulated browser acknowledgements; Node tests exercise the storage bridge against simulated local storage and write locks. These tests do not prove the technical truth or measured difficulty of each question. CLI exhibits are authored scenarios, not output from executed device labs. The collection has not been statistically calibrated against learner performance or Cisco exam results.

## Release checks

- 1,000 questions: ten sets of 100, each with the requested 20 / 20 / 25 / 10 / 15 / 10 split.
- All 53 top-level objectives are tagged in every set; every lettered objective is tagged somewhere in the collection.
- 48 Python tests and 10 Node storage-bridge tests passed.
- The original Set 01 bank retains SHA-256 `c0d9ce89219f4ddd788452560c56438ed3829ec7b26b0ad05178ea93237d4b7d`.
- The collection-wide lexical screen normalized numeric values and IP addresses and found no prompt pair above the configured 0.70 TF-IDF threshold within the same domain. This does not mean the same curriculum principle never recurs.
