---
title: "Electric linear actuator end of stroke micro switch NO and NC terminals"
description: "electric linear actuator end of stroke micro switch NO and NC terminals: Understand the operating idea, essential terminology, practical checks,."
date: 2026-10-13 13:45:35 +0800
category: Applications
tags:
  - electric linear actuator end of stroke micro switch NO and NC terminals
  - micro switches
  - Applications
author: editorial_team
---

An electric linear actuator end of stroke micro switch NO and NC terminals describe contact states, not a universal wiring plan or a guaranteed actuator response. In some designs, mechanical movement near a travel limit operates a micro switch; the switch’s contact change is distinct from what the actuator’s controller or circuit does with that change. The exact terminal identification, reference condition, mechanical arrangement, and circuit function must come from documentation for the particular switch and equipment.

## What the end-of-stroke micro switch does

A micro switch is an electromechanical component that can change an electrical contact state in response to movement of its actuator. A miniature snap-action switch may be used for position or limit detection. Some electric linear actuator designs may use a micro switch near a travel limit, but that is not a feature that should be assumed for every actuator.

The parts and events should be kept distinct. The actuator’s moving assembly may contact a linkage, cam, stop, or another mechanical feature. That feature may move the switch actuator. Movement of the switch actuator can then change the state of the switch contacts. Separately, a connected control circuit may interpret an electrical change and produce an outcome. These are related stages, but one does not establish the details of the next.

For example, evidence that a moving assembly can mechanically operate a switch does not, by itself, establish the exact position where the switch changes state. Nor does the occurrence of a contact change establish that the actuator has reached a particular endpoint, stopped, or reversed. Those details depend on the specific mechanical arrangement and circuit, and they must be confirmed for the design in question.

This distinction matters because “end of stroke” describes a travel-limit context, while NO and NC identify contact states relative to a documented reference condition. Neither phrase supplies a complete wiring description. A generic physical layout or the presence of a switch near moving parts is not enough to identify terminals, determine their reference state, or infer how the surrounding equipment responds.

## Electric linear actuator end of stroke micro switch NO and NC terminals

NO and NC are contact labels interpreted relative to the reference condition specified for the particular contact arrangement. In a generic changeover contact, the terminals may be labeled common, normally closed, and normally open. The exact device marking or schematic controls; the generic labels alone do not establish the configuration or state of a particular switch.

When the switch actuator is operated, the contact state may change. But the labels do not say which contact state occurs when an electric linear actuator extends, retracts, reaches either travel limit, or rests in any particular position. That relationship depends on the switch’s documented reference condition and the mechanism that operates it. Without those details, it is not sound to call one terminal state the universal “extended” or “retracted” state.

It is useful to keep three questions separate:

- Which terminals are identified as common, NO, and NC on this exact switch?
- What reference condition does its documentation use to define those contact labels?
- What mechanical position or event operates the switch in this actuator design?

An answer to one does not automatically answer the others. A terminal label does not locate the switch’s mechanical operating point, and a known travel limit does not identify the contact state unless the mechanism and reference condition are documented. The same caution applies when interpreting a diagram: use the applicable switch and equipment documentation rather than inferring terminal function from a generic drawing or physical placement.

Therefore, NO and NC can explain the switch’s contact state under a specified reference condition, but they cannot alone identify which state corresponds to either end of actuator travel. If the reference condition, switch arrangement, or actuation point is not documented, that relationship remains unresolved. Do not fill the gap by assuming a familiar actuator design or by treating the labels as endpoint instructions.

## Why terminal labels do not determine actuator behavior

A switch contact change and a controller’s response are different events. The switch provides a change in contact state when mechanically operated, while the external circuit determines whether that change is used to stop movement, reverse it, signal a condition, or serve another function. The terminal names do not disclose that circuit logic.

For instance, identifying a contact as NO or NC does not prove that it is connected to a controller input, a motor circuit, an indicator, or an interlock. It also does not establish whether the circuit treats a particular state as an instruction, a status signal, or no action. Those conclusions require the actual circuit function and wiring information. No specific stopping, reversing, signaling, or safety behavior should be inferred from NO and NC labels alone.

The mechanical path also does not settle the circuit response. A moving assembly may operate the switch near a limit, and the switch may change contact state, while the result in the host equipment depends on how the circuit is designed and connected. Conversely, evidence of a circuit’s intended response would not, by itself, establish that a particular actuator contains a micro switch or that its mechanical actuation occurs at a specific position.

This boundary prevents a common interpretive error: treating a component label as a full description of the equipment. Contact terminology describes the switch under a stated reference condition. Travel behavior describes the actuator and its mechanical arrangement. Operational behavior describes the connected circuit or controller. A valid explanation of a specific actuator must connect these facts using its documentation, not assumptions based on the terminal names.

### Related guides

- [accelerator pedal position stop micro switch NO and NC terminals](/guides/accelerator-pedal-position-stop-micro-switch-no-and-nc-terminals/)
- [industrial boiler travel limit micro switch maintenance](/guides/industrial-boiler-travel-limit-micro-switch-maintenance/)
- [access control door position micro switch NO and NC terminals](/guides/access-control-door-position-micro-switch-no-and-nc-terminals/)
- [capping machine guard interlock micro switch actuator travel](/guides/capping-machine-guard-interlock-micro-switch-actuator-travel/)

## What to verify for a specific actuator design

For a particular design, check the applicable switch and equipment documentation for the terminal identification, the reference condition used for NO and NC, the mechanical feature that operates the switch, the actuation point, and the circuit function. Confirm the connection diagram and the permissible load documented for the exact switch and equipment. Do not infer terminal identity or ratings from a generic physical layout.

These checks answer different questions. Terminal markings or a schematic establish how the documented device identifies its contacts. The mechanical description establishes how the moving assembly operates the switch, if a switch is used. The equipment circuit documentation establishes how a contact change is intended to be interpreted. If any of these details is absent or unclear, the corresponding relationship should remain unknown rather than being supplied by a general rule.

If documentation describes an isolated continuity check and that check is appropriate, interpret it only for the specified switch state and isolation condition. An isolated contact reading concerns the switch under that test condition; it does not prove that the installed actuator assembly is safe or fully functional. It also does not, by itself, verify the controller’s response or the mechanical relationship between actuator travel and switch operation.

Follow applicable deenergization and qualification requirements. Energized circuit inspection, or work beyond the documented safe procedure, should be left to qualified personnel. A terminal label, a mechanical observation, or a single contact check is not a substitute for the documentation and verification needed to establish the behavior of the particular assembly.

In short, an electric linear actuator end of stroke micro switch NO and NC terminals identify contact states only in relation to the documented switch arrangement and reference condition. They do not independently identify an actuator endpoint or predict what its control circuit will do. Confirm the switch, mechanical actuation, and circuit function separately before drawing a conclusion about a specific design.

## Sources and references

- Defense Logistics Agency ASSIST: [MIL-PRF-8805K: Switches and Switch Assemblies, Sensitive, Snap Action, General Specification For](https://quicksearch.dla.mil/qsDocDetails.aspx?ident_number=7196){: rel="nofollow noopener noreferrer" }
- Occupational Safety and Health Administration: [29 CFR 1910.333: Selection and Use of Work Practices](https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.333){: rel="nofollow noopener noreferrer" }
- Wikipedia: [Miniature snap-action switch](https://en.wikipedia.org/wiki/Miniature_snap-action_switch){: rel="nofollow noopener noreferrer" }
