# Domain 2 authoring and audit notes

Status: 180 original Network Access questions for Sets 02–10, 20 per set. The existing Set 01 file was read but not modified. Final IDs span CCNA2-021 through CCNA10-040 in their respective sets.

## Coverage and format

Every set covers all nine parent objectives 2.1–2.9. Across the nine sets, all lettered children are assessed: 2.1.a/b/c, 2.2.a/b/c, and 2.5.a/b/c/d. Each set contains 16 single-answer questions, 3 select-two questions, and 1 matching question. Totals: 144 single, 27 multiple, 9 matching. Difficulty totals: 148 Applied, 24 Challenge, 8 Foundation. There are 49 constructed code/table exhibits after the final Set 08 hash-input exhibit was added; each fragment has at least four.

Questions are hand-written literal records in `author_domain2.py`. The helper assigns IDs and deterministically shuffles options; it does not generate scenario permutations. It writes the flat `domain2.json` array. All exhibits are constructed teaching cases, not captured device output or executed lab measurements.

## Source and scope decisions

The Cisco 200-301 v1.1 blueprint was opened and used for numbering and scope:
https://learningcontent.cisco.com/documents/marketing/exam-topics/200-301-CCNA-v1.1.pdf

Catalyst switching assumptions follow the referenced IOS XE guides. Wireless questions name AireOS or Catalyst 9800 when GUI behavior differs. Legacy rogue detector and SE-Connect questions explicitly require a supporting AP model. AireOS 5520 static LAG is distinguished from negotiated LACP; this is not asserted for every wireless-controller platform. Cloud architecture questions specify local bridge-mode forwarding and relevant authentication assumptions.

Thirty technical primary-source pages used in the final material were opened during this authoring task or independently verified by the reviewer. Their actual URLs appear below. Older dead guessed inter-VLAN URL 41860-howto-L3-intervlanrouting.html was rejected and replaced with the working Cisco document 41260-189.html. No dead URL was retained in final references. SVI autostate uses the dedicated Interface Characteristics guide rather than the general inter-VLAN guide.

## Reasoning audit

- VLAN membership, VLAN existence, native classification, admitted trunk lists, and SVI routing are tested separately. Native-VLAN questions distinguish ordinary user data from Cisco control traffic and explicitly name tagging behavior where needed.
- CCNA3-021 was tightened so the access switch is Layer 2 only and the voice VLAN gateway lies beyond the affected uplinks. This makes VLAN carriage across those uplinks necessary.
- CCNA3-022 now describes administrative enable and line protocol down without assuming a platform-specific status rendering. Default autostate with no override is explicit, and the source covers the required active forwarding attachment.
- CCNA7-023 was corrected to A=10.10.10.10/24 and B=10.10.20.20 with an erroneous /16 instead of its intended /24. Proxy ARP is explicitly disabled. Python ipaddress independently confirmed that A lies inside B's erroneous /16 and outside B's proper /24.
- STP checks include total path costs, sender bridge ID before sender port ID before receiver port ID, extended system-ID arithmetic, one root per connected instance, per-VLAN root placement, role versus state, normal alternate blocking, and shared-segment backup roles. The 12+4 versus 0+19 comparison and priority additions were recalculated.
- PortFast alone is not BPDU guard or unconditional filtering. Global PortFast-dependent defaults are explicitly distinguished from interface-level enable. Root guard reacts to superior BPDUs; loop guard reacts to disappearance of expected BPDUs. Root/loop inconsistent states are not described as identical to error-disable. Their automatic recovery and mutual exclusion are stated in the relevant cases.
- LACP questions separate local channel-group numbering, protocol compatibility, logical routed addressing, member compatibility, standby flags, total capacity, and stable-flow hashing. No item promises a single flow the full aggregate rate, equal byte distribution, zero loss on failure, or chassis independence from multiple cables.
- Wireless verification follows the actual AP/client/controller forwarding path and policy bindings, including AP groups, 9800 policy tags and profiles, Flex native-VLAN mapping, SSID versus profile name, WPA2 key-management methods, WMM admission, session timers, peer actions, and QoS limits. Captures, RF analysis, client service, and mesh roles are distinct.
- CCNA10-040 replaced an initially repeated Bronze/P2P setting combination with a new per-client versus per-SSID sustained-rate interpretation. Independent arithmetic gives per-client upstream ceiling 2,000 Kb/s and per-SSID upstream ceiling on the same AP radio min(5×2,000, 8,000)=8,000 Kb/s; the question does not claim equal allocation or measured throughput.
- Answer positions after stable option shuffling are A=38, B=34, C=33, D=39 for single-answer items. Matching maps were remapped alongside option IDs, so no key depends on the unshuffled order.

