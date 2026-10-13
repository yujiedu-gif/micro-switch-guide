---
title: "Aircraft cockpit push button micro switch NO and NC terminals"
description: "aircraft cockpit push button micro switch NO and NC terminals: Understand the operating idea, essential terminology, practical checks, limitations, and."
date: 2026-10-12 17:55:05 +0800
category: Applications
tags:
  - aircraft cockpit push button micro switch NO and NC terminals
  - micro switches
  - Applications
author: editorial_team
---

An aircraft cockpit push button micro switch NO and NC terminals should be identified by the exact switch and assembly documentation, not by a generic assumption about physical layout. On a documented changeover arrangement, normally open (NO) and normally closed (NC) describe contact relationships relative to the micro switch’s unactuated state. They do not, by themselves, describe whether the cockpit button appears pushed, released, or latched. To verify terminal states, the switch must be isolated and de-energized, then checked in both relevant actuator positions under an appropriate procedure. The observed results should be recorded and compared with the device documentation. A component-level terminal check does not establish the behavior or serviceability of the aircraft circuit around it.

## Aircraft cockpit push button micro switch NO and NC terminals: what the labels mean

For generic changeover terminology, COM is the common terminal, NO is the normally open terminal, and NC is the normally closed terminal. These names refer to the contact arrangement at the micro switch, with NO and NC defined relative to the switch’s unactuated state. The exact device schematic must be checked before applying that terminology to a particular assembly.

In a changeover arrangement, the common terminal is the connection that changes between the two contacts as the micro switch actuator moves. In the unactuated reference state, COM is connected to NC and not to NO. When the switch is actuated, the contact relationship changes: COM connects to NO and no longer connects to NC. This explains the labels as contact-state descriptions, not as universal instructions for interpreting the appearance of a cockpit control.

The visible button position is not the reference that defines NO and NC. A button may be visibly out while an internal mechanism holds the micro switch actuator in a different position, or the button may move without using this particular contact arrangement. The labels alone cannot establish how a specific assembly is mechanically coupled. Confirm the switch schematic and the assembly documentation before mapping a visible button position to the micro switch’s unactuated or actuated state.

A terminal label also does not establish what a circuit does with the contact change. The electrical function depends on the actual circuit and equipment design. Therefore, a statement such as “the button is off, so COM must be on NC” is not justified without knowing the mechanism’s reference state and the documented terminal arrangement. Identify the micro switch terminals from the exact device information rather than inferring them from their physical placement or from the external control’s position.

## How the micro switch changes contacts when the button moves

A micro switch contact change occurs when its actuator is mechanically moved from the unactuated condition to the actuated condition. In a documented COM-NO-NC changeover arrangement, that movement changes which contact is connected to COM. The released and actuated states should be treated as states of the micro switch actuator, not automatically as synonyms for a cockpit button being out or in.

The push button’s external action is a separate question. A control may be momentary, or it may have an externally maintained or latched position. That behavior describes how the button or its surrounding mechanism stays or returns; it does not redefine NO and NC. A momentary button may move the switch actuator only while pressed, while a maintained mechanism may hold a position. Whether either arrangement is used, and how it couples to the micro switch, must be established from documentation for that assembly. Do not infer a cockpit control’s latching behavior from the micro switch terminal names.

This explanation applies only to assemblies that actually use a micro switch with the documented changeover arrangement. Not every cockpit push button is known to contain a micro switch, and the terminal arrangement of a specific assembly cannot be assumed from the word “push button.” If a device uses different contacts, has different markings, or lacks a confirmed schematic, the generic COM-NO-NC relationship may not describe it. Resolve that uncertainty using the exact switch and equipment documentation rather than applying a familiar layout by analogy.

The distinction matters during verification: observing a button move does not, by itself, prove the micro switch has changed state. The button’s mechanical path and the internal actuator’s state must be understood for the specific assembly. Likewise, a contact change at the component does not specify the effect on the aircraft system. That effect depends on the surrounding circuit and its function, which are outside a terminal-state check.

## Verify NO and NC states with an isolated continuity check

