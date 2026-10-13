---
title: "Stacker crane end of stroke micro switch NO and NC terminals"
description: "stacker crane end of stroke micro switch NO and NC terminals: Understand the operating idea, essential terminology, practical checks, limitations, and."
date: 2026-07-08 14:17:31 +0800
last_modified_at: 2026-10-13 11:46:37 +0800
category: Applications
tags:
  - stacker crane end of stroke micro switch NO and NC terminals
  - micro switches
  - Applications
author: editorial_team
---

For a **stacker crane end of stroke micro switch NO and NC terminals**, the labels describe contact states relative to a defined reference condition of the switch actuator. They do not, by themselves, identify a particular crane position or say whether the crane will stop, signal, or interlock. Those equipment-level results depend on the actual wiring and control logic.

A micro switch is an electromechanical component: movement of its actuator can change an electrical contact state. A miniature snap-action switch can be used for position or travel-limit detection, but that does not make every end-of-stroke device a micro switch. To interpret NO and NC, first find the exact switch’s contact arrangement and the reference actuator condition in its documentation. Then keep the switch’s contact behavior separate from the crane controller’s response.

## What NO and NC mean on a stacker crane end of stroke micro switch NO and NC terminals

NO and NC are contact labels, not names for crane positions. Where the documented device has a changeover contact, the terminals may be marked common (COM), normally closed (NC), and normally open (NO). The exact device marking or schematic controls; do not assume that every micro switch has this arrangement.

“Normally” must be tied to the reference actuator condition specified for that switch. Relative to that condition, the NO contact is the contact identified as open and the NC contact is the one identified as closed. If actuator movement operates the switch, the contact state may change. The exact transition and the condition in which it occurs must be established from the switch documentation, rather than inferred from terminal names alone.

This reference condition is not automatically the stacker crane’s home position, stopped state, or end of travel. A crane position describes the equipment; the terminal labels describe contact states under a specified switch condition. The switch might be actuated at a particular travel point, but that relationship is not established by NO or NC markings. Without the apparatus arrangement and documentation, the physical crane position corresponding to the reference actuator condition remains unknown.

The labels also do not establish which terminals are used in the crane circuit. A changeover contact may offer more than one contact path, but the installed circuit could use only one path, or the documented device may have a different arrangement. Identify the actual terminals using the exact switch’s markings or schematic. Do not infer their function from their physical layout or from a generic drawing of another switch.

## How actuator movement changes the contact state

A mechanism on the crane can move a micro switch’s actuator. If the particular switch uses snap action, actuator movement can cause a rapid change in contact state. That is the component-level relationship: mechanical input at the actuator may produce an electrical transition at the documented contacts. It does not specify which direction of crane travel causes movement, where the actuator is engaged, or what the controller does with the resulting signal.

To describe the transition accurately, keep the reference state and operated state distinct. First establish the documented contact state at the stated reference actuator condition. Then establish what the documentation says happens when the actuator is moved into its operated condition. If the relevant arrangement is a documented changeover contact, the contact relationship can change as the switch operates. Do not assign an open or closed state to a particular point in crane travel unless that connection is documented for the switch and apparatus.

A click may indicate movement of a snap mechanism, but it does not prove electrical continuity, correct terminal identification, correct wiring, or suitability for the circuit load. Mechanical movement and electrical contact condition are different observations. A sound alone cannot establish whether the contacts are making the connection expected by the crane circuit.

Likewise, a contact transition at the switch is not necessarily evidence that the whole travel-limit function has worked. The switch is one component in a possible detection arrangement. The wiring and control system determine whether a contact change reaches the controller and how that input is interpreted. Keep conclusions about the switch’s mechanical or contact state separate from conclusions about equipment behavior.

## Why terminal labels do not specify the crane response

A terminal label identifies a contact relationship under a defined switch condition. It does not say that a stacker crane will stop, sound an alarm, signal a controller, or block movement. Those outcomes depend on which terminals are connected, the circuit function, and the controller’s logic. The same label cannot establish the response of an undocumented circuit.

