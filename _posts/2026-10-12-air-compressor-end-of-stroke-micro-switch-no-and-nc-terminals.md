---
title: "air compressor end of stroke micro switch NO and NC terminals: What the Contacts Mean"
description: "air compressor end of stroke micro switch NO and NC terminals: Understand the operating idea, essential terminology, practical checks, limitations, and."
date: 2026-10-12 16:49:35 +0800
category: Applications
tags:
  - air compressor end of stroke micro switch NO and NC terminals
  - micro switches
  - Applications
author: editorial_team
---

An **air compressor end of stroke micro switch NO and NC terminals** check begins with the switch’s own unactuated state, not with whether the compressor is running. NO and NC describe contact relationships at rest. When the compressor mechanism reaches its travel limit and operates the switch actuator, a changeover contact set can transfer continuity from one path to the other. That transfer does not, by itself, establish what the compressor controller will do.

For a reliable check, identify the terminals from the exact device’s markings and connection diagram, observe the switch in both actuator positions, and keep switch behavior separate from wiring and controller behavior. Continuity testing requires isolated electrical power. If the intended circuit or a safe test cannot be established from the equipment documentation, have a qualified technician perform the diagnosis.

## air compressor end of stroke micro switch NO and NC terminals: Identify the contact states

For a changeover switch, **COM** means common terminal, **NC** means normally closed terminal, and **NO** means normally open terminal. “Normally” refers to the switch’s unactuated state. With a common terminal provided, the expected resting relationships are continuity between COM and NC, and no continuity between COM and NO. These terms describe contacts, not the compressor’s operating condition.

Confirm that the specific switch actually has the expected contact arrangement. Read its terminal markings and connection diagram rather than identifying terminals by their physical position, wire color, or resemblance to another switch. A generic layout is not enough to establish which terminal is common or which circuit path the equipment uses.

In a changeover contact set, operating the actuator generally transfers the common contact: COM-to-NC opens, while COM-to-NO closes. This is a description of contact behavior, not a rating or permission to connect a particular load. Use the documented circuit function and permissible load for the exact switch and equipment. The switch’s electrical ratings and connection details cannot be inferred from the NO, NC, or COM labels alone.

## What changes when the compressor mechanism reaches end of stroke

At the travel limit, a moving part of the compressor mechanism contacts the switch’s plunger or lever. If the actuator is moved far enough to operate the switch, a changeover contact set should change from its unactuated relationships to its actuated relationships. In the unactuated position, COM-NC is closed and COM-NO is open; in the actuated position, COM-NC is open and COM-NO is closed. Verify the change at the terminals rather than assuming that reaching a visible travel limit guarantees the switch has operated.

The mechanical event and the electrical response are separate observations. A moving part might reach the limit without properly engaging the actuator, or the actuator might move without producing the expected terminal change. Checking the switch at its terminals helps distinguish these possibilities from a problem farther along the circuit.

The contact transfer also does not tell you, by itself, whether the compressor should stop, continue, or signal another state. A controller may use either contact path, and its response depends on the circuit design. The switch provides a change in contact state; the controller interprets the resulting input through its wiring and logic. Do not assume that NO means “run” or NC means “stop.”

## Check NO and NC continuity safely with power isolated

Before a continuity check, disconnect and isolate electrical power. Do not use a meter’s continuity or resistance mode on an energized circuit. Follow the applicable deenergization and qualification requirements for the equipment. If you cannot confirm that power is isolated or identify the correct terminals from documentation, stop and ask a qualified technician.

Use the exact switch markings and equipment connection diagram to identify COM, NO, and NC. Where practical and appropriate, separate the switch from parallel circuit paths so other components do not affect the measurement. Do not disconnect wiring without understanding the equipment documentation and applicable requirements.

With the switch unactuated, check COM-to-NC and COM-to-NO. Record whether COM-to-NC shows continuity and COM-to-NO does not. Then operate the actuator as intended and check both pairs again. For a changeover contact set, the expected result is that COM-to-NC no longer has continuity and COM-to-NO does. The useful evidence is whether the readings change between positions, not an assumed machine-level meaning for either reading.

