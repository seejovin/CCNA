# CCNA Practice — Set 07

100 original questions aligned to CCNA 200-301 v1.1. No interactive labs.

Answers and explanations follow each question. For an unrevealed attempt, use the Streamlit app.

Content review date: 2026-09-14.

## CCNA7-001 · Network Fundamentals

Objectives: 1.1.h · single · Applied

A switch has a configured usable PoE budget of 240 W and 220 W is already reserved. A replacement AP requires a 30 W reservation; its old AP reserved 10 W. Per-port limits permit either. What happens if the old AP is removed before installing the replacement?

| Power quantity | Value |
| --- | --- |
| Usable budget | 240 W |
| Existing reservations | 220 W |
| Old AP reservation | 10 W |
| Replacement request | 30 W |

- **A.** The replacement still exceeds budget by 30 W
- **B.** The new reservation fits exactly at 240 W total
- **C.** The budget becomes 270 W because reservations compound forever
- **D.** The switch supplies only 20 W regardless of the request

**Answer: B**

Account for the removed device as well as the new allocation. The net increase is 20 W, equal to the original spare budget.

**Option explanations**

- **A:** Removing the old reservation frees another 10 W.
- **B:** 220 − 10 + 30 equals 240 W.
- **C:** A released reservation does not remain charged indefinitely in this scenario.
- **D:** The stated new request fits after releasing the old 10 W.

**Further reading**

- [Interface and Hardware Components Configuration Guide, Cisco IOS XE 17.14.x (Catalyst 9200 Switches): Configuring Power over Ethernet](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst9200/software/release/17-14/configuration_guide/int_hw/b_1714_int_and_hw_9200_cg/configuring_poe.html) — Powered-Device Detection and Initial Power Allocation

---

## CCNA7-002 · Network Fundamentals

Objectives: 1.2.d · single · Applied

A branch can reach its local printer but loses communication with servers in headquarters after its carrier circuit fails. Which architectural component is directly implicated by that event?

- **A.** The local printer’s USB bus
- **B.** The headquarters server’s guest kernel
- **C.** The branch’s SSID spelling
- **D.** The WAN connection between sites

**Answer: D**

Local LAN success can coexist with WAN failure. The symptom scope follows the connectivity dependency that failed.

**Option explanations**

- **A:** The reported failure is the intersite circuit.
- **B:** No evidence of a server OS failure is provided.
- **C:** The carrier failure is independent of the WLAN name.
- **D:** The failed carrier path supplies intersite connectivity.

**Further reading**