## Validation and limitations

A local validator checked 180 unique IDs, exact 20-question fragments, all parent objectives per fragment, all 10 lettered children across the collection, unique prompts and choices, valid keyed options, exact select-two wording/cardinality, complete pair mappings, nonempty per-option explanations, and HTTPS technical references. Normalized prompt similarity flagged one pair at 0.649 similarity: CCNA4-025 trunk-setting matching versus CCNA3-037 management-method matching. Their matching instruction phrasing overlaps but their assessed concepts and options are distinct. The one shared bare option vocabulary (AP mode names) between a single item and a matching item was expanded with role descriptors in the matching item, leaving no unchanged complete option sets across the new collection and Set 01. Independent subject-matter review by the automation-domain author checked all 180 records. The final rate-limit question was tightened to five clients on the same AP radio, with all limits and offered traffic explicitly upstream, because the source describes per-WLAN limits per AP/radio rather than a controller-wide SSID cap. No remaining key defects were reported.

This is authored practice material, not recalled exam questions or a psychometrically calibrated mock examination. No labs were executed. Correct configuration interpretation is not itself measured production capability. Coverage tags document assessed concepts rather than guaranteeing every real-exam variation is represented.

## Technical pages opened and used

- Meraki Cloud Architecture
  - https://documentation.meraki.com/Platform_Management/Dashboard_Administration/Design_and_Configure/Architectures_and_Best_Practices/Cisco_Meraki_Best_Practice_Design/Meraki_Cloud_Architecture
- Configure Inter VLAN Routing with the Use of an External Router
  - https://www.cisco.com/c/en/us/support/docs/lan-switching/inter-vlan-routing/14976-50.html
- Configure Inter-VLAN Routing with Catalyst Switches
  - https://www.cisco.com/c/en/us/support/docs/lan-switching/inter-vlan-routing/41260-189.html
- Understand STP Loop Guard and UDLD Features
  - https://www.cisco.com/c/en/us/support/docs/lan-switching/spanning-tree-protocol-stp-8021d/218321-configure-stp-with-loop-guard-and-bpdu-s.html
- Enhance STP with Root Guard
  - https://www.cisco.com/c/en/us/support/docs/lan-switching/spanning-tree-protocol/10588-74.html
- Understand Rapid Spanning Tree Protocol (802.1w)
  - https://www.cisco.com/c/en/us/support/docs/lan-switching/spanning-tree-protocol/24062-146.html
- Configure FlexConnect with Authentication on Catalyst 9800 WLC
  - https://www.cisco.com/c/en/us/support/docs/wireless/catalyst-9800-series-wireless-controllers/213921-flexconnect-configuration-with-central-a.html
- Interface and Hardware Components Configuration Guide, Cisco IOS XE 17.15.x — Configuring Interface Characteristics
  - https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst9300/software/release/17-15/configuration_guide/int_hw/b_1715_int_and_hw_9300_cg/configuring_interface_characteristics.html
- Interface and Hardware Components Configuration Guide, Cisco IOS XE 17.15.x — Configuring LLDP, LLDP-MED, and Wired Location Service
  - https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst9300/software/release/17-15/configuration_guide/int_hw/b_1715_int_and_hw_9300_cg/configuring_lldp__lldp_med__and_wired_location_service.html
- Layer 2 Configuration Guide, Cisco IOS XE 17.15.x — Configuring EtherChannels
  - https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst9300/software/release/17-15/configuration_guide/lyr2/b_1715_lyr2_9300_cg/configuring_etherchannels.html
- Layer 2 Configuration Guide, Cisco IOS XE 17.15.x — Configuring Optional Spanning-Tree Features
  - https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst9300/software/release/17-15/configuration_guide/lyr2/b_1715_lyr2_9300_cg/configuring_optional_spanning_tree_features.html
- Layer 2 Configuration Guide, Cisco IOS XE 17.15.x — Configuring Spanning Tree Protocol
  - https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst9300/software/release/17-15/configuration_guide/lyr2/b_1715_lyr2_9300_cg/configuring_spanning_tree_protocol.html