For example, a contact change may be used as an input to equipment control, but the meaning assigned to that input belongs to the actual circuit and control logic. Without that information, it is not possible to say whether the controller treats a particular contact state as a travel limit, a normal condition, a fault, or something else. Do not infer a stop, alarm, or direction interlock merely because a micro switch is present at a travel boundary.

This distinction also prevents a common mix-up: “normally closed” does not mean “closed when the crane is in its normal operating position.” The terminal label’s reference is the specified actuator condition, not an assumed crane mode or location. The reference condition must be found in the switch documentation. The relationship between that condition and a crane position must be established separately from the documented mechanical arrangement.

A terminal label alone therefore cannot confirm circuit function. Even if the contact state is known, it does not show whether the correct terminals are connected to the controller, whether the controller is configured to interpret the input as expected, or whether the broader arrangement operates as intended. Nor does a label establish whether the switch is suitable for the circuit’s load. Suitability depends on the permissible load documented for the exact switch and equipment, not on NO or NC alone.

### Related guides

- [bottling machine home position micro switch location](/guides/bottling-machine-home-position-micro-switch-location/)
- [incinerator end of stroke micro switch maintenance](/guides/incinerator-end-of-stroke-micro-switch-maintenance/)
- [rotary indexing table guard interlock micro switch location](/guides/rotary-indexing-table-guard-interlock-micro-switch-location/)
- [security barrier open position micro switch wiring](/guides/security-barrier-open-position-micro-switch-wiring/)

## What must be verified for a particular crane circuit

For a particular stacker crane, begin with the exact switch documentation. Confirm the contact arrangement, terminal markings, and the actuator condition used as the reference for the NO and NC descriptions. Use the connection diagram and terminal marking for that exact device rather than inferring terminal identity from a generic physical layout. If the documentation does not establish how a particular crane position moves the actuator, that position-to-actuator relationship remains unresolved.

The circuit’s use requires separate evidence. Establish which documented terminals are connected and how the crane controller interprets the input. The connection diagram, circuit function, and permissible load documented for the exact switch and equipment are relevant; the terminal labels alone do not provide them. This is not a procedure for installing, adjusting, replacing, or troubleshooting the crane circuit. Electrical work must remain within applicable deenergization and qualification requirements.

If continuity is checked as part of verification, interpret the result only for the isolated switch, a defined actuator state, and a specified test method. A reading under one state does not establish behavior under another state, identify undocumented wiring, or prove that the installed crane system is safe or functional. An isolated-switch result and an in-equipment response answer different questions.

In the United States workplace context, the cited rule generally requires exposed live parts to be deenergized before work, requires a qualified person to verify the deenergized condition with test equipment, and limits work on energized parts to qualified persons. Verify all applicable requirements. Do not use an isolated continuity reading as a substitute for those requirements or as proof about the complete equipment.

The bounded interpretation is straightforward: NO and NC describe contact states relative to the micro switch’s documented reference actuator condition. Actuator movement may change those states, but the labels do not identify a crane position or determine the controller’s response. For a **stacker crane end of stroke micro switch NO and NC terminals**, exact switch documentation and circuit evidence are needed to connect terminal behavior to the equipment function.

## Sources and references

- Defense Logistics Agency ASSIST: [MIL-PRF-8805K: Switches and Switch Assemblies, Sensitive, Snap Action, General Specification For](https://quicksearch.dla.mil/qsDocDetails.aspx?ident_number=7196){: rel="nofollow noopener noreferrer" }
- Occupational Safety and Health Administration: [29 CFR 1910.333: Selection and Use of Work Practices](https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.333){: rel="nofollow noopener noreferrer" }
- Wikipedia: [Miniature snap-action switch](https://en.wikipedia.org/wiki/Miniature_snap-action_switch){: rel="nofollow noopener noreferrer" }
