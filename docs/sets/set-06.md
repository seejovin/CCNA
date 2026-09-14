# CCNA Practice — Set 06

100 original questions aligned to CCNA 200-301 v1.1. No interactive labs.

Answers and explanations follow each question. For an unrevealed attempt, use the Streamlit app.

Content review date: 2026-09-14.

## CCNA6-001 · Network Fundamentals

Objectives: 1.1.b · single · Foundation

A Layer 3 switch has routing enabled and an interface in each of two IP subnets. How does this differ from operating the same device only as a Layer 2 switch?

- **A.** It must stop using MAC addresses on Ethernet
- **B.** It can never forward frames within a VLAN
- **C.** It can forward packets between the configured IP networks
- **D.** It automatically encrypts all routed packets

**Answer: C**

A platform’s capabilities depend on its effective configuration. Enabling routing adds a Layer 3 function while Ethernet remains the link transport.

**Option explanations**

- **A:** Routed Ethernet still uses link-layer headers.
- **B:** Layer 2 switching and Layer 3 routing can coexist.
- **C:** The enabled routing function supplies inter-subnet forwarding.
- **D:** Routing enablement does not imply encryption.

**Further reading**

- [Comparing Layer 3 and Layer 2 Switches](https://documentation.meraki.com/Switching/MS_-_Switches/Design_and_Configure/Configuration_Guides/Layer_3_Switching/Comparing_Layer_3_and_Layer_2_Switches) — Comparing Layer 3 and Layer 2 Switches (main article)

---

## CCNA6-002 · Network Fundamentals

Objectives: 1.2.b · single · Applied

In a three-tier campus, access switches connect user devices, distribution aggregates access blocks, and the core connects distribution blocks. Which failure is most directly an access-layer fault?

- **A.** One floor’s endpoint-facing switch loses power
- **B.** The central interconnection between distribution blocks fails
- **C.** Every distribution-to-core route is withdrawn
- **D.** The offsite cloud provider stops its application service

**Answer: A**

Classify the failed function in the hierarchy. A local endpoint attachment failure belongs to the access layer even when its users lose remote services.

**Option explanations**

- **A:** The failed device directly provides endpoint attachment.
- **B:** That concerns the core role.
- **C:** That affects aggregation/core connectivity.
- **D:** That is outside the specified campus access function.

**Further reading**

- [Campus LAN and Wireless LAN Solution Design Guide](https://www.cisco.com/c/en/us/td/docs/solutions/CVD/Campus/cisco-campus-lan-wlan-design-guide.html) — Hierarchical design model; Access layer

---

## CCNA6-003 · Network Fundamentals

Objectives: 1.3.a · single · Applied

A contractor proposes a 160 m uninterrupted 1000BASE-T copper channel between two switches. The project requires standards-compliant reach with no intermediate active equipment. What is the appropriate response?

- **A.** Accept it because the cable jacket is blue
- **B.** Accept it if both IP masks are /16
- **C.** Force half duplex to double the supported distance
- **D.** Use a suitable supported fiber link or redesign the physical path

**Answer: D**

Physical medium constraints must be met before higher-layer configuration matters. A compatible optical solution can satisfy longer distances.

**Option explanations**

- **A:** Jacket color does not extend standardized reach.
- **B:** IP masks do not alter electrical channel limits.
- **C:** That does not satisfy the proposed gigabit copper specification.
- **D:** The proposed copper channel exceeds normal 100 m reach.

**Further reading**

- [Configure and Verify Ethernet 10/100/1000Mb Half/Full Duplex Auto-Negotiation](https://www.cisco.com/c/en/us/support/docs/lan-switching/ethernet/10561-3.html) — Background Information; Auto-Negotiation on Catalyst Switches that Run Cisco IOS Software
- [Cisco 10GBASE SFP+ Modules Data Sheet](https://www.cisco.com/c/en/us/products/collateral/interfaces-modules/transceiver-modules/data_sheet_c78-455693.html) — Cisco SFP-10G-SR module; Cisco SFP-10G-LR module; Cisco SFP-10G-T-X module

---

## CCNA6-004 · Network Fundamentals

Objectives: 1.4 · single · Applied

The counters in the exhibit were cleared immediately before a 10-minute test. Duplex is verified full at both ends. What is the best next focus?

```text
Operational duplex: full
Input packets: 180000
CRC errors: 430
Collisions: 0
```

- **A.** Change the subnet mask to remove CRC errors
- **B.** Investigate physical-layer integrity and interface hardware
- **C.** Treat collisions as normal because the link is full duplex
- **D.** Conclude DNS is definitively the cause

**Answer: B**

Fresh CRC errors are link-integrity evidence. They do not by themselves prove which cable or hardware component is defective.

**Option explanations**

- **A:** A mask change does not correct damaged Ethernet frames.
- **B:** New CRC errors justify cable, optic, connector, or hardware checks.
- **C:** No collisions are shown, and full duplex does not use contention collisions.
- **D:** Frame error counters do not establish a DNS fault.

**Further reading**

- [Configure and Verify Ethernet 10/100/1000Mb Half/Full Duplex Auto-Negotiation](https://www.cisco.com/c/en/us/support/docs/lan-switching/ethernet/10561-3.html) — Background Information; Auto-Negotiation on Catalyst Switches that Run Cisco IOS Software

---

## CCNA6-005 · Network Fundamentals

Objectives: 1.5 · single · Applied

An application sends two messages of 40 bytes each over one TCP connection. Which statement about receiver application reads is correct?

- **A.** Each read must return exactly one 40-byte message
- **B.** TCP will combine the messages into one UDP datagram
- **C.** The application needs its own framing to identify message boundaries
- **D.** TCP guarantees two separate Ethernet frames

**Answer: C**

TCP preserves ordered bytes, not the sender’s write boundaries. Length fields or delimiters can supply application-level framing.

**Option explanations**

- **A:** TCP does not preserve application message boundaries.
- **B:** TCP does not change transport protocol in this way.
- **C:** TCP delivers a byte stream whose read sizes can vary.
- **D:** Segmentation and link framing are independent of application write calls.

**Further reading**

- [RFC 9293: Transmission Control Protocol (TCP)](https://www.rfc-editor.org/rfc/rfc9293.html#section-2.2) — 2.2. Key TCP Concepts

---

## CCNA6-006 · Network Fundamentals

Objectives: 1.6 · single · Applied

A host is 192.168.60.29/28. The router interface is 192.168.60.17/28, and .18 is unused. Which proposed change keeps an ordinary valid host on the same subnet?

- **A.** Change the host to 192.168.60.18/28
- **B.** Change the host to 192.168.60.16/28
- **C.** Change the host to 192.168.60.31/28
- **D.** Change the host to 192.168.60.33/28

**Answer: A**

The two devices currently belong to 192.168.60.16/28. Preserve the prefix and choose an unused address between .17 and .30.

**Option explanations**

- **A:** The address is usable in the .16–.31 subnet.
- **B:** That is the subnet identifier.
- **C:** That is the directed broadcast address.
- **D:** That belongs to the next /28.

**Further reading**

- [Configure IP Addresses and Unique Subnets for New Users](https://www.cisco.com/c/en/us/support/docs/ip/routing-information-protocol-rip/13788-3.html) — Network Masks; Understand Subnetting; VLSM Example

---

## CCNA6-007 · Network Fundamentals

Objectives: 1.7 · single · Foundation

An internal router has routes between private subnets 10.1.0.0/24 and 10.2.0.0/24. Must it translate addresses to route traffic between them?

- **A.** Yes, because routers reject every RFC 1918 destination
- **B.** Yes, because /24 prefixes are illegal inside 10.0.0.0/8
- **C.** Yes, because private addresses are link-local
- **D.** No; ordinary internal routing can forward them without NAT

**Answer: D**

Private IPv4 addresses are usable across an organization’s routed network. Their non-global nature does not prohibit internal routing.

**Option explanations**

- **A:** Routers can route private prefixes within configured networks.
- **B:** Classless subnets of the private block are valid.
- **C:** RFC 1918 scope is not limited to one physical link.
- **D:** NAT is not a prerequisite for routing between these private subnets.

**Further reading**

- [RFC 1918: Address Allocation for Private Internets](https://www.rfc-editor.org/rfc/rfc1918#section-3) — 3. Private Address Space

---

## CCNA6-008 · Network Fundamentals

Objectives: 1.8 · single · Applied

Which IPv6 text string is invalid because it uses zero compression ambiguously?

- **A.** 2001:db8:0:5::1
- **B.** 2001::db8::1
- **C.** 2001:0db8:0000:0005:0000:0000:0000:0001
- **D.** 2001:db8:0:5:0:0:0:1

**Answer: B**

The double-colon compression symbol may occur only once in a valid address. Leading-zero suppression inside individual hextets is separate.

**Option explanations**

- **A:** One double colon can represent the omitted zero hextets.
- **B:** Two double colons make the positions of omitted hextets ambiguous.
- **C:** Eight explicit hextets are valid.
- **D:** Leading zeros may be omitted in each hextet.

**Further reading**

- [RFC 4291: IP Version 6 Addressing Architecture](https://www.rfc-editor.org/rfc/rfc4291#section-2.3) — 2.3. Text Representation of Address Prefixes; 2.4. Address Type Identification; 2.5.6. Link-Local IPv6 Unicast Addresses; 2.7. Multicast Addresses

---

## CCNA6-009 · Network Fundamentals

Objectives: 1.9.a, 1.9.b · multiple · Applied

Which TWO statements about IPv6 anycast are accurate? Select two.

- **A.** Anycast has a mandatory ff prefix
- **B.** Anycast inherently sends a copy to every instance
- **C.** An anycast address is assigned to multiple interfaces for the same service role
- **D.** Its textual format can be indistinguishable from unicast
- **E.** It guarantees the same server handles all future connections

**Answer: C, D**

Anycast is defined by assignment and routing behavior, not a separate visible prefix. Its path can change when routing changes.

**Option explanations**

- **A:** ff identifies multicast, not anycast.
- **B:** Delivery is toward a selected instance, not all members.
- **C:** Multiple instances share the destination address.
- **D:** Anycast addresses are drawn from unicast address space.
- **E:** Routing changes can change the selected instance.

**Further reading**

- [RFC 4291: IP Version 6 Addressing Architecture](https://www.rfc-editor.org/rfc/rfc4291#section-2.3) — 2.3. Text Representation of Address Prefixes; 2.4. Address Type Identification; 2.5.6. Link-Local IPv6 Unicast Addresses; 2.7. Multicast Addresses
- [RFC 4786: Operation of Anycast Services](https://www.rfc-editor.org/rfc/rfc4786#section-2) — 2. Terminology; 3.1. General Description; 3.2. Goals

---

## CCNA6-010 · Network Fundamentals

Objectives: 1.10, 1.8 · single · Applied

The Linux display shows a global-scope IPv6 address and a link-local address on enp2s0. Which value supplies the interface’s configured global /64 prefix?

```text
$ ip -6 address show dev enp2s0
inet6 2001:db8:55:8::20/64 scope global
inet6 fe80::20/64 scope link
```

- **A.** fe80::/64
- **B.** 2001:db8:55::/48
- **C.** 2001:db8:55:8::20/128
- **D.** 2001:db8:55:8::/64

**Answer: D**

Read the prefix length with its address. Multiple addresses on one interface do not make their scopes or network prefixes interchangeable.

**Option explanations**

- **A:** That is the displayed link-local prefix.
- **B:** This discards the configured fourth-hextet subnet.
- **C:** This denotes the specific host, not its /64.
- **D:** The first four hextets define the displayed global prefix.

**Further reading**

- [ip-address(8) — Linux manual page](https://man7.org/linux/man-pages/man8/ip-address.8.html) — ip address show; scope; address flags
- [RFC 4291: IP Version 6 Addressing Architecture](https://www.rfc-editor.org/rfc/rfc4291#section-2.3) — 2.3. Text Representation of Address Prefixes; 2.4. Address Type Identification; 2.5.6. Link-Local IPv6 Unicast Addresses; 2.7. Multicast Addresses

---

## CCNA6-011 · Network Fundamentals

Objectives: 1.11.a, 1.11.c · single · Applied

APs A and B hear one another and use the same 20 MHz channel. Their SSIDs differ. Which problem can still occur?

- **A.** Shared-channel airtime contention
- **B.** An unavoidable duplicate IPv4 address
- **C.** A forced optical wavelength mismatch
- **D.** A mandatory TCP port collision

**Answer: A**

Devices using a shared channel can compete for airtime. Naming the networks differently does not separate the physical medium.

**Option explanations**

- **A:** Different SSID names do not create separate RF spectrum.
- **B:** SSID difference does not determine assigned IP addresses.
- **C:** These are wireless RF channels, not fiber wavelengths.
- **D:** RF channel sharing is unrelated to TCP port assignment.

**Further reading**

- [Channel Planning Best Practices](https://documentation.meraki.com/Wireless/Design_and_Configure/Architecture_and_Best_Practices/Channel_Planning_Best_Practices) — 2.4 GHz

---

## CCNA6-012 · Network Fundamentals

Objectives: 1.12 · multiple · Applied

A team wants two tenants with identical IPv4 prefixes to remain in separate routed contexts on one router. Which TWO design statements are sound? Select two.

- **A.** Put both tenant interfaces in one routing table with identical connected prefixes
- **B.** Associate each tenant’s interfaces with its intended VRF
- **C.** Assume creating VRFs encrypts all tenant data
- **D.** Control any deliberate route leaking between the VRFs
- **E.** Assume a VRF is a container runtime

**Answer: B, D**

VRFs separate routing and forwarding state. Any deliberate exchange of reachability changes that isolation boundary.

**Option explanations**

- **A:** A common routing context does not supply the requested separation.
- **B:** Ingress context identifies the appropriate routing table.
- **C:** VRFs provide forwarding separation, not encryption.
- **D:** Interconnection must be explicitly designed rather than assumed isolated forever.
- **E:** VRFs do not launch application process containers.

**Further reading**

- [IP Routing Configuration Guide, Cisco IOS XE Dublin 17.12.x (Catalyst 9500 Switches): Configuring VRF-lite](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst9500/software/release/17-12/configuration_guide/rtng/b_1712_rtng_9500_cg/configuring_vrf_lite.html) — Information About VRF-lite; Guidelines for Configuring VRF-lite

---

## CCNA6-013 · Network Fundamentals

Objectives: 1.13.b, 1.13.d · multiple · Applied

Which TWO fields are essential to interpret the dynamic forwarding entries shown? Select two.

```text
VLAN   MAC address       Type      Ports
10     0011.2200.0033     DYNAMIC   Gi1/0/3
20     0011.2200.0033     DYNAMIC   Gi1/0/8
```

- **A.** The host’s DNS resolver address
- **B.** The destination TCP port
- **C.** The VLAN associated with each MAC entry
- **D.** The port associated with each MAC entry
- **E.** The client’s default IPv6 route

**Answer: C, D**

A MAC address table relates Layer 2 addresses to interfaces within VLAN context. Do not interpret it as an IP routing table.

**Option explanations**

- **A:** DNS settings are not shown or required for these mappings.
- **B:** The table describes Layer 2 location, not transport sessions.
- **C:** The same MAC can appear in distinct VLAN contexts.
- **D:** The port identifies the learned forwarding location.
- **E:** That belongs to a different forwarding layer.

**Further reading**

- [Configuring MAC Address Tables](https://www.cisco.com/c/en/us/td/docs/switches/datacenter/nexus5500/sw/layer2/7x/b_5500_Layer2_Config_7x/config_mac_address_tables.pdf) — Information About MAC Addresses (page 1); Configuring the Aging Time for the MAC Table (page 2)

---

## CCNA6-014 · Network Fundamentals

Objectives: 1.1.c · single · Applied

A security requirement distinguishes two applications that both use TCP 443. Which component capability addresses that requirement more directly than a port-only rule?

- **A.** Increasing switch MAC aging time
- **B.** Using a passive copper coupler
- **C.** Replacing all IPv4 addresses with IPv6
- **D.** Application-aware inspection on an NGFW

**Answer: D**

A shared port is not a unique application identifier. Application-aware inspection can support a more specific policy, subject to visibility and configuration.

**Option explanations**

- **A:** MAC aging does not identify applications.
- **B:** A coupler does not apply application policy.
- **C:** The address family does not inherently identify the application.
- **D:** It can apply policy beyond the shared transport port.

**Further reading**

- [NGFW vs traditional firewall: what’s different [Explained]](https://www.cisco.com/site/us/en/learn/topics/security/what-is-a-next-generation-firewall.html) — Next-generation firewall overview

---

## CCNA6-015 · Network Fundamentals

Objectives: 1.6 · single · Applied

A /24 is divided into /29 subnets. How many subnets are created, and how many ordinary usable addresses does each provide?

- **A.** 32 subnets, 6 usable addresses each
- **B.** 8 subnets, 30 usable addresses each
- **C.** 16 subnets, 14 usable addresses each
- **D.** 32 subnets, 8 usable addresses each

**Answer: A**

Subtract prefix lengths to count subnet bits and subtract from 32 to count host bits. Ordinary subnet host counts exclude two boundary addresses.

**Option explanations**

- **A:** Five borrowed bits create 32 blocks; three host bits leave six usable addresses.
- **B:** That describes a /24-to-/27 split.
- **C:** That describes a /24-to-/28 split.
- **D:** Eight is the total address count, including network and broadcast.

**Further reading**

- [Configure IP Addresses and Unique Subnets for New Users](https://www.cisco.com/c/en/us/support/docs/ip/routing-information-protocol-rip/13788-3.html) — Network Masks; Understand Subnetting; VLSM Example

---

## CCNA6-016 · Network Fundamentals

Objectives: 1.9.c · single · Applied

A router’s local-link all-routers group is ff02::2. Which part of that address distinguishes it from the all-nodes group ff02::1?

- **A.** The initial ff byte
- **B.** The final group identifier
- **C.** The scope value 2
- **D.** A hidden subnet mask stored in the address

**Answer: B**

Both groups have the same multicast type and link-local scope. Their group identifiers distinguish all routers from all nodes.

**Option explanations**

- **A:** Both addresses are multicast.
- **B:** The final value identifies the different reserved multicast groups.
- **C:** Both have the same link-local scope.
- **D:** The distinction is in the explicit group bits.

**Further reading**

- [RFC 4291: IP Version 6 Addressing Architecture](https://www.rfc-editor.org/rfc/rfc4291#section-2.3) — 2.3. Text Representation of Address Prefixes; 2.4. Address Type Identification; 2.5.6. Link-Local IPv6 Unicast Addresses; 2.7. Multicast Addresses

---

## CCNA6-017 · Network Fundamentals

Objectives: 1.11.d · single · Foundation

A WLAN administrator chooses encryption settings. Which objective is specifically addressed by encrypting wireless data frames?

- **A.** Increasing the number of RF channels
- **B.** Reducing the copper cable length
- **C.** Protecting data confidentiality over the radio link
- **D.** Assigning globally unique MAC addresses

**Answer: C**

Encryption addresses protection of data on the wireless link. It does not substitute for RF planning or addressing.

**Option explanations**

- **A:** Encryption does not allocate spectrum.
- **B:** Wireless encryption does not alter cabling.
- **C:** Encryption obscures protected frame payloads to unauthorized observers.
- **D:** Address allocation is a separate mechanism.

**Further reading**

- [Wireless Fundamentals: Encryption and Authentication](https://documentation.meraki.com/Wireless/Design_and_Configure/Architecture_and_Best_Practices/Wireless_Fundamentals:_Encryption_and_Authentication) — WPA2 – Personal; Hidden SSID

---

## CCNA6-018 · Network Fundamentals

Objectives: 1.13.a, 1.13.c · single · Applied

All dynamic MAC entries are cleared during maintenance, but VLANs and forwarding ports remain unchanged. What is likely for the first unicast frames to previously learned destinations?

- **A.** Unknown destinations may be flooded until relearned
- **B.** Every VLAN is automatically deleted
- **C.** IP packets become permanently unroutable everywhere
- **D.** The switch must obtain destination locations from DNS

**Answer: A**

The table can rebuild from new source traffic. Temporary unknown-unicast flooding is distinct from loss of VLAN configuration.

**Option explanations**

- **A:** The missing mappings initially remove directed forwarding information.
- **B:** Clearing dynamic MAC entries does not delete VLAN configuration.
- **C:** Layer 2 mappings can be learned again.
- **D:** Ethernet source learning does not query DNS.

**Further reading**

- [Configuring MAC Address Tables](https://www.cisco.com/c/en/us/td/docs/switches/datacenter/nexus5500/sw/layer2/7x/b_5500_Layer2_Config_7x/config_mac_address_tables.pdf) — Information About MAC Addresses (page 1); Configuring the Aging Time for the MAC Table (page 2)

---

## CCNA6-019 · Network Fundamentals

Objectives: 1.2.c · single · Challenge

A leaf has 48 server-facing ports at 10 Gb/s and four spine uplinks at 40 Gb/s. All speeds are usable as stated; ignore overhead. What is its aggregate downlink-to-uplink bandwidth ratio?

- **A.** 1:1
- **B.** 4:1
- **C.** 12:1
- **D.** 3:1

**Answer: D**

Use aggregate bandwidth rather than just port counts. This ratio indicates possible contention if all servers simultaneously require the uplinks at full rate.

**Option explanations**

- **A:** Downlinks total 480 Gb/s, while uplinks total 160 Gb/s.
- **B:** That ratio would require only 120 Gb/s of uplink capacity.
- **C:** This divides port counts without accounting for different speeds.
- **D:** 480 divided by 160 equals 3.

**Further reading**

- [Cisco Massively Scalable Data Center Network Fabric Design and Operation White Paper](https://www.cisco.com/c/en/us/products/collateral/switches/nexus-9000-series-switches/white-paper-c11-743245.html) — MSDC Layer 3 IP fabric design evolution; Cisco MSDC design example 1: Two-tiered spine-leaf topology

---

## CCNA6-020 · Network Fundamentals

Objectives: 1.3.a, 1.3.b · matching · Applied

Match each physical design requirement or observation with the appropriate medium/link property. Use each option once.

1. A legacy hub connects stations that detect collisions.
2. An access link must deliver standards-based PoE to a phone.
3. A supported long-reach optic pair serves a distant building using the specified optical cable.
4. A server and switch concurrently send to each other on their dedicated full-duplex link.

- **A.** Full-duplex point-to-point Ethernet
- **B.** Copper twisted pair
- **C.** Single-mode optical fiber
- **D.** Half-duplex shared Ethernet

**Answer: 1 → D; 2 → B; 3 → C; 4 → A**

Distinguish medium selection from access behavior. Optical versus copper and shared versus point-to-point answer different physical-design questions.

**Option explanations**

- **A:** A dedicated link supports simultaneous transmission and reception.
- **B:** The electrical medium can carry both compatible Ethernet data and PoE.
- **C:** Matching long-reach optics can support an interbuilding distance beyond ordinary copper reach.
- **D:** A hub repeats signals among stations that contend on a common medium.

**Further reading**

- [Cisco 10GBASE SFP+ Modules Data Sheet](https://www.cisco.com/c/en/us/products/collateral/interfaces-modules/transceiver-modules/data_sheet_c78-455693.html) — Cisco SFP-10G-SR module; Cisco SFP-10G-LR module; Cisco SFP-10G-T-X module
- [Configure and Verify Ethernet 10/100/1000Mb Half/Full Duplex Auto-Negotiation](https://www.cisco.com/c/en/us/support/docs/lan-switching/ethernet/10561-3.html) — Background Information; Auto-Negotiation on Catalyst Switches that Run Cisco IOS Software
- [Interface and Hardware Components Configuration Guide, Cisco IOS XE 17.14.x (Catalyst 9200 Switches): Configuring Power over Ethernet](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst9200/software/release/17-14/configuration_guide/int_hw/b_1714_int_and_hw_9200_cg/configuring_poe.html) — Powered-Device Detection and Initial Power Allocation

---

## CCNA6-021 · Network Access

Objectives: 2.1 · multiple · Applied

VLAN 72 must cross SW-A, transit SW-B, and SW-C. SW-B has no local users in VLAN 72. All switches use local VLAN configuration without VTP propagation. Which TWO requirements still apply at SW-B? Select TWO.

- **A.** SW-B must have an SVI IP in VLAN 72 solely to switch its frames.
- **B.** The incoming and outgoing trunks must permit VLAN 72.
- **C.** VLAN 72 must exist and be active on SW-B.
- **D.** Every access port on SW-B must join VLAN 72.

**Answer: B, C**

A transit VLAN still needs local availability and working trunk carriage. It does not require local clients or a routing interface on every switch.

**Option explanations**

- **A:** Layer 2 transit forwarding does not require a local IP gateway.
- **B:** Transit data needs an admitted path through both links.
- **C:** A transit switch still needs the VLAN’s Layer 2 forwarding instance.
- **D:** Unrelated access ports do not need to join the transit VLAN.

**Further reading**

- [VLAN Configuration Guide, Cisco IOS XE 17.15.x — Configuring VLANs](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst9300/software/release/17-15/configuration_guide/vlan/b_1715_vlan_9300_cg/configuring_vlans.html) — Supported VLANs; Deleting a VLAN; VLAN Port Membership Modes
- [VLAN Configuration Guide, Cisco IOS XE 17.15.x — Configuring VLAN Trunks](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst9300/software/release/17-15/configuration_guide/vlan/b_1715_vlan_9300_cg/configuring_vlan_trunks.html) — Allowed VLANs on a Trunk; Configuring the Native VLAN for Untagged Traffic

---

## CCNA6-022 · Network Access

Objectives: 2.1.c · single · Applied

A router-on-a-stick design uses subinterface Gi0/1.900 to route VLAN 45. Its encapsulation is dot1Q 45 and addressing matches the VLAN 45 subnet. The trunk allows tagged VLAN 45. Which assessment is correct?

```text
interface GigabitEthernet0/1.900
 encapsulation dot1Q 45
 ip address 10.45.0.1 255.255.255.0
```

- **A.** The subinterface suffix may differ from the VLAN ID; encapsulation 45 supplies the binding.
- **B.** The router must use VLAN 900 because of the suffix.
- **C.** The switch must permit VLAN 900 instead of VLAN 45.
- **D.** The subnet mask must be /9 to match the suffix.

**Answer: A**

Read the encapsulation statement instead of inferring VLAN membership from the subinterface name. The naming convention is optional.

**Option explanations**

- **A:** The suffix is an interface identifier rather than the on-wire VLAN selector.
- **B:** The explicit encapsulation command determines the tag.
- **C:** The routed subinterface exchanges frames tagged for VLAN 45.
- **D:** Subinterface numbering does not constrain prefix length.

**Further reading**

- [Configure Inter VLAN Routing with the Use of an External Router](https://www.cisco.com/c/en/us/support/docs/lan-switching/inter-vlan-routing/14976-50.html) — Configure — Configurations; Sample Command Output — Cisco Router

---

## CCNA6-023 · Network Access

Objectives: 2.1.a · single · Applied

A trunk Gi1/0/48 carries VLAN 25, but show vlan brief lists only Gi1/0/7 and Gi1/0/8 beside VLAN 25. Why is the missing trunk from that row not proof of a VLAN failure?

```text
VLAN Name           Status  Ports
25   Logistics      active  Gi1/0/7, Gi1/0/8

Separate check: Gi1/0/48 is trunking; VLAN 25 is allowed and forwarding.
```

- **A.** A trunk cannot carry a VLAN unless it appears in that row.
- **B.** The switch is routing every frame on Gi1/0/48.
- **C.** VLAN 25 must have exactly two ports by protocol.
- **D.** The brief VLAN membership display primarily lists access memberships; use trunk output to verify the trunk.

**Answer: D**

Choose verification commands that expose the property being tested. VLAN access membership and operational trunk admission are different views.

**Option explanations**

- **A:** Trunk carriage is verified through the trunk’s own operational information.
- **B:** A missing entry in this display does not turn a Layer 2 trunk into a routed port.
- **C:** There is no two-port membership requirement.
- **D:** An operational trunk need not appear alongside the access ports in that row.

**Further reading**

- [VLAN Configuration Guide, Cisco IOS XE 17.15.x — Configuring VLANs](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst9300/software/release/17-15/configuration_guide/vlan/b_1715_vlan_9300_cg/configuring_vlans.html) — Supported VLANs; Deleting a VLAN; VLAN Port Membership Modes
- [VLAN Configuration Guide, Cisco IOS XE 17.15.x — Configuring VLAN Trunks](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst9300/software/release/17-15/configuration_guide/vlan/b_1715_vlan_9300_cg/configuring_vlan_trunks.html) — Allowed VLANs on a Trunk; Configuring the Native VLAN for Untagged Traffic

---

## CCNA6-024 · Network Access

Objectives: 2.2.a, 2.2.c · single · Challenge

Both ends of an 802.1Q trunk use native VLAN 90, but the allowed lists contain only 10 and 20. No native tagging override is configured. What is wrong with claiming that ordinary VLAN 90 user data must pass just because it is native?

- **A.** Native VLAN 90 changes every access port to VLAN 90.
- **B.** Native VLANs are always outside all VLAN filtering rules.
- **C.** Using any native VLAN other than 1 disables 802.1Q.
- **D.** Being native does not automatically override the trunk’s VLAN admission policy.

**Answer: D**

Native describes how traffic is represented on the link, not an exemption from allowed-VLAN controls. Verify both classification and admission.

**Option explanations**

- **A:** The native setting does not migrate access ports.
- **B:** Native tagging behavior and VLAN permission are separate.
- **C:** Alternative native VLANs are valid when configured consistently.
- **D:** Ordinary native-VLAN user traffic still needs the VLAN allowed on the trunk.

**Further reading**

- [VLAN Configuration Guide, Cisco IOS XE 17.15.x — Configuring VLAN Trunks](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst9300/software/release/17-15/configuration_guide/vlan/b_1715_vlan_9300_cg/configuring_vlan_trunks.html) — Allowed VLANs on a Trunk; Configuring the Native VLAN for Untagged Traffic

---

## CCNA6-025 · Network Access

Objectives: 2.2.b · single · Applied

A server’s NIC is configured to send VLAN 250 tags for its virtual machines. Its switch connection is an ordinary static access port in VLAN 50, with no voice VLAN or special tag handling. Which design should be used to intentionally transport VLAN 250 and other tagged VM VLANs?

- **A.** A console connection to the server
- **B.** A configured 802.1Q trunk with matching permitted VLANs and host tagging
- **C.** An access port selected by the VM’s IP address
- **D.** A change to the server’s default DNS suffix

**Answer: B**

Tagged virtualization traffic needs an intentional compatible trunk design. A conventional access port is not a general multi-VLAN attachment.

**Option explanations**

- **A:** Console transport is not an Ethernet VLAN data path.
- **B:** The server and switch must agree on a multi-VLAN tagged attachment.
- **C:** Ordinary access membership is not chosen by the endpoint’s IP.
- **D:** DNS naming does not configure VLAN encapsulation.

**Further reading**

- [VLAN Configuration Guide, Cisco IOS XE 17.15.x — Configuring VLAN Trunks](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst9300/software/release/17-15/configuration_guide/vlan/b_1715_vlan_9300_cg/configuring_vlan_trunks.html) — Allowed VLANs on a Trunk; Configuring the Native VLAN for Untagged Traffic

---

## CCNA6-026 · Network Access

Objectives: 2.3 · single · Applied

SW-X learns SW-Y with LLDP, but SW-Y never learns SW-X. Physical traffic works in both directions. SW-X has lldp run, lldp receive, and no lldp transmit on this link. Which conclusion follows?

```text
SW-X interface settings:
 lldp receive
 no lldp transmit
```

- **A.** SW-X is receiving LLDP but not advertising itself to SW-Y.
- **B.** SW-X cannot possibly learn neighbors while transmit is disabled.
- **C.** An IP routing adjacency is required before SW-Y can learn SW-X.
- **D.** LLDP has selected SW-Y as the spanning-tree root.

**Answer: A**

Discovery can be asymmetric when transmission and reception differ. Check the sender’s advertisement configuration before replacing a working cable.

**Option explanations**

- **A:** The two directional controls explain the asymmetric tables.
- **B:** Reception can operate independently of transmission.
- **C:** LLDP operates directly at Layer 2.
- **D:** LLDP advertisements do not conduct spanning-tree election.

**Further reading**

- [Interface and Hardware Components Configuration Guide, Cisco IOS XE 17.15.x — Configuring LLDP, LLDP-MED, and Wired Location Service](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst9300/software/release/17-15/configuration_guide/int_hw/b_1715_int_and_hw_9300_cg/configuring_lldp__lldp_med__and_wired_location_service.html) — LLDP; Enabling LLDP; Monitoring and Maintaining LLDP, LLDP-MED, and Wired Location Service

---

## CCNA6-027 · Network Access

Objectives: 2.4 · matching · Applied

Match each Cisco channel configuration to its negotiation behavior. Each example concerns otherwise compatible interfaces; use each answer once.

1. channel-group 4 mode active
2. channel-group 4 mode passive
3. channel-group 4 mode on
4. channel-group 4 mode desirable

- **A.** LACP responder
- **B.** Static aggregation without a negotiation protocol
- **C.** LACP initiator
- **D.** PAgP initiator

**Answer: 1 → C; 2 → A; 3 → B; 4 → D**

Mode names identify both the protocol and whether negotiation is initiated. Static on should not be confused with LACP active.

**Option explanations**

- **A:** Mode passive responds to received LACP negotiation.
- **B:** Mode on does not send LACP or PAgP negotiation.
- **C:** Mode active starts LACP negotiation.
- **D:** Mode desirable uses Cisco PAgP rather than LACP.

**Further reading**

- [Layer 2 Configuration Guide, Cisco IOS XE 17.15.x — Configuring EtherChannels](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst9300/software/release/17-15/configuration_guide/lyr2/b_1715_lyr2_9300_cg/configuring_etherchannels.html) — LACP Modes; EtherChannel Configuration Guidelines; Load Balancing; Layer 3 EtherChannels; Hot-Standby Ports

---

## CCNA6-028 · Network Access

Objectives: 2.4 · single · Applied

Both intended member links are physically up, but the two switches use the different channel protocols shown below. Which change provides a standards-based negotiated aggregate?

```text
SW-X: channel-group 4 mode active
SW-Y: channel-group 4 mode desirable
```

- **A.** Change only the port-channel’s VLAN name.
- **B.** Retain the protocol mismatch and change both descriptions.
- **C.** Give every member the same IPv4 address.
- **D.** Change the PAgP side to a compatible LACP mode.

**Answer: D**

LACP and PAgP are separate aggregation protocols. Select a consistent protocol at the two endpoints.

**Option explanations**

- **A:** VLAN labels do not make PAgP and LACP interoperate.
- **B:** Descriptions do not reconcile negotiation protocols.
- **C:** Duplicate member addressing does not establish a compatible channel protocol.
- **D:** Active LACP can negotiate with active or passive LACP, not PAgP desirable.

**Further reading**

- [Layer 2 Configuration Guide, Cisco IOS XE 17.15.x — Configuring EtherChannels](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst9300/software/release/17-15/configuration_guide/lyr2/b_1715_lyr2_9300_cg/configuring_etherchannels.html) — LACP Modes; EtherChannel Configuration Guidelines; Load Balancing; Layer 3 EtherChannels; Hot-Standby Ports

---

## CCNA6-029 · Network Access

Objectives: 2.5.a · single · Challenge

SW-C has two equal-cost links to the same upstream bridge. Received root ID, cost, and sender bridge ID all tie. Link 1 receives sender port ID 128.20 on local Gi1/0/1; link 2 receives sender port ID 128.10 on local Gi1/0/2. Which path wins the next tie-break?

- **A.** Both links, because port IDs never matter in RSTP.
- **B.** Local Gi1/0/2, because its received sender port ID is lower.
- **C.** Local Gi1/0/1, because its local interface number is lower.
- **D.** Neither link until their VLAN IDs are changed.

**Answer: B**

Distinguish the sending bridge’s port ID from the receiving switch’s local port number. The lower received port ID wins at this step.

**Option explanations**

- **A:** Port IDs are part of the spanning-tree tie-break sequence.
- **B:** Sender port ID is compared before the local receiver’s port ID.
- **C:** The sender-port comparison already resolves this tie.
- **D:** The given BPDU identifiers are sufficient to resolve the choice.

**Further reading**

- [Understand Rapid Spanning Tree Protocol (802.1w)](https://www.cisco.com/c/en/us/support/docs/lan-switching/spanning-tree-protocol/24062-146.html) — New Port States and Port Roles — Port States; Alternate and Backup Port Roles
- [Layer 2 Configuration Guide, Cisco IOS XE 17.15.x — Configuring Spanning Tree Protocol](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst9300/software/release/17-15/configuration_guide/lyr2/b_1715_lyr2_9300_cg/configuring_spanning_tree_protocol.html) — Spanning-Tree Topology and Bridge Protocol Data Units; Bridge ID, Device Priority, and Extended System ID; (Optional) Configuring a Secondary Root Device

---

## CCNA6-030 · Network Access

Objectives: 2.5.b · single · Applied

A new point-to-point link connects two RSTP-capable switches. They exchange proposal and agreement information and synchronize the topology before rapidly forwarding. What permits this behavior?

- **A.** RSTP’s rapid agreement process on a suitable point-to-point link
- **B.** Assigning every port the alternate role
- **C.** Disabling BPDU transmission at both ends
- **D.** A mandatory DHCP handshake between the switches

**Answer: A**

Rapid convergence relies on protocol agreement and a safe topology state. It is not simply a fixed promise to forward every new link immediately.

**Option explanations**

- **A:** The protocol can establish a safe forwarding role without waiting through all legacy timer stages.
- **B:** Alternate ports normally discard user traffic rather than supplying the new forwarding path.
- **C:** That removes the information required for the agreement.
- **D:** DHCP is unrelated to spanning-tree role agreement.

**Further reading**

- [Understand Rapid Spanning Tree Protocol (802.1w)](https://www.cisco.com/c/en/us/support/docs/lan-switching/spanning-tree-protocol/24062-146.html) — New Port States and Port Roles — Port States; Alternate and Backup Port Roles

---

## CCNA6-031 · Network Access

Objectives: 2.5.c · single · Applied

An installer proposes globally enabling PortFast on all nontrunking ports without first checking where those ports connect. Which finding requires correcting that assumption?

- **A.** An edge printer uses a low-speed Ethernet link.
- **B.** A port connects to a single nonbridging workstation.
- **C.** An edge workstation has a static IPv4 address.
- **D.** An access-mode port connects to another switch with an alternative Layer 2 path.

**Answer: D**

Assess topology rather than only access/trunk configuration. A switch-to-switch access link can still participate in a Layer 2 loop.

**Option explanations**

- **A:** Link speed alone does not invalidate an otherwise genuine edge attachment.
- **B:** That is the typical edge use case.
- **C:** Static addressing does not make the host a Layer 2 bridge.
- **D:** A nontrunking mode does not prove the interface is a true edge attachment.

**Further reading**

- [Layer 2 Configuration Guide, Cisco IOS XE 17.15.x — Configuring Optional Spanning-Tree Features](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst9300/software/release/17-15/configuration_guide/lyr2/b_1715_lyr2_9300_cg/configuring_optional_spanning_tree_features.html) — PortFast; Bridge Protocol Data Unit Guard; Bridge Protocol Data Unit Filtering; Root Guard; Loop Guard

---

## CCNA6-032 · Network Access

Objectives: 2.5.d · multiple · Applied

Root guard is explicitly enabled on a downstream designated port; BPDU guard is absent. The peer sends ordinary inferior BPDUs advertising the legitimate existing root. Which TWO statements are correct? Select TWO.

- **A.** A later superior BPDU can put the affected instance into root-inconsistent.
- **B.** Every inferior BPDU immediately error-disables the port.
- **C.** Root guard suppresses every outbound BPDU.
- **D.** Root guard does not block merely because any BPDU arrives.

**Answer: A, D**

A downstream switch may legitimately participate in spanning tree without being allowed to move the root. Root guard enforces that distinction.

**Option explanations**

- **A:** That is the condition the feature is designed to prevent from changing root placement.
- **B:** That conflates root guard with interface BPDU guard.
- **C:** BPDU suppression is a different feature.
- **D:** It rejects superior root information, not all normal spanning-tree participation.

**Further reading**

- [Enhance STP with Root Guard](https://www.cisco.com/c/en/us/support/docs/lan-switching/spanning-tree-protocol/10588-74.html) — Feature Description

---

## CCNA6-033 · Network Access

Objectives: 2.6 · single · Foundation

A legacy Cisco AP model explicitly supports rogue detector mode. It is configured for that role to correlate rogue activity with the wired LAN. What radio behavior belongs to this mode?

- **A.** It becomes an 802.1X authentication server for all clients.
- **B.** It creates a wireless mesh backhaul automatically.
- **C.** Its radios are disabled while it monitors the wired LAN.
- **D.** It provides the production SSID while bridging all client traffic.

**Answer: C**

Do not confuse legacy rogue detector with monitor mode. The question assumes a supported older model because this mode is not available on every AP family.

**Option explanations**

- **A:** Rogue detection does not make it a RADIUS authentication service.
- **B:** Mesh backhaul belongs to supported bridge modes.
- **C:** The legacy rogue detector role is distinct from an RF monitor or client-serving AP.
- **D:** That is not the dedicated rogue detector role.

**Further reading**

- [Cisco Wireless Controller Configuration Guide, Release 8.5 — Managing APs](https://www.cisco.com/c/en/us/td/docs/wireless/controller/8-5/config-guide/b_cg85/managing_aps.html) — AP Modes: client-serving and network management modes

---

## CCNA6-034 · Network Access

Objectives: 2.6 · single · Applied

A local-mode AP loses its controller connection, while its PoE supply and Ethernet link remain up. The WLANs use central switching and no alternate controller is available. Why can the link LEDs stay lit while wireless service fails?

- **A.** Local mode always changes into standalone FlexConnect after a timeout.
- **B.** Physical connectivity does not preserve the required controller and client tunnel dependencies.
- **C.** PoE automatically means the AP has joined a WLC.
- **D.** A lit Ethernet LED proves every WLAN is forwarding end to end.

**Answer: B**

Test physical, controller, and client data states separately. A powered and linked AP can still be unable to supply its configured service.

**Option explanations**

- **A:** There is no guaranteed automatic conversion to that different design.
- **B:** Local-mode client service depends on controller connectivity, beyond mere Ethernet link state.
- **C:** Power delivery does not establish controller state.
- **D:** A physical indicator cannot prove tunnel, policy, or application operation.

**Further reading**

- [Cisco Wireless Controller Configuration Guide, Release 8.5 — Managing APs](https://www.cisco.com/c/en/us/td/docs/wireless/controller/8-5/config-guide/b_cg85/managing_aps.html) — AP Modes: client-serving and network management modes
- [Cisco Wireless Controller Configuration Guide, Release 8.10 — AP Connectivity to Controller](https://www.cisco.com/c/en/us/td/docs/wireless/controller/8-10/config-guide/b_cg810/ap_connectivity_to_cisco_wlc.html) — CAPWAP

---

## CCNA6-035 · Network Access

Objectives: 2.7 · single · Applied

A branch adds a locally switched guest VLAN to a FlexConnect AP. The WLC remains centrally located. Which wired location must carry the guest client VLAN for local egress?

- **A.** Only the controller console cable
- **B.** Only the remote WLC distribution trunk
- **C.** Only the branch DNS server’s management port
- **D.** The branch AP uplink and the local path to the guest gateway

**Answer: D**

Locate the point where client data exits its wireless tunnel or AP. Local switching moves the VLAN infrastructure requirement to the branch.

**Option explanations**

- **A:** Console is not a VLAN data attachment.
- **B:** That is not where locally switched guest frames leave the AP.
- **C:** DNS service does not provide the AP’s VLAN forwarding path.
- **D:** Locally switched client frames enter the wired network at the AP’s site.

**Further reading**

- [Cisco Wireless Controller Configuration Guide, Release 8.10 — FlexConnect](https://www.cisco.com/c/en/us/td/docs/wireless/controller/8-10/config-guide/b_cg810/flexconnect.html) — Configuring the Switch at a Remote Site; Configuring an Access Point for FlexConnect (GUI)

---

## CCNA6-036 · Network Access

Objectives: 2.7 · single · Applied

An AireOS 5520 controller’s documented LAG design uses static aggregation. The adjacent Catalyst output shows Po5(SU), both members P, and a dash in the Protocol column. What is the proper interpretation?

```text
Group  Port-channel  Protocol  Ports
5      Po5(SU)       -         Gi1/0/21(P) Gi1/0/22(P)
```

- **A.** The controller must be changed to PAgP desirable.
- **B.** A protocol dash can be expected for a static channel; verify the required bundle and VLAN operation.
- **C.** The dash means the channel is routed rather than switched.
- **D.** The dash proves both physical cables are disconnected.

**Answer: B**

Interpret an output field in the platform’s intended design. Absence of LACP is not an error when the documented controller aggregate is static.

**Option explanations**

- **A:** The stated AireOS LAG design is static rather than PAgP.
- **B:** Static on aggregation has no LACP or PAgP protocol to display.
- **C:** S, not the protocol dash, identifies the Layer 2 channel type.
- **D:** The member P and channel SU flags contradict that conclusion.

**Further reading**

- [Cisco Wireless Controller Configuration Guide, Release 8.10 — Ports and Interfaces](https://www.cisco.com/c/en/us/td/docs/wireless/controller/8-10/config-guide/b_cg810/ports_and_interfaces.html) — Restrictions on Link Aggregation; Configuring Neighbor Devices to Support Link Aggregation
- [Layer 2 Configuration Guide, Cisco IOS XE 17.15.x — Configuring EtherChannels](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst9300/software/release/17-15/configuration_guide/lyr2/b_1715_lyr2_9300_cg/configuring_etherchannels.html) — LACP Modes; EtherChannel Configuration Guidelines; Load Balancing; Layer 3 EtherChannels; Hot-Standby Ports

---

## CCNA6-037 · Network Access

Objectives: 2.8 · single · Applied

An administrator successfully authenticates to a controller’s web GUI using a local management account. A new WPA2-Enterprise wireless client is rejected by RADIUS. What conclusion is justified?

- **A.** The radio is proven physically defective.
- **B.** Management login success does not validate the separate WLAN client authentication path.
- **C.** The RADIUS server must accept every account that can open the GUI.
- **D.** HTTPS replaces the client’s 802.1X authentication.

**Answer: B**

Identify which principal and service are being authenticated. Device management access and network-client admission are separate policies.

**Option explanations**

- **A:** A reported authentication rejection is not evidence of a broken radio.
- **B:** The identities, method lists, and servers can differ between device administration and WLAN admission.
- **C:** Device administrator accounts need not be wireless user accounts.
- **D:** HTTPS protects the management browser session, not the wireless supplicant exchange.

**Further reading**

- [Cisco Wireless Controller Configuration Guide, Release 8.10 — AAA Administration](https://www.cisco.com/c/en/us/td/docs/wireless/controller/8-10/config-guide/b_cg810/aaa_administration.html) — Configuring TACACS+ (GUI)
- [Cisco Wireless Controller Configuration Guide, Release 8.10 — WLAN Security](https://www.cisco.com/c/en/us/td/docs/wireless/controller/8-10/config-guide/b_cg810/wlan_security.html) — Configuring WPA1+WPA2 (GUI); Configuring Peer-to-Peer Blocking (GUI)

---

## CCNA6-038 · Network Access

Objectives: 2.9 · multiple · Applied

A scanner must use WPA2-Personal with AES. The AireOS draft GUI instead enables 802.1X and has no PSK configured. Which TWO changes are required for the intended authentication design? Select TWO.

- **A.** Select Bronze QoS to replace the missing key.
- **B.** Enter the controller administrator password only on the scanner.
- **C.** Configure the approved key identically on the WLAN and scanner.
- **D.** Select PSK as the authentication key-management method.

**Answer: C, D**

Match the key-management method and actual credential, not just the WPA2 cipher. A correct SSID alone does not finish client configuration.

**Option explanations**

- **A:** QoS cannot supply an authentication credential.
- **B:** The device management password is not automatically the WLAN PSK.
- **C:** Matching key material is required for the shared-key handshake.
- **D:** Personal authentication uses a pre-shared key rather than the enterprise EAP method.

**Further reading**

- [Cisco Wireless Controller Configuration Guide, Release 8.10 — WLAN Security](https://www.cisco.com/c/en/us/td/docs/wireless/controller/8-10/config-guide/b_cg810/wlan_security.html) — Configuring WPA1+WPA2 (GUI); Configuring Peer-to-Peer Blocking (GUI)

---

## CCNA6-039 · Network Access

Objectives: 2.9 · single · Applied

The AireOS GUI has WLAN Production enabled globally, but AP-B belongs to a custom AP group whose WLAN list contains only Visitor. The radios are healthy. What should the engineer change to advertise Production at AP-B?

| GUI view | Value |
| --- | --- |
| Production WLAN status | Enabled |
| AP-B group | Factory-East |
| Factory-East WLANs | Visitor only |
| AP-B radio state | Enabled |

- **A.** Add the intended Production WLAN mapping to AP-B’s assigned AP group.
- **B.** Make AP-B a dedicated sniffer.
- **C.** Change only the Production profile description.
- **D.** Increase the client’s DHCP lease duration.

**Answer: A**

Global WLAN existence is not the entire effective configuration. Verify AP membership and the group’s WLAN mappings.

**Option explanations**

- **A:** That group controls which WLANs are offered by its APs.
- **B:** Sniffer mode removes ordinary WLAN service.
- **C:** A description does not add the WLAN to the AP group.
- **D:** Address leases are irrelevant before the WLAN is offered.

**Further reading**

- [Cisco Wireless Controller Configuration Guide, Release 8.10 — AP Groups](https://www.cisco.com/c/en/us/td/docs/wireless/controller/8-10/config-guide/b_cg810/configuring_ap_groups.html) — Access Point Groups; Creating Access Point Groups (GUI)

---

## CCNA6-040 · Network Access

Objectives: 2.9 · single · Applied

A WLAN’s AireOS QoS profile changes from Silver to Platinum, but the AP still has severe RF contention and an overloaded upstream link. Which statement correctly limits what this GUI change proves?

- **A.** Every voice packet is now guaranteed zero delay.
- **B.** The configured service class changed; end-to-end latency still requires measurement and capacity checks.
- **C.** The AP has automatically doubled its physical channel width.
- **D.** The WLAN’s PSK has been strengthened automatically.

**Answer: B**

A policy setting expresses intended treatment rather than a measured service outcome. Verify queues, airtime, and the complete traffic path.

**Option explanations**

- **A:** No such guarantee follows from selecting a profile.
- **B:** Priority policy cannot create unlimited airtime or remove every upstream bottleneck.
- **C:** A QoS profile selection does not itself change RF channel width.
- **D:** QoS and credential security are independent settings.

**Further reading**

- [Cisco Wireless Controller Configuration Guide, Release 8.10 — Wireless Quality of Service](https://www.cisco.com/c/en/us/td/docs/wireless/controller/8-10/config-guide/b_cg810/wireless_quality_of_service.html) — QoS Profiles; Configuring QoS Profiles (GUI); Assigning a QoS Profile to a WLAN (GUI)

---

## CCNA6-041 · IP Connectivity

Objectives: 3.1.a, 3.1.g · single · Foundation

A route begins with S* in Cisco IOS show ip route. Which reading correctly separates the two symbols?

- **A.** S means subnet; * means every packet ignores specific routes.
- **B.** S means secure; * means encrypted forwarding.
- **C.** S means standby; * means the route is never installed.
- **D.** S identifies a static source; * marks a candidate default.

**Answer: D**

Read route codes and auxiliary markers separately. A candidate-default indication is not a security property or permission to override more specific prefixes.

**Option explanations**

- **A:** The marker does not override longest-prefix forwarding.
- **B:** Neither symbol reports packet encryption.
- **C:** S denotes static, not the HSRP standby role.
- **D:** The source code and candidate-default marker convey different attributes.

**Further reading**

- [Understand Administrative Distance](https://www.cisco.com/c/en/us/support/docs/ip/border-gateway-protocol-bgp/15986-admin-distance.html) — RIB Route Comparison; Route Installation; Default AD Values

---

## CCNA6-042 · IP Connectivity

Objectives: 3.1.e, 3.1.f · single · Applied

The only changed field between these two snapshots is shown. Which conclusion is justified?

```text
Before: O 10.35.70.0/24 [110/20] via 192.0.2.2
After:  O 10.35.70.0/24 [110/70] via 192.0.2.2
```

- **A.** The route changed from OSPF to static.
- **B.** The destination prefix expanded by 50 addresses.
- **C.** The OSPF metric increased while administrative distance stayed 110.
- **D.** The administrative distance increased by 50.

**Answer: C**

Use exact field positions to identify what changed. This output alone does not reveal whether the increased cost came from a manual edit or a different path.

**Option explanations**

- **A:** The O source code remains unchanged.
- **B:** The /24 destination field did not change.
- **C:** The second bracket field changed from 20 to 70.
- **D:** The distance occupies the first bracket field and remains 110.

**Further reading**

- [Understand Administrative Distance](https://www.cisco.com/c/en/us/support/docs/ip/border-gateway-protocol-bgp/15986-admin-distance.html) — RIB Route Comparison; Route Installation; Default AD Values

---

## CCNA6-043 · IP Connectivity

Objectives: 3.2.a · single · Applied

A router has an installed 10.16.0.0/12 route and no default. Which destination has no matching route among the four options?

- **A.** 10.16.1.1
- **B.** 10.23.250.1
- **C.** 10.31.254.1
- **D.** 10.32.1.1

**Answer: D**

This prefix fixes the high four bits of the second octet. Without another matching route or default, 10.32.1.1 has no forwarding entry.

**Option explanations**

- **A:** Second octet 16 is inside the /12.
- **B:** Second octet 23 is inside 16–31.
- **C:** Second octet 31 remains inside the /12.
- **D:** The /12 ends at 10.31.255.255, so second octet 32 is outside it.

**Further reading**

- [RFC 1812: Requirements for IP Version 4 Routers](https://www.rfc-editor.org/rfc/rfc1812.html) — 5.2.4 Determining the Next Hop Address
- [Configure Route Selection for Routers](https://www.cisco.com/c/en/us/support/docs/ip/enhanced-interior-gateway-routing-protocol-eigrp/8651-21.html) — Build the Routing Table; Make Forwarding Decisions

---

## CCNA6-044 · IP Connectivity

Objectives: 3.2.b · single · Applied

An OSPF route remains preferred after an operator lowers a competing RIP route’s hop metric from 5 to 1. Distances are OSPF 110 and RIP 120 for the same /24. Why?

- **A.** RIP metrics can only be larger than 110.
- **B.** Lowering a metric makes that route less preferred.
- **C.** OSPF copies the RIP metric and therefore always ties.
- **D.** The improved RIP metric does not overcome its higher source distance.

**Answer: D**

An optimization within one protocol does not necessarily change the route source installed by the router. Evaluate metric and administrative distance at their separate stages.

**Option explanations**

- **A:** RIP’s metric scale is not the administrative-distance scale.
- **B:** The issue is source distance, not a reversal of RIP metric ordering.
- **C:** The routing protocols calculate their own metrics.
- **D:** OSPF remains preferred in the same-prefix comparison.

**Further reading**

- [Understand Administrative Distance](https://www.cisco.com/c/en/us/support/docs/ip/border-gateway-protocol-bgp/15986-admin-distance.html) — RIB Route Comparison; Route Installation; Default AD Values

---

## CCNA6-045 · IP Connectivity

Objectives: 3.2.c · single · Challenge

The constructed cost audit shows the outgoing interface costs along the same OSPF path in opposite directions. What does this imply?

| Direction | Outgoing costs, in order |
| --- | --- |
| Forward | 12, 8, 5 |
| Reverse | 30, 8, 5 |

- **A.** OSPF rejects every asymmetric link cost.
- **B.** OSPF path costs can differ by direction.
- **C.** The costs must be averaged to 34 in both directions.
- **D.** The router IDs determine which direction is allowed.

**Answer: B**

The forward total is 25 and the reverse total is 43. Directional metrics can influence asymmetric path choices without themselves indicating an adjacency fault.

**Option explanations**

- **A:** Equal cost in opposite directions is not an adjacency requirement.
- **B:** Each router contributes the cost of its outgoing interface for that direction.
- **C:** SPF does not average the two directional path totals.
- **D:** Router-ID values do not prohibit directional forwarding.

**Further reading**

- [RFC 2328: OSPF Version 2](https://www.rfc-editor.org/rfc/rfc2328.html) — 9.4 Electing the Designated Router; 10 The Neighbor Data Structure; 16 Calculation of the routing table

---

## CCNA6-046 · IP Connectivity

Objectives: 3.1.b, 3.1.c, 3.3.c · matching · Applied

Match each route prefix to its destination scope.

1. 203.0.113.11/32
2. 2001:db8:22::11/128
3. 0.0.0.0/0
4. 10.63.18.0/23

- **A.** Exactly one IPv6 address
- **B.** A block of 512 IPv4 addresses
- **C.** Exactly one IPv4 address
- **D.** All IPv4 destinations as a fallback

**Answer: 1 → C; 2 → A; 3 → D; 4 → B**

The prefix length determines the covered destination set. Whether a matching route is selected also depends on the other installed prefixes.

**Option explanations**

- **A:** An IPv6 /128 leaves no host bits variable.
- **B:** An IPv4 /23 leaves nine address bits variable.
- **C:** An IPv4 /32 leaves no host bits variable.
- **D:** An IPv4 /0 fixes none of the destination bits.

**Further reading**

- [RFC 1812: Requirements for IP Version 4 Routers](https://www.rfc-editor.org/rfc/rfc1812.html) — 5.2.4 Determining the Next Hop Address
- [IPv6 Routing: Static Routing — Cisco IOS XE 17.x](https://www.cisco.com/c/en/us/td/docs/routers/ios/config/17-x/ip-routing/b-ip-routing/m_ip6-route-static-xe.html) — Recursive Static Routes; Fully Specified Static Routes; Floating Static Routes

---

## CCNA6-047 · IP Connectivity

Objectives: 3.3.b · single · Applied

A proposed IPv4 static uses destination 10.28.7.0 with mask 255.255.252.0. The intended network is the /22 containing 10.28.7.50. Which destination should the engineer use for the canonical network route?

- **A.** 10.28.8.0
- **B.** 10.28.7.0
- **C.** 10.28.4.0
- **D.** 10.28.0.0

**Answer: C**

Canonical route prefixes must align to their mask. Work from the destination’s actual block before writing the network field.

**Option explanations**

- **A:** That begins the next /22 block and excludes the destination.
- **B:** This has nonzero host bits for the /22 network field.
- **C:** The /22 block containing third octet 7 starts at 4 and ends at 7.
- **D:** With /22 this covers third octets 0–3, not 7.

**Further reading**

- [RFC 1812: Requirements for IP Version 4 Routers](https://www.rfc-editor.org/rfc/rfc1812.html) — 5.2.4 Determining the Next Hop Address
- [Configure a Next Hop IP Address for Static Routes](https://www.cisco.com/c/en/us/support/docs/dial-access/floating-static-route/118263-technote-nexthop-00.html) — Background Information; Floating Static Route Example

---

## CCNA6-048 · IP Connectivity

Objectives: 3.3.a · single · Applied

A branch has exactly one upstream router. The operator mistakenly installs a host route to the upstream’s interface and expects it to provide Internet fallback. What additional destination scope is required?

- **A.** An ARP entry for 0.0.0.0
- **B.** A local /32 route for every branch interface
- **C.** A default route through the upstream neighbor
- **D.** An OSPF router ID with prefix length zero

**Answer: C**

Knowing how to reach the exit router is different from directing unknown destinations through it. The default supplies the latter policy.

**Option explanations**

- **A:** ARP maps neighbors and does not create a catch-all IP route.
- **B:** Local ownership routes do not cover arbitrary remote destinations.
- **C:** A neighbor host route reaches only that one address, not otherwise unknown destinations.
- **D:** Router IDs are not default-route configuration.

**Further reading**

- [Configure a Next Hop IP Address for Static Routes](https://www.cisco.com/c/en/us/support/docs/dial-access/floating-static-route/118263-technote-nexthop-00.html) — Background Information; Floating Static Route Example
- [Configure Route Selection for Routers](https://www.cisco.com/c/en/us/support/docs/ip/enhanced-interior-gateway-routing-protocol-eigrp/8651-21.html) — Build the Routing Table; Make Forwarding Decisions

---

## CCNA6-049 · IP Connectivity

Objectives: 3.3.c · single · Applied

An installed IPv4 host route sends 10.56.8.44 through an alternate neighbor. A user reports 10.56.8.45 still uses the ordinary /24 path. Is this consistent with the route’s intended scope?

- **A.** Yes; a /32 exception affects only 10.56.8.44.
- **B.** Yes, because routes are selected by source-port number.
- **C.** No; the alternate next hop should replace every route in the RIB.
- **D.** No; a host route always covers two adjacent host addresses.

**Answer: A**

Validate a narrow exception with both a positive case and a nearby negative case. Correct behavior includes preserving the normal path for other hosts.

**Option explanations**

- **A:** The neighboring address differs in bits fixed by the host route.
- **B:** The stated behavior follows destination scope, not transport ports.
- **C:** A single host exception does not replace unrelated destinations.
- **D:** A /32 contains exactly one address.

**Further reading**

- [Local Host Routes Installed in the Routing Table on Cisco IOS and Cisco IOS-XR](https://www.cisco.com/c/en/us/support/docs/ip/ip-routing/116264-technote-ios-00.html) — Cisco IOS Local Routes; Manually Configured Host Routes
- [Configure Route Selection for Routers](https://www.cisco.com/c/en/us/support/docs/ip/enhanced-interior-gateway-routing-protocol-eigrp/8651-21.html) — Build the Routing Table; Make Forwarding Decisions

---

## CCNA6-050 · IP Connectivity

Objectives: 3.3.d · single · Applied

An engineer plans to test a floating static by disconnecting the primary upstream at the provider’s remote edge. The local primary next hop remains reachable and no tracking is configured. Which test limitation must be recognized?

- **A.** Any upstream packet loss automatically lowers every static distance.
- **B.** The primary static may remain installed, so this may not trigger the intended backup.
- **C.** The backup can install only if the router loses electrical power.
- **D.** A floating route cannot be tested on a working network.

**Answer: B**

Choose tests that match the failure-detection design. If remote reachability should drive failover, the design needs an appropriate supported tracking mechanism.

**Option explanations**

- **A:** Administrative distances do not adapt to arbitrary loss.
- **B:** A distant failure need not invalidate the local static’s resolution.
- **C:** Route withdrawal can occur without a chassis power failure.
- **D:** Controlled tests are possible when their failure conditions are understood.

**Further reading**

- [Configure a Next Hop IP Address for Static Routes](https://www.cisco.com/c/en/us/support/docs/dial-access/floating-static-route/118263-technote-nexthop-00.html) — Background Information; Floating Static Route Example

---

## CCNA6-051 · IP Connectivity

Objectives: 3.3.b, 3.3.d · multiple · Applied

The IPv6 primary and backup routes are shown, with both next hops directly reachable. Which two observations are correct before a failure? Select two.

```text
ipv6 route 2001:db8:610::/64 2001:db8:a::2 5
ipv6 route 2001:db8:610::/64 2001:db8:b::2 180
```

- **A.** The ::/0 default must disappear when either command is added.
- **B.** The distance-180 route carries all IPv6 traffic because 180 is larger.
- **C.** The distance-5 route is preferred for this /64.
- **D.** The distance-180 command can remain configured without being the active route.

**Answer: C, D**

Configured candidates and selected routes are different inventories. Both source preference and destination coverage matter when interpreting the result.

**Option explanations**

- **A:** An unrelated default can coexist with this more specific network route.
- **B:** Higher distance is less preferred, and the route covers only its /64.
- **C:** It has the lower distance among the same-prefix candidates.
- **D:** A backup configuration need not appear as the selected route.

**Further reading**

- [IPv6 Routing: Static Routing — Cisco IOS XE 17.x](https://www.cisco.com/c/en/us/td/docs/routers/ios/config/17-x/ip-routing/b-ip-routing/m_ip6-route-static-xe.html) — Recursive Static Routes; Fully Specified Static Routes; Floating Static Routes
- [Understand Administrative Distance](https://www.cisco.com/c/en/us/support/docs/ip/border-gateway-protocol-bgp/15986-admin-distance.html) — RIB Route Comparison; Route Installation; Default AD Values

---

## CCNA6-052 · IP Connectivity

Objectives: 3.3.b · single · Applied

A static IPv6 network route uses a valid global next hop that is directly reachable on an up IPv6-enabled Ethernet link. Which statement about omitting the interface is correct?

- **A.** Omitting the interface makes the route a host route automatically.
- **B.** Every IPv6 next hop requires an interface even when globally scoped and directly resolved.
- **C.** The interface can be determined by resolving that global next-hop address.
- **D.** The router must convert the next hop into an IPv4 address.

**Answer: C**

Global and link-local next hops have different scope requirements. A global next hop can be used recursively when its resolution is valid.

**Option explanations**

- **A:** The destination prefix, not next-hop syntax, determines route scope.
- **B:** The mandatory link context for link-local next hops does not prohibit global recursion.
- **C:** The connected route supplies the outgoing interface for this recursive form.
- **D:** IPv6 static resolution does not require IPv4 conversion.

**Further reading**

- [IPv6 Routing: Static Routing — Cisco IOS XE 17.x](https://www.cisco.com/c/en/us/td/docs/routers/ios/config/17-x/ip-routing/b-ip-routing/m_ip6-route-static-xe.html) — Recursive Static Routes; Fully Specified Static Routes; Floating Static Routes

---

## CCNA6-053 · IP Connectivity

Objectives: 3.4.a · single · Applied

After an ACL change, two same-subnet routers can still ping but their OSPF adjacency expires. The ACL permits ICMP and drops IP protocol 89. What is the direct explanation?

- **A.** A working ping guarantees every IP protocol is permitted.
- **B.** The ACL blocks OSPF packets while allowing the ping traffic.
- **C.** ICMP always carries OSPF database updates.
- **D.** OSPF requires TCP port 89, which ping automatically opens.

**Answer: B**

Test the traffic class used by the actual control protocol. General IP reachability does not establish OSPF packet permission.

**Option explanations**

- **A:** ACLs can permit one protocol and deny another.
- **B:** OSPFv2 uses IP protocol 89; ICMP success tests a different protocol.
- **C:** ICMP ping is not the OSPF transport.
- **D:** OSPFv2 runs directly over IP rather than TCP port 89.

**Further reading**

- [Troubleshoot OSPF Neighbor Problems](https://www.cisco.com/c/en/us/support/docs/ip/open-shortest-path-first-ospf/13699-29.html) — No State Revealed; Neighbors Stuck in Exstart/Exchange State
- [RFC 2328: OSPF Version 2](https://www.rfc-editor.org/rfc/rfc2328.html) — 9.4 Electing the Designated Router; 10 The Neighbor Data Structure; 16 Calculation of the routing table

---

## CCNA6-054 · IP Connectivity

Objectives: 3.4.a · single · Applied

R1’s neighbor list shows R2 in Full. Which claim goes beyond what this single observation proves?

- **A.** The adjacency completed its database synchronization.
- **B.** R1 has a current OSPF neighbor relationship with R2.
- **C.** Every application behind R2 is healthy.
- **D.** R1 and R2 reached a bidirectional neighbor relationship.

**Answer: C**

Full is strong evidence at the OSPF adjacency layer. It does not certify server state, ACL policy, return routing, or transport success for every application.

**Option explanations**

- **A:** That is the meaning of Full for this neighbor.
- **B:** The observed operational entry directly supports that statement.
- **C:** Full adjacency establishes OSPF synchronization, not remote application availability.
- **D:** Full necessarily follows bidirectional discovery.

**Further reading**

- [Understand OSPF Neighbor States](https://www.cisco.com/c/en/us/support/docs/ip/open-shortest-path-first-ospf/13685-13.html) — OSPF Neighbor States

---

## CCNA6-055 · IP Connectivity

Objectives: 3.4.b · single · Foundation

Two serial point-to-point interfaces have compatible OSPF settings and are in Full state. A technician searches for a BDR entry but finds none. Which additional action is required solely to create a healthy adjacency?

- **A.** Replace the /30 transit mask with a /24 to force a BDR.
- **B.** None; Full without a BDR is expected on this link type.
- **C.** Increase Hello intervals until a BDR appears.
- **D.** Add a loopback named BDR on each router.

**Answer: B**

Use the protocol’s expected state model rather than expecting every field on every interface type. No missing BDR needs repair here.

**Option explanations**

- **A:** Address mask alone is not the required network-type redesign.
- **B:** Point-to-point adjacency is complete without a broadcast election.
- **C:** Timers do not introduce DR/BDR elections on point-to-point links.
- **D:** Interface naming does not provide an OSPF elected role.

**Further reading**

- [RFC 2328: OSPF Version 2](https://www.rfc-editor.org/rfc/rfc2328.html) — 9.4 Electing the Designated Router; 10 The Neighbor Data Structure; 16 Calculation of the routing table
- [Understand OSPF Neighbor States](https://www.cisco.com/c/en/us/support/docs/ip/open-shortest-path-first-ospf/13685-13.html) — OSPF Neighbor States

---

## CCNA6-056 · IP Connectivity

Objectives: 3.4.c · multiple · Applied

In a fresh OSPF broadcast election, R1 has priority 0 and the highest router ID; R2 and R3 have nonzero priorities. All routers hear each other before the election. Which two statements hold? Select two.

- **A.** R1 wins DR because router ID is checked before eligibility.
- **B.** R1 is excluded from both DR and BDR selection.
- **C.** R1 can still form an adjacency with the elected DR.
- **D.** R1’s zero priority prevents R2 and R3 from electing any DR.

**Answer: B, C**

Eligibility precedes ranking among eligible routers. This lets a router participate without taking broadcast leadership.

**Option explanations**

- **A:** An ineligible router is not rescued by its identifier.
- **B:** Priority zero removes election eligibility.
- **C:** It remains an OSPF participant as a DROTHER.
- **D:** One ineligible participant does not remove others’ eligibility.

**Further reading**

- [RFC 2328: OSPF Version 2](https://www.rfc-editor.org/rfc/rfc2328.html) — 9.4 Electing the Designated Router; 10 The Neighbor Data Structure; 16 Calculation of the routing table

---

## CCNA6-057 · IP Connectivity

Objectives: 3.4.d · single · Applied

A router boots with two up loopbacks: 10.9.0.200 and 10.10.0.1. A physical interface has 203.0.113.250. With no explicit ID, which value should a newly started OSPF process choose?

- **A.** 10.10.0.1
- **B.** 10.0.0.0
- **C.** 10.9.0.200
- **D.** 203.0.113.250

**Answer: A**

Apply the interface-class preference first, then compare complete addresses within that class. Last-octet size alone is misleading.

**Option explanations**

- **A:** Loopbacks are preferred, and 10.10.0.1 is the higher loopback address.
- **B:** OSPF does not summarize the loopbacks to construct a router ID.
- **C:** Compare the second octet before the last; 10 exceeds 9.
- **D:** A higher physical address does not override available loopbacks in this selection.

**Further reading**

- [Configuring OSPF — IP Routing: OSPF Configuration Guide](https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/iproute_ospf/configuration/xe-16/iro-xe-16-book/iro-cfg.html) — Enabling OSPF; Configuring OSPF Interface Parameters

---

## CCNA6-058 · IP Connectivity

Objectives: 3.4.d · single · Applied

A maintenance plan changes an OSPF router ID on a router with several Full peers. Why should the plan anticipate adjacency reconvergence when the new ID is applied?

- **A.** The physical Ethernet MAC is guaranteed to change.
- **B.** Neighbors see a changed routing-protocol identity and must rebuild the affected relationships.
- **C.** Every interface IP address is automatically renumbered.
- **D.** All TCP applications must change their destination ports.

**Answer: B**

A router-ID change is an operational topology change, not merely a display-name edit. Plan and verify convergence around the activation step.

**Option explanations**

- **A:** Router-ID configuration does not inherently change hardware MAC addresses.
- **B:** A router-ID transition changes the identity used in OSPF’s topology and adjacency state.
- **C:** The identifier change does not rewrite all interface addresses.
- **D:** OSPF identity does not define application port numbers.

**Further reading**

- [Configuring OSPF — IP Routing: OSPF Configuration Guide](https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/iproute_ospf/configuration/xe-16/iro-xe-16-book/iro-cfg.html) — Enabling OSPF; Configuring OSPF Interface Parameters
- [RFC 2328: OSPF Version 2](https://www.rfc-editor.org/rfc/rfc2328.html) — 9.4 Electing the Designated Router; 10 The Neighbor Data Structure; 16 Calculation of the routing table

---

## CCNA6-059 · IP Connectivity

Objectives: 3.2.c · single · Applied

A network consistently applies the shown OSPF reference bandwidth. With automatic costs and no overrides, what costs distinguish its 1 Gb/s and 10 Gb/s interfaces?

```text
router ospf 1
 auto-cost reference-bandwidth 10000
! Reference bandwidth is expressed in Mb/s.
```

- **A.** 1 for both interfaces
- **B.** 1 for 1 Gb/s and 10 for 10 Gb/s
- **C.** 10,000 for both interfaces
- **D.** 10 for 1 Gb/s and 1 for 10 Gb/s

**Answer: D**

Convert interface rates to the same units as the reference before division. Consistent reference settings make the resulting costs interpretable across routers.

**Option explanations**

- **A:** That would fail to use the higher reference bandwidth’s cost resolution.
- **B:** This reverses the inverse relationship between bandwidth and cost.
- **C:** The reference must be divided by each interface bandwidth.
- **D:** 10,000/1,000 is 10; 10,000/10,000 is 1.

**Further reading**

- [Configuring OSPF — IP Routing: OSPF Configuration Guide](https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/iproute_ospf/configuration/xe-16/iro-xe-16-book/iro-cfg.html) — Enabling OSPF; Configuring OSPF Interface Parameters

---

## CCNA6-060 · IP Connectivity

Objectives: 3.4.a, 3.4.c · single · Applied

Four routers share a healthy broadcast LAN. A report marks every 2-Way entry as a failure. What context is essential before accepting that report?

- **A.** Whether both hostnames begin with the same letter
- **B.** Whether the local process number is the largest in the LAN
- **C.** Whether the prefix uses private or public addressing
- **D.** Whether the entry is between two DROTHER routers

**Answer: D**

Monitoring rules must account for network type and roles. A state can be healthy in one relationship and incomplete in another.

**Option explanations**

- **A:** Names do not determine required adjacency state.
- **B:** Local process-number ordering has no such meaning.
- **C:** Address allocation type does not change the DROTHER relationship rule.
- **D:** Such neighbors can legitimately remain 2-Way on broadcast networks.

**Further reading**

- [Understand OSPF Neighbor States](https://www.cisco.com/c/en/us/support/docs/ip/open-shortest-path-first-ospf/13685-13.html) — OSPF Neighbor States
- [RFC 2328: OSPF Version 2](https://www.rfc-editor.org/rfc/rfc2328.html) — 9.4 Electing the Designated Router; 10 The Neighbor Data Structure; 16 Calculation of the routing table

---

## CCNA6-061 · IP Connectivity

Objectives: 3.4.a · single · Applied

An OSPF-enabled interface is up but administratively configured passive. A packet capture sees no outgoing Hellos. Which command change specifically permits adjacency formation on that interface?

- **A.** no shutdown under the already-up interface
- **B.** ip ospf priority 255 under the passive interface
- **C.** no passive-interface followed by that interface under the OSPF process
- **D.** ip route 0.0.0.0 0.0.0.0 Null0

**Answer: C**

Change the setting responsible for the observed behavior. Retain passive operation on other host-facing interfaces when that remains intended.

**Option explanations**

- **A:** The link is already up; administrative interface state is not the stated blocker.
- **B:** Election preference cannot override passive suppression.
- **C:** This removes the suppression of OSPF neighbor participation on the selected interface.
- **D:** A discard default does not enable OSPF Hellos.

**Further reading**

- [Default Passive Interfaces — Cisco IOS XE 17.x](https://www.cisco.com/c/en/us/td/docs/routers/ios/config/17-x/ip-routing/b-ip-routing/m_iri-default-passive-interface.html) — Information About Default Passive Interfaces

---

## CCNA6-062 · IP Connectivity

Objectives: 3.5 · single · Applied

A site runs a virtual-gateway group successfully on VLAN 30. Hosts in isolated VLAN 40 are configured with that VLAN-30 virtual IP as their gateway, and cannot ARP for it. What requirement is missing?

- **A.** An IPv4 broadcast address as the replacement gateway
- **B.** A reachable first-hop gateway within the hosts’ own on-link subnet/VLAN design
- **C.** Identical OSPF costs on every interface
- **D.** A higher HSRP priority on the VLAN-30 active router

**Answer: B**

A virtual IP is still subject to the host’s local addressing and Layer 2 reachability requirements. Creating one redundancy group does not automatically serve unrelated VLANs.

**Option explanations**

- **A:** A broadcast destination is not a valid substitute for a router next hop.
- **B:** The hosts must be able to reach the virtual gateway on their local Layer 2 segment.
- **C:** OSPF costs do not make an off-link gateway ARP-reachable.
- **D:** Priority does not carry ARP across an isolated VLAN boundary.

**Further reading**

- [Understand the Hot Standby Router Protocol Features and Functionality](https://www.cisco.com/c/en/us/support/docs/ip/hot-standby-router-protocol-hsrp/9234-hsrpguidetoc.html) — HSRP Background and Operations; HSRP Operation
- [RFC 1812: Requirements for IP Version 4 Routers](https://www.rfc-editor.org/rfc/rfc1812.html) — 5.2.4 Determining the Next Hop Address

---

## CCNA6-063 · IP Connectivity

Objectives: 3.5 · single · Challenge

An active HSRP router tracks only whether its uplink interface is up. The interface stays up while an upstream device drops all traffic. Why might gateway ownership remain unchanged?

- **A.** The tracked condition has not transitioned to failure.
- **B.** The standby’s virtual IP must be different during an outage.
- **C.** HSRP always measures every Internet destination automatically.
- **D.** Tracking can only operate when both routers are shut down.

**Answer: A**

Detection coverage is defined by the tracked object. Test the actual failure mode, not just the existence of a tracking command.

**Option explanations**

- **A:** Interface-up tracking cannot directly detect every farther-upstream outage.
- **B:** The group preserves its virtual address rather than requiring a second one.
- **C:** Such broad end-to-end monitoring is not inherent in basic HSRP.
- **D:** Tracking responds to live object state, not a simultaneous shutdown prerequisite.

**Further reading**

- [Use HSRP Preempt and Track Commands](https://www.cisco.com/c/en/us/support/docs/ip/hot-standby-router-protocol-hsrp/13780-6.html) — Preempt and Track Commands

---

## CCNA6-064 · IP Connectivity

Objectives: 3.5 · multiple · Applied

Which two statements correctly describe the boundary between first-hop redundancy and dynamic routing? Select two.

- **A.** FHRP preserves a usable virtual gateway identity for attached hosts.
- **B.** Dynamic routing can supply onward routes on each gateway router.
- **C.** An OSPF DR automatically supplies an HSRP virtual address.
- **D.** FHRP automatically replaces all interior routing protocols.

**Answer: A, B**

The mechanisms can complement each other without being interchangeable. Validate both first-hop ownership and the surviving router’s routing table.

**Option explanations**

- **A:** Its purpose centers on the hosts’ first routed hop.
- **B:** Routers still need destination paths after accepting host traffic.
- **C:** The protocols configure and elect independent functions.
- **D:** Virtual-gateway ownership does not compute every network path.

**Further reading**

- [Understand the Hot Standby Router Protocol Features and Functionality](https://www.cisco.com/c/en/us/support/docs/ip/hot-standby-router-protocol-hsrp/9234-hsrpguidetoc.html) — HSRP Background and Operations; HSRP Operation
- [RFC 9568: Virtual Router Redundancy Protocol (VRRP) Version 3 for IPv4 and IPv6](https://www.rfc-editor.org/rfc/rfc9568.html) — 1 Introduction; 2 Required Features; 6 Protocol State Machine
- [RFC 2328: OSPF Version 2](https://www.rfc-editor.org/rfc/rfc2328.html) — 9.4 Electing the Designated Router; 10 The Neighbor Data Structure; 16 Calculation of the routing table

---

## CCNA6-065 · IP Connectivity

Objectives: 3.3.b, 3.1.c · single · Applied

The intended static route covers 192.168.90.128 through 192.168.90.255 inclusive. Which prefix expresses exactly that range?

- **A.** 192.168.90.0/24
- **B.** 192.168.90.0/25
- **C.** 192.168.90.128/26
- **D.** 192.168.90.128/25

**Answer: D**

Derive the prefix from the required boundaries, not only the number of host devices currently present. Network routes cover every address in their prefix.

**Option explanations**

- **A:** This also includes .0–.127, outside the requested range.
- **B:** This covers the lower half, .0–.127.
- **C:** This covers only .128–.191.
- **D:** A /25 divides the /24 into two aligned 128-address blocks.

**Further reading**

- [RFC 1812: Requirements for IP Version 4 Routers](https://www.rfc-editor.org/rfc/rfc1812.html) — 5.2.4 Determining the Next Hop Address
- [Configure a Next Hop IP Address for Static Routes](https://www.cisco.com/c/en/us/support/docs/dial-access/floating-static-route/118263-technote-nexthop-00.html) — Background Information; Floating Static Route Example

---

## CCNA6-066 · IP Services

Objectives: 4.1 · single · Applied

An engineer tests dynamic inside-source NAT on a quiet router. The inside client is powered off and has generated no matching traffic since translations were cleared. The configuration is correct, and show ip nat translations is empty. What is the best interpretation?

- **A.** The empty table proves that the inside interface is administratively down.
- **B.** An empty dynamic table is expected until eligible traffic creates a mapping.
- **C.** The pool must be converted to static NAT before any translation can be shown.
- **D.** Every address in a configured dynamic pool must appear as an active translation immediately.

**Answer: B**

Test dynamic NAT with relevant traffic and then inspect allocated state. A configuration object can exist before any host has requested the corresponding runtime mapping.

**Option explanations**

- **A:** No interface-state evidence is provided.
- **B:** Dynamic translations are established on demand, so the table alone does not contradict the configuration.
- **C:** Dynamic NAT can create and display translations once triggered.
- **D:** Pool availability and allocated translations are different states.

**Further reading**

- [IP Addressing Configuration Guide, Cisco IOS XE 17.x — Configuring NAT for IP Address Conservation](https://www.cisco.com/c/en/us/td/docs/routers/ios/config/17-x/ip-addressing/b-ip-addressing/m_iadnat-addr-consv-xe.html) — Inside source address translation; static and dynamic translations; monitoring NAT

---

## CCNA6-067 · IP Services

Objectives: 4.2 · single · Applied

R1 has successfully synchronized to an external NTP server. R2 is configured with ntp server pointing to R1, and R1 permits and answers these requests. An engineer proposes ntp master on R1 so R2 can use it. Is that command required for this purpose?

- **A.** No; a synchronized NTP participant can serve its learned time to downstream clients.
- **B.** Yes; an NTP client can never answer any server-mode request.
- **C.** Yes; ntp master supplies the remote server's IP address to R2.
- **D.** No; R2 will obtain time through DHCP instead of NTP.

**Answer: A**

One device can obtain time upstream while supplying it downstream. ntp master concerns using the local clock as an authoritative source and is not a general prerequisite for serving synchronized time.

**Option explanations**

- **A:** R1 does not need to designate its free-running local clock as an authority.
- **B:** Client and server roles can coexist on a participating device.
- **C:** R2's ntp server command already identifies R1.
- **D:** The stated association is an NTP time exchange.

**Further reading**

- [Setting Time and Calendar Services](https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/bsm/configuration/15-mt/bsm-15-mt-book/bsm-time-calendar-set.html) — Network Time Protocol; configuring NTP associations; monitoring NTP
- [Use Best Practices for Network Time Protocol](https://www.cisco.com/c/en/us/support/docs/availability/high-availability/19643-ntpm.html) — NTP architecture; synchronization; verification

---

## CCNA6-068 · IP Services

Objectives: 4.3 · single · Applied

An authoritative DNS record was changed from 192.0.2.10 to 192.0.2.20. A recursive resolver had cached the old answer shortly before the change, and its original TTL has not expired. The resolver has no special refresh or serve-stale policy. Why can a client still receive 192.0.2.10?

- **A.** An A record is permanently immutable after its first query.
- **B.** The new address is invalid because DNS cannot return more than one address over a name's lifetime.
- **C.** The resolver can answer from its still-valid cached record.
- **D.** The DHCP server must change the host's MAC address first.

**Answer: C**

TTL bounds ordinary cache reuse; it is not a push notification of authoritative changes. The observations are consistent with an unexpired cache, without requiring a routing or DHCP fault.

**Option explanations**

- **A:** Records can change; caching controls temporary reuse.
- **B:** A host name can resolve to different addresses as its records change.
- **C:** Updating the authority does not instantly invalidate every existing cache.
- **D:** MAC identity does not control DNS cache expiration.

**Further reading**

- [RFC 1034 — Domain Names - Concepts and Facilities](https://www.rfc-editor.org/rfc/rfc1034.html) — 3.6 Resource records; 4.3 Name server algorithms; 5 Resolvers

---

## CCNA6-069 · IP Services

Objectives: 4.4 · single · Applied

A network monitor should read interface utilization but must not modify router settings. Its SNMP access is currently read-write. Which access change directly reduces the unnecessary capability while preserving polling?

- **A.** Disable all responses from the agent.
- **B.** Keep read-write access and poll more slowly.
- **C.** Grant only the required read access to the relevant objects.
- **D.** Replace Get requests with Set requests for every counter.

**Answer: C**

The manager's required function is retrieval, so write authority is unnecessary. Limiting accessible objects and operations reduces management capability without disabling the intended monitoring.

**Option explanations**

- **A:** This would also prevent the required monitoring.
- **B:** Polling frequency does not remove modification authority.
- **C:** Reads can continue without granting Set operations.
- **D:** Set changes writable values and is not a counter-reading operation.

**Further reading**

- [SNMP Configuration Guide, Cisco IOS XE 17 — Configuring SNMP Support](https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/snmp/configuration/xe-17-x/snmp-xe-17-book/nm-snmp-cfg-snmp-support.html) — Components of SNMP; operations; versions; traps and informs

---

## CCNA6-070 · IP Services

Objectives: 4.4 · single · Applied

An SNMP monitor successfully retrieves a router's uptime but receives noSuchObject for a vendor-specific sensor OID. The sensor object is not implemented by this model, and credentials are otherwise correct. What does this demonstrate?

- **A.** SNMP reachability does not imply that every vendor OID is implemented on every device.
- **B.** The missing OID proves the sensor reading is zero.
- **C.** All SNMP messages must be blocked by the network firewall.
- **D.** Changing from Get to GetNext makes the missing sensor object appear.

**Answer: A**

Management data depends on the device's supported MIB objects as well as transport and access. An unavailable object must not be silently converted into a normal zero reading.

**Option explanations**

- **A:** The agent can support standard objects while lacking this platform-specific object.
- **B:** An absent object is different from an existing object whose value is zero.
- **C:** A successful uptime response disproves a complete communication block.
- **D:** GetNext can advance to another implemented object but cannot create the unsupported sensor object.

**Further reading**

- [RFC 3416 — Version 2 of the Protocol Operations for the Simple Network Management Protocol (SNMP)](https://www.rfc-editor.org/rfc/rfc3416.html) — 4.2 PDU processing: Get, GetNext, GetBulk, Set, notifications
- [SNMP Configuration Guide, Cisco IOS XE 17 — Configuring SNMP Support](https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/snmp/configuration/xe-17-x/snmp-xe-17-book/nm-snmp-cfg-snmp-support.html) — Components of SNMP; operations; versions; traps and informs

---

## CCNA6-071 · IP Services

Objectives: 4.5 · matching · Applied

An operations runbook must interpret numeric syslog levels consistently. Match each described condition to its severity number. Use each option once.

1. A normal but significant operational state change.
2. The highest-urgency condition in the syslog severity scale.
3. Detailed diagnostic output intended for debugging.
4. A condition categorized as critical rather than warning or informational.

- **A.** 2 — critical
- **B.** 7 — debugging
- **C.** 5 — notifications
- **D.** 0 — emergencies

**Answer: 1 → C; 2 → D; 3 → B; 4 → A**

Severity numbers increase as urgency decreases. A significant event is not necessarily an error, while detailed debugging occupies level 7.

**Option explanations**

- **A:** This is the critical-conditions level, below alerts in urgency.
- **B:** This is the least urgent severity used for debugging detail.
- **C:** This records a normal but significant event.
- **D:** The most urgent severity denotes an unusable or unstable system condition.

**Further reading**

- [RFC 5424 — The Syslog Protocol](https://www.rfc-editor.org/rfc/rfc5424.html) — 6.2.1 PRI; 6.2.3 TIMESTAMP
- [System Message Logging](https://www.cisco.com/c/en/us/td/docs/routers/access/wireless/software/guide/SysMsgLogging.html) — System log message format; logging destinations; severity levels; timestamps

---

## CCNA6-072 · IP Services

Objectives: 4.6 · single · Applied

An IOS XE router obtains a WAN IPv4 address with ip address dhcp. The ISP replaces its DHCP server and starts rejecting this router's client identifier. The router sends requests but receives no usable lease. Which evidence is most relevant to investigate next?

- **A.** The DNS search domain offered to the WAN client.
- **B.** The client identifier in its requests and the ISP's matching allocation policy.
- **C.** The requested lease lifetime, assuming it replaces all identity checks.
- **D.** A helper address on an unrelated client VLAN.

**Answer: B**

A DHCP client needs more than physical link availability: the server must accept the request and allocate appropriate configuration. Compare the actual identifier sent with the server's intended client policy.

**Option explanations**

- **A:** A DNS suffix is a delivered parameter, not the stated identity used to accept this client.
- **B:** The stated rejection concerns DHCP client identity and eligibility.
- **C:** A lifetime preference does not replace the server's stated client-identifier eligibility policy.
- **D:** This WAN interface is requesting its own lease from the ISP; relaying another VLAN does not correct its identifier.

**Further reading**

- [IP Addressing: DHCP Configuration Guide, Cisco IOS XE 17 — Configuring the Cisco IOS XE DHCP Client](https://www.cisco.com/c/en/us/td/docs/routers/asr920/configuration/guide/ipaddr-dhcp/17-1-1/b-dhcp-xe-17-1-asr920/m_config-dhcp-client-xe.html) — Configuring the DHCP client; monitoring and maintaining DHCP client operation
- [RFC 2131 — Dynamic Host Configuration Protocol](https://www.rfc-editor.org/rfc/rfc2131.html) — 3.1 Address allocation; 4.3 Server behavior; 4.4 Client behavior

---

## CCNA6-073 · IP Services

Objectives: 4.7 · multiple · Applied

A QoS policy must distinguish business application traffic from other traffic, then set a DSCP value in selected packets. Which two functions are involved? Select two.

- **A.** Queuing
- **B.** Shaping
- **C.** Classification
- **D.** Scheduling
- **E.** Marking

**Answer: C, E**

Classification decides which traffic is being handled; marking encodes a treatment label. Queue selection and bandwidth enforcement remain additional policy functions.

**Option explanations**

- **A:** Queuing stores packets waiting for service; the stated task asks to identify traffic and write a label.
- **B:** Shaping controls release timing against a profile rather than identifying the application and setting DSCP.
- **C:** It identifies the class to which a packet belongs.
- **D:** Scheduling selects packets for transmission, which is beyond the stated identification and header-label task.
- **E:** It writes the selected label into the packet header.

**Further reading**

- [RFC 2475 — An Architecture for Differentiated Services](https://www.rfc-editor.org/rfc/rfc2475.html) — 2.3 Traffic classification and conditioning; 2.4 Per-hop behaviors

---

## CCNA6-074 · IP Services

Objectives: 4.8 · single · Applied

A router is configured for SSH-only VTY transport and login local. AAA is disabled. SSH key exchange succeeds, but every attempted username is rejected. Configuration inspection confirms that no local usernames exist. What change addresses the authentication gap?

- **A.** Replace ip ssh version 2 with version 1.
- **B.** Regenerate the already-working SSH host key without adding an account.
- **C.** Create the authorized local username with an appropriate secret.
- **D.** Set only a VTY line password while retaining login local.

**Answer: C**

Transport establishment and user authentication are separate stages. A functioning SSH host key can support the encrypted session while login still fails because the selected account database is empty.

**Option explanations**

- **A:** A protocol downgrade does not create an authorized username.
- **B:** Key exchange already works; the missing object is the user account.
- **C:** login local needs an account in the local username database.
- **D:** Local username authentication does not use a standalone line password as the account database.

**Further reading**

- [Configure SSH on Routers](https://www.cisco.com/c/en/us/support/docs/security-vpn/secure-shell-ssh/4145-ssh.html) — SSH server prerequisites; SSHv2; VTY restrictions; show commands

---

## CCNA6-075 · IP Services

Objectives: 4.9 · single · Applied

A passive-mode FTP server answers PASV with a data endpoint. The client can initiate outbound TCP connections to both the server's control and advertised data endpoints. Which host initiates the passive-mode data TCP connection?

- **A.** The DHCP relay
- **B.** The FTP server, always from TCP port 20
- **C.** The DNS resolver
- **D.** The FTP client

**Answer: D**

Passive mode changes who opens the data connection: the server listens and the client connects. The control connection and data connection remain separate.

**Option explanations**

- **A:** The relay does not establish file-transfer data connections.
- **B:** That describes the conventional active-mode direction rather than passive mode.
- **C:** The resolver is not an FTP data endpoint.
- **D:** Passive mode has the client connect to the server's advertised listening data endpoint.

**Further reading**

- [RFC 959 — File Transfer Protocol (FTP)](https://www.rfc-editor.org/rfc/rfc959.html) — 2.3 FTP model; 3.2 Data connections; 4.1 FTP commands

---

## CCNA6-076 · Security Fundamentals

Objectives: 5.1 · multiple · Applied

A firewall blocks an attempted exploit against a management server. The server still runs the vulnerable release. Which two statements are supported? Select two.

- **A.** The vulnerable software still needs remediation or an approved continuing treatment.
- **B.** The firewall event proves that no other exploit path exists.
- **C.** The server is no longer vulnerable because exploitation did not succeed on this attempt.
- **D.** The observed attempt was mitigated on the monitored path.

**Answer: A, D**

Use the block as specific evidence, not a claim that the defect or all exposure has disappeared. The vulnerable component’s lifecycle still requires a deliberate treatment.

**Option explanations**

- **A:** A blocked packet does not remove the underlying defect.
- **B:** One observed decision does not establish every path’s state.
- **C:** Vulnerability existence and this attempt’s outcome are separate facts.
- **D:** The logged block is evidence for that attempt and enforcement point.

**Further reading**

- [RFC 4949: Internet Security Glossary, Version 2](https://www.rfc-editor.org/rfc/rfc4949.html) — Section 2: threat, vulnerability, exploit, and countermeasure

---

## CCNA6-077 · Security Fundamentals

Objectives: 5.2 · single · Applied

A new network operator knows how to recognize phishing but has never performed the company’s approved equipment-room visitor procedure. Which program element most directly fills this gap?

- **A.** A badge reader purchase with no operating instructions.
- **B.** Another generic phishing awareness poster without visitor instructions.
- **C.** An annual signoff stating that training exists.
- **D.** Role-specific training that rehearses visitor verification and escort steps.

**Answer: D**

Awareness and task-specific training serve related but different needs. Teach and check the procedure the operator must actually carry out.

**Option explanations**

- **A:** Equipment procurement does not establish staff competence in visitor handling.
- **B:** This reinforces a skill already present rather than the identified gap.
- **C:** Acknowledgement alone does not teach or verify execution of the procedure.
- **D:** The missing ability is an operational procedure tied to the role.

**Further reading**

- [NIST SP 800-53 Rev. 5: Security and Privacy Controls for Information Systems and Organizations](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-53r5.pdf) — AT-2, AT-3, PE-2, and PE-3: awareness, training, and physical access

---

## CCNA6-078 · Security Fundamentals

Objectives: 5.3 · single · Challenge

A device has VTY lines 0–15 and AAA is disabled. An engineer configured login local only on lines 0–4; lines 5–15 contain login and a line password instead. SSH is allowed on every VTY. Which correction gives all available remote sessions the same local-account requirement?

```text
username engineer secret ValidLocal!
line vty 0 4
 login local
 transport input ssh
line vty 5 15
 password LegacyShared!
 login
 transport input ssh
```

- **A.** Change only the password under line vty 0 4.
- **B.** Apply login local to line vty 0 15 after confirming a working local account.
- **C.** Configure a stronger enable secret but leave the VTY authentication sources unchanged.
- **D.** Configure login local only under line console 0.

**Answer: B**

Verify every applicable VTY range. With AAA disabled, configure login local on all lines that should use the local username database, then verify authorized SSH access.

**Option explanations**

- **A:** Lines 0–4 already select local accounts; changing their line password does not configure local authentication on lines 5–15.
- **B:** All VTY lines capable of accepting sessions need the same authentication source.
- **C:** The enable challenge does not replace the initial VTY login source.
- **D:** That changes physical console login rather than all remote VTY lines.

**Further reading**

- [Catalyst 3750-X and 3560-X Configuration Guide: Configuring Switch-Based Authentication](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst3750x_3560x/software/release/15-0_2_se/configuration/guide/3750x_cg/swauthen.html) — Protecting Access to Privileged EXEC Commands; Configuring Username and Password Pairs
- [Configure SSH on Routers](https://www.cisco.com/c/en/us/support/docs/security-vpn/secure-shell-ssh/4145-ssh.html) — Configure SSH on a Cisco Router Using Password Authentication; Recommendations

---

## CCNA6-079 · Security Fundamentals

Objectives: 5.4 · single · Applied

A login requires a smart card to prove possession of a private key and a PIN to activate that card. The PIN is checked by the authenticator as required. Which two factor categories are represented?

- **A.** Knowledge and knowledge only.
- **B.** Possession and knowledge.
- **C.** Inherence and knowledge.
- **D.** Possession and inherence.

**Answer: B**

The authenticator demonstrates possession of its protected key, while its activation PIN demonstrates knowledge. The factor classification depends on what must actually be proven, not merely how many fields appear.

**Option explanations**

- **A:** The card’s private-key proof adds possession, not another memorized value.
- **B:** The physical key-bearing card and the memorized activation PIN are distinct categories.
- **C:** The card is an object under the user’s control, not a bodily characteristic.
- **D:** No biometric characteristic is described.

**Further reading**

- [NIST SP 800-63B-4: Digital Identity Guidelines — Authentication and Authenticator Management](https://pages.nist.gov/800-63-4/sp800-63b.html) — Authentication factors; password verifiers; authenticator management

---

## CCNA6-080 · Security Fundamentals

Objectives: 5.5 · single · Applied

A VPN gateway’s policy marks one corporate prefix for IPsec protection and marks a separate Internet destination for bypass. Both packets are routable. Which outcome correctly reflects this security policy?

- **A.** Both packets must be encrypted because a tunnel exists on the gateway.
- **B.** The bypass packet establishes a second encrypted tunnel automatically.
- **C.** Protect the corporate-prefix packet; bypass IPsec for the other packet.
- **D.** Both packets must be discarded because their destinations differ.

**Answer: C**

IPsec is applied according to policy selectors and actions. Inspect the traffic classification before interpreting tunnel existence as protection for a particular packet.

**Option explanations**

- **A:** An established tunnel does not override the configured selection policy.
- **B:** Bypass means that this IPsec policy does not apply protection.
- **C:** The configured policy applies different protection actions to the two traffic classes.
- **D:** Different destination classes are valid policy inputs.

**Further reading**

- [RFC 4301: Security Architecture for the Internet Protocol](https://www.rfc-editor.org/rfc/rfc4301.html) — Sections 3, 4.1, 4.4.1: IPsec services, tunnel mode, and security policy

---

## CCNA6-081 · Security Fundamentals

Objectives: 5.6 · single · Challenge

A stateless inbound ACL on the external interface permits only TCP packets from server 203.0.113.44 with source port 443 to client 10.6.0.8 with destination ports above 1023. Which claim would overstate what this ACL proves?

- **A.** A UDP packet will fail this TCP permit entry.
- **B.** Every permitted packet must belong to a TCP connection that the client previously established.
- **C.** A TCP packet with a different source address will fail this permit entry.
- **D.** A packet with destination port 22 will fail the stated destination-port condition.

**Answer: B**

Static ACLs inspect configured packet fields rather than validating a full connection history. Matching the expected return tuple alone is not proof of an established conversation.

**Option explanations**

- **A:** The transport protocol does not match.
- **B:** A static field match does not maintain or prove connection state.
- **C:** The entry fixes the source address.
- **D:** Port 22 is not above 1023.

**Further reading**

- [Configure IP Access Lists](https://www.cisco.com/c/en/us/support/docs/security/ios-firewall/23602-confaccesslists.html) — ACL Concepts; Masks; Process ACLs; Apply ACLs; Extended ACLs

---

## CCNA6-082 · Security Fundamentals

Objectives: 5.7 · single · Applied

DAI is active on VLAN 70. This switch has a valid snooping binding for a PC on untrusted Gi1/0/7. An ARP packet on that port claims the PC’s correct IP but a different sender MAC. No ARP ACL applies. What does DAI do when checking the sender binding?

- **A.** Accept the claim because the port’s access VLAN matches.
- **B.** Update the snooping table to the newly claimed MAC automatically.
- **C.** Accept the claim because the IP occurs anywhere in the binding table.
- **D.** Reject the claim because the IP-to-MAC pair does not match the authorized binding.

**Answer: D**

DAI is designed to prevent unauthorized ARP claims from replacing trusted mappings. The received sender must agree with the authorized binding or another explicit policy.

**Option explanations**

- **A:** VLAN membership alone does not validate the sender pair.
- **B:** Untrusted ARP is not authority to rewrite the DHCP-learned binding.
- **C:** Validation requires the permitted mapping, not merely a listed IP.
- **D:** A correct IP alone is insufficient when the associated MAC is wrong.

**Further reading**

- [Catalyst 3750-X and 3560-X Configuration Guide: Configuring Dynamic ARP Inspection](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst3750x_3560x/software/release/15-0_2_se/configuration/guide/3750x_cg/swdynarp.html) — Understanding Dynamic ARP Inspection; Rate Limiting; ARP ACLs

---

## CCNA6-083 · Security Fundamentals

Objectives: 5.8 · single · Applied

A central service rejects an incorrect password before any EXEC session is opened. Which function is failing in this observed exchange?

- **A.** Authentication.
- **B.** Command accounting.
- **C.** Command authorization.
- **D.** Session accounting retention.

**Answer: A**

Locate the failed stage in the access sequence. A credential rejection occurs during authentication, before later command permissions become the issue.

**Option explanations**

- **A:** The claimed identity has not been verified by the supplied credential.
- **B:** The user has not executed a command in the attempted session.
- **C:** No authenticated session has reached a command request in the described exchange.
- **D:** The rejection is an access decision, not a failure to retain records.

**Further reading**

- [RFC 8907: The Terminal Access Controller Access-Control System Plus (TACACS+) Protocol](https://www.rfc-editor.org/rfc/rfc8907.html) — Sections 5, 6, and 7: authentication, authorization, and accounting

---

## CCNA6-084 · Security Fundamentals

Objectives: 5.9 · single · Applied

A WPA3-Personal-only deployment requires protected management frames. One older client supports WPA2-Personal but lacks both SAE and PMF. Which conclusion is correct for that client?

- **A.** It can associate if the same passphrase text is configured.
- **B.** It can associate if the administrator hides the SSID.
- **C.** It can associate because PMF is only an IP routing feature.
- **D.** It cannot meet this WLAN’s stated WPA3-only security requirements.

**Answer: D**

Client capability is part of WLAN security compatibility. Credential agreement cannot compensate for absence of the authentication and management protection mechanisms.

**Option explanations**

- **A:** Matching text does not add the missing protocol capabilities.
- **B:** SSID advertisement does not supply SAE or PMF support.
- **C:** PMF protects defined wireless management exchanges, not IP routes.
- **D:** The client lacks required authentication and management-frame capabilities.

**Further reading**

- [Cisco Catalyst 9800 Configuration Guide, IOS XE 17.3.x: Wi-Fi Protected Access 3](https://www.cisco.com/c/en/us/td/docs/wireless/controller/9800/17-3/config-guide/b_wl_17_3_cg/m_wpa3.html) — WPA3-Personal; WPA3-Personal Transition Mode; Protected Management Frames

---

## CCNA6-085 · Security Fundamentals

Objectives: 5.10 · single · Applied

In an AireOS 8.10 maintenance window, a technician changes a WLAN to the approved WPA2-PSK settings, clicks Apply, and verifies a client connection. The controller’s saved configuration still contains the old settings. What completes persistence of the verified change?

- **A.** Repeat the client’s DHCP renewal without saving.
- **B.** Change the PSK again after verification but do not save.
- **C.** Close the GUI browser tab and assume Apply always saves startup state.
- **D.** Use Save Configuration after successful verification.

**Answer: D**

Applying a WLAN change and saving it are separate operations in the documented workflow. Verification confirms current behavior; saving preserves the intended state across restart.

**Option explanations**

- **A:** A client lease operation does not persist controller configuration.
- **B:** Another unsaved change does not solve the persistence gap.
- **C:** Closing the browser does not perform the controller’s save operation.
- **D:** Saving records the applied state for restoration after reboot.

**Further reading**

- [Cisco Wireless Controller Configuration Guide, Release 8.10: WLAN Security](https://www.cisco.com/c/en/us/td/docs/wireless/controller/8-10/config-guide/b_cg810/wlan_security.html) — WPA1+WPA2; Configuring WPA1+WPA2 (GUI); Protected Management Frames

---

## CCNA6-086 · Security Fundamentals

Objectives: 5.6 · single · Applied

The constructed ACL is inbound on a student VLAN. Which entry determines an ICMP echo packet from 10.60.3.25 to 192.0.2.12?

```text
ip access-list extended STUDENT-IN
 10 deny tcp any host 192.0.2.12 eq 80
 20 permit ip host 10.60.3.25 any
 30 deny ip any any
```

- **A.** Sequence 20 permits it.
- **B.** Sequence 10 denies it because the destination address matches.
- **C.** No ACL entry can match ICMP because ICMP has no ports.
- **D.** Sequence 30 denies it because all ICMP is implicit traffic.

**Answer: A**

Matching a destination alone does not make a TCP entry match an ICMP packet. Evaluation continues to the next applicable rule and stops at the host permit.

**Option explanations**

- **A:** The ICMP packet does not match the TCP deny but does match the source-host IP permit.
- **B:** Every specified field must match; ICMP is not TCP.
- **C:** The ip protocol keyword encompasses ICMP without a port test.
- **D:** The packet already matches an explicit permit.

**Further reading**

- [Configure IP Access Lists](https://www.cisco.com/c/en/us/support/docs/security/ios-firewall/23602-confaccesslists.html) — ACL Concepts; Masks; Process ACLs; Apply ACLs; Extended ACLs

---

## CCNA6-087 · Security Fundamentals

Objectives: 5.6 · single · Applied

A policy requires one ACL entry matching precisely the source range 192.168.48.0 through 192.168.51.255. Which pair expresses this aligned range?

- **A.** 192.168.48.0 0.0.1.255
- **B.** 192.168.48.0 0.0.3.255
- **C.** 192.168.48.0 0.0.0.255
- **D.** 192.168.48.0 0.0.7.255

**Answer: B**

Four aligned /24 networks combine into a /22. Inverting 255.255.252.0 gives the wildcard 0.0.3.255.

**Option explanations**

- **A:** One variable bit covers only third octets 48–49.
- **B:** Two variable low bits in the third octet cover 48–51.
- **C:** This covers only one /24, third octet 48.
- **D:** Three variable bits extend the range through third octet 55.

**Further reading**

- [Configure IP Access Lists](https://www.cisco.com/c/en/us/support/docs/security/ios-firewall/23602-confaccesslists.html) — ACL Concepts; Masks; Process ACLs; Apply ACLs; Extended ACLs

---

## CCNA6-088 · Security Fundamentals

Objectives: 5.7 · multiple · Applied

An operator wants authorized server replies accepted only on Gi1/0/48 while leaving client interfaces untrusted. Which two lines are part of the required DHCP snooping setup for VLAN 80? Select two. Snooping is already globally enabled.

- **A.** ip dhcp snooping vlan 80 in global configuration.
- **B.** ip dhcp snooping trust under every VLAN 80 access port.
- **C.** ip dhcp snooping trust under Gi1/0/48.
- **D.** no ip dhcp snooping in global configuration.

**Answer: A, C**

The feature needs both the correct VLAN scope and a justified trusted server path. Client-facing ports retain their untrusted state.

**Option explanations**

- **A:** This selects VLAN 80 for inspection.
- **B:** Trusting all client ingress would defeat the required server-message restriction.
- **C:** This permits authorized server messages arriving over the verified server path.
- **D:** Disabling the feature removes the intended inspection.

**Further reading**

- [Catalyst 3750-X and 3560-X Configuration Guide: Configuring DHCP Features and IP Source Guard](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst3750x_3560x/software/release/15-0_2_se/configuration/guide/3750x_cg/swdhcp82.html) — DHCP Snooping; DHCP Snooping Binding Database; Enabling DHCP Snooping

---

## CCNA6-089 · Security Fundamentals

Objectives: 5.7 · single · Applied

A Catalyst port has a manually configured secure MAC for a workstation. The workstation’s NIC is replaced, and the new NIC has a different MAC. The port’s secure-address maximum is 1. What maintenance action preserves a one-device policy?

- **A.** Disable logging without changing the secure MAC.
- **B.** Increase the maximum to 100 and leave the old entry in place.
- **C.** Change the workstation’s IP address while retaining the new MAC and old secure entry.
- **D.** Verify the replacement NIC and replace the obsolete secure MAC entry with its approved address.

**Answer: D**

A secure MAC restriction follows the configured link-layer identity. Hardware replacement requires controlled update of that identity and verification of the resulting forwarding behavior.

**Option explanations**

- **A:** Reducing visibility does not authorize the new source.
- **B:** This greatly broadens access instead of retaining a one-device policy.
- **C:** Port security checks the source MAC rather than fixing the issue through IP addressing.
- **D:** The authorized hardware change must be reflected in the pinned source identity.

**Further reading**

- [Catalyst 3750-X and 3560-X Configuration Guide: Configuring Port-Based Traffic Control](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst3750x_3560x/software/release/15-0_2_se/configuration/guide/3750x_cg/swtrafc.html) — Secure MAC Addresses; Security Violations; Port Security Aging

---

## CCNA6-090 · Security Fundamentals

Objectives: 5.4 · single · Applied

A biometric characteristic is part of an authentication design. Which management consideration distinguishes it from an ordinary memorized password?

- **A.** A compromised biometric characteristic cannot be replaced as freely as a generated password.
- **B.** The biometric trait can be made secret simply by changing the username.
- **C.** Biometrics make every additional authentication control unnecessary.
- **D.** A biometric match necessarily identifies the user’s current authorization role.

**Answer: A**

Biometrics require careful protection and recovery planning because the underlying traits are not easily rotated. Authentication evidence also remains separate from the permissions granted afterward.

**Option explanations**

- **A:** Biometric traits are inherently less replaceable, so template protection and other safeguards matter.
- **B:** Changing an account identifier does not replace the physical characteristic.
- **C:** A biometric mechanism still has limitations and is part of a larger authenticator design.
- **D:** Matching a characteristic does not determine the permissions granted.

**Further reading**

- [NIST SP 800-63B-4: Digital Identity Guidelines — Authentication and Authenticator Management](https://pages.nist.gov/800-63-4/sp800-63b.html) — Authentication factors; password verifiers; authenticator management

---

## CCNA6-091 · Automation and Programmability

Objectives: 6.1 · single · Applied

An automated change disables a required service on several switches. The team has a known-good configuration backup and an approved restoration workflow. Which use of automation best supports recovery?

- **A.** Rerun the faulty change until all devices are identical
- **B.** Mark the deployment successful because the script completed
- **C.** Restore the known-good settings and verify service behavior on each target
- **D.** Discard the backups because automated changes are irreversible

**Answer: C**

Automation can assist recovery as well as deployment. A known-good restoration followed by service verification gives evidence that the affected targets have returned to the required condition.

**Option explanations**

- **A:** Consistency with a harmful configuration does not restore the required service.
- **B:** Completion is not evidence that the service works.
- **C:** Recovery needs both controlled restoration and confirmation of the intended result.
- **D:** Automation can also perform an authorized restoration workflow.

**Further reading**

- [What Is Network Automation?](https://www.cisco.com/site/us/en/learn/topics/networking/what-is-network-automation.html) — Network automation; profiles and policies; automated lifecycle management

---

## CCNA6-092 · Automation and Programmability

Objectives: 6.2 · single · Applied

A campus replaces isolated device-management screens with a controller that collects topology and health information across the managed network. Which operational advantage follows directly from that capability?

- **A.** Operators can examine related device observations in a common network view
- **B.** Every user packet is now captured in full by the controller
- **C.** A common screen proves the controller’s observations are always current
- **D.** Physical cabling failures become impossible

**Answer: A**

A controller can consolidate information that would otherwise be inspected device by device. The consolidated view improves visibility, but the freshness and completeness of its observations still matter.

**Option explanations**

- **A:** Aggregated information helps relate events and dependencies across devices.
- **B:** Topology and health collection do not imply full packet capture.
- **C:** Telemetry can still be delayed or missing.
- **D:** Management visibility does not eliminate physical failure mechanisms.

**Further reading**

- [Software-Defined Networking (SDN) Definition](https://www.cisco.com/c/en/us/solutions/software-defined-networking/overview.html) — SDN elements; Features and benefits

---

## CCNA6-093 · Automation and Programmability

Objectives: 6.3 · single · Challenge

An overlay adds encapsulation headers to client traffic. Small overlay packets cross the underlay, but larger ones exceed the supported transport MTU and are dropped; fragmentation is not available. Which action addresses the stated cause?

- **A.** Rename the overlay virtual network
- **B.** Ensure the underlay path supports the encapsulated packet size
- **C.** Move the client address into the northbound API URI
- **D.** Remove the route to the remote tunnel endpoint

**Answer: B**

Overlay encapsulation increases the size of the packet that the underlay must carry. An MTU design must account for that overhead along the entire transport path.

**Option explanations**

- **A:** A name change does not reduce packet size or increase supported MTU.
- **B:** The transport must accommodate the original traffic plus encapsulation overhead.
- **C:** API resource naming is unrelated to the data-packet MTU.
- **D:** Loss of endpoint reachability would prevent all such overlay transport.

**Further reading**

- [Software-Defined Access](https://www.cisco.com/c/en/us/td/docs/solutions/CVD/Campus/cisco-sda-design-guide.html) — SD-Access architecture; Underlay network; Overlay network; Overlay control plane – LISP; Data plane – VXLAN

---

## CCNA6-094 · Automation and Programmability

Objectives: 6.4 · single · Applied

A model predicts low wireless risk, but its inputs omit every access point in a newly opened building. Users there report repeated disconnections. What limitation best explains why the model’s output is insufficient for that building?

- **A.** Predictive models must always report high risk for new sites
- **B.** JSON telemetry cannot contain wireless measurements
- **C.** A low-risk prediction is equivalent to a successful client connectivity test
- **D.** Missing relevant telemetry limits what the model can infer

**Answer: D**

AI analytics cannot compensate reliably for a missing operational view merely by processing other sites’ data. The new building needs appropriate observations and validation before the prediction can support a conclusion about it.

**Option explanations**

- **A:** The appropriate conclusion depends on evidence, not a mandatory risk label.
- **B:** JSON can represent measurements from many network types.
- **C:** A prediction is not a direct test of those clients.
- **D:** The model lacks observations for the location being evaluated.

**Further reading**

- [What is AIOps?](https://developer.cisco.com/articles/what-is-aiops/) — The core components of AIOps; Is AIOps all you need?

---

## CCNA6-095 · Automation and Programmability

Objectives: 6.5 · matching · Applied

Match each documented API action with its HTTP method. The API uses standard resource CRUD conventions and supports the stated operations. Use each method once.

1. Read the existing /sites/8 resource
2. Create a new member of /sites as documented
3. Replace the complete existing /sites/8 representation
4. Remove the /sites/8 resource association

- **A.** DELETE
- **B.** GET
- **C.** POST
- **D.** PUT

**Answer: 1 → B; 2 → C; 3 → D; 4 → A**

The method supplies the operation semantics while the URI identifies its target. This API documents collection creation with POST and complete replacement with PUT.

**Option explanations**

- **A:** DELETE requests removal of the identified resource association.
- **B:** GET retrieves a representation without requesting a state change.
- **C:** POST to this documented collection creates a new member.
- **D:** PUT supplies replacement state for this existing resource.

**Further reading**

- [RFC 9110: HTTP Semantics](https://www.rfc-editor.org/rfc/rfc9110.html) — 9 Methods; 15 Status Codes

---

## CCNA6-096 · Automation and Programmability

Objectives: 6.5 · multiple · Applied

An automation script uses a Meraki Dashboard API key owned by an administrator. That administrator has read-only access to an organization. Which two statements correctly describe this access model? Select two.

- **A.** The key inherits that administrator’s permissions in the organization
- **B.** The key grants write access merely because the request is automated
- **C.** Changing GET to POST changes the administrator’s role
- **D.** The key should be handled as a secret credential
- **E.** Publishing the key in the script is safe because it is not a password

**Answer: A, D**

An admin-scoped API key carries the permissions associated with its owner in the relevant organization. It needs secret handling even when the permitted access is read-only.

**Option explanations**

- **A:** Admin-scoped API keys operate within the owner’s role.
- **B:** Automation does not elevate a read-only administrative role.
- **C:** HTTP methods request operations; they do not grant authorization.
- **D:** Disclosure can expose the authority associated with the key.
- **E:** An API key is still sensitive authentication material.

**Further reading**

- [Authorization - Meraki Dashboard API v1](https://developer.cisco.com/meraki/api-v1/authorization/) — Admin-scoped access: API keys; Bearer Auth; Security Best Practice

---

## CCNA6-097 · Automation and Programmability

Objectives: 6.6 · single · Foundation

A network team stores reusable Ansible tasks, defaults and templates in a standard package so multiple playbooks can apply the same configuration function. Which Ansible capability is being used?

- **A.** An inventory alias
- **B.** A forwarding information base
- **C.** A role
- **D.** A Terraform state lock

**Answer: C**

Ansible roles package related automation content in a standard structure. This supports reuse across playbooks without independently rewriting the same tasks and templates.

**Option explanations**

- **A:** An alias identifies a managed host; it does not package this reusable task structure.
- **B:** The forwarding table is part of packet handling.
- **C:** Roles organize reusable tasks and related files for inclusion in playbooks.
- **D:** A state lock coordinates Terraform state access, not Ansible task reuse.

**Further reading**

- [Roles](https://docs.ansible.com/projects/ansible/latest/playbook_guide/playbooks_reuse_roles.html) — Role directory structure; Using roles

---

## CCNA6-098 · Automation and Programmability

Objectives: 6.6 · single · Challenge

A team marks a Terraform input as sensitive so normal CLI output hides its value. The value is still stored in a local state file by the resource being used. What protection remains necessary?

- **A.** No additional protection, because sensitive means the file is encrypted
- **B.** Protect access to the state file and any copies containing the value
- **C.** Rename the variable so the value disappears from existing state
- **D.** Put the state file in a public repository for integrity

**Answer: B**

A sensitive marking controls ordinary display; it does not make every stored occurrence confidential. In this stated case, the state file and backups require appropriate access protection.

**Option explanations**

- **A:** Output redaction is not state-file encryption.
- **B:** The stored secret remains sensitive even when console output is redacted.
- **C:** Renaming is not reliable deletion of stored sensitive data.
- **D:** Public exposure conflicts with keeping its sensitive contents confidential.

**Further reading**

- [Manage sensitive data in your configuration](https://developer.hashicorp.com/terraform/language/manage-sensitive-data) — Hide sensitive variables and outputs; state and plan files

---

## CCNA6-099 · Automation and Programmability

Objectives: 6.7 · single · Applied

A client processes the array of interface objects shown. Which statement accurately locates the administratively disabled interface?

```text
[{"name":"Gi1/0/1","enabled":true},{"name":"Gi1/0/2","enabled":false}]
```

- **A.** The second array element has enabled:false
- **B.** The first array element has enabled:false
- **C.** The root value is an object keyed by interface name
- **D.** There are four array elements because there are four members

**Answer: A**

The root is an array of two objects. The enabled member in the second object is false, identifying Gi1/0/2 under the stated administrative interpretation.

**Option explanations**

- **A:** The second element describes Gi1/0/2 with a Boolean false value.
- **B:** The first element’s enabled value is true.
- **C:** The outer square brackets contain an array, not such a keyed object.
- **D:** Two members inside each object do not create separate outer elements.

**Further reading**

- [RFC 8259: The JavaScript Object Notation (JSON) Data Interchange Format](https://www.rfc-editor.org/rfc/rfc8259.html) — 2 JSON Grammar; 3 Values; 4 Objects; 5 Arrays; 6 Numbers; 7 Strings

---

## CCNA6-100 · Automation and Programmability

Objectives: 6.7 · single · Foundation

A JSON request is rejected for invalid syntax. Which change fixes only the syntax error in the exhibit, preserving both member values?

```text
{"name":"loopback-4","mtu":1500,}
```

- **A.** Quote the complete document as one string
- **B.** Replace the colon after mtu with an equals sign
- **C.** Replace 1500 with the word fifteen-hundred
- **D.** Remove the comma immediately before the closing brace

**Answer: D**

Commas separate members; they do not follow the final member of an object. Removing that trailing comma preserves the existing name and numeric MTU.

**Option explanations**

- **A:** That changes the root into a string rather than preserving the object.
- **B:** JSON member names and values are separated with a colon.
- **C:** That unquoted text is not a valid JSON value.
- **D:** JSON does not allow a trailing comma after the last object member.

**Further reading**

- [RFC 8259: The JavaScript Object Notation (JSON) Data Interchange Format](https://www.rfc-editor.org/rfc/rfc8259.html) — 2 JSON Grammar; 3 Values; 4 Objects; 5 Arrays; 6 Numbers; 7 Strings

---
