# Security Fundamentals authoring and audit notes

Completed 135 original questions, fifteen for each Set 02–10. Existing Set 01 was read for comparison and not edited. All ten parent objectives (5.1–5.10) are assessed in every new set; the v1.1 blueprint has no lettered children in domain 5.

## Counts

| Set | Single | Multiple | Matching | Exhibits |
|---|---:|---:|---:|---:|
| 02 | 13 | 2 | 0 | 4 |
| 03 | 12 | 2 | 1 | 2 |
| 04 | 13 | 2 | 0 | 2 |
| 05 | 11 | 3 | 1 | 2 |
| 06 | 13 | 2 | 0 | 2 |
| 07 | 13 | 2 | 0 | 1 |
| 08 | 12 | 2 | 1 | 1 |
| 09 | 13 | 2 | 0 | 3 |
| 10 | 12 | 3 | 0 | 4 |

Total: 112 single-select, 20 multiple-select (always select two), and 3 matching. Choice order is deterministically shuffled by question ID; scoring keys move with choices. Every answer option includes a specific rationale.

## Verification performed

- Structural audit: 135 unique IDs, correct 076–090 ranges, fifteen questions per set, all domain parents per set, valid answer cardinality and choice IDs, complete explanations and HTTPS references. No identical prompts or identical option sets. A normalized text comparison against the original domain and all new prompts found no SequenceMatcher prompt similarity above 0.60. This is a lexical screen, not a claim of psychometric uniqueness.
- Re-solved the answer keys and reviewed distractors against each scenario’s conditions. Kept authentication, authorization, accounting, trust state, retained state, and observation scope separate.
- Wildcard arithmetic independently checked with IPv4 bit comparisons: /26 (.64–.127), its /25 and /27 distractors; /23 third octets 8–9; /22 third octets 48–51; exact-host wildcard; and the two /27 ranges in CCNA10-086.
- ACL cases checked for source-versus-destination port operator position, first-match behavior, terminal implicit deny, standard versus extended scope, interface direction, IPv4 versus IPv6 scope, and VTY versus transit attachment. TCP/UDP reply tuples and inclusive port ranges were manually re-solved.
- Source review corrected CCNA8-081 to a numbered VTY ACL consistent with the cited Catalyst/IOS guide; replaced the local-login-selector question closest to Set 01 with effective-session privilege verification. Added specific references for IPv6 ACLs, password storage, WLAN interfaces and all three features in the L2 matching question.
- L2 cases specify whether bindings exist, interfaces are trusted, aging is active, and violations or counters are current versus historical. DHCP snooping and DAI trust are independently configured. A valid binding is not an exemption from a rate limit.
- WLAN cases distinguish cipher, key management, format (8–63 ASCII versus 64 hexadecimal digits), configured versus saved state, compatible clients, and the phase of a connection failure. WPA3 transition compatibility is not presented as SAE protection for legacy WPA2 clients.
- No physical-device or emulated lab execution was performed. CLI and GUI exhibits are constructed cases. This is independently authored curriculum practice, not Cisco exam content, a commercial-bank reproduction, or a calibrated score predictor.

## Primary sources opened and used

