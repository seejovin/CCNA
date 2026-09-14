# CCNA Practice — Set 02

100 original questions aligned to CCNA 200-301 v1.1. No interactive labs.

Answers and explanations follow each question. For an unrevealed attempt, use the Streamlit app.

Content review date: 2026-09-14.

## CCNA2-001 · Network Fundamentals

Objectives: 1.1.a, 1.1.b · single · Foundation

Two departments occupy different IP subnets on separate VLANs. Their switch forwards frames only at Layer 2. Which additional capability is required for the departments to exchange IP packets?

- **A.** A larger dynamic MAC table
- **B.** IP routing between the VLANs
- **C.** A shared SSID
- **D.** PoE on both uplinks

**Answer: B**

Each VLAN provides a separate Layer 2 domain. Communication between its IP subnet and another subnet requires a Layer 3 forwarding function.

**Option explanations**

- **A:** More MAC entries do not provide inter-subnet forwarding.
- **B:** A router or routing-enabled Layer 3 switch connects their IP networks.
- **C:** An SSID identifies a wireless network, not an inter-VLAN route.
- **D:** Electrical power delivery does not route IP packets.

**Further reading**

- [Comparing Layer 3 and Layer 2 Switches](https://documentation.meraki.com/Switching/MS_-_Switches/Design_and_Configure/Configuration_Guides/Layer_3_Switching/Comparing_Layer_3_and_Layer_2_Switches) — Comparing Layer 3 and Layer 2 Switches (main article)

---

## CCNA2-002 · Network Fundamentals

Objectives: 1.2.c · single · Applied

In a basic two-tier spine-leaf fabric, a server on Leaf A exchanges traffic with a server on Leaf B. Every leaf connects to every spine, with no leaf-to-leaf links. Which path follows this architecture?

- **A.** Leaf A → another leaf → Leaf B
- **B.** Leaf A → spine → another spine → Leaf B
- **C.** Leaf A → distribution → campus core → Leaf B
- **D.** Leaf A → one spine → Leaf B

**Answer: D**

The leaf-spine-leaf path crosses the fabric through one spine. Adding servers on different leaves does not insert a campus distribution tier.

**Option explanations**

- **A:** The design explicitly has no leaf-to-leaf links.
- **B:** The stated two-tier fabric does not require spine-to-spine transit.
- **C:** Those are campus tiers, absent from this fabric.
- **D:** A spine connects directly to both leaves.

**Further reading**

- [Cisco Massively Scalable Data Center Network Fabric Design and Operation White Paper](https://www.cisco.com/c/en/us/products/collateral/switches/nexus-9000-series-switches/white-paper-c11-743245.html) — MSDC Layer 3 IP fabric design evolution; Cisco MSDC design example 1: Two-tiered spine-leaf topology

---

## CCNA2-003 · Network Fundamentals

Objectives: 1.3.a · single · Applied

A switch uplink must cross an electrically noisy production area. Cable length is within both candidate Ethernet standards, and power delivery is unnecessary. Which property favors optical fiber over copper?

- **A.** Fiber does not carry data as electrical current susceptible to electromagnetic pickup
- **B.** Fiber always supports any optic regardless of wavelength
- **C.** Fiber eliminates the need for link-budget checks
- **D.** Fiber supplies DC power to remote endpoints

**Answer: A**

Fiber is useful where electromagnetic interference or electrical isolation is a concern. It still requires compatible optics, cabling, and acceptable optical loss.

**Option explanations**

- **A:** Its optical signaling avoids electromagnetic induction into the data signal.
- **B:** Optic wavelength and fiber compatibility still matter.
- **C:** Optical loss and receiver limits still constrain a link.
- **D:** Optical fiber does not itself deliver PoE.

**Further reading**

- [Cisco 10GBASE SFP+ Modules Data Sheet](https://www.cisco.com/c/en/us/products/collateral/interfaces-modules/transceiver-modules/data_sheet_c78-455693.html) — Cisco SFP-10G-SR module; Cisco SFP-10G-LR module; Cisco SFP-10G-T-X module

---

## CCNA2-004 · Network Fundamentals

Objectives: 1.4 · single · Applied

A replacement copper cable restores a full-duplex Ethernet link. Over the next hour, CRC errors stop increasing while old error totals remain visible. Which conclusion is justified?

| Time | CRC errors |
| --- | --- |
| 14:00, after replacement | 248 |
| 15:00 | 248 |

- **A.** The replacement failed because cumulative errors remain nonzero
- **B.** The subnet mask repaired the frame checksum
- **C.** The observed error rate fell to zero during the measurement interval
- **D.** Every application transaction must now succeed

**Answer: C**

Compare counter deltas over a known interval. The evidence supports improved link integrity during that interval, not a guarantee about every application.

**Option explanations**

- **A:** Historical counters do not have to reset when a fault is repaired.
- **B:** IP addressing does not repair physical frame corruption.
- **C:** The unchanged cumulative counter means no additional counted CRC errors appeared.
- **D:** A clean link does not prove higher-layer service success.

**Further reading**

- [Configure and Verify Ethernet 10/100/1000Mb Half/Full Duplex Auto-Negotiation](https://www.cisco.com/c/en/us/support/docs/lan-switching/ethernet/10561-3.html) — Background Information; Auto-Negotiation on Catalyst Switches that Run Cisco IOS Software

---

## CCNA2-005 · Network Fundamentals

Objectives: 1.5 · single · Foundation

A sensor application sends independent UDP measurements. Packet 71 is lost, but packet 72 arrives. No application retransmission or ordering mechanism exists. What can the receiver expect from UDP itself?

- **A.** UDP requests packet 71 before exposing packet 72
- **B.** Packet 72 may be delivered without recovering packet 71
- **C.** UDP resets the connection after the missing packet
- **D.** UDP reconstructs packet 71 from its checksum

**Answer: B**

UDP can deliver a later datagram even when an earlier one was lost. If the application needs recovery or sequencing, it must use additional mechanisms.

**Option explanations**

- **A:** UDP has no such sequence-based recovery service.
- **B:** Independent datagrams do not wait for missing earlier datagrams.
- **C:** UDP does not maintain a TCP-style connection to reset.
- **D:** A checksum detects some corruption; it cannot reconstruct lost payload.

**Further reading**

- [RFC 768: User Datagram Protocol](https://www.rfc-editor.org/rfc/rfc768) — Introduction; Fields

---

## CCNA2-006 · Network Fundamentals

Objectives: 1.6 · single · Applied

A workstation is 10.6.4.126/26. Its gateway must be an unused ordinary host address in the same subnet. Which candidate is valid?

- **A.** 10.6.4.64
- **B.** 10.6.4.127
- **C.** 10.6.4.129
- **D.** 10.6.4.65

**Answer: D**

The /26 block is .64 through .127, with usable addresses .65 through .126. A gateway on another subnet is not an on-link next hop under these assumptions.

**Option explanations**

- **A:** This is the subnet identifier.
- **B:** This is the directed broadcast address.
- **C:** This belongs to the next /26 subnet.
- **D:** This is a usable address in 10.6.4.64/26.

**Further reading**

- [Configure IP Addresses and Unique Subnets for New Users](https://www.cisco.com/c/en/us/support/docs/ip/routing-information-protocol-rip/13788-3.html) — Network Masks; Understand Subnetting; VLSM Example

---

## CCNA2-007 · Network Fundamentals

Objectives: 1.7 · multiple · Applied

Two companies independently use 10.20.0.0/16 and plan to interconnect. Which TWO conclusions follow? Select two.

- **A.** Their address plans may overlap because private addresses are reusable
- **B.** Private addressing automatically encrypts their traffic
- **C.** They must examine overlapping subnets before ordinary routed integration
- **D.** RFC 1918 guarantees unique addresses between companies
- **E.** The 10.20.0.0/16 prefix is globally assigned to only one company

**Answer: A, C**

Both organizations may legitimately use this range independently. Integration needs an address plan or another explicit overlap-handling design.

**Option explanations**

- **A:** Private assignments are not globally unique.
- **B:** Address classification does not supply cryptography.
- **C:** Identical prefixes can create ambiguous destination reachability.
- **D:** Uniqueness is managed within the relevant administrative scope.
- **E:** It lies within reusable 10.0.0.0/8 private space.

**Further reading**

- [RFC 1918: Address Allocation for Private Internets](https://www.rfc-editor.org/rfc/rfc1918#section-3) — 3. Private Address Space

---

## CCNA2-008 · Network Fundamentals

Objectives: 1.8 · single · Applied

Which fully expanded address equals 2001:db8:42::7:9?

- **A.** 2001:0db8:0042:0000:0000:0000:0007:0009
- **B.** 2001:0db8:0042:0000:0000:0007:0000:0009
- **C.** 2001:0db8:0042:0000:0000:0000:0070:0090
- **D.** 2001:0db8:0042:0000:0000:0007:0009:0000

**Answer: A**

IPv6 has eight 16-bit hextets. Preserve the position and value of every explicitly written hextet when expanding the single double colon.

**Option explanations**

- **A:** The compression replaces three zero hextets.
- **B:** This moves the 7 into a different hextet.
- **C:** Leading zeros may be omitted; trailing zeros may not.
- **D:** This adds a zero after the final hextet.

**Further reading**

- [RFC 4291: IP Version 6 Addressing Architecture](https://www.rfc-editor.org/rfc/rfc4291#section-2.3) — 2.3. Text Representation of Address Prefixes; 2.4. Address Type Identification; 2.5.6. Link-Local IPv6 Unicast Addresses; 2.7. Multicast Addresses

---

## CCNA2-009 · Network Fundamentals

Objectives: 1.9.a · single · Applied

A router receives a packet whose destination is fe80::23 on one LAN. A device on another LAN happens to use the same link-local address. What should ordinary IPv6 routing do?

- **A.** Forward it to the lowest-metric matching remote LAN
- **B.** Translate fe80 into a global prefix automatically
- **C.** Keep link-local traffic confined to its original link
- **D.** Broadcast it across every attached subnet

**Answer: C**

A link-local address is meaningful within one link. Reusing its numeric value on another link does not make those links a single addressing scope.

**Option explanations**

- **A:** Link-local scope prevents forwarding it to another link.
- **B:** IPv6 routing does not automatically translate that scope.
- **C:** A router must not forward link-local destinations onto another link.
- **D:** IPv6 has no broadcast delivery mode.

**Further reading**

- [RFC 4291: IP Version 6 Addressing Architecture](https://www.rfc-editor.org/rfc/rfc4291#section-2.3) — 2.3. Text Representation of Address Prefixes; 2.4. Address Type Identification; 2.5.6. Link-Local IPv6 Unicast Addresses; 2.7. Multicast Addresses

---

## CCNA2-010 · Network Fundamentals

Objectives: 1.10, 1.6 · single · Applied

The Windows values shown were manually entered. The LAN uses 192.168.44.0/25, and its router is 192.168.44.1. Which field is inconsistent with that LAN?

```text
IPv4 Address . . . . : 192.168.44.170
Subnet Mask  . . . . : 255.255.255.128
Default Gateway . . : 192.168.44.1
DNS Servers . . . . : 192.168.44.10
```

- **A.** DNS server
- **B.** IPv4 address
- **C.** Subnet mask
- **D.** Default gateway

**Answer: B**

With /25, .170 belongs to 192.168.44.128/25. The workstation address must be corrected to an unused host in the intended subnet.

**Option explanations**

- **A:** The displayed resolver is a usable local address.
- **B:** 192.168.44.170 is outside the required .0–.127 subnet.
- **C:** 255.255.255.128 is the required /25 mask.
- **D:** 192.168.44.1 is the stated router on the intended LAN.

**Further reading**

- [ipconfig](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/ipconfig) — Syntax; Parameters (/all)
- [Configure IP Addresses and Unique Subnets for New Users](https://www.cisco.com/c/en/us/support/docs/ip/routing-information-protocol-rip/13788-3.html) — Network Masks; Understand Subnetting; VLSM Example

---

## CCNA2-011 · Network Fundamentals

Objectives: 1.11.b, 1.11.c · multiple · Applied

Two nearby APs advertise the same SSID on the same channel. Which TWO statements are correct? Select two.

- **A.** Matching SSIDs make the APs one physical radio
- **B.** Changing the SSID alone removes RF contention
- **C.** The SSID identifies the advertised wireless network name
- **D.** Their transmissions can contend for airtime on that channel
- **E.** The SSID supplies a unique IPv4 address to each client

**Answer: C, D**

Network naming and RF resource sharing are different properties. The same or different SSIDs do not, by themselves, prevent neighboring radios from sharing a channel.

**Option explanations**

- **A:** Each AP retains its own radio and BSSID.
- **B:** SSID naming does not move RF transmissions to another channel.
- **C:** Multiple APs can advertise the same network name.
- **D:** RF sharing is determined by channel use and reception conditions.
- **E:** IP address assignment is a separate function.

**Further reading**

- [Channel Planning Best Practices](https://documentation.meraki.com/Wireless/Design_and_Configure/Architecture_and_Best_Practices/Channel_Planning_Best_Practices) — 2.4 GHz
- [Wireless Fundamentals: Encryption and Authentication](https://documentation.meraki.com/Wireless/Design_and_Configure/Architecture_and_Best_Practices/Wireless_Fundamentals:_Encryption_and_Authentication) — WPA2 – Personal; Hidden SSID

---

## CCNA2-012 · Network Fundamentals

Objectives: 1.12 · multiple · Applied

Two Linux process containers run in the same Linux VM. Which TWO resources do they necessarily share at the stated virtualization level? Select two.

- **A.** The guest Linux kernel
- **B.** One mandatory application process
- **C.** One mandatory IP address
- **D.** One mandatory root filesystem
- **E.** The physical host underlying their VM

**Answer: A, E**

Container isolation does not create independent guest kernels. This arrangement also has a common physical-host dependency despite separate container environments.

**Option explanations**

- **A:** Ordinary process containers use the kernel of their host OS.
- **B:** Containers can run different application processes.
- **C:** Container networking can assign distinct addresses.
- **D:** Containers can have distinct filesystem views.
- **E:** Both containers execute within the same VM on that host.

**Further reading**

- [What is a container?](https://docs.docker.com/get-started/docker-concepts/the-basics/what-is-a-container/#containers-versus-virtual-machines-vms) — Containers versus virtual machines (VMs)

---

## CCNA2-013 · Network Fundamentals

Objectives: 1.13.a, 1.13.d · single · Applied

A dynamic MAC entry maps host H to Gi1/0/2 in VLAN 30. H is moved to Gi1/0/8 and immediately sends a valid frame there. Both ports are forwarding access ports in VLAN 30 and no security restrictions apply. What happens to H’s entry?

- **A.** It remains on Gi1/0/2 until the complete aging interval expires
- **B.** It is permanently installed on both ports
- **C.** It changes to Gi1/0/8
- **D.** The destination MAC is assigned to Gi1/0/8 instead

**Answer: C**

Dynamic source learning accommodates a host move. Waiting for aging is unnecessary when a fresh frame establishes the new ingress port.

**Option explanations**

- **A:** New source traffic can update a dynamic entry before aging.
- **B:** Ordinary dynamic learning updates the source location.
- **C:** The newly observed source location replaces the old dynamic mapping.
- **D:** Learning tracks the received source, not the destination.

**Further reading**

- [Configuring MAC Address Tables](https://www.cisco.com/c/en/us/td/docs/switches/datacenter/nexus5500/sw/layer2/7x/b_5500_Layer2_Config_7x/config_mac_address_tables.pdf) — Information About MAC Addresses (page 1); Configuring the Aging Time for the MAC Table (page 2)

---

## CCNA2-014 · Network Fundamentals

Objectives: 1.1.h · single · Applied

A standards-compliant PoE switch has ample total budget, but a particular port can allocate at most 15 W. Its new powered device requires a 25 W allocation to operate fully. What prevents full operation?

- **A.** The per-port power limit
- **B.** An insufficient number of MAC addresses
- **C.** The use of a private IPv4 address
- **D.** The access port being in VLAN 1

**Answer: A**

Both total power budget and the individual port capability must satisfy the device requirement. This port cannot supply the required allocation.

**Option explanations**

- **A:** A large system budget does not raise an individual port limit.
- **B:** MAC capacity is unrelated to this electrical limit.
- **C:** PoE admission does not depend on public addressing.
- **D:** A VLAN identifier does not increase PoE capability.

**Further reading**

- [Interface and Hardware Components Configuration Guide, Cisco IOS XE 17.14.x (Catalyst 9200 Switches): Configuring Power over Ethernet](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst9200/software/release/17-14/configuration_guide/int_hw/b_1714_int_and_hw_9200_cg/configuring_poe.html) — Powered-Device Detection and Initial Power Allocation

---

## CCNA2-015 · Network Fundamentals

Objectives: 1.6 · single · Applied

A new LAN needs 120 endpoint addresses plus one router interface. Excluding network and broadcast addresses, which is the longest prefix that supplies enough addresses?

- **A.** /24
- **B.** /26
- **C.** /27
- **D.** /25

**Answer: D**

Seven host bits provide 128 total addresses, or 126 ordinary usable addresses. Six host bits would provide only 62.

**Option explanations**

- **A:** It fits, but /25 provides sufficient addresses with a longer prefix.
- **B:** It supplies only 62 usable addresses.
- **C:** It supplies only 30 usable addresses.
- **D:** It supplies 126 usable addresses for the required 121 interfaces.

**Further reading**

- [Configure IP Addresses and Unique Subnets for New Users](https://www.cisco.com/c/en/us/support/docs/ip/routing-information-protocol-rip/13788-3.html) — Network Masks; Understand Subnetting; VLSM Example

---

## CCNA2-016 · Network Fundamentals

Objectives: 1.9.c · single · Foundation

A capture shows an IPv6 packet addressed to ff02::1. Which recipient group is intended?

- **A.** All IPv6 routers globally
- **B.** All IPv6 nodes on the local link
- **C.** Only the source node itself
- **D.** One nearest service instance

**Answer: B**

The ff prefix indicates multicast. The scope value 2 limits this all-nodes group to the local link.

**Option explanations**

- **A:** The group is all nodes, and its scope is link-local.
- **B:** ff02::1 is the link-local all-nodes multicast address.
- **C:** Loopback uses ::1.
- **D:** That describes anycast, not this multicast group.

**Further reading**

- [RFC 4291: IP Version 6 Addressing Architecture](https://www.rfc-editor.org/rfc/rfc4291#section-2.3) — 2.3. Text Representation of Address Prefixes; 2.4. Address Type Identification; 2.5.6. Link-Local IPv6 Unicast Addresses; 2.7. Multicast Addresses

---

## CCNA2-017 · Network Fundamentals

Objectives: 1.2.a, 1.2.b · single · Applied

A campus grows from one distribution block to several. The proposed core should interconnect these blocks while their distribution switches retain policy aggregation. What architectural change is described?

- **A.** Replacing every access switch with a server
- **B.** Collapsing distribution and access into one hub
- **C.** Moving from a collapsed core to a three-tier campus
- **D.** Converting the campus into a single SOHO wireless router

**Answer: C**

A dedicated core interconnects distribution blocks in a three-tier design. Distribution continues aggregating access connectivity and applying relevant policy.

**Option explanations**

- **A:** Servers do not supply the described campus tier.
- **B:** The proposal adds a separate interconnection tier.
- **C:** Access, distribution, and core become distinct roles.
- **D:** That does not match multiple distribution blocks.

**Further reading**

- [Campus LAN and Wireless LAN Solution Design Guide](https://www.cisco.com/c/en/us/td/docs/solutions/CVD/Campus/cisco-campus-lan-wlan-design-guide.html) — Hierarchical design model; Three-tier design; Core layer

---

## CCNA2-018 · Network Fundamentals

Objectives: 1.13.b, 1.13.d · single · Applied

A frame enters Gi1/0/1 in VLAN 10. The destination is dynamically mapped to Gi1/0/1 in VLAN 10. There are no special forwarding features. What does the switch do with this frame?

- **A.** Filter it instead of sending it back through the ingress port
- **B.** Flood it to every other VLAN 10 port
- **C.** Transmit it back through Gi1/0/1
- **D.** Route it into VLAN 20

**Answer: A**

When ingress and learned destination ports are the same, normal Layer 2 forwarding filters the frame. Sending it back would not help reach another segment.

**Option explanations**

- **A:** The destination is already reachable on the segment where the frame arrived.
- **B:** The destination is known; unknown-unicast flooding does not apply.
- **C:** Ordinary bridge forwarding does not reflect it back onto ingress.
- **D:** A MAC lookup alone does not initiate inter-VLAN routing.

**Further reading**

- [Configuring MAC Address Tables](https://www.cisco.com/c/en/us/td/docs/switches/datacenter/nexus5500/sw/layer2/7x/b_5500_Layer2_Config_7x/config_mac_address_tables.pdf) — Information About MAC Addresses (page 1); Configuring the Aging Time for the MAC Table (page 2)

---

## CCNA2-019 · Network Fundamentals

Objectives: 1.3.b · single · Applied

Four legacy stations attach to one Ethernet hub and operate half duplex. Which statement describes their medium?

- **A.** Each station has an independent collision domain
- **B.** All stations can simultaneously send at full rate without contention
- **C.** The hub uses a destination MAC table to isolate transmissions
- **D.** The stations share one collision domain

**Answer: D**

Half-duplex hub Ethernet uses shared-medium access. A switched full-duplex point-to-point link has different collision behavior.

**Option explanations**

- **A:** The hub repeats signals into a shared collision domain.
- **B:** Simultaneous transmissions can collide.
- **C:** A hub does not perform learned frame switching.
- **D:** The repeater exposes the stations to the same shared medium.

**Further reading**

- [Configure and Verify Ethernet 10/100/1000Mb Half/Full Duplex Auto-Negotiation](https://www.cisco.com/c/en/us/support/docs/lan-switching/ethernet/10561-3.html) — Background Information; Auto-Negotiation on Catalyst Switches that Run Cisco IOS Software

---

## CCNA2-020 · Network Fundamentals

Objectives: 1.1.c, 1.1.d, 1.1.e, 1.1.g · matching · Applied

Match each operational observation to its most specific component role. Use each role once.

1. An operator pushes WLAN settings centrally to 40 managed APs.
2. A device enforces different policies for identified applications sharing TCP port 443.
3. A ceiling device exchanges 802.11 frames with nearby laptops.
4. A host processes inventory queries and returns records to clients.

- **A.** Wireless controller
- **B.** Application server
- **C.** Next-generation firewall
- **D.** Access point

**Answer: 1 → A; 2 → C; 3 → D; 4 → B**

Match the observed function rather than the physical enclosure. Central management, radio access, application service, and traffic inspection are separate roles.

**Option explanations**

- **A:** Coordinates configuration and policy for managed APs.
- **B:** Answers client requests for an application service.
- **C:** Combines stateful filtering with application-aware inspection.
- **D:** Provides the radio link between wireless clients and the LAN.

**Further reading**

- [Campus LAN and Wireless LAN Solution Design Guide](https://www.cisco.com/c/en/us/td/docs/solutions/CVD/Campus/cisco-campus-lan-wlan-design-guide.html) — Centralized (local-mode) design model
- [NGFW vs traditional firewall: what’s different [Explained]](https://www.cisco.com/site/us/en/learn/topics/security/what-is-a-next-generation-firewall.html) — Next-generation firewall overview
- [RFC 9110: HTTP Semantics](https://www.rfc-editor.org/rfc/rfc9110.html#section-3.3) — 3.3. Connections, Clients, and Servers

---

## CCNA2-021 · Network Access

Objectives: 2.1.a · single · Applied

After a desk move, a PC receives an address from the engineering subnet instead of the finance subnet. DHCP scopes and the upstream trunk are correct. What configuration error is established by the access-port output?

```text
Design: Finance VLAN 24; Engineering VLAN 44
Name: Gi1/0/16
Administrative Mode: static access
Operational Mode: static access
Access Mode VLAN: 44 (Engineering)
Voice VLAN: none
```

- **A.** The PC must add VLAN 24 tags itself.
- **B.** The port has become an 802.1Q trunk.
- **C.** The voice VLAN overrides all PC data.
- **D.** The port still assigns untagged traffic to VLAN 44.

**Answer: D**

An access switch classifies the PC frame using the port membership. Reassign this port to the existing finance VLAN 24.

**Option explanations**

- **A:** The design uses a normal untagged access connection.
- **B:** Its operational mode is static access.
- **C:** No voice VLAN is configured, and voice assignment would not override ordinary untagged PC data.
- **D:** The operational access VLAN is engineering VLAN 44.

**Further reading**

- [VLAN Configuration Guide, Cisco IOS XE 17.15.x — Configuring VLANs](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst9300/software/release/17-15/configuration_guide/vlan/b_1715_vlan_9300_cg/configuring_vlans.html) — Supported VLANs; Deleting a VLAN; VLAN Port Membership Modes

---

## CCNA2-022 · Network Access

Objectives: 2.1.b · single · Foundation

An unused Catalyst access port has its explicit access-VLAN command removed with no switchport access vlan. No interface template applies. Where will an ordinary untagged frame be classified when the port is enabled?

- **A.** No VLAN until a DHCP lease is obtained
- **B.** The lowest numbered user-created VLAN
- **C.** The trunk native VLAN of the uplink
- **D.** VLAN 1

**Answer: D**

The default access VLAN is VLAN 1. DHCP does not determine a switch port’s VLAN membership.

**Option explanations**

- **A:** Layer 2 classification precedes DHCP addressing.
- **B:** The switch does not choose an arbitrary existing user VLAN.
- **C:** An uplink native VLAN does not set local access-port membership.
- **D:** Removing the explicit assignment restores the default access VLAN.

**Further reading**

- [VLAN Configuration Guide, Cisco IOS XE 17.15.x — Configuring VLANs](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst9300/software/release/17-15/configuration_guide/vlan/b_1715_vlan_9300_cg/configuring_vlans.html) — Supported VLANs; Deleting a VLAN; VLAN Port Membership Modes

---

## CCNA2-023 · Network Access

Objectives: 2.1.c · single · Applied

Two operational SVIs on a Layer 3 Catalyst switch are the default gateways for their respective subnets. Hosts reach their own gateways but cannot reach the other subnet. No ACLs apply. Which missing global command explains this configuration?

```text
no ip routing
interface Vlan24
 ip address 10.24.0.1 255.255.255.0
interface Vlan44
 ip address 10.44.0.1 255.255.255.0
```

- **A.** switchport mode trunk
- **B.** ip default-gateway 10.24.0.1
- **C.** spanning-tree mode rapid-pvst
- **D.** ip routing

**Answer: D**

Having IP addresses on SVIs does not by itself enable transit IPv4 routing. Enable routing on the multilayer switch.

**Option explanations**

- **A:** This is an interface command and does not enable Layer 3 forwarding.
- **B:** A management default gateway does not enable transit routing between SVIs.
- **C:** STP selects Layer 2 paths; it does not route packets.
- **D:** This enables IPv4 forwarding between the operational SVIs.

**Further reading**

- [Configure Inter-VLAN Routing with Catalyst Switches](https://www.cisco.com/c/en/us/support/docs/lan-switching/inter-vlan-routing/41260-189.html) — Configure; Troubleshoot

---

## CCNA2-024 · Network Access

Objectives: 2.2.a · single · Applied

Two Cisco switch interfaces are configured as dynamic auto. Both use the same VTP domain, and no other link or forced trunk setting exists. Why does the new link remain an access link?

- **A.** DTP requires an IP address on each physical interface.
- **B.** Neither side actively requests trunk negotiation.
- **C.** The native VLAN must be deleted first.
- **D.** Dynamic auto enables LACP rather than DTP.

**Answer: B**

DTP dynamic auto on both ends does not initiate a trunk. Configure the intended trunk explicitly or provide a compatible initiating DTP mode.

**Option explanations**

- **A:** DTP is a Layer 2 negotiation protocol.
- **B:** Auto responds to an initiating peer but auto/auto does not form a trunk.
- **C:** Trunk formation does not require deleting a VLAN.
- **D:** LACP aggregates links; dynamic auto concerns DTP trunk negotiation.

**Further reading**

- [VLAN Configuration Guide, Cisco IOS XE 17.15.x — Configuring VLAN Trunks](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst9300/software/release/17-15/configuration_guide/vlan/b_1715_vlan_9300_cg/configuring_vlan_trunks.html) — Allowed VLANs on a Trunk; Configuring the Native VLAN for Untagged Traffic

---

## CCNA2-025 · Network Access

Objectives: 2.2.b, 2.2.c · single · Challenge

During a maintenance window, trunk A uses native VLAN 17 and trunk B uses native VLAN 27. Native tagging is disabled. Assume an untagged user frame reaches B before any STP inconsistency blocks the link. Into which VLAN does B classify that frame?

- **A.** The VLAN matching the source IP subnet
- **B.** VLAN 27
- **C.** VLAN 17
- **D.** Both VLANs 17 and 27

**Answer: B**

Native VLAN mismatch can associate the same untagged frame with different VLANs at opposite ends. Both trunk endpoints should agree on the native VLAN.

**Option explanations**

- **A:** The switch does not infer this Layer 2 tag from the source IP.
- **B:** An untagged ingress frame takes the receiving trunk’s native VLAN.
- **C:** No 17 tag is present for B to read.
- **D:** Native classification assigns one VLAN, not a copy to each.

**Further reading**

- [VLAN Configuration Guide, Cisco IOS XE 17.15.x — Configuring VLAN Trunks](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst9300/software/release/17-15/configuration_guide/vlan/b_1715_vlan_9300_cg/configuring_vlan_trunks.html) — Allowed VLANs on a Trunk; Configuring the Native VLAN for Untagged Traffic

---

## CCNA2-026 · Network Access

Objectives: 2.3 · multiple · Applied

An engineer needs the local cable termination and the remote switch port, not an IP route. Which TWO fields provide this mapping in the neighbor record? Select TWO.

```text
Device ID: DIST-7
Local interface: Gi1/0/46
Holdtime: 121 sec
Capability: S I
Port ID: Gi1/0/2
```

- **A.** Holdtime 121 seconds
- **B.** Remote port ID Gi1/0/2
- **C.** Local interface Gi1/0/46
- **D.** Capability S I

**Answer: B, C**

Pair the local interface with the remote port ID. A device identifier names the peer, while the two interface fields locate the cable ends.

**Option explanations**

- **A:** Holdtime is a cache lifetime, not a cable endpoint.
- **B:** The peer advertises its own connected interface as the port ID.
- **C:** This identifies the interface on the switch producing the output.
- **D:** Capabilities describe device functions, not a physical port.

**Further reading**

- [Network Management Configuration Guide, Cisco IOS XE 17.15.x — Configuring Cisco Discovery Protocol](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst9300/software/release/17-15/configuration_guide/nmgmt/b_1715_nmgmt_9300_cg/configuring_the_cisco_discovery_protocol.html) — Configuring Cisco Discovery Protocol; Monitoring and Maintaining Cisco Discovery Protocol

---

## CCNA2-027 · Network Access

Objectives: 2.4 · single · Applied

A newly configured port-channel is shown below. According to the included flag legend, what conclusion is supported?

```text
Flags: S - Layer2  R - Layer3  U - in use
       P - bundled in port-channel  s - suspended
Group  Port-channel  Protocol  Ports
6      Po6(SU)       LACP      Gi1/0/5(P) Gi1/0/6(P)
```

- **A.** Po6 is a Layer 2 channel in use, with both interfaces bundled.
- **B.** Po6 is routed because its protocol is LACP.
- **C.** Both physical ports are suspended.
- **D.** Only Gi1/0/5 is forwarding because STP blocks Gi1/0/6.

**Answer: A**

Read the logical channel flags and member flags separately. These flags establish bundle membership, but do not prove every VLAN or application is working.

**Option explanations**

- **A:** S means Layer 2, U means in use, and P identifies members in the channel.
- **B:** LACP is usable with Layer 2 and Layer 3 channels.
- **C:** The displayed P flag means bundled; s would indicate suspended.
- **D:** STP treats the functioning bundle as one logical link, not independent parallel links.

**Further reading**

- [Layer 2 Configuration Guide, Cisco IOS XE 17.15.x — Configuring EtherChannels](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst9300/software/release/17-15/configuration_guide/lyr2/b_1715_lyr2_9300_cg/configuring_etherchannels.html) — LACP Modes; EtherChannel Configuration Guidelines; Load Balancing; Layer 3 EtherChannels; Hot-Standby Ports

---

## CCNA2-028 · Network Access

Objectives: 2.4 · single · Applied

A server sends one long TCP flow across a healthy four-member 1-Gb/s EtherChannel. The switch uses a stable per-flow hash, all members are otherwise idle, and each member is 1 Gb/s. What bandwidth expectation is justified?

- **A.** The flow uses one member and cannot exceed that member’s line rate.
- **B.** LACP increases each physical member’s negotiated speed to 4 Gb/s.
- **C.** All four links carry identical copies for reliability.
- **D.** The flow automatically receives 4 Gb/s.

**Answer: A**

EtherChannel increases aggregate capacity and provides member redundancy. Its hashing behavior limits this single flow to one physical path.

**Option explanations**

- **A:** A stable flow hash selects a member rather than striping each packet across all links.
- **B:** Negotiated physical speed remains 1 Gb/s per member.
- **C:** Normal EtherChannel forwarding distributes traffic instead of replicating it.
- **D:** Aggregate capacity is available across distributed flows, not guaranteed to one flow.

**Further reading**

- [Layer 2 Configuration Guide, Cisco IOS XE 17.15.x — Configuring EtherChannels](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst9300/software/release/17-15/configuration_guide/lyr2/b_1715_lyr2_9300_cg/configuring_etherchannels.html) — LACP Modes; EtherChannel Configuration Guidelines; Load Balancing; Layer 3 EtherChannels; Hot-Standby Ports

---

## CCNA2-029 · Network Access

Objectives: 2.5.a, 2.5.b · matching · Applied

Match each observed Rapid PVST+ situation to its port role. These are separate examples for one VLAN; use every role once.

1. The sole best upstream path selected by a nonroot switch
2. The winning port representing a switch on an attached segment
3. A spare upstream path via a different neighboring bridge
4. A second port of the same switch on its shared Ethernet segment

- **A.** Root port
- **B.** Alternate port
- **C.** Backup port
- **D.** Designated port

**Answer: 1 → A; 2 → D; 3 → B; 4 → C**

Roles describe each port’s place in the topology. Alternate and backup both discard ordinary traffic, but protect different paths.

**Option explanations**

- **A:** This is a nonroot switch’s selected best path toward the root bridge.
- **B:** This offers another path toward the root through a different bridge.
- **C:** This backs up the same switch’s designated port on a shared segment.
- **D:** This is the selected forwarding port for its segment, advertising the best path there.

**Further reading**

- [Understand Rapid Spanning Tree Protocol (802.1w)](https://www.cisco.com/c/en/us/support/docs/lan-switching/spanning-tree-protocol/24062-146.html) — New Port States and Port Roles — Port States; Alternate and Backup Port Roles

---

## CCNA2-030 · Network Access

Objectives: 2.5.a · single · Challenge

SW-A and SW-B advertise the same root ID and the same root-path cost to SW-C. SW-C adds the same local port cost for either path. SW-A has bridge ID 24586/0010.0000.000a and SW-B has 28682/0000.0000.000b. Which upstream neighbor wins SW-C’s next tie-break?

- **A.** SW-A, because its sender bridge ID is lower.
- **B.** SW-B, because its MAC address is lower.
- **C.** Whichever advertises the highest port number.
- **D.** Whichever link becomes active last.

**Answer: A**

After root and total path cost tie, compare sender bridge IDs. SW-A’s smaller priority component wins before MAC addresses are considered.

**Option explanations**

- **A:** The priority portion is compared before the MAC portion of the sender bridge ID.
- **B:** Its larger priority makes its complete bridge ID worse despite the lower MAC.
- **C:** Port ID is considered only after earlier comparisons tie, and lower is better.
- **D:** Arrival order is not the spanning-tree tie-break.

**Further reading**

- [Layer 2 Configuration Guide, Cisco IOS XE 17.15.x — Configuring Spanning Tree Protocol](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst9300/software/release/17-15/configuration_guide/lyr2/b_1715_lyr2_9300_cg/configuring_spanning_tree_protocol.html) — Spanning-Tree Topology and Bridge Protocol Data Units; Bridge ID, Device Priority, and Extended System ID; (Optional) Configuring a Secondary Root Device
- [Understand Rapid Spanning Tree Protocol (802.1w)](https://www.cisco.com/c/en/us/support/docs/lan-switching/spanning-tree-protocol/24062-146.html) — New Port States and Port Roles — Port States; Alternate and Backup Port Roles

---

## CCNA2-031 · Network Access

Objectives: 2.5.c · single · Applied

A workstation-facing port uses PortFast but neither BPDU guard nor BPDU filtering. Someone replaces the workstation with a bridge, and the port receives a BPDU. What should be expected?

- **A.** The port loses operational edge status and participates in normal spanning tree.
- **B.** The port must become error-disabled immediately.
- **C.** The BPDU is always discarded without inspection.
- **D.** The local switch automatically becomes the root.

**Answer: A**

PortFast accelerates an actual edge link. It is not a substitute for a feature that blocks unexpected bridges.

**Option explanations**

- **A:** PortFast alone does not suppress or reject BPDUs.
- **B:** That shutdown behavior requires BPDU guard or another error condition.
- **C:** That describes explicit BPDU filtering, which is absent.
- **D:** Root election still compares the advertised bridge information.

**Further reading**

- [Layer 2 Configuration Guide, Cisco IOS XE 17.15.x — Configuring Optional Spanning-Tree Features](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst9300/software/release/17-15/configuration_guide/lyr2/b_1715_lyr2_9300_cg/configuring_optional_spanning_tree_features.html) — PortFast; Bridge Protocol Data Unit Guard; Bridge Protocol Data Unit Filtering; Root Guard; Loop Guard
- [Understand Rapid Spanning Tree Protocol (802.1w)](https://www.cisco.com/c/en/us/support/docs/lan-switching/spanning-tree-protocol/24062-146.html) — New Port States and Port Roles — Port States; Alternate and Backup Port Roles

---

## CCNA2-032 · Network Access

Objectives: 2.5.d · multiple · Applied

A downstream switch temporarily advertises a superior BPDU into a root-guard port. After the downstream configuration is corrected, only normal inferior BPDUs arrive. Which TWO statements describe the root-guard behavior? Select TWO.

- **A.** The downstream switch becomes root until an administrator shuts the port.
- **B.** Normal forwarding can recover automatically after superior BPDUs cease.
- **C.** Any BPDU permanently disables the physical interface.
- **D.** The affected port enters root-inconsistent while the superior information persists.

**Answer: B, D**

Root guard enforces where the root may reside. It blocks the affected spanning-tree instance and recovers when the offending information disappears.

**Option explanations**

- **A:** Root guard blocks the undesired root path instead.
- **B:** Root-inconsistent is not the same as an error-disabled shutdown.
- **C:** Root guard reacts to superior BPDUs and allows automatic recovery.
- **D:** Root guard prevents that port from becoming a path to a better root.

**Further reading**

- [Enhance STP with Root Guard](https://www.cisco.com/c/en/us/support/docs/lan-switching/spanning-tree-protocol/10588-74.html) — Feature Description

---

## CCNA2-033 · Network Access

Objectives: 2.6 · single · Applied

A branch needs employee frames to reach its local file server without traversing the WAN to a WLC. Central configuration is still desired. Which design directly supplies that data path?

- **A.** FlexConnect with local switching for the employee WLAN
- **B.** Sniffer mode with a packet analyzer
- **C.** Local-mode AP with central switching
- **D.** Monitor mode with central switching

**Answer: A**

Separate where policy is managed from where client data is forwarded. FlexConnect can retain controller management while switching the selected WLAN locally.

**Option explanations**

- **A:** The AP bridges this WLAN into the branch VLAN locally.
- **B:** Sniffer mode collects radio traffic rather than providing the employee WLAN.
- **C:** Client traffic follows the CAPWAP data path to the controller.
- **D:** Monitor mode is dedicated to observation, not ordinary client service.

**Further reading**

- [Cisco Wireless Controller Configuration Guide, Release 8.10 — FlexConnect](https://www.cisco.com/c/en/us/td/docs/wireless/controller/8-10/config-guide/b_cg810/flexconnect.html) — Configuring the Switch at a Remote Site; Configuring an Access Point for FlexConnect (GUI)
- [Cisco Wireless Controller Configuration Guide, Release 8.5 — Managing APs](https://www.cisco.com/c/en/us/td/docs/wireless/controller/8-5/config-guide/b_cg85/managing_aps.html) — AP Modes: client-serving and network management modes

---

## CCNA2-034 · Network Access

Objectives: 2.6 · single · Applied

An analyst needs actual 802.11 frames on one selected channel delivered to a packet analyzer. A spare compatible AP will stop serving clients for the investigation. Which AP mode fits?

- **A.** Bridge
- **B.** Sniffer
- **C.** FlexConnect
- **D.** Local

**Answer: B**

Sniffer mode turns the AP into a remote wireless capture point. Channel selection and analyzer configuration still need to match the investigation.

**Option explanations**

- **A:** Bridge mode provides wireless backhaul between network locations.
- **B:** It captures wireless frames and exports them for packet analysis.
- **C:** FlexConnect selects branch forwarding behavior rather than dedicated frame capture.
- **D:** This normally provides client service and is not the dedicated capture mode.

**Further reading**

- [Cisco Wireless Controller Configuration Guide, Release 8.5 — Managing APs](https://www.cisco.com/c/en/us/td/docs/wireless/controller/8-5/config-guide/b_cg85/managing_aps.html) — AP Modes: client-serving and network management modes

---

## CCNA2-035 · Network Access

Objectives: 2.7 · single · Applied

A local-mode lightweight AP uses central switching for all WLANs. Its management address is in VLAN 70 and its Ethernet traffic is untagged. Client VLANs terminate at the WLC. What must the AP’s switch port carry?

- **A.** A routed EtherChannel for each wireless client
- **B.** A trunk with every centrally switched client VLAN is mandatory.
- **C.** An access connection in VLAN 70 is sufficient for the stated traffic.
- **D.** Only an access connection in each client VLAN, using one cable per SSID

**Answer: C**

Central switching changes the AP uplink requirement. The switch provides AP management transport to the WLC, while the controller supplies client VLAN attachment.

**Option explanations**

- **A:** Wireless client membership does not require individual EtherChannels.
- **B:** Those client VLANs terminate at the WLC in this design.
- **C:** Client VLAN frames are inside the CAPWAP tunnel, not exposed as local VLAN tags.
- **D:** One management IP path can carry multiple tunneled WLANs.

**Further reading**

- [Cisco Wireless Controller Configuration Guide, Release 8.10 — AP Connectivity to Controller](https://www.cisco.com/c/en/us/td/docs/wireless/controller/8-10/config-guide/b_cg810/ap_connectivity_to_cisco_wlc.html) — CAPWAP
- [Cisco Wireless Controller Configuration Guide, Release 8.10 — Ports and Interfaces](https://www.cisco.com/c/en/us/td/docs/wireless/controller/8-10/config-guide/b_cg810/ports_and_interfaces.html) — Restrictions on Link Aggregation; Configuring Neighbor Devices to Support Link Aggregation

---

## CCNA2-036 · Network Access

Objectives: 2.7 · single · Applied

An AireOS controller centrally switches three WLANs into three different wired VLANs through one distribution-system connection. What kind of switch interface is required on that connection?

- **A.** An 802.1Q trunk permitting the required VLANs
- **B.** A SPAN destination with transmit traffic disabled
- **C.** An access port in one arbitrary client VLAN
- **D.** A console port carrying the three WLANs

**Answer: A**

The controller distribution interface must carry the VLANs where it releases centrally switched client traffic. Its VLAN configuration and the adjacent trunk must agree.

**Option explanations**

- **A:** A single trunk distinguishes multiple VLANs on the shared link.
- **B:** A monitor destination is not a normal bidirectional distribution uplink.
- **C:** An ordinary access port provides only one untagged data VLAN.
- **D:** The console is for management, not client Ethernet forwarding.

**Further reading**

- [Cisco Wireless Controller Configuration Guide, Release 8.10 — Ports and Interfaces](https://www.cisco.com/c/en/us/td/docs/wireless/controller/8-10/config-guide/b_cg810/ports_and_interfaces.html) — Restrictions on Link Aggregation; Configuring Neighbor Devices to Support Link Aggregation
- [VLAN Configuration Guide, Cisco IOS XE 17.15.x — Configuring VLAN Trunks](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst9300/software/release/17-15/configuration_guide/vlan/b_1715_vlan_9300_cg/configuring_vlan_trunks.html) — Allowed VLANs on a Trunk; Configuring the Native VLAN for Untagged Traffic

---

## CCNA2-037 · Network Access

Objectives: 2.8 · single · Applied

An operator can ping a switch and reach its SSH login prompt, but TACACS+ authentication times out after a firewall change. Which path needs investigation first?

- **A.** The terminal’s console cable
- **B.** The switch-to-NTP path only
- **C.** The switch-to-TACACS+ server path
- **D.** The workstation’s 802.1Q native VLAN

**Answer: C**

Management access transport and centralized authentication are separate dependencies. A reachable SSH service may still fail login when its AAA server is unreachable.

**Option explanations**

- **A:** This is a remote SSH session, not a console session.
- **B:** NTP is not the transport carrying this TACACS+ authentication request.
- **C:** The interactive SSH connection works; the device still needs a separate AAA exchange.
- **D:** The established SSH transport already proves basic IP reachability to the switch.

**Further reading**

- [Cisco Wireless Controller Configuration Guide, Release 8.10 — AAA Administration](https://www.cisco.com/c/en/us/td/docs/wireless/controller/8-10/config-guide/b_cg810/aaa_administration.html) — Configuring TACACS+ (GUI)
- [Cisco Wireless Controller Configuration Guide, Release 8.10 — Administration of Controller](https://www.cisco.com/c/en/us/td/docs/wireless/controller/8-10/config-guide/b_cg810/administration_of_cisco_wlc.html) — Logging on to the Controller CLI; Enabling Web and Secure Web Modes (GUI); Enabling Web and Secure Web Modes (CLI)

---

## CCNA2-038 · Network Access

Objectives: 2.9 · single · Applied

The applied AireOS settings below are for a centrally switched staff WLAN. The required employee subnet is VLAN 310, but authenticated clients receive guest addresses. DHCP scopes themselves are correct. Which GUI binding should be corrected?

| GUI field | Value |
| --- | --- |
| SSID | Staff |
| Status | Enabled |
| Interface/Interface Group | guest-vlan (VLAN 320) |
| Available interface | staff-vlan (VLAN 310) |
| QoS | Silver |

- **A.** Interface/Interface Group: change guest-vlan to staff-vlan
- **B.** Broadcast SSID: disable it
- **C.** Profile Name: change Staff-Profile to Employees
- **D.** QoS: change Silver to Platinum

**Answer: A**

Successful wireless authentication does not verify wired VLAN placement. Bind the WLAN to the interface representing VLAN 310.

**Option explanations**

- **A:** The WLAN interface binding places centrally switched clients in the selected wired VLAN.
- **B:** Hiding the SSID does not change its wired VLAN.
- **C:** The profile name is an administrative label, not the VLAN binding.
- **D:** QoS class does not select the client IP subnet.

**Further reading**

- [Cisco Wireless Controller Configuration Guide, Release 8.10 — WLANs](https://www.cisco.com/c/en/us/td/docs/wireless/controller/8-10/config-guide/b_cg810/wlans.html) — Prerequisites for WLANs; Enabling and Disabling WLANs (GUI); Editing WLAN SSID or Profile Name for WLANs (GUI)
- [Cisco Wireless Controller Configuration Guide, Release 8.10 — Ports and Interfaces](https://www.cisco.com/c/en/us/td/docs/wireless/controller/8-10/config-guide/b_cg810/ports_and_interfaces.html) — Restrictions on Link Aggregation; Configuring Neighbor Devices to Support Link Aggregation

---

## CCNA2-039 · Network Access

Objectives: 2.9 · single · Foundation

A WLAN administrator edits the AireOS Profile Name from Warehouse-Old to Warehouse-New, but leaves SSID = ScannerNet. Which name should an ordinary client use when selecting this WLAN?

- **A.** Warehouse-New
- **B.** ScannerNet
- **C.** Warehouse-Old
- **D.** The controller’s management hostname

**Answer: B**

A controller profile name and an SSID serve different purposes. The client-facing identity remains ScannerNet.

**Option explanations**

- **A:** The profile name identifies the controller configuration object.
- **B:** The SSID is the over-the-air network name used by clients.
- **C:** Renaming the profile does not preserve it as a separate client SSID.
- **D:** That hostname identifies the device, not this WLAN.

**Further reading**

- [Cisco Wireless Controller Configuration Guide, Release 8.10 — WLANs](https://www.cisco.com/c/en/us/td/docs/wireless/controller/8-10/config-guide/b_cg810/wlans.html) — Prerequisites for WLANs; Enabling and Disabling WLANs (GUI); Editing WLAN SSID or Profile Name for WLANs (GUI)

---

## CCNA2-040 · Network Access

Objectives: 2.9 · multiple · Applied

A voice-only AireOS WLAN must use the standard voice QoS profile and WPA2-Enterprise with 802.1X. A valid RADIUS server is already selected. The applied GUI currently uses Silver and PSK. Which TWO changes meet the requirement? Select TWO.

- **A.** Keep PSK and rename the WLAN Enterprise.
- **B.** Select the Platinum QoS profile.
- **C.** Select the Bronze QoS profile.
- **D.** Replace PSK key management with 802.1X.

**Answer: B, D**

QoS treatment and authentication must each match the design. Selecting Platinum changes the profile; selecting 802.1X changes the credential exchange.

**Option explanations**

- **A:** A label does not change shared-key authentication into 802.1X.
- **B:** Platinum is the AireOS voice profile.
- **C:** Bronze is the background profile, not voice.
- **D:** 802.1X uses the configured enterprise authentication service.

**Further reading**

- [Cisco Wireless Controller Configuration Guide, Release 8.10 — Wireless Quality of Service](https://www.cisco.com/c/en/us/td/docs/wireless/controller/8-10/config-guide/b_cg810/wireless_quality_of_service.html) — QoS Profiles; Configuring QoS Profiles (GUI); Assigning a QoS Profile to a WLAN (GUI)
- [Cisco Wireless Controller Configuration Guide, Release 8.10 — WLAN Security](https://www.cisco.com/c/en/us/td/docs/wireless/controller/8-10/config-guide/b_cg810/wlan_security.html) — Configuring WPA1+WPA2 (GUI); Configuring Peer-to-Peer Blocking (GUI)

---

## CCNA2-041 · IP Connectivity

Objectives: 3.1.a, 3.1.e, 3.1.f · single · Applied

A change ticket calls the displayed route a manually configured path with distance 34. Which correction should the reviewer make?

```text
O 10.44.8.0/24 [110/34] via 192.0.2.6, 00:03:12, GigabitEthernet0/1
```

- **A.** It is an OSPF route whose next hop has distance 34.
- **B.** It is a connected route with a 110-hop limit.
- **C.** It is a static route with administrative distance 34.
- **D.** It is an OSPF route with administrative distance 110 and cost 34.

**Answer: D**

The source code and bracket positions must be read together. Neither field describes TTL or the neighbor’s configuration.

**Option explanations**

- **A:** The metric describes this route, not the neighbor’s administrative distance.
- **B:** Connected routes use C; administrative distance is not a packet hop limit.
- **C:** A static route uses S, and 34 occupies the metric position.
- **D:** O identifies OSPF; the bracket fields are distance followed by metric.

**Further reading**

- [Understand Administrative Distance](https://www.cisco.com/c/en/us/support/docs/ip/border-gateway-protocol-bgp/15986-admin-distance.html) — RIB Route Comparison; Route Installation; Default AD Values

---

## CCNA2-042 · IP Connectivity

Objectives: 3.1.g, 3.2.a · single · Foundation

A router displays “Gateway of last resort is not set” but has an installed, usable route to 172.21.8.0/24. What happens to an otherwise valid packet for 172.21.8.40 under ordinary forwarding?

- **A.** It is dropped because every router needs a default.
- **B.** It uses the matching /24 route.
- **C.** It is sent to the packet’s source gateway.
- **D.** It is broadcast to every routed interface.

**Answer: B**

An absent gateway of last resort limits reachability to destinations without a matching route. It does not disable specific routes.

**Option explanations**

- **A:** A default is needed only when no more specific installed route matches.
- **B:** A specific matching route does not require a default route.
- **C:** The destination lookup does not select the sender’s configured gateway.
- **D:** Routers do not discover unicast paths by flooding routed interfaces.

**Further reading**

- [RFC 1812: Requirements for IP Version 4 Routers](https://www.rfc-editor.org/rfc/rfc1812.html) — 5.2.4 Determining the Next Hop Address

---

## CCNA2-043 · IP Connectivity

Objectives: 3.1.b, 3.1.c, 3.2.a · multiple · Challenge

The only installed routes are shown. Which two destinations use the route through 192.0.2.9? Select two.

```text
S 10.18.32.0/20 via 192.0.2.9
O 10.18.40.0/24 via 192.0.2.13
S* 0.0.0.0/0 via 192.0.2.1
```

- **A.** 10.18.33.10
- **B.** 10.18.47.250
- **C.** 10.18.48.1
- **D.** 10.18.40.10

**Answer: A, B**

The /20 spans 10.18.32.0–10.18.47.255. Remove destinations matched by the /24 before assigning traffic to that aggregate.

**Option explanations**

- **A:** Third octet 33 is inside 32–47 and does not match the /24.
- **B:** Third octet 47 is inside the /20, outside the more specific /24.
- **C:** Third octet 48 lies outside the /20 and uses the default.
- **D:** The installed /24 overrides the broader /20 for this destination.

**Further reading**

- [Configure Route Selection for Routers](https://www.cisco.com/c/en/us/support/docs/ip/enhanced-interior-gateway-routing-protocol-eigrp/8651-21.html) — Build the Routing Table; Make Forwarding Decisions
- [RFC 1812: Requirements for IP Version 4 Routers](https://www.rfc-editor.org/rfc/rfc1812.html) — 5.2.4 Determining the Next Hop Address

---

## CCNA2-044 · IP Connectivity

Objectives: 3.2.b · single · Applied

Two routers receive the same valid OSPF and static candidates for 10.66.0.0/16. On R1 the static distance is 200; on R2 it is 1. OSPF distance is 110 on both. What is expected?

- **A.** Neither installs a route because the distances disagree.
- **B.** Both install static because static always outranks OSPF.
- **C.** Both install OSPF because its distance is advertised to R2.
- **D.** R1 installs OSPF; R2 installs static.

**Answer: D**

Local distance overrides can produce different routing choices on adjacent routers. The route’s source alone does not determine preference once distance is changed.

**Option explanations**

- **A:** Routers do not require equal local administrative distances.
- **B:** An explicit static distance can make OSPF preferable.
- **C:** Administrative distance is a local preference, not an OSPF advertisement.
- **D:** Each router compares its own administrative distances for this prefix.

**Further reading**

- [Understand Administrative Distance](https://www.cisco.com/c/en/us/support/docs/ip/border-gateway-protocol-bgp/15986-admin-distance.html) — RIB Route Comparison; Route Installation; Default AD Values

---

## CCNA2-045 · IP Connectivity

Objectives: 3.1.a, 3.1.b, 3.1.d · matching · Applied

Match each constructed routing-table fragment to its operational meaning.

1. L 192.0.2.1/32 is directly connected, GigabitEthernet0/0
2. C 192.0.2.0/30 is directly connected, GigabitEthernet0/0
3. S 10.80.0.0/16 via 192.0.2.2
4. S* 0.0.0.0/0 via 198.51.100.2

- **A.** Forward through a remote next hop
- **B.** Local delivery to the router
- **C.** Use for otherwise unmatched destinations
- **D.** A directly attached subnet

**Answer: 1 → B; 2 → D; 3 → A; 4 → C**

Local and connected routes serve different purposes even when they name the same interface. A static network route and a default also cover different destination sets.

**Option explanations**

- **A:** An S entry with via names a statically selected next hop.
- **B:** An L host route identifies an address owned by this router.
- **C:** An installed default covers destinations lacking a more specific match.
- **D:** A C network route describes an operational connected network.

**Further reading**

- [Local Host Routes Installed in the Routing Table on Cisco IOS and Cisco IOS-XR](https://www.cisco.com/c/en/us/support/docs/ip/ip-routing/116264-technote-ios-00.html) — Cisco IOS Local Routes; Manually Configured Host Routes
- [Configure Route Selection for Routers](https://www.cisco.com/c/en/us/support/docs/ip/enhanced-interior-gateway-routing-protocol-eigrp/8651-21.html) — Build the Routing Table; Make Forwarding Decisions

---

## CCNA2-046 · IP Connectivity

Objectives: 3.3.b · single · Applied

A branch has a working 192.0.2.0/30 link: branch .1, hub .2. Only the branch lacks a route to hub LAN 10.15.20.0/24. Which command supplies it without adding a default?

- **A.** ip route 10.15.20.0 255.255.255.0 192.0.2.2
- **B.** ip route 192.0.2.0 255.255.255.252 10.15.20.1
- **C.** ip route 10.15.20.0 255.255.255.0 192.0.2.1
- **D.** ip route 0.0.0.0 0.0.0.0 192.0.2.2

**Answer: A**

The next hop must lead away from the branch toward the destination. The working connected transit route already exists.

**Option explanations**

- **A:** The destination is the hub LAN and the next hop is the hub’s transit address.
- **B:** This reverses the transit network and remote destination roles.
- **C:** The proposed next hop is the branch itself.
- **D:** This adds a default, broader than the requested LAN-only route.

**Further reading**

- [Configure a Next Hop IP Address for Static Routes](https://www.cisco.com/c/en/us/support/docs/dial-access/floating-static-route/118263-technote-nexthop-00.html) — Background Information; Floating Static Route Example

---

## CCNA2-047 · IP Connectivity

Objectives: 3.3.a, 3.3.b · single · Applied

R1 and R2 have only the shown installed routes. All links work. A packet for 203.0.113.7 arrives at R1. What defect does this reveal?

```text
R1: S* 0.0.0.0/0 via 192.0.2.2
R2: S* 0.0.0.0/0 via 192.0.2.1
Transit: R1=192.0.2.1/30, R2=192.0.2.2/30
```

- **A.** R1 will suppress its default after reading R2’s configuration.
- **B.** The two defaults create a forwarding loop for this destination.
- **C.** R2 will deliver the packet locally because its route is /0.
- **D.** The defaults automatically discover an Internet exit.

**Answer: B**

An installed route is not proof that the chain reaches a destination. TTL bounds IPv4 looping, but does not repair the two mutually pointing defaults.

**Option explanations**

- **A:** Static routes do not exchange configuration or perform loop prevention.
- **B:** Each router sends an unmatched destination back to the other.
- **C:** A default denotes a forwarding fallback, not ownership of every address.
- **D:** A static default does not discover upstream connectivity.

**Further reading**

- [RFC 1812: Requirements for IP Version 4 Routers](https://www.rfc-editor.org/rfc/rfc1812.html) — 5.2.4 Determining the Next Hop Address
- [Configure a Next Hop IP Address for Static Routes](https://www.cisco.com/c/en/us/support/docs/dial-access/floating-static-route/118263-technote-nexthop-00.html) — Background Information; Floating Static Route Example

---

## CCNA2-048 · IP Connectivity

Objectives: 3.3.c, 3.2.a · single · Applied

A management server at 10.32.5.9 must use a temporary backup next hop; all other addresses in 10.32.5.0/24 must keep the existing path. Both next hops are reachable. What is the narrowest change?

- **A.** Add a /32 static route for 10.32.5.9 through the backup.
- **B.** Add a /24 route with a higher distance through the backup.
- **C.** Replace the /24 route with the backup next hop.
- **D.** Add a lower-distance default through the backup.

**Answer: A**

A host route isolates the temporary exception. Its destination specificity, rather than a lower-distance default, controls this forwarding choice.

**Option explanations**

- **A:** A host route overrides the /24 only for that one destination.
- **B:** A floating /24 does not override the active /24 for one host.
- **C:** This moves every destination in the subnet.
- **D:** A default remains less specific than the installed /24.

**Further reading**

- [Local Host Routes Installed in the Routing Table on Cisco IOS and Cisco IOS-XR](https://www.cisco.com/c/en/us/support/docs/ip/ip-routing/116264-technote-ios-00.html) — Cisco IOS Local Routes; Manually Configured Host Routes
- [Configure Route Selection for Routers](https://www.cisco.com/c/en/us/support/docs/ip/enhanced-interior-gateway-routing-protocol-eigrp/8651-21.html) — Build the Routing Table; Make Forwarding Decisions

---

## CCNA2-049 · IP Connectivity

Objectives: 3.3.b · single · Applied

An IPv6 static route specifies only GigabitEthernet0/0, a multiaccess Ethernet link. The destination /64 is actually behind a neighboring router. Hosts are not on this Ethernet and no proxy Neighbor Discovery is provided. What correction avoids treating every remote host as on-link?

- **A.** Disable IPv6 unicast routing.
- **B.** Increase the static route’s administrative distance.
- **C.** Specify the actual neighbor next hop, with the exit interface when link-local.
- **D.** Replace the /64 with a /128 for the entire subnet.

**Answer: C**

An interface-only IPv6 static on Ethernet assumes destinations are directly attached. A fully specified route states both the link and the router to reach.

**Option explanations**

- **A:** That prevents the required transit forwarding rather than correcting it.
- **B:** Distance changes preference but does not fix next-hop resolution.
- **C:** This directs Neighbor Discovery toward the adjacent router instead of remote hosts.
- **D:** A /128 identifies one address and cannot represent an entire subnet.

**Further reading**

- [IPv6 Routing: Static Routing — Cisco IOS XE 17.x](https://www.cisco.com/c/en/us/td/docs/routers/ios/config/17-x/ip-routing/b-ip-routing/m_ip6-route-static-xe.html) — Recursive Static Routes; Fully Specified Static Routes; Floating Static Routes

---

## CCNA2-050 · IP Connectivity

Objectives: 3.3.d, 3.2.b · single · Applied

A valid OSPF route to 10.53.0.0/16 has distance 110. A proposed backup static for exactly that prefix has distance 100 and a reachable next hop. Which change makes it a backup to OSPF?

- **A.** Keep distance 100 and call the route “backup.”
- **B.** Change the static distance to 1.
- **C.** Change the static distance to 150.
- **D.** Change OSPF’s metric from 20 to 5.

**Answer: C**

A floating route requires a less preferred administrative distance than its primary competitor for the same prefix. It must still be valid when needed.

**Option explanations**

- **A:** A descriptive label does not alter route selection.
- **B:** This makes the static even more preferred.
- **C:** 150 is higher than 110, so OSPF remains preferred while available.
- **D:** An OSPF metric cannot override a different source’s lower distance.

**Further reading**

- [Understand Administrative Distance](https://www.cisco.com/c/en/us/support/docs/ip/border-gateway-protocol-bgp/15986-admin-distance.html) — RIB Route Comparison; Route Installation; Default AD Values

---

## CCNA2-051 · IP Connectivity

Objectives: 3.3.b, 3.1.d · single · Applied

An IPv6 route appears in running-config but not show ipv6 route. Its next hop is a global address with no resolving route; all connected routes are elsewhere. What must be repaired first?

- **A.** Provide a valid path that resolves the configured next hop.
- **B.** Set the OSPFv2 router ID to the next-hop address.
- **C.** Add an ARP entry for the IPv6 next hop.
- **D.** Raise its distance above every other route.

**Answer: A**

Configuration expresses intent; route installation additionally depends on resolution. The remote prefix cannot bootstrap its own unreachable next hop.

**Option explanations**

- **A:** A recursive static must resolve to a usable IPv6 output interface.
- **B:** OSPFv2 router IDs are unrelated to IPv6 static recursion.
- **C:** IPv6 uses Neighbor Discovery, and a neighbor entry alone cannot supply remote route recursion.
- **D:** A larger distance does not create next-hop reachability.

**Further reading**

- [IPv6 Routing: Static Routing — Cisco IOS XE 17.x](https://www.cisco.com/c/en/us/td/docs/routers/ios/config/17-x/ip-routing/b-ip-routing/m_ip6-route-static-xe.html) — Recursive Static Routes; Fully Specified Static Routes; Floating Static Routes

---

## CCNA2-052 · IP Connectivity

Objectives: 3.3.a, 3.3.d · multiple · Applied

After the primary directly connected transit link goes down, its ordinary static default is removed. A second default with distance 220 has a still-resolvable next hop. No other defaults exist. Which two observations should follow after convergence? Select two.

- **A.** The second default becomes eligible for installation.
- **B.** Unmatched destinations use the second default once it is installed.
- **C.** The distance must be reduced to zero during the outage.
- **D.** The second default needs an OSPF neighbor before it can install.

**Answer: A, B**

This failure removes the primary route’s own resolving link, unlike an undetected distant ISP failure. The higher distance does not prevent use when the preferred candidate vanishes.

**Option explanations**

- **A:** Its valid next hop remains available after the primary route disappears.
- **B:** The installed default supplies the remaining fallback path.
- **C:** Distance 220 can win when no lower-distance default remains.
- **D:** Static route installation does not require OSPF.

**Further reading**

- [Configure a Next Hop IP Address for Static Routes](https://www.cisco.com/c/en/us/support/docs/dial-access/floating-static-route/118263-technote-nexthop-00.html) — Background Information; Floating Static Route Example
- [Understand Administrative Distance](https://www.cisco.com/c/en/us/support/docs/ip/border-gateway-protocol-bgp/15986-admin-distance.html) — RIB Route Comparison; Route Installation; Default AD Values

---

## CCNA2-053 · IP Connectivity

Objectives: 3.4.a · single · Applied

A router’s LAN prefix remains reachable through OSPF, but no OSPF Hellos leave that LAN interface. The interface is up and enabled in area 0. Which setting explains both observations?

- **A.** passive-interface on the LAN
- **B.** shutdown on the LAN
- **C.** An OSPF priority of zero on the LAN
- **D.** A duplicate router ID on a remote router

**Answer: A**

Passive operation is useful on host-only LANs. Other nonpassive adjacencies can still carry the subnet advertisement.

**Option explanations**

- **A:** OSPF can advertise the subnet while suppressing adjacency formation on that interface.
- **B:** Shutdown would remove the working connected LAN path described.
- **C:** Priority zero prevents DR election, not Hello transmission.
- **D:** Duplicate IDs are a fault, not the intended way to advertise without LAN Hellos.

**Further reading**

- [Default Passive Interfaces — Cisco IOS XE 17.x](https://www.cisco.com/c/en/us/td/docs/routers/ios/config/17-x/ip-routing/b-ip-routing/m_iri-default-passive-interface.html) — Information About Default Passive Interfaces

---

## CCNA2-054 · IP Connectivity

Objectives: 3.4.a · single · Foundation

R1 and R2 share a working broadcast subnet. R1 uses OSPF process 1 and R2 process 99; both interfaces are in area 0. All other adjacency requirements match. What should the engineer do about these process IDs?

- **A.** Create an area 99 on R1.
- **B.** Leave them; the process numbers are locally significant.
- **C.** Set each interface priority equal to the other process ID.
- **D.** Change both to process 0.

**Answer: B**

The local process identifier organizes configuration on one device. Area IDs, timers and authentication are among the actual neighbor compatibility checks.

**Option explanations**

- **A:** Changing the area would break the stated area match.
- **B:** OSPF neighbors do not need identical local process numbers.
- **C:** DR priority is independent of the local process identifier.
- **D:** A shared process number is unnecessary and zero is not the solution.

**Further reading**

- [Configuring OSPF — IP Routing: OSPF Configuration Guide](https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/iproute_ospf/configuration/xe-16/iro-xe-16-book/iro-cfg.html) — Enabling OSPF; Configuring OSPF Interface Parameters
- [Troubleshoot OSPF Neighbor Problems](https://www.cisco.com/c/en/us/support/docs/ip/open-shortest-path-first-ospf/13699-29.html) — No State Revealed; Neighbors Stuck in Exstart/Exchange State

---

## CCNA2-055 · IP Connectivity

Objectives: 3.4.a · single · Applied

Two newly connected routers exchange Hellos but remain in ExStart/Exchange. The excerpt is their only discovered mismatch; authentication, area, subnet, timers and network type match. What is the most appropriate repair?

```text
R1 GigabitEthernet0/0: IP MTU 1500, OSPF area 0
R2 GigabitEthernet0/0: IP MTU 1400, OSPF area 0
```

- **A.** Add a default route on both routers.
- **B.** Make the IP MTU consistent with the supported end-to-end link.
- **C.** Assign the same router ID to both routers.
- **D.** Increase the DR priority on both routers.

**Answer: B**

Hello success does not prove database synchronization can complete. Correcting the underlying MTU mismatch is preferable to hiding it with a check override.

**Option explanations**

- **A:** Direct OSPF adjacency does not require an Internet default.
- **B:** MTU mismatch can prevent database-description exchange from completing.
- **C:** Router IDs must be unique; this creates an additional fault.
- **D:** Election priority does not repair database-description MTU checks.

**Further reading**

- [Troubleshoot OSPF Neighbor Problems](https://www.cisco.com/c/en/us/support/docs/ip/open-shortest-path-first-ospf/13699-29.html) — No State Revealed; Neighbors Stuck in Exstart/Exchange State

---

## CCNA2-056 · IP Connectivity

Objectives: 3.4.b, 3.4.c · single · Applied

Two Ethernet interfaces will be dedicated to a router-to-router OSPF link. The design requires no DR/BDR election on that link. Which interface-level change belongs on both routers?

- **A.** ip ospf network point-to-point
- **B.** ip ospf priority 0
- **C.** ip ospf cost 1
- **D.** passive-interface under OSPF

**Answer: A**

The physical medium can be Ethernet while the OSPF network type is point-to-point. Configure the intended type consistently at both ends.

**Option explanations**

- **A:** This explicitly selects the OSPF type without DR/BDR election.
- **B:** Two ineligible broadcast routers do not turn the link into point-to-point.
- **C:** Cost affects path ranking, not the OSPF network type.
- **D:** Passive operation prevents the required adjacency.

**Further reading**

- [Configuring OSPF — IP Routing: OSPF Configuration Guide](https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/iproute_ospf/configuration/xe-16/iro-xe-16-book/iro-cfg.html) — Enabling OSPF; Configuring OSPF Interface Parameters
- [RFC 2328: OSPF Version 2](https://www.rfc-editor.org/rfc/rfc2328.html) — 9.4 Electing the Designated Router; 10 The Neighbor Data Structure; 16 Calculation of the routing table

---

## CCNA2-057 · IP Connectivity

Objectives: 3.4.c · single · Applied

R1 is DR, R2 is BDR and R3 is DROTHER on a stable broadcast LAN. R1 fails. R2 and R3 remain eligible, and no new router joins. After failure detection, which role does R2 take?

- **A.** Passive router
- **B.** DR
- **C.** DROTHER until R3 fails
- **D.** Area border router

**Answer: B**

The BDR provides a prepared successor on the shared segment. Its promotion avoids treating every DR loss as an unrelated fresh start.

**Option explanations**

- **A:** Passive-interface is a configuration property, not an elected replacement role.
- **B:** The existing BDR takes over when the DR disappears.
- **C:** The BDR is specifically positioned to replace the DR.
- **D:** DR election does not change the areas to which a router belongs.

**Further reading**

- [RFC 2328: OSPF Version 2](https://www.rfc-editor.org/rfc/rfc2328.html) — 9.4 Electing the Designated Router; 10 The Neighbor Data Structure; 16 Calculation of the routing table

---

## CCNA2-058 · IP Connectivity

Objectives: 3.4.c, 3.4.d · single · Applied

Three eligible OSPFv2 routers share a new broadcast LAN. Before the initial election, all three have discovered one another bidirectionally, and no router has already declared itself DR or BDR. Under these assumptions, which router becomes DR?

| Router | Priority | Router ID |
| --- | --- | --- |
| R1 | 1 | 250.1.1.1 |
| R2 | 80 | 10.0.0.20 |
| R3 | 80 | 10.0.0.9 |

- **A.** No router, because the priorities are not unique
- **B.** R3
- **C.** R2
- **D.** R1

**Answer: C**

Compare priority before router ID. The question specifies an initial election, so no incumbent nonpreemption behavior changes the result.

**Option explanations**

- **A:** Equal priorities are resolved by router ID.
- **B:** R3 ties on priority but loses the router-ID comparison.
- **C:** R2 and R3 tie at priority 80; R2 has the higher router ID.
- **D:** A higher router ID cannot overcome R1’s lower interface priority.

**Further reading**

- [RFC 2328: OSPF Version 2](https://www.rfc-editor.org/rfc/rfc2328.html#section-9.4) — 9.4 Electing the Designated Router

---

## CCNA2-059 · IP Connectivity

Objectives: 3.4.d · single · Applied

OSPF already uses router ID 10.0.0.1. An engineer adds an up loopback with address 10.255.255.255 but does not restart OSPF. What router ID should be expected immediately afterward?

- **A.** 0.0.0.0
- **B.** 10.255.255.255
- **C.** 10.0.0.1
- **D.** The highest neighbor router ID

**Answer: C**

A selected router ID is stable during normal process operation. Planned ID changes require attention to the process restart and adjacency impact.

**Option explanations**

- **A:** The running OSPF process does not discard a valid ID for this change.
- **B:** Automatic selection is not rerun merely because a new loopback appears.
- **C:** Adding a higher-address loopback does not automatically replace an active router ID.
- **D:** Each router chooses its own ID, not a neighbor’s.

**Further reading**

- [Configuring OSPF — IP Routing: OSPF Configuration Guide](https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/iproute_ospf/configuration/xe-16/iro-xe-16-book/iro-cfg.html) — Enabling OSPF; Configuring OSPF Interface Parameters

---

## CCNA2-060 · IP Connectivity

Objectives: 3.4.d · single · Foundation

A router starts OSPF for the first time with explicit router-id 4.4.4.4. Its up loopback is 10.10.10.10 and physical interface is 192.0.2.10. Which address identifies this OSPF router?

- **A.** The address with the longest subnet mask
- **B.** 4.4.4.4
- **C.** 10.10.10.10
- **D.** 192.0.2.10

**Answer: B**

The OSPF router ID is a 32-bit identifier. An explicitly configured value does not have to equal an interface address.

**Option explanations**

- **A:** Router-ID selection is not a longest-prefix lookup.
- **B:** The explicit router-id setting takes precedence over automatic interface selection.
- **C:** Loopback preference applies when no explicit router ID is configured.
- **D:** The physical address does not override a configured router ID.

**Further reading**

- [Configuring OSPF — IP Routing: OSPF Configuration Guide](https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/iproute_ospf/configuration/xe-16/iro-xe-16-book/iro-cfg.html) — Enabling OSPF; Configuring OSPF Interface Parameters

---

## CCNA2-061 · IP Connectivity

Objectives: 3.2.c · single · Applied

Two intra-area OSPF paths to a LAN have equal total cost 30. Both next hops are valid and the configured maximum-paths is 2. What should the RIB be able to install?

- **A.** Both equal-cost next hops
- **B.** Only the path through the higher router ID
- **C.** Neither path until their costs differ
- **D.** Only the path with fewer physical hops

**Answer: A**

OSPF can offer multiple equal-cost paths to the same prefix. This does not promise that every individual flow uses both paths.

**Option explanations**

- **A:** The equal-cost paths fit the configured multipath limit.
- **B:** Router ID is not a blanket tie-break that disables eligible ECMP.
- **C:** Equal cost permits multipath; it is not an installation error.
- **D:** OSPF ranks these intra-area paths by their total cost, not hop count.

**Further reading**

- [Configure Route Selection for Routers](https://www.cisco.com/c/en/us/support/docs/ip/enhanced-interior-gateway-routing-protocol-eigrp/8651-21.html) — Build the Routing Table; Make Forwarding Decisions
- [RFC 2328: OSPF Version 2](https://www.rfc-editor.org/rfc/rfc2328.html) — 9.4 Electing the Designated Router; 10 The Neighbor Data Structure; 16 Calculation of the routing table

---

## CCNA2-062 · IP Connectivity

Objectives: 3.4.a, 3.4.b · multiple · Applied

R1 is FULL with R2 over a point-to-point OSPF link. An engineer accidentally makes that interface passive on R1. Assuming no other adjacency exists between them, which two outcomes are expected after detection? Select two.

- **A.** Their adjacency on this link is lost.
- **B.** Routes dependent only on that adjacency can be withdrawn.
- **C.** The physical interface is administratively shut down.
- **D.** R1 becomes the link’s BDR.

**Answer: A, B**

Passive-interface changes OSPF control-plane participation while the physical IP link may remain operational. Connected traffic and routing adjacency state are separate observations.

**Option explanations**

- **A:** R1 no longer participates in Hello-based adjacency formation on the interface.
- **B:** Losing the only path removes reachability learned through that neighbor.
- **C:** Passive OSPF does not issue an interface shutdown.
- **D:** A point-to-point OSPF link has no DR/BDR role.

**Further reading**

- [Default Passive Interfaces — Cisco IOS XE 17.x](https://www.cisco.com/c/en/us/td/docs/routers/ios/config/17-x/ip-routing/b-ip-routing/m_iri-default-passive-interface.html) — Information About Default Passive Interfaces
- [Understand OSPF Neighbor States](https://www.cisco.com/c/en/us/support/docs/ip/open-shortest-path-first-ospf/13685-13.html) — OSPF Neighbor States

---

## CCNA2-063 · IP Connectivity

Objectives: 3.5 · single · Applied

A host was configured to use R1’s physical address as its gateway. R1 and R2 also run a healthy HSRP group, but the host loses off-subnet access when R1 fails. Which correction addresses the host configuration?

- **A.** Use the subnet broadcast address as the gateway.
- **B.** Increase the host’s subnet prefix length to /32.
- **C.** Configure the HSRP virtual IP as the host gateway.
- **D.** Configure R2’s OSPF router ID as the host gateway.

**Answer: C**

An operational redundancy group helps hosts that actually use its virtual gateway. It cannot transparently transfer an arbitrary physical interface address.

**Option explanations**

- **A:** A broadcast address does not identify a forwarding next hop.
- **B:** Changing the mask does not make R1’s failed physical address redundant.
- **C:** The virtual address is the stable first-hop identity transferred during failover.
- **D:** A router ID is not necessarily an address reachable on the host’s LAN.

**Further reading**

- [Understand the Hot Standby Router Protocol Features and Functionality](https://www.cisco.com/c/en/us/support/docs/ip/hot-standby-router-protocol-hsrp/9234-hsrpguidetoc.html) — HSRP Background and Operations; HSRP Operation

---

## CCNA2-064 · IP Connectivity

Objectives: 3.5 · single · Challenge

R1 is HSRP active with priority 110; R2 is standby with priority 100. R1 remains reachable on the LAN but loses a tracked uplink, causing a decrement of 20. R2 has preemption enabled and a working upstream path. What follows after protocol convergence?

- **A.** R1 stays active because tracking only changes its MAC address.
- **B.** R2 takes the active role because 100 exceeds R1’s new priority 90.
- **C.** R2 lowers its own priority to 80.
- **D.** Both routers must reboot before the priority changes.

**Answer: B**

Calculate effective priority after the tracked event. The explicit preemption condition allows the healthier router to take over while R1 still sends Hellos.

**Option explanations**

- **A:** Tracking changes priority; it does not create a new MAC address.
- **B:** The tracked failure lowers R1 below the preempting standby.
- **C:** The configured decrement applies to R1, whose object failed.
- **D:** Tracked state changes can affect priority while routers are running.

**Further reading**

- [Use HSRP Preempt and Track Commands](https://www.cisco.com/c/en/us/support/docs/ip/hot-standby-router-protocol-hsrp/13780-6.html) — Preempt and Track Commands

---

## CCNA2-065 · IP Connectivity

Objectives: 3.5 · single · Foundation

Two routers provide VRRPv3 for a VLAN. The active router fails and the backup assumes forwarding responsibility. What should a correctly configured host retain?

- **A.** A dependency on the failed router’s physical MAC
- **B.** A newly assigned IP subnet for every failover
- **C.** Its configured virtual default-gateway address
- **D.** An OSPF adjacency with the replacement router

**Answer: C**

First-hop redundancy moves responsibility for a virtual router. It avoids a host configuration change during an eligible gateway failure.

**Option explanations**

- **A:** The service relies on the virtual gateway, not a permanently fixed physical router.
- **B:** First-hop role changes do not require renumbering the host subnet.
- **C:** VRRP preserves the virtual router identity across the change of physical forwarder.
- **D:** Ordinary end hosts need not run OSPF for first-hop redundancy.

**Further reading**

- [RFC 9568: Virtual Router Redundancy Protocol (VRRP) Version 3 for IPv4 and IPv6](https://www.rfc-editor.org/rfc/rfc9568.html) — 1 Introduction; 2 Required Features; 6 Protocol State Machine

---

## CCNA2-066 · IP Services

Objectives: 4.1 · single · Applied

The constructed NAT table shows a connection opened by an inside workstation. Which address is the workstation's inside global address?

```text
Pro  Inside global       Inside local       Outside local       Outside global
tcp  203.0.113.41:49180   10.18.5.41:49180   192.0.2.80:443      192.0.2.80:443
```

- **A.** 10.18.5.1
- **B.** 192.0.2.80
- **C.** 203.0.113.41
- **D.** 10.18.5.41

**Answer: C**

Read the inside-global column for the inside host's translated address. The outside columns describe the remote server, even though both contain the same address in this example.

**Option explanations**

- **A:** The router gateway is not the workstation's translated identity.
- **B:** This is the outside server; its local and global addresses are equal here.
- **C:** This is the translated identity of the inside workstation as seen from outside.
- **D:** This is the inside local address before translation.

**Further reading**

- [Configure Network Address Translation](https://www.cisco.com/c/en/us/support/docs/ip/network-address-translation-nat/13772-12.html) — NAT definitions; configuring inside source translation

---

## CCNA2-067 · IP Services

Objectives: 4.1 · single · Applied

A router should translate clients in 10.12.7.0/24 using a dynamic pool without overload. Its inside/outside interface designations and routes are correct, and the pool has unused addresses. A packet from 10.12.7.25 crosses the router but does not create a translation. Which change corrects the shown mismatch?

```text
access-list 12 permit 10.12.8.0 0.0.0.255
ip nat pool CLIENTS 203.0.113.50 203.0.113.60 netmask 255.255.255.0
ip nat inside source list 12 pool CLIENTS
```

- **A.** Change the NAT rule from inside source to outside source.
- **B.** Replace ACL 12 with a permit for 10.12.7.0 0.0.0.255.
- **C.** Add overload to the NAT rule.
- **D.** Change the pool mask to 255.255.0.0.

**Answer: B**

The NAT ACL identifies which inside source addresses are eligible for this dynamic mapping. Correcting 10.12.8.0/24 to 10.12.7.0/24 addresses the fault; an ACL used only for NAT selection is not an interface filtering ACL.

**Option explanations**

- **A:** The required translation still concerns inside client source addresses.
- **B:** The current rule selects the wrong inside subnet.
- **C:** Port sharing does not make the wrong ACL match this client.
- **D:** The pool mask does not select the inside source subnet.

**Further reading**

- [IP Addressing Configuration Guide, Cisco IOS XE 17.x — Configuring NAT for IP Address Conservation](https://www.cisco.com/c/en/us/td/docs/routers/ios/config/17-x/ip-addressing/b-ip-addressing/m_iadnat-addr-consv-xe.html) — Inside source address translation; static and dynamic translations; monitoring NAT

---

## CCNA2-068 · IP Services

Objectives: 4.2 · single · Applied

An engineer checks a router immediately after configuring an NTP server. The constructed status below remains unchanged after several polling intervals. Which conclusion is justified?

```text
R3# show ntp status
Clock is unsynchronized, stratum 16, no reference clock
```

- **A.** The router is synchronized because the server address is present in running configuration.
- **B.** Changing the display time zone is required before NTP can synchronize.
- **C.** The router has not established synchronization; configuration alone is insufficient proof.
- **D.** Stratum 16 identifies a particularly accurate reference clock.

**Answer: C**

NTP operating state must be checked separately from intended configuration. Unsynchronized status requires investigation of reachability, server suitability, and NTP exchanges; the output does not isolate one specific cause.

**Option explanations**

- **A:** A configured association does not establish that usable time was received.
- **B:** Time-zone display settings do not establish the NTP association.
- **C:** The status explicitly reports unsynchronized operation and stratum 16.
- **D:** Stratum 16 represents unsynchronized operation, not high accuracy.

**Further reading**

- [RFC 5905 — Network Time Protocol Version 4: Protocol and Algorithms Specification](https://www.rfc-editor.org/rfc/rfc5905.html) — 7 NTP protocol data structures; 9 Peer process; 11 System process
- [Setting Time and Calendar Services](https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/bsm/configuration/15-mt/bsm-15-mt-book/bsm-time-calendar-set.html) — Network Time Protocol; configuring NTP associations; monitoring NTP

---

## CCNA2-069 · IP Services

Objectives: 4.3 · single · Applied

A laptop receives a DHCP lease and successfully resolves files.example to 192.0.2.44. A connection to that address then times out. Which statement correctly separates the services involved?

- **A.** The successful DNS reply proves that TCP port 445 on 192.0.2.44 is accepting connections.
- **B.** The DHCP lease guarantees a route from every remote server back to the laptop.
- **C.** DHCP supplied host configuration and DNS supplied a name-to-address result; neither proves the file service is reachable.
- **D.** The DNS server must forward the laptop's file traffic after returning the address.

**Answer: C**

Successful setup steps narrow troubleshooting but do not certify end-to-end application operation. The next investigation concerns routing, filtering, transport, or the target service rather than assuming DNS success guarantees delivery.

**Option explanations**

- **A:** DNS returns records; it does not test that application port.
- **B:** A lease does not validate the complete routing path.
- **C:** Address configuration and name resolution can succeed independently of application connectivity.
- **D:** A resolver normally returns an answer without becoming the application data path.

**Further reading**

- [RFC 2131 — Dynamic Host Configuration Protocol](https://www.rfc-editor.org/rfc/rfc2131.html) — 3.1 Address allocation; 4.3 Server behavior; 4.4 Client behavior
- [RFC 1034 — Domain Names - Concepts and Facilities](https://www.rfc-editor.org/rfc/rfc1034.html) — 3.6 Resource records; 4.3 Name server algorithms; 5 Resolvers

---

## CCNA2-070 · IP Services

Objectives: 4.4 · single · Applied

A monitoring team requires SNMP notifications for critical events and wants the receiving manager to acknowledge receipt. Which operation meets that requirement?

- **A.** GetNext request
- **B.** SNMPv2 trap
- **C.** Inform request
- **D.** Set request to the interface counter

**Answer: C**

An inform adds acknowledgment to asynchronous event notification. It improves delivery feedback over traps but still cannot guarantee success when the path or manager remains unavailable.

**Option explanations**

- **A:** GetNext retrieves the next object instance; it is not an acknowledged event notification.
- **B:** A trap does not receive an SNMP acknowledgment.
- **C:** An inform expects a response from the receiving manager and can be retried.
- **D:** Set modifies writable objects; an interface traffic counter is not an event delivery service.

**Further reading**

- [RFC 3416 — Version 2 of the Protocol Operations for the Simple Network Management Protocol (SNMP)](https://www.rfc-editor.org/rfc/rfc3416.html) — 4.2 PDU processing: Get, GetNext, GetBulk, Set, notifications

---

## CCNA2-071 · IP Services

Objectives: 4.5 · multiple · Applied

A console displays debugging messages while a remote syslog server receives only errors and more severe events. Which two statements follow from the constructed configuration? Select two.

```text
logging console debugging
logging host 10.90.0.15
logging trap errors
```

- **A.** A severity 4 warning is excluded from the remote server.
- **B.** Console debugging automatically raises the remote threshold to debugging.
- **C.** The logging host command overrides all severity filtering.
- **D.** A severity 6 message can appear on the console.
- **E.** Severity 0 messages are excluded from both destinations.

**Answer: A, D**

Destination-specific thresholds allow detailed local logging and more selective remote collection. Lower numeric severity means greater urgency, so an errors threshold includes 0, 1, 2, and 3.

**Option explanations**

- **A:** The remote threshold is errors, admitting levels 0 through 3.
- **B:** Each destination has its own threshold.
- **C:** The host specifies the destination; logging trap still controls its severity threshold.
- **D:** Console debugging admits levels 0 through 7, including informational level 6.
- **E:** Level 0 is the most severe and is within both configured thresholds.

**Further reading**

- [System Message Logging](https://www.cisco.com/c/en/us/td/docs/routers/access/wireless/software/guide/SysMsgLogging.html) — System log message format; logging destinations; severity levels; timestamps

---

## CCNA2-072 · IP Services

Objectives: 4.6 · single · Applied

A DHCPDISCOVER arrives on a router's VLAN 24 interface, 10.24.0.1/24. The interface has ip helper-address 10.99.0.20. With default relay behavior, one primary address, and no relay overrides, which giaddr does the forwarded DHCP message contain?

- **A.** 10.24.0.1
- **B.** The future address offered to the client
- **C.** 255.255.255.255
- **D.** 10.99.0.20

**Answer: A**

The relay inserts its client-facing interface address into giaddr. The server can then select the client subnet's scope and direct its reply to the relay.

**Option explanations**

- **A:** The relay identifies the client subnet with the receiving interface's address.
- **B:** The relay forwards discovery before an offered client address has been selected.
- **C:** That is a broadcast destination, not the relay's giaddr.
- **D:** This is the DHCP server destination, not the relay gateway-address field.

**Further reading**

- [IP Addressing: DHCP Configuration Guide, Cisco IOS XE Everest 16.6 — Configuring the Cisco IOS XE DHCP Relay Agent](https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/ipaddr_dhcp/configuration/xe-16-6/dhcp-xe-16-6-book/dhcp-relay-agent-xe.html) — Packet forwarding address; giaddr; specifying the packet forwarding address

---

## CCNA2-073 · IP Services

Objectives: 4.7 · single · Applied

A branch sends bursts over a 1 Gb/s handoff into a provider service limited to 50 Mb/s. The provider drops traffic outside its profile. The branch can tolerate buffering delay and wants to smooth its outbound bursts before the handoff. Which mechanism best fits?

- **A.** Egress shaping to the contracted rate
- **B.** Ingress policing with excess traffic dropped
- **C.** Changing every packet to the priority queue
- **D.** DSCP marking alone

**Answer: A**

Shaping trades additional queuing delay for smoother transmission into the downstream rate limit. Buffers remain finite, so persistent offered load above the shaped rate can still cause drops.

**Option explanations**

- **A:** Shaping delays eligible queued packets to control their release rate.
- **B:** Dropping bursts at ingress does not smooth them through delayed transmission.
- **C:** Priority scheduling does not by itself impose the required 50 Mb/s profile.
- **D:** A header label does not enforce a sending rate.

**Further reading**

- [Compare Traffic Policing and Traffic Shaping to Limit Bandwidth](https://www.cisco.com/c/en/us/support/docs/quality-of-service-qos/qos-policing/19645-policevsshape.html) — Traffic policing and traffic shaping comparison

---

## CCNA2-074 · IP Services

Objectives: 4.8 · single · Applied

An IOS XE router uses local password authentication, has SSH-capable software, a configured hostname/domain, and correct VTY settings. show ip ssh reports that SSH is disabled, and inspection confirms that no host key exists. Which remaining action enables the missing prerequisite?

- **A.** Configure ip name-server for public DNS.
- **B.** Change transport input ssh to transport input telnet.
- **C.** Set an enable secret without generating keys.
- **D.** Generate a supported RSA host key pair with crypto key generate rsa.

**Answer: D**

A conventional IOS XE RSA-based SSH server requires a generated host key pair. Use a key size supported by the platform and policy; creating the key addresses the stated missing dependency.

**Option explanations**

- **A:** DNS lookup service is not a substitute for the server host key.
- **B:** That permits a different protocol and does not enable SSH.
- **C:** An enable secret controls privilege escalation and does not supply the SSH host key.
- **D:** The SSH server needs a host key; the other prerequisites already exist.

**Further reading**

- [Configure SSH on Routers](https://www.cisco.com/c/en/us/support/docs/security-vpn/secure-shell-ssh/4145-ssh.html) — SSH server prerequisites; SSHv2; VTY restrictions; show commands

---

## CCNA2-075 · IP Services

Objectives: 4.9 · single · Applied

An FTP client logs in successfully over TCP port 21, but directory listing and file downloads both stall. A firewall permits only that control connection and has no FTP inspection or additional data rules. Which explanation best fits?

- **A.** The client must switch the control connection to UDP port 69.
- **B.** FTP carries all file data inside the TCP port 21 control stream.
- **C.** A successful login guarantees that every FTP data transfer is allowed.
- **D.** FTP needs a separate data connection that the firewall has not permitted.

**Answer: D**

The control connection can work while the data connection fails. The required data connection depends on active or passive mode, so firewall behavior must match the selected FTP mode.

**Option explanations**

- **A:** That is associated with TFTP requests, not FTP control.
- **B:** The FTP model separates commands/replies from file data.
- **C:** Authentication success does not verify the separate data path.
- **D:** Listing and file contents use the data connection, not only the control connection.

**Further reading**

- [RFC 959 — File Transfer Protocol (FTP)](https://www.rfc-editor.org/rfc/rfc959.html) — 2.3 FTP model; 3.2 Data connections; 4.1 FTP commands

---

## CCNA2-076 · Security Fundamentals

Objectives: 5.1 · single · Applied

A branch router exposes an unnecessary management service. An attacker sends a specially crafted request that uses a defect in that service to execute code. Which part of this account is the exploit?

- **A.** Disabling the unused management service.
- **B.** The software defect before any request arrives.
- **C.** The crafted request that triggers the defect.
- **D.** The organization’s possible loss of router control.

**Answer: C**

Distinguish the weakness from its use: the defect is a vulnerability, and the crafted request exploits it. Removing the unnecessary service can reduce the exposed attack surface.

**Option explanations**

- **A:** Disabling the service is a mitigation that removes an exposure.
- **B:** The defect is the vulnerability, independent of an attack attempt.
- **C:** The request is the mechanism used to take advantage of the weakness.
- **D:** Loss of control is an adverse consequence, not the mechanism.

**Further reading**

- [RFC 4949: Internet Security Glossary, Version 2](https://www.rfc-editor.org/rfc/rfc4949.html) — Section 2: threat, vulnerability, exploit, and countermeasure

---

## CCNA2-077 · Security Fundamentals

Objectives: 5.2 · single · Applied

A courier carrying a large package asks an engineer to hold open a badge-controlled equipment-room door. The courier is not on the approved visitor list. Which response follows effective physical access control?

- **A.** Direct the courier to the visitor verification process before entry.
- **B.** Ask the courier to avoid touching the switches after entering.
- **C.** Admit the courier if the package displays the company logo.
- **D.** Admit the courier and record the engineer’s badge number.

**Answer: A**

A secured doorway is ineffective if an authorized person lets an unverified visitor bypass it. Follow the visitor process, including any required approval and escort.

**Option explanations**

- **A:** Identity and authorization must be checked before access is granted.
- **B:** An informal promise does not enforce the restricted boundary.
- **C:** A package marking is not proof of access authorization.
- **D:** One person’s badge does not authorize an unverified visitor.

**Further reading**

- [NIST SP 800-53 Rev. 5: Security and Privacy Controls for Information Systems and Organizations](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-53r5.pdf) — AT-2, AT-3, PE-2, and PE-3: awareness, training, and physical access

---

## CCNA2-078 · Security Fundamentals

Objectives: 5.3 · single · Applied

On this IOS device, AAA is disabled and no custom privilege levels exist. A user logs in at the R1> prompt, types enable, and is asked for a password. Which configured credential is checked?

```text
username junior privilege 1 secret LoginKey!
enable password EntryKey!
enable secret PrivilegeKey!
line console 0
 login local
```

- **A.** Both EntryKey! and PrivilegeKey! in sequence.
- **B.** PrivilegeKey!
- **C.** EntryKey!
- **D.** LoginKey!

**Answer: B**

The login credential and the privileged EXEC credential control different transitions. With both enable commands present, the enable secret is the effective enable credential.

**Option explanations**

- **A:** IOS does not require both enable credentials.
- **B:** The enable secret takes precedence for the default privileged EXEC level.
- **C:** The enable password is superseded when an enable secret is configured.
- **D:** This is the local account secret used for login, not the separate enable challenge.

**Further reading**

- [Catalyst 3750-X and 3560-X Configuration Guide: Configuring Switch-Based Authentication](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst3750x_3560x/software/release/15-0_2_se/configuration/guide/3750x_cg/swauthen.html) — Protecting Access to Privileged EXEC Commands; Configuring Username and Password Pairs

---

## CCNA2-079 · Security Fundamentals

Objectives: 5.4 · single · Applied

A contractor leaves after learning a shared router administrator password. The account cannot immediately be removed because other engineers still use it. Which action directly removes the former contractor’s knowledge-based access?

- **A.** Rotate the shared password and distribute the replacement only to authorized users.
- **B.** Require a second security question with an answer known to the contractor.
- **C.** Disable the contractor’s VPN profile but keep the exposed shared password valid on other reachable management paths.
- **D.** Increase the session idle timeout.

**Answer: A**

Change credentials when their authorized holders change or compromise is suspected. Individual accounts would make later revocation and attribution easier.

**Option explanations**

- **A:** The previously disclosed value must stop authenticating.
- **B:** Another known secret does not revoke the existing access.
- **C:** Removing one access path does not revoke a known shared credential on the remaining paths.
- **D:** This affects inactivity, not possession of a valid password.

**Further reading**

- [NIST SP 800-63B-4: Digital Identity Guidelines — Authentication and Authenticator Management](https://pages.nist.gov/800-63-4/sp800-63b.html) — Authentication factors; password verifiers; authenticator management

---

## CCNA2-080 · Security Fundamentals

Objectives: 5.5 · single · Applied

An employee uses a remote-access IPsec VPN from a hotel. Split tunneling sends only corporate prefixes through the tunnel. Which traffic is protected by this VPN under that policy?

- **A.** All traffic generated by every device on the hotel LAN.
- **B.** Only DNS traffic, because IPsec cannot carry TCP.
- **C.** Corporate-prefix traffic selected for the tunnel.
- **D.** All traffic from this laptop regardless of its route or VPN policy.

**Answer: C**

An active VPN does not imply that every packet uses it. The selected corporate traffic enters the tunnel; traffic sent directly through the hotel connection is outside this VPN’s protection.

**Option explanations**

- **A:** A single endpoint VPN does not encompass other hotel devices.
- **B:** IPsec can protect ordinary IP traffic, including TCP.
- **C:** Split-tunnel policy determines which endpoint traffic enters IPsec.
- **D:** The premise explicitly excludes noncorporate destinations from the tunnel.

**Further reading**

- [RFC 4301: Security Architecture for the Internet Protocol](https://www.rfc-editor.org/rfc/rfc4301.html) — Sections 3, 4.1, 4.4.1: IPsec services, tunnel mode, and security policy

---

## CCNA2-081 · Security Fundamentals

Objectives: 5.6 · single · Applied

An IPv4 ACL must permit exactly the source subnet 172.20.44.64/26. Which source-and-wildcard pair represents that range?

- **A.** 172.20.44.64 0.0.0.31
- **B.** 172.20.44.64 0.0.0.63
- **C.** 172.20.44.64 0.0.0.127
- **D.** 172.20.44.64 255.255.255.192

**Answer: B**

A /26 fixes 26 bits and leaves six address bits variable. Its wildcard is 0.0.0.63; the aligned range starts at .64 and ends at .127.

**Option explanations**

- **A:** Five variable bits cover only .64 through .95.
- **B:** The six low bits may vary, covering .64 through .127.
- **C:** Seven variable bits include the entire .0 through .127 range.
- **D:** This is the subnet mask, not the wildcard for this prefix.

**Further reading**

- [Configure IP Access Lists](https://www.cisco.com/c/en/us/support/docs/security/ios-firewall/23602-confaccesslists.html) — ACL Concepts; Masks; Process ACLs; Apply ACLs; Extended ACLs

---

## CCNA2-082 · Security Fundamentals

Objectives: 5.7 · single · Applied

A switch reports DHCP snooping enabled globally but only VLAN 10 is listed as enabled. A rogue DHCP server is connected to an untrusted access port in VLAN 30. Which missing configuration explains why snooping does not filter its replies in VLAN 30?

- **A.** ip dhcp snooping vlan 30
- **B.** ip arp inspection vlan 30
- **C.** switchport port-security maximum 30
- **D.** ip dhcp snooping trust on the rogue server port

**Answer: A**

Global activation alone does not select every VLAN. Enable DHCP snooping for VLAN 30 and retain untrusted client-facing ingress.

**Option explanations**

- **A:** Snooping must also be enabled for the VLAN carrying the messages.
- **B:** DAI examines ARP, not DHCP server replies.
- **C:** A secure MAC limit does not enable DHCP message inspection.
- **D:** Trusting that ingress would permit the unwanted server messages.

**Further reading**

- [Catalyst 3750-X and 3560-X Configuration Guide: Configuring DHCP Features and IP Source Guard](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst3750x_3560x/software/release/15-0_2_se/configuration/guide/3750x_cg/swdhcp82.html) — DHCP Snooping; DHCP Snooping Binding Database; Enabling DHCP Snooping

---

## CCNA2-083 · Security Fundamentals

Objectives: 5.8 · single · Applied

A technician can log in to a network device with a valid identity, but the device rejects configure terminal according to a central role policy. Which AAA function made the command decision?

- **A.** Authentication
- **B.** Encryption
- **C.** Accounting
- **D.** Authorization

**Answer: D**

Successful authentication does not grant every privilege. The command is denied because the authorization policy excludes configuration access for that role.

**Option explanations**

- **A:** Identity was already accepted before the command was requested.
- **B:** Encryption protects data representation and transport; it is not this permission decision.
- **C:** Accounting records activity rather than deciding whether this command is allowed.
- **D:** Authorization evaluates the authenticated user’s permitted actions.

**Further reading**

- [RFC 8907: The Terminal Access Controller Access-Control System Plus (TACACS+) Protocol](https://www.rfc-editor.org/rfc/rfc8907.html) — Sections 5, 6, and 7: authentication, authorization, and accounting

---

## CCNA2-084 · Security Fundamentals

Objectives: 5.9 · single · Applied

An office is replacing a legacy WPA/TKIP WLAN. Its selected replacement is WPA2-Personal using AES-CCMP. Which statement correctly separates the authentication choice from the cipher choice?

- **A.** AES-CCMP supplies each employee with a unique enterprise identity.
- **B.** Personal selects shared-key authentication; AES-CCMP protects wireless data frames.
- **C.** Personal means that wireless traffic is unencrypted.
- **D.** Selecting AES-CCMP changes PSK authentication into 802.1X automatically.

**Answer: B**

WPA2-Personal uses a preshared credential, whereas AES-CCMP supplies the data-protection mechanism. Enterprise authentication requires an appropriate 802.1X deployment.

**Option explanations**

- **A:** The cipher does not create individual accounts.
- **B:** The credential model and the data-protection suite are separate settings.
- **C:** WPA2-Personal still encrypts protected wireless data.
- **D:** The cipher does not switch the authentication key-management method.

**Further reading**

- [Cisco Wireless Controller Configuration Guide, Release 8.10: WLAN Security](https://www.cisco.com/c/en/us/td/docs/wireless/controller/8-10/config-guide/b_cg810/wlan_security.html) — WPA1+WPA2; Configuring WPA1+WPA2 (GUI); Protected Management Frames

---

## CCNA2-085 · Security Fundamentals

Objectives: 5.10 · single · Applied

A constructed AireOS 8.10 GUI summary shows a WLAN prepared for WPA2-PSK clients that support AES-CCMP only. A valid matching PSK is already configured. Which security adjustment resolves the displayed cipher mismatch?

| Field | Value |
| --- | --- |
| Security | WPA+WPA2 |
| WPA Policy | Disabled |
| WPA2 Policy | Enabled |
| WPA2 AES | Disabled |
| WPA2 TKIP | Enabled |
| Key management | PSK |

- **A.** Enable AES under WPA2 Policy and remove TKIP from the intended policy.
- **B.** Enable legacy WPA/TKIP while leaving WPA2 AES disabled.
- **C.** Change the SSID broadcast setting only.
- **D.** Replace PSK key management with 802.1X.

**Answer: A**

The authentication method and PSK already agree. The WLAN must offer the agreed AES-CCMP cipher rather than a TKIP-only policy.

**Option explanations**

- **A:** This supplies the cipher supported by the clients and required by the design.
- **B:** The intended AES-only clients still lack their required compatible cipher.
- **C:** SSID advertisement does not change the negotiated cipher.
- **D:** That changes authentication and does not meet the PSK requirement.

**Further reading**

- [Cisco Wireless Controller Configuration Guide, Release 8.10: WLAN Security](https://www.cisco.com/c/en/us/td/docs/wireless/controller/8-10/config-guide/b_cg810/wlan_security.html) — WPA1+WPA2; Configuring WPA1+WPA2 (GUI); Protected Management Frames

---

## CCNA2-086 · Security Fundamentals

Objectives: 5.6 · single · Challenge

The shown ACL is the only input ACL on a router’s user interface. A host sends UDP from source port 53000 to DNS server 192.0.2.53, destination port 53. Which statement explains the result?

```text
ip access-list extended DNS-ONLY
 10 permit udp any eq 53 host 192.0.2.53
 20 deny ip any any
```

- **A.** The packet is permitted because port 53 appears anywhere in the entry.
- **B.** The packet is denied because sequence 10 requires source port 53.
- **C.** The packet is denied because standard ACLs cannot match UDP.
- **D.** The packet is permitted because all DNS packets bypass interface ACLs.

**Answer: B**

The command places eq 53 immediately after the source, so it does not permit this client request. For the intended destination-port test, put eq 53 after the destination address.

**Option explanations**

- **A:** The position of a port operator determines whether it tests source or destination.
- **B:** The eq clause precedes the destination address and therefore tests the source port.
- **C:** This is an extended ACL; its field placement is the fault.
- **D:** DNS traffic is subject to ordinary ACL processing.

**Further reading**

- [Configure IP Access Lists](https://www.cisco.com/c/en/us/support/docs/security/ios-firewall/23602-confaccesslists.html) — ACL Concepts; Masks; Process ACLs; Apply ACLs; Extended ACLs

---

## CCNA2-087 · Security Fundamentals

Objectives: 5.6 · single · Applied

An applied standard IPv4 ACL contains only deny host 10.8.0.9. The requirement is to block that source and allow every other IPv4 source. Which additional entry, placed after the deny, completes the requirement?

- **A.** permit host 10.8.0.9
- **B.** permit any
- **C.** permit 10.8.0.9 0.0.0.0
- **D.** deny any

**Answer: B**

An ACL with a deny entry does not automatically permit everything else. The terminal implicit deny also blocks otherwise unmatched traffic.

**Option explanations**

- **A:** The earlier matching deny still blocks that host and others remain unmatched.
- **B:** All other sources need an explicit permit before the implicit deny.
- **C:** This is another host-only permit for the source already denied.
- **D:** This makes the existing implicit denial explicit without allowing other hosts.

**Further reading**

- [Configure IP Access Lists](https://www.cisco.com/c/en/us/support/docs/security/ios-firewall/23602-confaccesslists.html) — ACL Concepts; Masks; Process ACLs; Apply ACLs; Extended ACLs

---

## CCNA2-088 · Security Fundamentals

Objectives: 5.7 · single · Applied

An access port learned one sticky secure MAC address in its running configuration. Startup configuration still has no learned address, and no further hosts will connect. Which step preserves this learned restriction across a power cycle?

- **A.** Set the access VLAN to the native VLAN.
- **B.** Disable port security before the power cycle.
- **C.** Clear the dynamic MAC address table.
- **D.** Copy running-config to startup-config after confirming the learned address.

**Answer: D**

Sticky learning adds secure addresses to running configuration. Saving that configuration makes the approved learned entry available after restart.

**Option explanations**

- **A:** VLAN selection does not persist the learned configuration.
- **B:** Disabling enforcement does not preserve the intended restriction.
- **C:** Clearing ordinary forwarding entries does not save the configuration.
- **D:** The sticky entry is retained on reboot only if the configuration containing it is saved.

**Further reading**

- [Catalyst 3750-X and 3560-X Configuration Guide: Configuring Port-Based Traffic Control](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst3750x_3560x/software/release/15-0_2_se/configuration/guide/3750x_cg/swtrafc.html) — Secure MAC Addresses; Security Violations; Port Security Aging

---

## CCNA2-089 · Security Fundamentals

Objectives: 5.7 · multiple · Applied

DAI is active on VLAN 60, and the receiving port is untrusted. No ARP ACL overrides the DHCP snooping table. Which two ARP sender mappings would fail binding validation against the displayed entries? Select two. Ignore rate and optional validation checks.

| Bound IP | Bound MAC |
| --- | --- |
| 10.60.0.21 | 00:11:22:33:44:21 |
| 10.60.0.22 | 00:11:22:33:44:22 |

- **A.** 10.60.0.1 / 00:11:22:33:44:21
- **B.** 10.60.0.21 / 00:11:22:33:44:99
- **C.** 10.60.0.22 / 00:11:22:33:44:22
- **D.** 10.60.0.21 / 00:11:22:33:44:21

**Answer: A, B**

DAI uses authorized address bindings to reject forged ARP sender claims. Being a known MAC does not authorize that device to claim every IP address.

**Option explanations**

- **A:** The host’s MAC does not authorize it to claim the gateway IP.
- **B:** The claimed IP is bound to a different MAC.
- **C:** This pair agrees with the authorized binding.
- **D:** This IP and MAC exactly match a listed binding.

**Further reading**

- [Catalyst 3750-X and 3560-X Configuration Guide: Configuring Dynamic ARP Inspection](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst3750x_3560x/software/release/15-0_2_se/configuration/guide/3750x_cg/swdynarp.html) — Understanding Dynamic ARP Inspection; Rate Limiting; ARP ACLs

---

## CCNA2-090 · Security Fundamentals

Objectives: 5.4 · multiple · Applied

A help desk is evaluating a certificate-based login. Which two items must be present for the client to demonstrate the certificate identity cryptographically? Select two.

- **A.** A hostname whose text matches the user’s display name.
- **B.** A certificate acceptable to the relying system.
- **C.** The ability to prove possession of the corresponding private key.
- **D.** A printed copy of the public certificate only.

**Answer: B, C**

A certificate carries a public-key identity binding; it is not a secret by itself. Authentication also requires proof using the corresponding private key.

**Option explanations**

- **A:** A naming coincidence is not cryptographic proof of identity.
- **B:** The system must accept the certificate’s identity binding under its trust policy.
- **C:** A challenge or protocol signature demonstrates control of the private credential.
- **D:** A public certificate can be copied without possessing its private key.

**Further reading**

- [NIST SP 800-63B-4: Digital Identity Guidelines — Authentication and Authenticator Management](https://pages.nist.gov/800-63-4/sp800-63b.html) — Authentication factors; password verifiers; authenticator management

---

## CCNA2-091 · Automation and Programmability

Objectives: 6.1 · single · Applied

A weekly script collects switch software versions and compares them with an approved list. It sends a report without changing any device. Which network-management benefit does this workflow provide?

- **A.** Automatic installation of every available image
- **B.** Repeatable inventory and compliance checks
- **C.** Replacement of routing protocols with the script
- **D.** Removal of the need to approve software versions

**Answer: B**

Automation includes observation and verification as well as configuration changes. This workflow repeatedly compares actual software inventory with an approved baseline.

**Option explanations**

- **A:** The workflow is read-only and does not install software.
- **B:** Regular collection and comparison reduce manual audit work.
- **C:** Software inventory does not calculate packet routes.
- **D:** The script relies on an approved version list as an input.

**Further reading**

- [What Is Network Automation?](https://www.cisco.com/site/us/en/learn/topics/networking/what-is-network-automation.html) — Network automation; profiles and policies; automated lifecycle management

---

## CCNA2-092 · Automation and Programmability

Objectives: 6.2 · single · Applied

A company manages 60 switches separately and must translate the same access policy into commands on each switch. A controller-based replacement provides a supported network-wide policy service. What changes most directly for the operator?

- **A.** Each application must now calculate an Ethernet FCS
- **B.** IP forwarding must take place on the controller server
- **C.** All physical paths become point-to-point application APIs
- **D.** The operator can express common policy through the controller

**Answer: D**

A controller can provide a network-level policy interface and coordinate supported devices. This reduces the need to express the same intent independently on each switch.

**Option explanations**

- **A:** Frame error checking remains a data-link function.
- **B:** The switches can continue forwarding user traffic.
- **C:** Physical transport links do not become application interfaces.
- **D:** The controller provides a common management and policy abstraction.

**Further reading**

- [Software-Defined Networking (SDN) Definition](https://www.cisco.com/c/en/us/solutions/software-defined-networking/overview.html) — SDN elements; Features and benefits
- [RFC 7426: Software-Defined Networking (SDN): Layers and Architecture Terminology](https://www.rfc-editor.org/rfc/rfc7426.html) — 3.1 Overview; 3.2 Network Devices; 3.3 Control Plane; 3.5.3 Locality

---

## CCNA2-093 · Automation and Programmability

Objectives: 6.3 · single · Applied

Two fabric edge switches have valid overlay configuration but cannot reach one another’s tunnel endpoint IP addresses. The routed physical path is the only transport between them. Which dependency should the engineer restore first?

- **A.** Underlay IP reachability between the tunnel endpoints
- **B.** A direct cable between every pair of overlay endpoints
- **C.** The number of application users in each virtual network
- **D.** A unique physical switch for every virtual network

**Answer: A**

Overlay connectivity depends on the transport supplied by the underlay. A correct logical configuration cannot deliver encapsulated packets across a physical routed path that lacks reachability.

**Option explanations**

- **A:** The overlay packets need a functioning routed transport path.
- **B:** An overlay can cross intermediate underlay devices.
- **C:** User counts do not restore the missing transport reachability.
- **D:** Several overlays can share the same physical infrastructure.

**Further reading**

- [Software-Defined Access](https://www.cisco.com/c/en/us/td/docs/solutions/CVD/Campus/cisco-sda-design-guide.html) — SD-Access architecture; Underlay network; Overlay network; Overlay control plane – LISP; Data plane – VXLAN

---

## CCNA2-094 · Automation and Programmability

Objectives: 6.4 · single · Applied

A network analytics model learns each site’s normal latency by time of day. It flags a 25-ms observation at a normally 5-ms site, but accepts 25 ms at a site where that value is typical. What capability explains this behavior?

- **A.** A universal fixed threshold applied equally to both sites
- **B.** Generative creation of a new routing protocol
- **C.** Machine-learning-based anomaly detection using contextual baselines
- **D.** Encryption of the measured latency before comparison

**Answer: C**

Learned baselines let an analytics system evaluate a measurement in context. The same raw value can be ordinary at one site and unusual at another.

**Option explanations**

- **A:** A single identical latency threshold would not account for the different baselines.
- **B:** The model evaluates observations; it is not generating a protocol.
- **C:** The model compares observations with learned normal behavior for each site.
- **D:** Encryption protects data but does not supply behavioral context.

**Further reading**

- [What is AIOps?](https://developer.cisco.com/articles/what-is-aiops/) — The core components of AIOps; Is AIOps all you need?

---

## CCNA2-095 · Automation and Programmability

Objectives: 6.5 · multiple · Applied

An inventory API documents GET /devices as returning the device collection without requesting a configuration change. A dashboard needs to display that inventory. Which two statements apply? Select two.

- **A.** The dashboard should use the HTTP GET method
- **B.** The operation is Create in CRUD terminology
- **C.** The dashboard must send DELETE before reading
- **D.** The operation is Read in CRUD terminology
- **E.** GET requires a JSON body containing every existing device

**Answer: A, D**

The URI identifies the device collection, while GET requests its representation. This corresponds to Read in CRUD terminology.

**Option explanations**

- **A:** GET retrieves a representation of the target resource.
- **B:** Displaying an existing collection is a read operation.
- **C:** Deletion is unrelated to retrieving this inventory.
- **D:** The request obtains existing resource information.
- **E:** GET does not require such a body to identify this collection.

**Further reading**

- [RFC 9110: HTTP Semantics](https://www.rfc-editor.org/rfc/rfc9110.html) — 9 Methods; 15 Status Codes

---

## CCNA2-096 · Automation and Programmability

Objectives: 6.5 · single · Applied

A lab API accepts HTTP Basic authentication. A colleague says its Base64-encoded Authorization value encrypts the password, so HTTP is sufficient. Which correction is accurate?

- **A.** Base64 is a one-way password hash
- **B.** Basic encoding is reversible; HTTPS protects it during transport
- **C.** Basic authentication prevents all credential replay without TLS
- **D.** Switching the request body from JSON to XML encrypts the header

**Answer: B**

HTTP Basic encodes username/password credentials; the encoding itself does not keep them secret. Use a protected transport such as HTTPS and validate the server certificate.

**Option explanations**

- **A:** Base64 is a reversible representation, not a password hash.
- **B:** TLS provides transport confidentiality that Basic encoding does not.
- **C:** Captured Basic credentials can be reused; encoding does not prevent replay.
- **D:** Body encoding does not protect an authentication header.

**Further reading**

- [RFC 7617: The 'Basic' HTTP Authentication Scheme](https://www.rfc-editor.org/rfc/rfc7617.html) — 2 The Basic Authentication Scheme; 4 Security Considerations

---

## CCNA2-097 · Automation and Programmability

Objectives: 6.6 · single · Applied

An Ansible playbook targets the inventory group access_switches. The inventory excerpt is complete, and no additional host limit is used. Which devices are selected?

```text
[access_switches]
access-a
access-b

[wan_routers]
edge-r1
```

- **A.** All three devices because they share one inventory file
- **B.** Only edge-r1 because routers control switch access
- **C.** Only access-a because Ansible cannot target a group
- **D.** access-a and access-b

**Answer: D**

Inventory groups define collections of managed hosts. A play targeting access_switches selects its two listed members under the stated conditions.

**Option explanations**

- **A:** A play targets its selected group, not automatically the complete inventory.
- **B:** Device routing roles do not determine group membership.
- **C:** Inventory groups allow multiple managed hosts to be selected.
- **D:** Both hosts appear in the named access_switches group.

**Further reading**

- [How to build your inventory](https://docs.ansible.com/projects/ansible/latest/inventory_guide/intro_inventory.html) — Inventory basics: formats, hosts, and groups; Inventory setup examples

---

## CCNA2-098 · Automation and Programmability

Objectives: 6.6 · single · Applied

A Terraform configuration includes a DNS record and a virtual subnet managed through different services. What allows the same Terraform workflow to interact with both services?

- **A.** Providers implementing the relevant resource types and APIs
- **B.** An OSPF adjacency between Terraform and each service
- **C.** A requirement that both services run the same operating system
- **D.** A JSON file that removes the need for any API credentials

**Answer: A**

Terraform uses provider plugins to work with supported resource APIs. One configuration can use more than one provider to manage different kinds of infrastructure.

**Option explanations**

- **A:** Each provider translates supported resource operations into its service interface.
- **B:** Terraform providers are not routing protocol neighbors.
- **C:** API integrations do not require identical service operating systems.
- **D:** Configuration encoding does not replace provider access requirements.

**Further reading**

- [Providers](https://developer.hashicorp.com/terraform/language/providers) — What Providers Do; Provider Documentation
- [What is Terraform?](https://developer.hashicorp.com/terraform/intro) — How does Terraform work?; Manage any infrastructure; Track your infrastructure

---

## CCNA2-099 · Automation and Programmability

Objectives: 6.7 · single · Applied

A monitoring response is shown. Which value is the interface description, as distinct from the device name or interface identifier?

```text
{"device":"agg-3","interface":{"name":"Gi1/0/7","description":"uplink-to-core"}}
```

- **A.** Gi1/0/7
- **B.** agg-3
- **C.** uplink-to-core
- **D.** interface

**Answer: C**

The response contains an interface object nested inside the root object. Its description member holds uplink-to-core.

**Option explanations**

- **A:** This is the interface object’s name member.
- **B:** This is the outer device member.
- **C:** This string is the description member inside the interface object.
- **D:** This is a member name whose value is an object.

**Further reading**

- [RFC 8259: The JavaScript Object Notation (JSON) Data Interchange Format](https://www.rfc-editor.org/rfc/rfc8259.html) — 2 JSON Grammar; 3 Values; 4 Objects; 5 Arrays; 6 Numbers; 7 Strings

---

## CCNA2-100 · Automation and Programmability

Objectives: 6.7 · single · Foundation

An API rejects the JSON shown before it evaluates any network settings. Which edit makes this document valid JSON while preserving the intended Boolean value?

```text
{"enabled":True,"vlan":30}
```

- **A.** Put single quotes around every member name
- **B.** Change True to true
- **C.** Change the braces to square brackets
- **D.** Remove the comma between the members

**Answer: B**

JSON recognizes the literal true, not Python-style True. The quoted member names, numeric value and separating comma are otherwise valid.

**Option explanations**

- **A:** JSON member names require double-quoted strings.
- **B:** JSON’s Boolean literals are lowercase.
- **C:** The colon-separated members require an object structure.
- **D:** The comma is required to separate these object members.

**Further reading**

- [RFC 8259: The JavaScript Object Notation (JSON) Data Interchange Format](https://www.rfc-editor.org/rfc/rfc8259.html) — 2 JSON Grammar; 3 Values; 4 Objects; 5 Arrays; 6 Numbers; 7 Strings

---
