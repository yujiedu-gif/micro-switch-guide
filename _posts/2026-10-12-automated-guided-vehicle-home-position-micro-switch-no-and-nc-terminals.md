---
title: "automated guided vehicle home position micro switch NO and NC terminals: Reading the Signal"
description: "automated guided vehicle home position micro switch NO and NC terminals: Understand the operating idea, essential terminology, practical checks,."
date: 2026-10-12 16:49:35 +0800
category: Applications
tags:
  - automated guided vehicle home position micro switch NO and NC terminals
  - micro switches
  - Applications
author: editorial_team
---

An **automated guided vehicle home position micro switch NO and NC terminals** can provide a change in electrical contact state when a mechanical actuator moves the switch. That change may be used as a position input, but the terminal labels alone do not say whether the vehicle is at home. The vehicle’s wiring and controller logic determine how the input is interpreted.

Verification therefore needs to follow the signal path: establish the intended mechanical position from the vehicle documentation, check the switch’s contact behavior with the circuit safely isolated, and then compare the powered input indication with the documented logic. This separates the switch’s electrical operation from wiring and control-system interpretation. Use the connection diagram, terminal markings, circuit function, and permissible load documented for the exact switch and equipment rather than inferring them from a generic layout.

## What NO and NC terminals mean on an automated guided vehicle home position micro switch NO and NC terminals

COM means common terminal, NO means normally open, and NC means normally closed. In generic changeover terminology, “normally” refers to the switch’s released, unactuated condition. With the switch released, COM and NC have continuity, while COM and NO do not. When the actuator operates the switch, the common contact transfers: COM–NO has continuity and COM–NC does not. Confirm this relationship against the schematic for the exact device.

These terms describe the switch contacts, not vehicle status. NO does not mean “not home,” and NC does not mean “home.” A controller may receive a signal through either contact arrangement, and the logic assigned to that signal depends on the system design. The same physical switch state can therefore correspond to different displayed or interpreted vehicle states in different configurations.

Keep the mechanical state separate from the electrical one. The mechanical question is whether the actuator is released or operating the switch. The electrical question is which COM pair has continuity in that state. Only after those are established can the signal be compared with the system’s definition of home.

## How the micro switch can signal home position

A position signal has several steps: the vehicle reaches a mechanical position, that position engages or releases the actuator, the switch changes its COM contact relationship, and wiring carries the resulting input to the control system. The controller then interprets that input according to its documented configuration. A disagreement at any step can make the indicated state differ from the vehicle’s physical position.

An input may use the NO path or the NC path. Do not assume that either arrangement is universal. Nor can the contact labels establish whether a closed circuit means home, not-home, or a fault. That meaning depends on the vehicle’s wiring and controller logic. The documented input arrangement and polarity are needed to interpret the signal.

It is useful to compare three observations rather than treating them as one: the actuator’s mechanical position, continuity at the switch, and the controller’s input indication. If the actuator moves but the contact state does not change as expected, the issue is at the mechanical engagement, switch, or measurement step. If the contact changes correctly but the controller indication does not match the documentation, the next checks belong in the wiring and input-interpretation path.

## Verify the home-position signal safely from switch to controller

Start with the vehicle’s electrical documentation and the system procedure for placing equipment in an approved safe state. Follow applicable deenergization and qualification requirements. Isolate power before resistance or continuity measurements; do not make those measurements on an energized circuit. Do not bypass a safety function as part of signal checking.

With the circuit safely isolated, inspect whether the actuator reaches the switch at the documented position and whether the mounting appears secure. Then test COM–NO and COM–NC in both released and actuated states. Compare the results with the switch schematic and expected contact behavior. An in-circuit reading may be affected by other paths, so do not infer switch failure from a measurement made without accounting for the circuit. Use the system’s approved test procedure when the result is unclear.

After isolated checks, restore the circuit only as directed by the system procedure. Observe the controller input indication while comparing the mechanical position and switch state with the documented logic. The indication should be interpreted using the vehicle’s specified input arrangement, not a general assumption about NO or NC. Keep the test bounded to the documented signal path and required safe conditions.

## Separate alignment, contact, wiring, and logic faults

If the actuator does not engage consistently at the intended point, inspect mechanical reach and mounting security against the vehicle documentation. Do not assume universal actuator settings or travel. The applicable operating travel and position requirements must come from the documentation for the actual switch and equipment. A switch can have defined operating characteristics, but those characteristics should not be guessed from its terminal labels.

If the actuator moves but isolated COM–NO and COM–NC continuity does not change as expected, check the test setup and the switch behavior against its schematic. Distinguish a measurement affected by connected circuitry from a contact-state result obtained with the circuit appropriately isolated. A single unexplained reading is not enough to identify the cause.

If the contact state is correct but the controller input disagrees, trace the documented wiring and terminal connections, then check the input interpretation and specified polarity. Loose or damaged wiring is a different fault path from mechanical misalignment or a contact that does not change state. Incorrect input interpretation is another possibility when the switch and wiring match the documentation but the displayed state does not. Identify where the observed signal first differs from the documented expectation instead of changing several parts of the chain at once.

### Related guides

- [ball screw actuator home position micro switch replacement](/guides/ball-screw-actuator-home-position-micro-switch-replacement/)
- [bottling machine end of stroke micro switch](/guides/bottling-machine-end-of-stroke-micro-switch/)
- [automated guided vehicle home position micro switch location](/guides/automated-guided-vehicle-home-position-micro-switch-location/)
- [accelerator pedal position stop micro switch operating force](/guides/accelerator-pedal-position-stop-micro-switch-operating-force/)

## Confirm the documented home state before adjustment

Use the vehicle documentation to establish the intended home point, the switch state expected there, and the controller’s interpretation of that state. Confirm the exact switch schematic, wiring arrangement, permissible load, and applicable operating travel from the documentation for the switch and equipment. Physical terminal layout alone is not a reliable basis for identifying function or ratings.

Do not adjust the actuator or change NO/NC wiring solely to make an indicator appear correct. First determine whether the mismatch lies in mechanical engagement, switch continuity, wiring, or input logic. Where the documentation or observed behavior does not resolve the issue, leave the setting and interpretation unresolved rather than applying a generic assumption.

Before returning the vehicle to service, require repeatable operation and the system-approved functional verification. The **automated guided vehicle home position micro switch NO and NC terminals** identify contact behavior; the documented vehicle design determines what that behavior means as a home-position signal.

## Sources and references

- Defense Logistics Agency ASSIST: [MIL-PRF-8805K: Switches and Switch Assemblies, Sensitive, Snap Action, General Specification For](https://quicksearch.dla.mil/qsDocDetails.aspx?ident_number=7196){: rel="nofollow noopener noreferrer" }
- Occupational Safety and Health Administration: [29 CFR 1910.333: Selection and Use of Work Practices](https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.333){: rel="nofollow noopener noreferrer" }
- Wikipedia: [Miniature snap-action switch](https://en.wikipedia.org/wiki/Miniature_snap-action_switch){: rel="nofollow noopener noreferrer" }