Do not bypass a safety-related stop circuit to make the equipment run or to test a theory. A continuity reading on an isolated switch checks its contacts; it does not prove that the wiring, controller input, or overall stop function works as intended. Those require interpretation against the equipment’s electrical documentation.

## Trace a failed end-of-stroke signal from actuator to controller

Begin with the mechanical interface. With the equipment in a safe condition, determine whether the moving part reaches the switch and operates its actuator. Look for a missed contact point or binding that prevents the intended movement. Do not force the mechanism or alter its position as part of this check.

Next, observe the terminal state. If operating the actuator does not change COM-to-NC and COM-to-NO continuity as expected, the evidence points to the switch path: the actuator may not be moving it sufficiently, the switch may be misaligned, or the switch may be damaged. A controller fault is not the first conclusion when the contact state itself has not changed.

If the terminal state changes at the switch, follow the documented wiring path and inspect its continuity and connections. A change at the switch terminals does not establish that the same signal reaches the controller. If the wiring path is intact but the controller input does not respond as expected, controller-input behavior and circuit logic remain to be assessed against the equipment documentation. Do not infer a controller defect from terminal readings alone.

This sequence separates four observations: actuator engagement, switch-terminal continuity, wiring continuity, and controller input. Unexpected stopping or failure to stop requires safe shutdown and qualified diagnosis. Do not treat every end-of-stroke fault as a pressure, motor, or pneumatic problem; first establish where the documented signal path stops behaving as expected.

### Related guides

- [ball screw actuator home position micro switch replacement](/guides/ball-screw-actuator-home-position-micro-switch-replacement/)
- [bottling machine end of stroke micro switch](/guides/bottling-machine-end-of-stroke-micro-switch/)
- [automated guided vehicle home position micro switch location](/guides/automated-guided-vehicle-home-position-micro-switch-location/)
- [accelerator pedal position stop micro switch operating force](/guides/accelerator-pedal-position-stop-micro-switch-operating-force/)

## Interpret readings without assuming a universal stop circuit

NO and NC name contact states relative to the switch’s unactuated position. They do not identify whether the compressor is running, stopped, or at a particular pressure. They also do not establish which contact the equipment uses. Relay logic, controller inputs, and wiring can change how a contact transfer appears at the machine level, so the same switch state cannot be assigned a universal “stop” or “run” meaning.

Use the equipment’s electrical documentation to confirm which path is intended, how the terminals are connected, and what the controller input should represent. Confirm terminal identity on the device instead of relying on physical layout. If the documented circuit, contact readings, and observed controller response do not agree, leave the circuit in a safe condition and seek qualified diagnosis rather than bypassing contacts or guessing at the logic.

The practical conclusion is limited but useful: a changeover switch can be checked by comparing COM-to-NC and COM-to-NO continuity in its unactuated and actuated positions, with power isolated. That check establishes contact behavior only. The equipment documentation is needed to determine whether the actuator, wiring, and controller input together produce the intended end-of-stroke response. An **air compressor end of stroke micro switch NO and NC terminals** reading must therefore be interpreted as one point in the documented signal path, not as a standalone diagnosis of the compressor.

## Sources and references

- Defense Logistics Agency ASSIST: [MIL-PRF-8805K: Switches and Switch Assemblies, Sensitive, Snap Action, General Specification For](https://quicksearch.dla.mil/qsDocDetails.aspx?ident_number=7196){: rel="nofollow noopener noreferrer" }
- Occupational Safety and Health Administration: [29 CFR 1910.333: Selection and Use of Work Practices](https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.333){: rel="nofollow noopener noreferrer" }
- Wikipedia: [Miniature snap-action switch](https://en.wikipedia.org/wiki/Miniature_snap-action_switch){: rel="nofollow noopener noreferrer" }
