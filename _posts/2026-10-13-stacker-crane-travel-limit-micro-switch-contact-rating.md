---
title: "Stacker crane travel limit micro switch contact rating: what does it mean?"
description: "stacker crane travel limit micro switch contact rating: Understand the operating idea, essential terminology, practical checks, limitations, and evidence."
date: 2026-10-13 11:27:16 +0800
category: Applications
tags:
  - stacker crane travel limit micro switch contact rating
  - micro switches
  - Applications
author: editorial_team
---

A **stacker crane travel limit micro switch contact rating** describes the electrical conditions under which the switch contacts are specified to operate; it does not, by itself, establish that the switch is suitable for every crane circuit or that the crane will stop as intended. Any rating must be read with its stated voltage, current, AC or DC supply, and load type. The switch is one component in a mechanical and electrical chain: a travel feature may move its actuator, the contacts may change state, and the crane’s particular control circuit may respond to that input.

That distinction matters because the contact rating concerns the switch, while stopping behavior depends on the equipment design and circuit. The rating cannot independently verify the control response, stopping performance, or condition of the installed assembly. The relevant evidence is the documentation for the switch and the equipment, interpreted without extending a stated rating beyond its conditions.

## What a stacker crane travel limit micro switch contact rating describes

A contact rating is a specification of electrical capability or operating conditions for the switch contacts. It is not a general capacity that follows from calling a component a micro switch, and it does not automatically describe every circuit in which that component might be used. Electrical ratings are tied to their stated load and test conditions, rather than being universal switching capacities (MIL-PRF-8805K 6.1.1 and applicable specification sheets).

When a specification gives a value, keep the conditions attached to it. Voltage and current matter, as do whether the supply is AC or DC and the type of load covered. A value without its associated conditions is incomplete evidence for interpreting a particular circuit. Likewise, a rating identified for one load category should not be treated as a rating for a different category merely because both circuits operate the same travel mechanism.

The application name does not fill in missing rating information. “Travel limit” describes a role in an equipment arrangement, not a universal electrical duty for the switch. If the applicable specification sheet does not state the conditions needed to interpret a value, those conditions remain unresolved. Do not infer a rating from the crane’s function, the switch’s physical movement, or a label that lacks the relevant electrical context.

## How a travel mechanism can use a micro switch

A travel-related mechanical feature may move a micro switch actuator when a moving part reaches a defined position. Actuator movement can cause the contacts to change state. The crane’s control circuit may then interpret that contact change as an input. This describes a possible relationship between mechanism, switch, and control system; it does not establish the arrangement or response of any particular crane.

The contact change is not proof that the switch directly interrupts motor power. A particular design may use the contact as an input to control logic, but the actual circuit and response must be established from the equipment documentation. Without that evidence, do not assume which contact state the system uses, what action follows, or whether the switch is the only element involved in limiting travel.

The movement also has design-specific limits. Pretravel runs from the actuator’s free position to its operating position, while overtravel runs from the operating position to the extreme permitted actuator position (MIL-PRF-8805K 6.5.14 and 6.5.16). These terms describe actuator travel, not crane stopping distance. Numerical travel limits are requirements of the applicable specification sheet and must not be inferred from the component category. A travel mechanism’s movement and the contact rating therefore answer different questions: one concerns mechanical actuation, and the other concerns specified electrical conditions.

## Conditions that must match before comparing a rating with the circuit

To compare a documented rating with a crane circuit, identify the conditions stated for that rating and compare them with the circuit conditions. Keep the supply type, voltage, current, and load category together. If any of those details differ or are not documented, the rating does not establish applicability to that circuit.

In particular, do not transfer an AC rating to a DC circuit, or a rating for one load type to another. A matching voltage alone is not enough to show that the documented conditions match. Nor does the fact that a contact changes state at a travel position determine the electrical load it switches. The circuit documentation must identify the relevant electrical conditions independently of the mechanical role of the switch.

The rating also does not settle the effect of the surrounding circuit arrangement. A contact may serve as an input to a control system, but its role and the system’s response depend on the specific design. Therefore, even when a contact rating appears to match stated circuit conditions, that comparison alone does not establish that the entire travel-limiting arrangement is suitable. Where the documentation leaves a condition unclear, record it as unknown rather than treating the rating as a general approval.

## What the contact rating cannot verify about crane stopping

A contact rating does not establish how far a crane travels after a contact changes state, what control logic follows, or whether the equipment will stop under a particular operating condition. It also does not establish redundancy or verify the condition of the installed assembly. These are system-level matters, not conclusions contained in a contact rating.

Keep the component and system questions separate. The rating addresses stated electrical conditions for the switch contacts. Whether the mechanical feature moves the actuator as intended, whether the contact change reaches the control input, and how the control system responds are distinct parts of the equipment arrangement. A discrepancy in any one of these areas cannot be diagnosed from the rating alone. Nor does the presence of a travel limit switch prove that another protective function exists or operates in a particular way.

For the same reason, a rating label is not evidence by itself that the crane will stop safely. It does not verify actuator alignment, wiring, the control input, or other system elements. No single component-level specification establishes the performance or condition of the complete installed arrangement. Claims about stopping behavior require evidence for the particular crane design and circuit, not an extrapolation from the switch’s contact rating.

### Related guides

- [bottling machine home position micro switch location](/guides/bottling-machine-home-position-micro-switch-location/)
- [incinerator end of stroke micro switch maintenance](/guides/incinerator-end-of-stroke-micro-switch-maintenance/)
- [rotary indexing table guard interlock micro switch location](/guides/rotary-indexing-table-guard-interlock-micro-switch-location/)
- [security barrier open position micro switch wiring](/guides/security-barrier-open-position-micro-switch-wiring/)

## What documentation to check when the rating is unclear

Use the applicable switch specification sheet to identify the contact rating and its stated electrical conditions. Use the equipment documentation to understand the intended circuit use and the role of the contact in the travel-control arrangement. The rating and the equipment description answer related but different questions: one defines the documented contact conditions, while the other describes how the host system uses the contact.

If the load type, contact arrangement, supply conditions, or system response is not stated, keep that item unresolved. Do not infer a contact arrangement or crane response from the words “travel limit,” and do not treat a switch rating as evidence that the installed equipment has been verified. Numerical travel limits likewise require the applicable specification sheet; they cannot be supplied by a generic component description.

For an installation-specific electrical assessment, qualified personnel should use the approved procedure and relevant equipment documentation. This article does not provide a wiring method, a test procedure, or a compatibility determination for a particular crane or switch. The useful decision boundary is straightforward: a documented rating can be compared only with the conditions it actually states, and it cannot by itself establish crane stopping performance. The **stacker crane travel limit micro switch contact rating** is evidence about the contact under specified conditions, not proof of the behavior or suitability of the whole system.

## Sources and references

- Defense Logistics Agency ASSIST: [MIL-PRF-8805K: Switches and Switch Assemblies, Sensitive, Snap Action, General Specification For](https://quicksearch.dla.mil/qsDocDetails.aspx?ident_number=7196){: rel="nofollow noopener noreferrer" }
