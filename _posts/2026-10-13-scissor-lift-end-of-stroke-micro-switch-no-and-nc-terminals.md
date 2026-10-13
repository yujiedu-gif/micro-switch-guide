---
title: "Scissor lift end of stroke micro switch NO and NC terminals: what do they mean?"
description: "scissor lift end of stroke micro switch NO and NC terminals: Understand the operating idea, essential terminology, practical checks, limitations, and."
date: 2026-10-13 09:00:00 +0800
category: Applications
tags:
  - scissor lift end of stroke micro switch NO and NC terminals
  - micro switches
  - Applications
author: editorial_team
---

For **scissor lift end of stroke micro switch NO and NC terminals**, NO and NC describe contact states relative to the switch’s specified reference condition. They do not, by themselves, identify a lift command or predict what the lift will do. To interpret them, first identify the contact arrangement and reference condition documented for the particular switch, then distinguish that switch behavior from the lift’s wiring and controller logic.

A miniature snap-action switch can change an electrical contact state in response to mechanical actuator movement and is commonly used for position or limit detection. But whether a particular scissor lift uses a micro switch for end-of-stroke sensing, and how it is configured, must be established from documentation for that equipment. Labels alone do not establish a universal end-stop state.

## Scissor lift end of stroke micro switch NO and NC terminals: the direct answer

NO means “normally open,” and NC means “normally closed.” In this context, “normal” refers to the switch’s documented reference condition, not automatically to the lift’s ordinary operating position, a particular end of travel, or a safe state. The terms identify contact behavior only when the applicable contact arrangement and reference condition are known.

For a documented contact arrangement, the reference condition establishes which contact path is open and which is closed. Mechanical actuation may change the contact state, but the labels do not say whether the actuator is being pressed at the lift’s end of stroke. That relationship depends on the installed mechanism and the particular switch’s arrangement.

Therefore, NO and NC are not universal descriptions of “lift moving” versus “lift stopped,” nor do they specify what a controller will interpret as an end-of-stroke signal. They name contact states relative to a reference condition. To map a contact to a lift position, use the switch contact diagram together with lift-specific documentation showing how the switch is installed and used.

The presence of a micro switch is not guaranteed across all scissor lifts, and its configuration cannot be inferred from the equipment type alone. If the relevant diagram or reference condition is unavailable, the contact-to-position mapping remains unknown; do not supply it by assuming a common wiring pattern.

## How the micro switch actuator changes the contact state

A micro switch responds to mechanical movement at its actuator. In a position or limit-detection arrangement, an external mechanism may move the actuator as part of the equipment’s motion. That movement can change an electrical contact state. This general mechanism explains why a micro switch can be used for detection, but it does not establish the geometry, actuation point, or end-of-stroke position for a specific lift.

Keep three ideas separate: the documented reference condition, mechanical actuation, and the lift position associated with that actuation. The reference condition is the basis for the NO and NC labels. Mechanical actuation is the movement that changes the switch state in the documented arrangement. The lift position is an equipment-level relationship that must be established from the lift’s design documentation. Those ideas cannot be substituted for one another without evidence.

For example, identifying a terminal as NO does not establish that the contact is open when the lift platform is at a particular height. That conclusion would require knowing the switch’s contact arrangement and reference condition, how the actuator is moved, and how the switch is positioned in the lift. Without those details, state only the documented contact behavior and leave the position mapping unresolved.

Nor does the general snap-action description establish a specific number of contacts or a particular transition sequence for an unidentified switch. Treat the switch diagram and equipment documentation as the evidence for the actual arrangement. Avoid assigning a terminal state to “end of stroke” based only on the NO or NC label.

## Why NO or NC does not tell you what the lift will do

A switch contact state is not the same thing as a controller decision. The lift’s wiring and control logic determine how a contact change is interpreted. The resulting equipment response, if any, depends on that design. NO or NC alone does not establish that a contact change stops movement, blocks travel in a direction, triggers an alarm, or produces another response.

This distinction matters because a contact can be identified correctly while its role in the larger circuit is still unknown. The terminal label describes the switch contact relative to its reference condition; it does not describe the lift’s complete control circuit. Likewise, knowing that a switch is associated with end-of-stroke sensing does not establish what the controller does with its signal.

Do not infer a stopping or safety function merely from the presence of a micro switch or from a contact label. The equipment schematic or service documentation must establish the switch’s circuit role and the controller’s intended response. If those documents do not show the relationship, the response remains unresolved. A general explanation of NO and NC cannot fill that gap.

This boundary also prevents treating every scissor lift as though it uses the same sensing arrangement. A particular design may use a micro switch, but its location, contact use, and control interpretation are design-specific. The general fact that miniature snap-action switches are commonly used for position or limit detection is not evidence of a particular lift’s wiring or behavior.

### Related guides

- [bottling machine home position micro switch location](/guides/bottling-machine-home-position-micro-switch-location/)
- [incinerator end of stroke micro switch maintenance](/guides/incinerator-end-of-stroke-micro-switch-maintenance/)
- [rotary indexing table guard interlock micro switch location](/guides/rotary-indexing-table-guard-interlock-micro-switch-location/)
- [security barrier open position micro switch wiring](/guides/security-barrier-open-position-micro-switch-wiring/)

## What documentation can verify the terminal assignment

Start with the contact diagram and terminal markings for the exact switch, then consult the lift-specific schematic or service documentation. Together, those records can identify the documented contact arrangement and show how the switch is used in the equipment. Use the equipment documentation to establish any claimed relationship between mechanical actuation, lift position, circuit function, and controller interpretation.

Do not infer a terminal assignment from physical layout, wire color, a generic diagram, or the equipment category. The connection diagram, terminal marking, circuit function, and permissible load documented for the exact switch and equipment govern applicability. A generic drawing or a label without its reference condition may not answer how the installed circuit behaves.

If the documentation does not identify the reference condition, contact arrangement, or end-of-stroke mapping, treat the missing detail as unknown rather than assigning a state. In particular, do not assume that every lift has a micro switch, that terminal numbering is universal, or that a contact label predicts stopping behavior.

Electrical work must remain within applicable requirements. In the United States workplace context, the cited rule generally requires exposed live parts to be deenergized before work, requires a qualified person to verify the deenergized condition with test equipment, and limits work on energized parts to qualified persons. Verify all applicable requirements; this boundary does not establish a procedure for inspecting or servicing a particular lift.

In short, **scissor lift end of stroke micro switch NO and NC terminals** identify contact states only in relation to the documented switch reference condition. The switch’s mechanical actuation, its mapping to lift position, and the controller’s response are separate facts. Confirm each from the appropriate switch and equipment documentation rather than deriving lift behavior from NO or NC alone.

## Sources and references

- Defense Logistics Agency ASSIST: [MIL-PRF-8805K: Switches and Switch Assemblies, Sensitive, Snap Action, General Specification For](https://quicksearch.dla.mil/qsDocDetails.aspx?ident_number=7196){: rel="nofollow noopener noreferrer" }
- Occupational Safety and Health Administration: [29 CFR 1910.333: Selection and Use of Work Practices](https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.333){: rel="nofollow noopener noreferrer" }
- Wikipedia: [Miniature snap-action switch](https://en.wikipedia.org/wiki/Miniature_snap-action_switch){: rel="nofollow noopener noreferrer" }
