# IP Services author and audit notes

Completed 90 original questions: Sets 02–10, IDs 066–075 per set. Each fragment has exactly 10 questions and assesses all parents 4.1–4.9. The blueprint has no lettered subobjectives in this domain. Existing Set 01 was read for overlap and not edited.

Types: {'single': 75, 'multiple': 12, 'matching': 3}. Difficulty labels: {'Applied': 73, 'Foundation': 7, 'Challenge': 10}. Single-answer key positions: {'C': 19, 'B': 19, 'A': 19, 'D': 18}.

## Technical review

- Re-solved each keyed response and checked every distractor against the stated initial conditions. Distractor revisions replaced unrelated protocol names in several QoS/monitoring questions with plausible mechanism-level confusions.
- NAT: distinguish inside-local/global and translation direction; dynamic mapping creation from configuration; NAT selection ACLs from packet-filter ACLs; mapping state from application success. Pool mask does not expand its explicit endpoints. Port sharing is never inferred when overload is absent. Incoming static translation assumes routing, roles and permission as stated.
- NTP: distinguish configured, reachable, authenticated and synchronized states; stratum 16 is unsynchronized. Source-interface configuration affects the actual request source. A synchronized client can also answer downstream clients. Stratum is hierarchy, not a direct latency or accuracy measurement. Local-clock authority is explicitly isolated from external accuracy claims.
- DHCP: distinguish initial ACK, renewal at T1, existing-valid-lease operation and post-expiration behavior. The relay's giaddr selects client scope and is a return destination; interface roles and a working return route are stated. Global no service dhcp and client/relay confusion are covered separately. Requested lease length is distinguished from a server-granted lifetime.
- DNS: records, aliases, address families, cache TTL, negative answers and ordinary UDP/TCP transport are separate decisions. Resolution success never certifies the target application.
- SNMP: Get/GetNext/GetBulk/Set/Inform roles; authPriv versus authNoPriv; read-only requirements; unsupported objects; asynchronous loss; counter rate, width and discontinuity.
- Syslog: IOS subsystem facility names are distinguished from the numeric protocol facility in PRI. Destination thresholds, volatility, delivery limitations, terminal display and timestamps are separate questions.
- QoS: explicit configured actions distinguish policing from shaping. Shaping can add delay; sustained overload can exhaust any finite queue. Marking alone supplies neither bandwidth reservation nor differentiated treatment without appropriate downstream policy. Untrusted labels are not inherently authoritative.
- SSH: conventional host-key prerequisites, all VTY ranges, local database selection, actual account presence, protocol version, host-identity checking, current sessions versus enabled service, source restrictions and command authority are separately assessed. The legacy Cisco SSH guide is used only to verify stable client command syntax; obsolete key sizes and cipher recommendations are not adopted.
- FTP/TFTP: control and data connections, passive connection initiation, plain FTP confidentiality, upload direction, TFTP transfer ports, application errors, acknowledgment/retransmission, final short block and binary octet mode checked against primary protocol specifications.

## Calculations and structural checks

- CCNA4-070: (12,000,000 − 7,000,000) octets × 8 / 10 seconds = 4,000,000 bit/s. No wrap/reset is explicitly assumed.
- CCNA8-070: a 32-bit octet counter at 10 Gb/s can wrap in about 3.44 seconds, well within a 60-second interval; multiple wraps are possible.
- CCNA8-075: 1,024 / 512 = two full data blocks, followed by the required short (zero-data) final block.
- CCNA10-067: inclusive .100–.109 range contains ten addresses.
- CCNA10-071: divmod(132, 8) = (16, 4), numeric facility local0 and severity warning.
- All IDs, lengths, types, cardinalities, answer membership, per-choice reasons, HTTPS references, four-pair matching bijections and per-set nine-parent coverage checked. No repeated prompt or identical option set occurs. Prompt similarity scan against this fragment and original domain 4 found no SequenceMatcher ratio above 0.56. This lexical check is supplementary; semantic topic overlap is expected across independent practice sets.

These are authored practice questions with constructed observations. No Cisco endorsement, recalled exam content, actual-device execution, psychometric calibration, or guaranteed results are claimed. Difficulty labels are editorial judgments.

## Primary sources opened during authoring

Blueprint: https://learningcontent.cisco.com/documents/marketing/exam-topics/200-301-CCNA-v1.1.pdf

