# CCNA Practice — Set 05

100 original questions aligned to CCNA 200-301 v1.1. No interactive labs.

Answers and explanations follow each question. For an unrevealed attempt, use the Streamlit app.

Content review date: 2026-09-14.

## CCNA5-001 · Network Fundamentals

Objectives: 1.1.a · single · Foundation

A branch has one subnet for users and another for servers. A packet crosses their router. Which action belongs to the router’s Layer 3 role?

- **A.** Choosing an RF channel for the client
- **B.** Learning only the packet’s destination MAC as a source
- **C.** Supplying a guest operating-system kernel
- **D.** Selecting a next hop using the destination IP address

**Answer: D**

The router chooses a forwarding path in the IP topology. Ethernet headers serve the individual link rather than replacing the IP routing decision.

**Option explanations**

- **A:** That is a wireless radio-management function.
- **B:** MAC source learning is a different Layer 2 operation.
- **C:** That is unrelated to routing.
- **D:** The routing function chooses how to reach the destination network.

**Further reading**

- [Networking Basics: What You Need To Know](https://www.cisco.com/site/us/en/learn/topics/small-business/networking-basics.html) — Switches; Routers; Access Points

---

## CCNA5-002 · Network Fundamentals

Objectives: 1.2.a · single · Applied

A building uses access switches connected to a redundant pair that combines distribution and core functions. What makes this a two-tier campus?

- **A.** Exactly two physical switches exist
- **B.** Distribution and core roles are combined in one tier
- **C.** Only two VLANs are supported
- **D.** Every server must connect directly to every switch

**Answer: B**

Count architectural roles, not chassis. Redundancy within a tier does not create an additional tier.

**Option explanations**

- **A:** There may be many access switches and two aggregation devices.
- **B:** The access tier plus collapsed distribution/core creates two logical tiers.
- **C:** Tier count does not determine VLAN count.
- **D:** That is not a collapsed-core requirement.

**Further reading**

- [Campus LAN and Wireless LAN Solution Design Guide](https://www.cisco.com/c/en/us/td/docs/solutions/CVD/Campus/cisco-campus-lan-wlan-design-guide.html) — Distribution layer — Two-tier design

---

## CCNA5-003 · Network Fundamentals

Objectives: 1.3.a · single · Applied

The same duplex LC connector fits an SR module and an LR module. Why is connector fit insufficient to establish compatibility?

- **A.** An LC connector forces every module to 1 Gb/s
- **B.** SR and LR must use the same wavelength because both use LC
- **C.** Fiber mode, wavelength, reach, and optical levels must also match
- **D.** IPv4 private addressing prevents LR operation

**Answer: C**

Physical fit is only one requirement. Select optics and fiber as an interoperable end-to-end channel.

**Option explanations**

- **A:** Connector type alone does not select the data rate.
- **B:** The modules can require different optical signaling and fiber.
- **C:** Mechanical mating does not establish an acceptable optical channel.
- **D:** Address classification does not determine optical compatibility.

**Further reading**

- [Cisco 10GBASE SFP+ Modules Data Sheet](https://www.cisco.com/c/en/us/products/collateral/interfaces-modules/transceiver-modules/data_sheet_c78-455693.html) — Cisco SFP-10G-SR module; Cisco SFP-10G-LR module; Cisco SFP-10G-T-X module

---

## CCNA5-004 · Network Fundamentals

Objectives: 1.4 · single · Foundation

A half-duplex legacy Ethernet port records ordinary collisions while transmitting on a correctly sized hub segment. There are no late collisions, errors, or mismatches. What is the sound interpretation?

- **A.** Some collisions are expected during shared-medium contention
- **B.** Any collision proves an IP address conflict
- **C.** The interface must actually be full duplex
- **D.** The hub has learned the wrong MAC address

**Answer: A**

An ordinary collision is not automatically a cabling fault in this explicitly half-duplex environment. Interpret counters against the link’s intended operating mode.

**Option explanations**

- **A:** CSMA/CD resolves overlapping attempts on half-duplex shared Ethernet.
- **B:** Collision counters describe link access, not duplicate IP assignments.
- **C:** Full-duplex operation does not use collisions for access.
- **D:** A hub does not build a MAC forwarding table.

**Further reading**

- [Configure and Verify Ethernet 10/100/1000Mb Half/Full Duplex Auto-Negotiation](https://www.cisco.com/c/en/us/support/docs/lan-switching/ethernet/10561-3.html) — Background Information; Auto-Negotiation on Catalyst Switches that Run Cisco IOS Software

---

## CCNA5-005 · Network Fundamentals

Objectives: 1.5 · single · Applied

A packet capture shows the first three control exchanges of a standard successful TCP connection. Which sequence is expected?

| Exchange | Direction |
| --- | --- |
| 1 | Client to server |
| 2 | Server to client |
| 3 | Client to server |

- **A.** ACK → FIN → SYN
- **B.** SYN → SYN → FIN
- **C.** FIN → ACK → RST
- **D.** SYN → SYN-ACK → ACK

**Answer: D**

TCP synchronizes both directions of sequence space during establishment. UDP does not perform this protocol-level handshake.

**Option explanations**

- **A:** FIN is used for closing, not this establishment sequence.
- **B:** This omits the normal acknowledgment progression.
- **C:** These flags describe termination/reset actions.
- **D:** This is the normal three-way establishment handshake.

**Further reading**

- [RFC 9293: Transmission Control Protocol (TCP)](https://www.rfc-editor.org/rfc/rfc9293.html#section-2.2) — 2.2. Key TCP Concepts

---

## CCNA5-006 · Network Fundamentals

Objectives: 1.6 · single · Challenge

A printer was assigned 10.30.7.0/23. An engineer rejects it solely because its final octet is zero. Which assessment is correct?

- **A.** It is the /23 network address
- **B.** It is an ordinary usable address in 10.30.6.0/23
- **C.** It is the /23 directed broadcast address
- **D.** Every address ending in .0 is prohibited

**Answer: B**

The host field spans the last bit of the third octet and all of the fourth. Here it is neither all zero nor all one.

**Option explanations**

- **A:** The containing /23 begins at 10.30.6.0.
- **B:** A zero final octet is allowed when the complete host field is not all zero.
- **C:** That address is 10.30.7.255.
- **D:** Validity depends on all host bits under the configured mask.

**Further reading**

- [Configure IP Addresses and Unique Subnets for New Users](https://www.cisco.com/c/en/us/support/docs/ip/routing-information-protocol-rip/13788-3.html) — Network Masks; Understand Subnetting; VLSM Example

---

## CCNA5-007 · Network Fundamentals

Objectives: 1.7 · multiple · Challenge

Which TWO complete proposed subnets are wholly contained in RFC 1918 space? Select two.

- **A.** 172.0.0.0/12
- **B.** 192.168.0.0/15
- **C.** 10.96.0.0/11
- **D.** 172.24.0.0/13
- **E.** 192.0.0.0/8

**Answer: C, D**

Classify the entire proposed prefix, not only its first displayed address. A larger supernet can include nonprivate space.

**Option explanations**

- **A:** This spans 172.0–172.15, outside the private 172.16/12 range.
- **B:** The /15 also includes 192.169.0.0/16, which is not RFC 1918.
- **C:** Every address remains inside private 10.0.0.0/8.
- **D:** Its second octet spans 24–31, entirely within private 172.16/12.
- **E:** Only a much smaller portion of this /8 is RFC 1918.

**Further reading**

- [RFC 1918: Address Allocation for Private Internets](https://www.rfc-editor.org/rfc/rfc1918#section-3) — 3. Private Address Space
- [Configure IP Addresses and Unique Subnets for New Users](https://www.cisco.com/c/en/us/support/docs/ip/routing-information-protocol-rip/13788-3.html) — Network Masks; Understand Subnetting; VLSM Example

---

## CCNA5-008 · Network Fundamentals

Objectives: 1.8 · single · Applied

An inventory lists 2001:db8:4:9:0:0:0:10/64. Which prefix should be recorded as the directly attached /64 network?

- **A.** 2001:db8:4:9::/64
- **B.** 2001:db8:4::/64
- **C.** 2001:db8:4:9::10/128
- **D.** 2001:db8:4:10::/64

**Answer: A**

A /64 boundary falls after the fourth hextet. Host bits are zeroed when representing the network prefix.

**Option explanations**

- **A:** The first four hextets are the 64-bit prefix.
- **B:** This replaces the fourth hextet 9 with zero.
- **C:** This describes the host, not the attached /64.
- **D:** This changes the fourth hextet from 9 to 10 and therefore identifies a different /64.

**Further reading**

- [RFC 4291: IP Version 6 Addressing Architecture](https://www.rfc-editor.org/rfc/rfc4291#section-2.3) — 2.3. Text Representation of Address Prefixes; 2.4. Address Type Identification; 2.5.6. Link-Local IPv6 Unicast Addresses; 2.7. Multicast Addresses

---

## CCNA5-009 · Network Fundamentals

Objectives: 1.9.a · multiple · Applied

One interface has fe80::14 and fd48:2190:abcd:3::14. Which TWO statements are correct? Select two.

- **A.** Only one IPv6 address may exist per interface
- **B.** The fe80 address is confined to its link
- **C.** The fd48 address must be globally advertised
- **D.** The fe80 address is an IPv6 broadcast address
- **E.** The fd48 address can participate in routing within selected private networks

**Answer: B, E**

IPv6 interfaces commonly have multiple addresses. Link-local and ULA serve different scopes and can exist together.

**Option explanations**

- **A:** Multiple addresses and scopes can coexist.
- **B:** That address has link-local unicast scope.
- **C:** ULA does not require global Internet advertisement.
- **D:** IPv6 has no broadcast address type.
- **E:** Unique local addresses are not restricted to a single link.

**Further reading**

- [RFC 4291: IP Version 6 Addressing Architecture](https://www.rfc-editor.org/rfc/rfc4291#section-2.3) — 2.3. Text Representation of Address Prefixes; 2.4. Address Type Identification; 2.5.6. Link-Local IPv6 Unicast Addresses; 2.7. Multicast Addresses
- [RFC 4193: Unique Local IPv6 Unicast Addresses](https://www.rfc-editor.org/rfc/rfc4193#section-3.1) — 1. Introduction; 3.1. Format

---

## CCNA5-010 · Network Fundamentals

Objectives: 1.10 · single · Foundation

A Windows administrator needs to inspect whether DHCP is enabled and which DNS servers are configured. Which command provides those adapter details?

- **A.** ipconfig /flushdns
- **B.** ipconfig /release
- **C.** ipconfig /all
- **D.** ipconfig /displaydns

**Answer: C**

Use a read-only detailed configuration view before changing the adapter. Resolver cache entries are different from configured DNS server addresses.

**Option explanations**

- **A:** This clears cached DNS entries rather than displaying the full adapter configuration.
- **B:** This releases applicable DHCP configuration and is not a read-only inspection.
- **C:** The detailed display includes DHCP and DNS configuration fields.
- **D:** This shows the resolver cache, not all adapter parameters.

**Further reading**

- [ipconfig](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/ipconfig) — Syntax; Parameters (/all)

---

## CCNA5-011 · Network Fundamentals

Objectives: 1.11.b · single · Applied

A client sees two APs with SSID Warehouse but different BSSIDs. Which conclusion is justified?

- **A.** The APs must be on the same physical channel
- **B.** The client has discovered a mandatory address conflict
- **C.** BSSID is the shared human-readable network name
- **D.** The shared name can be advertised by distinct basic service sets

**Answer: D**

SSID naming permits a common network identity across APs. A BSSID distinguishes the individual basic service set.

**Option explanations**

- **A:** The same SSID may be used across different channels.
- **B:** SSID reuse is normal and does not imply an IP conflict.
- **C:** That is the SSID; BSSID identifies a basic service set.
- **D:** Different AP radio service sets can support the same WLAN name.

**Further reading**

- [Campus LAN and Wireless LAN Solution Design Guide](https://www.cisco.com/c/en/us/td/docs/solutions/CVD/Campus/cisco-campus-lan-wlan-design-guide.html) — Centralized (local-mode) design model

---

## CCNA5-012 · Network Fundamentals

Objectives: 1.12 · single · Applied

An application requires a different operating-system kernel from its neighboring workload on the same physical server. Which technology most directly supplies separate guest kernels?

- **A.** Conventional virtual machines
- **B.** Two ordinary Linux containers in one Linux host OS
- **C.** Two VRFs in one router
- **D.** Two SSIDs on one AP

**Answer: A**

VMs virtualize a machine environment for separate guest operating systems. Standard process containers isolate workloads while sharing their host kernel.

**Option explanations**

- **A:** Each VM can run its own guest operating system.
- **B:** Those process containers share the host kernel.
- **C:** VRFs separate routing contexts, not guest operating systems.
- **D:** Wireless names do not create OS kernels.

**Further reading**

- [What is a container?](https://docs.docker.com/get-started/docker-concepts/the-basics/what-is-a-container/#containers-versus-virtual-machines-vms) — Containers versus virtual machines (VMs)

---

## CCNA5-013 · Network Fundamentals

Objectives: 1.13.a, 1.13.d · single · Applied

A destination host only receives traffic and sends no eligible source frames for longer than the configured MAC aging time. Its dynamic entry expires. Why did received traffic not necessarily keep the entry fresh?

- **A.** Aging occurs only when a VLAN is deleted
- **B.** Dynamic learning refreshes location from observed source traffic
- **C.** The switch refreshes only IPv6 hosts
- **D.** The destination must be assigned a static IP to prevent aging

**Answer: B**

Traffic sent toward a location is not evidence received from that location. Source observations are the basis for ordinary dynamic MAC learning.

**Option explanations**

- **A:** Dynamic entries can expire in an unchanged VLAN.
- **B:** Packets addressed to a host do not prove its current ingress location.
- **C:** Source learning is independent of that IP address family.
- **D:** IP assignment method does not itself create a static MAC entry.

**Further reading**

- [Configuring MAC Address Tables](https://www.cisco.com/c/en/us/td/docs/switches/datacenter/nexus5500/sw/layer2/7x/b_5500_Layer2_Config_7x/config_mac_address_tables.pdf) — Information About MAC Addresses (page 1); Configuring the Aging Time for the MAC Table (page 2)

---

## CCNA5-014 · Network Fundamentals

Objectives: 1.1.h · single · Applied

A non-PoE Ethernet printer is connected to a standards-compliant PoE port operating in automatic detection mode. What should happen before normal PoE power is supplied?

- **A.** The port forces maximum voltage into every attached device
- **B.** The printer must receive a DHCP lease as its power signature
- **C.** The port checks for a compatible powered-device signature
- **D.** The printer’s MAC address must be globally unique in a cloud database

**Answer: C**

Automatic PoE power admission is distinct from ordinary data link attachment. Connecting a non-PoE device does not make it request PoE power.

**Option explanations**

- **A:** Standards-based automatic operation detects an eligible powered device first.
- **B:** PoE detection is not DHCP.
- **C:** Detection prevents ordinary PoE allocation to an ineligible device.
- **D:** PoE detection does not use such an inventory lookup.

**Further reading**

- [Interface and Hardware Components Configuration Guide, Cisco IOS XE 17.14.x (Catalyst 9200 Switches): Configuring Power over Ethernet](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst9200/software/release/17-14/configuration_guide/int_hw/b_1714_int_and_hw_9200_cg/configuring_poe.html) — Powered-Device Detection and Initial Power Allocation

---

## CCNA5-015 · Network Fundamentals

Objectives: 1.6 · single · Applied

The only addresses available for a new point-to-point link are 192.0.2.20/30 through 192.0.2.23/30. Using ordinary /30 addressing, which pair belongs on its two interfaces?

- **A.** 192.0.2.20 and 192.0.2.21
- **B.** 192.0.2.22 and 192.0.2.23
- **C.** 192.0.2.20 and 192.0.2.23
- **D.** 192.0.2.21 and 192.0.2.22

**Answer: D**

A /30 block has four addresses. For this block, its middle two addresses identify the link interfaces.

**Option explanations**

- **A:** The .20 address identifies the /30 subnet.
- **B:** The .23 address is the /30 broadcast.
- **C:** These are both reserved boundary addresses for this /30.
- **D:** These are the two ordinary usable host addresses.

**Further reading**

- [Configure IP Addresses and Unique Subnets for New Users](https://www.cisco.com/c/en/us/support/docs/ip/routing-information-protocol-rip/13788-3.html) — Network Masks; Understand Subnetting; VLSM Example

---

## CCNA5-016 · Network Fundamentals

Objectives: 1.9.d · single · Challenge

An EUI-64-derived interface identifier is 021a:2bff:fe3c:4d5e. Assuming it came from a 48-bit MAC through the specified modified EUI-64 procedure, which original MAC is recovered?

- **A.** 00-1A-2B-3C-4D-5E
- **B.** 02-1A-2B-3C-4D-5E
- **C.** 03-1A-2B-3C-4D-5E
- **D.** 00-1A-FF-FE-4D-5E

**Answer: A**

The specified transformation is reversible when its origin is known. Do not assume every IPv6 identifier containing ff:fe was necessarily generated this way.

**Option explanations**

- **A:** Remove FF-FE and invert the 02 bit in the first byte.
- **B:** This removes the inserted bytes but does not reverse the U/L inversion.
- **C:** This changes the wrong first-byte bit.
- **D:** This removes original bytes rather than the inserted middle pair.

**Further reading**

- [RFC 2464: Transmission of IPv6 Packets over Ethernet Networks](https://datatracker.ietf.org/doc/html/rfc2464#section-4) — 4. Stateless Autoconfiguration

---

## CCNA5-017 · Network Fundamentals

Objectives: 1.11.c · single · Applied

A wireless survey records signal −62 dBm and noise −92 dBm at location A, then signal −62 dBm and noise −75 dBm at location B. Which location has the better signal-to-noise margin?

| Location | Signal | Noise |
| --- | --- | --- |
| A | −62 dBm | −92 dBm |
| B | −62 dBm | −75 dBm |

- **A.** B, because −75 is numerically greater than −92
- **B.** A, because its signal is 30 dB above noise rather than 13 dB
- **C.** Both, because equal signal strength guarantees equal quality
- **D.** Neither, because negative dBm means no signal exists

**Answer: B**

Assess desired signal relative to the noise floor. The same signal power can produce very different margins in different noise conditions.

**Option explanations**

- **A:** The higher noise floor reduces the margin.
- **B:** Subtract noise from signal in each location.
- **C:** Noise differs despite identical received signal.
- **D:** Negative dBm indicates power below 1 mW, not absent power.

**Further reading**

- [Meraki Wireless for Enterprise Best Practices — RF Design](https://documentation.meraki.com/Platform_Management/Dashboard_Administration/Design_and_Configure/Architectures_and_Best_Practices/Meraki_Wireless_for_Enterprise_Best_Practices/Meraki_Wireless_for_Enterprise_Best_Practices_-_RF_Design) — RF design; signal-to-noise ratio; transmit power

---

## CCNA5-018 · Network Fundamentals

Objectives: 1.13.b, 1.13.c · multiple · Applied

A switch’s table contains destination MAC M only in VLAN 20. A frame for M arrives in VLAN 10, where M has no entry. Which TWO statements follow with ordinary forwarding and no filtering features? Select two.

- **A.** The VLAN 20 entry authorizes routing into VLAN 20
- **B.** The switch ignores VLAN identity in its lookup
- **C.** The destination is unknown within VLAN 10
- **D.** The frame is flooded to the other eligible VLAN 10 ports
- **E.** The frame must be sent through every port in every VLAN

**Answer: C, D**

A MAC address table is not a single VLAN-independent location list. Use the entry in the frame’s forwarding context.

**Option explanations**

- **A:** A MAC entry does not authorize or perform inter-VLAN routing.
- **B:** MAC forwarding context includes the VLAN.
- **C:** A mapping in another VLAN does not supply this lookup.
- **D:** Unknown-unicast flooding remains in the ingress VLAN.
- **E:** Flooding does not remove VLAN boundaries.

**Further reading**

- [Configuring MAC Address Tables](https://www.cisco.com/c/en/us/td/docs/switches/datacenter/nexus5500/sw/layer2/7x/b_5500_Layer2_Config_7x/config_mac_address_tables.pdf) — Information About MAC Addresses (page 1); Configuring the Aging Time for the MAC Table (page 2)

---

## CCNA5-019 · Network Fundamentals

Objectives: 1.2.f · single · Applied

An organization operates its own fixed server racks without a self-service cloud layer. Moving an application from a rented public-cloud VM into those racks changes which aspect?

- **A.** The application’s required transport protocol must become UDP
- **B.** The physical Ethernet frame length must double
- **C.** The hosting model changes to traditional on-premises infrastructure
- **D.** The service becomes a WAN circuit

**Answer: C**

The change concerns where and how computing resources are provided. It does not by itself determine application protocol or frame format.

**Option explanations**

- **A:** Hosting location does not mandate a transport change.
- **B:** That is not implied by the move.
- **C:** The organization now operates the application on its own fixed equipment.
- **D:** Compute hosting and connectivity are different aspects.

**Further reading**

- [NIST SP 800-145: The NIST Definition of Cloud Computing](https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-145.pdf) — 2. The NIST Definition of Cloud Computing — Essential Characteristics; Deployment Models

---

## CCNA5-020 · Network Fundamentals

Objectives: 1.10 · matching · Applied

Match each displayed client value with the IP parameter it represents. Use each parameter once.

1. Client interface: 192.168.9.34
2. Mask: 255.255.255.224
3. Router: 192.168.9.33
4. Name server: 192.168.9.35

- **A.** Default gateway
- **B.** IPv4 address
- **C.** DNS resolver
- **D.** Subnet mask

**Answer: 1 → B; 2 → D; 3 → A; 4 → C**

These parameters answer different questions: who the interface is, which network is local, where remote packets go, and how names are resolved.

**Option explanations**

- **A:** The normal next-hop router for destinations outside locally known routes.
- **B:** The address assigned to the client interface.
- **C:** The configured service consulted for name resolution.
- **D:** The bit boundary used to distinguish the local prefix and host portion.

**Further reading**

- [ipconfig](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/ipconfig) — Syntax; Parameters (/all)
- [Change TCP/IP settings on Mac](https://support.apple.com/en-hk/guide/mac-help/mh14129/mac) — IP address, subnet mask, and router settings

---

## CCNA5-021 · Network Access

Objectives: 2.1.a · multiple · Applied

An access switch must place a phone’s tagged voice in VLAN 260 and its attached PC’s untagged data in VLAN 160. Both VLANs exist and the phone supports the configured advertisement method. Which TWO interface commands implement the assignments? Select TWO.

- **A.** switchport trunk native vlan 260
- **B.** switchport access vlan 260
- **C.** switchport voice vlan 260
- **D.** switchport access vlan 160

**Answer: C, D**

An access port can support separate data and voice treatment. Keep the PC’s access membership distinct from the phone’s voice VLAN.

**Option explanations**

- **A:** A trunk native command is not the intended access-plus-voice assignment.
- **B:** This places untagged PC traffic in the voice VLAN instead of VLAN 160.
- **C:** This advertises and supports the separate tagged voice VLAN.
- **D:** This sets the untagged data membership.

**Further reading**

- [VLAN Configuration Guide, Cisco IOS XE 17.15.x — Configuring Voice VLANs](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst9300/software/release/17-15/configuration_guide/vlan/b_1715_vlan_9300_cg/configuring_voice_vlans.html) — Cisco IP Phone Voice Traffic; Cisco IP Phone Data Traffic

---

## CCNA5-022 · Network Access

Objectives: 2.1.c · single · Applied

Host A in VLAN 16 can reach Host B in VLAN 26. Both use their switch’s SVIs as gateways. When A sends a packet to B, which destination MAC does A use in its initial Ethernet frame?

- **A.** B’s MAC learned by broadcasting directly across both VLANs
- **B.** The native VLAN ID encoded as a MAC address
- **C.** The broadcast MAC for every routed data packet
- **D.** The MAC of A’s VLAN 16 gateway

**Answer: D**

Inter-VLAN routing is a Layer 3 hop. The source host first sends its packet inside a frame addressed to its own local gateway.

**Option explanations**

- **A:** ARP for a local neighbor does not automatically cross the VLAN routing boundary.
- **B:** A VLAN number is not an Ethernet destination address.
- **C:** Only resolution exchanges use broadcasts; ordinary routed unicast uses the gateway MAC.
- **D:** A sends off-subnet traffic to its local router attachment, which then routes it.

**Further reading**

- [Configure Inter-VLAN Routing with Catalyst Switches](https://www.cisco.com/c/en/us/support/docs/lan-switching/inter-vlan-routing/41260-189.html) — Configure; Troubleshoot

---

## CCNA5-023 · Network Access

Objectives: 2.1.b, 2.2.c · single · Applied

A trunk’s native VLAN is changed from 1 to 300 at both ends, with other port settings left untouched. What happens to unrelated access ports that still have the default access VLAN?

- **A.** They cease to belong to any VLAN.
- **B.** They become VLAN 300 trunks.
- **C.** They all move to VLAN 300.
- **D.** They remain assigned to VLAN 1.

**Answer: D**

Default access VLAN and trunk native VLAN are separate concepts. Changing one trunk property does not migrate endpoint ports.

**Option explanations**

- **A:** Their unchanged default membership still exists.
- **B:** Neither their mode nor membership is changed by this action.
- **C:** A trunk native change does not rewrite other ports’ access settings.
- **D:** Access membership is separate from the native VLAN configured on another interface.

**Further reading**

- [VLAN Configuration Guide, Cisco IOS XE 17.15.x — Configuring VLAN Trunks](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst9300/software/release/17-15/configuration_guide/vlan/b_1715_vlan_9300_cg/configuring_vlan_trunks.html) — Allowed VLANs on a Trunk; Configuring the Native VLAN for Untagged Traffic
- [VLAN Configuration Guide, Cisco IOS XE 17.15.x — Configuring VLANs](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst9300/software/release/17-15/configuration_guide/vlan/b_1715_vlan_9300_cg/configuring_vlans.html) — Supported VLANs; Deleting a VLAN; VLAN Port Membership Modes

---

## CCNA5-024 · Network Access

Objectives: 2.2.a · single · Applied

An interswitch link has the output below. A technician wants proof that VLAN 62 user data is forwarding over this particular link. What additional issue must be checked?

```text
Status: trunking
Vlans allowed on trunk: 12,62
Vlans allowed and active in management domain: 12,62
Vlans in spanning tree forwarding state and not pruned: 12
```

- **A.** Whether VLAN 62 is beyond 4094
- **B.** Whether the trunk’s administrative mode is access
- **C.** Why VLAN 62 is absent from the forwarding-and-not-pruned list
- **D.** Whether the physical interface has a host IP address

**Answer: C**

The final trunk summary list is operational evidence. Inspect spanning tree and pruning for VLAN 62 before declaring this path available.

**Option explanations**

- **A:** VLAN 62 is a valid ordinary VLAN number.
- **B:** The link is already reported as trunking.
- **C:** Allowed and active VLANs need not currently forward on every redundant trunk.
- **D:** A Layer 2 trunk does not need its own host IP to carry VLAN traffic.

**Further reading**

- [VLAN Configuration Guide, Cisco IOS XE 17.15.x — Configuring VLAN Trunks](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst9300/software/release/17-15/configuration_guide/vlan/b_1715_vlan_9300_cg/configuring_vlan_trunks.html) — Allowed VLANs on a Trunk; Configuring the Native VLAN for Untagged Traffic

---

## CCNA5-025 · Network Access

Objectives: 2.2.a, 2.2.b · single · Applied

A non-Cisco peer expects a static 802.1Q trunk and does not participate in DTP. Which Cisco-side configuration expresses that requirement without sending DTP?

- **A.** channel-group 1 mode active only
- **B.** switchport mode access; switchport nonegotiate
- **C.** switchport mode dynamic auto only
- **D.** switchport mode trunk; switchport nonegotiate

**Answer: D**

Select trunk operation explicitly when the peer will not negotiate. DTP suppression controls negotiation messages, not the data tagging mechanism.

**Option explanations**

- **A:** LACP aggregation does not itself select the intended trunk configuration.
- **B:** Suppressing DTP does not turn an access interface into a trunk.
- **C:** A passive dynamic configuration relies on a compatible initiating peer.
- **D:** Static trunk mode plus suppressed negotiation matches a peer that does not use DTP.

**Further reading**

- [VLAN Configuration Guide, Cisco IOS XE 17.15.x — Configuring VLAN Trunks](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst9300/software/release/17-15/configuration_guide/vlan/b_1715_vlan_9300_cg/configuring_vlan_trunks.html) — Allowed VLANs on a Trunk; Configuring the Native VLAN for Untagged Traffic

---

## CCNA5-026 · Network Access

Objectives: 2.3 · single · Applied

A neighboring IP phone supports LLDP-MED. The engineer wants the switch to advertise the phone’s voice VLAN and QoS policy without manually configuring those values on every phone. Which LLDP-MED information is relevant?

- **A.** Network-policy TLV
- **B.** An OSPF router-LSA
- **C.** The spanning-tree root bridge’s MAC address only
- **D.** A DHCP lease timer interpreted as a VLAN tag

**Answer: A**

LLDP-MED extends neighbor discovery with endpoint-specific policy information. The endpoint and switch must support the advertised policy.

**Option explanations**

- **A:** This can advertise application VLAN, tagging, and priority policy to the endpoint.
- **B:** OSPF routing information does not configure a phone’s LLDP-MED policy.
- **C:** Root election identity is unrelated to the phone application policy.
- **D:** A timer is not the LLDP-MED network-policy advertisement.

**Further reading**

- [Interface and Hardware Components Configuration Guide, Cisco IOS XE 17.15.x — Configuring LLDP, LLDP-MED, and Wired Location Service](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst9300/software/release/17-15/configuration_guide/int_hw/b_1715_int_and_hw_9300_cg/configuring_lldp__lldp_med__and_wired_location_service.html) — LLDP; Enabling LLDP; Monitoring and Maintaining LLDP, LLDP-MED, and Wired Location Service

---

## CCNA5-027 · Network Access

Objectives: 2.4 · multiple · Applied

A two-switch LACP installation has one active end and one passive end. A review proposes changing the passive end to active while retaining compatible member settings. Which TWO statements are correct? Select TWO.

- **A.** The change does not double each member’s physical line rate.
- **B.** LACP requires exactly one passive endpoint.
- **C.** Two active ends necessarily create a Layer 2 loop.
- **D.** Active/active is a valid LACP combination.

**Answer: A, D**

The active/passive choice governs initiation of negotiation. It does not determine physical link speed or require opposite modes.

**Option explanations**

- **A:** Negotiation mode does not alter the Ethernet PHY’s speed.
- **B:** At least one active endpoint is required; a passive endpoint is not mandatory.
- **C:** LACP can negotiate one logical bundle with both ends active.
- **D:** Both ends may initiate LACP negotiation.

**Further reading**

- [Layer 2 Configuration Guide, Cisco IOS XE 17.15.x — Configuring EtherChannels](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst9300/software/release/17-15/configuration_guide/lyr2/b_1715_lyr2_9300_cg/configuring_etherchannels.html) — LACP Modes; EtherChannel Configuration Guidelines; Load Balancing; Layer 3 EtherChannels; Hot-Standby Ports

---

## CCNA5-028 · Network Access

Objectives: 2.4 · single · Challenge

A Catalyst LACP channel has a configured maximum of two active members. Its summary shows Gi1/0/1(P), Gi1/0/2(P), and Gi1/0/3(H). The legend defines H as hot standby. Which action is justified solely by that evidence?

```text
interface Port-channel11
 lacp max-bundle 2

Group  Port-channel  Protocol  Ports
11     Po11(SU)      LACP      Gi1/0/1(P) Gi1/0/2(P) Gi1/0/3(H)
```

- **A.** Disable LACP because it supports only two configured members.
- **B.** Treat Gi1/0/3 as forwarding an equal share of current traffic.
- **C.** Add VLAN 3 to make port 3 active.
- **D.** Recognize Gi1/0/3 as a standby member rather than immediately replacing its cable.

**Answer: D**

Interpret standby state in the context of the configured bundle limit. Not every nonforwarding member represents a physical fault.

**Option explanations**

- **A:** More configured members may exist than the active maximum.
- **B:** Hot standby is not an active bundled forwarding member.
- **C:** Its standby role follows the active-member limit, not its interface number.
- **D:** The explicit maximum and H state explain why the compatible member is not active.

**Further reading**

- [Layer 2 Configuration Guide, Cisco IOS XE 17.15.x — Configuring EtherChannels](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst9300/software/release/17-15/configuration_guide/lyr2/b_1715_lyr2_9300_cg/configuring_etherchannels.html) — LACP Modes; EtherChannel Configuration Guidelines; Load Balancing; Layer 3 EtherChannels; Hot-Standby Ports

---

## CCNA5-029 · Network Access

Objectives: 2.5.a · single · Foundation

A Catalyst switch displays bridge priority 32828 for VLAN 60 with the extended system ID enabled. Which configured base priority does this represent?

```text
Bridge ID Priority 32828 (priority 32768 sys-id-ext 60)
```

- **A.** 32768
- **B.** 4096
- **C.** 60
- **D.** 32828

**Answer: A**

Rapid PVST+ incorporates the VLAN ID into the bridge priority field. Separate the configurable base priority from the extended system ID.

**Option explanations**

- **A:** The displayed priority includes the VLAN ID: 32768 + 60 = 32828.
- **B:** 4096 is a permitted priority increment but does not produce the displayed value.
- **C:** The VLAN ID supplies the extension, not the whole base priority.
- **D:** That is the combined value, not the configurable base priority.

**Further reading**

- [Layer 2 Configuration Guide, Cisco IOS XE 17.15.x — Configuring Spanning Tree Protocol](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst9300/software/release/17-15/configuration_guide/lyr2/b_1715_lyr2_9300_cg/configuring_spanning_tree_protocol.html) — Spanning-Tree Topology and Bridge Protocol Data Units; Bridge ID, Device Priority, and Extended System ID; (Optional) Configuring a Secondary Root Device

---

## CCNA5-030 · Network Access

Objectives: 2.5.a, 2.5.b · single · Applied

A converged root bridge has three normal point-to-point links, each to a different downstream switch. There are no shared segments, parallel self-loops, or guard inconsistencies. Which statement is true for this VLAN?

- **A.** Every port must be alternate because root traffic is special.
- **B.** Only one of its three downstream links may ever forward.
- **C.** It selects the lowest numbered downstream link as its root port.
- **D.** It has no root port; these downstream ports are designated.

**Answer: D**

Root-port selection applies to nonroot switches. On the root, these ordinary downstream segments are served by designated ports.

**Option explanations**

- **A:** Its normal downstream ports provide designated paths.
- **B:** Independent downstream segments can each have a designated forwarding port.
- **C:** The root bridge does not require a root port.
- **D:** The root has no upstream path to itself and offers the best root information on these links.

**Further reading**

- [Understand Rapid Spanning Tree Protocol (802.1w)](https://www.cisco.com/c/en/us/support/docs/lan-switching/spanning-tree-protocol/24062-146.html) — New Port States and Port Roles — Port States; Alternate and Backup Port Roles

---

## CCNA5-031 · Network Access

Objectives: 2.5.c · single · Applied

A hypervisor attaches through a trunk carrying several guest VLANs. The design verifies that this host does not bridge to another physical switch and needs edge startup behavior. What is the careful PortFast interpretation?

- **A.** PortFast can apply to a genuine edge trunk when explicitly configured for that role.
- **B.** PortFast proves that the host can never create a loop.
- **C.** PortFast turns off every VLAN on that trunk.
- **D.** PortFast is impossible on any trunk.

**Answer: A**

A trunk can terminate at an edge device. Verify the absence of Layer 2 forwarding paths through the host before applying edge treatment.

**Option explanations**

- **A:** Edge status is about topology, not a rule that all trunks connect switches.
- **B:** Configuration expresses an assumption; it does not prove future host behavior.
- **C:** It changes spanning-tree edge transition behavior, not VLAN admission.
- **D:** Cisco supports explicit edge behavior for suitable trunk attachments.

**Further reading**

- [Layer 2 Configuration Guide, Cisco IOS XE 17.15.x — Configuring Optional Spanning-Tree Features](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst9300/software/release/17-15/configuration_guide/lyr2/b_1715_lyr2_9300_cg/configuring_optional_spanning_tree_features.html) — PortFast; Bridge Protocol Data Unit Guard; Bridge Protocol Data Unit Filtering; Root Guard; Loop Guard

---

## CCNA5-032 · Network Access

Objectives: 2.5.d · single · Challenge

A change review finds spanning-tree bpdufilter enable explicitly configured on both ends of a new redundant switch link. Why is that unsafe?

- **A.** BPDU filtering encrypts BPDUs so peers cannot decrypt them.
- **B.** Filtering makes LACP incompatible with every port-channel.
- **C.** The feature automatically rejects every tagged data frame.
- **D.** The link can forward without exchanging the BPDUs needed to detect its loop contribution.

**Answer: D**

A redundant physical path needs functioning loop prevention. Explicit interface BPDU filtering can remove the information that spanning tree relies on.

**Option explanations**

- **A:** The feature suppresses processing and transmission; it does not encrypt.
- **B:** The identified risk is hidden Layer 2 loops, not a blanket LACP prohibition.
- **C:** Its purpose concerns BPDUs, not all user VLAN tags.
- **D:** Unconditional interface filtering defeats spanning-tree visibility on that path.

**Further reading**

- [Layer 2 Configuration Guide, Cisco IOS XE 17.15.x — Configuring Optional Spanning-Tree Features](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst9300/software/release/17-15/configuration_guide/lyr2/b_1715_lyr2_9300_cg/configuring_optional_spanning_tree_features.html) — PortFast; Bridge Protocol Data Unit Guard; Bridge Protocol Data Unit Filtering; Root Guard; Loop Guard

---

## CCNA5-033 · Network Access

Objectives: 2.6 · single · Applied

A branch AP locally switches employee traffic but centrally switches a guest WLAN to the WLC. Must these WLANs use different physical APs because their data paths differ?

- **A.** Yes; the guest SSID requires sniffer mode.
- **B.** No; because centrally switched traffic bypasses the WLC.
- **C.** Yes; FlexConnect forces every WLAN to use the same local path.
- **D.** No; a FlexConnect AP can use the configured switching behavior for each WLAN.

**Answer: D**

Choose switching behavior per WLAN according to its policy and location. One capable FlexConnect AP can implement the mixed design.

**Option explanations**

- **A:** Sniffer mode is a capture role, not guest service.
- **B:** By definition, that selected client data path reaches the controller.
- **C:** FlexConnect can support both selected central and local switching.
- **D:** Local versus central forwarding can be selected per WLAN in the supported design.

**Further reading**

- [Cisco Wireless Controller Configuration Guide, Release 8.10 — FlexConnect](https://www.cisco.com/c/en/us/td/docs/wireless/controller/8-10/config-guide/b_cg810/flexconnect.html) — Configuring the Switch at a Remote Site; Configuring an Access Point for FlexConnect (GUI)
- [Cisco Wireless Controller Configuration Guide, Release 8.5 — Managing APs](https://www.cisco.com/c/en/us/td/docs/wireless/controller/8-5/config-guide/b_cg85/managing_aps.html) — AP Modes: client-serving and network management modes

---

## CCNA5-034 · Network Access

Objectives: 2.6 · single · Applied

A remote site has functioning LAN and Internet connectivity, but access to its cloud management dashboard is interrupted. For Meraki bridge-mode WLANs with no additional cloud-dependent authentication service, which effect follows directly from loss of management access?

- **A.** All local SSIDs become unencrypted.
- **B.** Every local client frame must stop because it was passing through the dashboard.
- **C.** New cloud configuration and monitoring are impaired, while existing local forwarding can continue.
- **D.** The AP changes automatically into an autonomous Cisco IOS router.

**Answer: C**

Evaluate management and forwarding dependencies separately. The stated design excludes extra cloud authentication dependencies that could change client admission behavior.

**Option explanations**

- **A:** A management outage does not automatically remove the applied security policy.
- **B:** Ordinary bridge-mode client data does not transit the management dashboard.
- **C:** The management outage does not inherently remove the bridge-mode local data path.
- **D:** Loss of dashboard reachability does not change it into that product architecture.

**Further reading**

- [Meraki Cloud Architecture](https://documentation.meraki.com/Platform_Management/Dashboard_Administration/Design_and_Configure/Architectures_and_Best_Practices/Cisco_Meraki_Best_Practice_Design/Meraki_Cloud_Architecture) — Network and Management Data Segregation; The Meraki dashboard

---

## CCNA5-035 · Network Access

Objectives: 2.7 · single · Applied

A campus extends centrally switched client VLANs to the WLC but does not permit the AP management subnet to reach the controller. AP switch ports and power are healthy. What infrastructure requirement is still unmet?

- **A.** The WLAN name must equal the AP management VLAN number.
- **B.** Every AP needs the WLC service port connected directly to its radio.
- **C.** The AP needs its own working IP path to establish controller connectivity.
- **D.** Client VLANs must be removed from the WLC uplink.

**Answer: C**

Build and verify AP-to-controller connectivity independently of the wired client VLANs. Both are needed in a centrally switched deployment.

**Option explanations**

- **A:** SSID strings do not establish network reachability.
- **B:** Service ports are not per-AP tunnel cables.
- **C:** Client VLAN presence at the WLC does not supply AP management transport.
- **D:** Removing the data attachment would not repair the AP’s control path.

**Further reading**

- [Cisco Wireless Controller Configuration Guide, Release 8.10 — AP Connectivity to Controller](https://www.cisco.com/c/en/us/td/docs/wireless/controller/8-10/config-guide/b_cg810/ap_connectivity_to_cisco_wlc.html) — CAPWAP
- [Cisco Wireless Controller Configuration Guide, Release 8.10 — Ports and Interfaces](https://www.cisco.com/c/en/us/td/docs/wireless/controller/8-10/config-guide/b_cg810/ports_and_interfaces.html) — Restrictions on Link Aggregation; Configuring Neighbor Devices to Support Link Aggregation

---

## CCNA5-036 · Network Access

Objectives: 2.7 · single · Applied

A WLC LAG uses four physical links to one access switch. A design review claims the controller remains connected if that entire switch fails. What is wrong with the claim?

- **A.** LAG replicates the access switch’s control plane inside the WLC.
- **B.** Changing VLAN names automatically removes the shared dependency.
- **C.** Four links guarantee four independent network paths.
- **D.** All four links share the same failed switch as a common dependency.

**Answer: D**

Link redundancy and device independence are different. Assess the whole path, including the shared switch and controller, when describing availability.

**Option explanations**

- **A:** It does not create a replacement switching device.
- **B:** Logical names do not change the physical attachment.
- **C:** Link count alone does not establish independent failure domains.
- **D:** Multiple cables protect member failures but not loss of their single termination device.

**Further reading**

- [Cisco Wireless Controller Configuration Guide, Release 8.10 — Ports and Interfaces](https://www.cisco.com/c/en/us/td/docs/wireless/controller/8-10/config-guide/b_cg810/ports_and_interfaces.html) — Restrictions on Link Aggregation; Configuring Neighbor Devices to Support Link Aggregation

---

## CCNA5-037 · Network Access

Objectives: 2.8 · single · Applied

A remote engineer needs to know who entered configuration commands on a Catalyst 9300 switch running IOS XE 17.13 after a change window. Which configured management capability directly supplies that record?

- **A.** Changing all administrators to one shared account
- **B.** Centralized TACACS+ command accounting for the relevant privilege levels
- **C.** LLDP neighbor capability advertisements
- **D.** The presence of an HTTPS padlock alone

**Answer: B**

An encrypted session is not an audit trail by itself. Configure appropriate accounting and identifiable administrator credentials.

**Option explanations**

- **A:** A shared identity weakens attribution instead of providing individual records.
- **B:** Configured command accounting records command activity and the associated username at the accounting server.
- **C:** LLDP describes neighbors, not operator configuration actions.
- **D:** TLS protects a session but does not by itself create command accounting records.

**Further reading**

- [Security Configuration Guide, Cisco IOS XE 17.13.x (Catalyst 9300 Switches) — Configuring Accounting](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst9300/software/release/17-13/configuration_guide/sec/b_1713_sec_9300_cg/configuring_accounting.html) — AAA Accounting Types — Command Accounting

---

## CCNA5-038 · Network Access

Objectives: 2.9 · multiple · Applied

A Catalyst 9800 policy profile for a branch WLAN shows Central Switching enabled. The requirement is local client switching, and Central Association is already disabled. Which TWO checks complete the intended setup? Select TWO.

| Object | Current state |
| --- | --- |
| AP mode | FlexConnect |
| Central Association | Disabled |
| Policy Profile Central Switching | Enabled |
| Requested client data path | Local branch VLAN |

- **A.** Verify the AP’s assigned policy tag maps this WLAN to that profile.
- **B.** Keep the profile unused and change only its description.
- **C.** Disable Central Switching in the relevant policy profile.
- **D.** Enable dedicated monitor mode on the AP.

**Answer: A, C**

A profile’s values matter only when the correct WLAN and AP bindings use it. The FlexConnect site and switch VLAN settings must also be compatible.

**Option explanations**

- **A:** An unreferenced profile does not apply to the serving AP’s WLAN.
- **B:** Descriptions do not bind a WLAN to a forwarding policy.
- **C:** This selects local client data forwarding for the FlexConnect WLAN.
- **D:** That would remove ordinary client service rather than implement local switching.

**Further reading**

- [Configure FlexConnect with Authentication on Catalyst 9800 WLC](https://www.cisco.com/c/en/us/support/docs/wireless/catalyst-9800-series-wireless-controllers/213921-flexconnect-configuration-with-central-a.html) — Background Information; Policy Profile Configuration

---

## CCNA5-039 · Network Access

Objectives: 2.9 · matching · Applied

Match each applied AireOS QoS profile to the standard service class it represents. The profiles have not been customized; use each answer once.

1. Voice handset WLAN
2. Interactive video WLAN
3. Ordinary best-effort employee WLAN
4. Background transfer WLAN

- **A.** Silver
- **B.** Platinum
- **C.** Gold
- **D.** Bronze

**Answer: 1 → B; 2 → C; 3 → A; 4 → D**

These profile names summarize intended service classes. Selecting a profile does not guarantee end-to-end performance under every load.

**Option explanations**

- **A:** The standard profile associated with best effort.
- **B:** The standard profile associated with voice.
- **C:** The standard profile associated with video.
- **D:** The standard profile associated with background traffic.

**Further reading**

- [Cisco Wireless Controller Configuration Guide, Release 8.10 — Wireless Quality of Service](https://www.cisco.com/c/en/us/td/docs/wireless/controller/8-10/config-guide/b_cg810/wireless_quality_of_service.html) — QoS Profiles; Configuring QoS Profiles (GUI); Assigning a QoS Profile to a WLAN (GUI)

---

## CCNA5-040 · Network Access

Objectives: 2.9 · single · Applied

A Catalyst 9800 GUI shows a WLAN mapped to policy profile Guest-Local in the policy tag assigned to AP-9. The engineer edits the unused profile Guest-Test instead. Why do AP-9 clients retain their existing VLAN?

| Configuration object | Value |
| --- | --- |
| AP-9 Policy Tag | Branch-East |
| Branch-East WLAN mapping | Guest → Guest-Local |
| Guest-Local VLAN | 210 |
| Edited profile | Guest-Test VLAN 220 |

- **A.** All profiles with Guest in their names are automatically merged.
- **B.** AP-9’s WLAN still references Guest-Local, so the edited profile is not on its effective configuration path.
- **C.** VLAN changes require a new radio frequency by definition.
- **D.** Policy profiles only control the administrator’s browser theme.

**Answer: B**

Trace the applied object relationships before changing a value. Editing an unused object cannot change the client policy used by this AP.

**Option explanations**

- **A:** Profile names do not imply automatic policy merging.
- **B:** The active policy-tag mapping determines which profile applies.
- **C:** Wired VLAN policy does not inherently require changing RF channels.
- **D:** They include client network and forwarding policies.

**Further reading**

- [Configure FlexConnect with Authentication on Catalyst 9800 WLC](https://www.cisco.com/c/en/us/support/docs/wireless/catalyst-9800-series-wireless-controllers/213921-flexconnect-configuration-with-central-a.html) — Background Information; Policy Profile Configuration

---

## CCNA5-041 · IP Connectivity

Objectives: 3.1.b, 3.1.d · single · Applied

The routing-table line below is installed. An operator interprets 10.240.12.0 as the adjacent router to ARP for. What is the correction?

```text
O 10.240.12.0/22 [110/25] via 192.0.2.18, GigabitEthernet0/3
```

- **A.** 10.240.12.0/22 is the destination prefix; 192.0.2.18 is the next hop.
- **B.** The route uses every address in 10.240.0.0/16 as a next hop.
- **C.** 10.240.12.0 is the local router’s management address.
- **D.** 192.0.2.18 is the subnet mask in decimal form.

**Answer: A**

The destination describes what traffic a route covers; the next hop describes where that traffic goes next. Confusing them leads to incorrect neighbor-resolution troubleshooting.

**Option explanations**

- **A:** The prefix precedes the bracket and the neighbor follows via.
- **B:** The /22 defines destinations, not a pool of neighboring routers.
- **C:** The entry does not identify that address as locally owned.
- **D:** The next-hop address is not a mask.

**Further reading**

- [Configure Route Selection for Routers](https://www.cisco.com/c/en/us/support/docs/ip/enhanced-interior-gateway-routing-protocol-eigrp/8651-21.html) — Build the Routing Table; Make Forwarding Decisions

---

## CCNA5-042 · IP Connectivity

Objectives: 3.1.e, 3.2.b · single · Applied

A static route to a warehouse is changed from distance 1 to 130. OSPF offers the same exact prefix at distance 110. All paths work. Which verification outcome confirms the intended switch to OSPF?

- **A.** All broader prefixes disappear from the RIB.
- **B.** The main routing table now shows the OSPF candidate for that prefix.
- **C.** OSPF’s advertised metric changes to 130 on every neighbor.
- **D.** The static command disappears automatically from running-config.

**Answer: B**

Changing local route preference can alter installed ownership without deleting the backup configuration. Inspect the live route for the exact destination prefix.

**Option explanations**

- **A:** Different destination prefixes can remain independently installed.
- **B:** 110 is preferable to the revised static distance 130.
- **C:** A local static distance change is not a distributed OSPF metric update.
- **D:** A losing static candidate can remain configured.

**Further reading**

- [Understand Administrative Distance](https://www.cisco.com/c/en/us/support/docs/ip/border-gateway-protocol-bgp/15986-admin-distance.html) — RIB Route Comparison; Route Installation; Default AD Values

---

## CCNA5-043 · IP Connectivity

Objectives: 3.2.a · single · Applied

Two installed IPv6 routes are shown. A packet targets 2001:db8:abcd:1234::7. Which interpretation is correct?

```text
S 2001:db8:abcd::/48 [1/0] via 2001:db8:1::2
S 2001:db8:abcd:1234::/64 [200/0] via 2001:db8:2::2
```

- **A.** Neither matches because ::7 is not written in either prefix.
- **B.** The /64 through 2001:db8:2::2 handles this destination.
- **C.** The /48 wins because its administrative distance is lower.
- **D.** Both routes match equally because IPv6 ignores the fourth hextet.

**Answer: B**

IPv6 uses longest-prefix forwarding just as IPv4 does. Matching the variable host portion is not required for a network route.

**Option explanations**

- **A:** Host bits need not be zero in a packet destination to match a network prefix.
- **B:** The entire first four hextets match that more specific installed prefix.
- **C:** Distance does not override specificity between installed prefixes.
- **D:** The fourth hextet contributes to a /64 match.

**Further reading**

- [IPv6 Routing: Static Routing — Cisco IOS XE 17.x](https://www.cisco.com/c/en/us/td/docs/routers/ios/config/17-x/ip-routing/b-ip-routing/m_ip6-route-static-xe.html) — Recursive Static Routes; Fully Specified Static Routes; Floating Static Routes
- [Configure Route Selection for Routers](https://www.cisco.com/c/en/us/support/docs/ip/enhanced-interior-gateway-routing-protocol-eigrp/8651-21.html) — Build the Routing Table; Make Forwarding Decisions

---

## CCNA5-044 · IP Connectivity

Objectives: 3.2.c · single · Foundation

An operator compares two OSPF intra-area paths: one uses a fast but long-distance fiber circuit, the other a slower short circuit. Only interface costs are supplied. What determines the OSPF choice by default?

- **A.** The lower sum of configured or calculated OSPF costs
- **B.** The path whose next-hop address has fewer digits
- **C.** The path with the geographically closest next hop
- **D.** The lower measured application response time

**Answer: A**

A routing metric is a configured model of preference, not a direct guarantee of every performance measure. Validate latency separately if it is a service requirement.

**Option explanations**

- **A:** Ordinary intra-area SPF uses accumulated link cost.
- **B:** Address spelling is unrelated to route cost.
- **C:** Geographic distance is not the default SPF metric.
- **D:** OSPF does not automatically substitute live application latency for link costs.

**Further reading**

- [RFC 2328: OSPF Version 2](https://www.rfc-editor.org/rfc/rfc2328.html) — 9.4 Electing the Designated Router; 10 The Neighbor Data Structure; 16 Calculation of the routing table

---

## CCNA5-045 · IP Connectivity

Objectives: 3.1.g, 3.2.a · multiple · Applied

A branch can reach every corporate /24 in its routing table but no other IPv4 network. Which two pieces of evidence would support a missing-default diagnosis? Select two.

- **A.** The OSPF process number differs from the hub’s.
- **B.** One connected subnet has mask /30.
- **C.** The intended external destination matches none of the installed specific routes.
- **D.** show ip route reports no gateway of last resort and no installed default.

**Answer: C, D**

Combine destination coverage with observed route state. A symptom alone cannot distinguish missing default from a failed remote service.

**Option explanations**

- **A:** Locally different process numbers do not explain missing external coverage.
- **B:** A /30 transit is compatible with perfectly functional default routing.
- **C:** That destination would require a fallback route in this design.
- **D:** The necessary fallback is absent from the operational table.

**Further reading**

- [Configure Route Selection for Routers](https://www.cisco.com/c/en/us/support/docs/ip/enhanced-interior-gateway-routing-protocol-eigrp/8651-21.html) — Build the Routing Table; Make Forwarding Decisions

---

## CCNA5-046 · IP Connectivity

Objectives: 3.3.b · single · Applied

A warehouse router must summarize exactly 10.88.12.0/24, 10.88.13.0/24, 10.88.14.0/24 and 10.88.15.0/24 into one static route. Which destination and mask are correct?

- **A.** 10.88.8.0 255.255.248.0
- **B.** 10.88.12.0 255.255.254.0
- **C.** 10.88.0.0 255.255.0.0
- **D.** 10.88.12.0 255.255.252.0

**Answer: D**

Choose both an aligned network boundary and sufficient prefix length. Four contiguous /24s collapse exactly here because 12 is aligned to a four-block boundary.

**Option explanations**

- **A:** The /21 additionally includes third octets 8–11.
- **B:** A /23 covers only third octets 12–13.
- **C:** The /16 includes many networks outside the stated requirement.
- **D:** The aligned /22 spans exactly third octets 12–15.

**Further reading**

- [RFC 1812: Requirements for IP Version 4 Routers](https://www.rfc-editor.org/rfc/rfc1812.html) — 5.2.4 Determining the Next Hop Address
- [Configure a Next Hop IP Address for Static Routes](https://www.cisco.com/c/en/us/support/docs/dial-access/floating-static-route/118263-technote-nexthop-00.html) — Background Information; Floating Static Route Example

---

## CCNA5-047 · IP Connectivity

Objectives: 3.3.b · single · Applied

A Cisco IOS router has ip route 10.170.0.0 255.255.0.0 GigabitEthernet0/0. The destination is beyond an Ethernet neighbor that has proxy ARP disabled. Why might the route appear installed while remote traffic fails?

- **A.** The interface-only route causes ARP attempts for remote destination addresses.
- **B.** Proxy ARP is required for all correctly specified next-hop statics.
- **C.** The /16 mask disables Ethernet framing.
- **D.** Every installed static route automatically verifies remote application health.

**Answer: A**

Interface reachability can be sufficient for this route to install while the implied neighbor model is wrong. Specify the real next hop on a multiaccess transit.

**Option explanations**

- **A:** The route treats those destinations as directly attached to the Ethernet exit.
- **B:** A route naming the adjacent router can resolve that router normally without proxying remote hosts.
- **C:** Prefix length affects destination scope, not Ethernet frame availability.
- **D:** Route installation does not test application or remote-host delivery.

**Further reading**

- [Configure a Next Hop IP Address for Static Routes](https://www.cisco.com/c/en/us/support/docs/dial-access/floating-static-route/118263-technote-nexthop-00.html) — Background Information; Floating Static Route Example

---

## CCNA5-048 · IP Connectivity

Objectives: 3.3.c, 3.2.a · single · Challenge

A router has an installed /24 through the normal exit and a /32 static exception through a maintenance exit. The maintenance next hop becomes unresolved and the /32 is withdrawn. Both paths were ordinary routes without permanent. What happens to that host’s traffic after convergence?

- **A.** It is permanently blackholed because a /32 once existed.
- **B.** It uses the remaining matching /24.
- **C.** It is sent simultaneously to all default gateways.
- **D.** It creates a /32 through the normal exit automatically in configuration.

**Answer: B**

Fallback depends on which routes remain installed. A removed specific route differs from an installed specific route whose downstream service is broken.

**Option explanations**

- **A:** A withdrawn route does not remain a forwarding match.
- **B:** Removing the host exception allows the broader route to become the longest remaining match.
- **C:** Ordinary forwarding follows the selected remaining match.
- **D:** Using a broader route does not generate a new static command.

**Further reading**

- [Configure Route Selection for Routers](https://www.cisco.com/c/en/us/support/docs/ip/enhanced-interior-gateway-routing-protocol-eigrp/8651-21.html) — Build the Routing Table; Make Forwarding Decisions
- [Configure a Next Hop IP Address for Static Routes](https://www.cisco.com/c/en/us/support/docs/dial-access/floating-static-route/118263-technote-nexthop-00.html) — Background Information; Floating Static Route Example

---

## CCNA5-049 · IP Connectivity

Objectives: 3.3.d · single · Challenge

A backup next hop is reachable only through the same physical interface as the primary next hop. Both statics depend solely on that interface, with no alternate resolution. What happens if that shared interface goes down?

- **A.** Only the lower-distance route is affected by interface state.
- **B.** The primary becomes more reliable because the backup has a larger distance.
- **C.** The higher-distance static creates a new physical link.
- **D.** Both routes can become unusable despite different administrative distances.

**Answer: D**

Two configured routes are not necessarily two independent paths. Verify failure domains in addition to preference order.

**Option explanations**

- **A:** Both routes rely on the same failed interface.
- **B:** Distance represents preference, not physical independence.
- **C:** Administrative preference cannot supply missing hardware connectivity.
- **D:** The common resolving interface is a shared dependency.

**Further reading**

- [Configure a Next Hop IP Address for Static Routes](https://www.cisco.com/c/en/us/support/docs/dial-access/floating-static-route/118263-technote-nexthop-00.html) — Background Information; Floating Static Route Example
- [Understand Administrative Distance](https://www.cisco.com/c/en/us/support/docs/ip/border-gateway-protocol-bgp/15986-admin-distance.html) — RIB Route Comparison; Route Installation; Default AD Values

---

## CCNA5-050 · IP Connectivity

Objectives: 3.3.b · single · Applied

A dual-stack link has the same neighbor link-local address FE80::1 reused on two separate interfaces. A static IPv6 route must use the neighbor on GigabitEthernet0/2. Which information resolves the ambiguity?

- **A.** Use FE80::1/128 as the destination for the remote LAN.
- **B.** Remove the interface and keep FE80::1 alone.
- **C.** Raise the next hop’s OSPF priority.
- **D.** Specify GigabitEthernet0/2 with FE80::1 in the route.

**Answer: D**

Reuse of a link-local value on different links is allowed. The route must carry the link context when that address is the next hop.

**Option explanations**

- **A:** That would describe the neighbor address rather than the remote network.
- **B:** The link-local value alone cannot distinguish the two links.
- **C:** OSPF priority does not select an IPv6 link-local scope.
- **D:** A link-local address is scoped to a link, so the interface identifies the intended neighbor.

**Further reading**

- [IPv6 Routing: Static Routing — Cisco IOS XE 17.x](https://www.cisco.com/c/en/us/td/docs/routers/ios/config/17-x/ip-routing/b-ip-routing/m_ip6-route-static-xe.html) — Recursive Static Routes; Fully Specified Static Routes; Floating Static Routes

---

## CCNA5-051 · IP Connectivity

Objectives: 3.3.a, 3.3.d · multiple · Applied

An IPv6 default learned dynamically has distance 95. Which two proposed static defaults would be less preferred while remaining usable as floating alternatives, assuming valid independent next hops? Select two.

- **A.** A ::/0 static with distance 255
- **B.** A ::/0 static with distance 90
- **C.** A ::/0 static with distance 96
- **D.** A ::/0 static with distance 200

**Answer: C, D**

Choose a distance relative to the actual primary, including any configured override. A backup must also remain independently resolvable.

**Option explanations**

- **A:** 255 prevents installation rather than providing a usable last resort.
- **B:** 90 would be preferred over the dynamic default.
- **C:** 96 is higher than 95 and below the unusable value 255.
- **D:** 200 is a valid less-preferred source distance.

**Further reading**

- [Understand Administrative Distance](https://www.cisco.com/c/en/us/support/docs/ip/border-gateway-protocol-bgp/15986-admin-distance.html) — RIB Route Comparison; Route Installation; Default AD Values
- [IPv6 Routing: Static Routing — Cisco IOS XE 17.x](https://www.cisco.com/c/en/us/td/docs/routers/ios/config/17-x/ip-routing/b-ip-routing/m_ip6-route-static-xe.html) — Recursive Static Routes; Fully Specified Static Routes; Floating Static Routes

---

## CCNA5-052 · IP Connectivity

Objectives: 3.4.a · single · Applied

An OSPF network statement is shown with local interface addresses. Which interfaces does it select for area 0?

```text
router ospf 2
 network 10.6.0.4 0.0.0.3 area 0

Gi0/0 10.6.0.4/31
Gi0/1 10.6.0.6/31
Gi0/2 10.6.0.8/31
```

- **A.** Gi0/2 only
- **B.** Gi0/0 and Gi0/1
- **C.** Gi0/0 only because the statement ends in .4
- **D.** Every interface in 10.0.0.0/8

**Answer: B**

An OSPF network command selects matching local interface addresses. Its wildcard is not a request to install one remote static prefix.

**Option explanations**

- **A:** 10.6.0.8 is outside the wildcard-selected block.
- **B:** Wildcard 0.0.0.3 matches the address block 10.6.0.4–10.6.0.7.
- **C:** A nonzero wildcard permits variation in the low two bits.
- **D:** The first 30 address bits are constrained by this statement.

**Further reading**

- [Configuring OSPF — IP Routing: OSPF Configuration Guide](https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/iproute_ospf/configuration/xe-16/iro-xe-16-book/iro-cfg.html) — Enabling OSPF; Configuring OSPF Interface Parameters

---

## CCNA5-053 · IP Connectivity

Objectives: 3.4.a · single · Applied

The desired transit interface has address 10.92.0.2/30. Which interface-mode command enables OSPF process 7 in area 0 directly, without using a router-level network statement?

- **A.** ip ospf 7 area 0
- **B.** ip ospf router-id 7 area 0
- **C.** ip route 10.92.0.0 255.255.255.252 7
- **D.** router ospf 7 area 0

**Answer: A**

Interface-level activation is explicit and avoids wildcard scope mistakes. Other adjacency requirements must still match the peer.

**Option explanations**

- **A:** This activates the selected interface in the named local process and area.
- **B:** Router-ID selection is not expressed by this activation syntax.
- **C:** A static route command does not enable OSPF on an interface.
- **D:** This is not the interface command syntax for activation.

**Further reading**

- [Configuring OSPF — IP Routing: OSPF Configuration Guide](https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/iproute_ospf/configuration/xe-16/iro-xe-16-book/iro-cfg.html) — Enabling OSPF; Configuring OSPF Interface Parameters

---

## CCNA5-054 · IP Connectivity

Objectives: 3.4.a · single · Applied

Two area-0 peers have compatible addresses, timers, network type, MTU and unique IDs. R1 requires OSPF authentication while R2 sends unauthenticated Hellos. Which action addresses the specific fault?

- **A.** Configure matching OSPF authentication parameters on the link.
- **B.** Use identical local OSPF process numbers.
- **C.** Install a default route on R2.
- **D.** Set both interface costs to the same value.

**Answer: A**

Compatibility includes authentication, not only IP reachability. Do not treat successful ping as proof that OSPF control packets meet the peer’s requirements.

**Option explanations**

- **A:** The peers must agree on the required authentication behavior and credentials.
- **B:** Process-number equality does not authenticate Hello packets.
- **C:** Default routing does not satisfy an OSPF authentication check.
- **D:** Neighbor interface costs may differ and do not repair authentication.

**Further reading**

- [Troubleshoot OSPF Neighbor Problems](https://www.cisco.com/c/en/us/support/docs/ip/open-shortest-path-first-ospf/13699-29.html) — No State Revealed; Neighbors Stuck in Exstart/Exchange State

---

## CCNA5-055 · IP Connectivity

Objectives: 3.4.b · single · Foundation

An Ethernet OSPF link is configured as point-to-point on both ends. An engineer sees that neither neighbor is labeled DR or BDR and proposes increasing priorities. What is the right response?

- **A.** Force a duplicate router ID to create a tie.
- **B.** Increase both priorities until one becomes DR.
- **C.** Keep the intended network type; the absent elected roles are expected.
- **D.** Add a third router without changing the design.

**Answer: C**

Validate the output against the intended OSPF network type. Absence of a broadcast-specific role is not itself a problem.

**Option explanations**

- **A:** Duplicate identifiers are faults, not an election mechanism.
- **B:** Priority changes cannot create an election on this OSPF type.
- **C:** Point-to-point operation intentionally omits DR and BDR.
- **D:** A third participant changes the assumptions of a dedicated point-to-point link.

**Further reading**

- [RFC 2328: OSPF Version 2](https://www.rfc-editor.org/rfc/rfc2328.html) — 9.4 Electing the Designated Router; 10 The Neighbor Data Structure; 16 Calculation of the routing table

---

## CCNA5-056 · IP Connectivity

Objectives: 3.4.c · single · Applied

The DR and BDR are healthy on an OSPF LAN. Only a DROTHER router fails. Which expected behavior best fits this event?

- **A.** The BDR must become DR immediately.
- **B.** The current DR and BDR roles can remain unchanged.
- **C.** Every router must set its priority to zero.
- **D.** All LAN hosts must change their default gateways to the DR.

**Answer: B**

Identify which role was lost before predicting an election effect. Neighbor loss still changes topology information without necessarily changing the elected leaders.

**Option explanations**

- **A:** The current DR has not failed.
- **B:** Losing a non-elected participant does not require displacing healthy incumbents.
- **C:** The protocol does not require making all survivors ineligible.
- **D:** An OSPF DR is not automatically the LAN’s host gateway.

**Further reading**

- [RFC 2328: OSPF Version 2](https://www.rfc-editor.org/rfc/rfc2328.html) — 9.4 Electing the Designated Router; 10 The Neighbor Data Structure; 16 Calculation of the routing table

---

## CCNA5-057 · IP Connectivity

Objectives: 3.4.c, 3.5 · single · Applied

The HSRP active gateway and the OSPF DR on a VLAN are different routers. Both protocols are healthy. Which interpretation is correct?

- **A.** This can be valid because the two protocols elect roles for different functions.
- **B.** The HSRP active must always be the OSPF DR.
- **C.** The OSPF DR cannot forward ordinary IP packets.
- **D.** The HSRP standby must be an OSPF area border router.

**Answer: A**

Do not confuse similarly named leadership roles. A design may coordinate them, but protocol correctness does not require them to be on one device.

**Option explanations**

- **A:** HSRP supplies a virtual first hop; the OSPF DR organizes broadcast adjacency exchange.
- **B:** The protocols have independent selection mechanisms and purposes.
- **C:** DR status does not prohibit data-plane forwarding.
- **D:** Standby status does not determine area membership.

**Further reading**

- [RFC 2328: OSPF Version 2](https://www.rfc-editor.org/rfc/rfc2328.html) — 9.4 Electing the Designated Router; 10 The Neighbor Data Structure; 16 Calculation of the routing table
- [Understand the Hot Standby Router Protocol Features and Functionality](https://www.cisco.com/c/en/us/support/docs/ip/hot-standby-router-protocol-hsrp/9234-hsrpguidetoc.html) — HSRP Background and Operations; HSRP Operation

---

## CCNA5-058 · IP Connectivity

Objectives: 3.4.d · single · Applied

An OSPF process explicitly uses router ID 203.0.113.200, although no interface has that address. Neighbors form normally. Which statement is correct?

- **A.** The router must answer ARP for that address on every interface.
- **B.** The identifier can be valid without being an assigned interface address.
- **C.** The neighbor state must be fabricated because IDs require loopbacks.
- **D.** The router must own the entire 203.0.113.0/24 subnet.

**Answer: B**

Keep identity and reachability separate. Uniqueness is required, but the router-ID command alone does not establish an IP endpoint at that value.

**Option explanations**

- **A:** Router-ID configuration does not assign an IP address to each link.
- **B:** An explicit router ID is a unique 32-bit OSPF identifier.
- **C:** An explicit ID does not require a matching loopback.
- **D:** Selecting an ID does not create network ownership or routes.

**Further reading**

- [Configuring OSPF — IP Routing: OSPF Configuration Guide](https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/iproute_ospf/configuration/xe-16/iro-xe-16-book/iro-cfg.html) — Enabling OSPF; Configuring OSPF Interface Parameters

---

## CCNA5-059 · IP Connectivity

Objectives: 3.2.c · multiple · Applied

An engineer changes only an interface’s OSPF cost from 10 to 100. The link stays up and other adjacency parameters are unchanged. Which two consequences are appropriate to assess? Select two.

- **A.** Paths using the changed outgoing link can become less preferred.
- **B.** The OSPF topology change must converge before final path behavior is assessed.
- **C.** The Hello interval automatically changes to 100 seconds.
- **D.** The local router ID automatically becomes 100.

**Answer: A, B**

Cost is a path-selection input. Verify resulting routes after convergence instead of assuming a cost change also modifies identity or neighbor timers.

**Option explanations**

- **A:** Higher accumulated cost can change shortest-path selection.
- **B:** The updated cost is propagated and routing calculations respond.
- **C:** Cost is independent of Hello timer configuration.
- **D:** Interface cost is unrelated to router-ID selection.

**Further reading**

- [Configuring OSPF — IP Routing: OSPF Configuration Guide](https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/iproute_ospf/configuration/xe-16/iro-xe-16-book/iro-cfg.html) — Enabling OSPF; Configuring OSPF Interface Parameters
- [RFC 2328: OSPF Version 2](https://www.rfc-editor.org/rfc/rfc2328.html) — 9.4 Electing the Designated Router; 10 The Neighbor Data Structure; 16 Calculation of the routing table

---

## CCNA5-060 · IP Connectivity

Objectives: 3.4.a, 3.4.c, 3.4.d · matching · Applied

Match the operator’s verification goal to the most appropriate Cisco IOS command.

1. Determine whether a peer has synchronized to Full
2. Check the local broadcast link’s Hello interval and DR
3. Verify the current process router ID after a restart
4. Find which OSPF-learned prefixes actually won main-table installation

- **A.** show ip ospf neighbor
- **B.** show ip ospf
- **C.** show ip route ospf
- **D.** show ip ospf interface

**Answer: 1 → A; 2 → D; 3 → B; 4 → C**

Choose evidence at the correct scope: neighbor, interface, process, or installed route. One command does not prove every layer is healthy.

**Option explanations**

- **A:** This reports live peers, neighbor states and their roles.
- **B:** This reports the running OSPF process, including its router ID.
- **C:** This filters the main routing table to installed OSPF routes.
- **D:** This reports interface-specific area, timers, network type, cost and elected information.

**Further reading**

- [Configuring OSPF — IP Routing: OSPF Configuration Guide](https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/iproute_ospf/configuration/xe-16/iro-xe-16-book/iro-cfg.html) — Enabling OSPF; Configuring OSPF Interface Parameters
- [Understand OSPF Neighbor States](https://www.cisco.com/c/en/us/support/docs/ip/open-shortest-path-first-ospf/13685-13.html) — OSPF Neighbor States

---

## CCNA5-061 · IP Connectivity

Objectives: 3.2.c · single · Challenge

The table shows all outgoing OSPF interface costs along two complete intra-area paths to a LAN. What change to Path A’s final cost makes the two paths equal?

| Path | Outgoing interface costs, in order |
| --- | --- |
| A | 6, 4, 10 |
| B | 9, 12 |

- **A.** Decrease its final cost from 10 to 9.
- **B.** Increase the first router’s ID by 1.
- **C.** Increase its final cost from 10 to 11.
- **D.** Increase its final cost from 10 to 21.

**Answer: C**

Work with complete path totals rather than individual link values. Equal-cost paths can then qualify for ECMP subject to the configured limit.

**Option explanations**

- **A:** That lowers the path to 19, farther from 21.
- **B:** Router-ID arithmetic does not add path cost.
- **C:** 6 + 4 + 11 equals the alternative’s 9 + 12 = 21.
- **D:** The total becomes 31, not 21.

**Further reading**

- [RFC 2328: OSPF Version 2](https://www.rfc-editor.org/rfc/rfc2328.html) — 9.4 Electing the Designated Router; 10 The Neighbor Data Structure; 16 Calculation of the routing table

---

## CCNA5-062 · IP Connectivity

Objectives: 3.5 · single · Challenge

Two HSRP peers are separated by a VLAN partition that prevents their Hello messages from crossing, while each still serves local hosts. What risk does this create?

- **A.** Each side may believe it should own the active virtual gateway.
- **B.** The routers automatically repair the failed Layer 2 connection.
- **C.** The virtual address must immediately become an IPv6 multicast address.
- **D.** All local hosts automatically migrate to the other switch.

**Answer: A**

Failure detection depends on communication with the peer. A partition differs from a clean single-router power failure and requires checking duplicate active ownership after reconnection.

**Option explanations**

- **A:** Loss of peer visibility can cause conflicting active ownership across a partition.
- **B:** HSRP does not reconstruct the physical or VLAN transport.
- **C:** A partition does not change the configured address family.
- **D:** FHRP cannot move physical host attachments.

**Further reading**

- [Understand the Hot Standby Router Protocol Features and Functionality](https://www.cisco.com/c/en/us/support/docs/ip/hot-standby-router-protocol-hsrp/9234-hsrpguidetoc.html) — HSRP Background and Operations; HSRP Operation

---

## CCNA5-063 · IP Connectivity

Objectives: 3.5 · single · Applied

A host sends traffic to another host in the same /24 VLAN. Its normal mask and connected path are correct. Does an HSRP active-router failover necessarily participate in this local host-to-host forwarding?

- **A.** No, because HSRP disables all local switching.
- **B.** Yes; every Ethernet frame must cross the HSRP active router.
- **C.** Yes; the standby must translate every local destination address.
- **D.** No; the host normally resolves and reaches the local peer directly.

**Answer: D**

Assess redundancy against the actual traffic path. A default-gateway protocol primarily matters when the host needs a routed next hop.

**Option explanations**

- **A:** HSRP does not disable ordinary VLAN switching.
- **B:** Switching within a subnet does not inherently require routed forwarding.
- **C:** HSRP does not provide this address-translation function.
- **D:** Same-subnet traffic does not ordinarily traverse the default gateway.

**Further reading**

- [Understand the Hot Standby Router Protocol Features and Functionality](https://www.cisco.com/c/en/us/support/docs/ip/hot-standby-router-protocol-hsrp/9234-hsrpguidetoc.html) — HSRP Background and Operations; HSRP Operation
- [RFC 1812: Requirements for IP Version 4 Routers](https://www.rfc-editor.org/rfc/rfc1812.html) — 5.2.4 Determining the Next Hop Address

---

## CCNA5-064 · IP Connectivity

Objectives: 3.5 · single · Applied

A recovered HSRP router has higher priority and preemption configured with a delay. Why might the design intentionally wait before reclaiming active status?

- **A.** To eliminate the need for any standby router.
- **B.** To make the virtual IP numerically larger.
- **C.** To allow routing and other required services to become ready first.
- **D.** To cause hosts to run OSPF while waiting.

**Answer: C**

Link-up and full service readiness are different milestones. A preemption delay can reduce disruption during recovery, though its adequacy should be tested.

**Option explanations**

- **A:** Delayed preemption still operates within a redundancy group.
- **B:** Time delay does not alter the virtual address.
- **C:** Immediate gateway ownership can be premature while the recovered router reconverges.
- **D:** Ordinary hosts do not need to become routing peers during this delay.

**Further reading**

- [Use HSRP Preempt and Track Commands](https://www.cisco.com/c/en/us/support/docs/ip/hot-standby-router-protocol-hsrp/13780-6.html) — Preempt and Track Commands

---

## CCNA5-065 · IP Connectivity

Objectives: 3.3.b, 3.1.d · single · Applied

A static network route points to a reachable adjacent router, but packets stop one hop beyond it. The local static remains installed. What does this indicate about local route verification?

- **A.** The adjacent next hop must secretly be the destination host.
- **B.** The installed route proves every downstream router has the correct return path.
- **C.** Reachable next-hop resolution does not prove the complete downstream path works.
- **D.** The local static must automatically change to a different network prefix.

**Answer: C**

Trace the failure beyond the locally resolved adjacency. Route validity and end-to-end delivery must be verified with different evidence.

**Option explanations**

- **A:** A next hop can remain reachable while further forwarding fails.
- **B:** Local installation does not inspect every remote routing table.
- **C:** The local router can keep a valid forwarding entry while a later hop is broken.
- **D:** Static routes do not infer a new destination prefix from distant failure.

**Further reading**

- [Configure a Next Hop IP Address for Static Routes](https://www.cisco.com/c/en/us/support/docs/dial-access/floating-static-route/118263-technote-nexthop-00.html) — Background Information; Floating Static Route Example
- [RFC 1812: Requirements for IP Version 4 Routers](https://www.rfc-editor.org/rfc/rfc1812.html) — 5.2.4 Determining the Next Hop Address

---

## CCNA5-066 · IP Services

Objectives: 4.1 · single · Applied

A technician defines the shown NAT pool and inside-client ACL, but no dynamic translation rule exists. NAT interface roles and routes are correct. Which command binds these two objects for basic dynamic inside-source NAT without port sharing?

```text
access-list 18 permit 10.18.0.0 0.0.0.255
ip nat pool PUBLIC 198.51.100.80 198.51.100.89 netmask 255.255.255.0
```

- **A.** ip nat inside source list 18 pool PUBLIC
- **B.** ip nat outside source list 18 pool PUBLIC
- **C.** ip nat inside source list 18 interface GigabitEthernet0/1 overload
- **D.** ip nat pool PUBLIC 10.18.0.1 10.18.0.254 netmask 255.255.255.0

**Answer: A**

A pool definition only describes available translated addresses. The inside-source list-to-pool rule connects eligible client addresses to that resource.

**Option explanations**

- **A:** This associates ACL 18 with the named global-address pool.
- **B:** This selects outside-source translation instead of inside-source translation.
- **C:** This uses interface-address port sharing rather than the required pool mapping.
- **D:** This replaces the global-address pool with inside addresses and still supplies no binding rule.

**Further reading**

- [IP Addressing Configuration Guide, Cisco IOS XE 17.x — Configuring NAT for IP Address Conservation](https://www.cisco.com/c/en/us/td/docs/routers/ios/config/17-x/ip-addressing/b-ip-addressing/m_iadnat-addr-consv-xe.html) — Inside source address translation; static and dynamic translations; monitoring NAT

---

## CCNA5-067 · IP Services

Objectives: 4.2 · single · Applied

An NTP server permits requests only from a router's loopback address, 10.255.5.5. The router currently sources its requests from the outgoing interface, and the server rejects them. All relevant routes exist. Which IOS configuration aligns the requests with the server policy?

- **A.** ntp master 5
- **B.** clock timezone UTC 0
- **C.** ntp source Loopback0, where Loopback0 is 10.255.5.5
- **D.** logging source-interface Loopback0

**Answer: C**

Management service access policies must match the effective packet source. Selecting the loopback for NTP fixes this source mismatch while the stated routes support responses to it.

**Option explanations**

- **A:** Making the local clock an authority does not fix the requested client source address.
- **B:** Time-zone presentation does not select the packet source.
- **C:** This selects the intended stable source address for the NTP packets.
- **D:** This selects a syslog source, not the NTP source.

**Further reading**

- [Setting Time and Calendar Services](https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/bsm/configuration/15-mt/bsm-15-mt-book/bsm-time-calendar-set.html) — Network Time Protocol; configuring NTP associations; monitoring NTP

---

## CCNA5-068 · IP Services

Objectives: 4.3 · multiple · Applied

A DHCPv4 client with a valid lease enters the normal RENEWING state at T1. Its original server is reachable. Which two statements describe this phase? Select two.

- **A.** It must send a DHCPDISCOVER before every renewal request.
- **B.** It must stop using the address immediately when T1 arrives.
- **C.** It can keep using the still-valid leased address during renewal.
- **D.** It asks a DNS server to extend the DHCP lease.
- **E.** It normally unicasts a DHCPREQUEST to the original leasing server.

**Answer: C, E**

Renewal extends an existing lease rather than necessarily beginning a fresh four-message allocation. If renewal fails, later rebinding and eventual lease expiration are separate state transitions.

**Option explanations**

- **A:** A bound client renewing its lease does not repeat initial discovery first.
- **B:** The lease remains valid beyond T1 until its actual expiration.
- **C:** Reaching T1 does not itself expire the lease.
- **D:** DNS does not own DHCP lease allocation.
- **E:** Renewal first attempts to extend the existing lease with that server.

**Further reading**

- [RFC 2131 — Dynamic Host Configuration Protocol](https://www.rfc-editor.org/rfc/rfc2131.html) — 3.1 Address allocation; 4.3 Server behavior; 4.4 Client behavior

---

## CCNA5-069 · IP Services

Objectives: 4.4 · matching · Applied

Match each SNMP management requirement to the appropriate operation. Use each option once.

1. Read one known temperature-sensor object instance.
2. Retrieve many interface-table values without one request per next entry.
3. Change a writable administrative description using authorized management access.
4. Report an event asynchronously and request acknowledgment of receipt.

- **A.** Get
- **B.** Inform
- **C.** Set
- **D.** GetBulk

**Answer: 1 → A; 2 → D; 3 → C; 4 → B**

SNMP distinguishes object retrieval, authorized modification, and event notification. The object must exist and the requester must have the necessary access for the chosen operation.

**Option explanations**

- **A:** Reads a specifically named object instance.
- **B:** Sends an event notification for which the receiving manager returns a response.
- **C:** Requests a change to a writable managed object.
- **D:** Retrieves multiple successive values efficiently, useful for walking a large table.

**Further reading**

- [RFC 3416 — Version 2 of the Protocol Operations for the Simple Network Management Protocol (SNMP)](https://www.rfc-editor.org/rfc/rfc3416.html) — 4.2 PDU processing: Get, GetNext, GetBulk, Set, notifications

---

## CCNA5-070 · IP Services

Objectives: 4.5 · single · Applied

A router stores logs only in a finite RAM buffer. After a power failure and reboot, the operator needs events from just before the failure. No remote collector or persistent local logging had been configured. Which conclusion is justified?

- **A.** show logging must reconstruct every prior event from the startup configuration.
- **B.** Raising severity to emergencies makes the RAM buffer nonvolatile.
- **C.** A larger in-memory buffer guarantees survival through power loss.
- **D.** The previous RAM-buffer contents may be lost; future retention needs a suitable external or persistent destination.

**Answer: D**

Retention depends on storage and collection design, not just message generation. A local RAM log can help during a running session but is insufficient evidence retention for a total power loss.

**Option explanations**

- **A:** Configuration stores intended settings, not a complete historical event journal.
- **B:** Severity filtering does not change memory persistence.
- **C:** Additional volatile capacity does not provide durability.
- **D:** A volatile buffer does not preserve the prior boot's event history across loss of power.

**Further reading**

- [System Message Logging](https://www.cisco.com/c/en/us/td/docs/routers/access/wireless/software/guide/SysMsgLogging.html) — System log message format; logging destinations; severity levels; timestamps

---

## CCNA5-071 · IP Services

Objectives: 4.6 · single · Applied

A VLAN previously used DHCP server 10.9.0.10. That server is now decommissioned, and its replacement at 10.9.0.20 has working scopes and routes. Static hosts on the VLAN work, but fresh DHCP clients fail. What is the smallest correction to the shown relay configuration?

```text
interface Vlan60
 ip address 10.60.0.1 255.255.255.0
 ip helper-address 10.9.0.10
```

- **A.** Replace the helper address with 10.9.0.20 on Vlan60.
- **B.** Change the VLAN gateway to 10.9.0.20/24.
- **C.** Replace the SVI's static address with ip address dhcp.
- **D.** Change every DHCP scope to the server's 10.9.0.0 subnet.

**Answer: A**

Static reachability can survive while the DHCP provisioning path points to a retired service. Update the helper destination and retain the VLAN's gateway address and client scope.

**Option explanations**

- **A:** The relay still forwards requests to the retired server.
- **B:** The remote server is not the local clients' gateway interface.
- **C:** That would alter the gateway's own addressing, not its server destination.
- **D:** Scopes must still correspond to the client subnet identified by the relay.

**Further reading**

- [IP Addressing: DHCP Configuration Guide, Cisco IOS XE Everest 16.6 — Configuring the Cisco IOS XE DHCP Relay Agent](https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/ipaddr_dhcp/configuration/xe-16-6/dhcp-xe-16-6-book/dhcp-relay-agent-xe.html) — Packet forwarding address; giaddr; specifying the packet forwarding address

---

## CCNA5-072 · IP Services

Objectives: 4.7 · single · Challenge

A 100 Mb/s egress link receives a sustained 140 Mb/s of offered traffic. A finite queue fills even though all packets have valid DSCP markings. Which statement explains why marking alone cannot prevent the drops?

- **A.** Correct markings automatically increase the interface to 140 Mb/s.
- **B.** An infinite retry count in DNS expands the queue.
- **C.** The sustained arrival rate exceeds service capacity; finite buffering cannot absorb the excess indefinitely.
- **D.** Any queue can store unlimited packets if they share one DSCP.

**Answer: C**

Queuing can absorb a bounded burst, but not an unending positive rate difference. QoS determines treatment under contention; it does not remove the capacity constraint.

**Option explanations**

- **A:** A packet label does not change physical capacity.
- **B:** DNS retry behavior does not provide egress buffering capacity.
- **C:** The queue accumulates the continuing 40 Mb/s excess until its capacity is reached.
- **D:** Queue storage remains finite regardless of class labels.

**Further reading**

- [Quality of Service Configuration Guide — Quality of service](https://www.cisco.com/c/en/us/td/docs/switches/lan/c9000/qos/quality-of-service-configuration-guide/m-quality-of-service.html) — Classification; marking; queuing and scheduling; policing and shaping
- [RFC 2475 — An Architecture for Differentiated Services](https://www.rfc-editor.org/rfc/rfc2475.html) — 2.3 Traffic classification and conditioning; 2.4 Per-hop behaviors

---

## CCNA5-073 · IP Services

Objectives: 4.8 · multiple · Applied

A network team needs evidence that an IOS XE router supports SSH version 2 and that an administrator currently has an SSH session. Which two show commands directly provide these distinct checks? Select two.

- **A.** show ip ssh
- **B.** show ntp associations
- **C.** show ssh
- **D.** show ip route
- **E.** show ip nat translations

**Answer: A, C**

Verify both the service configuration and its active use. A server can be enabled with no current sessions, so the two observations answer different questions.

**Option explanations**

- **A:** This displays SSH server version and configuration status.
- **B:** Time-source associations do not list SSH sessions.
- **C:** This displays current SSH server connections.
- **D:** Routes support reachability but do not report the SSH version or session state.
- **E:** NAT bindings do not establish the router's own SSH server state.

**Further reading**

- [Configure SSH on Routers](https://www.cisco.com/c/en/us/support/docs/security-vpn/secure-shell-ssh/4145-ssh.html) — SSH server prerequisites; SSHv2; VTY restrictions; show commands

---

## CCNA5-074 · IP Services

Objectives: 4.8 · single · Applied

A router's SSH host key was deliberately replaced during a documented rebuild. A client now reports that its saved host key differs from the presented key. What should the administrator do before accepting the replacement?

- **A.** Disable all host-key checking permanently.
- **B.** Verify the new fingerprint through an independently trusted record or console path.
- **C.** Assume the password prompt proves the server is the intended router.
- **D.** Treat a successful ICMP echo as proof of the new key's identity.

**Answer: B**

The saved host key binds a server identity to later SSH connections. A legitimate rebuild explains why change is possible, but the replacement fingerprint still needs trustworthy verification before updating that binding.

**Option explanations**

- **A:** That removes server identity verification for future connections.
- **B:** A key change can be legitimate, but authentication of the new key must be re-established.
- **C:** An impostor can also present a password prompt.
- **D:** IP reachability does not authenticate the SSH host key.

**Further reading**

- [RFC 4251 — The Secure Shell (SSH) Protocol Architecture](https://www.rfc-editor.org/rfc/rfc4251.html) — 4 Architecture; 9 Security considerations

---

## CCNA5-075 · IP Services

Objectives: 4.9 · single · Applied

A capture shows a TFTP client sending its initial read request to UDP destination 69. The server replies from UDP port 53012. The firewall allows the request but drops that reply solely because its source port is not 69. Which conclusion is correct?

- **A.** TFTP must negotiate this reply over TCP port 21 first.
- **B.** The server is necessarily violating base TFTP by using any port other than 69.
- **C.** The server may select a transfer-specific port; the rule is too restrictive for this exchange.
- **D.** The client should acknowledge every block back to UDP 69 regardless of the server port.

**Answer: C**

UDP 69 is the rendezvous port for the initial request. Subsequent TFTP packets use the selected endpoint transfer ports, which a firewall must accommodate appropriately.

**Option explanations**

- **A:** FTP's control port is unrelated to TFTP transfer setup.
- **B:** TFTP selects transfer identifiers for the actual transfer.
- **C:** The initial well-known port and the server's transfer identifier need not be the same.
- **D:** The transfer continues using the selected transfer identifiers.

**Further reading**

- [RFC 1350 — The TFTP Protocol (Revision 2)](https://www.rfc-editor.org/info/rfc1350/) — 2 Protocol overview; 3 Relation to other protocols; 4 Initial connection; 6 Normal termination

---

## CCNA5-076 · Security Fundamentals

Objectives: 5.1 · matching · Applied

An incident report contains the following four items. Match each to its security concept. Use each concept once.

1. A reachable service fails to validate a specific input length.
2. A crafted oversized request uses that defect to obtain code execution.
3. A hostile actor intends to take control of the management service.
4. The operator blocks unapproved access paths while arranging a repair.

- **A.** Threat
- **B.** Vulnerability
- **C.** Exploit
- **D.** Mitigation

**Answer: 1 → B; 2 → C; 3 → A; 4 → D**

Separate the weakness, the mechanism using it, the harmful actor or possibility, and the risk-reducing action. They describe different parts of the same event.

**Option explanations**

- **A:** A possible harmful event or actor can exploit a weakness.
- **B:** A weakness can make an asset susceptible to harm.
- **C:** A mechanism or action takes advantage of the weakness.
- **D:** An action reduces the likelihood or impact of harm.

**Further reading**

- [RFC 4949: Internet Security Glossary, Version 2](https://www.rfc-editor.org/rfc/rfc4949.html) — Section 2: threat, vulnerability, exploit, and countermeasure

---

## CCNA5-077 · Security Fundamentals

Objectives: 5.2 · multiple · Applied

A data-room access review finds that a departed contractor’s badge still opens the door. Which two program actions directly address the failure and help prevent recurrence? Select two.

- **A.** Leave the badge active until its originally scheduled annual expiry.
- **B.** Revoke the contractor’s physical access authorization.
- **C.** Tie badge removal to the personnel departure process and verify completion.
- **D.** Publish the contractor’s badge number on the reception wall.

**Answer: B, C**

Access authorization must follow current roles and affiliation. The fix includes removing the stale access and correcting the process that should have removed it.

**Option explanations**

- **A:** That retains known unauthorized access after the contractor has departed.
- **B:** The identified obsolete authorization must stop granting entry.
- **C:** A repeatable offboarding control reduces recurrence.
- **D:** Public disclosure does not revoke the credential.

**Further reading**

- [NIST SP 800-53 Rev. 5: Security and Privacy Controls for Information Systems and Organizations](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-53r5.pdf) — AT-2, AT-3, PE-2, and PE-3: awareness, training, and physical access

---

## CCNA5-078 · Security Fundamentals

Objectives: 5.3 · single · Applied

With AAA disabled, a router has login local on its VTY lines but the local username database is empty. SSH transport and reachability are already verified. What must be added for username-based local authentication to succeed?

- **A.** A default route to a RADIUS server without changing authentication configuration.
- **B.** A valid local username and secret.
- **C.** Only an enable secret.
- **D.** Only a password command under the VTY lines.

**Answer: B**

The line selects the local account database, so that database must contain the intended user. Transport reachability and authentication prerequisites are separate checks.

**Option explanations**

- **A:** The selected method is local; routing alone does not configure server authentication.
- **B:** login local needs an actual account in the local database.
- **C:** That controls the enable transition and does not create a login account.
- **D:** A line password is not the credential source selected by login local.

**Further reading**

- [Catalyst 3750-X and 3560-X Configuration Guide: Configuring Switch-Based Authentication](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst3750x_3560x/software/release/15-0_2_se/configuration/guide/3750x_cg/swauthen.html) — Protecting Access to Privileged EXEC Commands; Configuring Username and Password Pairs

---

## CCNA5-079 · Security Fundamentals

Objectives: 5.4 · single · Applied

An administrator accidentally pastes a live device password into an unrestricted ticket. Removing the visible text is possible. Which response best addresses the credential exposure?

- **A.** Raise minimum password complexity without changing the exposed active credential.
- **B.** Delete the text and assume nobody retained it.
- **C.** Remove the exposed text and rotate the credential through the approved process.
- **D.** Append an exclamation mark to the public ticket without changing the device password.

**Answer: C**

Treat the disclosed credential as exposed even if the ticket is edited. Invalidate the old value and distribute its replacement only through approved channels.

**Option explanations**

- **A:** A prospective policy requirement does not invalidate the already disclosed password.
- **B:** The exposed value may already have been copied or logged.
- **C:** Copies or prior readers may retain the old value, so deletion alone is insufficient.
- **D:** The live credential remains unchanged.

**Further reading**

- [NIST SP 800-63B-4: Digital Identity Guidelines — Authentication and Authenticator Management](https://pages.nist.gov/800-63-4/sp800-63b.html) — Authentication factors; password verifiers; authenticator management

---

## CCNA5-080 · Security Fundamentals

Objectives: 5.5 · single · Applied

A remote-access VPN policy gives a support laptop access to two internal subnets. A successful tunnel connection is followed by a denied application login. Which explanation is most consistent with a correctly separated design?

- **A.** IPsec cannot transport application-layer authentication messages.
- **B.** Every application must accept a user whenever a VPN connects.
- **C.** A received application denial proves that the tunnel cannot forward any application traffic.
- **D.** VPN connectivity and application authorization are independent controls.

**Answer: D**

A VPN establishes a protected network path under its policy. The application may still require its own credentials and permissions before providing service.

**Option explanations**

- **A:** IPsec can carry ordinary application traffic.
- **B:** Tunnel admission does not imply unrestricted application authorization.
- **C:** An application-level response can traverse a functioning tunnel while the application refuses access.
- **D:** Access to a network path need not grant an application identity permission.

**Further reading**

- [RFC 4301: Security Architecture for the Internet Protocol](https://www.rfc-editor.org/rfc/rfc4301.html) — Sections 3, 4.1, 4.4.1: IPsec services, tunnel mode, and security policy

---

## CCNA5-081 · Security Fundamentals

Objectives: 5.6 · single · Applied

An engineer added deny tcp any host 192.0.2.90 eq 23 to the end of the displayed ACL. Telnet to that host is still permitted. Which edit enforces the Telnet restriction while preserving all other traffic?

```text
ip access-list extended SERVER-OUT
 10 permit ip any any
 20 deny tcp any host 192.0.2.90 eq 23
```

- **A.** Insert the Telnet deny before permit ip any any.
- **B.** Replace eq 23 with eq 22 but keep the same position.
- **C.** Change the ACL’s name without changing order.
- **D.** Append a second identical Telnet deny after the first.

**Answer: A**

The existing broad permit matches the test before the appended denial is reached. Entry order must express the exception before the general case.

**Option explanations**

- **A:** The specific rejection must be evaluated before the general permit.
- **B:** That targets SSH and is still shadowed by the general permit.
- **C:** The name does not affect rule evaluation order.
- **D:** Both later denies remain unreachable for traffic already permitted.

**Further reading**

- [Configure IP Access Lists](https://www.cisco.com/c/en/us/support/docs/security/ios-firewall/23602-confaccesslists.html) — ACL Concepts; Masks; Process ACLs; Apply ACLs; Extended ACLs

---

## CCNA5-082 · Security Fundamentals

Objectives: 5.7 · single · Applied

A phone and its attached PC send two distinct source MAC addresses through one access port. Port security permits only one secure address, and the phone’s address has already been learned. What configuration change permits exactly these two approved sources without disabling port security?

- **A.** Keep maximum 1 and enable PortFast.
- **B.** Set maximum 2 and use approved secure entries for the phone and PC.
- **C.** Change the violation mode to protect and keep maximum 1.
- **D.** Trust the port for DHCP snooping only.

**Answer: B**

The phone’s embedded switch can place multiple source MACs on one physical link. Size and verify the secure-address policy for the actual approved endpoint population.

**Option explanations**

- **A:** STP edge behavior does not increase the secure source limit.
- **B:** Two accepted source identities require a two-address allowance and correct bindings.
- **C:** Protect still drops sources beyond the configured maximum.
- **D:** DHCP trust does not change port-security enforcement.

**Further reading**

- [Catalyst 3750-X and 3560-X Configuration Guide: Configuring Port-Based Traffic Control](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst3750x_3560x/software/release/15-0_2_se/configuration/guide/3750x_cg/swtrafc.html) — Secure MAC Addresses; Security Violations; Port Security Aging

---

## CCNA5-083 · Security Fundamentals

Objectives: 5.8 · single · Applied

The security team can see a login success record, but cannot determine which configuration commands the user entered. Which statement is accurate?

- **A.** Accounting replaces the need to authenticate a user.
- **B.** Session authentication evidence does not by itself provide command accounting.
- **C.** A login success proves every later command was recorded.
- **D.** Command authorization always stores a permanent command history automatically.

**Answer: B**

Specify accounting granularity explicitly. Session start and stop records may be adequate for one requirement, but an investigation of changes needs suitable activity records.

**Option explanations**

- **A:** Recording activity does not verify identity.
- **B:** A login result and a record of executed commands are different evidence.
- **C:** There is no guarantee of command-level accounting in the premise.
- **D:** A permission decision does not inherently establish retained accounting records.

**Further reading**

- [RFC 8907: The Terminal Access Controller Access-Control System Plus (TACACS+) Protocol](https://www.rfc-editor.org/rfc/rfc8907.html) — Sections 5, 6, and 7: authentication, authorization, and accounting

---

## CCNA5-084 · Security Fundamentals

Objectives: 5.9 · multiple · Applied

Which two statements correctly compare common WLAN security arrangements? Select two.

- **A.** WPA3-Personal uses SAE for password-based authentication.
- **B.** WPA-Personal and WPA3-Personal are identical if their passphrase text matches.
- **C.** WPA2-Personal can use a shared PSK with AES-CCMP.
- **D.** WPA2-Enterprise requires every employee to know one common WLAN PSK.

**Answer: A, C**

Compare both the authentication method and the data-protection mode. Reusing a password does not turn a legacy protocol into WPA3.

**Option explanations**

- **A:** SAE is the WPA3-Personal authentication mechanism.
- **B:** Using the same text does not make the protocols or exchanges identical.
- **C:** This is a standard personal-authentication and cipher combination.
- **D:** Enterprise authentication is based on 802.1X rather than a required shared personal PSK.

**Further reading**

- [Cisco Wireless Controller Configuration Guide, Release 8.10: WLAN Security](https://www.cisco.com/c/en/us/td/docs/wireless/controller/8-10/config-guide/b_cg810/wlan_security.html) — WPA1+WPA2; Configuring WPA1+WPA2 (GUI); Protected Management Frames
- [Cisco Catalyst 9800 Configuration Guide, IOS XE 17.3.x: Wi-Fi Protected Access 3](https://www.cisco.com/c/en/us/td/docs/wireless/controller/9800/17-3/config-guide/b_wl_17_3_cg/m_wpa3.html) — WPA3-Personal; WPA3-Personal Transition Mode; Protected Management Frames

---

## CCNA5-085 · Security Fundamentals

Objectives: 5.10 · single · Applied

A technician enters a 64-digit hexadecimal raw PSK in an AireOS 8.10 WLAN GUI, but leaves PSK Format set to ASCII. The intended key is exactly those 32 bytes, not a passphrase. What adjustment is needed?

- **A.** Select 802.1X instead of PSK.
- **B.** Select HEX for PSK Format and enter the same valid 64 hexadecimal digits.
- **C.** Delete one digit and keep ASCII.
- **D.** Enter the digits as the SSID and leave the PSK empty.

**Answer: B**

Input format determines whether the field contains a passphrase or raw hexadecimal key material. The specified 64-digit key must be entered using HEX format.

**Option explanations**

- **A:** That changes the authentication design and does not encode the intended PSK.
- **B:** HEX tells the controller to interpret the input as a raw 256-bit key.
- **C:** That changes the intended credential and turns it into a different passphrase input.
- **D:** The network name is not the preshared key field.

**Further reading**

- [Cisco Wireless Controller Configuration Guide, Release 8.10: WLAN Security](https://www.cisco.com/c/en/us/td/docs/wireless/controller/8-10/config-guide/b_cg810/wlan_security.html) — WPA1+WPA2; Configuring WPA1+WPA2 (GUI); Protected Management Frames

---

## CCNA5-086 · Security Fundamentals

Objectives: 5.6 · single · Applied

During a controlled ACL test, counters start at zero. One TCP packet to destination port 22 enters the interface, then show access-lists reports the following. What does this evidence establish?

```text
Extended IP access list EDGE-IN
 10 deny tcp any host 203.0.113.7 eq 22 (1 match)
 20 permit ip any any (0 matches)
```

- **A.** The router has no route to the destination.
- **B.** The packet matched the SSH deny entry on this observed ACL.
- **C.** The ACL permits SSH because the last entry is a permit.
- **D.** The SSH application authenticated the user and then rejected a command.

**Answer: B**

A controlled counter change connects the test packet to a specific filtering decision. It establishes the local ACL action, not the state of the remote application.

**Option explanations**

- **A:** ACL matches do not reveal the routing table’s contents.
- **B:** The matching deny counter increased for the controlled test.
- **C:** The earlier match ends ACL processing.
- **D:** An ACL counter does not demonstrate application authentication.

**Further reading**

- [Configure IP Access Lists](https://www.cisco.com/c/en/us/support/docs/security/ios-firewall/23602-confaccesslists.html) — ACL Concepts; Masks; Process ACLs; Apply ACLs; Extended ACLs

---

## CCNA5-087 · Security Fundamentals

Objectives: 5.6 · single · Applied

A router’s output ACL toward a client permits only TCP from a web server’s source port 443. The client also uses a DNS server over UDP. Both have valid routes. Why can HTTPS return packets pass while DNS replies fail?

- **A.** HTTPS and DNS must always use the same transport protocol.
- **B.** A valid route overrides an explicit or implicit ACL deny.
- **C.** A TCP permit does not also permit UDP DNS traffic.
- **D.** An outbound ACL does not inspect return traffic.

**Answer: C**

Stateless ACL entries match their specified protocol and fields. A permitted service’s return traffic does not implicitly permit another service.

**Option explanations**

- **A:** Ordinary DNS UDP traffic differs from HTTPS over TCP in this case.
- **B:** Routing reachability does not bypass interface filtering.
- **C:** The DNS reply needs its own matching permit under the restrictive ACL.
- **D:** Return packets leaving the interface are still subject to its output ACL.

**Further reading**

- [Configure IP Access Lists](https://www.cisco.com/c/en/us/support/docs/security/ios-firewall/23602-confaccesslists.html) — ACL Concepts; Masks; Process ACLs; Apply ACLs; Extended ACLs

---

## CCNA5-088 · Security Fundamentals

Objectives: 5.7 · single · Applied

An authorized DHCP server is reached through a verified uplink. The uplink is trusted for DHCP snooping, but remains untrusted for DAI. Which conclusion follows?

- **A.** DHCP snooping trust automatically disables every Layer 2 security feature on the interface.
- **B.** ARP messages are DHCP server replies and inherit DHCP trust.
- **C.** DAI can inspect only ports with DHCP snooping disabled.
- **D.** The two features have separate trust settings; DHCP trust alone does not bypass ARP inspection.

**Answer: D**

Do not infer one feature’s effective state from another feature’s trust flag. Verify DHCP snooping and DAI interface treatment separately.

**Option explanations**

- **A:** The command changes DHCP snooping treatment, not all protections.
- **B:** ARP and DHCP are different protocols.
- **C:** The features are commonly used together.
- **D:** Trust is configured independently for the inspection features.

**Further reading**

- [Catalyst 3750-X and 3560-X Configuration Guide: Configuring DHCP Features and IP Source Guard](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst3750x_3560x/software/release/15-0_2_se/configuration/guide/3750x_cg/swdhcp82.html) — DHCP Snooping; DHCP Snooping Binding Database; Enabling DHCP Snooping
- [Catalyst 3750-X and 3560-X Configuration Guide: Configuring Dynamic ARP Inspection](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst3750x_3560x/software/release/15-0_2_se/configuration/guide/3750x_cg/swdynarp.html) — Understanding Dynamic ARP Inspection; Rate Limiting; ARP ACLs

---

## CCNA5-089 · Security Fundamentals

Objectives: 5.7 · multiple · Applied

An operator enables DAI on a user VLAN after clients have obtained DHCP leases. Which two verification checks directly help explain whether ordinary client ARP should pass? Select two.

- **A.** Confirm the ingress trust state and any applied ARP ACL for the VLAN.
- **B.** Confirm the expected client IP-to-MAC bindings exist in the snooping database.
- **C.** Confirm every access port has become a routed port.
- **D.** Confirm that the switch’s hostname contains the VLAN number.

**Answer: A, B**

Check the information DAI actually consults and where inspection occurs. A VLAN-level enable command alone is not proof that every legitimate static or dynamic host is authorized.

**Option explanations**

- **A:** These determine whether and how the packet is inspected.
- **B:** Untrusted ARP needs an authorized mapping unless another configured policy supplies it.
- **C:** Changing the access architecture is neither required nor a validation check for this VLAN design.
- **D:** Naming conventions do not determine ARP validation.

**Further reading**

- [Catalyst 3750-X and 3560-X Configuration Guide: Configuring Dynamic ARP Inspection](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst3750x_3560x/software/release/15-0_2_se/configuration/guide/3750x_cg/swdynarp.html) — Understanding Dynamic ARP Inspection; Rate Limiting; ARP ACLs

---

## CCNA5-090 · Security Fundamentals

Objectives: 5.3 · single · Applied

A new local password works until the router is power-cycled, after which the previous password works again. No automation restores configuration. What is the most likely missed operation?

- **A.** Saving the verified running configuration to startup configuration.
- **B.** Changing the banner after changing the password.
- **C.** Replacing the console cable after authentication succeeds.
- **D.** Disabling the router’s forwarding interfaces.

**Answer: A**

A working running configuration and a persistent startup configuration are different states. Verify the change, then save it so reboot restores the intended credentials.

**Option explanations**

- **A:** The restart loads the older saved credential if the updated running state was not saved.
- **B:** A banner does not persist local credentials.
- **C:** A cable cannot choose which configured password returns after restart.
- **D:** Interface shutdown is unrelated to saving the password.

**Further reading**

- [Catalyst 3750-X and 3560-X Configuration Guide: Configuring Switch-Based Authentication](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst3750x_3560x/software/release/15-0_2_se/configuration/guide/3750x_cg/swauthen.html) — Protecting Access to Privileged EXEC Commands; Configuring Username and Password Pairs

---

## CCNA5-091 · Automation and Programmability

Objectives: 6.1 · single · Applied

Before pushing a switch template, an automation workflow compares its required features with each target’s platform and software version. What problem does this precheck address most directly?

- **A.** Every platform implements every command identically
- **B.** The speed at which Ethernet frames enter a port
- **C.** Whether all users have memorized the switch hostname
- **D.** Applying an unsupported configuration to an incompatible target

**Answer: D**

A common automation workflow can encounter different device capabilities. Checking explicit requirements before deployment helps identify incompatible targets before their configuration is changed.

**Option explanations**

- **A:** Platform and release differences are the reason compatibility needs checking.
- **B:** The precheck concerns configuration support, not physical frame timing.
- **C:** User recollection is unrelated to feature compatibility.
- **D:** The check can identify targets that do not meet the template’s requirements.

**Further reading**

- [What Is Network Automation?](https://www.cisco.com/site/us/en/learn/topics/networking/what-is-network-automation.html) — Network automation; profiles and policies; automated lifecycle management
- [How Network Automation is Different](https://docs.ansible.com/projects/ansible/latest/network/getting_started/network_differences.html) — Execution on the control node; Multiple communication protocols; Collections organized by network platform

---

## CCNA5-092 · Automation and Programmability

Objectives: 6.2 · single · Applied

A controller-based design uses three cooperating controller servers to present one logical policy service. How does this compare with a single logical controller?

- **A.** A logical controller must always be one physical computer
- **B.** A single logical control service can be implemented by multiple servers
- **C.** Three servers force each data packet to traverse all three
- **D.** Using multiple servers makes a northbound API impossible

**Answer: B**

Logical and physical organization are different dimensions. A controller cluster can provide one logical service, although its actual availability still depends on its implementation and failure conditions.

**Option explanations**

- **A:** Logical centralization does not dictate the physical server count.
- **B:** The physical cluster can present a coordinated logical controller.
- **C:** Controller replication does not inherently place all servers in the user path.
- **D:** Applications can consume a logical service backed by several servers.

**Further reading**

- [RFC 7426: Software-Defined Networking (SDN): Layers and Architecture Terminology](https://www.rfc-editor.org/rfc/rfc7426.html) — 3.1 Overview; 3.2 Network Devices; 3.3 Control Plane; 3.5.3 Locality

---

## CCNA5-093 · Automation and Programmability

Objectives: 6.3.b · multiple · Applied

A service application sends a network intent to a controller. The controller uses a device-management protocol to implement the request. Which two functions belong to these respective boundaries? Select two.

- **A.** The application uses the controller’s northbound interface
- **B.** The application must directly program every switch ASIC
- **C.** The controller uses a southbound interface toward managed devices
- **D.** The southbound API is defined by traffic going geographically south
- **E.** The application’s reply to the controller becomes a new data plane

**Answer: A, C**

The application consumes the controller’s service abstraction through the northbound side. The controller interacts with managed devices through its southbound side.

**Option explanations**

- **A:** The northbound boundary exposes network services to applications.
- **B:** The controller abstraction can hide those device-specific details.
- **C:** That boundary connects the controller with the infrastructure it manages.
- **D:** Northbound and southbound are architectural labels, not compass directions.
- **E:** Application API exchanges do not replace device forwarding.

**Further reading**

- [Software-Defined Networking (SDN) Definition](https://www.cisco.com/c/en/us/solutions/software-defined-networking/overview.html) — SDN elements; Features and benefits
- [RFC 7426: Software-Defined Networking (SDN): Layers and Architecture Terminology](https://www.rfc-editor.org/rfc/rfc7426.html) — 3.1 Overview; 3.2 Network Devices; 3.3 Control Plane; 3.5.3 Locality

---

## CCNA5-094 · Automation and Programmability

Objectives: 6.4 · single · Applied

A script sends an alert whenever utilization exceeds a manually entered 80% threshold. It does not learn from past data or adapt that threshold. Which conclusion is justified?

- **A.** The script is generative AI because it creates an alert message
- **B.** Every automated action is evidence of machine learning
- **C.** The script demonstrates rule-based automation, not a learned model
- **D.** The script must forecast tomorrow’s utilization before alerting

**Answer: C**

Automation and machine learning are not interchangeable. This script executes an explicitly programmed condition rather than deriving a decision model from data.

**Option explanations**

- **A:** Creating a fixed alert message does not establish a generative model.
- **B:** Automation can execute fixed rules without learning.
- **C:** The described decision rule was explicitly programmed and remains fixed.
- **D:** The stated rule compares the present observation with a threshold.

**Further reading**

- [What is AIOps?](https://developer.cisco.com/articles/what-is-aiops/) — The core components of AIOps; Is AIOps all you need?

---

## CCNA5-095 · Automation and Programmability

Objectives: 6.5 · single · Applied

A controller returns the response shown after accepting a configuration job. The API documentation says jobs run asynchronously. What does this response establish?

```text
HTTP/1.1 202 Accepted
Content-Type: application/json

{"jobId":"job-327","status":"queued"}
```

- **A.** The server accepted the request; the client should check the job’s final result
- **B.** Every target device has already applied and verified the change
- **C.** The request was rejected because 202 is a client error
- **D.** The client must immediately repeat POST to acknowledge the job

**Answer: A**

Acceptance and completion are different states in an asynchronous API. The client should follow the documented job-status process to learn whether execution ultimately succeeded.

**Option explanations**

- **A:** 202 Accepted does not establish completion of asynchronous processing.
- **B:** The response reports acceptance rather than per-device success.
- **C:** 202 belongs to the successful 2xx response class.
- **D:** No such duplicate-submission requirement is stated.

**Further reading**

- [RFC 9110: HTTP Semantics](https://www.rfc-editor.org/rfc/rfc9110.html) — 9 Methods; 15 Status Codes

---

## CCNA5-096 · Automation and Programmability

Objectives: 6.5 · single · Applied

A device API documents JSON and XML representations for its interface resource. A client can use the same URI and GET method with different supported response media types. Which statement is accurate?

- **A.** Changing representation changes GET into a Create operation
- **B.** XML responses prove the API cannot be REST-based
- **C.** JSON carries authentication automatically but XML cannot
- **D.** The resource can have different representations without changing the requested Read operation

**Answer: D**

An API resource can be represented in supported formats such as JSON or XML. The retrieval operation remains GET/Read even when the representation format changes.

**Option explanations**

- **A:** The method still requests retrieval.
- **B:** REST does not require JSON as its only representation format.
- **C:** Neither encoding supplies authentication by itself.
- **D:** The resource identity, operation and data encoding are separate concepts.

**Further reading**

- [RFC 9110: HTTP Semantics](https://www.rfc-editor.org/rfc/rfc9110.html) — 9 Methods; 15 Status Codes
- [Architectural Styles and the Design of Network-based Software Architectures, Chapter 5: Representational State Transfer](https://ics.uci.edu/~fielding/pubs/dissertation/rest_arch_style.htm) — 5.1.3 Stateless; 5.1.5 Uniform Interface

---

## CCNA5-097 · Automation and Programmability

Objectives: 6.6 · multiple · Challenge

An engineer wants to preview changes from an Ansible playbook. Every task’s module supports check mode, and no task forces normal execution. Which two statements apply to running it with --check? Select two.

- **A.** It guarantees that production application traffic will work after a later deployment
- **B.** Supported modules report changes they would make
- **C.** It encrypts all playbook secrets automatically
- **D.** It applies all changes and then rolls them back
- **E.** It can help review the playbook without applying its remote changes

**Answer: B, E**

Check mode is useful for previewing supported configuration tasks. It is not proof of application-level correctness, and its guarantees depend on module support and task settings.

**Option explanations**

- **A:** A dry run is not an end-to-end service acceptance test.
- **B:** Check mode can describe proposed changes.
- **C:** Check mode controls execution behavior, not secret encryption.
- **D:** Under these assumptions it does not apply the changes in the first place.
- **E:** The stated support and absence of overrides permit the dry-run behavior.

**Further reading**

- [Validating tasks: check mode and diff mode](https://docs.ansible.com/projects/ansible/latest/playbook_guide/playbooks_checkmode.html) — Using check mode; Using diff mode; Enforcing or preventing check mode on tasks

---

## CCNA5-098 · Automation and Programmability

Objectives: 6.6 · single · Applied

Terraform manages an existing virtual network. The team deletes only Terraform’s state file, leaving the actual network and configuration untouched. Which risk should it recognize?

- **A.** Deleting state automatically deletes the network through its API
- **B.** The configuration becomes a complete replacement for every missing object binding
- **C.** Terraform loses recorded bindings to the existing managed objects
- **D.** The virtual network immediately stops routing because state is its forwarding table

**Answer: C**

Terraform state records the relationship between resource declarations and real objects. Losing that information can lead to unintended management behavior even though the infrastructure still exists.

**Option explanations**

- **A:** Removing a local tracking file is not a resource-destruction request.
- **B:** Configuration alone does not necessarily identify the real managed object IDs.
- **C:** State maps resource declarations to actual objects, so losing it disrupts management.
- **D:** Terraform state is management metadata, not the network’s packet-forwarding table.

**Further reading**

- [State](https://developer.hashicorp.com/terraform/language/state) — State; mapping configuration to real resources

---

## CCNA5-099 · Automation and Programmability

Objectives: 6.7 · single · Applied

A response schema defines serial:null as “unknown,” serial:"" as “known empty text,” and an omitted serial member as “not returned.” The exhibit is one response. Which interpretation fits it?

```text
{"hostname":"wireless-2","serial":null}
```

- **A.** The serial value is explicitly unknown
- **B.** The serial field was omitted from the response
- **C.** The serial value is a zero-length string
- **D.** The serial value is the string null

**Answer: A**

JSON null, an empty string and an absent object member are different structures. The scenario’s explicit schema determines what those distinctions mean operationally.

**Option explanations**

- **A:** The member is present with the null literal as defined by this schema.
- **B:** The member is visibly present.
- **C:** A zero-length string would be written as "".
- **D:** The value would need quotation marks to be that string.

**Further reading**

- [RFC 8259: The JavaScript Object Notation (JSON) Data Interchange Format](https://www.rfc-editor.org/rfc/rfc8259.html) — 2 JSON Grammar; 3 Values; 4 Objects; 5 Arrays; 6 Numbers; 7 Strings

---

## CCNA5-100 · Automation and Programmability

Objectives: 6.7 · single · Applied

The interface API expects counters to be a JSON object with numeric in and out members. Which candidate meets that requirement?

- **A.** {"counters":[12,9]}
- **B.** {"counters":{"in":"12","out":"9"}}
- **C.** {"counters":"{in:12,out:9}"}
- **D.** {"counters":{"in":12,"out":9}}

**Answer: D**

Valid JSON alone is not enough to satisfy a particular API’s data contract. The accepted candidate has both the required object structure and the required numeric value types.

**Option explanations**

- **A:** This supplies an array, without named in and out members.
- **B:** The values are strings rather than the required numbers.
- **C:** The counters value is one string, not a nested object.
- **D:** The nested object contains the required names and numeric values.

**Further reading**

- [RFC 8259: The JavaScript Object Notation (JSON) Data Interchange Format](https://www.rfc-editor.org/rfc/rfc8259.html) — 2 JSON Grammar; 3 Values; 4 Objects; 5 Arrays; 6 Numbers; 7 Strings

---
