---
title: "Bottling machine end of stroke micro switch wiring: trace contacts and verify the control circuit"
description: "bottling machine end of stroke micro switch wiring: Understand the operating idea, essential terminology, practical checks, limitations, and evidence."
date: 2026-10-12 16:49:35 +0800
category: Applications
tags:
  - bottling machine end of stroke micro switch wiring
  - micro switches
  - Applications
author: editorial_team
---

A bottling machine end of stroke micro switch wiring arrangement is specific to the machine’s control design. The switch may provide a position-dependent contact to a control circuit, but its contact state alone does not establish whether the machine stops, advances, or changes sequence. Trace the documented circuit from the switch to the assigned controller input, then verify the contact transition at the actual actuator limit. Do not infer terminal functions from the switch’s appearance or assume that a particular wiring pattern applies to every bottling machine.

Before inspection or wiring changes, follow the machine’s isolation and lockout procedure. For continuity checks, the switch must be isolated and power removed. Use the machine schematic and switch documentation to establish the intended contact, input, and actuator positions. If the observed behavior does not match the documentation, stop and have the mismatch reviewed by qualified personnel.

## What the end-of-stroke micro switch does in a bottling machine

When this design is used, the micro switch acts as a position-dependent contact in a control circuit. Movement of the machine actuator changes the contact state at a point in its stroke. The control system can then receive the input shown on the machine schematic. That describes the switch’s role, not the machine’s overall response: a contact transition does not, by itself, establish that the bottling machine will stop or perform any particular sequence step.

Start with the machine schematic to identify which stroke the switch monitors and which control input is associated with it. Confirm that the documented switch symbol and input correspond to the device being inspected. Do not assume that every bottling machine uses an end-of-stroke micro switch, or that similar-looking switches serve the same function.

Keep three questions separate: what the switch contacts do, which circuit the machine connects to them, and what the controller does with the resulting input. The contact markings and isolated test address the first question. The schematic and input specifications address the second. The machine’s documented control behavior addresses the third. A correct answer to one does not establish the others.

## Bottling machine end of stroke micro switch wiring: identify COM, NO, and NC

Use the switch documentation to identify terminal markings and functions. In generic changeover terminology, COM is the common terminal, NO is the normally open terminal, and NC is the normally closed terminal. These names do not identify where terminals sit on a particular switch, and appearance is not enough to determine terminal function. Check the exact device schematic or documentation before making a connection.

For a changeover contact, the actuator position determines which contact path is closed. With the actuator released, check the documented contact state between COM and NO and between COM and NC. Then actuate the switch and check both paths again. Use an isolated switch with power removed for continuity testing. Record what changes; do not assume which path the installed circuit uses based only on NO or NC terminology.

The intended connection depends on the machine circuit shown in its schematic. The schematic, not a general convention, determines whether the control path uses COM with NO or COM with NC. If the switch markings, documentation, and observed isolated contact states disagree, do not proceed on an assumption. Resolve the discrepancy before wiring.

## Trace the control-input path from the switch to the machine schematic

Once the contact functions are confirmed, follow the schematic from the control supply, through the selected switch contact, to the controller input or any interposing device shown. Trace both sides of the path as documented rather than relying on wire color or terminal position. Identify the input assigned to this end-of-stroke signal and confirm that the switch being inspected is the one represented in that circuit.

Keep this control-input path distinct from motor and other power wiring. The switch’s control contact may be part of an input circuit; that does not establish that the switch carries motor power or that a power circuit should be connected to it. Do not use a generic wiring diagram to bridge missing details. The supplied machine schematic and relevant input specifications must establish the actual connection.

Do not assume input polarity, voltage, or whether the circuit is monitored. Those details are machine-specific and must be verified in the schematic and input specifications. If the documents do not establish the input requirements or the circuit path, leave the connection unresolved and request qualified review. A terminal label alone cannot supply missing controller-input information.

## Wire and verify the switch at the actuator limit

Apply the machine’s isolation and lockout procedure before inspecting or changing wiring. Confirm terminal functions from documentation, identify conductors against the schematic, and check that terminations are secure. Check actuator alignment against the documented stroke limits. Do not reposition the actuator or infer a permitted limit from how the switch looks.

After wiring, verify the documented circuit state at three positions: with the actuator released, at the actuated transition, and at any permitted overtravel position. Check continuity only with the switch isolated and power removed. If the machine procedure calls for checking the controller input indication, use that procedure and the documented input behavior; do not assume an indication pattern or test live conductors outside authorized site procedures.

The distinction between operating position and further actuator travel matters when assessing the limit. Under MIL-PRF-8805K sections 6.5.14 and 6.5.16, pretravel runs from free position to operating position, while overtravel runs from operating position to the extreme permitted actuator position. Use the documented actuator limits rather than treating any additional movement as acceptable. Verify that the contact transition occurs where the machine documentation requires and that the actuator does not pass beyond its permitted position.

Compare each observed state with the machine schematic and documented input behavior. A mismatch at release, actuation, or permitted overtravel means the circuit has not been verified. Stop rather than compensating by swapping terminals or moving the actuator without a documented basis.

### Related guides

- [ball screw actuator home position micro switch replacement](/guides/ball-screw-actuator-home-position-micro-switch-replacement/)
- [bottling machine end of stroke micro switch](/guides/bottling-machine-end-of-stroke-micro-switch/)
- [automated guided vehicle home position micro switch location](/guides/automated-guided-vehicle-home-position-micro-switch-location/)
- [accelerator pedal position stop micro switch operating force](/guides/accelerator-pedal-position-stop-micro-switch-operating-force/)

## Common wiring errors and safe checks

Check contact assumptions first. Treating NO or NC as a physical terminal location, or choosing a contact without consulting the machine schematic, can produce a circuit state different from the documented one. Confirm the switch-side behavior with the switch isolated and power removed, then compare it with the circuit path shown on the schematic.

Check for a wrong controller input separately from a contact-state problem. Trace the conductor to the assigned input and any interposing device shown. Also check for loose terminations and conductor identification that does not match the documented path. These are distinct checks; finding one does not rule out the others.

Finally, check actuator alignment and travel against documented limits. A contact may change state, yet the installed actuator position may not match the required stroke transition. Do not bypass the switch, defeat an interlock, or test live conductors unless qualified and authorized under site procedures. If the schematic, switch markings, or observed input behavior conflict, stop and escalate for qualified review.

The verification is complete only when the documented contact functions, control-input path, and states at release, actuation, and permitted overtravel agree. This keeps the wiring decision tied to the actual bottling machine rather than an assumed universal arrangement.

This concludes the explanation of bottling machine end of stroke micro switch wiring.

## Sources and references

- Defense Logistics Agency ASSIST: [MIL-PRF-8805K: Switches and Switch Assemblies, Sensitive, Snap Action, General Specification For](https://quicksearch.dla.mil/qsDocDetails.aspx?ident_number=7196){: rel="nofollow noopener noreferrer" }
- Wikipedia: [Miniature snap-action switch](https://en.wikipedia.org/wiki/Miniature_snap-action_switch){: rel="nofollow noopener noreferrer" }
