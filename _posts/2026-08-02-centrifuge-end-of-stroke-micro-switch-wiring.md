---
title: "Centrifuge End of Stroke Micro Switch Wiring: What the Contacts Show"
description: "centrifuge end of stroke micro switch wiring: Understand the operating idea, essential terminology, practical checks, limitations, and evidence needed for."
date: 2026-08-02 11:37:22 +0800
sitemap_omit_lastmod: true
category: Applications
tags:
  - centrifuge end of stroke micro switch wiring
  - micro switches
  - Applications
author: editorial_team
---

A centrifuge end of stroke micro switch wiring diagram can explain how a documented switch contact connects to the machine’s circuit, but it cannot establish the control behavior by itself. The interpretation depends on the exact switch’s contact diagram and the centrifuge circuit documentation. Only centrifuge designs documented to use a micro switch are covered here; the presence and function of one cannot be assumed for every centrifuge.

The useful way to trace the signal is to follow the physical movement to the actuator, then the contact change, and finally the circuit response. Each link depends on the specific design. Without matching documentation, terminal connections and the machine’s response remain unresolved.

## What centrifuge end of stroke micro switch wiring can, and cannot, tell you

Wiring information has two distinct parts: the switch’s documented contact arrangement and the centrifuge’s documented circuit. The switch diagram identifies its terminals and contact relationships under a stated reference condition. The machine diagram shows how those terminals are connected into a particular control circuit. Neither document should be substituted for the other.

A switch-level diagram may show how a contact changes state when its actuator moves. It does not, on its own, say whether the centrifuge stops, signals an alarm, changes another control state, or performs some other function. That effect depends on the actual circuit and the design of the equipment. Do not infer it solely from the switch’s location or from a terminal label.

Likewise, a physical arrangement that resembles a familiar terminal pattern is not evidence of terminal identity. Use the connection diagram, terminal marking, circuit function, and permissible load documented for the exact switch and equipment. If those details are missing or do not match, the wiring interpretation is not established.

This boundary matters because a switch is one component in a larger system. The actuator’s movement and the switch’s contact state describe component-level events. The centrifuge’s response is a system-level result. A diagram or observation must support each step before drawing a conclusion about the whole machine.

## How end-position motion reaches the micro switch contacts

In a centrifuge design that documents a micro switch for end-position sensing, the mechanical sequence begins when a moving part or linkage reaches the relevant position. That movement may act on the switch’s actuator. If the actuator moves through the switch’s operating motion, the contacts can change state according to the documented contact arrangement. This is a conditional description, not a claim about how every centrifuge is built.

The contact change becomes a signal to the machine only through the connected circuit. The circuit determines what that electrical change means in the equipment. The switch alone does not establish whether the machine treats the signal as an end-of-motion indication, a stop command, an alarm input, an interlock, or something else. Those functions must be established from the centrifuge’s own documentation.

The actuator’s travel terminology can help describe the mechanical sequence when applicable documentation uses it. Under MIL-PRF-8805K sections 6.5.14 and 6.5.16, pretravel runs from the free position to the operating position, while overtravel runs from the operating position to the extreme permitted actuator position. These definitions describe travel points; they do not identify a centrifuge’s end position or prove that a particular actuator has reached it.

A physical movement that appears to reach an endpoint therefore does not, by itself, prove that the actuator operated, that the contacts changed as expected, or that the control circuit received or acted on a signal. Those are separate links in the chain. The documented mechanism, contact arrangement, and circuit are needed to interpret them.

## Read terminal names from the documented reference condition

COM, NO, and NC are useful terminal names only when the exact switch’s contact arrangement and reference condition are documented. In that documentation, COM means common; NO and NC describe contact states relative to the specified reference condition. The labels do not provide a universal physical terminal layout, and they should not be treated as an unqualified promise about current flow in an installed circuit.

Before interpreting a label, identify the switch diagram and the condition it uses to describe the contacts. A statement about contact state is meaningful only with that reference condition attached. If the reference condition or arrangement is unknown, do not assign a state to a terminal based on appearance, remembered conventions, or the position of a wire.

