---
title: "boom lift home position micro switch NO and NC terminals"
description: "boom lift home position micro switch NO and NC terminals: Understand the operating idea, essential terminology, practical checks, limitations, and."
date: 2026-10-12 16:49:35 +0800
category: Applications
tags:
  - boom lift home position micro switch NO and NC terminals
  - micro switches
  - Applications
author: editorial_team
---

The **boom lift home position micro switch NO and NC terminals** describe electrical contact paths relative to the switch’s unactuated mechanical state. They do not, by themselves, identify whether a boom is at home. The installed switch’s actuator position, mounting orientation, contact arrangement, and machine wiring determine what a terminal state means for the equipment.

A contact check can help establish how a particular switch changes state, but it is different from diagnosing the controller’s interpretation of that state. Before testing, confirm the exact switch diagram and the equipment’s approved procedure. Do not infer terminal functions or machine logic from a generic layout.

## What NO and NC mean on a boom lift home position micro switch NO and NC terminals

In generic changeover terminology, **COM** means common, **NC** means normally closed, and **NO** means normally open. “Normally” refers to the switch’s unactuated mechanical position, not to the boom’s normal position or to a presumed home state. The exact device marking or schematic controls if its configuration differs from this terminology.

For a typical changeover contact, COM is the shared terminal. With the actuator released, the contact path is between COM and NC; the COM–NO path is open. When the actuator is operated, the contact transfers: the COM–NO path closes and the COM–NC path opens. This describes a typical changeover arrangement, not a guarantee that every switch has all three terminals or both paths. Some configurations may provide only one contact path.

The terminal names therefore describe the contact arrangement, not a boom-position label. NO does not inherently mean “boom home,” and NC does not inherently mean “boom away.” To interpret a reading, first identify the switch’s unactuated state and determine which terminal paths the exact switch diagram documents.

## How boom position changes the micro switch contact state

The boom mechanism can move the switch actuator as it approaches or leaves the position where the switch is installed. If that movement presses the actuator, a typical changeover contact transfers from the released state to the operated state. If the actuator is released, the contact returns to its unactuated state. The electrical description follows actuator position, not the name assigned to a boom position.

How this maps to “home” depends on the installation. The switch’s mounting orientation and the relationship between its actuator and the boom mechanism determine whether the actuator is pressed or released when the boom is home. The equipment wiring and documented circuit function determine which contact path is used for the intended signal. Without that information, NO or NC alone cannot establish the expected home-position state.

Keep the mechanical state separate from the controller’s interpretation. A switch may change its contact path as expected while the signal observed elsewhere differs because of wiring or input logic. Conversely, a controller’s displayed state does not, on its own, establish the switch’s isolated contact state. These are related checks, but they answer different questions.

## How to check the terminals safely

Use the equipment’s approved isolation and immobilization procedure before testing, and prevent unintended boom movement. Testing must follow applicable deenergization and qualification requirements. Confirm the machine-specific procedure and the exact switch diagram before connecting a meter. Do not assume that a generic terminal layout identifies the test points on the installed equipment.

With the circuit de-energized, isolate the switch as required by the equipment documentation. Use a continuity or resistance measurement between COM and each documented contact terminal. Record the readings with the actuator released, then repeat with it operated only as the approved procedure permits. Compare the two states with the exact switch diagram. For a typical changeover contact, the expected pattern is COM–NC continuity when unactuated and COM–NO continuity when operated; verify that this applies to the device being checked rather than assuming it.

If there is no COM terminal, or the switch diagram shows a different contact arrangement, do not force the typical changeover interpretation onto the readings. Confirm the marking and connection diagram, then follow the machine’s procedure for that configuration. The permissible load and circuit function must also come from documentation for the exact switch and equipment, not from a generic physical-layout inference.

An isolated contact check establishes the switch’s measured contact behavior under the test conditions. It does not establish that the installed wiring, controller input, or overall machine logic is functioning as intended. Keep those conclusions separate when recording or interpreting results.

## Why terminal readings may not match the home-position signal

A measurement made at the controller or elsewhere in the circuit can reflect more than the switch contact alone. Wiring, connector faults, parallel circuit paths, input configuration, or a different contact arrangement can affect a circuit-level observation. Therefore, an energized controller-input reading is not a substitute for an isolated, de-energized contact check.

This distinction matters when a controller indication appears inconsistent with the switch’s terminal readings. The contact check concerns the switch’s path between its documented terminals. A controller-side observation concerns a signal in the installed circuit and its interpretation. Neither result should be used to assume the other without the equipment’s wiring information and diagnostic procedure.

If the measured state conflicts with the machine documentation, stop and follow the equipment-specific diagnostic procedure. Do not infer that the boom is home from a terminal label, or infer a switch fault from a controller-side indication alone. The machine’s approved test points and procedures govern any further diagnosis.

### Related guides

- [ball screw actuator home position micro switch replacement](/guides/ball-screw-actuator-home-position-micro-switch-replacement/)
- [bottling machine end of stroke micro switch](/guides/bottling-machine-end-of-stroke-micro-switch/)
- [automated guided vehicle home position micro switch location](/guides/automated-guided-vehicle-home-position-micro-switch-location/)
- [accelerator pedal position stop micro switch operating force](/guides/accelerator-pedal-position-stop-micro-switch-operating-force/)

## What to confirm before interpreting a result

Before deciding what a reading means, confirm the terminal markings and the exact switch contact diagram. Identify the actuator’s released and operated states, and establish the installed orientation from the equipment documentation. Then use the machine wiring information to determine which contact path is intended to represent the home-position condition.

Also confirm that the test was performed under the specified isolation conditions and at the appropriate points for the intended check. A generic changeover description can explain how COM, NO, and NC are commonly used, but it cannot replace the exact switch and equipment documentation. If markings, diagram, or measured behavior do not align, treat the intended logic as unresolved and follow the machine-specific procedure.

The **boom lift home position micro switch NO and NC terminals** identify contact paths relative to the switch’s unactuated state; they do not independently declare boom position. Verify the contact state with the documented terminal arrangement and an approved de-energized procedure, then use the equipment wiring information to connect that result to the home-position signal.

## Sources and references

- Defense Logistics Agency ASSIST: [MIL-PRF-8805K: Switches and Switch Assemblies, Sensitive, Snap Action, General Specification For](https://quicksearch.dla.mil/qsDocDetails.aspx?ident_number=7196){: rel="nofollow noopener noreferrer" }
- Occupational Safety and Health Administration: [29 CFR 1910.333: Selection and Use of Work Practices](https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.333){: rel="nofollow noopener noreferrer" }
- Wikipedia: [Miniature snap-action switch](https://en.wikipedia.org/wiki/Miniature_snap-action_switch){: rel="nofollow noopener noreferrer" }
