# Set 01 review notes

Review date: 2026-09-14. This is the first original practice set, authored and reviewed with AI assistance. It has not received Cisco endorsement, human instructor certification or learner-performance calibration.

## Content checks

Each domain was drafted against the v1.1 objective IDs. Authors opened the cited primary technical documents and checked supporting sections. The exam blueprint supplies the scope; technical documentation supplies answer evidence.

After drafting, a separate review pass re-solved questions and challenged distractors. Domains 1 and 4, 2 and 3, and 5 and 6 received paired independent review. The main review also checked the full bank and integrated corrections.

Specific checks included subnet boundaries and VLSM, IPv6 prefix arithmetic and EUI-64, switching behavior, native-VLAN assumptions, LACP modes, STP roles, RIB selection versus packet forwarding, recursive routes, OSPF election conditions, NAT pool exhaustion, NTP stratum, ACL ordering and direction, IPsec tunnel visibility, and controller/API boundaries.

## Corrections made

- Broadened Network Fundamentals items to assess component roles and topology types that were missing from the initial draft, within the fixed 20-question allocation.
- Replaced a weak DHCP distractor with a plausible confusion between DNS-server and search-domain options.
- Removed an inter-VLAN objective tag from an item that only assesses trunk admission.
- Removed a PSK answer cue from the wireless question's premise.
- Improved an ACL distractor to test source-versus-destination field interpretation.
- Replaced a simple VPN-benefit item with an applied ESP tunnel-mode header-visibility scenario, explicitly using TCP.
- Preserved line breaks in configuration exhibits and rendered multiline answer configurations as code blocks.
- Corrected the navigation button label to accurately describe going to the first unanswered question.

## Application checks

The pinned Streamlit 1.55.0 app was tested on Python 3.12. Automated tests cover:

- Exactly 100 unique IDs and the requested 20/20/25/10/15/10 allocation.
- Required question fields, answer references, objective-domain agreement and reading links.
- Rejection of missing, incomplete, duplicate and extra selections; all-or-nothing matching and multiple-answer scoring.
- Hidden feedback before submission and feedback for every option afterward.
- First-answer retention across navigation and disabling resubmission.
- Domain navigation, review flags, results, a completed-set score and restart.

These software checks establish app behavior. They do not independently establish technical truth. Configuration excerpts are constructed examples, and no Cisco devices or simulated labs were executed for this release.

## Scope of the pilot

The objective map records assessment tags, not mastery of every variation under an objective. A 100-question non-lab set cannot replace repeated study, hands-on configuration or future sets. Difficulty labels are editorial estimates. Once learners use the bank, incorrect-response patterns and item feedback should guide further revision.
