---
title: "Centrifuge home position micro switch wiring: how the signal path works"
description: "centrifuge home position micro switch wiring: Understand the operating idea, essential terminology, practical checks, limitations, and evidence needed for."
date: 2026-10-13 09:00:00 +0800
category: Applications
tags:
  - centrifuge home position micro switch wiring
  - micro switches
  - Applications
author: editorial_team
---

A centrifuge home position micro switch wiring arrangement, when a design uses one, carries a contact-state input from a mechanically actuated component to the centrifuge’s control circuit. The switch does not define what the centrifuge does with that input. Its contact behavior and the host system’s response are separate parts of the signal path.

This explanation applies only to centrifuge designs that use an electromechanical micro switch for a home-position signal. Other designs may use another sensing technology, and a micro switch is not synonymous with every home-position sensor. Without design-specific documentation, terminal assignments, wiring, and control behavior remain unknown.

## What centrifuge home position micro switch wiring describes

The phrase describes the electrical connection through which a micro switch may provide a home-position input. It does not, by itself, identify a particular switch, establish a terminal arrangement, or explain the centrifuge’s control logic.

In a design that uses a micro switch, the component is a small electromechanical switch operated by an external mechanism. It is distinct from the centrifuge around it and from the control system that receives its input. A different centrifuge may use another sensor or a different arrangement, so the presence and role of a micro switch must come from that design’s documentation.

The distinction matters because a wiring description can refer to different layers: the mechanism that moves the switch actuator, the switch’s documented contact behavior, the wires connected to those contacts, and the control circuit that interprets the resulting input. Evidence about one layer does not establish the details of the others. For example, knowing that a component is actuated at a mechanical home position would not, by itself, establish which contact is wired to the control input or what response the controller produces.

Accordingly, there is no universal centrifuge home-position wiring diagram, wire color, or terminal assignment to infer from the application name alone. A specific arrangement requires documentation for the particular switch and centrifuge design. The explanation below follows the conditional signal path without assigning undocumented terminals or system behavior.

## Follow the home-position signal from mechanism to control input

The signal path begins with a mechanical relationship. A target, linkage, or other part of a particular design may move the micro switch’s actuator when the mechanism reaches a defined position. The actuator’s movement can cause the switch’s documented contacts to change state. Wiring then carries that contact state to a control input, where the centrifuge’s control circuit interprets it according to the system design.

These are connected steps, but they are not interchangeable. The mechanism provides motion; the switch changes contact state; the wiring conveys an electrical condition; and the controller applies its own logic. A description of the switch alone cannot establish whether the centrifuge stops, continues, signals an operator, permits another action, or responds in some other way. Those outcomes depend on the documented circuit and control logic.

The switch’s home-position role is therefore conditional, not a general property of every centrifuge. Even when a switch is used, the relationship between the mechanism and the actuator must be established for that design. The name “home position” does not tell you whether the actuator is pressed or released at that point, nor does it establish which contact state the control input receives.

A useful wiring description keeps each link explicit: what mechanical part actuates the switch, which documented contacts are connected, what actuator condition defines the stated contact state, and which control input receives the signal. If one of those links is undocumented, it should remain unresolved rather than being filled in from a generic diagram or assumptions about typical equipment.

## Identify terminals and contact state before interpreting wiring

Terminal labels and contact states must be identified from documentation for the specific switch. Use COM, NO, or NC only when the actual contact arrangement is documented. COM means common for that documented arrangement; NO and NC describe contact states relative to a specified reference condition. The labels do not independently reveal which wire leads to the centrifuge’s control input.

The reference actuator condition is essential. A statement that a contact is open or closed is incomplete if it does not say whether the actuator is at its free position, operating position, or another defined condition. Do not assume that the centrifuge’s mechanical home position corresponds to a particular actuator state. That relationship depends on the mechanism and switch installation.

Actuator travel also has distinct stages. Under MIL-PRF-8805K sections 6.5.14 and 6.5.16, pretravel runs from the free position to the operating position, while overtravel runs from the operating position to the extreme permitted actuator position. These terms describe actuator movement; they do not identify terminal wiring or establish how a centrifuge controller interprets a contact change.

A click is not a terminal identification method. It may indicate movement of a snap mechanism, but it does not establish continuity, the contact state at a particular reference condition, the wire’s destination, or the control system’s response. Wire color and an assumed resting or home position likewise do not establish terminal function. The switch documentation and the defined actuator condition are the basis for interpreting a contact description.

Operating and release are also separate events. The position at which a switch operates and the position at which it releases need not be treated as the same event. A single observed actuator position therefore does not establish the full behavior across movement in both directions, much less the complete homing behavior of the centrifuge.

### Related guides

- [bottling machine home position micro switch location](/guides/bottling-machine-home-position-micro-switch-location/)
- [incinerator end of stroke micro switch maintenance](/guides/incinerator-end-of-stroke-micro-switch-maintenance/)
- [rotary indexing table guard interlock micro switch location](/guides/rotary-indexing-table-guard-interlock-micro-switch-location/)
- [security barrier open position micro switch wiring](/guides/security-barrier-open-position-micro-switch-wiring/)

## What wiring checks can and cannot establish

A continuity check should be described only when a procedure specifies the isolation condition, the actuator state, the measuring method, and the expected contact behavior. The accepted information here does not provide a complete procedure or expected readings for a particular centrifuge switch. It is therefore not enough to prescribe probe placement, assign a pass/fail reading, or state that a particular contact should be open or closed in a given installation.

Even a properly defined isolated-switch reading would address only that switch under the tested condition. It would not, on its own, establish that the installed wiring is correct, that the control input receives the signal, or that the centrifuge’s control circuit interprets it as intended. A discrepancy could involve the mechanical input, the switch contacts, terminal identification, wiring, or another part of the equipment. The available information does not distinguish those possibilities for a specific machine.

Do not infer an installed circuit’s condition from a click or an isolated contact reading, and do not treat general switch terminology as a live-circuit test procedure. Live electrical work and diagnosis of undocumented circuits are outside this explanation. The relevant boundary is the design-specific documentation: it must establish the switch, actuator reference condition, contact connections, and control input before the wiring can be interpreted.

In short, centrifuge home position micro switch wiring can describe a conditional path from mechanical actuation, through documented switch contacts, to a control input. It cannot establish a universal terminal map or tell you what the centrifuge will do without evidence for that particular design.

## Sources and references

- Defense Logistics Agency ASSIST: [MIL-PRF-8805K: Switches and Switch Assemblies, Sensitive, Snap Action, General Specification For](https://quicksearch.dla.mil/qsDocDetails.aspx?ident_number=7196){: rel="nofollow noopener noreferrer" }
