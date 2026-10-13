---
title: "bucket elevator end of stroke micro switch NO and NC terminals"
description: "bucket elevator end of stroke micro switch NO and NC terminals: Understand the operating idea, essential terminology, practical checks, limitations, and."
date: 2026-05-12 21:43:28 +0800
last_modified_at: 2026-10-13 11:46:37 +0800
category: Applications
tags:
  - bucket elevator end of stroke micro switch NO and NC terminals
  - micro switches
  - Applications
author: editorial_team
---

A **bucket elevator end of stroke micro switch NO and NC terminals** describe contact states within a switch, not the bucket elevator’s complete control behavior. NO and NC have meaning only in relation to the reference condition documented for the particular micro switch. When the actuator moves, the contact state may change as specified by that design. The controller’s response to that change depends on the actual circuit, so the labels alone do not establish whether the elevator stops, signals, or continues operating.

A micro switch is an electromechanical component. In some end-of-stroke arrangements, a moving part or linkage operates its actuator; other bucket elevator designs may use a different arrangement. The switch’s contact transition and the equipment’s interpretation of that transition are separate questions. To interpret the terminals, use the exact switch documentation and the equipment circuit information rather than inferring behavior from the labels or a terminal’s physical position.

## What NO and NC mean on a micro switch

NO means normally open, and NC means normally closed, when those labels are used for a documented changeover contact arrangement. “Normally” refers to the switch’s specified reference condition. It does not, by itself, identify the physical position of the elevator, the actuator position in every installation, or whether current flows in the installed circuit. Establish the reference condition from the exact switch marking or schematic before interpreting either label.

A generic changeover contact may also have a COM, or common, terminal. The device’s own marking or schematic controls whether that arrangement and those terminal names apply. Do not assume that every micro switch has all three terminals, or that a terminal occupies a standard physical location. If the documentation does not establish the contact arrangement, reference condition, or terminal identification, those details remain unknown.

For a documented arrangement, actuator operation can change the contact state. A contact identified as open in the reference condition may be closed in another specified state, and a contact identified as closed may be open in that state. The exact transition must come from the switch documentation; the labels alone do not specify the actuator travel, the position at which operation occurs, or the state at every point of movement.

This distinction matters when reading an end-of-stroke description. The reference condition belongs to the switch’s definition, while “end of stroke” describes a position in the host mechanism. Those conditions should not be treated as identical unless the design documentation connects them. NO and NC are contact-state labels, not unqualified promises about current flow or machine status.

## How a bucket elevator end of stroke micro switch NO and NC terminals may be used

In a bucket elevator design that uses a micro switch for end-of-stroke sensing, a moving mechanical part or linkage may act on the switch actuator. The switch can then change contact state as its documented mechanism operates. This describes the component’s possible role, not a claim that every bucket elevator uses a micro switch or the same mechanical arrangement.

To relate a terminal label to the elevator’s end-of-stroke position, the design information must establish both the switch’s reference condition and which actuator state corresponds to that position. A label such as NO does not say, on its own, whether the contact is open when the elevator mechanism reaches end of stroke. That depends on how the particular switch is referenced and actuated in that design.

Keep the switch separate from the surrounding control system. The micro switch provides a contact state; it is not, by that fact alone, the controller or stopping mechanism. A circuit may use the contact change as an input, but the switch label does not describe what the controller does with that input. The actual circuit and documented terminal arrangement are needed to connect the component’s behavior to the application.

The physical layout of terminals is not a substitute for that evidence. A generic expectation about where COM, NO, or NC might be located cannot establish the terminal identity for a particular device. Use the switch’s connection diagram and markings, together with the equipment documentation, to identify the relevant contacts and their relationship to the stated actuator condition.

## What the terminal labels do not tell you about elevator behavior

NO and NC do not independently mean “run,” “stop,” “alarm,” “safe,” or “normal operation.” They describe contact states only relative to the documented switch reference condition. Whether a contact change produces any of those equipment responses depends on the elevator’s actual control circuit and its interpretation of the input. Do not infer a response from a terminal label alone.

The same boundary applies to the word “end.” Knowing that a switch is used for end-of-stroke sensing does not establish which physical movement operates it, which actuator state represents the endpoint, or what the controller does after the contact changes. Those details are design-specific. Without documentation that connects them, the switch’s terminal state and the elevator’s resulting behavior cannot be determined from NO or NC alone.

A terminal marking also does not establish how the switch is wired, what load it serves, or whether the installed arrangement is suitable. These questions require the connection diagram, terminal marking, circuit function, and permissible load documented for the exact switch and equipment. Do not infer a wiring arrangement from a generic diagram or from the apparent location of terminals.

This is a boundary on interpretation, not a troubleshooting procedure. The labels can help identify a documented contact arrangement, but they cannot by themselves diagnose a failure, establish a complete machine state, or prove a safety function. If the available documentation does not show how the circuit interprets the switch input, the equipment response remains unresolved.

### Related guides

- [bottling machine home position micro switch location](/guides/bottling-machine-home-position-micro-switch-location/)
- [incinerator end of stroke micro switch maintenance](/guides/incinerator-end-of-stroke-micro-switch-maintenance/)
- [rotary indexing table guard interlock micro switch location](/guides/rotary-indexing-table-guard-interlock-micro-switch-location/)
- [security barrier open position micro switch wiring](/guides/security-barrier-open-position-micro-switch-wiring/)

## What to verify before interpreting the contact state

Begin with the exact switch documentation. Confirm whether the device has the contact arrangement in question, how its terminals are marked, and what reference condition the documentation uses for NO and NC. Where the device provides a connection diagram, use it rather than a generic physical-layout inference. If those details are absent or unclear, do not assign a contact state based on an assumed terminal position.

Next, use the equipment documentation to establish which physical actuator condition corresponds to the stated end-of-stroke position in that design. This step links a mechanical position to the switch’s reference and operating states; it does not establish how the controller responds. The circuit information is separately needed to determine how the contact transition is interpreted by the equipment.

If a continuity check is used to confirm contact behavior, it should concern the isolated switch and a defined actuator state. Interpret the result only against the documented terminal arrangement and reference condition. Such a check does not establish the safety of the installed circuit, confirm its wiring, or prove that the elevator as a whole functions correctly.

Electrical work has a separate safety boundary. Under the cited United States workplace rule, exposed live parts generally must be deenergized before work; a qualified person must verify the deenergized condition with test equipment; and work on energized parts is limited to qualified persons. Verify all applicable requirements. The contact-state explanation does not replace those requirements or provide an installation or repair procedure.

The defensible conclusion is limited: NO and NC identify contact states relative to a documented reference condition, and actuator operation may change those states as specified for the switch. In a bucket elevator design that uses a micro switch for end-of-stroke sensing, the mechanical relationship and the controller’s response must be established from the relevant design documentation. The phrase **bucket elevator end of stroke micro switch NO and NC terminals** does not, by itself, identify the installed wiring or determine the elevator’s behavior.

## Sources and references

- Defense Logistics Agency ASSIST: [MIL-PRF-8805K: Switches and Switch Assemblies, Sensitive, Snap Action, General Specification For](https://quicksearch.dla.mil/qsDocDetails.aspx?ident_number=7196){: rel="nofollow noopener noreferrer" }
- Occupational Safety and Health Administration: [29 CFR 1910.333: Selection and Use of Work Practices](https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.333){: rel="nofollow noopener noreferrer" }
- Wikipedia: [Miniature snap-action switch](https://en.wikipedia.org/wiki/Miniature_snap-action_switch){: rel="nofollow noopener noreferrer" }
