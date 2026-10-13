---
title: "Antenna rotator travel limit micro switch wiring: contacts and circuit checks"
description: "antenna rotator travel limit micro switch wiring: Understand the operating idea, essential terminology, practical checks, limitations, and evidence needed."
date: 2026-10-12 16:49:35 +0800
category: Applications
tags:
  - antenna rotator travel limit micro switch wiring
  - micro switches
  - Applications
author: editorial_team
---

An **antenna rotator travel limit micro switch wiring** arrangement must match the rotator’s actual circuit: the switch may interrupt drive power, or it may send a limit signal to a controller. Those are different functions, and the right contact cannot be chosen from a generic diagram or the switch’s physical appearance. Confirm the rotator schematic, switch markings, and applicable ratings before making a connection.

The verification path is equally important. With power removed, identify COM, NO, and NC from the markings and check contact behavior with continuity measurements. Then compare the results with the circuit design. A powered operational check comes only after the wiring and ratings have been confirmed, and it must follow the equipment’s prescribed procedure.

## What the antenna rotator travel limit micro switch wiring must accomplish

At the travel endpoint, the micro switch changes a contact state so the rotator’s designed circuit can respond to the limit. What that response is depends on the equipment: the contact may open or close a drive-power path, or it may change a signal monitored by a controller. The switch’s role in the circuit, rather than its name alone, determines how it should be wired.

For a power-interruption design, the limit contact is part of the specified drive circuit. Reaching the endpoint changes that path so the rotator drive is interrupted as designed. For a controller-sensing design, the switch changes an input state, while the controller’s circuit determines the response. Do not assume that a sensing contact carries motor current, or that a motor-power contact is a controller input.

Before connecting anything, use the rotator’s connection diagram and the exact switch documentation to establish the intended function. The diagram must identify the relevant circuit and permissible load. If the equipment documentation does not show whether the switch interrupts power or reports a limit state, the topology remains unresolved. Do not supply a generic wiring arrangement in its place.

## Identify COM, NO, and NC on the micro switch

Use the switch’s terminal markings and documentation to identify the contacts. In generic changeover terminology, COM means common terminal, NC means normally closed terminal, and NO means normally open terminal. These names do not establish where a terminal sits on the switch body. Verify the exact device schematic rather than inferring assignments from position, shape, or appearance.

Check contact behavior with the circuit de-energized. First, make sure the switch is isolated from powered equipment and that the measurement setup is appropriate for the circuit. Use a continuity check to record which contacts are connected at rest. Then operate the actuator as intended and check which contacts change state. The observed result, together with the switch documentation, establishes the contact behavior for that device.

“Normally” refers to the contact state before the actuator changes it, not to an assumed rotator direction or an unverified position in a wiring diagram. Do not conclude that NC must be the correct limit contact merely because a particular circuit is expected to stop at an endpoint. The rotator schematic determines the required contact and how its state is interpreted. If the measured states do not agree with the documentation, stop and resolve the discrepancy before connection.

## Wire the antenna rotator travel limit micro switch wiring for its circuit type

For a design that interrupts motor power, follow the rotator schematic to identify the specified drive path and contact. Confirm that the switch’s permissible load covers the actual circuit conditions. The connection diagram, terminal markings, circuit function, and load documentation for the exact switch and equipment govern the wiring; physical terminal layout alone does not. There is no universal COM, NO, or NC assignment for all rotators.

For a controller-sensing design, follow the controller’s input documentation and wire the switch as the specified signal path. Keep this function distinct from motor-current interruption. A controller input may use a different circuit arrangement from a drive-power path, so a diagram intended for one function cannot be assumed suitable for the other. The documentation must establish the intended input behavior and relevant electrical limits.

In either case, match the device terminal identification to the documented circuit function before connecting conductors. Do not copy a diagram unless it matches the actual rotator, controller, and switch. Terminal assignments and wiring topology vary. If a schematic, marking, or required connection is unclear, leave the circuit unconnected until the applicable documentation resolves it. Generic terminal names are not enough to establish a safe or correct topology.

## Check ratings, isolation, and load conditions before connection

Compare the switch’s documented electrical rating with the circuit’s voltage and current and with the actual load. In particular, establish whether the contact is switching motor power or serving a controller input. A motor or other inductive-load condition must be addressed by the equipment and switch documentation; do not assume that a rating stated for another load or circuit applies. Any required provisions for the load must also come from the applicable documentation.

Confirm the connection diagram, terminal markings, circuit function, and permissible load for the exact switch and equipment. Do not infer compatibility from the fact that a component has COM, NO, and NC terminals. If voltage, current, load conditions, topology, or required circuit provisions cannot be confirmed, do not proceed with the connection. This guide does not establish the ratings or compatibility of an unidentified switch or rotator.

For electrical work, follow applicable requirements for the work setting. Under the cited United States workplace rule, exposed live parts generally must be deenergized before work, a qualified person must verify the deenergized condition with test equipment, and work on energized parts is limited to qualified persons. Verify all applicable requirements. Do not make continuity measurements on an energized circuit.

### Related guides

- [ball screw actuator home position micro switch replacement](/guides/ball-screw-actuator-home-position-micro-switch-replacement/)
- [bottling machine end of stroke micro switch](/guides/bottling-machine-end-of-stroke-micro-switch/)
- [automated guided vehicle home position micro switch location](/guides/automated-guided-vehicle-home-position-micro-switch-location/)
- [accelerator pedal position stop micro switch operating force](/guides/accelerator-pedal-position-stop-micro-switch-operating-force/)

## Verify continuity and test the travel limit safely

Use an ordered check:

1. **De-energize the circuit.** Follow the applicable work requirements and equipment procedure before handling conductors or measuring continuity. A qualified person must verify the deenergized condition with test equipment where the cited workplace rule applies.
2. **Confirm the switch identity and terminals.** Read the exact switch markings and schematic. Do not substitute a physical-layout guess for terminal identification.
3. **Check the contacts.** With power removed, use continuity measurements to establish the state at rest and again with the actuator operated. Compare both results with the switch documentation and the state required by the rotator circuit.
4. **Compare the wiring with the equipment diagram.** Confirm whether the contact interrupts drive power or provides a controller signal, and check that the selected contact and load match the documented design.
5. **Reconnect only after the checks agree.** Follow the equipment’s prescribed procedure for a cautious operational limit test. Confirm that the drive stops or that the controller registers the limit, according to the actual circuit design.

If the contact state, schematic, or observed operation does not agree, de-energize the circuit and reassess the contact choice and wiring. Do not bypass the limit to make the system operate. Numerical travel limits are specified by the applicable specification sheet; they must not be inferred from the component category. The correct result is established by the exact equipment documentation and verified circuit behavior, not by a universal wiring diagram.

This concludes the explanation of antenna rotator travel limit micro switch wiring.

## Sources and references

- Defense Logistics Agency ASSIST: [MIL-PRF-8805K: Switches and Switch Assemblies, Sensitive, Snap Action, General Specification For](https://quicksearch.dla.mil/qsDocDetails.aspx?ident_number=7196){: rel="nofollow noopener noreferrer" }
- Occupational Safety and Health Administration: [29 CFR 1910.333: Selection and Use of Work Practices](https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.333){: rel="nofollow noopener noreferrer" }
- Wikipedia: [Miniature snap-action switch](https://en.wikipedia.org/wiki/Miniature_snap-action_switch){: rel="nofollow noopener noreferrer" }