A continuity check is meaningful only when performed under a defined, isolated condition and with the actuator placed in identified states. For a component-level check, the assembly must be isolated and de-energized before measurement. Do not use circuit behavior or a visible button position as a substitute for identifying the micro switch’s terminals and actuator states.

Use the exact switch schematic and assembly documentation to identify COM, NO, and NC and to determine which mechanical positions correspond to the micro switch’s released and actuated states. Then check COM-to-NC and COM-to-NO in each of those two states. Record what was observed for each pair and each state, and compare those observations with the documented contact arrangement. For a standard documented changeover relationship, the expected pattern is COM-to-NC connected and COM-to-NO not connected in the unactuated state, with the relationships reversed in the actuated state. Apply that expectation only when the specific device documentation confirms that arrangement.

Do not infer terminal identity from where a terminal sits on the housing. Do not infer the contact result from a label alone, a click, or the external button position. Those observations are not a substitute for the schematic, the identified actuator states, and the measured results. If the assembly cannot be isolated, terminal identification is uncertain, the actuator state cannot be established, or the observed results do not match the applicable documentation, the check does not resolve the terminal behavior. Stop short of assigning a cause from that result alone.

Keep a clear record of the tested terminal pair, the micro switch state used, and the observed continuity result. The purpose is to verify the component’s contact relationships under the stated conditions, not to diagnose every part of an installed control. A reading taken through connected aircraft wiring may reflect paths elsewhere in the circuit, so it cannot automatically be treated as the isolated micro switch’s contact state. The exact test setup and maintenance method must follow the applicable equipment procedures.

### Related guides

- [ball screw actuator home position micro switch replacement](/guides/ball-screw-actuator-home-position-micro-switch-replacement/)
- [bottling machine end of stroke micro switch](/guides/bottling-machine-end-of-stroke-micro-switch/)
- [automated guided vehicle home position micro switch location](/guides/automated-guided-vehicle-home-position-micro-switch-location/)
- [accelerator pedal position stop micro switch operating force](/guides/accelerator-pedal-position-stop-micro-switch-operating-force/)

## What terminal checks cannot establish about a cockpit control

A component-level continuity result does not establish the function of the full aircraft circuit, the state of a flight system, or the serviceability of the complete cockpit control. It verifies only the contact relationship observed at the tested terminals and states, under the conditions of that check. Other wiring, equipment, control logic, or mechanical parts may affect system behavior. Do not treat a matching component-level result as proof that the aircraft circuit operates as intended.

Terminal layouts and contact arrangements can differ. The connection diagram, terminal markings, circuit function, and permissible load documented for the exact switch and equipment govern; a generic physical-layout inference is not sufficient. This also means that a general COM-NO-NC description should not be used to identify an undocumented terminal or to conclude that a particular cockpit assembly uses a changeover micro switch.

Electrical work has an additional boundary. Under the cited United States workplace rule, exposed live parts generally must be de-energized before work; a qualified person must verify the de-energized condition with test equipment; and work on energized parts is limited to qualified persons. Verify applicable requirements for the work context. Aircraft maintenance and return-to-service decisions must follow approved procedures and be made by qualified personnel. A terminal check described here does not authorize maintenance or establish return-to-service status.

The practical conclusion is limited: use the exact documentation to identify the device and its reference states, verify COM-to-NC and COM-to-NO in both released and actuated positions only under an isolated, de-energized procedure, and record the observed results. The aircraft cockpit push button micro switch NO and NC terminals describe a component’s contact relationships, not a universal button position or a complete aircraft-system function.

## Sources and references

- Defense Logistics Agency ASSIST: [MIL-PRF-8805K: Switches and Switch Assemblies, Sensitive, Snap Action, General Specification For](https://quicksearch.dla.mil/qsDocDetails.aspx?ident_number=7196){: rel="nofollow noopener noreferrer" }
- Occupational Safety and Health Administration: [29 CFR 1910.333: Selection and Use of Work Practices](https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.333){: rel="nofollow noopener noreferrer" }
- Wikipedia: [Miniature snap-action switch](https://en.wikipedia.org/wiki/Miniature_snap-action_switch){: rel="nofollow noopener noreferrer" }
