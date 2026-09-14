# CCNA Practice — Set 08

100 original questions aligned to CCNA 200-301 v1.1. No interactive labs.

Answers and explanations follow each question. For an unrevealed attempt, use the Streamlit app.

Content review date: 2026-09-14.

## CCNA8-001 · Network Fundamentals

Objectives: 1.1.f, 1.1.g · single · Applied

A camera uploads footage to a recording server. The camera is considered an endpoint in this design. Which evidence identifies the recording host’s server role?

- **A.** It has a shorter Ethernet cable
- **B.** Its MAC address starts with a lower number
- **C.** It must never initiate any other network connection
- **D.** It accepts the camera’s uploads and provides the recording service

**Answer: D**

Endpoint and server classifications describe the device’s role in the service being examined. Hardware appearance or address order is not decisive.

**Option explanations**

- **A:** Cable length does not establish application role.
- **B:** Numeric MAC ordering does not identify servers.
- **C:** A server can also initiate separate client interactions.
- **D:** Providing the requested service establishes its role in this interaction.

**Further reading**

- [RFC 9110: HTTP Semantics](https://www.rfc-editor.org/rfc/rfc9110.html#section-3.3) — 3.3. Connections, Clients, and Servers

---

## CCNA8-002 · Network Fundamentals

Objectives: 1.2.c · single · Applied

In a basic leaf-spine fabric, all spines are healthy but one leaf fails. Servers are single-homed to that failed leaf. What does the spine redundancy provide those servers?

- **A.** Automatic attachment to another leaf without another link
- **B.** Automatic wireless access to every spine
- **C.** No replacement for their failed only attachment point
- **D.** A new virtual NIC inside every server

**Answer: C**

Redundancy must cover the actual failed dependency. Multiple fabric paths do not make a single server attachment redundant.

**Option explanations**

- **A:** No alternate server-to-leaf link exists.
- **B:** No radio access is specified.
- **C:** Redundant spines cannot bypass a lost sole server access link.
- **D:** Spines do not create host NICs.

**Further reading**

- [Cisco Massively Scalable Data Center Network Fabric Design and Operation White Paper](https://www.cisco.com/c/en/us/products/collateral/switches/nexus-9000-series-switches/white-paper-c11-743245.html) — MSDC Layer 3 IP fabric design evolution; Cisco MSDC design example 1: Two-tiered spine-leaf topology

---

## CCNA8-003 · Network Fundamentals

Objectives: 1.3.a · single · Challenge

An optical receiver’s specified acceptable input is −14 to −1 dBm. The measured receive level is −17 dBm; other compatibility requirements are met. Which assessment follows?

| Quantity | Value |
| --- | --- |
| Minimum acceptable receive level | −14 dBm |
| Maximum acceptable receive level | −1 dBm |
| Measured receive level | −17 dBm |

- **A.** Receive power is below the specified minimum
- **B.** Receive power is too high
- **C.** Receive power is within range because all values are negative
- **D.** The measurement alone proves a duplex mismatch

**Answer: A**

Compare the measured optical level with both limits of the receiver range. Investigate excess loss or insufficient transmitted power when reception is too weak.

**Option explanations**

- **A:** −17 dBm is 3 dB below −14 dBm.
- **B:** The measured value is weaker, not stronger, than the allowed range.
- **C:** Negative dBm still has an ordered numeric scale.
- **D:** Optical receive level does not show duplex configuration.

**Further reading**

- [Cisco 10GBASE SFP+ Modules Data Sheet](https://www.cisco.com/c/en/us/products/collateral/interfaces-modules/transceiver-modules/data_sheet_c78-455693.html) — Cisco SFP-10G-SR module; Cisco SFP-10G-LR module; Cisco SFP-10G-T-X module

---

## CCNA8-004 · Network Fundamentals

Objectives: 1.4 · multiple · Applied

After a repair, which TWO observations meaningfully verify Ethernet link operation? Select two.

- **A.** The interface description includes the word healthy
- **B.** Both ends report the intended compatible speed and duplex
- **C.** Only the switch hostname changed
- **D.** Error counter deltas remain acceptable during representative traffic
- **E.** The cable jacket matches the rack color

**Answer: B, D**

Combine state inspection with behavior under representative traffic. A label or idle link alone provides weaker evidence than operational measurements.

**Option explanations**

- **A:** An administrative description is not operational evidence.
- **B:** This checks actual link agreement against the requirement.
- **C:** The hostname is not a link-health measurement.
- **D:** Measured new errors help evaluate behavior under use.
- **E:** Appearance does not demonstrate electrical or optical quality.

**Further reading**

- [Configure and Verify Ethernet 10/100/1000Mb Half/Full Duplex Auto-Negotiation](https://www.cisco.com/c/en/us/support/docs/lan-switching/ethernet/10561-3.html) — Background Information; Auto-Negotiation on Catalyst Switches that Run Cisco IOS Software

---

## CCNA8-005 · Network Fundamentals

Objectives: 1.5 · single · Applied

A TCP receiver advertises a receive window of zero while its application is temporarily unable to drain the receive buffer. What does that signal to the sender?

```text
Receiver → Sender: ACK=8200, Window=0
```

- **A.** Change to UDP without notifying the application
- **B.** The path has no Ethernet carrier
- **C.** The receiver currently advertises no space for additional ordinary data
- **D.** All previously acknowledged data must be resent immediately

**Answer: C**

The advertised window reflects receiver-side flow control. TCP has mechanisms for detecting when the window opens again; it need not abandon the connection immediately.

**Option explanations**

- **A:** TCP does not silently replace its transport.
- **B:** A receive window is not a physical link-status field.
- **C:** Flow control limits sending according to the available receive window.
- **D:** Zero window does not invalidate all previous acknowledgments.

**Further reading**

- [RFC 9293: Transmission Control Protocol (TCP)](https://www.rfc-editor.org/rfc/rfc9293.html#section-2.2) — 2.2. Key TCP Concepts

---

## CCNA8-006 · Network Fundamentals

Objectives: 1.6 · single · Challenge

A technician enters mask 255.255.250.0. Why is it unsuitable as an ordinary contiguous IPv4 subnet mask?

- **A.** The third octet’s binary ones are interrupted by a zero
- **B.** All valid masks must end in 255
- **C.** Masks may contain only 255 and 0
- **D.** It is an IPv6-only mask

**Answer: A**

A prefix mask contains one uninterrupted run of leading ones. Converting the boundary octet to binary exposes the gap.

**Option explanations**

- **A:** 250 is 11111010, not contiguous leading ones followed by zeros.
- **B:** Many valid masks end in zero.
- **C:** Values such as 128, 192, and 252 can be valid at the boundary.
- **D:** This dotted mask is not a valid IPv6 prefix notation either.

**Further reading**

- [Configure IP Addresses and Unique Subnets for New Users](https://www.cisco.com/c/en/us/support/docs/ip/routing-information-protocol-rip/13788-3.html) — Network Masks; Understand Subnetting; VLSM Example

---

## CCNA8-007 · Network Fundamentals

Objectives: 1.7 · single · Foundation

A company plans to advertise 192.168.70.0/24 as its globally reachable Internet service prefix. What is wrong with relying on that plan?

- **A.** The prefix has no usable host addresses
- **B.** RFC 1918 forbids internal web servers
- **C.** The prefix can be used only on Wi-Fi
- **D.** It is private space that is not intended as a globally routed public prefix

**Answer: D**

Private address reuse conflicts with treating the prefix as a globally unique public allocation. Internal usability does not establish Internet-wide reachability.

**Option explanations**

- **A:** A /24 has ordinary usable host addresses.
- **B:** Private-addressed servers can operate internally.
- **C:** Private IPv4 addressing is independent of link technology.
- **D:** External reachability requires a suitable public addressing/service design.

**Further reading**

- [RFC 1918: Address Allocation for Private Internets](https://www.rfc-editor.org/rfc/rfc1918#section-3) — 3. Private Address Space

---

## CCNA8-008 · Network Fundamentals

Objectives: 1.8 · single · Challenge

Which address is the last /64 subnet prefix inside 2001:db8:600:ab00::/56?

- **A.** 2001:db8:600:ab0f::/64
- **B.** 2001:db8:600:abff::/64
- **C.** 2001:db8:600:ac00::/64
- **D.** 2001:db8:601:abff::/64

**Answer: B**

The /56 contains 256 /64 prefixes. The fixed fourth-hextet high byte is ab, and its final low byte reaches ff.

**Option explanations**

- **A:** This varies only four of the eight available subnet bits.
- **B:** The low byte of the fourth hextet varies from 00 to ff.
- **C:** This starts the next /56.
- **D:** This changes fixed bits in the third hextet.

**Further reading**

- [RFC 4291: IP Version 6 Addressing Architecture](https://www.rfc-editor.org/rfc/rfc4291#section-2.3) — 2.3. Text Representation of Address Prefixes; 2.4. Address Type Identification; 2.5.6. Link-Local IPv6 Unicast Addresses; 2.7. Multicast Addresses

---

## CCNA8-009 · Network Fundamentals

Objectives: 1.9.a · single · Foundation

Which statement correctly compares a global-unicast IPv6 address with a link-local address on the same interface?

- **A.** Only the link-local address may have a prefix length
- **B.** The global address must encode the NIC’s MAC address
- **C.** The global address can support routing beyond the local link; the link-local address cannot be forwarded off-link
- **D.** The presence of a global address disables link-local operation

**Answer: C**

Address scope and interface attachment are separate properties. Global address classification still does not prove that a route or policy currently permits access.

**Option explanations**

- **A:** Both address forms are interpreted with relevant prefixes.
- **B:** Other interface identifier methods are possible.
- **C:** Their scopes differ even though they share an interface.
- **D:** Both can coexist and serve different purposes.

**Further reading**

- [RFC 4291: IP Version 6 Addressing Architecture](https://www.rfc-editor.org/rfc/rfc4291#section-2.3) — 2.3. Text Representation of Address Prefixes; 2.4. Address Type Identification; 2.5.6. Link-Local IPv6 Unicast Addresses; 2.7. Multicast Addresses

---

## CCNA8-010 · Network Fundamentals

Objectives: 1.10 · single · Applied

A Linux interface has address 10.45.2.88/24 and is operationally up. Which command is the direct read-only next check for its configured IPv4 gateway routes?

- **A.** ip -4 route show
- **B.** ip link delete enp1s0
- **C.** ip address flush dev enp1s0
- **D.** hostname

**Answer: A**

Address and carrier state do not reveal all route configuration. Inspect the relevant address-family routing table.

**Option explanations**

- **A:** This displays the IPv4 routing entries, including any default route.
- **B:** This is a destructive interface operation, not route inspection.
- **C:** This removes addressing rather than displaying gateway configuration.
- **D:** The host’s name does not list gateway routes.

**Further reading**

- [ip-route(8) — Linux manual page](https://man7.org/linux/man-pages/man8/ip-route.8.html) — ip route show; route types and nexthops

---

## CCNA8-011 · Network Fundamentals

Objectives: 1.11.b, 1.11.d · multiple · Applied

An attacker creates an AP advertising the same SSID as the company WLAN. Which TWO conclusions are correct? Select two.

- **A.** Matching SSID text proves company ownership
- **B.** SSID is not a cryptographic proof of AP identity
- **C.** Every matching SSID necessarily uses the same keys
- **D.** The client’s security configuration still matters when selecting and authenticating a network
- **E.** The duplicate SSID changes both APs’ IPv4 addresses

**Answer: B, D**

A network name is an identifier, not a trust credential. Evaluate authentication and encryption settings separately from the displayed SSID.

**Option explanations**

- **A:** An advertised name can be copied.
- **B:** Identity assurance requires the configured security mechanisms.
- **C:** A name does not determine cryptographic keys.
- **D:** Authentication requirements must be satisfied independently of the name.
- **E:** SSID text does not automatically rewrite IP configuration.

**Further reading**

- [Wireless Fundamentals: Encryption and Authentication](https://documentation.meraki.com/Wireless/Design_and_Configure/Architecture_and_Best_Practices/Wireless_Fundamentals:_Encryption_and_Authentication) — WPA2 – Personal; Hidden SSID

---

## CCNA8-012 · Network Fundamentals

Objectives: 1.12 · single · Applied

A virtual router exposes two VRFs, and both are hosted inside one VM. What remains shared despite separate routing tables?

- **A.** Every route must be identical in both VRFs
- **B.** Every tenant must use the same destination MAC
- **C.** Every application session must be visible in both VRFs
- **D.** The VM and its underlying host are common operational dependencies

**Answer: D**

VRFs isolate Layer 3 contexts within the router. They do not, by themselves, provide independent operating-system or hardware failure domains.

**Option explanations**

- **A:** The routing tables can differ.
- **B:** VRF separation does not require identical MAC destinations.
- **C:** Forwarding separation can keep tenant traffic apart.
- **D:** Separate forwarding contexts do not create separate virtual or physical machines.

**Further reading**

- [IP Routing Configuration Guide, Cisco IOS XE Dublin 17.12.x (Catalyst 9500 Switches): Configuring VRF-lite](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst9500/software/release/17-12/configuration_guide/rtng/b_1712_rtng_9500_cg/configuring_vrf_lite.html) — Information About VRF-lite; Guidelines for Configuring VRF-lite
- [What is a container?](https://docs.docker.com/get-started/docker-concepts/the-basics/what-is-a-container/#containers-versus-virtual-machines-vms) — Containers versus virtual machines (VMs)

---

## CCNA8-013 · Network Fundamentals

Objectives: 1.13.c · single · Applied

A frame with an unknown unicast destination enters VLAN 80 through a forwarding port. Another VLAN 80 port is administratively down. No special features apply. Why is no copy sent through that down port?

- **A.** Unknown-unicast flooding targets only VLAN 1
- **B.** Every unknown frame must first become a broadcast address
- **C.** Flooding uses eligible operational forwarding ports
- **D.** The switch must route the frame instead

**Answer: C**

Flooding is bounded by both VLAN context and port eligibility. It is not an instruction to transmit through unusable interfaces.

**Option explanations**

- **A:** It follows the actual ingress VLAN.
- **B:** The original destination remains unchanged.
- **C:** VLAN membership alone does not make a down port usable.
- **D:** No Layer 3 routing requirement follows from a down port.

**Further reading**

- [Configuring MAC Address Tables](https://www.cisco.com/c/en/us/td/docs/switches/datacenter/nexus5500/sw/layer2/7x/b_5500_Layer2_Config_7x/config_mac_address_tables.pdf) — Information About MAC Addresses (page 1); Configuring the Aging Time for the MAC Table (page 2)

---

## CCNA8-014 · Network Fundamentals

Objectives: 1.1.c · single · Foundation

A next-generation firewall has an IPS feature available in its product specification, but the inspection policy is disabled. What can be concluded about IPS protection?

- **A.** Capability alone does not establish that inspection is being enforced
- **B.** Every supported signature is necessarily blocking traffic
- **C.** All traffic is automatically encrypted
- **D.** Disabling IPS removes all Layer 2 connectivity

**Answer: A**

Distinguish what a product can do from what its active policy does. Verification must examine effective enforcement settings and behavior.

**Option explanations**

- **A:** Effective configuration must enable and apply the feature.
- **B:** The feature is explicitly disabled.
- **C:** IPS availability does not imply encryption.
- **D:** Inspection policy and basic forwarding are distinct functions.

**Further reading**

- [NGFW vs traditional firewall: what’s different [Explained]](https://www.cisco.com/site/us/en/learn/topics/security/what-is-a-next-generation-firewall.html) — Next-generation firewall overview

---

## CCNA8-015 · Network Fundamentals

Objectives: 1.6 · multiple · Challenge

Which TWO statements about 10.70.15.254/20 are correct? Select two.

- **A.** Its subnet mask is 255.255.255.240
- **B.** Its subnet starts at 10.70.15.0
- **C.** Its network address is 10.70.0.0
- **D.** Its directed broadcast address is 10.70.15.255
- **E.** Its last usable address is 10.70.16.254

**Answer: C, D**

The mask is 255.255.240.0. The subnet includes third octets 0 through 15, with .15.255 as broadcast.

**Option explanations**

- **A:** That is /28, not /20.
- **B:** A /20 groups third-octet values in blocks of 16.
- **C:** The third octet 15 lies in the 0–15 /20 block.
- **D:** All host bits set gives the end of that block.
- **E:** That address belongs to a different /20 block.

**Further reading**

- [Configure IP Addresses and Unique Subnets for New Users](https://www.cisco.com/c/en/us/support/docs/ip/routing-information-protocol-rip/13788-3.html) — Network Masks; Understand Subnetting; VLSM Example

---

## CCNA8-016 · Network Fundamentals

Objectives: 1.9.b · single · Applied

An anycast service withdraws the failed site’s route, and routing converges to another advertising site. What enabled the client to use the same destination address after convergence?

- **A.** IPv6 multicast copied the session state
- **B.** Multiple service instances use the shared anycast address
- **C.** The client’s MAC address became a global route
- **D.** Anycast guarantees existing stateful sessions survive unchanged

**Answer: B**

The address remains constant while the selected reachable instance changes. Session survival still depends on application behavior and state.

**Option explanations**

- **A:** Anycast does not automatically replicate application state.
- **B:** Routing can direct new traffic to another instance advertising that address.
- **C:** The service route is not derived from the client MAC.
- **D:** Network redirection does not guarantee application-state continuity.

**Further reading**

- [RFC 4786: Operation of Anycast Services](https://www.rfc-editor.org/rfc/rfc4786#section-2) — 2. Terminology; 3.1. General Description; 3.2. Goals

---

## CCNA8-017 · Network Fundamentals

Objectives: 1.11.c · single · Applied

A Wi-Fi adapter reports a high PHY link rate, but measured application throughput is lower. Which explanation is sound?

- **A.** A PHY rate must equal application payload throughput
- **B.** A high PHY rate proves there is no contention
- **C.** The reported rate means every TCP transaction was acknowledged by the application
- **D.** Management traffic, contention, retransmissions, and protocol overhead consume capacity

**Answer: D**

Compare measurements at the same layer. A radio’s negotiated physical rate describes signaling capability rather than delivered application payload.

**Option explanations**

- **A:** Protocol overhead and medium sharing reduce useful payload rate.
- **B:** Other stations can still compete for airtime.
- **C:** PHY signaling is not application confirmation.
- **D:** The physical signaling rate is not a guarantee of useful application throughput.

**Further reading**

- [Wireless Throughput Calculations and Limitations](https://documentation.meraki.com/Wireless/Design_and_Configure/Architecture_and_Best_Practices/Wireless_Throughput_Calculations_and_Limitations) — Limitations and Factors Affecting Throughput

---

## CCNA8-018 · Network Fundamentals

Objectives: 1.13.a, 1.13.d · single · Applied

A MAC address appears alternately on two ports in one VLAN as new source frames arrive from both. Both ports are forwarding. What does the table behavior establish?

- **A.** The source MAC is being observed at changing ingress locations
- **B.** The switch has proven the exact cable fault
- **C.** The source’s IP subnet mask is necessarily wrong
- **D.** Every entry is static and immune to updates

**Answer: A**

MAC-table changes are evidence of source location observations. A loop, duplicate MAC use, or legitimate movement needs further investigation.

**Option explanations**

- **A:** The observations support movement or duplication; they do not alone identify its cause.
- **B:** The table alone does not identify a specific physical defect.
- **C:** MAC movement does not prove an IP mask error.
- **D:** Dynamic updates are explicitly occurring.

**Further reading**

- [Configuring MAC Address Tables](https://www.cisco.com/c/en/us/td/docs/switches/datacenter/nexus5500/sw/layer2/7x/b_5500_Layer2_Config_7x/config_mac_address_tables.pdf) — Information About MAC Addresses (page 1); Configuring the Aging Time for the MAC Table (page 2)

---

## CCNA8-019 · Network Fundamentals

Objectives: 1.2.e, 1.1.a, 1.1.b, 1.1.d · single · Applied

A SOHO appliance has four LAN switch ports, one WAN routed interface, and a Wi-Fi radio. Which path describes a local wireless client reaching a wired host in the same bridged LAN?

- **A.** A mandatory trip through the ISP and back
- **B.** A mandatory route through the public cloud
- **C.** Wireless access followed by local Layer 2 forwarding
- **D.** Direct optical transmission from the client to the server

**Answer: C**

Integrated devices combine roles, but a particular flow need not use every role. Same-LAN traffic can remain local to the bridging functions.

**Option explanations**

- **A:** Local bridging does not require external transit.
- **B:** No cloud forwarding dependency is stated.
- **C:** The integrated AP and switching functions can bridge the local traffic.
- **D:** The client’s link is Wi-Fi, not optical fiber.

**Further reading**

- [How do I set up a small business network?](https://www.cisco.com/site/us/en/learn/topics/small-business/how-to-set-up-a-network.html) — Introduction; What is a switch?; What is a router?
- [Networking Basics: What You Need To Know](https://www.cisco.com/site/us/en/learn/topics/small-business/networking-basics.html) — Switches; Routers; Access Points

---

## CCNA8-020 · Network Fundamentals

Objectives: 1.6 · matching · Applied

Match each addressing requirement with its smallest ordinary IPv4 subnet size. Include network and broadcast reservations; use each prefix once.

1. Two router interfaces on an ordinary numbered link.
2. Thirteen total interface addresses in a small LAN.
3. Twenty-nine total interface addresses in a workgroup LAN.
4. One hundred total interface addresses in an office LAN.

- **A.** /30
- **B.** /27
- **C.** /28
- **D.** /25

**Answer: 1 → A; 2 → C; 3 → B; 4 → D**

Choose the longest prefix whose usable host count meets the complete interface requirement. A larger subnet may work but would not be the smallest here.

**Option explanations**

- **A:** Two usable addresses support a two-interface link.
- **B:** Thirty usable addresses support the stated 29 interfaces.
- **C:** Fourteen usable addresses support the stated 13 interfaces.
- **D:** 126 usable addresses support the stated 100 interfaces.

**Further reading**

- [Configure IP Addresses and Unique Subnets for New Users](https://www.cisco.com/c/en/us/support/docs/ip/routing-information-protocol-rip/13788-3.html) — Network Masks; Understand Subnetting; VLSM Example

---

## CCNA8-021 · Network Access

Objectives: 2.1 · single · Foundation

VLAN 35 is named Research on SW-A and Lab on SW-B. A healthy trunk permits VLAN 35, and both VLAN instances are active. Hosts in VLAN 35 use compatible IP settings. Which conclusion follows from the different names alone?

- **A.** The trunk converts VLAN 35 into native VLAN 1.
- **B.** The names alone do not prevent VLAN 35 frame forwarding across the trunk.
- **C.** The VLANs become different broadcast domains because their labels differ.
- **D.** Both switches must disable MAC learning until names match.

**Answer: B**

Operational identity on an ordinary trunk comes from the VLAN number. Consistent names help humans, but are not the frame’s VLAN identifier.

**Option explanations**

- **A:** Names do not control native tagging behavior.
- **B:** 802.1Q carries the VLAN ID, not the human-readable local VLAN name.
- **C:** Different labels do not change the shared on-wire VLAN ID.
- **D:** MAC learning does not depend on identical descriptive VLAN labels.

**Further reading**

- [VLAN Configuration Guide, Cisco IOS XE 17.15.x — Configuring VLANs](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst9300/software/release/17-15/configuration_guide/vlan/b_1715_vlan_9300_cg/configuring_vlans.html) — Supported VLANs; Deleting a VLAN; VLAN Port Membership Modes
- [VLAN Configuration Guide, Cisco IOS XE 17.15.x — Configuring VLAN Trunks](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst9300/software/release/17-15/configuration_guide/vlan/b_1715_vlan_9300_cg/configuring_vlan_trunks.html) — Allowed VLANs on a Trunk; Configuring the Native VLAN for Untagged Traffic

---

## CCNA8-022 · Network Access

Objectives: 2.1.c · single · Applied

A Layer 3 switch has IP routing enabled and two up/up SVIs with nonoverlapping directly connected subnets. Hosts use the correct SVI gateways and no filters apply. What routing configuration is necessary just to route between those two local subnets?

```text
ip routing
Vlan15  172.16.15.1/24  up/up
Vlan25  172.16.25.1/24  up/up
Connected routes: 172.16.15.0/24, 172.16.25.0/24
```

- **A.** An OSPF adjacency must exist with every endpoint.
- **B.** A default route pointing to one of the same local hosts is mandatory.
- **C.** The two VLANs must share the same IP prefix.
- **D.** No additional static route is needed for the already connected subnets.

**Answer: D**

Routing between directly attached networks uses connected route information. Default routes serve destinations not already covered by more specific installed routes.

**Option explanations**

- **A:** Ordinary endpoints do not need routing-protocol adjacencies for inter-VLAN communication.
- **B:** A default route is not needed to choose a known connected destination.
- **C:** Separate routed VLAN subnets should not overlap in this simple design.
- **D:** Operational addressed SVIs install their directly connected routes.

**Further reading**

- [Configure Inter-VLAN Routing with Catalyst Switches](https://www.cisco.com/c/en/us/support/docs/lan-switching/inter-vlan-routing/41260-189.html) — Configure; Troubleshoot

---

## CCNA8-023 · Network Access

Objectives: 2.1.a · single · Applied

A deployment standard requires user data on access VLAN 65 while keeping a phone’s voice VLAN 165 unchanged. The current switch-port settings are below. Which single assignment should change?

```text
interface GigabitEthernet1/0/19
 switchport mode access
 switchport access vlan 55
 switchport voice vlan 165
```

- **A.** Change the trunk native VLAN to 65 on every uplink.
- **B.** Remove the voice VLAN entirely.
- **C.** Change switchport voice vlan 165 to 65.
- **D.** Change switchport access vlan 55 to switchport access vlan 65.

**Answer: D**

Apply the narrow change to the incorrect traffic class. A phone-and-PC port has separate assignments that need not be modified together.

**Option explanations**

- **A:** The problem is the local access membership, not all trunk native settings.
- **B:** That violates the requirement to preserve voice VLAN 165.
- **C:** That moves voice instead of correcting the PC data membership.
- **D:** Only the untagged user data membership differs from the requirement.

**Further reading**

- [VLAN Configuration Guide, Cisco IOS XE 17.15.x — Configuring Voice VLANs](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst9300/software/release/17-15/configuration_guide/vlan/b_1715_vlan_9300_cg/configuring_voice_vlans.html) — Cisco IP Phone Voice Traffic; Cisco IP Phone Data Traffic

---

## CCNA8-024 · Network Access

Objectives: 2.2.a · single · Applied

A workstation port is administratively set to switchport mode access. An adjacent device sends DTP advertisements requesting a trunk. What is the expected operational mode of this statically configured access port?

- **A.** It must start LACP before deciding.
- **B.** It always becomes a trunk because DTP overrides administrator configuration.
- **C.** It remains nontrunking access.
- **D.** It changes to a routed no-switchport interface.

**Answer: C**

Explicit interface mode is an important part of the effective Layer 2 boundary. A peer’s DTP request does not override a fixed access setting.

**Option explanations**

- **A:** Aggregation negotiation is separate from trunk-mode selection.
- **B:** The static access choice constrains the negotiated result.
- **C:** Static access mode does not become a trunk merely because the neighbor requests one.
- **D:** DTP does not create an IP routed interface.

**Further reading**

- [VLAN Configuration Guide, Cisco IOS XE 17.15.x — Configuring VLAN Trunks](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst9300/software/release/17-15/configuration_guide/vlan/b_1715_vlan_9300_cg/configuring_vlan_trunks.html) — Allowed VLANs on a Trunk; Configuring the Native VLAN for Untagged Traffic

---

## CCNA8-025 · Network Access

Objectives: 2.2.b, 2.2.c · multiple · Applied

A trunk capture contains both untagged user frames and frames with VID 140. The native VLAN is 130 and native tagging is disabled. Select TWO correct interpretations.

- **A.** The presence of untagged frames proves this cannot be a trunk.
- **B.** Untagged ordinary user frames are associated with native VLAN 130.
- **C.** Frames carrying VID 140 are explicitly identified as VLAN 140.
- **D.** Both types must belong to VLAN 130 because it is native.

**Answer: B, C**

A trunk can carry a mix of tagged and untagged data under the stated native policy. Decode each frame according to whether a VLAN tag is present.

**Option explanations**

- **A:** Ordinary native-VLAN traffic can be untagged on an 802.1Q trunk.
- **B:** The receiving trunk uses its native assignment for the untagged data.
- **C:** The tag preserves that separate VLAN identity.
- **D:** Native classification does not override valid nonnative tags.

**Further reading**

- [VLAN Configuration Guide, Cisco IOS XE 17.15.x — Configuring VLAN Trunks](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst9300/software/release/17-15/configuration_guide/vlan/b_1715_vlan_9300_cg/configuring_vlan_trunks.html) — Allowed VLANs on a Trunk; Configuring the Native VLAN for Untagged Traffic

---

## CCNA8-026 · Network Access

Objectives: 2.3 · matching · Applied

Match each LLDP detail field to the inventory fact it supplies. Use every answer once.

1. Local interface Gi1/0/12
2. Port ID Ethernet1/49
3. System name Spine-2
4. Management address 192.0.2.42

- **A.** Remote attachment
- **B.** Peer identity label
- **C.** Local attachment
- **D.** Peer management endpoint

**Answer: 1 → C; 2 → A; 3 → B; 4 → D**

The field names distinguish which end of the cable and which management identity are being described. An advertised address does not itself guarantee reachability.

**Option explanations**

- **A:** The advertised port ID identifies the sender’s connected port.
- **B:** The system name gives the neighbor’s advertised name.
- **C:** The local interface is the switch port receiving the advertisement.
- **D:** The management-address TLV can advertise an address for managing the peer.

**Further reading**

- [Interface and Hardware Components Configuration Guide, Cisco IOS XE 17.15.x — Configuring LLDP, LLDP-MED, and Wired Location Service](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst9300/software/release/17-15/configuration_guide/int_hw/b_1715_int_and_hw_9300_cg/configuring_lldp__lldp_med__and_wired_location_service.html) — LLDP; Enabling LLDP; Monitoring and Maintaining LLDP, LLDP-MED, and Wired Location Service

---

## CCNA8-027 · Network Access

Objectives: 2.4 · single · Challenge

A server forms one LACP bundle, but its two cables terminate on two independent switches with distinct LACP system IDs. No stacking, virtual chassis, or multichassis aggregation feature exists. What is the architectural problem?

- **A.** Changing both switch ports to passive always joins the systems.
- **B.** LACP requires every server to have exactly one NIC.
- **C.** The server is not seeing one coordinated remote aggregation system.
- **D.** Matching the VLAN names alone merges both switch control planes.

**Answer: C**

Physical link count is not enough to define a valid aggregate. Use an explicitly supported shared logical-switch or multichassis design when distributing members across chassis.

**Option explanations**

- **A:** Negotiation mode does not combine independent switch identities.
- **B:** Multiple NICs can form a supported bundle with the correct peer design.
- **C:** A normal bundle expects a compatible logical partner rather than two independent switch systems.
- **D:** Names do not create a shared aggregation system.

**Further reading**

- [Layer 2 Configuration Guide, Cisco IOS XE 17.15.x — Configuring EtherChannels](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst9300/software/release/17-15/configuration_guide/lyr2/b_1715_lyr2_9300_cg/configuring_etherchannels.html) — LACP Modes; EtherChannel Configuration Guidelines; Load Balancing; Layer 3 EtherChannels; Hot-Standby Ports

---

## CCNA8-028 · Network Access

Objectives: 2.4 · multiple · Challenge

A switch hashes EtherChannel traffic only by destination MAC. Many client flows go to different remote IP subnets through the same router MAC. One member is busy while another is mostly idle. Select TWO justified observations.

```text
port-channel load-balance dst-mac

Traffic sample:
Many remote IP destinations
Common Ethernet next hop: 0011.2233.4455
```

- **A.** Different IP destinations can still hash together because their next-hop destination MAC is the same.
- **B.** LACP negotiation mode active guarantees equal byte counts on every member.
- **C.** The idle member must be electrically down even if it is bundled.
- **D.** A supported hash using additional varying fields may improve distribution across these flows.

**Answer: A, D**

Understand the actual hash inputs and the traffic population. A correct aggregate can still distribute a particular workload unevenly.

**Option explanations**

- **A:** The selected hash input is Layer 2 destination, not remote IP identity.
- **B:** Negotiation mode does not schedule equal traffic volumes.
- **C:** Hash distribution can leave a healthy member underused.
- **D:** More diverse inputs can produce different member selections, though equal load is not guaranteed.

**Further reading**

- [Layer 2 Configuration Guide, Cisco IOS XE 17.15.x — Configuring EtherChannels](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst9300/software/release/17-15/configuration_guide/lyr2/b_1715_lyr2_9300_cg/configuring_etherchannels.html) — LACP Modes; EtherChannel Configuration Guidelines; Load Balancing; Layer 3 EtherChannels; Hot-Standby Ports

---

## CCNA8-029 · Network Access

Objectives: 2.5.a · single · Applied

A new switch joins a connected Rapid PVST+ VLAN with a lower bridge ID than the current root. All links exchange valid BPDUs and no root guard applies. Must it wait for the old root to fail before becoming root?

- **A.** No; superior bridge information can trigger a new root election while the old root is healthy.
- **B.** Yes; root election is always nonpreemptive until a power failure.
- **C.** No; because the newest switch always wins regardless of bridge ID.
- **D.** Yes; only the first switch powered on can be root.

**Answer: A**

The root role follows the best available bridge information. Adding a lower-priority candidate can alter the topology during normal operation.

**Option explanations**

- **A:** Spanning tree compares bridge IDs continuously rather than waiting for an incumbent failure.
- **B:** An existing root does not retain its role against superior information by that rule.
- **C:** The lower bridge ID, not novelty, makes this new switch superior.
- **D:** Startup order is not the election criterion.

**Further reading**

- [Layer 2 Configuration Guide, Cisco IOS XE 17.15.x — Configuring Spanning Tree Protocol](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst9300/software/release/17-15/configuration_guide/lyr2/b_1715_lyr2_9300_cg/configuring_spanning_tree_protocol.html) — Spanning-Tree Topology and Bridge Protocol Data Units; Bridge ID, Device Priority, and Extended System ID; (Optional) Configuring a Secondary Root Device

---

## CCNA8-030 · Network Access

Objectives: 2.5.b · single · Challenge

One switch has two ports attached to the same shared Ethernet segment. For a VLAN, one of its ports is designated and the other receives the same switch’s better BPDU through that shared segment. What role can the second port take under RSTP?

- **A.** Root
- **B.** Designated on a second independent segment
- **C.** Backup
- **D.** Alternate through a different upstream bridge

**Answer: C**

Backup and alternate roles have different topology meanings. Backup concerns a redundant attachment by the same bridge to the same shared segment.

**Option explanations**

- **A:** A self-received BPDU does not describe a better upstream path through a different bridge.
- **B:** Both ports attach to the same shared segment, not separate ones.
- **C:** It backs up the same bridge’s designated connection to that shared segment.
- **D:** The scenario explicitly involves the same bridge and shared segment.

**Further reading**

- [Understand Rapid Spanning Tree Protocol (802.1w)](https://www.cisco.com/c/en/us/support/docs/lan-switching/spanning-tree-protocol/24062-146.html) — New Port States and Port Roles — Port States; Alternate and Backup Port Roles

---

## CCNA8-031 · Network Access

Objectives: 2.5.c · single · Applied

Global PortFast default behavior is enabled for nontrunking ports. A verified edge server trunk still undergoes normal nonedge handling because it has no explicit edge-trunk setting. Which interpretation is correct?

- **A.** The server must stop tagging every VLAN before it can have an IP address.
- **B.** Server trunks cannot ever support edge treatment.
- **C.** The global nontrunking default does not by itself enable PortFast on this trunk.
- **D.** Any enabled global PortFast command forces every trunk to be edge.

**Answer: C**

Check the scope of the global default and the effective interface state. Administrative intent does not imply that a trunk has inherited an access-port default.

**Option explanations**

- **A:** VLAN tagging and an interface’s edge transition are separate properties.
- **B:** An actual nonbridging edge trunk can be configured appropriately.
- **C:** A suitable trunk edge requires the appropriate explicit configuration.
- **D:** The stated default specifically covers nontrunking interfaces.

**Further reading**

- [Layer 2 Configuration Guide, Cisco IOS XE 17.15.x — Configuring Optional Spanning-Tree Features](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst9300/software/release/17-15/configuration_guide/lyr2/b_1715_lyr2_9300_cg/configuring_optional_spanning_tree_features.html) — PortFast; Bridge Protocol Data Unit Guard; Bridge Protocol Data Unit Filtering; Root Guard; Loop Guard

---

## CCNA8-032 · Network Access

Objectives: 2.5.d · single · Challenge

An interface has spanning-tree bpduguard enable but PortFast is disabled. A BPDU arrives. Which result is expected from this explicit interface setting?

- **A.** Only superior BPDUs can trigger this interface setting.
- **B.** The feature can only change the port’s VLAN name.
- **C.** BPDU guard can error-disable the port even without PortFast.
- **D.** The BPDU must be ignored because PortFast is disabled.

**Answer: C**

Scope matters: explicit interface BPDU guard differs from the global default tied to operational PortFast. Read both the feature and where it is configured.

**Option explanations**

- **A:** BPDU guard reacts to any BPDU, unlike root guard.
- **B:** It controls protection against unexpected BPDU reception.
- **C:** Interface-level BPDU guard applies independently of PortFast operation.
- **D:** That restriction belongs to the global PortFast-dependent default, not explicit interface enable.

**Further reading**

- [Layer 2 Configuration Guide, Cisco IOS XE 17.15.x — Configuring Optional Spanning-Tree Features](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst9300/software/release/17-15/configuration_guide/lyr2/b_1715_lyr2_9300_cg/configuring_optional_spanning_tree_features.html) — PortFast; Bridge Protocol Data Unit Guard; Bridge Protocol Data Unit Filtering; Root Guard; Loop Guard

---

## CCNA8-033 · Network Access

Objectives: 2.6 · single · Applied

A monitoring team asks for an AP to examine radio channels continuously without serving clients. Operations proposes local mode because local APs can also scan. What is the distinction the review should make?

- **A.** Local mode disables all radios permanently.
- **B.** Monitor mode is another name for local switching into an access VLAN.
- **C.** All AP modes provide identical association behavior.
- **D.** Dedicated monitor mode prioritizes observation, while local mode retains a client-serving role.

**Answer: D**

Select an AP role from the service requirement. Occasional scanning capability does not make every AP mode equivalent.

**Option explanations**

- **A:** Local APs normally use radios to serve clients.
- **B:** That forwarding choice belongs to a client-serving design such as FlexConnect.
- **C:** Dedicated management modes and client-serving modes differ.
- **D:** Background scans in local mode are not the same operating objective as dedicated monitoring.

**Further reading**

- [Cisco Wireless Controller Configuration Guide, Release 8.5 — Managing APs](https://www.cisco.com/c/en/us/td/docs/wireless/controller/8-5/config-guide/b_cg85/managing_aps.html) — AP Modes: client-serving and network management modes

---

## CCNA8-034 · Network Access

Objectives: 2.6 · single · Applied

A FlexConnect branch uses central authentication and local data switching. A firewall change blocks the AP/controller authentication dependency but leaves the local VLAN healthy. Why might new clients fail while some existing local flows continue?

- **A.** Existing clients must have changed themselves into monitor mode.
- **B.** Local switching guarantees all future RADIUS authentications without a server.
- **C.** A healthy local VLAN proves the central authentication server is reachable.
- **D.** Client admission and existing local forwarding have different dependencies.

**Answer: D**

A working local data path is not evidence that every new session can be admitted. Verify both forwarding and authentication under the intended failure scenario.

**Option explanations**

- **A:** Client operation does not turn an infrastructure AP into a monitoring role.
- **B:** Authentication still follows its configured method and dependencies.
- **C:** Local Layer 2 health does not establish the remote AAA path.
- **D:** Local switching can preserve a data path without ensuring a fresh centralized authentication exchange.

**Further reading**

- [Cisco Wireless Controller Configuration Guide, Release 8.10 — FlexConnect](https://www.cisco.com/c/en/us/td/docs/wireless/controller/8-10/config-guide/b_cg810/flexconnect.html) — Configuring the Switch at a Remote Site; Configuring an Access Point for FlexConnect (GUI)
- [Configure FlexConnect with Authentication on Catalyst 9800 WLC](https://www.cisco.com/c/en/us/support/docs/wireless/catalyst-9800-series-wireless-controllers/213921-flexconnect-configuration-with-central-a.html) — Background Information; Policy Profile Configuration

---

## CCNA8-035 · Network Access

Objectives: 2.7 · single · Applied

A single AP cable must carry CAPWAP management in native VLAN 700 and locally switched employee traffic in tagged VLAN 710. Which check directly confirms the switch-side attachment matches that design?

- **A.** Verify operational trunk mode, native VLAN 700, and admission of VLAN 710.
- **B.** Verify only that the interface description says AP.
- **C.** Verify only that the controller has VLAN 710 locally.
- **D.** Verify only that PoE is supplying power.

**Answer: A**

Translate the AP traffic classes into the switch’s actual interface requirements. Verify operational state, not just a descriptive label or power status.

**Option explanations**

- **A:** Those properties correspond to the untagged management and tagged client requirements.
- **B:** A label is not effective interface configuration.
- **C:** The data exits at the AP, so the branch uplink also matters.
- **D:** Power does not prove the intended VLAN carriage.

**Further reading**

- [Cisco Wireless Controller Configuration Guide, Release 8.10 — FlexConnect](https://www.cisco.com/c/en/us/td/docs/wireless/controller/8-10/config-guide/b_cg810/flexconnect.html) — Configuring the Switch at a Remote Site; Configuring an Access Point for FlexConnect (GUI)
- [VLAN Configuration Guide, Cisco IOS XE 17.15.x — Configuring VLAN Trunks](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst9300/software/release/17-15/configuration_guide/vlan/b_1715_vlan_9300_cg/configuring_vlan_trunks.html) — Allowed VLANs on a Trunk; Configuring the Native VLAN for Untagged Traffic

---

## CCNA8-036 · Network Access

Objectives: 2.7 · single · Applied

A local-mode AP receives PoE through its Ethernet cable. An engineer describes PoE, CAPWAP, and 802.1Q as interchangeable ways of connecting the AP. Which correction is accurate?

- **A.** PoE supplies power, CAPWAP carries controller communication, and 802.1Q identifies VLAN traffic.
- **B.** 802.1Q replaces the need for every controller IP address.
- **C.** CAPWAP provides DC electrical power over copper pairs.
- **D.** PoE authenticates wireless users through RADIUS.

**Answer: A**

One cable can support multiple functions, but each function must be verified separately. A powered AP can still have wrong VLAN or controller settings.

**Option explanations**

- **A:** They address different physical and logical requirements on the connection.
- **B:** VLAN tagging does not remove IP dependencies from controller communication.
- **C:** CAPWAP is a network protocol, not a power-delivery standard.
- **D:** Power negotiation does not authenticate WLAN users.

**Further reading**

- [Cisco Wireless Controller Configuration Guide, Release 8.10 — AP Connectivity to Controller](https://www.cisco.com/c/en/us/td/docs/wireless/controller/8-10/config-guide/b_cg810/ap_connectivity_to_cisco_wlc.html) — CAPWAP
- [VLAN Configuration Guide, Cisco IOS XE 17.15.x — Configuring Voice VLANs](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst9300/software/release/17-15/configuration_guide/vlan/b_1715_vlan_9300_cg/configuring_voice_vlans.html) — Cisco IP Phone Voice Traffic; Cisco IP Phone Data Traffic
- [VLAN Configuration Guide, Cisco IOS XE 17.15.x — Configuring VLAN Trunks](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst9300/software/release/17-15/configuration_guide/vlan/b_1715_vlan_9300_cg/configuring_vlan_trunks.html) — Allowed VLANs on a Trunk; Configuring the Native VLAN for Untagged Traffic

---

## CCNA8-037 · Network Access

Objectives: 2.8 · single · Applied

Which management design best supports centrally enforced administrator permissions while protecting remote CLI traffic in transit?

- **A.** Telnet plus a complex TACACS+ password
- **B.** HTTP plus LLDP inventory
- **C.** Console with no login policy exposed through an unauthenticated terminal server
- **D.** SSH for the operator session, with configured TACACS+ AAA for authorization

**Answer: D**

Combine a protected access transport with an appropriate AAA policy. One component does not automatically provide the other’s function.

**Option explanations**

- **A:** Centralized AAA does not encrypt the cleartext Telnet operator session.
- **B:** Neither provides the requested encrypted CLI and command authorization combination.
- **C:** This does not meet the central permission and protected remote-access requirements.
- **D:** SSH protects the session transport while TACACS+ can govern administrative permissions.

**Further reading**

- [Cisco Wireless Controller Configuration Guide, Release 8.10 — AAA Administration](https://www.cisco.com/c/en/us/td/docs/wireless/controller/8-10/config-guide/b_cg810/aaa_administration.html) — Configuring TACACS+ (GUI)
- [Cisco Wireless Controller Configuration Guide, Release 8.10 — Administration of Controller](https://www.cisco.com/c/en/us/td/docs/wireless/controller/8-10/config-guide/b_cg810/administration_of_cisco_wlc.html) — Logging on to the Controller CLI; Enabling Web and Secure Web Modes (GUI); Enabling Web and Secure Web Modes (CLI)

---

## CCNA8-038 · Network Access

Objectives: 2.9 · single · Applied

A Catalyst 9800 Flex profile shows Native VLAN ID 70, while the AP’s adjacent trunk uses native VLAN 80. The intended AP management VLAN is 70. Which correction aligns these GUI and switch settings?

| Configuration | Value |
| --- | --- |
| Flex profile Native VLAN ID | 70 |
| Switch trunk native VLAN | 80 |
| Design AP management VLAN | 70 |

- **A.** Set the adjacent trunk’s native VLAN to the intended VLAN 70 and verify the complete management path.
- **B.** Change only the SSID’s capitalization.
- **C.** Rename the policy profile to Native80 while keeping its values.
- **D.** Assign Bronze QoS to the AP management connection.

**Answer: A**

The controller’s AP-related VLAN assumptions must match the physical switch attachment. A mismatch can break management reachability regardless of WLAN credentials.

**Option explanations**

- **A:** The Flex profile’s native value and the physical switch-port native value must agree.
- **B:** SSID text does not fix untagged management classification.
- **C:** A profile name does not change the actual VLAN setting.
- **D:** QoS selection does not reconcile VLAN IDs.

**Further reading**

- [Configure FlexConnect with Authentication on Catalyst 9800 WLC](https://www.cisco.com/c/en/us/support/docs/wireless/catalyst-9800-series-wireless-controllers/213921-flexconnect-configuration-with-central-a.html) — Background Information; Policy Profile Configuration

---

## CCNA8-039 · Network Access

Objectives: 2.9 · multiple · Applied

A Catalyst 9800 branch AP is intended for FlexConnect, but the applied site tag still has Enable Local Site checked. The branch Flex profile exists but is not applied through a nonlocal site tag. Which TWO changes establish the intended relationship? Select TWO.

- **A.** Associate the intended Flex profile and apply the site tag to the AP.
- **B.** Leave the AP on the local-site tag and change only the profile description.
- **C.** Enable sniffer mode to obtain local client switching.
- **D.** Use a site tag with Enable Local Site unchecked.

**Answer: A, D**

Create the right policy objects and connect them to the AP. Merely having a Flex profile in the configuration is insufficient.

**Option explanations**

- **A:** The profile must be in the AP’s effective configuration path.
- **B:** An unused description change does not alter AP mode or bindings.
- **C:** Sniffer mode does not provide the requested branch WLAN service.
- **D:** That site-tag setting supports the FlexConnect deployment role.

**Further reading**

- [Configure FlexConnect with Authentication on Catalyst 9800 WLC](https://www.cisco.com/c/en/us/support/docs/wireless/catalyst-9800-series-wireless-controllers/213921-flexconnect-configuration-with-central-a.html) — Background Information; Policy Profile Configuration

---

## CCNA8-040 · Network Access

Objectives: 2.9 · single · Applied

A WPA2-PSK WLAN key is intentionally rotated. Newly updated clients connect, but one handheld with the old stored key repeatedly fails the four-way handshake. The SSID, radio policy, and VLAN remain unchanged. What is the targeted correction?

- **A.** Update the handheld’s saved WLAN key to the approved new key.
- **B.** Remove the guest VLAN from every trunk.
- **C.** Change the controller’s management password to the old WLAN key.
- **D.** Increase the WLAN session timeout indefinitely.

**Answer: A**

Use the successful updated clients to narrow the fault. Correct the stale client credential without changing unrelated network policy.

**Option explanations**

- **A:** The old shared key no longer matches the WLAN’s key material.
- **B:** The failure is during authentication/key establishment, before the stated wired changes would help.
- **C:** Administrator credentials do not repair the wireless client PSK mismatch.
- **D:** A timer change does not make different PSKs match.

**Further reading**

- [Cisco Wireless Controller Configuration Guide, Release 8.10 — WLAN Security](https://www.cisco.com/c/en/us/td/docs/wireless/controller/8-10/config-guide/b_cg810/wlan_security.html) — Configuring WPA1+WPA2 (GUI); Configuring Peer-to-Peer Blocking (GUI)

---

## CCNA8-041 · IP Connectivity

Objectives: 3.1.a, 3.1.e, 3.1.f · single · Applied

A monitoring rule treats the first number in brackets as hop count. It raises a 110-hop alarm for the entry below. What should be corrected?

```text
O 172.19.22.0/24 [110/7] via 198.51.100.18
```

- **A.** The router should lower its TTL to 7.
- **B.** The router should convert the O route into an L route.
- **C.** The parser should label 110 as administrative distance and 7 as the OSPF metric.
- **D.** The parser should add 110 and 7 to calculate 117 hops.

**Answer: C**

Operational tooling must preserve the meaning of each field. A faulty interpretation can create false incident reports even when the router is behaving correctly.

**Option explanations**

- **A:** Neither bracket field configures packet TTL.
- **B:** Changing route type would not be a valid repair for a parser error.
- **C:** The bracket format is distance/metric, and OSPF cost is not a universal hop count.
- **D:** These fields represent different concepts and should not be added.

**Further reading**

- [Understand Administrative Distance](https://www.cisco.com/c/en/us/support/docs/ip/border-gateway-protocol-bgp/15986-admin-distance.html) — RIB Route Comparison; Route Installation; Default AD Values

---

## CCNA8-042 · IP Connectivity

Objectives: 3.1.b, 3.1.c, 3.2.a · single · Applied

The only specific route is 172.24.96.0/19; a working default handles all other destinations. Which pair is inside that specific route’s inclusive address range?

- **A.** 172.24.64.1 and 172.24.95.254
- **B.** 172.24.96.1 and 172.24.127.254
- **C.** 172.24.95.254 and 172.24.96.1
- **D.** 172.24.127.254 and 172.24.128.1

**Answer: B**

The route 172.24.96.0/19 spans 172.24.96.0 through 172.24.127.255. Both 172.24.96.1 and 172.24.127.254 are inside that inclusive range.

**Option explanations**

- **A:** Both belong to the preceding /19 block.
- **B:** The /19 spans third octets 96 through 127.
- **C:** The first address is just below the start of the prefix.
- **D:** The second address is just beyond the prefix’s end.

**Further reading**

- [RFC 1812: Requirements for IP Version 4 Routers](https://www.rfc-editor.org/rfc/rfc1812.html) — 5.2.4 Determining the Next Hop Address
- [Configure Route Selection for Routers](https://www.cisco.com/c/en/us/support/docs/ip/enhanced-interior-gateway-routing-protocol-eigrp/8651-21.html) — Build the Routing Table; Make Forwarding Decisions

---

## CCNA8-043 · IP Connectivity

Objectives: 3.2.b, 3.2.a · multiple · Challenge

For 10.218.0.0/16, a valid static has distance 250 and a valid OSPF candidate has distance 110. Separately, a valid static for 10.218.7.0/24 has distance 250. Which two statements are correct? Select two.

- **A.** OSPF can supply the installed /16.
- **B.** The /16 static and OSPF route must both be used equally.
- **C.** The /24 static can still forward traffic to 10.218.7.30.
- **D.** The /24 is rejected solely because its distance exceeds the /16’s distance.

**Answer: A, C**

First compare candidates for each exact prefix, then perform the destination lookup across the installed prefixes. These are separate decisions.

**Option explanations**

- **A:** For the identical /16, OSPF has the lower administrative distance.
- **B:** Their unequal distances do not create an equal-preference pair.
- **C:** That distinct prefix can install and is more specific for the host.
- **D:** Administrative-distance competition is for the same destination prefix.

**Further reading**

- [Understand Administrative Distance](https://www.cisco.com/c/en/us/support/docs/ip/border-gateway-protocol-bgp/15986-admin-distance.html) — RIB Route Comparison; Route Installation; Default AD Values
- [Configure Route Selection for Routers](https://www.cisco.com/c/en/us/support/docs/ip/enhanced-interior-gateway-routing-protocol-eigrp/8651-21.html) — Build the Routing Table; Make Forwarding Decisions

---

## CCNA8-044 · IP Connectivity

Objectives: 3.2.c · single · Challenge

The table shows every outgoing cost on two complete intra-area OSPF paths to the same LAN. Which minimum change to Path A’s final link makes Path B strictly preferable?

| Path | Outgoing costs, in order |
| --- | --- |
| A | 15, 15, 5 |
| B | 20, 20 |

- **A.** Raise the final cost from 5 to 10.
- **B.** Raise the final cost from 5 to 11.
- **C.** Lower the final cost from 5 to 1.
- **D.** Change the OSPF process number from 1 to 2.

**Answer: B**

Distinguish crossing a threshold from merely reaching equal cost. The requested strictly preferred alternate requires Path A’s total to exceed 40.

**Option explanations**

- **A:** That makes both paths cost 40, permitting a tie rather than strict preference.
- **B:** Path A becomes 41, just greater than Path B’s 40.
- **C:** That makes Path A even cheaper at 31.
- **D:** The local process number is not a cost contribution.

**Further reading**

- [RFC 2328: OSPF Version 2](https://www.rfc-editor.org/rfc/rfc2328.html) — 9.4 Electing the Designated Router; 10 The Neighbor Data Structure; 16 Calculation of the routing table

---

## CCNA8-045 · IP Connectivity

Objectives: 3.1.d · single · Applied

A packet’s route resolves to adjacent router 192.0.2.62, but ARP for .62 receives no reply on the correct up Ethernet segment. What is the immediate forwarding dependency still missing?

- **A.** A larger administrative distance for the destination route
- **B.** A lower OSPF router ID at the final server
- **C.** An ARP reply from the remote destination several routed hops away
- **D.** A usable Layer 2 adjacency to the selected next hop

**Answer: D**

A route lookup can identify the correct next hop while adjacency resolution still fails. Continue troubleshooting at the selected Ethernet link.

**Option explanations**

- **A:** Preference changes do not directly resolve the selected neighbor’s MAC.
- **B:** End servers are not assigned routing identities to satisfy this ARP exchange.
- **C:** The selected adjacent router, not the remote host, is the local frame destination.
- **D:** The router cannot build the normal unicast Ethernet frame to that neighbor without resolution.

**Further reading**

- [RFC 1812: Requirements for IP Version 4 Routers](https://www.rfc-editor.org/rfc/rfc1812.html) — 5.2.4 Determining the Next Hop Address
- [Configure a Next Hop IP Address for Static Routes](https://www.cisco.com/c/en/us/support/docs/dial-access/floating-static-route/118263-technote-nexthop-00.html) — Background Information; Floating Static Route Example

---

## CCNA8-046 · IP Connectivity

Objectives: 3.3.b · single · Challenge

The two adjacent warehouse networks shown must be represented without covering any other /24. Can a single /23 do this?

| Network |
| --- |
| 10.119.7.0/24 |
| 10.119.8.0/24 |

- **A.** Yes; any adjacent /24s can always be summarized as a /23.
- **B.** Yes; 10.119.8.0/23 covers 7 and 8.
- **C.** Yes; 10.119.7.0/23 is an aligned prefix covering exactly both.
- **D.** No; the pair straddles a /23 boundary, so two /24 routes are needed for exact coverage.

**Answer: D**

Summary size and boundary alignment must both be correct. Here a broader summary would include unwanted destinations, so exact coverage needs two entries.

**Option explanations**

- **A:** Contiguity alone is insufficient; binary alignment also matters.
- **B:** That /23 covers 8 and 9.
- **C:** An odd third-octet value is not the network boundary of a /23.
- **D:** Aligned /23 blocks pair 6 with 7 and 8 with 9.

**Further reading**

- [RFC 1812: Requirements for IP Version 4 Routers](https://www.rfc-editor.org/rfc/rfc1812.html) — 5.2.4 Determining the Next Hop Address
- [Configure a Next Hop IP Address for Static Routes](https://www.cisco.com/c/en/us/support/docs/dial-access/floating-static-route/118263-technote-nexthop-00.html) — Background Information; Floating Static Route Example

---

## CCNA8-047 · IP Connectivity

Objectives: 3.3.a, 3.3.d · single · Applied

A branch’s primary default is tied to a tracking object. The object changes to Down and the primary default is withdrawn. A higher-distance default through an independent working interface is valid. Which result is expected?

- **A.** The valid backup default can become active.
- **B.** The primary default must remain because its physical interface is still up.
- **C.** The backup remains forbidden because its distance is not 1.
- **D.** Both interfaces must be administratively shut down first.

**Answer: A**

The trigger is the effective route withdrawal, whether caused by interface loss or a supported tracking policy. Confirm both the control-plane transition and the surviving data path.

**Option explanations**

- **A:** Tracking has removed the preferred candidate, leaving the backup eligible.
- **B:** The premise explicitly states tracking withdrew it.
- **C:** Higher valid distances can win after preferred candidates disappear.
- **D:** A tracked route withdrawal does not require shutting all interfaces.

**Further reading**

- [Configure a Next Hop IP Address for Static Routes](https://www.cisco.com/c/en/us/support/docs/dial-access/floating-static-route/118263-technote-nexthop-00.html) — Background Information; Floating Static Route Example
- [Understand Administrative Distance](https://www.cisco.com/c/en/us/support/docs/ip/border-gateway-protocol-bgp/15986-admin-distance.html) — RIB Route Comparison; Route Installation; Default AD Values

---

## CCNA8-048 · IP Connectivity

Objectives: 3.3.c · single · Applied

A remote IPv4 management loopback is 203.0.113.199/32. The router has no default or covering network route to it. A host static through reachable 192.0.2.66 is added. Which test most directly verifies the narrow route’s intended destination?

- **A.** Count the number of static commands and assume all are active.
- **B.** Probe only adjacent 192.0.2.66 and declare the remote loopback working.
- **C.** Probe 203.0.113.200 and expect the /32 to cover it.
- **D.** Look up and probe 203.0.113.199 using the intended source path.

**Answer: D**

Verify the target actually covered by the route. Use an appropriate source address because remote return routing can differ by source network.

**Option explanations**

- **A:** Configuration count is not operational verification of the selected destination.
- **B:** The neighbor probe does not test forwarding or return routing to the remote loopback.
- **C:** That neighboring address is outside the host route.
- **D:** This tests the exact host covered by the new /32 and its required return path.

**Further reading**

- [Local Host Routes Installed in the Routing Table on Cisco IOS and Cisco IOS-XR](https://www.cisco.com/c/en/us/support/docs/ip/ip-routing/116264-technote-ios-00.html) — Cisco IOS Local Routes; Manually Configured Host Routes
- [RFC 1812: Requirements for IP Version 4 Routers](https://www.rfc-editor.org/rfc/rfc1812.html) — 5.2.4 Determining the Next Hop Address

---

## CCNA8-049 · IP Connectivity

Objectives: 3.3.b · multiple · Applied

A router has an IPv6 static to 2001:db8:830::/64 through global next hop 2001:db8:ffff::2. A more specific resolving route leads to an up IPv6 transit interface. Which two conditions are required for valid recursive installation? Select two.

- **A.** The next hop must be the numerically largest IPv6 address in the router.
- **B.** The route does not depend on itself to resolve its own next hop.
- **C.** The resolution chain reaches a usable IPv6 output interface.
- **D.** The IPv6 route’s prefix must equal the OSPFv2 router ID.

**Answer: B, C**

Recursive validity concerns the dependency chain, not just the existence of a next-hop string in configuration. A resolving route must lead to an actual usable exit.

**Option explanations**

- **A:** Address magnitude does not establish route validity.
- **B:** Self-recursion cannot establish independent forwarding reachability.
- **C:** The recursive route needs a real interface path at the end of resolution.
- **D:** The two identifiers belong to different mechanisms and formats.

**Further reading**

- [IPv6 Routing: Static Routing — Cisco IOS XE 17.x](https://www.cisco.com/c/en/us/td/docs/routers/ios/config/17-x/ip-routing/b-ip-routing/m_ip6-route-static-xe.html) — Recursive Static Routes; Fully Specified Static Routes; Floating Static Routes

---

## CCNA8-050 · IP Connectivity

Objectives: 3.3.d · single · Challenge

A backup /24 points to a next hop whose only resolving route also depends on the primary WAN. What should be checked before accepting the backup as protection against that WAN failing?

- **A.** Whether the backup has more characters in its description
- **B.** Whether the backup’s destination is changed to the neighbor’s address
- **C.** Whether both route metrics are written with leading zeros
- **D.** Whether the backup next hop remains resolvable after the primary WAN is removed

**Answer: D**

Resolve the backup’s dependencies under the failure condition, not only in the healthy topology. A configured alternate can conceal the same failure dependency as the primary.

**Option explanations**

- **A:** Description length has no bearing on path independence.
- **B:** That would change the routing requirement rather than establish resilience.
- **C:** Numeric formatting does not alter dependency or preference.
- **D:** The nominal alternate must not depend on the failed primary for its own reachability.

**Further reading**

- [Configure a Next Hop IP Address for Static Routes](https://www.cisco.com/c/en/us/support/docs/dial-access/floating-static-route/118263-technote-nexthop-00.html) — Background Information; Floating Static Route Example
- [IPv6 Routing: Static Routing — Cisco IOS XE 17.x](https://www.cisco.com/c/en/us/td/docs/routers/ios/config/17-x/ip-routing/b-ip-routing/m_ip6-route-static-xe.html) — Recursive Static Routes; Fully Specified Static Routes; Floating Static Routes

---

## CCNA8-051 · IP Connectivity

Objectives: 3.3.a, 3.1.g · single · Applied

A router has separate IPv4 and IPv6 forwarding tables. An IPv4 default is installed, but no IPv6 default or matching specific IPv6 route exists. What happens to an otherwise valid unmatched IPv6 transit packet?

- **A.** It lacks an IPv6 forwarding route; the IPv4 default does not cover it.
- **B.** It uses the IPv4 default by converting its destination automatically.
- **C.** It is broadcast on every IPv6-enabled interface.
- **D.** It is delivered to the OSPFv2 router ID.

**Answer: A**

Dual-stack reachability must be validated per address family. Success of one family’s default does not establish the other’s forwarding coverage.

**Option explanations**

- **A:** Routing entries are scoped to their address family.
- **B:** Ordinary dual-stack routing does not imply automatic address-family translation.
- **C:** IPv6 routing does not discover an exit by flooding arbitrary unicast packets.
- **D:** A router ID is not a fallback IPv6 destination.

**Further reading**

- [IPv6 Routing: Static Routing — Cisco IOS XE 17.x](https://www.cisco.com/c/en/us/td/docs/routers/ios/config/17-x/ip-routing/b-ip-routing/m_ip6-route-static-xe.html) — Recursive Static Routes; Fully Specified Static Routes; Floating Static Routes
- [RFC 1812: Requirements for IP Version 4 Routers](https://www.rfc-editor.org/rfc/rfc1812.html) — 5.2.4 Determining the Next Hop Address

---

## CCNA8-052 · IP Connectivity

Objectives: 3.4.a · matching · Applied

Match each OSPF packet function during adjacency formation to its packet type.

1. Discover a peer and list neighbors heard on the link
2. Send summaries that let a neighbor compare known link-state information
3. Ask for a particular LSA identified as missing
4. Deliver the requested LSA contents

- **A.** Link State Update
- **B.** Hello
- **C.** Link State Request
- **D.** Database Description

**Answer: 1 → B; 2 → D; 3 → C; 4 → A**

Neighbor synchronization uses different packet roles rather than sending the entire routing table in each Hello. Follow the appropriate packet type when isolating a stalled stage.

**Option explanations**

- **A:** Updates carry LSAs, including information sent in response to requests.
- **B:** Hello packets discover peers and maintain the bidirectional neighbor relationship.
- **C:** Requests identify specific missing or newer LSAs needed from a neighbor.
- **D:** Database Description packets summarize database contents during exchange.

**Further reading**

- [RFC 2328: OSPF Version 2](https://www.rfc-editor.org/rfc/rfc2328.html) — 9.4 Electing the Designated Router; 10 The Neighbor Data Structure; 16 Calculation of the routing table
- [Understand OSPF Neighbor States](https://www.cisco.com/c/en/us/support/docs/ip/open-shortest-path-first-ospf/13685-13.html) — OSPF Neighbor States

---

## CCNA8-053 · IP Connectivity

Objectives: 3.4.a · single · Applied

Two broadcast interfaces share a switch but are addressed 10.90.0.1/24 and 10.90.1.2/24. All OSPF parameters otherwise match. They have no secondary addresses. What addressing issue must be repaired for this intended shared-subnet adjacency?

- **A.** Both interfaces use a /24 mask.
- **B.** The last octets are not identical.
- **C.** The interface addresses are in different IPv4 subnets.
- **D.** Both addresses are privately allocated.

**Answer: C**

A common switch is only Layer 2 evidence. The intended IP subnet relationship must also be correct.

**Option explanations**

- **A:** A /24 is valid; using different /24 network portions is the problem.
- **B:** Different host addresses are required; the subnet mismatch is the issue.
- **C:** Broadcast OSPF neighbors on this intended link need compatible same-subnet addressing.
- **D:** Private IPv4 space is usable for OSPF transit networks.

**Further reading**

- [Troubleshoot OSPF Neighbor Problems](https://www.cisco.com/c/en/us/support/docs/ip/open-shortest-path-first-ospf/13699-29.html) — No State Revealed; Neighbors Stuck in Exstart/Exchange State

---

## CCNA8-054 · IP Connectivity

Objectives: 3.4.a, 3.4.c · single · Applied

Five routers share a healthy OSPF broadcast segment. One is DR, one BDR, and three are DROTHER. At convergence, how many Full neighbor relationships should the DR have on this segment?

| Role | Number of routers |
| --- | --- |
| DR | 1 |
| BDR | 1 |
| DROTHER | 3 |

- **A.** Five
- **B.** One
- **C.** Four
- **D.** Two

**Answer: C**

Count peers from the observer’s role. The DR’s expected adjacency count differs from a DROTHER’s count on the same healthy LAN.

**Option explanations**

- **A:** A router does not list itself as its own Full neighbor.
- **B:** That would count only the BDR and omit the DROTHER adjacencies.
- **C:** The DR forms Full adjacencies with every other participating router on this segment.
- **D:** The two-Full-neighbor pattern applies to a DROTHER here, not the DR.

**Further reading**

- [RFC 2328: OSPF Version 2](https://www.rfc-editor.org/rfc/rfc2328.html) — 9.4 Electing the Designated Router; 10 The Neighbor Data Structure; 16 Calculation of the routing table
- [Understand OSPF Neighbor States](https://www.cisco.com/c/en/us/support/docs/ip/open-shortest-path-first-ospf/13685-13.html) — OSPF Neighbor States

---

## CCNA8-055 · IP Connectivity

Objectives: 3.4.b · single · Applied

An OSPF point-to-point link has failed Hellos because an ACL blocks destination 224.0.0.5. Why can permitting only 224.0.0.6 be insufficient for normal OSPF discovery on this link?

- **A.** 224.0.0.6 is the IPv4 default-route address.
- **B.** OSPF Hellos use the AllSPFRouters group 224.0.0.5 here.
- **C.** Multicast group permissions never affect routing protocols.
- **D.** Point-to-point OSPF uses only broadcast address 255.255.255.255.

**Answer: B**

Permit the actual control packets used by the chosen link type. A rule aimed only at a broadcast-segment elected-router group can miss normal Hello discovery.

**Option explanations**

- **A:** It is an OSPF multicast group, not 0.0.0.0/0.
- **B:** Permitting only the designated-router group does not permit these Hello packets.
- **C:** ACLs can block required OSPF multicast traffic.
- **D:** Normal point-to-point OSPF uses the stated multicast discovery group.

**Further reading**

- [RFC 2328: OSPF Version 2](https://www.rfc-editor.org/rfc/rfc2328.html) — 9.4 Electing the Designated Router; 10 The Neighbor Data Structure; 16 Calculation of the routing table
- [Troubleshoot OSPF Neighbor Problems](https://www.cisco.com/c/en/us/support/docs/ip/open-shortest-path-first-ospf/13699-29.html) — No State Revealed; Neighbors Stuck in Exstart/Exchange State

---

## CCNA8-056 · IP Connectivity

Objectives: 3.4.c · single · Applied

An OSPF broadcast segment starts with only two routers, both explicitly set to priority 0. They reach 2-Way but no DR/BDR appears. What is the key design defect?

- **A.** The OSPF process numbers must both be 255.
- **B.** The IP subnet must have at least 254 usable hosts.
- **C.** No router is eligible to provide DR/BDR service on this broadcast segment.
- **D.** The highest router ID should ignore priority zero and force itself to DR.

**Answer: C**

Excluding every participant from an elected role is different from excluding only selected routers. For a dedicated two-router design, a consistent point-to-point network type is another deliberate option.

**Option explanations**

- **A:** Local process numbers are unrelated to election eligibility.
- **B:** Subnet size does not create an eligible designated router.
- **C:** Both interfaces were excluded from election by priority zero.
- **D:** Zero priority is an eligibility exclusion, not merely a low ranking.

**Further reading**

- [RFC 2328: OSPF Version 2](https://www.rfc-editor.org/rfc/rfc2328.html) — 9.4 Electing the Designated Router; 10 The Neighbor Data Structure; 16 Calculation of the routing table

---

## CCNA8-057 · IP Connectivity

Objectives: 3.4.c · single · Applied

A new router is added to a healthy broadcast LAN with the goal of becoming DR immediately. It has the highest priority, but no existing router fails or resets. Which premise in the goal is wrong?

- **A.** The DR must always have the smallest router ID.
- **B.** Only a host can become DR.
- **C.** A higher-priority late arrival does not automatically preempt the incumbent DR.
- **D.** Router priority is always ignored during any OSPF election.

**Answer: C**

Changing a future-election preference is not the same as requesting immediate role migration. Any planned role transition needs an appropriate maintenance procedure.

**Option explanations**

- **A:** Higher router ID is preferred when an eligible initial-election priority tie is compared.
- **B:** DR is a router role.
- **C:** Existing healthy role ownership is preserved by OSPF’s nonpreemptive election behavior.
- **D:** Priority matters in eligible election comparisons; incumbency changes the timing result.

**Further reading**

- [RFC 2328: OSPF Version 2](https://www.rfc-editor.org/rfc/rfc2328.html) — 9.4 Electing the Designated Router; 10 The Neighbor Data Structure; 16 Calculation of the routing table

---

## CCNA8-058 · IP Connectivity

Objectives: 3.4.d · single · Foundation

A device’s name is changed from BRANCH-OLD to BRANCH-NEW while its OSPF router ID and interfaces remain unchanged. What should this rename alone do to the OSPF identity?

- **A.** Convert the router ID into the hostname’s ASCII bytes.
- **B.** Automatically select the highest neighbor’s router ID.
- **C.** Leave the OSPF router ID unchanged.
- **D.** Create a second OSPF router with the old name.

**Answer: C**

Human-readable names and routing identifiers are different configuration elements. Verify the actual router ID when investigating an identity-related event.

**Option explanations**

- **A:** OSPF does not derive the ID by encoding the hostname.
- **B:** A hostname change does not trigger that selection.
- **C:** The hostname is not the 32-bit identifier used for OSPF router identity.
- **D:** Renaming the device does not create a second protocol participant.

**Further reading**

- [Configuring OSPF — IP Routing: OSPF Configuration Guide](https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/iproute_ospf/configuration/xe-16/iro-xe-16-book/iro-cfg.html) — Enabling OSPF; Configuring OSPF Interface Parameters

---

## CCNA8-059 · IP Connectivity

Objectives: 3.4.a · single · Applied

A router-level OSPF network statement matches none of the device’s local interface addresses. No interface-level OSPF activation exists. What can that statement accomplish by itself?

- **A.** It creates an Ethernet interface with a matching address.
- **B.** It installs a static route toward every remote prefix in that range.
- **C.** It forces every neighbor to move into the named area.
- **D.** It does not activate an interface merely because a remote destination falls in that range.

**Answer: D**

Understand the command’s object: local interface participation. The address range is a selector, not an advertisement of arbitrary nonexistent connectivity.

**Option explanations**

- **A:** The statement does not create physical interfaces or assign addresses.
- **B:** OSPF activation syntax is not static-route configuration.
- **C:** A local unmatched statement does not reconfigure peers.
- **D:** The network statement selects local interfaces for OSPF participation.

**Further reading**

- [Configuring OSPF — IP Routing: OSPF Configuration Guide](https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/iproute_ospf/configuration/xe-16/iro-xe-16-book/iro-cfg.html) — Enabling OSPF; Configuring OSPF Interface Parameters

---

## CCNA8-060 · IP Connectivity

Objectives: 3.2.c, 3.4.a · multiple · Applied

A cost audit finds that one area-0 router uses reference bandwidth 100 Mb/s and another uses 10,000 Mb/s, with automatic costs. Which two actions or conclusions are appropriate? Select two.

- **A.** Check and align the reference-bandwidth policy for consistent cost interpretation.
- **B.** Assume the mismatch prevents Hello adjacency by itself.
- **C.** Set identical router IDs to make the costs comparable.
- **D.** Verify resulting routes after any correction converges.

**Answer: A, D**

Metric consistency and adjacency compatibility are different checks. A network can form neighbors yet implement an unintended cost model.

**Option explanations**

- **A:** Different references can assign different automatic costs to links of the same bandwidth.
- **B:** Reference bandwidth is not a required matching Hello parameter.
- **C:** Duplicate IDs create a separate fault and do not align metric calculation.
- **D:** Changing effective costs can change shortest paths.

**Further reading**

- [Configuring OSPF — IP Routing: OSPF Configuration Guide](https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/iproute_ospf/configuration/xe-16/iro-xe-16-book/iro-cfg.html) — Enabling OSPF; Configuring OSPF Interface Parameters
- [RFC 2328: OSPF Version 2](https://www.rfc-editor.org/rfc/rfc2328.html) — 9.4 Electing the Designated Router; 10 The Neighbor Data Structure; 16 Calculation of the routing table

---

## CCNA8-061 · IP Connectivity

Objectives: 3.4.a · single · Applied

An engineer sees Init briefly, then 2-Way, then ExStart, Exchange, Loading and Full after enabling a point-to-point link. What is the best interpretation of this recorded sequence?

- **A.** Full means the router has exhausted its routing-table capacity.
- **B.** It is consistent with normal progression from discovery to synchronized adjacency.
- **C.** Loading means the router must be rebooting its operating system.
- **D.** Any observation of Init proves permanent failure.

**Answer: B**

Time context matters when interpreting operational states. A stable stalled stage deserves investigation; a successful transition through stages does not indicate the same fault.

**Option explanations**

- **A:** Full describes adjacency completeness, not memory utilization.
- **B:** The states represent successive neighbor formation and database synchronization steps.
- **C:** OSPF Loading is a database synchronization state, not the device boot process.
- **D:** Transient early states are expected while a neighbor forms.

**Further reading**

- [Understand OSPF Neighbor States](https://www.cisco.com/c/en/us/support/docs/ip/open-shortest-path-first-ospf/13685-13.html) — OSPF Neighbor States

---

## CCNA8-062 · IP Connectivity

Objectives: 3.5 · single · Applied

An HSRP active advertises a 10-second hold time. The standby’s last accepted Hello from it was at time 0, and no further Hellos arrive. Ignoring processing delay, when does that liveness evidence expire?

- **A.** Only after every host clears its ARP cache
- **B.** Immediately at time 0
- **C.** At exactly one second because HSRP is always instantaneous
- **D.** At about 10 seconds after the last accepted Hello

**Answer: D**

This identifies the protocol detection point, not a guarantee that all traffic has recovered at that instant. Role transition and Layer 2/data-path convergence add separate work.

**Option explanations**

- **A:** Host ARP expiration is not the standby’s active-peer hold timer.
- **B:** One missing next packet does not erase the configured hold interval.
- **C:** Detection is governed by the stated timers, not a universal one-second rule.
- **D:** The hold time defines how long the last active Hello remains valid.

**Further reading**

- [Understand the Hot Standby Router Protocol Features and Functionality](https://www.cisco.com/c/en/us/support/docs/ip/hot-standby-router-protocol-hsrp/9234-hsrpguidetoc.html) — HSRP Background and Operations; HSRP Operation

---

## CCNA8-063 · IP Connectivity

Objectives: 3.5 · single · Challenge

Both redundant gateway routers connect the user VLAN through one access switch. That switch loses power and every user-to-gateway link is lost. What does FHRP alone provide for those disconnected users?

- **A.** It cannot restore their missing Layer 2 path to either gateway.
- **B.** It creates a wireless backup path automatically.
- **C.** It moves every user’s cable to the surviving router.
- **D.** It guarantees service because two router chassis remain powered.

**Answer: A**

Gateway redundancy is only useful while a usable path to a gateway remains. Design and test common access dependencies as well as router failures.

**Option explanations**

- **A:** A shared access-switch failure removes the users’ connectivity to both possible first hops.
- **B:** FHRP does not create alternative physical media.
- **C:** A control protocol cannot change the physical cabling.
- **D:** Powered routers do not help users whose common access path is gone.

**Further reading**

- [Understand the Hot Standby Router Protocol Features and Functionality](https://www.cisco.com/c/en/us/support/docs/ip/hot-standby-router-protocol-hsrp/9234-hsrpguidetoc.html) — HSRP Background and Operations; HSRP Operation
- [RFC 9568: Virtual Router Redundancy Protocol (VRRP) Version 3 for IPv4 and IPv6](https://www.rfc-editor.org/rfc/rfc9568.html) — 1 Introduction; 2 Required Features; 6 Protocol State Machine

---

## CCNA8-064 · IP Connectivity

Objectives: 3.5 · single · Applied

The virtual gateway remains reachable during a maintenance test, but the failed router’s unique physical interface address does not respond. What is the most reasonable interpretation?

- **A.** The virtual address is now the subnet broadcast address.
- **B.** The test must have failed because every physical address must transfer.
- **C.** The virtual service can survive while that failed physical endpoint remains unavailable.
- **D.** All hosts must have changed their default gateways.

**Answer: C**

Use the service identity as the failover target while retaining physical addresses for device-specific management. Those tests answer different questions.

**Option explanations**

- **A:** Reachability does not imply that address transformation.
- **B:** Unique router interface addresses are not normally transferred by the group.
- **C:** FHRP transfers virtual ownership, not necessarily the failed router’s unique address.
- **D:** A working virtual gateway is intended to avoid that change.

**Further reading**

- [Understand the Hot Standby Router Protocol Features and Functionality](https://www.cisco.com/c/en/us/support/docs/ip/hot-standby-router-protocol-hsrp/9234-hsrpguidetoc.html) — HSRP Background and Operations; HSRP Operation

---

## CCNA8-065 · IP Connectivity

Objectives: 3.1.g, 3.3.a · single · Applied

A route audit finds two default commands in configuration but only one gateway of last resort in the operational table. The commands have different distances and valid next hops. What is the best interpretation?

- **A.** One default command must have been corrupted because two are never allowed.
- **B.** The default with the longest textual IP address must be selected.
- **C.** The higher-distance default must be forwarding all traffic invisibly.
- **D.** The operational table can select the preferred default while retaining the other as a configured candidate.

**Answer: D**

Reconcile intended redundancy with selected operational state. Then test that the unselected candidate becomes usable under the relevant failure condition.

**Option explanations**

- **A:** Multiple primary and floating static defaults are a normal design.
- **B:** String length is not an administrative preference rule.
- **C:** Higher-distance candidacy does not imply active use.
- **D:** Configuration inventory and the current selected fallback are different views.

**Further reading**

- [Understand Administrative Distance](https://www.cisco.com/c/en/us/support/docs/ip/border-gateway-protocol-bgp/15986-admin-distance.html) — RIB Route Comparison; Route Installation; Default AD Values
- [Configure a Next Hop IP Address for Static Routes](https://www.cisco.com/c/en/us/support/docs/dial-access/floating-static-route/118263-technote-nexthop-00.html) — Background Information; Floating Static Route Example

---

## CCNA8-066 · IP Services

Objectives: 4.1 · single · Applied

The constructed NAT configuration and observations are collected during a failed connection to an external server. Which statement is supported without assuming a cause beyond the evidence?

| Observation | Result |
| --- | --- |
| Client connection target | 192.0.2.81:443 |
| Inside local address | 10.81.0.16 |
| Allocated inside global address | 198.51.100.116 |
| Application response | None before timeout |

- **A.** DNS must be broken even though the test uses a numeric server address.
- **B.** The TCP application must be healthy because the source address was translated.
- **C.** The client obtained a translation, but successful NAT allocation alone does not prove application reachability.
- **D.** The NAT pool is exhausted for this client because a translation exists.

**Answer: C**

A NAT table is evidence of address translation state, not a complete end-to-end health check. Follow the translated packet and its return path to investigate the remaining failure.

**Option explanations**

- **A:** The specified numeric-address test does not depend on resolving a name.
- **B:** Translation state does not verify completion of an application exchange.
- **C:** A translation can exist while routing, filtering, or the remote service still prevents success.
- **D:** The observation shows that this client already has a mapping.

**Further reading**

- [IP Addressing Configuration Guide, Cisco IOS XE 17.x — Configuring NAT for IP Address Conservation](https://www.cisco.com/c/en/us/td/docs/routers/ios/config/17-x/ip-addressing/b-ip-addressing/m_iadnat-addr-consv-xe.html) — Inside source address translation; static and dynamic translations; monitoring NAT

---

## CCNA8-067 · IP Services

Objectives: 4.2 · single · Challenge

An isolated training network has no external time reference. Its router is deliberately configured with ntp master 8, and clients synchronize to it. Which statement accurately describes the result?

- **A.** The clients can share a common time source, but this setup does not establish accuracy against an external reference.
- **B.** The command automatically obtains GPS time over the Internet.
- **C.** Stratum 8 guarantees that the clock is accurate to eight microseconds.
- **D.** Clients cannot synchronize unless the master has a physically attached atomic clock.

**Answer: A**

Consistency among clients and accuracy against real-world reference time are different properties. This explicit local authority can provide consistency while inheriting the local clock's error and drift.

**Option explanations**

- **A:** The chosen authority is the router's local clock without external synchronization.
- **B:** No external reference or Internet access exists in the scenario.
- **C:** Stratum is not a fixed accuracy value in microseconds.
- **D:** The local-clock master mode exists for a configured local authority.

**Further reading**

- [Setting Time and Calendar Services](https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/bsm/configuration/15-mt/bsm-15-mt-book/bsm-time-calendar-set.html) — Network Time Protocol; configuring NTP associations; monitoring NTP

---

## CCNA8-068 · IP Services

Objectives: 4.2 · single · Applied

Two NTP-synchronized routers show local clock displays exactly eight hours apart. One is configured for UTC and the other for UTC+8; their UTC timestamps agree. Which action is appropriate?

- **A.** Treat the difference as time-zone presentation, and compare normalized timestamps.
- **B.** Move one NTP clock eight hours so both local displays match without changing zones.
- **C.** Force both devices to stratum 1 to eliminate the display offset.
- **D.** Disable NTP on the UTC+8 device because NTP supports only local time.

**Answer: A**

A display offset need not indicate clock error. Normalize the time zone when correlating events and avoid changing synchronized time to compensate for intentional presentation settings.

**Option explanations**

- **A:** Their underlying UTC time is already consistent.
- **B:** That would corrupt the currently correct UTC time.
- **C:** Stratum selection does not change time-zone formatting.
- **D:** NTP time synchronization is independent of the chosen local display offset.

**Further reading**

- [Setting Time and Calendar Services](https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/bsm/configuration/15-mt/bsm-15-mt-book/bsm-time-calendar-set.html) — Network Time Protocol; configuring NTP associations; monitoring NTP
- [RFC 5905 — Network Time Protocol Version 4: Protocol and Algorithms Specification](https://www.rfc-editor.org/rfc/rfc5905.html) — 7 NTP protocol data structures; 9 Peer process; 11 System process

---

## CCNA8-069 · IP Services

Objectives: 4.3 · single · Applied

A client sends a DNS query for misspelledhost.example and receives a valid NXDOMAIN response from its configured resolver. Which distinction is correct?

- **A.** NXDOMAIN guarantees that every other name in example also fails.
- **B.** NXDOMAIN proves that the DNS server is unreachable.
- **C.** NXDOMAIN assigns the client a new IPv4 address.
- **D.** The resolver answered that the queried name does not exist; this differs from receiving no response.

**Answer: D**

An explicit negative name result and a timeout lead to different investigations. Check spelling and authoritative name data for this case instead of assuming the resolver could not be contacted.

**Option explanations**

- **A:** The result concerns the queried name, not every name in the namespace.
- **B:** A received DNS response contradicts total resolver unreachability.
- **C:** DNS error replies do not allocate DHCP leases.
- **D:** NXDOMAIN is an explicit DNS result rather than a timeout.

**Further reading**

- [RFC 1035 — Domain Names - Implementation and Specification](https://www.rfc-editor.org/rfc/rfc1035.html) — 3.3 Standard resource records; 4.1 Message format; 4.2 Transport

---

## CCNA8-070 · IP Services

Objectives: 4.4 · single · Challenge

A 10 Gb/s interface is monitored once per minute using a 32-bit octet counter. Multiple wraps can occur between samples, making the calculated traffic rate ambiguous. The agent and manager support 64-bit interface counters. What change best addresses this counter-width issue?

- **A.** Treat every sample as though exactly one wrap occurred.
- **B.** Poll the corresponding high-capacity 64-bit octet counter.
- **C.** Convert the final 32-bit value to a longer decimal string.
- **D.** Replace the utilization counter with sysUpTime.

**Answer: B**

Use counter types suitable for the measured link rate and polling interval. A wider counter helps prevent ambiguity from rapid wrap, while reset/discontinuity handling is still necessary.

**Option explanations**

- **A:** Multiple wraps are possible within the interval, so a fixed single-wrap correction remains ambiguous.
- **B:** The wider counter avoids the rapid wrap limitation of the 32-bit octet value.
- **C:** Changing display format does not recover wrapped counter information.
- **D:** Uptime does not measure transferred interface octets.

**Further reading**

- [RFC 2863 — The Interfaces Group MIB](https://www.rfc-editor.org/rfc/rfc2863.html) — 3.1.6 Counter size; ifHCInOctets; ifCounterDiscontinuityTime

---

## CCNA8-071 · IP Services

Objectives: 4.5 · single · Applied

Router logs contain only elapsed uptime prefixes. During an investigation spanning multiple devices, the team needs calendar date/time with millisecond resolution in newly generated IOS log messages. NTP is already synchronized. Which global command supplies this timestamp format?

- **A.** service timestamps debug uptime
- **B.** clock set 00:00:00 1 JAN 2000
- **C.** logging trap 3
- **D.** service timestamps log datetime msec

**Answer: D**

Clock synchronization supplies time; logging configuration controls how it is recorded. Configure the log timestamp format separately and use a consistent time-zone convention when comparing devices.

**Option explanations**

- **A:** This affects debug uptime format rather than the required log date/time format.
- **B:** Manually setting an incorrect clock does not enable the requested log format.
- **C:** This changes the remote severity threshold rather than timestamp formatting.
- **D:** This selects date/time and milliseconds for log timestamps.

**Further reading**

- [System Message Logging](https://www.cisco.com/c/en/us/td/docs/routers/access/wireless/software/guide/SysMsgLogging.html) — System log message format; logging destinations; severity levels; timestamps

---

## CCNA8-072 · IP Services

Objectives: 4.6 · multiple · Applied

A central DHCP server services VLANs 10 and 20 through two SVIs on one router. Both SVIs relay to the same server, but each has its own primary IPv4 subnet. No giaddr overrides or option-based scope policies are configured. Which two statements describe normal operation? Select two.

- **A.** Requests from the two VLANs carry different giaddr values.
- **B.** The server can use giaddr to select the matching scope for each VLAN.
- **C.** Both VLANs must receive addresses from the DHCP server's own local subnet.
- **D.** The helper destination must be unique for every VLAN even when one server holds all scopes.
- **E.** The router must bridge the two VLANs into one broadcast domain.

**Answer: A, B**

Relay information separates client subnet identity from the DHCP server's location. This enables centralized address service without extending one Layer 2 broadcast domain across all client networks.

**Option explanations**

- **A:** Each receiving SVI contributes its own address to identify the client subnet.
- **B:** The same server destination can serve several client subnets identified by the relay.
- **C:** The relay information allows remote client-subnet scope selection.
- **D:** Several interfaces can relay to the same server.
- **E:** Relaying allows separate broadcast domains to use a common server.

**Further reading**

- [IP Addressing: DHCP Configuration Guide, Cisco IOS XE Everest 16.6 — Configuring the Cisco IOS XE DHCP Relay Agent](https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/ipaddr_dhcp/configuration/xe-16-6/dhcp-xe-16-6-book/dhcp-relay-agent-xe.html) — Packet forwarding address; giaddr; specifying the packet forwarding address

---

## CCNA8-073 · IP Services

Objectives: 4.7 · single · Applied

A shaper is configured for a lower average rate than the physical link speed. A short permitted burst is buffered and eventually transmitted without packet loss. Which trade-off should the operator expect?

- **A.** An increase in the physical line rate above its configured speed.
- **B.** Additional queueing delay while packets wait for release under the profile.
- **C.** A requirement to discard every packet that arrived during the burst.
- **D.** Automatic elimination of all latency regardless of traffic volume.

**Answer: B**

Shaping can reduce downstream loss by holding traffic, but the held packets take longer to leave. The absence of loss in this bounded burst does not mean latency is unchanged or buffers are unlimited.

**Option explanations**

- **A:** Shaping constrains transmission behavior and does not speed up the medium.
- **B:** Delayed release is how shaping smooths the burst.
- **C:** The stated buffer and profile allow the burst to be delayed and sent.
- **D:** Buffering can add delay rather than eliminate it.

**Further reading**

- [Compare Traffic Policing and Traffic Shaping to Limit Bandwidth](https://www.cisco.com/c/en/us/support/docs/quality-of-service-qos/qos-policing/19645-policevsshape.html) — Traffic policing and traffic shaping comparison

---

## CCNA8-074 · IP Services

Objectives: 4.8 · single · Applied

An administrator can reach a router's SSH port and complete key exchange. AAA is disabled. A configuration review finds that the shown VTY lines do not select the intended local username database. Which single line should replace login to select that database?

```text
username operator secret <configured-secret>
line vty 0 4
 password <line-password>
 login
 transport input ssh
```

- **A.** password local
- **B.** ip domain name local
- **C.** login local
- **D.** transport input ssh

**Answer: C**

With AAA disabled, login local selects the local username database for these VTY lines. Retain the intended SSH transport restriction and a working local account, and verify authentication after the change.

**Option explanations**

- **A:** This would set the literal line password to local rather than select local accounts.
- **B:** A domain name does not change VTY authentication selection.
- **C:** This selects the local username database on the VTY lines.
- **D:** Transport is already restricted; that command does not select the account database.

**Further reading**

- [Configure SSH on Routers](https://www.cisco.com/c/en/us/support/docs/security-vpn/secure-shell-ssh/4145-ssh.html) — Configure SSH on a Cisco Router Using Password Authentication; Recommendations

---

## CCNA8-075 · IP Services

Objectives: 4.9 · single · Challenge

A base TFTP transfer without extensions sends a file that is exactly 1,024 bytes long. DATA blocks carry at most 512 bytes. After the receiver acknowledges two full data blocks, how does the sender signal normal end of file?

- **A.** Send a third DATA block containing zero data bytes, then receive its acknowledgment.
- **B.** Close a TCP connection immediately after the second block.
- **C.** Send a DHCPRELEASE containing the filename.
- **D.** Stop after the two full blocks, because a full 512-byte block is the end marker.

**Answer: A**

Base TFTP marks the final block by its short data length, including zero bytes. Both 512-byte blocks are full, so the separate zero-length DATA block supplies the termination marker.

**Option explanations**

- **A:** A data block shorter than 512 bytes marks completion; an exact multiple needs a final empty block.
- **B:** This transfer is not a TCP session.
- **C:** DHCP lease release is unrelated to TFTP completion.
- **D:** A full block signals that the transfer has not yet supplied the required short final block.

**Further reading**

- [RFC 1350 — The TFTP Protocol (Revision 2)](https://www.rfc-editor.org/info/rfc1350/) — 2 Protocol overview; 3 Relation to other protocols; 4 Initial connection; 6 Normal termination

---

## CCNA8-076 · Security Fundamentals

Objectives: 5.1 · single · Applied

An attacker steals a valid administrator password and uses it to log in through the normal management service. Which mitigation most directly reduces the usefulness of that stolen password for future logins?

- **A.** Change the login banner but keep password-only authentication and the exposed value.
- **B.** Increase the number of permitted simultaneous sessions for the account.
- **C.** Require an additional independent authentication factor and revoke the exposed password.
- **D.** Suppress failed-login logs because the attacker’s password is valid.

**Answer: C**

An attacker can abuse a valid credential without exploiting a software bug. Treatment should address the compromised credential and the authentication mechanism.

**Option explanations**

- **A:** A notice does not invalidate or supplement the stolen credential.
- **B:** This changes capacity rather than reducing credential misuse.
- **C:** Invalidating the known secret and requiring a different factor directly address password-only impersonation.
- **D:** Removing evidence does not stop use of the credential.

**Further reading**

- [RFC 4949: Internet Security Glossary, Version 2](https://www.rfc-editor.org/rfc/rfc4949.html) — Section 2: threat, vulnerability, exploit, and countermeasure
- [NIST SP 800-63B-4: Digital Identity Guidelines — Authentication and Authenticator Management](https://pages.nist.gov/800-63-4/sp800-63b.html) — Authentication factors; password verifiers; authenticator management

---

## CCNA8-077 · Security Fundamentals

Objectives: 5.2 · single · Applied

A network team proposes replacing individually assigned equipment-room badges with one shared badge left at reception. Which security-program capability is most directly weakened?

- **A.** Ability to associate authorized entry with a specific individual.
- **B.** The ability of the reader to recognize its existing badge credential format.
- **C.** The ability to record that this particular shared badge was presented.
- **D.** The ability of the door to latch when nobody is entering.

**Answer: A**

Individual physical credentials support accountable entry and selective revocation. A shared badge weakens those properties even if the same reader still controls the door.

**Option explanations**

- **A:** A shared credential obscures who actually used it and complicates individual revocation.
- **B:** Sharing the badge does not inherently change its technical credential format.
- **C:** The reader can still log the shared credential; associating it with a specific person is what becomes weaker.
- **D:** A shared credential does not by itself prevent the same physical door from latching.

**Further reading**

- [NIST SP 800-53 Rev. 5: Security and Privacy Controls for Information Systems and Organizations](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-53r5.pdf) — AT-2, AT-3, PE-2, and PE-3: awareness, training, and physical access

---

## CCNA8-078 · Security Fundamentals

Objectives: 5.3 · single · Applied

A junior local account should begin in user EXEC and require a separately controlled enable secret for privileged EXEC. AAA and custom privilege mappings are absent. Which configuration meets that requirement?

- **A.** username junior privilege 15 secret SeparateEnable!
**Configuration B**

```text
username junior privilege 15 secret JuniorLogin!
enable secret SeparateEnable!
```

**Configuration C**

```text
username junior privilege 1 secret JuniorLogin!
no enable secret
```

**Configuration D**

```text
username junior privilege 1 secret JuniorLogin!
enable secret SeparateEnable!
```


**Answer: D**

The account’s initial privilege and the enable credential must both express the design. Giving level 15 at login removes the intended later privilege gate.

**Option explanations**

- **A:** This merges login with immediate privileged access and omits the intended separate transition.
- **B:** Level 15 starts the account with the privilege that should require a later transition.
- **C:** This leaves the required separately controlled enable secret unconfigured.
- **D:** The account starts at level 1 and a separate secret controls the enable transition.

**Further reading**

- [Catalyst 3750-X and 3560-X Configuration Guide: Configuring Switch-Based Authentication](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst3750x_3560x/software/release/15-0_2_se/configuration/guide/3750x_cg/swauthen.html) — Protecting Access to Privileged EXEC Commands; Configuring Username and Password Pairs

---

## CCNA8-079 · Security Fundamentals

Objectives: 5.4 · single · Applied

A lost hardware authentication token has been reported, while the user’s password remains private. Which response correctly treats the lost factor?

- **A.** Publish the token’s recovery code so anyone can assist the user.
- **B.** Keep the token active indefinitely because the password has not been disclosed.
- **C.** Rename the account and keep all authenticators bound unchanged.
- **D.** Revoke or disable the lost token’s authentication binding and enroll an authorized replacement.

**Answer: D**

Authenticator management includes loss and replacement, not only initial enrollment. Revoke the missing credential and verify the user through the approved recovery process.

**Option explanations**

- **A:** A public recovery secret would weaken the authentication path.
- **B:** The lost factor remains exposed even if another factor is not known to be compromised.
- **C:** A cosmetic account-name change does not invalidate the lost credential.
- **D:** The missing possession factor must stop being accepted and recovery must follow an identity-checked process.

**Further reading**

- [NIST SP 800-63B-4: Digital Identity Guidelines — Authentication and Authenticator Management](https://pages.nist.gov/800-63-4/sp800-63b.html) — Authentication factors; password verifiers; authenticator management

---

## CCNA8-080 · Security Fundamentals

Objectives: 5.5 · single · Applied

A headquarters IPsec gateway authenticates a branch gateway as its site-to-site peer. The branch contains 50 users. What does that peer authentication directly identify?

- **A.** The remote IPsec peer according to the configured gateway authentication policy.
- **B.** The authorization role of every application user behind the peer.
- **C.** The physical security status of every branch endpoint.
- **D.** The individual human responsible for every inner packet from the branch.

**Answer: A**

A site-to-site security association authenticates its configured peers. Individual host or user identity requires additional mechanisms and evidence.

**Option explanations**

- **A:** The cryptographic peer identity belongs to the terminating gateway relationship.
- **B:** Application permissions are not supplied by gateway authentication alone.
- **C:** A valid peer credential does not prove all local assets are physically secure.
- **D:** Gateway peer authentication does not identify each LAN user.

**Further reading**

- [RFC 4301: Security Architecture for the Internet Protocol](https://www.rfc-editor.org/rfc/rfc4301.html) — Sections 3, 4.1, 4.4.1: IPsec services, tunnel mode, and security policy

---

## CCNA8-081 · Security Fundamentals

Objectives: 5.6 · single · Applied

A standard IPv4 ACL numbered 10 permits only source host 10.88.0.10. It is applied inbound as a VTY access-class on an IOS device. Which behavior is the direct purpose of this application?

```text
access-list 10 permit host 10.88.0.10
line vty 0 15
 access-class 10 in
 login local
 transport input ssh
```

- **A.** Filter every forwarded packet traversing the router from that source.
- **B.** Encrypt management packets from the permitted source.
- **C.** Permit that source to run every command without authentication.
- **D.** Restrict incoming management sessions to the permitted source address.

**Answer: D**

The same policy object can have different effects depending on its attachment. A VTY access-class restricts access to the management lines rather than defining all transit forwarding policy.

**Option explanations**

- **A:** Transit interface filtering requires application to the forwarding path, not only VTY lines.
- **B:** ACL matching does not provide transport encryption.
- **C:** An access-class source permit does not replace line authentication or command privilege.
- **D:** A VTY access-class controls access to terminal lines.

**Further reading**

- [Catalyst 3750-X and 3560-X Configuration Guide: Configuring Network Security with ACLs](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst3750x_3560x/software/release/15-0_2_se/configuration/guide/3750x_cg/swacl.html) — Applying an IPv4 ACL to a Terminal Line; Including Comments in ACLs

---

## CCNA8-082 · Security Fundamentals

Objectives: 5.7 · single · Applied

Port security allows only MAC 00:aa:bb:cc:dd:01 on a desk port. The approved device is disconnected, and another device deliberately sends using that same MAC. Ignore other protections. What limitation does this illustrate?

- **A.** The configured MAC limit must reject the copied MAC because it came from a new user.
- **B.** A MAC-based permit does not cryptographically prove the device’s identity.
- **C.** An accepted MAC proves the operating system is uncompromised.
- **D.** Port security authenticates every accepted source using a private key.

**Answer: B**

Port security constrains source MACs and learning, but a MAC value is not an unforgeable credential. Use its protection claims within that boundary.

**Option explanations**

- **A:** This feature is not measuring the human identity in the scenario.
- **B:** A sender can imitate an allowed source address; the filter alone cannot attest the hardware or user.
- **C:** Source address acceptance says nothing about software integrity.
- **D:** No cryptographic authentication is described by a MAC allow entry.

**Further reading**

- [Catalyst 3750-X and 3560-X Configuration Guide: Configuring Port-Based Traffic Control](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst3750x_3560x/software/release/15-0_2_se/configuration/guide/3750x_cg/swtrafc.html) — Secure MAC Addresses; Security Violations; Port Security Aging

---

## CCNA8-083 · Security Fundamentals

Objectives: 5.8 · matching · Applied

Match each management-system requirement to the AAA function that primarily supplies it. Use each function once.

1. Reject a login whose credential proof is invalid.
2. Allow a monitoring role to inspect interfaces but prevent configuration changes.
3. Retain session-start and session-stop events for an investigation.

- **A.** Accounting
- **B.** Authorization
- **C.** Authentication

**Answer: 1 → C; 2 → B; 3 → A**

Identity proof, permission decisions, and activity records require distinct checks. Success of one function is not proof that the other two were configured.

**Option explanations**

- **A:** It creates records that support review of access and activity.
- **B:** It decides which services or commands a verified identity may use.
- **C:** It checks a claimed identity using accepted credentials.

**Further reading**

- [RFC 8907: The Terminal Access Controller Access-Control System Plus (TACACS+) Protocol](https://www.rfc-editor.org/rfc/rfc8907.html) — Sections 5, 6, and 7: authentication, authorization, and accounting

---

## CCNA8-084 · Security Fundamentals

Objectives: 5.9 · single · Applied

An engineer claims that changing a WPA2-Personal WLAN’s passphrase to a longer value upgrades the WLAN protocol to WPA3. Which response is correct?

- **A.** WPA2-Personal never uses a password, so the change has no meaning.
- **B.** WPA3 is selected solely by changing the SSID text to include WPA3.
- **C.** Passphrase strength changes; selecting WPA3 still requires SAE.
- **D.** Any passphrase longer than 16 characters automatically selects SAE.

**Answer: C**

Configuration labels and credential strength must not be confused with protocol state. Verify the actual authentication method and client negotiation when claiming WPA3.

**Option explanations**

- **A:** WPA2-Personal commonly derives keys from a configured shared passphrase.
- **B:** The SSID is a name, not the security negotiation setting.
- **C:** Credential quality does not change the negotiated security protocol.
- **D:** There is no such automatic protocol transition based on that length.

**Further reading**

- [Cisco Catalyst 9800 Configuration Guide, IOS XE 17.3.x: Wi-Fi Protected Access 3](https://www.cisco.com/c/en/us/td/docs/wireless/controller/9800/17-3/config-guide/b_wl_17_3_cg/m_wpa3.html) — WPA3-Personal; WPA3-Personal Transition Mode; Protected Management Frames

---

## CCNA8-085 · Security Fundamentals

Objectives: 5.10 · single · Applied

A constructed WLAN GUI lists these four candidate security profiles. The requirement is WPA2-Personal with AES-CCMP and a valid shared passphrase, with no enterprise authentication. Which profile meets it?

- **A.** WPA2 enabled; AES enabled; PSK selected; valid matching passphrase.
- **B.** Layer 2 security None; a passphrase written in the WLAN description.
- **C.** WPA enabled only; TKIP enabled; PSK selected.
- **D.** WPA2 enabled; AES enabled; 802.1X selected; no PSK.

**Answer: A**

Evaluate the complete security combination, not a single field. A correct cipher with the wrong key-management mode still fails the intended design.

**Option explanations**

- **A:** This combines the required WPA2 policy, cipher, and key-management method.
- **B:** Description text is not a security credential and the WLAN remains open.
- **C:** This provides legacy WPA/TKIP rather than the requested WPA2/AES profile.
- **D:** This selects enterprise authentication rather than the required shared passphrase.

**Further reading**

- [Cisco Wireless Controller Configuration Guide, Release 8.10: WLAN Security](https://www.cisco.com/c/en/us/td/docs/wireless/controller/8-10/config-guide/b_cg810/wlan_security.html) — WPA1+WPA2; Configuring WPA1+WPA2 (GUI); Protected Management Frames

---

## CCNA8-086 · Security Fundamentals

Objectives: 5.6 · single · Applied

Only inbound ICMP echo-replies from server 192.0.2.81 to diagnostic host 10.8.0.81 should be allowed through this ACL. Which entry expresses the required message type and direction?

- **A.** permit icmp host 192.0.2.81 host 10.8.0.81 echo
- **B.** permit ip host 192.0.2.81 host 10.8.0.81
- **C.** permit icmp host 192.0.2.81 host 10.8.0.81 echo-reply
- **D.** permit icmp host 10.8.0.81 host 192.0.2.81 echo

**Answer: C**

ICMP ACLs can distinguish request and response message types. Pair the correct message type with the source and destination as seen at this enforcement point.

**Option explanations**

- **A:** This admits server-originated echo requests, not replies.
- **B:** This admits every IP protocol and does not constrain the ICMP type.
- **C:** The server is the reply source and the message is an echo-reply.
- **D:** This expresses the diagnostic request traveling in the opposite direction.

**Further reading**

- [Configure Commonly Used IP ACLs](https://www.cisco.com/c/en/us/support/docs/ip/access-lists/26448-ACLsamples.html) — Allow Pings (ICMP); Allow DNS; TCP/UDP ACL syntax

---

## CCNA8-087 · Security Fundamentals

Objectives: 5.6 · single · Applied

A host-specific IPv4 ACL entry uses source 198.51.100.29 0.0.0.0. Which alternative source expression is exactly equivalent?

- **A.** 198.51.100.0 0.0.0.255
- **B.** host 198.51.100.29
- **C.** any
- **D.** 198.51.100.29 255.255.255.255

**Answer: B**

Wildcard zero means exact match for each bit. The host keyword is the shorthand for that exact-address condition.

**Option explanations**

- **A:** This permits an entire /24 rather than the single address.
- **B:** A zero wildcard requires every address bit to match that one host.
- **C:** This accepts every source address.
- **D:** All bits become do-not-care, so the address is not restricted.

**Further reading**

- [Configure IP Access Lists](https://www.cisco.com/c/en/us/support/docs/security/ios-firewall/23602-confaccesslists.html) — ACL Concepts; Masks; Process ACLs; Apply ACLs; Extended ACLs

---

## CCNA8-088 · Security Fundamentals

Objectives: 5.7 · single · Applied

A DAI-protected VLAN has a trusted uplink and untrusted user access ports. An ARP packet with a false sender mapping arrives on the trusted uplink. What does the trusted state mean for DAI on that ingress?

- **A.** The switch automatically rewrites the false mapping to the correct MAC.
- **B.** The false mapping forces the uplink to become untrusted automatically.
- **C.** DAI bypasses its normal untrusted-port validation for that ingress.
- **D.** DAI validates the packet more strictly than it does on user ports.

**Answer: C**

Trust creates an inspection boundary; it does not establish that every upstream packet is true. Justify trusted paths and understand which device validates upstream traffic.

**Option explanations**

- **A:** DAI is not a repair service that rewrites arbitrary ARP sender claims.
- **B:** Trust configuration is not automatically revised on the basis of an unchecked claim.
- **C:** A trusted interface is outside that local inspection check, so upstream protection matters.
- **D:** Trusted ingress is not the stricter inspection category.

**Further reading**

- [Catalyst 3750-X and 3560-X Configuration Guide: Configuring Dynamic ARP Inspection](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst3750x_3560x/software/release/15-0_2_se/configuration/guide/3750x_cg/swdynarp.html) — Understanding Dynamic ARP Inspection; Rate Limiting; ARP ACLs

---

## CCNA8-089 · Security Fundamentals

Objectives: 5.7 · multiple · Applied

Snooping is enabled globally and on VLAN 90. A DHCP client can send DISCOVER, but the authorized OFFER arrives over an uplink still marked untrusted and is dropped. Which two observations best confirm this diagnosis? Select two.

- **A.** The DHCP lease duration configured on the server is long.
- **B.** A controlled packet observation shows the OFFER arriving there but not reaching the client.
- **C.** The server successfully issued leases earlier through a different uplink.
- **D.** The snooping interface view shows the server-facing ingress as untrusted.

**Answer: B, D**

Correlate effective feature state with the actual packet path. A valid server can still be blocked if its ingress is incorrectly treated as an untrusted client path.

**Option explanations**

- **A:** Lease duration does not determine ingress trust or prove a dropped OFFER.
- **B:** This places the failure at the filtering point described.
- **C:** Historical success over another path does not establish the current ingress trust or this OFFER’s forwarding.
- **D:** That state explains why a server reply is not authorized on the ingress.

**Further reading**

- [Catalyst 3750-X and 3560-X Configuration Guide: Configuring DHCP Features and IP Source Guard](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst3750x_3560x/software/release/15-0_2_se/configuration/guide/3750x_cg/swdhcp82.html) — DHCP Snooping; DHCP Snooping Binding Database; Enabling DHCP Snooping

---

## CCNA8-090 · Security Fundamentals

Objectives: 5.4 · multiple · Applied

Which two proposed login requirements use different factor categories rather than two knowledge checks? Select two.

- **A.** A cryptographic security key requiring local fingerprint activation.
- **B.** A password plus a different memorized PIN entered into the same form, with no possession mechanism.
- **C.** A password plus proof from a separately held hardware OTP token.
- **D.** A password plus the answer to a personal security question.

**Answer: A, C**

Classify what each check proves. Two prompts do not necessarily provide multifactor authentication if both test memorized information.

**Option explanations**

- **A:** The key provides possession and fingerprint activation supplies inherence.
- **B:** Two memorized values still represent one factor category.
- **C:** The login combines a memorized secret with possession of the token.
- **D:** Both checks rely on knowledge.

**Further reading**

- [NIST SP 800-63B-4: Digital Identity Guidelines — Authentication and Authenticator Management](https://pages.nist.gov/800-63-4/sp800-63b.html) — Authentication factors; password verifiers; authenticator management

---

## CCNA8-091 · Automation and Programmability

Objectives: 6.1 · single · Applied

An automation job finishes without exceptions after changing a management ACL. The operator must determine whether authorized monitoring still works and unauthorized access is blocked. Which evidence is most useful?

- **A.** Only the absence of a scripting exception
- **B.** Verification of the applied ACL plus allowed and denied access tests
- **C.** The number of lines in the playbook
- **D.** A screenshot of the job’s start time

**Answer: B**

Automation execution and network acceptance are separate questions. Checking effective configuration and representative allowed/denied behavior provides evidence that the management requirement was achieved.

**Option explanations**

- **A:** A successful workflow execution does not itself prove the intended access behavior.
- **B:** These checks compare effective behavior with the stated management requirement.
- **C:** Script length does not establish policy correctness.
- **D:** A start timestamp does not show the resulting access behavior.

**Further reading**

- [What Is Network Automation?](https://www.cisco.com/site/us/en/learn/topics/networking/what-is-network-automation.html) — Network automation; profiles and policies; automated lifecycle management

---

## CCNA8-092 · Automation and Programmability

Objectives: 6.2, 6.3.a · single · Applied

A traditional router runs a routing protocol locally and forwards packets in hardware. A controller-managed switch receives forwarding rules from an external controller and also forwards packets in hardware. What difference is established by the scenario?

- **A.** Only the controller-managed switch has a data plane
- **B.** Hardware forwarding is possible only in the traditional router
- **C.** The controller-managed switch must send every packet to the application layer
- **D.** The location of the described control decision differs

**Answer: D**

Both devices have data-plane forwarding. The comparison concerns where the described forwarding decisions are made, not whether user packets can be forwarded in hardware.

**Option explanations**

- **A:** Both devices perform packet forwarding.
- **B:** The scenario explicitly uses hardware forwarding in both.
- **C:** Local hardware forwarding is specified.
- **D:** The traditional router calculates locally, while the switch receives the rules externally.

**Further reading**

- [RFC 7426: Software-Defined Networking (SDN): Layers and Architecture Terminology](https://www.rfc-editor.org/rfc/rfc7426.html) — 3.1 Overview; 3.2 Network Devices; 3.3 Control Plane; 3.5.3 Locality

---

## CCNA8-093 · Automation and Programmability

Objectives: 6.3.b · single · Applied

A controller has a healthy southbound connection to its switches, but a service portal’s credentials for the controller API have expired. Existing device forwarding is normal. Which boundary is preventing the portal from requesting new supported services?

- **A.** The northbound application-to-controller boundary
- **B.** The underlay’s physical link layer
- **C.** The southbound controller-to-device boundary
- **D.** The user-packet data plane in every switch

**Answer: A**

The failed credential belongs to an application consuming controller services. That is a northbound issue; the scenario gives separate evidence that southbound connectivity and existing forwarding remain healthy.

**Option explanations**

- **A:** The portal’s failed authentication concerns its use of the controller’s application API.
- **B:** The reported fault is an API credential problem, not a physical transport failure.
- **C:** Those connections are explicitly healthy.
- **D:** Normal existing forwarding does not depend on this portal credential being valid.

**Further reading**

- [Software-Defined Networking (SDN) Definition](https://www.cisco.com/c/en/us/solutions/software-defined-networking/overview.html) — SDN elements; Features and benefits
- [RFC 7426: Software-Defined Networking (SDN): Layers and Architecture Terminology](https://www.rfc-editor.org/rfc/rfc7426.html) — 3.1 Overview; 3.2 Network Devices; 3.3 Control Plane; 3.5.3 Locality

---

## CCNA8-094 · Automation and Programmability

Objectives: 6.4 · multiple · Applied

After a permanent change in business hours, an analytics model trained on the old schedule repeatedly flags the new routine traffic as unusual. Which two actions are appropriate? Select two.

- **A.** Disable all telemetry because the model disagrees with operations
- **B.** Treat every flagged observation as a confirmed attack
- **C.** Check whether the model’s baseline still represents current normal operations
- **D.** Use representative current data to update the model through the supported process
- **E.** Assume all new traffic must be harmless because schedules changed

**Answer: C, D**

Learned baselines depend on the operating patterns represented in data. A lasting change calls for investigation and supported baseline adaptation, while preserving the distinction between an anomaly and its cause.

**Option explanations**

- **A:** Removing observations would weaken the ability to understand and update the baseline.
- **B:** An anomaly relative to an old baseline is not proof of malicious activity.
- **C:** The operating pattern has changed since the relevant learning data.
- **D:** An adapted baseline can account for the new legitimate pattern.
- **E:** A schedule change does not make every observation benign.

**Further reading**

- [What is AIOps?](https://developer.cisco.com/articles/what-is-aiops/) — The core components of AIOps; Is AIOps all you need?

---

## CCNA8-095 · Automation and Programmability

Objectives: 6.5 · single · Applied

A client sends the request excerpt shown. It intends to submit JSON, but the API reports an unsupported request media type. The documented endpoint accepts application/json. Which header needs correction?

```text
POST /sites
Content-Type: application/xml
Accept: application/json

{"name":"branch-west"}
```

- **A.** Accept should be deleted because JSON cannot be returned
- **B.** Content-Type should identify application/json
- **C.** POST should be replaced by a header named Create
- **D.** Authorization should contain application/json instead of credentials

**Answer: B**

Content-Type describes the representation sent in the request body. Accept instead describes acceptable response representations, so the existing Accept value does not repair a mislabeled request body.

**Option explanations**

- **A:** Accept can legitimately request a JSON response.
- **B:** The body is JSON, while the header incorrectly identifies an XML representation.
- **C:** POST is a method; CRUD is not an HTTP header scheme.
- **D:** The media type belongs in Content-Type, not the credential field.

**Further reading**

- [RFC 9110: HTTP Semantics](https://www.rfc-editor.org/rfc/rfc9110.html) — 9 Methods; 15 Status Codes

---

## CCNA8-096 · Automation and Programmability

Objectives: 6.5 · single · Foundation

An API supports GET /interfaces for the complete collection and GET /interfaces/eth7 for one member. An application needs only eth7’s current representation and must not request a change. Which request directly matches that need?

- **A.** POST /interfaces/eth7
- **B.** DELETE /interfaces/eth7
- **C.** PUT /interfaces with a body naming eth7
- **D.** GET /interfaces/eth7

**Answer: D**

The URI identifies which resource is targeted, and the method describes the requested operation. The documented individual URI with GET retrieves the required representation directly.

**Option explanations**

- **A:** POST does not express the documented member retrieval.
- **B:** DELETE would request removal rather than reading.
- **C:** This does not match the documented individual Read request.
- **D:** This combines the retrieval method with the URI of the required member.

**Further reading**

- [RFC 9110: HTTP Semantics](https://www.rfc-editor.org/rfc/rfc9110.html) — 9 Methods; 15 Status Codes

---

## CCNA8-097 · Automation and Programmability

Objectives: 6.6 · single · Applied

A supported network platform exposes an HTTPS management API but does not provide CLI-over-SSH access for the proposed automation. What should an Ansible designer investigate first?

- **A.** A supported collection and connection method for that platform’s API
- **B.** Whether changing a YAML file extension enables SSH on the device
- **C.** Whether Ansible always requires CLI over SSH for every network device
- **D.** Whether a playbook can bypass device authentication by using JSON

**Answer: A**

Ansible support depends on the platform, selected modules and connection method. A suitable API integration can be appropriate when the required CLI transport is unavailable.

**Option explanations**

- **A:** Ansible network support can use different transport methods depending on the platform and modules.
- **B:** A filename change cannot create a management service.
- **C:** Network automation can also use supported API and NETCONF connections.
- **D:** Data encoding does not bypass management access requirements.

**Further reading**

- [How Network Automation is Different](https://docs.ansible.com/projects/ansible/latest/network/getting_started/network_differences.html) — Execution on the control node; Multiple communication protocols; Collections organized by network platform

---

## CCNA8-098 · Automation and Programmability

Objectives: 6.6 · single · Applied

A Terraform provider supports reading a particular controller setting but offers no resource operation to configure it. The team needs to manage that setting’s lifecycle. Which conclusion is justified?

- **A.** Reading a setting guarantees the provider can modify it
- **B.** Terraform automatically derives every missing write API from JSON output
- **C.** The team must find a supported management integration for that setting
- **D.** The setting is impossible to automate with any tool

**Answer: C**

Providers expose particular supported capabilities. The team must verify that the desired resource operation exists rather than assume a read-only capability also supports changes.

**Option explanations**

- **A:** Read support does not imply support for lifecycle operations.
- **B:** Output data does not supply missing provider operations.
- **C:** The current provider capability does not meet the stated lifecycle requirement.
- **D:** The limitation shown is the chosen integration, not all possible tools.

**Further reading**

- [Providers](https://developer.hashicorp.com/terraform/language/providers) — What Providers Do; Provider Documentation

---

## CCNA8-099 · Automation and Programmability

Objectives: 6.7 · multiple · Foundation

An API returns {"devices":[],"errors":{}}. Which two interpretations are correct? Select two.

- **A.** devices is an empty array
- **B.** errors is an empty object
- **C.** Both values are JSON null
- **D.** errors contains one blank-string member
- **E.** devices contains one empty object

**Answer: A, B**

Empty containers still have distinct types. [] has zero array elements, whereas {} has zero object members.

**Option explanations**

- **A:** Square brackets with no elements represent an empty array.
- **B:** Braces with no members represent an empty object.
- **C:** Neither value uses the null literal.
- **D:** An empty object has no members, including no blank-string member.
- **E:** An array containing an empty object would be written [{}].

**Further reading**

- [RFC 8259: The JavaScript Object Notation (JSON) Data Interchange Format](https://www.rfc-editor.org/rfc/rfc8259.html) — 2 JSON Grammar; 3 Values; 4 Objects; 5 Arrays; 6 Numbers; 7 Strings

---

## CCNA8-100 · Automation and Programmability

Objectives: 6.7 · single · Challenge

A client parses the complete JSON response shown. The API defines count as the number of returned device objects. Which defect should the client’s data validation detect?

```text
{"count":3,"devices":[{"name":"rtr-a"},{"name":"rtr-b"}]}
```

- **A.** The response is invalid JSON because count is numeric
- **B.** A JSON array cannot contain two objects
- **C.** The two devices must have identical name values
- **D.** count disagrees with the actual number of array elements

**Answer: D**

Syntax validity and data consistency are different checks. The document parses as JSON, but its stated count does not match its two returned objects.

**Option explanations**

- **A:** An unquoted number is valid JSON.
- **B:** Arrays can contain multiple object elements.
- **C:** The schema described does not require identical device names.
- **D:** The array contains two device objects, while count reports three.

**Further reading**

- [RFC 8259: The JavaScript Object Notation (JSON) Data Interchange Format](https://www.rfc-editor.org/rfc/rfc8259.html) — 2 JSON Grammar; 3 Values; 4 Objects; 5 Arrays; 6 Numbers; 7 Strings

---
