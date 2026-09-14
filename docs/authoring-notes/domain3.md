# Domain 3 authoring and audit notes

Scope: 175 new original IP Connectivity questions for Sets 02–08, 25 per set. The parent author owns Sets 09–10 separately. Existing Set 01 was read for overlap review and remains unchanged by this author.

## Deliverables

- `domain3-agent-final.json`: author snapshot of the 175 finished records. The parent has subsequently combined these with its own 50 records in `domain3.json` (225 total).
- `author_domain3.py`: literal hand-authored scenarios; helpers only serialize choices, deterministic answer-position shuffling, and matching mappings.
- `audit_domain3.py`: structural checks plus independent ipaddress, arithmetic, wildcard and router-ID comparisons; filters Sets02–08 so it remains usable after parent assembly.

## Results

- 147 single-answer, 21 multiple-answer (each says Select two), 7 matching questions.
- Every set covers parents 3.1, 3.2, 3.3, 3.4 and 3.5. Every lettered child across the allocation is directly represented.
- Every set has at least four constructed exhibits. Additional calculation/configuration scenarios appear in the prompts.
- Difficulty: 136 Applied, 16 Foundation, 23 Challenge.
- Key positions across single and multiple questions: A43, B46, C50, D50. Options are deterministically shuffled without moving their explanations away from their keyed meaning.
- No exact duplicate prompts among these questions or against original Set 01.
- Audit command: `python ccna-expansion/audit_domain3.py` passes.

## Technical audit decisions

- Administrative distance is used for valid candidate installation for an exact prefix; ordinary forwarding selects the longest installed destination match. Cross-protocol metrics are not compared as common units.
- Equal-cost OSPF examples state same intra-area destinations, complete outgoing path costs, and applicable maximum-paths/forwarding conditions. ECMP does not guarantee packet-by-packet or single-flow balance.
- Removed adjacency/network-type objective tags from cost-only questions. Reference-bandwidth mismatch question retains adjacency tag because it explicitly distinguishes metric inconsistency from a Hello-compatibility failure.
- Router-ID cases state process startup, active interface availability, explicit-ID/loopback conditions, or whether a restart occurs. One wildcard exhibit was corrected to nonoverlapping /31 interfaces during audit.
- DR/BDR cases distinguish fresh simultaneous elections, incumbent nonpreemption, BDR succession, vacant backup roles, priority-zero eligibility and point-to-point absence of elected roles.
- IPv6 statics distinguish /0, /64 and /128 scope; link-local next hops include the link context; recursion must reach an independently usable exit and must not self-recurse.
- Floating statics are checked for destination-prefix equality, usable distance below255, next-hop validity, common dependencies, and the actual failure-detection trigger. A remote outage does not inherently withdraw a locally resolved static.
- FHRP protects virtual first-hop ownership; it does not itself supply missing onward routes, rebuild shared access links or replicate every NAT/firewall session. HSRP hold-time timing uses the advertised value and does not promise instantaneous end-to-end recovery.
- Recomputed CIDR boundaries, /23 and /22 alignment, longest-prefix inclusion examples, cost sums/strict thresholds, reference-bandwidth conversion, HSRP decrement, and router-ID numeric ordering with separate assertions.

## Primary sources opened

Blueprint opened: https://learningcontent.cisco.com/documents/marketing/exam-topics/200-301-CCNA-v1.1.pdf

- Configure Route Selection for Routers
  - URL: https://www.cisco.com/c/en/us/support/docs/ip/enhanced-interior-gateway-routing-protocol-eigrp/8651-21.html
  - Supporting concepts: Build the Routing Table; Make Forwarding Decisions
- Understand Administrative Distance
  - URL: https://www.cisco.com/c/en/us/support/docs/ip/border-gateway-protocol-bgp/15986-admin-distance.html
  - Supporting concepts: RIB Route Comparison; Route Installation; Default AD Values
- Local Host Routes Installed in the Routing Table on Cisco IOS and Cisco IOS-XR
  - URL: https://www.cisco.com/c/en/us/support/docs/ip/ip-routing/116264-technote-ios-00.html
  - Supporting concepts: Cisco IOS Local Routes; Manually Configured Host Routes
