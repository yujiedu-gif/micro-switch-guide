---
title: "shift lever position micro switch NO and NC terminals: How to Identify Them"
description: "shift lever position micro switch NO and NC terminals: Understand the operating idea, essential terminology, practical checks, limitations, and evidence."
date: 2026-10-08 09:00:00 +0800
category: Applications
tags:
  - shift lever position micro switch NO and NC terminals
  - micro switches
  - Applications
author: editorial_team
---

A **shift lever position micro switch NO and NC terminals** must be identified from its markings or documentation, then checked by comparing continuity in the switch’s two actuator states. Do not assign terminal functions from wire color or pin location alone. The key reference is the switch’s own unactuated state, which may differ from the position it occupies after installation if the lever presses its actuator.

A continuity check can verify whether the identified contact paths change as expected when the actuator moves. It does not, by itself, diagnose the surrounding shift system or establish that the switch is suitable for a particular circuit. Keep terminal identification, switch testing, and equipment-level diagnosis separate.

## What NO and NC mean on a shift lever position micro switch NO and NC terminals

COM is the common terminal. In generic changeover-switch terminology, NC means normally closed and NO means normally open. “Normally” refers to the switch’s unactuated reference state, not automatically to the lever’s installed resting position or to a particular vehicle operating condition.

For a changeover arrangement, the expected contact paths are:

- With the switch unactuated, COM-to-NC is closed and COM-to-NO is open.
- With the switch actuated, COM-to-NC is open and COM-to-NO is closed.

These descriptions concern the contact relationship between the named terminals. They do not establish what a connected circuit will do, because that depends on the circuit and equipment design. Confirm the exact switch schematic before applying the generic changeover description to a particular device.

A shift lever or linkage may press the switch actuator when installed. If it does, the switch can be actuated even when the lever appears to be in its usual resting position. Therefore, record whether a reading is taken with the switch actuator released or pressed. Do not use the equipment’s lever position as a substitute for identifying the switch’s unactuated reference state.

## Identify COM, NO, and NC without guessing from terminal position

First inspect the switch for molded or printed COM, NO, and NC markings, or for a connection diagram. If the markings are missing or unclear, consult documentation for the exact switch and equipment. Do not treat a generic drawing or a similar-looking switch as proof of the terminal arrangement.

Terminal order and physical layout are not universal identifiers. Wire colors are not universal identifiers either. A wire connected to a terminal may reflect the equipment’s circuit design, but it does not independently establish that the terminal is COM, NO, or NC. Identify the terminals from the device’s own markings or diagram before interpreting meter readings.

The circuit diagram, terminal marking, circuit function, and permissible load documented for the exact switch and equipment provide the relevant context. A continuity test can help verify contact behavior once the terminals are identified; it should not be used to infer a load rating or reconstruct the equipment wiring from appearance alone.

If the markings and documentation do not establish the terminals, do not guess from connector position. Keep the identification unresolved until the exact terminal diagram or other applicable documentation is available. This is different from finding a wiring fault: a mistaken terminal reference can produce confusing readings even when the measured contact itself is functioning.

## Test the shift lever position micro switch with a multimeter

Use a de-energized, isolated test so the reading represents the switch contacts rather than other circuit paths. Follow the applicable de-energization and qualification requirements. If the switch remains connected to the equipment wiring, other paths may affect the measurement; disconnect the switch when needed to isolate it. Do not treat a reading on an energized or unisolated circuit as this contact test.

With the switch isolated, set the meter to continuity or resistance. Keep the actuator in its unactuated, released position and measure COM-to-NO, then COM-to-NC. Record both results and label the actuator state. For a changeover arrangement, the expected unactuated pattern is an open COM-to-NO path and a closed COM-to-NC path.

Next move the actuator through the switch’s actual operating position without forcing it beyond its intended travel. Repeat both measurements and record them as the actuated state. The expected changeover pattern is a closed COM-to-NO path and an open COM-to-NC path. Comparing both paths in both states is more informative than checking only one terminal pair: it shows whether the expected relationship changes and helps expose a wrongly chosen reference terminal.

