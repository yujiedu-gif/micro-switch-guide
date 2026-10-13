---
title: "boom lift travel limit micro switch NO and NC terminals: What Do They Indicate?"
description: "boom lift travel limit micro switch NO and NC terminals: Understand the operating idea, essential terminology, practical checks, limitations, and evidence."
date: 2026-08-04 16:38:12 +0800
last_modified_at: 2026-10-13 11:46:37 +0800
category: Applications
tags:
  - boom lift travel limit micro switch NO and NC terminals
  - micro switches
  - Applications
author: editorial_team
---

A **boom lift travel limit micro switch NO and NC terminals** describes contact labels on a component, not a complete statement about how a boom lift behaves. NO and NC indicate contact relationships at a defined reference condition. To interpret them, first establish that condition for the particular switch and distinguish the switch’s actuator position from the lift mechanism’s travel-limit position. The labels alone do not show how the lift is wired or what its control system does when a contact changes.

## boom lift travel limit micro switch NO and NC terminals: the direct answer

NO and NC identify contact relationships relative to a specified reference condition for the micro switch. They do not, by themselves, say whether the lift is moving, whether it has reached a travel limit, or whether a circuit is energized. The correct interpretation depends on the reference condition documented for the particular switch and on the contact arrangement it actually has.

In the terminology used here, NO means normally open and NC means normally closed. “Normally” must be tied to a defined switch state, such as the documented actuator condition; it should not be treated as an undefined promise about the switch while installed in equipment. Without that reference, the labels cannot tell you which contact relationship applies at a particular point in the lift’s motion.

The terms also describe contacts, not a command to the boom lift. A change in a switch contact could be an input to a larger circuit, but the labels do not establish what that circuit does. They do not show whether the lift stops, raises an alert, permits another movement, or takes any other action. Those outcomes depend on the host equipment’s actual wiring and control logic, which cannot be inferred from NO and NC alone.

For that reason, an explanation of the labels must start with two particulars: the switch’s documented reference condition and the contact arrangement. If either is unknown, the terminal names alone are insufficient to determine the contact state at a specific actuator position. The same caution applies even when the switch is associated with a lift travel limit: the application name does not define the switch’s reference state or the lift’s response.

## Read NO and NC from the micro switch reference state

A micro switch is an electromechanical component in which mechanical movement of an actuator can change an electrical contact state. A miniature snap-action switch can be used for position or limit detection, but that general use does not establish the arrangement in any particular boom lift. In this context, the actuator is the part of the switch moved by an external mechanism. The switch’s actuator state is therefore a component-level condition, distinct from the position of the lift’s boom or its travel-limit mechanism.

To read NO and NC, identify the reference condition specified for the switch, then interpret the contact labels relative to that condition. NO refers to the contact relationship designated as open at that reference state; NC refers to the relationship designated as closed at that reference state. These labels are not independent of the reference condition. If it is not documented or otherwise established for the particular switch, avoid assigning an open or closed state to a terminal at an assumed lift position.

COM means common when that terminal arrangement is documented. Do not assume a COM terminal, or a particular set of contacts, merely because a component is called a micro switch. The physical terminal arrangement and the applicable documentation must support those identifications. If COM is present, NO and NC describe their respective contact relationships to it only in the context of the documented arrangement and reference condition.

Actuator movement may cause a contact transition, but the switch’s transition is not identical to the lift reaching a mechanical limit. A lift mechanism could move an actuator, and a resulting contact change could be used for position or limit detection. However, neither the terminal labels nor the general use of a micro switch establishes the geometry, adjustment, or exact point at which a particular lift mechanism moves the actuator. Numerical travel limits are requirements of the applicable specification sheet and must not be inferred from the component category.

## Relate actuator movement to the lift limit without assuming control behavior

If a boom lift uses a micro switch in a travel-limit arrangement, the lift’s mechanical mechanism may move the switch actuator as the mechanism changes position. The actuator movement may then change a contact relationship. That is a conditional description of how a component can participate in position or limit detection, not a claim that every boom lift uses the same switch arrangement or that a specific actuator position corresponds to a specific boom position.

Keep the causal steps separate: the host mechanism moves, the switch actuator may move, the contact state may change, and the lift’s circuit may interpret that change. The terminal labels address the contact relationship at the switch. They do not specify the mechanical relationship between the boom and actuator, the circuit’s wiring, or the controller’s response. A switch can provide a contact change without the labels revealing what the rest of the equipment does with it.

The control circuit determines what a contact change means to the equipment. The available information does not establish whether a particular circuit uses NO or NC, what state it expects during normal travel, or whether a change causes stopping, an alarm, or another response. Do not infer a shutdown or safety function from the presence of a travel-limit switch, from a terminal label, or from the fact that a contact changes state. The actual arrangement and control response must be established from the equipment’s applicable documentation and design information.

This boundary matters because the switch’s component-level state and the lift’s system-level state answer different questions. Knowing that a contact is open or closed under a defined switch condition does not identify the lift’s operating state. Likewise, knowing that a mechanical travel limit has been reached does not, by itself, establish the contact state unless the relationship between the mechanism and the switch is documented. Keep the component description conditional wherever those details are not established.

### Related guides

- [aircraft door closed monitor micro switch NO and NC terminals](/guides/aircraft-door-closed-monitor-micro-switch-no-and-nc-terminals/)
- [access control door position micro switch function](/guides/access-control-door-position-micro-switch-function/)
- [ball screw actuator end of stroke micro switch contact rating](/guides/ball-screw-actuator-end-of-stroke-micro-switch-contact-rating/)
- [capping machine guard interlock micro switch actuator travel](/guides/capping-machine-guard-interlock-micro-switch-actuator-travel/)

## What a terminal observation can and cannot establish

A terminal observation can address the switch’s contact state only when the tested switch, reference condition, and method are clearly defined. It does not automatically establish that the installed wiring is correct, that a controller recognizes the input, or that the boom lift responds as intended. Those are separate questions about the surrounding circuit and equipment. An isolated switch observation must not be treated as proof of the installed system’s safety or correct operation.

A click, if heard during actuator movement, is not enough to prove continuity, correct terminal identification, correct wiring, or suitability for a load. It can indicate movement of a snap mechanism, but the sound does not establish the electrical condition of the contacts. Similarly, an observed contact change at the switch does not prove that a signal reaches or is interpreted by the lift’s controller.

Do not turn the terminal labels into an adjustment or replacement procedure. The available facts do not establish a particular switch model, its ratings, its mounting arrangement, its compatibility, or the lift’s prescribed verification process. Travel requirements must come from the applicable specification sheet rather than assumptions based on the category “micro switch.” If the reference condition, terminal arrangement, or relationship to the lift mechanism is unknown, leave that point unresolved rather than guessing.

The useful conclusion is limited but clear: NO and NC describe contact relationships relative to a defined reference condition for the particular switch. In a possible boom lift travel-limit arrangement, actuator movement may change those contacts, but the labels alone do not establish when that occurs or what the lift does afterward. The **boom lift travel limit micro switch NO and NC terminals** therefore identify component-level contact relationships, not the lift’s wiring, control response, or overall travel-limiting function.

## Sources and references

- Defense Logistics Agency ASSIST: [MIL-PRF-8805K: Switches and Switch Assemblies, Sensitive, Snap Action, General Specification For](https://quicksearch.dla.mil/qsDocDetails.aspx?ident_number=7196){: rel="nofollow noopener noreferrer" }
- Wikipedia: [Miniature snap-action switch](https://en.wikipedia.org/wiki/Miniature_snap-action_switch){: rel="nofollow noopener noreferrer" }
