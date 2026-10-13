---
title: "blow molding machine guard interlock micro switch NO and NC terminals"
description: "blow molding machine guard interlock micro switch NO and NC terminals: Understand the operating idea, essential terminology, practical checks,."
date: 2026-10-12 16:49:35 +0800
category: Applications
tags:
  - blow molding machine guard interlock micro switch NO and NC terminals
  - micro switches
  - Applications
author: editorial_team
---

A **blow molding machine guard interlock micro switch NO and NC terminals** must be understood from the switch’s own contact diagram and the machine’s wiring documentation. The terminal labels describe contact relationships at the switch; they do not, by themselves, reveal whether the guard is considered closed, whether a controller input is satisfied, or whether the machine is safe to operate.

In generic changeover terminology, COM is the common terminal, NC is normally closed, and NO is normally open. “Normally” refers to the switch actuator’s unactuated position. Moving the actuator changes which contact path is continuous. Verify the exact component’s markings and schematic rather than assuming that a physical terminal layout or a familiar convention applies. Any inspection must follow applicable deenergization and qualification requirements.

## What NO and NC mean on a micro switch

For a changeover switch, COM is the common connection that can make contact with either the NC or NO side. In the unactuated reference position, the expected relationship is continuity between COM and NC, with COM and NO open. When the actuator is operated, the contact relationships are expected to change: COM-NC opens and COM-NO becomes continuous. These descriptions concern the switch contacts, not the machine’s control logic.

The reference state matters. “Normally closed” does not mean closed whenever a machine guard is closed, and “normally open” does not mean open whenever the guard is open. The terms refer to the switch actuator being unactuated. Whether a particular guard mechanically depresses or releases the actuator, and what that movement does to the machine circuit, must be established from the equipment design and documentation.

Use the terminal symbols and connection diagram for the exact switch to identify COM, NC, and NO. Do not infer terminal identity from screw position, wire color, or a generic drawing. If the component’s markings are unclear, or its diagram does not match the expected configuration, stop and have the identification resolved by qualified personnel before testing or reconnecting wiring.

A contact-state description is also not a rating statement. The permissible load, circuit function, and terminal identification must come from documentation for the exact switch and equipment. Generic terminal terminology cannot establish suitability for a particular circuit or load.

## blow molding machine guard interlock micro switch NO and NC terminals: trace the contact paths

Trace the two contact paths at the switch, first with its actuator unactuated and then in the operated position. In the unactuated reference state, check the documented COM-NC path as the expected closed contact path and COM-NO as the expected open path. With the actuator operated, the expected paths reverse: COM-NC is open and COM-NO is closed. These are switch-level relationships; confirm the actual device schematic before applying them.

For a guard interlock, the switch may be connected into a machine circuit, but the terminal labels alone do not disclose how that circuit interprets either contact. The machine’s guard-closed logic depends on its wiring and control design. The guard’s mechanical position, the actuator’s position, the switch contact state, a controller input state, and the machine’s actual safety status are distinct things. Do not treat one as proof of another.

Use the machine wiring documentation to follow the relevant conductors from the switch into the equipment circuit. Compare the documented terminal designations and circuit function with the markings on the installed component. If the machine documentation does not establish which path corresponds to the intended guard function, do not guess from NO or NC terminology. Obtain qualified help to resolve the circuit identity.

A continuity result at COM-NC or COM-NO can show whether that isolated switch path is open or continuous in the tested actuator position. It cannot, by itself, show that the guard interlock is correctly wired, that a controller recognizes the intended input, or that the machine reaches a safe state when the guard changes position. Those conclusions require machine-level verification against the applicable equipment documentation and procedures.

## How to verify the micro switch terminals safely

Before accessing the switch or its wiring, follow the site’s applicable deenergization and qualification requirements. The verification described here is a de-energized contact check, not a live circuit test. If you are not qualified to isolate or assess the equipment, leave the work to qualified personnel. Do not probe an energized circuit or treat a contact reading as permission to operate the machine.

With the switch isolated from the circuit as required by the equipment procedure, identify COM, NC, and NO from the component markings and exact-device connection diagram. Use a meter’s continuity function across COM-NC, then across COM-NO. Record the results with the actuator unactuated. If the component documentation confirms a changeover arrangement, the expected reference results are COM-NC continuous and COM-NO open.

Change the actuator position only as permitted by the equipment procedure. Repeat the measurements across the same terminal pairs. For the stated changeover behavior, the operated-position results are expected to be COM-NC open and COM-NO continuous. If readings do not change as documented, or the actual markings do not support these expected pairs, stop rather than forcing a conclusion from generic terminology.

Compare the observations with both the switch diagram and the machine wiring documentation. A de-energized continuity check can establish the observed open or continuous state of a tested, isolated contact path under the test conditions. It cannot validate the complete interlock circuit, controller response, guard function, or machine safety. Do not use a bench result as a substitute for machine-level verification, and do not reconnect or return equipment to service unless the prescribed process is completed by qualified personnel.

### Related guides

- [ball screw actuator home position micro switch replacement](/guides/ball-screw-actuator-home-position-micro-switch-replacement/)
- [bottling machine end of stroke micro switch](/guides/bottling-machine-end-of-stroke-micro-switch/)
- [automated guided vehicle home position micro switch location](/guides/automated-guided-vehicle-home-position-micro-switch-location/)
- [accelerator pedal position stop micro switch operating force](/guides/accelerator-pedal-position-stop-micro-switch-operating-force/)

## When terminal readings do not match expectations

An unexpected reading is a reason to investigate, not proof of a particular fault. Possible explanations include misidentified terminals, a contact arrangement different from the assumed changeover pattern, actuator position or mechanical alignment, damaged wiring that has not been fully isolated from the measurement, or a failed switch. The available contact reading alone does not identify which explanation applies.

Stop if the observed states conflict with the exact switch documentation, if terminal identity remains uncertain, or if the guard does not produce the response specified for the equipment. Do not bridge contacts, bypass the interlock, or operate the machine with a defeated guard. These actions can conceal the fault and do not verify protective function.

Have qualified personnel compare the installed switch, machine wiring diagram, and required machine-level test procedure. The documentation should govern terminal identification, circuit function, and permissible load for the exact switch and equipment. Restore operation only through the applicable qualified process; a matching continuity pattern at the switch alone is not evidence that the entire guard-interlock system functions correctly.

The **blow molding machine guard interlock micro switch NO and NC terminals** identify contact paths by reference to the actuator’s unactuated state. Trace COM-NC and COM-NO at the isolated switch, confirm the exact schematic and machine wiring, and keep the contact result separate from any conclusion about guard logic or machine safety.

## Sources and references

- Defense Logistics Agency ASSIST: [MIL-PRF-8805K: Switches and Switch Assemblies, Sensitive, Snap Action, General Specification For](https://quicksearch.dla.mil/qsDocDetails.aspx?ident_number=7196){: rel="nofollow noopener noreferrer" }
- Occupational Safety and Health Administration: [29 CFR 1910.333: Selection and Use of Work Practices](https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.333){: rel="nofollow noopener noreferrer" }
- Wikipedia: [Miniature snap-action switch](https://en.wikipedia.org/wiki/Miniature_snap-action_switch){: rel="nofollow noopener noreferrer" }