Blueprint opened: [CCNA Exam v1.1 (200-301)](https://learningcontent.cisco.com/documents/marketing/exam-topics/200-301-CCNA-v1.1.pdf).

The following technical pages were opened during authoring. References in each question identify supporting concepts rather than claiming the source supplied the constructed scenario.

- [NIST SP 800-53 Rev. 5: Security and Privacy Controls for Information Systems and Organizations](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-53r5.pdf) — AT-2, AT-3, PE-2, and PE-3: awareness, training, and physical access.
- [NIST SP 800-63B-4: Digital Identity Guidelines — Authentication and Authenticator Management](https://pages.nist.gov/800-63-4/sp800-63b.html) — Authentication factors; password verifiers; authenticator management.
- [Configure Commonly Used IP ACLs](https://www.cisco.com/c/en/us/support/docs/ip/access-lists/26448-ACLsamples.html) — Allow Pings (ICMP); Allow DNS; TCP/UDP ACL syntax.
- [Understand Cisco IOS Password Encryption](https://www.cisco.com/c/en/us/support/docs/security-vpn/remote-authentication-dial-user-service-radius/107614-64.html) — Cisco IOS password encryption and reversible type 7 limitations.
- [Configure IP Access Lists](https://www.cisco.com/c/en/us/support/docs/security/ios-firewall/23602-confaccesslists.html) — ACL Concepts; Masks; Process ACLs; Apply ACLs; Extended ACLs.
- [Security and VPN Configuration Guide, Cisco IOS XE 17.x: IPv6 Access Control Lists](https://www.cisco.com/c/en/us/td/docs/routers/ios/config/17-x/sec-vpn/b-security-vpn/m_ip6-acls-xe.html) — Access Control Lists for IPv6 Traffic Filtering; Applying the IPv6 ACL to an Interface.
- [Security and VPN Configuration Guide, Cisco IOS XE 17.x: Configuring Security with Passwords, Privileges, and Logins](https://www.cisco.com/c/en/us/td/docs/routers/ios/config/17-x/sec-vpn/b-security-vpn/m_sec-cfg-sec-4cli-0.html) — Protecting Access to User EXEC Mode; Password Encryption Levels; Password Change Verification.
- [Catalyst 3750-X and 3560-X Configuration Guide: Configuring Network Security with ACLs](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst3750x_3560x/software/release/15-0_2_se/configuration/guide/3750x_cg/swacl.html) — Applying an IPv4 ACL to a Terminal Line; Including Comments in ACLs.
- [Catalyst 3750-X and 3560-X Configuration Guide: Configuring Switch-Based Authentication](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst3750x_3560x/software/release/15-0_2_se/configuration/guide/3750x_cg/swauthen.html) — Protecting Access to Privileged EXEC Commands; Configuring Username and Password Pairs.
- [Catalyst 3750-X and 3560-X Configuration Guide: Configuring DHCP Features and IP Source Guard](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst3750x_3560x/software/release/15-0_2_se/configuration/guide/3750x_cg/swdhcp82.html) — DHCP Snooping; DHCP Snooping Binding Database; Enabling DHCP Snooping.
- [Catalyst 3750-X and 3560-X Configuration Guide: Configuring Dynamic ARP Inspection](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst3750x_3560x/software/release/15-0_2_se/configuration/guide/3750x_cg/swdynarp.html) — Understanding Dynamic ARP Inspection; Rate Limiting; ARP ACLs.
- [Catalyst 3750-X and 3560-X Configuration Guide: Configuring Port-Based Traffic Control](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst3750x_3560x/software/release/15-0_2_se/configuration/guide/3750x_cg/swtrafc.html) — Secure MAC Addresses; Security Violations; Port Security Aging.
- [Cisco Wireless Controller Configuration Guide, Release 8.10: Ports and Interfaces](https://www.cisco.com/c/en/us/td/docs/wireless/controller/8-10/config-guide/b_cg810/ports_and_interfaces.html) — Dynamic Interfaces; Interface Groups; WLAN interface mapping and DHCP.
- [Cisco Wireless Controller Configuration Guide, Release 8.10: WLAN Security](https://www.cisco.com/c/en/us/td/docs/wireless/controller/8-10/config-guide/b_cg810/wlan_security.html) — WPA1+WPA2; Configuring WPA1+WPA2 (GUI); Protected Management Frames.
- [Cisco Catalyst 9800 Configuration Guide, IOS XE 17.3.x: Wi-Fi Protected Access 3](https://www.cisco.com/c/en/us/td/docs/wireless/controller/9800/17-3/config-guide/b_wl_17_3_cg/m_wpa3.html) — WPA3-Personal; WPA3-Personal Transition Mode; Protected Management Frames.
- [RFC 4301: Security Architecture for the Internet Protocol](https://www.rfc-editor.org/rfc/rfc4301.html) — Sections 3, 4.1, 4.4.1: IPsec services, tunnel mode, and security policy.
- [RFC 4949: Internet Security Glossary, Version 2](https://www.rfc-editor.org/rfc/rfc4949.html) — Section 2: threat, vulnerability, exploit, and countermeasure.
- [RFC 8907: The Terminal Access Controller Access-Control System Plus (TACACS+) Protocol](https://www.rfc-editor.org/rfc/rfc8907.html) — Sections 5, 6, and 7: authentication, authorization, and accounting.

Also opened to locate the final technical PDF: [NIST SP 800-53 Rev. 5 publication page](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final). Search-result snippets were not used as a substitute for the cited technical pages.

## Independent ACL review

A second author independently reviewed all 27 ACL items and reported that the keys, wildcard calculations, port placement, ordering, ICMP cases, and stateless-filter claims checked out; nine independent assertions passed. Applied two wording clarifications: CCNA3-087 explicitly states that the test packet enters Gi0/0, and CCNA9-087 explicitly identifies client-initiated connections to the server’s destination ports 23 and 22. Neither correction changed a key.

## Remaining limits

Recurring objectives necessarily revisit some principles across sets, but question faults, decisions, evidence, and constrained packet cases vary. Human field testing is still required to estimate item difficulty, discrimination, and exam performance; no such measurements are claimed. Platform-specific cases deliberately identify IOS, Catalyst or AireOS context, and legacy command recognition is not a recommendation to deploy obsolete equipment or weak password formats.

Final domain5.json SHA-256: `2e00c2228bf6c661d6bd4478b673e3a11135d760c320745692f34fb1718090e6`
