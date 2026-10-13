---
title: "automated guided vehicle end of stroke micro switch NO and NC terminals: How They Work"
description: "automated guided vehicle end of stroke micro switch NO and NC terminals: Understand the operating idea, essential terminology, practical checks,."
date: 2026-10-12 16:49:35 +0800
category: Applications
tags:
  - automated guided vehicle end of stroke micro switch NO and NC terminals
  - micro switches
  - Applications
author: editorial_team
---

An **automated guided vehicle end of stroke micro switch NO and NC terminals** arrangement can indicate whether a mechanical actuator is released or operated. The contact-state terms describe the switch contacts, not a guaranteed vehicle command. The relevant travel-limit detection method and circuit logic depend on the specific AGV installation.

To check the switching sequence, first identify the terminals from the exact switch markings and connection diagram. Then, with power safely isolated and the relevant conductors disconnected as appropriate, test the switch contacts in both actuator states. Comparing those results with the connected wiring and input behavior helps separate a contact-state issue from a problem elsewhere in the circuit.

## What the end-of-stroke micro switch detects on an AGV

In an AGV design that uses a micro switch for end-of-stroke detection, the switch responds to a mechanical travel limit. As the moving part reaches the relevant position, it interacts with the switch actuator. The actuator’s movement can change the state of the switch contacts, providing an electrical indication of the mechanical event.

This description applies only where the particular AGV design uses this type of switch for that purpose. It does not establish that all automated guided vehicles use an end-of-stroke micro switch. Other designs may detect travel limits differently, and the available information does not define those alternatives.

Keep the mechanical event and the electrical indication distinct. Reaching a travel limit is a physical condition; a change in NO or NC continuity is a contact condition. How that contact change is connected to an AGV input, and what the vehicle does in response, depends on the actual installation. A contact-state reading alone does not establish the vehicle’s motion or stopping behavior.

For an accurate check, identify which moving part engages the actuator and how the switch is intended to be actuated in that installation. Do not assume the actuator reaches its operating point merely because a controller shows a status change, or infer the switch’s contact state from vehicle behavior. Verify the physical switch and its documented connections directly.

## automated guided vehicle end of stroke micro switch NO and NC terminals: released and operated states

For the contact-state check, the **released state** means the actuator is not being pressed; the **operated state** means the actuator is actuated. In generic changeover terminology, COM means common, NC means normally closed, and NO means normally open. Confirm the exact device schematic before relying on those symbols for a particular switch.

The NO contact is open in the released state and closes when the actuator is operated. The NC contact is closed in the released state and opens when the actuator is operated. These descriptions concern the contact behavior in relation to the switch’s released state. They do not, by themselves, specify the circuit’s logic or the AGV’s response.

Do not assign terminals by physical layout, wire color, or controller indication alone. Use the connection diagram and terminal markings for the exact switch and equipment, together with the circuit function and permissible load documented for that installation. Actual terminal identification and contact arrangement must be verified at the device.

A useful check records both contacts in both actuator states. For example, note the measured condition of the NO pair with the actuator released, then operate the actuator and note whether that pair changes. Repeat for the NC pair. The expected pattern is an open-to-closed change for NO and a closed-to-open change for NC. If the observed pattern differs, verify terminal identification and actuator movement before drawing a conclusion about a fault.

## How to verify NO and NC continuity safely

Use a continuity or resistance meter only after isolating power in accordance with applicable deenergization and qualification requirements. Disconnect the relevant switch conductors as appropriate so the measurement is made across the intended switch contacts rather than through an unknown connected circuit. Follow the applicable safe service procedure; a powered circuit is not the place for a continuity check.

With the switch isolated for measurement, identify the relevant terminal pairs from the exact device schematic and markings. Record the measurement for the NO contact pair with the actuator released. Then actuate the switch and repeat the measurement. Test the NC contact pair in the same two states. Compare the results with the contact-state map: NO should be open when released and closed when operated; NC should be closed when released and open when operated.

The test depends on correctly identifying the terminals and observing the actual actuator state. A measurement taken across the wrong pair, or with the actuator not in the intended state, cannot confirm the expected switching sequence. If the mechanical setup is unclear, verify the installation documentation and observe whether the actuator reaches its intended operating point. Do not substitute wire color or a controller display for direct terminal identification and measurement.

The continuity results establish the switch-contact behavior under the tested conditions. They do not establish how the AGV’s full circuit is configured or whether an input will respond. Keep the switch-level measurement separate from later checks of the connected wiring and input path.

## Separate a switch fault from wiring or input behavior

If continuity changes at the switch in the expected way, that supports the conclusion that the tested contacts changed state under those conditions. It does not prove that the connected wiring carries that change correctly or that the AGV input recognizes it. If the input does not respond as expected, check the connected wiring and input path using the vehicle’s safe service procedure.

If continuity does not change as expected, first confirm that the correct terminals were tested and that the actuator actually moved between released and operated states. Recheck the device markings and schematic, and verify that the mechanical actuator reaches its intended operating point. Only after those checks should the result be treated as evidence of a possible switch-contact problem; a single unexplained reading is not enough to establish its cause.

Keep the diagnostic layers separate: actuator movement, switch-contact continuity, connected wiring, and AGV input behavior. A mismatch between layers helps locate where further verification is needed, but it does not identify a specific failed component on its own. Controller indications can help assess input behavior, but they do not determine whether the switch’s NO or NC contact is open or closed. Verify that state at the switch terminals.

### Related guides

- [ball screw actuator home position micro switch replacement](/guides/ball-screw-actuator-home-position-micro-switch-replacement/)
- [bottling machine end of stroke micro switch](/guides/bottling-machine-end-of-stroke-micro-switch/)
- [automated guided vehicle home position micro switch location](/guides/automated-guided-vehicle-home-position-micro-switch-location/)
- [accelerator pedal position stop micro switch operating force](/guides/accelerator-pedal-position-stop-micro-switch-operating-force/)

## Limits of the terminal-state interpretation

NO and NC describe the contacts relative to the switch’s released state. Those names do not guarantee a particular stop, motion command, or other vehicle action when a contact changes. Circuit logic, safety architecture, and input configuration determine how the AGV uses that change. Do not infer a universal circuit or vehicle response from the contact labels alone.

Before making a functional conclusion, verify the actual terminal markings, actuator setup, circuit diagram, and wiring for the specific installation. Use the documented connection diagram, circuit function, and permissible load for the exact switch and equipment rather than inferring a connection or rating from generic terminal layout. If the observed contact sequence and the documented circuit behavior disagree, treat the interpretation as unresolved until the installation is checked.

In short, test the NO and NC contacts at the isolated switch in both released and operated states, then assess the wiring and input separately under the vehicle’s safe service procedure. The **automated guided vehicle end of stroke micro switch NO and NC terminals** identify contact behavior; they do not, by themselves, establish what the AGV will do.

## Sources and references

- Defense Logistics Agency ASSIST: [MIL-PRF-8805K: Switches and Switch Assemblies, Sensitive, Snap Action, General Specification For](https://quicksearch.dla.mil/qsDocDetails.aspx?ident_number=7196){: rel="nofollow noopener noreferrer" }
- Occupational Safety and Health Administration: [29 CFR 1910.333: Selection and Use of Work Practices](https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.333){: rel="nofollow noopener noreferrer" }
- Wikipedia: [Miniature snap-action switch](https://en.wikipedia.org/wiki/Miniature_snap-action_switch){: rel="nofollow noopener noreferrer" }
