# CCNA Practice — Set 03

100 original questions aligned to CCNA 200-301 v1.1. No interactive labs.

Answers and explanations follow each question. For an unrevealed attempt, use the Streamlit app.

Content review date: 2026-09-14.

## CCNA3-001 · Network Fundamentals

Objectives: 1.1.f, 1.1.g · single · Foundation

A laptop requests a file from a host, then shares its own printer with another laptop. Which conclusion about client and server roles is correct?

- **A.** A laptop can never provide a server function
- **B.** A server must always initiate every request
- **C.** One device can act as a client in one exchange and a server in another
- **D.** Using Ethernet makes both devices routers

**Answer: C**

Client and server describe service roles. A machine can consume one service while providing another.

**Option explanations**

- **A:** Device form factor does not prohibit serving requests.
- **B:** Clients generally initiate the service requests in these examples.
- **C:** Roles depend on which service interaction is being considered.
- **D:** Ethernet attachment does not confer routing functionality.

**Further reading**

- [RFC 9110: HTTP Semantics](https://www.rfc-editor.org/rfc/rfc9110.html#section-3.3) — 3.3. Connections, Clients, and Servers

---

## CCNA3-002 · Network Fundamentals

Objectives: 1.2.d, 1.2.f · single · Applied

A company keeps its ERP server on its premises and connects three cities through a carrier network. Which description fits?

- **A.** On-premises hosting with WAN connectivity
- **B.** Public-cloud hosting because a carrier is involved
- **C.** One shared Ethernet collision domain across all cities
- **D.** A spine-leaf fabric because there are three locations

**Answer: A**

The ERP hosting remains on premises. The carrier connection supplies wide-area connectivity between site networks.

**Option explanations**

- **A:** Server ownership/location and intersite connectivity describe separate design aspects.
- **B:** Carrier transport does not relocate the ERP service into a cloud.
- **C:** WAN connectivity does not imply a single shared physical medium.
- **D:** The number of cities does not establish leaf-to-spine cabling.

**Further reading**

- [What is a WAN (wide-area network)?](https://www.cisco.com/site/us/en/learn/topics/networking/what-is-a-wan-wide-area-network.html) — What is a WAN (wide-area network)?; What is a WAN router?
- [NIST SP 800-145: The NIST Definition of Cloud Computing](https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-145.pdf) — 2. The NIST Definition of Cloud Computing — Essential Characteristics; Deployment Models

---

## CCNA3-003 · Network Fundamentals

Objectives: 1.3.a · multiple · Applied

An installed 10 Gb/s optical link uses OM3 multimode fiber. Its optics are being replaced. Which TWO checks are directly relevant to selecting replacements? Select two.

- **A.** Whether the SSIDs are identical
- **B.** Whether the modules support the installed fiber type and distance
- **C.** Whether both interface descriptions match
- **D.** Whether transmit/receive wavelengths and optical specifications are compatible
- **E.** Whether the IP addresses have consecutive host numbers

**Answer: B, D**

Optical compatibility depends on the signaling and physical path. Administrative labels and IP numbering cannot compensate for incompatible optics.

**Option explanations**

- **A:** Wireless names do not determine optical compatibility.
- **B:** Module reach is specified for particular fiber characteristics.
- **C:** Descriptions are administrative text, not signaling requirements.
- **D:** Optical endpoints must interoperate within their receive limits.
- **E:** Host-number ordering does not establish a physical optical link.

**Further reading**

- [Cisco 10GBASE SFP+ Modules Data Sheet](https://www.cisco.com/c/en/us/products/collateral/interfaces-modules/transceiver-modules/data_sheet_c78-455693.html) — Cisco SFP-10G-SR module; Cisco SFP-10G-LR module; Cisco SFP-10G-T-X module

---

## CCNA3-004 · Network Fundamentals

Objectives: 1.4 · single · Applied

A port reports administratively down, line protocol down. Its peer and cable are known good. Which local action addresses the condition explicitly shown?

```text
GigabitEthernet1/0/12 is administratively down, line protocol is down
```

- **A.** Change the DNS server
- **B.** Disable MAC aging
- **C.** Change the subnet broadcast address
- **D.** Enable the interface with no shutdown

**Answer: D**

The explicit administrative state identifies a local configuration issue. Physical troubleshooting alone cannot activate an interface that remains shut down.

**Option explanations**

- **A:** DNS cannot clear an administrative shutdown.
- **B:** MAC aging does not enable a disabled interface.
- **C:** Broadcast calculation does not alter administrative state.
- **D:** Administrative disablement is removed by enabling the interface.

**Further reading**

- [Configure and Verify Ethernet 10/100/1000Mb Half/Full Duplex Auto-Negotiation](https://www.cisco.com/c/en/us/support/docs/lan-switching/ethernet/10561-3.html) — Background Information; Auto-Negotiation on Catalyst Switches that Run Cisco IOS Software

---

## CCNA3-005 · Network Fundamentals

Objectives: 1.5 · single · Applied

A TCP receiver has received all data bytes through sequence number 5000 in order and sends ACK=5001. What does this acknowledgment mean?

```text
Receiver → Sender: ACK=5001
```

- **A.** It acknowledges the data through sequence number 5000 and identifies 5001 as the next expected sequence number
- **B.** It confirms receipt of exactly 5001 separate packets
- **C.** It proves the application saved the data to disk
- **D.** It identifies the receiving UDP port

**Answer: A**

The receiver has cumulatively acknowledged the preceding byte sequence. This is transport-level evidence, not confirmation of a completed business transaction.

**Option explanations**

- **A:** A cumulative TCP acknowledgment names the next expected sequence number.
- **B:** TCP sequence space counts bytes, not packets.
- **C:** Transport receipt does not establish application persistence.
- **D:** UDP ports are not TCP acknowledgment numbers.

**Further reading**

- [RFC 9293: Transmission Control Protocol (TCP)](https://www.rfc-editor.org/rfc/rfc9293.html#section-3.4) — 3.4 Sequence Numbers — cumulative acknowledgments and SEG.ACK

---

## CCNA3-006 · Network Fundamentals

Objectives: 1.6 · single · Applied

A network needs four equal-sized subnets from 192.168.70.0/24. Each must support 50 ordinary host addresses. Which prefix satisfies both constraints?

- **A.** /25
- **B.** /27
- **C.** /26
- **D.** /28

**Answer: C**

Borrowing two bits creates four subnets. The six remaining host bits allow 62 usable addresses per subnet.

**Option explanations**

- **A:** Only two /25 subnets fit in a /24.
- **B:** A /27 has only 30 usable host addresses.
- **C:** Four /26 subnets fit, each with 62 usable addresses.
- **D:** A /28 supports only 14 usable hosts.

**Further reading**

- [Configure IP Addresses and Unique Subnets for New Users](https://www.cisco.com/c/en/us/support/docs/ip/routing-information-protocol-rip/13788-3.html) — Network Masks; Understand Subnetting; VLSM Example

---

## CCNA3-007 · Network Fundamentals

Objectives: 1.7 · single · Applied

A customer is assigned 100.64.12.8 by an ISP. An engineer calls it RFC 1918 private space. Which correction is accurate?

- **A.** All 100.0.0.0/8 is RFC 1918 space
- **B.** 100.64.0.0/10 is shared address space, distinct from RFC 1918
- **C.** It is an IPv4 multicast address
- **D.** It must be publicly reachable from the Internet

**Answer: B**

The familiar private ranges are not the only special-use IPv4 space. Carrier shared addressing has a separate purpose and allocation.

**Option explanations**

- **A:** RFC 1918 does not reserve that /8.
- **B:** The carrier shared range is separately defined.
- **C:** IPv4 multicast is in 224.0.0.0/4.
- **D:** Not being RFC 1918 does not imply global reachability.

**Further reading**

- [RFC 1918: Address Allocation for Private Internets](https://www.rfc-editor.org/rfc/rfc1918#section-3) — 3. Private Address Space
- [RFC 6598: IANA-Reserved IPv4 Prefix for Shared Address Space](https://www.rfc-editor.org/rfc/rfc6598.html) — 4. Shared Address Space

---

## CCNA3-008 · Network Fundamentals

Objectives: 1.8 · single · Applied

A router interface should use host address 2001:db8:33:7::1 on the /64 LAN. Which Cisco IOS interface command directly assigns that address and prefix?

```text
interface GigabitEthernet0/0
 ! Insert the IPv6 address command here
```

- **A.** ipv6 address 2001:db8:33:7::1/48
- **B.** ip address 2001:db8:33:7::1 255.255.255.0
- **C.** ipv6 address 2001:db8:33::7:1/64
- **D.** ipv6 address 2001:db8:33:7::1/64

**Answer: D**

The /64 fixes the first four hextets as the LAN prefix. Preserve their positions when entering compressed notation.

**Option explanations**

- **A:** This assigns a different prefix length.
- **B:** The IPv4 command and mask cannot configure this IPv6 address.
- **C:** This places the interface in a different /64.
- **D:** Both the host address and prefix length match the requirement.

**Further reading**

- [RFC 4291: IP Version 6 Addressing Architecture](https://www.rfc-editor.org/rfc/rfc4291#section-2.3) — 2.3. Text Representation of Address Prefixes; 2.4. Address Type Identification; 2.5.6. Link-Local IPv6 Unicast Addresses; 2.7. Multicast Addresses
- [IP Routing Configuration Guide, Cisco IOS XE 17.14.x (Catalyst 9400 Switches): Configuring IPv6 Unicast Routing](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst9400/software/release/17-14/configuration_guide/rtng/b_1714_rtng_9400_cg/configuring_ipv6_unicast_routing.html) — Configuring IPv6 Addressing and Enabling IPv6 Routing

---

## CCNA3-009 · Network Fundamentals

Objectives: 1.9.b · single · Applied

An IPv6 anycast instance keeps advertising its service route after the application process fails. Network routing remains healthy. Which conclusion is sound?

- **A.** Anycast automatically verifies that every application transaction succeeds
- **B.** A shared anycast address guarantees traffic can never reach a failed process
- **C.** Routing may continue directing traffic to that unhealthy instance until reachability is adjusted
- **D.** IPv6 multicast immediately delivers copies to every other service instance

**Answer: C**

An available network route is not proof of a functioning service. An anycast design needs explicit health handling if application failure should remove an instance from selection.

**Option explanations**

- **A:** Ordinary routing does not inherently validate the application service.
- **B:** The unhealthy instance can remain selected while its route is advertised.
- **C:** Service health must be connected to route advertisement or another explicit recovery mechanism.
- **D:** Anycast forwarding does not become multicast replication on application failure.

**Further reading**

- [RFC 4786: Operation of Anycast Services](https://www.rfc-editor.org/rfc/rfc4786.html#section-4.4.1) — 4.4.1. Signalling Service Availability

---

## CCNA3-010 · Network Fundamentals

Objectives: 1.10 · single · Applied

A Linux workstation can reach 10.12.5.20 on its local LAN but reports Network is unreachable for a remote IPv4 address. The exhibit is its complete IPv4 route output. What is missing for ordinary off-subnet access?

```text
$ ip -4 route show
10.12.5.0/24 dev enp1s0 proto kernel scope link src 10.12.5.25
```

- **A.** A usable default or specific route toward remote networks
- **B.** A second loopback MAC address
- **C.** A new SSID for the Ethernet interface
- **D.** A larger TCP receive window

**Answer: A**

The connected route handles local destinations only. A route through an appropriate gateway is needed for destinations outside that prefix.

**Option explanations**

- **A:** Only an on-link route is installed.
- **B:** Loopback MAC addressing is unrelated.
- **C:** The interface already reaches its local Ethernet LAN.
- **D:** A transport window cannot create a missing route.

**Further reading**

- [ip-route(8) — Linux manual page](https://man7.org/linux/man-pages/man8/ip-route.8.html) — ip route show; route types and nexthops

---

## CCNA3-011 · Network Fundamentals

Objectives: 1.11.c · single · Applied

An AP increases transmit power, and a distant client now hears its beacons. The client still cannot reliably send frames back at its unchanged power. What does this demonstrate?

- **A.** Beacon reception proves a bidirectional data path
- **B.** An SSID mismatch always causes weak uplink signals
- **C.** The client must transmit at the AP’s configured wattage
- **D.** Coverage must support both AP-to-client and client-to-AP communication

**Answer: D**

Wi-Fi exchanges require usable communication in both directions. Stronger AP transmission does not automatically strengthen a client’s return signal.

**Option explanations**

- **A:** Downlink reception alone cannot prove the uplink.
- **B:** SSID names do not determine received RF power.
- **C:** Client power is separately constrained and configured.
- **D:** A one-sided power increase can leave an asymmetric link budget.

**Further reading**

- [Meraki Wireless for Enterprise Best Practices — RF Design](https://documentation.meraki.com/Platform_Management/Dashboard_Administration/Design_and_Configure/Architectures_and_Best_Practices/Meraki_Wireless_for_Enterprise_Best_Practices/Meraki_Wireless_for_Enterprise_Best_Practices_-_RF_Design) — RF design; signal-to-noise ratio; transmit power

---

## CCNA3-012 · Network Fundamentals

Objectives: 1.12 · single · Applied

Two VRFs have connected interfaces numbered 10.9.0.1/24 for different tenants. No routes are leaked. Which statement best explains why this can work?

- **A.** A VRF changes IPv4 into IPv6 internally
- **B.** The same prefix is interpreted in separate routing contexts
- **C.** The router globally merges both connected networks
- **D.** All packets are automatically NATed

**Answer: B**

The ingress routing context identifies which tenant’s 10.9.0.0/24 is meant. Overlapping numeric prefixes need not collide across isolated VRFs.

**Option explanations**

- **A:** Address-family translation is not its defining function.
- **B:** Each VRF holds independent forwarding information.
- **C:** Merging would defeat the described isolation.
- **D:** VRF isolation does not inherently perform NAT.

**Further reading**

- [IP Routing Configuration Guide, Cisco IOS XE Dublin 17.12.x (Catalyst 9500 Switches): Configuring VRF-lite](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst9500/software/release/17-12/configuration_guide/rtng/b_1712_rtng_9500_cg/configuring_vrf_lite.html) — Information About VRF-lite; Guidelines for Configuring VRF-lite

---

## CCNA3-013 · Network Fundamentals

Objectives: 1.13.a, 1.13.d · single · Foundation

A switch receives a valid frame with source 00aa.0000.0011 and destination 00bb.0000.0022 on Gi1/0/4. Neither address is in its table. Which address does ordinary source learning associate with Gi1/0/4?

- **A.** 00bb.0000.0022 only
- **B.** Both addresses
- **C.** 00aa.0000.0011 only
- **D.** Neither until an ARP reply arrives

**Answer: C**

Source learning records where traffic came from. It does not infer that the destination is reachable through the same ingress port.

**Option explanations**

- **A:** The destination does not reveal where its owner is attached.
- **B:** A received frame establishes only its source’s ingress location.
- **C:** The source was observed arriving on that port.
- **D:** Learning can use any eligible Ethernet frame, not only ARP.

**Further reading**

- [Configuring MAC Address Tables](https://www.cisco.com/c/en/us/td/docs/switches/datacenter/nexus5500/sw/layer2/7x/b_5500_Layer2_Config_7x/config_mac_address_tables.pdf) — Information About MAC Addresses (page 1); Configuring the Aging Time for the MAC Table (page 2)

---

## CCNA3-014 · Network Fundamentals

Objectives: 1.1.c · single · Applied

An IPS receives only a mirrored copy of traffic and has no inline or active-response enforcement mechanism. Which capability is absent from this arrangement?

- **A.** Dropping the original packet before it reaches the destination
- **B.** Examining the copied packet’s headers
- **C.** Raising an alert about a detected pattern
- **D.** Recording the observed source address

**Answer: A**

Blocking an original packet requires an enforcement point in its path or another explicit response mechanism. Passive inspection alone provides visibility.

**Option explanations**

- **A:** A copied observation cannot itself stop the already-forwarded original.
- **B:** A mirror can supply headers for inspection.
- **C:** Detection and alerting can occur from copied traffic.
- **D:** The observed headers can include source addressing.

**Further reading**

- [What is an Intrusion Prevention System?](https://www.paloaltonetworks.com/cyberpedia/what-is-an-intrusion-prevention-system-ips) — How Intrusion Prevention Systems Work

---

## CCNA3-015 · Network Fundamentals

Objectives: 1.6 · multiple · Applied

Which TWO host addresses belong to 172.18.8.128/27 and are ordinary usable hosts? Select two.

- **A.** 172.18.8.127
- **B.** 172.18.8.128
- **C.** 172.18.8.129
- **D.** 172.18.8.158
- **E.** 172.18.8.160

**Answer: C, D**

The /27 block spans .128 through .159. The two boundary addresses are excluded from ordinary host assignment.

**Option explanations**

- **A:** It lies before this subnet and is the preceding /27 broadcast.
- **B:** This identifies the subnet itself.
- **C:** This is the first usable address in the subnet.
- **D:** This is the last usable address before broadcast .159.
- **E:** This starts the next /27 subnet.

**Further reading**

- [Configure IP Addresses and Unique Subnets for New Users](https://www.cisco.com/c/en/us/support/docs/ip/routing-information-protocol-rip/13788-3.html) — Network Masks; Understand Subnetting; VLSM Example

---

## CCNA3-016 · Network Fundamentals

Objectives: 1.9.d · single · Challenge

An interface forms a modified EUI-64 identifier from MAC 02-11-22-33-44-55. Which transformation is correct?

- **A.** Set the first byte to 03 and append FFFF
- **B.** Invert the 02 bit in the first byte and insert FF-FE in the middle
- **C.** Keep 02 unchanged because the MAC is locally administered
- **D.** Reverse all six MAC bytes before adding zeros

**Answer: B**

XOR 02 with 02 to obtain 00, and insert FF-FE between 22 and 33. An initially set U/L bit becomes clear.

**Option explanations**

- **A:** This changes the wrong bit and inserts the wrong value.
- **B:** The resulting identifier is 0011:22ff:fe33:4455.
- **C:** The specified modified EUI-64 procedure still inverts the U/L bit.
- **D:** Byte reversal is not the specified transformation.

**Further reading**

- [RFC 2464: Transmission of IPv6 Packets over Ethernet Networks](https://datatracker.ietf.org/doc/html/rfc2464#section-4) — 4. Stateless Autoconfiguration

---

## CCNA3-017 · Network Fundamentals

Objectives: 1.11.a · single · Applied

Under a conventional US 2.4 GHz, 20 MHz plan, AP A already uses channel 1 and AP B uses channel 11. Which available channel best avoids overlap with both?

- **A.** 2
- **B.** 10
- **C.** 3
- **D.** 6

**Answer: D**

The listed neighboring channel numbers are not independent 20 MHz channels. Channel 6 provides the intended separation between 1 and 11.

**Option explanations**

- **A:** It overlaps channel 1.
- **B:** It overlaps channel 11.
- **C:** It overlaps channel 1.
- **D:** It completes the conventional 1/6/11 plan.

**Further reading**

- [Channel Planning Best Practices](https://documentation.meraki.com/Wireless/Design_and_Configure/Architecture_and_Best_Practices/Channel_Planning_Best_Practices) — 2.4 GHz

---

## CCNA3-018 · Network Fundamentals

Objectives: 1.13.b, 1.13.c · multiple · Applied

Which TWO statements apply when an ordinary Layer 2 switch forwards a known unicast frame within one VLAN? Select two.

- **A.** It uses the destination MAC lookup to select the output port
- **B.** It decrements the packet’s IP TTL
- **C.** It changes the destination IP to the switch address
- **D.** It always floods every forwarding port
- **E.** It can learn or refresh the source MAC entry on ingress

**Answer: A, E**

A known destination avoids unknown-unicast flooding. Learning the source can still occur during the same received frame.

**Option explanations**

- **A:** The learned destination mapping guides forwarding.
- **B:** Ordinary Layer 2 switching is not an IP routing hop.
- **C:** Transparent bridging does not perform that rewrite.
- **D:** A known destination normally permits directed forwarding.
- **E:** Source learning and destination forwarding are separate operations.

**Further reading**

- [Configuring MAC Address Tables](https://www.cisco.com/c/en/us/td/docs/switches/datacenter/nexus5500/sw/layer2/7x/b_5500_Layer2_Config_7x/config_mac_address_tables.pdf) — Information About MAC Addresses (page 1); Configuring the Aging Time for the MAC Table (page 2)

---

## CCNA3-019 · Network Fundamentals

Objectives: 1.2.e · single · Foundation

A home office uses one integrated appliance for Wi-Fi, Ethernet switching, DHCP, and Internet routing. Which interpretation is correct?

- **A.** It is necessarily a three-tier campus
- **B.** Its wireless function eliminates the routing function
- **C.** One enclosure can combine several network component roles
- **D.** Every attached device must use a public address

**Answer: C**

SOHO products commonly integrate functions that larger designs distribute across devices. Count functions separately from physical boxes.

**Option explanations**

- **A:** An integrated small-office appliance does not establish three separate tiers.
- **B:** These functions can coexist.
- **C:** The functions remain conceptually distinct despite integration.
- **D:** Private addressing is common and compatible with this environment.

**Further reading**

- [How do I set up a small business network?](https://www.cisco.com/site/us/en/learn/topics/small-business/how-to-set-up-a-network.html) — Introduction; What is a switch?; What is a router?

---

## CCNA3-020 · Network Fundamentals

Objectives: 1.9.a, 1.9.c · matching · Applied

Match each IPv6 destination to its address category. Use each category once.

1. fd53:6a12:4900:1::10
2. fe80::e12
3. 2001:4860:5::7
4. ff02::2

- **A.** Link-local unicast
- **B.** Multicast
- **C.** Unique local unicast
- **D.** Global unicast

**Answer: 1 → C; 2 → A; 3 → D; 4 → B**

Prefix bits classify these addresses. Classification alone does not establish actual routing reachability.

**Option explanations**

- **A:** fe80::/10 is confined to a link.
- **B:** ff00::/8 identifies multicast destinations.
- **C:** The locally assigned ULA format begins fd.
- **D:** The example is in global-unicast address space.

**Further reading**

- [RFC 4291: IP Version 6 Addressing Architecture](https://www.rfc-editor.org/rfc/rfc4291#section-2.3) — 2.3. Text Representation of Address Prefixes; 2.4. Address Type Identification; 2.5.6. Link-Local IPv6 Unicast Addresses; 2.7. Multicast Addresses
- [RFC 4193: Unique Local IPv6 Unicast Addresses](https://www.rfc-editor.org/rfc/rfc4193#section-3.1) — 1. Introduction; 3.1. Format

---

## CCNA3-021 · Network Access

Objectives: 2.1.a · single · Applied

A voice deployment uses VLAN 150 for phones and VLAN 50 for attached PCs. The access switch performs only Layer 2 switching, and the VLAN 150 gateway is beyond its uplinks. The phone correctly tags voice for 150, but those uplinks only carry 50. Which change is required for calls to reach the remote call-control subnet?

- **A.** Carry VLAN 150 across the required uplinks to its gateway.
- **B.** Increase the access port’s STP priority.
- **C.** Remove the phone’s VLAN tag.
- **D.** Move the PC into VLAN 150.

**Answer: A**

Verify voice membership from the phone port through every trunk to the gateway. A working data VLAN can hide a missing voice VLAN upstream.

**Option explanations**

- **A:** Separating voice at the edge is insufficient unless that VLAN reaches its Layer 3 attachment.
- **B:** STP port priority does not add VLANs to an allowed list.
- **C:** The deployment explicitly places voice in tagged VLAN 150.
- **D:** This does not repair the missing voice path and changes the intended separation.

**Further reading**

- [VLAN Configuration Guide, Cisco IOS XE 17.15.x — Configuring Voice VLANs](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst9300/software/release/17-15/configuration_guide/vlan/b_1715_vlan_9300_cg/configuring_voice_vlans.html) — Cisco IP Phone Voice Traffic; Cisco IP Phone Data Traffic
- [VLAN Configuration Guide, Cisco IOS XE 17.15.x — Configuring VLAN Trunks](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst9300/software/release/17-15/configuration_guide/vlan/b_1715_vlan_9300_cg/configuring_vlan_trunks.html) — Allowed VLANs on a Trunk; Configuring the Native VLAN for Untagged Traffic

---

## CCNA3-022 · Network Access

Objectives: 2.1.c · single · Challenge

A switch SVI is administratively enabled, and VLAN 60 exists. All access ports in VLAN 60 are down and no forwarding trunk carries it. Default SVI autostate applies. What best explains Vlan60 having its line protocol down?

```text
Configuration summary:
Vlan60 address: 10.60.0.254/24
Administrative state: enabled
Line protocol: down
SVI autostate: default (no override)
```

- **A.** There is no operational Layer 2 forwarding member for VLAN 60.
- **B.** An SVI requires two active access ports.
- **C.** The SVI’s IP address must end in .1.
- **D.** VLAN 60 is outside the normal VLAN range.

**Answer: A**

The VLAN database, administrative state, and Layer 2 forwarding state are separate checks. The SVI needs a live forwarding attachment before its line protocol comes up.

**Option explanations**

- **A:** Default SVI autostate depends on an active forwarding attachment in its VLAN.
- **B:** One eligible forwarding member is sufficient under ordinary autostate behavior.
- **C:** Any suitable unicast host address in the subnet can be a gateway.
- **D:** VLAN 60 is a normal-range VLAN.

**Further reading**

- [Interface and Hardware Components Configuration Guide, Cisco IOS XE 17.15.x — Configuring Interface Characteristics](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst9300/software/release/17-15/configuration_guide/int_hw/b_1715_int_and_hw_9300_cg/configuring_interface_characteristics.html) — Switch Virtual Interfaces; Layer 3 Interfaces; Configuring SVI Autostate Exclude

---

## CCNA3-023 · Network Access

Objectives: 2.1.a, 2.1.b · multiple · Applied

After a factory-reset Catalyst switch is installed, unconfigured user access ports forward ordinary data in VLAN 1. Policy places users in VLAN 80. Select TWO appropriate actions.

- **A.** Delete VLAN 1 from the switch.
- **B.** Explicitly assign the user access ports to VLAN 80.
- **C.** Change only the switch hostname to Users80.
- **D.** Create or verify VLAN 80 in the local VLAN database.

**Answer: B, D**

Moving from defaults requires both VLAN availability and explicit access assignments. Renaming a device or removing the default VLAN is not a substitute.

**Option explanations**

- **A:** VLAN 1 is the built-in default VLAN and cannot simply be deleted.
- **B:** Default access membership otherwise remains VLAN 1.
- **C:** A hostname does not configure VLAN membership.
- **D:** The intended VLAN must exist for the access ports to operate in it.

**Further reading**

- [VLAN Configuration Guide, Cisco IOS XE 17.15.x — Configuring VLANs](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst9300/software/release/17-15/configuration_guide/vlan/b_1715_vlan_9300_cg/configuring_vlans.html) — Supported VLANs; Deleting a VLAN; VLAN Port Membership Modes

---

## CCNA3-024 · Network Access

Objectives: 2.2.a · single · Applied

The displayed trunk summary comes from a switch using locally configured VLANs. VLAN 222 should reach a host beyond this link. Which local condition is missing?

```text
Port     Mode  Encapsulation  Status    Native vlan
Gi1/0/48 on    802.1q         trunking  1
Vlans allowed on trunk: 1-4094
Vlans allowed and active in management domain: 1,110
Vlans in spanning tree forwarding state and not pruned: 1,110
```

- **A.** The interface is physically down.
- **B.** VLAN 222 is excluded from the allowed list.
- **C.** VLAN 222 is not active in this switch’s VLAN database.
- **D.** Native VLAN 1 must be changed to 222.

**Answer: C**

Interpret each trunk summary stage separately. Permission on the trunk does not create the VLAN locally.

**Option explanations**

- **A:** The status explicitly says trunking.
- **B:** The allowed range 1-4094 includes 222.
- **C:** It is allowed but absent from the allowed-and-active list.
- **D:** A nonnative VLAN can cross as tagged traffic without becoming native.

**Further reading**

- [VLAN Configuration Guide, Cisco IOS XE 17.15.x — Configuring VLAN Trunks](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst9300/software/release/17-15/configuration_guide/vlan/b_1715_vlan_9300_cg/configuring_vlan_trunks.html) — Allowed VLANs on a Trunk; Configuring the Native VLAN for Untagged Traffic
- [VLAN Configuration Guide, Cisco IOS XE 17.15.x — Configuring VLANs](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst9300/software/release/17-15/configuration_guide/vlan/b_1715_vlan_9300_cg/configuring_vlans.html) — Supported VLANs; Deleting a VLAN; VLAN Port Membership Modes

---

## CCNA3-025 · Network Access

Objectives: 2.2.b · single · Foundation

A packet capture on an interswitch trunk shows an ordinary Ethernet frame with an 802.1Q VLAN ID of 36. The receiving trunk permits VLAN 36; its native VLAN is 99. Which classification applies?

- **A.** The VLAN matching the destination MAC’s last byte
- **B.** VLAN 1, because switches remove tags before forwarding
- **C.** VLAN 99, because native VLAN overrides all tags
- **D.** VLAN 36, using the explicit tag

**Answer: D**

A native VLAN is not a default override for valid tagged traffic. The 802.1Q VID identifies the frame as VLAN 36.

**Option explanations**

- **A:** VLAN membership is not encoded in a MAC suffix.
- **B:** Removing a tag for an eventual access egress does not erase internal VLAN identity.
- **C:** Native classification is relevant to ordinary untagged ingress traffic.
- **D:** A valid nonnative tag identifies this frame’s VLAN.

**Further reading**

- [VLAN Configuration Guide, Cisco IOS XE 17.15.x — Configuring VLAN Trunks](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst9300/software/release/17-15/configuration_guide/vlan/b_1715_vlan_9300_cg/configuring_vlan_trunks.html) — Allowed VLANs on a Trunk; Configuring the Native VLAN for Untagged Traffic

---

## CCNA3-026 · Network Access

Objectives: 2.3 · single · Applied

LLDP is globally enabled on a Catalyst switch. The peer transmits LLDP, and the link is healthy, but the local neighbor table remains empty after all old entries have aged out. Which command repairs the displayed local configuration while preserving local advertisement?

```text
lldp run
interface GigabitEthernet1/0/10
 lldp transmit
 no lldp receive
```

- **A.** ip routing
- **B.** no lldp transmit
- **C.** cdp enable
- **D.** lldp receive

**Answer: D**

LLDP has independent transmit and receive controls. Here the local receive setting is the demonstrated blocker.

**Option explanations**

- **A:** LLDP neighbor learning does not require IP routing.
- **B:** This would stop advertising without enabling reception.
- **C:** CDP configuration does not enable LLDP reception.
- **D:** Reception is disabled on this interface despite global LLDP operation.

**Further reading**

- [Interface and Hardware Components Configuration Guide, Cisco IOS XE 17.15.x — Configuring LLDP, LLDP-MED, and Wired Location Service](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst9300/software/release/17-15/configuration_guide/int_hw/b_1715_int_and_hw_9300_cg/configuring_lldp__lldp_med__and_wired_location_service.html) — LLDP; Enabling LLDP; Monitoring and Maintaining LLDP, LLDP-MED, and Wired Location Service

---

## CCNA3-027 · Network Access

Objectives: 2.4 · single · Applied

A Layer 2 EtherChannel’s two intended members use the same speed and duplex, but one is an access port and the other a trunk. What should the engineer do before expecting a valid bundle?

```text
Gi1/0/1: switchport mode access; access vlan 18
Gi1/0/2: switchport mode trunk; allowed vlan 18,28
Both: channel-group 9 mode active
```

- **A.** Add an IP address to each member.
- **B.** Use different channel-group numbers on the local members.
- **C.** Make the Layer 2 modes and relevant VLAN settings consistent.
- **D.** Configure mode on to ignore the inconsistency.

**Answer: C**

LACP is not a replacement for compatible member configuration. Correct the access/trunk mismatch before verifying negotiation and traffic.

**Option explanations**

- **A:** That conflicts with the intended Layer 2 bundle and does not reconcile the modes.
- **B:** That would create different logical groups rather than one bundle.
- **C:** Members of one Layer 2 logical link must agree on these switching properties.
- **D:** Static mode is not a safe remedy for incompatible member settings.

**Further reading**

- [Layer 2 Configuration Guide, Cisco IOS XE 17.15.x — Configuring EtherChannels](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst9300/software/release/17-15/configuration_guide/lyr2/b_1715_lyr2_9300_cg/configuring_etherchannels.html) — LACP Modes; EtherChannel Configuration Guidelines; Load Balancing; Layer 3 EtherChannels; Hot-Standby Ports

---

## CCNA3-028 · Network Access

Objectives: 2.4 · multiple · Applied

A routed LACP bundle has Po12(RU), two member interfaces flagged P, and 192.0.2.2/30 on Port-channel12. The peer uses 192.0.2.1/30. Which TWO checks address the intended Layer 3 adjacency? Select TWO.

- **A.** Create VLAN 12 because the channel number must match a VLAN.
- **B.** Verify Port-channel12 is up/up and ping the peer’s 192.0.2.1 address.
- **C.** Verify no switchport on the port-channel and compatible routed members.
- **D.** Assign 192.0.2.2 to each physical member.

**Answer: B, C**

Verify the aggregate as one routed interface. Successful LACP membership establishes link aggregation but still needs Layer 3 verification.

**Option explanations**

- **A:** The port-channel number does not imply a VLAN.
- **B:** This checks the logical routed link and direct peer IP reachability.
- **C:** The intended aggregate is routed, as indicated by R.
- **D:** The logical interface owns the bundle’s Layer 3 address.

**Further reading**

- [Layer 2 Configuration Guide, Cisco IOS XE 17.15.x — Configuring EtherChannels](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst9300/software/release/17-15/configuration_guide/lyr2/b_1715_lyr2_9300_cg/configuring_etherchannels.html) — LACP Modes; EtherChannel Configuration Guidelines; Load Balancing; Layer 3 EtherChannels; Hot-Standby Ports

---

## CCNA3-029 · Network Access

Objectives: 2.5.a · single · Challenge

A nonroot switch sees the same root bridge through two upstream paths. Gi1/0/1 receives advertised cost 12 and has local cost 4. Gi1/0/2 receives advertised cost 0 and has local cost 19. Which becomes its root port, assuming no other paths?

- **A.** Gi1/0/2, because its upstream neighbor is the root
- **B.** Gi1/0/2, because advertised cost zero ignores local cost
- **C.** Gi1/0/1, with total root-path cost 16
- **D.** Both, because each can reach the same root

**Answer: C**

Compare complete path costs, not hop count or only the neighbor’s advertised cost. The indirect path costs 16 and wins.

**Option explanations**

- **A:** A direct path is not automatically preferred over a lower-cost indirect path.
- **B:** The local interface cost must be added.
- **C:** The received cost and local ingress-port cost sum to 16, lower than 19.
- **D:** A nonroot switch selects one root port per spanning-tree instance.

**Further reading**

- [Layer 2 Configuration Guide, Cisco IOS XE 17.15.x — Configuring Spanning Tree Protocol](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst9300/software/release/17-15/configuration_guide/lyr2/b_1715_lyr2_9300_cg/configuring_spanning_tree_protocol.html) — Spanning-Tree Topology and Bridge Protocol Data Units; Bridge ID, Device Priority, and Extended System ID; (Optional) Configuring a Secondary Root Device
- [Understand Rapid Spanning Tree Protocol (802.1w)](https://www.cisco.com/c/en/us/support/docs/lan-switching/spanning-tree-protocol/24062-146.html) — New Port States and Port Roles — Port States; Alternate and Backup Port Roles

---

## CCNA3-030 · Network Access

Objectives: 2.5.b · single · Applied

A Rapid PVST+ port is temporarily in the learning state. Which behavior distinguishes learning from both discarding and forwarding?

- **A.** It forwards frames only when their IP TTL is greater than one.
- **B.** It forwards user frames but cannot learn MAC addresses.
- **C.** It neither learns MAC addresses nor forwards user frames.
- **D.** It learns source MAC addresses but does not forward ordinary user frames.

**Answer: D**

Port state describes forwarding and learning behavior. A port can learn before it is permitted to carry normal transit data.

**Option explanations**

- **A:** STP state controls Layer 2 forwarding independently of IP TTL.
- **B:** That reverses learning-state behavior.
- **C:** That describes discarding for ordinary data traffic.
- **D:** Learning builds MAC information without opening the data forwarding path.

**Further reading**

- [Understand Rapid Spanning Tree Protocol (802.1w)](https://www.cisco.com/c/en/us/support/docs/lan-switching/spanning-tree-protocol/24062-146.html) — New Port States and Port Roles — Port States; Alternate and Backup Port Roles

---

## CCNA3-031 · Network Access

Objectives: 2.5.c, 2.5.d · single · Applied

The design requires fast startup on a workstation port and shutdown if any BPDU arrives from that port. Which configuration meets both requirements?

- **A.** spanning-tree guard loop only
- **B.** spanning-tree portfast; spanning-tree bpdufilter enable
- **C.** spanning-tree portfast; spanning-tree bpduguard enable
- **D.** spanning-tree guard root only

**Answer: C**

Use separate features for fast edge connectivity and BPDU-triggered shutdown. Explicit BPDU filtering undermines the desired detection behavior.

**Option explanations**

- **A:** Loop guard addresses lost expected BPDUs on nonedge paths.
- **B:** Explicit BPDU filtering hides BPDUs rather than triggering the required shutdown.
- **C:** PortFast accelerates the edge transition and interface BPDU guard rejects unexpected bridges.
- **D:** Root guard addresses superior root information, not every BPDU or edge startup.

**Further reading**

- [Layer 2 Configuration Guide, Cisco IOS XE 17.15.x — Configuring Optional Spanning-Tree Features](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst9300/software/release/17-15/configuration_guide/lyr2/b_1715_lyr2_9300_cg/configuring_optional_spanning_tree_features.html) — PortFast; Bridge Protocol Data Unit Guard; Bridge Protocol Data Unit Filtering; Root Guard; Loop Guard

---

## CCNA3-032 · Network Access

Objectives: 2.5.d · single · Challenge

A point-to-point alternate port protected by loop guard stops receiving expected BPDUs while its physical link stays up. Why is automatic promotion to designated forwarding prevented?

- **A.** Any nonzero BPDU count requires error-disable.
- **B.** Loss of BPDUs may reflect a one-way failure rather than removal of the Layer 2 loop.
- **C.** Loop guard elects itself the root bridge.
- **D.** The port must be a workstation PortFast edge.

**Answer: B**

A physically up link can still fail in one direction. Loop guard prevents that information loss from opening an unsafe forwarding path.

**Option explanations**

- **A:** Loop guard reacts to missing expected BPDUs, not any received BPDU.
- **B:** Loop guard preserves blocking when expected topology information disappears.
- **C:** It protects port behavior; it does not win root election.
- **D:** An alternate port is an upstream nonedge topology role.

**Further reading**

- [Understand STP Loop Guard and UDLD Features](https://www.cisco.com/c/en/us/support/docs/lan-switching/spanning-tree-protocol-stp-8021d/218321-configure-stp-with-loop-guard-and-bpdu-s.html) — STP Port Roles; STP Loop Guard

---

## CCNA3-033 · Network Access

Objectives: 2.6 · single · Applied

An enterprise uses Meraki bridge-mode SSIDs. Which traffic normally needs the Meraki cloud for management, while ordinary local client forwarding remains on site?

- **A.** All local Ethernet broadcasts before delivery to any access port
- **B.** Dashboard configuration and device-management telemetry
- **C.** Every client frame between a laptop and its local printer
- **D.** Every radio acknowledgment between AP and client

**Answer: B**

A cloud-managed architecture separates management from the local data path. A cloud dashboard does not imply that all user traffic is cloud tunneled.

**Option explanations**

- **A:** The cloud is not the local Ethernet broadcast relay.
- **B:** Cloud management exchanges configuration and operational information with devices.
- **C:** Bridge-mode client data need not transit the Meraki management cloud.
- **D:** 802.11 acknowledgments are time-sensitive local radio exchanges.

**Further reading**

- [Meraki Cloud Architecture](https://documentation.meraki.com/Platform_Management/Dashboard_Administration/Design_and_Configure/Architectures_and_Best_Practices/Cisco_Meraki_Best_Practice_Design/Meraki_Cloud_Architecture) — Network and Management Data Segregation; The Meraki dashboard

---

## CCNA3-034 · Network Access

Objectives: 2.6 · single · Applied

A warehouse cannot cable one remote AP back to the LAN but has supported mesh APs and a viable wireless backhaul path. Which operating role is relevant to that backhaul requirement?

- **A.** Dedicated monitor mode
- **B.** Dedicated sniffer mode
- **C.** Bridge/mesh mode
- **D.** Rogue detector mode

**Answer: C**

A mesh design must provide a supported wireless backhaul path and suitable root attachment. Verify the particular AP’s mesh capabilities.

**Option explanations**

- **A:** Monitoring observes RF; it is not a client/backhaul forwarding replacement.
- **B:** Capturing frames does not supply a production backhaul.
- **C:** Supported bridge-mode deployments use wireless backhaul between mesh APs.
- **D:** This legacy mode inspects wired activity and does not build mesh backhaul.

**Further reading**

- [Cisco Wireless Controller Configuration Guide, Release 8.5 — Managing APs](https://www.cisco.com/c/en/us/td/docs/wireless/controller/8-5/config-guide/b_cg85/managing_aps.html) — AP Modes: client-serving and network management modes

---

## CCNA3-035 · Network Access

Objectives: 2.7 · single · Applied

An AP joins its remote WLC across two routed subnets. All WLANs are centrally switched. Which infrastructure statement is accurate?

- **A.** Every router between them must act as an 802.1Q trunk bridge.
- **B.** IP reachability can transport CAPWAP without extending the AP management VLAN to the WLC.
- **C.** AP and WLC must share the same Ethernet broadcast domain.
- **D.** The console cable provides the CAPWAP data channel.

**Answer: B**

Do not confuse controller discovery and IP transport with a requirement for one Layer 2 segment. The necessary tunnel traffic must be permitted end to end.

**Option explanations**

- **A:** The tunnel is carried by normal Layer 3 forwarding.
- **B:** CAPWAP uses an IP transport across the routed network.
- **C:** A routed IP path is supported for their tunnel.
- **D:** The console is not the AP’s network tunnel transport.

**Further reading**

- [Cisco Wireless Controller Configuration Guide, Release 8.10 — AP Connectivity to Controller](https://www.cisco.com/c/en/us/td/docs/wireless/controller/8-10/config-guide/b_cg810/ap_connectivity_to_cisco_wlc.html) — CAPWAP

---

## CCNA3-036 · Network Access

Objectives: 2.7 · single · Applied

AireOS LAG is already operational over two controller distribution ports. One member cable fails; the remaining member and adjacent switch remain healthy. Which outcome is the purpose of this aggregation?

- **A.** The controller requires a different management IP for the remaining cable.
- **B.** The logical uplink can continue through the remaining member with reduced aggregate capacity.
- **C.** LAG creates a replacement physical controller.
- **D.** All WLAN client VLANs must become native immediately.

**Answer: B**

LAG protects against loss of an individual member link within its design limits. It does not make the controller chassis itself redundant.

**Option explanations**

- **A:** The aggregate preserves the logical interfaces across member changes.
- **B:** Member redundancy preserves a surviving path while losing that member’s bandwidth.
- **C:** Link aggregation does not provide controller hardware redundancy.
- **D:** Member failure does not require changing VLAN tagging.

**Further reading**

- [Cisco Wireless Controller Configuration Guide, Release 8.10 — Ports and Interfaces](https://www.cisco.com/c/en/us/td/docs/wireless/controller/8-10/config-guide/b_cg810/ports_and_interfaces.html) — Restrictions on Link Aggregation; Configuring Neighbor Devices to Support Link Aggregation

---

## CCNA3-037 · Network Access

Objectives: 2.8 · matching · Applied

Match each management requirement to the appropriate mechanism. Use each answer once.

1. Encrypted terminal session over an operational IP network
2. Encrypted web GUI session from a browser
3. Local recovery when the management IP configuration is unusable
4. Central server governing administrator login and command permissions

- **A.** Console
- **B.** HTTPS
- **C.** SSH
- **D.** TACACS+

**Answer: 1 → C; 2 → B; 3 → A; 4 → D**

An access method carries an operator session, while AAA decides and records access. Console provides a separate local access path.

**Option explanations**

- **A:** A direct console connection can operate without the device’s IP path.
- **B:** HTTPS protects browser management using TLS.
- **C:** SSH provides an encrypted interactive remote CLI.
- **D:** TACACS+ supplies centralized device-management AAA services.

**Further reading**

- [Cisco Wireless Controller Configuration Guide, Release 8.10 — Administration of Controller](https://www.cisco.com/c/en/us/td/docs/wireless/controller/8-10/config-guide/b_cg810/administration_of_cisco_wlc.html) — Logging on to the Controller CLI; Enabling Web and Secure Web Modes (GUI); Enabling Web and Secure Web Modes (CLI)
- [Cisco Wireless Controller Configuration Guide, Release 8.10 — AAA Administration](https://www.cisco.com/c/en/us/td/docs/wireless/controller/8-10/config-guide/b_cg810/aaa_administration.html) — Configuring TACACS+ (GUI)

---

## CCNA3-038 · Network Access

Objectives: 2.9 · single · Applied

In the applied AireOS WLAN GUI, Broadcast SSID is disabled but the WLAN and radios are enabled. The client has the exact SSID and correct security settings manually configured. What is the best interpretation?

- **A.** Disabling broadcast always disables the WLAN.
- **B.** The WLAN can still support a manually configured client; hiding its name is not authentication.
- **C.** The SSID becomes the controller’s profile name.
- **D.** Any client can now join without credentials.

**Answer: B**

A hidden SSID may require manual client configuration. It is not a replacement for a secure authentication and encryption method.

**Option explanations**

- **A:** WLAN status and SSID broadcasting are distinct settings.
- **B:** Broadcast suppression affects ordinary discovery, not the configured authentication method.
- **C:** Disabling broadcast does not change the SSID.
- **D:** The security method remains in effect.

**Further reading**

- [Cisco Wireless Controller Configuration Guide, Release 8.10 — WLANs](https://www.cisco.com/c/en/us/td/docs/wireless/controller/8-10/config-guide/b_cg810/wlans.html) — Prerequisites for WLANs; Enabling and Disabling WLANs (GUI); Editing WLAN SSID or Profile Name for WLANs (GUI)
- [Cisco Wireless Controller Configuration Guide, Release 8.10 — WLAN Security](https://www.cisco.com/c/en/us/td/docs/wireless/controller/8-10/config-guide/b_cg810/wlan_security.html) — Configuring WPA1+WPA2 (GUI); Configuring Peer-to-Peer Blocking (GUI)

---

## CCNA3-039 · Network Access

Objectives: 2.9 · single · Applied

AireOS shows WPA2 policy and AES enabled, but Auth Key Management is 802.1X. The technician is trying to connect a PSK-only handheld. Other enterprise clients authenticate successfully. What mismatch must be addressed?

| Security field | Applied value |
| --- | --- |
| WPA2 Policy | Enabled |
| WPA2 Encryption | AES |
| Auth Key Management | 802.1X |
| PSK | Disabled |

- **A.** The WLAN profile name must equal the handheld username.
- **B.** The handheld expects a shared key while the WLAN requires 802.1X.
- **C.** AES means the SSID is hidden.
- **D.** The QoS profile prevents every PSK exchange.

**Answer: B**

Check both the encryption policy and authentication/key-management method. Use a compatible client profile or a separately approved PSK WLAN.

**Option explanations**

- **A:** Profile labels are not identity credentials.
- **B:** WPA2 cipher compatibility alone does not make authentication methods interchangeable.
- **C:** Cipher selection does not control SSID advertising.
- **D:** QoS selection is not the demonstrated authentication mismatch.

**Further reading**

- [Cisco Wireless Controller Configuration Guide, Release 8.10 — WLAN Security](https://www.cisco.com/c/en/us/td/docs/wireless/controller/8-10/config-guide/b_cg810/wlan_security.html) — Configuring WPA1+WPA2 (GUI); Configuring Peer-to-Peer Blocking (GUI)

---

## CCNA3-040 · Network Access

Objectives: 2.9 · multiple · Applied

A centrally switched AireOS guest WLAN must send wireless peer unicast traffic toward an upstream policy device instead of locally bridging it. The standard video QoS profile is also required. Which TWO GUI selections match this request? Select TWO.

- **A.** P2P Blocking Action = Forward-UpStream
- **B.** QoS = Gold
- **C.** P2P Blocking Action = Drop
- **D.** QoS = Silver

**Answer: A, B**

The advanced peer action chooses how peer traffic leaves the controller; the QoS profile independently chooses the intended class. The upstream design must still enforce policy.

**Option explanations**

- **A:** This selects upstream forwarding rather than local peer forwarding or unconditional drop.
- **B:** Gold is the standard AireOS video profile.
- **C:** Drop discards peer traffic rather than delivering it to the upstream policy path.
- **D:** Silver is best effort, not the requested video profile.

**Further reading**

- [Cisco Wireless Controller Configuration Guide, Release 8.10 — WLAN Security](https://www.cisco.com/c/en/us/td/docs/wireless/controller/8-10/config-guide/b_cg810/wlan_security.html) — Configuring WPA1+WPA2 (GUI); Configuring Peer-to-Peer Blocking (GUI)
- [Cisco Wireless Controller Configuration Guide, Release 8.10 — Wireless Quality of Service](https://www.cisco.com/c/en/us/td/docs/wireless/controller/8-10/config-guide/b_cg810/wireless_quality_of_service.html) — QoS Profiles; Configuring QoS Profiles (GUI); Assigning a QoS Profile to a WLAN (GUI)

---

## CCNA3-041 · IP Connectivity

Objectives: 3.1.d · single · Applied

A route to 10.96.0.0/16 lists “via 192.0.2.2, GigabitEthernet0/0.” Which address is normally resolved to a destination Ethernet MAC on that directly attached transit link?

- **A.** The packet’s original source address
- **B.** The remote host in 10.96.0.0/16
- **C.** The OSPF process number
- **D.** 192.0.2.2

**Answer: D**

The IP destination remains the remote host during ordinary routing. The outgoing Ethernet frame is addressed to the adjacent router.

**Option explanations**

- **A:** The source does not determine the outgoing frame’s destination MAC.
- **B:** The remote host is behind the next hop, not on this Ethernet segment.
- **C:** A process number is not an IP neighbor address.
- **D:** The adjacent next-hop router is the Layer 2 destination for the forwarded frame.

**Further reading**

- [RFC 1812: Requirements for IP Version 4 Routers](https://www.rfc-editor.org/rfc/rfc1812.html) — 5.2.4 Determining the Next Hop Address

---

## CCNA3-042 · IP Connectivity

Objectives: 3.1.a, 3.1.e · single · Applied

The displayed connected interface goes down and both C and L entries disappear. What is the most accurate interpretation?

```text
Before failure:
C 198.51.100.8/30 is directly connected, GigabitEthernet0/2
L 198.51.100.9/32 is directly connected, GigabitEthernet0/2
```

- **A.** A remote router withdrew these routes with an OSPF update.
- **B.** The OSPF process has deleted every route in area 0.
- **C.** The router has lost this connected subnet route and its local-address route.
- **D.** The interface’s administrative distance rose from 0 to 255.

**Answer: C**

Routing-table source codes identify how an entry exists. Losing the interface can remove both its attached-network route and local host route.

**Option explanations**

- **A:** These local entries derive from this router’s interface state.
- **B:** C and L entries do not by themselves describe all OSPF routes.
- **C:** The two entries correspond to the subnet and the router’s own interface address.
- **D:** Route removal follows interface availability, not an automatic AD increase.

**Further reading**

- [Local Host Routes Installed in the Routing Table on Cisco IOS and Cisco IOS-XR](https://www.cisco.com/c/en/us/support/docs/ip/ip-routing/116264-technote-ios-00.html) — Cisco IOS Local Routes; Manually Configured Host Routes

---

## CCNA3-043 · IP Connectivity

Objectives: 3.2.a, 3.1.c · single · Challenge

A maintenance change adds an installed route to 172.30.64.0/18 through a new exit. A previously installed 172.30.80.0/20 route stays valid. Which traffic is redirected to the new exit?

- **A.** 172.30.127.7 and 172.30.129.7 together
- **B.** 172.30.100.7
- **C.** 172.30.83.7
- **D.** Every address in 172.30.0.0/16

**Answer: B**

A route change affects the destinations for which that prefix becomes the best match. More specific retained routes continue to override it.

**Option explanations**

- **A:** The /18 ends at third octet 127; 129 is outside it.
- **B:** It matches the /18 but lies outside the retained /20, which spans third octets 80–95.
- **C:** The retained /20 remains more specific for this destination.
- **D:** The new /18 covers only third octets 64–127.

**Further reading**

- [Configure Route Selection for Routers](https://www.cisco.com/c/en/us/support/docs/ip/enhanced-interior-gateway-routing-protocol-eigrp/8651-21.html) — Build the Routing Table; Make Forwarding Decisions
- [RFC 1812: Requirements for IP Version 4 Routers](https://www.rfc-editor.org/rfc/rfc1812.html) — 5.2.4 Determining the Next Hop Address

---

## CCNA3-044 · IP Connectivity

Objectives: 3.2.b, 3.2.c · single · Applied

For one exact /24 prefix, an OSPF intra-area path has metric 8 and distance 110. An internal EIGRP candidate has metric 51200 and distance 90. Both are valid. Why can the EIGRP route be installed?

- **A.** 51200 represents more available bandwidth than 8 in the same units.
- **B.** Its route source has the lower administrative distance.
- **C.** The larger metric always wins.
- **D.** OSPF can never install /24 routes.

**Answer: B**

A small metric does not make a route universally better across routing protocols. Both candidates must first be compared using the applicable local source preference.

**Option explanations**

- **A:** The values do not share a common cross-protocol metric unit.
- **B:** Different protocol metrics are not directly comparable; source preference decides here.
- **C:** These protocol metrics do not use a universal larger-is-better rule.
- **D:** OSPF supports /24 prefixes; its lower preference is the issue here.

**Further reading**

- [Understand Administrative Distance](https://www.cisco.com/c/en/us/support/docs/ip/border-gateway-protocol-bgp/15986-admin-distance.html) — RIB Route Comparison; Route Installation; Default AD Values

---

## CCNA3-045 · IP Connectivity

Objectives: 3.3.a, 3.3.b, 3.3.c, 3.3.d · matching · Applied

Match each static-route requirement to the appropriate route design.

1. Reach unknown external destinations through the only exit
2. Send only 10.150.8.0/21 toward the warehouse
3. Pin only 2001:db8:900::7 to a maintenance path
4. Use a standby path only after the preferred route disappears

- **A.** Network route
- **B.** Default route
- **C.** Floating static route
- **D.** Host route

**Answer: 1 → B; 2 → A; 3 → D; 4 → C**

Route scope and route preference solve different requirements. A floating static can itself be a default, network, or host route.

**Option explanations**

- **A:** A network route covers an explicitly selected subnet or aggregate.
- **B:** A default provides a catch-all when no more specific route matches.
- **C:** A higher-distance static stands behind a preferred route to the same prefix.
- **D:** A host route specifies exactly one IPv4 /32 or IPv6 /128 destination.

**Further reading**

- [Configure a Next Hop IP Address for Static Routes](https://www.cisco.com/c/en/us/support/docs/dial-access/floating-static-route/118263-technote-nexthop-00.html) — Background Information; Floating Static Route Example
- [IPv6 Routing: Static Routing — Cisco IOS XE 17.x](https://www.cisco.com/c/en/us/td/docs/routers/ios/config/17-x/ip-routing/b-ip-routing/m_ip6-route-static-xe.html) — Recursive Static Routes; Fully Specified Static Routes; Floating Static Routes

---

## CCNA3-046 · IP Connectivity

Objectives: 3.3.a · single · Applied

An IPv6-enabled branch must send destinations absent from its more specific routes to adjacent global next hop 2001:db8:10::2. Which Cisco IOS command expresses this?

- **A.** ip route 0.0.0.0 0.0.0.0 2001:db8:10::2
- **B.** ipv6 route 2001:db8:10::/64 ::
- **C.** ipv6 route ::/128 2001:db8:10::2
- **D.** ipv6 route ::/0 2001:db8:10::2

**Answer: D**

IPv6 defaults use ::/0. More specific IPv6 routes continue to win when they match.

**Option explanations**

- **A:** The IPv4 command cannot express an IPv6 route this way.
- **B:** This names the transit subnet rather than a default and lacks a useful neighbor.
- **C:** This covers only the all-zero address.
- **D:** The zero-length IPv6 prefix matches every IPv6 destination.

**Further reading**

- [IPv6 Routing: Static Routing — Cisco IOS XE 17.x](https://www.cisco.com/c/en/us/td/docs/routers/ios/config/17-x/ip-routing/b-ip-routing/m_ip6-route-static-xe.html) — Recursive Static Routes; Fully Specified Static Routes; Floating Static Routes

---

## CCNA3-047 · IP Connectivity

Objectives: 3.3.b · single · Applied

R1 can ping R2’s transit address, but a host behind R1 cannot ping a host behind R2. R1 has a route to R2’s LAN; R2 has no route or default matching R1’s LAN. ACLs and host gateways are correct. What route is missing?

- **A.** A route on R2 back to R1’s LAN
- **B.** Another route on R1 to R2’s transit subnet
- **C.** A lower OSPF router ID on R2
- **D.** A host route on R1 to its own interface address

**Answer: A**

End-to-end communication requires valid forwarding in both directions. A successful adjacent-interface ping tests a narrower path than LAN-to-LAN traffic.

**Option explanations**

- **A:** The echo reply needs a return path to the original source network.
- **B:** The successful transit ping already demonstrates that connected reachability.
- **C:** Router-ID ordering does not supply the missing static return path.
- **D:** A local interface route does not repair R2’s return lookup.

**Further reading**

- [Configure a Next Hop IP Address for Static Routes](https://www.cisco.com/c/en/us/support/docs/dial-access/floating-static-route/118263-technote-nexthop-00.html) — Background Information; Floating Static Route Example
- [RFC 1812: Requirements for IP Version 4 Routers](https://www.rfc-editor.org/rfc/rfc1812.html) — 5.2.4 Determining the Next Hop Address

---

## CCNA3-048 · IP Connectivity

Objectives: 3.3.c · single · Applied

An engineer entered the first command to isolate one IPv6 server. It also redirects other servers in that subnet. Which replacement narrows the route correctly?

```text
Existing command:
ipv6 route 2001:db8:450::/64 2001:db8:1::2
Required exception: only 2001:db8:450::25
```

- **A.** ipv6 route ::/0 2001:db8:1::2
- **B.** ipv6 route 2001:db8:450::25/128 2001:db8:1::2
- **C.** ipv6 route 2001:db8:450::/48 2001:db8:1::2
- **D.** ipv6 route 2001:db8:450::/64 2001:db8:1::2 250

**Answer: B**

Use prefix length to limit scope. Administrative distance is not an address filter.

**Option explanations**

- **A:** A default is broader still and does not isolate one server.
- **B:** The /128 fixes all address bits and selects only the named server.
- **C:** A /48 broadens the affected destination space.
- **D:** Raising distance changes preference, not the /64 destination scope.

**Further reading**

- [IPv6 Routing: Static Routing — Cisco IOS XE 17.x](https://www.cisco.com/c/en/us/td/docs/routers/ios/config/17-x/ip-routing/b-ip-routing/m_ip6-route-static-xe.html) — Recursive Static Routes; Fully Specified Static Routes; Floating Static Routes

---

## CCNA3-049 · IP Connectivity

Objectives: 3.3.d · single · Applied

A router’s backup static route has administrative distance 255. Its next hop is reachable, and the preferred route has disappeared. Why does the backup still not install?

- **A.** Distance 255 marks an unusable route source on Cisco IOS.
- **B.** All static routes require administrative distance exactly 1.
- **C.** The route must have a /0 prefix to float.
- **D.** The next-hop IP must equal the destination network address.

**Answer: A**

A floating route needs a usable distance higher than the primary, such as 200 when appropriate. The maximum numeric value is not a functioning emergency preference.

**Option explanations**

- **A:** 255 is not an ordinary last-choice distance; such routes are not installed.
- **B:** Usable higher distances are routinely used for floating statics.
- **C:** Host and network routes can also be floating statics.
- **D:** Next-hop and destination-prefix roles are separate.

**Further reading**

- [Understand Administrative Distance](https://www.cisco.com/c/en/us/support/docs/ip/border-gateway-protocol-bgp/15986-admin-distance.html) — RIB Route Comparison; Route Installation; Default AD Values

---

## CCNA3-050 · IP Connectivity

Objectives: 3.3.b, 3.3.d · multiple · Challenge

Two proposed backup commands are shown. A dynamic primary covers 10.72.0.0/16 with distance 110. Both proposed next hops resolve. Which two statements are correct? Select two.

```text
1: ip route 10.72.0.0 255.255.0.0 192.0.2.2 200
2: ip route 10.72.9.0 255.255.255.0 192.0.2.6 200
```

- **A.** Command 1 can float behind the /16 primary.
- **B.** Command 2 can redirect matching /24 traffic while the primary remains.
- **C.** Command 2 is less specific than command 1.
- **D.** Both commands remain inactive solely because their distances exceed 110.

**Answer: A, B**

To float behind a primary, match its destination prefix as well as choosing a higher distance. A more specific route changes forwarding scope.

**Option explanations**

- **A:** It competes for the same prefix with a higher distance.
- **B:** The /24 is a distinct more specific destination, not a backup candidate for the /16.
- **C:** A /24 fixes more destination bits than a /16.
- **D:** The /24 does not compete with the /16 during same-prefix installation.

**Further reading**

- [Configure Route Selection for Routers](https://www.cisco.com/c/en/us/support/docs/ip/enhanced-interior-gateway-routing-protocol-eigrp/8651-21.html) — Build the Routing Table; Make Forwarding Decisions
- [Understand Administrative Distance](https://www.cisco.com/c/en/us/support/docs/ip/border-gateway-protocol-bgp/15986-admin-distance.html) — RIB Route Comparison; Route Installation; Default AD Values

---

## CCNA3-051 · IP Connectivity

Objectives: 3.1.d, 3.3.b · single · Applied

For the installed route chain below, which adjacent router receives packets to 10.211.4.8? Assume ordinary routing and successful neighbor resolution.

```text
S 10.211.0.0/16 via 192.0.2.200
S 192.0.2.200/32 via 198.51.100.6
C 198.51.100.4/30 is directly connected, GigabitEthernet0/2
L 198.51.100.5/32 is directly connected, GigabitEthernet0/2
```

- **A.** 10.211.4.8
- **B.** 198.51.100.5
- **C.** 192.0.2.200 directly on GigabitEthernet0/2
- **D.** 198.51.100.6

**Answer: D**

Resolve the route’s next hop until a connected adjacency is reached. The logical next-hop address in the first route need not be the frame’s final Ethernet neighbor.

**Option explanations**

- **A:** The destination is not on the directly connected transit link.
- **B:** That address belongs to the forwarding router itself.
- **C:** That address is reached recursively through another router, not as a local Ethernet neighbor.
- **D:** The recursive lookup for 192.0.2.200 reaches this directly attached next hop.

**Further reading**

- [Configure a Next Hop IP Address for Static Routes](https://www.cisco.com/c/en/us/support/docs/dial-access/floating-static-route/118263-technote-nexthop-00.html) — Background Information; Floating Static Route Example

---

## CCNA3-052 · IP Connectivity

Objectives: 3.4.a · single · Applied

Two routers are in the same Ethernet subnet with all OSPF parameters compatible except the displayed timers. Which change directly restores timer compatibility?

| Router | Hello | Dead |
| --- | --- | --- |
| R1 | 10 s | 40 s |
| R2 | 10 s | 120 s |

- **A.** Set R2’s router ID equal to R1’s.
- **B.** Set R1’s priority to 120.
- **C.** Change both OSPF process IDs to 40.
- **D.** Set R2’s dead interval to 40 seconds.

**Answer: D**

Neighbor compatibility checks include both Hello and Dead intervals. Matching only the Hello interval is insufficient.

**Option explanations**

- **A:** Unique router IDs are required; this does not correct timer mismatch.
- **B:** DR priority is not the neighbor dead interval.
- **C:** Local process numbers do not synchronize Hello parameters.
- **D:** R1 and R2 would then both advertise Hello 10 and Dead 40.

**Further reading**

- [Troubleshoot OSPF Neighbor Problems](https://www.cisco.com/c/en/us/support/docs/ip/open-shortest-path-first-ospf/13699-29.html) — No State Revealed; Neighbors Stuck in Exstart/Exchange State

---

## CCNA3-053 · IP Connectivity

Objectives: 3.4.a · single · Applied

An OSPF neighbor changes from Exchange to Loading. What is the router doing during Loading?

- **A.** Waiting for the first-ever Hello from this router.
- **B.** Electing a new DR for every advertised subnet.
- **C.** Requesting missing or newer link-state information identified during database exchange.
- **D.** Forwarding nothing until every router in the enterprise has identical routes.

**Answer: C**

Database descriptions summarize information; Loading obtains the required detailed LSAs. Full follows when synchronization requirements are satisfied.

**Option explanations**

- **A:** The routers have already progressed beyond initial Hello discovery.
- **B:** Loading is a neighbor synchronization state, not a network-wide election.
- **C:** Link-state requests fill gaps before the databases are fully synchronized.
- **D:** OSPF neighbor synchronization is not a requirement for enterprise-wide identical routing tables.

**Further reading**

- [Understand OSPF Neighbor States](https://www.cisco.com/c/en/us/support/docs/ip/open-shortest-path-first-ospf/13685-13.html) — OSPF Neighbor States

---

## CCNA3-054 · IP Connectivity

Objectives: 3.4.a, 3.4.d · single · Applied

A router cloned from a template has the same explicit OSPF router ID as an existing router in area 0. What change addresses the identity conflict?

- **A.** Set both interface priorities to zero.
- **B.** Give the clone the same physical interface IP as the original.
- **C.** Raise the clone’s administrative distance.
- **D.** Assign a unique router ID and apply it with a planned OSPF restart.

**Answer: D**

Cloned interface-independent identifiers require explicit review. Changing the active router ID affects adjacencies and should be applied deliberately.

**Option explanations**

- **A:** DR ineligibility does not remove duplicate router IDs.
- **B:** That adds an IP address conflict rather than fixing the OSPF identity.
- **C:** Distance changes local route preference, not its OSPF identifier.
- **D:** Each OSPF router requires a distinct identifier; restarting applies the changed identity.

**Further reading**

- [Configuring OSPF — IP Routing: OSPF Configuration Guide](https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/iproute_ospf/configuration/xe-16/iro-xe-16-book/iro-cfg.html) — Enabling OSPF; Configuring OSPF Interface Parameters
- [Troubleshoot OSPF Neighbor Problems](https://www.cisco.com/c/en/us/support/docs/ip/open-shortest-path-first-ospf/13699-29.html) — No State Revealed; Neighbors Stuck in Exstart/Exchange State

---

## CCNA3-055 · IP Connectivity

Objectives: 3.4.a, 3.4.c · multiple · Applied

R1’s broadcast-interface OSPF priority is changed to 0 before it joins a new segment. Which two capabilities remain possible when other eligible routers provide DR/BDR service? Select two.

- **A.** R1 can become BDR but never DR.
- **B.** R1 can exchange Hellos with neighbors.
- **C.** R1 can win the DR election using a high router ID.
- **D.** R1 can become fully adjacent to the DR.

**Answer: B, D**

Priority controls election eligibility, not ordinary participation. A priority-zero router can still learn and advertise routes through valid adjacencies.

**Option explanations**

- **A:** Priority zero excludes both elected roles.
- **B:** Zero priority does not disable OSPF on the interface.
- **C:** Priority zero removes it from DR/BDR eligibility regardless of router ID.
- **D:** DROTHER routers synchronize with the DR on a broadcast segment.

**Further reading**

- [RFC 2328: OSPF Version 2](https://www.rfc-editor.org/rfc/rfc2328.html) — 9.4 Electing the Designated Router; 10 The Neighbor Data Structure; 16 Calculation of the routing table

---

## CCNA3-056 · IP Connectivity

Objectives: 3.4.c · single · Applied

R1 is BDR and R2 is a healthy DR. R1’s interface priority is raised above R2’s without resetting either adjacency. What immediate role change should the engineer expect?

- **A.** R1 instantly becomes DR.
- **B.** R1 stops forwarding because its priority is out of order.
- **C.** R1 remains BDR while the existing DR stays healthy.
- **D.** Both become DR until their router IDs change.

**Answer: C**

Changing a priority prepares a future election rather than guaranteeing immediate leadership. Incumbent state is part of the election reasoning.

**Option explanations**

- **A:** OSPF DR election is nonpreemptive for an established healthy DR.
- **B:** Priority ordering is not a data-plane forwarding prerequisite.
- **C:** Changing relative priority does not preempt the incumbent DR.
- **D:** A priority increase does not intentionally create two DRs.

**Further reading**

- [RFC 2328: OSPF Version 2](https://www.rfc-editor.org/rfc/rfc2328.html) — 9.4 Electing the Designated Router; 10 The Neighbor Data Structure; 16 Calculation of the routing table

---

## CCNA3-057 · IP Connectivity

Objectives: 3.4.b · single · Foundation

A point-to-point OSPF link has two Full neighbors with interface priorities 1 and 255. Which interpretation is correct?

- **A.** Neither priority creates a DR/BDR role on this network type.
- **B.** The priority-255 router must be DR.
- **C.** The priority-1 router must stop advertising routes.
- **D.** The Full state is invalid unless priorities match.

**Answer: A**

Interpret election fields in the context of network type. Full adjacency is expected on a compatible point-to-point link.

**Option explanations**

- **A:** Point-to-point OSPF does not use the broadcast election process.
- **B:** That priority comparison matters only on network types that elect a DR.
- **C:** Its priority does not prevent participation on a point-to-point link.
- **D:** OSPF adjacency does not require equal interface priorities.

**Further reading**

- [RFC 2328: OSPF Version 2](https://www.rfc-editor.org/rfc/rfc2328.html) — 9.4 Electing the Designated Router; 10 The Neighbor Data Structure; 16 Calculation of the routing table

---

## CCNA3-058 · IP Connectivity

Objectives: 3.4.a · single · Applied

A router has area 0 enabled only on its transit interface. Its new LAN is up, but remote OSPF routers never learn that LAN. No redistribution is configured. What is the targeted correction?

- **A.** Enable the LAN interface in OSPF area 0, making it passive if it has only hosts.
- **B.** Change the LAN’s default gateway to an OSPF process number.
- **C.** Increase the transit interface DR priority.
- **D.** Configure the LAN subnet as the router ID.

**Answer: A**

An operational connected network is not automatically advertised merely because some other interface runs OSPF. Include the intended interface in the routing process.

**Option explanations**

- **A:** This includes the connected LAN in OSPF while optionally preventing host-facing adjacencies.
- **B:** Hosts need an IP next hop, not a local routing-process identifier.
- **C:** Election priority does not include an unenabled LAN in OSPF.
- **D:** An identifier is not a subnet-advertisement command.

**Further reading**

- [Configuring OSPF — IP Routing: OSPF Configuration Guide](https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/iproute_ospf/configuration/xe-16/iro-xe-16-book/iro-cfg.html) — Enabling OSPF; Configuring OSPF Interface Parameters
- [Default Passive Interfaces — Cisco IOS XE 17.x](https://www.cisco.com/c/en/us/td/docs/routers/ios/config/17-x/ip-routing/b-ip-routing/m_iri-default-passive-interface.html) — Information About Default Passive Interfaces

---

## CCNA3-059 · IP Connectivity

Objectives: 3.2.c · single · Applied

A routed link is upgraded from 100 Mb/s to 1 Gb/s. Both ends keep Cisco’s 100 Mb/s OSPF reference bandwidth and automatic cost, with no manual cost. Why might path selection remain unchanged?

- **A.** The router ID must equal the new bandwidth.
- **B.** OSPF always ignores bandwidth.
- **C.** OSPF compares Ethernet MAC addresses before cost.
- **D.** Both bandwidths produce the minimum interface cost of 1.

**Answer: D**

Cost resolution depends on the chosen reference bandwidth. A consistent larger reference can distinguish higher-speed links when no manual costs override it.

**Option explanations**

- **A:** Router ID is an identifier, not the link-cost setting.
- **B:** Automatic Cisco OSPF interface cost is based on reference bandwidth and interface bandwidth.
- **C:** MAC ordering does not select an intra-area shortest path.
- **D:** The old reference bandwidth cannot distinguish these faster links with integer cost.

**Further reading**

- [Configuring OSPF — IP Routing: OSPF Configuration Guide](https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/iproute_ospf/configuration/xe-16/iro-xe-16-book/iro-cfg.html) — Enabling OSPF; Configuring OSPF Interface Parameters

---

## CCNA3-060 · IP Connectivity

Objectives: 3.4.a · single · Foundation

Which command most directly verifies whether the local router has reached Full adjacency with an OSPFv2 peer?

- **A.** show startup-config
- **B.** show arp
- **C.** show ip ospf neighbor
- **D.** show ip interface brief

**Answer: C**

Choose an operational command that reports the specific state being tested. An up interface or correct saved configuration alone does not demonstrate Full adjacency.

**Option explanations**

- **A:** Saved configuration is not live evidence of adjacency convergence.
- **B:** ARP reports IPv4 Layer 2 neighbors, not OSPF adjacency state.
- **C:** The neighbor table reports each OSPF peer and its adjacency state.
- **D:** Interface state and addressing do not report OSPF database synchronization.

**Further reading**

- [Understand OSPF Neighbor States](https://www.cisco.com/c/en/us/support/docs/ip/open-shortest-path-first-ospf/13685-13.html) — OSPF Neighbor States

---

## CCNA3-061 · IP Connectivity

Objectives: 3.2.c · single · Applied

The only two OSPF intra-area paths to a LAN are described below, including the destination-LAN interface cost. Which path is selected?

| Path | Outgoing costs, in order |
| --- | --- |
| R1 → R2 → LAN | 20, 1 |
| R1 → R3 → R4 → LAN | 7, 7, 2 |

- **A.** The path through R2, because 20 is greater than 7
- **B.** The path through R3, cost 16
- **C.** Both paths, because both end at the same LAN
- **D.** The path through R2, because it has fewer routed links

**Answer: B**

Sum the outgoing costs along each complete path. The result is 21 through R2 versus 16 through R3 and R4.

**Option explanations**

- **A:** Lower accumulated cost is preferred.
- **B:** 7 + 7 + 2 is 16, lower than the other path’s 21.
- **C:** Equal destination does not mean equal total metric.
- **D:** OSPF cost can favor a path with more links.

**Further reading**

- [RFC 2328: OSPF Version 2](https://www.rfc-editor.org/rfc/rfc2328.html) — 9.4 Electing the Designated Router; 10 The Neighbor Data Structure; 16 Calculation of the routing table

---

## CCNA3-062 · IP Connectivity

Objectives: 3.5 · single · Applied

A switch learns the normal HSRP virtual MAC on the standby router’s port after a successful gateway failover. What does this change support?

- **A.** Frames addressed to the same virtual MAC reach the new active router.
- **B.** All hosts must learn a new subnet mask.
- **C.** The standby router has become the STP root by definition.
- **D.** All upstream routing tables are automatically identical.

**Answer: A**

Failover includes delivering traffic to the new owner of the virtual gateway. A stable virtual identity can move between switch ports.

**Option explanations**

- **A:** Layer 2 learning follows the moved virtual forwarding responsibility.
- **B:** MAC location changes do not imply IP renumbering.
- **C:** HSRP role and STP root election are separate processes.
- **D:** HSRP does not synchronize every route on the routers.

**Further reading**

- [Understand the Hot Standby Router Protocol Features and Functionality](https://www.cisco.com/c/en/us/support/docs/ip/hot-standby-router-protocol-hsrp/9234-hsrpguidetoc.html) — HSRP Background and Operations; HSRP Operation

---

## CCNA3-063 · IP Connectivity

Objectives: 3.5 · single · Applied

A design uses HSRP but disables preemption on both routers. The former preferred active router returns with higher priority after an outage; the current active remains healthy. What is expected?

- **A.** Both routers must withdraw all static routes.
- **B.** The recovered router always retakes active immediately.
- **C.** The current active can remain active.
- **D.** The virtual IP is permanently deleted.

**Answer: C**

Distinguish failure takeover from planned role reclamation. Preemption controls whether the returning higher-priority router displaces an existing active.

**Option explanations**

- **A:** HSRP recovery is not a command to delete routing configuration.
- **B:** That behavior depends on preemption rather than priority alone.
- **C:** A recovered higher-priority HSRP router does not reclaim the role without preemption.
- **D:** Recovery does not inherently remove the configured group address.

**Further reading**

- [Use HSRP Preempt and Track Commands](https://www.cisco.com/c/en/us/support/docs/ip/hot-standby-router-protocol-hsrp/13780-6.html) — Preempt and Track Commands

---

## CCNA3-064 · IP Connectivity

Objectives: 3.5 · multiple · Applied

A network team proposes FHRP to protect against a single default-gateway router failing. Which two design conditions are necessary for useful surviving service? Select two.

- **A.** Both routers use the same physical interface IP address.
- **B.** All hosts run the same interior routing protocol as the routers.
- **C.** Hosts use the redundant virtual gateway identity.
- **D.** The surviving router has a usable path toward required destinations.

**Answer: C, D**

Gateway identity redundancy and onward reachability are complementary requirements. Verify both during failover testing.

**Option explanations**

- **A:** Normal designs use unique physical addresses and a shared virtual identity.
- **B:** FHRP is designed to provide redundancy without making ordinary hosts routing peers.
- **C:** Hosts must send traffic to the identity the surviving router can assume.
- **D:** Owning a virtual IP cannot replace missing onward connectivity.

**Further reading**

- [RFC 9568: Virtual Router Redundancy Protocol (VRRP) Version 3 for IPv4 and IPv6](https://www.rfc-editor.org/rfc/rfc9568.html) — 1 Introduction; 2 Required Features; 6 Protocol State Machine
- [Understand the Hot Standby Router Protocol Features and Functionality](https://www.cisco.com/c/en/us/support/docs/ip/hot-standby-router-protocol-hsrp/9234-hsrpguidetoc.html) — HSRP Background and Operations; HSRP Operation

---

## CCNA3-065 · IP Connectivity

Objectives: 3.1.g, 3.3.a · single · Foundation

A router has a valid installed default via 192.0.2.2. The operator sees “Gateway of last resort is 192.0.2.2 to network 0.0.0.0.” What does this establish?

- **A.** Every Internet application is reachable through that neighbor.
- **B.** 192.0.2.2 is the router’s own configured interface address.
- **C.** The default overrides all installed host routes.
- **D.** A fallback next hop is selected for unmatched IPv4 destinations.

**Answer: D**

This is local route-selection evidence. It does not prove the neighbor can deliver packets all the way to an external service.

**Option explanations**

- **A:** A local default does not prove remote routing, DNS, transport, or application health.
- **B:** The message names the default next hop, not necessarily a local address.
- **C:** More specific routes still win ordinary destination lookups.
- **D:** The message identifies the selected default forwarding path.

**Further reading**

- [Configure Route Selection for Routers](https://www.cisco.com/c/en/us/support/docs/ip/enhanced-interior-gateway-routing-protocol-eigrp/8651-21.html) — Build the Routing Table; Make Forwarding Decisions

---

## CCNA3-066 · IP Services

Objectives: 4.1 · single · Applied

A static inside-source mapping binds 10.30.8.10 to 203.0.113.10. An outside client sends an allowed packet to 203.0.113.10. Routes and NAT interface roles are correct. Which translation occurs as this reply-direction traffic passes from outside to inside?

- **A.** The packet must first create a dynamic pool allocation.
- **B.** The outside client's source becomes 203.0.113.10.
- **C.** Source 203.0.113.10 becomes 10.30.8.10.
- **D.** Destination 203.0.113.10 becomes 10.30.8.10.

**Answer: D**

Inside source NAT describes the inside-originating mapping, but its reverse operation rewrites the destination of inbound traffic. Translation alone does not imply permission; the question separately states that the packet is allowed.

**Option explanations**

- **A:** The stated static mapping already defines the translation.
- **B:** That would translate the outside sender rather than deliver to the mapped inside server.
- **C:** 203.0.113.10 is the destination of this incoming packet, not its source.
- **D:** The reverse direction of the static mapping restores the inside local destination.

**Further reading**

- [IP Addressing Configuration Guide, Cisco IOS XE 17.x — Configuring NAT for IP Address Conservation](https://www.cisco.com/c/en/us/td/docs/routers/ios/config/17-x/ip-addressing/b-ip-addressing/m_iadnat-addr-consv-xe.html) — Inside source address translation; static and dynamic translations; monitoring NAT
- [RFC 3022 — Traditional IP Network Address Translator (Traditional NAT)](https://www.rfc-editor.org/rfc/rfc3022.html) — 2 Overview; 3 Translation phases

---

## CCNA3-067 · IP Services

Objectives: 4.2 · single · Foundation

R8 must remain an NTP client of 10.8.0.20. The network is reachable, but a stateless ACL on the server-facing path blocks requests to the server's well-known NTP port. Which destination service must be permitted for ordinary unicast NTP requests?

- **A.** TCP 123
- **B.** TCP 22
- **C.** UDP 123
- **D.** UDP 161

**Answer: C**

Permitting the relevant UDP exchange is necessary for synchronization; compatible return traffic must also pass. An ICMP echo response alone would not demonstrate that NTP traffic is allowed.

**Option explanations**

- **A:** The normal NTP client/server exchange is not carried over TCP.
- **B:** Port 22 is the SSH service, not time synchronization.
- **C:** NTP exchanges use UDP with server port 123.
- **D:** Port 161 is associated with SNMP requests.

**Further reading**

- [RFC 5905 — Network Time Protocol Version 4: Protocol and Algorithms Specification](https://www.rfc-editor.org/rfc/rfc5905.html) — 7 NTP protocol data structures; 9 Peer process; 11 System process

---

## CCNA3-068 · IP Services

Objectives: 4.3 · single · Foundation

A DHCPv4 client selected an offered address and broadcast a DHCPREQUEST. The server accepts that request. Which message confirms the lease and supplied configuration so the client can complete this allocation?

- **A.** DHCPOFFER
- **B.** DHCPDISCOVER
- **C.** DHCPNAK
- **D.** DHCPACK

**Answer: D**

The familiar initial allocation sequence is discovery, offer, request, acknowledgment. An offer alone is not the final positive acknowledgment of the client's selected request.

**Option explanations**

- **A:** An offer proposes configuration before the selected request is accepted.
- **B:** Discovery is initiated by the client to locate servers.
- **C:** A negative acknowledgment rejects the requested configuration.
- **D:** This acknowledges the accepted request and provides the committed configuration.

**Further reading**

- [RFC 2131 — Dynamic Host Configuration Protocol](https://www.rfc-editor.org/rfc/rfc2131.html) — 3.1 Address allocation; 4.3 Server behavior; 4.4 Client behavior

---

## CCNA3-069 · IP Services

Objectives: 4.4 · single · Applied

A monitoring account must retrieve device counters while protecting both message integrity and the confidentiality of their contents. Which SNMP security choice meets both conditions?

- **A.** SNMPv3 authNoPriv
- **B.** SNMPv3 noAuthNoPriv
- **C.** SNMPv2c with a long community string
- **D.** SNMPv3 authPriv

**Answer: D**

The security level matters in addition to the protocol version. Use authPriv with supported authentication and encryption algorithms when both integrity and confidentiality are required.

**Option explanations**

- **A:** It authenticates messages but does not encrypt their contents.
- **B:** It provides neither the requested authentication protection nor privacy.
- **C:** A longer community string does not add SNMPv3 message encryption.
- **D:** This level combines authentication/integrity protection with privacy encryption.

**Further reading**

- [RFC 3414 — User-based Security Model (USM) for version 3 of the Simple Network Management Protocol (SNMPv3)](https://www.rfc-editor.org/rfc/rfc3414.html) — 1.2 Goals and constraints; authentication and privacy
- [SNMP Configuration Guide, Cisco IOS XE 17 — Configuring SNMP Support](https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/snmp/configuration/xe-17-x/snmp-xe-17-book/nm-snmp-cfg-snmp-support.html) — Components of SNMP; operations; versions; traps and informs

---

## CCNA3-070 · IP Services

Objectives: 4.5 · single · Applied

A collector must retain two IOS messages: %OSPF-5-ADJCHG and %SYS-5-CONFIG_I. The operator wants separate views for routing events and system configuration events without changing the common severity threshold. Which message component distinguishes these categories?

- **A.** IP time-to-live
- **B.** Numeric severity
- **C.** Facility
- **D.** NTP stratum

**Answer: C**

IOS facilities identify the subsystem associated with a message; severity describes urgency. The two messages can share severity 5 while being categorized under different facilities.

**Option explanations**

- **A:** TTL is not the IOS subsystem category in the displayed log message.
- **B:** Both messages already have severity 5, so severity cannot separate them.
- **C:** OSPF and SYS identify the producing subsystems in the IOS message format.
- **D:** Stratum describes time-source hierarchy and is not a syslog event category.

**Further reading**

- [System Message Logging](https://www.cisco.com/c/en/us/td/docs/routers/access/wireless/software/guide/SysMsgLogging.html) — System log message format; logging destinations; severity levels; timestamps

---

## CCNA3-071 · IP Services

Objectives: 4.6 · multiple · Applied

The constructed output was collected on an IOS XE WAN interface expected to obtain its IPv4 address from an ISP DHCP server. Which two observations are supported? Select two.

```text
R-WAN# show ip interface brief
Interface          IP-Address       OK? Method Status Protocol
GigabitEthernet0/0  198.51.100.126   YES DHCP   up     up
```

- **A.** The output proves that the lease will survive indefinitely without renewal.
- **B.** The interface and line protocol are currently up.
- **C.** The interface is acting as a DHCP relay for all LAN clients.
- **D.** The interface currently has an IPv4 address learned using DHCP.
- **E.** The output proves that DNS resolution to public names works.

**Answer: B, D**

This verifies the local interface's DHCP-derived address and operational state. It does not verify relay service, DNS, or the rest of the Internet path.

**Option explanations**

- **A:** A current address does not remove DHCP lease timing.
- **B:** Both Status and Protocol report up.
- **C:** The DHCP method indicates local client addressing, not helper configuration.
- **D:** The Method column is DHCP and an address is present.
- **E:** Interface addressing does not test a resolver.

**Further reading**

- [IP Addressing: DHCP Configuration Guide, Cisco IOS XE 17 — Configuring the Cisco IOS XE DHCP Client](https://www.cisco.com/c/en/us/td/docs/routers/asr920/configuration/guide/ipaddr-dhcp/17-1-1/b-dhcp-xe-17-1-asr920/m_config-dhcp-client-xe.html) — Configuring the DHCP client; monitoring and maintaining DHCP client operation

---

## CCNA3-072 · IP Services

Objectives: 4.7 · single · Applied

A switch correctly marks voice packets DSCP EF. The next router deliberately maps all received DSCP values into one best-effort queue. During congestion, voice experiences the same delay as bulk transfers. What best explains the result?

- **A.** EF automatically reserves bandwidth across every router regardless of configuration.
- **B.** Marking requires corresponding per-hop classification and scheduling to provide differentiated treatment.
- **C.** DSCP marking changes the physical link speed for each marked packet.
- **D.** QoS can act only at the sending endpoint, never at an intermediate router.

**Answer: B**

A DSCP is an input to a node's forwarding treatment, not an unconditional performance guarantee. The stated downstream policy collapses the marked classes into the same treatment.

**Option explanations**

- **A:** A DSCP value does not create end-to-end reservations.
- **B:** The next hop ignores the distinction when mapping traffic into its queue.
- **C:** Marking labels a packet; it does not alter link capacity.
- **D:** Intermediate nodes implement the per-hop forwarding behaviors.

**Further reading**

- [RFC 2474 — Definition of the Differentiated Services Field (DS Field) in the IPv4 and IPv6 Headers](https://www.rfc-editor.org/rfc/rfc2474.html) — 3 Differentiated Services field; 4 Per-hop behaviors
- [RFC 2475 — An Architecture for Differentiated Services](https://www.rfc-editor.org/rfc/rfc2475.html) — 2.3 Traffic classification and conditioning; 2.4 Per-hop behaviors

---

## CCNA3-073 · IP Services

Objectives: 4.7 · multiple · Applied

During a brief egress burst, two classes wait for an interface that can transmit only one packet at a time. Which two functions directly determine how waiting packets are stored and which class is served next? Select two.

- **A.** Marking alone
- **B.** Queuing
- **C.** Classification alone
- **D.** Policing with immediate drop actions
- **E.** Scheduling

**Answer: B, E**

Queuing and scheduling handle contention for a constrained output resource. Classification and marking can inform those functions, but neither creates additional physical capacity.

**Option explanations**

- **A:** Writing a header label does not itself provide output queue storage or scheduling.
- **B:** Queues hold packets awaiting service.
- **C:** Classification identifies a traffic class but does not itself store waiting packets or choose service order.
- **D:** This enforces a profile through drops rather than providing the requested waiting storage and service selection.
- **E:** The scheduler chooses the next queue or packet to serve.

**Further reading**

- [Quality of Service Configuration Guide — Quality of service](https://www.cisco.com/c/en/us/td/docs/switches/lan/c9000/qos/quality-of-service-configuration-guide/m-quality-of-service.html) — Classification; marking; queuing and scheduling; policing and shaping

---

## CCNA3-074 · IP Services

Objectives: 4.8 · single · Applied

A router permits only SSH on its VTY lines. A client connects successfully, but an audit finds that the device is willing to negotiate an obsolete SSH protocol version in addition to version 2. Which global command explicitly restricts the IOS XE SSH server to version 2?

- **A.** ip ssh version 2
- **B.** ip ssh time-out 2
- **C.** service password-encryption
- **D.** transport input ssh

**Answer: A**

VTY transport selection and SSH version selection solve different configuration requirements. An SSH-only VTY still needs the explicit version setting where version negotiation is otherwise broader.

**Option explanations**

- **A:** This selects SSH protocol version 2 for the server.
- **B:** This changes authentication timeout, not the negotiated protocol version.
- **C:** That command does not select SSH protocol versions.
- **D:** This selects the allowed VTY protocol family, not its version.

**Further reading**

- [Configure SSH on Routers](https://www.cisco.com/c/en/us/support/docs/security-vpn/secure-shell-ssh/4145-ssh.html) — SSH server prerequisites; SSHv2; VTY restrictions; show commands

---

## CCNA3-075 · IP Services

Objectives: 4.9 · single · Applied

A firmware transfer uses base TFTP with 512-byte data blocks and no negotiated extensions. One DATA block is lost. Which behavior allows recovery despite UDP lacking transport retransmissions?

- **A.** UDP acknowledges the missing block and resends it.
- **B.** TFTP opens a TCP recovery connection for the lost block.
- **C.** The receiver treats the missing block as an end-of-file marker.
- **D.** TFTP uses block acknowledgments and timeout-based retransmission.

**Answer: D**

TFTP supplies its own simple reliability above UDP. A transfer can recover individual losses without UDP becoming a reliable transport.

**Option explanations**

- **A:** UDP provides no such acknowledgment or retransmission service.
- **B:** Base TFTP does not switch to TCP after a loss.
- **C:** A missing datagram is not the defined short final DATA block.
- **D:** Reliability for this transfer is implemented by TFTP itself.

**Further reading**

- [RFC 1350 — The TFTP Protocol (Revision 2)](https://www.rfc-editor.org/info/rfc1350/) — 2 Protocol overview; 3 Relation to other protocols; 4 Initial connection; 6 Normal termination

---

## CCNA3-076 · Security Fundamentals

Objectives: 5.1 · single · Applied

A management VLAN is reachable by an untrusted guest segment. No intrusion has been observed. Which statement is justified by this finding alone?

- **A.** A guest IP address is itself an exploit.
- **B.** The reachable management path is an exposure that can increase attack opportunities.
- **C.** The absence of alerts proves that no threat exists.
- **D.** An attacker has already executed code on every managed switch.

**Answer: B**

Exposure and demonstrated compromise are different claims. Restricting unnecessary reachability can mitigate opportunity while investigation determines whether any exploitation occurred.

**Option explanations**

- **A:** An address is not a technique that exploits a weakness.
- **B:** The path can enable threats to reach management services, even without observed exploitation.
- **C:** Detection absence does not establish absence of possible harmful activity.
- **D:** Reachability does not demonstrate a successful exploit or compromise.

**Further reading**

- [RFC 4949: Internet Security Glossary, Version 2](https://www.rfc-editor.org/rfc/rfc4949.html) — Section 2: threat, vulnerability, exploit, and countermeasure

---

## CCNA3-077 · Security Fundamentals

Objectives: 5.2 · single · Applied

A company has published a policy explaining how to report suspected phishing. Staff still forward suspected messages to colleagues to ask whether they are safe. Which improvement best addresses the observed behavior?

- **A.** Remove the reporting channel so users make their own decisions.
- **B.** Require another policy acknowledgement without practicing the reporting procedure.
- **C.** Shorten the policy title but provide no additional instruction.
- **D.** Practice the approved reporting workflow with realistic training examples.

**Answer: D**

A policy’s existence is weaker evidence than staff using it correctly. Scenario-based practice should teach recognition and the actual reporting channel.

**Option explanations**

- **A:** This eliminates the intended process rather than helping staff use it.
- **B:** Acknowledgement alone does not resolve the demonstrated behavior gap.
- **C:** A shorter title does not resolve the demonstrated workflow gap.
- **D:** Rehearsal connects the written policy to the action users must take.

**Further reading**

- [NIST SP 800-53 Rev. 5: Security and Privacy Controls for Information Systems and Organizations](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-53r5.pdf) — AT-2, AT-3, PE-2, and PE-3: awareness, training, and physical access

---

## CCNA3-078 · Security Fundamentals

Objectives: 5.3 · single · Foundation

An IOS router uses local username authentication. An engineer is checking the privilege actually assigned to the current logged-in session after an account change. Which command directly verifies that session’s current privilege level?

- **A.** show running-config | include username
- **B.** show privilege
- **C.** show users
- **D.** show line

**Answer: B**

show privilege reports the level of the current EXEC session. A configuration listing describes configured accounts, whereas this command checks the effective privilege of the session being used.

**Option explanations**

- **A:** This lists configured local accounts but does not directly identify the current session’s effective privilege.
- **B:** This displays the privilege level currently assigned to the CLI session.
- **C:** This identifies terminal sessions and usernames, but is not the direct display of the current privilege level.
- **D:** This reports terminal-line information rather than the current EXEC privilege level.

**Further reading**

- [Security and VPN Configuration Guide, Cisco IOS XE 17.x: Configuring Security with Passwords, Privileges, and Logins](https://www.cisco.com/c/en/us/td/docs/routers/ios/config/17-x/sec-vpn/b-security-vpn/m_sec-cfg-sec-4cli-0.html) — Protecting Access to User EXEC Mode; Password Encryption Levels; Password Change Verification

---

## CCNA3-079 · Security Fundamentals

Objectives: 5.4 · single · Applied

A team wants to reduce damage when one unrelated website leaks an engineer’s password. Which password-management practice most directly prevents the leaked value from also opening router administration accounts?

- **A.** Use the same complex password everywhere.
- **B.** Store the password hint in the public device banner.
- **C.** Use a unique password for each administrative account or service.
- **D.** Use the router’s management address as its password.

**Answer: C**

A password can satisfy complexity rules and still be compromised elsewhere. Unique administrative credentials limit the reuse path from a separate breach.

**Option explanations**

- **A:** Complexity does not stop reuse of an already disclosed value.
- **B:** Publishing a hint can assist guessing without preventing reuse.
- **C:** Unique credentials prevent reuse of that same leaked password elsewhere.
- **D:** A predictable identifier is not an appropriate secret.

**Further reading**

- [NIST SP 800-63B-4: Digital Identity Guidelines — Authentication and Authenticator Management](https://pages.nist.gov/800-63-4/sp800-63b.html) — Authentication factors; password verifiers; authenticator management

---

## CCNA3-080 · Security Fundamentals

Objectives: 5.5 · single · Applied

Two office VPN gateways have an established IPsec tunnel. A compromised workstation inside one protected LAN sends a malicious application request through it. What does successful IPsec authentication and integrity checking establish?

- **A.** The application request is harmless because it crossed IPsec.
- **B.** The protected packet passed the tunnel’s cryptographic checks; its application content may still be malicious.
- **C.** Every destination application must authorize the request.
- **D.** The original workstation operator necessarily supplied MFA for this packet.

**Answer: B**

IPsec protects selected traffic between its security endpoints. Endpoint compromise and application authorization remain relevant even when the tunnel operates correctly.

**Option explanations**

- **A:** Transport protection does not inspect the request’s business intent or safety.
- **B:** Authenticated protected transport does not make a compromised endpoint trustworthy.
- **C:** Application authorization remains a separate decision.
- **D:** Gateway-to-gateway IPsec does not prove an individual user’s authentication factors.

**Further reading**

- [RFC 4301: Security Architecture for the Internet Protocol](https://www.rfc-editor.org/rfc/rfc4301.html) — Sections 3, 4.1, 4.4.1: IPsec services, tunnel mode, and security policy

---

## CCNA3-081 · Security Fundamentals

Objectives: 5.6 · multiple · Applied

The displayed extended ACL is applied to traffic entering from an application subnet. Which two packets are permitted? Select two. Source ports are arbitrary ephemeral ports.

```text
ip access-list extended APP-IN
 permit tcp 10.9.4.0 0.0.0.255 host 192.0.2.40 eq 443
 permit udp 10.9.4.0 0.0.0.255 host 192.0.2.53 eq 53
```

- **A.** TCP from 10.9.4.7 to 192.0.2.40, destination port 80.
- **B.** UDP from 10.9.5.7 to 192.0.2.53, destination port 53.
- **C.** TCP from 10.9.4.7 to 192.0.2.40, destination port 443.
- **D.** UDP from 10.9.4.7 to 192.0.2.53, destination port 53.

**Answer: C, D**

Each permit combines source, destination, transport protocol, and destination port. A packet must match all fields of at least one permit before the implicit deny.

**Option explanations**

- **A:** No entry permits HTTP to that server.
- **B:** The source is outside 10.9.4.0/24.
- **C:** It matches the HTTPS permit for the source /24 and destination host.
- **D:** It matches the DNS permit.

**Further reading**

- [Configure IP Access Lists](https://www.cisco.com/c/en/us/support/docs/security/ios-firewall/23602-confaccesslists.html) — ACL Concepts; Masks; Process ACLs; Apply ACLs; Extended ACLs

---

## CCNA3-082 · Security Fundamentals

Objectives: 5.7 · single · Applied

On a Catalyst access port, port security uses shutdown mode. An unauthorized source causes a violation and the port becomes error-disabled. The unauthorized device is removed and the approved secure MAC remains configured. Which action can manually restore the port?

- **A.** Issue shutdown followed by no shutdown on that interface.
- **B.** Change the DNS server offered to the approved endpoint.
- **C.** Increase the switch MAC aging timer only.
- **D.** Send an ARP reply from the approved device without changing interface state.

**Answer: A**

Remove the violation’s cause before recovery. A manual interface shutdown/no shutdown cycle can restore service; otherwise the same cause may immediately trigger another shutdown.

**Option explanations**

- **A:** This manually re-enables an error-disabled interface after the cause is removed.
- **B:** DHCP option changes do not clear the interface’s error-disabled state.
- **C:** That does not clear the security shutdown condition.
- **D:** Ordinary traffic does not manually recover the disabled port.

**Further reading**

- [Catalyst 3750-X and 3560-X Configuration Guide: Configuring Port-Based Traffic Control](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst3750x_3560x/software/release/15-0_2_se/configuration/guide/3750x_cg/swtrafc.html) — Secure MAC Addresses; Security Violations; Port Security Aging

---

## CCNA3-083 · Security Fundamentals

Objectives: 5.8 · single · Applied

An audit requires evidence of who logged in, when the session began, and when it ended. Authentication and command restrictions already work, but these events are not retained. Which AAA function needs attention?

- **A.** Accounting
- **B.** Authentication
- **C.** Address translation
- **D.** Authorization

**Answer: A**

An access decision and an audit record serve different purposes. Configure and verify accounting delivery and retention for the required session events.

**Option explanations**

- **A:** Accounting produces the session and activity records required for the audit.
- **B:** Verifying credentials does not guarantee that session records are retained.
- **C:** NAT is not an AAA function and cannot supply account-level session evidence.
- **D:** Permission enforcement is already working and does not by itself retain the requested events.

**Further reading**

- [RFC 8907: The Terminal Access Controller Access-Control System Plus (TACACS+) Protocol](https://www.rfc-editor.org/rfc/rfc8907.html) — Sections 5, 6, and 7: authentication, authorization, and accounting

---

## CCNA3-084 · Security Fundamentals

Objectives: 5.9 · single · Applied

All intended clients support WPA3-Personal, and the organization wants to prevent WPA2-Personal association to the new WLAN. Which mode fits that requirement?

- **A.** WPA2/WPA3-Personal transition mode.
- **B.** WPA/TKIP with a longer passphrase.
- **C.** WPA3-Personal only with SAE.
- **D.** Open security with the SSID hidden.

**Answer: C**

Transition mode supports migration by admitting both types of client. A WPA3-only requirement instead calls for the corresponding SAE-only configuration and compatible clients.

**Option explanations**

- **A:** Transition mode intentionally retains WPA2-Personal client compatibility.
- **B:** Legacy WPA does not meet the WPA3 requirement.
- **C:** SAE-only WPA3-Personal excludes the legacy WPA2-PSK association path.
- **D:** SSID hiding does not supply authentication or WPA3 protection.

**Further reading**

- [Cisco Catalyst 9800 Configuration Guide, IOS XE 17.3.x: Wi-Fi Protected Access 3](https://www.cisco.com/c/en/us/td/docs/wireless/controller/9800/17-3/config-guide/b_wl_17_3_cg/m_wpa3.html) — WPA3-Personal; WPA3-Personal Transition Mode; Protected Management Frames

---

## CCNA3-085 · Security Fundamentals

Objectives: 5.10 · single · Applied

A constructed AireOS 8.10 WLAN is set to WPA2-AES with PSK key management. The PSK Format field is ASCII. Which candidate is valid for that field based on its length and character format? This is a format check, not a strength recommendation.

- **A.** A 7-character ASCII string.
- **B.** A 20-character ASCII passphrase.
- **C.** An empty string because WPA2 provides encryption independently.
- **D.** A 64-character ASCII passphrase entered as ASCII.

**Answer: B**

AireOS accepts an 8–63-character ASCII passphrase or a 64-digit hexadecimal PSK in the corresponding format. A valid format alone does not establish password strength.

**Option explanations**

- **A:** ASCII passphrases must have at least eight characters.
- **B:** Twenty ASCII characters fall within the supported 8–63 range.
- **C:** PSK authentication requires an actual valid shared credential.
- **D:** The ASCII passphrase limit is 63; a 64-digit hexadecimal key uses HEX format.

**Further reading**

- [Cisco Wireless Controller Configuration Guide, Release 8.10: WLAN Security](https://www.cisco.com/c/en/us/td/docs/wireless/controller/8-10/config-guide/b_cg810/wlan_security.html) — WPA1+WPA2; Configuring WPA1+WPA2 (GUI); Protected Management Frames

---

## CCNA3-086 · Security Fundamentals

Objectives: 5.6 · single · Challenge

A router connects a shared source LAN to two destination LANs. A standard ACL must block host 10.20.0.8 only from the finance LAN while preserving its access to the other LAN. Where should that source-only ACL be applied?

- **A.** Outbound on the other destination LAN interface.
- **B.** Inbound on the finance-facing interface.
- **C.** Outbound on the finance-facing interface.
- **D.** Inbound on the shared source interface.

**Answer: C**

A standard ACL cannot distinguish destinations in its entries. Applying it on the finance egress path provides the destination scope through placement.

**Option explanations**

- **A:** This would filter the destination that must remain reachable.
- **B:** This checks traffic entering from finance, not traffic being sent to it.
- **C:** The egress path limits the source-only denial to finance-bound traffic.
- **D:** This would deny that source before its finance and nonfinance traffic separate.

**Further reading**

- [Configure IP Access Lists](https://www.cisco.com/c/en/us/support/docs/security/ios-firewall/23602-confaccesslists.html) — ACL Concepts; Masks; Process ACLs; Apply ACLs; Extended ACLs

---

## CCNA3-087 · Security Fundamentals

Objectives: 5.6 · single · Applied

An engineer creates the displayed ACL. A test packet from 10.66.0.12 enters the router through Gi0/0 and still reaches the target. Gi0/0 has no IPv4 input ACL. What is the missing enforcement step?

```text
ip access-list extended TEST-IN
 deny ip host 10.66.0.12 any
 permit ip any any
```

- **A.** Apply TEST-IN with ip access-group TEST-IN in under Gi0/0.
- **B.** Delete the permit ip any any statement.
- **C.** Rename TEST-IN to access-list 1.
- **D.** Change deny ip to deny tcp without checking the test protocol.

**Answer: A**

An ACL definition is a policy object; it has no interface-filtering effect until applied. Verify both its entries and its attachment to the intended direction.

**Option explanations**

- **A:** Creating an ACL does not attach it to the packet path.
- **B:** That changes policy and still does not attach the ACL.
- **C:** The name is valid; naming does not apply the ACL.
- **D:** Narrowing the protocol does not resolve missing interface application.

**Further reading**

- [Configure IP Access Lists](https://www.cisco.com/c/en/us/support/docs/security/ios-firewall/23602-confaccesslists.html) — ACL Concepts; Masks; Process ACLs; Apply ACLs; Extended ACLs

---

## CCNA3-088 · Security Fundamentals

Objectives: 5.7 · matching · Applied

Match each observed Layer 2 attack with the feature that directly inspects or limits the stated behavior. Use each feature once.

1. An endpoint answers clients with unauthorized DHCP offers.
2. An endpoint advertises a forged gateway IP-to-MAC mapping in ARP.
3. A port must accept only its explicitly configured source MAC.

- **A.** DHCP snooping
- **B.** Dynamic ARP inspection
- **C.** Port security

**Answer: 1 → A; 2 → B; 3 → C**

Choose a control for the protocol or identity field being abused. These features complement one another rather than serving as interchangeable filters.

**Option explanations**

- **A:** It filters unauthorized DHCP server messages on untrusted ingress.
- **B:** It validates ARP address claims against authorized bindings or configured policy.
- **C:** It limits or pins source MAC addresses accepted on a switch port.

**Further reading**

- [Catalyst 3750-X and 3560-X Configuration Guide: Configuring DHCP Features and IP Source Guard](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst3750x_3560x/software/release/15-0_2_se/configuration/guide/3750x_cg/swdhcp82.html) — DHCP Snooping; DHCP Snooping Binding Database; Enabling DHCP Snooping
- [Catalyst 3750-X and 3560-X Configuration Guide: Configuring Dynamic ARP Inspection](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst3750x_3560x/software/release/15-0_2_se/configuration/guide/3750x_cg/swdynarp.html) — Understanding Dynamic ARP Inspection; Rate Limiting; ARP ACLs
- [Catalyst 3750-X and 3560-X Configuration Guide: Configuring Port-Based Traffic Control](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst3750x_3560x/software/release/15-0_2_se/configuration/guide/3750x_cg/swtrafc.html) — Secure MAC Addresses; Security Violations; Port Security Aging

---

## CCNA3-089 · Security Fundamentals

Objectives: 5.7 · multiple · Applied

A switch’s DHCP snooping binding table contains an approved client’s IP, MAC, VLAN, lease, and interface. Which two uses of this information are valid? Select two.

- **A.** An operator can compare the learned interface with the client’s expected attachment.
- **B.** DAI can use the IP-to-MAC binding to validate ARP claims.
- **C.** The table proves which human is currently using the endpoint.
- **D.** The table automatically encrypts all frames from the client.

**Answer: A, B**

The binding table ties a learned DHCP allocation to link-layer and attachment information. It supports verification and dependent protections but is not a user identity or encryption mechanism.

**Option explanations**

- **A:** The interface field is useful verification evidence.
- **B:** That binding provides an authorized mapping for ARP inspection.
- **C:** A network binding is not individual user authentication.
- **D:** Binding records do not provide encryption.

**Further reading**

- [Catalyst 3750-X and 3560-X Configuration Guide: Configuring DHCP Features and IP Source Guard](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst3750x_3560x/software/release/15-0_2_se/configuration/guide/3750x_cg/swdhcp82.html) — DHCP Snooping; DHCP Snooping Binding Database; Enabling DHCP Snooping
- [Catalyst 3750-X and 3560-X Configuration Guide: Configuring Dynamic ARP Inspection](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst3750x_3560x/software/release/15-0_2_se/configuration/guide/3750x_cg/swdynarp.html) — Understanding Dynamic ARP Inspection; Rate Limiting; ARP ACLs

---

## CCNA3-090 · Security Fundamentals

Objectives: 5.3 · single · Applied

A router configuration includes service password-encryption. The running configuration now displays a type 7 console password. Which conclusion is correct?

- **A.** The console automatically requires a username.
- **B.** All Telnet traffic is now encrypted.
- **C.** The console password is obscured in the configuration but type 7 is reversible.
- **D.** The router has enabled MFA for privileged access.

**Answer: C**

Type 7 protects against casual plaintext viewing, not determined recovery of a captured configuration. Protect configuration access and use appropriate secrets and encrypted management transport.

**Option explanations**

- **A:** The line’s login selection, not password-encryption, determines that behavior.
- **B:** Password storage obfuscation does not change Telnet transport.
- **C:** This feature is not strong protection against someone who can obtain the configuration.
- **D:** No second factor is introduced by this command.

**Further reading**

- [Understand Cisco IOS Password Encryption](https://www.cisco.com/c/en/us/support/docs/security-vpn/remote-authentication-dial-user-service-radius/107614-64.html) — Cisco IOS password encryption and reversible type 7 limitations

---

## CCNA3-091 · Automation and Programmability

Objectives: 6.1 · single · Applied

A nightly automation job compares the approved DNS-server setting with each switch’s running configuration. It reports three switches with an unexpected setting but makes no changes. What has the job detected?

- **A.** Successful convergence to the approved configuration
- **B.** An unavoidable limitation of JSON parsing
- **C.** Configuration drift from the approved state
- **D.** Proof that all three switches were compromised

**Answer: C**

Automated comparison can expose configuration drift consistently across a fleet. The finding establishes a discrepancy; determining whether it came from maintenance, an error or compromise requires further evidence.

**Option explanations**

- **A:** The three reported configurations differ from the baseline.
- **B:** No parsing failure is described.
- **C:** The comparison identifies differences between intended and observed settings.
- **D:** A configuration difference alone does not establish its cause.

**Further reading**

- [What Is Network Automation?](https://www.cisco.com/site/us/en/learn/topics/networking/what-is-network-automation.html) — Network automation; profiles and policies; automated lifecycle management

---

## CCNA3-092 · Automation and Programmability

Objectives: 6.2, 6.3.a · single · Challenge

In a proposed SDN deployment, switches retain installed forwarding entries indefinitely during a controller outage. No links or endpoints change, and all traffic in question matches those entries. Which outcome follows from these assumptions?

- **A.** Matching traffic can continue while new control decisions are unavailable
- **B.** Every matching packet must be dropped immediately
- **C.** The controller must return to retransmit each Ethernet frame
- **D.** All future network changes will also work without control services

**Answer: A**

Separating control and data functions can let existing forwarding continue without the controller for this bounded case. It does not establish how new flows, topology changes or other implementations behave.

**Option explanations**

- **A:** The retained data-plane entries suffice for the stated unchanged traffic.
- **B:** The scenario explicitly retains usable forwarding entries.
- **C:** The controller does not forward every frame in this design.
- **D:** The assumptions cover existing entries and unchanged conditions only.

**Further reading**

- [RFC 7426: Software-Defined Networking (SDN): Layers and Architecture Terminology](https://www.rfc-editor.org/rfc/rfc7426.html) — 3.1 Overview; 3.2 Network Devices; 3.3 Control Plane; 3.5.3 Locality

---

## CCNA3-093 · Automation and Programmability

Objectives: 6.3.b · single · Applied

A controller receives interface counters from a switch through its managed-device API. A capacity-planning application then reads those counters from the controller’s application API. Which classification is correct?

- **A.** Both exchanges are northbound because the data moves toward an application
- **B.** Both exchanges are data-plane packet forwarding
- **C.** The switch-controller exchange is northbound; the application-controller exchange is southbound
- **D.** The switch-controller exchange is southbound; the application-controller exchange is northbound

**Answer: D**

API direction labels identify the controller’s relationships. They do not change when a managed device sends counters back to the controller.

**Option explanations**

- **A:** The architectural boundaries remain different even when both exchanges carry telemetry.
- **B:** Management telemetry and application queries are not ordinary user forwarding.
- **C:** This reverses the controller’s device and application boundaries.
- **D:** Southbound connects managed devices; northbound exposes controller services to applications.

**Further reading**

- [Software-Defined Networking (SDN) Definition](https://www.cisco.com/c/en/us/solutions/software-defined-networking/overview.html) — SDN elements; Features and benefits
- [RFC 7426: Software-Defined Networking (SDN): Layers and Architecture Terminology](https://www.rfc-editor.org/rfc/rfc7426.html) — 3.1 Overview; 3.2 Network Devices; 3.3 Control Plane; 3.5.3 Locality

---

## CCNA3-094 · Automation and Programmability

Objectives: 6.4 · single · Applied

A generative AI assistant drafts an incident summary from supplied switch logs. The draft names an interface that is absent from those logs. What should the operator do before using the summary to direct a change?

- **A.** Treat the generated interface name as newly discovered telemetry
- **B.** Verify the claim against device evidence and correct the draft
- **C.** Configure the named interface to make the summary accurate
- **D.** Assume longer generated summaries are more accurate

**Answer: B**

Generative AI can assist with drafting, but generated content is not itself a measurement. The unsupported interface reference must be checked before it is used in an operational decision.

**Option explanations**

- **A:** Generated text is not evidence that the interface was observed.
- **B:** Operational decisions need support from actual device state and records.
- **C:** Changing the network to fit unsupported text reverses the purpose of diagnosis.
- **D:** Length does not demonstrate factual correctness.

**Further reading**

- [How To Get Started Using LLMs in IT and Network Engineering](https://blogs.cisco.com/developer/how-to-get-started-using-llms-in-it-and-network-engineering) — Introducing the LLM; Applying LLMs to IT and Network Engineering Use Cases
- [What is AIOps?](https://developer.cisco.com/articles/what-is-aiops/) — The core components of AIOps; Is AIOps all you need?

---

## CCNA3-095 · Automation and Programmability

Objectives: 6.5 · single · Challenge

A controller API documents POST /jobs as starting a new job on every accepted request. A client times out after sending a POST and cannot tell whether it succeeded. Which next step best avoids accidentally starting a duplicate job?

- **A.** Resend POST repeatedly because all HTTP methods are idempotent
- **B.** Replace POST with GET and assume the new job will be created
- **C.** Check the documented job status or deduplication mechanism before retrying
- **D.** Change the body to XML so duplicate execution becomes impossible

**Answer: C**

A timeout does not prove that the server failed to process the request. This POST starts a job each time, so the client must reconcile the uncertain outcome using the API’s documented facilities.

**Option explanations**

- **A:** POST does not generally guarantee an unchanged effect when repeated.
- **B:** The documented GET behavior is not job creation.
- **C:** The original request may have succeeded even though its response was lost.
- **D:** Data encoding does not add duplicate-request protection.

**Further reading**

- [RFC 9110: HTTP Semantics](https://www.rfc-editor.org/rfc/rfc9110.html) — 9 Methods; 15 Status Codes

---

## CCNA3-096 · Automation and Programmability

Objectives: 6.5 · single · Applied

The API response is shown after a client sends a previously valid access token. Which action addresses the reported problem?

```text
HTTP/1.1 401 Unauthorized
WWW-Authenticate: Bearer error="invalid_token", error_description="The access token expired"
```

- **A.** Obtain a valid token through the authorized authentication flow
- **B.** Remove HTTPS because authentication failures are caused by encryption
- **C.** Send a DELETE request to reset the target device
- **D.** Encode the same expired token as a JSON number

**Answer: A**

The 401 response and invalid_token indication identify a credential problem. The client needs a valid credential, rather than a different resource method or data format.

**Option explanations**

- **A:** The response identifies an invalid or expired bearer credential.
- **B:** TLS does not make an expired token valid.
- **C:** A destructive resource operation does not renew the credential.
- **D:** Changing representation does not restore token validity.

**Further reading**

- [RFC 6750: The OAuth 2.0 Authorization Framework: Bearer Token Usage](https://www.rfc-editor.org/rfc/rfc6750.html) — 2 Authenticated Requests; 3 The WWW-Authenticate Response Header Field; 5 Security Considerations

---

## CCNA3-097 · Automation and Programmability

Objectives: 6.6 · multiple · Applied

A supported Ansible task ensures that a logging server is configured. The first run changes the switch; the second run reports no change, and the required server is still present. Which two interpretations are correct? Select two.

- **A.** The second run necessarily failed to reach the switch
- **B.** The first run should have created a duplicate server on every later run
- **C.** The task has demonstrated idempotent behavior for this setting
- **D.** Every Ansible playbook is therefore guaranteed to be idempotent
- **E.** No further configuration change was needed on the second run

**Answer: C, E**

The observed task converges to the desired setting and leaves it unchanged on repetition. That behavior is specific evidence for this task, not a guarantee about every possible playbook.

**Option explanations**

- **A:** A successful no-change result can mean that the desired state already exists.
- **B:** A state-aware task avoids unnecessary repeated changes.
- **C:** Repeating it leaves the same desired configuration state.
- **D:** Other modules or tasks may perform non-idempotent actions.
- **E:** The desired server was already present and remained so.

**Further reading**

- [Ansible playbooks](https://docs.ansible.com/projects/ansible/latest/playbook_guide/playbooks_intro.html) — Playbook syntax; Playbook execution; Desired state and idempotency

---

## CCNA3-098 · Automation and Programmability

Objectives: 6.6 · single · Applied

An engineer changes a cloud subnet manually after Terraform created it. A later Terraform plan, using a provider that can read the changed attribute, proposes restoring the value declared in configuration. What explains the proposal?

- **A.** Terraform converts manual edits into routing updates
- **B.** The current resource differs from the declared desired state
- **C.** Every plan destroys every resource before reading it
- **D.** Terraform cannot observe any resource that already exists

**Answer: B**

An out-of-band change can create drift between configuration and the actual resource. After refreshing observed information, Terraform can propose changes to reconcile that difference.

**Option explanations**

- **A:** A plan concerns resource state, not dynamic route advertisements.
- **B:** The detected change is drift that the proposed operation would reconcile.
- **C:** Planning does not require universal destruction.
- **D:** Providers can read existing managed resources during planning.

**Further reading**

- [Manage resource drift](https://developer.hashicorp.com/terraform/tutorials/state/resource-drift) — Detect drift; reconcile configuration and changed resources
- [State](https://developer.hashicorp.com/terraform/language/state) — State; mapping configuration to real resources

---

## CCNA3-099 · Automation and Programmability

Objectives: 6.7 · multiple · Foundation

A payload contains both "portCount":48 and "assetTag":"0048". Which two statements preserve the intended distinction? Select two.

```text
{"portCount":48,"assetTag":"0048"}
```

- **A.** portCount is a JSON number
- **B.** assetTag is a JSON string
- **C.** Both values must be numbers because they contain only digits
- **D.** Removing the quotes from 0048 always produces valid JSON
- **E.** The member names must be unquoted for the document to be valid

**Answer: A, B**

JSON distinguishes numeric values from textual identifiers. Keeping assetTag as a string preserves its leading zeros without using an invalid numeric representation.

**Option explanations**

- **A:** The value 48 is unquoted numeric data.
- **B:** Quotation marks preserve the identifier’s textual form, including leading zeros.
- **C:** Quoted digits remain a string.
- **D:** JSON numbers do not allow this leading-zero form.
- **E:** JSON object member names are strings and require quotes.

**Further reading**

- [RFC 8259: The JavaScript Object Notation (JSON) Data Interchange Format](https://www.rfc-editor.org/rfc/rfc8259.html) — 2 JSON Grammar; 3 Values; 4 Objects; 5 Arrays; 6 Numbers; 7 Strings

---

## CCNA3-100 · Automation and Programmability

Objectives: 6.7 · single · Applied

An API returns the same object twice with only its member order changed, as shown. Member names are unique. What should a client conclude about the represented device information?

```text
{"hostname":"dist-8","site":"west"}

{"site":"west","hostname":"dist-8"}
```

- **A.** The first object must refer to the hostname and the second to the site
- **B.** The second object is invalid because hostname must appear first
- **C.** The site changed because the member moved earlier
- **D.** The two objects convey the same member values

**Answer: D**

Clients identify object values by their member names, not by assuming a fixed printed order. Both objects associate the same values with hostname and site.

**Option explanations**

- **A:** Changing object member order does not change name/value associations.
- **B:** JSON does not prescribe this member ordering.
- **C:** Its associated string remains west.
- **D:** Object member order is not a positional data model for these unique names.

**Further reading**

- [RFC 8259: The JavaScript Object Notation (JSON) Data Interchange Format](https://www.rfc-editor.org/rfc/rfc8259.html) — 2 JSON Grammar; 3 Values; 4 Objects; 5 Arrays; 6 Numbers; 7 Strings

---
