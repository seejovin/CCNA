# CCNA Practice — Set 10

100 original questions aligned to CCNA 200-301 v1.1. No interactive labs.

Answers and explanations follow each question. For an unrevealed attempt, use the Streamlit app.

Content review date: 2026-09-14.

## CCNA10-001 · Network Fundamentals

Objectives: 1.1.a, 1.1.b, 1.1.d · single · Applied

A floor adds wireless clients to an existing user VLAN. A device must provide radio access and bridge those clients into that LAN, without becoming their IP default gateway. Which role meets the requirement?

- **A.** A routed WAN interface
- **B.** A router configured only with wired interfaces
- **C.** An access point using the intended bridged WLAN/VLAN mapping
- **D.** A Layer 2 switch with no wireless radio

**Answer: C**

Identify both the required radio function and the specified forwarding model. An AP need not also be the clients’ IP router.

**Option explanations**

- **A:** It does not directly provide the specified Wi-Fi radio access.
- **B:** That does not supply the required radio interface.
- **C:** The AP provides wireless attachment while another device retains the routing role.
- **D:** It can switch Ethernet but cannot directly serve 802.11 clients.

**Further reading**

- [Networking Basics: What You Need To Know](https://www.cisco.com/site/us/en/learn/topics/small-business/networking-basics.html) — Switches; Routers; Access Points
- [Campus LAN and Wireless LAN Solution Design Guide](https://www.cisco.com/c/en/us/td/docs/solutions/CVD/Campus/cisco-campus-lan-wlan-design-guide.html) — Centralized (local-mode) design model

---

## CCNA10-002 · Network Fundamentals

Objectives: 1.2.c · single · Applied

A new spine is added to an existing basic two-tier leaf-spine fabric. The design requires every leaf to connect once to every spine. There are six leaves. Which implementation completes that requirement?

- **A.** Connect the new spine to each of the six leaves
- **B.** Connect the new spine only to an old spine
- **C.** Connect the new spine to one leaf and rely on leaf-to-leaf links
- **D.** Connect all servers directly to the new spine

**Answer: A**

Adding a spine extends the leaf-to-spine mesh. The change requires capacity and connections on every participating leaf.

**Option explanations**

- **A:** Each leaf needs its own link to the new spine.
- **B:** That does not provide the required leaf-to-new-spine links.
- **C:** The required relationship is not satisfied by that shortcut.
- **D:** That bypasses the specified leaf attachment role.

**Further reading**

- [Cisco Massively Scalable Data Center Network Fabric Design and Operation White Paper](https://www.cisco.com/c/en/us/products/collateral/switches/nexus-9000-series-switches/white-paper-c11-743245.html) — MSDC Layer 3 IP fabric design evolution; Cisco MSDC design example 1: Two-tiered spine-leaf topology

---

## CCNA10-003 · Network Fundamentals

Objectives: 1.3.a · single · Foundation

A PoE phone needs one Ethernet cable for both network data and electrical power from its access switch. Which proposed medium directly supports that requirement with ordinary compatible PoE ports?

- **A.** A duplex fiber pair without a separate power feed
- **B.** A passive optical splitter
- **C.** An RF-only connection
- **D.** Compatible copper twisted-pair Ethernet cabling

**Answer: D**

Choose a medium that supports both requested functions. A fiber data link would need a separate power arrangement for this endpoint.

**Option explanations**

- **A:** Optical data fiber does not itself carry PoE electrical power.
- **B:** It does not supply the required Ethernet copper power path.
- **C:** Wi-Fi data access does not deliver ordinary wired PoE.
- **D:** The cable can carry the supported Ethernet and PoE signals together.

**Further reading**

- [Interface and Hardware Components Configuration Guide, Cisco IOS XE 17.14.x (Catalyst 9200 Switches): Configuring Power over Ethernet](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst9200/software/release/17-14/configuration_guide/int_hw/b_1714_int_and_hw_9200_cg/configuring_poe.html) — Powered-Device Detection and Initial Power Allocation
- [Cisco 10GBASE SFP+ Modules Data Sheet](https://www.cisco.com/c/en/us/products/collateral/interfaces-modules/transceiver-modules/data_sheet_c78-455693.html) — Cisco SFP-10G-SR module; Cisco SFP-10G-LR module; Cisco SFP-10G-T-X module

---

## CCNA10-004 · Network Fundamentals

Objectives: 1.4 · single · Applied

A legacy 100 Mb/s link has both ends forced full duplex. Its late-collision counter is zero, but a cable movement causes carrier flaps. Which next action is best aligned with the evidence?

- **A.** Assume the lack of collisions proves the cable is good
- **B.** Inspect and test the affected cable, connector, and port path
- **C.** Change both ends to half duplex to remove all physical faults
- **D.** Increase the DNS cache size

**Answer: B**

Use the observed failure mechanism to choose the next check. Zero collisions does not rule out an intermittent physical link.

**Option explanations**

- **A:** A cable can lose carrier without generating collisions.
- **B:** Movement-correlated carrier loss points toward physical connectivity.
- **C:** Duplex changes do not repair intermittent contact.
- **D:** Resolver caching does not stabilize electrical carrier.

**Further reading**

- [Configure and Verify Ethernet 10/100/1000Mb Half/Full Duplex Auto-Negotiation](https://www.cisco.com/c/en/us/support/docs/lan-switching/ethernet/10561-3.html) — Background Information; Auto-Negotiation on Catalyst Switches that Run Cisco IOS Software

---

## CCNA10-005 · Network Fundamentals

Objectives: 1.5 · single · Foundation

A sender reports that TCP acknowledged all bytes containing a database update. Which conclusion is justified by that acknowledgment alone?

- **A.** The database transaction is committed to durable storage
- **B.** The receiving user has read the updated record
- **C.** The receiving TCP endpoint accepted the acknowledged byte sequence
- **D.** The operation can never be rolled back

**Answer: C**

Transport success and application completion are different events. The application protocol must provide the evidence needed for database commit.

**Option explanations**

- **A:** TCP receipt is not an application commit acknowledgment.
- **B:** Transport acknowledgment does not establish user interaction.
- **C:** The evidence is at the transport layer.
- **D:** Application state and rollback behavior are outside TCP’s guarantee.

**Further reading**

- [RFC 9293: Transmission Control Protocol (TCP)](https://www.rfc-editor.org/rfc/rfc9293.html#section-2.2) — 2.2. Key TCP Concepts

---

## CCNA10-006 · Network Fundamentals

Objectives: 1.6 · single · Applied

A host is configured as 10.60.10.200/24, but its VLAN is assigned 10.60.10.192/27. Its router is 10.60.10.193/27. Which correction aligns the host’s local-subnet decision with the intended VLAN?

| Device | Address |
| --- | --- |
| Host, current | 10.60.10.200/24 |
| Router, intended | 10.60.10.193/27 |

- **A.** Keep the address and change the mask to 255.255.255.224
- **B.** Keep /24 because the first three octets match the router
- **C.** Change the host to 10.60.10.192/27
- **D.** Change the router to 10.60.10.223/27

**Answer: A**

The address can stay while its prefix length is corrected. A too-broad mask can cause incorrect on-link assumptions for other destinations.

**Option explanations**

- **A:** The host address is usable in .192/27, but its current mask is too broad.
- **B:** Matching visible octets does not make different prefix boundaries equivalent.
- **C:** That would assign the subnet identifier to the host.
- **D:** That would assign the directed broadcast address to the router.

**Further reading**

- [Configure IP Addresses and Unique Subnets for New Users](https://www.cisco.com/c/en/us/support/docs/ip/routing-information-protocol-rip/13788-3.html) — Network Masks; Understand Subnetting; VLSM Example

---

## CCNA10-007 · Network Fundamentals

Objectives: 1.7 · multiple · Applied

Which TWO statements correctly describe private IPv4 use? Select two.

- **A.** A private source is automatically trustworthy
- **B.** Only one organization may assign 192.168.1.0/24
- **C.** Private IPv4 addresses cannot cross any router
- **D.** Private space avoids consuming globally unique public addresses for internal-only hosts
- **E.** Renumbering or another explicit design may be needed when overlapping private networks are joined

**Answer: D, E**

Private addressing helps conserve public address allocations while permitting independent reuse. Reuse requires care when separate addressing domains are interconnected.

**Option explanations**

- **A:** An address range does not authenticate a sender.
- **B:** Independent organizations can reuse private space.
- **C:** They can be routed internally.
- **D:** RFC 1918 supports internal addressing without public allocation.
- **E:** Reuse creates a potential integration conflict.

**Further reading**

- [RFC 1918: Address Allocation for Private Internets](https://www.rfc-editor.org/rfc/rfc1918#section-3) — 3. Private Address Space

---

## CCNA10-008 · Network Fundamentals

Objectives: 1.8 · single · Applied

A /64 interface configuration changes from 2001:db8:17:6::15 to 2001:db8:17:6::150. What changed?

- **A.** The /64 LAN prefix
- **B.** The interface identifier within the same /64
- **C.** The address family from IPv6 to IPv4
- **D.** The link-local scope identifier

**Answer: B**

Trailing zeros inside a hextet are significant; ::15 and ::150 are different addresses. Their first 64 bits still match.

**Option explanations**

- **A:** The first four hextets remain the same.
- **B:** The differing low-order value lies after the prefix boundary.
- **C:** Both strings are IPv6 addresses.
- **D:** Both examples use the same documentation global-unicast prefix, not a link-local zone.

**Further reading**

- [RFC 4291: IP Version 6 Addressing Architecture](https://www.rfc-editor.org/rfc/rfc4291#section-2.3) — 2.3. Text Representation of Address Prefixes; 2.4. Address Type Identification; 2.5.6. Link-Local IPv6 Unicast Addresses; 2.7. Multicast Addresses

---

## CCNA10-009 · Network Fundamentals

Objectives: 1.9.a, 1.9.c · multiple · Applied

Which TWO assertions about IPv6 addressing are correct? Select two.

- **A.** IPv6 uses 255.255.255.255 for all-nodes broadcast
- **B.** The address ::1 identifies every router on the link
- **C.** IPv6 uses multicast for functions that might otherwise require broadcast-style group delivery
- **D.** A link-local unicast destination must not be forwarded onto another link
- **E.** Every global-unicast address must be generated from a MAC

**Answer: C, D**

IPv6 distinguishes individual, group, loopback, and scoped uses. Similar operational goals do not imply identical IPv4 and IPv6 address mechanisms.

**Option explanations**

- **A:** That is IPv4 notation, and IPv6 has no broadcast type.
- **B:** ::1 is the local loopback address.
- **C:** Multicast supplies IPv6 group addressing without a broadcast address type.
- **D:** Its scope is restricted to the link.
- **E:** IPv6 permits other identifier-generation methods.

**Further reading**

- [RFC 4291: IP Version 6 Addressing Architecture](https://www.rfc-editor.org/rfc/rfc4291#section-2.3) — 2.3. Text Representation of Address Prefixes; 2.4. Address Type Identification; 2.5.6. Link-Local IPv6 Unicast Addresses; 2.7. Multicast Addresses

---

## CCNA10-010 · Network Fundamentals

Objectives: 1.10 · single · Applied

A laptop has both Ethernet and Wi-Fi enabled. An operator inspects only the Ethernet IP values while the tested traffic uses Wi-Fi. What should be corrected in the verification method?

- **A.** Inspect the actual interface and route used by the tested traffic
- **B.** Assume both interfaces always have identical gateway and DNS settings
- **C.** Disable IPv6 permanently before inspecting any settings
- **D.** Infer the active gateway solely from the laptop’s hostname

**Answer: A**

Verify effective state for the relevant interface and address family. A machine can have several simultaneous network configurations.

**Option explanations**

- **A:** Parameters on an unused interface do not describe the active path.
- **B:** Separate network services can have different parameters.
- **C:** That is not necessary to identify the actual traffic path.
- **D:** Names do not identify the selected egress route.

**Further reading**

- [ipconfig](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/ipconfig) — Syntax; Parameters (/all)
- [ip-route(8) — Linux manual page](https://man7.org/linux/man-pages/man8/ip-route.8.html) — ip route show; route types and nexthops
- [Change TCP/IP settings on Mac](https://support.apple.com/en-hk/guide/mac-help/mh14129/mac) — IP address, subnet mask, and router settings

---

## CCNA10-011 · Network Fundamentals

Objectives: 1.11.a, 1.11.c · single · Applied

An AP’s channel width is increased while nearby APs retain their current channel assignments. Why should the RF plan be checked again?

- **A.** SSID spelling automatically changes with width
- **B.** Encryption no longer works on wider channels
- **C.** Every neighboring AP receives a new private address
- **D.** The wider occupied spectrum may overlap more neighboring transmissions

**Answer: D**

Assess occupied bandwidth as well as channel center. Wider channels can change frequency reuse and contention conditions.

**Option explanations**

- **A:** The network name is independent of channel width.
- **B:** Width alone does not disable configured encryption.
- **C:** RF changes do not inherently renumber IP interfaces.
- **D:** A previously suitable narrow-channel plan may not remain suitable.

**Further reading**

- [Channel Planning Best Practices](https://documentation.meraki.com/Wireless/Design_and_Configure/Architecture_and_Best_Practices/Channel_Planning_Best_Practices) — 2.4 GHz

---

## CCNA10-012 · Network Fundamentals

Objectives: 1.12 · multiple · Applied

Two VMs use separate guest kernels but share one physical NIC through a virtual switch. Which TWO conclusions follow? Select two.

- **A.** The VMs necessarily use one combined guest kernel
- **B.** The physical NIC is a common connectivity dependency
- **C.** VM isolation automatically doubles that NIC’s line rate
- **D.** All frames must leave the host even for local virtual-switch traffic
- **E.** Separate virtual NICs do not establish independent physical network paths

**Answer: B, E**

Logical interfaces can be isolated while relying on shared physical resources. Capacity and failure independence require examination of the underlying paths.

**Option explanations**

- **A:** The scenario explicitly provides separate guest kernels.
- **B:** Both external paths traverse the same underlying NIC.
- **C:** Virtualization does not create additional physical bandwidth.
- **D:** Local virtual switching can keep eligible traffic inside the host.
- **E:** Their configured external path still shares one NIC.

**Further reading**

- [Network XML format](https://libvirt.org/formatnetwork.html) — Connectivity; isolated network; bridge
- [What is a container?](https://docs.docker.com/get-started/docker-concepts/the-basics/what-is-a-container/#containers-versus-virtual-machines-vms) — Containers versus virtual machines (VMs)

---

## CCNA10-013 · Network Fundamentals

Objectives: 1.13.a, 1.13.b, 1.13.d · single · Applied

The table below contains a fresh destination entry for B in VLAN 60. A frame from A to B enters Gi1/0/2 in VLAN 60. All relevant ports are forwarding. Which action is correct?

```text
VLAN   MAC address       Type      Port
60     00bb.0000.0060     DYNAMIC   Gi1/0/7

Received frame:
source A = 00aa.0000.0060
destination B = 00bb.0000.0060
```

- **A.** Send only to Gi1/0/2 because it is the source port
- **B.** Flood VLAN 60 because A is not yet in the table
- **C.** Learn A on Gi1/0/2 and forward toward B on Gi1/0/7
- **D.** Learn B on Gi1/0/2 and forward to VLAN 70

**Answer: C**

Consult the destination mapping independently of whether the source is new. A fresh source can be learned during a directed unicast forwarding operation.

**Option explanations**

- **A:** The destination entry points to a different port.
- **B:** An unknown source does not make the known destination unknown.
- **C:** Source learning and known-destination forwarding can occur together.
- **D:** Learning uses the source and forwarding remains in VLAN 60.

**Further reading**

- [Configuring MAC Address Tables](https://www.cisco.com/c/en/us/td/docs/switches/datacenter/nexus5500/sw/layer2/7x/b_5500_Layer2_Config_7x/config_mac_address_tables.pdf) — Information About MAC Addresses (page 1); Configuring the Aging Time for the MAC Table (page 2)

---

## CCNA10-014 · Network Fundamentals

Objectives: 1.1.h · single · Applied

A switch reserves 30 W at the power-sourcing port for an AP. A technician expects the AP to receive every reserved watt after a long compliant copper channel. What must the technician account for?

- **A.** Power loss in the cable and the distinction between source allocation and delivered device power
- **B.** An Ethernet checksum adding power to the signal
- **C.** The SSID determining the cable resistance
- **D.** The IP subnet increasing PoE voltage automatically

**Answer: A**

Source power and powered-device input power are different measurement points. Relevant PoE specifications account for channel losses.

**Option explanations**

- **A:** Not all sourced electrical power reaches the powered device.
- **B:** Checksums do not supply electrical energy.
- **C:** A network name has no such electrical effect.
- **D:** IP addressing does not regulate this power delivery.

**Further reading**

- [Interface and Hardware Components Configuration Guide, Cisco IOS XE 17.14.x (Catalyst 9200 Switches): Configuring Power over Ethernet](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst9200/software/release/17-14/configuration_guide/int_hw/b_1714_int_and_hw_9200_cg/configuring_poe.html) — Powered-Device Detection and Initial Power Allocation

---

## CCNA10-015 · Network Fundamentals

Objectives: 1.6 · single · Challenge

Inside 10.90.0.0/24, 10.90.0.0/25 and 10.90.0.128/26 are allocated. A new LAN needs 40 ordinary host addresses. Which remaining allocation fits without overlap?

- **A.** 10.90.0.160/26
- **B.** 10.90.0.192/27
- **C.** 10.90.1.0/26
- **D.** 10.90.0.192/26

**Answer: D**

A 40-host LAN needs at least /26. The first two allocations leave exactly one free /26 inside the specified /24.

**Option explanations**

- **A:** That written address falls in the already allocated .128/26 block.
- **B:** A /27 has only 30 usable addresses.
- **C:** This is outside the required /24 parent allocation.
- **D:** It occupies the free .192–.255 block and supports 62 usable hosts.

**Further reading**

- [Configure IP Addresses and Unique Subnets for New Users](https://www.cisco.com/c/en/us/support/docs/ip/routing-information-protocol-rip/13788-3.html) — Network Masks; Understand Subnetting; VLSM Example

---

## CCNA10-016 · Network Fundamentals

Objectives: 1.9.d · single · Applied

An administrator intends to derive an IPv6 identifier from MAC 00-25-96-12-34-56 using modified EUI-64. The proposed result is 0025:96ff:fe12:3456. Which correction is needed?

- **A.** Remove the FF-FE insertion
- **B.** Change the first hextet from 0025 to 0225
- **C.** Change the last hextet to 5634
- **D.** Add another zero hextet at the end

**Answer: B**

The insertion is already correct. Inverting the 02 bit changes first byte 00 to 02, producing 0225:96ff:fe12:3456.

**Option explanations**

- **A:** The middle insertion is required by the specified procedure.
- **B:** The U/L bit in the first byte has not yet been inverted.
- **C:** The procedure does not reverse the original MAC bytes.
- **D:** An interface identifier must remain 64 bits, or four hextets.

**Further reading**

- [RFC 2464: Transmission of IPv6 Packets over Ethernet Networks](https://datatracker.ietf.org/doc/html/rfc2464#section-4) — 4. Stateless Autoconfiguration

---

## CCNA10-017 · Network Fundamentals

Objectives: 1.11.b · single · Foundation

An AP advertises both Staff and Guest SSIDs through one radio. What does the second SSID create by itself?

- **A.** A second independent physical frequency channel
- **B.** A guaranteed security boundary between all traffic
- **C.** Another advertised WLAN name on that radio
- **D.** A dedicated full-duplex medium for Guest

**Answer: C**

One radio can advertise multiple logical WLANs. Channel resources and security policy must be evaluated separately.

**Option explanations**

- **A:** Multiple SSIDs can share one radio channel.
- **B:** Isolation depends on forwarding and policy configuration.
- **C:** The SSID identifies a network; other settings define its behavior.
- **D:** Another name does not change shared wireless medium behavior.

**Further reading**

- [Campus LAN and Wireless LAN Solution Design Guide](https://www.cisco.com/c/en/us/td/docs/solutions/CVD/Campus/cisco-campus-lan-wlan-design-guide.html) — Centralized (local-mode) design model
- [Wireless Fundamentals: Encryption and Authentication](https://documentation.meraki.com/Wireless/Design_and_Configure/Architecture_and_Best_Practices/Wireless_Fundamentals:_Encryption_and_Authentication) — WPA2 – Personal; Hidden SSID

---

## CCNA10-018 · Network Fundamentals

Objectives: 1.13.c · single · Applied

A switch floods a unicast frame because its destination is absent from the MAC table. Which destination MAC is carried in the transmitted copies?

- **A.** The original unicast destination MAC
- **B.** The Ethernet broadcast MAC in every copy
- **C.** The switch management MAC
- **D.** A different random MAC on each egress port

**Answer: A**

Flooding describes where copies are transmitted. It does not change a unicast destination address into a broadcast destination.

**Option explanations**

- **A:** Flooding replicates the frame without converting its destination into broadcast.
- **B:** Flooded unicast and broadcast addressing are not the same.
- **C:** The switch is forwarding the host’s frame, not addressing it to itself.
- **D:** Ordinary flooding does not randomly rewrite destinations.

**Further reading**

- [Configuring MAC Address Tables](https://www.cisco.com/c/en/us/td/docs/switches/datacenter/nexus5500/sw/layer2/7x/b_5500_Layer2_Config_7x/config_mac_address_tables.pdf) — Information About MAC Addresses (page 1); Configuring the Aging Time for the MAC Table (page 2)

---

## CCNA10-019 · Network Fundamentals

Objectives: 1.2.f · single · Applied

A diagram labels one application on-premises and another in public cloud. Which question still needs separate evidence before concluding the two can communicate?

- **A.** Do both applications have names of equal length?
- **B.** Are both applications implemented in the same language?
- **C.** Do both servers use the same MAC address?
- **D.** Is an allowed network path, with appropriate routing and service access, configured between them?

**Answer: D**

A hosting classification is not a reachability test. Verify the path and the actual service requirements.

**Option explanations**

- **A:** Naming length is not a connectivity condition.
- **B:** Compatible protocols can connect different implementations.
- **C:** Matching MACs is neither required nor desirable as a general connectivity condition.
- **D:** Hosting labels alone do not establish effective communication.

**Further reading**

- [NIST SP 800-145: The NIST Definition of Cloud Computing](https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-145.pdf) — 2. The NIST Definition of Cloud Computing — Essential Characteristics; Deployment Models
- [What is a WAN (wide-area network)?](https://www.cisco.com/site/us/en/learn/topics/networking/what-is-a-wan-wide-area-network.html) — What is a WAN (wide-area network)?; What is a WAN router?

---

## CCNA10-020 · Network Fundamentals

Objectives: 1.4 · matching · Applied

Match each verified interface observation with the issue it directly establishes. Use each issue once.

1. One end is forced to 100 Mb/s and the other to 10 Mb/s on a direct link.
2. Both ends use 100 Mb/s, but one is full duplex and the other half duplex.
3. The local interface reports administratively down and its configuration includes shutdown.
4. A sustained traffic burst exceeds egress capacity, with increasing output drops and no new CRC errors.

- **A.** Administrative shutdown
- **B.** Speed mismatch
- **C.** Duplex mismatch
- **D.** Egress congestion

**Answer: 1 → B; 2 → C; 3 → A; 4 → D**

Identify the issue established by each observation. Similar user-visible slowness or outage symptoms can originate at different interface mechanisms.

**Option explanations**

- **A:** The interface is intentionally disabled in configuration.
- **B:** The two fixed operational rate requirements disagree.
- **C:** The two ends disagree on simultaneous versus shared-medium behavior.
- **D:** Offered traffic exceeds output capacity and the output queue discards excess frames.

**Further reading**

- [Configure and Verify Ethernet 10/100/1000Mb Half/Full Duplex Auto-Negotiation](https://www.cisco.com/c/en/us/support/docs/lan-switching/ethernet/10561-3.html) — Background Information; Auto-Negotiation on Catalyst Switches that Run Cisco IOS Software
- [QoS Frequently Asked Questions](https://www.cisco.com/c/en/us/support/docs/quality-of-service-qos/qos-policing/22833-qos-faq.html) — Queueing and Congestion Management

---

## CCNA10-021 · Network Access

Objectives: 2.1.a, 2.3 · single · Applied

A Cisco phone has rebooted without a saved voice VLAN. It is designed to learn VLAN 190 using CDP; LLDP and manual phone VLAN configuration are not used. The switch has correct data and voice VLAN commands. Global CDP is running, but the interface is configured with no cdp enable. What is the targeted correction?

- **A.** Change the PC’s access VLAN to 190.
- **B.** Make every uplink use native VLAN 190.
- **C.** Enable CDP on the phone-facing interface while global CDP is running.
- **D.** Change the switch’s default route to the phone’s MAC address.

**Answer: C**

A correct voice VLAN command still depends on the selected endpoint-discovery method. Verify the phone learns the intended policy after restoring CDP.

**Option explanations**

- **A:** That moves PC data and does not restore the configured phone advertisement mechanism.
- **B:** The missing local CDP advertisement is independent of those upstream native settings.
- **C:** The selected mechanism for telling this phone its voice VLAN must be operational.
- **D:** An Ethernet MAC is not an IP route next hop, and routing does not supply CDP.

**Further reading**

- [VLAN Configuration Guide, Cisco IOS XE 17.15.x — Configuring Voice VLANs](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst9300/software/release/17-15/configuration_guide/vlan/b_1715_vlan_9300_cg/configuring_voice_vlans.html) — Cisco IP Phone Voice Traffic; Cisco IP Phone Data Traffic
- [Network Management Configuration Guide, Cisco IOS XE 17.15.x — Configuring Cisco Discovery Protocol](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst9300/software/release/17-15/configuration_guide/nmgmt/b_1715_nmgmt_9300_cg/configuring_the_cisco_discovery_protocol.html) — Configuring Cisco Discovery Protocol; Monitoring and Maintaining Cisco Discovery Protocol

---

## CCNA10-022 · Network Access

Objectives: 2.1.c · single · Applied

A multilayer switch routes a packet from VLAN 14 to VLAN 24. There is no NAT, the destination host is directly attached, and ARP resolution is complete. Which Ethernet destination should the switch use on the VLAN 24 egress frame?

- **A.** The VLAN 24 number repeated as a MAC address
- **B.** The destination host’s resolved MAC address in VLAN 24
- **C.** The source host’s default-gateway MAC in VLAN 14
- **D.** The original source host’s MAC address

**Answer: B**

Routing preserves the intended IP destination while using a new Layer 2 header for the next link. For a directly attached destination, ARP supplies the host MAC.

**Option explanations**

- **A:** VLAN identifiers are not substituted for destination MAC addresses.
- **B:** The router builds the next Ethernet frame for the directly connected destination.
- **C:** That was relevant to the incoming frame, not the new egress destination.
- **D:** That would send the frame toward the wrong endpoint.

**Further reading**

- [Configure Inter-VLAN Routing with Catalyst Switches](https://www.cisco.com/c/en/us/support/docs/lan-switching/inter-vlan-routing/41260-189.html) — Configure; Troubleshoot

---

## CCNA10-023 · Network Access

Objectives: 2.1.b · single · Applied

VLAN 1 exists and has two active access ports connected to compatible hosts. The administrator shuts down interface Vlan1, which was used only for switch management. No filters or other topology changes apply. What happens to ordinary same-VLAN Layer 2 traffic between those hosts?

```text
vlan 1
interface Vlan1
 shutdown
! Access ports in VLAN 1 remain up and forwarding.
```

- **A.** It must stop because every VLAN requires an active management IP.
- **B.** It is automatically routed through VLAN 2.
- **C.** Both hosts acquire the switch’s old management IP.
- **D.** It can continue because shutting the SVI does not delete VLAN 1 or shut its access ports.

**Answer: D**

Do not equate a VLAN with its optional Layer 3 interface. This change removes SVI service while leaving the stated Layer 2 memberships intact.

**Option explanations**

- **A:** Pure Layer 2 forwarding does not require a live local SVI.
- **B:** An SVI shutdown does not migrate traffic to a different VLAN.
- **C:** The switch does not transfer its address to attached hosts.
- **D:** The management Layer 3 interface is distinct from the VLAN’s Layer 2 switching instance.

**Further reading**

- [VLAN Configuration Guide, Cisco IOS XE 17.15.x — Configuring VLANs](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst9300/software/release/17-15/configuration_guide/vlan/b_1715_vlan_9300_cg/configuring_vlans.html) — Supported VLANs; Deleting a VLAN; VLAN Port Membership Modes
- [Interface and Hardware Components Configuration Guide, Cisco IOS XE 17.15.x — Configuring Interface Characteristics](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst9300/software/release/17-15/configuration_guide/int_hw/b_1715_int_and_hw_9300_cg/configuring_interface_characteristics.html) — Switch Virtual Interfaces; Layer 3 Interfaces; Configuring SVI Autostate Exclude

---

## CCNA10-024 · Network Access

Objectives: 2.2.a · multiple · Applied

Two trunk endpoints have the admitted VLAN lists shown. Every listed VLAN exists at both ends and STP forwards all of them where allowed. Which TWO VLANs have an admitted bidirectional user-data path across this link? Select TWO.

| Endpoint | Allowed VLANs |
| --- | --- |
| SW-A | 12,23,34 |
| SW-B | 12,34,45 |

- **A.** VLAN 12
- **B.** VLAN 45
- **C.** VLAN 23
- **D.** VLAN 34

**Answer: A, D**

End-to-end admission is the intersection of the two trunk policies under the stated conditions. Local allowance alone does not establish a two-way path.

**Option explanations**

- **A:** It appears in both endpoints’ allowed lists.
- **B:** SW-A does not permit VLAN 45 on the trunk.
- **C:** SW-B does not permit VLAN 23 on the trunk.
- **D:** It appears in both endpoints’ allowed lists.

**Further reading**

- [VLAN Configuration Guide, Cisco IOS XE 17.15.x — Configuring VLAN Trunks](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst9300/software/release/17-15/configuration_guide/vlan/b_1715_vlan_9300_cg/configuring_vlan_trunks.html) — Allowed VLANs on a Trunk; Configuring the Native VLAN for Untagged Traffic

---

## CCNA10-025 · Network Access

Objectives: 2.2.c · single · Applied

After an uplink replacement, CDP logs a native VLAN mismatch between local VLAN 73 and peer VLAN 37. The design requires native VLAN 73 at both ends. What is the corrective action rather than merely hiding the diagnostic?

```text
%CDP-4-NATIVE_VLAN_MISMATCH: Native VLAN mismatch discovered
on GigabitEthernet1/0/48 (73), with DIST-3 GigabitEthernet1/0/2 (37).
```

- **A.** Disable CDP so the mismatch message disappears.
- **B.** Rename VLAN 37 to 73 without changing its VLAN ID.
- **C.** Increase the CDP holdtime indefinitely.
- **D.** Align the peer trunk’s native VLAN with the intended VLAN 73 and verify both ends.

**Answer: D**

A warning is evidence of effective configuration disagreement. Correct the data-path setting and then verify that the warning and mismatch are resolved.

**Option explanations**

- **A:** Suppressing the warning leaves the underlying native assignments inconsistent.
- **B:** A name change does not alter the numeric native VLAN setting.
- **C:** The timer does not repair incompatible VLAN classification.
- **D:** This addresses the actual untagged-frame classification mismatch.

**Further reading**

- [VLAN Configuration Guide, Cisco IOS XE 17.15.x — Configuring VLAN Trunks](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst9300/software/release/17-15/configuration_guide/vlan/b_1715_vlan_9300_cg/configuring_vlan_trunks.html) — Allowed VLANs on a Trunk; Configuring the Native VLAN for Untagged Traffic
- [Network Management Configuration Guide, Cisco IOS XE 17.15.x — Configuring Cisco Discovery Protocol](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst9300/software/release/17-15/configuration_guide/nmgmt/b_1715_nmgmt_9300_cg/configuring_the_cisco_discovery_protocol.html) — Configuring Cisco Discovery Protocol; Monitoring and Maintaining Cisco Discovery Protocol

---

## CCNA10-026 · Network Access

Objectives: 2.3 · single · Applied

SW-1 is connected directly to R1, and R1 routes to R2 on a separate Ethernet segment. There is no Layer 2 tunneling. Which router should normal CDP on SW-1 discover on its R1-facing link?

- **A.** R1 only
- **B.** R2 only, because routing skips the first neighbor
- **C.** Neither unless all three share one IP subnet
- **D.** Both R1 and R2 automatically

**Answer: A**

Discovery scope follows the local Layer 2 attachment. Build wider topology knowledge by collecting neighbor information at multiple devices.

**Option explanations**

- **A:** CDP is a directly connected Layer 2 discovery protocol and does not normally cross R1’s routed boundary.
- **B:** Discovery does not operate like an end-to-end routed destination lookup.
- **C:** CDP does not require matching IP subnets for directly attached neighbor discovery.
- **D:** R1 does not ordinarily forward CDP as routed IP traffic to reveal R2.

**Further reading**

- [Network Management Configuration Guide, Cisco IOS XE 17.15.x — Configuring Cisco Discovery Protocol](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst9300/software/release/17-15/configuration_guide/nmgmt/b_1715_nmgmt_9300_cg/configuring_the_cisco_discovery_protocol.html) — Configuring Cisco Discovery Protocol; Monitoring and Maintaining Cisco Discovery Protocol

---

## CCNA10-027 · Network Access

Objectives: 2.4 · single · Applied

One intended LACP member negotiates 1 Gb/s and the other negotiates 100 Mb/s on a Catalyst configuration requiring uniform member speed and duplex. Both cables show link up. What must be resolved before treating them as a compatible two-link bundle?

| Member | Operational speed | Duplex |
| --- | --- | --- |
| Gi1/0/3 | 1000 Mb/s | Full |
| Gi1/0/4 | 100 Mb/s | Full |

- **A.** The number of VLAN names in the inventory document only
- **B.** The absence of individual member default gateways
- **C.** The fact that there are two cables
- **D.** The member speed mismatch

**Answer: D**

Check physical negotiation as well as aggregation configuration. A working link at the wrong speed may still be unsuitable for the intended bundle.

**Option explanations**

- **A:** The demonstrated incompatibility is actual member speed.
- **B:** Physical members of a Layer 2 bundle do not need their own default gateways.
- **C:** Two compatible members are a normal aggregate design.
- **D:** Physical link-up does not satisfy the aggregate’s uniform member requirements.

**Further reading**

- [Layer 2 Configuration Guide, Cisco IOS XE 17.15.x — Configuring EtherChannels](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst9300/software/release/17-15/configuration_guide/lyr2/b_1715_lyr2_9300_cg/configuring_etherchannels.html) — LACP Modes; EtherChannel Configuration Guidelines; Load Balancing; Layer 3 EtherChannels; Hot-Standby Ports

---

## CCNA10-028 · Network Access

Objectives: 2.4 · single · Applied

A switch reports an operational port-channel but one expected physical member is flagged I, with the supplied legend defining I as stand-alone. Which evidence is needed before claiming the intended aggregate capacity?

```text
Flags: P - bundled in port-channel; I - stand-alone
Group  Port-channel  Protocol  Ports
8      Po8(SU)       LACP      Gi1/0/1(P) Gi1/0/2(I)
```

- **A.** Assume the port-channel number specifies its bandwidth in gigabits.
- **B.** Rename the stand-alone member to Bundled.
- **C.** Count every physically installed cable as active aggregate bandwidth.
- **D.** Verify that every intended active member actually joins the channel, then validate traffic distribution.

**Answer: D**

Logical interface availability and full intended capacity are different acceptance criteria. Member state must support the capacity claim.

**Option explanations**

- **A:** The numeric identifier is not a capacity measurement.
- **B:** An interface description cannot change its aggregation state.
- **C:** Physical presence is not proof of bundle membership.
- **D:** A stand-alone member does not contribute as a bundled member in the reported state.

**Further reading**

- [Layer 2 Configuration Guide, Cisco IOS XE 17.15.x — Configuring EtherChannels](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst9300/software/release/17-15/configuration_guide/lyr2/b_1715_lyr2_9300_cg/configuring_etherchannels.html) — LACP Modes; EtherChannel Configuration Guidelines; Load Balancing; Layer 3 EtherChannels; Hot-Standby Ports

---

## CCNA10-029 · Network Access

Objectives: 2.5.a · single · Applied

An engineer runs show spanning-tree vlan 90 on SW-Core. Root ID and Bridge ID both show priority 24666 and address 0011.2200.0090, and the output says This bridge is the root. Which fact confirms the root role?

```text
VLAN0090
 Root ID    Priority 24666
            Address  0011.2200.0090
            This bridge is the root
 Bridge ID  Priority 24666
            Address  0011.2200.0090
```

- **A.** The local bridge identity matches the elected root identity for VLAN 90.
- **B.** The switch must have the highest bridge priority in the network.
- **C.** The VLAN ID is greater than every port number.
- **D.** The switch hostname contains Core.

**Answer: A**

Use operational spanning-tree identity rather than naming conventions. The root role is evaluated for the particular VLAN instance.

**Option explanations**

- **A:** Equality of those identities and the explicit root indication establish the local root role.
- **B:** The lowest bridge ID wins, not the highest.
- **C:** That comparison is not an STP decision rule.
- **D:** Names do not participate in the root election.

**Further reading**

- [Layer 2 Configuration Guide, Cisco IOS XE 17.15.x — Configuring Spanning Tree Protocol](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst9300/software/release/17-15/configuration_guide/lyr2/b_1715_lyr2_9300_cg/configuring_spanning_tree_protocol.html) — Spanning-Tree Topology and Bridge Protocol Data Units; Bridge ID, Device Priority, and Extended System ID; (Optional) Configuring a Secondary Root Device

---

## CCNA10-030 · Network Access

Objectives: 2.5.b · matching · Applied

Match each observation of ordinary user-frame handling to its RSTP port state. Ignore control BPDUs in these observations; use each state once.

1. No user-data forwarding and no source MAC learning from user frames
2. Source MAC learning occurs, but user-data forwarding does not
3. Both source MAC learning and user-data forwarding occur

- **A.** Learning
- **B.** Discarding
- **C.** Forwarding

**Answer: 1 → B; 2 → A; 3 → C**

Port states describe user-data learning and forwarding behavior, while roles describe topology responsibility. Control protocol handling must not be inferred solely from user-frame blocking.

**Option explanations**

- **A:** Source MAC addresses can be learned while ordinary forwarding remains closed.
- **B:** Ordinary user frames are neither forwarded nor used for MAC learning.
- **C:** The port can both learn source MAC addresses and forward user data.

**Further reading**

- [Understand Rapid Spanning Tree Protocol (802.1w)](https://www.cisco.com/c/en/us/support/docs/lan-switching/spanning-tree-protocol/24062-146.html) — New Port States and Port Roles — Port States; Alternate and Backup Port Roles

---

## CCNA10-031 · Network Access

Objectives: 2.5.c · single · Applied

An edge workstation uses PortFast. A remote core-link failure still causes a temporary outage while the network reconverges. Why does this not contradict the purpose of PortFast?

- **A.** The workstation must be elected the root to avoid core failures.
- **B.** PortFast accelerates the edge port’s initial forwarding transition, not every remote failure in the network.
- **C.** PortFast automatically installs all missing IP routes.
- **D.** PortFast guarantees no outage anywhere once enabled on one port.

**Answer: B**

Keep the feature’s scope aligned with the observed event. Fast edge startup does not eliminate upstream convergence or routing dependencies.

**Option explanations**

- **A:** A nonbridging endpoint does not solve upstream topology failure by becoming root.
- **B:** The rest of the topology has its own convergence and service dependencies.
- **C:** The feature does not populate the routing table.
- **D:** Its scope is not a universal end-to-end availability guarantee.

**Further reading**

- [Layer 2 Configuration Guide, Cisco IOS XE 17.15.x — Configuring Optional Spanning-Tree Features](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst9300/software/release/17-15/configuration_guide/lyr2/b_1715_lyr2_9300_cg/configuring_optional_spanning_tree_features.html) — PortFast; Bridge Protocol Data Unit Guard; Bridge Protocol Data Unit Filtering; Root Guard; Loop Guard
- [Understand Rapid Spanning Tree Protocol (802.1w)](https://www.cisco.com/c/en/us/support/docs/lan-switching/spanning-tree-protocol/24062-146.html) — New Port States and Port Roles — Port States; Alternate and Backup Port Roles

---

## CCNA10-032 · Network Access

Objectives: 2.5.c, 2.5.d · multiple · Challenge

A Catalyst switch enables global spanning-tree portfast bpduguard default. Gi1/0/10 is operationally PortFast; Gi1/0/48 is a normal non-PortFast trunk with no explicit interface BPDU guard. Select TWO correct interpretations.

- **A.** The global default suppresses all outbound BPDUs on every port.
- **B.** Gi1/0/48 cannot participate in spanning tree because it is a trunk.
- **C.** A BPDU received on Gi1/0/10 can trigger the global default’s BPDU-guard shutdown.
- **D.** The global default alone does not apply that same PortFast-dependent guard behavior to Gi1/0/48.

**Answer: C, D**

Interpret global feature defaults through their activation conditions. An explicit per-interface enable would have a different scope.

**Option explanations**

- **A:** That is not the function of BPDU guard.
- **B:** Normal trunks commonly participate in spanning tree.
- **C:** The default applies to ports in operational PortFast state.
- **D:** The trunk is not operationally PortFast and has no explicit interface enable.

**Further reading**

- [Layer 2 Configuration Guide, Cisco IOS XE 17.15.x — Configuring Optional Spanning-Tree Features](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst9300/software/release/17-15/configuration_guide/lyr2/b_1715_lyr2_9300_cg/configuring_optional_spanning_tree_features.html) — PortFast; Bridge Protocol Data Unit Guard; Bridge Protocol Data Unit Filtering; Root Guard; Loop Guard

---

## CCNA10-033 · Network Access

Objectives: 2.6 · single · Applied

A cloud-managed AP deployment uses local bridge-mode forwarding. An engineer claims every AP requires a customer-hosted physical WLC because it is centrally managed. What is the architectural correction?

- **A.** Every client must become a controller for its own packets.
- **B.** Cloud-managed APs cannot have centralized configuration.
- **C.** A cloud management service can supply centralized management without a customer-hosted physical WLC for this design.
- **D.** Local bridge-mode forwarding is impossible with cloud management.

**Answer: C**

Describe where management services live independently of where user data goes. Centralized management can take more than one deployment form.

**Option explanations**

- **A:** Clients do not replace infrastructure management that way.
- **B:** The dashboard provides centralized management capabilities.
- **C:** Central management does not require the same on-premises controller appliance architecture.
- **D:** The stated architecture separates cloud management from local data handling.

**Further reading**

- [Meraki Cloud Architecture](https://documentation.meraki.com/Platform_Management/Dashboard_Administration/Design_and_Configure/Architectures_and_Best_Practices/Cisco_Meraki_Best_Practice_Design/Meraki_Cloud_Architecture) — Network and Management Data Segregation; The Meraki dashboard

---

## CCNA10-034 · Network Access

Objectives: 2.6 · single · Applied

A spare AP was placed in sniffer mode for troubleshooting. The capture task is finished, but users still cannot associate to that AP. It remains in sniffer mode and no other failures are found. What must change?

- **A.** Change only the switch port description to Production AP.
- **B.** Make every client send raw captured frames back to the analyzer.
- **C.** Increase the analyzer’s file-retention time.
- **D.** Return it to the appropriate supported client-serving mode and verify its WLAN policy.

**Answer: D**

Operational recovery includes restoring the intended service mode. Verify both the AP role and its applied WLAN configuration after diagnostic use.

**Option explanations**

- **A:** A label cannot reconfigure the AP mode.
- **B:** That is not ordinary WLAN association and service.
- **C:** Capture storage settings do not change the AP’s operating role.
- **D:** A dedicated capture role does not resume client service merely because analysis has ended.

**Further reading**

- [Cisco Wireless Controller Configuration Guide, Release 8.5 — Managing APs](https://www.cisco.com/c/en/us/td/docs/wireless/controller/8-5/config-guide/b_cg85/managing_aps.html) — AP Modes: client-serving and network management modes

---

## CCNA10-035 · Network Access

Objectives: 2.7 · single · Applied

An AP supports two SSIDs with centralized switching to one WLC. A technician requests two separate physical Ethernet cables solely because there are two SSIDs. What is the correct infrastructure assessment?

- **A.** Every SSID always requires its own console cable.
- **B.** Two SSIDs force the AP into a dedicated monitor role.
- **C.** One suitable AP IP connection can transport both WLANs through the controller tunnel.
- **D.** Each wireless client requires a separate controller distribution cable.

**Answer: C**

Logical WLAN count and physical uplink count are different design dimensions. Capacity, redundancy, and supported AP features determine the actual uplink requirement.

**Option explanations**

- **A:** The console does not transport an SSID’s client traffic.
- **B:** SSID count does not imply a monitoring-only mode.
- **C:** Multiple SSIDs do not inherently require one physical cable each.
- **D:** The wired interfaces aggregate many client flows.

**Further reading**

- [Cisco Wireless Controller Configuration Guide, Release 8.10 — AP Connectivity to Controller](https://www.cisco.com/c/en/us/td/docs/wireless/controller/8-10/config-guide/b_cg810/ap_connectivity_to_cisco_wlc.html) — CAPWAP
- [Cisco Wireless Controller Configuration Guide, Release 8.10 — Ports and Interfaces](https://www.cisco.com/c/en/us/td/docs/wireless/controller/8-10/config-guide/b_cg810/ports_and_interfaces.html) — Restrictions on Link Aggregation; Configuring Neighbor Devices to Support Link Aggregation

---

## CCNA10-036 · Network Access

Objectives: 2.7 · single · Applied

A FlexConnect AP’s switch trunk carries management and two local client VLANs. A maintenance change removes the management VLAN but retains both client VLANs. Why is checking only client VLAN admission an incomplete acceptance test?

- **A.** The AP still needs its management/controller connectivity for its configured control functions.
- **B.** The WLC console port transparently replaces the missing management VLAN.
- **C.** Management traffic always changes itself to any allowed client VLAN.
- **D.** Each client’s DHCP lease stores a backup of the AP control tunnel.

**Answer: A**

Verify each traffic class carried by the shared physical attachment. A change can leave user VLANs intact while removing a separate control dependency.

**Option explanations**

- **A:** A surviving local client VLAN does not prove the AP’s management path remains available.
- **B:** There is no such automatic Ethernet-path replacement.
- **C:** The configured management classification does not automatically follow the allowed list.
- **D:** Client addressing does not preserve AP controller state.

**Further reading**

- [Cisco Wireless Controller Configuration Guide, Release 8.10 — FlexConnect](https://www.cisco.com/c/en/us/td/docs/wireless/controller/8-10/config-guide/b_cg810/flexconnect.html) — Configuring the Switch at a Remote Site; Configuring an Access Point for FlexConnect (GUI)
- [Cisco Wireless Controller Configuration Guide, Release 8.10 — AP Connectivity to Controller](https://www.cisco.com/c/en/us/td/docs/wireless/controller/8-10/config-guide/b_cg810/ap_connectivity_to_cisco_wlc.html) — CAPWAP

---

## CCNA10-037 · Network Access

Objectives: 2.8 · single · Applied

An emergency console session works, but remote SSH management fails after the management VLAN was removed from an uplink. Which interpretation separates the evidence correctly?

- **A.** Working console proves the management VLAN is forwarding end to end.
- **B.** The console cable is carrying all remote IP traffic successfully.
- **C.** Local console access can remain healthy while the independent in-band IP path is broken.
- **D.** SSH must therefore have been replaced by Telnet automatically.

**Answer: C**

Use the console to inspect and repair the failed IP attachment. Local access success does not validate remote-management transport.

**Option explanations**

- **A:** Console access bypasses that VLAN path.
- **B:** A direct console is not the management VLAN’s general forwarding path.
- **C:** The two access methods do not share every transport dependency.
- **D:** Loss of reachability does not automatically change the configured protocol.

**Further reading**

- [Cisco Wireless Controller Configuration Guide, Release 8.10 — Administration of Controller](https://www.cisco.com/c/en/us/td/docs/wireless/controller/8-10/config-guide/b_cg810/administration_of_cisco_wlc.html) — Logging on to the Controller CLI; Enabling Web and Secure Web Modes (GUI); Enabling Web and Secure Web Modes (CLI)
- [VLAN Configuration Guide, Cisco IOS XE 17.15.x — Configuring VLAN Trunks](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst9300/software/release/17-15/configuration_guide/vlan/b_1715_vlan_9300_cg/configuring_vlan_trunks.html) — Allowed VLANs on a Trunk; Configuring the Native VLAN for Untagged Traffic

---

## CCNA10-038 · Network Access

Objectives: 2.9 · single · Applied

A Catalyst 9800 WLAN uses 802.1X. Its Security GUI points to authentication method list Guest-AAA, but the approved staff RADIUS group is referenced by Staff-AAA. Both servers are reachable, and guest users succeed while staff users are rejected. Which binding should be reviewed first?

| GUI relationship | Current mapping |
| --- | --- |
| Staff WLAN Authentication List | Guest-AAA |
| Guest-AAA server group | Guest-RADIUS |
| Staff-AAA server group | Staff-RADIUS |
| Approved staff group | Staff-RADIUS |

- **A.** The controller’s browser bookmark name
- **B.** The SSID broadcast checkbox only
- **C.** The WLAN’s authentication-list selection should reference the approved Staff-AAA policy.
- **D.** The AP’s PoE power class

**Answer: C**

Reachability alone is insufficient if the WLAN uses the wrong authentication policy. Trace the selected list to its intended server group.

**Option explanations**

- **A:** A bookmark label does not alter WLAN authentication.
- **B:** Broadcasting the name does not select the RADIUS policy.
- **C:** The applied list currently sends authentication through the guest policy chain.
- **D:** Server-specific authentication behavior does not establish a power problem.

**Further reading**

- [Configure FlexConnect with Authentication on Catalyst 9800 WLC](https://www.cisco.com/c/en/us/support/docs/wireless/catalyst-9800-series-wireless-controllers/213921-flexconnect-configuration-with-central-a.html) — Background Information; Policy Profile Configuration

---

## CCNA10-039 · Network Access

Objectives: 2.9 · single · Applied

An AireOS GUI change has been applied and saved, but the client is still connected to a different similarly named SSID on another controller. Which verification best prevents attributing the wrong result to the edited WLAN?

- **A.** Confirm the client’s actual SSID/AP/controller association before comparing its behavior with the edited profile.
- **B.** Assume similar SSID names mean both controllers share one profile.
- **C.** Change the QoS profile repeatedly until any nearby client reconnects.
- **D.** Use the management hostname as proof of every client association.

**Answer: A**

Acceptance testing must connect the observed client to the effective WLAN configuration. Otherwise a valid configuration change can be judged using unrelated traffic.

**Option explanations**

- **A:** The tested client must use the configuration object whose behavior is being evaluated.
- **B:** Names do not establish shared configuration or actual association.
- **C:** That does not identify which service the test client is using.
- **D:** A controller identity does not show that this client is attached to it.

**Further reading**

- [Cisco Wireless Controller Configuration Guide, Release 8.10 — WLANs](https://www.cisco.com/c/en/us/td/docs/wireless/controller/8-10/config-guide/b_cg810/wlans.html) — Prerequisites for WLANs; Enabling and Disabling WLANs (GUI); Editing WLAN SSID or Profile Name for WLANs (GUI)
- [Configure FlexConnect with Authentication on Catalyst 9800 WLC](https://www.cisco.com/c/en/us/support/docs/wireless/catalyst-9800-series-wireless-controllers/213921-flexconnect-configuration-with-central-a.html) — Background Information; Policy Profile Configuration

---

## CCNA10-040 · Network Access

Objectives: 2.9 · multiple · Challenge

An AireOS WLAN GUI applies the sustained TCP rate limits below. Five clients on the same AP radio each offer 3,000 Kb/s upstream. Both shown limits are upstream limits for this WLAN on that AP radio. Assume both limits are enforced independently, ignore temporary bursts, and assume all other capacity is sufficient. Which TWO limits constrain the delivered sustained traffic? Select TWO.

| GUI sustained upstream TCP limit | Value |
| --- | --- |
| Per client | 2,000 Kb/s |
| Per SSID on this AP radio | 8,000 Kb/s |
| Clients on this AP radio offering 3,000 Kb/s each | 5 |

- **A.** The five clients can sustain 10,000 Kb/s together because five times 2,000 equals 10,000.
- **B.** Every client can sustain 3,000 Kb/s because the SSID limit is larger.
- **C.** The five clients together are limited to at most 8,000 Kb/s upstream on this WLAN and AP radio.
- **D.** Each client is limited to at most 2,000 Kb/s.

**Answer: C, D**

Interpret the scope of each GUI rate field. Both a per-client ceiling and a per-SSID ceiling on the AP radio constrain the specified upstream traffic; neither promises equal allocation during contention.

**Option explanations**

- **A:** That calculation exceeds the independent 8,000-Kb/s per-SSID limit.
- **B:** An aggregate cap does not override the smaller individual-client cap.
- **C:** The per-SSID limit on this AP radio applies in addition to each client’s upstream cap.
- **D:** The per-client sustained setting caps a single client below its offered rate.

**Further reading**

- [Cisco Wireless Controller Configuration Guide, Release 8.10 — Wireless Quality of Service](https://www.cisco.com/c/en/us/td/docs/wireless/controller/8-10/config-guide/b_cg810/wireless_quality_of_service.html) — QoS Profiles; Configuring QoS Profiles (GUI); Assigning a QoS Profile to a WLAN (GUI)

---

## CCNA10-041 · IP Connectivity

Objectives: 3.2.a, 3.2.b, 3.2.c · multiple · Challenge

All candidates in this change review are usable. The static and OSPF /24 refer to the identical destination prefix; OSPF routes are intra-area. Which TWO results follow after normal route selection? Select two.

```text
Candidates:
0.0.0.0/0       static, AD 1,   next hop 192.0.2.1
10.222.16.0/24   static, AD 160, next hop 192.0.2.5
10.222.16.0/24   OSPF,  AD 110, cost 80, next hop 192.0.2.9
10.222.16.0/25   OSPF,  AD 110, cost 90, next hop 192.0.2.13
```

- **A.** The distance-1 default suppresses all three specific candidates.
- **B.** The static /24 wins because its metric is numerically zero.
- **C.** Packets to 10.222.16.200 use the OSPF /24 next hop.
- **D.** Packets to 10.222.16.20 use the /25 next hop.

**Answer: C, D**

First resolve the two competitors for the /24. Then compare the installed destination prefixes for each packet; the /25 and default remain separate destinations.

**Option explanations**

- **A:** Routes to different prefixes are not discarded merely because a default has lower distance.
- **B:** Metrics from these different sources do not replace administrative-distance comparison.
- **C:** OSPF distance 110 beats static distance 160 for the /24, and .200 misses the /25.
- **D:** The /25 is a more specific installed match for .20.

**Further reading**

- [Configure Route Selection for Routers](https://www.cisco.com/c/en/us/support/docs/ip/enhanced-interior-gateway-routing-protocol-eigrp/8651-21.html) — Build the Routing Table; Make Forwarding Decisions

---

## CCNA10-042 · IP Connectivity

Objectives: 3.1.d, 3.1.g · single · Applied

A forwarding record says next hop 192.0.2.9 and gateway of last resort 192.0.2.1. An operator assumes this is inconsistent. The selected destination has its own more specific route. Which explanation resolves the apparent conflict?

- **A.** The two addresses must be aliases of the same interface.
- **B.** The selected next hop must be the packet’s original source.
- **C.** Every route must use the gateway-of-last-resort address.
- **D.** A specific route can use a different next hop from the default.

**Answer: D**

The two fields describe different scopes: one selected route and the fallback route. Their next hops can legitimately differ.

**Option explanations**

- **A:** Different forwarding next hops do not imply aliasing.
- **B:** Next-hop forwarding is not determined that way.
- **C:** That would incorrectly force all destinations onto the default path.
- **D:** The gateway of last resort applies only when a more specific usable route does not match.

**Further reading**

- [Configure Route Selection for Routers](https://www.cisco.com/c/en/us/support/docs/ip/enhanced-interior-gateway-routing-protocol-eigrp/8651-21.html) — Build the Routing Table; Make Forwarding Decisions

---

## CCNA10-043 · IP Connectivity

Objectives: 3.3.a · single · Applied

A dual-stack router has an IPv4 default and no IPv6 default or other route for 2001:db8:ffff::7. IPv6 forwarding is enabled. Why does a working IPv4 Internet test not establish IPv6 reachability?

- **A.** The IPv4 default does not supply an IPv6 destination route.
- **B.** IPv6 unicast routing converts every unresolved IPv6 packet into IPv4.
- **C.** The IPv4 route is automatically translated into ::/0 after a successful ping.
- **D.** All IPv6 destinations require individual /128 routes.

**Answer: A**

Test and verify both address families independently. A working IPv4 route does not fill a missing IPv6 forwarding entry.

**Option explanations**

- **A:** Each address family needs appropriate forwarding information.
- **B:** Enabling routing does not enable an automatic translation mechanism.
- **C:** A ping does not create an IPv6 default from IPv4 configuration.
- **D:** Network and default IPv6 routes can cover many destinations.

**Further reading**

- [IPv6 Routing: Static Routing — Cisco IOS XE 17.x](https://www.cisco.com/c/en/us/td/docs/routers/ios/config/17-x/ip-routing/b-ip-routing/m_ip6-route-static-xe.html) — Recursive Static Routes; Fully Specified Static Routes; Floating Static Routes

---

## CCNA10-044 · IP Connectivity

Objectives: 3.3.b, 3.1.c · single · Applied

An engineer copied the ACL wildcard 0.0.3.255 into the mask field of an IPv4 static-route command for 10.124.12.0/22. Which mask belongs in that route command?

- **A.** 0.0.3.255
- **B.** 255.255.255.252
- **C.** 255.255.252.0
- **D.** 255.255.0.0

**Answer: C**

An IPv4 route command takes a subnet mask; an ACL can take a wildcard. The two values describe different matching conventions.

**Option explanations**

- **A:** That is the ACL wildcard, not the required contiguous network mask.
- **B:** This is /30 and would cover only four addresses.
- **C:** A /22 network mask has 22 one bits and is the inverse of the cited wildcard.
- **D:** This is /16 and is broader than the required /22.

**Further reading**

- [RFC 1812: Requirements for IP Version 4 Routers](https://www.rfc-editor.org/rfc/rfc1812.html) — 5.2.4 Determining the Next Hop Address

---

## CCNA10-045 · IP Connectivity

Objectives: 3.3.c, 3.2.a · single · Applied

A narrow maintenance route sends 2001:db8:90::99/128 through a test router. The normal 2001:db8:90::/64 remains installed through the production router. Which traffic is affected by the exception?

- **A.** Every packet sourced by 2001:db8:90::99, regardless of destination.
- **B.** All destinations beginning with 2001:db8:90.
- **C.** All IPv4 packets for the same physical server.
- **D.** Traffic whose destination is exactly 2001:db8:90::99.

**Answer: D**

The host route changes one destination lookup. It does not express an endpoint-wide or source-address forwarding policy.

**Option explanations**

- **A:** The configured route is destination-based, not source policy.
- **B:** The /128 exception does not cover the entire /64.
- **C:** The IPv6 route does not create an IPv4 exception.
- **D:** Only that destination matches the /128.

**Further reading**

- [IPv6 Routing: Static Routing — Cisco IOS XE 17.x](https://www.cisco.com/c/en/us/td/docs/routers/ios/config/17-x/ip-routing/b-ip-routing/m_ip6-route-static-xe.html) — Recursive Static Routes; Fully Specified Static Routes; Floating Static Routes

---

## CCNA10-046 · IP Connectivity

Objectives: 3.3.d · single · Applied

A primary static route has been removed from the RIB. A configured floating static has a preferred-enough distance to be selected, but its directly attached next-hop address has been mistyped into an unrelated, unresolved subnet. Which repair is necessary?

- **A.** Wait for a host’s ARP entry for the final remote destination to expire.
- **B.** Correct the backup next-hop address so it resolves over the intended surviving link.
- **C.** Decrease the failed primary’s configured metric only.
- **D.** Raise the backup distance to 255 to force installation.

**Answer: B**

Preference cannot compensate for invalid forwarding information. Test backup next-hop resolution before relying on a failure-triggered switchover.

**Option explanations**

- **A:** The fault is the router’s backup next-hop addressing, not that host cache.
- **B:** The backup candidate must be usable as well as appropriately ranked.
- **C:** That does not fix the backup’s unresolved next hop.
- **D:** Distance 255 prevents normal route installation rather than forcing it.

**Further reading**

- [Configure Route Selection for Routers](https://www.cisco.com/c/en/us/support/docs/ip/enhanced-interior-gateway-routing-protocol-eigrp/8651-21.html) — Build the Routing Table; Make Forwarding Decisions

---

## CCNA10-047 · IP Connectivity

Objectives: 3.3.b, 3.1.d · single · Applied

An IPv6 router has two adjacent peers on the same Ethernet segment. One leads to the archive subnet and the other to a development subnet. Why is specifying only that exit interface insufficient to identify the intended off-link archive path?

- **A.** Ethernet permits only one IPv6 router per subnet.
- **B.** The interface identifies a shared link, but not which router should receive off-link traffic.
- **C.** An exit interface automatically selects the highest peer link-local address.
- **D.** The interface must be replaced by a VLAN name in every IPv6 route.

**Answer: B**

Shared-link reachability and next-router choice are separate facts. A fully specified static makes that choice explicit.

**Option explanations**

- **A:** Multiple IPv6 routers can share an Ethernet segment.
- **B:** A next-hop address resolves the intended peer on that multiaccess link.
- **C:** No such route-selection rule is specified.
- **D:** A VLAN name is not the missing next-hop identity.

**Further reading**

- [IPv6 Routing: Static Routing — Cisco IOS XE 17.x](https://www.cisco.com/c/en/us/td/docs/routers/ios/config/17-x/ip-routing/b-ip-routing/m_ip6-route-static-xe.html) — Recursive Static Routes; Fully Specified Static Routes; Floating Static Routes

---

## CCNA10-048 · IP Connectivity

Objectives: 3.1.a, 3.1.d, 3.1.e, 3.1.f · matching · Applied

A troubleshooting worksheet has four fields. Match each entered value with the field it belongs to for an OSPF route. Use each field once.

1. O
2. 110, the first value inside [110/37]
3. 37, the second value inside [110/37]
4. 192.0.2.42, after the word via

- **A.** Administrative distance
- **B.** OSPF metric
- **C.** Route source code
- **D.** Next-hop address

**Answer: 1 → C; 2 → A; 3 → B; 4 → D**

A route’s protocol label, preference, cost and neighbor address serve distinct purposes. Record each in the correct worksheet field.

**Option explanations**

- **A:** This is the source-preference value used for an exact prefix.
- **B:** This is the OSPF path cost recorded for the route.
- **C:** A routing-table letter identifies the route’s source.
- **D:** This identifies the next router along the selected path.

**Further reading**

- [Configure Route Selection for Routers](https://www.cisco.com/c/en/us/support/docs/ip/enhanced-interior-gateway-routing-protocol-eigrp/8651-21.html) — Build the Routing Table; Make Forwarding Decisions

---

## CCNA10-049 · IP Connectivity

Objectives: 3.1.b, 3.1.c, 3.3.b · single · Challenge

A router must forward exactly the contiguous networks 172.23.120.0/24 through 172.23.123.0/24 to one reachable neighbor. The operator wants one static network route and no extra /24s. Which destination prefix fits?

- **A.** 172.23.122.0/23
- **B.** 172.23.120.0/21
- **C.** 172.23.120.0/22
- **D.** 172.23.120.0/23

**Answer: C**

Four aligned /24s form one /22. Check the starting boundary as well as the number of address blocks.

**Option explanations**

- **A:** This covers only 122–123 and misses the first two LANs.
- **B:** The /21 covers 120–127, including four unwanted /24s.
- **C:** The aligned /22 covers precisely third octets 120–123.
- **D:** The /23 covers only 120–121.

**Further reading**

- [RFC 1812: Requirements for IP Version 4 Routers](https://www.rfc-editor.org/rfc/rfc1812.html) — 5.2.4 Determining the Next Hop Address

---

## CCNA10-050 · IP Connectivity

Objectives: 3.4, 3.2.c · single · Applied

A link is upgraded, and the OSPF reference bandwidth is also changed. Its interface configuration still contains ip ospf cost 45. With that explicit override in effect, what cost should this interface advertise?

- **A.** The neighbor’s interface priority.
- **B.** 45
- **C.** A new automatic value, because any speed change removes the override.
- **D.** Zero, because the upgraded link is faster than the old reference.

**Answer: B**

Inspect effective configuration before applying an automatic-cost formula. The explicit override remains the deciding setting.

**Option explanations**

- **A:** Election priority and path cost are different values.
- **B:** The explicit interface cost overrides automatic bandwidth-derived calculation.
- **C:** A speed change does not delete the explicit cost command.
- **D:** The override still specifies 45, not zero.

**Further reading**

- [Configuring OSPF — IP Routing: OSPF Configuration Guide](https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/iproute_ospf/configuration/xe-16/iro-xe-16-book/iro-cfg.html) — Enabling OSPF; Configuring OSPF Interface Parameters

---

## CCNA10-051 · IP Connectivity

Objectives: 3.4.a · single · Applied

On R1, an OSPF neighbor is repeatedly Full, then Down after its dead timer expires, then Full again. What does this evidence justify?

- **A.** The dead timer proves the physical cable is the only possible cause.
- **B.** The OSPF process ID must be identical on both ends.
- **C.** Valid Hellos are intermittently not being received within the dead interval.
- **D.** The area IDs have permanently mismatched since first deployment.

**Answer: C**

The state transition identifies what timed out, not the unique root cause. Correlate neighbor events with interface, filtering and device evidence.

**Option explanations**

- **A:** Filtering, control-plane load and other causes can also interrupt accepted Hellos.
- **B:** Local process-number agreement is not required.
- **C:** The timed loss reflects a lapse in accepted neighbor communication.
- **D:** Repeated Full states contradict that simple permanent-mismatch explanation.

**Further reading**

- [Understand OSPF Neighbor States](https://www.cisco.com/c/en/us/support/docs/ip/open-shortest-path-first-ospf/13685-13.html) — OSPF Neighbor States

---

## CCNA10-052 · IP Connectivity

Objectives: 3.4.a · single · Applied

A new OSPF neighbor reaches Full, but an operator cannot ping the router ID address. The explicit router ID was never assigned to any interface, and routing to the actual interface addresses works. Which interpretation is justified?

- **A.** Full adjacency can be valid even though that identifier is not a reachable host address.
- **B.** The router ID must be learned through DHCP before adjacency can work.
- **C.** A failed ping to the identifier proves the Full state is impossible.
- **D.** The neighbor must change every interface to the router ID address.

**Answer: A**

Choose a test destination that is intended to be reachable. A protocol identifier printed as an IPv4-style value does not necessarily name a pingable interface.

**Option explanations**

- **A:** The explicit router ID identifies the protocol speaker; it need not be a configured interface destination.
- **B:** OSPF imposes no such DHCP prerequisite.
- **C:** The adjacency exchanges use the actual link addresses.
- **D:** That would incorrectly conflate identity with interface addressing.

**Further reading**

- [Configuring OSPF — IP Routing: OSPF Configuration Guide](https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/iproute_ospf/configuration/xe-16/iro-xe-16-book/iro-cfg.html) — Enabling OSPF; Configuring OSPF Interface Parameters
- [RFC 2328: OSPF Version 2](https://www.rfc-editor.org/rfc/rfc2328.html) — 9.4 Electing the Designated Router; 10 The Neighbor Data Structure; 16 Calculation of the routing table

---

## CCNA10-053 · IP Connectivity

Objectives: 3.4.b · single · Applied

On a point-to-point OSPF link, R1 loses its sole neighbor R2 and no alternate path exists to R2’s LAN. After failure detection and route recalculation, which outcome is expected?

- **A.** R1 elects itself DR to recreate reachability to R2’s LAN.
- **B.** The OSPF route relying solely on R2 is withdrawn.
- **C.** R1 automatically assigns R2’s LAN addresses to itself.
- **D.** The route stays usable because its last metric is still known.

**Answer: B**

Convergence updates forwarding to reflect the remaining topology. When no alternate path exists, correct convergence can mean route removal.

**Option explanations**

- **A:** This network type has no DR, and an election cannot recreate the failed path.
- **B:** No surviving OSPF path exists under the stated conditions.
- **C:** OSPF failure handling does not move that host subnet configuration.
- **D:** A stale metric is insufficient when the only path has failed.

**Further reading**

- [RFC 2328: OSPF Version 2](https://www.rfc-editor.org/rfc/rfc2328.html) — 9.4 Electing the Designated Router; 10 The Neighbor Data Structure; 16 Calculation of the routing table

---

## CCNA10-054 · IP Connectivity

Objectives: 3.4.c · single · Applied

R1 is DR, R2 is BDR and R3 is DROTHER on a stable OSPF broadcast LAN. An operator lowers only R1’s nonzero interface priority below R3’s without any failure or interface/process reset. Which result should be expected immediately?

- **A.** The DR role moves to whichever device has the lowest route metric.
- **B.** All neighbors must transition to Down when a priority value changes.
- **C.** The existing DR remains DR; priority changes do not force a preemptive election.
- **D.** R3 instantly becomes DR and R1 becomes BDR.

**Answer: C**

Design priority before an election, and plan any role-changing maintenance explicitly. A configuration change alone is not evidence that the operational role changed.

**Option explanations**

- **A:** Path cost does not choose the DR role.
- **B:** The change does not itself require every adjacency to fail.
- **C:** A healthy elected DR is not displaced merely by changing relative priorities.
- **D:** The election does not use that immediate preemptive behavior.

**Further reading**

- [RFC 2328: OSPF Version 2](https://www.rfc-editor.org/rfc/rfc2328.html) — 9.4 Electing the Designated Router; 10 The Neighbor Data Structure; 16 Calculation of the routing table

---

## CCNA10-055 · IP Connectivity

Objectives: 3.4.d · single · Applied

Two routers have explicit, unique OSPF router IDs and already participate in area 0. Their hostnames are changed during an inventory cleanup; no router-id command or process restart occurs. What router-ID change should the inventory system expect from the hostname change alone?

- **A.** None.
- **B.** Both IDs become 0.0.0.0 until the next Hello.
- **C.** Both IDs become the first resolved DNS address of each new hostname.
- **D.** Both IDs increment by one to indicate a configuration revision.

**Answer: A**

Names used by operators and identifiers used by OSPF are separate attributes. Inventory automation should not infer a router-ID change from renaming.

**Option explanations**

- **A:** The explicit router-ID settings are independent of hostname text.
- **B:** Renaming the device does not invalidate the existing explicit identity.
- **C:** The explicit configuration is not replaced through hostname DNS resolution.
- **D:** Router IDs are not revision counters.

**Further reading**

- [Configuring OSPF — IP Routing: OSPF Configuration Guide](https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/iproute_ospf/configuration/xe-16/iro-xe-16-book/iro-cfg.html) — Enabling OSPF; Configuring OSPF Interface Parameters

---

## CCNA10-056 · IP Connectivity

Objectives: 3.4, 3.2.c · multiple · Applied

Three valid OSPF intra-area paths to one LAN have total costs 18, 18 and 22. Equal-cost multipath is enabled with a maximum of four paths. Which TWO statements describe the selected paths? Select two.

- **A.** The cost-22 path is not selected merely because a fourth slot is available.
- **B.** The two cost-18 paths are eligible together.
- **C.** The path with the highest neighbor router ID wins even though ECMP is enabled.
- **D.** All three paths must be installed because four are allowed.

**Answer: A, B**

The maximum is a capacity limit, not a target number of routes. Eligible paths must satisfy the protocol’s equal-cost selection conditions.

**Option explanations**

- **A:** A maximum path count does not make unequal-cost paths equal.
- **B:** They tie for the lowest intra-area cost and fit the configured path limit.
- **C:** That statement incorrectly discards the equal-cost multipath condition.
- **D:** The metric condition must also be met.

**Further reading**

- [Configure Route Selection for Routers](https://www.cisco.com/c/en/us/support/docs/ip/enhanced-interior-gateway-routing-protocol-eigrp/8651-21.html) — Build the Routing Table; Make Forwarding Decisions
- [RFC 2328: OSPF Version 2](https://www.rfc-editor.org/rfc/rfc2328.html) — 9.4 Electing the Designated Router; 10 The Neighbor Data Structure; 16 Calculation of the routing table

---

## CCNA10-057 · IP Connectivity

Objectives: 3.4.a · single · Applied

A team compares an OSPF neighbor table and routing table captured ten minutes apart during an outage. The first shows Full; the second lacks the expected route. What is the strongest next step before declaring the outputs contradictory?

- **A.** Assume the missing prefix uses the neighbor’s router ID as its mask.
- **B.** Collect time-aligned neighbor and route states and identify the prefix’s actual source.
- **C.** Delete the OSPF process because the two observations cannot coexist.
- **D.** Replace all static routes with defaults to force agreement.

**Answer: B**

An adjacency and a destination route are different observations. Align timestamps and follow the particular prefix before changing configuration.

**Option explanations**

- **A:** Router ID does not determine prefix masks.
- **B:** State may have changed, and Full does not imply every expected prefix was advertised.
- **C:** They can coexist at different times or when the prefix is not supplied.
- **D:** That is unrelated to establishing comparable evidence.

**Further reading**

- [Understand OSPF Neighbor States](https://www.cisco.com/c/en/us/support/docs/ip/open-shortest-path-first-ospf/13685-13.html) — OSPF Neighbor States
- [Configure Route Selection for Routers](https://www.cisco.com/c/en/us/support/docs/ip/enhanced-interior-gateway-routing-protocol-eigrp/8651-21.html) — Build the Routing Table; Make Forwarding Decisions

---

## CCNA10-058 · IP Connectivity

Objectives: 3.4, 3.2.c · single · Challenge

Only two OSPF intra-area paths reach a destination. Path A costs 6 + 6 + 1; Path B costs 4 + 4 + 4 + 1. All terms are outgoing costs including the destination LAN. Both next hops are valid, and maximum-paths is 2. What is expected?

- **A.** Both paths can be installed at cost 13.
- **B.** Only Path A, because it has fewer routed links.
- **C.** Only Path B, because its first cost is lower.
- **D.** Neither, because different path lengths cannot have equal OSPF metrics.

**Answer: A**

6 + 6 + 1 and 4 + 4 + 4 + 1 both equal 13. The stated multipath limit permits both equal-cost next hops.

**Option explanations**

- **A:** The two different hop sequences produce equal total costs.
- **B:** OSPF compares total cost rather than the count of listed links.
- **C:** The complete sums are equal.
- **D:** Unequal hop counts can yield the same summed cost.

**Further reading**

- [RFC 2328: OSPF Version 2](https://www.rfc-editor.org/rfc/rfc2328.html) — 9.4 Electing the Designated Router; 10 The Neighbor Data Structure; 16 Calculation of the routing table

---

## CCNA10-059 · IP Connectivity

Objectives: 3.3.b, 3.2.b · multiple · Applied

An OSPF route used for a remote management subnet is replaced by a valid static route of distance 1 for the identical prefix. OSPF neighbors remain Full and the OSPF candidate remains valid. Which TWO statements explain the observations? Select two.

- **A.** The OSPF adjacency can stay Full while a different route source is selected.
- **B.** The OSPF route’s prefix became longer when the static was entered.
- **C.** The static source won local route preference for that exact prefix.
- **D.** The router compares the textual command order before distance.

**Answer: A, C**

Route installation can change without any adjacency failure. Check newly configured route sources before treating every path change as a protocol outage.

**Option explanations**

- **A:** Adjacency state and local selection among route sources are separate decisions.
- **B:** Both routes still refer to the identical prefix.
- **C:** Default static distance 1 is preferred to default OSPF distance 110.
- **D:** The described normal route selection is not based on command text position.

**Further reading**

- [Configure Route Selection for Routers](https://www.cisco.com/c/en/us/support/docs/ip/enhanced-interior-gateway-routing-protocol-eigrp/8651-21.html) — Build the Routing Table; Make Forwarding Decisions

---

## CCNA10-060 · IP Connectivity

Objectives: 3.3.a, 3.3.d · single · Applied

A maintenance plan lowers a backup static default’s distance from 210 to 5. The primary default is a valid static with distance 1. All next hops resolve and no other defaults exist. What changes in the selected default immediately?

- **A.** The two defaults become equal-cost automatically.
- **B.** The primary becomes invalid because another distance changed.
- **C.** The backup becomes primary because its distance is now one digit.
- **D.** Nothing: the distance-1 primary remains preferred.

**Answer: D**

Compare the resulting values, not just whether one value decreased. Lowering a backup distance need not cross the primary’s preference threshold.

**Option explanations**

- **A:** Their administrative distances remain different.
- **B:** Changing the backup’s ranking does not invalidate the primary path.
- **C:** Digit count has no route-selection meaning; compare numeric values.
- **D:** The modified backup still has a higher distance for the same default prefix.

**Further reading**

- [Configure Route Selection for Routers](https://www.cisco.com/c/en/us/support/docs/ip/enhanced-interior-gateway-routing-protocol-eigrp/8651-21.html) — Build the Routing Table; Make Forwarding Decisions

---

## CCNA10-061 · IP Connectivity

Objectives: 3.5 · single · Applied

Two routers provide a healthy virtual gateway at 10.25.0.1. A newly installed printer was accidentally assigned that same address. Clients intermittently learn the printer’s MAC for their gateway IP. Which change addresses this fault while retaining the virtual-gateway design?

- **A.** Give the printer an unused non-gateway address and verify that gateway ARP mappings recover.
- **B.** Point every client at the printer as its permanent gateway.
- **C.** Change only the printer’s DNS name while keeping its IP address.
- **D.** Increase the standby router’s OSPF interface cost.

**Answer: A**

FHRP coordinates its participating routers, not an unrelated device misusing the virtual address. Keep the gateway address reserved and verify the resulting Layer 2 mapping.

**Option explanations**

- **A:** The printer conflicts with the virtual gateway identity on the LAN.
- **B:** The printer does not provide the intended redundant routing service.
- **C:** A new name does not remove the duplicate IP claim.
- **D:** Path cost does not remove another device claiming the gateway IP.

**Further reading**

- [RFC 9568: Virtual Router Redundancy Protocol (VRRP) Version 3 for IPv4 and IPv6](https://www.rfc-editor.org/rfc/rfc9568.html) — 1 Introduction; 2 Required Features; 6 Protocol State Machine
- [RFC 5227: IPv4 Address Conflict Detection](https://www.rfc-editor.org/rfc/rfc5227.html) — 1 Introduction; 2.4 Ongoing Address Conflict Detection and Address Defense

---

## CCNA10-062 · IP Connectivity

Objectives: 3.5 · single · Applied

The standby gateway passes a local-interface ping test before a failover exercise. Which additional test is most useful for proving it can provide the required service after takeover?

- **A.** Verify only that the virtual IP is documented in a spreadsheet.
- **B.** Verify only that its console banner matches the primary.
- **C.** Verify only that its chassis serial number appears in inventory.
- **D.** Verify client traffic reaches the required remote subnet through the active replacement.

**Answer: D**

A local ping checks only a small part of the dependency chain. Test the service path and confirm which gateway carries it.

**Option explanations**

- **A:** A documented address does not prove operational ownership or forwarding.
- **B:** A banner is unrelated to transit forwarding capability.
- **C:** Inventory presence does not establish routed service.
- **D:** This exercises the client-facing gateway and its onward forwarding path.

**Further reading**

- [RFC 9568: Virtual Router Redundancy Protocol (VRRP) Version 3 for IPv4 and IPv6](https://www.rfc-editor.org/rfc/rfc9568.html) — 1 Introduction; 2 Required Features; 6 Protocol State Machine

---

## CCNA10-063 · IP Connectivity

Objectives: 3.5 · single · Applied

After a first-hop redundancy transition, the client keeps the same virtual gateway IP and traffic resumes. Which inference is unsupported by that result alone?

- **A.** The client did not need a different configured gateway IP for this transition.
- **B.** Every TCP session and application transaction was preserved without loss.
- **C.** The virtual gateway identity reduced the need for per-host reconfiguration.
- **D.** A surviving gateway path became available to the client.

**Answer: B**

Different acceptance criteria require different evidence. Gateway recovery is useful, while transport and application continuity need their own observations.

**Option explanations**

- **A:** The unchanged configuration and resumed traffic support that observation.
- **B:** Basic gateway reachability does not prove session-state synchronization or application continuity.
- **C:** That is the purpose demonstrated by the unchanged gateway setting.
- **D:** Resumed off-subnet traffic is consistent with a usable surviving path.

**Further reading**

- [RFC 9568: Virtual Router Redundancy Protocol (VRRP) Version 3 for IPv4 and IPv6](https://www.rfc-editor.org/rfc/rfc9568.html) — 1 Introduction; 2 Required Features; 6 Protocol State Machine

---

## CCNA10-064 · IP Connectivity

Objectives: 3.1.b, 3.2.a · single · Applied

A router has usable installed routes for 10.9.0.0/16 and 10.9.64.0/18, but no default. Which destination is outside both routes and therefore has no match?

- **A.** 10.9.0.10
- **B.** 10.9.200.1
- **C.** 10.9.127.254
- **D.** 10.10.64.1

**Answer: D**

Check every applicable prefix before deciding there is no route. Missing the most specific entry does not mean missing all covering entries.

**Option explanations**

- **A:** It matches the /16 even though it misses the /18.
- **B:** It misses the /18 but still matches the /16.
- **C:** It lies in the /18 block 64–127.
- **D:** Its second octet is 10 rather than 9, so neither prefix covers it.

**Further reading**

- [RFC 1812: Requirements for IP Version 4 Routers](https://www.rfc-editor.org/rfc/rfc1812.html) — 5.2.4 Determining the Next Hop Address

---

## CCNA10-065 · IP Connectivity

Objectives: 3.3.b, 3.4.a · single · Applied

An engineer adds a static route on R1 and expects R2 to learn it through their existing OSPF adjacency. No redistribution, default origination, or other advertisement mechanism is configured, and the prefix is not an OSPF-enabled connected network. What should the engineer expect?

- **A.** The static route remains local to R1 unless an appropriate advertisement mechanism is configured.
- **B.** R2 automatically copies every static command from R1 after Full state.
- **C.** The adjacency must fail whenever R1 has a static route.
- **D.** R2 learns it as a connected route because R1 knows it.

**Answer: A**

Local route knowledge and protocol advertisement are separate steps. Full adjacency does not imply that every local routing-table entry is exported.

**Option explanations**

- **A:** A static command does not by itself originate that destination into OSPF.
- **B:** OSPF exchanges routing information according to configuration, not the neighbor’s entire configuration file.
- **C:** Static and OSPF routing can coexist.
- **D:** Connected routes describe locally attached networks.

**Further reading**

- [Configuring OSPF — IP Routing: OSPF Configuration Guide](https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/iproute_ospf/configuration/xe-16/iro-xe-16-book/iro-cfg.html) — Enabling OSPF; Configuring OSPF Interface Parameters

---

## CCNA10-066 · IP Services

Objectives: 4.1 · single · Challenge

A NAT rule should translate traffic sourced by subnet 10.106.0.0/24. An engineer tests it using a ping generated by the router itself with source address 198.51.100.2, which is outside that subnet. No new translation appears. Which test is better evidence for the intended rule?

- **A.** Generate traffic from an eligible inside host through the NAT inside-to-outside path.
- **B.** Ping only the router's own inside interface from the router itself.
- **C.** Repeat the same router-originated ping indefinitely without changing its source.
- **D.** Inspect only the DNS cache for the server's name.

**Answer: A**

A verification test must exercise the feature's matching conditions. The original probe does not match the specified inside source subnet, so its empty translation result does not demonstrate failure of the intended host rule.

**Option explanations**

- **A:** This exercises the rule's source match and the intended transit direction.
- **B:** That does not exercise the intended transit translation path.
- **C:** It still does not match the rule's eligible inside subnet.
- **D:** DNS cache contents do not verify address translation for the client flow.

**Further reading**

- [IP Addressing Configuration Guide, Cisco IOS XE 17.x — Configuring NAT for IP Address Conservation](https://www.cisco.com/c/en/us/td/docs/routers/ios/config/17-x/ip-addressing/b-ip-addressing/m_iadnat-addr-consv-xe.html) — Inside source address translation; static and dynamic translations; monitoring NAT

---

## CCNA10-067 · IP Services

Objectives: 4.1 · multiple · Applied

A basic dynamic NAT pool is configured with start address 203.0.113.100 and end address 203.0.113.109, mask 255.255.255.0, without overload. No mappings are active. Which two statements about the pool are correct? Select two.

- **A.** Basic dynamic NAT allocates a separate global address for each simultaneous inside-address binding.
- **B.** Every client must keep its inside local address within 203.0.113.0/24.
- **C.** The explicit range supplies ten global addresses.
- **D.** The /24 mask expands allocation to every usable address in the /24.
- **E.** The router automatically permits ten inbound application ports on every host.

**Answer: A, C**

Read the explicit allocation range separately from its mask and the inside address-selection rule. The absence of overload means basic address bindings use distinct pool addresses.

**Option explanations**

- **A:** Without overload, clients do not share a global address by translated ports.
- **B:** The pool describes translated global addresses, not the inside client subnet.
- **C:** The inclusive .100–.109 allocation range contains ten addresses.
- **D:** The configured start and end delimit the actual pool range.
- **E:** A pool count is not an application firewall rule.

**Further reading**

- [IP Addressing Configuration Guide, Cisco IOS XE 17.x — Configuring NAT for IP Address Conservation](https://www.cisco.com/c/en/us/td/docs/routers/ios/config/17-x/ip-addressing/b-ip-addressing/m_iadnat-addr-consv-xe.html) — Inside source address translation; static and dynamic translations; monitoring NAT
- [RFC 3022 — Traditional IP Network Address Translator (Traditional NAT)](https://www.rfc-editor.org/rfc/rfc3022.html) — 2 Overview; 3 Translation phases

---

## CCNA10-068 · IP Services

Objectives: 4.2 · single · Applied

An NTP client receives replies from its configured server, but authentication verification fails after a key rotation. The network path and server clock are healthy. Which repair directly targets the reported fault?

- **A.** Change the client's display time zone by one hour.
- **B.** Align the client/server authentication configuration with the authorized key rotation.
- **C.** Increase the NAT pool size for unrelated application clients.
- **D.** Assign the server a lower stratum without changing authentication.

**Answer: B**

Packet arrival is not the same as acceptance as a trusted time source. Correct the matching authentication settings while preserving the intended validation policy, then verify synchronization.

**Option explanations**

- **A:** Formatting local time does not correct key verification.
- **B:** The exchange is reachable but fails its configured authenticity check.
- **C:** Unrelated address-pool capacity does not repair this established NTP exchange.
- **D:** Hierarchy preference does not make a failed cryptographic check pass.

**Further reading**

- [RFC 5905 — Network Time Protocol Version 4: Protocol and Algorithms Specification](https://www.rfc-editor.org/rfc/rfc5905.html) — 7 NTP protocol data structures; 9 Peer process; 11 System process
- [Setting Time and Calendar Services](https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/bsm/configuration/15-mt/bsm-15-mt-book/bsm-time-calendar-set.html) — Network Time Protocol; configuring NTP associations; monitoring NTP

---

## CCNA10-069 · IP Services

Objectives: 4.3 · multiple · Applied

An internal resolver must support ordinary DNS over both standard UDP and TCP transports. Encrypted DNS alternatives are outside this requirement. Which two destination services should the clients be able to reach on that resolver? Select two.

- **A.** UDP port 161
- **B.** TCP port 21
- **C.** TCP port 53
- **D.** UDP port 67
- **E.** UDP port 53

**Answer: C, E**

Traditional DNS is not exclusively UDP. Filtering that assumes only one transport can produce failures even when some small queries succeed.

**Option explanations**

- **A:** This is commonly used for SNMP requests.
- **B:** This is the FTP control service.
- **C:** DNS also uses TCP, including exchanges requiring TCP handling.
- **D:** This is a DHCP server port, not the DNS service.
- **E:** Ordinary DNS queries commonly use this transport endpoint.

**Further reading**

- [RFC 1035 — Domain Names - Implementation and Specification](https://www.rfc-editor.org/rfc/rfc1035.html) — 3.3 Standard resource records; 4.1 Message format; 4.2 Transport

---

## CCNA10-070 · IP Services

Objectives: 4.4 · single · Foundation

An SNMP manager is walking a table and does not know the object identifier of the next available instance. Which operation requests the lexicographically next accessible object after the supplied identifier?

- **A.** Trap
- **B.** DHCPREQUEST
- **C.** Set
- **D.** GetNext

**Answer: D**

Get reads a specifically named instance; GetNext advances through accessible managed objects. This lets a manager discover table entries without predicting every instance identifier.

**Option explanations**

- **A:** It is an unsolicited notification, not the manager's next-object query.
- **B:** It belongs to address allocation rather than SNMP object traversal.
- **C:** It requests modification rather than advancing a table walk.
- **D:** It returns the next accessible object instance in object-identifier order.

**Further reading**

- [RFC 3416 — Version 2 of the Protocol Operations for the Simple Network Management Protocol (SNMP)](https://www.rfc-editor.org/rfc/rfc3416.html) — 4.2 PDU processing: Get, GetNext, GetBulk, Set, notifications

---

## CCNA10-071 · IP Services

Objectives: 4.5 · single · Challenge

A standards-format syslog message begins with <132>. For this question, PRI = facility × 8 + severity, and facility 16 denotes local0. Which interpretation is correct?

- **A.** Facility local0, severity 4 (warning)
- **B.** Severity 132 with no facility information
- **C.** Facility 4, severity 16
- **D.** Facility local0, severity 5 (notice)

**Answer: A**

Divide PRI by eight: the integer quotient identifies the facility and the remainder identifies severity. The numeric syslog facility here should not be confused with an IOS mnemonic embedded in a message body.

**Option explanations**

- **A:** 132 = 16 × 8 + 4, so the remainder gives warning severity.
- **B:** PRI combines both a facility and a severity value.
- **C:** Severity is restricted to 0–7; the fields have been reversed.
- **D:** That combination produces PRI 133 rather than 132.

**Further reading**

- [RFC 5424 — The Syslog Protocol](https://www.rfc-editor.org/rfc/rfc5424.html) — 6.2.1 PRI; 6.2.3 TIMESTAMP

---

## CCNA10-072 · IP Services

Objectives: 4.6 · single · Applied

A router's WAN interface requests its own IPv4 address from the directly attached ISP DHCP service. It has no static address and no lease. A technician adds only ip helper-address under that interface, expecting the router to become a DHCP client. Which correction is needed?

- **A.** Configure ip nat outside instead of any DHCP client command.
- **B.** Configure ip address dhcp on the WAN interface.
- **C.** Keep only the helper; a relay always leases its own interface automatically.
- **D.** Add a DNS CNAME for the interface.

**Answer: B**

A helper is a relay function for received client messages. Requesting the router interface's own address is a separate client function enabled by ip address dhcp.

**Option explanations**

- **A:** A NAT role does not request an address from the ISP.
- **B:** This enables DHCP acquisition for the interface itself.
- **C:** Relaying other clients' requests does not configure the interface as a DHCP client.
- **D:** A DNS alias does not allocate interface addressing.

**Further reading**

- [IP Addressing: DHCP Configuration Guide, Cisco IOS XE 17 — Configuring the Cisco IOS XE DHCP Client](https://www.cisco.com/c/en/us/td/docs/routers/asr920/configuration/guide/ipaddr-dhcp/17-1-1/b-dhcp-xe-17-1-asr920/m_config-dhcp-client-xe.html) — Configuring the DHCP client; monitoring and maintaining DHCP client operation
- [IP Addressing: DHCP Configuration Guide, Cisco IOS XE Everest 16.6 — Configuring the Cisco IOS XE DHCP Relay Agent](https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/ipaddr_dhcp/configuration/xe-16-6/dhcp-xe-16-6-book/dhcp-relay-agent-xe.html) — Packet forwarding address; giaddr; specifying the packet forwarding address

---

## CCNA10-073 · IP Services

Objectives: 4.7 · single · Challenge

A monitoring dashboard shows tail drops when a congested output queue reaches its configured storage limit. The operator proposes doubling that queue while keeping link rate and offered load unchanged. Which consequence is possible?

- **A.** Longer waiting time for queued packets, without solving sustained overload.
- **B.** Guaranteed lower latency for every class because the buffer is larger.
- **C.** A guaranteed doubling of the link's physical bandwidth.
- **D.** Permanent elimination of drops for any offered load.

**Answer: A**

Buffer sizing affects how much burst traffic can wait and how long it may wait. When the long-term arrival rate exceeds service rate, increasing storage postpones rather than eliminates overflow.

**Option explanations**

- **A:** A larger buffer can absorb more traffic temporarily but does not increase the departure rate.
- **B:** A deeper backlog can increase waiting time rather than ensure lower latency.
- **C:** Buffer capacity and transmission capacity are different resources.
- **D:** Finite buffering can still fill under continuing excess arrivals.

**Further reading**

- [Quality of Service Configuration Guide — Quality of service](https://www.cisco.com/c/en/us/td/docs/switches/lan/c9000/qos/quality-of-service-configuration-guide/m-quality-of-service.html) — Classification; marking; queuing and scheduling; policing and shaping
- [Compare Traffic Policing and Traffic Shaping to Limit Bandwidth](https://www.cisco.com/c/en/us/support/docs/quality-of-service-qos/qos-policing/19645-policevsshape.html) — Traffic policing and traffic shaping comparison

---

## CCNA10-074 · IP Services

Objectives: 4.8 · single · Applied

A router administrator successfully logs in over SSH and sees the user EXEC prompt R10>. The change task needs privileged EXEC commands. Which statement best explains why SSH login alone did not produce R10#?

- **A.** All SSH sessions are required to remain in user EXEC permanently.
- **B.** SSH establishes protected remote access; privilege level is determined separately by account and authorization configuration.
- **C.** The RSA host key's length directly selects whether the prompt ends in > or #.
- **D.** The router must enable Telnet before any user can reach privileged EXEC.

**Answer: B**

Remote protocol choice and command authority are separate controls. The account may enter user EXEC and require an authorized enable step or a configured privilege assignment.

**Option explanations**

- **A:** SSH can carry sessions with different authorized privilege levels.
- **B:** Successful transport and login do not automatically grant privileged EXEC authority.
- **C:** Host-key parameters do not define the user's command authority.
- **D:** Telnet is not a prerequisite for privilege escalation.

**Further reading**

- [Configure SSH on Routers](https://www.cisco.com/c/en/us/support/docs/security-vpn/secure-shell-ssh/4145-ssh.html) — SSH server prerequisites; SSHv2; VTY restrictions; show commands
- [RFC 4251 — The Secure Shell (SSH) Protocol Architecture](https://www.rfc-editor.org/rfc/rfc4251.html) — 4 Architecture; 9 Security considerations

---

## CCNA10-075 · IP Services

Objectives: 4.9 · single · Foundation

A technician transfers a binary device image using TFTP. The bytes must be preserved exactly, without text newline conversion. Which transfer mode fits this requirement?

- **A.** FTP USER mode
- **B.** Netascii
- **C.** DNS recursive mode
- **D.** Octet

**Answer: D**

Binary images require byte-preserving transfer. Octet mode meets that representation requirement; a successful transfer should still be checked against the expected image integrity information before use.

**Option explanations**

- **A:** USER is an FTP login command, not a TFTP transfer mode.
- **B:** Netascii is a text representation that may translate line-ending conventions.
- **C:** DNS recursion has no file-transfer byte-preservation role.
- **D:** Octet mode transfers raw 8-bit bytes without netascii text conversion.

**Further reading**

- [RFC 1350 — The TFTP Protocol (Revision 2)](https://www.rfc-editor.org/info/rfc1350/) — 2 Protocol overview; 3 Relation to other protocols; 4 Initial connection; 6 Normal termination

---

## CCNA10-076 · Security Fundamentals

Objectives: 5.1 · single · Applied

A flood exhausts a public service’s capacity and prevents legitimate clients from obtaining responses. Which security consequence is directly demonstrated, even without evidence of data theft?

- **A.** Proven disclosure of stored passwords.
- **B.** Proven unauthorized alteration of every stored record.
- **C.** Successful implementation of least privilege.
- **D.** Loss of availability.

**Answer: D**

A threat can cause harm through disruption as well as disclosure or alteration. The observed failure establishes an availability impact; other consequences require their own evidence.

**Option explanations**

- **A:** The traffic flood and failed service do not demonstrate that disclosure.
- **B:** No record modification is established by the stated evidence.
- **C:** This is not an access-minimization outcome.
- **D:** The service cannot deliver its required function to legitimate clients.

**Further reading**

- [RFC 4949: Internet Security Glossary, Version 2](https://www.rfc-editor.org/rfc/rfc4949.html) — Section 2: threat, vulnerability, exploit, and countermeasure

---

## CCNA10-077 · Security Fundamentals

Objectives: 5.2 · multiple · Applied

A facility wants to stop unauthorized entry at a restricted door and retain evidence of attempted misuse. Which two controls directly support those respective aims? Select two.

- **A.** A shared mechanical key whose holders are neither recorded nor reviewed.
- **B.** A camera that records continuously while the door remains unlocked and unchecked.
- **C.** An enforced door-access check against current individual authorization.
- **D.** Retained access events and reviewed alarms for rejected or abnormal entry attempts.

**Answer: C, D**

Prevention and evidence are complementary needs. Check the person’s authorization at the boundary, then retain and use the event information.

**Option explanations**

- **A:** Untracked shared possession cannot enforce or audit current individual authorization adequately.
- **B:** Recording may provide evidence but does not satisfy the requirement to stop entry at the door.
- **C:** This makes entry depend on the person’s approved access.
- **D:** These records support detection and follow-up after attempted misuse.

**Further reading**

- [NIST SP 800-53 Rev. 5: Security and Privacy Controls for Information Systems and Organizations](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-53r5.pdf) — AT-2, AT-3, PE-2, and PE-3: awareness, training, and physical access

---

## CCNA10-078 · Security Fundamentals

Objectives: 5.3 · single · Challenge

An IOS engineer accidentally pastes a cleartext password after username audit secret 5. The supplied value is not a valid precomputed type-5 hash. What is the error in the command’s intended use?

- **A.** The secret keyword creates a VTY line password instead of a user credential.
- **B.** The explicit type indicator tells IOS to expect an already encoded secret rather than hash arbitrary plaintext as entered.
- **C.** The number 5 grants the user privilege level 5.
- **D.** A type indicator always causes the supplied value to be displayed as plaintext.

**Answer: B**

Do not confuse a precomputed-hash import with plaintext secret configuration. Explicit type fields require correctly encoded values; verify the platform’s supported secret syntax and test new logins.

**Option explanations**

- **A:** Under username it configures a local account credential.
- **B:** To supply plaintext for ordinary secret generation, use the appropriate supported syntax without claiming it is a precomputed hash.
- **C:** The privilege keyword selects privilege; this number identifies the secret’s encoding.
- **D:** An encoding type does not have that display meaning.

**Further reading**

- [Catalyst 3750-X and 3560-X Configuration Guide: Configuring Switch-Based Authentication](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst3750x_3560x/software/release/15-0_2_se/configuration/guide/3750x_cg/swauthen.html) — Protecting Access to Privileged EXEC Commands; Configuring Username and Password Pairs
- [Security and VPN Configuration Guide, Cisco IOS XE 17.x: Configuring Security with Passwords, Privileges, and Logins](https://www.cisco.com/c/en/us/td/docs/routers/ios/config/17-x/sec-vpn/b-security-vpn/m_sec-cfg-sec-4cli-0.html) — Protecting Access to User EXEC Mode; Password Encryption Levels; Password Change Verification

---

## CCNA10-079 · Security Fundamentals

Objectives: 5.4 · single · Applied

A manager suggests treating an employee number and password as MFA because two fields must be entered. What is the flaw in this classification?

- **A.** The password automatically becomes a biometric factor when paired with a number.
- **B.** An employee number proves possession of the employee’s device.
- **C.** The employee number is an identifier, and the password supplies only a knowledge factor.
- **D.** Two fields always represent possession and knowledge regardless of their contents.

**Answer: C**

An account identifier specifies who claims access. It does not add another factor to the password used to verify that claim.

**Option explanations**

- **A:** The password remains a memorized secret.
- **B:** A known identifier does not demonstrate control of an authenticator.
- **C:** Identifying the claimed account is not an independent proof factor.
- **D:** Factor categories depend on the evidence required, not the number of fields.

**Further reading**

- [NIST SP 800-63B-4: Digital Identity Guidelines — Authentication and Authenticator Management](https://pages.nist.gov/800-63-4/sp800-63b.html) — Authentication factors; password verifiers; authenticator management

---

## CCNA10-080 · Security Fundamentals

Objectives: 5.5 · single · Applied

A company’s security requirement says that an IPsec deployment must provide confidentiality for selected business traffic. Which implementation fact must be verified rather than inferred from the name IPsec alone?

- **A.** Every application uses TCP rather than UDP.
- **B.** The selected protected traffic actually uses an encryption service with the intended endpoints and policy.
- **C.** All inner hosts have publicly routable addresses.
- **D.** The inner host addresses must equal the gateways’ outer addresses.

**Answer: B**

Verify the configured protection and the actual selected traffic. An IPsec label by itself is not sufficient evidence of the required confidentiality scope.

**Option explanations**

- **A:** IPsec can protect IP traffic independent of that transport choice.
- **B:** IPsec is a security architecture with selectable services; the configured protection must meet the requirement.
- **C:** Public inner addressing is not a prerequisite for tunnel confidentiality.
- **D:** Tunnel protection does not require the original host addresses to be the same as the tunnel endpoints.

**Further reading**

- [RFC 4301: Security Architecture for the Internet Protocol](https://www.rfc-editor.org/rfc/rfc4301.html) — Sections 3, 4.1, 4.4.1: IPsec services, tunnel mode, and security policy

---

## CCNA10-081 · Security Fundamentals

Objectives: 5.6 · single · Applied

The ACL below is the only IPv4 filter on the observed packet path. A technician expects the remark to block HTTP, but a TCP packet to destination port 80 is permitted. Why?

```text
ip access-list extended WEB-POLICY
 10 remark Block client HTTP before deployment
 20 permit ip any any
```

- **A.** The ACL automatically translates HTTP to HTTPS.
- **B.** A remark is documentation; the permit ip any any entry determines this packet’s action.
- **C.** The deny is implicit before the first configured entry.
- **D.** The remark blocks HTTP only after the permit counter reaches 100.

**Answer: B**

Review executable policy entries separately from descriptions. The intended HTTP prohibition needs a real deny entry placed before the general permit.

**Option explanations**

- **A:** Filtering rules do not convert the application protocol.
- **B:** Comment text does not create a deny rule.
- **C:** The implicit deny is reached only after no explicit entry matches.
- **D:** Remarks have no counter-triggered filtering behavior.

**Further reading**

- [Catalyst 3750-X and 3560-X Configuration Guide: Configuring Network Security with ACLs](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst3750x_3560x/software/release/15-0_2_se/configuration/guide/3750x_cg/swacl.html) — Applying an IPv4 ACL to a Terminal Line; Including Comments in ACLs

---

## CCNA10-082 · Security Fundamentals

Objectives: 5.7 · single · Applied

A switchport currently shows Secure-up, maximum 1, one approved secure MAC, and Security Violation Count 12. A fresh controlled test from the approved device succeeds and the counter stays at 12. What does this establish?

| Field | Value |
| --- | --- |
| Port Status | Secure-up |
| Maximum MAC Addresses | 1 |
| Total MAC Addresses | 1 |
| Violation counter before test | 12 |
| Violation counter after test | 12 |
| Approved-device test | Successful |

- **A.** Every current frame is being dropped because the counter is nonzero.
- **B.** Exactly 12 unauthorized devices are currently connected.
- **C.** The counter includes earlier violations; it does not demonstrate a new violation during this successful test.
- **D.** The maximum permits 12 sources because the violation count is 12.

**Answer: C**

Separate current state, cumulative counters, and changes during a controlled observation. A historical count is useful evidence but not a direct measure of current unauthorized devices.

**Option explanations**

- **A:** The approved device’s successful test contradicts that conclusion.
- **B:** A violation count is not a current inventory of distinct devices.
- **C:** The current test did not change the retained cumulative count.
- **D:** The configured maximum and a recorded counter have different meanings.

**Further reading**

- [Catalyst 3750-X and 3560-X Configuration Guide: Configuring Port-Based Traffic Control](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst3750x_3560x/software/release/15-0_2_se/configuration/guide/3750x_cg/swtrafc.html) — Secure MAC Addresses; Security Violations; Port Security Aging

---

## CCNA10-083 · Security Fundamentals

Objectives: 5.8 · multiple · Applied

A constructed management log shows: credential accepted; configuration command denied by role policy; denial event delivered to the audit collector. Which two conclusions are supported? Select two.

- **A.** Authentication succeeded for this login.
- **B.** The denied command proves that the password was incorrect.
- **C.** A delivered accounting record proves that every other device uses the same role policy.
- **D.** Authorization prevented the requested configuration command, and accounting recorded the denial.

**Answer: A, D**

Read each event against its AAA function and limit conclusions to the observed system. Denied commands can coexist with successful login and useful accounting.

**Option explanations**

- **A:** The credential-accepted event identifies successful identity verification.
- **B:** The log already states the credential was accepted.
- **C:** The evidence describes this event, not the configuration of other devices.
- **D:** The subsequent events show the permission decision and its retained activity record.

**Further reading**

- [RFC 8907: The Terminal Access Controller Access-Control System Plus (TACACS+) Protocol](https://www.rfc-editor.org/rfc/rfc8907.html) — Sections 5, 6, and 7: authentication, authorization, and accounting

---

## CCNA10-084 · Security Fundamentals

Objectives: 5.9 · single · Applied

A laptop’s WPA2-AES connection to an access point is working. The application uses plaintext HTTP after the AP forwards its traffic onto the wired LAN. Which claim correctly describes WPA2’s protection here?

- **A.** It prevents every authorized wired device from observing any subsequent plaintext segment.
- **B.** It converts HTTP to HTTPS when packets leave the AP.
- **C.** It makes the plaintext HTTP server a WPA3 endpoint.
- **D.** It protects the configured wireless link; it does not by itself encrypt the application’s entire wired path.

**Answer: D**

Wireless security and application transport security cover different portions of a path. Use application-layer protection where the requirement extends beyond the radio link.

**Option explanations**

- **A:** Wireless encryption alone does not supply end-to-end confidentiality on the wired path.
- **B:** WPA2 does not change the application protocol into TLS.
- **C:** The server does not become a wireless-security peer through this forwarding.
- **D:** Wireless link protection ends at its participating wireless endpoints.

**Further reading**

- [Cisco Wireless Controller Configuration Guide, Release 8.10: WLAN Security](https://www.cisco.com/c/en/us/td/docs/wireless/controller/8-10/config-guide/b_cg810/wlan_security.html) — WPA1+WPA2; Configuring WPA1+WPA2 (GUI); Protected Management Frames

---

## CCNA10-085 · Security Fundamentals

Objectives: 5.10 · single · Applied

A constructed AireOS 8.10 WLAN GUI shows correct WPA2-AES/PSK settings. MAC Filtering is also enabled, and the client event says that this approved laptop’s current MAC is absent from the allowlist. The design requires retaining MAC filtering. What is the targeted correction?

| Field | Value |
| --- | --- |
| Layer 2 security | WPA+WPA2 |
| WPA2 / AES / PSK | Enabled / Enabled / Selected |
| MAC Filtering | Enabled |
| Current client MAC | Not in applicable allowlist |
| Observed failure | MAC filtering denied |

- **A.** Disable MAC filtering permanently for all clients.
- **B.** Disable AES while leaving MAC filtering unchanged.
- **C.** Rotate the PSK for all clients although the stated failure is the MAC check.
- **D.** Verify and add the approved laptop’s current MAC to the applicable allowlist.

**Answer: D**

WPA2-PSK is not necessarily the only enabled WLAN access condition. Use the reported failing check and preserve the required control while correcting its authorized data.

**Option explanations**

- **A:** This violates the explicit requirement to retain the control.
- **B:** Changing the cipher does not fix the missing allowlist entry and breaks the desired security profile.
- **C:** A new shared secret does not add the missing MAC authorization.
- **D:** The failed additional access check needs the correct approved entry.

**Further reading**

- [Cisco Wireless Controller Configuration Guide, Release 8.10: WLAN Security](https://www.cisco.com/c/en/us/td/docs/wireless/controller/8-10/config-guide/b_cg810/wlan_security.html) — WPA1+WPA2; Configuring WPA1+WPA2 (GUI); Protected Management Frames

---

## CCNA10-086 · Security Fundamentals

Objectives: 5.6 · single · Challenge

A packet from 10.10.40.35 to server 192.0.2.140 uses TCP destination port 443. Which result follows from the constructed ACL?

```text
ip access-list extended RESTRICTED
 10 deny ip 10.10.40.0 0.0.0.31 any
 20 permit tcp 10.10.40.32 0.0.0.31 host 192.0.2.140 eq 443
 30 deny ip any any
```

- **A.** Sequence 30 denies it because the source is not a network address.
- **B.** The router selects the entry with the largest wildcard instead of processing in order.
- **C.** Sequence 20 permits the packet.
- **D.** Sequence 10 denies it.

**Answer: C**

Compute each source range before evaluating the remaining fields. The source .35 matches the second /27-sized range and the HTTPS tuple completes that permit.

**Option explanations**

- **A:** ACL matching applies to packet addresses and already finds the second permit.
- **B:** ACL processing is ordered first match, not a wildcard-size ranking.
- **C:** The source is outside .0–.31 but inside .32–.63, and the protocol, host, and port match the second entry.
- **D:** Wildcard .31 on base .0 covers only .0 through .31, excluding .35.

**Further reading**

- [Configure IP Access Lists](https://www.cisco.com/c/en/us/support/docs/security/ios-firewall/23602-confaccesslists.html) — ACL Concepts; Masks; Process ACLs; Apply ACLs; Extended ACLs

---

## CCNA10-087 · Security Fundamentals

Objectives: 5.6 · single · Challenge

A stateless ACL on the client-facing egress must allow this DNS reply: UDP source 192.0.2.53:53 to destination 10.10.8.5:54000. Which entry matches that reply with both port fields constrained?

- **A.** permit tcp host 192.0.2.53 eq 53 host 10.10.8.5 eq 54000
- **B.** permit udp host 10.10.8.5 eq 54000 host 192.0.2.53 eq 53
- **C.** permit udp host 192.0.2.53 eq 54000 host 10.10.8.5 eq 53
- **D.** permit udp host 192.0.2.53 eq 53 host 10.10.8.5 eq 54000

**Answer: D**

Port operators attach to the address field immediately before them. Trace the actual reply tuple rather than reusing the client’s query direction.

**Option explanations**

- **A:** The reply is UDP, not TCP.
- **B:** This matches the query in the opposite direction.
- **C:** This reverses the reply’s source and destination port numbers.
- **D:** The source and destination addresses and their respective ports match the reply.

**Further reading**

- [Configure Commonly Used IP ACLs](https://www.cisco.com/c/en/us/support/docs/ip/access-lists/26448-ACLsamples.html) — Allow Pings (ICMP); Allow DNS; TCP/UDP ACL syntax

---

## CCNA10-088 · Security Fundamentals

Objectives: 5.7 · single · Applied

DAI is enabled only for VLAN 110. A switch also carries user VLAN 120, whose ports are untrusted by default. No other ARP protection is present. Which statement correctly describes VLAN 120?

- **A.** It is automatically inspected because it uses the same physical switch.
- **B.** It inherits DAI if its VLAN number is higher than 110.
- **C.** It is automatically inspected because all user ports are untrusted.
- **D.** Its untrusted port state alone does not enable DAI for that VLAN.

**Answer: D**

Feature activation scope and interface trust are separate requirements. Confirm the intended VLAN is actually enabled as well as checking the path’s trust settings.

**Option explanations**

- **A:** A VLAN-specific enable does not cover every VLAN on the device.
- **B:** VLAN numbering does not create inheritance of inspection policy.
- **C:** Trust state governs treatment within enabled feature scope, not VLAN activation.
- **D:** DAI must be enabled for the VLAN before the feature inspects its ARP traffic.

**Further reading**

- [Catalyst 3750-X and 3560-X Configuration Guide: Configuring Dynamic ARP Inspection](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst3750x_3560x/software/release/15-0_2_se/configuration/guide/3750x_cg/swdynarp.html) — Understanding Dynamic ARP Inspection; Rate Limiting; ARP ACLs

---

## CCNA10-089 · Security Fundamentals

Objectives: 5.7 · single · Applied

A switch loses its DHCP snooping bindings during maintenance. A DHCP client completes a fresh exchange through the correct untrusted client port and trusted server path. The new valid binding appears. What has this restored for DAI, assuming its other policy checks are satisfied?

- **A.** A guarantee that the client’s user has administrator privileges.
- **B.** An authorized IP-to-MAC binding against which the client’s ARP claim can be checked.
- **C.** Automatic exemption of the client port from all ARP checks.
- **D.** End-to-end encryption of the client’s ARP packets.

**Answer: B**

Restoring the dependent authorization data can restore normal inspection behavior. Verify the new binding and resulting ARP forwarding rather than bypassing DAI broadly.

**Option explanations**

- **A:** A DHCP binding is not user authorization.
- **B:** The learned DHCP allocation supplies the missing mapping information.
- **C:** A learned binding permits validation; it does not convert the port to trusted.
- **D:** The binding supports inspection rather than encryption.

**Further reading**

- [Catalyst 3750-X and 3560-X Configuration Guide: Configuring DHCP Features and IP Source Guard](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst3750x_3560x/software/release/15-0_2_se/configuration/guide/3750x_cg/swdhcp82.html) — DHCP Snooping; DHCP Snooping Binding Database; Enabling DHCP Snooping
- [Catalyst 3750-X and 3560-X Configuration Guide: Configuring Dynamic ARP Inspection](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst3750x_3560x/software/release/15-0_2_se/configuration/guide/3750x_cg/swdynarp.html) — Understanding Dynamic ARP Inspection; Rate Limiting; ARP ACLs

---

## CCNA10-090 · Security Fundamentals

Objectives: 5.5 · multiple · Applied

Two designs are proposed: A connects a support engineer’s laptop directly to a corporate IPsec gateway; B connects two office gateways that protect traffic for their LANs. Which two descriptions are correct? Select two.

- **A.** B is a site-to-site arrangement whose endpoints are the office gateways.
- **B.** B proves that every office application uses the same user authentication database.
- **C.** A requires every hotel guest to have the engineer’s corporate account.
- **D.** A is a remote-access arrangement whose endpoint includes the engineer’s laptop.

**Answer: A, D**

Identify the actual tunnel endpoints and the population they serve. Remote access and site-to-site can both use IPsec while expressing different endpoint and operational models.

**Option explanations**

- **A:** The gateways protect traffic on behalf of the participating networks.
- **B:** Network tunnel endpoints do not determine every application’s identity service.
- **C:** Other hotel devices are not part of the individual client’s tunnel.
- **D:** The individual endpoint establishes the client-to-gateway protected path.

**Further reading**

- [RFC 4301: Security Architecture for the Internet Protocol](https://www.rfc-editor.org/rfc/rfc4301.html) — Sections 3, 4.1, 4.4.1: IPsec services, tunnel mode, and security policy

---

## CCNA10-091 · Automation and Programmability

Objectives: 6.1 · single · Applied

A team keeps its approved automation templates and nonsecret per-site inputs under version control. Following a fault, it must identify which intended change was deployed last week. What direct management benefit does this practice provide?

- **A.** It guarantees that every historical deployment met the network requirement
- **B.** It replaces all device-state verification with file timestamps
- **C.** It makes changes to the intended configuration traceable and reproducible
- **D.** It prevents any manual change from occurring on a device

**Answer: C**

Versioned automation content provides a record of intended changes and reusable inputs. That record supports investigation and controlled reproduction, while observed device state remains separate evidence.

**Option explanations**

- **A:** Version history records inputs and changes, not automatic proof of successful outcomes.
- **B:** Intended files still need comparison with effective device state.
- **C:** Recorded revisions help reconstruct and review the selected configuration inputs.
- **D:** Version control does not physically prevent out-of-band device changes.

**Further reading**

- [Ansible playbooks](https://docs.ansible.com/projects/ansible/latest/playbook_guide/playbooks_intro.html) — Playbook syntax; Playbook execution; Desired state and idempotency
- [What is Terraform?](https://developer.hashicorp.com/terraform/intro) — How does Terraform work?; Manage any infrastructure; Track your infrastructure

---

## CCNA10-092 · Automation and Programmability

Objectives: 6.2 · single · Applied

A branch controller supports policy deployment through one API, but a newly purchased switch model is not supported by that controller. Which planning conclusion is most appropriate?

- **A.** Controller-based management still depends on device integration support
- **B.** Any Ethernet switch is automatically fully manageable by every controller
- **C.** A northbound application can ignore the compatibility limitation by renaming the switch
- **D.** The unsupported switch therefore cannot forward ordinary Ethernet frames

**Answer: A**

Controllers abstract supported infrastructure, not arbitrary unknown capabilities. The team must confirm the device and feature compatibility needed for the intended network services.

**Option explanations**

- **A:** A common API cannot manage a device feature unless the controller can implement it on that target.
- **B:** Ethernet interoperability does not establish management feature support.
- **C:** Changing a name cannot supply a missing device integration.
- **D:** A management-support limitation does not establish a data-plane failure.

**Further reading**

- [Software-Defined Networking (SDN) Definition](https://www.cisco.com/c/en/us/solutions/software-defined-networking/overview.html) — SDN elements; Features and benefits
- [RFC 7426: Software-Defined Networking (SDN): Layers and Architecture Terminology](https://www.rfc-editor.org/rfc/rfc7426.html) — 3.1 Overview; 3.2 Network Devices; 3.3 Control Plane; 3.5.3 Locality

---

## CCNA10-093 · Automation and Programmability

Objectives: 6.3 · single · Applied

An SD-Access fabric’s underlay provides IP reachability between all fabric nodes. A user in one virtual network still cannot reach a server in another because no inter-network routing policy exists. Which conclusion follows?

- **A.** Underlay reachability automatically grants every overlay endpoint access to every other endpoint
- **B.** The underlay must be broken because any client connection failed
- **C.** All overlays must use one shared client subnet
- **D.** Working underlay transport is necessary but does not itself define cross-overlay connectivity

**Answer: D**

A functioning underlay transports fabric traffic, but it does not create every possible logical connection between endpoints. Cross-virtual-network communication must be deliberately supported and configured.

**Option explanations**

- **A:** The physical transport and overlay reachability policy are different layers.
- **B:** The stated underlay tests succeed; the missing relationship is between virtual networks.
- **C:** Virtual networks do not require one common endpoint subnet.
- **D:** The required logical routing and policy relationship must also exist.

**Further reading**

- [Software-Defined Access](https://www.cisco.com/c/en/us/td/docs/solutions/CVD/Campus/cisco-sda-design-guide.html) — SD-Access architecture; Underlay network; Overlay network; Overlay control plane – LISP; Data plane – VXLAN

---

## CCNA10-094 · Automation and Programmability

Objectives: 6.4 · multiple · Applied

An operations team trains a model using historical link telemetry labeled normal or degraded. It then checks the model using separate labeled records that were not used for training. Which two statements describe this workflow? Select two.

- **A.** The label makes the model a fixed, manually entered utilization threshold
- **B.** The training examples help the model learn an association between telemetry and condition
- **C.** The model has no need for new telemetry after training
- **D.** Correctly classifying every training record guarantees all future decisions will be correct
- **E.** Separate evaluation records can reveal errors on examples not used to train the model

**Answer: B, E**

This is a supervised-learning use of operational data: observed conditions label the examples used for learning. Evaluation compares predictions with known outcomes on separate examples; it provides evidence rather than a guarantee of perfect future performance.

**Option explanations**

- **A:** Labeled examples supply training outcomes; they do not mean the decision rule is a fixed threshold.
- **B:** The known condition supplies the outcome to learn from the telemetry.
- **C:** Applying the learned model still requires the relevant input data.
- **D:** Performance on training examples is not a guarantee about unseen cases.
- **E:** Checking predictions against known outcomes provides evidence about performance beyond the training records.

**Further reading**

- [Supervised Learning](https://developers.google.com/machine-learning/intro-to-ml/supervised) — Foundational supervised learning concepts; Training; Evaluating
- [What is AIOps?](https://developer.cisco.com/articles/what-is-aiops/) — The core components of AIOps; Is AIOps all you need?

---

## CCNA10-095 · Automation and Programmability

Objectives: 6.5 · single · Applied

A resource API returns the documented response shown after a successful deletion. A script reports failure only because it cannot parse a JSON body. What should the script recognize?

```text
DELETE /policies/retired

HTTP/1.1 204 No Content
```

- **A.** Every successful HTTP response must contain a JSON object
- **B.** 204 means authentication failed
- **C.** This successful response intentionally contains no body to decode
- **D.** The server must resend the deleted resource before the client can succeed

**Answer: C**

The response status and the API contract determine whether content is expected. A successful 204 response should not be treated as a failure simply because there is no JSON document.

**Option explanations**

- **A:** Successful responses need not include a representation body.
- **B:** 204 No Content is a success status, not a credential error.
- **C:** A 204 response has no response content for a JSON parser.
- **D:** The documented no-content response does not require that behavior.

**Further reading**

- [RFC 9110: HTTP Semantics](https://www.rfc-editor.org/rfc/rfc9110.html) — 9 Methods; 15 Status Codes

---

## CCNA10-096 · Automation and Programmability

Objectives: 6.5 · single · Challenge

A lab API permits changing an existing interface description through a documented PATCH endpoint. Its contract explicitly says the body is JSON Patch with media type application/json-patch+json. Which choice follows that contract?

```text
Documented example body for this resource:
[{"op":"replace","path":"/description","value":"to-distribution"}]
```

- **A.** Send the supported patch document with Content-Type: application/json-patch+json
- **B.** Send arbitrary XML while declaring application/json-patch+json
- **C.** Send a full unmodified interface object using GET
- **D.** Omit the method because JSON Patch determines the URI automatically

**Answer: A**

The HTTP method, target URI and patch document format work together. This contract requires PATCH with a JSON Patch representation, rather than an arbitrary partial object or another encoding.

**Option explanations**

- **A:** The declared media type tells the server how to interpret the patch instructions.
- **B:** The declared encoding and actual body would disagree.
- **C:** GET does not express the requested modification and the object is not the required patch document.
- **D:** A patch document does not replace the HTTP method and target resource.

**Further reading**

- [RFC 5789: PATCH Method for HTTP](https://www.rfc-editor.org/rfc/rfc5789.html#section-2) — 2 The PATCH Method
- [RFC 6902: JavaScript Object Notation (JSON) Patch](https://www.rfc-editor.org/rfc/rfc6902.html) — 3 Document Structure; 4 Operations

---

## CCNA10-097 · Automation and Programmability

Objectives: 6.6 · single · Applied

A supported Ansible network task reads current interface information using the device API. The task does not change configuration. Which capability does this demonstrate?

- **A.** Ansible must modify a setting whenever a module runs
- **B.** Ansible can collect network state for later validation or reporting
- **C.** The task has become the switch’s packet-forwarding engine
- **D.** Ansible can work only from previously saved offline files

**Answer: B**

Network automation includes gathering operational or configuration information. Ansible tasks can supply observations used by later checks and reports without performing a device change.

**Option explanations**

- **A:** Modules can gather information without changing device configuration.
- **B:** Read operations can be part of an automation workflow.
- **C:** Management information gathering is not user packet forwarding.
- **D:** Supported modules can obtain current information from devices.

**Further reading**

- [How Network Automation is Different](https://docs.ansible.com/projects/ansible/latest/network/getting_started/network_differences.html) — Execution on the control node; Multiple communication protocols; Collections organized by network platform
- [Ansible playbooks](https://docs.ansible.com/projects/ansible/latest/playbook_guide/playbooks_intro.html) — Playbook syntax; Playbook execution; Desired state and idempotency

---

## CCNA10-098 · Automation and Programmability

Objectives: 6.6 · single · Challenge

A Terraform plan for a maintenance change proposes replacing a virtual network that the operator expected to update in place. No apply has occurred. What is the plan’s value at this point?

- **A.** The plan proves the network was already destroyed
- **B.** The operator must apply immediately because plans cannot be rejected
- **C.** The replacement can be ignored because resource names never change
- **D.** It exposes an unexpected lifecycle action before the operator commits the change

**Answer: D**

Planning makes proposed resource actions visible before execution. An unexpected replacement is a reason to examine the configuration and provider behavior while the infrastructure remains unchanged by this plan.

**Option explanations**

- **A:** A proposed replacement is not evidence that apply has executed.
- **B:** A plan is available for review before execution.
- **C:** A stable name does not negate the proposed lifecycle action.
- **D:** The proposed replacement can be investigated and the configuration adjusted before apply.

**Further reading**

- [What is Terraform?](https://developer.hashicorp.com/terraform/intro) — How does Terraform work?; Manage any infrastructure; Track your infrastructure

---

## CCNA10-099 · Automation and Programmability

Objectives: 6.7 · single · Challenge

The complete payload is a valid JSON value but contains only a quoted string, as shown. The API requires an object with a hostname member. Which assessment is correct?

```text
"edge-12"
```

- **A.** The payload is valid JSON but does not meet the API’s required structure
- **B.** All JSON documents must begin with an opening brace
- **C.** The string automatically becomes {"hostname":"edge-12"} when parsed
- **D.** Adding whitespace around the string creates the required object

**Answer: A**

JSON grammar permits a serialized string as the complete document. The separate application contract still requires an object containing a named member, so this payload is unsuitable.

**Option explanations**

- **A:** A string is a valid JSON value, while the contract specifically requires an object.
- **B:** JSON can represent values other than objects.
- **C:** A JSON parser does not invent the missing member or enclosing object.
- **D:** Whitespace does not change its value type or structure.

**Further reading**

- [RFC 8259: The JavaScript Object Notation (JSON) Data Interchange Format](https://www.rfc-editor.org/rfc/rfc8259.html) — 2 JSON Grammar; 3 Values; 4 Objects; 5 Arrays; 6 Numbers; 7 Strings

---

## CCNA10-100 · Automation and Programmability

Objectives: 6.7 · single · Applied

The JSON response contains a routes array and a nested nextHop object. Which statement correctly describes its structure?

```text
{"routes":[{"prefix":"0.0.0.0/0","nextHop":{"family":"ipv4","address":"192.0.2.1"}}]}
```

- **A.** nextHop is the second element of the routes array
- **B.** address is an array because it contains a dotted-decimal value
- **C.** routes contains one object whose nextHop member contains another object
- **D.** The value ipv4 is a JSON member name

**Answer: C**

Follow each delimiter boundary: routes is an array, its sole element is an object, and nextHop holds a nested object. The address text is a string within that nested object.

**Option explanations**

- **A:** nextHop is a member within the first route object.
- **B:** The braces establish an object; punctuation inside the string does not make an array.
- **C:** The array has one route element, and that element nests the next-hop object.
- **D:** ipv4 is the value of the family member.

**Further reading**

- [RFC 8259: The JavaScript Object Notation (JSON) Data Interchange Format](https://www.rfc-editor.org/rfc/rfc8259.html) — 2 JSON Grammar; 3 Values; 4 Objects; 5 Arrays; 6 Numbers; 7 Strings

---