A useful record is a four-entry table:

| Actuator state | COM-to-NO | COM-to-NC |
|---|---|---|
| Released, unactuated | Open expected | Closed expected |
| Pressed, actuated | Closed expected | Open expected |

Use the table only if the exact device documentation confirms a changeover arrangement. If its schematic specifies a different contact configuration, follow that schematic rather than assuming the generic pattern. A continuity indication or resistance value describes the tested, isolated contact path in that state; it does not prove that the installed equipment or its wiring is correct.

## Interpret readings and separate contact faults from setup errors

For a documented changeover switch, the expected result is one closed and one open COM path in each stable actuator state, with the paths exchanging states after actuation. If neither path changes, that observation alone does not identify the cause. Recheck that COM was identified correctly, that the switch was isolated, and that the actuator actually moved through its operating position.

Also consider the mechanical reference state. Mounting preload can hold the actuator in an actuated position before the test begins. A switch tested while pressed may appear to contradict the expected unactuated pattern even when the terminal identification is correct. Release the actuator and distinguish that free state from the installed state before drawing a conclusion.

If the readings do not match the markings or documentation, verify the exact terminal diagram and test setup before concluding that a contact has failed. A wrong COM reference can make both measured pairs appear inconsistent. So can measuring through connected circuit paths instead of an isolated switch. If the terminal identities, isolation condition, and actuator states are established and the contact paths still do not show the documented change, the result supports further investigation of the switch, but it does not by itself diagnose the entire shift system.

Stop rather than assigning functions by trial and error when the measured behavior conflicts with the exact device documentation. The switch’s contact test and the equipment’s circuit diagnosis are separate tasks; a switch reading cannot establish the condition of other components or control logic.

### Related guides

- [ball screw actuator home position micro switch replacement](/guides/ball-screw-actuator-home-position-micro-switch-replacement/)
- [bottling machine end of stroke micro switch](/guides/bottling-machine-end-of-stroke-micro-switch/)
- [automated guided vehicle home position micro switch location](/guides/automated-guided-vehicle-home-position-micro-switch-location/)
- [accelerator pedal position stop micro switch operating force](/guides/accelerator-pedal-position-stop-micro-switch-operating-force/)

## Check the installed lever position and wiring context

After the isolated test, compare the switch’s released actuator state with the installed mechanical position. A shift lever, cam, or linkage may press the actuator during installation, so the contact state observed in place may correspond to the actuated state rather than the unactuated reference state. Keep those states distinct when comparing a meter result with a wiring diagram or expected equipment behavior.

Check whether the lever reaches the switch’s operating position and whether mounting preload is already holding the actuator. Do not force the actuator beyond its intended travel. The goal is to understand which mechanical state produced each reading, not to infer an adjustment specification or repair procedure that is not established by the switch documentation.

Before interpreting an installed circuit, use the exact equipment connection diagram and documented circuit function. The contact state alone does not establish whether the equipment should start, stop, indicate a position, or behave in another way. If an equipment-level result remains unexplained, keep that diagnosis separate from the isolated terminal test and follow applicable electrical safety and qualification requirements.

In short, identify COM, NO, and NC from the exact switch markings or documentation, then compare COM-to-NO and COM-to-NC with the actuator released and pressed. For the **shift lever position micro switch NO and NC terminals**, the decisive check is the documented contact-state change, interpreted with the switch’s true unactuated reference state and its installed lever position kept distinct.

## Sources and references

- Defense Logistics Agency ASSIST: [MIL-PRF-8805K: Switches and Switch Assemblies, Sensitive, Snap Action, General Specification For](https://quicksearch.dla.mil/qsDocDetails.aspx?ident_number=7196){: rel="nofollow noopener noreferrer" }
- Occupational Safety and Health Administration: [29 CFR 1910.333: Selection and Use of Work Practices](https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.333){: rel="nofollow noopener noreferrer" }
- Wikipedia: [Miniature snap-action switch](https://en.wikipedia.org/wiki/Miniature_snap-action_switch){: rel="nofollow noopener noreferrer" }
