# V2 content corrections

Corrected 23 questions: 14 confirmed content/reference issues and 9 documented concerns. All 1,000 question IDs, choice IDs, answer keys and matching mappings are preserved.

| Question | Category | Correction |
|---|---|---|
| CCNA4-083 | confirmed content defect | Separate individual identity benefits from the additional accounting needed for historical attribution. |
| CCNA8-042 | confirmed content defect | Identify the correct addresses explicitly instead of incorrectly naming the first displayed pair. |
| CCNA9-089 | confirmed content defect | Narrow the requested observation to what the keyed command reports; separately explain how to list secure MAC addresses. |
| CCNA2-017 | confirmed reference defect | Replace the wireless local-mode locator with the relevant wired campus hierarchy section. |
| CCNA5-002 | confirmed reference defect | Replace the wireless local-mode locator with the relevant wired campus hierarchy section. |
| CCNA6-002 | confirmed reference defect | Replace the wireless local-mode locator with the relevant wired campus hierarchy section. |
| CCNA9-002 | confirmed reference defect | Replace the wireless local-mode locator with the relevant wired campus hierarchy section. |
| CCNA4-017 | confirmed reference defect | Cite 5-GHz channel width, channel reuse and data-rate tradeoffs instead of a 2.4-GHz locator. |
| CCNA3-009 | confirmed reference defect | Align the URL fragment with the cited anycast service-availability section. |
| CCNA4-039 | confirmed reference defect | Use the actual AireOS 8.10 section describing Required and Allowed WMM admission policies. |
| CCNA9-039 | confirmed reference defect | Use the actual AireOS 8.10 section describing Required and Allowed WMM admission policies. |
| CCNA4-071 | confirmed reference defect | Correct the syslog congestion-control section number and link target. |
| CCNA7-038 | confirmed reference defect | Scope the GUI example to verified AireOS 8.5 documentation and cite the actual General-tab radio-policy field. |
| CCNA7-040 | confirmed reference defect | Scope all four GUI relationships to AireOS 8.5 and replace scattered unrelated locators with verified General, security and AP-group fields in the matching-release help. |
| CCNA8-074 | wording concern | Remove the unsupported claim that SSH successfully follows a VTY line password; ask directly about selecting local-user authentication. |
| CCNA6-078 | wording concern | Describe the configuration mismatch without claiming that shared VTY line-password SSH authentication succeeds. |
| CCNA7-014 | reference-fit concern | Specify the documented controller architecture and cite management-plane failure behavior directly. |
| CCNA7-019 | reference-fit concern | Use direct dependency/failure-analysis guidance and describe independence from the failed connection rather than requiring every dependency to be physically local. |
| CCNA5-037 | reference-fit concern | Replace wireless-controller instructions with switch accounting guidance and specify the documented TACACS+ command-accounting mechanism. |
| CCNA7-037 | reference-fit concern | Use direct Catalyst switch console-access documentation rather than wireless-controller administration guidance. |
| CCNA9-060 | wording concern | Limit successful ARP evidence to next-hop MAC resolution rather than claiming observed delivery of a data packet. |
| CCNA3-005 | wording concern | Describe the acknowledgment as cumulative receipt and the next expected sequence number, not a request for a byte. |
| CCNA2-058 | wording concern | Make the initial OSPF election assumptions explicit so no unstated incumbent or neighbor-discovery timing changes the ranking exercise. |

## New exact URL strings

- https://documentation.meraki.com/Platform_Management/Dashboard_Administration/Design_and_Configure/Architectures_and_Best_Practices/Cisco_Meraki_Best_Practice_Design/Best_Practice_Design_-_MR_Wireless/High_Density_Wi-Fi_Deployments
- https://learn.microsoft.com/en-us/azure/well-architected/reliability/failure-mode-analysis
- https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst9300/software/release/17-13/command_reference/b_1713_9300_cr/using_the_command_line_interface.html
- https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst9300/software/release/17-13/configuration_guide/sec/b_1713_sec_9300_cg/configuring_accounting.html
- https://www.cisco.com/c/en/us/td/docs/wireless/controller/8-10/config-guide/b_cg810/radio_bands.html
- https://www.cisco.com/c/en/us/td/docs/wireless/controller/8-5/olh/wlc-olh/wlansc.html
- https://www.rfc-editor.org/rfc/rfc2328.html#section-9.4
- https://www.rfc-editor.org/rfc/rfc4786.html#section-4.4.1
- https://www.rfc-editor.org/rfc/rfc5426.html#section-4.3
- https://www.rfc-editor.org/rfc/rfc9293.html#section-3.4

Verification: updated/new references were checked against current primary-source pages on 2026-09-14. RFC targets use the matching section IDs. The radio-policy scenarios explicitly use AireOS 8.5 because its verified online-help chapter contains the required GUI fields. Study guides, coverage maps and reference index are regenerated from JSON; regeneration does not change scoring.