- Network Management Configuration Guide, Cisco IOS XE 17.15.x — Configuring Cisco Discovery Protocol
  - https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst9300/software/release/17-15/configuration_guide/nmgmt/b_1715_nmgmt_9300_cg/configuring_the_cisco_discovery_protocol.html
- VLAN Configuration Guide, Cisco IOS XE 17.15.x — Configuring VLAN Trunks
  - https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst9300/software/release/17-15/configuration_guide/vlan/b_1715_vlan_9300_cg/configuring_vlan_trunks.html
- VLAN Configuration Guide, Cisco IOS XE 17.15.x — Configuring VLANs
  - https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst9300/software/release/17-15/configuration_guide/vlan/b_1715_vlan_9300_cg/configuring_vlans.html
- VLAN Configuration Guide, Cisco IOS XE 17.15.x — Configuring Voice VLANs
  - https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst9300/software/release/17-15/configuration_guide/vlan/b_1715_vlan_9300_cg/configuring_voice_vlans.html
- Cisco Wireless Controller Configuration Guide, Release 8.10 — AAA Administration
  - https://www.cisco.com/c/en/us/td/docs/wireless/controller/8-10/config-guide/b_cg810/aaa_administration.html
- Cisco Wireless Controller Configuration Guide, Release 8.10 — Administration of Controller
  - https://www.cisco.com/c/en/us/td/docs/wireless/controller/8-10/config-guide/b_cg810/administration_of_cisco_wlc.html
- Cisco Wireless Controller Configuration Guide, Release 8.10 — AP Connectivity to Controller
  - https://www.cisco.com/c/en/us/td/docs/wireless/controller/8-10/config-guide/b_cg810/ap_connectivity_to_cisco_wlc.html
- Cisco Wireless Controller Configuration Guide, Release 8.10 — AP Groups
  - https://www.cisco.com/c/en/us/td/docs/wireless/controller/8-10/config-guide/b_cg810/configuring_ap_groups.html
- Cisco Wireless Controller Configuration Guide, Release 8.10 — DHCP
  - https://www.cisco.com/c/en/us/td/docs/wireless/controller/8-10/config-guide/b_cg810/dhcp.html
- Cisco Wireless Controller Configuration Guide, Release 8.10 — FlexConnect
  - https://www.cisco.com/c/en/us/td/docs/wireless/controller/8-10/config-guide/b_cg810/flexconnect.html
- Cisco Wireless Controller Configuration Guide, Release 8.10 — Per-WLAN Wireless Settings
  - https://www.cisco.com/c/en/us/td/docs/wireless/controller/8-10/config-guide/b_cg810/per_wlan_wireless_settings.html
- Cisco Wireless Controller Configuration Guide, Release 8.10 — Ports and Interfaces
  - https://www.cisco.com/c/en/us/td/docs/wireless/controller/8-10/config-guide/b_cg810/ports_and_interfaces.html
- Cisco Wireless Controller Configuration Guide, Release 8.10 — Quality of Service
  - https://www.cisco.com/c/en/us/td/docs/wireless/controller/8-10/config-guide/b_cg810/quality_of_service.html
- Cisco Wireless Controller Configuration Guide, Release 8.10 — Wireless Quality of Service
  - https://www.cisco.com/c/en/us/td/docs/wireless/controller/8-10/config-guide/b_cg810/wireless_quality_of_service.html
- Cisco Wireless Controller Configuration Guide, Release 8.10 — WLAN Security
  - https://www.cisco.com/c/en/us/td/docs/wireless/controller/8-10/config-guide/b_cg810/wlan_security.html
- Cisco Wireless Controller Configuration Guide, Release 8.10 — WLAN Timeouts
  - https://www.cisco.com/c/en/us/td/docs/wireless/controller/8-10/config-guide/b_cg810/wlan_timeouts.html
- Cisco Wireless Controller Configuration Guide, Release 8.10 — WLANs
  - https://www.cisco.com/c/en/us/td/docs/wireless/controller/8-10/config-guide/b_cg810/wlans.html
- Cisco Wireless Controller Configuration Guide, Release 8.5 — Managing APs
  - https://www.cisco.com/c/en/us/td/docs/wireless/controller/8-5/config-guide/b_cg85/managing_aps.html
