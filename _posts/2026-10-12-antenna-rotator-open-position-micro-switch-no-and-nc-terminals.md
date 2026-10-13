---
title: "Antenna rotator open position micro switch NO and NC terminals"
description: "antenna rotator open position micro switch NO and NC terminals: Understand the operating idea, essential terminology, practical checks, limitations, and."
date: 2026-10-12 16:49:35 +0800
category: Applications
tags:
  - antenna rotator open position micro switch NO and NC terminals
  - micro switches
  - Applications
author: editorial_team
---

An **antenna rotator open position micro switch NO and NC terminals** are identified by their relationship to the switch actuator, not by the words “open position” on the rotator. The open-position function describes what the switch is intended to signal within a particular rotator. It does not, by itself, tell you which contact path the control circuit uses. To verify the switch, isolate power, identify the marked terminals, and compare continuity with the actuator released and operated. Then use the rotator’s own wiring diagram to relate the observed change to its open-position indication. Do not infer the electrical state from a terminal label or a generic terminal layout.

## What NO and NC mean on an antenna rotator open position micro switch NO and NC terminals

NO means normally open; NC means normally closed. “Normally” refers to the switch actuator’s unoperated position, not to whether the antenna rotator is at its open limit. In a generic changeover contact, COM is the common terminal, NC is the normally closed terminal, and NO is the normally open terminal. The exact device marking or schematic controls, so check the documentation for the specific switch rather than relying on a generic arrangement.

At the unoperated actuator position, the NO path is open and the NC path is closed in the usual meaning of those labels. When the actuator is operated, a changeover contact changes which path connects to COM. Verify the actual switch behavior rather than treating the label as a substitute for a test. The force or torque needed for the actuator to return is a separate specification: release force is the force or torque to which force on the actuator must be reduced to permit the contacts to return to the unoperated position after operation.

The phrase “open-position switch” identifies an intended limit function in the rotator. It does not establish whether the rotator’s circuit signals that limit through COM-NO or COM-NC. The actuator may be released or operated at the physical limit, and the circuit’s indication depends on how that switch is arranged and connected. Therefore, a NO label does not mean “open position,” and an NC label does not mean “closed position.” Determine the mechanical actuator state and electrical indication separately.

## Verify the open-limit micro switch contacts with power isolated

First, isolate power according to the rotator documentation. Continuity testing is a de-energized check; do not test resistance or continuity on an energized circuit. Follow the applicable de-energization and qualification requirements, and consult the equipment documentation before accessing or testing the switch. This sequence verifies contact behavior; it is not a procedure for installing or rewiring a rotator.

1. **Identify the terminals.** Read the markings on the exact switch and check its schematic or the rotator diagram. Where the device identifies COM, NO, and NC, use those markings. Do not identify terminals from physical position alone: a generic layout is not proof of the exact device’s terminal arrangement.
2. **Set the actuator to its unoperated position.** Observe whether it is released or otherwise not being pressed. Use the switch’s mechanical condition, not the rotator’s open-position label, to define this test state.
3. **Check COM-NO and COM-NC.** With power isolated, use a continuity tester to check each pair. Record whether each pair conducts or remains open. Keep the probe connections on the identified terminals and avoid treating a reading through other connected circuitry as proof of the switch’s standalone contact state.
4. **Operate the actuator and repeat.** Press or otherwise operate the actuator as the switch is designed to be operated. Recheck COM-NO and COM-NC, then record which path changed. Release the actuator and confirm whether the readings return to their initial state.

The comparison between released and operated states is the useful result. It shows whether and how the contact paths change during the test. If the terminals are not clearly marked, the actuator cannot be operated as intended, or the readings do not give a clear result, do not guess. Check the exact switch schematic and rotator service documentation. The available information here does not establish a universal actuator position, reading, or contact arrangement for all rotators.

## Map verified contact changes to the rotator’s open-position indication

Once the contact behavior has been recorded, compare it with the connection diagram or service documentation for the exact rotator and switch. The diagram, terminal marking, circuit function, and permissible load documented for that equipment govern the interpretation. Do not use a generic physical layout or a generic expectation about NO and NC to decide how the rotator detects its open limit.

The documentation may show that the control circuit uses one of the contact paths as part of its indication. Relate the measured change to that documented path only. For example, if the diagram identifies a particular COM path as the open-limit input, compare that path with the released and operated readings. This establishes whether the observed contact change matches the documented switch state. It does not justify assuming that another rotator uses the same path or logic.

Keep two observations distinct:

- **Mechanical state:** whether the switch actuator is released or operated at the rotator’s open limit.
- **Electrical indication state:** which contact path the control circuit uses, and what the equipment documentation says that path signals.

A limit label or physical position alone cannot establish the electrical indication state. Nor does a continuity result by itself establish what the rotator display or controller should show. That interpretation comes from the rotator’s wiring diagram or service documentation.

If the diagram and test results conflict, stop before changing connections. Recheck that the correct switch and terminals were tested, that the actuator was in the stated condition, and that the diagram applies to the equipment being examined. Then check the documented switch adjustment and wiring information. Do not bridge contacts or change connections based on an assumed NO/NC convention. Follow the rotator documentation and applicable de-energization requirements.

### Related guides

- [ball screw actuator home position micro switch replacement](/guides/ball-screw-actuator-home-position-micro-switch-replacement/)
- [bottling machine end of stroke micro switch](/guides/bottling-machine-end-of-stroke-micro-switch/)
- [automated guided vehicle home position micro switch location](/guides/automated-guided-vehicle-home-position-micro-switch-location/)
- [accelerator pedal position stop micro switch operating force](/guides/accelerator-pedal-position-stop-micro-switch-operating-force/)

## Common interpretation errors and next checks

The most common mistake is reading NO as “open limit” and NC as “closed limit.” Those terms describe contact relationships to the unoperated actuator state; they do not name the rotator position. Another mistake is assuming that all rotators use the same contact path or place COM, NO, and NC in the same physical order. Use the exact marking and schematic instead.

If the verified contact change does not match the documented open-limit path, keep the next checks tied to that specific design. Confirm the actuator moves between released and operated positions as the limit is reached, and review the documented mechanical alignment and switch adjustment. Do not bypass safety procedures or alter the wiring merely to make an indication appear. If a closed-position switch is present, treat it as a separate comparison and consult its documentation; its arrangement does not establish the open-limit switch’s behavior.

The reliable conclusion is limited but useful: identify the terminals from the exact device documentation, test COM-NO and COM-NC with power isolated in both actuator states, and map the recorded change to the rotator’s documented circuit function. Only that equipment-specific diagram can connect the verified contact change to the open-position indication.

This concludes the explanation of antenna rotator open position micro switch NO and NC terminals.

## Sources and references

- Defense Logistics Agency ASSIST: [MIL-PRF-8805K: Switches and Switch Assemblies, Sensitive, Snap Action, General Specification For](https://quicksearch.dla.mil/qsDocDetails.aspx?ident_number=7196){: rel="nofollow noopener noreferrer" }
- Occupational Safety and Health Administration: [29 CFR 1910.333: Selection and Use of Work Practices](https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.333){: rel="nofollow noopener noreferrer" }
- Wikipedia: [Miniature snap-action switch](https://en.wikipedia.org/wiki/Miniature_snap-action_switch){: rel="nofollow noopener noreferrer" }
