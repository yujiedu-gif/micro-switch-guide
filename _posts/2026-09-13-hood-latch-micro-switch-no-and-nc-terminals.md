---
title: "hood latch micro switch NO and NC terminals: How to Identify and Test Them"
description: "hood latch micro switch NO and NC terminals: Understand the operating idea, essential terminology, practical checks, limitations, and evidence needed for."
date: 2026-09-13 09:00:00 +0800
category: Applications
tags:
  - hood latch micro switch NO and NC terminals
  - micro switches
  - Applications
author: editorial_team
---

# Identifying NO and NC Contacts in a Hood-Latch Circuit

The **hood latch micro switch NO and NC terminals** describe electrical contact relationships, not whether the hood is physically open or closed. Their behavior depends on the switch actuator’s position. A latch assembly may use a different sensing design or may not contain a micro switch at all, so identify the component before testing it. When a switch is present, its terminal markings and the equipment’s connection diagram are the best references for interpreting its connections. A continuity check can help verify contact behavior, but an unexpected reading is a reason to pause and investigate, not to guess at terminal identity or conclude that the entire vehicle circuit has failed.

## What NO and NC mean on a hood latch micro switch NO and NC terminals

In generic changeover-switch terminology, **COM** means common, **NC** means normally closed, and **NO** means normally open. These labels refer to the switch’s contact arrangement in its normal, unactuated state. For a conventional changeover micro switch, COM–NC has continuity while the actuator is unactuated, and COM–NO does not. When the actuator is operated, the contact paths change state: COM–NC opens and COM–NO closes.

“Normal” here means the actuator’s unactuated position. It does not mean that the hood is in its usual position, that the latch is open, or that a dashboard indication is on or off. The latch mechanism may hold or release the switch actuator differently as the hood moves. Thus, the hood’s mechanical position and the switch’s state are related only through the design and position of the actuator; they are not interchangeable descriptions.

These state expectations apply to generic changeover terminology. Check the schematic for the exact switch before treating a terminal marking or observed reading as definitive. A device may not be a conventional changeover switch, and an installed switch may already be actuated. The equipment diagram can also clarify which contacts the circuit uses and what function they serve.

## Confirm the latch actually contains a micro switch

Do not assume every hood latch contains a discrete micro switch. Inspect the assembly for a switch body and an actuator, such as a plunger or lever, before attempting a terminal test. Some latch designs may sense position another way, or may not provide a separate serviceable switch. Without identifying the component and its terminals, a continuity test could be applied to the wrong part of the assembly.

If the switch is present, look for terminal markings and consult the circuit or connection diagram. Use the diagram to relate the terminal labels to the circuit, rather than assigning a function based on where a terminal sits physically. The connection diagram, terminal marking, circuit function, and permissible load documented for the exact switch and equipment are more reliable than a generic physical-layout inference. Wire color or the hood’s position alone does not establish which terminal is COM, NO, or NC.

The diagram and markings also set the bounds for interpreting a test. Generic COM–NC and COM–NO expectations explain the usual behavior of a changeover switch, but they do not establish the exact switch type, circuit design, or intended signal for a particular vehicle. If the component identity or terminal layout is unclear, leave it unresolved until the applicable information is available.

## Identify COM, NO, and NC with a continuity meter

A continuity check should be made with the switch deenergized. Follow applicable vehicle service precautions, switch off power, and disconnect the switch from the circuit where practical. Use the exact switch diagram or terminal markings to identify candidate terminals. Do not rely on a generic view of the switch body to decide which pin is common.

With the switch’s actuator released, check between candidate COM and NC. For a conventional changeover micro switch, that pair should show continuity. Then check candidate COM and NO; that pair should not show continuity in the unactuated state. These are contact-state expectations, not a test of whether the hood is open or closed.

Next, operate the actuator and repeat both checks. For a conventional changeover switch, the expected paths reverse: COM–NC should no longer show continuity, while COM–NO should show continuity. Keep track of whether the actuator is released or pressed for each reading. A test made while the actuator is already pressed does not represent its unactuated state, even if the hood appears to be in a familiar position.

If the circuit cannot be disconnected, or the terminal identities remain uncertain, do not interpret a reading as a direct test of the switch contacts. Consult the applicable circuit information or obtain qualified help. The test described here verifies contact behavior under the stated conditions; it does not establish that the vehicle’s full warning or safety system functions correctly.

## Interpret readings without confusing latch position and switch state

A switch with correctly marked terminals can seem reversed if its actuator is already pressed during the test. The latch’s mechanism may also change actuator position as the hood moves. Record the actuator state, not merely whether the hood is open or closed, and compare readings against the diagram and the switch’s unactuated state.

An open circuit on both tested paths, continuity on both paths, or readings that do not change when the actuator is operated do not, by themselves, identify the cause. Check whether the correct component and terminals were selected, whether the switch was isolated from the circuit where practical, whether the actuator actually moved, and whether the meter probes made contact. Also check the documented switch type. These are setup and interpretation checks, not proof that the latch, wiring, or vehicle system is faulty.

If readings still conflict with the markings or diagram, stop rather than relabeling terminals by trial and error. Recheck the exact connection information and component identity. The generic state pattern applies to a conventional changeover switch, but the supplied evidence does not establish that every latch switch uses that arrangement. Further diagnosis may be needed to determine whether the issue lies in the test setup, the switch, or another part of the circuit.

### Related guides

- [ball screw actuator home position micro switch replacement](/guides/ball-screw-actuator-home-position-micro-switch-replacement/)
- [bottling machine end of stroke micro switch](/guides/bottling-machine-end-of-stroke-micro-switch/)
- [automated guided vehicle home position micro switch location](/guides/automated-guided-vehicle-home-position-micro-switch-location/)
- [accelerator pedal position stop micro switch operating force](/guides/accelerator-pedal-position-stop-micro-switch-operating-force/)

## Reconnect and verify the hood-latch circuit safely

After testing, restore any connector that was disconnected. Confirm that the connector is secure and that wiring is routed without pinching or interfering with latch operation. Do not alter the latch or bypass the switch as a way to obtain a desired reading or indication.

Use the applicable circuit information to verify the intended signal behavior with the hood in the positions specified for that equipment. Do not assume that a particular hood position must correspond to a particular NO or NC state without the circuit information and the switch-actuator relationship. A continuity test of isolated contacts is not proof that the complete warning or safety system works as intended.

For the **hood latch micro switch NO and NC terminals**, the reliable reference is the switch’s documented terminal arrangement and the actual actuator state during the test. If the observed contact behavior disagrees with those references, do not guess at terminal identity or infer a vehicle-system fault from one reading. Seek further diagnosis using the applicable equipment information and service requirements.

## Sources and references

- Defense Logistics Agency ASSIST: [MIL-PRF-8805K: Switches and Switch Assemblies, Sensitive, Snap Action, General Specification For](https://quicksearch.dla.mil/qsDocDetails.aspx?ident_number=7196){: rel="nofollow noopener noreferrer" }
- Occupational Safety and Health Administration: [29 CFR 1910.333: Selection and Use of Work Practices](https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.333){: rel="nofollow noopener noreferrer" }
- Wikipedia: [Miniature snap-action switch](https://en.wikipedia.org/wiki/Miniature_snap-action_switch){: rel="nofollow noopener noreferrer" }
