# Domain 6 authoring and verification notes

Completed: 90 original questions, CCNA2-091 through CCNA10-100 (10 questions per set). Sources reopened 2026-09-14. Existing Set 01 was read for comparison and was not edited.

## Coverage and format

- Every new set assesses all seven parent objectives, 6.1 through 6.7.
- Lettered objectives 6.3.a and 6.3.b are assessed explicitly across the collection.
- Types: 74 single-answer, 13 select-two, 3 matching. Every matching question has four pairs and uses each term once.
- Difficulty labels: 8 Foundation, 69 Applied, 13 Challenge. These are author judgments, not psychometric measurements.
- Correct single-answer positions: A=19, B=18, C=17, D=20.
- Every question includes scenario-specific explanations for every option and primary-source further-reading references.

## Diversity review

The objective sequence is stable within each domain fragment, but the reasoning cases are individually authored. There is no question template that substitutes device names or parameters to make another set. The 90 prompts and 90 option-text tuples are unique. Similar wording in matching instructions does not indicate a repeated underlying matching task.

- 6.1 varies inventory auditing, configuration drift, partial rollout, compatibility prechecks, recovery, staged rollout, behavior verification, credential authority, and versioned inputs.
- 6.2 varies network-wide policy, a bounded controller outage, automation versus control organization, logical versus physical centralization, application abstraction, aggregated visibility, hardware forwarding versus control location, central monitoring versus distributed routing, and device compatibility.
- 6.3 varies failed underlay reachability, telemetry API relationships, outer-header transit forwarding, intent APIs, encapsulation MTU, shared-underlay dependencies, application authentication failure, control/data/API classification, and cross-overlay connectivity.
- 6.4 varies contextual anomalies, unsupported generated claims, capacity forecasts, fixed rules versus learning, missing telemetry, text generation, changed baselines, correlation versus cause, and model training/evaluation. The initial draft of Set 10’s AI question was replaced because its predictive/generative comparison was too close to Set 01.
- 6.5 covers URI selection, Basic versus TLS, non-idempotent retries, expired versus underprivileged tokens, PUT/PATCH distinctions, asynchronous status, multiple representations, CRUD matching, API-key authority, REST statelessness, DELETE idempotency, Content-Type versus Accept, resource creation with PUT, secret redaction, 204 responses and an explicitly documented JSON Patch contract.
- 6.6 covers inventory groups, providers, observed idempotency, drift, playbooks, desired-state tracking, check-mode limitations, lost state, roles, sensitive state data, multiple group membership, resource dependencies, supported transport, read-only integrations, Vault, on-premises support, information gathering, and unexpected plan replacements.
- 6.7 includes nested members, invalid literals, string/number distinctions, unordered object members, ordered arrays, type matching, null versus omitted/empty, API shape contracts, arrays of objects, trailing commas, quoted Booleans, duplicate names, empty containers, data consistency, structure versus misleading embedded text, native versus stringified arrays, root scalar values and nested route objects.

## Technical and answer review

All answer keys and distractors were reread against the stated conditions. Important precision choices:

- Controller-outage behavior is bounded by explicit retained forwarding entries, unchanged topology/endpoints and matching traffic; it makes no universal outage-survival claim.
- The southbound/northbound distinction follows architectural endpoints, including replies and telemetry, not packet direction or the initiator.
- The transit-router case explicitly excludes tunnel termination and assumes ordinary IP forwarding of the outer packet.
- Shared overlay transport is not claimed to provide physical failure independence or automatic inter-network reachability.
- PATCH questions specify the API-supported partial-update contract. PUT can create when the target is absent and the given contract supports it; method names are not oversimplified into universal one-to-one CRUD rules.
- HTTP idempotency concerns the intended effect, not identical response status codes. POST timeout handling acknowledges uncertain server execution.
- 202 Accepted is distinguished from completed device execution; 204 No Content is intentionally not parsed as a JSON body.
- Ansible idempotency is observed for a specified task, not guaranteed for all tasks. The check-mode scenario specifies module support and absence of task overrides.
- Terraform sensitive output redaction is distinguished from protection of an explicitly present secret in state; newer ephemeral capabilities are not incorrectly excluded.
- JSON syntax, value types and application schema consistency are separate. Duplicate member names are treated as an interoperability problem and an explicit API-contract violation, not falsely labeled universally unparsable JSON.
- The empty VLAN array is explicitly permitted in the question to remove ambiguity.
- The final route-structure prompt was corrected to call nextHop the nested object, while address is its string member.

`python ccna-expansion/audit_domain6.py` passed. It checks all 90 IDs, exact per-set counts, parent and child coverage, schema, selection counts, unique prompts and option tuples, reference fields, and independently parses JSON exhibits and option candidates. It verifies deliberately malformed JSON rejects, corrected JSON parses, duplicate member detection and schema-versus-data mismatches. No network commands or labs were executed.

## Sources opened and used