- RFC 1812: Requirements for IP Version 4 Routers
  - URL: https://www.rfc-editor.org/rfc/rfc1812.html
  - Supporting concepts: 5.2.4 Determining the Next Hop Address
- Configure a Next Hop IP Address for Static Routes
  - URL: https://www.cisco.com/c/en/us/support/docs/dial-access/floating-static-route/118263-technote-nexthop-00.html
  - Supporting concepts: Background Information; Floating Static Route Example
- IPv6 Routing: Static Routing — Cisco IOS XE 17.x
  - URL: https://www.cisco.com/c/en/us/td/docs/routers/ios/config/17-x/ip-routing/b-ip-routing/m_ip6-route-static-xe.html
  - Supporting concepts: Recursive Static Routes; Fully Specified Static Routes; Floating Static Routes
- Configuring OSPF — IP Routing: OSPF Configuration Guide
  - URL: https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/iproute_ospf/configuration/xe-16/iro-xe-16-book/iro-cfg.html
  - Supporting concepts: Enabling OSPF; Configuring OSPF Interface Parameters
- Understand OSPF Neighbor States
  - URL: https://www.cisco.com/c/en/us/support/docs/ip/open-shortest-path-first-ospf/13685-13.html
  - Supporting concepts: OSPF Neighbor States
- Troubleshoot OSPF Neighbor Problems
  - URL: https://www.cisco.com/c/en/us/support/docs/ip/open-shortest-path-first-ospf/13699-29.html
  - Supporting concepts: No State Revealed; Neighbors Stuck in Exstart/Exchange State
- RFC 2328: OSPF Version 2
  - URL: https://www.rfc-editor.org/rfc/rfc2328.html
  - Supporting concepts: 9.4 Electing the Designated Router; 10 The Neighbor Data Structure; 16 Calculation of the routing table
- Understand the Hot Standby Router Protocol Features and Functionality
  - URL: https://www.cisco.com/c/en/us/support/docs/ip/hot-standby-router-protocol-hsrp/9234-hsrpguidetoc.html
  - Supporting concepts: HSRP Background and Operations; HSRP Operation
- Use HSRP Preempt and Track Commands
  - URL: https://www.cisco.com/c/en/us/support/docs/ip/hot-standby-router-protocol-hsrp/13780-6.html
  - Supporting concepts: Preempt and Track Commands
- RFC 9568: Virtual Router Redundancy Protocol (VRRP) Version 3 for IPv4 and IPv6
  - URL: https://www.rfc-editor.org/rfc/rfc9568.html
  - Supporting concepts: 1 Introduction; 2 Required Features; 6 Protocol State Machine
- Default Passive Interfaces — Cisco IOS XE 17.x
  - URL: https://www.cisco.com/c/en/us/td/docs/routers/ios/config/17-x/ip-routing/b-ip-routing/m_iri-default-passive-interface.html
  - Supporting concepts: Information About Default Passive Interfaces

The next-hop static-route URL was initially attempted with an incorrect extra `/ip/` path, then the correct official URL listed above was opened successfully. Source references in the bank use the corrected URL. Official Cisco documents and IETF specifications underpin the protocol concepts; addresses, route tables, failures, wording and distractors are newly constructed. No commercial question bank or recalled exam content was copied.

## Limits

These are original educational scenarios, not device-emulator output or captured production observations. No executable labs were created. Structural and arithmetic checks do not constitute psychometric validation, and the content makes no score guarantee or Cisco endorsement claim. Repeated objectives intentionally use differing evidence and failure conditions; some core principles recur because every set must independently sample the same blueprint.

Similarity audit: sequence comparison across this allocation and original Set01 found no exact duplicates. Highest prompt similarity was 0.732 for CCNA5-061 versus CCNA8-044: the former calculates an ECMP tie and the latter a strictly preferred alternative. The requested outcomes differ intentionally (equality versus crossing the threshold); no nine-set numeric substitution template is used.