- [IP Addressing Configuration Guide, Cisco IOS XE 17.x — Configuring NAT for IP Address Conservation](https://www.cisco.com/c/en/us/td/docs/routers/ios/config/17-x/ip-addressing/b-ip-addressing/m_iadnat-addr-consv-xe.html) — Inside source address translation; static and dynamic translations; monitoring NAT.
- [Configure Network Address Translation](https://www.cisco.com/c/en/us/support/docs/ip/network-address-translation-nat/13772-12.html) — NAT definitions; configuring inside source translation.
- [RFC 3022 — Traditional IP Network Address Translator (Traditional NAT)](https://www.rfc-editor.org/rfc/rfc3022.html) — 2 Overview; 3 Translation phases.
- [Setting Time and Calendar Services](https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/bsm/configuration/15-mt/bsm-15-mt-book/bsm-time-calendar-set.html) — Network Time Protocol; configuring NTP associations; monitoring NTP.
- [Use Best Practices for Network Time Protocol](https://www.cisco.com/c/en/us/support/docs/availability/high-availability/19643-ntpm.html) — NTP architecture; synchronization; verification.
- [RFC 5905 — Network Time Protocol Version 4: Protocol and Algorithms Specification](https://www.rfc-editor.org/rfc/rfc5905.html) — 7 NTP protocol data structures; 9 Peer process; 11 System process.
- [RFC 2131 — Dynamic Host Configuration Protocol](https://www.rfc-editor.org/rfc/rfc2131.html) — 3.1 Address allocation; 4.3 Server behavior; 4.4 Client behavior.
- [RFC 2132 — DHCP Options and BOOTP Vendor Extensions](https://www.rfc-editor.org/rfc/rfc2132.html) — 3.3 Subnet Mask; 3.5 Router; 3.8 Domain Name Server; 3.17 Domain Name.
- [RFC 1034 — Domain Names - Concepts and Facilities](https://www.rfc-editor.org/rfc/rfc1034.html) — 3.6 Resource records; 4.3 Name server algorithms; 5 Resolvers.
- [RFC 1035 — Domain Names - Implementation and Specification](https://www.rfc-editor.org/rfc/rfc1035.html) — 3.3 Standard resource records; 4.1 Message format; 4.2 Transport.
- [RFC 3596 — DNS Extensions to Support IP Version 6](https://www.rfc-editor.org/rfc/rfc3596.html) — 2 AAAA resource record.
- [SNMP Configuration Guide, Cisco IOS XE 17 — Configuring SNMP Support](https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/snmp/configuration/xe-17-x/snmp-xe-17-book/nm-snmp-cfg-snmp-support.html) — Components of SNMP; operations; versions; traps and informs.
- [RFC 3416 — Version 2 of the Protocol Operations for the Simple Network Management Protocol (SNMP)](https://www.rfc-editor.org/rfc/rfc3416.html) — 4.2 PDU processing: Get, GetNext, GetBulk, Set, notifications.
- [RFC 3414 — User-based Security Model (USM) for version 3 of the Simple Network Management Protocol (SNMPv3)](https://www.rfc-editor.org/rfc/rfc3414.html) — 1.2 Goals and constraints; authentication and privacy.
- [RFC 2863 — The Interfaces Group MIB](https://www.rfc-editor.org/rfc/rfc2863.html) — 3.1.6 Counter size; ifHCInOctets; ifCounterDiscontinuityTime.
- [System Message Logging](https://www.cisco.com/c/en/us/td/docs/routers/access/wireless/software/guide/SysMsgLogging.html) — System log message format; logging destinations; severity levels; timestamps.
- [RFC 5424 — The Syslog Protocol](https://www.rfc-editor.org/rfc/rfc5424.html) — 6.2.1 PRI; 6.2.3 TIMESTAMP.
- [RFC 5426 — Transmission of Syslog Messages over UDP](https://www.rfc-editor.org/rfc/rfc5426.html) — 4.1 Reliability; 4.2 Congestion control.
- [IP Addressing: DHCP Configuration Guide, Cisco IOS XE Everest 16.6 — Configuring the Cisco IOS XE DHCP Relay Agent](https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/ipaddr_dhcp/configuration/xe-16-6/dhcp-xe-16-6-book/dhcp-relay-agent-xe.html) — Packet forwarding address; giaddr; specifying the packet forwarding address.
- [IP Addressing: DHCP Configuration Guide, Cisco IOS XE 17 — Configuring the Cisco IOS XE DHCP Client](https://www.cisco.com/c/en/us/td/docs/routers/asr920/configuration/guide/ipaddr-dhcp/17-1-1/b-dhcp-xe-17-1-asr920/m_config-dhcp-client-xe.html) — Configuring the DHCP client; monitoring and maintaining DHCP client operation.
- [Quality of Service Configuration Guide — Quality of service](https://www.cisco.com/c/en/us/td/docs/switches/lan/c9000/qos/quality-of-service-configuration-guide/m-quality-of-service.html) — Classification; marking; queuing and scheduling; policing and shaping.
- [Compare Traffic Policing and Traffic Shaping to Limit Bandwidth](https://www.cisco.com/c/en/us/support/docs/quality-of-service-qos/qos-policing/19645-policevsshape.html) — Traffic policing and traffic shaping comparison.
- [RFC 2474 — Definition of the Differentiated Services Field (DS Field) in the IPv4 and IPv6 Headers](https://www.rfc-editor.org/rfc/rfc2474.html) — 3 Differentiated Services field; 4 Per-hop behaviors.
- [RFC 2475 — An Architecture for Differentiated Services](https://www.rfc-editor.org/rfc/rfc2475.html) — 2.3 Traffic classification and conditioning; 2.4 Per-hop behaviors.
- [Configure SSH on Routers](https://www.cisco.com/c/en/us/support/docs/security-vpn/secure-shell-ssh/4145-ssh.html) — SSH server prerequisites; SSHv2; VTY restrictions; show commands.
- [RFC 4251 — The Secure Shell (SSH) Protocol Architecture](https://www.rfc-editor.org/rfc/rfc4251.html) — 4 Architecture; 9 Security considerations.
- [RFC 959 — File Transfer Protocol (FTP)](https://www.rfc-editor.org/rfc/rfc959.html) — 2.3 FTP model; 3.2 Data connections; 4.1 FTP commands.
- [RFC 4217 — Securing FTP with TLS](https://www.rfc-editor.org/rfc/rfc4217.html) — 4 Session negotiation on the control port; 7 Data connection behavior.
- [RFC 1350 — The TFTP Protocol (Revision 2)](https://www.rfc-editor.org/info/rfc1350/) — 2 Protocol overview; 3 Relation to other protocols; 4 Initial connection; 6 Normal termination.
- [Secure Shell Configuration Guide, Cisco IOS XE Release 2 — Secure Shell Version 2 Support](https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/sec_usr_ssh/configuration/xe-2/sec-usr-ssh-xe-2-book/sec-secure-shell-v2.html) — SSH client example: ssh -l username destination.