- [What is a WAN (wide-area network)?](https://www.cisco.com/site/us/en/learn/topics/networking/what-is-a-wan-wide-area-network.html) — What is a WAN (wide-area network)?; What is a WAN router?

---

## CCNA7-003 · Network Fundamentals

Objectives: 1.3.a · multiple · Applied

A data-center fiber patch must be selected for new optics. Which TWO records are useful evidence of physical suitability? Select two.

- **A.** The installed fiber category and certified path length/loss
- **B.** The users’ application passwords
- **C.** The transceiver specifications at both ends
- **D.** The DHCP scope’s lease duration
- **E.** The spelling of switch hostnames

**Answer: A, C**

Check both the optical endpoints and the path joining them. Administrative or higher-layer configuration cannot establish a valid physical channel.

**Option explanations**

- **A:** These determine whether the optical channel fits the module specification.
- **B:** Credentials do not establish optical performance.
- **C:** Both endpoints must support compatible optical signaling.
- **D:** Lease timing does not change the optical path.
- **E:** Names are not optical compatibility parameters.

**Further reading**

- [Cisco 10GBASE SFP+ Modules Data Sheet](https://www.cisco.com/c/en/us/products/collateral/interfaces-modules/transceiver-modules/data_sheet_c78-455693.html) — Cisco SFP-10G-SR module; Cisco SFP-10G-LR module; Cisco SFP-10G-T-X module

---

## CCNA7-004 · Network Fundamentals

Objectives: 1.4 · single · Applied

A link remains down after one Fast Ethernet end is manually fixed at 100 Mb/s and the other at 10 Mb/s. Duplex settings agree and the cable is known good. Which mismatch must be corrected?

| Interface | Configured speed | Configured duplex |
| --- | --- | --- |
| A | 100 Mb/s | full |
| B | 10 Mb/s | full |

- **A.** Speed
- **B.** SSID
- **C.** IP subnet
- **D.** TCP window

**Answer: A**

Both sides must support a compatible operational rate. A valid cable cannot make incompatible forced speeds interoperate.

**Option explanations**

- **A:** The two ends are forced to different data rates.
- **B:** This is an Ethernet interface setting, not a WLAN name.
- **C:** A subnet mismatch does not cause the explicitly different physical rates.
- **D:** Transport windows do not negotiate Ethernet signaling speed.

**Further reading**

- [Configure and Verify Ethernet 10/100/1000Mb Half/Full Duplex Auto-Negotiation](https://www.cisco.com/c/en/us/support/docs/lan-switching/ethernet/10561-3.html) — Background Information; Auto-Negotiation on Catalyst Switches that Run Cisco IOS Software

---

## CCNA7-005 · Network Fundamentals

Objectives: 1.5 · single · Applied

A UDP-based voice application prefers discarding late audio over waiting for lost audio to be retransmitted. Why can UDP suit this design?

- **A.** UDP guarantees that every packet arrives before its deadline
- **B.** UDP eliminates all application sequencing needs
- **C.** UDP does not impose TCP’s reliable ordered byte-stream recovery
- **D.** UDP encrypts every voice sample automatically

**Answer: C**

The application chooses its timing and recovery policy above UDP. Low protocol overhead does not guarantee latency or successful delivery.

**Option explanations**

- **A:** UDP provides no deadline guarantee.
- **B:** An application may still need timestamps or sequence numbers.
- **C:** The application can choose its own loss and lateness behavior.
- **D:** Encryption is separate from UDP.

**Further reading**

- [RFC 768: User Datagram Protocol](https://www.rfc-editor.org/rfc/rfc768) — Introduction; Fields
- [RFC 9293: Transmission Control Protocol (TCP)](https://www.rfc-editor.org/rfc/rfc9293.html#section-2.2) — 2.2. Key TCP Concepts

---

## CCNA7-006 · Network Fundamentals

Objectives: 1.6 · single · Applied

A /26 LAN currently has 55 endpoints and one router address. Seven more endpoints must be added without changing existing addresses. Does the present subnet have enough ordinary host addresses?

- **A.** Yes, because /26 provides 64 usable addresses
- **B.** No, because the new total is 63 and /26 provides 62 usable addresses
- **C.** No, because /26 supports only 30 hosts
- **D.** Yes, because the router does not consume an IP address

**Answer: B**

Include infrastructure addresses in the requirement. The proposed 63 interfaces exceed the ordinary /26 host capacity.

**Option explanations**

- **A:** 64 is the total; only 62 are ordinarily usable.
- **B:** 55 + 1 + 7 exceeds capacity by one.
- **C:** That is the ordinary /27 host capacity.
- **D:** Its interface occupies one usable address in this LAN.

**Further reading**

- [Configure IP Addresses and Unique Subnets for New Users](https://www.cisco.com/c/en/us/support/docs/ip/routing-information-protocol-rip/13788-3.html) — Network Masks; Understand Subnetting; VLSM Example

---

## CCNA7-007 · Network Fundamentals

Objectives: 1.7 · multiple · Foundation

An address audit must identify prefixes that are not RFC 1918 private space. Which TWO entries should be flagged for that reason? Select two.

- **A.** 192.168.200.0/24
- **B.** 172.16.4.0/23
- **C.** 10.250.0.0/16
- **D.** 172.15.8.0/24
- **E.** 192.167.8.0/24

**Answer: D, E**

The familiar leading octets do not reserve every similar-looking prefix. Match the actual RFC 1918 boundaries.

**Option explanations**

- **A:** This is inside private 192.168.0.0/16.
- **B:** This is inside private 172.16.0.0/12.
- **C:** This is inside private 10.0.0.0/8.
- **D:** Its second octet precedes the private 16–31 range.
- **E:** It is outside private 192.168.0.0/16.

**Further reading**

- [RFC 1918: Address Allocation for Private Internets](https://www.rfc-editor.org/rfc/rfc1918#section-3) — 3. Private Address Space

---

## CCNA7-008 · Network Fundamentals

Objectives: 1.8 · single · Applied

A site owns 2001:db8:8100::/48 and uses /64 LANs. Which part can be varied to identify individual LANs while remaining inside this allocation?

- **A.** The fourth hextet
- **B.** Only the first hextet
- **C.** Only the final eight bits
- **D.** The first three hextets together

**Answer: A**

The subnet field here is 16 bits wide. Interface identifiers occupy the remaining low-order 64 bits.

**Option explanations**

- **A:** It supplies the 16 bits between the /48 site prefix and /64 LAN boundary.
- **B:** Changing it can leave the allocated site prefix.
- **C:** Those bits belong to the interface portion of a /64.
- **D:** Those 48 bits are fixed by the allocation.

**Further reading**

- [RFC 4291: IP Version 6 Addressing Architecture](https://www.rfc-editor.org/rfc/rfc4291#section-2.3) — 2.3. Text Representation of Address Prefixes; 2.4. Address Type Identification; 2.5.6. Link-Local IPv6 Unicast Addresses; 2.7. Multicast Addresses

---

## CCNA7-009 · Network Fundamentals

Objectives: 1.9.a · single · Applied

A network operator wants to ping a neighbor’s fe80::1 from a machine connected to two separate IPv6 links. Why may the outgoing interface need to be specified?

- **A.** Link-local addresses have no destination bits
- **B.** IPv6 requires a TCP handshake before ping
- **C.** fe80::1 is always a globally unique router ID
- **D.** The interface identifies which link-local zone is intended

**Answer: D**

Scope includes the link on which the address is used. A zone or interface disambiguates identical link-local values on different links.

**Option explanations**

- **A:** They are complete IPv6 addresses.
- **B:** ICMPv6 echo does not use a TCP connection.
- **C:** The numeric link-local address can be reused on different links.
- **D:** The same link-local value may be meaningful on both attached links.

**Further reading**

- [RFC 4291: IP Version 6 Addressing Architecture](https://www.rfc-editor.org/rfc/rfc4291#section-2.3) — 2.3. Text Representation of Address Prefixes; 2.4. Address Type Identification; 2.5.6. Link-Local IPv6 Unicast Addresses; 2.7. Multicast Addresses
- [RFC 4007: IPv6 Scoped Address Architecture](https://www.rfc-editor.org/rfc/rfc4007.html) — 6. Zone Indices; 11. Textual Representation

---

## CCNA7-010 · Network Fundamentals

Objectives: 1.10 · single · Applied

A Mac’s TCP/IP panel shows address 172.19.5.44, mask 255.255.255.0, and router 172.19.5.1. Which statement can be concluded from those values alone?

| Parameter | Value |
| --- | --- |
| IP address | 172.19.5.44 |
| Subnet mask | 255.255.255.0 |
| Router | 172.19.5.1 |

- **A.** The configured DNS resolver is responding
- **B.** The Internet service is functioning
- **C.** The configured router is in the same /24 as the client
- **D.** The router has authenticated the user

**Answer: C**

Configuration inspection can establish addressing consistency. Reachability and service behavior require additional observations.

**Option explanations**

- **A:** No DNS server or response evidence is shown.
- **B:** Configuration is not proof of working service.
- **C:** Both share prefix 172.19.5.0/24.
- **D:** Address fields do not show authentication state.

**Further reading**

- [Change TCP/IP settings on Mac](https://support.apple.com/en-hk/guide/mac-help/mh14129/mac) — IP address, subnet mask, and router settings
- [Configure IP Addresses and Unique Subnets for New Users](https://www.cisco.com/c/en/us/support/docs/ip/routing-information-protocol-rip/13788-3.html) — Network Masks; Understand Subnetting; VLSM Example

---

## CCNA7-011 · Network Fundamentals

Objectives: 1.11.c · single · Applied

A wireless link performs well in an empty room but degrades when movable metal shelving blocks the path. The configuration is unchanged. Which mechanism should be investigated?

- **A.** IPv4 subnetting automatically changed because of the shelving
- **B.** RF attenuation and reflection altered the propagation environment
- **C.** The SSID has become an optical wavelength
- **D.** TCP stopped using port numbers

**Answer: B**

The environment is part of the RF link. Physical changes can alter coverage even when AP configuration remains constant.

**Option explanations**

- **A:** Physical obstacles do not rewrite configured masks.
- **B:** Metal objects can obstruct or redirect radio propagation.
- **C:** SSID and wavelength are unrelated quantities.
- **D:** Transport field definitions do not change with room layout.

**Further reading**

- [Meraki Wireless for Enterprise Best Practices — RF Design](https://documentation.meraki.com/Platform_Management/Dashboard_Administration/Design_and_Configure/Architectures_and_Best_Practices/Meraki_Wireless_for_Enterprise_Best_Practices/Meraki_Wireless_for_Enterprise_Best_Practices_-_RF_Design) — RF design; signal-to-noise ratio; transmit power

---

## CCNA7-012 · Network Fundamentals

Objectives: 1.12 · single · Applied

A VM’s virtual NIC connects to a virtual switch inside its hypervisor. Another VM on the same virtual switch exchanges frames with it. What does this demonstrate?

- **A.** Layer 2 switching can be implemented in software
- **B.** Each VM requires a separate physical switch chassis
- **C.** A virtual NIC cannot use a MAC address
- **D.** Virtual switching automatically eliminates VLAN requirements

**Answer: A**

Virtualization changes the implementation location of the switching function. Ethernet forwarding concepts still apply to virtual interfaces.

**Option explanations**

- **A:** Virtual switches can forward frames among virtual interfaces.
- **B:** Virtual attachment can exist inside the host.
- **C:** Ethernet virtual NICs still use MAC addressing.
- **D:** Segmentation requirements can still apply to virtual networks.

**Further reading**

- [Network XML format](https://libvirt.org/formatnetwork.html) — Connectivity; isolated network; bridge

---

## CCNA7-013 · Network Fundamentals

Objectives: 1.13.b · single · Foundation

A host on VLAN 12 sends to another host in that same VLAN. The destination MAC is known on a different forwarding port. Which information selects the Layer 2 egress port?

- **A.** The source host’s TCP acknowledgment number
- **B.** The destination DNS hostname
- **C.** The destination IP longest prefix
- **D.** The destination MAC within VLAN 12

**Answer: D**

A same-VLAN Ethernet forwarding decision uses the destination MAC table. The payload’s IP routing information is not required for that bridge lookup.

**Option explanations**

- **A:** Transport sequence information is not the MAC lookup key.
- **B:** Ordinary Layer 2 lookup does not resolve names.
- **C:** That is a routing decision at a different layer.
- **D:** The MAC-to-port mapping in that VLAN identifies the egress.

**Further reading**

- [Configuring MAC Address Tables](https://www.cisco.com/c/en/us/td/docs/switches/datacenter/nexus5500/sw/layer2/7x/b_5500_Layer2_Config_7x/config_mac_address_tables.pdf) — Information About MAC Addresses (page 1); Configuring the Aging Time for the MAC Table (page 2)

---

## CCNA7-014 · Network Fundamentals

Objectives: 1.1.e · single · Applied

Cisco Catalyst Center is unreachable in an SD-Access network, but a switch retains its installed forwarding state and continues passing eligible traffic. Which conclusion is supported?

- **A.** Controllers can never influence switches
- **B.** The switch must be forwarding through the missing controller
- **C.** Loss of management reachability need not immediately remove existing forwarding state
- **D.** Every network must behave identically during controller failure

**Answer: C**

Distinguish controller access from the state currently installed in a device. The scenario proves continued forwarding here, not a universal controller-failure guarantee.

**Option explanations**

- **A:** Management/control influence is compatible with retained data forwarding.
- **B:** The scenario states the controller is unreachable.
- **C:** Behavior depends on architecture and retained device state.
- **D:** Different designs have different failure behavior.

**Further reading**

- [Cisco Software-Defined Access Design Guide](https://www.cisco.com/c/en/us/td/docs/solutions/CVD/Campus/cisco-sda-design-guide.html) — SD-Access design considerations — Management plane considerations

---

## CCNA7-015 · Network Fundamentals

Objectives: 1.6 · single · Applied

Two static address proposals for the same /24 LAN are 192.168.4.10/24 and 192.168.4.10/24 on different NICs. Both masks and gateways are correct. What issue remains?

- **A.** A subnet mask that is too long
- **B.** Duplicate IPv4 address assignment
- **C.** A mandatory optical loss failure
- **D.** A shortage of IPv6 multicast groups

**Answer: B**

Correct subnet membership does not prove host uniqueness. Each ordinary unicast interface address must also be unique within this connected addressing context.

**Option explanations**

- **A:** /24 itself is not the conflict here.
- **B:** The same host address is assigned to two interfaces on one LAN.
- **C:** Address duplication does not imply an optical fault.
- **D:** That is unrelated to the duplicated IPv4 address.

**Further reading**

- [Configure IP Addresses and Unique Subnets for New Users](https://www.cisco.com/c/en/us/support/docs/ip/routing-information-protocol-rip/13788-3.html) — Network Masks; Understand Subnetting; VLSM Example

---

## CCNA7-016 · Network Fundamentals

Objectives: 1.9.d · multiple · Challenge

The specified EUI-64 process converts MAC A4-B1-C1-02-03-04 into an interface identifier. Which TWO steps are correct? Select two.

- **A.** Change first byte A4 to A6
- **B.** Change first byte A4 to A5
- **C.** Append FF-FE after all six MAC bytes
- **D.** Reverse the order of 02-03-04
- **E.** Insert FF-FE between C1 and 02

**Answer: A, E**

The result is a6b1:c1ff:fe02:0304. The transformation changes one bit and inserts two bytes; it does not reverse the address.

**Option explanations**

- **A:** XOR A4 with 02 to invert the U/L bit.
- **B:** That changes the low-order multicast bit instead.
- **C:** The inserted pair belongs in the middle.
- **D:** The MAC byte order is retained.
- **E:** The inserted pair divides the original six bytes into two groups of three.

**Further reading**

- [RFC 2464: Transmission of IPv6 Packets over Ethernet Networks](https://datatracker.ietf.org/doc/html/rfc2464#section-4) — 4. Stateless Autoconfiguration

---

## CCNA7-017 · Network Fundamentals

Objectives: 1.11.a · single · Foundation

An engineer labels channels 1 and 2 as independent 20 MHz channels in the 2.4 GHz band. What is the error?

- **A.** 2.4 GHz has only one channel number
- **B.** Channel numbers are always 20 MHz apart
- **C.** Adjacent channel numbers overlap substantially at this width
- **D.** Only SSID names determine whether channels overlap

**Answer: C**

The spacing of channel centers is distinct from the width of occupied spectrum. Overlap must be assessed from both quantities.

**Option explanations**

- **A:** Several numbered channels exist.
- **B:** Their centers are more closely spaced than that.
- **C:** Channel numbering does not imply nonoverlapping occupied spectrum.
- **D:** RF frequency use determines spectral overlap.

**Further reading**

- [Channel Planning Best Practices](https://documentation.meraki.com/Wireless/Design_and_Configure/Architecture_and_Best_Practices/Channel_Planning_Best_Practices) — 2.4 GHz

---

## CCNA7-018 · Network Fundamentals

Objectives: 1.13.a, 1.13.c · single · Applied

An unknown-unicast frame from host A enters a switch. Host B receives the flooded copy and replies. Which event enables later directed forwarding toward B?

- **A.** The first frame’s destination automatically creates a B entry
- **B.** A DNS server returns B’s name
- **C.** A’s source entry is deleted
- **D.** B’s reply is observed with B as source on its ingress port

**Answer: D**

Unknown-unicast flooding can deliver traffic before the destination is known. A reply lets the switch learn where that destination actually resides.

**Option explanations**

- **A:** Destination naming alone does not establish B’s ingress location.
- **B:** Ordinary MAC learning does not query DNS.
- **C:** Deleting A’s entry does not locate B.
- **D:** The reply provides the source-location evidence to learn B.

**Further reading**

- [Configuring MAC Address Tables](https://www.cisco.com/c/en/us/td/docs/switches/datacenter/nexus5500/sw/layer2/7x/b_5500_Layer2_Config_7x/config_mac_address_tables.pdf) — Information About MAC Addresses (page 1); Configuring the Aging Time for the MAC Table (page 2)

---

## CCNA7-019 · Network Fundamentals

Objectives: 1.2.f · single · Applied

A business retains local compute for a service that must continue during Internet outages and uses a public-cloud service for a different workload. Which dependency must be checked for the local service’s objective?

- **A.** Whether its authentication, name resolution, and data dependencies remain available without the failed Internet connection
- **B.** Whether every local address is publicly routable
- **C.** Whether the service uses the longest possible hostname
- **D.** Whether the cloud server’s switch has the same MAC address

**Answer: A**

Hosting an application locally does not prove independence from remote services. Evaluate the complete path needed for its normal operation.

**Option explanations**

- **A:** Local compute alone does not eliminate remote dependencies.
- **B:** Public addressing is not required for local continuity.
- **C:** Hostname length does not provide continuity.
- **D:** Matching MAC addresses would not resolve service dependencies.

**Further reading**

- [Azure Well-Architected Framework — Architecture strategies for performing failure mode analysis](https://learn.microsoft.com/en-us/azure/well-architected/reliability/failure-mode-analysis) — Decompose your workload; Identify workload dependencies; Evaluate failure points in your flows — Plan mitigation strategies

---

## CCNA7-020 · Network Fundamentals

Objectives: 1.5 · matching · Applied

Match each transport observation with the protocol behavior it demonstrates. Use each option once.

1. A receiver advertises a smaller available receive window.
2. A missing segment’s byte range is sent again by the transport.
3. An application receives separate datagrams rather than an unframed byte stream.
4. Peers exchange SYN, SYN-ACK, and ACK before ordinary connected data exchange.

- **A.** TCP flow control
- **B.** UDP datagram service
- **C.** TCP connection establishment
- **D.** TCP loss recovery

**Answer: 1 → A; 2 → D; 3 → B; 4 → C**

Identify the function evidenced by the exchange. Reliability, flow control, establishment, and datagram boundaries are different properties.

**Option explanations**

- **A:** A receiver-advertised window constrains outstanding data.
- **B:** Each independently delivered unit retains its datagram boundary.
- **C:** SYN, SYN-ACK, and ACK establish the ordinary connection.
- **D:** Missing byte-stream data is retransmitted using TCP mechanisms.

**Further reading**

- [RFC 9293: Transmission Control Protocol (TCP)](https://www.rfc-editor.org/rfc/rfc9293.html#section-2.2) — 2.2. Key TCP Concepts
- [RFC 768: User Datagram Protocol](https://www.rfc-editor.org/rfc/rfc768) — Introduction; Fields

---

## CCNA7-021 · Network Access

Objectives: 2.1.a, 2.1.c · single · Applied

A laptop is moved from an access port in VLAN 30 to an access port in VLAN 40. The new VLAN’s gateway and DHCP scope are healthy, but the laptop retains its old 10.30.0.90/24 address and gateway. What is the next targeted client action?

- **A.** Obtain an address, mask, and gateway appropriate for VLAN 40.
- **B.** Disable inter-VLAN routing throughout the campus.
- **C.** Rename VLAN 40 to VLAN 30 without changing its ID.
- **D.** Add the old gateway as an allowed VLAN on the laptop.

**Answer: A**

After changing access membership, verify the endpoint’s Layer 3 configuration as well. A valid old lease is not necessarily valid on the new VLAN.

**Option explanations**

- **A:** Moving the Layer 2 attachment does not make the old subnet configuration valid.
- **B:** That removes service and does not correct the laptop’s stale configuration.
- **C:** VLAN names do not merge Layer 2 domains or fix the IP parameters.
- **D:** An IP gateway address is not a VLAN identifier.

**Further reading**

- [Configure Inter-VLAN Routing with Catalyst Switches](https://www.cisco.com/c/en/us/support/docs/lan-switching/inter-vlan-routing/41260-189.html) — Configure; Troubleshoot
- [VLAN Configuration Guide, Cisco IOS XE 17.15.x — Configuring VLANs](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst9300/software/release/17-15/configuration_guide/vlan/b_1715_vlan_9300_cg/configuring_vlans.html) — Supported VLANs; Deleting a VLAN; VLAN Port Membership Modes

---

## CCNA7-022 · Network Access

Objectives: 2.1.b, 2.2.a · single · Challenge

VLAN 1 is removed from a Catalyst trunk’s allowed data-VLAN list, yet the directly connected Cisco peer still appears in fresh CDP advertisements. Which statement explains this observation?

- **A.** Some Cisco link-control traffic can still be exchanged despite removing ordinary VLAN 1 user traffic.
- **B.** Every access port has automatically become VLAN 1 again.
- **C.** CDP necessarily tunnels through the user’s Internet browser.
- **D.** The allowed list can never exclude ordinary VLAN 1 user data.

**Answer: A**

Do not use the presence of link-control traffic as proof that ordinary user traffic in the same default VLAN is allowed. Control-plane handling can differ.

**Option explanations**

- **A:** The documented trunk behavior preserves control protocols such as CDP.
- **B:** The trunk policy does not reset unrelated access memberships.
- **C:** CDP is a directly connected Layer 2 discovery protocol.
- **D:** The list can restrict that data; the observation concerns control traffic.

**Further reading**

- [VLAN Configuration Guide, Cisco IOS XE 17.15.x — Configuring VLAN Trunks](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst9300/software/release/17-15/configuration_guide/vlan/b_1715_vlan_9300_cg/configuring_vlan_trunks.html) — Allowed VLANs on a Trunk; Configuring the Native VLAN for Untagged Traffic

---

## CCNA7-023 · Network Access

Objectives: 2.1.c · multiple · Challenge

Two hosts in different VLANs can each ping their own operational gateway SVI, and IP routing is enabled. Proxy ARP is disabled on the gateway. Host A uses its correct /24 mask; Host B mistakenly uses /16 and treats A’s address as local. Which TWO consequences follow? Select TWO.

| Host | Address | Intended VLAN subnet | Configured mask |
| --- | --- | --- | --- |
| A | 10.10.10.10 | 10.10.10.0/24 | 255.255.255.0 |
| B | 10.10.20.20 | 10.10.20.0/24 | 255.255.0.0 |

- **A.** Successful gateway pings prove every host mask is correct.
- **B.** The switch automatically corrects B’s mask when it sees an ARP.
- **C.** Correcting B’s mask to its intended /24 can repair the return path.
- **D.** B can try ARP for A directly in B’s VLAN instead of sending the reply to its gateway.

**Answer: C, D**

Verify each endpoint’s forwarding decision as well as the switch’s routing. A wrong mask can break inter-VLAN return traffic even when gateway tests succeed.

**Option explanations**

- **A:** A nearby gateway may remain reachable with an overly broad mask.
- **B:** ARP does not rewrite the endpoint’s configured subnet mask.
- **C:** The correct mask makes A remote and selects B’s gateway.
- **D:** An overly broad mask changes B’s local-versus-remote decision.

**Further reading**

- [Configure Inter-VLAN Routing with Catalyst Switches](https://www.cisco.com/c/en/us/support/docs/lan-switching/inter-vlan-routing/41260-189.html) — Configure; Troubleshoot

---

## CCNA7-024 · Network Access

Objectives: 2.2.a · single · Applied

A working trunk currently allows VLANs 10, 20, and 30. During an addition, an operator enters switchport trunk allowed vlan 40 without the add keyword. What user-data scope results on that trunk?

```text
Before: switchport trunk allowed vlan 10,20,30
Entered: switchport trunk allowed vlan 40
```

- **A.** VLAN 40 is removed and the old three remain.
- **B.** VLANs 10, 20, 30, and 40 are all allowed.
- **C.** The port automatically becomes access VLAN 40.
- **D.** Only VLAN 40 remains in the allowed list.

**Answer: D**

Small syntax differences can change the blast radius of a trunk edit. Verify the resulting allowed list immediately after the command.

**Option explanations**

- **A:** Removal uses the remove keyword.
- **B:** That would require the add form for an incremental addition.
- **C:** Editing the allowed list does not change the interface mode.
- **D:** The command replaces the current explicit list instead of appending.

**Further reading**

- [VLAN Configuration Guide, Cisco IOS XE 17.15.x — Configuring VLAN Trunks](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst9300/software/release/17-15/configuration_guide/vlan/b_1715_vlan_9300_cg/configuring_vlan_trunks.html) — Allowed VLANs on a Trunk; Configuring the Native VLAN for Untagged Traffic

---

## CCNA7-025 · Network Access

Objectives: 2.2.b, 2.2.c · single · Applied

A switch is configured to tag native-VLAN traffic, and both ends are explicitly compatible with that design. How does this differ from the usual untagged-native behavior for ordinary data frames?

- **A.** Every VLAN is merged into the native VLAN.
- **B.** Native-VLAN data is transmitted with an 802.1Q tag under the enabled tagging policy.
- **C.** The native VLAN no longer has a VLAN ID.
- **D.** The switch must remove all tags from nonnative VLANs.

**Answer: B**

State the platform’s native-tagging policy before reasoning about captures. The conventional untagged exception can be changed by explicit configuration.

**Option explanations**

- **A:** Tagging does not collapse VLAN separation.
- **B:** The explicit native-tagging setting changes the usual untagged representation.
- **C:** The VLAN remains identified even when its traffic is tagged.
- **D:** The policy does not reverse nonnative VLAN tagging.

**Further reading**

- [VLAN Configuration Guide, Cisco IOS XE 17.15.x — Configuring VLAN Trunks](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst9300/software/release/17-15/configuration_guide/vlan/b_1715_vlan_9300_cg/configuring_vlan_trunks.html) — Allowed VLANs on a Trunk; Configuring the Native VLAN for Untagged Traffic

---

## CCNA7-026 · Network Access

Objectives: 2.3 · single · Applied

A topology record says SW-1 Gi1/0/47 connects to DIST-A Gi1/0/1. Current LLDP instead reports system name DIST-B and port ID Gi1/0/24. Which next action best uses that evidence?

```text
Local interface: Gi1/0/47
System name: DIST-B
Port ID: Gi1/0/24
System capabilities: Bridge, Router
```

- **A.** Change STP cost to overwrite the remote system name.
- **B.** Change the IP default route until the LLDP name becomes DIST-A.
- **C.** Assume the record is authoritative and ignore the observed peer.
- **D.** Reconcile the physical patching and inventory against the current neighbor identity.

**Answer: D**

Discovery output is useful evidence for cabling verification, though identities should be checked against inventory. Correct the discrepancy before assuming the intended path exists.

**Option explanations**

- **A:** STP path cost does not rewrite LLDP identity.
- **B:** Routing does not choose the directly attached LLDP sender.
- **C:** Effective state should be investigated when it contradicts the documented design.
- **D:** The received neighbor identifies a different termination than the recorded design.

**Further reading**

- [Interface and Hardware Components Configuration Guide, Cisco IOS XE 17.15.x — Configuring LLDP, LLDP-MED, and Wired Location Service](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst9300/software/release/17-15/configuration_guide/int_hw/b_1715_int_and_hw_9300_cg/configuring_lldp__lldp_med__and_wired_location_service.html) — LLDP; Enabling LLDP; Monitoring and Maintaining LLDP, LLDP-MED, and Wired Location Service

---

## CCNA7-027 · Network Access

Objectives: 2.4 · single · Applied

LACP reports both members bundled, yet traffic from VLAN 92 fails across Po20. VLAN 91 works. The physical members inherit a port-channel allowed list containing only 91. What should be corrected?

```text
interface Port-channel20
 switchport mode trunk
 switchport trunk allowed vlan 91

Po20(SU) LACP Gi1/0/1(P) Gi1/0/2(P)
```

- **A.** Replace both cables solely because VLAN 91 works.
- **B.** Assign VLAN 92 an IP address on each physical member.
- **C.** The logical trunk’s permitted VLAN list must include the required VLAN 92.
- **D.** Change active LACP to passive at both ends.

**Answer: C**

Bundle formation and VLAN forwarding are separate verification layers. Fix the demonstrated logical trunk restriction.

**Option explanations**

- **A:** Working traffic and bundled state point to the displayed VLAN policy instead.
- **B:** This is a Layer 2 trunk; member addressing does not fix VLAN admission.
- **C:** A healthy aggregate does not imply that all intended VLANs are admitted.
- **D:** Passive/passive would impair new negotiation and does not add VLAN 92.

**Further reading**

- [Layer 2 Configuration Guide, Cisco IOS XE 17.15.x — Configuring EtherChannels](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst9300/software/release/17-15/configuration_guide/lyr2/b_1715_lyr2_9300_cg/configuring_etherchannels.html) — LACP Modes; EtherChannel Configuration Guidelines; Load Balancing; Layer 3 EtherChannels; Hot-Standby Ports
- [VLAN Configuration Guide, Cisco IOS XE 17.15.x — Configuring VLAN Trunks](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst9300/software/release/17-15/configuration_guide/vlan/b_1715_vlan_9300_cg/configuring_vlan_trunks.html) — Allowed VLANs on a Trunk; Configuring the Native VLAN for Untagged Traffic

---

## CCNA7-028 · Network Access

Objectives: 2.4 · multiple · Applied

Which TWO observations distinguish a routed EtherChannel from a switched trunk EtherChannel in a configuration review? Select TWO.

- **A.** Its transit IP address belongs to the port-channel interface.
- **B.** It must use PAgP because LACP is Layer 2 only.
- **C.** Its channel-group number must equal a native VLAN.
- **D.** The routed port-channel uses no switchport.

**Answer: A, D**

The forwarding role is independent of LACP negotiation. Review interface mode and the logical address location to identify a routed aggregate.

**Option explanations**

- **A:** Layer 3 addressing is on the logical aggregate.
- **B:** LACP supports routed and switched aggregates.
- **C:** A routed channel does not use native-VLAN switching on that logical interface.
- **D:** This places the logical interface into Layer 3 mode.

**Further reading**

- [Layer 2 Configuration Guide, Cisco IOS XE 17.15.x — Configuring EtherChannels](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst9300/software/release/17-15/configuration_guide/lyr2/b_1715_lyr2_9300_cg/configuring_etherchannels.html) — LACP Modes; EtherChannel Configuration Guidelines; Load Balancing; Layer 3 EtherChannels; Hot-Standby Ports

---

## CCNA7-029 · Network Access

Objectives: 2.5.a · single · Challenge

SW-Primary fails. Remaining connected switches have the base priorities shown for VLAN 80; MAC tie-breaks are unnecessary. Why does the switch named Backup not become root?

| Surviving switch | Base priority |
| --- | --- |
| Backup | 28672 |
| SW-Transit | 24576 |
| SW-Access | 32768 |

- **A.** VLAN 80 has no spanning-tree instance after one switch fails.
- **B.** SW-Transit has a lower actual bridge priority than Backup.
- **C.** A secondary designation overrides every configured priority.
- **D.** A switch named Backup can never be root.

**Answer: B**

A planned secondary root must actually outrank all other surviving candidates. The name or historical configuration command does not override current values.

**Option explanations**

- **A:** The surviving connected switches continue their election.
- **B:** Root election uses effective bridge IDs rather than device names or operator intentions.
- **C:** The election still follows the bridge ID values.
- **D:** Names have no such protocol meaning.

**Further reading**

- [Layer 2 Configuration Guide, Cisco IOS XE 17.15.x — Configuring Spanning Tree Protocol](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst9300/software/release/17-15/configuration_guide/lyr2/b_1715_lyr2_9300_cg/configuring_spanning_tree_protocol.html) — Spanning-Tree Topology and Bridge Protocol Data Units; Bridge ID, Device Priority, and Extended System ID; (Optional) Configuring a Secondary Root Device

---

## CCNA7-030 · Network Access

Objectives: 2.5.b · single · Applied

A Catalyst uses Rapid PVST+, but its show spanning-tree output labels an alternate port Altn BLK. What does that imply for ordinary user traffic on that port in the shown VLAN?

```text
Spanning tree enabled protocol rstp
Interface    Role Sts Cost
Gi1/0/1      Root FWD 4
Gi1/0/2      Altn BLK 4
```

- **A.** It is not forwarding user traffic; BLK represents the nonforwarding alternate state in this display.
- **B.** It is necessarily physically broken.
- **C.** It is forwarding half the flows for load balancing.
- **D.** Rapid PVST+ has been disabled because BLK can appear only with legacy STP.

**Answer: A**

Interpret role, state, and protocol together. A blocked alternate path is normal loop prevention, not automatically a fault.

**Option explanations**

- **A:** Cisco CLI terminology may retain BLK while RSTP groups nonforwarding behavior as discarding.
- **B:** A healthy redundant path may deliberately be nonforwarding.
- **C:** An alternate port does not actively share ordinary traffic in that instance.
- **D:** The display label alone does not prove a protocol-mode change.

**Further reading**

- [Understand Rapid Spanning Tree Protocol (802.1w)](https://www.cisco.com/c/en/us/support/docs/lan-switching/spanning-tree-protocol/24062-146.html) — New Port States and Port Roles — Port States; Alternate and Backup Port Roles

---

## CCNA7-031 · Network Access

Objectives: 2.5.c · single · Applied

A PortFast edge link to a single workstation repeatedly goes up and down. Compared with a nonedge switching link, what RSTP property helps avoid needless topology-change processing for ordinary edge transitions?

- **A.** The switch disables MAC learning on all other ports.
- **B.** PortFast prevents all future electrical link failures.
- **C.** The workstation becomes the root bridge during every link flap.
- **D.** Operational edge-port transitions do not trigger the same topology-change behavior as nonedge forwarding changes.

**Answer: D**

Edge treatment reflects that this link is not a transit bridge path. It reduces unnecessary topology disruption but does not repair an unstable endpoint link.

**Option explanations**

- **A:** Edge handling does not require globally disabling learning.
- **B:** The feature cannot stabilize cabling or power.
- **C:** An ordinary nonbridging workstation does not enter root election.
- **D:** A workstation attachment does not create a new transit path through the topology.

**Further reading**

- [Understand Rapid Spanning Tree Protocol (802.1w)](https://www.cisco.com/c/en/us/support/docs/lan-switching/spanning-tree-protocol/24062-146.html) — New Port States and Port Roles — Port States; Alternate and Backup Port Roles
- [Layer 2 Configuration Guide, Cisco IOS XE 17.15.x — Configuring Optional Spanning-Tree Features](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst9300/software/release/17-15/configuration_guide/lyr2/b_1715_lyr2_9300_cg/configuring_optional_spanning_tree_features.html) — PortFast; Bridge Protocol Data Unit Guard; Bridge Protocol Data Unit Filtering; Root Guard; Loop Guard

---

## CCNA7-032 · Network Access

Objectives: 2.5.d · single · Applied

A loop-guard-protected alternate port enters loop-inconsistent after losing BPDUs. Bidirectional operation returns and valid BPDUs resume. Which recovery is expected?

- **A.** Every VLAN database entry must be deleted.
- **B.** The port becomes a PortFast edge to avoid future monitoring.
- **C.** Loop guard can automatically release the inconsistency when valid BPDU reception resumes.
- **D.** The port always remains error-disabled until a reboot.

**Answer: C**

Recovery follows restoration of the expected protocol information. Verify the underlying one-way failure is resolved before declaring the path healthy.

**Option explanations**

- **A:** The inconsistency is related to missing BPDUs, not corrupt VLAN IDs.
- **B:** Recovery does not turn an upstream switching path into an edge.
- **C:** The feature tracks the return of the expected topology information.
- **D:** Loop-inconsistent is not inherently a permanent error-disabled shutdown.

**Further reading**

- [Understand STP Loop Guard and UDLD Features](https://www.cisco.com/c/en/us/support/docs/lan-switching/spanning-tree-protocol-stp-8021d/218321-configure-stp-with-loop-guard-and-bpdu-s.html) — STP Port Roles; STP Loop Guard

---

## CCNA7-033 · Network Access

Objectives: 2.6 · single · Applied

A compatible CleanAir AP is required as a dedicated spectrum-analysis source for a supported RF analysis application. The requirement is spectrum information rather than decoding selected Wi-Fi packets. Which AP mode is the closest fit?

- **A.** SE-Connect
- **B.** Rogue detector
- **C.** Local
- **D.** Sniffer

**Answer: A**

Choose the tool mode that matches the evidence required. RF spectrum analysis and packet decoding answer different troubleshooting questions.

**Option explanations**

- **A:** This supported mode dedicates the AP’s spectrum-analysis function to an external analysis tool.
- **B:** That legacy role monitors wired-LAN rogue activity with radios disabled.
- **C:** Local mode primarily serves centrally switched wireless clients.
- **D:** Sniffer is aimed at capture of wireless frames for packet analysis.

**Further reading**

- [Cisco Wireless Controller Configuration Guide, Release 8.5 — Managing APs](https://www.cisco.com/c/en/us/td/docs/wireless/controller/8-5/config-guide/b_cg85/managing_aps.html) — AP Modes: client-serving and network management modes

---

## CCNA7-034 · Network Access

Objectives: 2.6 · single · Applied

A branch wants centralized WLAN configuration but does not want a separate physical WLC at every branch. Its routing team can provide reliable IP reachability to a central controller. Which architecture directly fits?

- **A.** A dedicated sniffer as every branch’s production AP
- **B.** Controller-managed branch APs using a supported FlexConnect deployment
- **C.** A console-only connection between all APs and the WLC
- **D.** A separate independent local-mode controller process on every client laptop

**Answer: B**

Controller location and AP location need not coincide. The branch’s switching and authentication settings then determine its data and failure behavior.

**Option explanations**

- **A:** A capture device does not provide the required client service.
- **B:** FlexConnect supports centralized management of remote APs with configurable local data handling.
- **C:** Console cables are not the routed controller-management architecture.
- **D:** Clients do not assume that controller infrastructure role.

**Further reading**

- [Cisco Wireless Controller Configuration Guide, Release 8.10 — FlexConnect](https://www.cisco.com/c/en/us/td/docs/wireless/controller/8-10/config-guide/b_cg810/flexconnect.html) — Configuring the Switch at a Remote Site; Configuring an Access Point for FlexConnect (GUI)

---

## CCNA7-035 · Network Access

Objectives: 2.7 · single · Applied

A controller and switch are connected by a trunk that carries WLAN client VLANs. The engineer is told to move the switch interface to no switchport without redesigning controller addressing or client attachments. Why is that not a like-for-like change?

- **A.** A routed interface no longer supplies the same multi-VLAN Layer 2 trunk attachment.
- **B.** No switchport only changes the interface description.
- **C.** Routed interfaces automatically carry every 802.1Q client VLAN unchanged.
- **D.** Controller WLAN names become IP routes automatically.

**Answer: A**

Physical link state alone does not preserve interface semantics. Changing the wired forwarding mode requires a corresponding supported controller and network redesign.

**Option explanations**

- **A:** Changing the forwarding mode removes the existing VLAN carriage model.
- **B:** It changes Layer 2 versus Layer 3 interface operation.
- **C:** A plain routed port is not a replacement for this trunk design.
- **D:** No such automatic mapping restores the attachment.

**Further reading**

- [Cisco Wireless Controller Configuration Guide, Release 8.10 — Ports and Interfaces](https://www.cisco.com/c/en/us/td/docs/wireless/controller/8-10/config-guide/b_cg810/ports_and_interfaces.html) — Restrictions on Link Aggregation; Configuring Neighbor Devices to Support Link Aggregation
- [VLAN Configuration Guide, Cisco IOS XE 17.15.x — Configuring VLAN Trunks](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst9300/software/release/17-15/configuration_guide/vlan/b_1715_vlan_9300_cg/configuring_vlan_trunks.html) — Allowed VLANs on a Trunk; Configuring the Native VLAN for Untagged Traffic

---

## CCNA7-036 · Network Access

Objectives: 2.7 · single · Applied

An AP using central switching has a working CAPWAP tunnel and clients complete authentication, but the controller’s distribution trunk excludes the client VLAN. Where is the demonstrated data-path gap?

| Check | Result |
| --- | --- |
| AP joined | Yes |
| Client authentication | Successful |
| Client VLAN | 420 |
| WLC trunk allowed VLANs | 100,410 |

- **A.** In the LLDP system description on a remote printer
- **B.** Between the controller’s client VLAN interface and the wired client network
- **C.** In the console baud rate
- **D.** Between the client and AP solely because the SSID is visible

**Answer: B**

Follow the complete central-switching path past authentication. A working tunnel cannot compensate for a missing controller-side VLAN attachment.

**Option explanations**

- **A:** That metadata does not control the WLC trunk’s VLAN policy.
- **B:** That is where centrally switched client traffic must leave the controller.
- **C:** Console speed does not carry client data.
- **D:** Visibility and successful authentication do not identify this displayed wired restriction as RF failure.

**Further reading**

- [Cisco Wireless Controller Configuration Guide, Release 8.10 — AP Connectivity to Controller](https://www.cisco.com/c/en/us/td/docs/wireless/controller/8-10/config-guide/b_cg810/ap_connectivity_to_cisco_wlc.html) — CAPWAP
- [Cisco Wireless Controller Configuration Guide, Release 8.10 — Ports and Interfaces](https://www.cisco.com/c/en/us/td/docs/wireless/controller/8-10/config-guide/b_cg810/ports_and_interfaces.html) — Restrictions on Link Aggregation; Configuring Neighbor Devices to Support Link Aggregation

---

## CCNA7-037 · Network Access

Objectives: 2.8 · single · Foundation

A switch’s management SVI is misconfigured and its default route is unusable. An authorized technician is at the rack with a console cable and valid local console credentials. Which access path can still support recovery without fixing IP first?

- **A.** SSH to the unreachable management address
- **B.** A cloud dashboard over the failed management path
- **C.** HTTPS to the same unreachable management address
- **D.** The directly connected console

**Answer: D**

An out-of-band local console is useful when in-band IP configuration is broken. Its own physical and authentication requirements still apply.

**Option explanations**

- **A:** SSH depends on network transport to that address.
- **B:** The failed transport is still a dependency for that remote management route.
- **C:** HTTPS also needs a working IP path.
- **D:** A local console session does not depend on the switch’s IP forwarding path.

**Further reading**

- [Command Reference, Cisco IOS XE 17.13.x (Catalyst 9300 Switches) — Using the Command-Line Interface](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst9300/software/release/17-13/command_reference/b_1713_9300_cr/using_the_command_line_interface.html) — Accessing the CLI — Accessing the CLI through a Console Connection or through Telnet

---

## CCNA7-038 · Network Access

Objectives: 2.9 · single · Applied

An AireOS 8.5 WLAN has radio policy 802.11a only. A warehouse scanner supports only 2.4 GHz 802.11b/g/n. APs have operational radios in both bands and other WLANs work. Which GUI mismatch explains why this scanner cannot use the selected WLAN?

| Field | Value |
| --- | --- |
| WLAN Status | Enabled |
| Radio Policy | 802.11a only |
| Scanner support | 2.4 GHz only |
| Both AP radios | Operational |

- **A.** Its DHCP address must begin with the WLAN ID.
- **B.** The WLAN is restricted to 5-GHz service while the scanner supports only 2.4 GHz.
- **C.** The profile name is too short for 802.11n.
- **D.** A Gold QoS profile would add a 5-GHz radio to the scanner.

**Answer: B**

Check the WLAN’s radio policy against the actual client’s supported bands. Good AP radio health does not make every SSID available on every band.

**Option explanations**

- **A:** IP addressing is not derived from a WLAN identifier.
- **B:** AireOS 802.11a radio policy refers to the 5-GHz radio family.
- **C:** Name length does not supply the missing band compatibility.
- **D:** QoS cannot add a missing physical radio capability.

**Further reading**

- [Cisco Wireless Controller Online Help, Release 8.5 — WLANs Tab](https://www.cisco.com/c/en/us/td/docs/wireless/controller/8-5/olh/wlc-olh/wlansc.html) — Editing WLANs — General tab, Table 3-3: Radio Policy

---

## CCNA7-039 · Network Access

Objectives: 2.9 · multiple · Applied

An AireOS WLAN GUI enables a 900-second session timeout. A supported client is otherwise stable and must reauthenticate when that configured session interval expires. Which TWO statements are justified? Select TWO.

- **A.** Check authentication success at the timer boundary before assuming RF coverage loss.
- **B.** A repeat near 15 minutes is consistent with the configured session timer.
- **C.** The setting proves the AP loses electrical power every 900 seconds.
- **D.** The setting means a DHCP lease always lasts exactly 900 seconds.

**Answer: A, B**

Correlate observed timing with configured policy. Reauthentication and a DHCP lease renewal are distinct state changes.

**Option explanations**

- **A:** The policy timer supplies a specific alternative explanation for the event.
- **B:** 900 seconds equals 15 minutes.
- **C:** A session policy does not schedule AP power failure.
- **D:** Session timeout and DHCP lease duration are different timers.

**Further reading**

- [Cisco Wireless Controller Configuration Guide, Release 8.10 — WLAN Timeouts](https://www.cisco.com/c/en/us/td/docs/wireless/controller/8-10/config-guide/b_cg810/wlan_timeouts.html) — Session Timeout

---

## CCNA7-040 · Network Access

Objectives: 2.9 · matching · Applied

On an AireOS 8.5 controller, match the wireless GUI observation to the first configuration relationship it calls into question. Each case states an independent symptom and known evidence; use each answer once.

1. PSK-only client meets an 802.1X-only WLAN
2. Authentication succeeds but the bound interface is the guest VLAN instead of staff
3. WLAN is enabled but omitted from the serving AP’s custom group
4. 2.4-GHz-only client encounters a 5-GHz-only WLAN

- **A.** AP group WLAN membership
- **B.** Wired client VLAN mapping
- **C.** Client authentication method
- **D.** Radio-band policy

**Answer: 1 → C; 2 → B; 3 → A; 4 → D**

Different stages of client connectivity have different dependencies. Use the supplied evidence to select the relevant policy relationship.

**Option explanations**

- **A:** A WLAN absent from the assigned AP group may not be offered there.
- **B:** An authenticated client in the wrong DHCP subnet points toward the network attachment.
- **C:** A PSK-only client cannot perform a WLAN’s required 802.1X exchange.
- **D:** A single-band client must share an allowed operating band with the WLAN.

**Further reading**

- [Cisco Wireless Controller Online Help, Release 8.5 — WLANs Tab](https://www.cisco.com/c/en/us/td/docs/wireless/controller/8-5/olh/wlc-olh/wlansc.html) — Editing WLANs — General tab (Radio Policy; Interface/Interface Group); Layer 2 WPA + WPA2 Parameters (Authentication Key Management); AP Groups; Editing AP Groups

---

## CCNA7-041 · IP Connectivity

Objectives: 3.1.d, 3.4.d · single · Applied

The OSPF neighbor output has different values in Neighbor ID and Address. Which value identifies the adjacent interface used as the IPv4 next hop on this link?

```text
Neighbor ID     Pri   State      Dead Time   Address       Interface
10.255.0.2        1    FULL/DR    00:00:33    192.0.2.34    Gi0/0
```

- **A.** 10.255.0.2
- **B.** 1
- **C.** 192.0.2.34
- **D.** 00:00:33

**Answer: C**

Router ID identifies the OSPF speaker, while the neighbor address identifies its reachable interface on the link. Confusing them can produce incorrect static routes.

**Option explanations**

- **A:** This is the peer’s router ID, which need not be the transit next-hop address.
- **B:** The priority is not an IPv4 address.
- **C:** The Address field names the peer’s interface address on this adjacency.
- **D:** The dead timer is remaining time, not a next-hop identifier.

**Further reading**

- [Configuring OSPF — IP Routing: OSPF Configuration Guide](https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/iproute_ospf/configuration/xe-16/iro-xe-16-book/iro-cfg.html) — Enabling OSPF; Configuring OSPF Interface Parameters
- [Understand OSPF Neighbor States](https://www.cisco.com/c/en/us/support/docs/ip/open-shortest-path-first-ospf/13685-13.html) — OSPF Neighbor States

---

## CCNA7-042 · IP Connectivity

Objectives: 3.1.c, 3.1.b · single · Applied

An engineer compares these two installed route prefixes in an inventory. Which statement correctly distinguishes their destination coverage?

| Route inventory entry | Prefix |
| --- | --- |
| A | 10.160.0.0/13 |
| B | 10.160.0.0/16 |

- **A.** The /16 is broader because 16 is numerically larger.
- **B.** The /13 starts at 10.0.0.0 because 10 is private.
- **C.** Both prefixes contain exactly the same destination set.
- **D.** The /13 includes second octets 160–167; the /16 includes only 160.

**Answer: D**

Use the given prefix length independently of historical address classes. Both network fields are aligned, but their destination coverage differs substantially.

**Option explanations**

- **A:** A longer prefix is more specific, not broader.
- **B:** Private-address classification does not replace the explicit route boundary.
- **C:** Their prefix lengths constrain different numbers of bits.
- **D:** A /13 leaves three bits variable in the second octet.

**Further reading**

- [RFC 1812: Requirements for IP Version 4 Routers](https://www.rfc-editor.org/rfc/rfc1812.html) — 5.2.4 Determining the Next Hop Address

---

## CCNA7-043 · IP Connectivity

Objectives: 3.2.a · single · Applied

A troubleshooting capture shows packets sent toward a /24 route’s next hop even though the router also has a lower-distance /16 route. All installed routes are valid. Which test best checks whether this is ordinary longest-prefix behavior?

- **A.** Compare the packet’s source port to the /16 metric.
- **B.** Check whether the /16 was configured earlier in the text file.
- **C.** Check whether the /24 next hop has a longer hostname.
- **D.** Compare the packet’s destination against the /24’s address range.

**Answer: D**

Trace the packet’s actual destination through the installed table. A low-distance summary route does not displace a matching more specific route.

**Option explanations**

- **A:** Ordinary destination routing does not use that comparison.
- **B:** Configuration line order does not override installed-prefix specificity.
- **C:** Hostnames do not determine route selection.
- **D:** A matching /24 legitimately overrides a broader /16 during forwarding.

**Further reading**

- [Configure Route Selection for Routers](https://www.cisco.com/c/en/us/support/docs/ip/enhanced-interior-gateway-routing-protocol-eigrp/8651-21.html) — Build the Routing Table; Make Forwarding Decisions

---

## CCNA7-044 · IP Connectivity

Objectives: 3.2.b, 3.1.e · single · Applied

The candidate table lists two usable static routes for one exact /24. Which one wins installation, and what is the decisive field?

```text
ip route 10.177.4.0 255.255.255.0 192.0.2.42 5
ip route 10.177.4.0 255.255.255.0 192.0.2.46 50
```

- **A.** Both, because static routes ignore distance
- **B.** Via 192.0.2.46, because its address is larger
- **C.** Via 192.0.2.42, because distance 5 is lower
- **D.** Via 192.0.2.46, because distance 50 provides more redundancy

**Answer: C**

The final numeric argument in these commands is administrative distance. Both next hops are valid, so local preference decides which candidate is active.

**Option explanations**

- **A:** Static distances can distinguish primary and backup candidates.
- **B:** Numeric next-hop address ordering is not this preference rule.
- **C:** The same-prefix candidates differ in administrative preference.
- **D:** Higher distance makes a candidate less preferred, not more capable.

**Further reading**

- [Understand Administrative Distance](https://www.cisco.com/c/en/us/support/docs/ip/border-gateway-protocol-bgp/15986-admin-distance.html) — RIB Route Comparison; Route Installation; Default AD Values

---

## CCNA7-045 · IP Connectivity

Objectives: 3.2.c · single · Challenge

The local RIB contains two equal-cost OSPF next hops for a prefix. A single large TCP flow uses only one next hop under the configured per-flow forwarding hash. What does this observation imply?

- **A.** The unused next hop’s administrative distance must be 255.
- **B.** OSPF necessarily failed to install the other path.
- **C.** Every flow must alternate packets evenly across both paths.
- **D.** It is compatible with ECMP; one flow can remain on one selected path.

**Answer: D**

Routing eligibility and traffic distribution are separate observations. Test multiple flows or inspect forwarding state before concluding that a quiet equal-cost link is broken.

**Option explanations**

- **A:** A path at unusable distance would not be part of the installed ECMP set.
- **B:** The premise says both next hops are installed.
- **C:** That would describe a different forwarding behavior than the stated per-flow hash.
- **D:** Per-flow hashing need not split packets of a single flow across every next hop.

**Further reading**

- [Configure Route Selection for Routers](https://www.cisco.com/c/en/us/support/docs/ip/enhanced-interior-gateway-routing-protocol-eigrp/8651-21.html) — Build the Routing Table; Make Forwarding Decisions

---

## CCNA7-046 · IP Connectivity

Objectives: 3.3.b · single · Applied

A network route to remote 10.191.0.0/16 must use adjacent 198.51.100.10 specifically through GigabitEthernet0/1. Which Cisco IOS static form states both constraints?

- **A.** ip route 10.191.0.0 255.255.0.0 GigabitEthernet0/1
- **B.** ip route 10.191.0.0 0.0.255.255 198.51.100.10
- **C.** ip route 10.191.0.0 255.255.0.0 GigabitEthernet0/1 198.51.100.10
- **D.** ip route 198.51.100.10 255.255.255.255 10.191.0.1

**Answer: C**

A fully specified route removes ambiguity about both where to exit and which adjacent router to use. The destination mask remains an ordinary subnet mask.

**Option explanations**

- **A:** This omits the adjacent-router constraint on the multiaccess exit.
- **B:** ip route takes a subnet mask here, not an ACL wildcard.
- **C:** This fully specifies the exit interface and next-hop router.
- **D:** This reverses the destination and forwarding direction.

**Further reading**

- [Configure a Next Hop IP Address for Static Routes](https://www.cisco.com/c/en/us/support/docs/dial-access/floating-static-route/118263-technote-nexthop-00.html) — Background Information; Floating Static Route Example

---

## CCNA7-047 · IP Connectivity

Objectives: 3.3.a · multiple · Applied

A router has a static default whose next hop is valid and all remote specific routes have been removed for maintenance. Which two statements remain true? Select two.

- **A.** Selecting the default does not prove successful delivery beyond the neighbor.
- **B.** The default supplies an ARP response for every remote host.
- **C.** A default can match only publicly allocated addresses.
- **D.** Any otherwise unmatched IPv4 unicast destination can select the default.

**Answer: A, D**

A default describes destination coverage, not a promise about remote reachability or address allocation. Keep the forwarding decision separate from the eventual outcome.

**Option explanations**

- **A:** The neighbor’s onward path remains a separate dependency.
- **B:** A next-hop default directs frames to the adjacent router, not an ARP service for every host.
- **C:** Private versus public status does not change /0 matching.
- **D:** The /0 covers every IPv4 destination as a fallback.

**Further reading**

- [Configure Route Selection for Routers](https://www.cisco.com/c/en/us/support/docs/ip/enhanced-interior-gateway-routing-protocol-eigrp/8651-21.html) — Build the Routing Table; Make Forwarding Decisions
- [RFC 1812: Requirements for IP Version 4 Routers](https://www.rfc-editor.org/rfc/rfc1812.html) — 5.2.4 Determining the Next Hop Address

---

## CCNA7-048 · IP Connectivity

Objectives: 3.3.c, 3.1.a · single · Applied

A table contains L 10.14.0.1/32 and S 10.14.0.2/32 via another router. What is the key distinction despite both being host-length routes?

- **A.** Both addresses must be assigned to this router.
- **B.** The S route is automatically an HSRP standby address.
- **C.** L is a local address of this router; S is a configured route to a destination elsewhere.
- **D.** The L route always forwards packets to the S route.

**Answer: C**

Prefix length states scope; the route source and next-hop behavior state purpose. A host route is not necessarily a local interface address.

**Option explanations**

- **A:** A static host route does not imply local address ownership.
- **B:** S denotes static routing, not an FHRP role.
- **C:** Source and forwarding meaning differ even when prefix lengths match.
- **D:** Local delivery is not a chain to the neighboring host route.

**Further reading**

- [Local Host Routes Installed in the Routing Table on Cisco IOS and Cisco IOS-XR](https://www.cisco.com/c/en/us/support/docs/ip/ip-routing/116264-technote-ios-00.html) — Cisco IOS Local Routes; Manually Configured Host Routes

---

## CCNA7-049 · IP Connectivity

Objectives: 3.3.d · single · Applied

A static backup route is absent from show ip route but present in running-config. Its primary dynamic route is currently installed and healthy. What should be checked before treating the absence as a fault?

- **A.** Whether the next-hop address is numerically higher than the primary
- **B.** Whether its higher distance intentionally makes it a floating candidate for that same prefix
- **C.** Whether every host has a matching backup route command
- **D.** Whether the route’s text appears before the hostname command

**Answer: B**

Assess observed absence against intended standby behavior. Separately verify that the backup’s next hop remains valid for the failure being protected against.

**Option explanations**

- **A:** Address magnitude is not the floating-route condition.
- **B:** A correctly configured backup can be unselected during healthy primary operation.
- **C:** Ordinary hosts do not need to mirror router static configuration.
- **D:** Configuration display position does not determine backup validity.

**Further reading**

- [Understand Administrative Distance](https://www.cisco.com/c/en/us/support/docs/ip/border-gateway-protocol-bgp/15986-admin-distance.html) — RIB Route Comparison; Route Installation; Default AD Values
- [Configure a Next Hop IP Address for Static Routes](https://www.cisco.com/c/en/us/support/docs/dial-access/floating-static-route/118263-technote-nexthop-00.html) — Background Information; Floating Static Route Example

---

## CCNA7-050 · IP Connectivity

Objectives: 3.3.b · single · Applied

A remote IPv6 subnet moves behind a new adjacent router. The old neighbor still responds, and the original static remains installed. What configuration property explains why the path has not automatically followed the move?

- **A.** IPv6 static routes continuously discover the nearest server location.
- **B.** The static route retains its explicitly configured next hop until changed or invalidated.
- **C.** A /64 destination guarantees reachability through every adjacent router.
- **D.** An installed route always follows a destination’s MAC wherever it moves globally.

**Answer: B**

Static configuration can remain operationally valid yet point toward an obsolete path. Maintenance must update routing intent as well as checking local neighbor reachability.

**Option explanations**

- **A:** Static routing does not perform that discovery.
- **B:** It does not learn this topology move through a routing protocol.
- **C:** The prefix does not prove every neighbor has an onward path.
- **D:** MAC learning is link-local and not a replacement for routed topology updates.

**Further reading**

- [IPv6 Routing: Static Routing — Cisco IOS XE 17.x](https://www.cisco.com/c/en/us/td/docs/routers/ios/config/17-x/ip-routing/b-ip-routing/m_ip6-route-static-xe.html) — Recursive Static Routes; Fully Specified Static Routes; Floating Static Routes

---

## CCNA7-051 · IP Connectivity

Objectives: 3.3.b, 3.3.c · single · Applied

A temporary IPv6 host route should redirect only 2001:db8:720::9 through FE80::2 on GigabitEthernet0/3. IPv6 forwarding is enabled and the neighbor is reachable. Which command meets both host scope and next-hop scope?

- **A.** ipv6 route 2001:db8:720::/64 GigabitEthernet0/3 FE80::2
- **B.** ipv6 route FE80::2/128 GigabitEthernet0/3 2001:db8:720::9
- **C.** ipv6 route 2001:db8:720::9/128 GigabitEthernet0/3 FE80::2
- **D.** ipv6 route 2001:db8:720::9/128 FE80::2

**Answer: C**

Two independent scopes must be correct: destination prefix length and next-hop link context. A correct address with either scope wrong does not meet the requirement.

**Option explanations**

- **A:** The /64 affects the entire remote subnet.
- **B:** This reverses the destination and neighbor roles.
- **C:** The /128 isolates the host, and the interface scopes the link-local neighbor.
- **D:** The link-local next hop lacks its required interface scope.

**Further reading**

- [IPv6 Routing: Static Routing — Cisco IOS XE 17.x](https://www.cisco.com/c/en/us/td/docs/routers/ios/config/17-x/ip-routing/b-ip-routing/m_ip6-route-static-xe.html) — Recursive Static Routes; Fully Specified Static Routes; Floating Static Routes

---

## CCNA7-052 · IP Connectivity

Objectives: 3.3.b, 3.3.d · matching · Applied

Match each static-routing observation to the most directly indicated issue or interpretation.

1. Configured recursive route absent, and its next hop has no resolving route
2. Backup /24 absent while a lower-distance route to that /24 is active
3. Static still installed, neighbor responds, but the provider’s far-end circuit is down
4. A /24 maintenance exception unexpectedly redirects every server in the LAN

- **A.** Expected standby behavior
- **B.** Next-hop resolution failure
- **C.** Remote-path failure beyond local validity checks
- **D.** Overly broad destination scope

**Answer: 1 → B; 2 → A; 3 → C; 4 → D**

Identical user symptoms can arise from different route properties. Identify validity, preference, remote delivery, and scope separately.

**Option explanations**

- **A:** A valid higher-distance candidate can remain unselected while the primary exists.
- **B:** Without a usable resolving route, a recursive static is not an installable path.
- **C:** An adjacent next hop can stay reachable while a more distant path breaks.
- **D:** A network prefix can redirect additional hosts when a host exception was intended.

**Further reading**

- [Configure a Next Hop IP Address for Static Routes](https://www.cisco.com/c/en/us/support/docs/dial-access/floating-static-route/118263-technote-nexthop-00.html) — Background Information; Floating Static Route Example
- [Understand Administrative Distance](https://www.cisco.com/c/en/us/support/docs/ip/border-gateway-protocol-bgp/15986-admin-distance.html) — RIB Route Comparison; Route Installation; Default AD Values
- [IPv6 Routing: Static Routing — Cisco IOS XE 17.x](https://www.cisco.com/c/en/us/td/docs/routers/ios/config/17-x/ip-routing/b-ip-routing/m_ip6-route-static-xe.html) — Recursive Static Routes; Fully Specified Static Routes; Floating Static Routes

---

## CCNA7-053 · IP Connectivity

Objectives: 3.4.a · single · Applied

Both routers’ OSPF interfaces use Hello 5 and Dead 20 on the same area-0 broadcast subnet. Other requirements match. A reviewer objects because the timers differ from common Ethernet defaults. What is correct?

- **A.** Every broadcast OSPF link must use Hello 10 and Dead 40.
- **B.** Matching supported nondefault timers can still form an adjacency.
- **C.** Only the DR is allowed to use a nondefault Hello interval.
- **D.** The timers must instead equal the local process numbers.

**Answer: B**

Distinguish a default value from a mandatory protocol-wide constant. Verify that the chosen timers are supported and consistent on the link.

**Option explanations**

- **A:** Configured supported timer values can be changed consistently.
- **B:** Compatibility requires agreement; it does not require keeping the common defaults.
- **C:** Neighbors still need compatible advertised timers.
- **D:** Process numbers do not define the adjacency timers.

**Further reading**

- [Configuring OSPF — IP Routing: OSPF Configuration Guide](https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/iproute_ospf/configuration/xe-16/iro-xe-16-book/iro-cfg.html) — Enabling OSPF; Configuring OSPF Interface Parameters
- [Troubleshoot OSPF Neighbor Problems](https://www.cisco.com/c/en/us/support/docs/ip/open-shortest-path-first-ospf/13699-29.html) — No State Revealed; Neighbors Stuck in Exstart/Exchange State

---

## CCNA7-054 · IP Connectivity

Objectives: 3.4.a · single · Foundation

The neighbor dead countdown repeatedly resets before reaching zero while valid Hellos continue arriving. What does this indicate?

- **A.** The router is repeatedly changing its router ID.
- **B.** The OSPF process must be restarting every few seconds.
- **C.** Each accepted Hello refreshes the neighbor’s liveness timer.
- **D.** The route metric is counting downward until it reaches zero.

**Answer: C**

A countdown that refreshes is expected during healthy neighbor maintenance. Focus on missed refreshes or expiry when investigating adjacency loss.

**Option explanations**

- **A:** Normal Hello reception does not change the router’s identity.
- **B:** Timer refresh is normal behavior and does not imply process restart.
- **C:** Regular Hello reception prevents the inactivity timer from expiring.
- **D:** Dead time is liveness state, not path cost.

**Further reading**

- [RFC 2328: OSPF Version 2](https://www.rfc-editor.org/rfc/rfc2328.html) — 9.4 Electing the Designated Router; 10 The Neighbor Data Structure; 16 Calculation of the routing table
- [Understand OSPF Neighbor States](https://www.cisco.com/c/en/us/support/docs/ip/open-shortest-path-first-ospf/13685-13.html) — OSPF Neighbor States

---

## CCNA7-055 · IP Connectivity

Objectives: 3.4.a · single · Challenge

R1 and R2 are Full in one OSPF area, but their best next hops to the same LAN differ. Is that necessarily an OSPF database-synchronization failure?

- **A.** No; each router computes shortest paths from its own position.
- **B.** Yes; only the DR may calculate shortest paths.
- **C.** No, because Full routers never use a link-state database.
- **D.** Yes; every router in an area must have an identical routing table.

**Answer: A**

Identical topology knowledge and identical forwarding tables are different concepts. Each router evaluates paths from itself toward each destination.

**Option explanations**

- **A:** A shared topology database does not require identical next-hop choices at different roots.
- **B:** Each OSPF router performs its own route calculation.
- **C:** The explanation is root-relative calculation, not absence of a database.
- **D:** Different local positions naturally produce different forwarding next hops.

**Further reading**

- [RFC 2328: OSPF Version 2](https://www.rfc-editor.org/rfc/rfc2328.html) — 9.4 Electing the Designated Router; 10 The Neighbor Data Structure; 16 Calculation of the routing table

---

## CCNA7-056 · IP Connectivity

Objectives: 3.4.b · single · Applied

A change converts both ends of an Ethernet link from OSPF broadcast to point-to-point during an approved maintenance window. What is the intended protocol-level simplification?

- **A.** Remove the DR/BDR election and broadcast pseudonode relationship on that two-router link.
- **B.** Make OSPF use TCP instead of IP protocol 89.
- **C.** Remove the need for unique router IDs.
- **D.** Remove all Hello packets and neighbor failure detection.

**Answer: A**

The network type changes the adjacency model, not the need for liveness or identity. Apply it consistently and verify reconvergence.

**Option explanations**

- **A:** Point-to-point directly models the adjacency between the two participants.
- **B:** Network type does not change OSPFv2 into a TCP application.
- **C:** Unique OSPF identities remain required.
- **D:** Point-to-point OSPF still uses neighbor discovery and maintenance.

**Further reading**

- [RFC 2328: OSPF Version 2](https://www.rfc-editor.org/rfc/rfc2328.html) — 9.4 Electing the Designated Router; 10 The Neighbor Data Structure; 16 Calculation of the routing table
- [Configuring OSPF — IP Routing: OSPF Configuration Guide](https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/iproute_ospf/configuration/xe-16/iro-xe-16-book/iro-cfg.html) — Enabling OSPF; Configuring OSPF Interface Parameters

---

## CCNA7-057 · IP Connectivity

Objectives: 3.4.c · single · Challenge

A broadcast LAN contains an established DR and no BDR because all other routers have priority 0. A new eligible router joins with priority 50. The DR stays healthy. What role can the newcomer acquire after election processing?

- **A.** A second simultaneous DR by design
- **B.** DR solely because every other non-DR has priority 0
- **C.** BDR while the incumbent remains DR
- **D.** No role until the entire LAN restarts

**Answer: C**

An unfilled backup role and an occupied active role are different election conditions. Existing role state still constrains the result.

**Option explanations**

- **A:** The intended segment state has one DR, not two healthy concurrent DRs.
- **B:** The established DR is not displaced merely by the newcomer’s eligibility.
- **C:** It can fill the vacant backup role without preempting the healthy DR.
- **D:** The protocol can fill a vacant BDR role during normal operation.

**Further reading**

- [RFC 2328: OSPF Version 2](https://www.rfc-editor.org/rfc/rfc2328.html) — 9.4 Electing the Designated Router; 10 The Neighbor Data Structure; 16 Calculation of the routing table

---

## CCNA7-058 · IP Connectivity

Objectives: 3.4.c, 3.4.d · multiple · Applied

For a new broadcast segment with no incumbent DR/BDR, all eligible routers have priority 1. Which two inputs or conditions matter to predicting the result? Select two.

- **A.** The devices’ chassis serial numbers
- **B.** The alphabetical order of interface descriptions
- **C.** Which routers have actually participated before the initial election completes
- **D.** The routers’ OSPF router IDs

**Answer: C, D**

Router-ID comparison is valid only within the actual election participants and state. Stating timing assumptions is essential for a deterministic initial-election question.

**Option explanations**

- **A:** Serial numbers are not advertised election tie-breakers.
- **B:** Descriptions are not part of DR election.
- **C:** Arrival timing and existing role declarations can alter a simplistic simultaneous-start assumption.
- **D:** With equal nonzero priorities, higher router IDs rank higher.

**Further reading**

- [RFC 2328: OSPF Version 2](https://www.rfc-editor.org/rfc/rfc2328.html) — 9.4 Electing the Designated Router; 10 The Neighbor Data Structure; 16 Calculation of the routing table

---

## CCNA7-059 · IP Connectivity

Objectives: 3.4.d · single · Applied

A router’s highest physical IPv4 interface is administratively down before its first OSPF startup; there are no loopbacks or explicit ID. Which set should automatic selection examine?

- **A.** Eligible active interface IPv4 addresses
- **B.** Every address ever present in startup-config, regardless of availability
- **C.** Only the directly connected peer’s addresses
- **D.** Only IPv6 link-local addresses converted to decimal

**Answer: A**

Initial conditions matter: interface availability at selection time is different from adding or removing addresses after an ID is already active.

**Option explanations**

- **A:** The unavailable interface should not be treated as an active candidate at initial selection.
- **B:** Configured history alone does not make a down interface an active selection candidate.
- **C:** A router chooses its own identity, not a peer’s address.
- **D:** OSPFv2 router-ID selection here uses a 32-bit IPv4-format identifier.

**Further reading**

- [Configuring OSPF — IP Routing: OSPF Configuration Guide](https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/iproute_ospf/configuration/xe-16/iro-xe-16-book/iro-cfg.html) — Enabling OSPF; Configuring OSPF Interface Parameters

---

## CCNA7-060 · IP Connectivity

Objectives: 3.2.c · single · Applied

A manual cost change on R1 makes its outgoing path through R2 cheaper. R2’s interface costs are unchanged. What must not be assumed about return traffic?

- **A.** That R1 will recalculate affected shortest paths
- **B.** That other routers may receive updated topology information
- **C.** That the reverse path automatically changes in the same way
- **D.** That next-hop choices should be verified after convergence

**Answer: C**

Routing is directional. A forward-path optimization does not by itself impose a symmetric return path.

**Option explanations**

- **A:** Changing a link cost is an input to the local and distributed OSPF calculation.
- **B:** The changed advertised cost can be propagated through OSPF.
- **C:** Each router’s own cost and topology calculations determine its forwarding direction.
- **D:** Operational verification is appropriate after the change.

**Further reading**

- [RFC 2328: OSPF Version 2](https://www.rfc-editor.org/rfc/rfc2328.html) — 9.4 Electing the Designated Router; 10 The Neighbor Data Structure; 16 Calculation of the routing table

---

## CCNA7-061 · IP Connectivity

Objectives: 3.4.a · single · Applied

An OSPF neighbor has remained in Loading for several minutes. What evidence is more useful than repeatedly increasing the interface priority?

- **A.** The HSRP virtual MAC’s hexadecimal value
- **B.** The number of user DHCP leases
- **C.** Whether requested LSAs and their responses are being delivered successfully
- **D.** The router hostname’s character count

**Answer: C**

Investigate the packets and state associated with the stage that is stuck. Election-priority changes do not repair missing link-state information.

**Option explanations**

- **A:** That does not directly explain OSPF link-state request completion.
- **B:** Lease count is not the direct state-machine condition for Loading completion.
- **C:** Loading is concerned with obtaining database information still missing or outdated.
- **D:** The name length does not govern database synchronization.

**Further reading**

- [Understand OSPF Neighbor States](https://www.cisco.com/c/en/us/support/docs/ip/open-shortest-path-first-ospf/13685-13.html) — OSPF Neighbor States
- [Troubleshoot OSPF Neighbor Problems](https://www.cisco.com/c/en/us/support/docs/ip/open-shortest-path-first-ospf/13699-29.html) — No State Revealed; Neighbors Stuck in Exstart/Exchange State

---

## CCNA7-062 · IP Connectivity

Objectives: 3.5 · single · Foundation

A dual-stack LAN needs first-hop redundancy for IPv4 and IPv6. Which statement about VRRPv3 is correct at the capability level?

- **A.** VRRPv3 requires converting IPv6 traffic to IPv4.
- **B.** VRRPv3 is an OSPF network type.
- **C.** VRRPv3 eliminates each router’s need for onward IPv6 routes.
- **D.** VRRPv3 is specified for both IPv4 and IPv6 virtual routers.

**Answer: D**

Address-family support is part of selecting an appropriate first-hop mechanism. Configuration and platform support must then implement the intended family-specific groups.

**Option explanations**

- **A:** IPv6 virtual-router operation is supported without that conversion requirement.
- **B:** VRRP is a separate first-hop redundancy protocol.
- **C:** The active forwarder still requires usable IPv6 routing information.
- **D:** The current protocol specification covers both address families.

**Further reading**

- [RFC 9568: Virtual Router Redundancy Protocol (VRRP) Version 3 for IPv4 and IPv6](https://www.rfc-editor.org/rfc/rfc9568.html) — 1 Introduction; 2 Required Features; 6 Protocol State Machine

---

## CCNA7-063 · IP Connectivity

Objectives: 3.5 · single · Applied

During a clean HSRP active-router power failure, the host’s cached mapping already points to the normal virtual MAC. Once the standby takes over and Layer 2 forwarding converges, why can the existing mapping remain useful?

- **A.** The host automatically chooses a new subnet from the standby’s router ID.
- **B.** The standby sends all packets through the powered-off router.
- **C.** Every failover requires a different virtual MAC by definition.
- **D.** The new active uses the group’s virtual gateway identity.

**Answer: D**

The stable virtual identity reduces host changes during failover. The network must still deliver frames to the new physical owner.

**Option explanations**

- **A:** The host does not derive its subnet from OSPF identity.
- **B:** The new active is expected to forward using its own usable path.
- **C:** Normal HSRP preserves the group’s virtual identity.
- **D:** The virtual IP-to-MAC association can remain stable while its physical owner changes.

**Further reading**

- [Understand the Hot Standby Router Protocol Features and Functionality](https://www.cisco.com/c/en/us/support/docs/ip/hot-standby-router-protocol-hsrp/9234-hsrpguidetoc.html) — HSRP Background and Operations; HSRP Operation

---

## CCNA7-064 · IP Connectivity

Objectives: 3.5 · single · Applied

A standby gateway has a working LAN interface but no route to a critical remote subnet. The primary is about to be removed for maintenance. Which acceptance gap matters most?

- **A.** The standby does not use the primary’s physical IP address.
- **B.** The standby’s hostname is different from the primary’s.
- **C.** The standby’s onward reachability to that subnet has not been established.
- **D.** The standby’s OSPF process number is not identical to the primary’s.

**Answer: C**

Commission the path that will exist after the failure, not only the current active path. A standby label is not evidence of complete routing readiness.

**Option explanations**

- **A:** Distinct physical addresses are normal.
- **B:** Different names do not prevent correct forwarding.
- **C:** Taking ownership of the virtual gateway is insufficient without a usable onward path.
- **D:** Locally significant process numbers need not match.

**Further reading**

- [Understand the Hot Standby Router Protocol Features and Functionality](https://www.cisco.com/c/en/us/support/docs/ip/hot-standby-router-protocol-hsrp/9234-hsrpguidetoc.html) — HSRP Background and Operations; HSRP Operation
- [RFC 9568: Virtual Router Redundancy Protocol (VRRP) Version 3 for IPv4 and IPv6](https://www.rfc-editor.org/rfc/rfc9568.html) — 1 Introduction; 2 Required Features; 6 Protocol State Machine

---

## CCNA7-065 · IP Connectivity

Objectives: 3.2.a, 3.1.g · multiple · Challenge

The installed /24 route is withdrawn, while the displayed summary discard route and default remain installed. Which two statements describe traffic after convergence? Select two.

```text
Before withdrawal:
O 10.202.9.0/24 [110/15] via 192.0.2.50
S 10.202.0.0/16 [200/0] is directly connected, Null0
S* 0.0.0.0/0 [1/0] via 192.0.2.54
```

- **A.** Traffic for 10.202.9.10 is discarded by the /16 route.
- **B.** Traffic for 203.0.113.10 can still use the default.
- **C.** The default must be withdrawn when the /24 disappears.
- **D.** Traffic for 10.202.9.10 automatically falls through Null0 to the default.

**Answer: A, B**

An aggregate discard can intentionally stop traffic for holes in the aggregate. Removing a specific exception can therefore change forwarding into discarding, while unrelated default traffic still works.

**Option explanations**

- **A:** The removed exception exposes the covering discard route as the longest remaining match.
- **B:** That destination is outside the /16 discard prefix.
- **C:** The independent default is stated to remain installed.
- **D:** An installed discard route is a terminal forwarding action, not a failed lookup.

**Further reading**

- [Configure Route Selection for Routers](https://www.cisco.com/c/en/us/support/docs/ip/enhanced-interior-gateway-routing-protocol-eigrp/8651-21.html) — Build the Routing Table; Make Forwarding Decisions
- [Configure a Next Hop IP Address for Static Routes](https://www.cisco.com/c/en/us/support/docs/dial-access/floating-static-route/118263-technote-nexthop-00.html) — Background Information; Floating Static Route Example

---

## CCNA7-066 · IP Services

Objectives: 4.1 · multiple · Applied

A server uses a full-address static inside-source NAT mapping. The same private server must remain reachable through a stable translated address after idle periods, and security policy is enforced separately. Which two statements are correct? Select two.

- **A.** The configured static mapping provides a fixed inside-local to inside-global binding.
- **B.** The server must open an outbound connection before any configured static mapping can exist.
- **C.** The mapping alone does not define a complete firewall permission policy.
- **D.** A static mapping encrypts the application payload crossing the router.
- **E.** Idle expiration must assign the server a different global address from a dynamic pool.

**Answer: A, C**

Static NAT provides a stable address association that is useful for a published internal service. It neither supplies encryption nor replaces the separately specified security policy.

**Option explanations**

- **A:** Its identity does not depend on borrowing whichever pool address is free for a new dynamic binding.
- **B:** A static mapping is defined by configuration rather than first outbound allocation.
- **C:** Address translation and traffic authorization are separate functions.
- **D:** Address translation does not encrypt the payload.
- **E:** That describes a possibility for dynamic allocation, not the fixed static binding.

**Further reading**

- [Configure Network Address Translation](https://www.cisco.com/c/en/us/support/docs/ip/network-address-translation-nat/13772-12.html) — NAT definitions; configuring inside source translation
- [RFC 3022 — Traditional IP Network Address Translator (Traditional NAT)](https://www.rfc-editor.org/rfc/rfc3022.html) — 2 Overview; 3 Translation phases

---

## CCNA7-067 · IP Services

Objectives: 4.2 · single · Applied

A router has two configured NTP associations. The constructed operational summary identifies one as the selected system time source and the other as an eligible candidate. What can be concluded from this snapshot?

| Server | Reachable | Association state |
| --- | --- | --- |
| 10.70.0.10 | Yes | Selected system time source |
| 10.70.0.20 | Yes | Eligible candidate |

- **A.** The router currently disciplines its clock using the selected source, while the other remains a candidate.
- **B.** Both server addresses must be averaged equally because both are configured.
- **C.** The unselected candidate must be unreachable.
- **D.** The selected source is permanently fixed and cannot change after a failure.

**Answer: A**

Interpret current selection separately from configured alternatives. A healthy candidate can remain unselected, and source choice can change when synchronization conditions change.

**Option explanations**

- **A:** Candidate availability and current selection are distinct operational states.
- **B:** The summary distinguishes a selected source from a candidate; configuration alone does not imply equal contribution.
- **C:** It is explicitly listed as reachable and eligible.
- **D:** NTP can reevaluate source suitability as conditions change.

**Further reading**

- [RFC 5905 — Network Time Protocol Version 4: Protocol and Algorithms Specification](https://www.rfc-editor.org/rfc/rfc5905.html) — 7 NTP protocol data structures; 9 Peer process; 11 System process
- [Use Best Practices for Network Time Protocol](https://www.cisco.com/c/en/us/support/docs/availability/high-availability/19643-ntpm.html) — NTP architecture; synchronization; verification

---

## CCNA7-068 · IP Services

Objectives: 4.3 · single · Foundation

A web team wants portal.example to be an alias for webcluster.example, so the alias follows the canonical name's address records. Which record type expresses that relationship?

- **A.** PTR
- **B.** AAAA containing webcluster.example
- **C.** CNAME
- **D.** DHCP router option

**Answer: C**

A CNAME supplies another name for the resolver to follow. The canonical name's A or AAAA records provide the actual addresses.

**Option explanations**

- **A:** It is used for pointer records, commonly reverse-address lookup.
- **B:** AAAA holds an IPv6 address, not a canonical domain name.
- **C:** It maps an alias name to a canonical domain name.
- **D:** That DHCP option advertises gateways and does not create a DNS alias.

**Further reading**

- [RFC 1034 — Domain Names - Concepts and Facilities](https://www.rfc-editor.org/rfc/rfc1034.html) — 3.6 Resource records; 4.3 Name server algorithms; 5 Resolvers
- [RFC 1035 — Domain Names - Implementation and Specification](https://www.rfc-editor.org/rfc/rfc1035.html) — 3.3 Standard resource records; 4.1 Message format; 4.2 Transport

---

## CCNA7-069 · IP Services

Objectives: 4.3 · single · Applied

A DHCP scope for 10.77.0.0/24 advertises router option 10.77.0.254, but the only functioning gateway on that VLAN is 10.77.0.1. Clients can communicate with local peers and a local DNS server, but cannot reach remote subnets. Which scope correction targets the demonstrated problem?

- **A.** Advertise a longer DNS search suffix.
- **B.** Advertise 10.77.0.1 as the router option.
- **C.** Change all client leases to permanent without changing the gateway option.
- **D.** Replace the DNS server option with 10.77.0.254.

**Answer: B**

DHCP distributes several independent settings; a usable address and resolver do not guarantee a correct default gateway. Correct the router option and ensure clients obtain the updated configuration.

**Option explanations**

- **A:** Name expansion cannot make the nonexistent gateway forward packets.
- **B:** The clients need the actual first-hop gateway for off-subnet traffic.
- **C:** Lease duration does not correct the bad next-hop address.
- **D:** Changing the resolver to an unused gateway address worsens name resolution without fixing forwarding.

**Further reading**

- [RFC 2132 — DHCP Options and BOOTP Vendor Extensions](https://www.rfc-editor.org/rfc/rfc2132.html) — 3.3 Subnet Mask; 3.5 Router; 3.8 Domain Name Server; 3.17 Domain Name

---

## CCNA7-070 · IP Services

Objectives: 4.4 · single · Applied

A router sends an SNMP linkDown trap while its management path is also failing. The manager receives no trap. Which statement correctly describes the evidentiary limit?

- **A.** SNMP guarantees that all managers receive every event in exact order.
- **B.** The missing trap does not establish that the link remained up.
- **C.** A trap can be delivered even when every possible path to the manager is unavailable.
- **D.** SNMP traps automatically keep retrying until the manager acknowledges them.

**Answer: B**

A monitoring channel can fail during the same event it is meant to report. Corroborate with later polling or other evidence rather than treating absence of a trap as proof of healthy state.

**Option explanations**

- **A:** The protocol does not provide that guarantee for traps.
- **B:** An unacknowledged event notification can be lost along the failed path.
- **C:** A notification still depends on a working communication path.
- **D:** That acknowledgment behavior belongs to informs rather than traps.

**Further reading**

- [RFC 3416 — Version 2 of the Protocol Operations for the Simple Network Management Protocol (SNMP)](https://www.rfc-editor.org/rfc/rfc3416.html) — 4.2 PDU processing: Get, GetNext, GetBulk, Set, notifications

---

## CCNA7-071 · IP Services

Objectives: 4.5 · single · Applied

During a planned change, a collector needs normal but significant severity-5 notifications and all more urgent events, while excluding informational and debugging messages. Which IOS remote logging threshold meets that exact requirement?

- **A.** logging trap warnings
- **B.** logging trap notifications
- **C.** logging trap debugging
- **D.** logging trap informational

**Answer: B**

Select the numerically highest severity that should pass. The threshold is inclusive and also admits all numerically lower, more urgent levels.

**Option explanations**

- **A:** This admits only 0 through 4 and therefore loses the required notifications.
- **B:** This admits levels 0 through 5 and excludes levels 6 and 7.
- **C:** This admits all severities, including both excluded levels.
- **D:** This also admits level 6, which the requirement excludes.

**Further reading**

- [System Message Logging](https://www.cisco.com/c/en/us/td/docs/routers/access/wireless/software/guide/SysMsgLogging.html) — System log message format; logging destinations; severity levels; timestamps

---

## CCNA7-072 · IP Services

Objectives: 4.6 · single · Applied

An IOS XE router has a correct helper address on the client-facing interface, reachable DHCP server scopes, and valid return routes. After a hardening change, no DHCP broadcasts are relayed. Which shown line directly disables the required DHCP relay function?

```text
no service dhcp
interface GigabitEthernet0/2
 description CLIENT-LAN
 ip address 10.72.0.1 255.255.255.0
 ip helper-address 10.9.0.40
```

- **A.** ip helper-address 10.9.0.40
- **B.** description CLIENT-LAN
- **C.** no service dhcp
- **D.** ip address 10.72.0.1 255.255.255.0

**Answer: C**

A correct interface helper still depends on the global DHCP service being enabled. Reenable service dhcp to restore this dependency, while retaining the verified scope and path configuration.

**Option explanations**

- **A:** This is the valid per-interface forwarding destination.
- **B:** An interface description does not disable DHCP forwarding.
- **C:** This disables the IOS XE DHCP server and relay service globally.
- **D:** This supplies the correct gateway address for the client subnet.

**Further reading**

- [IP Addressing: DHCP Configuration Guide, Cisco IOS XE Everest 16.6 — Configuring the Cisco IOS XE DHCP Relay Agent](https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/ipaddr_dhcp/configuration/xe-16-6/dhcp-xe-16-6-book/dhcp-relay-agent-xe.html) — Packet forwarding address; giaddr; specifying the packet forwarding address

---

## CCNA7-073 · IP Services

Objectives: 4.7 · single · Applied

A switch trusts incoming DSCP markings from every attached host. A bulk-transfer workstation marks its own packets with the value reserved for voice, and the switch gives them voice treatment. Which change best addresses the classification trust problem?

- **A.** Trust the IP address alone and retain every supplied DSCP unchanged.
- **B.** Make the voice queue larger while trusting every host unchanged.
- **C.** Validate or reclassify traffic at the appropriate trust boundary before accepting priority markings.
- **D.** Advertise a different default gateway through DHCP without changing policy.

**Answer: C**

A QoS label is an input whose trustworthiness depends on where it was set. Policy should distinguish trusted marking sources from hosts that can freely choose their own values.

**Option explanations**

- **A:** The stated problem is accepting an endpoint-controlled priority label without validating the traffic class.
- **B:** This does not stop unauthorized classification into that queue.
- **C:** An endpoint-controlled label should not alone authorize privileged treatment.
- **D:** Moving the next hop does not correct the stated trust decision.

**Further reading**

- [RFC 2475 — An Architecture for Differentiated Services](https://www.rfc-editor.org/rfc/rfc2475.html) — 2.3 Traffic classification and conditioning; 2.4 Per-hop behaviors
- [Quality of Service Configuration Guide — Quality of service](https://www.cisco.com/c/en/us/td/docs/switches/lan/c9000/qos/quality-of-service-configuration-guide/m-quality-of-service.html) — Classification; marking; queuing and scheduling; policing and shaping

---

## CCNA7-074 · IP Services

Objectives: 4.8 · single · Applied

From an IOS XE router with SSH client support, an administrator needs to open an SSH session to 10.74.0.20 as user netops. The destination accepts password authentication. Which privileged EXEC command initiates that client connection?

- **A.** username netops secret 10.74.0.20
- **B.** ssh -l netops 10.74.0.20
- **C.** telnet 10.74.0.20 22
- **D.** ip ssh version 2

**Answer: B**

An SSH client command initiates a session to the remote server. Local server configuration commands and merely connecting a terminal stream to TCP 22 are not equivalent operations.

**Option explanations**

- **A:** This is local account configuration, not a remote connection command.
- **B:** The -l option supplies the remote username for the SSH client.
- **C:** Opening a raw Telnet-style TCP session to port 22 does not negotiate SSH.
- **D:** This configures SSH version behavior; it does not open the requested remote session.

**Further reading**

- [Configure SSH on Routers](https://www.cisco.com/c/en/us/support/docs/security-vpn/secure-shell-ssh/4145-ssh.html) — SSH server prerequisites; SSHv2; VTY restrictions; show commands
- [Secure Shell Configuration Guide, Cisco IOS XE Release 2 — Secure Shell Version 2 Support](https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/sec_usr_ssh/configuration/xe-2/sec-usr-ssh-xe-2-book/sec-secure-shell-v2.html) — SSH client example: ssh -l username destination

---

## CCNA7-075 · IP Services

Objectives: 4.9 · single · Applied

A TFTP read request reaches a server, which returns an ERROR message saying "File not found." What is the most appropriate next check?

- **A.** Verify the requested filename and its availability in the server's permitted file area.
- **B.** Assume that no IP packets can pass between client and server.
- **C.** Generate an SSH host key on the TFTP server to authenticate the read.
- **D.** Increase the client's NTP stratum to make the file visible.

**Answer: A**

The explicit error narrows the issue from general reachability to the requested file operation. TFTP does not provide a directory-listing command to discover filenames, so check the intended path and server configuration.

**Option explanations**

- **A:** The server has responded with an application-level file lookup failure.
- **B:** The returned error already demonstrates some two-way packet exchange.
- **C:** Base TFTP does not use SSH host-key authentication.
- **D:** Time-source hierarchy does not resolve a missing requested file.

**Further reading**

- [RFC 1350 — The TFTP Protocol (Revision 2)](https://www.rfc-editor.org/info/rfc1350/) — 2 Protocol overview; 3 Relation to other protocols; 4 Initial connection; 6 Normal termination

---

## CCNA7-076 · Security Fundamentals

Objectives: 5.1 · single · Applied

A vulnerability scanner reports a potentially affected software version. A separate packet capture shows an attacker’s exploit attempt, but no execution result is available. Which conclusion best respects the evidence?

- **A.** There is a reported weakness and an observed attempt; successful compromise is not yet established.
- **B.** The absence of a captured result proves exploitation is impossible.
- **C.** The scanner report proves the attacker obtained administrator privileges.
- **D.** The exploit attempt proves the target is fully patched.

**Answer: A**

Keep vulnerability identification, exploit observation, and verified consequence separate. Further evidence is needed to determine the attempt’s actual outcome.

**Option explanations**

- **A:** Neither version detection nor an attack packet alone proves execution succeeded.
- **B:** Missing outcome evidence is not a proof of impossibility.
- **C:** Version-based findings do not demonstrate that outcome.
- **D:** Attack traffic does not establish the target’s patch state.

**Further reading**

- [RFC 4949: Internet Security Glossary, Version 2](https://www.rfc-editor.org/rfc/rfc4949.html) — Section 2: threat, vulnerability, exploit, and countermeasure

---

## CCNA7-077 · Security Fundamentals

Objectives: 5.2 · single · Applied

A company records excellent completion rates for awareness videos, but employees cannot identify the correct incident-reporting channel in a follow-up exercise. Which evidence should drive the program’s next improvement?

- **A.** The cost of the awareness platform alone.
- **B.** The number of pages in the training handout alone.
- **C.** The completion percentage alone, which proves the required behavior.
- **D.** The demonstrated inability to use the reporting process.

**Answer: D**

Assess whether users can perform the expected action. Use the exercise finding to improve the instruction and retest the reporting workflow.

**Option explanations**

- **A:** Purchase cost does not demonstrate that the learning objective was achieved.
- **B:** Document length does not measure the target behavior.
- **C:** Attendance or completion does not establish correct action under a scenario.
- **D:** Observed behavior reveals a practical gap despite course completion.

**Further reading**

- [NIST SP 800-53 Rev. 5: Security and Privacy Controls for Information Systems and Organizations](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-53r5.pdf) — AT-2, AT-3, PE-2, and PE-3: awareness, training, and physical access

---

## CCNA7-078 · Security Fundamentals

Objectives: 5.3 · single · Applied

AAA is disabled. A router’s console has a local user database and login local, but an engineer edits only the password under line console 0. Which outcome is expected for the next local-account login?

```text
username ops secret ExistingLocal!
line console 0
 password NewLineOnly!
 login local
```

- **A.** The existing username secret remains the relevant credential.
- **B.** The router prompts for both the local secret and the line password.
- **C.** The line password becomes an enable secret automatically.
- **D.** The new line password replaces every local user’s secret.

**Answer: A**

Change the credential actually selected by the authentication configuration. A password command in an unused credential path does not update a username secret.

**Option explanations**

- **A:** login local continues to select the local database rather than the line password.
- **B:** This configuration does not chain the two authentication sources.
- **C:** The line password and privileged EXEC secret are separate commands.
- **D:** Editing a line credential does not alter username entries.

**Further reading**

- [Catalyst 3750-X and 3560-X Configuration Guide: Configuring Switch-Based Authentication](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst3750x_3560x/software/release/15-0_2_se/configuration/guide/3750x_cg/swauthen.html) — Protecting Access to Privileged EXEC Commands; Configuring Username and Password Pairs

---

## CCNA7-079 · Security Fundamentals

Objectives: 5.4 · single · Applied

An engineer’s browser can download a public user certificate from a directory. The corresponding private key is held in a hardware token that the engineer does not possess. What can the downloaded certificate alone demonstrate at login?

- **A.** It proves the user’s control of the private key merely because the browser saved the certificate file.
- **B.** It supplies a biometric factor because certificates identify people.
- **C.** It can present a public identity binding but cannot prove possession of the missing private key.
- **D.** It authenticates the engineer as that user because the file has the user’s name.

**Answer: C**

Certificate-based authentication must verify more than possession of a copyable public document. The protocol needs proof tied to the corresponding private key.

**Option explanations**

- **A:** Saving public information is not a proof operation using the corresponding private key.
- **B:** An identity label is not measurement of a biological trait.
- **C:** The certificate is public information; proof requires the corresponding private credential.
- **D:** A named public certificate can be copied by someone else.

**Further reading**

- [NIST SP 800-63B-4: Digital Identity Guidelines — Authentication and Authenticator Management](https://pages.nist.gov/800-63-4/sp800-63b.html) — Authentication factors; password verifiers; authenticator management

---

## CCNA7-080 · Security Fundamentals

Objectives: 5.5 · single · Applied

A remote-access client sends selected corporate traffic through IPsec to headquarters. Headquarters then forwards the decrypted traffic over an internal LAN without additional encryption. Where does this VPN’s confidentiality protection end?

- **A.** Nowhere, because once encrypted a packet cannot be decrypted for forwarding.
- **B.** Only when the application process exits on the destination server.
- **C.** At the hotel access point before the packet reaches the Internet.
- **D.** At the headquarters VPN termination point.

**Answer: D**

A tunnel protects the path between its actual cryptographic endpoints. Evaluate local segments after tunnel termination separately.

**Option explanations**

- **A:** The authorized termination point decrypts protected traffic.
- **B:** The gateway tunnel does not inherently extend into the application process.
- **C:** The remote-access tunnel continues to its configured VPN peer.
- **D:** Traffic after decryption is outside this IPsec tunnel unless another protection applies.

**Further reading**

- [RFC 4301: Security Architecture for the Internet Protocol](https://www.rfc-editor.org/rfc/rfc4301.html) — Sections 3, 4.1, 4.4.1: IPsec services, tunnel mode, and security policy

---

## CCNA7-081 · Security Fundamentals

Objectives: 5.6 · single · Applied

An outbound ACL on a branch uplink must allow DNS queries from 10.77.0.0/24 only to resolver 192.0.2.53. The tested queries use UDP destination port 53. Which entry meets this stated flow requirement without permitting queries to any resolver?

- **A.** permit udp host 192.0.2.53 eq 53 10.77.0.0 0.0.0.255
- **B.** permit tcp 10.77.0.0 0.0.0.255 host 192.0.2.53 eq 53
- **C.** permit udp 10.77.0.0 0.0.0.255 any eq 53
- **D.** permit udp 10.77.0.0 0.0.0.255 host 192.0.2.53 eq 53

**Answer: D**

An ACL should express the required packet direction and all relevant selectors. DNS can also use TCP, but this question’s defined flow is specifically UDP queries.

**Option explanations**

- **A:** This describes the reverse reply direction.
- **B:** This does not match the UDP queries specified in the test.
- **C:** This admits DNS queries to every destination address.
- **D:** The source range, destination resolver, protocol, and destination port are constrained.

**Further reading**

- [Configure IP Access Lists](https://www.cisco.com/c/en/us/support/docs/security/ios-firewall/23602-confaccesslists.html) — ACL Concepts; Masks; Process ACLs; Apply ACLs; Extended ACLs

---

## CCNA7-082 · Security Fundamentals

Objectives: 5.7 · single · Applied

A Catalyst access port uses dynamic secure MAC learning with maximum 1 and no aging. The approved laptop disconnects and a different laptop connects later. The original dynamic secure entry is still present. What explains the new laptop’s violation?

- **A.** The switch must automatically replace the secure entry whenever the link reconnects.
- **B.** DHCP must assign the new laptop the same IP before port security accepts any MAC.
- **C.** The maximum applies only while both laptops transmit simultaneously.
- **D.** The secure entry has not aged or been cleared, so the address allowance is still occupied.

**Answer: D**

Read the actual secure-address state rather than assuming a physical move cleared it. An approved replacement needs the stale binding removed or an appropriate aging policy.

**Option explanations**

- **A:** The premise explicitly says the old entry remains present.
- **B:** Port security is enforcing the secure source MAC, not DHCP address reuse.
- **C:** The maximum counts retained secure addresses, not just simultaneous senders.
- **D:** Physical disconnection does not satisfy the stated requirement to remove this retained secure entry.

**Further reading**

- [Catalyst 3750-X and 3560-X Configuration Guide: Configuring Port-Based Traffic Control](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst3750x_3560x/software/release/15-0_2_se/configuration/guide/3750x_cg/swtrafc.html) — Secure MAC Addresses; Security Violations; Port Security Aging

---

## CCNA7-083 · Security Fundamentals

Objectives: 5.8 · single · Applied

A router accepts a user’s correct credentials and assigns a role permitting monitoring commands. An accounting collector is unavailable. Which statement correctly separates these functions?

- **A.** Monitoring permissions automatically repair the accounting path.
- **B.** A missing collector necessarily means the password was incorrect.
- **C.** Accounting delivery proves command authorization even when no policy is configured.
- **D.** Successful access decisions do not prove that the session’s records reached the collector.

**Answer: D**

Verify access control and evidence collection independently. Whether collector failure blocks access depends on the configured policy, which is not specified here.

**Option explanations**

- **A:** Authorization policy does not establish collector reachability.
- **B:** The premise states authentication succeeded; record delivery is a different stage.
- **C:** Recording and permission enforcement are distinct functions.
- **D:** Accounting delivery can fail independently of identity and permission checks.

**Further reading**

- [RFC 8907: The Terminal Access Controller Access-Control System Plus (TACACS+) Protocol](https://www.rfc-editor.org/rfc/rfc8907.html) — Sections 5, 6, and 7: authentication, authorization, and accounting

---

## CCNA7-084 · Security Fundamentals

Objectives: 5.9 · multiple · Applied

A WLAN engineer enables WPA2/WPA3-Personal transition mode to accommodate older clients. Which two client outcomes are consistent with that mode when all other settings are compatible? Select two.

- **A.** A WPA2-Personal client can use the PSK path.
- **B.** All clients must authenticate against an enterprise RADIUS server.
- **C.** Every connected client thereby uses SAE, including clients that do not implement it.
- **D.** A WPA3-capable client can use SAE.

**Answer: A, D**

Transition mode permits a mixed client population. It does not turn a WPA2 connection into a WPA3 SAE connection merely because both use the same WLAN.

**Option explanations**

- **A:** Backward-compatible personal authentication is the purpose of transition mode.
- **B:** Personal transition mode does not require enterprise 802.1X authentication.
- **C:** Compatibility mode does not add missing protocol support to an old client.
- **D:** Transition mode includes the WPA3-Personal authentication path.

**Further reading**

- [Cisco Catalyst 9800 Configuration Guide, IOS XE 17.3.x: Wi-Fi Protected Access 3](https://www.cisco.com/c/en/us/td/docs/wireless/controller/9800/17-3/config-guide/b_wl_17_3_cg/m_wpa3.html) — WPA3-Personal; WPA3-Personal Transition Mode; Protected Management Frames

---

## CCNA7-085 · Security Fundamentals

Objectives: 5.10 · single · Applied

The WLAN GUI has WPA2-AES and PSK selected, but the client profile is configured for WPA2-Enterprise and asks for a username. The intended deployment is shared-passphrase authentication. Which adjustment aligns the client with the WLAN?

- **A.** Keep Enterprise and enter the PSK as the username.
- **B.** Configure the client for WPA2-Personal and the WLAN’s approved PSK.
- **C.** Disable AES on the WLAN but retain the client’s Enterprise mode.
- **D.** Change only the client’s IP prefix length.

**Answer: B**

Cipher agreement alone does not ensure compatibility. The WLAN and client must also agree on PSK versus enterprise authentication.

**Option explanations**

- **A:** A username field does not convert 802.1X into PSK authentication.
- **B:** The client must use the same authentication model as the intended WLAN.
- **C:** Changing the cipher does not fix the key-management mismatch.
- **D:** IP addressing does not change WLAN authentication negotiation.

**Further reading**

- [Cisco Wireless Controller Configuration Guide, Release 8.10: WLAN Security](https://www.cisco.com/c/en/us/td/docs/wireless/controller/8-10/config-guide/b_cg810/wlan_security.html) — WPA1+WPA2; Configuring WPA1+WPA2 (GUI); Protected Management Frames

---

## CCNA7-086 · Security Fundamentals

Objectives: 5.6 · single · Applied

A router permits an application’s IPv4 traffic through an interface ACL. An engineer asks whether this also authorizes the same application’s IPv6 traffic on a dual-stack interface. Which answer is correct?

- **A.** Yes; IPv6 addresses are always converted to IPv4 before interface ACL evaluation.
- **B.** No; IPv6 filtering uses its own applicable IPv6 policy and attachment.
- **C.** Yes; the application name automatically applies the IPv4 ACL to both IP versions.
- **D.** No; IPv6 cannot be filtered on a routed interface.

**Answer: B**

Verify policy coverage for each address family present on a path. An IPv4 permit or deny is not evidence of the IPv6 interface’s effective filtering.

**Option explanations**

- **A:** Dual-stack operation does not inherently translate IPv6 into IPv4.
- **B:** An IPv4 ACL’s entries do not match IPv6 packets.
- **C:** An application label does not change the ACL address family.
- **D:** IPv6 traffic filtering is supported using the appropriate mechanism.

**Further reading**

- [Security and VPN Configuration Guide, Cisco IOS XE 17.x: IPv6 Access Control Lists](https://www.cisco.com/c/en/us/td/docs/routers/ios/config/17-x/sec-vpn/b-security-vpn/m_ip6-acls-xe.html) — Access Control Lists for IPv6 Traffic Filtering; Applying the IPv6 ACL to an Interface

---

## CCNA7-087 · Security Fundamentals

Objectives: 5.6 · multiple · Applied

An ACL entry is permit tcp host 10.7.1.4 host 192.0.2.14 range 8000 8003. Which two destination ports match the range operator? Select two.

- **A.** 8000
- **B.** 8003
- **C.** 7999
- **D.** 8004

**Answer: A, B**

The TCP port range is inclusive of both endpoints. Because the operator follows the destination address, it tests destination ports.

**Option explanations**

- **A:** The lower bound is included.
- **B:** The upper bound is included.
- **C:** This is below the configured lower bound.
- **D:** This is above the configured upper bound.

**Further reading**

- [Configure IP Access Lists](https://www.cisco.com/c/en/us/support/docs/security/ios-firewall/23602-confaccesslists.html) — ACL Concepts; Masks; Process ACLs; Apply ACLs; Extended ACLs

---

## CCNA7-088 · Security Fundamentals

Objectives: 5.7 · single · Applied

DHCP snooping correctly blocks rogue DHCP server replies on user ports. A malicious host instead sends forged ARP replies claiming the gateway’s IP. Which additional feature directly validates those ARP claims?

- **A.** DHCP snooping trust on every user port.
- **B.** Dynamic ARP inspection using authorized bindings or ARP ACLs.
- **C.** Sticky port security with an unlimited source population.
- **D.** A longer DHCP snooping lease database timeout alone.

**Answer: B**

Protocol-specific protections must cover the actual attack. DHCP snooping can supply bindings, but DAI must be configured to use the relevant authorization information for ARP.

**Option explanations**

- **A:** This weakens DHCP filtering and does not enable ARP validation.
- **B:** DAI examines the address claims carried by ARP.
- **C:** A MAC-count policy is not an IP-to-MAC ARP validation mechanism.
- **D:** Retaining DHCP bindings alone does not enable ARP inspection.

**Further reading**

- [Catalyst 3750-X and 3560-X Configuration Guide: Configuring DHCP Features and IP Source Guard](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst3750x_3560x/software/release/15-0_2_se/configuration/guide/3750x_cg/swdhcp82.html) — DHCP Snooping; DHCP Snooping Binding Database; Enabling DHCP Snooping
- [Catalyst 3750-X and 3560-X Configuration Guide: Configuring Dynamic ARP Inspection](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst3750x_3560x/software/release/15-0_2_se/configuration/guide/3750x_cg/swdynarp.html) — Understanding Dynamic ARP Inspection; Rate Limiting; ARP ACLs

---

## CCNA7-089 · Security Fundamentals

Objectives: 5.7 · single · Applied

An untrusted user port has DAI enabled through its VLAN. A legitimate DHCP client’s binding is present, but its ARP packets exceed the configured rate limit. Which statement is accurate?

- **A.** DAI rate limits are automatically equal to the client’s DHCP lease duration.
- **B.** Rate limits apply only to invalid ARP mappings.
- **C.** A valid mapping does not exempt the traffic from DAI rate-limit enforcement.
- **D.** A matching binding makes the interface permanently trusted.

**Answer: C**

A packet stream may be legitimate in its sender mapping yet violate a rate policy. Investigate the burst and size limits for the approved use rather than assuming binding validity bypasses every check.

**Option explanations**

- **A:** A lease duration is not an ARP packet-rate setting.
- **B:** DAI rate limits consider incoming ARP volume independently of individual legitimacy.
- **C:** Mapping validation and rate limits are separate checks.
- **D:** A valid packet does not change interface trust configuration.

**Further reading**

- [Catalyst 3750-X and 3560-X Configuration Guide: Configuring Dynamic ARP Inspection](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst3750x_3560x/software/release/15-0_2_se/configuration/guide/3750x_cg/swdynarp.html) — Understanding Dynamic ARP Inspection; Rate Limiting; ARP ACLs

---

## CCNA7-090 · Security Fundamentals

Objectives: 5.3 · single · Applied

An administrator adds a replacement local account while keeping a known-working console session open. Which verification should occur before the obsolete account is removed?

- **A.** Only confirm that the current already-authenticated session remains open.
- **B.** Test a new login with the replacement account through the intended management path.
- **C.** Only confirm that the replacement username appears in a banner.
- **D.** Only ping the device from the administrator’s workstation.

**Answer: B**

Credential maintenance should verify a new session, because an existing session can survive a broken future login configuration. Then retire obsolete access and save the intended state.

**Option explanations**

- **A:** An existing session does not exercise the new login credential.
- **B:** A fresh authentication exchange tests the new credential and the selected line policy.
- **C:** Banner text is not an active local account or authentication test.
- **D:** IP reachability does not establish successful account authentication.

**Further reading**

- [Catalyst 3750-X and 3560-X Configuration Guide: Configuring Switch-Based Authentication](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst3750x_3560x/software/release/15-0_2_se/configuration/guide/3750x_cg/swauthen.html) — Protecting Access to Privileged EXEC Commands; Configuring Username and Password Pairs
- [Security and VPN Configuration Guide, Cisco IOS XE 17.x: Configuring Security with Passwords, Privileges, and Logins](https://www.cisco.com/c/en/us/td/docs/routers/ios/config/17-x/sec-vpn/b-security-vpn/m_sec-cfg-sec-4cli-0.html) — Protecting Access to User EXEC Mode; Password Encryption Levels; Password Change Verification

---

## CCNA7-091 · Automation and Programmability

Objectives: 6.1 · single · Applied

A team can deploy a new standard to all branch routers at once or to a small representative group first. Both use the same automation and approved inputs. Why might the team choose the smaller initial rollout?

- **A.** It reduces the number of devices exposed before the resulting behavior is checked
- **B.** It proves the template cannot contain any error
- **C.** It prevents all differences between hardware platforms
- **D.** It removes the need to verify the later full rollout

**Answer: A**

Automation can change many devices quickly, so rollout scope is an operational control. A representative initial group supplies evidence before the same change reaches the remainder.

**Option explanations**

- **A:** A limited first deployment can reveal problems before expanding the scope.
- **B:** A limited rollout reduces initial exposure but does not prove perfect input.
- **C:** Selecting fewer devices does not remove platform differences.
- **D:** Later targets and operating conditions still need verification.

**Further reading**

- [What Is Network Automation?](https://www.cisco.com/site/us/en/learn/topics/networking/what-is-network-automation.html) — Network automation; profiles and policies; automated lifecycle management

---

## CCNA7-092 · Automation and Programmability

Objectives: 6.2 · single · Applied

A business application must request supported network services without knowing the CLI syntax of each switch platform. Which controller-based capability most directly meets that requirement?

- **A.** A separate terminal session from the application to every switch
- **B.** A requirement to make every switch the same physical model
- **C.** A controller API that abstracts supported network operations
- **D.** A static MAC address table embedded in the application

**Answer: C**

Controller abstraction can reduce the platform details an application must understand. This benefit applies to operations and devices supported by the controller’s service model.

**Option explanations**

- **A:** This would retain direct device-specific interaction.
- **B:** Homogeneous hardware is not the service abstraction being requested.
- **C:** The application requests the service while the controller handles supported infrastructure details.
- **D:** A MAC table is not a general network-service management interface.

**Further reading**

- [Software-Defined Networking (SDN) Definition](https://www.cisco.com/c/en/us/solutions/software-defined-networking/overview.html) — SDN elements; Features and benefits
- [RFC 7426: Software-Defined Networking (SDN): Layers and Architecture Terminology](https://www.rfc-editor.org/rfc/rfc7426.html) — 3.1 Overview; 3.2 Network Devices; 3.3 Control Plane; 3.5.3 Locality

---

## CCNA7-093 · Automation and Programmability

Objectives: 6.3 · multiple · Challenge

A fabric carries Research and Guest as distinct virtual networks over the same routed transport. No inter-virtual-network routing is configured. Which two statements correctly describe this design? Select two.

- **A.** Sharing an underlay automatically merges the two virtual networks
- **B.** The logical virtual networks can remain separated while sharing transport
- **C.** Research must have a dedicated cable on every underlay hop
- **D.** The underlay has become a northbound API
- **E.** A common underlay failure can affect both virtual networks

**Answer: B, E**

Overlays can provide separate logical networks on shared transport. That separation does not remove shared physical dependencies or automatically establish communication between the overlays.

**Option explanations**

- **A:** A common transport does not by itself merge overlay forwarding contexts.
- **B:** Overlay separation and physical transport sharing are compatible.
- **C:** The overlay does not require a separate physical path for every virtual network.
- **D:** The underlay remains the physical routed transport.
- **E:** Logical separation does not create independent physical infrastructure.

**Further reading**

- [Software-Defined Access](https://www.cisco.com/c/en/us/td/docs/solutions/CVD/Campus/cisco-sda-design-guide.html) — SD-Access architecture; Underlay network; Overlay network; Overlay control plane – LISP; Data plane – VXLAN

---

## CCNA7-094 · Automation and Programmability

Objectives: 6.4 · single · Applied

A troubleshooting assistant rewrites supplied event records into a plain-language explanation. The workflow does not estimate a future event probability. Which capability is central to the described task?

- **A.** A routing protocol choosing the shortest path
- **B.** Generative AI producing explanatory content
- **C.** Predictive forecasting of a future utilization value
- **D.** A mandatory replacement of network telemetry with synthetic events

**Answer: B**

Generative AI can turn incident context into explanatory text. The described task concerns content generation, whereas estimating a future network outcome would be predictive.

**Option explanations**

- **A:** The task is language generation from supplied information.
- **B:** Creating a natural-language explanation is a generative use case.
- **C:** No future estimate is part of the described output.
- **D:** The task uses supplied records; it does not require replacing observations.

**Further reading**

- [How To Get Started Using LLMs in IT and Network Engineering](https://blogs.cisco.com/developer/how-to-get-started-using-llms-in-it-and-network-engineering) — Introducing the LLM; Applying LLMs to IT and Network Engineering Use Cases

---

## CCNA7-095 · Automation and Programmability

Objectives: 6.5 · single · Applied

A REST-style API requires every protected request to carry the information needed to identify its resource and authenticate the client. The client cannot rely on an earlier “select device” interaction being remembered. Which characteristic does this illustrate?

- **A.** All resources must be deleted when a request ends
- **B.** The server cannot store configurations or an inventory database
- **C.** HTTP transport must use a new physical link for every request
- **D.** Requests are self-contained with respect to client session context

**Answer: D**

REST’s stateless constraint concerns the information needed to understand each client request. It does not mean that managed resources, databases or all server-side data cease to exist between requests.

**Option explanations**

- **A:** Stateless interactions do not require deletion of persistent resources.
- **B:** Resource state can persist even when request processing is stateless.
- **C:** Statelessness does not impose that physical transport requirement.
- **D:** The server need not remember a previous conversational selection to interpret the request.

**Further reading**

- [Architectural Styles and the Design of Network-based Software Architectures, Chapter 5: Representational State Transfer](https://ics.uci.edu/~fielding/pubs/dissertation/rest_arch_style.htm) — 5.1.3 Stateless; 5.1.5 Uniform Interface

---

## CCNA7-096 · Automation and Programmability

Objectives: 6.5 · single · Challenge

An API documents DELETE /vlans/71 as removing that resource. The first request returns 204 after removal; the identical second request returns 404 because it is absent. Which statement about idempotency is correct?

- **A.** Different response codes prove the operation is not idempotent
- **B.** DELETE becomes Create when repeated against an absent resource
- **C.** The final intended resource state can be the same after one or two requests
- **D.** A 404 response restores the deleted object automatically

**Answer: C**

An idempotent method has the same intended effect when repeated as when performed once. The responses can differ because the resource was present for the first request and absent for the second.

**Option explanations**

- **A:** Idempotency concerns intended server effect, not identical responses.
- **B:** The method does not change its meaning on repetition.
- **C:** The resource is absent in either case, despite different response codes.
- **D:** A not-found response does not recreate the resource.

**Further reading**

- [RFC 9110: HTTP Semantics](https://www.rfc-editor.org/rfc/rfc9110.html) — 9 Methods; 15 Status Codes

---

## CCNA7-097 · Automation and Programmability

Objectives: 6.6 · single · Applied

An Ansible inventory groups switches by both location and function. A switch belongs to munich and distribution. Which statement about this inventory organization is valid?

- **A.** A managed host can belong to multiple groups
- **B.** The host is automatically configured twice in every play
- **C.** The switch must have two management IP addresses
- **D.** Location groups can contain only physical servers

**Answer: A**

Ansible inventory can represent multiple group memberships for a host. The groups describe targeting and variable organization; they do not themselves create extra devices or configuration operations.

**Option explanations**

- **A:** Multiple group memberships allow the same host to be selected along different operational dimensions.
- **B:** Group membership alone does not specify a play’s execution.
- **C:** Inventory group membership does not require multiple management interfaces.
- **D:** Groups can organize supported managed hosts, including network devices.

**Further reading**

- [How to build your inventory](https://docs.ansible.com/projects/ansible/latest/inventory_guide/intro_inventory.html) — Inventory basics: formats, hosts, and groups; Inventory setup examples

---

## CCNA7-098 · Automation and Programmability

Objectives: 6.6 · single · Applied

A Terraform subnet resource refers to the ID of a virtual network declared in the same configuration. The network must exist before the subnet can be created. Which capability can use that reference to order provisioning?

- **A.** Alphabetical ordering of the filenames
- **B.** Terraform’s resource dependency graph
- **C.** The virtual network’s Spanning Tree Protocol root election
- **D.** An HTTP Accept header listing the network first

**Answer: B**

Terraform builds relationships between declared resources, including dependencies implied by references. It can therefore create the required network before a subnet that depends on its ID.

**Option explanations**

- **A:** Filename order is not the dependency model.
- **B:** A reference can express a dependency that informs operation ordering.
- **C:** STP is unrelated to ordering API resource creation.
- **D:** Response format preferences do not define Terraform dependencies.

**Further reading**

- [What is Terraform?](https://developer.hashicorp.com/terraform/intro) — How does Terraform work?; Manage any infrastructure; Track your infrastructure

---

## CCNA7-099 · Automation and Programmability

Objectives: 6.7 · single · Applied

The JSON shown is a valid payload. A developer claims the active member contains a Boolean because its text reads false. What is the correct interpretation?

```text
{"active":"false","verified":false}
```

- **A.** active is a Boolean because the letters spell false
- **B.** Both members contain JSON null values
- **C.** The entire payload is invalid because Boolean words cannot be quoted
- **D.** active is a string; verified is a Boolean

**Answer: D**

Value type follows JSON syntax, not the everyday meaning of quoted text. A client must not treat a quoted false as a Boolean unless an additional application rule explicitly converts it.

**Option explanations**

- **A:** Quotation marks make this value a string.
- **B:** Neither value uses the null literal.
- **C:** Quoted text containing false is a valid string.
- **D:** Only verified uses the unquoted Boolean literal.

**Further reading**

- [RFC 8259: The JavaScript Object Notation (JSON) Data Interchange Format](https://www.rfc-editor.org/rfc/rfc8259.html) — 2 JSON Grammar; 3 Values; 4 Objects; 5 Arrays; 6 Numbers; 7 Strings

---

## CCNA7-100 · Automation and Programmability

Objectives: 6.7 · single · Challenge

An API contract requires unique member names. A device record violates that rule as shown. Why should the producer fix the record rather than rely on clients agreeing?

```text
{"name":"core-a","name":"core-b","site":"campus"}
```

- **A.** JSON requires every object to contain exactly one member
- **B.** The two name members are automatically combined into an array
- **C.** Duplicate member names can be handled differently by parsers
- **D.** The second name is automatically interpreted as an HTTP header

**Answer: C**

Duplicate names create interoperability problems, and this API explicitly forbids them. A producer should emit a single unambiguous value rather than depend on a particular parser’s duplicate-handling behavior.

**Option explanations**

- **A:** Objects can contain several members.
- **B:** JSON does not define that automatic conversion.
- **C:** Implementations may keep different values, reject duplicates or expose them differently.
- **D:** Object members do not become HTTP headers automatically.

**Further reading**

- [RFC 8259: The JavaScript Object Notation (JSON) Data Interchange Format](https://www.rfc-editor.org/rfc/rfc8259.html) — 2 JSON Grammar; 3 Values; 4 Objects; 5 Arrays; 6 Numbers; 7 Strings

---
