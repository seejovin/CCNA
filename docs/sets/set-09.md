# CCNA Practice — Set 09

100 original questions aligned to CCNA 200-301 v1.1. No interactive labs.

Answers and explanations follow each question. For an unrevealed attempt, use the Streamlit app.

Content review date: 2026-09-14.

## CCNA9-001 · Network Fundamentals

Objectives: 1.1.b, 1.1.g · single · Applied

A server’s Ethernet interface sends to a second server in the same VLAN through a Layer 2 switch. Both servers have consistent same-subnet addressing. The default gateway is unavailable, but the destination MAC is known. Which outcome is expected if no other faults or policies interfere?

- **A.** Local communication must wait for the gateway to recover
- **B.** The servers can exchange local traffic through the switch
- **C.** Both servers must use their public addresses
- **D.** The switch must install a static IP route for the flow

**Answer: B**

A default gateway provides a path beyond the directly connected subnet. Local switched traffic can continue without it.

**Option explanations**

- **A:** Same-subnet Layer 2 delivery does not require that gateway.
- **B:** The switch can forward between their known local MAC locations.
- **C:** Local delivery does not require public address assignment.
- **D:** Ordinary same-VLAN forwarding needs no route for this local flow.

**Further reading**

- [Comparing Layer 3 and Layer 2 Switches](https://documentation.meraki.com/Switching/MS_-_Switches/Design_and_Configure/Configuration_Guides/Layer_3_Switching/Comparing_Layer_3_and_Layer_2_Switches) — Comparing Layer 3 and Layer 2 Switches (main article)
- [Configure IP Addresses and Unique Subnets for New Users](https://www.cisco.com/c/en/us/support/docs/ip/routing-information-protocol-rip/13788-3.html) — Network Masks; Understand Subnetting; VLSM Example

---

## CCNA9-002 · Network Fundamentals

Objectives: 1.2.a, 1.2.b · single · Foundation

A design has 20 access switches, four distribution switches, and two core switches. An engineer calls it a 26-tier design because it contains 26 devices. What is the correct classification?

- **A.** Two-tier because there are two core switches
- **B.** Four-tier because there are four distribution switches
- **C.** Twenty-six-tier because all devices forward traffic
- **D.** Three-tier because access, distribution, and core are separate roles

**Answer: D**

Tier names express hierarchy and function. Multiple devices can occupy the same architectural tier.

**Option explanations**

- **A:** Redundant devices in one tier do not determine the tier count.
- **B:** Distribution redundancy does not add functional tiers.
- **C:** Tier count is not a device count.
- **D:** The three functional layers define this campus hierarchy.

**Further reading**

- [Campus LAN and Wireless LAN Solution Design Guide](https://www.cisco.com/c/en/us/td/docs/solutions/CVD/Campus/cisco-campus-lan-wlan-design-guide.html) — Hierarchical design model; Three-tier design

---

## CCNA9-003 · Network Fundamentals

Objectives: 1.3.a · single · Applied

A transceiver pair supports 10GBASE-SR to 300 m on OM3 and 400 m on OM4. A 350 m path must be used, and its loss budget is otherwise satisfactory. Which supplied cable type meets the listed SR reach specification?

| Module mode | Fiber | Listed maximum reach |
| --- | --- | --- |
| 10GBASE-SR | OM3 | 300 m |
| 10GBASE-SR | OM4 | 400 m |

- **A.** OM4 multimode fiber
- **B.** OM3 multimode fiber
- **C.** 160 m of copper followed by passive copper extensions
- **D.** Any fiber type because loss alone determines reach

**Answer: A**

Use the reach specified for the exact fiber type. An acceptable loss budget does not override another documented distance or dispersion limit.

**Option explanations**

- **A:** The stated 350 m path is within its 400 m limit.
- **B:** The path exceeds the listed 300 m reach.
- **C:** That does not satisfy the proposed optical link specification.
- **D:** Fiber type and modal bandwidth constraints also matter.

**Further reading**

- [Cisco 10GBASE SFP+ Modules Data Sheet](https://www.cisco.com/c/en/us/products/collateral/interfaces-modules/transceiver-modules/data_sheet_c78-455693.html) — Cisco SFP-10G-SR module; Cisco SFP-10G-LR module; Cisco SFP-10G-T-X module

---

## CCNA9-004 · Network Fundamentals

Objectives: 1.4 · single · Applied

A full-duplex interface shows zero CRC errors but increasing output drops during a known sustained burst exceeding its egress capacity. Which interpretation is best supported?

```text
During overload interval:
CRC delta: 0
Output-drop delta: 2300
Operational duplex: full
```

- **A.** CRC-free traffic proves the interface has unlimited capacity
- **B.** Output drops prove the cable is reversing frame bits
- **C.** Egress congestion can discard otherwise valid frames
- **D.** The peer must be half duplex

**Answer: C**

Distinguish physical corruption counters from congestion-related discards. Both affect delivery, but they suggest different investigations.

**Option explanations**

- **A:** Frame integrity does not remove queue and bandwidth limits.
- **B:** CRC evidence does not support that physical-corruption conclusion.
- **C:** Finite output capacity can cause queue drops during overload.
- **D:** No duplex mismatch evidence is provided.

**Further reading**

- [Configure and Verify Ethernet 10/100/1000Mb Half/Full Duplex Auto-Negotiation](https://www.cisco.com/c/en/us/support/docs/lan-switching/ethernet/10561-3.html) — Background Information; Auto-Negotiation on Catalyst Switches that Run Cisco IOS Software
- [QoS Frequently Asked Questions](https://www.cisco.com/c/en/us/support/docs/quality-of-service-qos/qos-policing/22833-qos-faq.html) — Queueing and Congestion Management

---

## CCNA9-005 · Network Fundamentals

Objectives: 1.5 · multiple · Applied

Which TWO statements correctly compare TCP and UDP transport ports? Select two.

- **A.** Only TCP can distinguish multiple applications on one host
- **B.** Both headers contain source and destination port fields
- **C.** TCP port 53 and UDP port 53 are necessarily the same transport endpoint
- **D.** The IP transport protocol distinguishes otherwise equal TCP and UDP port numbers
- **E.** UDP has an acknowledgment number in place of its destination port

**Answer: B, D**

Port numbers are meaningful together with the transport protocol. Equal numbers do not make TCP and UDP interchangeable.

**Option explanations**

- **A:** UDP also provides source and destination ports.
- **B:** Ports support transport endpoint identification for both protocols.
- **C:** Protocol identity distinguishes the transport namespaces.
- **D:** TCP and UDP are separate protocols even when numeric ports match.
- **E:** UDP retains a destination port and has no TCP-style acknowledgment field.

**Further reading**

- [RFC 9293: Transmission Control Protocol (TCP)](https://www.rfc-editor.org/rfc/rfc9293.html#section-2.2) — 2.2. Key TCP Concepts
- [RFC 768: User Datagram Protocol](https://www.rfc-editor.org/rfc/rfc768) — Introduction; Fields

---

## CCNA9-006 · Network Fundamentals

Objectives: 1.6 · single · Challenge

A technician plans 10.88.5.64/26 for VLAN A and 10.88.5.96/27 for VLAN B on separate routed interfaces. What is the addressing problem?

- **A.** The two subnets overlap
- **B.** Both subnet identifiers are unaligned
- **C.** The /27 has no usable addresses
- **D.** Private IPv4 prefixes cannot be divided into VLAN subnets

**Answer: A**

Evaluate allocated ranges, not only whether their written starting addresses differ. A valid smaller subnet can still lie inside an existing larger one.

**Option explanations**

- **A:** The /26 spans .64–.127 and includes the entire proposed /27.
- **B:** Both are individually valid boundaries for their masks.
- **C:** It has 30 ordinary usable addresses.
- **D:** Subnetting private ranges is valid; overlap is the problem.

**Further reading**

- [Configure IP Addresses and Unique Subnets for New Users](https://www.cisco.com/c/en/us/support/docs/ip/routing-information-protocol-rip/13788-3.html) — Network Masks; Understand Subnetting; VLSM Example

---

## CCNA9-007 · Network Fundamentals

Objectives: 1.7 · single · Foundation

A branch host uses 172.30.4.10. Its administrator changes its mask from /24 to /25. Does that change whether the address is RFC 1918 private?

- **A.** Yes; only /24 masks qualify as private
- **B.** Yes; /25 turns it into IPv4 link-local
- **C.** Yes; a longer prefix makes the address public
- **D.** No; the address still lies within 172.16.0.0/12

**Answer: D**

The mask changes which destinations the host considers on-link. It does not move the numeric address out of its allocated private range.

**Option explanations**

- **A:** The private allocation is not limited to /24 local subnets.
- **B:** Changing this mask does not move the address into 169.254/16.
- **C:** Prefix length alone does not change the address’s membership in RFC 1918 space.
- **D:** Local subnetting does not alter the address’s private-range membership.

**Further reading**

- [RFC 1918: Address Allocation for Private Internets](https://www.rfc-editor.org/rfc/rfc1918#section-3) — 3. Private Address Space
- [Configure IP Addresses and Unique Subnets for New Users](https://www.cisco.com/c/en/us/support/docs/ip/routing-information-protocol-rip/13788-3.html) — Network Masks; Understand Subnetting; VLSM Example

---

## CCNA9-008 · Network Fundamentals

Objectives: 1.8 · multiple · Applied

Which TWO entries are in different /64 networks from 2001:db8:91:44::10/64? Select two.

- **A.** 2001:db8:91:44::abcd/64
- **B.** 2001:db8:91:44:1::10/64
- **C.** 2001:db8:91:45::10/64
- **D.** 2001:db8:92:44::10/64
- **E.** 2001:0db8:0091:0044:0000:0000:0000:0011/64

**Answer: C, D**

Compare the bits before the stated prefix boundary. Differences after the fourth hextet do not create another /64.

**Option explanations**

- **A:** Only host bits differ; the first four hextets match.
- **B:** The fifth hextet is in the interface portion.
- **C:** The fourth hextet differs inside the /64 prefix.
- **D:** The third hextet differs inside the /64 prefix.
- **E:** Expanded notation preserves the same first four hextets.

**Further reading**

- [RFC 4291: IP Version 6 Addressing Architecture](https://www.rfc-editor.org/rfc/rfc4291#section-2.3) — 2.3. Text Representation of Address Prefixes; 2.4. Address Type Identification; 2.5.6. Link-Local IPv6 Unicast Addresses; 2.7. Multicast Addresses

---

## CCNA9-009 · Network Fundamentals

Objectives: 1.9 · single · Applied

A packet capture shows source :: during initial IPv6 address configuration. Which interpretation is correct?

- **A.** It is the all-nodes multicast source
- **B.** It is the unspecified address used before an address is available for certain procedures
- **C.** It proves the source is the loopback interface ::1
- **D.** It is an ordinary global-unicast host allocation

**Answer: B**

The unspecified address differs from loopback and multicast. Its legitimate use is constrained to procedures that permit an unspecified source.

**Option explanations**

- **A:** All-nodes multicast is ff02::1, and multicast is not a normal source address.
- **B:** All-zero IPv6 denotes the absence of a specified source in allowed initialization exchanges.
- **C:** The unspecified and loopback addresses differ.
- **D:** The all-zero address is not assigned as a normal interface address.

**Further reading**

- [RFC 4291: IP Version 6 Addressing Architecture](https://www.rfc-editor.org/rfc/rfc4291#section-2.3) — 2.3. Text Representation of Address Prefixes; 2.4. Address Type Identification; 2.5.6. Link-Local IPv6 Unicast Addresses; 2.7. Multicast Addresses

---

## CCNA9-010 · Network Fundamentals

Objectives: 1.10 · single · Applied

Windows shows the intended IPv4 address, mask, and gateway, but a hostname fails while a test to its known IP succeeds. Which displayed parameter should be investigated next for name resolution?

- **A.** The Ethernet adapter’s physical address
- **B.** The DHCP lease duration alone
- **C.** The DNS Servers entries
- **D.** The subnet broadcast address

**Answer: C**

The differing results separate basic IP reachability from name lookup. Resolver configuration and responses are a logical next check, without yet proving a particular DNS root cause.

**Option explanations**

- **A:** Correct IP connectivity does not make that the direct resolver setting.
- **B:** Lease duration is not the configured resolver address.
- **C:** They identify the resolvers used for ordinary name lookups.
- **D:** Broadcast calculation does not identify the DNS service to query.

**Further reading**

- [ipconfig](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/ipconfig) — Syntax; Parameters (/all)

---

## CCNA9-011 · Network Fundamentals

Objectives: 1.11.c · single · Applied

A room has excellent signal from one AP but many simultaneously active clients. Adding transmit power alone does not improve aggregate application throughput. Which explanation is most plausible?

- **A.** Shared airtime and load can be the constraint even with strong signal
- **B.** A stronger signal necessarily creates more nonoverlapping channels
- **C.** Every client receives a dedicated physical channel on association
- **D.** RSSI is itself a direct measure of application throughput

**Answer: A**

A coverage measurement is not a capacity test. Contention, client rates, protocol overhead, and offered load influence delivered throughput.

**Option explanations**

- **A:** Coverage strength and traffic capacity are different dimensions.
- **B:** Transmit power does not add spectrum.
- **C:** Many clients share the AP’s channel resources.
- **D:** Received power does not include every throughput constraint.

**Further reading**

- [Wireless Throughput Calculations and Limitations](https://documentation.meraki.com/Wireless/Design_and_Configure/Architecture_and_Best_Practices/Wireless_Throughput_Calculations_and_Limitations) — Limitations and Factors Affecting Throughput

---

## CCNA9-012 · Network Fundamentals

Objectives: 1.12 · single · Applied

A container image is moved between two Linux hosts. Which requirement must be considered because ordinary Linux process containers share their host’s kernel?

- **A.** The image must include a booted independent guest kernel
- **B.** The source and destination must have identical MAC addresses
- **C.** The destination must use the same IPv4 host address
- **D.** The destination kernel must support the application’s required kernel interfaces/features

**Answer: D**

An image packages application userspace, while the host supplies the kernel. Portability still has compatibility requirements.

**Option explanations**

- **A:** Ordinary containers do not boot a separate kernel.
- **B:** MAC identity is not a kernel compatibility requirement.
- **C:** Address reuse is not required for container execution.
- **D:** Container packaging does not replace the underlying kernel ABI and capabilities.

**Further reading**

- [What is a container?](https://docs.docker.com/get-started/docker-concepts/the-basics/what-is-a-container/#containers-versus-virtual-machines-vms) — Containers versus virtual machines (VMs)

---

## CCNA9-013 · Network Fundamentals

Objectives: 1.13.a, 1.13.d · single · Applied

A switch has a manually configured static MAC mapping to Gi1/0/9. The destination remains silent beyond the dynamic aging interval. How should that interval affect the static mapping?

- **A.** It becomes dynamic after one aging period
- **B.** It is not removed merely by the dynamic-entry aging timer
- **C.** It moves to the lowest numbered port
- **D.** It forces all VLANs to share the same mapping

**Answer: B**

Dynamic expiration and static configuration have different lifecycles. An administrator must consider whether the configured static location remains correct.

**Option explanations**

- **A:** Aging does not convert static configuration into learned state.
- **B:** Static mappings are administratively configured rather than aged like dynamic entries.
- **C:** Silence does not establish a new port location.
- **D:** VLAN context remains relevant.

**Further reading**

- [Configuring MAC Address Tables](https://www.cisco.com/c/en/us/td/docs/switches/datacenter/nexus5500/sw/layer2/7x/b_5500_Layer2_Config_7x/config_mac_address_tables.pdf) — Information About MAC Addresses (page 1); Configuring the Aging Time for the MAC Table (page 2)

---

## CCNA9-014 · Network Fundamentals

Objectives: 1.1.h · multiple · Applied

A PoE switch can provide a powered device’s requested wattage, but the vendor states that the endpoint requires a compatible PoE standard and negotiation mechanism. Which TWO checks remain necessary? Select two.

- **A.** Whether the switch supports the required power delivery method
- **B.** Whether the client’s TCP port is below 1024
- **C.** Whether the device’s IPv6 address contains ff:fe
- **D.** Whether the SSID is broadcast
- **E.** Whether the installed channel supports the specified power/data requirements

**Answer: A, E**

PoE selection must satisfy electrical/protocol compatibility and the real channel, not just a wattage label. Budget is one constraint among several.

**Option explanations**

- **A:** Wattage alone does not establish protocol or electrical compatibility.
- **B:** Transport port numbering is unrelated to PoE negotiation.
- **C:** Interface identifier appearance is not a PoE requirement.
- **D:** WLAN name advertisement does not negotiate PoE.
- **E:** The physical channel is part of the power delivery path.

**Further reading**

- [Interface and Hardware Components Configuration Guide, Cisco IOS XE 17.14.x (Catalyst 9200 Switches): Configuring Power over Ethernet](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst9200/software/release/17-14/configuration_guide/int_hw/b_1714_int_and_hw_9200_cg/configuring_poe.html) — Powered-Device Detection and Initial Power Allocation

---

## CCNA9-015 · Network Fundamentals

Objectives: 1.6 · single · Applied

The planned LAN is 198.51.100.128/26. The router uses its first usable address, and a workstation must use its last usable address. Which workstation/gateway pair is correct?

- **A.** Workstation .191, gateway .129
- **B.** Workstation .190, gateway .128
- **C.** Workstation .190, gateway .129
- **D.** Workstation .254, gateway .193

**Answer: C**

The /26 block ends at .191. Use the addresses immediately inside its two reserved boundaries.

**Option explanations**

- **A:** The .191 address is broadcast.
- **B:** The .128 address is the subnet identifier.
- **C:** The usable range is .129 through .190.
- **D:** These belong to the next /26 subnet.

**Further reading**

- [Configure IP Addresses and Unique Subnets for New Users](https://www.cisco.com/c/en/us/support/docs/ip/routing-information-protocol-rip/13788-3.html) — Network Masks; Understand Subnetting; VLSM Example

---

## CCNA9-016 · Network Fundamentals

Objectives: 1.9.d · single · Applied

A host has a randomized stable IPv6 interface identifier. An engineer attempts to recover its MAC using the modified EUI-64 inverse operation. Why is that inference unjustified?

- **A.** Only addresses beginning fe80 can contain interface identifiers
- **B.** All IPv6 identifiers must equal the last 64 bits of a MAC address
- **C.** Modified EUI-64 always encrypts the MAC address
- **D.** The identifier was not specified as MAC-derived EUI-64

**Answer: D**

An IPv6 address does not inherently disclose a recoverable MAC address. Establish the identifier-generation method before applying EUI-64 reasoning.

**Option explanations**

- **A:** Global and unique local addresses also contain interface portions.
- **B:** Ethernet MAC addresses are ordinarily 48 bits, and several identifier methods exist.
- **C:** Its bit manipulation is not encryption.
- **D:** The reverse calculation only applies when the relevant derivation was used.

**Further reading**

- [RFC 2464: Transmission of IPv6 Packets over Ethernet Networks](https://datatracker.ietf.org/doc/html/rfc2464#section-4) — 4. Stateless Autoconfiguration
- [RFC 7217: A Method for Generating Semantically Opaque Interface Identifiers with IPv6 Stateless Address Autoconfiguration (SLAAC)](https://www.rfc-editor.org/rfc/rfc7217.html) — 4. Design Goals; 5. Algorithm Specification

---

## CCNA9-017 · Network Fundamentals

Objectives: 1.11.a, 1.11.c · single · Applied

A 2.4 GHz AP uses channel 6 at 20 MHz. A nearby non-Wi-Fi device emits energy across that frequency range. Why can a conventional nonoverlapping Wi-Fi channel plan still experience interference?

- **A.** The channel plan only separates planned Wi-Fi channels; it cannot silence unrelated emitters
- **B.** All non-Wi-Fi transmitters automatically join the SSID
- **C.** Nonoverlapping channels disable encryption
- **D.** Wi-Fi channel numbers describe TCP ports

**Answer: A**

Avoiding overlap among planned AP channels is useful but incomplete. The surrounding spectrum can contain other interfering sources.

**Option explanations**

- **A:** Other radio energy can overlap the chosen frequencies.
- **B:** They do not need WLAN association to emit RF energy.
- **C:** Channel allocation and encryption are separate.
- **D:** They describe RF channel placement.

**Further reading**

- [Channel Planning Best Practices](https://documentation.meraki.com/Wireless/Design_and_Configure/Architecture_and_Best_Practices/Channel_Planning_Best_Practices) — 2.4 GHz
- [Common Sources of Wireless Interference](https://documentation.meraki.com/Wireless/Design_and_Configure/Architecture_and_Best_Practices/Common_Sources_of_Wireless_Interference) — Physical interference; other wireless devices

---

## CCNA9-018 · Network Fundamentals

Objectives: 1.13.b · single · Applied

A router forwards an IP packet from one Ethernet LAN to another. Which destination MAC should appear on its outgoing Ethernet frame when the IP destination is a directly connected host?

- **A.** The original sender’s MAC
- **B.** The directly connected destination host’s resolved MAC
- **C.** The ingress switch’s management MAC
- **D.** The same destination MAC on every router hop regardless of next hop

**Answer: B**

Ethernet addressing is local to the current link. Routing preserves the relevant IP destination while constructing the next link’s frame.

**Option explanations**

- **A:** That source belongs to the previous link.
- **B:** The outgoing link-layer header identifies the next local recipient.
- **C:** That management address is not the forwarding destination.
- **D:** Layer 2 headers are constructed for each outgoing link.

**Further reading**

- [Comparing Layer 3 and Layer 2 Switches](https://documentation.meraki.com/Switching/MS_-_Switches/Design_and_Configure/Configuration_Guides/Layer_3_Switching/Comparing_Layer_3_and_Layer_2_Switches) — Comparing Layer 3 and Layer 2 Switches (main article)
- [Configuring MAC Address Tables](https://www.cisco.com/c/en/us/td/docs/switches/datacenter/nexus5500/sw/layer2/7x/b_5500_Layer2_Config_7x/config_mac_address_tables.pdf) — Information About MAC Addresses (page 1); Configuring the Aging Time for the MAC Table (page 2)

---

## CCNA9-019 · Network Fundamentals

Objectives: 1.2.f · single · Foundation

A workload moves to a public-cloud VM. Its operator assumes there is no underlying physical network to troubleshoot. Which statement corrects that assumption?

- **A.** Virtual networks replace Ethernet and optics everywhere
- **B.** Cloud traffic cannot cross a WAN
- **C.** Virtual resources still depend on physical compute and network infrastructure
- **D.** The customer must personally own every cloud switch

**Answer: C**

Cloud changes the service boundary and responsibility split. It does not eliminate physical dependencies.

**Option explanations**

- **A:** Physical infrastructure still carries underlying traffic.
- **B:** Cloud access can depend on wide-area connectivity.
- **C:** Virtualization abstracts underlying resources without removing them.
- **D:** The provider may own and operate that infrastructure.

**Further reading**

- [NIST SP 800-145: The NIST Definition of Cloud Computing](https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-145.pdf) — 2. The NIST Definition of Cloud Computing — Essential Characteristics; Deployment Models
- [What is a container?](https://docs.docker.com/get-started/docker-concepts/the-basics/what-is-a-container/#containers-versus-virtual-machines-vms) — Containers versus virtual machines (VMs)

---

## CCNA9-020 · Network Fundamentals

Objectives: 1.9.a, 1.9.b, 1.9.c · matching · Applied

Match each intended IPv6 delivery behavior to its address concept. Use each option once.

1. A packet is directed to one of several service instances advertising one shared address.
2. A host talks to a neighbor using its fe80 address on the selected link.
3. An internal server uses an fd prefix routed between selected corporate sites.
4. A sender targets subscribed members of an IPv6 group.

- **A.** Multicast
- **B.** Link-local unicast
- **C.** Anycast
- **D.** Unique local unicast

**Answer: 1 → C; 2 → B; 3 → D; 4 → A**

Scope and delivery model are distinct dimensions. Address use must match both the recipient pattern and the intended routing scope.

**Option explanations**

- **A:** Delivery targets members of a group.
- **B:** An individual interface is addressed within one link.
- **C:** A shared address reaches a routing-selected instance.
- **D:** An internally routed individual address uses the local ULA allocation.

**Further reading**

- [RFC 4291: IP Version 6 Addressing Architecture](https://www.rfc-editor.org/rfc/rfc4291#section-2.3) — 2.3. Text Representation of Address Prefixes; 2.4. Address Type Identification; 2.5.6. Link-Local IPv6 Unicast Addresses; 2.7. Multicast Addresses
- [RFC 4193: Unique Local IPv6 Unicast Addresses](https://www.rfc-editor.org/rfc/rfc4193#section-3.1) — 1. Introduction; 3.1. Format
- [RFC 4786: Operation of Anycast Services](https://www.rfc-editor.org/rfc/rfc4786#section-2) — 2. Terminology; 3.1. General Description; 3.2. Goals

---

## CCNA9-021 · Network Access

Objectives: 2.1.a · multiple · Challenge

A Cisco phone follows the displayed voice VLAN policy. Its attached PC sends ordinary untagged data. Which TWO interpretations apply to this dot1p design? Select TWO.

```text
interface GigabitEthernet1/0/6
 switchport mode access
 switchport access vlan 40
 switchport voice vlan dot1p
```

- **A.** The phone can include Layer 2 priority information with the priority-tagged voice frames.
- **B.** The switch creates a usable Ethernet broadcast domain named VLAN 0.
- **C.** The PC is automatically moved into VLAN 140.
- **D.** Voice remains in access VLAN 40 rather than a separate numbered voice VLAN.

**Answer: A, D**

The dot1p option differs from specifying a numbered voice VLAN. It supplies priority tagging while using the access/native classification described by this phone design.

**Option explanations**

- **A:** 802.1p priority tagging conveys CoS without choosing a separate nonzero VID.
- **B:** VID 0 indicates priority tagging, not an ordinary configurable VLAN membership.
- **C:** No VLAN 140 assignment appears in the configuration.
- **D:** Priority tagging with VID 0 does not select a separate user VLAN.

**Further reading**

- [VLAN Configuration Guide, Cisco IOS XE 17.15.x — Configuring Voice VLANs](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst9300/software/release/17-15/configuration_guide/vlan/b_1715_vlan_9300_cg/configuring_voice_vlans.html) — Cisco IP Phone Voice Traffic; Cisco IP Phone Data Traffic

---

## CCNA9-022 · Network Access

Objectives: 2.1.c · single · Applied

A host in VLAN 11 can reach a host in VLAN 21 through a correctly configured multilayer switch. An administrator claims that separate VLAN IDs alone guarantee those hosts cannot exchange IP packets. What does the working test demonstrate?

- **A.** A default VLAN automatically disables every routing policy.
- **B.** VLANs separate Layer 2 domains, while permitted Layer 3 routing can reconnect them.
- **C.** A switch cannot perform routing under any circumstances.
- **D.** Both hosts must actually be using the same VLAN ID.

**Answer: B**

Segmentation and communication policy are related but distinct. If inter-VLAN traffic must be restricted, the design needs the appropriate Layer 3 enforcement as well.

**Option explanations**

- **A:** The default VLAN has no such overriding function.
- **B:** A VLAN boundary alone is not a prohibition on configured inter-VLAN routing.
- **C:** A multilayer switch with routing enabled can route between SVIs.
- **D:** Different VLANs can communicate through their gateways.

**Further reading**

- [Configure Inter-VLAN Routing with Catalyst Switches](https://www.cisco.com/c/en/us/support/docs/lan-switching/inter-vlan-routing/41260-189.html) — Configure; Troubleshoot

---

## CCNA9-023 · Network Access

Objectives: 2.1 · single · Applied

Two switches have one link configured as an access port in VLAN 55 at both ends. Each switch has local users only in VLAN 55 for this test. There are no other paths. Can this link extend that one VLAN without being a trunk?

- **A.** Yes; an access link can connect the same single VLAN using untagged frames.
- **B.** No; the switches need an IP routing adjacency to exchange these same-VLAN frames.
- **C.** No; every interswitch cable must be a trunk regardless of the traffic.
- **D.** Yes; it automatically carries every VLAN as well.

**Answer: A**

Interface function follows the required traffic scope. A one-VLAN access connection is possible, although trunks are commonly used for multi-VLAN interswitch designs.

**Option explanations**

- **A:** A trunk is needed for multi-VLAN carriage, not every possible switch-to-switch link.
- **B:** Layer 2 switching within the VLAN does not require a routing protocol.
- **C:** An intentionally configured single-VLAN access link can forward that VLAN.
- **D:** An ordinary access link does not provide general multi-VLAN carriage.

**Further reading**

- [VLAN Configuration Guide, Cisco IOS XE 17.15.x — Configuring VLANs](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst9300/software/release/17-15/configuration_guide/vlan/b_1715_vlan_9300_cg/configuring_vlans.html) — Supported VLANs; Deleting a VLAN; VLAN Port Membership Modes
- [VLAN Configuration Guide, Cisco IOS XE 17.15.x — Configuring VLAN Trunks](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst9300/software/release/17-15/configuration_guide/vlan/b_1715_vlan_9300_cg/configuring_vlan_trunks.html) — Allowed VLANs on a Trunk; Configuring the Native VLAN for Untagged Traffic

---

## CCNA9-024 · Network Access

Objectives: 2.2.a · single · Applied

A new trunk must admit only approved user VLANs 101 and 102; all ordinary user traffic from other VLANs must be excluded. Which configuration directly expresses that whitelist?

- **A.** switchport trunk native vlan 101
- **B.** switchport access vlan 102
- **C.** switchport trunk allowed vlan 101,102
- **D.** switchport trunk allowed vlan all

**Answer: C**

Express the desired scope in the trunk’s allowed list. Native-VLAN selection and endpoint access assignment answer different configuration questions.

**Option explanations**

- **A:** Selecting a native VLAN does not restrict all other VLANs.
- **B:** An access assignment is not the allowed list of an operational trunk.
- **C:** An explicit allowed list confines admission to the stated VLANs.
- **D:** This permits additional VLANs beyond the requested whitelist.

**Further reading**

- [VLAN Configuration Guide, Cisco IOS XE 17.15.x — Configuring VLAN Trunks](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst9300/software/release/17-15/configuration_guide/vlan/b_1715_vlan_9300_cg/configuring_vlan_trunks.html) — Allowed VLANs on a Trunk; Configuring the Native VLAN for Untagged Traffic

---

## CCNA9-025 · Network Access

Objectives: 2.2.b · single · Applied

A switch forwards a VLAN 66 frame from a tagged 802.1Q trunk toward an ordinary untagged PC on an access port in VLAN 66. What Ethernet representation does the PC normally receive?

- **A.** A CAPWAP packet solely because the incoming frame was tagged
- **B.** An untagged frame on its access connection
- **C.** A frame whose IP destination is replaced with VLAN 66
- **D.** A frame carrying every VLAN tag allowed on the original trunk

**Answer: B**

VLAN tags are link-specific representations. The same VLAN can be tagged on a trunk and delivered untagged on an access edge.

**Option explanations**

- **A:** 802.1Q switching does not inherently create a wireless tunnel.
- **B:** The switch retains internal VLAN identity while using the access port’s untagged egress behavior.
- **C:** VLAN tagging does not replace the IP destination field.
- **D:** A frame is not replicated into a stack of every allowed VLAN tag.

**Further reading**

- [VLAN Configuration Guide, Cisco IOS XE 17.15.x — Configuring VLAN Trunks](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst9300/software/release/17-15/configuration_guide/vlan/b_1715_vlan_9300_cg/configuring_vlan_trunks.html) — Allowed VLANs on a Trunk; Configuring the Native VLAN for Untagged Traffic
- [VLAN Configuration Guide, Cisco IOS XE 17.15.x — Configuring VLANs](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst9300/software/release/17-15/configuration_guide/vlan/b_1715_vlan_9300_cg/configuring_vlans.html) — Supported VLANs; Deleting a VLAN; VLAN Port Membership Modes

---

## CCNA9-026 · Network Access

Objectives: 2.3 · single · Applied

An engineer enables lldp transmit and lldp receive on a Catalyst interface, but the global configuration still contains no lldp run. The peer is sending valid LLDP. What missing step should be checked first?

```text
no lldp run
interface GigabitEthernet1/0/14
 lldp transmit
 lldp receive
```

- **A.** Create a VLAN matching the neighbor’s hostname.
- **B.** Enable an OSPF area on the interface.
- **C.** Enable LLDP globally with lldp run.
- **D.** Set the port to passive LACP.

**Answer: C**

Neighbor discovery depends on both global and interface configuration. Confirm the protocol is actually running before investigating received neighbor fields.

**Option explanations**

- **A:** Names do not supply global discovery-protocol operation.
- **B:** Routing adjacencies are not prerequisites for LLDP.
- **C:** Interface direction settings do not replace the global protocol enable.
- **D:** Aggregation mode does not enable LLDP globally.

**Further reading**

- [Interface and Hardware Components Configuration Guide, Cisco IOS XE 17.15.x — Configuring LLDP, LLDP-MED, and Wired Location Service](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst9300/software/release/17-15/configuration_guide/int_hw/b_1715_int_and_hw_9300_cg/configuring_lldp__lldp_med__and_wired_location_service.html) — LLDP; Enabling LLDP; Monitoring and Maintaining LLDP, LLDP-MED, and Wired Location Service

---

## CCNA9-027 · Network Access

Objectives: 2.4 · single · Applied

Two physical trunks between a pair of switches previously appeared as separate STP paths. After a compatible LACP EtherChannel is formed, how should STP treat the bundle?

- **A.** As one logical port-channel path for each carried spanning-tree instance
- **B.** As no Layer 2 path because LACP disables every STP instance
- **C.** As two independent paths that must always block alternate physical members
- **D.** As one router adjacency per source MAC address

**Answer: A**

A valid bundle changes the logical topology presented to STP. Verify member consistency so the physical endpoints agree on that logical link.

**Option explanations**

- **A:** Aggregation hides the member links behind one logical switching interface.
- **B:** STP can operate on a Layer 2 EtherChannel.
- **C:** A correctly formed aggregate is not treated as independent parallel trunks.
- **D:** That is not spanning-tree or EtherChannel behavior.

**Further reading**

- [Layer 2 Configuration Guide, Cisco IOS XE 17.15.x — Configuring EtherChannels](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst9300/software/release/17-15/configuration_guide/lyr2/b_1715_lyr2_9300_cg/configuring_etherchannels.html) — LACP Modes; EtherChannel Configuration Guidelines; Load Balancing; Layer 3 EtherChannels; Hot-Standby Ports

---

## CCNA9-028 · Network Access

Objectives: 2.4 · multiple · Applied

A Layer 3 EtherChannel must keep working when either physical member is replaced during maintenance. Which TWO configuration practices support the correct logical attachment? Select TWO.

- **A.** Maintain compatible routed settings and LACP membership on the physical members.
- **B.** Keep the transit IP address on the port-channel.
- **C.** Bind each IP subnet to an individual cable instead of the aggregate.
- **D.** Assign the peer’s IP address to both local members.

**Answer: A, B**

Separate the stable logical interface from replaceable physical members. Correct addressing and compatible aggregation settings are both necessary.

**Option explanations**

- **A:** Members must still belong to the same supported routed aggregate.
- **B:** The address remains with the logical interface rather than a replaceable member.
- **C:** That changes the design into separate routed links rather than one aggregate.
- **D:** Duplicate peer addressing is incorrect and does not establish logical continuity.

**Further reading**

- [Layer 2 Configuration Guide, Cisco IOS XE 17.15.x — Configuring EtherChannels](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst9300/software/release/17-15/configuration_guide/lyr2/b_1715_lyr2_9300_cg/configuring_etherchannels.html) — LACP Modes; EtherChannel Configuration Guidelines; Load Balancing; Layer 3 EtherChannels; Hot-Standby Ports

---

## CCNA9-029 · Network Access

Objectives: 2.5.a · single · Challenge

An access switch reaches the same root by paths with total costs 8 and 12. The engineer must prefer the currently higher-cost path for this VLAN without changing root placement anywhere. Which type of adjustment directly targets that decision?

- **A.** Adjust this switch’s relevant per-VLAN interface path cost so the desired path has the lower total.
- **B.** Rename the preferred uplink RootPort.
- **C.** Increase the root bridge’s MAC address by changing an interface description.
- **D.** Disable all BPDUs on the undesired link.

**Answer: A**

Change the variable used by the intended decision. A local per-VLAN cost adjustment can steer the root path without requiring a different root bridge.

**Option explanations**

- **A:** Root-port selection compares path costs while the root identity can remain unchanged.
- **B:** Descriptions do not influence protocol comparisons.
- **C:** A description does not alter the bridge ID, and root placement is not the requested change.
- **D:** Suppressing topology information can create unsafe forwarding rather than controlled path selection.

**Further reading**

- [Layer 2 Configuration Guide, Cisco IOS XE 17.15.x — Configuring Spanning Tree Protocol](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst9300/software/release/17-15/configuration_guide/lyr2/b_1715_lyr2_9300_cg/configuring_spanning_tree_protocol.html) — Spanning-Tree Topology and Bridge Protocol Data Units; Bridge ID, Device Priority, and Extended System ID; (Optional) Configuring a Secondary Root Device
- [VLAN Configuration Guide, Cisco IOS XE 17.15.x — Configuring VLAN Trunks](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst9300/software/release/17-15/configuration_guide/vlan/b_1715_vlan_9300_cg/configuring_vlan_trunks.html) — Allowed VLANs on a Trunk; Configuring the Native VLAN for Untagged Traffic

---

## CCNA9-030 · Network Access

Objectives: 2.5.b · single · Applied

A nonedge Rapid PVST+ port is in discarding state. Which statement correctly describes ordinary data handling while that state persists?

- **A.** It forwards frames but suppresses only ARP.
- **B.** It learns all user MACs and forwards after one packet.
- **C.** It neither forwards ordinary user frames nor learns their source MAC addresses.
- **D.** It must ignore every BPDU because all frame processing is disabled.

**Answer: C**

Do not confuse user-data blocking with complete interface shutdown. STP still needs protocol information to determine whether the port should change state.

**Option explanations**

- **A:** Discarding is not an ARP-only restriction.
- **B:** That does not describe the defined discarding state.
- **C:** Discarding blocks both user forwarding and data-frame MAC learning.
- **D:** Spanning-tree control processing can continue while ordinary data is discarded.

**Further reading**

- [Understand Rapid Spanning Tree Protocol (802.1w)](https://www.cisco.com/c/en/us/support/docs/lan-switching/spanning-tree-protocol/24062-146.html) — New Port States and Port Roles — Port States; Alternate and Backup Port Roles

---

## CCNA9-031 · Network Access

Objectives: 2.5.c · single · Applied

A PortFast configuration was intended for a laptop port, but the cable now leads to a small bridge connecting another switch. Which operational evidence best tests whether the original edge assumption is still valid?

- **A.** The desktop wallpaper on the originally connected laptop
- **B.** Only successful DNS resolution from one host
- **C.** Only the access VLAN’s text description
- **D.** Received BPDUs and the actual downstream Layer 2 connections

**Answer: D**

PortFast configuration should be checked against the current attachment. Topology changes at the edge can invalidate an earlier safe assumption.

**Option explanations**

- **A:** That does not describe the current network topology.
- **B:** Application success does not rule out an unintended Layer 2 path.
- **C:** A label cannot prove that the connected device is nonbridging.
- **D:** These reveal whether the attachment participates in bridging beyond a single endpoint.

**Further reading**

- [Layer 2 Configuration Guide, Cisco IOS XE 17.15.x — Configuring Optional Spanning-Tree Features](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst9300/software/release/17-15/configuration_guide/lyr2/b_1715_lyr2_9300_cg/configuring_optional_spanning_tree_features.html) — PortFast; Bridge Protocol Data Unit Guard; Bridge Protocol Data Unit Filtering; Root Guard; Loop Guard
- [Understand Rapid Spanning Tree Protocol (802.1w)](https://www.cisco.com/c/en/us/support/docs/lan-switching/spanning-tree-protocol/24062-146.html) — New Port States and Port Roles — Port States; Alternate and Backup Port Roles

---

## CCNA9-032 · Network Access

Objectives: 2.5.d · single · Challenge

A port is protected by root guard. A colleague proposes adding loop guard on the same port as well in this Catalyst design. What must the review recognize?

- **A.** Combining them is mandatory on every workstation port.
- **B.** Root guard and loop guard are mutually exclusive on the same interface in this implementation.
- **C.** Root guard changes the interface into a routed port.
- **D.** Loop guard is only an alias for BPDU filtering.

**Answer: B**

Choose the guard according to the port’s intended role and failure condition. More enabled feature names do not automatically produce a valid design.

**Option explanations**

- **A:** Neither that universal placement nor simultaneous interface use is correct.
- **B:** They protect different topology conditions and cannot both be enabled there.
- **C:** It changes spanning-tree protection, not Layer 2/Layer 3 mode.
- **D:** Loop guard monitors missing expected BPDUs; filtering suppresses them.

**Further reading**

- [Layer 2 Configuration Guide, Cisco IOS XE 17.15.x — Configuring Optional Spanning-Tree Features](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst9300/software/release/17-15/configuration_guide/lyr2/b_1715_lyr2_9300_cg/configuring_optional_spanning_tree_features.html) — PortFast; Bridge Protocol Data Unit Guard; Bridge Protocol Data Unit Filtering; Root Guard; Loop Guard

---

## CCNA9-033 · Network Access

Objectives: 2.6 · matching · Applied

Match the requirement to a suitable Cisco AP operating mode, assuming the AP model supports each listed mode. Use each answer once.

1. Campus client traffic must all be tunneled to a controller
2. Branch clients need a locally switched WLAN
3. Troubleshooter needs selected-channel Wi-Fi frame captures
4. Supported deployment needs wireless backhaul between AP locations

- **A.** Bridge/mesh backhaul mode
- **B.** Sniffer packet-capture mode
- **C.** Local mode with central client switching
- **D.** FlexConnect branch service mode

**Answer: 1 → C; 2 → D; 3 → B; 4 → A**

The mode determines the AP’s primary service or observation role. Hardware support and the rest of the deployment still need verification.

**Option explanations**

- **A:** Bridge mode provides supported wireless mesh/backhaul operation.
- **B:** Sniffer captures 802.11 frames for packet analysis.
- **C:** Local mode provides controller-based client service with centrally tunneled traffic.
- **D:** FlexConnect supports selected local client switching at a branch.

**Further reading**

- [Cisco Wireless Controller Configuration Guide, Release 8.5 — Managing APs](https://www.cisco.com/c/en/us/td/docs/wireless/controller/8-5/config-guide/b_cg85/managing_aps.html) — AP Modes: client-serving and network management modes

---

## CCNA9-034 · Network Access

Objectives: 2.6 · single · Applied

A local-mode AP and its WLC are separated by a WAN. A design review considers moving one WLAN to FlexConnect local switching while keeping the same client SSID. Which architectural dependency changes for that WLAN’s ordinary data?

- **A.** The client no longer needs any authentication policy.
- **B.** The SSID becomes a routing protocol automatically.
- **C.** Its wired egress can move from the WLC to the branch AP.
- **D.** Every branch packet must still traverse the WLC data tunnel by definition.

**Answer: C**

Client-facing naming does not fully describe the data path. Changing switching architecture also changes where VLANs and network policy must be enforced.

**Option explanations**

- **A:** Switching location does not remove admission requirements.
- **B:** A network name does not acquire routing behavior.
- **C:** The forwarding location changes even if the client-facing name remains the same.
- **D:** That describes central switching rather than the proposed local path.

**Further reading**

- [Cisco Wireless Controller Configuration Guide, Release 8.10 — FlexConnect](https://www.cisco.com/c/en/us/td/docs/wireless/controller/8-10/config-guide/b_cg810/flexconnect.html) — Configuring the Switch at a Remote Site; Configuring an Access Point for FlexConnect (GUI)
- [Cisco Wireless Controller Configuration Guide, Release 8.5 — Managing APs](https://www.cisco.com/c/en/us/td/docs/wireless/controller/8-5/config-guide/b_cg85/managing_aps.html) — AP Modes: client-serving and network management modes

---

## CCNA9-035 · Network Access

Objectives: 2.7 · single · Applied

A branch client locally switched by an AP reaches its local gateway, but cannot reach headquarters during a WAN outage. The AP is operating as designed. Which claim should be rejected?

- **A.** Remote service reachability depends on a working path beyond the AP.
- **B.** Local switching guarantees connectivity to every remote destination during a WAN failure.
- **C.** AP health and WAN health should be measured separately.
- **D.** Local resources can remain available when their local dependencies survive.

**Answer: B**

Local switching can preserve local service, not erase remote-network dependencies. Define availability in terms of the destination and complete path.

**Option explanations**

- **A:** The WAN is still required for headquarters destinations.
- **B:** Local egress cannot restore a failed path beyond the branch.
- **C:** Those are distinct components of the end-to-end service path.
- **D:** That is consistent with the stated local gateway reachability.

**Further reading**

- [Cisco Wireless Controller Configuration Guide, Release 8.10 — FlexConnect](https://www.cisco.com/c/en/us/td/docs/wireless/controller/8-10/config-guide/b_cg810/flexconnect.html) — Configuring the Switch at a Remote Site; Configuring an Access Point for FlexConnect (GUI)

---

## CCNA9-036 · Network Access

Objectives: 2.7 · single · Applied

A WLC has two distribution links connected to one logical Catalyst stack as a documented supported aggregate. What property of the stack matters to this design compared with two unrelated switches?

- **A.** The stack replaces all WLAN security settings.
- **B.** The stack presents a coordinated logical switching system for the aggregate.
- **C.** The stack removes the need to permit client VLANs.
- **D.** The stack makes both power supplies impossible to fail together.

**Answer: B**

A supported shared logical-switch design addresses aggregate coordination. It does not automatically solve VLAN policy, power independence, or controller redundancy.

**Option explanations**

- **A:** Physical aggregation does not authenticate wireless clients.
- **B:** The member endpoints can participate in one supported logical switching design.
- **C:** The aggregate still needs the required trunk VLAN policy.
- **D:** A logical stack does not prove independent power or eliminate common failures.

**Further reading**

- [Cisco Wireless Controller Configuration Guide, Release 8.10 — Ports and Interfaces](https://www.cisco.com/c/en/us/td/docs/wireless/controller/8-10/config-guide/b_cg810/ports_and_interfaces.html) — Restrictions on Link Aggregation; Configuring Neighbor Devices to Support Link Aggregation
- [Layer 2 Configuration Guide, Cisco IOS XE 17.15.x — Configuring EtherChannels](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst9300/software/release/17-15/configuration_guide/lyr2/b_1715_lyr2_9300_cg/configuring_etherchannels.html) — LACP Modes; EtherChannel Configuration Guidelines; Load Balancing; Layer 3 EtherChannels; Hot-Standby Ports

---

## CCNA9-037 · Network Access

Objectives: 2.8 · single · Applied

An operator configures a valid TACACS+ server for device administration but leaves Telnet enabled as the only remote CLI transport. Which remaining weakness is directly related to the operator-to-device path?

- **A.** LLDP encrypts the Telnet payload on the local link.
- **B.** Every Telnet packet is automatically transformed into HTTPS.
- **C.** TACACS+ prevents any administrator from being identified.
- **D.** The Telnet session lacks encryption even though authentication is centralized.

**Answer: D**

Central authentication and encrypted remote administration must each be configured. Replace cleartext CLI access with a supported secure transport.

**Option explanations**

- **A:** Neighbor discovery does not encrypt other protocols.
- **B:** The transport does not change simply because a server handles AAA.
- **C:** Central AAA can identify users; that is not the stated issue.
- **D:** AAA server selection does not protect the separate terminal transport.

**Further reading**

- [Cisco Wireless Controller Configuration Guide, Release 8.10 — AAA Administration](https://www.cisco.com/c/en/us/td/docs/wireless/controller/8-10/config-guide/b_cg810/aaa_administration.html) — Configuring TACACS+ (GUI)
- [Cisco Wireless Controller Configuration Guide, Release 8.10 — Administration of Controller](https://www.cisco.com/c/en/us/td/docs/wireless/controller/8-10/config-guide/b_cg810/administration_of_cisco_wlc.html) — Logging on to the Controller CLI; Enabling Web and Secure Web Modes (GUI); Enabling Web and Secure Web Modes (CLI)

---

## CCNA9-038 · Network Access

Objectives: 2.9 · single · Applied

A Catalyst 9800 WLAN is mapped to policy profile Branch-Users. Its default VLAN field uses the name Employees. The branch Flex profile maps only Staff to VLAN 330, although the intended client VLAN is 330. Which inconsistency should be corrected?

| GUI object | Setting |
| --- | --- |
| Policy profile default VLAN | Employees |
| Flex profile VLAN mapping | Staff → 330 |
| Design client VLAN | 330 |

- **A.** Rename the AP radio interface Employees without changing profiles.
- **B.** Change the client’s username to Staff.
- **C.** Use a consistent VLAN-name mapping, or the intended explicit VLAN ID, across the policy and Flex profiles.
- **D.** Set every trunk’s native VLAN to the WLAN profile name.

**Answer: C**

A human-readable VLAN reference must resolve to the intended local VLAN. Check the mapping chain rather than relying on similar descriptive names.

**Option explanations**

- **A:** Radio names do not supply the VLAN-name-to-ID mapping.
- **B:** The identity string is not this profile mapping.
- **C:** The named VLAN must resolve correctly in the effective branch Flex configuration.
- **D:** Native VLAN configuration uses a VLAN ID, not a profile label.

**Further reading**

- [Configure FlexConnect with Authentication on Catalyst 9800 WLC](https://www.cisco.com/c/en/us/support/docs/wireless/catalyst-9800-series-wireless-controllers/213921-flexconnect-configuration-with-central-a.html) — Background Information; Policy Profile Configuration

---

## CCNA9-039 · Network Access

Objectives: 2.9 · single · Applied

An AireOS WLAN must support clients that implement WMM while also permitting supported legacy clients without WMM. The administrator wants WMM capability when available, rather than excluding non-WMM clients. Which policy matches?

- **A.** WMM Disabled
- **B.** WMM Required
- **C.** Broadcast SSID Disabled
- **D.** WMM Allowed

**Answer: D**

Choose allowed when the capability is optional for admission. Required and disabled impose different client-compatibility outcomes.

**Option explanations**

- **A:** Disabled does not offer WMM capability even to capable clients.
- **B:** Required excludes clients that cannot satisfy WMM capability.
- **C:** SSID advertisement is independent of WMM admission policy.
- **D:** Allowed permits WMM and compatible non-WMM clients rather than making the feature mandatory.

**Further reading**

- [Cisco Wireless Controller Configuration Guide, Release 8.10 — Radio Bands](https://www.cisco.com/c/en/us/td/docs/wireless/controller/8-10/config-guide/b_cg810/radio_bands.html) — Configuring the 802.11n Parameters (GUI), Step 5 — WMM Policy

---

## CCNA9-040 · Network Access

Objectives: 2.9 · multiple · Applied

The GUI values below are for a new AireOS employee WLAN. Policy requires enterprise credentials and ordinary best-effort service. A valid RADIUS server is already assigned. Which TWO values should change? Select TWO.

| Field | Applied value |
| --- | --- |
| SSID | Employees |
| Status | Enabled |
| Auth Key Management | PSK |
| QoS | Bronze |
| RADIUS server | Configured and reachable |

- **A.** SSID from Employees to the RADIUS server’s IP address
- **B.** Auth Key Management from PSK to 802.1X
- **C.** WLAN Status from Enabled to Disabled
- **D.** QoS from Bronze to Silver

**Answer: B, D**

The displayed security and QoS values contradict separate requirements. Correct each relevant field without disabling the intended WLAN.

**Option explanations**

- **A:** SSID naming does not select the authentication method.
- **B:** Enterprise credential validation uses the configured 802.1X/RADIUS path.
- **C:** That would remove the requested employee service.
- **D:** Silver is the standard best-effort profile.

**Further reading**

- [Cisco Wireless Controller Configuration Guide, Release 8.10 — WLAN Security](https://www.cisco.com/c/en/us/td/docs/wireless/controller/8-10/config-guide/b_cg810/wlan_security.html) — Configuring WPA1+WPA2 (GUI); Configuring Peer-to-Peer Blocking (GUI)
- [Cisco Wireless Controller Configuration Guide, Release 8.10 — Wireless Quality of Service](https://www.cisco.com/c/en/us/td/docs/wireless/controller/8-10/config-guide/b_cg810/wireless_quality_of_service.html) — QoS Profiles; Configuring QoS Profiles (GUI); Assigning a QoS Profile to a WLAN (GUI)

---

## CCNA9-041 · IP Connectivity

Objectives: 3.1.a, 3.1.e, 3.1.f · single · Applied

An inventory tool reads O 10.140.0.0/16 [110/52] via 192.0.2.10. It stores 110 as ospf_cost and 52 as administrative_distance. What defect should be fixed in the parser?

- **A.** The bracket fields have been assigned to the wrong attributes.
- **B.** The /16 value should be stored as the administrative distance.
- **C.** The next-hop address should replace the metric field.
- **D.** The O code means the destination is outside the autonomous system.

**Answer: A**

The corrected record has distance 110 and OSPF cost 52. A parser that swaps these values can produce misleading route-preference reports.

**Option explanations**

- **A:** The first value is administrative distance and the second is the source protocol metric.
- **B:** Prefix length describes destination matching, not source preference.
- **C:** An address cannot be substituted for the numeric path metric.
- **D:** A plain O identifies an OSPF intra-area route, not the outside address of a session.

**Further reading**

- [Configure Route Selection for Routers](https://www.cisco.com/c/en/us/support/docs/ip/enhanced-interior-gateway-routing-protocol-eigrp/8651-21.html) — Build the Routing Table; Make Forwarding Decisions

---

## CCNA9-042 · IP Connectivity

Objectives: 3.1.b, 3.1.c, 3.2.a · single · Applied

An access-policy report says every host in 172.27.6.0/24 uses the same egress. The installed routes below are the complete relevant table. Which observation disproves the report?

```text
S 172.27.6.0/24 via 192.0.2.1
S 172.27.6.0/25 via 192.0.2.5
```

- **A.** 172.27.6.70 and 172.27.6.200 use different next hops.
- **B.** Both hosts always use the route with the shorter mask.
- **C.** 172.27.6.70 is the broadcast address of the /24.
- **D.** The /25 cannot coexist with a /24 route.

**Answer: A**

Address allocation into one /24 does not guarantee identical routing for its entire range. A more specific installed route creates a forwarding exception.

**Option explanations**

- **A:** .70 matches the /25 whereas .200 matches only the /24.
- **B:** Ordinary forwarding selects the longest matching prefix.
- **C:** The /24 broadcast is .255.
- **D:** Overlapping prefixes of different lengths can both be installed.

**Further reading**

- [Configure Route Selection for Routers](https://www.cisco.com/c/en/us/support/docs/ip/enhanced-interior-gateway-routing-protocol-eigrp/8651-21.html) — Build the Routing Table; Make Forwarding Decisions

---

## CCNA9-043 · IP Connectivity

Objectives: 3.2.a, 3.2.b · multiple · Applied

Two valid packets have different source addresses but the same destination, 10.88.5.25. A router has one usable longest-match route and no policy routing, NAT, filtering, or ECMP. Which TWO statements describe its route lookup? Select two.

- **A.** The source address alone does not select another destination route.
- **B.** Both packets select that destination route.
- **C.** A lower-distance route to a less specific prefix displaces the longest match.
- **D.** The packet from the numerically larger source uses the default.

**Answer: A, B**

The assumptions remove source-based policy and multipath decisions. The destination match therefore selects the same route for both packets.

**Option explanations**

- **A:** Source-based route selection would need a mechanism excluded by the prompt.
- **B:** Changing only the source does not change this ordinary destination lookup.
- **C:** Distance selects competing route sources for an exact prefix, not across every matching prefix.
- **D:** No such source-order rule exists.

**Further reading**

- [Configure Route Selection for Routers](https://www.cisco.com/c/en/us/support/docs/ip/enhanced-interior-gateway-routing-protocol-eigrp/8651-21.html) — Build the Routing Table; Make Forwarding Decisions

---

## CCNA9-044 · IP Connectivity

Objectives: 3.3.b, 3.2.a · single · Challenge

During a migration, only LANs 10.164.8.0/24 and 10.164.9.0/24 move behind 192.0.2.18. A technician instead installs the shown route, while a broader route points elsewhere. Which additional LAN is unintentionally redirected?

```text
ip route 10.164.8.0 255.255.252.0 192.0.2.18
```

- **A.** 10.164.10.0/24
- **B.** 10.164.12.0/24
- **C.** 10.164.16.0/24
- **D.** 10.164.7.0/24

**Answer: A**

The /22 is broader than the two moved /24 LANs. A /23 beginning at 10.164.8.0 would cover exactly those two contiguous LANs.

**Option explanations**

- **A:** The /22 covers third octets 8 through 11, including this LAN.
- **B:** Third octet 12 begins the next /22 block.
- **C:** Third octet 16 is outside the configured /22.
- **D:** Third octet 7 lies before the /22 block.

**Further reading**

- [Configure Route Selection for Routers](https://www.cisco.com/c/en/us/support/docs/ip/enhanced-interior-gateway-routing-protocol-eigrp/8651-21.html) — Build the Routing Table; Make Forwarding Decisions

---

## CCNA9-045 · IP Connectivity

Objectives: 3.3.d · single · Applied

A backup default uses a different next-hop IP but shares the primary default’s only physical Ethernet interface. Both next hops become unreachable when that interface loses carrier; no other resolving route exists. What is the design failure?

- **A.** Any different next-hop IP automatically provides an independent path.
- **B.** The backup does not provide a surviving path for this interface failure.
- **C.** Raising the backup distance repairs the failed Ethernet interface.
- **D.** A floating route can forward without resolving its next hop.

**Answer: B**

Two configured candidates are insufficient when both depend on the failed component. Verify the backup’s actual path as well as its administrative distance.

**Option explanations**

- **A:** Different addresses do not imply independent physical dependencies.
- **B:** Both next-hop resolutions depend on the failed interface.
- **C:** Administrative distance cannot create physical reachability.
- **D:** The backup must still have a valid forwarding path.

**Further reading**

- [Configure Route Selection for Routers](https://www.cisco.com/c/en/us/support/docs/ip/enhanced-interior-gateway-routing-protocol-eigrp/8651-21.html) — Build the Routing Table; Make Forwarding Decisions

---

## CCNA9-046 · IP Connectivity

Objectives: 3.3.c, 3.3.b · single · Applied

A rollback removes a temporary /32 route to server 10.91.2.19. The valid covering 10.91.2.0/24 route remains installed. Under ordinary forwarding, what happens to new packets for the server?

- **A.** They use the deleted /32 until the server renews DHCP.
- **B.** They use the remaining /24 route.
- **C.** They are locally delivered because the /32 was removed.
- **D.** They must be dropped until another /32 is configured.

**Answer: B**

The rollback changes which installed prefix is the longest match. It does not require a corresponding host configuration change.

**Option explanations**

- **A:** DHCP lease renewal does not control the router’s installed route selection.
- **B:** Removing the specific exception exposes the covering route.
- **C:** Deleting a remote host route does not assign its address to the router.
- **D:** A host route is not required when a usable covering route exists.

**Further reading**

- [Configure Route Selection for Routers](https://www.cisco.com/c/en/us/support/docs/ip/enhanced-interior-gateway-routing-protocol-eigrp/8651-21.html) — Build the Routing Table; Make Forwarding Decisions

---

## CCNA9-047 · IP Connectivity

Objectives: 3.3.a, 3.1.g · single · Applied

An engineer removes the only static IPv4 default but leaves all connected and OSPF network routes unchanged. Which acceptance test most directly checks the default-dependent behavior?

- **A.** Send a valid transit packet to a destination outside every remaining prefix.
- **B.** Ping a neighbor on a directly connected subnet only.
- **C.** Ping the router’s own loopback only.
- **D.** Read the interface description on the WAN port only.

**Answer: A**

A useful test must require the route that changed. Reachability to local or specifically routed addresses does not validate the removed fallback.

**Option explanations**

- **A:** Such a packet specifically exercises the missing fallback path.
- **B:** That test uses the connected route rather than the removed default.
- **C:** Local delivery does not test a transit default.
- **D:** An interface description does not establish forwarding behavior.

**Further reading**

- [RFC 1812: Requirements for IP Version 4 Routers](https://www.rfc-editor.org/rfc/rfc1812.html) — 5.2.4 Determining the Next Hop Address

---

## CCNA9-048 · IP Connectivity

Objectives: 3.3.b · single · Applied

The same IPv6 link-local next-hop value, fe80::a, exists on two different links. A remote server subnet is behind the neighbor on GigabitEthernet0/2. Which information must the static route use to disambiguate the next hop?

- **A.** Only fe80::a, because link-local addresses are globally unique.
- **B.** A larger destination prefix length with no interface.
- **C.** GigabitEthernet0/2 together with fe80::a.
- **D.** The router’s highest global IPv6 address instead of an interface.

**Answer: C**

The neighbor identity is a scoped address, not the address text alone. This is why a fully specified static route includes the link.

**Option explanations**

- **A:** The value can legitimately be reused on separate links.
- **B:** Changing destination specificity does not establish link-local scope.
- **C:** The outgoing interface identifies the scope of the link-local neighbor.
- **D:** A local global address does not select the intended remote link-local neighbor.

**Further reading**

- [IPv6 Routing: Static Routing — Cisco IOS XE 17.x](https://www.cisco.com/c/en/us/td/docs/routers/ios/config/17-x/ip-routing/b-ip-routing/m_ip6-route-static-xe.html) — Recursive Static Routes; Fully Specified Static Routes; Floating Static Routes

---

## CCNA9-049 · IP Connectivity

Objectives: 3.3.d, 3.2.b · multiple · Applied

A backup IPv6 static for 2001:db8:640::/48 has distance 190. The primary valid route to the same /48 has distance 110 and remains installed. Which TWO observations are consistent with the intended backup design? Select two.

- **A.** The two distances are added to obtain a forwarding cost of 300.
- **B.** The configured backup may be absent from the active IPv6 routing table.
- **C.** Every other packet must use the backup for load balancing.
- **D.** The backup command can still be visible in the running configuration.

**Answer: B, D**

Compare intended configuration with the selected routing state. Absence of a floating route from the active RIB is expected while its primary competitor wins.

**Option explanations**

- **A:** Administrative distances are not added across competing route candidates.
- **B:** It loses selection while the preferred exact-prefix route remains valid.
- **C:** Unequal distances do not create the stated equal-preference load sharing.
- **D:** Configuration records intent even when the route is not the selected RIB entry.

**Further reading**

- [IPv6 Routing: Static Routing — Cisco IOS XE 17.x](https://www.cisco.com/c/en/us/td/docs/routers/ios/config/17-x/ip-routing/b-ip-routing/m_ip6-route-static-xe.html) — Recursive Static Routes; Fully Specified Static Routes; Floating Static Routes

---

## CCNA9-050 · IP Connectivity

Objectives: 3.1.d, 3.1.e, 3.1.f, 3.2.a · matching · Applied

Match each troubleshooting question to the routing information that directly answers it. Use each information category once.

1. Which installed entry applies most specifically to this destination?
2. Why did a static candidate beat an OSPF candidate for the identical prefix?
3. Which OSPF intra-area path has the smaller total cost?
4. Which neighboring router should receive the forwarded packet?

- **A.** Administrative distance
- **B.** Next hop
- **C.** Protocol metric
- **D.** Longest matching destination prefix

**Answer: 1 → D; 2 → A; 3 → C; 4 → B**

Keep destination matching, source preference, protocol path cost and next-hop selection separate. Confusing these categories sends troubleshooting toward the wrong field.

**Option explanations**

- **A:** This compares the preference of route sources for one exact prefix.
- **B:** This identifies the next router used for the selected forwarding path.
- **C:** This compares eligible paths inside the source protocol’s own selection rules.
- **D:** This identifies the most specific applicable installed route.

**Further reading**

- [Configure Route Selection for Routers](https://www.cisco.com/c/en/us/support/docs/ip/enhanced-interior-gateway-routing-protocol-eigrp/8651-21.html) — Build the Routing Table; Make Forwarding Decisions

---

## CCNA9-051 · IP Connectivity

Objectives: 3.4.a · single · Applied

A router’s OSPF neighbor reached Full at 09:00. At 09:30 the neighbor disappears and its routes are withdrawn. Which evidence is required before claiming that the 09:00 test proves current adjacency?

- **A.** The fact that both devices were purchased together.
- **B.** A fresh operational check of neighbor state and the changed link conditions.
- **C.** The existence of yesterday’s topology diagram alone.
- **D.** The unchanged router ospf command alone.

**Answer: B**

Use time-aligned evidence. The observed withdrawal already shows that an earlier acceptance result cannot be treated as proof of current operation.

**Option explanations**

- **A:** Acquisition history does not determine present protocol state.
- **B:** A past successful state does not establish the current state after a failure.
- **C:** A drawing describes intent and may predate the fault.
- **D:** The command proves configuration, not a live adjacency.

**Further reading**

- [Understand OSPF Neighbor States](https://www.cisco.com/c/en/us/support/docs/ip/open-shortest-path-first-ospf/13685-13.html) — OSPF Neighbor States

---

## CCNA9-052 · IP Connectivity

Objectives: 3.4.a · single · Applied

On an OSPF broadcast LAN, R7 and R8 are configured in area 0 and have compatible timers and authentication. R7 has address 10.46.0.1/24 and R8 has 10.46.0.2/25. Neither is passive. Which mismatch should be corrected?

- **A.** They use the same area number.
- **B.** Their host address portions differ.
- **C.** They have different OSPF process IDs.
- **D.** The network masks differ for this broadcast subnet.

**Answer: D**

The interfaces agree about some address bits but not the subnet boundary. Align the intended subnet masks before investigating a more complex adjacency fault.

**Option explanations**

- **A:** Area agreement is required, not a conflict.
- **B:** Distinct host addresses are expected on the same subnet.
- **C:** Process IDs are locally significant and do not need to match.
- **D:** Broadcast OSPF Hello processing checks the network mask.

**Further reading**

- [RFC 2328: OSPF Version 2](https://www.rfc-editor.org/rfc/rfc2328.html) — 9.4 Electing the Designated Router; 10 The Neighbor Data Structure; 16 Calculation of the routing table

---

## CCNA9-053 · IP Connectivity

Objectives: 3.4.a · single · Applied

The only intended routing peers are on Gi0/0 and Gi0/1. Gi0/2 is a user LAN. All three interfaces are enabled in OSPF area 0. Which addition to the shown process configuration enables Hellos on the missing peer link while keeping the user LAN passive?

```text
router ospf 31
 passive-interface default
 no passive-interface GigabitEthernet0/0
```

- **A.** no passive-interface default
- **B.** no passive-interface GigabitEthernet0/2
- **C.** no passive-interface GigabitEthernet0/1
- **D.** passive-interface GigabitEthernet0/0

**Answer: C**

With a passive default, list the intended peer-facing interfaces as exceptions. A narrow exception repairs the missing adjacency without widening participation.

**Option explanations**

- **A:** It would also activate Hellos on the user LAN, violating the stated requirement.
- **B:** It would enable the wrong interface.
- **C:** It overrides the passive default only on the second peer link.
- **D:** It would disable the already permitted peer link.

**Further reading**

- [Configuring OSPF — IP Routing: OSPF Configuration Guide](https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/iproute_ospf/configuration/xe-16/iro-xe-16-book/iro-cfg.html) — Enabling OSPF; Configuring OSPF Interface Parameters

---

## CCNA9-054 · IP Connectivity

Objectives: 3.4.b, 3.4.c · single · Applied

Two routers use OSPF point-to-point network type on a dedicated Ethernet link. A reviewer recommends setting priority 255 on one side to ensure a DR is elected. Which response is correct?

- **A.** Priority 255 changes the network type to broadcast.
- **B.** A DR is required whenever the physical medium is Ethernet.
- **C.** Both routers become DR because there are only two neighbors.
- **D.** No DR is elected for this point-to-point OSPF network type.

**Answer: D**

Do not infer the OSPF election model solely from the cable or interface technology. The explicit network type controls this behavior.

**Option explanations**

- **A:** Interface priority does not perform that configuration change.
- **B:** The configured OSPF network type is decisive in this scenario.
- **C:** Point-to-point operation does not assign DR roles.
- **D:** The network type, not a high priority, determines whether a DR election applies.

**Further reading**

- [RFC 2328: OSPF Version 2](https://www.rfc-editor.org/rfc/rfc2328.html) — 9.4 Electing the Designated Router; 10 The Neighbor Data Structure; 16 Calculation of the routing table

---

## CCNA9-055 · IP Connectivity

Objectives: 3.4.c · single · Applied

Before a new broadcast OSPF segment is started, every participating router is configured with interface priority 0. No DR or BDR already exists. Which change is needed to permit an election?

- **A.** Make at least one participating router eligible with a nonzero interface priority.
- **B.** Reduce only the hello interval while keeping all priorities zero.
- **C.** Set every dead interval to the same value but keep all priorities zero.
- **D.** Assign the same router ID to all participants.

**Answer: A**

An election needs an eligible candidate. Matching other adjacency parameters cannot substitute for eligibility.

**Option explanations**

- **A:** Priority zero excludes every current participant from DR/BDR election.
- **B:** Faster Hellos do not make an ineligible router eligible.
- **C:** Timer agreement is necessary for peers but does not change election eligibility.
- **D:** Router IDs must identify distinct OSPF routers and do not overcome zero eligibility.

**Further reading**

- [RFC 2328: OSPF Version 2](https://www.rfc-editor.org/rfc/rfc2328.html) — 9.4 Electing the Designated Router; 10 The Neighbor Data Structure; 16 Calculation of the routing table

---

## CCNA9-056 · IP Connectivity

Objectives: 3.4.d · single · Applied

A router is explicitly configured with OSPF router ID 7.7.7.7, which is unique in the domain but is not assigned to an interface. All actual OSPF links have working addresses. What must be true for this router ID to identify the OSPF speaker?

- **A.** It must be a valid unique 32-bit identifier; it need not be an assigned interface address.
- **B.** A host route to 7.7.7.7 must be installed on every neighbor first.
- **C.** Every other router must use 7.7.7.7 as its default gateway.
- **D.** The router must own 7.7.7.7 on each participating interface.

**Answer: A**

The router ID uses IPv4-style notation, but an explicit value is not automatically a data-plane destination. Keep identity selection separate from link addressing.

**Option explanations**

- **A:** An explicitly configured router ID is an OSPF identity value.
- **B:** Router ID identity does not itself impose that reachability requirement.
- **C:** Host/default forwarding configuration is unrelated to choosing the router ID.
- **D:** Interface addresses remain distinct from the protocol identifier.

**Further reading**

- [Configuring OSPF — IP Routing: OSPF Configuration Guide](https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/iproute_ospf/configuration/xe-16/iro-xe-16-book/iro-cfg.html) — Enabling OSPF; Configuring OSPF Interface Parameters
- [RFC 2328: OSPF Version 2](https://www.rfc-editor.org/rfc/rfc2328.html) — 9.4 Electing the Designated Router; 10 The Neighbor Data Structure; 16 Calculation of the routing table

---

## CCNA9-057 · IP Connectivity

Objectives: 3.4, 3.2.c · single · Challenge

R1 reaches a remote area-0 LAN by two possible intra-area paths. Path A has outgoing costs 4, 7 and 2; Path B has costs 3, 3, 3 and 2. These lists include the destination LAN cost. No other path exists. Why can Path B win?

- **A.** Its total cost is 11, compared with 13 for Path A.
- **B.** The first interface has lower cost, so later costs are ignored.
- **C.** It has more routers, which OSPF always prefers.
- **D.** Both paths have the same cost because they end with 2.

**Answer: A**

A shorter physical hop count need not produce a smaller OSPF metric. Add every specified outgoing cost before choosing the path.

**Option explanations**

- **A:** OSPF sums outgoing costs; the longer list still has the smaller total.
- **B:** The complete path cost must be considered.
- **C:** Hop count is not the stated selection metric.
- **D:** The destination interface is only one term in each sum.

**Further reading**

- [RFC 2328: OSPF Version 2](https://www.rfc-editor.org/rfc/rfc2328.html) — 9.4 Electing the Designated Router; 10 The Neighbor Data Structure; 16 Calculation of the routing table

---

## CCNA9-058 · IP Connectivity

Objectives: 3.4, 3.2.c · multiple · Applied

An engineer raises the OSPF cost on R1’s interface toward R2. No corresponding change is made on R2, and no link fails. Which TWO statements are accurate? Select two.

- **A.** The change affects the cost advertised for leaving R1 over that interface.
- **B.** The change forces the physical port speed to decrease.
- **C.** Both directions must always have identical configured OSPF costs.
- **D.** R2’s locally configured reverse-direction interface cost does not automatically change.

**Answer: A, D**

An undirected topology drawing can conceal directional metrics. Verify the advertised costs and resulting routes on both sides when changing path preference.

**Option explanations**

- **A:** The configured cost is associated with the local outgoing direction.
- **B:** An OSPF metric command changes routing cost, not line rate.
- **C:** OSPF can represent asymmetric directional link costs.
- **D:** OSPF does not copy the new local setting into its neighbor’s configuration.

**Further reading**

- [Configuring OSPF — IP Routing: OSPF Configuration Guide](https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/iproute_ospf/configuration/xe-16/iro-xe-16-book/iro-cfg.html) — Enabling OSPF; Configuring OSPF Interface Parameters
- [RFC 2328: OSPF Version 2](https://www.rfc-editor.org/rfc/rfc2328.html) — 9.4 Electing the Designated Router; 10 The Neighbor Data Structure; 16 Calculation of the routing table

---

## CCNA9-059 · IP Connectivity

Objectives: 3.4.a, 3.2.b · single · Applied

A router learns a valid OSPF candidate for 10.175.0.0/24 but already has that same prefix as a directly connected network on an up interface. Default administrative distances apply. Why is the active route still connected?

- **A.** A Full adjacency guarantees OSPF replaces connected routes.
- **B.** The connected source has administrative distance 0.
- **C.** OSPF refuses all prefixes using private addressing.
- **D.** The OSPF router ID must equal the network address.

**Answer: B**

A successfully learned protocol candidate need not become the selected route. Also check whether the connected prefix is intentional or an addressing error.

**Option explanations**

- **A:** Adjacency does not override source preference for an exact prefix.
- **B:** It outranks the OSPF candidate for the same prefix.
- **C:** OSPF routinely carries private prefixes.
- **D:** Router identity does not impose such a route-installation condition.

**Further reading**

- [Configure Route Selection for Routers](https://www.cisco.com/c/en/us/support/docs/ip/enhanced-interior-gateway-routing-protocol-eigrp/8651-21.html) — Build the Routing Table; Make Forwarding Decisions

---

## CCNA9-060 · IP Connectivity

Objectives: 3.1.d, 3.3.b · single · Applied

R1’s static route selects neighbor R2, and R2’s interface MAC resolves successfully. R2 has no route matching the final destination and no default. Which statement describes the limit of R1’s successful next-hop check?

- **A.** R2 must forward the packet back on its ingress link by default.
- **B.** Successful MAC resolution installs a destination route on R2.
- **C.** R1’s static route is automatically copied to R2.
- **D.** It establishes next-hop MAC resolution, not successful delivery along the complete path.

**Answer: D**

Validate each routed segment of the path. Successful next-hop MAC resolution neither proves delivery of a particular data packet nor supplies the missing destination route on R2.

**Option explanations**

- **A:** No such fallback replaces a missing route.
- **B:** Neighbor resolution does not configure remote routing.
- **C:** A manually configured static route is local configuration.
- **D:** MAC resolution enables R1 to address an Ethernet frame to R2. It does not prove data-packet delivery, and R2 still needs a route for onward forwarding.

**Further reading**

- [RFC 1812: Requirements for IP Version 4 Routers](https://www.rfc-editor.org/rfc/rfc1812.html) — 5.2.4 Determining the Next Hop Address

---

## CCNA9-061 · IP Connectivity

Objectives: 3.5 · single · Applied

A gateway failover test verifies that clients can still reach a remote subnet, but the acceptance record does not identify which router forwarded their traffic. Which added observation most directly verifies that the standby assumed the gateway role?

- **A.** Check only the DHCP server’s configured lease duration.
- **B.** Check the new active gateway state and its forwarding counters during the test.
- **C.** Check only that the original active router still has power.
- **D.** Check only the client’s unchanged hostname.

**Answer: B**

Reachability is a useful outcome test, but attributing it to failover requires evidence from the participating gateways. Record role and traffic observations together.

**Option explanations**

- **A:** Lease policy does not identify an FHRP role transition.
- **B:** These observations tie control state to the router actually carrying traffic.
- **C:** Power status neither proves role takeover nor identifies the forwarding router.
- **D:** A hostname does not verify a forwarding-role change.

**Further reading**

- [RFC 9568: Virtual Router Redundancy Protocol (VRRP) Version 3 for IPv4 and IPv6](https://www.rfc-editor.org/rfc/rfc9568.html) — 1 Introduction; 2 Required Features; 6 Protocol State Machine

---

## CCNA9-062 · IP Connectivity

Objectives: 3.5 · single · Applied

R1 and R2 protect the same VLAN with an FHRP virtual gateway. During maintenance, R2 is confirmed active and carries the test traffic. Which action maintains gateway service while R1 is reloaded?

- **A.** Keep R2 and its onward path operational throughout the R1 reload.
- **B.** Reload R2 at the same time because the virtual IP is shared.
- **C.** Move the virtual address onto an unrelated access switch without routing.
- **D.** Remove the client VLAN from both routers until R1 returns.

**Answer: A**

Protection during maintenance depends on a surviving operational participant and path. The virtual address is a shared service identity, not a third independent router.

**Option explanations**

- **A:** It is the remaining gateway path during the planned outage.
- **B:** A shared identity cannot forward if both participating routers are unavailable.
- **C:** Address placement alone does not create a working routed gateway.
- **D:** That removes access to the protected gateway rather than maintaining it.

**Further reading**

- [RFC 9568: Virtual Router Redundancy Protocol (VRRP) Version 3 for IPv4 and IPv6](https://www.rfc-editor.org/rfc/rfc9568.html) — 1 Introduction; 2 Required Features; 6 Protocol State Machine

---

## CCNA9-063 · IP Connectivity

Objectives: 3.3.a, 3.3.b · single · Applied

A router has a default toward an Internet edge and a 10.201.0.0/16 static toward an internal router. It receives a packet for 10.201.8.10. The internal next hop resolves but the remote service is down. What does ordinary routing do?

- **A.** Try the default after a single unsuccessful application request.
- **B.** Choose the default because private destinations always use NAT first.
- **C.** Delete the /16 after the host fails to answer one ping.
- **D.** Select the internal /16; it does not fall back to the default because the application failed.

**Answer: D**

Route availability and application availability are different states. Fallback requires the selected route to change, not merely a failed service transaction.

**Option explanations**

- **A:** Ordinary destination routing does not implement that application-level fallback.
- **B:** Private address space does not override destination matching.
- **C:** No tracking or dynamic withdrawal mechanism is stated.
- **D:** The installed prefix remains the longest match under the stated conditions.

**Further reading**

- [RFC 1812: Requirements for IP Version 4 Routers](https://www.rfc-editor.org/rfc/rfc1812.html) — 5.2.4 Determining the Next Hop Address

---

## CCNA9-064 · IP Connectivity

Objectives: 3.3.b, 3.3.c · single · Applied

An IPv6 change should reach all hosts in 2001:db8:aa::/64, but the engineer configured a route only to 2001:db8:aa::1/128. No covering route exists. What does a successful ping to 2001:db8:aa::1 fail to validate?

- **A.** Whether IPv6 packets contain a destination address.
- **B.** Whether 2001:db8:aa::1 belongs to that /64.
- **C.** Whether /128 is the most specific IPv6 prefix length.
- **D.** Reachability of the rest of the intended /64.

**Answer: D**

The selected test address happens to match the narrow route. Test another intended destination and configure the required network prefix.

**Option explanations**

- **A:** The ping result does not call the IPv6 packet format into question.
- **B:** The shown host address does belong to the intended prefix.
- **C:** It is the host prefix length, regardless of ping success.
- **D:** A /128 tests one address and supplies no route to other addresses.

**Further reading**

- [IPv6 Routing: Static Routing — Cisco IOS XE 17.x](https://www.cisco.com/c/en/us/td/docs/routers/ios/config/17-x/ip-routing/b-ip-routing/m_ip6-route-static-xe.html) — Recursive Static Routes; Fully Specified Static Routes; Floating Static Routes

---

## CCNA9-065 · IP Connectivity

Objectives: 3.4.a, 3.4.c · single · Applied

A broadcast area-0 LAN has five routers after convergence: one DR, one BDR and three DROTHERs. Focusing on one DROTHER, how many other routers should it normally be fully adjacent with on this LAN?

- **A.** One: only the DR.
- **B.** Two: the DR and BDR.
- **C.** Zero: DROTHERs cannot participate in routing.
- **D.** Four: every other router on the LAN.

**Answer: B**

The DR/BDR structure limits adjacency formation on a broadcast network. It does not exclude DROTHER routers from routing.

**Option explanations**

- **A:** The BDR also maintains full adjacencies.
- **B:** A DROTHER forms full adjacencies with these two elected routers.
- **C:** They still maintain adjacencies and can forward routed traffic.
- **D:** DROTHER-to-DROTHER relationships normally stop at 2-Way.

**Further reading**

- [RFC 2328: OSPF Version 2](https://www.rfc-editor.org/rfc/rfc2328.html) — 9.4 Electing the Designated Router; 10 The Neighbor Data Structure; 16 Calculation of the routing table

---

## CCNA9-066 · IP Services

Objectives: 4.1 · single · Challenge

ACL 27 is referenced only by the shown NAT rule and is not applied as an interface filter. An inside packet from 10.27.0.50 matches its deny entry. Routes and separate packet filters permit the flow. What does this ACL match mean for this NAT rule?

```text
access-list 27 deny host 10.27.0.50
access-list 27 permit 10.27.0.0 0.0.0.255
ip nat inside source list 27 pool PUBLIC
```

- **A.** The packet is not selected for translation by this rule.
- **B.** The packet must be encrypted before it is routed.
- **C.** The ACL necessarily drops the packet as an interface security filter.
- **D.** The packet receives the first address in PUBLIC because deny means translate first.

**Answer: A**

Interpret an ACL in the context of the feature using it. Here it selects address translation eligibility; packet filtering is explicitly handled separately.

**Option explanations**

- **A:** A deny in this NAT-selection ACL excludes the source from this mapping.
- **B:** A NAT-selection ACL does not request encryption.
- **C:** The ACL is not attached as an interface filter in the stated configuration.
- **D:** Deny excludes the match rather than allocating a pool entry.

**Further reading**

- [Configure Network Address Translation](https://www.cisco.com/c/en/us/support/docs/ip/network-address-translation-nat/13772-12.html) — NAT definitions; configuring inside source translation
- [IP Addressing Configuration Guide, Cisco IOS XE 17.x — Configuring NAT for IP Address Conservation](https://www.cisco.com/c/en/us/td/docs/routers/ios/config/17-x/ip-addressing/b-ip-addressing/m_iadnat-addr-consv-xe.html) — Inside source address translation; static and dynamic translations; monitoring NAT

---

## CCNA9-067 · IP Services

Objectives: 4.2 · single · Applied

Server A advertises NTP stratum 2 and server B advertises stratum 3. No delay, offset, jitter, or source-quality measurements are supplied. Which conclusion can be drawn from the stratum numbers alone?

- **A.** B necessarily uses UDP port 124 instead of 123.
- **B.** A's observed network round-trip delay must be lower than B's.
- **C.** A's actual clock error is guaranteed to be smaller than B's.
- **D.** A reports fewer synchronization levels from a reference source than B.

**Answer: D**

Stratum is useful hierarchy information, but it is not a direct measurement of path latency or clock accuracy. A source assessment needs operating measurements in addition to that number.

**Option explanations**

- **A:** Stratum does not choose an alternate NTP transport port.
- **B:** Network path delay is not encoded by stratum alone.
- **C:** Stratum alone is not a measurement of actual error.
- **D:** Stratum describes position in the time hierarchy.

**Further reading**

- [RFC 5905 — Network Time Protocol Version 4: Protocol and Algorithms Specification](https://www.rfc-editor.org/rfc/rfc5905.html) — 7 NTP protocol data structures; 9 Peer process; 11 System process
- [Use Best Practices for Network Time Protocol](https://www.cisco.com/c/en/us/support/docs/availability/high-availability/19643-ntpm.html) — NTP architecture; synchronization; verification

---

## CCNA9-068 · IP Services

Objectives: 4.3 · single · Applied

A DHCP client has failed both renewal and rebinding, and its lease has now expired. No replacement allocation exists. What is the protocol-required behavior for the expired address?

- **A.** Change only the DNS suffix and continue using the expired address.
- **B.** Keep using the address indefinitely because the Ethernet link is still up.
- **C.** Make the default gateway issue an ARP reply that renews the lease.
- **D.** Stop using that address and return to address acquisition.

**Answer: D**

The right to use a dynamically leased address ends when its lease expires. Continuing to use it could conflict with an address the server subsequently reallocates.

**Option explanations**

- **A:** A name-search setting does not repair lease expiration.
- **B:** Link state does not extend the DHCP lease.
- **C:** ARP does not renew DHCP allocation authority.
- **D:** The lease no longer authorizes continued use of the allocation.

**Further reading**

- [RFC 2131 — Dynamic Host Configuration Protocol](https://www.rfc-editor.org/rfc/rfc2131.html) — 3.1 Address allocation; 4.3 Server behavior; 4.4 Client behavior

---

## CCNA9-069 · IP Services

Objectives: 4.4 · single · Applied

An SNMP utilization collector samples an octet counter before and after a router reboot. The second value is lower, and the reboot is confirmed. What should the collector do with that interval?

- **A.** Report a negative traffic rate as real reverse-direction traffic.
- **B.** Assume exactly one counter wrap despite the confirmed reboot.
- **C.** Use the current counter value as the exact traffic total for the entire interval.
- **D.** Treat it as a counter discontinuity and establish a new baseline.

**Answer: D**

Counter-based rates require continuity assumptions. Detecting a reset prevents misleading rates and calls for a new baseline rather than fabricating the missing traffic amount.

**Option explanations**

- **A:** Counter reset is not negative traffic.
- **B:** The known reset invalidates that unsupported wrap assumption.
- **C:** That omits traffic accumulated before the reboot and falsely represents the full interval.
- **D:** A subtraction across the reset does not represent continuous traffic accumulation.

**Further reading**

- [RFC 2863 — The Interfaces Group MIB](https://www.rfc-editor.org/rfc/rfc2863.html) — 3.1.6 Counter size; ifHCInOctets; ifCounterDiscontinuityTime

---

## CCNA9-070 · IP Services

Objectives: 4.5 · single · Applied

An engineer connects over SSH and wants new log messages displayed in that terminal. Logging monitor is enabled at a sufficient severity, but the current terminal session has not enabled message display. Which EXEC command enables it for this session?

- **A.** logging host 127.0.0.1
- **B.** terminal no monitor
- **C.** terminal monitor
- **D.** show startup-config

**Answer: C**

The device's logging destination policy and the current terminal's display setting are separate. terminal monitor affects the active terminal session and must be enabled in later sessions when needed.

**Option explanations**

- **A:** A syslog destination is not the current terminal-session display setting.
- **B:** This disables the current session's monitoring display.
- **C:** This enables log/debug display to the current non-console terminal session.
- **D:** Displaying saved configuration does not subscribe the current terminal to new messages.

**Further reading**

- [System Message Logging](https://www.cisco.com/c/en/us/td/docs/routers/access/wireless/software/guide/SysMsgLogging.html) — System log message format; logging destinations; severity levels; timestamps

---

## CCNA9-071 · IP Services

Objectives: 4.6 · matching · Applied

For a branch provisioning design, match each role or verification item to its purpose. Use each option once.

1. The ISP should assign the branch router's WAN address.
2. Local workstations must reach a central address service without sharing its broadcast domain.
3. The central service must select addresses belonging to the workstations' subnet.
4. The engineer must confirm that the WAN request succeeded instead of only reviewing the command.

- **A.** DHCP relay on the client VLAN gateway
- **B.** DHCP client on the WAN interface
- **C.** Client interface address/lease verification
- **D.** DHCP server scope

**Answer: 1 → B; 2 → A; 3 → D; 4 → C**

Client, relay, and server functions are distinct even when some reside on the same router. Operational verification checks the resulting allocation, beyond intended configuration.

**Option explanations**

- **A:** It carries the VLAN clients' DHCP messages to a server on another subnet.
- **B:** It requests addressing parameters for that router interface.
- **C:** It checks that the intended address-allocation exchange actually produced usable client state.
- **D:** It defines the client subnet's allocatable addressing and configuration.

**Further reading**

- [IP Addressing: DHCP Configuration Guide, Cisco IOS XE 17 — Configuring the Cisco IOS XE DHCP Client](https://www.cisco.com/c/en/us/td/docs/routers/asr920/configuration/guide/ipaddr-dhcp/17-1-1/b-dhcp-xe-17-1-asr920/m_config-dhcp-client-xe.html) — Configuring the DHCP client; monitoring and maintaining DHCP client operation
- [IP Addressing: DHCP Configuration Guide, Cisco IOS XE Everest 16.6 — Configuring the Cisco IOS XE DHCP Relay Agent](https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/ipaddr_dhcp/configuration/xe-16-6/dhcp-xe-16-6-book/dhcp-relay-agent-xe.html) — Packet forwarding address; giaddr; specifying the packet forwarding address
- [RFC 2131 — Dynamic Host Configuration Protocol](https://www.rfc-editor.org/rfc/rfc2131.html) — 3.1 Address allocation; 4.3 Server behavior; 4.4 Client behavior

---

## CCNA9-072 · IP Services

Objectives: 4.6 · single · Applied

An IOS XE router's interface requests a one-hour DHCP lease using ip dhcp client lease, but the DHCP server returns a valid two-hour lease. The client accepts it. Which statement is correct?

- **A.** The longer lease disables routing on the interface until one hour passes.
- **B.** The ip dhcp client lease command creates a local DHCP pool for downstream hosts.
- **C.** The server must be defective because every lease suggestion is mandatory.
- **D.** The client requested a duration; the server's accepted lease allocation determines the actual lifetime.

**Answer: D**

Distinguish a client preference from the server's granted configuration. The accepted response carries the actual lease, which should be verified rather than inferred only from the requested value.

**Option explanations**

- **A:** No such routing consequence follows from the accepted lifetime.
- **B:** It customizes the requesting client's lease preference, not a server pool.
- **C:** The requested value does not force the server's allocation policy.
- **D:** A suggested lease time is not a unilateral client command to the server.

**Further reading**

- [IP Addressing: DHCP Configuration Guide, Cisco IOS XE 17 — Configuring the Cisco IOS XE DHCP Client](https://www.cisco.com/c/en/us/td/docs/routers/asr920/configuration/guide/ipaddr-dhcp/17-1-1/b-dhcp-xe-17-1-asr920/m_config-dhcp-client-xe.html) — Configuring the DHCP client; monitoring and maintaining DHCP client operation
- [RFC 2131 — Dynamic Host Configuration Protocol](https://www.rfc-editor.org/rfc/rfc2131.html) — 3.1 Address allocation; 4.3 Server behavior; 4.4 Client behavior

---

## CCNA9-073 · IP Services

Objectives: 4.7 · multiple · Applied

A branch compares two policies for a traffic class that exceeds its agreed profile. Policy P immediately drops excess packets; policy S holds eligible excess packets until they may be sent, provided buffer space remains. Which two statements are correct? Select two.

- **A.** P is policing with a drop action.
- **B.** S guarantees that no packet is ever dropped under sustained overload.
- **C.** Both policies merely change DSCP and have identical packet timing.
- **D.** P increases the downstream link capacity.
- **E.** S is shaping and can add queueing delay.

**Answer: A, E**

Policing and shaping can enforce rate profiles through different actions. The practical choice includes loss, burst absorption, and delay, while both remain constrained by finite capacity.

**Option explanations**

- **A:** Its response is immediate enforcement rather than delayed release.
- **B:** Its buffer is finite, so persistent excess traffic can still overflow it.
- **C:** The stated drop and delay behaviors differ materially.
- **D:** Discarding traffic cannot increase the medium's service rate.
- **E:** The buffer absorbs the burst and releases traffic according to a schedule.

**Further reading**

- [Compare Traffic Policing and Traffic Shaping to Limit Bandwidth](https://www.cisco.com/c/en/us/support/docs/quality-of-service-qos/qos-policing/19645-policevsshape.html) — Traffic policing and traffic shaping comparison

---

## CCNA9-074 · IP Services

Objectives: 4.8 · single · Applied

A change ticket requires encrypted remote CLI access to a router from subnet 10.94.0.0/24 only. SSH is already configured and working from all routed subnets. Which additional control directly restricts incoming VTY sessions by source subnet?

- **A.** Change transport input ssh to transport output ssh.
- **B.** Apply an appropriate source-permitting ACL with access-class in on all relevant VTY lines.
- **C.** Set an enable secret without an access restriction.
- **D.** Increase the SSH authentication timeout.

**Answer: B**

SSH protects the management session; a VTY access restriction limits where sessions may originate. Verify the complete usable VTY range so the policy does not leave another line group unrestricted.

**Option explanations**

- **A:** That controls outbound line connections rather than inbound source eligibility.
- **B:** This restricts who may reach the VTY service while retaining SSH transport.
- **C:** A privilege password does not restrict source subnets.
- **D:** Waiting longer for authentication does not enforce a source-subnet policy.

**Further reading**

- [Configure SSH on Routers](https://www.cisco.com/c/en/us/support/docs/security-vpn/secure-shell-ssh/4145-ssh.html) — SSH server prerequisites; SSHv2; VTY restrictions; show commands

---

## CCNA9-075 · IP Services

Objectives: 4.9 · single · Foundation

An FTP client is backing up a local configuration file to a remote FTP server. Which operation corresponds to the client sending the file contents to the server?

- **A.** USER
- **B.** STOR
- **C.** LIST
- **D.** RETR

**Answer: B**

FTP distinguishes upload, download, directory listing, and login operations. Backing up the client's local file to the server uses the store direction.

**Option explanations**

- **A:** USER supplies login identity and does not itself transfer the file.
- **B:** STOR requests that the server receive and store file data from the client.
- **C:** LIST requests directory information rather than uploading this file.
- **D:** RETR requests transfer from the server to the client.

**Further reading**

- [RFC 959 — File Transfer Protocol (FTP)](https://www.rfc-editor.org/rfc/rfc959.html) — 2.3 FTP model; 3.2 Data connections; 4.1 FTP commands

---

## CCNA9-076 · Security Fundamentals

Objectives: 5.1 · single · Applied

An obsolete management service has been removed from a switch, but administrators still need its SSH service. What is the security benefit of removing only the unnecessary service?

- **A.** It prevents all attacks by authenticated administrators.
- **B.** It reduces exposed functionality that an attacker could target while retaining the required management path.
- **C.** It proves no password can ever be stolen.
- **D.** It guarantees that the remaining SSH implementation has no vulnerabilities.

**Answer: B**

Reducing unnecessary exposed functionality is a mitigation technique. Its claim should match the component and path removed, not extend to every possible threat.

**Option explanations**

- **A:** Authorized access can still be misused through retained functionality.
- **B:** Attack surface can be reduced without disabling every legitimate service.
- **C:** Service removal does not eliminate every credential-compromise mechanism.
- **D:** Removing one component does not prove another is defect-free.

**Further reading**

- [RFC 4949: Internet Security Glossary, Version 2](https://www.rfc-editor.org/rfc/rfc4949.html) — Section 2: threat, vulnerability, exploit, and countermeasure

---

## CCNA9-077 · Security Fundamentals

Objectives: 5.2 · single · Applied

A visitor is approved for a supervised inspection of one equipment room. The proposed visitor badge also grants unescorted access to every wiring closet for a year. Which correction aligns the physical access authorization with the visit?

- **A.** Keep the broad badge and add a sign asking the visitor not to use it elsewhere.
- **B.** Let the visitor use another employee’s badge instead.
- **C.** Record entry only after the year-long access expires.
- **D.** Limit areas, validity period, and escort conditions to the approved activity.

**Answer: D**

Physical access should reflect the approved purpose, location, duration, and supervision. Verify that the issued credential and entry process enforce those limits.

**Option explanations**

- **A:** A sign does not enforce the approved physical access boundary.
- **B:** Sharing a credential weakens attribution and does not establish the correct scope.
- **C:** Delayed review leaves excessive active authorization unchanged.
- **D:** The credential should express the actual scope and duration of authorization.

**Further reading**

- [NIST SP 800-53 Rev. 5: Security and Privacy Controls for Information Systems and Organizations](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-53r5.pdf) — AT-2, AT-3, PE-2, and PE-3: awareness, training, and physical access

---

## CCNA9-078 · Security Fundamentals

Objectives: 5.3 · single · Applied

A local administrator must remove access for user tempops while preserving netops. AAA is disabled and both use login local. Which global configuration command removes only the obsolete local account?

- **A.** no login local
- **B.** no enable secret
- **C.** no username netops
- **D.** no username tempops

**Answer: D**

Revoke the intended identity rather than weakening the line’s authentication policy. Preserve and verify the remaining authorized account and save the updated configuration.

**Option explanations**

- **A:** Changing line authentication does not selectively delete the named user and is not the required global account command.
- **B:** This removes the privileged EXEC credential rather than the obsolete account.
- **C:** This deletes the account that must be retained.
- **D:** This deletes the named local username entry.

**Further reading**

- [Catalyst 3750-X and 3560-X Configuration Guide: Configuring Switch-Based Authentication](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst3750x_3560x/software/release/15-0_2_se/configuration/guide/3750x_cg/swauthen.html) — Protecting Access to Privileged EXEC Commands; Configuring Username and Password Pairs

---

## CCNA9-079 · Security Fundamentals

Objectives: 5.4 · single · Applied

A support process allows anyone who knows an employee’s publicly listed extension to reset that employee’s administrator password. Which weakness does this create?

- **A.** Account recovery is outside the scope of authentication management.
- **B.** A public extension is a possession factor equivalent to a protected token.
- **C.** The recovery path can bypass the strength of the normal credential check.
- **D.** The normal password becomes cryptographically stronger after every reset.

**Answer: C**

A strong routine login can be undermined by a weak reset process. Recovery must establish sufficient assurance about the requester before replacing credentials.

**Option explanations**

- **A:** Recovery determines who can regain control of the authenticator and is part of its lifecycle.
- **B:** Knowing a published number does not prove control of an authenticator.
- **C:** A public identifier does not adequately verify the requester’s identity for credential replacement.
- **D:** A weak recovery process does not improve the password verifier’s strength.

**Further reading**

- [NIST SP 800-63B-4: Digital Identity Guidelines — Authentication and Authenticator Management](https://pages.nist.gov/800-63-4/sp800-63b.html) — Authentication factors; password verifiers; authenticator management

---

## CCNA9-080 · Security Fundamentals

Objectives: 5.5 · single · Applied

A branch can reach its VPN peer’s public address, but the protected corporate prefixes remain unreachable. Which statement best guides the next verification?

- **A.** The router must replace IPsec with plaintext because the public peer responds.
- **B.** Private inner addresses cannot be carried by a site-to-site VPN.
- **C.** A successful ping to the public peer guarantees every protected subnet is reachable.
- **D.** Public peer reachability alone does not prove an IPsec security association and the intended protected traffic path are working.

**Answer: D**

Verify the actual IPsec state and the traffic selected for protection, then the routes and filters serving the inner flow. Reachability to a gateway’s outer address is a narrower result.

**Option explanations**

- **A:** A responding peer is no reason to abandon the required protection.
- **B:** IPsec tunnels commonly carry privately addressed site traffic.
- **C:** Tunnel negotiation, policy selection, routing, and filtering can still prevent delivery.
- **D:** Underlay IP reachability is one prerequisite, not proof of protected data delivery.

**Further reading**

- [RFC 4301: Security Architecture for the Internet Protocol](https://www.rfc-editor.org/rfc/rfc4301.html) — Sections 3, 4.1, 4.4.1: IPsec services, tunnel mode, and security policy

---

## CCNA9-081 · Security Fundamentals

Objectives: 5.6 · single · Applied

A user LAN must reach only application server 192.0.2.101 over TCP port 8443. The current ACL is shown. Which policy flaw does it contain?

```text
ip access-list extended APPLICATION
 permit tcp 10.90.0.0 0.0.0.255 192.0.2.0 0.0.0.255 eq 8443
```

- **A.** The permit allows the entire destination /24, not just the application server.
- **B.** The ACL permits UDP instead of TCP.
- **C.** The destination port is being matched as a source port.
- **D.** The source match accepts every IPv4 address.

**Answer: A**

A syntactically valid rule can still exceed the required authorization scope. Use host 192.0.2.101 for the destination if only that server is intended.

**Option explanations**

- **A:** The destination wildcard accepts every address in 192.0.2.0/24.
- **B:** The entry explicitly selects TCP.
- **C:** The eq operator follows the destination address and therefore tests the destination port.
- **D:** The source is constrained to 10.90.0.0/24.

**Further reading**

- [Configure IP Access Lists](https://www.cisco.com/c/en/us/support/docs/security/ios-firewall/23602-confaccesslists.html) — ACL Concepts; Masks; Process ACLs; Apply ACLs; Extended ACLs

---

## CCNA9-082 · Security Fundamentals

Objectives: 5.7 · single · Challenge

After an unexpected switch reboot, a DHCP client still holds a valid lease but the switch’s snooping binding table is empty. DAI now drops the client’s ARP on an untrusted port. No ARP ACL is configured. What has been lost from the switch’s verification state?

| Field | Value |
| --- | --- |
| Client lease | Still valid |
| Switch snooping binding | Absent after reboot |
| DAI | Enabled for client VLAN |
| Client ingress | Untrusted |
| ARP ACL | None |

- **A.** The learned binding DAI needs to authorize the client’s IP-to-MAC claim.
- **B.** The client’s private key used by ARP encryption.
- **C.** The DHCP server’s lease database necessarily.
- **D.** The switch’s ability to forward any Ethernet frame because DAI is a routing protocol.

**Answer: A**

Client, server, and switch can retain different state across a restart. A missing snooping binding can prevent DAI validation even when the client still believes its lease is valid.

**Option explanations**

- **A:** The client’s retained lease is not itself a binding record in the restarted switch.
- **B:** Ordinary ARP and DHCP snooping do not use that key mechanism.
- **C:** The premise identifies lost switch state; it does not show the server lost its leases.
- **D:** DAI is an inspection feature, not a routing protocol.

**Further reading**

- [Catalyst 3750-X and 3560-X Configuration Guide: Configuring DHCP Features and IP Source Guard](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst3750x_3560x/software/release/15-0_2_se/configuration/guide/3750x_cg/swdhcp82.html) — DHCP Snooping; DHCP Snooping Binding Database; Enabling DHCP Snooping
- [Catalyst 3750-X and 3560-X Configuration Guide: Configuring Dynamic ARP Inspection](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst3750x_3560x/software/release/15-0_2_se/configuration/guide/3750x_cg/swdynarp.html) — Understanding Dynamic ARP Inspection; Rate Limiting; ARP ACLs

---

## CCNA9-083 · Security Fundamentals

Objectives: 5.8 · single · Applied

A design review proposes granting configuration privileges to anyone who generates an accounting record. Which conceptual error is present?

- **A.** Authentication and accounting are two names for the same permission mechanism.
- **B.** Accounting must always run before any network packet exists.
- **C.** Authorization merely stores records after commands run.
- **D.** Creating an activity record is not an authorization decision.

**Answer: D**

A record says something about activity; it does not grant the right to act. Permissions must be evaluated through the intended authorization policy.

**Option explanations**

- **A:** Identity checking and activity recording are different functions.
- **B:** That timing assertion is not the relevant distinction.
- **C:** Authorization determines whether the requested action is permitted.
- **D:** Accounting evidence cannot substitute for checking an identity’s permitted actions.

**Further reading**

- [RFC 8907: The Terminal Access Controller Access-Control System Plus (TACACS+) Protocol](https://www.rfc-editor.org/rfc/rfc8907.html) — Sections 5, 6, and 7: authentication, authorization, and accounting

---

## CCNA9-084 · Security Fundamentals

Objectives: 5.9 · single · Applied

A guest WLAN uses WPA2-Personal with one PSK shared by many visitors. Which requirement cannot be satisfied merely by retaining that same common PSK and changing the radio channel?

- **A.** Encrypt wireless data using the configured WPA2 cipher.
- **B.** Allow compatible clients to associate when given the valid PSK.
- **C.** Advertise the same SSID after a channel change.
- **D.** Revoke one visitor’s credential while keeping every other visitor’s credential unchanged.

**Answer: D**

A shared PSK creates a shared revocation boundary. Individual identity requirements need an appropriate credential design rather than a radio adjustment.

**Option explanations**

- **A:** WPA2-Personal can provide data protection despite sharing its credential.
- **B:** That is the ordinary purpose of personal preshared-key access.
- **C:** The SSID can remain the same independently of radio channel selection.
- **D:** A common credential is shared; the radio channel does not make it individually revocable.

**Further reading**

- [Cisco Wireless Controller Configuration Guide, Release 8.10: WLAN Security](https://www.cisco.com/c/en/us/td/docs/wireless/controller/8-10/config-guide/b_cg810/wlan_security.html) — WPA1+WPA2; Configuring WPA1+WPA2 (GUI); Protected Management Frames

---

## CCNA9-085 · Security Fundamentals

Objectives: 5.10 · single · Applied

A constructed AireOS 8.10 GUI audit shows WPA2 policy enabled, AES enabled, PSK selected, and a valid PSK. The client uses the matching WPA2-Personal profile and successfully completes the security handshake, but receives no DHCP lease. Which next focus follows the evidence?

- **A.** Replace PSK with 802.1X to make DHCP packets valid.
- **B.** Disable AES because encrypted WLANs cannot use DHCP.
- **C.** Assume the valid PSK is wrong solely because DHCP failed.
- **D.** Investigate the WLAN’s client VLAN and DHCP delivery path.

**Answer: D**

Separate WLAN security negotiation from later IP configuration. Verify the stage that failed instead of changing a security setting already supported by the observed result.

**Option explanations**

- **A:** DHCP does not require that authentication-mode change.
- **B:** DHCP commonly operates after successful encrypted WLAN association.
- **C:** The successful security handshake is contrary evidence for that diagnosis.
- **D:** Successful security negotiation shifts the immediate fault search to post-authentication connectivity.

**Further reading**

- [Cisco Wireless Controller Configuration Guide, Release 8.10: WLAN Security](https://www.cisco.com/c/en/us/td/docs/wireless/controller/8-10/config-guide/b_cg810/wlan_security.html) — WPA1+WPA2; Configuring WPA1+WPA2 (GUI); Protected Management Frames
- [Cisco Wireless Controller Configuration Guide, Release 8.10: Ports and Interfaces](https://www.cisco.com/c/en/us/td/docs/wireless/controller/8-10/config-guide/b_cg810/ports_and_interfaces.html) — Dynamic Interfaces; Interface Groups; WLAN interface mapping and DHCP

---

## CCNA9-086 · Security Fundamentals

Objectives: 5.6 · single · Applied

The ACL shown should allow monitoring from 10.99.0.0/24 to a management server, except that host 10.99.0.50 must be blocked. Which single edit preserves the subnet permit while enforcing the exception?

```text
ip access-list extended MONITOR-IN
 10 permit ip 10.99.0.0 0.0.0.255 host 192.0.2.99
 20 deny ip host 10.99.0.50 host 192.0.2.99
 30 permit ip any any
```

- **A.** Widen the subnet wildcard to 0.0.255.255.
- **B.** Move the host deny before the subnet permit.
- **C.** Move permit ip any any to the first line.
- **D.** Change the host deny into a host permit.

**Answer: B**

The first rule currently includes the prohibited host. Correct ordering expresses the narrower rejection before the permitted broader group.

**Option explanations**

- **A:** A broader earlier permit increases exposure and retains the shadowing flaw.
- **B:** The exception must be tested before its encompassing permit.
- **C:** That would permit the prohibited host before either specific entry.
- **D:** That explicitly allows the source that must be denied.

**Further reading**

- [Configure IP Access Lists](https://www.cisco.com/c/en/us/support/docs/security/ios-firewall/23602-confaccesslists.html) — ACL Concepts; Masks; Process ACLs; Apply ACLs; Extended ACLs

---

## CCNA9-087 · Security Fundamentals

Objectives: 5.6 · multiple · Applied

An ACL change should block client-initiated TCP connections to a server’s destination port 23 and retain client-initiated TCP connections to that server’s destination port 22. Both services are available before the change. Which two post-change observations provide the most direct acceptance evidence for these requirements? Select two.

- **A.** The controlled port-22 connection succeeds through the same intended path.
- **B.** The ACL exists in running configuration without any test traffic.
- **C.** The router’s hostname has not changed.
- **D.** The controlled port-23 attempt fails and increments the intended deny entry’s counter.

**Answer: A, D**

Test both the prohibited flow and a required permitted flow. This detects not only failure to block, but also overbroad changes that unnecessarily remove service.

**Option explanations**

- **A:** This verifies that the required permitted service remains usable.
- **B:** Existence alone does not show correct attachment or actual forwarding behavior.
- **C:** A stable hostname does not demonstrate either flow’s outcome.
- **D:** This links the prohibited test to the intended enforcement decision.

**Further reading**

- [Configure IP Access Lists](https://www.cisco.com/c/en/us/support/docs/security/ios-firewall/23602-confaccesslists.html) — ACL Concepts; Masks; Process ACLs; Apply ACLs; Extended ACLs

---

## CCNA9-088 · Security Fundamentals

Objectives: 5.7 · single · Applied

An operator enables sticky learning on a port where a rogue laptop is currently the first and only connected source. There are no manually configured secure addresses. Why does this fail to establish that only approved equipment is allowed?

- **A.** Sticky learning records the observed source; it does not independently know whether that source is approved.
- **B.** Sticky learning accepts only factory-listed Cisco NIC addresses.
- **C.** The first learned MAC is automatically a trusted DHCP server.
- **D.** Sticky learning consults the employee directory and must automatically reject the rogue laptop.

**Answer: A**

Learning a source and authorizing a device are different activities. Control the commissioning conditions and verify learned entries before relying on them as approved restrictions.

**Option explanations**

- **A:** The initial learning population must be controlled or explicitly verified.
- **B:** The feature does not impose that manufacturer allowlist.
- **C:** Secure MAC learning does not grant DHCP snooping trust.
- **D:** No identity-directory lookup is part of the described feature.

**Further reading**

- [Catalyst 3750-X and 3560-X Configuration Guide: Configuring Port-Based Traffic Control](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst3750x_3560x/software/release/15-0_2_se/configuration/guide/3750x_cg/swtrafc.html) — Secure MAC Addresses; Security Violations; Port Security Aging

---

## CCNA9-089 · Security Fundamentals

Objectives: 5.7 · single · Applied

An engineer must verify the port-security status, current secure-address count, configured maximum, and violation mode on Gi1/0/12. Which command is most directly targeted to these interface settings and counters?

- **A.** show interfaces gigabitethernet1/0/12
- **B.** show ip dhcp snooping binding
- **C.** show mac address-table interface gigabitethernet1/0/12
- **D.** show port-security interface gigabitethernet1/0/12

**Answer: D**

Choose an observation that reports the feature being verified. To list the individual secure MAC addresses as an additional check, use show port-security interface gigabitethernet1/0/12 address.

**Option explanations**

- **A:** General interface operational statistics do not directly report the configured port-security maximum and violation mode.
- **B:** DHCP snooping bindings do not supply the port-security maximum or violation mode.
- **C:** The forwarding address table does not directly report port-security maximum and violation policy.
- **D:** This displays the interface port-security status, secure-address count, maximum, and violation mode.

**Further reading**

- [Catalyst 3750-X and 3560-X Configuration Guide: Configuring Port-Based Traffic Control](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst3750x_3560x/software/release/15-0_2_se/configuration/guide/3750x_cg/swtrafc.html) — Displaying Port-Based Traffic Control Settings — Table 1-4, show port-security and show port-security address

---

## CCNA9-090 · Security Fundamentals

Objectives: 5.4 · multiple · Applied

A device supports strong password hashing for local secrets. Which two handling practices remain necessary even when passwords are stored as hashes? Select two.

- **A.** Use unique, sufficiently strong passwords for the local accounts.
- **B.** Publish hashes freely because hashing makes guessing impossible.
- **C.** Restrict access to configuration backups containing the hashes.
- **D.** Reuse a publicly exposed password because the device stores only its hash.

**Answer: A, C**

Hashing protects stored credentials in a specific way; it does not remove the need for good source secrets and access control over the stored verifier. Apply protection through the credential’s full lifecycle.

**Option explanations**

- **A:** Hashing does not turn a predictable or reused original secret into a strong credential.
- **B:** A stored hash can still be tested against candidate passwords.
- **C:** A captured hash may enable offline guessing and the configuration contains other sensitive details.
- **D:** An attacker can submit the exposed plaintext password through the normal login path.

**Further reading**

- [NIST SP 800-63B-4: Digital Identity Guidelines — Authentication and Authenticator Management](https://pages.nist.gov/800-63-4/sp800-63b.html) — Authentication factors; password verifiers; authenticator management

---

## CCNA9-091 · Automation and Programmability

Objectives: 6.1 · single · Applied

A read-only inventory job uses an account with permission to erase every managed switch configuration. The team wants the job’s credentials to provide only the authority required for its work. Which change best addresses that mismatch?

- **A.** Increase the job frequency while retaining the account
- **B.** Use a management role limited to the required inventory reads
- **C.** Rename the account read_only without changing permissions
- **D.** Place the account password inside each generated report

**Answer: B**

Automation credentials define what a compromised or mistaken workflow could do. Assigning only the read operations this job needs limits the mismatch between its intended purpose and available authority.

**Option explanations**

- **A:** More frequent execution does not reduce excess authority.
- **B:** The role would align credential permissions with the workflow’s actual operations.
- **C:** A name does not change the account’s effective authority.
- **D:** Distributing credentials increases exposure rather than constraining authority.

**Further reading**

- [What Is Network Automation?](https://www.cisco.com/site/us/en/learn/topics/networking/what-is-network-automation.html) — Network automation; profiles and policies; automated lifecycle management
- [Authorization - Meraki Dashboard API v1](https://developer.cisco.com/meraki/api-v1/authorization/) — Admin-scoped access: API keys; Bearer Auth; Security Best Practice

---

## CCNA9-092 · Automation and Programmability

Objectives: 6.2 · single · Applied

A company adds a server that polls device health and displays a network map. Each router still computes its routes independently, and the new server never programs forwarding behavior. Which conclusion is supported?

- **A.** All router control planes have moved to the new server
- **B.** Polling has converted user traffic into northbound API calls
- **C.** The server must now forward every inter-router packet
- **D.** Centralized monitoring alone does not establish centralized forwarding control

**Answer: D**

A central management view and a centralized control plane are different architectural properties. The routers in this scenario continue their traditional distributed control function.

**Option explanations**

- **A:** The scenario explicitly retains local route computation.
- **B:** Management observations do not convert ordinary packets into application API requests.
- **C:** It collects health data and does not program or carry the forwarding path.
- **D:** The added function is monitoring; the routing decisions remain distributed.

**Further reading**

- [RFC 7426: Software-Defined Networking (SDN): Layers and Architecture Terminology](https://www.rfc-editor.org/rfc/rfc7426.html) — 3.1 Overview; 3.2 Network Devices; 3.3 Control Plane; 3.5.3 Locality

---

## CCNA9-093 · Automation and Programmability

Objectives: 6.3.a, 6.3.b · matching · Applied

Match each described operation with its architectural role. The design uses an SDN controller and programmable switches. Use each role once.

1. The controller selects a replacement forwarding path after a topology change
2. A portal requests a supported service from the controller
3. A switch transmits a user packet according to an installed entry
4. The controller sends a supported rule update to a switch

- **A.** Data-plane forwarding
- **B.** Northbound API interaction
- **C.** Control-plane decision
- **D.** Southbound API interaction

**Answer: 1 → C; 2 → B; 3 → A; 4 → D**

The control plane decides forwarding behavior and the data plane applies it. Northbound and southbound describe the controller’s application-facing and device-facing interfaces.

**Option explanations**

- **A:** The switch executes an installed action on a user packet.
- **B:** An application requests a service from the controller.
- **C:** The decision selects forwarding behavior to install.
- **D:** The controller programs its managed device through this boundary.

**Further reading**

- [RFC 7426: Software-Defined Networking (SDN): Layers and Architecture Terminology](https://www.rfc-editor.org/rfc/rfc7426.html) — 3.1 Overview; 3.2 Network Devices; 3.3 Control Plane; 3.5.3 Locality
- [Software-Defined Networking (SDN) Definition](https://www.cisco.com/c/en/us/solutions/software-defined-networking/overview.html) — SDN elements; Features and benefits

---

## CCNA9-094 · Automation and Programmability

Objectives: 6.4 · single · Applied

An AIOps system groups a WAN-link alarm and several application timeouts into one incident because they occur together. Which use of this result is most justified?

- **A.** Use the correlation to focus investigation, then verify the actual dependency and cause
- **B.** Declare the WAN alarm to be the proven root cause without further evidence
- **C.** Delete the application events because one event has explained all of them
- **D.** Assume the grouping is generative configuration deployment

**Answer: A**

Event correlation can reduce fragmented investigation by identifying observations that may be related. Operators still need evidence connecting the suspected network failure to the application symptoms.

**Option explanations**

- **A:** Correlated observations can guide diagnosis without proving causation by themselves.
- **B:** Coincidence or correlation alone does not establish a causal path.
- **C:** Removing evidence prematurely can hide unrelated or additional causes.
- **D:** Grouping events is an analytics function, not deployment of generated configuration.

**Further reading**

- [What is AIOps?](https://developer.cisco.com/articles/what-is-aiops/) — The core components of AIOps; Is AIOps all you need?

---

## CCNA9-095 · Automation and Programmability

Objectives: 6.5 · multiple · Challenge

An API supports PUT /policies/blue, creating the resource if absent or replacing it if present. The policy is currently absent, and the client supplies a valid complete representation. Which two statements fit this API contract? Select two.

- **A.** PUT can only update an existing resource under every API
- **B.** This successful request can perform a Create operation in CRUD terms
- **C.** The client must first send DELETE because the target is absent
- **D.** PUT has idempotent intended semantics for repeated identical requests
- **E.** PUT must assign a different resource URI on each retry

**Answer: B, D**

CRUD labels describe the resource operation; HTTP method semantics are not a rigid one-to-one mapping in every circumstance. This documented PUT can create the named resource and then converge on the same representation when repeated.

**Option explanations**

- **A:** HTTP PUT can create a representation at the target URI when permitted.
- **B:** The specified target does not yet exist and the contract permits its creation.
- **C:** Deleting an absent resource does not enable this documented PUT operation.
- **D:** Repeating the same desired representation need not create additional named resources.
- **E:** The client has already identified the target URI.

**Further reading**

- [RFC 9110: HTTP Semantics](https://www.rfc-editor.org/rfc/rfc9110.html) — 9 Methods; 15 Status Codes

---

## CCNA9-096 · Automation and Programmability

Objectives: 6.5 · single · Applied

A client holds a valid OAuth bearer token for an HTTPS API. Which handling practice most directly prevents exposing that credential through a shared debug report?

- **A.** Replace the token’s letters with Base64 before publishing it
- **B.** Include the full Authorization header so every reader can replay the request
- **C.** Redact the token while retaining nonsecret method, URI and status information
- **D.** Put the token in the request URI so it appears in fewer places

**Answer: C**

A bearer token can convey access to whoever possesses it. Diagnostic output should retain useful context while removing the credential itself.

**Option explanations**

- **A:** Reversible encoding does not keep the credential confidential.
- **B:** That distributes the bearer credential to the report’s readers.
- **C:** The report can preserve diagnostic context without disclosing reusable authority.
- **D:** URI credentials can leak through logs and other URL handling.

**Further reading**

- [RFC 6750: The OAuth 2.0 Authorization Framework: Bearer Token Usage](https://www.rfc-editor.org/rfc/rfc6750.html) — 2 Authenticated Requests; 3 The WWW-Authenticate Response Header Field; 5 Security Considerations

---

## CCNA9-097 · Automation and Programmability

Objectives: 6.6 · single · Applied

An engineer uses Ansible Vault to encrypt credentials stored with automation files. Which statement correctly describes that feature’s purpose?

- **A.** It negotiates OSPF neighbors using the encrypted password
- **B.** It protects sensitive stored automation content with encryption
- **C.** It grants the credentials additional device privileges
- **D.** It guarantees that decrypted secrets never appear in later task output

**Answer: B**

Ansible Vault provides encryption for sensitive automation data. Secret handling during execution and output still needs appropriate care because encryption at rest does not redefine how a task uses a value.

**Option explanations**

- **A:** Vault is an automation secret-storage feature, not an OSPF protocol function.
- **B:** Vault can encrypt variables or files that contain secrets.
- **C:** Encrypting stored data does not change its account permissions.
- **D:** Protecting stored content does not by itself protect every later use or log.

**Further reading**

- [Protecting sensitive data with Ansible vault](https://docs.ansible.com/projects/ansible/latest/vault_guide/index.html) — Encrypting and managing sensitive data

---

## CCNA9-098 · Automation and Programmability

Objectives: 6.6 · single · Applied

A team uses Ansible to configure supported router services and Terraform to manage supported virtual networks. A reviewer claims Terraform can manage only public-cloud resources, so it cannot be considered for an on-premises controller with a suitable provider. Which response is accurate?

- **A.** The reviewer is correct because the word infrastructure means public cloud
- **B.** Terraform automatically supports every on-premises controller without a provider
- **C.** Ansible can manage only operating-system packages, never network devices
- **D.** Terraform can manage on-premises resources when a suitable provider supports them

**Answer: D**

Terraform’s provider model can support cloud and on-premises infrastructure. Tool selection should examine the needed operations and supported integrations rather than rely only on where the infrastructure runs.

**Option explanations**

- **A:** Terraform infrastructure management is not restricted to public cloud.
- **B:** Actual API and resource support still must exist.
- **C:** Ansible has supported network automation integrations.
- **D:** The relevant boundary is supported resource/API capability, not solely deployment location.

**Further reading**

- [What is Terraform?](https://developer.hashicorp.com/terraform/intro) — How does Terraform work?; Manage any infrastructure; Track your infrastructure
- [Providers](https://developer.hashicorp.com/terraform/language/providers) — What Providers Do; Provider Documentation

---

## CCNA9-099 · Automation and Programmability

Objectives: 6.7 · single · Applied

A JSON client needs the numeric value of packets under statistics, not the string inside the note. Which value should it use?

```text
{"statistics":{"packets":2048},"note":"packets=4096"}
```

- **A.** 2048
- **B.** "packets=4096"
- **C.** 4096
- **D.** statistics

**Answer: A**

Named member structure determines where the value resides. Text inside another string does not override the numeric packets member in the statistics object.

**Option explanations**

- **A:** The packets member inside statistics contains the unquoted numeric value 2048.
- **B:** That is the complete note string, not the required numeric member.
- **C:** Those digits occur inside a string and do not define the statistics.packets value.
- **D:** This is the name of the enclosing object member, not its packet count.

**Further reading**

- [RFC 8259: The JavaScript Object Notation (JSON) Data Interchange Format](https://www.rfc-editor.org/rfc/rfc8259.html) — 2 JSON Grammar; 3 Values; 4 Objects; 5 Arrays; 6 Numbers; 7 Strings

---

## CCNA9-100 · Automation and Programmability

Objectives: 6.7 · multiple · Applied

A network API expects a native JSON array containing only VLAN numbers; an empty array is allowed. Which two payloads meet that requirement for the vlans value? Select two.

- **A.** {"vlans":"[10,20]"}
- **B.** {"vlans":{"10":true,"20":true}}
- **C.** {"vlans":[10,20]}
- **D.** {"vlans":["10","20"]}
- **E.** {"vlans":[]}

**Answer: C, E**

JSON distinguishes an array from a string that merely looks like serialized array text. The numeric array and the empty array have the required native container and permitted element types.

**Option explanations**

- **A:** This is a string whose characters resemble an array.
- **B:** This uses an object keyed by VLAN text.
- **C:** The value is an array with two numeric elements.
- **D:** This array contains strings rather than VLAN numbers.
- **E:** The value is an empty native array, containing no elements that violate the numeric requirement.

**Further reading**

- [RFC 8259: The JavaScript Object Notation (JSON) Data Interchange Format](https://www.rfc-editor.org/rfc/rfc8259.html) — 2 JSON Grammar; 3 Values; 4 Objects; 5 Arrays; 6 Numbers; 7 Strings

---
