---
title: "adjustable desk travel limit micro switch NO and NC terminals"
description: "adjustable desk travel limit micro switch NO and NC terminals: Understand the operating idea, essential terminology, practical checks, limitations, and."
date: 2026-07-26 09:00:00 +0800
category: Applications
tags:
  - adjustable desk travel limit micro switch NO and NC terminals
  - micro switches
  - Applications
author: editorial_team
---

An **adjustable desk travel limit micro switch NO and NC terminals** can provide a change of electrical state when its actuator moves. That change may tell a desk controller that the moving structure has reached a travel limit. It does not, by itself, establish how the controller responds or prove that motor power is interrupted.

The important distinction is between three events: the actuator moves, the switch contacts change state, and the controller interprets the signal. The switch’s mounting position determines where the contact change occurs in relation to the desk’s physical end of travel. Actual wiring and behavior therefore depend on the switch markings and controller documentation, not on the terminal names alone.

## What NO and NC mean on an adjustable desk travel limit micro switch NO and NC terminals

COM is the common terminal. NO means normally open, and NC means normally closed. “Normally” refers to the switch’s unactuated condition: the position with the actuator released, not a universal desk position or a command that the controller must follow.

For a changeover switch using these terminals, the released and pressed states are described as follows:

| Actuator condition | COM to NO | COM to NC |
|---|---|---|
| Released, unactuated | Open | Closed |
| Pressed, actuated | Closed | Open |

Here, “open” means the contact path is not continuous, while “closed” means it is continuous. Pressing the actuator changes which contact path is closed. Confirm the actual terminal markings and the device schematic: COM, NO, and NC are generic changeover terminology, and the exact device must be identified correctly before testing or wiring.

This state table describes contact behavior only. NO does not inherently mean “stop,” and NC does not inherently mean “allow motion.” A controller might interpret a transition as a limit reached, use a particular state as an enable condition, or report a change. Which interpretation applies cannot be determined from the switch labels. The controller’s input design and documentation govern that part of the circuit.

## How the switch can signal a desk travel limit

The conceptual signal path begins with movement of the desk structure or another moving part that contacts the switch actuator. Actuator movement changes the contact state. If the switch is connected to a controller input, the controller can detect that electrical change and apply its own logic to the travel-limit signal.

That path does not supply a universal pinout. The available evidence does not identify a specific desk controller, input terminal, signal voltage, or required contact state. Do not infer any of these from COM, NO, and NC alone. Controller documentation and switch terminal markings determine the actual connection and the expected input behavior.

A controller may use the transition to stop motion, enable or inhibit motion, or report a condition, depending on its design. The signal’s meaning is therefore a controller function, not a property of NO or NC. A change in continuity is evidence that the switch contacts changed state; it is not evidence that the controller recognized the signal or stopped the desk.

Also distinguish a controller signal from direct interruption of motor current. A switch connected to a controller input may carry a signal that the controller interprets, while motor control occurs elsewhere in the system. A design that directly interrupts motor current is a different circuit arrangement. The terminal names alone do not establish which arrangement is present, or whether the switch is intended to carry motor current. Do not treat a limit-switch contact change as proof of motor-power interruption.

## Positioning the switch relative to the end of travel

The switch changes state when its actuator is moved far enough to operate it. Its location and the movement available at the actuator determine where that electrical change occurs relative to the desk’s mechanical end of travel. The signal point and the physical end stop must not be assumed to coincide.

If the switch is mounted so the moving part reaches the actuator too late, the contact change may occur at or beyond the intended travel boundary. If it is mounted earlier, the signal may occur before the desk reaches its physical stop. The applicable specification sheet governs device-specific travel limits; numerical travel requirements cannot be inferred from the component category.

Actuator travel, mounting alignment, and persistent pressure also matter. Misalignment can change whether or how the moving part operates the actuator. If the mechanism continues to press the actuator at the end of movement, the switch may remain actuated rather than returning to its unactuated state. Do not assume a particular amount of overtravel or allowable preload without the applicable device information.

The practical distinction is simple: the electrical trip point is where the contact state changes, while the mechanical stop is a physical boundary. Positioning must be evaluated in relation to both. A contact transition at the wrong point can leave the controller with an unsuitable limit signal even if the switch itself changes state.

## Safe checks for NO and NC terminal behavior

For a continuity check, isolate power and prevent unexpected desk movement before touching the switch terminals. First confirm the terminal markings against the applicable device schematic. Do not assume a connector layout or controller pinout from the names COM, NO, and NC.

With the switch de-energized, check continuity between COM and NO, then between COM and NC, with the actuator released. Operate the actuator and repeat the checks. For the generic changeover behavior, COM-to-NO changes from open to closed when pressed, and COM-to-NC changes from closed to open. If the observed state does not match, first verify that the terminals and actuator condition were identified correctly. These checks establish contact behavior, not controller interpretation.

Reconnect only according to the controller documentation and the switch’s terminal markings. If the documentation does not identify the input or wiring, do not substitute a guessed connection. For functional verification, restore operation only when the actual connection is documented, keep the movement area clear, and observe whether the controller recognizes the switch transition. A contact check alone cannot confirm that result.

### Related guides

- [ball screw actuator home position micro switch replacement](/guides/ball-screw-actuator-home-position-micro-switch-replacement/)
- [bottling machine end of stroke micro switch](/guides/bottling-machine-end-of-stroke-micro-switch/)
- [automated guided vehicle home position micro switch location](/guides/automated-guided-vehicle-home-position-micro-switch-location/)
- [accelerator pedal position stop micro switch operating force](/guides/accelerator-pedal-position-stop-micro-switch-operating-force/)

## When the limit signal does not behave as expected

Separate the possible failure paths rather than treating every unexpected movement as a defective switch. The switch may not change state, the terminals may have been misidentified, the actuator may not meet the switch as intended, or the controller may not interpret the input as expected. An intermittent contact is another possibility, but the available information does not establish a particular cause for a specific desk.

Check whether the contact state changes when the actuator is operated. Then consider whether the switch changes state at the intended travel point, given its mounting position and the movement of the desk structure. Finally, whether the controller recognizes the input must be assessed from controller documentation and a documented connection. These are distinct checks: contact operation, mechanical timing, and controller response.

Stop testing if desk motion is uncontrolled, the switch is mechanically forced, or controller wiring is undocumented. Do not infer a repair or a safe operating configuration from a terminal-state test. The central question is whether a correctly identified switch changes state at the intended point and whether the documented controller input responds as designed. COM, NO, and NC describe contact states; they do not establish a universal desk command, pinout, or stopping method.

In short, **adjustable desk travel limit micro switch NO and NC terminals** identify contact paths relative to the unactuated state. The switch can signal a travel limit through a controller input, but the controller’s documentation determines how that signal is used, and switch placement determines when it occurs relative to the mechanical stop.

## Sources and references

- Defense Logistics Agency ASSIST: [MIL-PRF-8805K: Switches and Switch Assemblies, Sensitive, Snap Action, General Specification For](https://quicksearch.dla.mil/qsDocDetails.aspx?ident_number=7196){: rel="nofollow noopener noreferrer" }
- Wikipedia: [Miniature snap-action switch](https://en.wikipedia.org/wiki/Miniature_snap-action_switch){: rel="nofollow noopener noreferrer" }
