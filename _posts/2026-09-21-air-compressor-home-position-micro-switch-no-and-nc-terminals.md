---
title: "air compressor home position micro switch NO and NC terminals"
description: "air compressor home position micro switch NO and NC terminals: Understand the operating idea, essential terminology, practical checks, limitations, and."
date: 2026-09-21 09:00:00 +0800
category: Applications
tags:
  - air compressor home position micro switch NO and NC terminals
  - micro switches
  - Applications
author: editorial_team
---

An **air compressor home position micro switch NO and NC terminals** question involves two separate things: the switch’s contact state and the compressor mechanism’s position. The terminal labels describe how contacts relate to the switch actuator’s unoperated state. “Home,” by contrast, describes a position in the compressor mechanism. One does not establish the other.

A bounded check therefore has two parts. First identify the terminals and verify their continuity with electrical power isolated, in both unoperated and actuated positions. Then compare the observed state at the compressor’s home position with the compressor’s wiring information. A contact test can confirm a switch state, but it does not by itself establish how the compressor control circuit uses that state.

## What NO and NC mean on an air compressor home position micro switch NO and NC terminals

For a changeover switch, **COM** means common, **NO** means normally open, and **NC** means normally closed. “Normally” refers to the switch actuator’s unoperated position, not to the compressor’s usual operating condition or its home position. Confirm the terminology against the exact device schematic where available.

In the unoperated state, the expected continuity pattern is:

- **COM–NO:** open, with no continuity.
- **COM–NC:** closed, with continuity.

In the actuated state, the expected pattern reverses:

- **COM–NO:** closed, with continuity.
- **COM–NC:** open, with no continuity.

This reciprocal pattern describes the contact states, not a wiring instruction or a control signal. It also assumes the switch has these COM, NO, and NC terminals and uses the stated changeover arrangement. Do not identify terminals from their physical location alone. Use the switch markings and its connection diagram, and check the compressor documentation for the circuit function and permissible load.

The word “unoperated” is a reference to the switch actuator’s state. It does not mean that the compressor is off, unloaded, or at home. Likewise, “actuated” says that the actuator has operated; it does not tell you which compressor position caused that operation. Those distinctions matter when interpreting an otherwise correct continuity result.

## Relate the switch actuator state to the compressor home position

A compressor’s home position is a mechanism position. In a design that uses a micro switch for that position, a mechanism part may move the actuator, keep it in contact, or release it as the mechanism reaches or leaves home. The switch’s state at home depends on that specific mechanical relationship. The name “home-position switch” alone does not show whether the actuator is operated or unoperated at home.

To relate the positions, observe the actuator condition at the defined home point using the equipment’s service information and the applicable qualified procedure. Determine whether the mechanism is pressing or otherwise operating the actuator, or has released it. Then interpret the contact pattern using the unoperated and actuated definitions. If the mechanism releases the actuator at home, the unoperated pattern is expected there; if it operates the actuator, the actuated pattern is expected. These are conditional interpretations, not assumptions about every compressor.

Do not force the actuator or move compressor parts based on a generic description. The design, actuator travel, and mechanism arrangement are not established by terminal labels. Other compressors may use a different sensor or arrangement, so the existence and role of this switch must also be confirmed for the equipment being checked.

## Check NO and NC continuity with power isolated

Electrical power must be isolated and the circuit confirmed de-energized before checking continuity. Follow applicable deenergization and qualification requirements. If you are not qualified to perform the work, or cannot establish that the circuit is de-energized, stop and refer the task to a qualified technician. Do not use a continuity check as a reason to handle energized wiring.

Use the switch markings and exact-device connection information to identify COM, NO, and NC. Where needed for a valid component check, disconnect the switch from the circuit as appropriate under the equipment procedure; a connected circuit can affect what a measurement represents. Do not infer terminal identity from position or appearance. If markings and documentation do not agree, stop rather than guessing.

With the actuator unoperated, check between COM and NO, then between COM and NC. The expected results are open between COM–NO and closed between COM–NC. Without restoring power, place the actuator in its actuated position using the applicable procedure and check the same pairs again. The expected results reverse: closed between COM–NO and open between COM–NC. A continuity tester’s indication should be interpreted according to the tester’s instructions; the essential comparison is whether each pair is open or closed in each defined actuator state.

Record which actuator condition was tested, rather than labeling a reading simply “home” or “not home.” If a result differs from the expected pattern, first recheck terminal identification, the actuator state, and the exact switch documentation. Stop if the readings still do not match the markings or documentation. A mismatch does not, by itself, identify a cause or establish that the compressor control circuit has been diagnosed.

### Related guides

- [ball screw actuator home position micro switch replacement](/guides/ball-screw-actuator-home-position-micro-switch-replacement/)
- [bottling machine end of stroke micro switch](/guides/bottling-machine-end-of-stroke-micro-switch/)
- [automated guided vehicle home position micro switch location](/guides/automated-guided-vehicle-home-position-micro-switch-location/)
- [accelerator pedal position stop micro switch operating force](/guides/accelerator-pedal-position-stop-micro-switch-operating-force/)

## Map verified contact states to the compressor wiring information

After verifying the switch contacts, establish which actuator state occurs at the compressor’s home position and compare that observation with the compressor’s wiring diagram or service information. The documentation is needed to determine how the circuit uses the contacts. A circuit may use one contact pair or another, but the NO and NC labels alone do not reveal which state the compressor control expects.

Do not infer a control signal, wiring arrangement, permissible load, or safety function from the switch’s terminal names or a continuity result. Use the connection diagram, terminal markings, circuit function, and permissible load documented for the exact switch and equipment. Do not substitute a generic physical-layout assumption for that information. If the diagram is unavailable or the observed states cannot be reconciled with it, leave the circuit function unresolved rather than concluding that the switch or compressor is faulty.

Contact-state verification is limited: it establishes whether the tested pairs are open or closed in the tested actuator positions. It does not establish how the rest of the compressor circuit responds. Wiring work involving uncertain connections or mains voltage should be referred to a qualified technician. The **air compressor home position micro switch NO and NC terminals** can be interpreted reliably only by keeping the actuator reference, mechanism position, and documented circuit function separate.

## Sources and references

- Defense Logistics Agency ASSIST: [MIL-PRF-8805K: Switches and Switch Assemblies, Sensitive, Snap Action, General Specification For](https://quicksearch.dla.mil/qsDocDetails.aspx?ident_number=7196){: rel="nofollow noopener noreferrer" }
- Occupational Safety and Health Administration: [29 CFR 1910.333: Selection and Use of Work Practices](https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.333){: rel="nofollow noopener noreferrer" }
- Wikipedia: [Miniature snap-action switch](https://en.wikipedia.org/wiki/Miniature_snap-action_switch){: rel="nofollow noopener noreferrer" }
