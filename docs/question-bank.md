# CCNA Practice — Set 01

100 original questions aligned to CCNA 200-301 v1.1. No interactive labs.

Answers and explanations follow each question. For an unrevealed attempt, use the Streamlit app.

Content review date: 2026-09-14.

## CCNA1-001 · Network Fundamentals

Objectives: 1.1.a, 1.1.b, 1.1.c, 1.1.d · matching · Foundation

Match each requirement to the component whose primary role fulfills it. Use each component once; assume the Layer 2 switch has no routing function.

1. Forward IP packets between two different IP subnets.
2. Forward Ethernet frames within a VLAN using a learned MAC address table.
3. Inspect traffic passing through the device and block a matching attack.
4. Provide an 802.11 radio connection for wireless endpoints.

- **A.** Inline intrusion prevention system (IPS)
- **B.** Router or Layer 3 switch with IP routing enabled
- **C.** Wireless access point
- **D.** Layer 2 switch

**Answer: 1 → B; 2 → D; 3 → A; 4 → C**

Identify the required function: inter-network forwarding, local Ethernet switching, attack prevention, or wireless access. A multifunction product may combine roles, but these are the distinct component roles being matched.

**Option explanations**

- **A:** Matches requirement 3: an inline IPS can inspect and block attack traffic.
- **B:** Matches requirement 1: either can route IP packets between subnets.
- **C:** Matches requirement 4: an AP provides the radio connection for Wi-Fi clients.
- **D:** Matches requirement 2: Ethernet switching uses learned MAC-to-port mappings.

**Further reading**

