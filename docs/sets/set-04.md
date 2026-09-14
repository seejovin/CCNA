# CCNA Practice — Set 04

100 original questions aligned to CCNA 200-301 v1.1. No interactive labs.

Answers and explanations follow each question. For an unrevealed attempt, use the Streamlit app.

Content review date: 2026-09-14.

## CCNA4-001 · Network Fundamentals

Objectives: 1.1.d, 1.1.e · single · Applied

After a WLAN policy change, all APs managed by one controller advertise a new network consistently. What did the controller contribute?

- **A.** Conversion of every client into a router
- **B.** Central coordination of WLAN configuration
- **C.** Replacement of radio transmission with TCP
- **D.** Electrical power through the SSID

**Answer: B**

Central management reduces the need to configure each managed AP independently. The APs still provide the radio interfaces to clients.

**Option explanations**

- **A:** Client forwarding roles need not change.
- **B:** Managed AP policy can be distributed centrally.
- **C:** Clients still use an 802.11 radio link.
- **D:** SSID text does not deliver power.

**Further reading**

- [Campus LAN and Wireless LAN Solution Design Guide](https://www.cisco.com/c/en/us/td/docs/solutions/CVD/Campus/cisco-campus-lan-wlan-design-guide.html) — Centralized (local-mode) design model

---

## CCNA4-002 · Network Fundamentals

Objectives: 1.2.c · single · Applied

A basic fabric has four spines. A new leaf must connect once to every spine. How many additional leaf-to-spine links are required?

- **A.** One
- **B.** Two
- **C.** Eight
- **D.** Four

**Answer: D**

The connection count follows the full leaf-to-spine relationship. Existing leaf-to-spine links do not need to be duplicated for this new leaf.

**Option explanations**

- **A:** One link reaches only one of the four spines.
- **B:** Two spines would still lack the required connection.
- **C:** The requirement specifies one link per spine, not two.
- **D:** Each of the four spines needs one connection from the new leaf.

**Further reading**

- [Cisco Massively Scalable Data Center Network Fabric Design and Operation White Paper](https://www.cisco.com/c/en/us/products/collateral/switches/nexus-9000-series-switches/white-paper-c11-743245.html) — MSDC Layer 3 IP fabric design evolution; Cisco MSDC design example 1: Two-tiered spine-leaf topology

---

## CCNA4-003 · Network Fundamentals

Objectives: 1.3.b, 1.4 · single · Foundation

A switch port and server NIC operate at 1 Gb/s full duplex over a dedicated link. Which behavior is consistent with this connection?

- **A.** Both may transmit and receive simultaneously without Ethernet collisions
- **B.** They must use CSMA/CD to schedule every transmitted frame
- **C.** The server shares one collision domain with every switch port
- **D.** Only one direction can carry traffic at a time

**Answer: A**

A full-duplex point-to-point Ethernet link does not use collisions to arbitrate access. It can carry traffic in both directions concurrently.

**Option explanations**

- **A:** Full duplex separates simultaneous transmission and reception.
- **B:** Collision-based access applies to half-duplex Ethernet.
- **C:** The switch separates point-to-point links.
- **D:** That describes half-duplex behavior.

**Further reading**

- [Configure and Verify Ethernet 10/100/1000Mb Half/Full Duplex Auto-Negotiation](https://www.cisco.com/c/en/us/support/docs/lan-switching/ethernet/10561-3.html) — Background Information; Auto-Negotiation on Catalyst Switches that Run Cisco IOS Software

---

## CCNA4-004 · Network Fundamentals

Objectives: 1.4 · single · Applied

A copper link intended for 1 Gb/s negotiates at 100 Mb/s on both ends. A cable tester finds two usable pairs but faults on the other two; both ports support 1000BASE-T. What best explains the reduced rate?

- **A.** A DNS lookup selected a slower link
- **B.** A mismatched subnet forces half duplex
- **C.** The damaged pairs prevent the required four-pair gigabit operation
- **D.** 100 Mb/s proves all four pairs are intact

**Answer: C**

The physical evidence identifies a cable capability problem. Matching operational speed on both ends means this is not an observed speed mismatch.

**Option explanations**

- **A:** DNS does not negotiate physical link speed.
- **B:** Subnet masks do not control Ethernet negotiation.
- **C:** 1000BASE-T requires all four pairs, unlike 100BASE-TX.
- **D:** A 100 Mb/s link can work while pairs needed for gigabit are faulty.

**Further reading**

- [Configure and Verify Ethernet 10/100/1000Mb Half/Full Duplex Auto-Negotiation](https://www.cisco.com/c/en/us/support/docs/lan-switching/ethernet/10561-3.html) — Background Information; Auto-Negotiation on Catalyst Switches that Run Cisco IOS Software

---

## CCNA4-005 · Network Fundamentals

Objectives: 1.5 · multiple · Applied

Which TWO features are provided by TCP but not by the UDP protocol itself? Select two.

- **A.** A source port field
- **B.** A destination port field
- **C.** Connection establishment using SYN exchange
- **D.** Cumulative acknowledgment of received byte sequence
- **E.** Carriage inside IP packets

**Answer: C, D**

Ports and IP encapsulation are shared characteristics. TCP additionally maintains connection and reliable-stream state.

**Option explanations**

- **A:** Both protocols have transport ports.
- **B:** Both can demultiplex traffic using destination ports.
- **C:** TCP establishes connection state with a handshake.
- **D:** TCP acknowledges its byte-stream sequence space.
- **E:** Both TCP and UDP can be carried by IP.

**Further reading**

- [RFC 9293: Transmission Control Protocol (TCP)](https://www.rfc-editor.org/rfc/rfc9293.html#section-2.2) — 2.2. Key TCP Concepts
- [RFC 768: User Datagram Protocol](https://www.rfc-editor.org/rfc/rfc768) — Introduction; Fields

---

## CCNA4-006 · Network Fundamentals

Objectives: 1.6 · single · Applied

A host has 172.25.13.4 with mask 255.255.252.0. Which destination is considered on-link by that mask?

- **A.** 172.25.11.254
- **B.** 172.25.15.200
- **C.** 172.25.16.1
- **D.** 172.26.13.4

**Answer: B**

A /22 groups four consecutive third-octet values. Here the group is 12, 13, 14, and 15.

**Option explanations**

- **A:** Its third octet is below the containing 12–15 block.
- **B:** It belongs to the same 172.25.12.0/22 subnet.
- **C:** This begins the next /22 block.
- **D:** The second octet differs within the fixed prefix.

**Further reading**

- [Configure IP Addresses and Unique Subnets for New Users](https://www.cisco.com/c/en/us/support/docs/ip/routing-information-protocol-rip/13788-3.html) — Network Masks; Understand Subnetting; VLSM Example

---

## CCNA4-007 · Network Fundamentals

Objectives: 1.7 · single · Foundation

A small business assigns private IPv4 addresses to its LAN. Which statement about the resulting security is accurate?

- **A.** All inbound access is cryptographically blocked
- **B.** Private addresses authenticate the devices using them
- **C.** No additional access policy is ever needed
- **D.** Address selection alone does not define or enforce the security policy

**Answer: D**

RFC 1918 supplies reusable addressing, not an authorization system. A private network still needs a deliberate security policy.

**Option explanations**

- **A:** An address range is not a cryptographic control.
- **B:** Source address assignment does not prove identity.
- **C:** Reachability and allowed services still need explicit control.
- **D:** Filtering and authentication remain separate mechanisms.

**Further reading**

- [RFC 1918: Address Allocation for Private Internets](https://www.rfc-editor.org/rfc/rfc1918#section-3) — 3. Private Address Space

---

## CCNA4-008 · Network Fundamentals

Objectives: 1.8 · multiple · Challenge

Which TWO addresses share the prefix 2001:db8:84:1200::/56? Select two.

- **A.** 2001:db8:84:12ab::9
- **B.** 2001:db8:84:13ab::9
- **C.** 2001:db8:84:12ff::1
- **D.** 2001:db8:85:1200::9
- **E.** 2001:db8:84:11ff::1

**Answer: A, C**

A /56 fixes the first three hextets and the high byte of the fourth. The low byte of that fourth hextet may vary.

**Option explanations**

- **A:** The high byte of the fourth hextet remains 12.
- **B:** The fourth hextet begins 13, outside the /56.
- **C:** This remains within the fourth-hextet range 1200–12ff.
- **D:** The third hextet is outside the fixed first 48 bits.
- **E:** The fourth hextet begins 11, outside the /56.

**Further reading**

- [RFC 4291: IP Version 6 Addressing Architecture](https://www.rfc-editor.org/rfc/rfc4291#section-2.3) — 2.3. Text Representation of Address Prefixes; 2.4. Address Type Identification; 2.5.6. Link-Local IPv6 Unicast Addresses; 2.7. Multicast Addresses

---

## CCNA4-009 · Network Fundamentals

Objectives: 1.9.a · single · Foundation

An organization needs IPv6 addresses routable between its internal sites but does not intend to advertise them on the global Internet. Which address category is designed for local assignment with this scope?

- **A.** Link-local unicast
- **B.** Link-local all-nodes multicast
- **C.** Unique local unicast
- **D.** Unspecified address

**Answer: C**

Unique local addresses can be routed within selected internal networks. They differ from link-local addresses, which remain confined to one link.

**Option explanations**

- **A:** Link-local addresses cannot be routed across site links.
- **B:** This is a local delivery group, not individual routed host addressing.
- **C:** ULA supports internal routing beyond a single link.
- **D:** The all-zero address cannot identify an assigned interface.

**Further reading**

- [RFC 4193: Unique Local IPv6 Unicast Addresses](https://www.rfc-editor.org/rfc/rfc4193#section-3.1) — 1. Introduction; 3.1. Format
- [RFC 4291: IP Version 6 Addressing Architecture](https://www.rfc-editor.org/rfc/rfc4291#section-2.3) — 2.3. Text Representation of Address Prefixes; 2.4. Address Type Identification; 2.5.6. Link-Local IPv6 Unicast Addresses; 2.7. Multicast Addresses

---

## CCNA4-010 · Network Fundamentals

Objectives: 1.10 · single · Applied

A Mac network service shows Configure IPv4: Manually, with a valid address and subnet mask but an empty Router field. No other interface or route exists. What should the administrator check first for off-subnet access?

| TCP/IP field | Value |
| --- | --- |
| Configure IPv4 | Manually |
| IP address | 10.41.8.14 |
| Subnet mask | 255.255.255.0 |
| Router | blank |

- **A.** The configured default router value
- **B.** The computer’s display resolution
- **C.** Whether its hostname contains the subnet number
- **D.** Whether Wi-Fi encryption uses the router’s IP as a key

**Answer: A**

The Router setting specifies the gateway for that network service. A valid local address alone does not supply a route to remote networks.

**Option explanations**

- **A:** The service lacks the normal next hop for off-subnet destinations.
- **B:** Display settings do not determine routing.
- **C:** Hostnames do not have to encode addressing.
- **D:** Wireless keys and router addresses are distinct settings.

**Further reading**

- [Change TCP/IP settings on Mac](https://support.apple.com/en-hk/guide/mac-help/mh14129/mac) — IP address, subnet mask, and router settings

---

## CCNA4-011 · Network Fundamentals

Objectives: 1.11.d · single · Applied

A WLAN uses WPA2 with AES-CCMP. After frames leave the AP onto ordinary Ethernet, what does this wireless encryption alone guarantee?

- **A.** All subsequent Internet hops remain encrypted by CCMP
- **B.** The protected wireless data exchange had link-layer confidentiality
- **C.** The destination application has validated the user’s identity
- **D.** The server’s stored file is encrypted at rest

**Answer: B**

The wireless encryption boundary ends with that wireless link. End-to-end application encryption, such as TLS, protects a different scope.

**Option explanations**

- **A:** CCMP protects the wireless link, not every downstream segment.
- **B:** The protection applies to the negotiated wireless security association.
- **C:** Wireless link protection does not establish application authorization.
- **D:** Storage encryption is a separate function.

**Further reading**

- [Wireless Fundamentals: Encryption and Authentication](https://documentation.meraki.com/Wireless/Design_and_Configure/Architecture_and_Best_Practices/Wireless_Fundamentals:_Encryption_and_Authentication) — WPA2 – Personal; Hidden SSID

---

## CCNA4-012 · Network Fundamentals

Objectives: 1.12 · single · Applied

Two critical VMs run on the same physical hypervisor host with no replication elsewhere. Which single failure can stop both despite their separate guest operating systems?

- **A.** One guest changes its wallpaper
- **B.** One VM changes its local hostname
- **C.** A client closes one browser tab
- **D.** The physical host loses power

**Answer: D**

Guest isolation is not physical-host independence. A shared underlying host remains a common failure dependency.

**Option explanations**

- **A:** That does not inherently stop the other guest.
- **B:** Hostnames do not define physical failure independence.
- **C:** That does not necessarily affect either VM.
- **D:** Both VMs depend on the same powered hardware.

**Further reading**

- [What is a container?](https://docs.docker.com/get-started/docker-concepts/the-basics/what-is-a-container/#containers-versus-virtual-machines-vms) — Containers versus virtual machines (VMs)

---

## CCNA4-013 · Network Fundamentals

Objectives: 1.13.c · single · Applied

A VLAN 40 broadcast frame enters Gi1/0/1. Other VLAN 40 forwarding ports are Gi1/0/2 and Gi1/0/5; Gi1/0/3 belongs to VLAN 50. No suppression features apply. Where are copies sent?

- **A.** Gi1/0/1, Gi1/0/2, and Gi1/0/5
- **B.** Gi1/0/3 only
- **C.** Gi1/0/2 and Gi1/0/5
- **D.** No port because broadcasts have no unique destination entry

**Answer: C**

Broadcast scope follows the VLAN’s forwarding domain. Exclude the ingress port and ports belonging only to other VLANs.

**Option explanations**

- **A:** Normal flooding excludes ingress.
- **B:** The broadcast does not cross into another VLAN by Layer 2 flooding.
- **C:** These are the other eligible ports in the ingress VLAN.
- **D:** Broadcast forwarding does not require a learned unicast destination.

**Further reading**

- [Configuring MAC Address Tables](https://www.cisco.com/c/en/us/td/docs/switches/datacenter/nexus5500/sw/layer2/7x/b_5500_Layer2_Config_7x/config_mac_address_tables.pdf) — Information About MAC Addresses (page 1); Configuring the Aging Time for the MAC Table (page 2)

---

## CCNA4-014 · Network Fundamentals

Objectives: 1.1.h · single · Applied

A PoE AP loses power whenever its access switch loses power. There is no injector or secondary AP power source. Which change directly preserves the AP’s power during a short utility outage?

- **A.** Provide an appropriately sized UPS to the PoE switch
- **B.** Use a longer DHCP lease
- **C.** Change the AP’s SSID
- **D.** Increase the MAC aging timer

**Answer: A**

Power continuity must include the actual PoE source. Network configuration cannot substitute for a live electrical supply.

**Option explanations**

- **A:** The switch supplies the AP’s only power path.
- **B:** Address lease duration cannot power the AP.
- **C:** The network name has no electrical effect.
- **D:** Forwarding metadata cannot keep the PoE source energized.

**Further reading**

- [Interface and Hardware Components Configuration Guide, Cisco IOS XE 17.14.x (Catalyst 9200 Switches): Configuring Power over Ethernet](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst9200/software/release/17-14/configuration_guide/int_hw/b_1714_int_and_hw_9200_cg/configuring_poe.html) — Powered-Device Detection and Initial Power Allocation

---

## CCNA4-015 · Network Fundamentals

Objectives: 1.6 · single · Applied

A router rejects 192.168.28.63/27 as an ordinary interface host address. Why?

- **A.** Every address ending in 63 is invalid
- **B.** The address is in multicast space
- **C.** The mask is not contiguous
- **D.** It is the broadcast address of 192.168.28.32/27

**Answer: D**

Evaluate the address together with its prefix. The all-ones host field identifies the broadcast address of this ordinary subnet.

**Option explanations**

- **A:** Its validity depends on the subnet mask.
- **B:** 192.168.28.63 is not IPv4 multicast.
- **C:** /27 is a valid contiguous prefix.
- **D:** The .32–.63 block reserves .63 for directed broadcast.

**Further reading**

- [Configure IP Addresses and Unique Subnets for New Users](https://www.cisco.com/c/en/us/support/docs/ip/routing-information-protocol-rip/13788-3.html) — Network Masks; Understand Subnetting; VLSM Example

---

## CCNA4-016 · Network Fundamentals

Objectives: 1.9.c · single · Applied

A host sends to an IPv6 multicast group that has receivers on several links and is permitted to traverse routers by its scope and routing configuration. What is the intended delivery model?

- **A.** Exactly one nearest group member
- **B.** Members of the addressed group
- **C.** Every IPv6 node regardless of membership
- **D.** Only nodes with matching MAC vendor prefixes

**Answer: B**

Multicast enables group delivery. Actual forwarding also depends on scope, membership, and configured multicast support.

**Option explanations**

- **A:** That would be anycast behavior.
- **B:** Multicast addresses identify groups rather than one individual interface.
- **C:** Not every multicast group is the all-nodes group.
- **D:** Group membership is not selected by MAC manufacturer bits.

**Further reading**

- [RFC 4291: IP Version 6 Addressing Architecture](https://www.rfc-editor.org/rfc/rfc4291#section-2.3) — 2.3. Text Representation of Address Prefixes; 2.4. Address Type Identification; 2.5.6. Link-Local IPv6 Unicast Addresses; 2.7. Multicast Addresses

---

## CCNA4-017 · Network Fundamentals

Objectives: 1.11.a, 1.11.c · multiple · Applied

A crowded 5 GHz deployment changes channel width from 80 MHz to 20 MHz while retaining an appropriate channel plan. Which TWO effects are plausible? Select two.

- **A.** More separate nonoverlapping channels become available within the same spectrum
- **B.** Every client must obtain a new IPv6 address
- **C.** The SSID becomes hidden automatically
- **D.** Peak PHY rate per radio may decrease under comparable conditions
- **E.** All external interference disappears

**Answer: A, D**

Channel width trades potential per-radio throughput against frequency reuse. It does not alter names or guarantee an interference-free environment.

**Option explanations**

- **A:** Narrower channels consume less spectrum per channel.
- **B:** RF width does not inherently force IPv6 renumbering.
- **C:** Visibility is unrelated to channel width.
- **D:** Narrower bandwidth can reduce the achievable physical data rate.
- **E:** Other transmitters and noise sources can remain.

**Further reading**

- [Cisco Meraki — High Density Wi-Fi Deployments](https://documentation.meraki.com/Platform_Management/Dashboard_Administration/Design_and_Configure/Architectures_and_Best_Practices/Cisco_Meraki_Best_Practice_Design/Best_Practice_Design_-_MR_Wireless/High_Density_Wi-Fi_Deployments) — Default Channel Width; Estimate Device Throughput — channel-width data-rate table

---

## CCNA4-018 · Network Fundamentals

Objectives: 1.13.a · single · Applied

A dynamic MAC entry has a 300-second aging interval. Its source sends eligible frames every 60 seconds on the same port. With no topology changes, what should happen?

- **A.** The entry expires exactly 300 seconds after first learning
- **B.** The entry becomes a static configuration automatically
- **C.** The entry stays fresh while those source frames continue
- **D.** The switch forgets all other entries on each refresh

**Answer: C**

Aging removes unused dynamic information. Regular source observations maintain the mapping rather than letting its original timestamp dictate expiration.

**Option explanations**

- **A:** Subsequent source observations refresh its age.
- **B:** Frequent traffic does not convert dynamic entries to static.
- **C:** The timer is refreshed by relevant source traffic.
- **D:** Refreshing one entry does not clear the entire table.

**Further reading**

- [Configuring MAC Address Tables](https://www.cisco.com/c/en/us/td/docs/switches/datacenter/nexus5500/sw/layer2/7x/b_5500_Layer2_Config_7x/config_mac_address_tables.pdf) — Information About MAC Addresses (page 1); Configuring the Aging Time for the MAC Table (page 2)

---

## CCNA4-019 · Network Fundamentals

Objectives: 1.2.f · single · Applied

A provider exposes pooled computing capacity with self-service provisioning, elasticity, and metered usage. Which characteristic distinguishes this from simply renting a fixed remote server with manual provisioning?

- **A.** On-demand cloud service behavior
- **B.** Guaranteed absence of physical servers
- **C.** A requirement to use only public IP addresses
- **D.** No customer responsibility for configuration

**Answer: A**

Remote location alone does not define cloud computing. The service model and operational characteristics matter.

**Option explanations**

- **A:** The stated provisioning and elasticity characteristics align with cloud computing.
- **B:** Cloud services still rely on physical infrastructure.
- **C:** Cloud networks can use private addressing.
- **D:** Service responsibilities vary; cloud does not remove all customer configuration.

**Further reading**

- [NIST SP 800-145: The NIST Definition of Cloud Computing](https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-145.pdf) — 2. The NIST Definition of Cloud Computing — Essential Characteristics; Deployment Models

---

## CCNA4-020 · Network Fundamentals

Objectives: 1.13.a, 1.13.b, 1.13.c, 1.13.d · matching · Applied

Match each switch observation with the operation it demonstrates. Use each operation once.

1. A fresh source address is added against the port where its frame arrived.
2. A silent host’s unused dynamic mapping disappears after the configured timer.
3. A destination absent from the table is sent through the other forwarding ports of its VLAN.
4. A destination table entry identifies one different egress port.

- **A.** Unknown-unicast flooding
- **B.** Dynamic source learning
- **C.** Aging
- **D.** Known-unicast forwarding

**Answer: 1 → B; 2 → C; 3 → A; 4 → D**

Source observations maintain the table, and destination lookups use it. Unknown destinations and expired entries explain why flooding may occur.

**Option explanations**

- **A:** An absent destination entry causes forwarding to eligible other VLAN ports.
- **B:** The ingress source location is recorded.
- **C:** An unused dynamic mapping expires.
- **D:** A present destination mapping selects a particular output port.

**Further reading**

- [Configuring MAC Address Tables](https://www.cisco.com/c/en/us/td/docs/switches/datacenter/nexus5500/sw/layer2/7x/b_5500_Layer2_Config_7x/config_mac_address_tables.pdf) — Information About MAC Addresses (page 1); Configuring the Aging Time for the MAC Table (page 2)

---

## CCNA4-021 · Network Access

Objectives: 2.1.c, 2.2.c · single · Challenge

The switch-to-router trunk carries native VLAN 88 untagged, with native tagging disabled. R1 should be the gateway for VLAN 88, but the shown subinterface expects tagged traffic. What change aligns the router with the existing trunk design?

```text
interface GigabitEthernet0/0.88
 encapsulation dot1Q 88
 ip address 10.88.0.1 255.255.255.0
```

- **A.** Place a VLAN 88 access command on the router’s routed subinterface.
- **B.** Change the subnet mask to /16.
- **C.** Rename the subinterface Gi0/0.1 without changing encapsulation.
- **D.** Use encapsulation dot1Q 88 native on Gi0/0.88.

**Answer: D**

The router and switch must agree on whether this VLAN is tagged. The dot1Q native keyword matches the stated untagged gateway design.

**Option explanations**

- **A:** A routed subinterface uses dot1Q encapsulation, not switchport access membership.
- **B:** An IP mask does not repair a tagging mismatch.
- **C:** The suffix does not change frame classification.
- **D:** The native keyword binds untagged traffic to this router subinterface.

**Further reading**

- [Configure Inter VLAN Routing with the Use of an External Router](https://www.cisco.com/c/en/us/support/docs/lan-switching/inter-vlan-routing/14976-50.html) — Configure — Configurations; Sample Command Output — Cisco Router
- [VLAN Configuration Guide, Cisco IOS XE 17.15.x — Configuring VLAN Trunks](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst9300/software/release/17-15/configuration_guide/vlan/b_1715_vlan_9300_cg/configuring_vlan_trunks.html) — Allowed VLANs on a Trunk; Configuring the Native VLAN for Untagged Traffic

---

## CCNA4-022 · Network Access

Objectives: 2.1.a · single · Applied

Two ordinary untagged PCs connect to access ports assigned to VLANs 12 and 22. There is no router, SVI routing, or other connection between the VLANs. Giving both PCs addresses in 192.0.2.0/24 will have which consequence?

- **A.** The PCs communicate directly because equal masks bypass VLAN checks.
- **B.** The switch automatically merges both VLANs into one subnet.
- **C.** The PCs remain in separate Layer 2 broadcast domains.
- **D.** The switch converts both access ports into a trunk.

**Answer: C**

Layer 2 segmentation remains in effect even with overlapping host address plans. An address change alone cannot repair a VLAN separation problem.

**Option explanations**

- **A:** They still need Layer 2 reachability to resolve and exchange local frames.
- **B:** IP address configuration does not rewrite VLAN membership.
- **C:** Matching IP prefixes do not merge VLANs or deliver ARP across them.
- **D:** Host addressing does not negotiate trunk mode.

**Further reading**

- [VLAN Configuration Guide, Cisco IOS XE 17.15.x — Configuring VLANs](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst9300/software/release/17-15/configuration_guide/vlan/b_1715_vlan_9300_cg/configuring_vlans.html) — Supported VLANs; Deleting a VLAN; VLAN Port Membership Modes

---

## CCNA4-023 · Network Access

Objectives: 2.1 · multiple · Foundation

A design requests normal-range Ethernet VLANs for two new departments on Catalyst switches. Which TWO proposed VLAN IDs are both ordinary usable choices within that range? Select TWO.

- **A.** 100
- **B.** 2000
- **C.** 1002
- **D.** 1000
- **E.** 4095

**Answer: A, D**

Normal-range numbering extends through 1005, but not every number is an ordinary configurable Ethernet VLAN. Distinguish usable values from legacy reservations.

**Option explanations**

- **A:** VLAN 100 lies within the normal range and is not one of the reserved legacy defaults.
- **B:** VLAN 2000 is extended range, outside the stated normal-range requirement.
- **C:** Cisco reserves VLANs 1002-1005 for legacy media defaults.
- **D:** VLAN 1000 is within the normal range of 1-1005 and is usable for Ethernet.
- **E:** 4095 is a reserved 802.1Q VID and not a usable ordinary VLAN.

**Further reading**

- [VLAN Configuration Guide, Cisco IOS XE 17.15.x — Configuring VLANs](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst9300/software/release/17-15/configuration_guide/vlan/b_1715_vlan_9300_cg/configuring_vlans.html) — Supported VLANs; Deleting a VLAN; VLAN Port Membership Modes

---

## CCNA4-024 · Network Access

Objectives: 2.2.a · single · Applied

A maintenance engineer must remove VLAN 55 from a trunk without changing the allowed status of VLANs 15 and 35. Which command is appropriate?

```text
interface GigabitEthernet1/0/45
 switchport mode trunk
 switchport trunk allowed vlan 15,35,55
```

- **A.** switchport access vlan 15
- **B.** switchport trunk allowed vlan remove 55
- **C.** no vlan 55
- **D.** switchport trunk allowed vlan 55

**Answer: B**

Modify the specific trunk policy instead of deleting a VLAN globally. The command’s add/remove semantics matter during incremental changes.

**Option explanations**

- **A:** An access VLAN command does not edit an operational trunk’s allowed list.
- **B:** The remove form subtracts 55 while retaining the existing other entries.
- **C:** Deleting the VLAN is a switch-wide operation, not a scoped change to this trunk.
- **D:** This replaces the list with only VLAN 55, reversing the requirement.

**Further reading**

- [VLAN Configuration Guide, Cisco IOS XE 17.15.x — Configuring VLAN Trunks](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst9300/software/release/17-15/configuration_guide/vlan/b_1715_vlan_9300_cg/configuring_vlan_trunks.html) — Allowed VLANs on a Trunk; Configuring the Native VLAN for Untagged Traffic

---

## CCNA4-025 · Network Access

Objectives: 2.2.a, 2.2.b, 2.2.c · matching · Applied

Match each trunk setting to the property it controls. Native tagging is disabled. Use each answer once.

1. Carry multiple VLANs using a statically selected trunk mode
2. Restrict admitted VLANs to the explicitly listed IDs
3. Classify untagged incoming data as VLAN 90
4. Stop sending Cisco trunk-negotiation messages

- **A.** switchport trunk native vlan 90
- **B.** switchport mode trunk
- **C.** switchport nonegotiate
- **D.** switchport trunk allowed vlan 40,50

**Answer: 1 → B; 2 → D; 3 → A; 4 → C**

Trunk operation, VLAN admission, untagged classification, and negotiation are independent settings. One does not automatically supply the others.

**Option explanations**

- **A:** Sets the VLAN used for ordinary untagged data frames.
- **B:** Forces the interface to operate as a trunk.
- **C:** Suppresses DTP transmission; the peer must be configured appropriately.
- **D:** Limits which VLANs this trunk admits.

**Further reading**

- [VLAN Configuration Guide, Cisco IOS XE 17.15.x — Configuring VLAN Trunks](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst9300/software/release/17-15/configuration_guide/vlan/b_1715_vlan_9300_cg/configuring_vlan_trunks.html) — Allowed VLANs on a Trunk; Configuring the Native VLAN for Untagged Traffic

---

## CCNA4-026 · Network Access

Objectives: 2.3 · single · Applied

A technician unplugs a discovered neighbor. Shortly afterward the old CDP entry is still displayed with a decreasing holdtime. No new advertisements arrive. What is the most reasonable interpretation?

- **A.** The displayed entry can remain until its hold timer expires.
- **B.** CDP proves the disconnected cable still forwards user traffic.
- **C.** The holdtime is the Ethernet propagation delay.
- **D.** CDP must be routed through the Internet from that neighbor.

**Answer: A**

Read cached discovery output alongside interface state and elapsed time. An aging entry can outlast the last received advertisement.

**Option explanations**

- **A:** Discovery tables are cached and do not inherently prove a live connection at every instant.
- **B:** A remaining cache entry is not current forwarding evidence.
- **C:** It represents remaining advertisement validity, not cable delay.
- **D:** CDP discovers directly attached Layer 2 neighbors.

**Further reading**

- [Network Management Configuration Guide, Cisco IOS XE 17.15.x — Configuring Cisco Discovery Protocol](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst9300/software/release/17-15/configuration_guide/nmgmt/b_1715_nmgmt_9300_cg/configuring_the_cisco_discovery_protocol.html) — Configuring Cisco Discovery Protocol; Monitoring and Maintaining Cisco Discovery Protocol

---

## CCNA4-027 · Network Access

Objectives: 2.4 · single · Applied

The shown LACP configuration uses channel-group 3 on SW-A and channel-group 8 on SW-B. All other parameters and physical connections are compatible. Why can this still form one channel between the switches?

```text
SW-A members: channel-group 3 mode active
SW-B members: channel-group 8 mode passive
```

- **A.** Only static mode on permits different group numbers.
- **B.** Channel-group numbers identify local logical interfaces and need not match across peers.
- **C.** Both switches automatically rename themselves to group 1.
- **D.** The bundle must fail because the numbers become VLAN tags.

**Answer: B**

A channel-group number is locally significant. Verify actual negotiation and member compatibility instead of assuming peer numbering must be identical.

**Option explanations**

- **A:** This local numbering principle also applies to LACP.
- **B:** LACP uses its protocol identifiers and member compatibility, not equality of local CLI group numbers.
- **C:** No such renaming is required or implied.
- **D:** Port-channel identifiers are not 802.1Q VLAN IDs.

**Further reading**

- [Layer 2 Configuration Guide, Cisco IOS XE 17.15.x — Configuring EtherChannels](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst9300/software/release/17-15/configuration_guide/lyr2/b_1715_lyr2_9300_cg/configuring_etherchannels.html) — LACP Modes; EtherChannel Configuration Guidelines; Load Balancing; Layer 3 EtherChannels; Hot-Standby Ports

---

## CCNA4-028 · Network Access

Objectives: 2.4 · multiple · Applied

A healthy two-member 10-Gb/s Layer 2 LACP bundle connects two switches. Both links are in the bundle and there is no minimum-link threshold. One member fails. Select TWO correct expectations.

- **A.** The remaining member can keep the logical connection operational.
- **B.** The remaining member must be assigned an IP address to forward.
- **C.** Available aggregate link capacity falls to 10 Gb/s.
- **D.** LACP guarantees zero packet loss for every active flow during failure.

**Answer: A, C**

A bundle can survive a member failure with less capacity. Redundancy must still be distinguished from guaranteed uninterrupted delivery.

**Option explanations**

- **A:** One surviving active member can sustain the aggregate under the stated conditions.
- **B:** This remains a Layer 2 channel without a new member IP requirement.
- **C:** The failed member no longer contributes its 10-Gb/s capacity.
- **D:** Detection and rehashing can cause transient loss; zero loss is not guaranteed.

**Further reading**

- [Layer 2 Configuration Guide, Cisco IOS XE 17.15.x — Configuring EtherChannels](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst9300/software/release/17-15/configuration_guide/lyr2/b_1715_lyr2_9300_cg/configuring_etherchannels.html) — LACP Modes; EtherChannel Configuration Guidelines; Load Balancing; Layer 3 EtherChannels; Hot-Standby Ports

---

## CCNA4-029 · Network Access

Objectives: 2.5.a · single · Applied

Distribution A is configured with base priority 24576 for VLAN 10 and 28672 for VLAN 20. Distribution B uses 28672 for VLAN 10 and 24576 for VLAN 20. All other switches use 32768 and remain connected. Which root placement results?

- **A.** Both are simultaneously root for VLAN 10.
- **B.** B is root for all VLANs because it wins VLAN 20.
- **C.** A is root for VLAN 10; B is root for VLAN 20.
- **D.** A is root for all VLANs because VLAN 10 is lower.

**Answer: C**

Per-VLAN spanning tree allows intentional root distribution. The lower priority wins independently for each VLAN.

**Option explanations**

- **A:** A connected converged VLAN instance selects one root.
- **B:** Winning one instance does not override another instance.
- **C:** Rapid PVST+ compares bridge IDs separately in each VLAN instance.
- **D:** The VLAN number does not make one instance control every other instance.

**Further reading**

- [Layer 2 Configuration Guide, Cisco IOS XE 17.15.x — Configuring Spanning Tree Protocol](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst9300/software/release/17-15/configuration_guide/lyr2/b_1715_lyr2_9300_cg/configuring_spanning_tree_protocol.html) — Spanning-Tree Topology and Bridge Protocol Data Units; Bridge ID, Device Priority, and Extended System ID; (Optional) Configuring a Secondary Root Device

---

## CCNA4-030 · Network Access

Objectives: 2.5.a, 2.5.b · single · Applied

SW-P and SW-Q share a segment for VLAN 70. SW-P’s root-path cost is 8 and SW-Q’s is 12; their root IDs agree. Which switch supplies the designated port on that segment?

- **A.** SW-P, because it advertises the lower path cost to the root.
- **B.** Neither, because only root bridges have designated ports.
- **C.** SW-Q, because the larger cost gives it higher priority.
- **D.** Both, because neither is the root bridge.

**Answer: A**

Designated-port election chooses the best advertised path on each segment. It is not limited to ports on the root bridge.

**Option explanations**

- **A:** The better root information wins the designated-port election on that segment.
- **B:** Nonroot bridges also supply designated ports on downstream segments.
- **C:** Lower path cost is preferred.
- **D:** A shared segment elects one designated port for the instance.

**Further reading**

- [Understand Rapid Spanning Tree Protocol (802.1w)](https://www.cisco.com/c/en/us/support/docs/lan-switching/spanning-tree-protocol/24062-146.html) — New Port States and Port Roles — Port States; Alternate and Backup Port Roles

---

## CCNA4-031 · Network Access

Objectives: 2.5.c, 2.5.d · single · Challenge

A Catalyst switch uses global spanning-tree portfast bpdufilter default. A port is operationally PortFast and has no explicit interface BPDU-filter command. What happens when that port receives a BPDU?

- **A.** It enters error-disable solely because global BPDU filtering is enabled.
- **B.** It always ignores the BPDU forever.
- **C.** It disables spanning tree for the entire switch.
- **D.** It loses PortFast operation and resumes normal STP BPDU processing.

**Answer: D**

Global PortFast BPDU filtering and unconditional interface filtering are not equivalent. This global mode can fall back to ordinary spanning-tree operation.

**Option explanations**

- **A:** The stated configuration is filtering, not BPDU guard.
- **B:** That describes explicit interface filtering more closely, not this global mode.
- **C:** The behavior concerns this affected port, not every interface.
- **D:** Global conditional filtering disables itself when the edge assumption is contradicted.

**Further reading**

- [Layer 2 Configuration Guide, Cisco IOS XE 17.15.x — Configuring Optional Spanning-Tree Features](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst9300/software/release/17-15/configuration_guide/lyr2/b_1715_lyr2_9300_cg/configuring_optional_spanning_tree_features.html) — PortFast; Bridge Protocol Data Unit Guard; Bridge Protocol Data Unit Filtering; Root Guard; Loop Guard

---

## CCNA4-032 · Network Access

Objectives: 2.5.d · single · Challenge

An access switch’s only intended path toward the distribution root has spanning-tree guard root configured. Superior root information arrives from the legitimate upstream switch, and user connectivity is lost. What design mistake explains the failure?

- **A.** Root guard was placed on a port that is supposed to accept a superior root path.
- **B.** The access switch must disable its VLAN database.
- **C.** The upstream switch must stop sending all BPDUs.
- **D.** Root guard should always be enabled on every root port.

**Answer: A**

Place root guard at boundaries where the root must not appear. Applying it to the sole legitimate upstream root path enforces the opposite of the design intent.

**Option explanations**

- **A:** Root guard deliberately prevents that upstream path from becoming the root port.
- **B:** The root-inconsistent behavior is unrelated to deleting VLANs.
- **C:** Suppressing legitimate topology information is not a sound repair.
- **D:** It is intended where superior root information must not be accepted.

**Further reading**

- [Enhance STP with Root Guard](https://www.cisco.com/c/en/us/support/docs/lan-switching/spanning-tree-protocol/10588-74.html) — Feature Description

---

## CCNA4-033 · Network Access

Objectives: 2.6 · single · Applied

A local-mode Cisco AP serves clients and performs brief off-channel measurements between service intervals. Does observing those scans establish that it is in dedicated monitor mode?

- **A.** No; local mode cannot exchange information with a WLC.
- **B.** Yes; monitor mode is required for every SSID advertisement.
- **C.** No; client-serving local mode can also perform background RF monitoring.
- **D.** Yes; any RF measurement disables ordinary associations.

**Answer: C**

Identify an AP mode by its operating role, not one isolated observation. Background RF work can coexist with normal local-mode client service.

**Option explanations**

- **A:** Local-mode APs are controller managed and tunnel their traffic.
- **B:** Monitor mode is not the ordinary SSID-serving mode.
- **C:** Background measurements do not make the AP a dedicated monitor.
- **D:** Client-serving APs also support radio-management measurements.

**Further reading**

- [Cisco Wireless Controller Configuration Guide, Release 8.5 — Managing APs](https://www.cisco.com/c/en/us/td/docs/wireless/controller/8-5/config-guide/b_cg85/managing_aps.html) — AP Modes: client-serving and network management modes

---

## CCNA4-034 · Network Access

Objectives: 2.6 · single · Applied

A FlexConnect AP locally switches a PSK WLAN and already has valid client sessions. The WLC WAN path fails while the AP, local VLAN, and local server remain healthy. Which design property can preserve those local client-to-server flows?

- **A.** The local server automatically becomes a WLC.
- **B.** The wireless clients become Ethernet trunk ports.
- **C.** Their data path leaves the AP locally instead of traversing the failed controller path.
- **D.** The AP forwards all traffic through the failed CAPWAP data tunnel.

**Answer: C**

The stated existing sessions can use the surviving local data path. New authentication and other services still depend on their separately configured requirements.

**Option explanations**

- **A:** Ordinary servers do not assume controller roles.
- **B:** Client access does not transform into interswitch trunking.
- **C:** Local switching removes the WLC WAN path from these existing local data flows.
- **D:** A failed remote tunnel cannot carry those packets.

**Further reading**

- [Cisco Wireless Controller Configuration Guide, Release 8.10 — FlexConnect](https://www.cisco.com/c/en/us/td/docs/wireless/controller/8-10/config-guide/b_cg810/flexconnect.html) — Configuring the Switch at a Remote Site; Configuring an Access Point for FlexConnect (GUI)

---

## CCNA4-035 · Network Access

Objectives: 2.7 · single · Applied

An AP’s management address must remain in untagged native VLAN 100 while a locally switched WLAN uses tagged VLAN 200. The AP switch port is currently access VLAN 100. Which physical-link design is missing?

- **A.** A second console cable for VLAN 200
- **B.** A matching trunk that carries native 100 and tagged 200
- **C.** A switchport voice vlan 200 command as the wireless VLAN design
- **D.** A different SSID for every TCP session

**Answer: B**

The AP’s local VLAN egress requires corresponding switch infrastructure. Retain the management classification while adding a real tagged client path.

**Option explanations**

- **A:** Console transport does not carry ordinary client Ethernet traffic.
- **B:** The link must carry both untagged management and a distinct tagged local client VLAN.
- **C:** Voice VLAN is for a phone attachment and does not define this AP trunk.
- **D:** SSID naming does not supply wired VLAN carriage.

**Further reading**

- [Cisco Wireless Controller Configuration Guide, Release 8.10 — FlexConnect](https://www.cisco.com/c/en/us/td/docs/wireless/controller/8-10/config-guide/b_cg810/flexconnect.html) — Configuring the Switch at a Remote Site; Configuring an Access Point for FlexConnect (GUI)
- [VLAN Configuration Guide, Cisco IOS XE 17.15.x — Configuring VLAN Trunks](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst9300/software/release/17-15/configuration_guide/vlan/b_1715_vlan_9300_cg/configuring_vlan_trunks.html) — Allowed VLANs on a Trunk; Configuring the Native VLAN for Untagged Traffic

---

## CCNA4-036 · Network Access

Objectives: 2.7 · single · Applied

A technician connects an AireOS WLC service port where the design calls for a distribution-system uplink. Why is the service-port connection unsuitable for ordinary centrally switched WLAN client traffic?

- **A.** The service port is intended for out-of-band management, not the controller’s normal client data uplink.
- **B.** WLAN traffic is delivered over the console instead.
- **C.** Every service port automatically supports all VLAN trunks.
- **D.** A controller has no wired client-data attachment.

**Answer: A**

Controller ports have different functions. Verify the physical port role before diagnosing higher-layer WLAN settings.

**Option explanations**

- **A:** Distribution ports attach the controller’s client data interfaces to the wired network.
- **B:** The console provides local administration, not client data forwarding.
- **C:** Its management role is not equivalent to a normal distribution trunk.
- **D:** Centrally switched WLANs require a wired distribution attachment.

**Further reading**

- [Cisco Wireless Controller Configuration Guide, Release 8.10 — Ports and Interfaces](https://www.cisco.com/c/en/us/td/docs/wireless/controller/8-10/config-guide/b_cg810/ports_and_interfaces.html) — Restrictions on Link Aggregation; Configuring Neighbor Devices to Support Link Aggregation

---

## CCNA4-037 · Network Access

Objectives: 2.8 · single · Applied

An audit requires encrypted browser administration and forbids cleartext web sessions. The device currently exposes both HTTP and HTTPS. What action directly meets the transport requirement?

- **A.** Disable HTTP while retaining a correctly configured HTTPS service.
- **B.** Keep HTTP but use a longer administrator password.
- **C.** Use TACACS+ while leaving HTTP enabled.
- **D.** Rename the HTTP URL to include secure in the hostname.

**Answer: A**

Authentication policy and session transport protection are different controls. Use the encrypted web service and remove the prohibited cleartext service.

**Option explanations**

- **A:** HTTPS protects the browser session; disabling HTTP removes the cleartext alternative.
- **B:** Password length does not encrypt an HTTP session.
- **C:** Centralized AAA does not itself encrypt the operator’s HTTP transport.
- **D:** A name does not change the protocol or add TLS.

**Further reading**

- [Cisco Wireless Controller Configuration Guide, Release 8.10 — Administration of Controller](https://www.cisco.com/c/en/us/td/docs/wireless/controller/8-10/config-guide/b_cg810/administration_of_cisco_wlc.html) — Logging on to the Controller CLI; Enabling Web and Secure Web Modes (GUI); Enabling Web and Secure Web Modes (CLI)

---

## CCNA4-038 · Network Access

Objectives: 2.9 · single · Applied

A handheld with a correct static address authenticates to an AireOS WLAN but cannot pass normal IPv4 traffic. DHCP clients work. The GUI shows DHCP Addr. Assignment = Required. What is the first policy-consistent fix if static addressing is not required for this handheld?

| WLAN field | Value |
| --- | --- |
| Status | Enabled |
| DHCP Addr. Assignment | Required |
| WPA2 authentication | Successful |
| Client IPv4 method | Manual static |

- **A.** Rename the SSID to the static IP address.
- **B.** Change the WLAN’s QoS profile to Platinum.
- **C.** Configure the handheld to obtain its address through DHCP.
- **D.** Disable all encryption on the WLAN.

**Answer: C**

A correct static subnet alone does not satisfy a policy requiring observed DHCP assignment. Match the client’s addressing method to the applied advanced setting.

**Option explanations**

- **A:** An SSID does not serve as an address-assignment exchange.
- **B:** Priority selection does not satisfy DHCP enforcement.
- **C:** This satisfies the WLAN’s explicit DHCP-enforcement policy.
- **D:** Authentication already works; encryption removal does not meet the address policy.

**Further reading**

- [Cisco Wireless Controller Configuration Guide, Release 8.10 — DHCP](https://www.cisco.com/c/en/us/td/docs/wireless/controller/8-10/config-guide/b_cg810/dhcp.html) — Configuring DHCP; DHCP Address Assignment Required

---

## CCNA4-039 · Network Access

Objectives: 2.9 · single · Applied

An AireOS WLAN is configured with WMM Policy = Required. A legacy client does not support WMM. What consequence should the engineer expect from this compatibility policy?

- **A.** The client receives the controller’s management IP address.
- **B.** The client automatically gains WMM support from the controller.
- **C.** The SSID changes to the name of the QoS profile.
- **D.** The non-WMM client cannot associate to this WLAN under the required policy.

**Answer: D**

Required and allowed are different admission choices. Verify device capability before enforcing a WLAN-wide feature requirement.

**Option explanations**

- **A:** WMM is a QoS capability policy, not address assignment.
- **B:** The AP cannot add an unsupported client protocol capability.
- **C:** WMM requirements do not rename the network.
- **D:** Required permits WMM-capable clients rather than treating WMM as optional.

**Further reading**

- [Cisco Wireless Controller Configuration Guide, Release 8.10 — Radio Bands](https://www.cisco.com/c/en/us/td/docs/wireless/controller/8-10/config-guide/b_cg810/radio_bands.html) — Configuring the 802.11n Parameters (GUI), Step 5 — WMM Policy

---

## CCNA4-040 · Network Access

Objectives: 2.9 · multiple · Applied

A new AireOS WLAN must advertise the exact client network name Plant-Guest and use the standard best-effort profile. The draft GUI uses SSID Plant-Guests and QoS Gold. Select TWO corrections.

- **A.** Change only Profile Name to Plant-Guest.
- **B.** Change QoS to Bronze.
- **C.** Change QoS to Silver.
- **D.** Change SSID to Plant-Guest.

**Answer: C, D**

Interpret client-visible fields separately from administrative labels. The SSID and the profile’s service class each need to match the requirement.

**Option explanations**

- **A:** The administrative profile name does not replace the SSID.
- **B:** Bronze is background rather than best effort.
- **C:** Silver is the standard best-effort profile.
- **D:** Clients configured for the required string must find that exact SSID.

**Further reading**

- [Cisco Wireless Controller Configuration Guide, Release 8.10 — WLANs](https://www.cisco.com/c/en/us/td/docs/wireless/controller/8-10/config-guide/b_cg810/wlans.html) — Prerequisites for WLANs; Enabling and Disabling WLANs (GUI); Editing WLAN SSID or Profile Name for WLANs (GUI)
- [Cisco Wireless Controller Configuration Guide, Release 8.10 — Wireless Quality of Service](https://www.cisco.com/c/en/us/td/docs/wireless/controller/8-10/config-guide/b_cg810/wireless_quality_of_service.html) — QoS Profiles; Configuring QoS Profiles (GUI); Assigning a QoS Profile to a WLAN (GUI)

---

## CCNA4-041 · IP Connectivity

Objectives: 3.1.a, 3.1.f · single · Applied

The routing table uses D for one route and O for another. Both bracketed metrics happen to be 20. What can the engineer conclude about their path quality?

- **A.** Both protocols share the same administrative distance because metrics match.
- **B.** Both paths contain exactly 20 routers.
- **C.** The equal numbers alone do not make the two protocols’ paths equivalent.
- **D.** Both paths necessarily have equal latency.

**Answer: C**

Interpret a metric according to its routing source. Numeric equality across different metric systems does not establish equivalent performance.

**Option explanations**

- **A:** Distance is a separate bracket field and source preference.
- **B:** Neither the displayed EIGRP metric nor OSPF cost is a universal hop count.
- **C:** EIGRP and OSPF use different metric definitions.
- **D:** These metric numbers are not end-to-end latency measurements.

**Further reading**

- [Understand Administrative Distance](https://www.cisco.com/c/en/us/support/docs/ip/border-gateway-protocol-bgp/15986-admin-distance.html) — RIB Route Comparison; Route Installation; Default AD Values

---

## CCNA4-042 · IP Connectivity

Objectives: 3.1.b, 3.1.c · single · Foundation

An inventory system labels a route with mask 255.255.248.0 as /24. Which correction accurately describes that mask?

- **A.** /23, covering two aligned third-octet values
- **B.** /29, covering eight fourth-octet addresses
- **C.** /20, covering sixteen aligned third-octet values
- **D.** /21, covering eight aligned third-octet values

**Answer: D**

The position of the partial mask octet matters. Moving 248 from the third to the fourth octet changes /21 to /29.

**Option explanations**

- **A:** A /23 uses 255.255.254.0.
- **B:** A /29 uses 255.255.255.248, with 248 in a different octet.
- **C:** A /20 uses 255.255.240.0.
- **D:** The mask has 21 one bits and an eight-value third-octet block.

**Further reading**

- [RFC 1812: Requirements for IP Version 4 Routers](https://www.rfc-editor.org/rfc/rfc1812.html) — 5.2.4 Determining the Next Hop Address

---

## CCNA4-043 · IP Connectivity

Objectives: 3.2.a · single · Challenge

An installed discard route and a default are shown. All forwarding entries are usable. What happens to traffic for 10.120.70.5?

```text
S 10.120.0.0/16 [200/0] is directly connected, Null0
S* 0.0.0.0/0 [1/0] via 192.0.2.2
```

- **A.** It is discarded by the matching Null0 route.
- **B.** It falls through to the default because Null0 has no neighbor.
- **C.** It is sent to 192.0.2.2 because distance 1 beats 200.
- **D.** It is flooded until a host answers ARP.

**Answer: A**

Destination specificity also applies to discard routes. A default is not a second try after the selected route deliberately drops a packet.

**Option explanations**

- **A:** The /16 discard route is more specific than the default.
- **B:** A selected discard route does not fall through to a less specific route.
- **C:** These different prefix lengths coexist; forwarding chooses the longer match.
- **D:** Null0 intentionally discards; it does not perform neighbor discovery.

**Further reading**

- [Configure Route Selection for Routers](https://www.cisco.com/c/en/us/support/docs/ip/enhanced-interior-gateway-routing-protocol-eigrp/8651-21.html) — Build the Routing Table; Make Forwarding Decisions
- [Configure a Next Hop IP Address for Static Routes](https://www.cisco.com/c/en/us/support/docs/dial-access/floating-static-route/118263-technote-nexthop-00.html) — Background Information; Floating Static Route Example

---

## CCNA4-044 · IP Connectivity

Objectives: 3.2.b · single · Applied

An OSPF route with distance 110 disappears when a valid static for the exact same prefix is added at distance 1. The OSPF adjacency remains Full. Which explanation fits?

- **A.** The static won RIB installation without requiring OSPF adjacency failure.
- **B.** Full OSPF adjacency guarantees every OSPF candidate appears in the RIB.
- **C.** Adding a static automatically resets the OSPF router ID.
- **D.** OSPF’s metric must have become infinite.

**Answer: A**

Neighbor health and route installation answer different questions. OSPF may retain valid information even when another source supplies the installed route.

**Option explanations**

- **A:** Route-source preference can hide a valid OSPF candidate from the main table.
- **B:** A competing preferred source can prevent a candidate’s installation.
- **C:** Static route configuration does not normally replace the OSPF router ID.
- **D:** The specified distance difference explains the result without a metric failure.

**Further reading**

- [Understand Administrative Distance](https://www.cisco.com/c/en/us/support/docs/ip/border-gateway-protocol-bgp/15986-admin-distance.html) — RIB Route Comparison; Route Installation; Default AD Values

---

## CCNA4-045 · IP Connectivity

Objectives: 3.2.c · single · Applied

R1 has two valid intra-area OSPF next hops with costs 45 and 60 to the same /24. Maximum-paths is 4. Which route set should be selected by ordinary OSPF?

- **A.** Only the cost-60 path
- **B.** Neither path because the limit exceeds the number of neighbors
- **C.** Both paths because four paths are allowed
- **D.** Only the cost-45 path

**Answer: D**

First determine which paths satisfy equal-cost selection. Then apply the maximum-paths limit to the eligible set.

**Option explanations**

- **A:** Lower intra-area path cost is preferred.
- **B:** A maximum is not a minimum number of paths required.
- **C:** The limit does not authorize ordinary OSPF unequal-cost load sharing.
- **D:** Maximum-paths permits multiple equal-cost paths; it does not make unequal costs equal.

**Further reading**

- [Configure Route Selection for Routers](https://www.cisco.com/c/en/us/support/docs/ip/enhanced-interior-gateway-routing-protocol-eigrp/8651-21.html) — Build the Routing Table; Make Forwarding Decisions
- [RFC 2328: OSPF Version 2](https://www.rfc-editor.org/rfc/rfc2328.html) — 9.4 Electing the Designated Router; 10 The Neighbor Data Structure; 16 Calculation of the routing table

---

## CCNA4-046 · IP Connectivity

Objectives: 3.3.b · single · Applied

A static route uses the next-hop address 192.0.2.14. The only directly connected transit is 192.0.2.8/30, and no other route can resolve that next hop. What is the defect?

```text
C 192.0.2.8/30 is directly connected, GigabitEthernet0/0
Configured: ip route 10.181.0.0 255.255.0.0 192.0.2.14
```

- **A.** Changing the route metric to zero will add .14 to the subnet.
- **B.** The configured next hop is outside the connected /30 and is unresolved.
- **C.** A static next hop must always be a loopback address.
- **D.** Every /30 transit requires the next hop to end in .1.

**Answer: B**

Check next-hop reachability before administrative preference. An address that looks nearby numerically can still be outside the configured transit subnet.

**Option explanations**

- **A:** Metrics do not alter address membership or route resolution.
- **B:** 192.0.2.8/30 spans .8–.11; .14 belongs to a different block.
- **C:** A directly attached neighbor interface is a normal next hop.
- **D:** Usable host values depend on the particular subnet block.

**Further reading**

- [Configure a Next Hop IP Address for Static Routes](https://www.cisco.com/c/en/us/support/docs/dial-access/floating-static-route/118263-technote-nexthop-00.html) — Background Information; Floating Static Route Example
- [RFC 1812: Requirements for IP Version 4 Routers](https://www.rfc-editor.org/rfc/rfc1812.html) — 5.2.4 Determining the Next Hop Address

---

## CCNA4-047 · IP Connectivity

Objectives: 3.3.a, 3.3.b · single · Applied

A dual-stack router successfully routes IPv4 but drops IPv6 transit traffic. IPv6 addresses and static routes are configured; ipv6 unicast-routing is absent. What is the targeted global correction?

- **A.** Enable IPv4 proxy ARP.
- **B.** Enable ipv6 unicast-routing.
- **C.** Set the IPv6 static distance equal to the IPv4 distance.
- **D.** Translate every IPv6 address to an OSPFv2 router ID.

**Answer: B**

Addressing an interface does not by itself establish the required global forwarding behavior. Verify the IPv6 routing prerequisite separately from IPv4 success.

**Option explanations**

- **A:** ARP is not the IPv6 forwarding enable switch.
- **B:** This enables IPv6 packet forwarding on the router.
- **C:** Cross-family distance equality is not required for IPv6 routing.
- **D:** Router IDs do not replace IPv6 routing configuration.

**Further reading**

- [IPv6 Routing: Static Routing — Cisco IOS XE 17.x](https://www.cisco.com/c/en/us/td/docs/routers/ios/config/17-x/ip-routing/b-ip-routing/m_ip6-route-static-xe.html) — Recursive Static Routes; Fully Specified Static Routes; Floating Static Routes

---

## CCNA4-048 · IP Connectivity

Objectives: 3.3.c · multiple · Foundation

Which two destination fields describe exactly one host rather than a network containing other possible host addresses? Select two.

- **A.** 2001:db8:7::a/128
- **B.** 198.51.100.67 255.255.255.255
- **C.** 198.51.100.64 255.255.255.252
- **D.** 2001:db8:7::/64

**Answer: A, B**

Host routes fix the full address width in their protocol family. Address appearance alone does not make a prefix a host route.

**Option explanations**

- **A:** All 128 IPv6 bits are fixed.
- **B:** All 32 IPv4 bits are fixed.
- **C:** This /30 contains four IPv4 addresses.
- **D:** A /64 leaves 64 destination bits variable.

**Further reading**

- [Local Host Routes Installed in the Routing Table on Cisco IOS and Cisco IOS-XR](https://www.cisco.com/c/en/us/support/docs/ip/ip-routing/116264-technote-ios-00.html) — Cisco IOS Local Routes; Manually Configured Host Routes
- [IPv6 Routing: Static Routing — Cisco IOS XE 17.x](https://www.cisco.com/c/en/us/td/docs/routers/ios/config/17-x/ip-routing/b-ip-routing/m_ip6-route-static-xe.html) — Recursive Static Routes; Fully Specified Static Routes; Floating Static Routes

---

## CCNA4-049 · IP Connectivity

Objectives: 3.3.d · single · Applied

A router has a static backup /24 with distance 160 behind OSPF distance 110. A valid RIP route to the same /24, distance 120, also exists. OSPF withdraws its route. What should install next?

- **A.** Both RIP and static as equal-cost routes
- **B.** The RIP route
- **C.** The static route, because it was named the backup
- **D.** No route until OSPF recovers

**Answer: B**

A floating static is a backup relative to all competing candidates, not just the one the operator had in mind. Include every source in the preference analysis.

**Option explanations**

- **A:** Different distances are not made equal by sharing a destination.
- **B:** 120 is the lowest distance among the remaining valid candidates.
- **C:** The label does not outrank the available RIP source.
- **D:** Another valid source can take over after OSPF withdraws.

**Further reading**

- [Understand Administrative Distance](https://www.cisco.com/c/en/us/support/docs/ip/border-gateway-protocol-bgp/15986-admin-distance.html) — RIB Route Comparison; Route Installation; Default AD Values

---

## CCNA4-050 · IP Connectivity

Objectives: 3.3.b · single · Challenge

A route to 2001:db8:dead::/64 uses next hop 2001:db8:dead::1. No connected or other route resolves that next hop. Why is this invalid recursion?

- **A.** The route would need to resolve its own next hop through itself.
- **B.** The letters “dead” make the IPv6 prefix reserved for errors.
- **C.** IPv6 forbids static routes with global next-hop addresses.
- **D.** A /64 is too short for a static network route.

**Answer: A**

A recursive path must eventually reach independently established interface reachability. Reusing the target prefix to justify its own next hop is circular.

**Option explanations**

- **A:** Self-recursion cannot supply an independent usable exit interface.
- **B:** Hexadecimal spelling has no such routing meaning.
- **C:** Global next-hop addresses are valid when independently resolvable.
- **D:** A /64 is a common valid IPv6 network-route length.

**Further reading**

- [IPv6 Routing: Static Routing — Cisco IOS XE 17.x](https://www.cisco.com/c/en/us/td/docs/routers/ios/config/17-x/ip-routing/b-ip-routing/m_ip6-route-static-xe.html) — Recursive Static Routes; Fully Specified Static Routes; Floating Static Routes

---

## CCNA4-051 · IP Connectivity

Objectives: 3.3.a, 3.3.d · single · Applied

The displayed primary interface is manually shut down; the backup interface remains up with a reachable neighbor. Neither static uses permanent or tracking. Which configured entry should become the installed default?

```text
Gi0/0: 192.0.2.1/30
Gi0/1: 198.51.100.1/30
ip route 0.0.0.0 0.0.0.0 192.0.2.2
ip route 0.0.0.0 0.0.0.0 198.51.100.2 180
```

- **A.** Both defaults because their masks match
- **B.** Neither, because interface shutdown disables the entire router
- **C.** The default through 192.0.2.2 because distance 1 never changes
- **D.** The static through 198.51.100.2 at distance 180

**Answer: D**

Route validity is checked before preference. The lower-distance route must still have a usable resolving path.

**Option explanations**

- **A:** Equal prefix length alone is insufficient for both unequal-distance routes to install.
- **B:** Shutting one interface does not shut every independent interface.
- **C:** A lower distance cannot rescue an unresolved route.
- **D:** The preferred default loses its connected resolution; the remaining valid default can install.

**Further reading**

- [Configure a Next Hop IP Address for Static Routes](https://www.cisco.com/c/en/us/support/docs/dial-access/floating-static-route/118263-technote-nexthop-00.html) — Background Information; Floating Static Route Example
- [Understand Administrative Distance](https://www.cisco.com/c/en/us/support/docs/ip/border-gateway-protocol-bgp/15986-admin-distance.html) — RIB Route Comparison; Route Installation; Default AD Values

---

## CCNA4-052 · IP Connectivity

Objectives: 3.4.a · matching · Applied

Match each observed OSPF neighbor state to the next troubleshooting interpretation.

1. Init
2. ExStart
3. Loading
4. Full

- **A.** Bidirectional Hello communication is not yet established
- **B.** Adjacency databases are synchronized
- **C.** Database contents are being synchronized through requests
- **D.** Database exchange setup is underway

**Answer: 1 → A; 2 → D; 3 → C; 4 → B**

Neighbor states identify distinct stages of OSPF formation. Use the stage to focus the next evidence collection rather than treating every non-Full state identically.

**Option explanations**

- **A:** Init means a Hello was received without the receiver’s ID listed by the neighbor.
- **B:** Full is the completed adjacency state.
- **C:** Loading requests missing or newer LSAs identified during exchange.
- **D:** ExStart negotiates the master/slave relationship and database-description sequencing.

**Further reading**

- [Understand OSPF Neighbor States](https://www.cisco.com/c/en/us/support/docs/ip/open-shortest-path-first-ospf/13685-13.html) — OSPF Neighbor States

---

## CCNA4-053 · IP Connectivity

Objectives: 3.4.a · single · Applied

R1 has passive-interface default, then no passive-interface GigabitEthernet0/0. Both Gi0/0 and Gi0/1 are enabled in OSPF area 0. Where can it initiate an OSPF adjacency?

```text
router ospf 10
 network 10.40.0.0 0.0.255.255 area 0
 passive-interface default
 no passive-interface GigabitEthernet0/0
! Gi0/0=10.40.1.1/30; Gi0/1=10.40.2.1/24
```

- **A.** Both interfaces
- **B.** Neither interface
- **C.** Gi0/1 only
- **D.** Gi0/0 only

**Answer: D**

Apply the default and its exception together. The passive LAN can still be included in OSPF advertisements through the transit adjacency.

**Option explanations**

- **A:** Enabling an interface in the area does not override passive-interface default.
- **B:** The no passive-interface exception permits adjacency formation on Gi0/0.
- **C:** Gi0/1 has no exception from the passive default.
- **D:** The explicit exception enables Hellos there while Gi0/1 remains passive.

**Further reading**

- [Default Passive Interfaces — Cisco IOS XE 17.x](https://www.cisco.com/c/en/us/td/docs/routers/ios/config/17-x/ip-routing/b-ip-routing/m_iri-default-passive-interface.html) — Information About Default Passive Interfaces

---

## CCNA4-054 · IP Connectivity

Objectives: 3.4.a · single · Applied

Routers share an Ethernet LAN but one OSPF interface is in area 0 and the other is in area 1. All other settings match. Which statement explains their failure to form an adjacency?

- **A.** Their local OSPF process numbers must equal their area IDs.
- **B.** An Ethernet link can only run OSPF in area 1.
- **C.** Their subnet masks must be different to join different areas.
- **D.** OSPF requires matching area IDs on that shared link.

**Answer: D**

Single-area operation requires each intended adjacency interface to join that same area. Route redistribution is not a substitute for correcting a local area mismatch.

**Option explanations**

- **A:** Process numbers are locally significant and need not equal area IDs.
- **B:** Area 0 can operate over Ethernet.
- **C:** Changing subnet masks does not repair an area mismatch on the same link.
- **D:** The Hello area must agree for neighbors on the link.

**Further reading**

- [Troubleshoot OSPF Neighbor Problems](https://www.cisco.com/c/en/us/support/docs/ip/open-shortest-path-first-ospf/13699-29.html) — No State Revealed; Neighbors Stuck in Exstart/Exchange State

---

## CCNA4-055 · IP Connectivity

Objectives: 3.4.a · single · Applied

A packet capture shows valid Hellos from R1 entering R2. R2 lists R1 in Init. Captures also show R2’s Hellos are blocked before reaching R1. What should be repaired?

- **A.** The OSPF route metric on R2’s loopback
- **B.** R2’s DR priority by raising it to 255
- **C.** R1’s static default route
- **D.** The one-way OSPF packet path from R2 to R1

**Answer: D**

Init can expose one-way visibility. Follow the actual packet path in each direction instead of assuming an up Ethernet link permits all control traffic.

**Option explanations**

- **A:** Path cost does not restore blocked Hello communication.
- **B:** Election priority cannot substitute for bidirectional discovery.
- **C:** The peers already share a local segment; a default does not unblock these Hellos.
- **D:** R1 cannot acknowledge R2 in its Hello neighbor list until it hears R2.

**Further reading**

- [Understand OSPF Neighbor States](https://www.cisco.com/c/en/us/support/docs/ip/open-shortest-path-first-ospf/13685-13.html) — OSPF Neighbor States
- [Troubleshoot OSPF Neighbor Problems](https://www.cisco.com/c/en/us/support/docs/ip/open-shortest-path-first-ospf/13699-29.html) — No State Revealed; Neighbors Stuck in Exstart/Exchange State

---

## CCNA4-056 · IP Connectivity

Objectives: 3.4.b, 3.4.c · multiple · Applied

A design review compares a two-router OSPF point-to-point link with a four-router OSPF broadcast LAN. Which two distinctions are correct? Select two.

- **A.** Point-to-point OSPF requires all routers to have the same router ID.
- **B.** The point-to-point link has no DR/BDR election.
- **C.** Broadcast OSPF never exchanges Hellos.
- **D.** The broadcast LAN’s DROTHER routers need not be Full with each other.

**Answer: B, D**

Network type changes expected adjacency relationships. A healthy 2-Way state between two DROTHER routers is different from a stalled point-to-point adjacency.

**Option explanations**

- **A:** Router IDs still must be unique.
- **B:** That network type forms a direct adjacency without elected pseudonode roles.
- **C:** Hellos discover neighbors and maintain election-related state.
- **D:** DROTHER pairs normally stay 2-Way while synchronizing with DR and BDR.

**Further reading**

- [RFC 2328: OSPF Version 2](https://www.rfc-editor.org/rfc/rfc2328.html) — 9.4 Electing the Designated Router; 10 The Neighbor Data Structure; 16 Calculation of the routing table
- [Understand OSPF Neighbor States](https://www.cisco.com/c/en/us/support/docs/ip/open-shortest-path-first-ospf/13685-13.html) — OSPF Neighbor States

---

## CCNA4-057 · IP Connectivity

Objectives: 3.4.c · single · Challenge

The DR fails on a broadcast segment where the existing BDR has priority 10 and a DROTHER has priority 200. Both survivors are healthy. Who becomes DR after the old DR is declared down?

- **A.** No router unless all participants restart
- **B.** The priority-200 DROTHER automatically
- **C.** Whichever router has the lower interface IP address
- **D.** The existing BDR

**Answer: D**

Existing role state matters during a failure. Do not apply the initial-election comparison as if no BDR already existed.

**Option explanations**

- **A:** The election process handles DR loss without a mandatory full restart.
- **B:** This ignores the existing BDR role in the succession process.
- **C:** Lower interface IP is not this succession rule.
- **D:** The prepared BDR is promoted rather than displaced by a DROTHER’s higher priority.

**Further reading**

- [RFC 2328: OSPF Version 2](https://www.rfc-editor.org/rfc/rfc2328.html) — 9.4 Electing the Designated Router; 10 The Neighbor Data Structure; 16 Calculation of the routing table

---

## CCNA4-058 · IP Connectivity

Objectives: 3.4.d · single · Applied

An OSPF process begins with no explicit router ID and no loopbacks. All shown physical interfaces are up before startup. Which router ID is selected?

| Interface | IPv4 address |
| --- | --- |
| Gi0/0 | 192.0.2.250 |
| Gi0/1 | 198.51.100.20 |
| Gi0/2 | 10.255.255.254 |

- **A.** 198.51.100.20
- **B.** 10.255.255.254
- **C.** 192.0.2.250
- **D.** 0.0.0.0

**Answer: A**

Compare full 32-bit address values. Loopback preference is irrelevant here because no loopbacks exist at process startup.

**Option explanations**

- **A:** It is the highest available IPv4 interface address under the stated selection conditions.
- **B:** The comparison starts at the first octet, not the last.
- **C:** 198 in the first octet outranks 192 despite the larger last octet.
- **D:** Eligible interface addresses exist, so zero is not the chosen identity.

**Further reading**

- [Configuring OSPF — IP Routing: OSPF Configuration Guide](https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/iproute_ospf/configuration/xe-16/iro-xe-16-book/iro-cfg.html) — Enabling OSPF; Configuring OSPF Interface Parameters

---

## CCNA4-059 · IP Connectivity

Objectives: 3.4.d · single · Applied

An operator changes an active OSPF router-id in configuration and wants to verify the ID the running process actually uses before a maintenance restart. Which command is most direct?

- **A.** show running-config alone
- **B.** show mac address-table
- **C.** show ip dhcp binding
- **D.** show ip ospf

**Answer: D**

Compare effective state with intended configuration. Router-ID changes are a case where seeing the new command is not sufficient evidence that the running ID changed.

**Option explanations**

- **A:** Configuration intent may differ from the still-active ID before application.
- **B:** MAC learning does not report the OSPF process identifier.
- **C:** DHCP leases do not establish the router’s OSPF identity.
- **D:** It reports the running OSPF process and its current router ID.

**Further reading**

- [Configuring OSPF — IP Routing: OSPF Configuration Guide](https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/iproute_ospf/configuration/xe-16/iro-xe-16-book/iro-cfg.html) — Enabling OSPF; Configuring OSPF Interface Parameters

---

## CCNA4-060 · IP Connectivity

Objectives: 3.2.c · single · Applied

An OSPF interface has manual ip ospf cost 50. Its bandwidth is upgraded, and automatic reference-bandwidth calculations would now yield cost 10. What cost should ordinary IOS OSPF use until the manual setting changes?

- **A.** 60
- **B.** 10
- **C.** 50
- **D.** 0

**Answer: C**

Inspect configuration overrides when a physical upgrade does not alter the routing metric. Effective cost can remain independent of actual interface speed.

**Option explanations**

- **A:** OSPF does not add manual cost to calculated cost.
- **B:** The automatic result does not override a still-configured manual cost.
- **C:** An explicitly configured interface cost overrides automatic bandwidth calculation.
- **D:** A faster interface does not create a zero-cost transit link.

**Further reading**

- [Configuring OSPF — IP Routing: OSPF Configuration Guide](https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/iproute_ospf/configuration/xe-16/iro-xe-16-book/iro-cfg.html) — Enabling OSPF; Configuring OSPF Interface Parameters

---

## CCNA4-061 · IP Connectivity

Objectives: 3.4.a · single · Applied

A router’s OSPF neighbor is Full, but a specific remote LAN route is absent. Which next check most directly tests whether the LAN was included in OSPF at its source?

- **A.** Replace the local default gateway address on all hosts.
- **B.** Change the DR’s MAC address.
- **C.** Inspect OSPF activation and the LAN prefix at the advertising router.
- **D.** Assume the Full state guarantees every remote LAN is advertised.

**Answer: C**

Use the neighbor state to narrow the problem, not to declare all route coverage correct. Trace the missing prefix back to its originating interface and process.

**Option explanations**

- **A:** A missing remote advertisement is a router control-plane issue in this scenario.
- **B:** That does not correct missing OSPF activation on a remote LAN.
- **C:** A healthy transit adjacency cannot advertise a subnet that was never included.
- **D:** Adjacency synchronization and intended prefix coverage are distinct.

**Further reading**

- [Configuring OSPF — IP Routing: OSPF Configuration Guide](https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/iproute_ospf/configuration/xe-16/iro-xe-16-book/iro-cfg.html) — Enabling OSPF; Configuring OSPF Interface Parameters
- [Understand OSPF Neighbor States](https://www.cisco.com/c/en/us/support/docs/ip/open-shortest-path-first-ospf/13685-13.html) — OSPF Neighbor States

---

## CCNA4-062 · IP Connectivity

Objectives: 3.5 · single · Applied

A network uses one HSRP group per VLAN, with router A preferred on VLAN 10 and router B preferred on VLAN 20. What benefit does this arrangement provide under normal operation?

- **A.** Each packet in a single HSRP group is automatically split across both routers.
- **B.** Both routers must share one physical IP per interface.
- **C.** OSPF is automatically enabled on every VLAN.
- **D.** Different VLANs can use different active gateway routers.

**Answer: D**

Load distribution can be achieved across groups by assigning different preferred actives. That is different from promising simultaneous forwarding by both routers for one ordinary group.

**Option explanations**

- **A:** Ordinary HSRP has one active forwarder for a group.
- **B:** Distinct physical IPs remain necessary in the normal design.
- **C:** HSRP group configuration does not enable OSPF.
- **D:** Each group can elect its own active router while retaining redundancy.

**Further reading**

- [Understand the Hot Standby Router Protocol Features and Functionality](https://www.cisco.com/c/en/us/support/docs/ip/hot-standby-router-protocol-hsrp/9234-hsrpguidetoc.html) — HSRP Background and Operations; HSRP Operation

---

## CCNA4-063 · IP Connectivity

Objectives: 3.5 · single · Challenge

A standby gateway becomes active during a planned router outage. Basic routing works, but sessions dependent on stateful NAT on the failed router break. What does this demonstrate about FHRP by itself?

- **A.** The standby cannot have any working route.
- **B.** Virtual-gateway failover does not inherently replicate every stateful service session.
- **C.** FHRP is incapable of moving a virtual IP.
- **D.** The host must have changed its MAC address.

**Answer: B**

Preserving a first-hop identity is narrower than preserving all application or middlebox state. Acceptance tests should distinguish new connectivity from continuity of existing sessions.

**Option explanations**

- **A:** The stated successful basic routing contradicts that conclusion.
- **B:** NAT or firewall state synchronization requires separate supported mechanisms.
- **C:** Basic routing through the new active confirms that gateway movement occurred.
- **D:** Session loss does not imply a host MAC change.

**Further reading**

- [Understand the Hot Standby Router Protocol Features and Functionality](https://www.cisco.com/c/en/us/support/docs/ip/hot-standby-router-protocol-hsrp/9234-hsrpguidetoc.html) — HSRP Background and Operations; HSRP Operation
- [RFC 9568: Virtual Router Redundancy Protocol (VRRP) Version 3 for IPv4 and IPv6](https://www.rfc-editor.org/rfc/rfc9568.html) — 1 Introduction; 2 Required Features; 6 Protocol State Machine

---

## CCNA4-064 · IP Connectivity

Objectives: 3.5 · multiple · Applied

Which two checks directly test the intended HSRP behavior during a controlled active-router failure? Select two.

- **A.** Verify the two router hostnames are identical.
- **B.** Verify only that both chassis power LEDs were on before the test.
- **C.** Verify a host using the virtual gateway can still reach a routed test destination.
- **D.** Verify the standby assumes the active role and virtual address.

**Answer: C, D**

A useful failover test observes both the protocol role transition and packet delivery. Neither configuration review nor hardware power alone proves the intended service.

**Option explanations**

- **A:** Hostnames do not provide HSRP interoperability or service continuity.
- **B:** Power status does not demonstrate failover or continued forwarding.
- **C:** This checks actual data-plane service through the surviving path.
- **D:** This checks the first-hop state transition itself.

**Further reading**

- [Understand the Hot Standby Router Protocol Features and Functionality](https://www.cisco.com/c/en/us/support/docs/ip/hot-standby-router-protocol-hsrp/9234-hsrpguidetoc.html) — HSRP Background and Operations; HSRP Operation

---

## CCNA4-065 · IP Connectivity

Objectives: 3.1.g, 3.2.a · single · Applied

An engineer removes the only default route but leaves all connected and OSPF network routes intact. Which new failure should be expected under ordinary classless routing?

- **A.** Destinations without any remaining matching prefix become unreachable through this router.
- **B.** Every OSPF neighbor immediately changes to Down.
- **C.** Every directly attached neighbor becomes unreachable.
- **D.** All packets are forwarded to the lowest-numbered interface.

**Answer: A**

Default removal changes the catch-all coverage. It does not erase independently installed specific routes or their local interfaces.

**Option explanations**

- **A:** The deleted default had provided their only forwarding match.
- **B:** Direct adjacency maintenance does not inherently require a default.
- **C:** Connected routes are still present.
- **D:** No such fallback replaces an absent matching route.

**Further reading**

- [Configure Route Selection for Routers](https://www.cisco.com/c/en/us/support/docs/ip/enhanced-interior-gateway-routing-protocol-eigrp/8651-21.html) — Build the Routing Table; Make Forwarding Decisions
- [RFC 1812: Requirements for IP Version 4 Routers](https://www.rfc-editor.org/rfc/rfc1812.html) — 5.2.4 Determining the Next Hop Address

---

## CCNA4-066 · IP Services

Objectives: 4.1 · multiple · Applied

A router has a valid dynamic inside-source rule and unused pool addresses. Inside traffic enters GigabitEthernet0/0 and exits GigabitEthernet0/1, but neither interface has a NAT role configured. Which two interface commands complete the conventional inside/outside NAT design? Select two.

- **A.** ip nat outside on GigabitEthernet0/1
- **B.** ip nat inside on GigabitEthernet0/0
- **C.** ip nat inside on GigabitEthernet0/1
- **D.** ip helper-address on both interfaces
- **E.** ip nat outside on GigabitEthernet0/0

**Answer: A, B**

Conventional IOS inside-source NAT depends on the interfaces' inside/outside designations as well as the mapping rule. The roles follow the addressing realms, not which interface happens to have the larger number.

**Option explanations**

- **A:** This designates the interface facing the translated outside network.
- **B:** This designates the interface facing the original inside hosts.
- **C:** This reverses the stated outside interface role.
- **D:** A DHCP helper does not identify NAT direction.
- **E:** This reverses the stated inside interface role.

**Further reading**

- [IP Addressing Configuration Guide, Cisco IOS XE 17.x — Configuring NAT for IP Address Conservation](https://www.cisco.com/c/en/us/td/docs/routers/ios/config/17-x/ip-addressing/b-ip-addressing/m_iadnat-addr-consv-xe.html) — Inside source address translation; static and dynamic translations; monitoring NAT

---

## CCNA4-067 · IP Services

Objectives: 4.2 · single · Applied

Two routers log the same link outage with timestamps several minutes apart. Their time zones are already identical, but their clocks are manually set and drift independently. Which service addresses the underlying clock-alignment problem?

- **A.** NTP synchronization to a suitable shared time hierarchy
- **B.** Changing syslog severity to debugging
- **C.** Increasing SNMP polling frequency
- **D.** Adding a second DNS search suffix

**Answer: A**

Comparable timestamps require clocks that track a consistent time reference. The same displayed time zone does not ensure the underlying clocks remain synchronized.

**Option explanations**

- **A:** NTP adjusts device clocks against time sources, improving cross-device correlation.
- **B:** More messages do not align clocks.
- **C:** More samples do not synchronize device time.
- **D:** Name expansion does not correct clock drift.

**Further reading**

- [Use Best Practices for Network Time Protocol](https://www.cisco.com/c/en/us/support/docs/availability/high-availability/19643-ntpm.html) — NTP architecture; synchronization; verification
- [Setting Time and Calendar Services](https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/bsm/configuration/15-mt/bsm-15-mt-book/bsm-time-calendar-set.html) — Network Time Protocol; configuring NTP associations; monitoring NTP

---

## CCNA4-068 · IP Services

Objectives: 4.3 · single · Foundation

An application name must return an IPv6 address directly, while its IPv4 address remains in an A record. Which DNS record should be added for the IPv6 address?

- **A.** CNAME containing the literal IPv6 address
- **B.** MX
- **C.** PTR
- **D.** AAAA

**Answer: D**

Use the address record matching the address family. A and AAAA records can coexist for one host name and allow clients to obtain IPv4 and IPv6 addresses respectively.

**Option explanations**

- **A:** CNAME refers to another domain name, not an address literal.
- **B:** MX identifies a mail exchanger, not this application's IPv6 address.
- **C:** PTR supports reverse-name mapping rather than a direct IPv6 address answer.
- **D:** An AAAA record contains a 128-bit IPv6 address.

**Further reading**

- [RFC 3596 — DNS Extensions to Support IP Version 6](https://www.rfc-editor.org/rfc/rfc3596.html) — 2 AAAA resource record
- [RFC 1035 — Domain Names - Implementation and Specification](https://www.rfc-editor.org/rfc/rfc1035.html) — 3.3 Standard resource records; 4.1 Message format; 4.2 Transport

---

## CCNA4-069 · IP Services

Objectives: 4.3 · single · Applied

A DHCP server becomes unavailable just after a workstation receives a valid eight-hour lease. The workstation remains connected, its network parameters remain valid, and no conflict is detected. What should happen immediately?

- **A.** It must immediately stop all IPv4 traffic because DHCP is in every packet path.
- **B.** It can continue using its leased address while the lease remains valid.
- **C.** It must immediately replace its address with the default gateway's address.
- **D.** It can keep the leased address forever because the last ACK made it permanent.

**Answer: B**

DHCP allocates configuration with a lease lifetime; it does not forward the client's ordinary traffic. Failure to renew later matters, and the client must stop using the address once the lease expires.

**Option explanations**

- **A:** DHCP is not an intermediary for ordinary host data traffic.
- **B:** A brief server outage does not immediately revoke an existing valid lease.
- **C:** The router address is not a replacement host allocation.
- **D:** The lease remains time-limited and needs renewal or eventual cessation.

**Further reading**

- [RFC 2131 — Dynamic Host Configuration Protocol](https://www.rfc-editor.org/rfc/rfc2131.html) — 3.1 Address allocation; 4.3 Server behavior; 4.4 Client behavior

---

## CCNA4-070 · IP Services

Objectives: 4.4 · single · Challenge

A switch returns an SNMP counter value of 7,000,000 octets and, exactly 10 seconds later, 12,000,000 octets. The same counter instance is used, with no wrap, reset, or discontinuity. What average rate does this represent over the interval?

- **A.** 0.5 Mb/s
- **B.** 4 Mb/s
- **C.** 9.6 Mb/s
- **D.** 40 Mb/s

**Answer: B**

Counters are cumulative, so calculate a difference before calculating a rate. This constructed sample averages traffic over ten seconds and does not reveal instantaneous peaks.

**Option explanations**

- **A:** This treats octets per second as bits per second.
- **B:** The increase is 5,000,000 octets; multiplying by eight and dividing by ten gives 4,000,000 bits/s.
- **C:** This divides the final total by the interval instead of taking the counter difference.
- **D:** This omits division by the ten-second measurement interval.

**Further reading**

- [RFC 2863 — The Interfaces Group MIB](https://www.rfc-editor.org/rfc/rfc2863.html) — 3.1.6 Counter size; ifHCInOctets; ifCounterDiscontinuityTime

---

## CCNA4-071 · IP Services

Objectives: 4.5 · single · Applied

A router sends syslog using UDP to a collector. During congestion, several messages disappear even though the router generated them. Which limitation is relevant?

- **A.** UDP syslog does not acknowledge delivery or retransmit lost messages by itself.
- **B.** The absence of a message at the collector proves the event never occurred.
- **C.** A syslog facility code guarantees delivery independently of transport.
- **D.** Severity 0 messages automatically use a separate reliable transport.

**Answer: A**

A generated event and a collected event are different observations. Lossy transport can leave gaps, so absence at the collector alone does not establish absence on the device.

**Option explanations**

- **A:** The selected transport does not provide a reliable delivery exchange.
- **B:** Loss between generation and collection can explain that absence.
- **C:** A facility categorizes the message; it does not recover packet loss.
- **D:** Severity does not automatically change the configured UDP transport.

**Further reading**

- [RFC 5426 — Transmission of Syslog Messages over UDP](https://www.rfc-editor.org/rfc/rfc5426.html#section-4.3) — 4.1 Reliability; 4.3 Congestion Control

---

## CCNA4-072 · IP Services

Objectives: 4.6 · single · Challenge

Clients in VLAN 50 cannot obtain leases from a remote server. The server receives relayed requests with giaddr 10.50.0.1 and has the correct scope. Captures show replies leaving the server toward 10.50.0.1, but the server-side gateway has no route to 10.50.0.0/24. Which repair addresses the demonstrated fault?

- **A.** Move the helper to an unrelated WAN interface.
- **B.** Restore the return route to the relay's client-facing subnet.
- **C.** Replace every client address with the DHCP server's address.
- **D.** Replace the helper destination with 255.255.255.255.

**Answer: B**

Relay operation depends on both the forward request path and the server's return path to giaddr. The captures isolate a routing gap after the server has processed the request.

**Option explanations**

- **A:** The client broadcasts already reached the correct relay and server.
- **B:** The replies need to reach the giaddr address before the relay can deliver them to clients.
- **C:** That would create address conflicts and does not restore the return path.
- **D:** The server was already reached by its unicast address.

**Further reading**

- [IP Addressing: DHCP Configuration Guide, Cisco IOS XE Everest 16.6 — Configuring the Cisco IOS XE DHCP Relay Agent](https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/ipaddr_dhcp/configuration/xe-16-6/dhcp-xe-16-6-book/dhcp-relay-agent-xe.html) — Packet forwarding address; giaddr; specifying the packet forwarding address
- [RFC 2131 — Dynamic Host Configuration Protocol](https://www.rfc-editor.org/rfc/rfc2131.html) — 3.1 Address allocation; 4.3 Server behavior; 4.4 Client behavior

---

## CCNA4-073 · IP Services

Objectives: 4.7 · single · Applied

A traffic policy classifies a flow as excess but is configured to remark excess packets to a lower-priority DSCP and transmit them. An operator claims every policer must drop every excess packet. Which assessment is correct?

- **A.** The policy increases the link bandwidth to fit excess traffic.
- **B.** The claim is true; any packet identified as excess is always discarded.
- **C.** The policy is a shaper because it changes DSCP.
- **D.** The claim is false; a policer applies its configured actions and may remark rather than drop.

**Answer: D**

Metering determines whether traffic conforms; the policy determines the consequent action. A policer need not drop excess traffic, and remarking alone does not smooth it by buffering.

**Option explanations**

- **A:** Classification and remarking cannot increase the physical transmission rate.
- **B:** The stated conform/exceed actions determine what is done.
- **C:** Remarking a header does not introduce the delayed release characteristic of shaping.
- **D:** Policing can select different actions for traffic outside the profile.

**Further reading**

- [Compare Traffic Policing and Traffic Shaping to Limit Bandwidth](https://www.cisco.com/c/en/us/support/docs/quality-of-service-qos/qos-policing/19645-policevsshape.html) — Traffic policing and traffic shaping comparison
- [RFC 2475 — An Architecture for Differentiated Services](https://www.rfc-editor.org/rfc/rfc2475.html) — 2.3 Traffic classification and conditioning; 2.4 Per-hop behaviors

---

## CCNA4-074 · IP Services

Objectives: 4.8 · single · Applied

An IOS XE device has VTY lines 0–15. Lines 0–4 allow only SSH, but lines 5–15 still allow Telnet and SSH. All other SSH prerequisites are correct. What change is needed to enforce SSH-only access consistently?

- **A.** Apply transport input ssh to lines 5–15 as well.
- **B.** Increase the RSA modulus while leaving lines 5–15 unchanged.
- **C.** Set ip ssh version 2 without changing lines 5–15.
- **D.** Apply transport output ssh only to line 0.

**Answer: A**

A line-range mismatch can leave an alternate remote entry point open. The intended transport policy must cover the device's full usable VTY range.

**Option explanations**

- **A:** All VTY lines that can accept remote sessions must enforce the policy.
- **B:** Stronger keys do not disable Telnet on other lines.
- **C:** Selecting the SSH version does not remove a separately allowed Telnet transport.
- **D:** Outgoing line connections are not the incoming VTY access policy.

**Further reading**

- [Configure SSH on Routers](https://www.cisco.com/c/en/us/support/docs/security-vpn/secure-shell-ssh/4145-ssh.html) — SSH server prerequisites; SSHv2; VTY restrictions; show commands

---

## CCNA4-075 · IP Services

Objectives: 4.9 · single · Applied

A technician selects standard FTP for sending a router configuration containing credentials over a network they do not trust. No TLS, SSH, IPsec, or other protective tunnel is used. Which property matters most to this choice?

- **A.** Using TCP guarantees that no observer can read the transfer.
- **B.** FTP encrypts file contents automatically whenever a username is supplied.
- **C.** Standard FTP does not encrypt its control credentials or file contents.
- **D.** Changing to base TFTP would automatically encrypt the configuration.

**Answer: C**

Do not infer encryption from authentication or reliable transport. Protection requires an appropriate secure transfer mechanism or protected path; FTP with TLS is an extension beyond the standard FTP assumed here.

**Option explanations**

- **A:** TCP reliability does not imply confidentiality.
- **B:** Login and encryption are separate capabilities.
- **C:** The base protocol does not provide the required confidentiality.
- **D:** Base TFTP does not add encryption either.

**Further reading**

- [RFC 959 — File Transfer Protocol (FTP)](https://www.rfc-editor.org/rfc/rfc959.html) — 2.3 FTP model; 3.2 Data connections; 4.1 FTP commands
- [RFC 4217 — Securing FTP with TLS](https://www.rfc-editor.org/rfc/rfc4217.html) — 4 Session negotiation on the control port; 7 Data connection behavior

---

## CCNA4-076 · Security Fundamentals

Objectives: 5.1 · single · Applied

An attacker is sending exploit traffic at a vulnerable service. The vendor patch cannot be installed until tonight. A temporary interface ACL allows the service only from a controlled jump host. How should this change be described?

- **A.** It eliminates every possible attack path to the device.
- **B.** It proves the software defect has been removed.
- **C.** It mitigates exposure while the underlying software vulnerability remains.
- **D.** It converts the attack into ordinary authorized traffic.

**Answer: C**

A compensating access restriction can reduce risk during a patch window. Verification should establish the intended reachability change, while the actual defect still requires remediation.

**Option explanations**

- **A:** The stated ACL protects one path; other paths and authorized-host compromise remain possible.
- **B:** An ACL changes reachability, not the vulnerable implementation.
- **C:** The restricted path reduces opportunities but does not repair the defect.
- **D:** Filtering does not change an attacker’s intent or an exploit’s nature.

**Further reading**

- [RFC 4949: Internet Security Glossary, Version 2](https://www.rfc-editor.org/rfc/rfc4949.html) — Section 2: threat, vulnerability, exploit, and countermeasure

---

## CCNA4-077 · Security Fundamentals

Objectives: 5.2 · single · Applied

An equipment-room badge reader records entries, but the door is routinely propped open for deliveries. Which finding most directly explains why the physical access control is ineffective?

- **A.** The badge reader is beside the door.
- **B.** A camera records people entering the open doorway.
- **C.** Entry logs have timestamps.
- **D.** The door can be crossed without triggering its authorization check.

**Answer: D**

An installed control must actually govern entry. Delivery procedures must keep the controlled boundary effective instead of depending on a reader that can be bypassed.

**Option explanations**

- **A:** Its location alone does not cause the demonstrated failure.
- **B:** Recording may provide evidence, but it is the bypassed entry check that explains the prevention failure.
- **C:** Timestamps are useful evidence and are not the bypass.
- **D:** The open door bypasses the boundary enforced by the badge reader.

**Further reading**

- [NIST SP 800-53 Rev. 5: Security and Privacy Controls for Information Systems and Organizations](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-53r5.pdf) — AT-2, AT-3, PE-2, and PE-3: awareness, training, and physical access

---

## CCNA4-078 · Security Fundamentals

Objectives: 5.3 · single · Applied

AAA is disabled on this IOS switch, and local line authentication is working. Which username command grants the named account default level-15 privileges immediately after a successful local login?

```text
line vty 0 15
 login local
 transport input ssh
```

- **A.** username maint privilege 15 secret MaintenanceOnly!
- **B.** line vty 0 15
- **C.** enable secret MaintenanceOnly!
- **D.** username maint privilege 1 secret MaintenanceOnly!

**Answer: A**

An account’s configured privilege controls its initial EXEC privilege when local login uses that account. VTY line numbers and enable secrets have different roles.

**Option explanations**

- **A:** The privilege 15 attribute selects the initial privileged EXEC level.
- **B:** This selects a range of VTY lines; 15 here is a line number.
- **C:** This configures an enable credential, not the named account’s initial privilege.
- **D:** Level 1 is ordinary user EXEC rather than level 15.

**Further reading**

- [Catalyst 3750-X and 3560-X Configuration Guide: Configuring Switch-Based Authentication](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst3750x_3560x/software/release/15-0_2_se/configuration/guide/3750x_cg/swauthen.html) — Protecting Access to Privileged EXEC Commands; Configuring Username and Password Pairs

---

## CCNA4-079 · Security Fundamentals

Objectives: 5.4 · multiple · Applied

A password policy requires a minimum length and disallows predictable organization-related passwords. Which two proposed practices support this policy’s security purpose? Select two.

- **A.** Use a password manager to generate and retain unique long secrets.
- **B.** Share a single complex password through a public team page.
- **C.** Accept any short password if it contains a punctuation mark.
- **D.** Reject a password composed of the company name and a predictable year.

**Answer: A, D**

Length, unpredictability, and controlled handling work together. A visual mixture of character types does not make a predictable or widely exposed credential safe.

**Option explanations**

- **A:** This supports length and uniqueness without depending on memorable patterns.
- **B:** Public distribution defeats the credential’s secrecy.
- **C:** One symbol does not compensate for failure of the minimum-length requirement.
- **D:** An organization-specific predictable value remains weak despite extra characters.

**Further reading**

- [NIST SP 800-63B-4: Digital Identity Guidelines — Authentication and Authenticator Management](https://pages.nist.gov/800-63-4/sp800-63b.html) — Authentication factors; password verifiers; authenticator management

---

## CCNA4-080 · Security Fundamentals

Objectives: 5.5 · single · Applied

A company has two routed sites with many ordinary LAN hosts. It wants IPsec protection across the Internet without installing VPN clients on those hosts. Where should the site-to-site VPN terminate?

- **A.** At the two site gateways that route the selected LAN traffic.
- **B.** At every access-switch port independently.
- **C.** Only at each employee’s browser.
- **D.** At the public DNS servers used by both sites.

**Answer: A**

Site-to-site VPN gateways protect traffic for participating networks. End hosts can send ordinary routed IP packets while the gateways perform the tunnel processing.

**Option explanations**

- **A:** The gateways can apply IPsec on behalf of their attached networks.
- **B:** The stated requirement uses routed site gateways, not per-port IPsec clients.
- **C:** Browser sessions do not provide the required gateway-to-gateway network tunnel.
- **D:** Resolving names does not make DNS servers the sites’ VPN endpoints.

**Further reading**

- [RFC 4301: Security Architecture for the Internet Protocol](https://www.rfc-editor.org/rfc/rfc4301.html) — Sections 3, 4.1, 4.4.1: IPsec services, tunnel mode, and security policy

---

## CCNA4-081 · Security Fundamentals

Objectives: 5.6 · single · Applied

A stateless IOS extended ACL must permit SSH initiated by host 10.30.1.18 to server 192.0.2.18 and deny its other traffic through this interface. Which permit entry is precise for the initiation direction?

- **A.** permit ip host 10.30.1.18 host 192.0.2.18
- **B.** permit tcp host 10.30.1.18 host 192.0.2.18 eq 22
- **C.** permit tcp host 192.0.2.18 host 10.30.1.18 eq 22
- **D.** permit tcp host 10.30.1.18 eq 22 host 192.0.2.18

**Answer: B**

For a client-initiated connection, the known service is the destination port. Place eq 22 after the destination, with the correct source and destination hosts.

**Option explanations**

- **A:** This permits every IP protocol between the hosts, not just SSH.
- **B:** It fixes both hosts, TCP, and the destination service port.
- **C:** This reverses the initiating source and destination.
- **D:** This requires the client’s source port to be 22.

**Further reading**

- [Configure IP Access Lists](https://www.cisco.com/c/en/us/support/docs/security/ios-firewall/23602-confaccesslists.html) — ACL Concepts; Masks; Process ACLs; Apply ACLs; Extended ACLs

---

## CCNA4-082 · Security Fundamentals

Objectives: 5.7 · single · Applied

A switch port’s output reports Port Security: Enabled, Violation Mode: Protect, Maximum MAC Addresses: 1, and Total MAC Addresses: 1. A second source sends frames. No other feature is dropping traffic. Which observation is consistent with protect mode?

| Field | Value |
| --- | --- |
| Port Security | Enabled |
| Violation Mode | Protect |
| Maximum MAC Addresses | 1 |
| Total MAC Addresses | 1 |

- **A.** The second source is dropped while the approved source continues, without a port-security violation notification.
- **B.** The interface must become error-disabled.
- **C.** Both sources are forwarded because the maximum counts only destinations.
- **D.** The second source replaces the first immediately.

**Answer: A**

Protect enforces the secure-source limit but gives less violation visibility than restrict. The configured mode matters when interpreting a silent forwarding failure.

**Option explanations**

- **A:** Protect mode drops excess unknown sources without the restrict-mode notification behavior.
- **B:** That is shutdown behavior, not protect.
- **C:** Port security limits accepted source MAC addresses.
- **D:** The maximum does not establish automatic replacement.

**Further reading**

- [Catalyst 3750-X and 3560-X Configuration Guide: Configuring Port-Based Traffic Control](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst3750x_3560x/software/release/15-0_2_se/configuration/guide/3750x_cg/swtrafc.html) — Secure MAC Addresses; Security Violations; Port Security Aging

---

## CCNA4-083 · Security Fundamentals

Objectives: 5.8 · single · Applied

A network team replaces one shared login with individual accounts but leaves every account permitted to run every command. Which AAA improvement has clearly been made, and which separation still needs work?

- **A.** All accounts now have least privilege automatically.
- **B.** Identity attribution improves; differentiated command authorization still needs configuration.
- **C.** Authentication is no longer required for individual accounts.
- **D.** Accounting is unnecessary once usernames are unique.

**Answer: B**

Separate accounts help identify who is accessing the device. Permissions and accounting remain distinct design and verification tasks.

**Option explanations**

- **A:** Individual account creation does not by itself restrict commands.
- **B:** Individual identity can distinguish sessions, but the described permissions remain identical.
- **C:** Each claimed individual identity still requires verification.
- **D:** Individual accounts still support separate authentication, revocation, and authorization. Retained accounting records are additionally needed to attribute past actions.

**Further reading**

- [RFC 8907: The Terminal Access Controller Access-Control System Plus (TACACS+) Protocol](https://www.rfc-editor.org/rfc/rfc8907.html) — Sections 5, 6, and 7: authentication, authorization, and accounting

---

## CCNA4-084 · Security Fundamentals

Objectives: 5.9 · single · Applied

A WLAN is using WPA2-Personal with a shared passphrase. Management now requires each employee to authenticate with a separately revocable enterprise identity. Which change addresses the identity requirement?

- **A.** Replace AES with TKIP while retaining the PSK.
- **B.** Keep the shared PSK and reduce transmit power.
- **C.** Keep the shared PSK but hide the SSID.
- **D.** Adopt WPA2-Enterprise with an appropriate 802.1X authentication service.

**Answer: D**

Personal and Enterprise describe different authentication arrangements. The same shared secret cannot provide independent per-user revocation simply by changing radio settings.

**Option explanations**

- **A:** A cipher downgrade does not alter the shared credential model.
- **B:** RF coverage changes do not provide separately revocable identities.
- **C:** SSID visibility does not create individual credentials.
- **D:** Enterprise authentication can use individual identities instead of one shared PSK.

**Further reading**

- [Cisco Wireless Controller Configuration Guide, Release 8.10: WLAN Security](https://www.cisco.com/c/en/us/td/docs/wireless/controller/8-10/config-guide/b_cg810/wlan_security.html) — WPA1+WPA2; Configuring WPA1+WPA2 (GUI); Protected Management Frames

---

## CCNA4-085 · Security Fundamentals

Objectives: 5.10 · single · Applied

After a planned PSK rotation, a WPA2-PSK WLAN works for newly provisioned clients. One laptop still has the previous saved passphrase and fails the security handshake. RF coverage and the selected SSID are correct. What should be changed first?

- **A.** Change the router’s OSPF cost.
- **B.** Replace the VLAN’s DHCP server.
- **C.** Disable WPA2 on the controller.
- **D.** Update the laptop’s saved PSK.

**Answer: D**

A PSK rotation requires coordinated client credential updates. Working newly provisioned clients and an old saved secret point to the laptop’s profile.

**Option explanations**

- **A:** Routing metrics do not reconcile the WLAN credentials.
- **B:** The security handshake fails before an ordinary DHCP exchange can complete.
- **C:** Removing the required protection is unnecessary and changes the design.
- **D:** The evidence identifies a client credential mismatch after rotation.

**Further reading**

- [Cisco Wireless Controller Configuration Guide, Release 8.10: WLAN Security](https://www.cisco.com/c/en/us/td/docs/wireless/controller/8-10/config-guide/b_cg810/wlan_security.html) — WPA1+WPA2; Configuring WPA1+WPA2 (GUI); Protected Management Frames

---

## CCNA4-086 · Security Fundamentals

Objectives: 5.6 · single · Applied

An applied IPv4 ACL permits TCP destination port 443 and then denies all other IP traffic. HTTPS works, but an ICMP echo test to the same server fails. What is the best conclusion from these two tests?

- **A.** The ACL must be choosing its last rule for all traffic.
- **B.** The server must be completely unreachable at Layer 3.
- **C.** The ACL can explain the different results because ICMP is not TCP port 443.
- **D.** ICMP echo uses TCP destination port 443 by default.

**Answer: C**

A failed ping is not conclusive evidence that every application is unreachable. Interpret each test against the policy fields and protocol it actually uses.

**Option explanations**

- **A:** The HTTPS success is consistent with first-match processing.
- **B:** Successful HTTPS demonstrates at least one working IP path to the service.
- **C:** The tests use distinct protocols that encounter different ACL outcomes.
- **D:** ICMP is a separate IP protocol without TCP port fields.

**Further reading**

- [Configure IP Access Lists](https://www.cisco.com/c/en/us/support/docs/security/ios-firewall/23602-confaccesslists.html) — ACL Concepts; Masks; Process ACLs; Apply ACLs; Extended ACLs

---

## CCNA4-087 · Security Fundamentals

Objectives: 5.6 · single · Applied

A policy permits clients in 10.44.8.0/23 to a service. An engineer writes source 10.44.8.0 0.0.1.255 in the ACL. Which address falls outside that match?

- **A.** 10.44.8.250
- **B.** 10.44.10.1
- **C.** 10.44.9.254
- **D.** 10.44.9.1

**Answer: B**

The mask allows third octets 8 and 9 while allowing any final octet. The next subnet beginning at 10.44.10.0 is not included.

**Option explanations**

- **A:** The third octet 8 is in the covered pair.
- **B:** Third octet 10 changes a fixed bit and is outside the /23.
- **C:** All last-octet values are permitted within third octet 9.
- **D:** The wildcard allows the low bit of the third octet to vary to 9.

**Further reading**

- [Configure IP Access Lists](https://www.cisco.com/c/en/us/support/docs/security/ios-firewall/23602-confaccesslists.html) — ACL Concepts; Masks; Process ACLs; Apply ACLs; Extended ACLs

---

## CCNA4-088 · Security Fundamentals

Objectives: 5.7 · single · Applied

DHCP snooping is enabled on a VLAN. A rogue server sends a DHCPOFFER into a client-facing interface that was accidentally marked trusted. Which correction restores the intended trust boundary?

- **A.** Remove DHCP snooping trust from that client-facing ingress.
- **B.** Trust every interface so the roles are consistent.
- **C.** Configure only a larger DHCP lease time.
- **D.** Disable DAI while retaining the trusted client port.

**Answer: A**

Trust is a deliberate statement about where authorized server messages may enter. Applying it to a user port creates an opening for rogue DHCP replies.

**Option explanations**

- **A:** Server-originated messages should not be accepted from an unapproved client path.
- **B:** This removes the filtering distinction everywhere.
- **C:** Lease duration does not change ingress trust.
- **D:** ARP inspection settings do not correct DHCP snooping trust.

**Further reading**

- [Catalyst 3750-X and 3560-X Configuration Guide: Configuring DHCP Features and IP Source Guard](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst3750x_3560x/software/release/15-0_2_se/configuration/guide/3750x_cg/swdhcp82.html) — DHCP Snooping; DHCP Snooping Binding Database; Enabling DHCP Snooping

---

## CCNA4-089 · Security Fundamentals

Objectives: 5.7 · single · Applied

On a Catalyst 3750-X, DAI is enabled and an untrusted interface has an explicitly configured ARP rate limit of 20 packets per second with a one-second burst interval. The documented rate threshold is exceeded, and no automatic recovery is configured. What interface action is expected?

- **A.** The switch silently raises the limit to the observed rate.
- **B.** DAI permanently converts that interface to trusted.
- **C.** The interface becomes error-disabled because the ARP limit was exceeded.
- **D.** Only the ARP cache timer is shortened.

**Answer: C**

DAI rate enforcement is separate from whether each individual mapping is valid. Investigate why the threshold was exceeded before restoring the interface or changing its limit.

**Option explanations**

- **A:** The configured limit does not automatically expand to fit traffic.
- **B:** A violation does not grant the offending ingress more trust.
- **C:** DAI rate-limit violations can disable the ingress interface.
- **D:** Rate-limit enforcement is not an ARP cache aging change.

**Further reading**

- [Catalyst 3750-X and 3560-X Configuration Guide: Configuring Dynamic ARP Inspection](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst3750x_3560x/software/release/15-0_2_se/configuration/guide/3750x_cg/swdynarp.html) — Understanding Dynamic ARP Inspection; Rate Limiting; ARP ACLs

---

## CCNA4-090 · Security Fundamentals

Objectives: 5.5 · multiple · Applied

A branch requires confidentiality for selected IP traffic over an untrusted WAN. Which two statements describe the required security boundary correctly? Select two.

- **A.** Traffic outside the tunnel’s selected policy is not automatically protected by this VPN.
- **B.** The protected portion can terminate at the branch and headquarters VPN gateways.
- **C.** An encrypted tunnel removes the need to trust either terminating gateway.
- **D.** A gateway tunnel proves that traffic on both local LANs is encrypted by IPsec.

**Answer: A, B**

Locate the actual IPsec endpoints and selectors before stating what is protected. The WAN tunnel does not automatically extend encryption onto every local segment.

**Option explanations**

- **A:** IPsec policy determines which traffic receives protection.
- **B:** Gateway-to-gateway IPsec can protect the WAN portion of the path.
- **C:** The endpoints handle plaintext and keys and remain part of the trust boundary.
- **D:** Protection need not extend past the terminating gateways.

**Further reading**

- [RFC 4301: Security Architecture for the Internet Protocol](https://www.rfc-editor.org/rfc/rfc4301.html) — Sections 3, 4.1, 4.4.1: IPsec services, tunnel mode, and security policy

---

## CCNA4-091 · Automation and Programmability

Objectives: 6.1 · single · Applied

A configuration job reports success on 18 switches and connection failure on 2. The intended setting has been verified on the 18 successful devices only. Which statement best describes the deployment?

- **A.** The setting is verified across all 20 because the job ran
- **B.** The deployment is partial, and the two unverified devices need follow-up
- **C.** All 18 successful changes must have been automatically undone
- **D.** Automation cannot produce different results on different devices

**Answer: B**

Automation still operates against individual devices with individual outcomes. The report supports success for 18 targets and leaves two targets unresolved.

**Option explanations**

- **A:** Starting a job does not prove success on unreachable targets.
- **B:** Per-device outcomes show that fleet-wide completion has not been established.
- **C:** No rollback behavior is specified.
- **D:** Connectivity and device conditions can differ within the same run.

**Further reading**

- [What Is Network Automation?](https://www.cisco.com/site/us/en/learn/topics/networking/what-is-network-automation.html) — Network automation; profiles and policies; automated lifecycle management

---

## CCNA4-092 · Automation and Programmability

Objectives: 6.2 · single · Applied

A traditional switch network already supports SSH scripts that configure each device. A proposal adds a controller that exposes a supported network-wide policy API. Which comparison is most accurate?

- **A.** The existing network is incapable of any automation
- **B.** The controller removes every per-device control function by definition
- **C.** The existing network has no data plane because it uses CLI management
- **D.** Both can be automated, while the controller adds a network-level service abstraction

**Answer: D**

Programmable management is possible in traditional networks. A controller can additionally expose a coordinated network service so applications need less device-specific knowledge.

**Option explanations**

- **A:** SSH scripting is already a form of automation.
- **B:** Controller products can retain distributed or local control functions.
- **C:** CLI management does not eliminate packet forwarding.
- **D:** Automation and controller-based organization are related but distinct concepts.

**Further reading**

- [RFC 7426: Software-Defined Networking (SDN): Layers and Architecture Terminology](https://www.rfc-editor.org/rfc/rfc7426.html) — 3.1 Overview; 3.2 Network Devices; 3.3 Control Plane; 3.5.3 Locality
- [Software-Defined Networking (SDN) Definition](https://www.cisco.com/c/en/us/solutions/software-defined-networking/overview.html) — SDN elements; Features and benefits

---

## CCNA4-093 · Automation and Programmability

Objectives: 6.3, 6.3.a · single · Applied

An overlay tunnel carries a client packet across a routed underlay. A transit underlay router is not a tunnel endpoint and is configured only for ordinary IP forwarding. Which packet information does it principally use to forward the encapsulated packet?

- **A.** The destination address in the outer IP header
- **B.** The original client’s Ethernet access-port number
- **C.** The application’s northbound API password
- **D.** Only the inner client address, ignoring the outer header

**Answer: A**

Encapsulation creates an outer packet that the underlay can route. The tunnel endpoints interpret the overlay information; an ordinary transit router follows the outer IP destination.

**Option explanations**

- **A:** The underlay forwards the tunnel packet toward its tunnel endpoint.
- **B:** That attachment information does not select this router’s ordinary IP next hop.
- **C:** Application API credentials are not forwarding keys.
- **D:** A normal transit router forwards the encapsulated outer IP packet.

**Further reading**

- [Software-Defined Access](https://www.cisco.com/c/en/us/td/docs/solutions/CVD/Campus/cisco-sda-design-guide.html) — SD-Access architecture; Underlay network; Overlay network; Overlay control plane – LISP; Data plane – VXLAN
- [RFC 7426: Software-Defined Networking (SDN): Layers and Architecture Terminology](https://www.rfc-editor.org/rfc/rfc7426.html) — 3.1 Overview; 3.2 Network Devices; 3.3 Control Plane; 3.5.3 Locality

---

## CCNA4-094 · Automation and Programmability

Objectives: 6.4 · single · Applied

A capacity tool learns demand trends from months of WAN utilization and estimates that a circuit will be saturated next quarter. Which operational use best matches this predictive output?

- **A.** Treating the forecast as proof that saturation has already occurred
- **B.** Replacing utilization collection with the forecast permanently
- **C.** Prioritizing capacity investigation before users experience the predicted constraint
- **D.** Classifying the tool as generative solely because it displays a number

**Answer: C**

Predictive analysis can highlight likely future performance constraints. Operators can use the estimate to investigate capacity needs while checking the assumptions and subsequent observations.

**Option explanations**

- **A:** A future estimate is not a current measurement.
- **B:** Future predictions still depend on useful observations and changing conditions.
- **C:** A forecast can inform proactive planning before the anticipated event.
- **D:** Estimating a future quantity is a predictive task.

**Further reading**

- [Cisco Predictive Networks](https://www.cisco.com/c/m/en_us/solutions/predictive-networks/index.html) — Predictive networks; telemetry and learned patterns
- [What is AIOps?](https://developer.cisco.com/articles/what-is-aiops/) — The core components of AIOps; Is AIOps all you need?

---

## CCNA4-095 · Automation and Programmability

Objectives: 6.5 · single · Applied

The documented interface API supports PATCH for partial edits and PUT for complete replacement. Only the description must change; the client must preserve all other current attributes without resending them. Which request fits?

- **A.** PUT with a body containing only description
- **B.** PATCH with the documented description-change document
- **C.** POST to create another interface object
- **D.** GET with description included in the response preference

**Answer: B**

The API explicitly supports partial modification through PATCH. Using its documented patch format allows the client to change the description without supplying a full replacement.

**Option explanations**

- **A:** Under the stated contract, PUT expects complete replacement data.
- **B:** The partial-update method expresses the requested limited change.
- **C:** Creating another object does not edit the existing description.
- **D:** GET retrieves information and does not request this modification.

**Further reading**

- [RFC 5789: PATCH Method for HTTP](https://www.rfc-editor.org/rfc/rfc5789.html#section-2) — 2 The PATCH Method
- [RFC 9110: HTTP Semantics](https://www.rfc-editor.org/rfc/rfc9110.html) — 9 Methods; 15 Status Codes

---

## CCNA4-096 · Automation and Programmability

Objectives: 6.5 · single · Applied

A protected API recognizes a client’s valid bearer token but rejects an attempted change because the token lacks the required write scope. The response is shown. What is the relevant issue?

```text
HTTP/1.1 403 Forbidden
WWW-Authenticate: Bearer error="insufficient_scope", scope="network.write"
```

- **A.** The resource URI necessarily does not exist
- **B.** The token must be a malformed JSON document
- **C.** The client must convert HTTPS into plaintext HTTP
- **D.** The presented credential does not authorize this operation

**Answer: D**

Token validity and permission for an operation are separate checks. The client needs an appropriately authorized token through the approved access process.

**Option explanations**

- **A:** A 403 insufficient_scope response does not say the resource is absent.
- **B:** The API has recognized the credential and reported insufficient permissions.
- **C:** Changing transport protection does not grant write authorization.
- **D:** A valid token can still lack permission for a particular action.

**Further reading**

- [RFC 6750: The OAuth 2.0 Authorization Framework: Bearer Token Usage](https://www.rfc-editor.org/rfc/rfc6750.html) — 2 Authenticated Requests; 3 The WWW-Authenticate Response Header Field; 5 Security Considerations

---

## CCNA4-097 · Automation and Programmability

Objectives: 6.6 · single · Foundation

A team repeatedly performs an ordered backup, configuration and verification sequence on supported switches. Which Ansible artifact is intended to express this reusable sequence of tasks?

- **A.** A YAML playbook
- **B.** A switch forwarding table
- **C.** A TLS server certificate
- **D.** A Terraform provider lock entry

**Answer: A**

Ansible playbooks express reusable automation workflows as plays and tasks. They can organize the sequence and target appropriate managed hosts.

**Option explanations**

- **A:** A playbook organizes plays and tasks for repeatable execution.
- **B:** A forwarding table selects packet forwarding actions, not automation tasks.
- **C:** A certificate supports identity and TLS operations, not task sequencing.
- **D:** That entry concerns Terraform dependency versions, not an Ansible workflow.

**Further reading**

- [Ansible playbooks](https://docs.ansible.com/projects/ansible/latest/playbook_guide/playbooks_intro.html) — Playbook syntax; Playbook execution; Desired state and idempotency

---

## CCNA4-098 · Automation and Programmability

Objectives: 6.6 · multiple · Applied

A team uses Terraform for supported virtual-network resources. Which two statements describe its desired-state approach? Select two.

- **A.** The configuration must list every mouse click used in the cloud console
- **B.** State is unnecessary because every resource name is globally unique
- **C.** Configuration declares the infrastructure the team wants to manage
- **D.** State helps associate configuration resources with real objects
- **E.** Every resource must be created in the written order of file lines

**Answer: C, D**

Terraform describes desired infrastructure and uses state to track managed objects. It works with dependency relationships rather than merely replaying a console procedure.

**Option explanations**

- **A:** Terraform configuration declares resources rather than recording UI clicks.
- **B:** State records the association between declarations and managed objects.
- **C:** The declaration expresses desired resource properties.
- **D:** That association is essential to tracking managed infrastructure.
- **E:** Terraform can derive dependencies between resource declarations.

**Further reading**

- [What is Terraform?](https://developer.hashicorp.com/terraform/intro) — How does Terraform work?; Manage any infrastructure; Track your infrastructure
- [State](https://developer.hashicorp.com/terraform/language/state) — State; mapping configuration to real resources

---

## CCNA4-099 · Automation and Programmability

Objectives: 6.7 · single · Applied

A JSON response contains an ordered array of scheduled maintenance actions. Which edit changes the order in which a client that follows this array will process the actions?

```text
{"actions":["backup","upgrade","verify"],"site":"north"}
```

- **A.** Adding indentation before the array
- **B.** Moving the second array element before the first
- **C.** Moving the actions member to another position in the outer object
- **D.** Adding a space after the comma between array elements

**Answer: B**

JSON arrays represent ordered sequences. Moving elements changes the represented sequence; formatting changes and relocation of the enclosing object member do not.

**Option explanations**

- **A:** Insignificant whitespace does not change array element order.
- **B:** Arrays preserve element order, so swapping elements changes the sequence.
- **C:** Outer object member placement does not reorder the array itself.
- **D:** Whitespace after the separator does not change the sequence.

**Further reading**

- [RFC 8259: The JavaScript Object Notation (JSON) Data Interchange Format](https://www.rfc-editor.org/rfc/rfc8259.html) — 2 JSON Grammar; 3 Values; 4 Objects; 5 Arrays; 6 Numbers; 7 Strings

---

## CCNA4-100 · Automation and Programmability

Objectives: 6.7 · matching · Foundation

Match each value from the response with its JSON type. Use each type once.

```text
{"location":{"room":"R4"},"ports":[1,2],"rack":"R09","active":true}
```

1. The value of location
2. The value of ports
3. The value of rack
4. The value of active

- **A.** String
- **B.** Object
- **C.** Array
- **D.** Boolean

**Answer: 1 → B; 2 → C; 3 → A; 4 → D**

The values are distinguished by JSON syntax: braces for the object, brackets for the array, quotes for the string and an unquoted Boolean literal.

**Option explanations**

- **A:** The quoted rack identifier is textual data.
- **B:** The location value groups named members inside braces.
- **C:** The ports value is an ordered collection inside brackets.
- **D:** The active value is the unquoted literal true.

**Further reading**

- [RFC 8259: The JavaScript Object Notation (JSON) Data Interchange Format](https://www.rfc-editor.org/rfc/rfc8259.html) — 2 JSON Grammar; 3 Values; 4 Objects; 5 Arrays; 6 Numbers; 7 Strings

---
