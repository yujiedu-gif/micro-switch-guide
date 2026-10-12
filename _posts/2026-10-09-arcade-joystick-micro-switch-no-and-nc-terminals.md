---
title: "arcade joystick micro switch NO and NC terminals: What They Mean"
description: "arcade joystick micro switch NO and NC terminals: Understand the operating idea, essential terminology, practical checks, limitations, and evidence needed."
date: 2026-10-09 09:00:00 +0800
category: Applications
tags:
  - arcade joystick micro switch NO and NC terminals
  - micro switches
  - Applications
author: editorial_team
---

An **arcade joystick micro switch NO and NC terminals** can be understood by the contact paths they form in the switch’s unactuated and actuated states. On a typical changeover switch, COM connects to NC when the actuator is released, and COM connects to NO when the actuator is pressed. That describes the switch contacts, not a joystick direction or a controller signal voltage.

Use the exact switch markings or connection diagram to identify its terminals, then verify the expected paths with power disconnected. Do not assume a terminal’s position, wire color, or joystick direction identifies its contact function. Joystick and switch configurations can differ, so the particular device’s documentation and measured behavior matter.

## What arcade joystick micro switch NO and NC terminals mean

NO means normally open, and NC means normally closed. “Normally” refers to the switch’s unactuated condition, with its actuator at rest. These names describe contact relationships in that reference state; they do not, by themselves, specify the joystick’s direction, the controller’s logic, or whether a signal is energized.

In a typical changeover arrangement, COM is the common terminal. With the switch released, the COM-NC path is closed and the COM-NO path is open. When the actuator is pressed, the contact changes: COM-NO is closed and COM-NC is open. These terms describe which pair of contacts connects in each state. They do not establish what the joystick or controller does with that change.

The state being tested is important. A switch pressed by a joystick mechanism is not in its unactuated reference condition, even if the joystick is at a position someone informally calls “neutral.” The joystick’s mechanical position and the switch actuator’s actual position are related through the particular mechanism, but they are not interchangeable descriptions. For terminal identification, use the switch actuator’s released and pressed states as the references.

This behavior applies to a typical changeover switch, not automatically to every switch found in an arcade joystick. The exact device may have different markings or an arrangement that does not match the three-terminal example. Check its diagram and markings before treating a measured terminal pair as COM-NC or COM-NO. Do not infer an electrical state from the direction in which the joystick is moved.

## Identify COM, NO, and NC on the micro switch

Start with the terminal markings on the switch or its connection diagram. The generic symbols mean COM is common, NC is normally closed, and NO is normally open. For a typical changeover contact, the common terminal is the shared connection in the COM-NC and COM-NO paths. The exact switch marking or schematic controls; generic terminology does not establish where a terminal sits on the switch body.

Do not identify a terminal by assuming a fixed physical order. Nor should you use a wire’s color, the direction the joystick moves, or the terminal’s apparent position as a substitute for documentation. Those observations do not establish the contact function. If the device’s markings are unclear or absent, its exact connection diagram is the appropriate reference. If the available information does not establish the terminal identity, leave it unresolved rather than guessing.

Keep the contact labels separate from the joystick’s directional names. A joystick direction describes a mechanical or control-system relationship; NO and NC describe contact states relative to the switch actuator’s unactuated condition. A particular direction may operate a particular switch, but that does not make “direction” another name for NO, NC, or COM.

Once the labeled terminals are mapped, use the contact-state pattern as a check: at rest, COM should connect to NC in a typical changeover switch; when pressed, COM should connect to NO. This pattern can confirm the mapping only when the switch design and the tested state are known. It is not a reason to override a conflicting device diagram or to presume that all joystick switches share the same layout.

## Verify arcade joystick micro switch NO and NC terminals with a continuity test

Disconnect power from the controller before taking continuity measurements. A continuity or resistance measurement should be made on the unpowered switch, not through a powered controller circuit. Keep the test focused on the switch’s contact paths, with the actuator state recorded for each reading.

With the actuator released, place the meter probes on COM and NC. A typical changeover switch should show a closed path between those terminals. Then test COM and NO in the same released state; that path should be open. Next, press the switch actuator and check the same pairs again. The expected pattern reverses: COM-NO is closed, and COM-NC is open.

The purpose is to compare both contact pairs in both defined states, rather than to treat one beep or one reading as a complete diagnosis. The result is meaningful only if the terminals are correctly identified, the switch is unpowered, and the actuator is actually in the stated released or pressed condition. If the actuator does not reliably move between those conditions, a reading may not represent the intended test state.

If readings do not match the expected pattern, first recheck the probe locations against the switch markings or diagram and confirm the actuator’s position. Repeat the measurements across both pairs and both states. Do not conclude from an unexpected reading alone that a particular joystick direction or controller input is faulty. It may reflect an incorrect terminal mapping, an unclear state, a device arrangement that differs from the typical example, or a contact behavior that needs further investigation.

### Related guides

- [ball screw actuator home position micro switch replacement](/guides/ball-screw-actuator-home-position-micro-switch-replacement/)
- [bottling machine end of stroke micro switch](/guides/bottling-machine-end-of-stroke-micro-switch/)
- [automated guided vehicle home position micro switch location](/guides/automated-guided-vehicle-home-position-micro-switch-location/)
- [accelerator pedal position stop micro switch operating force](/guides/accelerator-pedal-position-stop-micro-switch-operating-force/)

## When readings or joystick inputs do not match expectations

Separate the switch test from the observed joystick input. A continuity test on the unpowered switch checks the contact path under the tested conditions. It does not establish that the joystick mechanism moves the actuator as intended, that wiring is correct, or that a controller input responds properly. Each is a separate part of the system.

If a reading is unexpected, check whether the probes are on the intended COM and NO or NC terminals and whether the actuator is fully released or pressed. Compare the result with the exact switch diagram. A connected circuit can create paths that affect a measurement, so an in-circuit reading may not represent the switch contact alone. If those paths obscure the result, isolate a terminal before repeating the continuity check, with power disconnected.

If the isolated switch shows the expected contact changes but a joystick input still does not behave as expected, the contact-state result does not identify the remaining cause. Wiring or the controller input may need separate examination. Conversely, a mismatch at the switch does not by itself prove that the joystick’s direction mechanism is the cause. Avoid collapsing a contact issue, a mechanical actuation issue, and a downstream circuit issue into one diagnosis.

The practical decision boundary is narrow: use the device marking or diagram to map terminals, then use an unpowered continuity test to compare COM-NC and COM-NO in released and pressed states. Interpret that result as evidence about the tested switch contacts only. For an arcade joystick micro switch NO and NC terminals, neither a direction label nor a single measurement establishes the behavior of the entire controller.

## Sources and references

- Defense Logistics Agency ASSIST: [MIL-PRF-8805K: Switches and Switch Assemblies, Sensitive, Snap Action, General Specification For](https://quicksearch.dla.mil/qsDocDetails.aspx?ident_number=7196){: rel="nofollow noopener noreferrer" }
- Occupational Safety and Health Administration: [29 CFR 1910.333: Selection and Use of Work Practices](https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.333){: rel="nofollow noopener noreferrer" }
- Wikipedia: [Miniature snap-action switch](https://en.wikipedia.org/wiki/Miniature_snap-action_switch){: rel="nofollow noopener noreferrer" }