- [How To Get Started Using LLMs in IT and Network Engineering](https://blogs.cisco.com/developer/how-to-get-started-using-llms-in-it-and-network-engineering) — Introducing the LLM; Applying LLMs to IT and Network Engineering Use Cases
- [What is AIOps?](https://developer.cisco.com/articles/what-is-aiops/) — The core components of AIOps; Is AIOps all you need?
- [Authorization - Meraki Dashboard API v1](https://developer.cisco.com/meraki/api-v1/authorization/) — Admin-scoped access: API keys; Bearer Auth; Security Best Practice
- [What is Terraform?](https://developer.hashicorp.com/terraform/intro) — How does Terraform work?; Manage any infrastructure; Track your infrastructure
- [Manage sensitive data in your configuration](https://developer.hashicorp.com/terraform/language/manage-sensitive-data) — Hide sensitive variables and outputs; state and plan files
- [Providers](https://developer.hashicorp.com/terraform/language/providers) — What Providers Do; Provider Documentation
- [State](https://developer.hashicorp.com/terraform/language/state) — State; mapping configuration to real resources
- [Manage resource drift](https://developer.hashicorp.com/terraform/tutorials/state/resource-drift) — Detect drift; reconcile configuration and changed resources
- [Supervised Learning](https://developers.google.com/machine-learning/intro-to-ml/supervised) — Foundational supervised learning concepts; Training; Evaluating
- [How to build your inventory](https://docs.ansible.com/projects/ansible/latest/inventory_guide/intro_inventory.html) — Inventory basics: formats, hosts, and groups; Inventory setup examples
- [How Network Automation is Different](https://docs.ansible.com/projects/ansible/latest/network/getting_started/network_differences.html) — Execution on the control node; Multiple communication protocols; Collections organized by network platform
- [Validating tasks: check mode and diff mode](https://docs.ansible.com/projects/ansible/latest/playbook_guide/playbooks_checkmode.html) — Using check mode; Using diff mode; Enforcing or preventing check mode on tasks
- [Ansible playbooks](https://docs.ansible.com/projects/ansible/latest/playbook_guide/playbooks_intro.html) — Playbook syntax; Playbook execution; Desired state and idempotency
- [Roles](https://docs.ansible.com/projects/ansible/latest/playbook_guide/playbooks_reuse_roles.html) — Role directory structure; Using roles
- [Protecting sensitive data with Ansible vault](https://docs.ansible.com/projects/ansible/latest/vault_guide/index.html) — Encrypting and managing sensitive data
- [Architectural Styles and the Design of Network-based Software Architectures, Chapter 5: Representational State Transfer](https://ics.uci.edu/~fielding/pubs/dissertation/rest_arch_style.htm) — 5.1.3 Stateless; 5.1.5 Uniform Interface
- [Software-Defined Networking (SDN) Definition](https://www.cisco.com/c/en/us/solutions/software-defined-networking/overview.html) — SDN elements; Features and benefits
- [Software-Defined Access](https://www.cisco.com/c/en/us/td/docs/solutions/CVD/Campus/cisco-sda-design-guide.html) — SD-Access architecture; Underlay network; Overlay network; Overlay control plane – LISP; Data plane – VXLAN
- [Cisco Predictive Networks](https://www.cisco.com/c/m/en_us/solutions/predictive-networks/index.html) — Predictive networks; telemetry and learned patterns
- [What Is Network Automation?](https://www.cisco.com/site/us/en/learn/topics/networking/what-is-network-automation.html) — Network automation; profiles and policies; automated lifecycle management
- [RFC 5789: PATCH Method for HTTP](https://www.rfc-editor.org/rfc/rfc5789.html#section-2) — 2 The PATCH Method
- [RFC 6750: The OAuth 2.0 Authorization Framework: Bearer Token Usage](https://www.rfc-editor.org/rfc/rfc6750.html) — 2 Authenticated Requests; 3 The WWW-Authenticate Response Header Field; 5 Security Considerations
- [RFC 6902: JavaScript Object Notation (JSON) Patch](https://www.rfc-editor.org/rfc/rfc6902.html) — 3 Document Structure; 4 Operations
- [RFC 7426: Software-Defined Networking (SDN): Layers and Architecture Terminology](https://www.rfc-editor.org/rfc/rfc7426.html) — 3.1 Overview; 3.2 Network Devices; 3.3 Control Plane; 3.5.3 Locality
- [RFC 7617: The 'Basic' HTTP Authentication Scheme](https://www.rfc-editor.org/rfc/rfc7617.html) — 2 The Basic Authentication Scheme; 4 Security Considerations
- [RFC 8259: The JavaScript Object Notation (JSON) Data Interchange Format](https://www.rfc-editor.org/rfc/rfc8259.html) — 2 JSON Grammar; 3 Values; 4 Objects; 5 Arrays; 6 Numbers; 7 Strings
- [RFC 9110: HTTP Semantics](https://www.rfc-editor.org/rfc/rfc9110.html) — 9 Methods; 15 Status Codes

## Other opened sources and access outcomes

- [Cisco CCNA 200-301 v1.1 blueprint](https://learningcontent.cisco.com/documents/marketing/exam-topics/200-301-CCNA-v1.1.pdf) — domain weights and exact objective numbering; not used as sole technical evidence.
- [Google: Dividing the original dataset](https://developers.google.com/machine-learning/crash-course/overfitting/dividing-datasets) — opened during ML evaluation review; the more introductory Supervised Learning page is the question reference.
- https://docs.ansible.com/ansible/latest/playbook_guide/playbooks_intro.html and https://docs.ansible.com/ansible/latest/playbook_guide/playbooks_checkmode.html — legacy URLs successfully redirected to the canonical /projects/ansible/ URLs after initial canonical fetches encountered a temporary 429/internal error; the successful canonical pages were read.
- https://developer.hashicorp.com/terraform/language/state/sensitive-data — redirected to /terraform/language/manage-sensitive-data, which is cited.
- https://developer.cisco.com/docs/dna-center/authentication-and-authorization/ — returned 404; not cited and no technical claim relies on it.
- RFC 5789 and all other referenced RFCs were opened at their full root document URLs; section fragments in question references point into those same documents.

## Limits

This is original constructed practice content supported by documentation. It is not recalled Cisco exam content, a reproduction of commercial banks, evidence of Cisco endorsement, or a psychometrically calibrated predictor of exam performance. The domain audit is a content and structure review, with executable verification of JSON cases; it is not independent human SME review or lab validation. All allocated questions are complete; there are no unresolved technical corrections identified in this domain review.