- [Networking Basics: What You Need To Know](https://www.cisco.com/site/us/en/learn/topics/small-business/networking-basics.html) — Switches; Routers; Access Points
- [What is an Intrusion Prevention System?](https://www.paloaltonetworks.com/cyberpedia/what-is-an-intrusion-prevention-system-ips) — How Intrusion Prevention Systems Work
- [Comparing Layer 3 and Layer 2 Switches](https://documentation.meraki.com/Switching/MS_-_Switches/Design_and_Configure/Configuration_Guides/Layer_3_Switching/Comparing_Layer_3_and_Layer_2_Switches) — Comparing Layer 3 and Layer 2 Switches (main article)

---

## CCNA1-002 · Network Fundamentals

Objectives: 1.2.a, 1.2.b, 1.2.c · single · Applied

An architect reviews the three designs in the exhibit. Which option correctly classifies all three?

| Design | Structure |
| --- | --- |
| X | Access switches uplink to a tier combining distribution and core roles. |
| Y | Access switches uplink to distribution switches; a separate core interconnects distribution blocks. |
| Z | Servers attach to leaves; every leaf connects to every spine. |

- **A.** X: three-tier campus; Y: two-tier campus; Z: spine-leaf
- **B.** X: two-tier campus; Y: spine-leaf; Z: three-tier campus
- **C.** X: two-tier campus; Y: three-tier campus; Z: spine-leaf
- **D.** X: spine-leaf; Y: three-tier campus; Z: two-tier collapsed-core campus

**Answer: C**

A two-tier campus combines distribution and core roles. A three-tier campus separates access, distribution, and core. In the basic spine-leaf design, every leaf connects to every spine.

**Option explanations**

- **A:** X combines distribution and core, whereas Y keeps them separate.
- **B:** Y has a separate campus core; Z describes complete leaf-to-spine connectivity.
- **C:** A collapsed core gives X two tiers; Y has three separate tiers; Z has leaf and spine tiers.
- **D:** X has a collapsed campus core; Z is identified by every leaf connecting to every spine.

**Further reading**

- [Campus LAN and Wireless LAN Solution Design Guide](https://www.cisco.com/c/en/us/td/docs/solutions/CVD/Campus/cisco-campus-lan-wlan-design-guide.html) — Hierarchical design model; Two-tier design; Three-tier design
- [Cisco Massively Scalable Data Center Network Fabric Design and Operation White Paper](https://www.cisco.com/c/en/us/products/collateral/switches/nexus-9000-series-switches/white-paper-c11-743245.html) — MSDC Layer 3 IP fabric design evolution; Cisco MSDC design example 1: Two-tiered spine-leaf topology

---

## CCNA1-003 · Network Fundamentals

Objectives: 1.1.h · single · Applied

A PoE switch has 120 W available for powered devices. It has already reserved 15 W for each of four phones. Every new AP requires a 30 W reservation at the switch, within the per-port limit. No reservations can be reduced. How many APs can receive their full requested allocation?

- **A.** 1
- **B.** 2
- **C.** 3
- **D.** 4

**Answer: B**

Power admission depends on the unallocated system budget as well as the per-port capability. The phones leave 60 W, sufficient for two 30 W AP reservations.

**Option explanations**

- **A:** Two 30 W allocations fit in the remaining budget.
- **B:** 120 − (4 × 15) = 60 W; 60 ÷ 30 = 2.
- **C:** Three APs would require 90 W beyond the 60 W already reserved.
- **D:** This ignores the 60 W reserved for the phones.

**Further reading**

- [Interface and Hardware Components Configuration Guide, Cisco IOS XE 17.14.x (Catalyst 9200 Switches): Configuring Power over Ethernet](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst9200/software/release/17-14/configuration_guide/int_hw/b_1714_int_and_hw_9200_cg/configuring_poe.html) — Powered-Device Detection and Initial Power Allocation

---

## CCNA1-004 · Network Fundamentals

Objectives: 1.3.a · single · Applied

Two buildings need a direct 10 Gb/s Ethernet link over a 2 km cable route. No intermediate equipment is permitted. Both switches support the listed modules, and the installed optical path will meet the selected modules’ loss budget. Which media and optic combination supports this distance?

- **A.** 10GBASE-SR optics with OM3 multimode fiber
- **B.** 10GBASE-SR optics with OM4 multimode fiber
- **C.** 10GBASE-T SFP+ modules with a 2 km copper cable
- **D.** 10GBASE-LR optics with compatible single-mode fiber

**Answer: D**

Use single-mode fiber with matching LR optics at both ends. SR multimode and copper alternatives cannot span the stated route at 10 Gb/s.

**Option explanations**

- **A:** The cited SR module supports up to 300 m on OM3, short of 2 km.
- **B:** The cited SR module supports up to 400 m on OM4, short of 2 km.
- **C:** Copper Ethernet reach does not support this uninterrupted 2 km span.
- **D:** LR supports a 10 km single-mode link, subject to the stated optical budget.

**Further reading**

- [Cisco 10GBASE SFP+ Modules Data Sheet](https://www.cisco.com/c/en/us/products/collateral/interfaces-modules/transceiver-modules/data_sheet_c78-455693.html) — Cisco SFP-10G-SR module; Cisco SFP-10G-LR module; Cisco SFP-10G-T-X module

---

## CCNA1-005 · Network Fundamentals

Objectives: 1.4, 1.3.b · single · Applied

Two switch ports are directly connected by a point-to-point 100BASE-TX link. Both remain up, but throughput degrades under bidirectional load. The exhibit summarizes their verified operational settings. Which issue is established by these settings?

| Endpoint | Operational speed | Operational duplex |
| --- | --- | --- |
| SW1 FastEthernet0/1 | 100 Mb/s | Full |
| SW2 FastEthernet0/1 | 100 Mb/s | Half |

- **A.** Duplex mismatch
- **B.** Speed mismatch
- **C.** Normal contention on a correctly configured shared hub segment
- **D.** An incorrect IPv4 subnet mask

**Answer: A**

The two endpoints agree on speed but disagree on duplex. A link can remain up with this mismatch; the half-duplex endpoint follows contention rules while the full-duplex endpoint can transmit and receive simultaneously.

**Option explanations**

- **A:** One endpoint uses full duplex while its peer uses half duplex.
- **B:** Both endpoints operate at the same 100 Mb/s speed.
- **C:** There is no hub in the stated point-to-point connection, and the duplex modes disagree.
- **D:** A subnet mask cannot explain the differing Ethernet duplex settings.

**Further reading**

- [Configure and Verify Ethernet 10/100/1000Mb Half/Full Duplex Auto-Negotiation](https://www.cisco.com/c/en/us/support/docs/lan-switching/ethernet/10561-3.html) — Background Information; Auto-Negotiation on Catalyst Switches that Run Cisco IOS Software

---

## CCNA1-006 · Network Fundamentals

Objectives: 1.5 · single · Foundation

An application needs its transport protocol to recover lost data and deliver a byte stream to the receiver in order. Which statement correctly compares TCP and UDP for this requirement?

- **A.** UDP satisfies the requirement because its checksum retransmits missing datagrams
- **B.** Both protocols provide the same delivery and ordering guarantees
- **C.** TCP provides these transport services; an application using UDP would need additional mechanisms
- **D.** TCP provides reliability only if the application assigns sequence numbers

**Answer: C**

TCP detects loss and uses retransmission while presenting an ordered byte stream. UDP can support applications that add reliability themselves, but UDP alone does not supply these guarantees.

**Option explanations**

- **A:** A checksum can detect corruption; it does not provide UDP retransmission.
- **B:** UDP does not itself provide reliable, ordered delivery.
- **C:** TCP supplies ordered delivery and retransmission; UDP leaves those services to other mechanisms.
- **D:** TCP maintains its own sequence numbers for its byte stream.

**Further reading**

- [RFC 9293: Transmission Control Protocol (TCP)](https://www.rfc-editor.org/rfc/rfc9293.html#section-2.2) — 2.2. Key TCP Concepts
- [RFC 768: User Datagram Protocol](https://www.rfc-editor.org/rfc/rfc768) — Introduction; Fields

---

## CCNA1-007 · Network Fundamentals

Objectives: 1.6 · single · Applied

An interface is assigned 172.22.14.173/27. What are its subnet address and directed broadcast address?

- **A.** 172.22.14.128 and 172.22.14.191
- **B.** 172.22.14.160 and 172.22.14.190
- **C.** 172.22.14.172 and 172.22.14.175
- **D.** 172.22.14.160 and 172.22.14.191

**Answer: D**

The mask is 255.255.255.224. The containing block starts at 160 and ends at 191; usable host addresses run from 161 through 190.

**Option explanations**

- **A:** Those boundaries describe a /26 block, not this /27.
- **B:** The subnet is correct, but .190 is the last usable host.
- **C:** Those boundaries describe the containing /30 block.
- **D:** A /27 has blocks of 32 addresses; .173 lies in .160–.191.

**Further reading**

- [Configure IP Addresses and Unique Subnets for New Users](https://www.cisco.com/c/en/us/support/docs/ip/routing-information-protocol-rip/13788-3.html) — Network Masks; Understand Subnetting; VLSM Example

---

## CCNA1-008 · Network Fundamentals

Objectives: 1.6 · single · Challenge

In 192.168.50.0/24, the subnets in the exhibit are already allocated. A new VLAN needs 28 usable host addresses. Choose the smallest suitable subnet at the lowest available address boundary that does not overlap an existing allocation.

| Existing VLAN | Allocated subnet |
| --- | --- |
| 10 | 192.168.50.0/26 |
| 20 | 192.168.50.64/28 |
| 30 | 192.168.50.80/28 |

- **A.** 192.168.50.96/27
- **B.** 192.168.50.80/27
- **C.** 192.168.50.96/28
- **D.** 192.168.50.128/26

**Answer: A**

Five host bits provide 2^5 − 2 = 30 usable addresses, so /27 is sufficient. Existing allocations occupy .0–.95, making .96/27 the first free aligned /27.

**Option explanations**

- **A:** The .96–.127 block is free and supplies 30 usable addresses.
- **B:** A /27 boundary is a multiple of 32; .80 belongs to .64/27, which overlaps an allocation.
- **C:** A /28 supplies only 14 usable addresses.
- **D:** It fits, but is larger than necessary and starts above an available suitable block.

**Further reading**

- [Configure IP Addresses and Unique Subnets for New Users](https://www.cisco.com/c/en/us/support/docs/ip/routing-information-protocol-rip/13788-3.html) — Network Masks; Understand Subnetting; VLSM Example

---

## CCNA1-009 · Network Fundamentals

Objectives: 1.7 · multiple · Foundation

Which TWO addresses belong to RFC 1918 private IPv4 space? Select two.

- **A.** 172.31.250.7
- **B.** 172.32.0.7
- **C.** 192.169.1.7
- **D.** 10.255.8.9
- **E.** 169.254.10.7

**Answer: A, D**

RFC 1918 defines 10.0.0.0/8, 172.16.0.0/12, and 192.168.0.0/16. Membership depends on the entire prefix, not just an address looking familiar.

**Option explanations**

- **A:** It falls within 172.16.0.0/12, whose second octet ranges from 16 through 31.
- **B:** The second octet is outside the private 172.16–172.31 range.
- **C:** RFC 1918 reserves 192.168.0.0/16, not all of 192.0.0.0/8.
- **D:** All addresses in 10.0.0.0/8 are private.
- **E:** IPv4 link-local space is distinct from RFC 1918 private space.

**Further reading**

- [RFC 1918: Address Allocation for Private Internets](https://www.rfc-editor.org/rfc/rfc1918#section-3) — 3. Private Address Space

---

## CCNA1-010 · Network Fundamentals

Objectives: 1.8 · single · Challenge

A site receives 2001:db8:7a00:a3f0::/60 and assigns one /64 to each VLAN. How many /64 subnets fit, and what is the last /64 prefix in this allocation?

- **A.** 4 subnets; 2001:db8:7a00:a3f3::/64
- **B.** 16 subnets; 2001:db8:7a00:a3ff::/64
- **C.** 16 subnets; 2001:db8:7a00:a400::/64
- **D.** 256 subnets; 2001:db8:7a00:a4ef::/64

**Answer: B**

The subnet count is 2^(64 − 60) = 16. The first three digits of the fourth hextet remain a3f; its last digit yields prefixes a3f0 through a3ff.

**Option explanations**

- **A:** Four additional prefix bits create 16 combinations, not four.
- **B:** The low hexadecimal digit of the fourth hextet varies from 0 through f.
- **C:** a400 lies outside the /60 whose fourth hextet begins a3f.
- **D:** A /60-to-/64 split adds four bits, not eight.

**Further reading**

- [RFC 4291: IP Version 6 Addressing Architecture](https://www.rfc-editor.org/rfc/rfc4291#section-2.3) — 2.3. Text Representation of Address Prefixes; 2.4. Address Type Identification; 2.5.6. Link-Local IPv6 Unicast Addresses; 2.7. Multicast Addresses

---

## CCNA1-011 · Network Fundamentals

Objectives: 1.9.d · single · Challenge

An Ethernet interface explicitly uses modified EUI-64 to form its IPv6 interface identifier from MAC address 3C-52-82-AB-10-FE. What 64-bit interface identifier results?

- **A.** 3c52:82ff:feab:10fe
- **B.** 3d52:82ff:feab:10fe
- **C.** 3e52:82ff:feab:10fe
- **D.** 3e52:82ff:ffab:10fe

**Answer: C**

Insert FF-FE between the third and fourth MAC octets, then invert the U/L bit in the first octet. The bytes become 3E-52-82-FF-FE-AB-10-FE. This question specifies EUI-64; IPv6 interfaces can use other identifier-generation methods.

**Option explanations**

- **A:** This inserts ff:fe but leaves the U/L bit unchanged.
- **B:** This changes the low-order bit instead of the U/L bit.
- **C:** Insert ff:fe in the middle and XOR the first byte 3c with 02 to obtain 3e.
- **D:** The inserted bytes must be ff:fe, not ff:ff.

**Further reading**

- [RFC 2464: Transmission of IPv6 Packets over Ethernet Networks](https://datatracker.ietf.org/doc/html/rfc2464#section-4) — 4. Stateless Autoconfiguration

---

## CCNA1-012 · Network Fundamentals

Objectives: 1.9.a, 1.9.c · multiple · Applied

Which THREE IPv6 address classifications are correct? Select three.

- **A.** 2001:4860:1234::8 is link-local unicast
- **B.** fd12:3456:789a:1::8 is unique local unicast
- **C.** fe80::8 is link-local unicast
- **D.** ff02::1 is global unicast
- **E.** ff02::2 is multicast

**Answer: B, C, E**

The prefixes distinguish unique local, link-local, and multicast addresses. Unique local addresses can be routed within an organization, whereas link-local unicast addresses remain on their local link.

**Option explanations**

- **A:** This is global unicast space; link-local unicast begins with fe80::/10.
- **B:** The fd prefix identifies the locally assigned part of fc00::/7.
- **C:** It is in the link-local unicast prefix and is confined to its link.
- **D:** An address beginning ff is multicast; the scope here is link-local.
- **E:** The ff prefix identifies multicast, and ff02::2 is the link-local all-routers group.

**Further reading**

- [RFC 4291: IP Version 6 Addressing Architecture](https://www.rfc-editor.org/rfc/rfc4291#section-2.3) — 2.3. Text Representation of Address Prefixes; 2.4. Address Type Identification; 2.5.6. Link-Local IPv6 Unicast Addresses; 2.7. Multicast Addresses
- [RFC 4193: Unique Local IPv6 Unicast Addresses](https://www.rfc-editor.org/rfc/rfc4193#section-3.1) — 1. Introduction; 3.1. Format

---

## CCNA1-013 · Network Fundamentals

Objectives: 1.9.b · single · Applied

Two service nodes at different sites advertise reachability to the same IPv6 anycast service address. Routing has converged, and a client sends one packet to that address. What does anycast provide?

- **A.** Delivery toward one service node according to the routing system’s selected path
- **B.** A copy of the packet delivered to both service nodes
- **C.** Delivery to the physically closest service node regardless of routing policy
- **D.** Delivery to the node with the lowest application response time, measured by anycast itself

**Answer: A**

Anycast presents the same service address from multiple locations. The network routes a packet toward one instance; its choice follows routing information and policy rather than an inherent geographic or application-latency measurement.

**Option explanations**

- **A:** Routing selects a path to one instance of the shared service address.
- **B:** That describes group delivery, not anycast.
- **C:** Routing preference does not necessarily correspond to geographic distance.
- **D:** Anycast does not inherently measure application response time.

**Further reading**

- [RFC 4786: Operation of Anycast Services](https://www.rfc-editor.org/rfc/rfc4786#section-2) — 2. Terminology; 3.1. General Description; 3.2. Goals

---

## CCNA1-014 · Network Fundamentals

Objectives: 1.10, 1.6 · single · Applied

A Windows client has the displayed configuration. Its VLAN uses 10.44.8.64/26, and the router interface serving that VLAN is 10.44.8.65. The client has no other adapter or manually added route. Which single client setting should be corrected to use that router for remote networks?

```text
C:\> ipconfig /all

Ethernet adapter Ethernet:
   IPv4 Address. . . . . . . . . . . : 10.44.8.70
   Subnet Mask . . . . . . . . . . . : 255.255.255.192
   Default Gateway . . . . . . . . . : 10.44.8.1
   DNS Servers . . . . . . . . . . . : 10.44.8.90
```

- **A.** Change the IPv4 address to 10.44.8.64
- **B.** Change the default gateway to 10.44.8.65
- **C.** Change the subnet mask to 255.255.255.0
- **D.** Change the DNS server to 10.44.8.65

**Answer: B**

The address and mask match the VLAN, but the configured gateway .1 does not. Set the default gateway to the stated router interface .65.

**Option explanations**

- **A:** That is the VLAN subnet address, not a usable host address.
- **B:** It is the stated router interface and lies in the client’s .64–.127 subnet.
- **C:** The configured /26 matches the VLAN design; widening it would misidentify remote addresses as local.
- **D:** Changing name resolution does not correct the default gateway.

**Further reading**

- [ipconfig](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/ipconfig) — Syntax; Parameters (/all)
- [Configure IP Addresses and Unique Subnets for New Users](https://www.cisco.com/c/en/us/support/docs/ip/routing-information-protocol-rip/13788-3.html) — Network Masks; Understand Subnetting; VLSM Example

---

## CCNA1-015 · Network Fundamentals

Objectives: 1.11.a, 1.11.c · single · Applied

Three nearby APs must operate in the 2.4 GHz band with 20 MHz channels under the usual United States channel plan. Which assignment uses three mutually nonoverlapping channels?

- **A.** Channels 1, 2, and 3
- **B.** Channels 1, 5, and 6
- **C.** Channels 3, 6, and 9
- **D.** Channels 1, 6, and 11

**Answer: D**

Channel numbers are spaced more closely than each channel’s occupied width. Using 1, 6, and 11 avoids overlap among these three AP channels; it does not eliminate interference from other transmitters.

**Option explanations**

- **A:** Adjacent numbered channels overlap substantially.
- **B:** Channels 5 and 6 overlap.
- **C:** These channel centers are too close for three nonoverlapping 20 MHz channels.
- **D:** These are the conventional three nonoverlapping 2.4 GHz channels in this plan.

**Further reading**

- [Channel Planning Best Practices](https://documentation.meraki.com/Wireless/Design_and_Configure/Architecture_and_Best_Practices/Channel_Planning_Best_Practices) — 2.4 GHz

---

## CCNA1-016 · Network Fundamentals

Objectives: 1.11.b, 1.11.d · multiple · Foundation

An administrator proposes hiding an SSID as a substitute for WPA2-Personal with AES-CCMP. Which TWO statements correctly distinguish these measures? Select two.

- **A.** Hiding the SSID does not provide encryption for user data
- **B.** A hidden SSID guarantees that radio observers cannot discover the network name
- **C.** WPA2-Personal with AES-CCMP provides protection for wireless user-data confidentiality
- **D.** Selecting a different RF channel performs the same cryptographic function as AES-CCMP
- **E.** Once an SSID is hidden, compatible clients need no authentication configuration

**Answer: A, C**

SSID hiding changes how a network is advertised. It cannot replace the authentication and encryption configured for the WLAN.

**Option explanations**

- **A:** SSID visibility is distinct from encrypting the wireless link.
- **B:** The name can still be discovered through wireless traffic.
- **C:** AES-CCMP protects transmitted data after the security association is established.
- **D:** Channel selection determines frequency use, not encryption.
- **E:** Hiding a name does not replace the configured authentication requirements.

**Further reading**

- [Wireless Fundamentals: Encryption and Authentication](https://documentation.meraki.com/Wireless/Design_and_Configure/Architecture_and_Best_Practices/Wireless_Fundamentals:_Encryption_and_Authentication) — WPA2 – Personal; Hidden SSID

---

## CCNA1-017 · Network Fundamentals

Objectives: 1.12 · multiple · Applied

A design uses conventional virtual machines, Linux process containers inside one VM, and separate VRFs on a router for two tenants. The tenants use overlapping IPv4 prefixes; there is no route leaking or external interconnection. Which THREE statements correctly describe these technologies? Select three.

- **A.** Each conventional VM has its own guest operating-system kernel
- **B.** The Linux process containers inside one VM share that VM’s kernel
- **C.** The two VRFs maintain separate routing and forwarding tables for the overlapping prefixes
- **D.** A VRF resolves address overlap by automatically performing NAT
- **E.** Each Linux process container must boot another complete guest kernel

**Answer: A, B, C**

VMs virtualize machines; process containers isolate applications using a shared kernel; VRFs isolate Layer 3 forwarding contexts. These mechanisms can coexist because they isolate different resources.

**Option explanations**

- **A:** VMs provide separate guest OS instances, even when sharing physical hardware.
- **B:** These containers isolate processes within their host guest OS.
- **C:** The ingress interface’s VRF distinguishes the routing contexts.
- **D:** VRFs separate forwarding contexts; they do not inherently translate addresses.
- **E:** Ordinary process containers share their host kernel rather than booting independent kernels.

**Further reading**

- [What is a container?](https://docs.docker.com/get-started/docker-concepts/the-basics/what-is-a-container/#containers-versus-virtual-machines-vms) — Containers versus virtual machines (VMs)
- [IP Routing Configuration Guide, Cisco IOS XE Dublin 17.12.x (Catalyst 9500 Switches): Configuring VRF-lite](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst9500/software/release/17-12/configuration_guide/rtng/b_1712_rtng_9500_cg/configuring_vrf_lite.html) — Information About VRF-lite; Guidelines for Configuring VRF-lite

---

## CCNA1-018 · Network Fundamentals

Objectives: 1.1.c, 1.1.e, 1.1.f, 1.1.g · single · Applied

The exhibit describes four components in an office network. Which option identifies their roles correctly? Classify Y by its role as an end-user device, and Z by the service it provides.

| Component | Observed function |
| --- | --- |
| W | Centrally manages WLAN policies for a group of access points. |
| X | Applies stateful traffic rules, identifies applications, and provides integrated IPS. |
| Y | An employee laptop whose browser requests an HR page. |
| Z | A host that accepts the HTTP request and returns the HR page. |

- **A.** W: access point; X: basic Layer 2 switch; Y: endpoint; Z: server
- **B.** W: wireless controller; X: NGFW; Y: server; Z: client endpoint
- **C.** W: wireless controller; X: basic router; Y: endpoint; Z: access point
- **D.** W: wireless controller; X: NGFW; Y: endpoint; Z: server

**Answer: D**

Controllers centrally manage wireless policies. NGFWs combine stateful filtering with application awareness and intrusion prevention. The laptop is an end-user endpoint; the host answering its application requests serves as a server.

**Option explanations**

- **A:** W centrally manages AP policies; X performs application-aware security inspection.
- **B:** Y initiates the user’s request, while Z provides the requested service.
- **C:** X adds application awareness and IPS; Z is an application server.
- **D:** These roles match centralized wireless management, integrated security, user access, and service delivery.

**Further reading**

- [Campus LAN and Wireless LAN Solution Design Guide](https://www.cisco.com/c/en/us/td/docs/solutions/CVD/Campus/cisco-campus-lan-wlan-design-guide.html) — Centralized (local-mode) design model
- [What is a next-generation firewall (NGFW)?](https://www.cisco.com/site/us/en/learn/topics/security/what-is-a-next-generation-firewall.html) — Next-generation firewall overview
- [RFC 9110: HTTP Semantics](https://www.rfc-editor.org/rfc/rfc9110.html#section-3.3) — 3.3. Connections, Clients, and Servers

---

## CCNA1-019 · Network Fundamentals

Objectives: 1.13.a, 1.13.b, 1.13.c, 1.13.d · single · Applied

A switch’s only MAC entry was learned dynamically for 0066.7788.9900 on Gi1/0/3. Its aging timer is explicitly 300 seconds. No further frames arrive for 600 seconds, and no topology changes occur. The listed ports are its only active ports, all are forwarding, and no filtering features are enabled. A frame from 0011.2233.4455 to 0066.7788.9900 now enters Gi1/0/1. What does the switch do?

| Port | Access VLAN |
| --- | --- |
| Gi1/0/1 | 10 |
| Gi1/0/2 | 10 |
| Gi1/0/3 | 10 |
| Gi1/0/4 | 20 |

- **A.** Learn 0011.2233.4455 on Gi1/0/1 in VLAN 10; transmit copies on Gi1/0/2 and Gi1/0/3
- **B.** Learn 0066.7788.9900 on Gi1/0/1; transmit copies on Gi1/0/2 and Gi1/0/3
- **C.** Learn 0011.2233.4455 on Gi1/0/1; transmit copies on all four ports
- **D.** Learn 0011.2233.4455 on Gi1/0/1; transmit only on Gi1/0/3 using the old destination mapping

**Answer: A**

The expired dynamic mapping no longer supplies an output port. The switch learns the new source on ingress and floods the unknown destination through the other eligible VLAN 10 ports.

**Option explanations**

- **A:** The source is learned on ingress, and the unknown destination is flooded within VLAN 10.
- **B:** Learning uses the source MAC, not the destination MAC.
- **C:** Flooding excludes ingress and does not cross into VLAN 20.
- **D:** The unused dynamic destination entry has aged out after the specified interval.

**Further reading**

- [Configuring MAC Address Tables](https://www.cisco.com/c/en/us/td/docs/switches/datacenter/nexus5500/sw/layer2/7x/b_5500_Layer2_Config_7x/config_mac_address_tables.pdf) — Information About MAC Addresses (page 1); Configuring the Aging Time for the MAC Table (page 2)

---

## CCNA1-020 · Network Fundamentals

Objectives: 1.2.d, 1.2.e, 1.2.f · matching · Applied

Match each description to the term that characterizes the stated aspect of the design. Use each term once. Scope, office size, and hosting model describe different aspects, so one real network can have several of these characteristics.

1. Network scope: a carrier service interconnects the company’s LANs in three different cities.
2. Hosting model: the organization buys and maintains fixed servers in its own equipment room, with no cloud service layer.
3. Hosting model: an external provider offers pooled computing capacity to the general public, with on-demand provisioning, elastic scaling, and metered usage.
4. Office environment: a home-based business connects four employee devices and a printer through a compact local network with Internet access.

- **A.** Public cloud computing
- **B.** Small office/home office (SOHO) network
- **C.** Wide-area network (WAN)
- **D.** Traditional on-premises hosting

**Answer: 1 → C; 2 → D; 3 → A; 4 → B**

WAN describes connectivity among geographically separated networks. SOHO describes a small office environment. Hosting can use locally operated infrastructure or cloud services; public cloud capacity is delivered from a provider’s pooled resources.

**Option explanations**

- **A:** Matches 3: the customer provisions elastic resources from an external provider’s shared infrastructure.
- **B:** Matches 4: this describes a compact office network supporting a small number of users.
- **C:** Matches 1: the connection interconnects site networks across cities.
- **D:** Matches 2: the organization operates its fixed server infrastructure at its own premises.

**Further reading**

- [What is a WAN (wide-area network)?](https://www.cisco.com/site/us/en/learn/topics/networking/what-is-a-wan-wide-area-network.html) — What is a WAN (wide-area network)?; What is a WAN router?
- [How do I set up a small business network?](https://www.cisco.com/site/us/en/learn/topics/small-business/how-to-set-up-a-network.html) — Introduction; What is a switch?; What is a router?
- [NIST SP 800-145: The NIST Definition of Cloud Computing](https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-145.pdf) — 2. The NIST Definition of Cloud Computing — Essential Characteristics; Deployment Models

---

## CCNA1-021 · Network Access

Objectives: 2.1.a · single · Applied

A Cisco IP phone connects to Gi1/0/12, and a PC connects through the phone. The phone has learned voice VLAN 120 through CDP. The PC sends untagged frames. With the configuration shown, how does the switch classify their traffic?

```text
interface GigabitEthernet1/0/12
 switchport mode access
 switchport access vlan 20
 switchport voice vlan 120
```

- **A.** Both devices use VLAN 20.
- **B.** PC data uses VLAN 20; tagged phone voice uses VLAN 120.
- **C.** PC data uses VLAN 120; phone voice uses VLAN 20.
- **D.** Neither device can communicate until this port becomes a trunk.

**Answer: B**

The access and voice VLAN commands serve different traffic on the same physical access port. Untagged PC frames enter VLAN 20; the phone supplies a VLAN 120 tag for voice.

**Option explanations**

- **A:** The voice VLAN setting gives the phone a separate tagged VLAN.
- **B:** The access VLAN classifies untagged PC data, while the phone tags voice for VLAN 120.
- **C:** This reverses the configured access and voice assignments.
- **D:** An access port with a voice VLAN supports this phone-and-PC arrangement.

**Further reading**

- [VLAN Configuration Guide, Cisco IOS XE 17.15.x — Configuring Voice VLANs](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst9300/software/release/17-15/configuration_guide/vlan/b_1715_vlan_9300_cg/configuring_voice_vlans.html) — Cisco IP Phone Voice Traffic; Cisco IP Phone Data Traffic

---

## CCNA1-022 · Network Access

Objectives: 2.1.b, 2.1.a · single · Applied

On a Catalyst switch, Gi1/0/8 is an access port explicitly assigned to VLAN 30. An administrator deletes VLAN 30 from the local VLAN database without changing the interface configuration. What happens to that port?

- **A.** It automatically returns to VLAN 1.
- **B.** It becomes a trunk using native VLAN 1.
- **C.** It continues forwarding in VLAN 30 until the switch restarts.
- **D.** It remains assigned to VLAN 30 and becomes inactive.

**Answer: D**

VLAN 1 is the default Ethernet VLAN, but it is not an automatic fallback when an explicitly assigned VLAN is deleted. The port keeps its VLAN 30 assignment and cannot forward normally in that absent VLAN.

**Option explanations**

- **A:** Deletion does not reset an explicit access VLAN assignment.
- **B:** Deleting a VLAN does not change the port mode.
- **C:** A deleted VLAN is not available for normal forwarding.
- **D:** The assignment persists; restoring the VLAN or assigning another existing VLAN restores its VLAN membership.

**Further reading**

- [VLAN Configuration Guide, Cisco IOS XE 17.15.x — Configuring VLANs](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst9300/software/release/17-15/configuration_guide/vlan/b_1715_vlan_9300_cg/configuring_vlans.html) — Supported VLANs; Deleting a VLAN; VLAN Port Membership Modes

---

## CCNA1-023 · Network Access

Objectives: 2.1.c, 2.2.b · single · Challenge

R1 routes between VLANs 10 and 20 through an 802.1Q trunk. Both VLANs are active and permitted on the switch trunk; neither is native. Hosts use the shown subinterface addresses as their gateways. The physical link is up, and no ACLs apply. VLAN 10 hosts reach their gateway; VLAN 20 hosts cannot. Which change corrects the configuration?

```text
interface GigabitEthernet0/0
 no ip address
 no shutdown
!
interface GigabitEthernet0/0.10
 encapsulation dot1Q 10
 ip address 192.0.2.1 255.255.255.128
!
interface GigabitEthernet0/0.20
 encapsulation dot1Q 200
 ip address 192.0.2.129 255.255.255.128
```

- **A.** Change Gi0/0.20 to encapsulation dot1Q 20.
- **B.** Add a static route to 192.0.2.128/25 through Gi0/0.10.
- **C.** Change Gi0/0.10 to encapsulation dot1Q 20.
- **D.** Configure the switch trunk with native VLAN 20.

**Answer: A**

Subinterface numbers are labels; the encapsulation command selects the actual VLAN tag. Binding Gi0/0.20 to VLAN 20 makes its 192.0.2.129/25 gateway reachable from that VLAN.

**Option explanations**

- **A:** The VLAN 20 gateway is currently bound to tag 200 instead of tag 20.
- **B:** Routing cannot repair the wrong incoming VLAN classification; this subnet is already assigned locally.
- **C:** That would misassign the working VLAN 10 gateway and leave Gi0/0.20 wrong.
- **D:** The design explicitly uses tagged VLAN 20; its router subinterface still expects VLAN 200.

**Further reading**

- [Configure Inter VLAN Routing with the Use of an External Router](https://www.cisco.com/c/en/us/support/docs/lan-switching/inter-vlan-routing/14976-50.html) — Configure — Configurations; Sample Command Output — Cisco Router

---

## CCNA1-024 · Network Access

Objectives: 2.2.a · single · Applied

SW1 and SW2 have a working trunk. VLANs 10, 20, and 30 exist on both switches and are forwarding wherever permitted. SW1 allows all three; SW2 has the configuration shown. Which interface command on SW2 restores VLAN 30 connectivity while preserving the currently allowed VLANs?

```text
interface GigabitEthernet1/0/48
 switchport mode trunk
 switchport trunk allowed vlan 10,20
```

- **A.** switchport access vlan 30
- **B.** switchport trunk native vlan 30
- **C.** switchport trunk allowed vlan add 30
- **D.** switchport trunk allowed vlan 30

**Answer: C**

VLAN existence and trunk admission are separate requirements. The add form permits VLAN 30 without replacing the existing allowed list.

**Option explanations**

- **A:** The access VLAN setting does not add traffic to an operational trunk.
- **B:** Changing the native VLAN does not add VLAN 30 to the allowed list.
- **C:** The add keyword extends the current list to 10,20,30.
- **D:** Without add, this replaces the list and removes VLANs 10 and 20.

**Further reading**

- [VLAN Configuration Guide, Cisco IOS XE 17.15.x — Configuring VLAN Trunks](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst9300/software/release/17-15/configuration_guide/vlan/b_1715_vlan_9300_cg/configuring_vlan_trunks.html) — Allowed VLANs on a Trunk; Configuring the Native VLAN for Untagged Traffic
- [VLAN Configuration Guide, Cisco IOS XE 17.15.x — Configuring VLANs](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst9300/software/release/17-15/configuration_guide/vlan/b_1715_vlan_9300_cg/configuring_vlans.html) — Supported VLANs; Deleting a VLAN; VLAN Port Membership Modes

---

## CCNA1-025 · Network Access

Objectives: 2.2.b, 2.2.c · single · Applied

An 802.1Q trunk has native VLAN 99 at both ends, and native-VLAN tagging is disabled. VLANs 10 and 99 are allowed and forwarding. Which describes ordinary data frames transmitted on this trunk?

- **A.** VLAN 10 frames are untagged; VLAN 99 frames carry tag 99.
- **B.** VLAN 10 frames carry tag 10; VLAN 99 frames are untagged.
- **C.** All frames are untagged because both native VLAN settings match.
- **D.** All frames carry tags because the port is a trunk.

**Answer: B**

802.1Q identifies nonnative VLAN traffic with a tag. With native tagging disabled, ordinary VLAN 99 traffic leaves untagged and is classified into native VLAN 99 at the other end.

**Option explanations**

- **A:** This reverses native and nonnative handling.
- **B:** Nonnative data is tagged, while native-VLAN data is untagged under the stated setting.
- **C:** A matching native VLAN does not remove tags from other VLANs.
- **D:** The stated native-VLAN setting provides the untagged exception.

**Further reading**

- [VLAN Configuration Guide, Cisco IOS XE 17.15.x — Configuring VLAN Trunks](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst9300/software/release/17-15/configuration_guide/vlan/b_1715_vlan_9300_cg/configuring_vlan_trunks.html) — Allowed VLANs on a Trunk; Configuring the Native VLAN for Untagged Traffic

---

## CCNA1-026 · Network Access

Objectives: 2.3 · multiple · Applied

A Cisco switch connects directly to a third-party switch that supports LLDP and does not advertise CDP. The physical link is up, and LLDP transmission and reception are enabled at both ends. Select TWO correct statements about neighbor discovery.

- **A.** show lldp neighbors can reveal the third-party switch and its connected port.
- **B.** A CDP entry is required before LLDP can learn a neighbor.
- **C.** LLDP establishes an IP routing adjacency with the neighboring switch.
- **D.** A neighbor missing from show cdp neighbors proves the cable is faulty.
- **E.** The lack of a CDP entry is consistent with the peer not sending CDP.

**Answer: A, E**

Use the discovery protocol supported by the peer. An operational link can have an LLDP neighbor without a corresponding CDP neighbor.

**Option explanations**

- **A:** LLDP supplies neighboring device and port information across supporting vendors.
- **B:** The two discovery protocols operate independently.
- **C:** LLDP discovers Layer 2 neighbors; it is not a routing protocol.
- **D:** A working peer that does not advertise CDP need not appear in CDP output.
- **E:** CDP output depends on received CDP advertisements, not merely an operational physical link.

**Further reading**

- [Interface and Hardware Components Configuration Guide, Cisco IOS XE 17.15.x — Configuring LLDP, LLDP-MED, and Wired Location Service](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst9300/software/release/17-15/configuration_guide/int_hw/b_1715_int_and_hw_9300_cg/configuring_lldp__lldp_med__and_wired_location_service.html) — LLDP; Enabling LLDP; Monitoring and Maintaining LLDP, LLDP-MED, and Wired Location Service
- [Network Management Configuration Guide, Cisco IOS XE 17.15.x — Configuring Cisco Discovery Protocol](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst9300/software/release/17-15/configuration_guide/nmgmt/b_1715_nmgmt_9300_cg/configuring_the_cisco_discovery_protocol.html) — Monitoring and Maintaining Cisco Discovery Protocol

---

## CCNA1-027 · Network Access

Objectives: 2.4 · single · Applied

Two switches are being connected using a new Layer 2 LACP EtherChannel. All physical and VLAN settings match, but every member on both ends uses channel-group 7 mode passive. No EtherChannel forms. Which change allows LACP negotiation while keeping the peer passive?

- **A.** Set the local members to mode desirable.
- **B.** Set the local members to mode on.
- **C.** Set the local members to mode auto.
- **D.** Set the local members to mode active.

**Answer: D**

Passive LACP ports respond to negotiation but do not start it. At least one end must be active for this newly established LACP channel to form.

**Option explanations**

- **A:** Desirable starts PAgP, which does not negotiate with LACP.
- **B:** On creates a static channel without LACP negotiation.
- **C:** Auto is a PAgP mode, not an initiating LACP mode.
- **D:** Active initiates LACP; the passive peer can respond and form the bundle.

**Further reading**

- [Layer 2 Configuration Guide, Cisco IOS XE 17.15.x — Configuring EtherChannels](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst9300/software/release/17-15/configuration_guide/lyr2/b_1715_lyr2_9300_cg/configuring_etherchannels.html) — Link Aggregation Control Protocol Modes; Configuring Layer 3 EtherChannels

---

## CCNA1-028 · Network Access

Objectives: 2.4 · single · Applied

An engineer is completing a routed EtherChannel on a Catalyst switch. Po7 and its member ports are configured with no switchport, and LACP has bundled both links. Where should the local IP address 198.51.100.1/30 be configured?

```text
interface Port-channel7
 no switchport
!
interface range GigabitEthernet1/0/1 - 2
 no switchport
 channel-group 7 mode active
```

- **A.** On both physical member interfaces.
- **B.** On an SVI whose VLAN number is 7.
- **C.** On interface Port-channel7 only.
- **D.** On only the lowest-numbered physical member.

**Answer: C**

A Layer 3 EtherChannel is one routed logical interface. Configure its IP address on the port-channel and keep member interfaces unnumbered.

**Option explanations**

- **A:** The members carry the aggregate traffic; duplicate addresses on them do not define the routed aggregate.
- **B:** A channel-group number does not create or select a VLAN.
- **C:** The logical routed interface owns the aggregate Layer 3 address.
- **D:** The address must remain with the logical link, independent of which member forwards traffic.

**Further reading**

- [Command Reference, Cisco IOS XE Everest 16.5.x — Layer 2/3 Commands](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst9300/software/release/16-5/command_reference/b_165_9300_cr/b_165_9300_cr_chapter_0111.html) — interface port-channel — Usage Guidelines
- [Layer 2 Configuration Guide, Cisco IOS XE 17.15.x — Configuring EtherChannels](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst9300/software/release/17-15/configuration_guide/lyr2/b_1715_lyr2_9300_cg/configuring_etherchannels.html) — Link Aggregation Control Protocol Modes; Configuring Layer 3 EtherChannels

---

## CCNA1-029 · Network Access

Objectives: 2.5.a · single · Challenge

Four connected switches participate in Rapid PVST+ for VLAN 40. The table lists configured base priorities before adding the VLAN ID. SW1 is currently root. If SW1 fails and the other three remain connected, which becomes root?

| Switch | Base priority | Bridge MAC |
| --- | --- | --- |
| SW1 | 24576 | 0011.2233.4400 |
| SW2 | 28672 | 0011.2233.5500 |
| SW3 | 28672 | 0011.2233.1100 |
| SW4 | 32768 | 0001.0000.0001 |

- **A.** SW3
- **B.** SW2
- **C.** SW4
- **D.** No switch until root secondary is configured.

**Answer: A**

Compare priority first and MAC address only to break a tie. Adding VLAN ID 40 to every base priority preserves the ordering, so SW3 wins among the surviving switches.

**Option explanations**

- **A:** SW2 and SW3 tie at priority 28672; SW3 has the lower MAC address.
- **B:** Its priority ties SW3, so the lower MAC address selects SW3.
- **C:** Its lower MAC address does not overcome its higher numerical priority.
- **D:** Root election is automatic; root secondary is a configuration convenience.

**Further reading**

- [Layer 2 Configuration Guide, Cisco IOS XE 17.15.x — Configuring Spanning Tree Protocol](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst9300/software/release/17-15/configuration_guide/lyr2/b_1715_lyr2_9300_cg/configuring_spanning_tree_protocol.html) — Spanning-Tree Topology and Bridge Protocol Data Units; Bridge ID, Device Priority, and Extended System ID; (Optional) Configuring a Secondary Root Device

---

## CCNA1-030 · Network Access

Objectives: 2.5.a, 2.5.b · single · Challenge

For VLAN 60, nonroot switch SW3 has two separate point-to-point links to the root bridge. Gi1/0/1 has path cost 4; Gi1/0/2 has path cost 19. There are no other links or STP guard features. After Rapid PVST+ converges, which describes Gi1/0/2 on SW3?

- **A.** Designated and forwarding
- **B.** Alternate and discarding
- **C.** Backup and discarding
- **D.** Root and learning permanently

**Answer: B**

Gi1/0/1 is the root port because it offers the lower cost. Gi1/0/2 is an alternate port in the discarding state; it can process BPDUs without forwarding user data or learning source MAC addresses.

**Option explanations**

- **A:** The root bridge is designated on this segment; SW3 has a better path through Gi1/0/1.
- **B:** It offers a less-preferred path to the root through another bridge and avoids forwarding a loop.
- **C:** A backup port protects a segment reached through the same bridge; this is an alternate root path.
- **D:** Gi1/0/1 has lower cost, and learning is a transitional state rather than a converged outcome here.

**Further reading**

- [Understand Rapid Spanning Tree Protocol (802.1w)](https://www.cisco.com/c/en/us/support/docs/lan-switching/spanning-tree-protocol/24062-146.html) — New Port States and Port Roles — Port States; Alternate and Backup Port Roles

---

## CCNA1-031 · Network Access

Objectives: 2.5.c · single · Foundation

A Rapid PVST+ access port connects to one workstation that does not bridge traffic. PortFast is enabled, and no BPDU filtering is configured. What does PortFast change when this edge link comes up?

- **A.** It permanently disables STP on the interface.
- **B.** It makes the workstation-facing switch the root bridge.
- **C.** It forces the interface into the alternate role.
- **D.** It allows the interface to begin forwarding immediately.

**Answer: D**

PortFast gives an end station prompt access when its link becomes operational. It should be used where the attached device does not create a bridging loop.

**Option explanations**

- **A:** PortFast accelerates the edge transition; it does not remove STP participation.
- **B:** Root election depends on bridge IDs, not PortFast.
- **C:** An ordinary workstation-facing port is not made an alternate by PortFast.
- **D:** PortFast avoids the normal forwarding delay for an edge connection.

**Further reading**

- [Layer 2 Configuration Guide, Cisco IOS XE 17.15.x — Configuring Optional Spanning-Tree Features](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst9300/software/release/17-15/configuration_guide/lyr2/b_1715_lyr2_9300_cg/configuring_optional_spanning_tree_features.html) — PortFast; Bridge Protocol Data Unit Guard; Bridge Protocol Data Unit Filtering

---

## CCNA1-032 · Network Access

Objectives: 2.5.d · matching · Applied

Match each behavior to its STP feature. For BPDU filter and BPDU guard, assume explicit interface-level configuration. Use each answer once.

1. A designated port enters root-inconsistent after receiving a superior BPDU.
2. A non-designated port is kept from forwarding after expected BPDUs stop arriving.
3. An interface enters error-disabled when it receives any BPDU.
4. An interface stops sending BPDUs and ignores received BPDUs.

- **A.** Root guard
- **B.** Loop guard
- **C.** BPDU guard
- **D.** BPDU filter

**Answer: 1 → A; 2 → B; 3 → C; 4 → D**

These features respond to different conditions: an unwanted superior root, missing expected BPDUs, any received BPDU, or deliberate BPDU suppression. Interface-level BPDU filtering differs from the global PortFast-dependent form.

**Option explanations**

- **A:** A superior BPDU triggers root-inconsistent; this is different from missing BPDUs or rejecting every BPDU.
- **B:** Missing expected BPDUs can trigger loop-inconsistent, preventing an unsafe move to forwarding.
- **C:** Receiving any BPDU triggers error-disable when this feature is explicitly enabled on the interface.
- **D:** The interface-level form suppresses sending and processing BPDUs; it is not an error-disable trigger.

**Further reading**

- [Layer 2 Configuration Guide, Cisco IOS XE 17.15.x — Configuring Optional Spanning-Tree Features](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst9300/software/release/17-15/configuration_guide/lyr2/b_1715_lyr2_9300_cg/configuring_optional_spanning_tree_features.html) — PortFast; Bridge Protocol Data Unit Guard; Bridge Protocol Data Unit Filtering
- [Enhance STP with Root Guard](https://www.cisco.com/c/en/us/support/docs/lan-switching/spanning-tree-protocol/10588-74.html) — Feature Description
- [Understand STP Loop Guard and UDLD Features](https://www.cisco.com/c/en/us/support/docs/lan-switching/spanning-tree-protocol-stp-8021d/218321-configure-stp-with-loop-guard-and-bpdu-s.html) — STP Port Roles; STP Loop Guard

---

## CCNA1-033 · Network Access

Objectives: 2.6, 2.8 · multiple · Applied

Select TWO accurate statements about the specified Cisco wireless architectures.

- **A.** A Meraki cloud-managed AP must send every user data packet through the Meraki management cloud.
- **B.** A FlexConnect AP can never switch client traffic onto a local branch VLAN.
- **C.** Meraki Dashboard centrally manages APs while ordinary user traffic follows its LAN or WAN destination.
- **D.** FlexConnect can combine centralized authentication with locally switched client data.
- **E.** CAPWAP requires the AP and controller to be in the same Ethernet broadcast domain.

**Answer: C, D**

Management, authentication, and data forwarding need not occur at the same place. Meraki separates its management service from user traffic, and FlexConnect can authenticate centrally while forwarding client data at the branch.

**Option explanations**

- **A:** Meraki separates cloud management from the normal client data path.
- **B:** Local switching is a supported FlexConnect function.
- **C:** Cloud management does not require ordinary client traffic to traverse the management cloud.
- **D:** Authentication placement and client data switching can be configured separately.
- **E:** CAPWAP uses IP transport, so routed AP-to-controller connectivity is supported.

**Further reading**

- [Meraki Cloud Architecture](https://documentation.meraki.com/Platform_Management/Dashboard_Administration/Design_and_Configure/Architectures_and_Best_Practices/Cisco_Meraki_Best_Practice_Design/Meraki_Cloud_Architecture) — Network and Management Data Segregation; The Meraki dashboard
- [Configure FlexConnect with Authentication on Catalyst 9800 WLC](https://www.cisco.com/c/en/us/support/docs/wireless/catalyst-9800-series-wireless-controllers/213921-flexconnect-configuration-with-central-a.html) — Background Information; Policy Profile Configuration
- [Cisco Wireless Controller Configuration Guide, Release 8.10 — AP Connectivity to Controller](https://www.cisco.com/c/en/us/td/docs/wireless/controller/8-10/config-guide/b_cg810/ap_connectivity_to_cisco_wlc.html) — CAPWAP

---

## CCNA1-034 · Network Access

Objectives: 2.6 · single · Foundation

A spare Cisco lightweight AP must act as a dedicated radio monitoring device and must not accept normal client associations. Which AP mode meets this requirement?

- **A.** Monitor
- **B.** Local
- **C.** FlexConnect
- **D.** Local mode with a lower transmit power

**Answer: A**

Monitor mode dedicates the AP to observation rather than normal client service. It is appropriate when sensing coverage is required without adding another client-serving radio.

**Option explanations**

- **A:** Monitor mode observes wireless channels without serving normal clients.
- **B:** Local mode is a client-serving mode with controller involvement.
- **C:** FlexConnect is a client-serving mode supporting branch deployments.
- **D:** Reducing transmit power does not convert a client-serving AP into a dedicated monitor.

**Further reading**

- [Cisco Catalyst 9800 Series Wireless Controller Software Configuration Guide, Cisco IOS XE 16.12.x — Monitor mode](https://www.cisco.com/c/en/us/td/docs/wireless/controller/9800/16-12/config-guide/b_wl_16_12_cg/monitor-mode.html) — Monitor mode; Enable monitor mode (GUI); returning AP to client-serving mode

---

## CCNA1-035 · Network Access

Objectives: 2.7, 2.2.c · single · Applied

An AireOS-managed FlexConnect AP locally switches employee traffic in VLAN 20 and guest traffic in VLAN 30. The AP sends its management traffic untagged in native VLAN 99. All three VLANs must traverse its single switch connection. Which switch-port configuration fits?

- **A.** Access VLAN 99
- **B.** Trunk, native VLAN 20, allowed VLANs 20,30,99
- **C.** Trunk, native VLAN 99, allowed VLANs 20,30,99
- **D.** Trunk, native VLAN 99, allowed VLAN 99 only

**Answer: C**

Local switching places the client VLANs on the AP uplink, so the link must carry more than the AP management VLAN. Its native VLAN must match the AP management handling described.

**Option explanations**

- **A:** An ordinary access port cannot carry the two additional tagged client VLANs as required.
- **B:** Untagged AP management frames would enter VLAN 20 instead of VLAN 99.
- **C:** The trunk carries both client VLANs and maps untagged management traffic to VLAN 99.
- **D:** The client VLANs would be excluded from the connection.

**Further reading**

- [Cisco Wireless Controller Configuration Guide, Release 8.10 — FlexConnect](https://www.cisco.com/c/en/us/td/docs/wireless/controller/8-10/config-guide/b_cg810/flexconnect.html) — Configuring the Switch at a Remote Site; Configuring an Access Point for FlexConnect (GUI)

---

## CCNA1-036 · Network Access

Objectives: 2.7 · single · Applied

A Cisco AireOS 5520 controller has LAG enabled and fully applied. Its two distribution ports connect to one Catalyst switch, carrying the same VLANs. Which Catalyst EtherChannel mode is appropriate for this controller?

- **A.** active
- **B.** on
- **C.** passive
- **D.** desirable

**Answer: B**

AireOS controller LAG is a platform-specific static bundle. Configure matching Layer 2 settings and a static channel on the connected Catalyst ports.

**Option explanations**

- **A:** This starts LACP, which this AireOS controller LAG implementation does not negotiate.
- **B:** AireOS controller LAG uses a static EtherChannel; the Catalyst side uses mode on.
- **C:** A passive LACP endpoint still requires an LACP-speaking peer.
- **D:** PAgP negotiation is not supported by this controller LAG implementation.

**Further reading**

- [Cisco Wireless Controller Configuration Guide, Release 8.10 — Ports and Interfaces](https://www.cisco.com/c/en/us/td/docs/wireless/controller/8-10/config-guide/b_cg810/ports_and_interfaces.html) — Restrictions on Link Aggregation; Configuring Neighbor Devices to Support Link Aggregation

---

## CCNA1-037 · Network Access

Objectives: 2.8 · single · Applied

A team requires encrypted remote CLI and browser management of a Cisco controller, plus a local connection usable when its IP management path fails. Which set maps those requirements correctly?

- **A.** CLI: Telnet; browser: HTTPS; local recovery: console
- **B.** CLI: SSH; browser: HTTP; local recovery: console
- **C.** CLI: TACACS+; browser: RADIUS; local recovery: SSH
- **D.** CLI: SSH; browser: HTTPS; local recovery: console

**Answer: D**

Choose the access transport separately from the authentication service. SSH and HTTPS provide the requested remote interfaces, while a console connection supplies local access if the network path is unavailable.

**Option explanations**

- **A:** Telnet does not provide an encrypted management session.
- **B:** Plain HTTP does not meet the encrypted browser requirement.
- **C:** TACACS+ and RADIUS provide AAA services, not these user interfaces; SSH needs network reachability.
- **D:** SSH and HTTPS protect remote sessions; a direct console connection does not require an IP path.

**Further reading**

- [Cisco Wireless Controller Configuration Guide, Release 8.10 — Administration of Controller](https://www.cisco.com/c/en/us/td/docs/wireless/controller/8-10/config-guide/b_cg810/administration_of_cisco_wlc.html) — Logging on to the Controller CLI; Enabling Web and Secure Web Modes (GUI); Enabling Web and Secure Web Modes (CLI)
- [Cisco Wireless Controller Configuration Guide, Release 8.10 — AAA Administration](https://www.cisco.com/c/en/us/td/docs/wireless/controller/8-10/config-guide/b_cg810/aaa_administration.html) — Configuring TACACS+ (GUI)

---

## CCNA1-038 · Network Access

Objectives: 2.9 · single · Applied

An AireOS controller GUI shows the fields below for a newly created WLAN. The relevant AP group includes this WLAN, and AP radios are operational. A correctly configured client is searching for the SSID Workshop. Which change is required before that AP can offer the WLAN?

| GUI field | Value |
| --- | --- |
| WLAN ID | 8 |
| Profile Name | Training-Profile |
| SSID | Workshop |
| Status | Disabled |
| Broadcast SSID | Enabled |

- **A.** Enable the WLAN Status setting and apply the change.
- **B.** Rename the profile from Training-Profile to Workshop.
- **C.** Set the WLAN ID to the client VLAN number.
- **D.** Disable Broadcast SSID.

**Answer: A**

The SSID is already Workshop, and its AP group assignment is present. Administrative status is the blocking condition shown; the profile name is an internal identifier.

**Option explanations**

- **A:** The WLAN is administratively disabled, so the AP cannot offer it.
- **B:** The internal profile name need not match the advertised SSID.
- **C:** WLAN identifiers and VLAN identifiers are separate values.
- **D:** Hiding an SSID does not enable a disabled WLAN.

**Further reading**

- [Cisco Wireless Controller Configuration Guide, Release 8.10 — WLANs](https://www.cisco.com/c/en/us/td/docs/wireless/controller/8-10/config-guide/b_cg810/wlans.html) — Prerequisites for WLANs; Enabling and Disabling WLANs (GUI); Editing WLAN SSID or Profile Name for WLANs (GUI)

---

## CCNA1-039 · Network Access

Objectives: 2.9 · single · Applied

The exhibited security values have been applied to an AireOS WLAN. A client has selected the correct SSID and WPA2-AES, but its credential field is blank. Which credential must the client supply to match this WLAN authentication method?

| GUI security field | Value |
| --- | --- |
| WPA2 Policy | Enabled |
| WPA2 AES | Enabled |
| Authentication Key Management | PSK |
| PSK Format | ASCII |
| PSK | Configured; masked |

- **A.** The administrator password used to sign in to the WLC GUI.
- **B.** An individual RADIUS username and password.
- **C.** The configured WLAN preshared key.
- **D.** The numeric WLAN ID.

**Answer: C**

PSK authentication uses a shared WLAN secret. A RADIUS user account or controller administrator password is not a substitute for that key.

**Option explanations**

- **A:** Controller management credentials are separate from the WLAN PSK.
- **B:** The exhibited authentication method is PSK, not 802.1X/EAP.
- **C:** The client must possess the same PSK used for this WLAN.
- **D:** A WLAN ID identifies the controller configuration; it is not an authentication secret.

**Further reading**

- [Cisco Wireless Controller Configuration Guide, Release 8.10 — WLAN Security](https://www.cisco.com/c/en/us/td/docs/wireless/controller/8-10/config-guide/b_cg810/wlan_security.html) — Configuring WPA1+WPA2 (GUI); Configuring Peer-to-Peer Blocking (GUI)

---

## CCNA1-040 · Network Access

Objectives: 2.9 · multiple · Challenge

An AireOS controller centrally switches a guest WLAN. Policy requires the standard background QoS profile and requires the controller to discard unicast traffic between wireless peers on this WLAN. Current GUI values are QoS = Silver and P2P Blocking = Disabled. Select TWO changes that satisfy the requirements.

- **A.** Set QoS to Bronze.
- **B.** Set QoS to Platinum.
- **C.** Set P2P Blocking to Forward-UpStream.
- **D.** Disable Broadcast SSID.
- **E.** Set P2P Blocking to Drop.

**Answer: A, E**

Bronze selects background treatment. P2P Blocking set to Drop enforces the requested controller action for peer traffic; forwarding upstream does not establish that same action.

**Option explanations**

- **A:** Bronze is the standard background profile.
- **B:** Platinum is the voice profile, not background.
- **C:** This delegates the forwarding decision to the upstream device rather than requiring the controller to discard it.
- **D:** SSID visibility does not enforce the requested peer traffic behavior or QoS profile.
- **E:** Drop makes the controller discard the affected peer traffic.

**Further reading**

- [Cisco Wireless Controller Configuration Guide, Release 8.10 — Wireless Quality of Service](https://www.cisco.com/c/en/us/td/docs/wireless/controller/8-10/config-guide/b_cg810/wireless_quality_of_service.html) — Assigning a QoS Profile to a WLAN (GUI)
- [Cisco Wireless Controller Configuration Guide, Release 8.10 — WLAN Security](https://www.cisco.com/c/en/us/td/docs/wireless/controller/8-10/config-guide/b_cg810/wlan_security.html) — Configuring WPA1+WPA2 (GUI); Configuring Peer-to-Peer Blocking (GUI)

---

## CCNA1-041 · IP Connectivity

Objectives: 3.1.a, 3.1.d, 3.1.e, 3.1.f · single · Foundation

An engineer examines this constructed Cisco IOS routing-table entry. Which interpretation is correct?

```text
O  10.44.8.0/24 [110/25] via 192.0.2.2, 00:02:11, GigabitEthernet0/1
```

- **A.** The route is static, with administrative distance 25 and metric 110.
- **B.** The route is OSPF, with administrative distance 110, metric 25, and next hop 192.0.2.2.
- **C.** The route is OSPF, and 00:02:11 is the dead interval of its next-hop neighbor.
- **D.** The route is directly connected, and GigabitEthernet0/1 is its remote next-hop address.

**Answer: B**

The O code identifies an OSPF route. The brackets contain administrative distance followed by metric; the address after via is the next hop.

**Option explanations**

- **A:** O identifies OSPF; the bracketed values are reversed here.
- **B:** Each value is mapped to its correct field.
- **C:** This field is route age, not an OSPF neighbor timer.
- **D:** The interface is local egress; the next-hop address follows via.

**Further reading**

- [Understand Administrative Distance](https://www.cisco.com/c/en/us/support/docs/ip/border-gateway-protocol-bgp/15986-admin-distance.html) — Additional Uses of AD

---

## CCNA1-042 · IP Connectivity

Objectives: 3.1.a, 3.1.b · multiple · Applied

A Cisco IOS router has the two constructed entries shown. No policy routing is configured. Which two statements correctly explain these entries? Select two.

```text
C  10.20.30.0/24 is directly connected, GigabitEthernet0/0
L  10.20.30.1/32 is directly connected, GigabitEthernet0/0
```

- **A.** The C entry represents the subnet directly attached to GigabitEthernet0/0.
- **B.** The L entry is a less-preferred alternate route to every host in the /24.
- **C.** The L entry was learned from an OSPF loopback advertisement.
- **D.** The /32 entry identifies 10.20.30.1 as an address of this router.
- **E.** The two entries prove that a second router is reachable on this LAN.

**Answer: A, D**

The connected prefix describes the attached network. The local host route separately identifies the router's own address for local delivery.

**Option explanations**

- **A:** C identifies the connected network prefix.
- **B:** It matches only the local interface address.
- **C:** L denotes local delivery, not an OSPF-learned route.
- **D:** An IOS local host route represents the interface address.
- **E:** Neither entry establishes the presence of another router.

**Further reading**

- [Local Host Routes Installed in the Routing Table on Cisco IOS and Cisco IOS-XR](https://www.cisco.com/c/en/us/support/docs/ip/ip-routing/116264-technote-ios-00.html) — Cisco IOS Local Routes

---

## CCNA1-043 · IP Connectivity

Objectives: 3.1.b, 3.1.c · single · Applied

A routing table contains the destination prefix 172.22.36.0/22. Which network mask and inclusive address range describe that prefix?

- **A.** 255.255.255.0; 172.22.36.0 through 172.22.36.255
- **B.** 255.255.248.0; 172.22.32.0 through 172.22.39.255
- **C.** 255.255.252.0; 172.22.36.0 through 172.22.39.255
- **D.** 255.255.252.0; 172.22.36.0 through 172.22.40.255

**Answer: C**

Twenty-two prefix bits give mask 255.255.252.0. The remaining ten bits cover 1,024 addresses, beginning at third octet 36 and ending at 39.255.

**Option explanations**

- **A:** A /24 spans one third-octet value, not four.
- **B:** These values describe the containing /21.
- **C:** A /22 has third-octet blocks of four; 36 is aligned.
- **D:** The range extends one /24 beyond the /22 boundary.

**Further reading**

- [RFC 1812: Requirements for IP Version 4 Routers](https://www.rfc-editor.org/rfc/rfc1812.html) — 2.2.5.2 Classless Inter Domain Routing (CIDR)

---

## CCNA1-044 · IP Connectivity

Objectives: 3.1.g, 3.2.a · single · Applied

The exhibit lists all installed IPv4 routes on a router with ordinary destination-based forwarding. An otherwise valid transit packet is destined for 203.0.113.25. What does the router do?

```text
Gateway of last resort is 192.0.2.2 to network 0.0.0.0
S* 0.0.0.0/0 [1/0] via 192.0.2.2
C  10.8.0.0/24 is directly connected, GigabitEthernet0/0
L  10.8.0.1/32 is directly connected, GigabitEthernet0/0
C  192.0.2.0/30 is directly connected, GigabitEthernet0/1
L  192.0.2.1/32 is directly connected, GigabitEthernet0/1
```

- **A.** It sends the packet out GigabitEthernet0/0 because connected routes have the lowest administrative distance.
- **B.** It resolves the MAC address of 203.0.113.25 on every interface.
- **C.** It discards the packet because there is no /24 route for 203.0.113.0.
- **D.** It forwards the packet toward 192.0.2.2 using the default route.

**Answer: D**

The destination matches neither connected subnet nor a local address. It matches 0.0.0.0/0, so the gateway of last resort supplies the next hop.

**Option explanations**

- **A:** That connected subnet does not match the destination.
- **B:** A remote destination is not resolved on every attached link.
- **C:** A default route provides a matching destination prefix.
- **D:** The /0 entry is the only matching route.

**Further reading**

- [RFC 1812: Requirements for IP Version 4 Routers](https://www.rfc-editor.org/rfc/rfc1812.html) — 5.2.4.3 Next Hop Address

---

## CCNA1-045 · IP Connectivity

Objectives: 3.2.b, 3.2.c · single · Applied

These are candidate routes offered to one router for exactly the same prefix. All next hops resolve, and the listed administrative distances are in effect. Which candidate is installed in the routing information base (RIB)?

| Prefix | Source | Administrative distance | Metric | Next hop |
| --- | --- | --- | --- | --- |
| 10.60.0.0/16 | Internal EIGRP | 90 | 30720 | 192.0.2.2 |
| 10.60.0.0/16 | OSPF | 110 | 2 | 198.51.100.2 |
| 10.60.0.0/16 | Static | 150 | 0 | 203.0.113.2 |

- **A.** The internal EIGRP route through 192.0.2.2.
- **B.** The OSPF route through 198.51.100.2.
- **C.** The static route through 203.0.113.2.
- **D.** All three, because the prefixes have equal lengths.

**Answer: A**

For competing sources of the same prefix, the router prefers lower administrative distance. EIGRP's metric and OSPF's cost use different scales, so comparing their raw values does not choose the RIB source.

**Option explanations**

- **A:** Administrative distance 90 is the smallest candidate distance.
- **B:** Its smaller numeric metric does not overcome administrative distance 110.
- **C:** Its configured distance is 150, not the static default of 1.
- **D:** Equal prefixes compete for installation; different protocol metrics are not comparable.

**Further reading**

- [Configure Route Selection for Routers](https://www.cisco.com/c/en/us/support/docs/ip/enhanced-interior-gateway-routing-protocol-eigrp/8651-21.html) — Build the Routing Table

---

## CCNA1-046 · IP Connectivity

Objectives: 3.2.a · single · Applied

The table shows installed, usable routes. With no policy routing, which next hop handles a packet destined for 10.70.20.190?

| Installed prefix | Source | AD / metric | Next hop |
| --- | --- | --- | --- |
| 0.0.0.0/0 | Static | 1 / 0 | 192.0.2.6 |
| 10.70.0.0/16 | Static | 1 / 0 | 192.0.2.2 |
| 10.70.20.0/24 | OSPF | 110 / 2 | 198.51.100.2 |
| 10.70.20.128/25 | RIP | 120 / 4 | 203.0.113.2 |

- **A.** 192.0.2.2, because its route has the lowest administrative distance.
- **B.** 198.51.100.2, because the OSPF route has the lowest dynamic metric.
- **C.** 203.0.113.2, because 10.70.20.128/25 is the longest matching prefix.
- **D.** 192.0.2.6, because it is the gateway of last resort.

**Answer: C**

Forwarding chooses the most specific installed match. Address 10.70.20.190 is inside the /25, so that route wins despite its higher administrative distance.

**Option explanations**

- **A:** The /16 matches but is less specific than the /25.
- **B:** The /24 matches but is less specific than the /25.
- **C:** The destination lies within 10.70.20.128 through 10.70.20.255.
- **D:** The default loses to all three matching specific routes.

**Further reading**

- [Configure Route Selection for Routers](https://www.cisco.com/c/en/us/support/docs/ip/enhanced-interior-gateway-routing-protocol-eigrp/8651-21.html) — Make Forwarding Decisions

---

## CCNA1-047 · IP Connectivity

Objectives: 3.2.c, 3.1.f · single · Applied

R1 has two OSPFv2 intra-area paths to the same LAN in area 0. The exhibit gives every outgoing-interface cost along each path, including the final interface to the destination LAN. No other paths or routing sources exist. Which path does OSPF select?

| Path | R1 outgoing cost | Next router outgoing cost | Final LAN-interface cost |
| --- | --- | --- | --- |
| North | 2 | 12 | 1 |
| South | 5 | 6 | 1 |

- **A.** Path North, because its first link has the smaller cost.
- **B.** Path South, with a total cost of 12.
- **C.** Path North, with a total cost of 11.
- **D.** Both paths, because both cross two intermediate routers.

**Answer: B**

North costs 2 + 12 + 1 = 15; South costs 5 + 6 + 1 = 12. For these same-type intra-area routes, the lower total cost selects South.

**Option explanations**

- **A:** OSPF evaluates accumulated path cost, not only the first link.
- **B:** South sums to 5 + 6 + 1 = 12.
- **C:** North totals 2 + 12 + 1 = 15, not 11.
- **D:** Equal hop counts do not imply equal OSPF costs.

**Further reading**

- [RFC 2328: OSPF Version 2](https://www.rfc-editor.org/rfc/rfc2328.html) — 16.1 Calculating the shortest-path tree for an area

---

## CCNA1-048 · IP Connectivity

Objectives: 3.2.a, 3.2.b · multiple · Challenge

A router learns the three candidates shown. All next hops resolve, the listed administrative distances apply, and no other route matches 10.90.7.20. Which two statements describe normal RIB selection and subsequent forwarding? Select two.

| Candidate prefix | Source | AD / metric | Next hop |
| --- | --- | --- | --- |
| 10.90.0.0/16 | Static | 1 / 0 | 192.0.2.2 |
| 10.90.7.0/24 | OSPF | 110 / 20 | 198.51.100.2 |
| 10.90.7.0/24 | RIP | 120 / 1 | 203.0.113.2 |

- **A.** The static /16 prevents either /24 candidate from being installed.
- **B.** The OSPF /24 is selected over the RIP /24 for installation.
- **C.** Packets for 10.90.7.20 use the static /16 because its administrative distance is 1.
- **D.** The RIP /24 is selected because its metric 1 is smaller than 20.
- **E.** Packets for 10.90.7.20 use the OSPF /24 next hop.

**Answer: B, E**

The two /24 candidates compete with each other, and OSPF wins by administrative distance. The static /16 can also be installed; forwarding to this destination then chooses the /24.

**Option explanations**

- **A:** Different prefixes can coexist even when they overlap.
- **B:** For the identical /24, administrative distance 110 beats 120.
- **C:** Forwarding prefers the installed /24 match.
- **D:** Raw metrics from different routing protocols do not select the RIB source.
- **E:** The selected /24 is more specific than the installed /16.

**Further reading**

- [Configure Route Selection for Routers](https://www.cisco.com/c/en/us/support/docs/ip/enhanced-interior-gateway-routing-protocol-eigrp/8651-21.html) — Prefix Lengths; Make Forwarding Decisions

---

## CCNA1-049 · IP Connectivity

Objectives: 3.3.b · single · Applied

On a Cisco IOS router, 192.0.2.2 is a reachable neighbor on an active transit link. An engineer needs one static route covering exactly 10.32.40.0/23 through that neighbor. Which global configuration command meets the requirement?

- **A.** ip route 10.32.40.0 0.0.1.255 192.0.2.2
- **B.** ip route 10.32.40.0 255.255.255.0 192.0.2.2
- **C.** ip route 192.0.2.0 255.255.255.252 10.32.40.1
- **D.** ip route 10.32.40.0 255.255.254.0 192.0.2.2

**Answer: D**

The destination and mask identify the remote network, followed by the next hop. Mask 255.255.254.0 represents /23 and covers third octets 40 and 41.

**Option explanations**

- **A:** An ip route command requires a subnet mask, not this wildcard.
- **B:** The /24 mask omits the 10.32.41.0/24 half.
- **C:** This reverses the target and next-hop roles.
- **D:** The prefix, /23 mask, and next hop match the requirement.

**Further reading**

- [Configure a Next Hop IP Address for Static Routes](https://www.cisco.com/c/en/us/support/docs/dial-access/floating-static-route/118263-technote-nexthop-00.html) — Floating Static Route Example — Problem
- [RFC 1812: Requirements for IP Version 4 Routers](https://www.rfc-editor.org/rfc/rfc1812.html) — 2.2.5.2 Classless Inter Domain Routing (CIDR)

---

## CCNA1-050 · IP Connectivity

Objectives: 3.3.b · single · Applied

IPv6 unicast routing is enabled on a Cisco IOS router. A neighboring router uses link-local address FE80::2 on the active GigabitEthernet0/1 link. Which command adds a route to remote network 2001:DB8:80::/64 through that neighbor?

- **A.** ipv6 route 2001:DB8:80::/64 GigabitEthernet0/1 FE80::2
- **B.** ipv6 route 2001:DB8:80::/64 FE80::2
- **C.** ipv6 route FE80::2/128 GigabitEthernet0/1 2001:DB8:80::1
- **D.** ipv6 route 2001:DB8:80::/128 GigabitEthernet0/1 FE80::2

**Answer: A**

A link-local next hop is scoped to a link, so IOS requires an interface with it. The /64 prefix preserves the full target network.

**Option explanations**

- **A:** The command supplies the destination and the link-local next hop with its interface.
- **B:** A link-local next hop requires the outgoing interface.
- **C:** This names the neighbor as the destination instead of the remote network.
- **D:** The /128 selects one address instead of the required /64 network.

**Further reading**

- [Cisco IOS IPv6 Command Reference — IPv6 Commands: ipv6 ospf de to ipv6 sp](https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/ipv6/command/ipv6-cr-book/ipv6-i4.html) — ipv6 route — Syntax Description

---

## CCNA1-051 · IP Connectivity

Objectives: 3.3.a · single · Applied

An IPv4 router has ip routing enabled and a working connected path to 198.51.100.2. It has no default route. The engineer configured ip default-gateway 198.51.100.2, but transit packets with no specific matching route still fail. Which change supplies the required default route?

- **A.** Configure no ip routing.
- **B.** Configure ip route 198.51.100.2 255.255.255.255 198.51.100.2.
- **C.** Configure ip route 0.0.0.0 0.0.0.0 198.51.100.2.
- **D.** Configure ip default-gateway 0.0.0.0.

**Answer: C**

With IP routing enabled, the router needs a route in its routing table for transit forwarding. A static 0.0.0.0/0 route supplies the fallback; ip default-gateway serves devices with IP routing disabled.

**Option explanations**

- **A:** Disabling routing prevents the required transit forwarding.
- **B:** A host route to the neighbor does not match arbitrary destinations.
- **C:** A /0 static route provides a fallback for transit traffic.
- **D:** That command does not install the needed transit default route.

**Further reading**

- [IP Routing Frequently Asked Questions](https://www.cisco.com/c/en/us/support/docs/ip/border-gateway-protocol-bgp/28745-44.html) — What is the difference between the ip default-gateway, ip default-network, and ip route 0.0.0.0/0 commands?

---

## CCNA1-052 · IP Connectivity

Objectives: 3.3.c · multiple · Foundation

A dual-stack Cisco IOS router must add host routes for exactly 192.0.2.77 and 2001:DB8:77::7. Both listed next-hop addresses are directly reachable, and IPv6 routing is enabled. Which two commands create the requested host routes? Select two.

- **A.** ip route 192.0.2.0 255.255.255.0 198.51.100.2
- **B.** ip route 192.0.2.77 255.255.255.255 198.51.100.2
- **C.** ipv6 route 2001:DB8:77::/64 2001:DB8:12::2
- **D.** ipv6 route 2001:DB8:77::7/128 2001:DB8:12::2
- **E.** ipv6 route ::/0 2001:DB8:12::2

**Answer: B, D**

A host route has no address bits left unspecified: /32 for IPv4 and /128 for IPv6. The other commands describe broader destinations.

**Option explanations**

- **A:** This covers 256 addresses rather than one host.
- **B:** The all-ones IPv4 mask identifies exactly one address.
- **C:** This covers a /64 network rather than one host.
- **D:** A /128 prefix identifies exactly one IPv6 address.
- **E:** This is an IPv6 default route, not a host route.

**Further reading**

- [Local Host Routes Installed in the Routing Table on Cisco IOS and Cisco IOS-XR](https://www.cisco.com/c/en/us/support/docs/ip/ip-routing/116264-technote-ios-00.html) — Manually Configured Host Routes
- [Cisco IOS IPv6 Command Reference — IPv6 Commands: ipv6 ospf de to ipv6 sp](https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/ipv6/command/ipv6-cr-book/ipv6-i4.html) — ipv6 route — Syntax Description

---

## CCNA1-053 · IP Connectivity

Objectives: 3.3.d, 3.2.b · single · Challenge

A Cisco IOS router has these two static defaults and no tracking or dynamic routing. Both next hops remain reachable through active directly connected links. The primary ISP loses connectivity farther upstream, but the primary static route remains installed. What happens to ordinary Internet-bound transit traffic?

```text
ip route 0.0.0.0 0.0.0.0 192.0.2.2
ip route 0.0.0.0 0.0.0.0 198.51.100.2 10
```

- **A.** It immediately moves to 198.51.100.2 because the upstream Internet failure changes administrative distance.
- **B.** It continues toward 192.0.2.2; the floating route does not activate under the stated conditions.
- **C.** It is load-balanced across both next hops because both routes are static.
- **D.** It moves to 198.51.100.2 after the OSPF dead timer expires.

**Answer: B**

The backup has distance 10, while the primary uses static distance 1. A floating route depends on the preferred route becoming unavailable to the routing table; an undetected remote failure does not do that.

**Option explanations**

- **A:** Upstream reachability does not automatically change the configured distance.
- **B:** The lower-distance primary remains an eligible installed route.
- **C:** The routes have unequal administrative distances.
- **D:** No OSPF process or neighbor detection exists in this scenario.

**Further reading**

- [Configure a Next Hop IP Address for Static Routes](https://www.cisco.com/c/en/us/support/docs/dial-access/floating-static-route/118263-technote-nexthop-00.html) — Background Information; Floating Static Route Example
- [Understand Administrative Distance](https://www.cisco.com/c/en/us/support/docs/ip/border-gateway-protocol-bgp/15986-admin-distance.html) — Additional Uses of AD

---

## CCNA1-054 · IP Connectivity

Objectives: 3.3.a, 3.3.d · single · Applied

A Cisco IOS router currently uses an IPv6 default learned through RIPng with administrative distance 120. The engineer needs a static default through directly reachable 2001:DB8:2::2 that is installed only if the RIPng default disappears. No other default candidates exist. Which command meets the requirement?

- **A.** ipv6 route ::/0 2001:DB8:2::2 1
- **B.** ipv6 route ::/0 2001:DB8:2::2 119
- **C.** ipv6 route 2001:DB8:2::/64 2001:DB8:2::2 121
- **D.** ipv6 route ::/0 2001:DB8:2::2 121

**Answer: D**

The fallback must name ::/0 and use a distance greater than the competing default's 120. With a reachable next hop, distance 121 makes this static default a backup.

**Option explanations**

- **A:** Distance 1 would replace the RIPng default now.
- **B:** Distance 119 is preferred over 120.
- **C:** This creates a network route rather than a default.
- **D:** The /0 is a default, and 121 is greater than 120.

**Further reading**

- [IPv6 Routing: Static Routing — IP Routing Configuration Guide, Cisco IOS XE 17.x](https://www.cisco.com/c/en/us/td/docs/routers/ios/config/17-x/ip-routing/b-ip-routing/m_ip6-route-static-xe.html) — Configuring a Floating Static IPv6 Route; Example: Configuring a Fixed Default Route

---

## CCNA1-055 · IP Connectivity

Objectives: 3.3.b, 3.1.d · single · Challenge

On a Cisco IOS router, the constructed table excerpt shows all routes relevant to resolving next hop 10.255.0.2. All displayed routes are installed and usable. For a packet destined for 10.100.50.9, what final outgoing interface and directly connected next hop result from recursive resolution?

```text
S  10.100.50.0/24 [1/0] via 10.255.0.2
O  10.255.0.2/32 [110/5] via 192.0.2.2, 00:01:20, GigabitEthernet0/1
C  192.0.2.0/30 is directly connected, GigabitEthernet0/1
C  10.10.0.0/24 is directly connected, GigabitEthernet0/2
```

- **A.** GigabitEthernet0/1, toward 192.0.2.2.
- **B.** GigabitEthernet0/2, toward 10.100.50.9.
- **C.** GigabitEthernet0/1, with an ARP request for 10.255.0.2.
- **D.** No interface; static next hops must always be directly attached.

**Answer: A**

The destination selects the static /24. Its next hop 10.255.0.2 resolves through the OSPF /32, which leads to on-link neighbor 192.0.2.2 on GigabitEthernet0/1.

**Option explanations**

- **A:** The static next hop resolves through the OSPF host route and connected transit link.
- **B:** The destination is remote; the unrelated connected interface does not resolve it.
- **C:** The on-link next hop after recursion is 192.0.2.2.
- **D:** A recursively resolvable next hop can be used by an IPv4 static route.

**Further reading**

- [Configure a Next Hop IP Address for Static Routes](https://www.cisco.com/c/en/us/support/docs/dial-access/floating-static-route/118263-technote-nexthop-00.html) — Floating Static Route Example — Problem

---

## CCNA1-056 · IP Connectivity

Objectives: 3.4.a · single · Applied

Two Cisco IOS routers share an Ethernet subnet. Their interfaces are up, OSPF is enabled and nonpassive, authentication is disabled on both, router IDs are unique, MTUs match, and no traffic is filtered. The remaining parameters appear below. They have never become OSPF neighbors. Which change to R2 addresses the mismatch preventing neighbor formation?

| Parameter | R1 | R2 |
| --- | --- | --- |
| Interface IPv4 address | 192.0.2.1/29 | 192.0.2.2/29 |
| Area | 0 | 0 |
| Network type | Broadcast | Broadcast |
| OSPF process ID | 10 | 20 |
| Router ID | 10.1.1.1 | 10.2.2.2 |
| Interface priority | 1 | 50 |
| Hello / dead seconds | 10 / 40 | 5 / 20 |

- **A.** Change the OSPF process ID on R2 to 10.
- **B.** Change R2 interface priority to 1.
- **C.** Change the R2 hello and dead intervals to 10 and 40 seconds.
- **D.** Change R2 router ID to 10.1.1.1.

**Answer: C**

The hello/dead pairs differ, so the Hello compatibility checks fail. The process numbers and priorities may differ; the router IDs must remain unique.

**Option explanations**

- **A:** Process IDs are local and need not match between neighbors.
- **B:** Unequal nonzero priorities are valid on a broadcast segment.
- **C:** Both OSPF timer values must match their R1 counterparts.
- **D:** Duplicating R1 router ID would introduce another failure.

**Further reading**

- [Troubleshoot OSPF Neighbor Problems](https://www.cisco.com/c/en/us/support/docs/ip/open-shortest-path-first-ospf/13699-29.html) — No State Revealed
- [IP Routing: OSPF Configuration Guide — Configuring OSPF](https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/iproute_ospf/configuration/xe-16/iro-xe-16-book/iro-cfg.html) — Example: Basic OSPF Configuration for Internal Router ABR and ASBRs

---

## CCNA1-057 · IP Connectivity

Objectives: 3.4.a · multiple · Applied

R1 has received valid OSPFv2 Hello packets from R2 and currently lists R2 in Init state. The latest received Hello does not include R1's router ID in its neighbor list. Which two conclusions follow directly? Select two.

- **A.** R1 has evidence of Hello delivery from R2 to R1.
- **B.** R1 and R2 have already synchronized their link-state databases.
- **C.** R2 must have been elected the designated router.
- **D.** R1 has verified bidirectional Hello communication with R2.
- **E.** R1 has not yet received the Hello acknowledgment needed to establish 2-Way state.

**Answer: A, E**

Init confirms that R1 hears R2. Seeing R1's own router ID in R2's Hello neighbor list is what establishes the required bidirectional evidence for 2-Way.

**Option explanations**

- **A:** Receiving a valid Hello establishes this direction of delivery.
- **B:** Init occurs before database synchronization.
- **C:** Init does not establish any DR election result.
- **D:** R1 has not yet seen itself acknowledged in R2 Hello packets.
- **E:** Its router ID is absent from the received neighbor list.

**Further reading**

- [Understand OSPF Neighbor States](https://www.cisco.com/c/en/us/support/docs/ip/open-shortest-path-first-ospf/13685-13.html) — Init; 2-Way

---

## CCNA1-058 · IP Connectivity

Objectives: 3.4.a · single · Applied

A Cisco IOS router has active interfaces 10.0.0.5/30 on GigabitEthernet0/0 and 10.0.0.9/30 on GigabitEthernet0/1. OSPF process 7 exists with no network statements and no interface-level OSPF commands. Which router-configuration command enables OSPF in area 0 on GigabitEthernet0/0 while leaving GigabitEthernet0/1 outside OSPF?

- **A.** network 10.0.0.0 0.0.0.15 area 0
- **B.** network 10.0.0.4 0.0.0.3 area 0
- **C.** network 10.0.0.8 0.0.0.3 area 0
- **D.** network 10.0.0.4 0.0.0.0 area 0

**Answer: B**

The OSPF network statement matches local interface addresses using a wildcard mask. The .4–.7 range includes .5 and excludes .9.

**Option explanations**

- **A:** The wildcard range includes both .5 and .9.
- **B:** The range .4 through .7 matches only GigabitEthernet0/0.
- **C:** The range .8 through .11 selects GigabitEthernet0/1 instead.
- **D:** This matches only address .4, which is not an interface address.

**Further reading**

- [IP Routing: OSPF Configuration Guide — Configuring OSPF](https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/iproute_ospf/configuration/xe-16/iro-xe-16-book/iro-cfg.html) — Enabling OSPF

---

## CCNA1-059 · IP Connectivity

Objectives: 3.4.a, 3.4.b · single · Foundation

Two routers are joined by a working link, and both interfaces are explicitly configured with OSPFv2 network type point-to-point in area 0. Their compatible OSPF settings have converged. A constructed neighbor entry on R1 shows FULL/- for R2. How should the engineer interpret it?

- **A.** The adjacency is incomplete because no designated router exists.
- **B.** The link must be converted to broadcast before routes can be exchanged.
- **C.** R2 has priority zero, so OSPF cannot exchange link-state information with it.
- **D.** The adjacency is fully established; this link has no DR/BDR role to display.

**Answer: D**

Point-to-point neighbors form a full adjacency without a DR/BDR election. The dash indicates that no broadcast-segment role applies.

**Option explanations**

- **A:** A designated router is not required on a point-to-point network.
- **B:** Point-to-point is a supported OSPF network type.
- **C:** The role marker does not prevent adjacency on this network type.
- **D:** FULL is the expected converged adjacency state on this link.

**Further reading**

- [Understand OSPF Neighbor States](https://www.cisco.com/c/en/us/support/docs/ip/open-shortest-path-first-ospf/13685-13.html) — Full
- [RFC 2328: OSPF Version 2](https://www.rfc-editor.org/rfc/rfc2328.html) — 10.4 Whether to become adjacent

---

## CCNA1-060 · IP Connectivity

Objectives: 3.4.c, 3.4.d · single · Applied

Four OSPFv2 routers start on a new broadcast segment with no existing DR or BDR. Assume all four learn one another bidirectionally before the initial election, and no router has already claimed either role. Using the values shown, which pair becomes DR and BDR?

| Router | OSPF interface priority | Router ID |
| --- | --- | --- |
| R1 | 1 | 10.0.0.9 |
| R2 | 100 | 10.0.0.2 |
| R3 | 100 | 10.0.0.3 |
| R4 | 0 | 10.0.0.254 |

- **A.** DR R3; BDR R2.
- **B.** DR R4; BDR R3.
- **C.** DR R1; BDR R3.
- **D.** DR R2; BDR R3.

**Answer: A**

Exclude R4 because its priority is zero. R2 and R3 outrank R1 by priority; R3 wins their router-ID tie-breaker and R2 becomes BDR.

**Option explanations**

- **A:** R2 and R3 tie at priority 100; R3 has the higher router ID.
- **B:** Priority zero makes R4 ineligible for either role.
- **C:** R1 has a higher ID than R3 but a lower priority.
- **D:** At equal priority, R3 wins the router-ID comparison.

**Further reading**

- [RFC 2328: OSPF Version 2](https://www.rfc-editor.org/rfc/rfc2328.html) — 9.4 Electing the Designated Router

---

## CCNA1-061 · IP Connectivity

Objectives: 3.4.c · single · Applied

On a stable OSPFv2 broadcast segment, R1 is DR and R2 is BDR, each with interface priority 1. R3 joins later with priority 200 and a higher router ID than either existing router. R1 and R2 remain healthy, and no OSPF process or interface is reset. After R3 converges, what are the DR and BDR roles?

- **A.** R3 is DR and R1 is BDR.
- **B.** R1 is DR and R3 is BDR.
- **C.** R1 remains DR and R2 remains BDR.
- **D.** R2 becomes DR and R3 becomes BDR.

**Answer: C**

OSPF does not preempt an established DR/BDR pair merely because a stronger candidate joins. The healthy elected routers retain their roles.

**Option explanations**

- **A:** The newcomer does not replace the existing elected routers.
- **B:** R3 does not displace the healthy existing BDR either.
- **C:** The existing DR and BDR retain their roles when R3 joins.
- **D:** R2 is not promoted while the existing DR remains available.

**Further reading**

- [RFC 2328: OSPF Version 2](https://www.rfc-editor.org/rfc/rfc2328.html) — 9.4 Electing the Designated Router

---

## CCNA1-062 · IP Connectivity

Objectives: 3.4.d · single · Applied

A Cisco IOS router starts its OSPFv2 process for the first time after all interfaces in the exhibit are configured and up. No explicit router-id command exists. Which router ID does it select?

| Interface | IPv4 address | State |
| --- | --- | --- |
| Loopback0 | 10.10.10.1/32 | up/up |
| Loopback7 | 10.10.10.9/32 | up/up |
| GigabitEthernet0/0 | 203.0.113.250/24 | up/up |
| GigabitEthernet0/1 | 192.0.2.1/30 | up/up |

- **A.** 203.0.113.250
- **B.** 10.10.10.9
- **C.** 10.10.10.1
- **D.** 192.0.2.1

**Answer: B**

With no explicit router ID, IOS prefers an available loopback address. It chooses the highest loopback address, which is 10.10.10.9.

**Option explanations**

- **A:** An available loopback address is preferred over this larger physical-interface address.
- **B:** This is the highest address among the available loopback interfaces.
- **C:** Loopback0 is not preferred merely because its interface number is lower.
- **D:** The presence of loopbacks prevents automatic selection from these physical interfaces.

**Further reading**

- [IP Routing: OSPF Configuration Guide — Configuring OSPF](https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/iproute_ospf/configuration/xe-16/iro-xe-16-book/iro-cfg.html) — Route Distribution for OSPF; Forcing the Router ID Choice with a Loopback Interface

---

## CCNA1-063 · IP Connectivity

Objectives: 3.4.a, 3.4.c · single · Applied

Four routers share one OSPFv2 broadcast LAN in area 0. R1 is DR, R2 is BDR, and R3 and R4 are DROTHER routers. All settings are compatible and convergence is complete. R3 shows R1 and R2 in Full state but R4 in 2-Way state. What does this indicate?

- **A.** A dead-interval mismatch exists specifically between R3 and R4.
- **B.** R4 cannot learn routes until it becomes BDR.
- **C.** R3 and R4 must be assigned different OSPF areas.
- **D.** This is the expected neighbor relationship between two DROTHER routers.

**Answer: D**

On a broadcast segment, DROTHER routers need full adjacencies with the DR and BDR. Their mutual neighbor relationship can remain at 2-Way after convergence.

**Option explanations**

- **A:** The stated compatibility and stable 2-Way relationship do not support that diagnosis.
- **B:** A DROTHER can learn routes through its full adjacencies with DR and BDR.
- **C:** Different areas would prevent this normal same-segment relationship.
- **D:** They maintain 2-Way with each other and Full with DR and BDR.

**Further reading**

- [Understand OSPF Neighbor States](https://www.cisco.com/c/en/us/support/docs/ip/open-shortest-path-first-ospf/13685-13.html) — 2-Way; Full

---

## CCNA1-064 · IP Connectivity

Objectives: 3.5 · single · Foundation

A VLAN has two routers: R1 at 10.40.0.2 and R2 at 10.40.0.3. They provide a functioning HSRP group with virtual address 10.40.0.1, using the normal virtual MAC address. A host at 10.40.0.50/24 must retain the same configured gateway if the active router fails and HSRP converges. Which default gateway should the host use?

- **A.** 10.40.0.1
- **B.** 10.40.0.2
- **C.** 10.40.0.3
- **D.** 10.40.0.255

**Answer: A**

The host uses the HSRP virtual IP address. After failover, the surviving active router assumes forwarding responsibility for that virtual gateway.

**Option explanations**

- **A:** The shared virtual gateway address survives a change of active router.
- **B:** This addresses R1 individually and ties the host gateway to R1.
- **C:** This addresses R2 individually and bypasses the virtual gateway.
- **D:** The subnet broadcast address is not a unicast default gateway.

**Further reading**

- [Understand the Hot Standby Router Protocol Features and Functionality](https://www.cisco.com/c/en/us/support/docs/ip/hot-standby-router-protocol-hsrp/9234-hsrpguidetoc.html) — HSRP Background and Operations; HSRP Operation

---

## CCNA1-065 · IP Connectivity

Objectives: 3.5 · single · Applied

Two edge routers provide a working first-hop redundancy group to a LAN, but both rely on the same upstream circuit. That shared circuit fails; both routers and all LAN links stay operational, and neither router has another route to the remote service. What can the first-hop redundancy protocol accomplish by itself?

- **A.** Restore the remote service by changing the host subnet mask.
- **B.** Create a replacement WAN path by synchronizing the routers' routing tables.
- **C.** Maintain a redundant local gateway, while the remote service remains unreachable.
- **D.** Make both routers encapsulate traffic directly to the remote service over the LAN.

**Answer: C**

First-hop redundancy keeps a virtual gateway available when a participating router fails. It does not provide an independent upstream path, so the shared circuit failure still isolates this service.

**Option explanations**

- **A:** First-hop redundancy does not change host subnet masks or create connectivity.
- **B:** The protocol does not create a missing upstream path.
- **C:** Gateway availability cannot compensate for the shared missing upstream path.
- **D:** The LAN cannot replace the failed circuit to the remote network.

**Further reading**

- [RFC 9568: Virtual Router Redundancy Protocol (VRRP) Version 3 for IPv4 and IPv6](https://www.rfc-editor.org/rfc/rfc9568.html#section-1) — 1 Introduction; 1.7 Definitions — Forwarding Responsibility
- [Understand the Hot Standby Router Protocol Features and Functionality](https://www.cisco.com/c/en/us/support/docs/ip/hot-standby-router-protocol-hsrp/9234-hsrpguidetoc.html) — HSRP Background and Operations

---

## CCNA1-066 · IP Services

Objectives: 4.1 · single · Applied

An IOS XE router already has correctly designated NAT inside and outside interfaces and working routes. An inside server at 10.24.8.20 must always appear as 198.51.100.20 to outside hosts. Which global configuration command creates the required static inside source address mapping?

- **A.** ip nat inside source static 198.51.100.20 10.24.8.20
- **B.** ip nat inside source static 10.24.8.20 198.51.100.20
- **C.** ip nat outside source static 198.51.100.20 10.24.8.20
- **D.** ip nat pool SERVER 198.51.100.20 198.51.100.20 netmask 255.255.255.0

**Answer: B**

Static inside source NAT binds a specified inside local address to a specified inside global address. The order is local, then global, so 10.24.8.20 must precede 198.51.100.20.

**Option explanations**

- **A:** This reverses the required inside local and inside global addresses.
- **B:** The command places the inside local address first and its fixed inside global address second.
- **C:** Outside source NAT defines an outside host mapping, not the requested inside source mapping.
- **D:** Defining a pool alone neither binds this server nor creates a static inside source mapping.

**Further reading**

- [IP Addressing Configuration Guide, Cisco IOS XE 17.x — Configuring NAT for IP Address Conservation](https://www.cisco.com/c/en/us/td/docs/routers/ios/config/17-x/ip-addressing/b-ip-addressing/m_iadnat-addr-consv-xe.html) — Configuring Static Translation of Inside Source Addresses

---

## CCNA1-067 · IP Services

Objectives: 4.1 · single · Challenge

The router uses the constructed configuration below. Interfaces and routes are correct, and these are its only NAT rules. Three different inside hosts already hold all available pool addresses, and none of those bindings expires. A fourth permitted inside host starts a TCP connection. What happens to that host's NAT allocation?

```text
access-list 10 permit 10.24.8.0 0.0.0.255
ip nat pool OUTSIDE 198.51.100.10 198.51.100.12 netmask 255.255.255.0
ip nat inside source list 10 pool OUTSIDE
```

- **A.** It shares an allocated address by receiving a translated TCP port.
- **B.** It receives 198.51.100.13 because the pool uses a /24 mask.
- **C.** It replaces an existing binding because its TCP connection is newer.
- **D.** It cannot obtain a new binding until a pool address becomes available.

**Answer: D**

The inclusive range .10 through .12 contains three addresses. Without overload, each concurrent inside address binding needs its own global address. A fourth host cannot obtain a binding while all three remain allocated.

**Option explanations**

- **A:** Port sharing requires NAT overload; this configuration does not enable it.
- **B:** The mask does not expand the explicit start-to-end allocation range.
- **C:** A new connection does not displace a valid binding merely because it is newer.
- **D:** The three-address pool is exhausted, and address sharing is not configured.

**Further reading**

- [RFC 3022 — Traditional IP Network Address Translator (Traditional NAT)](https://www.rfc-editor.org/rfc/rfc3022.html) — 2.1 Overview of Basic NAT; 3.1 Address binding; 5.4 Switch-over from Basic NAT to NAPT
- [Configure Network Address Translation](https://www.cisco.com/c/en/us/support/docs/ip/network-address-translation-nat/13772-12.html) — Configure NAT to Allow Internal Users to Access the Internet

---

## CCNA1-068 · IP Services

Objectives: 4.2 · multiple · Applied

R1 at 10.60.0.1 is synchronized to an upstream time source and operates as a stratum 2 NTP server. R2 must use R1 as its only unicast NTP time source. NTP traffic is allowed, and R2 eventually synchronizes successfully to R1. Which two statements are correct? Select two.

- **A.** Configure ntp server 10.60.0.1 on R2 to create the client association.
- **B.** Configure ntp master 2 on R2 to identify R1 as its remote server.
- **C.** R2 reports stratum 2 because clients copy the server's stratum unchanged.
- **D.** R2 reports stratum 3 after synchronizing to R1.
- **E.** R1 must have a reciprocal ntp peer command pointing to R2.

**Answer: A, D**

Configure the server address on the client with ntp server. Once R2 synchronizes to the specified stratum 2 server, its own stratum becomes 3. R1 can answer R2's client requests without forming a symmetric peer association.

**Option explanations**

- **A:** The ntp server command identifies the remote server from which the local device obtains time.
- **B:** ntp master makes the local device a time authority; it does not identify R1.
- **C:** A synchronized client is one NTP stratum farther from the reference than its selected server.
- **D:** R2's stratum is R1's stratum of 2 plus one.
- **E:** A unicast client/server association does not require a reciprocal symmetric peer configuration.

**Further reading**

- [Basic System Management Configuration Guide, Cisco IOS Release 15M&T — Network Time Protocol](https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/bsm/configuration/15-mt/bsm-15-mt-book/bsm-time-calendar-set.html) — Network Time Protocol; Poll-Based NTP Associations; Configuring Poll-Based NTP Associations; System as an Authoritative NTP Server
- [RFC 5905 — Network Time Protocol Version 4: Protocol and Algorithms Specification](https://www.rfc-editor.org/rfc/rfc5905.html) — 11.2.3 Combine Algorithm — system variable updates

---

## CCNA1-069 · IP Services

Objectives: 4.3 · single · Applied

DHCP clients receive valid IPv4 addresses, subnet masks, and default gateways. They can reach an application by its IP address. Inspection confirms that they have no DNS resolver address configured. A reachable DNS server at 10.80.0.53 contains the application's correct record. Which DHCP change supplies the missing information?

- **A.** Shorten the address lease so clients request their IPv4 addresses more often.
- **B.** Advertise 10.80.0.53 as the default gateway instead of the router.
- **C.** Advertise 10.80.0.53 in the DHCP domain name server option.
- **D.** Advertise the application's DNS domain as the DHCP domain name option.

**Answer: C**

DHCP can distribute a DNS server address along with other host settings. DNS then resolves the application name. Clients must obtain the updated DHCP configuration before using the supplied resolver.

**Option explanations**

- **A:** A shorter lease does not add a missing DNS resolver address.
- **B:** The DNS server's role does not make it the clients' IP forwarding gateway.
- **C:** This DHCP option supplies the DNS resolver address clients need for name queries.
- **D:** A DNS search domain can help expand short names, but it does not supply the missing resolver address.

**Further reading**

- [RFC 2132 — DHCP Options and BOOTP Vendor Extensions](https://www.rfc-editor.org/rfc/rfc2132.html) — 3.8 Domain Name Server Option; 3.17 Domain Name
- [RFC 1034 — Domain Names - Concepts and Facilities](https://www.rfc-editor.org/rfc/rfc1034.html) — 5.2.1 Typical functions

---

## CCNA1-070 · IP Services

Objectives: 4.4 · single · Foundation

An operations platform must collect a router's interface counter every minute and receive an SNMP notification when a monitored link fails without waiting for the next poll. Which assignment of SNMP roles and operations meets both requirements?

- **A.** The platform acts as manager, sends GET requests, and receives traps generated by the router's agent.
- **B.** The platform acts as agent, sends traps to request counters, and receives GET requests for link failures.
- **C.** The router sends SET requests each minute, and the platform answers with link-failure traps.
- **D.** The platform sends GET requests, and the router can report a link failure only in a later GET response.

**Answer: A**

The monitoring platform is the SNMP manager and the router runs the agent. A GET request reads an object such as an interface counter; a configured trap reports an event asynchronously. A trap has no SNMP acknowledgment, so sending one does not guarantee delivery.

**Option explanations**

- **A:** GET retrieves object values, while an agent can send an unsolicited trap for an event.
- **B:** This reverses the roles and misuses both GET requests and traps.
- **C:** SET changes object values; it is not the manager's periodic counter retrieval operation.
- **D:** Polling is valid, but SNMP also supports unsolicited event notifications.

**Further reading**

- [SNMP Configuration Guide, Cisco IOS XE 17 — Configuring SNMP Support](https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/snmp/configuration/xe-17-x/snmp-xe-17-book/nm-snmp-cfg-snmp-support.html) — SNMP Operations — SNMP Get, SNMP SET, and SNMP Notifications; Traps and Informs

---

## CCNA1-071 · IP Services

Objectives: 4.5 · single · Applied

An IOS device has remote logging enabled and the constructed configuration and message below. Assume the syslog server is reachable and no other message filters apply. Which interpretation is correct?

```text
logging host 10.70.0.50
logging trap warnings

%LINK-3-UPDOWN: Interface GigabitEthernet0/1, changed state to down
```

- **A.** LINK is severity 3, and UPDOWN is the facility; the message is excluded.
- **B.** LINK is the facility, 3 means errors, and the message passes the remote logging threshold.
- **C.** LINK is the facility, 3 means warnings, and the message passes the remote logging threshold.
- **D.** LINK is the facility, 3 means errors, and only severity 4 messages pass this threshold.

**Answer: B**

The IOS message format contains facility, numeric severity, and mnemonic. This message identifies the LINK facility and severity 3. A warnings threshold includes severity 4 and all numerically lower, more urgent levels.

**Option explanations**

- **A:** LINK is the facility, 3 is the severity, and UPDOWN is the mnemonic.
- **B:** A warnings threshold is severity 4 and includes the more severe, numerically lower level 3.
- **C:** The message passes the threshold, but severity 3 means errors; warnings is level 4.
- **D:** The threshold includes levels 0 through 4, not just messages at level 4.

**Further reading**

- [System Message Logging](https://www.cisco.com/c/en/us/td/docs/routers/access/wireless/software/guide/SysMsgLogging.html) — System Log Message Format; Defining the Message Severity Level — Table 3 Message Logging Level Keywords

---

## CCNA1-072 · IP Services

Objectives: 4.6 · multiple · Applied

An IOS XE router's GigabitEthernet0/0 serves LAN clients at 10.20.30.1/24. GigabitEthernet0/1 connects to an ISP that assigns the router's WAN address using DHCP. A central LAN DHCP server at 10.99.0.10 is reachable through a separate, already configured interface. DHCP service, return routes, and server scopes are correct. Which two interface changes enable the router's WAN DHCP client and relay the LAN clients' initial DHCP broadcasts? Select two.

- **A.** Configure ip helper-address 10.99.0.10 under GigabitEthernet0/1.
- **B.** Configure ip helper-address 10.99.0.10 under GigabitEthernet0/0.
- **C.** Replace GigabitEthernet0/0's address with ip address dhcp.
- **D.** Configure ip helper-address 10.20.30.1 under GigabitEthernet0/0.
- **E.** Configure ip address dhcp under GigabitEthernet0/1.

**Answer: B, E**

The WAN interface obtains its own address with ip address dhcp. The LAN interface needs ip helper-address pointing to the central server because that interface receives the clients' broadcasts. The client and relay functions serve different interfaces and purposes.

**Option explanations**

- **A:** The LAN broadcasts arrive on GigabitEthernet0/0, so the helper belongs on that interface.
- **B:** The client-facing interface relays its received DHCP broadcasts to the central server.
- **C:** That would make the LAN interface a DHCP client instead of preserving its required gateway address.
- **D:** A helper must identify the DHCP server destination, not this router's own LAN gateway address.
- **E:** This enables the router to request its WAN interface address from the ISP's DHCP service.

**Further reading**

- [IP Addressing: DHCP Configuration Guide, Cisco IOS XE Everest 16.6 — Configuring the Cisco IOS XE DHCP Relay Agent](https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/ipaddr_dhcp/configuration/xe-16-6/dhcp-xe-16-6-book/dhcp-relay-agent-xe.html) — Packet Forwarding Address; Specifying the Packet Forwarding Address
- [IP Addressing: DHCP Configuration Guide, Cisco IOS XE 17 (Cisco ASR 920 Series) — Configuring the Cisco IOS XE DHCP Client](https://www.cisco.com/c/en/us/td/docs/routers/asr920/configuration/guide/ipaddr-dhcp/17-1-1/b-dhcp-xe-17-1-asr920/m_config-dhcp-client-xe.html) — Configuring the DHCP Client; Configuring the DHCP Client Example

---

## CCNA1-073 · IP Services

Objectives: 4.7 · matching · Applied

Match each described QoS behavior to its mechanism. Use each option once. Treat the configured rate profile and the available buffer space as sufficient for the behavior described.

1. Identify voice packets by header fields, then set a DSCP value for downstream treatment.
2. Drop packets that exceed a configured traffic profile instead of delaying them to meet that profile.
3. Buffer a burst and release packets over time to keep transmission within a configured average rate.
4. During output congestion, hold packets in queues and choose which queue's packet is sent next.

- **A.** Policing
- **B.** Queuing and scheduling
- **C.** Classification and marking
- **D.** Shaping

**Answer: 1 → C; 2 → A; 3 → D; 4 → B**

Classification and marking identify traffic and label its intended treatment. Queuing and scheduling handle contention for an output link. Policing enforces a profile with actions such as drops, while shaping uses delay to smooth traffic to a configured rate.

**Option explanations**

- **A:** Policing applies a configured action, here dropping, to traffic outside its profile instead of smoothing it by delay.
- **B:** Queuing stores waiting packets; scheduling selects their service order during contention.
- **C:** Classification identifies the traffic class; marking writes the DSCP value. Neither action itself schedules transmission.
- **D:** Shaping uses buffering and delayed transmission to meet a rate profile. Ordinary queue selection alone does not impose that profile.

**Further reading**

- [Quality of Service Configuration Guide — Quality of service](https://www.cisco.com/c/en/us/td/docs/switches/lan/c9000/qos/quality-of-service-configuration-guide/m-quality-of-service.html) — Packet classification; Packet header marking; Class-based traffic shaping; Queuing and scheduling; Examples: Single-rate two-color policing configuration
- [QoS Frequently Asked Questions](https://www.cisco.com/c/en/us/support/docs/quality-of-service-qos/qos-policing/22833-qos-faq.html) — Queueing and Congestion Management — Q. What is the purpose of queueing?

---

## CCNA1-074 · IP Services

Objectives: 4.8 · single · Applied

An IOS XE router supports SSHv2 and already has a hostname, domain name, valid RSA keys, and a local administrator account. AAA is disabled. Only VTY lines 0–4 exist on this device. Which VTY configuration uses the local account database and accepts only SSH connections?

**Configuration A**

```text
line vty 0 4
 login
 transport input ssh
```

**Configuration B**

```text
line vty 0 4
 login local
 transport input telnet ssh
```

**Configuration C**

```text
line vty 0 4
 login local
 transport input ssh
```

**Configuration D**

```text
line vty 0 4
 login local
 transport output ssh
```


**Answer: C**

The existing SSH prerequisites allow the question to focus on the VTY configuration. login local selects the local user database. transport input ssh restricts incoming VTY sessions to SSH.

**Option explanations**

- **A:** login selects line-password authentication, not the local username database.
- **B:** Local authentication is selected, but Telnet is also allowed.
- **C:** login local selects the local accounts, and transport input ssh permits only SSH on these VTY lines.
- **D:** transport output controls connections initiated from the line, not incoming management access.

**Further reading**

- [Configure SSH on Routers](https://www.cisco.com/c/en/us/support/docs/security-vpn/secure-shell-ssh/4145-ssh.html) — Configure SSH on a Cisco Router Using Password Authentication; Prevent Non-SSH Connections

---

## CCNA1-075 · IP Services

Objectives: 4.9 · single · Foundation

A technician compares standard FTP with base TFTP for transferring a configuration file. Which statement correctly distinguishes protocol capabilities?

- **A.** TFTP includes username/password login and remote directory listing; FTP lacks both.
- **B.** TFTP uses TCP for file data, while FTP uses UDP for both control and data.
- **C.** TFTP requires an acknowledgment only after the whole file arrives because UDP handles lost blocks.
- **D.** FTP supports user authentication and directory listing; base TFTP provides simpler file reads and writes.

**Answer: D**

FTP provides a richer file-service interface, including user login and directory listings. Base TFTP uses UDP and implements its own block acknowledgments, but provides no user authentication or directory listing.

**Option explanations**

- **A:** These capabilities belong to FTP. Base TFTP has neither user authentication nor directory listing.
- **B:** The transport roles are reversed: TFTP uses UDP, while FTP uses TCP connections.
- **C:** UDP does not retransmit lost blocks. Base TFTP acknowledges data blocks during the transfer.
- **D:** FTP defines login and listing commands; base TFTP focuses on file transfer without those services.

**Further reading**

- [RFC 1350 — The TFTP Protocol (Revision 2)](https://www.rfc-editor.org/info/rfc1350/) — 1 Purpose; 2 Overview of the Protocol; 3 Relation to other Protocols
- [RFC 959 — File Transfer Protocol (FTP)](https://www.rfc-editor.org/rfc/rfc959.html) — 2.3 The FTP Model; 4.1.1 Access Control Commands; 4.1.3 FTP Service Commands — LIST

---

## CCNA1-076 · Security Fundamentals

Objectives: 5.1 · single · Foundation

An assessment finds an unpatched defect in a switch management service. A vendor update removes the defect. Which statement correctly identifies the vulnerability and the mitigation?

- **A.** The update is the vulnerability; the defect is the mitigation.
- **B.** The possibility of unauthorized access is the vulnerability; the defect is the mitigation.
- **C.** The unpatched defect is the vulnerability; installing the update is the mitigation.
- **D.** The defect is an exploit; the possibility of unauthorized access is the mitigation.

**Answer: C**

A vulnerability is an exploitable weakness. Installing the corrective update mitigates this weakness; an exploit would be a technique that takes advantage of it.

**Option explanations**

- **A:** The update reduces exposure; the defect creates the weakness.
- **B:** Possible harm is a threat, while the defect is a vulnerability.
- **C:** A weakness can be exploited; remediation reduces that exposure.
- **D:** An exploit uses a weakness; possible unauthorized access is a threat.

**Further reading**

- [RFC 4949: Internet Security Glossary, Version 2](https://www.rfc-editor.org/rfc/rfc4949.html) — Section 2: threat, vulnerability, and countermeasure

---

## CCNA1-077 · Security Fundamentals

Objectives: 5.2 · multiple · Applied

A company wants employees to recognize and report suspicious credential requests and wants to prevent unauthorized entry into its wiring closets. Which two measures directly address these goals? Select two.

- **A.** Provide recurring awareness sessions that practice recognition and the reporting procedure.
- **B.** Display a login banner on every switch.
- **C.** Place each wiring closet in a separate management VLAN.
- **D.** Use controlled door access that checks individual authorization before entry.
- **E.** Encrypt configuration backups stored in the data center.

**Answer: A, D**

Awareness and training help users act on suspicious requests. Physical access controls check who may enter restricted equipment areas; both belong in a security program.

**Option explanations**

- **A:** Training develops the required recognition and reporting behavior.
- **B:** A banner communicates a notice but does not teach or enforce these controls.
- **C:** Logical segmentation does not restrict people entering a closet.
- **D:** Door access control enforces the physical access requirement.
- **E:** Backup encryption addresses stored data, not either stated goal.

**Further reading**

- [NIST SP 800-53 Revision 5.1: Security and Privacy Controls for Information Systems and Organizations](https://csrc.nist.gov/CSRC/media/Projects/risk-management/800-53%20Downloads/800-53r5/SP_800-53_v5_1-derived-OSCAL.pdf) — AT-2 Literacy Training and Awareness; PE-3 Physical Access Control

---

## CCNA1-078 · Security Fundamentals

Objectives: 5.3 · single · Applied

This constructed IOS configuration uses a shared console password. AAA is not enabled, and the local netops account already works when tested through another management line. Which console-line command makes future console logins use the local username database?

```text
username netops secret ExampleLocal93!
!
line console 0
 password ExampleConsole92!
 login
```

- **A.** enable secret ExampleEnable94!
- **B.** login local
- **C.** service password-encryption
- **D.** transport input ssh

**Answer: B**

Apply login local under line console 0. The current login command checks the line password; login local instead requests a local username and its associated secret.

**Option explanations**

- **A:** The enable secret controls privileged access, not console login selection.
- **B:** This selects the local username database for line authentication.
- **C:** This changes storage representation for some passwords, not the authentication source.
- **D:** This does not select local console authentication.

**Further reading**

- [Catalyst 3750-X and 3560-X Configuration Guide: Configuring Switch-Based Authentication](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst3750x_3560x/software/release/15-0_2_se/configuration/guide/3750x_cg/swauthen.html) — Configuring Username and Password Pairs

---

## CCNA1-079 · Security Fundamentals

Objectives: 5.4 · single · Applied

A proposed password satisfies a company's length and character-complexity rules, but the entire password is present in its list of compromised passwords. Which password-policy control should reject it?

- **A.** A minimum-length check alone
- **B.** A requirement for one additional character category
- **C.** A rule permitting reuse after the next scheduled change
- **D.** Comparison against a blocklist of known compromised passwords

**Answer: D**

Complexity compliance does not make a known compromised password acceptable. A blocklist check prevents that value from being enrolled.

**Option explanations**

- **A:** The proposed password already passes the stated length requirement.
- **B:** Character categories do not establish that the password is uncompromised.
- **C:** Reuse does not resolve the known exposure.
- **D:** The full proposed value matches a password that must be rejected.

**Further reading**

- [NIST SP 800-63B-4: Digital Identity Guidelines — Authentication and Authenticator Management](https://pages.nist.gov/800-63-4/sp800-63b.html) — Section 3.1.1.2: Password Verifiers

---

## CCNA1-080 · Security Fundamentals

Objectives: 5.4 · multiple · Applied

Which two authentication designs require factors from two different categories? Select two. Treat the described checks as mandatory for each login.

- **A.** A memorized password and a memorized PIN
- **B.** A memorized password and an OTP generated by a separate hardware token
- **C.** A fingerprint scan and a face scan, with no possession check
- **D.** A username and an unprotected certificate file, with no private-key proof
- **E.** A smart card proving possession of its certificate private key, activated by a fingerprint

**Answer: B, E**

Two checks are not necessarily two factors. Password plus token combines knowledge and possession; biometric activation of a certificate-bearing smart card combines inherence and possession.

**Option explanations**

- **A:** Both are knowledge factors.
- **B:** This combines knowledge with possession of a token.
- **C:** Both are biometric factors, even though different traits are checked.
- **D:** An identifier and a public certificate do not prove two factors.
- **E:** The card supplies possession and its biometric activation supplies inherence.

**Further reading**

- [Duo 2FA: Authentication to Add Identity Defense](https://duo.com/product/multi-factor-authentication-mfa/two-factor-authentication-2fa) — FAQs: What is 2FA?
- [NIST SP 800-63B-4: Digital Identity Guidelines — Authentication and Authenticator Management](https://pages.nist.gov/800-63-4/sp800-63b.html) — Sections 2.2.1, 3.1.6, and 3.1.7: permitted authenticators and cryptographic authentication

---

## CCNA1-081 · Security Fundamentals

Objectives: 5.5 · multiple · Applied

A company needs encrypted IP connectivity for a traveling employee's laptop and between two permanent office LANs. Which two IPsec deployment descriptions fit these separate requirements? Select two.

- **A.** The laptop establishes a remote-access IPsec connection to the company VPN gateway.
- **B.** A site-to-site VPN requires every office workstation to establish its own IPsec tunnel.
- **C.** The two office gateways establish a site-to-site IPsec connection for selected interoffice traffic.
- **D.** The traveling laptop must become a permanent branch gateway to use IPsec.
- **E.** The company must give every private office host a public address before using a site-to-site VPN.

**Answer: A, C**

Remote access connects an individual endpoint to the company network. Site-to-site VPNs join networks through their gateways, which apply IPsec for the traffic selected by policy.

**Option explanations**

- **A:** A client-to-gateway VPN supports an individual remote endpoint.
- **B:** Office gateways can protect traffic on behalf of their LAN hosts.
- **C:** Gateway-to-gateway protection fits the network-to-network requirement.
- **D:** An endpoint can use a remote-access IPsec implementation.
- **E:** VPN gateways can carry traffic for privately addressed internal hosts.

**Further reading**

- [What Is a Virtual Private Network (VPN)?](https://www.cisco.com/site/us/en/learn/topics/security/what-is-a-virtual-private-network-vpn.html) — Types of VPNs: Remote access; Site-to-site

---

## CCNA1-082 · Security Fundamentals

Objectives: 5.6 · single · Challenge

The constructed ACL is applied inbound to the client-facing router interface. A packet from 10.24.8.25 to 192.0.2.80 has TCP destination port 443. Which entry decides its disposition?

```text
ip access-list extended CLIENTS-IN
 10 deny ip 10.24.8.0 0.0.0.255 any
 20 permit tcp host 10.24.8.25 host 192.0.2.80 eq 443
 30 permit ip any any
!
interface GigabitEthernet0/0
 ip access-group CLIENTS-IN in
```

- **A.** Sequence 10 denies it.
- **B.** Sequence 20 permits it because it is more specific.
- **C.** Sequence 30 permits it because the final explicit rule wins.
- **D.** The implicit deny rejects it because its destination is outside 10.24.8.0/24.

**Answer: A**

Sequence 10 matches 10.24.8.25 and all IP traffic from its /24. Processing stops there, so the HTTPS exception at sequence 20 is unreachable for this packet.

**Option explanations**

- **A:** The source matches the /24, and ip includes TCP.
- **B:** ACLs stop at the first match rather than choosing the most specific entry.
- **C:** Later rules are not reached after an earlier match.
- **D:** That prefix is a source match; the destination field in sequence 10 is any.

**Further reading**

- [Configure Commonly Used IP ACLs](https://www.cisco.com/c/en/us/support/docs/ip/access-lists/26448-ACLsamples.html) — Background Information; Deny a Select Host to Access the Network

---

## CCNA1-083 · Security Fundamentals

Objectives: 5.6 · single · Applied

R1 connects the employee LAN through Gi0/0 and the server LAN through Gi0/1. Employee packets enter Gi0/0 and leave Gi0/1. An extended ACL named EMPLOYEE-POLICY must filter these packets as they arrive from the employee LAN, before R1 makes its routing decision. Which application meets this requirement?

- **A.** ip access-group EMPLOYEE-POLICY out on Gi0/0
- **B.** ip access-group EMPLOYEE-POLICY in on Gi0/1
- **C.** ip access-group EMPLOYEE-POLICY out on Gi0/1
- **D.** ip access-group EMPLOYEE-POLICY in on Gi0/0

**Answer: D**

Direction is relative to the router interface. Inbound on Gi0/0 evaluates these packets before further routing processing; outbound on Gi0/1 evaluates them later.

**Option explanations**

- **A:** This checks traffic leaving R1 toward employees.
- **B:** This checks traffic arriving from the server LAN.
- **C:** This could filter the flow, but only after routing selects the egress interface.
- **D:** This checks the employee packets on arrival at R1.

**Further reading**

- [Configure IP Access Lists](https://www.cisco.com/c/en/us/support/docs/security/ios-firewall/23602-confaccesslists.html) — Define In, Out, Inbound, Outbound, Source, and Destination

---

## CCNA1-084 · Security Fundamentals

Objectives: 5.7 · single · Applied

DHCP snooping is enabled globally and for VLAN 40. Gi1/0/48 leads only to the authorized DHCP server, and Gi1/0/7 connects to an employee PC. Both interfaces are currently untrusted. Which change allows authorized server replies while retaining DHCP server filtering on the PC port?

- **A.** Configure ip dhcp snooping trust on Gi1/0/7 only.
- **B.** Configure ip dhcp snooping trust on Gi1/0/48 only.
- **C.** Configure ip dhcp snooping trust on both interfaces.
- **D.** Disable DHCP snooping on VLAN 40.

**Answer: B**

Snooping distinguishes the ingress path for authorized server messages from client-facing paths. Trust the verified server-facing port and retain the untrusted state on the employee port.

**Option explanations**

- **A:** Trusting the client port does not permit replies arriving on Gi1/0/48.
- **B:** The trusted server-facing ingress permits legitimate server replies.
- **C:** Trusting the PC port removes the required server-message filtering there.
- **D:** This also removes the requested filtering protection.

**Further reading**

- [Catalyst 3750-X and 3560-X Configuration Guide: Configuring DHCP Features and IP Source Guard](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst3750x_3560x/software/release/15-0_2_se/configuration/guide/3750x_cg/swdhcp82.html) — DHCP Snooping; Enabling DHCP Snooping and Option 82

---

## CCNA1-085 · Security Fundamentals

Objectives: 5.7 · single · Challenge

A statically addressed printer sends valid ARP messages from an untrusted switch port. Dynamic ARP inspection is enabled on its VLAN. The switch has no DHCP snooping entry or ARP ACL for the printer. What change permits its known IP-to-MAC mapping while keeping ARP inspection active on that port?

- **A.** Add the printer MAC address only to port security.
- **B.** Mark the printer port trusted for ARP inspection.
- **C.** Define an ARP ACL permitting the printer mapping and apply it to that VLAN for inspection.
- **D.** Increase the ARP rate limit on the printer port.

**Answer: C**

Static hosts may have no DHCP snooping binding. An applied ARP ACL authorizes the printer's specific mapping while the port remains subject to inspection.

**Option explanations**

- **A:** A secure MAC entry does not supply DAI with the required IP-to-MAC authorization.
- **B:** Trusted ingress bypasses inspection, contrary to the requirement.
- **C:** DAI can validate static hosts using an explicitly configured ARP ACL.
- **D:** A rate adjustment does not provide a missing valid binding.

**Further reading**

- [Catalyst 3750-X and 3560-X Configuration Guide: Configuring Dynamic ARP Inspection](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst3750x_3560x/software/release/15-0_2_se/configuration/guide/3750x_cg/swdynarp.html) — Understanding Dynamic ARP Inspection; Configuring ARP ACLs for Non-DHCP Environments

---

## CCNA1-086 · Security Fundamentals

Objectives: 5.7 · single · Applied

An access port has port security enabled, maximum 2, and violation mode restrict. Two secure MAC addresses are already learned; aging is disabled. A frame arrives from a third, unknown source MAC. What is the expected result?

- **A.** The frame is forwarded and becomes the third secure address.
- **B.** The oldest secure address is replaced by the new address.
- **C.** The entire interface becomes error-disabled.
- **D.** The frame is dropped, the violation counter increases, and the port remains operational.

**Answer: D**

Restrict mode drops traffic from additional unknown sources once the secure-address limit is reached. The existing secure devices can continue using the port.

**Option explanations**

- **A:** The configured maximum prevents learning another secure address.
- **B:** With aging disabled, reaching the limit does not evict an address.
- **C:** That is the shutdown violation behavior, not restrict.
- **D:** Restrict drops violating traffic and records violations without shutting down the port.

**Further reading**

- [Catalyst 3750-X and 3560-X Configuration Guide: Configuring Port-Based Traffic Control](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst3750x_3560x/software/release/15-0_2_se/configuration/guide/3750x_cg/swtrafc.html) — Security Violations; Enabling and Configuring Port Security

---

## CCNA1-087 · Security Fundamentals

Objectives: 5.8 · single · Applied

A management system verifies an engineer's identity, permits show commands but denies configuration commands, and stores a record of the session. Which mapping correctly identifies these three functions in that order?

- **A.** Authentication, authorization, accounting
- **B.** Authorization, authentication, accounting
- **C.** Authentication, accounting, authorization
- **D.** Accounting, authorization, authentication

**Answer: A**

Authentication establishes who is accessing the device. Authorization controls allowed actions, and accounting records the session or activity for later review.

**Option explanations**

- **A:** These functions establish identity, grant permissions, and record activity.
- **B:** The first two are reversed: identity verification is authentication.
- **C:** Permission enforcement is authorization; session recording is accounting.
- **D:** Accounting records activity; it does not verify the login identity.

**Further reading**

- [RFC 8907: The Terminal Access Controller Access-Control System Plus (TACACS+) Protocol](https://www.rfc-editor.org/rfc/rfc8907.html) — Sections 5 Authentication, 6 Authorization, and 7 Accounting

---

## CCNA1-088 · Security Fundamentals

Objectives: 5.9 · single · Foundation

A WLAN upgrade must retain a passphrase-based user experience and improve resistance to offline password guessing compared with WPA2-Personal. All clients support the chosen mode. Which configuration directly supplies that improvement?

- **A.** WPA-Personal using TKIP
- **B.** WPA3-Personal using SAE
- **C.** WPA2-Personal with the SSID hidden
- **D.** WPA2-Personal with a different channel width

**Answer: B**

WPA3-Personal uses Simultaneous Authentication of Equals for password-based authentication and resists offline dictionary guessing. WPA and WPA2-Personal do not gain that property merely through radio or SSID changes.

**Option explanations**

- **A:** The legacy WPA choice does not add SAE.
- **B:** SAE provides the requested password-authentication improvement.
- **C:** Hiding the SSID does not replace WPA2-PSK authentication with SAE.
- **D:** Channel width does not change the password-authentication mechanism.

**Further reading**

- [Cisco Catalyst 9800 Configuration Guide: Wi-Fi Protected Access 3](https://www.cisco.com/c/en/us/td/docs/wireless/controller/9800/17-3/config-guide/b_wl_17_3_cg/m_wpa3.html) — Simultaneous Authentication of Equals; Configure WPA3 SAE

---

## CCNA1-089 · Security Fundamentals

Objectives: 5.5 · single · Applied

A TCP packet from office host 10.1.10.15 to office host 10.2.20.25 crosses a site-to-site IPsec ESP tunnel between gateways 198.51.100.10 and 203.0.113.20. Tunnel mode and encryption are enabled. A transit router has no decryption keys. Which fields can it read directly from the packet crossing the tunnel?

- **A.** Both office host addresses; only the application data is encrypted.
- **B.** Both gateway addresses and the original TCP ports; only the host addresses are encrypted.
- **C.** Both gateway addresses in the outer IP header; the inner host addresses, TCP header, and application data are encrypted.
- **D.** Neither gateway nor host addresses; ESP encrypts both IP headers.

**Answer: C**

ESP tunnel mode carries the original IP packet inside an encrypted payload. Transit routers use the outer gateway addresses; they cannot directly read the encrypted inner addresses or TCP information without the keys.

**Option explanations**

- **A:** Tunnel-mode ESP encryption also covers the inner IP and TCP headers.
- **B:** The original TCP header is inside the encrypted payload.
- **C:** The outer header supports transit forwarding; the original packet is encrypted.
- **D:** The outer IP header remains readable by intervening routers.

**Further reading**

- [RFC 4301: Security Architecture for the Internet Protocol](https://www.rfc-editor.org/rfc/rfc4301.html) — Section 4.1: Definition and Scope; Section 4.2: SA Functionality

---

## CCNA1-090 · Security Fundamentals

Objectives: 5.10, 5.9 · single · Applied

The table summarizes a constructed Cisco AireOS 8.10 WLAN GUI configuration. The requirement is WPA2-Personal with a shared passphrase and no 802.1X authentication server. Which change completes the security settings?

| GUI field | Current setting |
| --- | --- |
| Layer 2 Security | WPA+WPA2 |
| Security Type | Enterprise |
| WPA Policy | Disabled |
| WPA2 Policy | Enabled |
| WPA2 Policy-AES | Enabled |
| Authentication Key Management | 802.1X |
| PSK | Not configured |

- **A.** Select Personal, use PSK key management, and configure the same valid passphrase on the WLAN and clients.
- **B.** Keep Enterprise and add a RADIUS server.
- **C.** Set Layer 2 Security to None and retain the passphrase on clients.
- **D.** Enable WPA Policy while leaving 802.1X key management selected.

**Answer: A**

The WPA2 policy and AES cipher are already selected. Personal security with PSK supplies the shared-passphrase authentication; matching client settings are required.

**Option explanations**

- **A:** Personal with PSK satisfies the shared-passphrase requirement.
- **B:** That selects enterprise authentication rather than the required shared passphrase.
- **C:** An open WLAN does not provide the required WPA2 protection.
- **D:** Enabling legacy WPA does not change the key management to PSK.

**Further reading**

- [Cisco Wireless Controller Configuration Guide, Release 8.10: WLAN Security](https://www.cisco.com/c/en/us/td/docs/wireless/controller/8-10/config-guide/b_cg810/wlan_security.html) — Configuring WPA1+WPA2 (GUI)

---

## CCNA1-091 · Automation and Programmability

Objectives: 6.1 · single · Applied

A team replaces individual CLI changes with a shared configuration template. A mistaken server address in the template is then applied consistently to 40 switches. Which conclusion about automation is supported by this outcome?

- **A.** A successful automation run proves that the resulting configuration meets the team's intent.
- **B.** Automation can reduce repetitive entry errors while also distributing a template error widely.
- **C.** Each switch must have independently introduced the same typing error.
- **D.** Automation eliminates the need to validate configuration inputs.

**Answer: B**

Automation reduces repeated manual work and can improve configuration consistency. Here, that repeatability spread an incorrect input; completion of a workflow and correctness of its inputs are separate concerns.

**Option explanations**

- **A:** Successful delivery of an incorrect address does not establish correctness.
- **B:** Reusing one template improves consistency, including consistency of mistakes.
- **C:** The scenario identifies the shared template as the source.
- **D:** The incorrect input demonstrates why validation remains necessary.

**Further reading**

- [What Is Network Automation?](https://www.cisco.com/site/us/en/learn/topics/networking/what-is-network-automation.html) — What is network automation?; Why automate your network?; Step 3: provisioning and connecting

---

## CCNA1-092 · Automation and Programmability

Objectives: 6.2, 6.3.a · single · Foundation

In a traditional network, routers calculate routes locally. A proposed SDN design instead uses a logically centralized controller to calculate forwarding rules and install them on switches. Which statement correctly compares the two designs?

- **A.** The SDN controller must forward every user packet itself.
- **B.** Traditional routers have data planes but no control planes.
- **C.** Logical centralization requires exactly one physical controller server.
- **D.** Control decisions are centralized in the proposed design, while switches execute forwarding rules.

**Answer: D**

The proposed design separates controller decisions from switch forwarding. Traditional routers perform control calculations locally; logically centralized control does not imply centralized forwarding or a single physical controller.

**Option explanations**

- **A:** Installing rules does not move packet forwarding to the controller.
- **B:** Their local route calculations are control-plane work.
- **C:** Logical organization does not specify the physical server count.
- **D:** The controller determines rules; device data planes apply them.

**Further reading**

- [RFC 7426: Software-Defined Networking (SDN): Layers and Architecture Terminology](https://www.rfc-editor.org/rfc/rfc7426.html#section-3.1) — 3.1 Overview; 3.5.3 Locality

---

## CCNA1-093 · Automation and Programmability

Objectives: 6.3, 6.3.a · matching · Foundation

Match each description in a Cisco SD-Access fabric to its architectural term. Use each term once.

1. The physical routed infrastructure providing IP reachability between fabric nodes
2. A logical virtual network carried across that physical infrastructure
3. The function that exchanges endpoint-to-location mappings using LISP
4. The function that encapsulates and transports endpoint traffic using VXLAN

- **A.** Overlay network
- **B.** Data plane
- **C.** Underlay network
- **D.** Overlay control plane

**Answer: 1 → C; 2 → A; 3 → D; 4 → B**

An SD-Access fabric places virtual overlays on a routed underlay. Its LISP control plane supplies mappings, while its VXLAN data plane carries endpoint traffic.

**Option explanations**

- **A:** This is the logical network carried over the underlay.
- **B:** This function carries endpoint packets using VXLAN encapsulation.
- **C:** This physical IP foundation transports traffic between fabric nodes.
- **D:** LISP mappings supply location information used for forwarding decisions.

**Further reading**

- [Software-Defined Access](https://www.cisco.com/c/en/us/td/docs/solutions/CVD/Campus/cisco-sda-design-guide.html) — Overlay control plane – LISP; Data plane – VXLAN; Underlay network; Overlay network

---

## CCNA1-094 · Automation and Programmability

Objectives: 6.3.b · multiple · Applied

A service portal requests network policy changes through a controller. The controller configures switches through their management interfaces. Which two descriptions correctly identify the API relationships? Select two.

- **A.** The controller-to-switch relationship is northbound because the controller initiates the request.
- **B.** The service-portal-to-controller relationship uses the controller's northbound API.
- **C.** User traffic between two servers is a southbound API exchange.
- **D.** A switch's API reply becomes northbound because it travels toward the controller.
- **E.** The controller-to-switch relationship uses a southbound interface.

**Answer: B, E**

Northbound identifies the application-to-controller boundary. Southbound identifies the controller-to-device boundary; these labels describe architectural relationships, not the direction of each individual message.

**Option explanations**

- **A:** Initiator direction does not determine the architectural relationship.
- **B:** The portal is an application consuming the controller's services.
- **C:** Ordinary user traffic is not this controller-to-device management relationship.
- **D:** Both request and reply belong to the same southbound relationship.
- **E:** Southbound interfaces connect controllers with managed network devices.

**Further reading**

- [Software-Defined Networking](https://www.cisco.com/c/en/us/solutions/software-defined-networking/overview.html) — SDN elements

---

## CCNA1-095 · Automation and Programmability

Objectives: 6.4 · single · Applied

A network operations platform has two features. Feature X learns patterns in historical telemetry to estimate the likelihood of a future performance issue. Feature Y uses a trained language model to draft a troubleshooting explanation from incident details. Which classification is correct?

- **A.** X is predictive AI; Y is generative AI; both use machine learning.
- **B.** X is generative AI; Y is predictive AI; both use machine learning.
- **C.** Both are generative AI because both produce an output.
- **D.** Both are predictive AI because both use previously collected information.

**Answer: A**

Predictive AI uses learned patterns to estimate outcomes. Generative AI creates content, such as a troubleshooting explanation; a trained language model is a machine-learning model.

**Option explanations**

- **A:** X estimates an outcome, while Y creates explanatory text.
- **B:** This reverses forecasting and content generation.
- **C:** Producing any output does not make a forecasting model generative.
- **D:** Training data also supports generative models; the described task distinguishes them.

**Further reading**

- [What is AIOps?](https://developer.cisco.com/articles/what-is-aiops/) — The core components of AIOps
- [Cisco Predictive Networks](https://www.cisco.com/c/m/en_us/solutions/predictive-networks/index.html) — What are customers saying? — following paragraph describing telemetry, learned patterns, and predictions
- [How To Get Started Using LLMs in IT and Network Engineering](https://blogs.cisco.com/developer/how-to-get-started-using-llms-in-it-and-network-engineering) — Introducing the LLM; Applying LLMs to IT and Network Engineering Use Cases

---

## CCNA1-096 · Automation and Programmability

Objectives: 6.5 · single · Applied

The exhibit summarizes an API's documented resources. POST to the collection creates a new policy. Policy 42 exists, and an engineer must replace its full representation in one request. Which method, URI, and CRUD operation fit?

| Resource | URI | Supported methods |
| --- | --- | --- |
| Policy collection | /policies | GET, POST |
| Existing policy 42 | /policies/42 | GET, PUT, DELETE |

- **A.** POST /policies — Create
- **B.** GET /policies/42 — Read
- **C.** PUT /policies/42 — Update
- **D.** DELETE /policies/42 — Delete

**Answer: C**

PUT targets the existing policy's URI with its complete replacement representation. This is an Update operation in CRUD terminology.

**Option explanations**

- **A:** This targets collection creation, not replacement of policy 42.
- **B:** GET retrieves the representation without requesting replacement.
- **C:** PUT supplies replacement state to the existing resource.
- **D:** Deletion does not request replacement with the supplied policy.

**Further reading**

- [RFC 9110: HTTP Semantics](https://www.rfc-editor.org/rfc/rfc9110.html#section-9.3.4) — 9.3.1 GET; 9.3.3 POST; 9.3.4 PUT; 9.3.5 DELETE

---

## CCNA1-097 · Automation and Programmability

Objectives: 6.5 · multiple · Applied

An HTTPS API requires an OAuth 2.0 bearer token in the Authorization header and a JSON request body. A client already has a valid token. Which two actions meet these requirements? Select two.

- **A.** Set Authorization to Bearer followed by the token.
- **B.** Use Accept: application/json instead of identifying the request body's format.
- **C.** Put the token after Basic in the Authorization header.
- **D.** Send valid JSON with Content-Type: application/json.
- **E.** Omit the token because JSON supplies authentication.

**Answer: A, D**

The bearer credential and JSON media type serve different purposes. Authentication identifies the presented credential; Content-Type describes the body.

**Option explanations**

- **A:** This supplies the required bearer credential.
- **B:** Accept expresses response-format preferences, not the request body's media type.
- **C:** Basic represents username/password credentials, not this bearer-token scheme.
- **D:** Content-Type identifies the submitted representation's format.
- **E:** JSON is data encoding, not an authentication mechanism.

**Further reading**

- [RFC 6750: The OAuth 2.0 Authorization Framework: Bearer Token Usage](https://www.rfc-editor.org/rfc/rfc6750.html#section-2.1) — 2.1 Authorization Request Header Field
- [RFC 9110: HTTP Semantics](https://www.rfc-editor.org/rfc/rfc9110.html#section-8.3) — 8.3 Content-Type; 12.5.1 Accept
- [RFC 7617: The 'Basic' HTTP Authentication Scheme](https://www.rfc-editor.org/rfc/rfc7617.html#section-2) — 2 The 'Basic' Authentication Scheme

---

## CCNA1-098 · Automation and Programmability

Objectives: 6.6 · single · Foundation

A team wants Ansible to apply interface descriptions to supported IOS switches. It will use a YAML playbook and the network_cli connection plugin. Which description matches this approach?

- **A.** Every switch must run a persistent Ansible agent that pulls the playbook.
- **B.** The YAML playbook replaces each switch's operating system.
- **C.** The switches execute the Ansible network modules in their own Python interpreters.
- **D.** The control node executes network modules and communicates with switches using CLI over SSH.

**Answer: D**

The YAML playbook organizes tasks that call modules. For this network automation approach, modules run on the control node and network_cli provides CLI communication over SSH.

**Option explanations**

- **A:** The specified network workflow executes modules on the control node.
- **B:** A playbook defines automation tasks, not a replacement network operating system.
- **C:** These network modules execute on the Ansible control node.
- **D:** This is the documented behavior of the network_cli approach.

**Further reading**

- [How Network Automation is Different](https://docs.ansible.com/projects/ansible/latest/network/getting_started/network_differences.html) — Execution on the control node; Multiple communication protocols
- [Ansible playbooks](https://docs.ansible.com/projects/ansible/latest/playbook_guide/playbooks_intro.html) — Playbook syntax; Playbook execution

---

## CCNA1-099 · Automation and Programmability

Objectives: 6.6 · single · Applied

An engineer declares a virtual network and two subnets in Terraform configuration. A suitable provider supports these resources. The team wants to inspect proposed changes before provisioning them. Which description correctly identifies Terraform's capabilities?

- **A.** A plan describes proposed changes; an apply performs them through the provider, with state tracking managed resources.
- **B.** Generating a plan creates the network immediately, while apply only displays it.
- **C.** A provider learns packet routes and replaces the virtual network's routing protocol.
- **D.** State contains only console logs and has no relationship to configured resources.

**Answer: A**

Terraform can manage infrastructure from declarative configuration using provider integrations. Planning previews proposed operations; applying carries them out, and state maintains the association with managed objects.

**Option explanations**

- **A:** This combines Terraform's planning, execution, provider, and state roles.
- **B:** This reverses the planning and execution phases.
- **C:** The provider integrates Terraform with resource APIs; it is not a routing protocol.
- **D:** State records bindings between configuration resources and real objects.

**Further reading**

- [What is Terraform?](https://developer.hashicorp.com/terraform/intro) — How does Terraform work?
- [State](https://developer.hashicorp.com/terraform/language/state) — State

---

## CCNA1-100 · Automation and Programmability

Objectives: 6.7 · single · Foundation

Which statement correctly interprets the JSON document in the exhibit?

```text
{
  "devices": [
    {"name": "R1", "managed": true, "vlans": [10, 20]},
    {"name": "R2", "managed": false, "vlans": [], "serial": null}
  ],
  "count": 2
}
```

- **A.** devices is an object containing two arrays.
- **B.** count is a number, and R2's vlans value is an empty array.
- **C.** R2's managed value is the string false.
- **D.** R2's serial value is an empty string.

**Answer: B**

The document has an object at its root. devices is an array of objects; count is numeric, [] is an empty array, and the unquoted false and null are distinct JSON literals.

**Option explanations**

- **A:** Square brackets make devices an array; its two elements are objects.
- **B:** The unquoted 2 is numeric, and [] contains zero elements.
- **C:** The unquoted false is a Boolean literal, not a string.
- **D:** null is distinct from an empty string, which would be written as two quotation marks.

**Further reading**

- [RFC 8259: The JavaScript Object Notation (JSON) Data Interchange Format](https://www.rfc-editor.org/rfc/rfc8259.html#section-3) — 3 Values; 4 Objects; 5 Arrays; 6 Numbers; 7 Strings

---