The centrifuge circuit diagram is also necessary. It identifies how the documented switch terminals relate to the equipment circuit, but it does not authorize transferring a connection from another centrifuge or switch. Wire colors, terminal positions, and control functions remain design-specific unless the relevant documentation establishes them.

The appropriate evidence is therefore the exact switch’s connection information, its terminal markings and contact-state reference, and the centrifuge circuit documentation. The documented circuit function and permissible load also matter when interpreting whether a connection is appropriate. Without that evidence, there is no supported basis for naming a terminal to connect to a particular supply or control point.

## Separate a switch contact check from centrifuge wiring diagnosis

A continuity check, when an applicable safe procedure is available, concerns the isolated switch in a defined actuator state. The result can inform whether the switch contacts have the expected continuity for that documented state. It does not establish that the installed wiring is correct or that the centrifuge control system responds as intended. An isolated component check and an installed-circuit diagnosis answer different questions.

A click may indicate movement of a snap mechanism, but it does not prove continuity, correct terminal identification, correct wiring, or suitability for the circuit. A switch can also be only one possible point in a larger chain. The observed condition could involve actuator movement, an internal contact, terminal identification, wiring, or another part of the control system. An unspecified symptom does not distinguish among these possibilities.

Keep the evidence tied to the thing being checked. A contact observation applies to the isolated switch and defined actuator state used for that check. An installed-circuit observation applies to the circuit under its documented test conditions. Neither observation alone proves the entire assembly good or bad.

Do not infer a safe test method or make assumptions about energized equipment from these general distinctions. Follow applicable deenergization and qualification requirements. Work on undocumented or hazardous installed circuitry belongs with qualified personnel using the equipment’s applicable procedures. This article does not provide a procedure for bypassing a switch or changing centrifuge wiring.

### Related guides

- [bottling machine home position micro switch location](/guides/bottling-machine-home-position-micro-switch-location/)
- [incinerator end of stroke micro switch maintenance](/guides/incinerator-end-of-stroke-micro-switch-maintenance/)
- [rotary indexing table guard interlock micro switch location](/guides/rotary-indexing-table-guard-interlock-micro-switch-location/)
- [security barrier open position micro switch wiring](/guides/security-barrier-open-position-micro-switch-wiring/)

## Evidence needed to interpret centrifuge end of stroke micro switch wiring

A defensible interpretation requires documentation that connects the component-level and machine-level information. First, identify the exact switch’s connection diagram and terminal markings. Confirm the documented contact arrangement and the reference condition used for its state descriptions. Without these, terminal names cannot establish which contacts are open or closed in a particular actuator state.

Next, identify the centrifuge circuit diagram that corresponds to the equipment being considered. It is needed to trace the switch contacts into the control circuit and establish what that circuit is documented to do. The diagram should also support interpretation of the circuit function and permissible load. A diagram from a different design, or an assumed standard layout, cannot fill a documentation gap.

If either the switch information or the machine circuit information is absent, the connection and control effect remain unresolved. The switch may have a documented contact change, but that alone does not identify the centrifuge’s response. A physical endpoint, a click, or a familiar-looking terminal arrangement is not a substitute for the missing evidence.

In short, use the switch documentation to establish its contact arrangement and state reference, then use the matching centrifuge circuit documentation to trace the signal and its role. No terminal instruction or conclusion about machine behavior is reliable without support from the specific documented design. When that support is unavailable, leave the wiring and control effect undetermined rather than infer them.

This concludes the explanation of centrifuge end of stroke micro switch wiring.

## Sources and references

- Defense Logistics Agency ASSIST: [MIL-PRF-8805K: Switches and Switch Assemblies, Sensitive, Snap Action, General Specification For](https://quicksearch.dla.mil/qsDocDetails.aspx?ident_number=7196){: rel="nofollow noopener noreferrer" }
- Occupational Safety and Health Administration: [29 CFR 1910.333: Selection and Use of Work Practices](https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.333){: rel="nofollow noopener noreferrer" }
