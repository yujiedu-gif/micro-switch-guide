---
title: "How Does a float switch mechanism micro switch NO and NC terminals Work?"
description: "float switch mechanism micro switch NO and NC terminals: Understand the operating idea, essential terminology, practical checks, limitations, and evidence."
date: 2026-10-13 11:27:16 +0800
category: Applications
tags:
  - float switch mechanism micro switch NO and NC terminals
  - micro switches
  - Applications
author: editorial_team
---

A float switch mechanism micro switch NO and NC terminals describes several distinct parts, not one universal device. In designs that use an electromechanical micro switch, movement of a float can pass through a linkage or another mechanism to the switch actuator. The actuator’s movement operates the switch contacts according to that switch’s design. The float’s position alone does not establish which contact state is present or what the connected equipment will do.

## How Does a float switch mechanism micro switch NO and NC terminals Work?

A float is the moving input in the level-responsive assembly. A linkage or other mechanism may transfer its movement to an actuator, the part that physically moves the micro switch. The micro switch is the electrical contact component; it is distinct from the float assembly and from the host circuit that uses its contacts.

When the mechanism moves the actuator to the switch’s operating position, the contacts change state according to the device’s design. That general sequence explains the component relationship, but it does not establish a particular float direction, operating level, contact arrangement, or control response. Those details depend on the documented mechanism and circuit.

The term “float switch” can describe an assembly that uses different designs. Some float-operated devices may use a micro switch, while others need not. Therefore, it is important not to treat every float device as a micro switch or to assume that the float directly moves a contact. The mechanical path may include a lever, rod, or another arrangement, if that is what the design documents show.

Keep the parts and their roles separate when interpreting an explanation or diagram:

- The float responds mechanically to its surroundings.
- A linkage or other mechanism transfers movement where the design includes one.
- The actuator is the part that moves the micro switch.
- The micro switch changes its contacts at its operating event.
- The host circuit determines how those contacts are used.

This separation prevents a common reasoning error: inferring a contact state or equipment action directly from “float up” or “float down.” The movement path and electrical response must be established for the particular design rather than supplied by the name of the assembly.

## From float movement to micro switch actuation

The causal path begins with float movement, but the next step is design-dependent. A float may drive a lever, rod, or other mechanism if the documented arrangement provides that connection. The mechanism then transfers motion to the micro switch actuator. Only after identifying this path can the float’s movement be related to the actuator’s movement.

The actuator’s movement brings the switch to an operating event. The switch’s contact state changes according to its construction and operating state; the term “operating position” refers to the position at which operation occurs. This describes the switch-side event without assigning a particular liquid level, float direction, or threshold. No specific travel distance or operating level follows from the general relationship alone.

Where actuator travel is described, pretravel runs from the free position to the operating position, while overtravel runs from the operating position to the extreme permitted actuator position. These terms describe portions of actuator motion, not a float’s level range. Applying them to a float assembly requires the mechanism’s geometry and the exact switch documentation; the terms do not establish how much float movement produces a given amount of actuator travel.

The path may be indirect, and its geometry matters. A float that rises could move an actuator in one direction in one arrangement and a different direction in another. A linkage may also alter how motion is transferred. Without the specific design information, it is not possible to infer whether the actuator is pressed, released, or held in an operating state at a particular float position.

This distinction also separates mechanical movement from electrical interpretation. Observing that a float moves does not, by itself, establish that the micro switch has reached its operating position. Likewise, describing an actuator movement does not establish which terminals are connected in the host circuit. The mechanism, switch contact arrangement, and circuit each need to be understood within their own documented scope.

## What NO and NC mean at the reference condition

NO means normally open, and NC means normally closed, when those labels are used for the documented contact arrangement. “Normally” refers to the specified reference condition for the switch, not automatically to a float’s raised or lowered position. The reference condition must come from the device’s documentation or schematic; the labels alone do not identify a liquid level or the float position at which the switch operates.

A generic changeover contact may use COM for common, alongside NO and NC. That is a general terminal arrangement, not a guarantee that every micro switch has those three terminals. The exact device marking or schematic controls. If the documented arrangement does not identify COM, NO, and NC, those labels should not be assigned from a switch’s physical layout or appearance.

NO and NC describe contact-state terminology at a stated reference condition. They do not, by themselves, promise a particular current flow in an installed circuit. Current flow and the equipment’s response depend on the circuit and its documented connections. Nor do these labels show whether the host system interprets a contact change as a request to start, stop, signal, or perform another function.

To relate a reference contact state to float movement, the documentation must connect the relevant conditions: the switch’s reference condition, the actuator’s position, and the float mechanism’s position. Without that information, it would be unsupported to say, for example, that a rising float makes NO close or NC open. Such a sequence may be stated only for a design whose mechanism and contact behavior are documented.

### Related guides

- [bottling machine home position micro switch location](/guides/bottling-machine-home-position-micro-switch-location/)
- [incinerator end of stroke micro switch maintenance](/guides/incinerator-end-of-stroke-micro-switch-maintenance/)
- [rotary indexing table guard interlock micro switch location](/guides/rotary-indexing-table-guard-interlock-micro-switch-location/)
- [security barrier open position micro switch wiring](/guides/security-barrier-open-position-micro-switch-wiring/)

## What the terminal labels do not tell you

Terminal labels do not establish the float position that operates the switch, the motion direction through the mechanism, or the level at which operation occurs. Those are mechanical and design-specific details. They also do not establish whether the host equipment starts a pump, raises an alarm, stops a process, or takes another action. A contact change is an input to a circuit; the circuit’s documented logic determines its use.

For a particular device, use its connection diagram, terminal markings, circuit function, and permissible load rather than inferring connections from a generic terminal layout. Rating values are specification-sheet requirements tied to their stated load and test conditions, not universal switching capacities. A rating for a stated condition should not be transferred to a different load or treated as a general property of all float-operated devices.

The useful interpretation boundary is therefore clear: the float supplies movement; the documented mechanism transfers that movement; the micro switch actuator operates the contacts; and the host circuit determines what the contact change means in the larger system. A specific float position can be associated with a specific NO or NC state only when the design documentation establishes the full relationship. The phrase float switch mechanism micro switch NO and NC terminals identifies that relationship as a question to trace, not a universal sequence to assume.

## Sources and references

- Defense Logistics Agency ASSIST: [MIL-PRF-8805K: Switches and Switch Assemblies, Sensitive, Snap Action, General Specification For](https://quicksearch.dla.mil/qsDocDetails.aspx?ident_number=7196){: rel="nofollow noopener noreferrer" }
- Occupational Safety and Health Administration: [29 CFR 1910.333: Selection and Use of Work Practices](https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.333){: rel="nofollow noopener noreferrer" }
- Wikipedia: [Miniature snap-action switch](https://en.wikipedia.org/wiki/Miniature_snap-action_switch){: rel="nofollow noopener noreferrer" }
