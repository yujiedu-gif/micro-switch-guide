---
title: "How to test a adjustable desk open position micro switch"
description: "how to test a adjustable desk open position micro switch: Understand the operating idea, essential terminology, practical checks, limitations, and."
date: 2026-09-06 09:00:00 +0800
category: Troubleshooting
tags:
  - how to test a adjustable desk open position micro switch
  - micro switches
  - Troubleshooting
author: editorial_team
---

How to test a adjustable desk open position micro switch depends on the switch’s documented contact state and how the desk mechanism engages its actuator. A continuity check can show whether the isolated switch changes electrical state when its actuator is released and pressed. It cannot, by itself, establish that the desk’s control board works or explain every cause of a desk that will not move.

Before access, disconnect the desk from power and secure it against unexpected movement. Do not probe energized control circuitry. The test has two distinct parts: check the switch contacts electrically, then determine whether the desk mechanism reaches and moves the actuator at the intended open position. Keeping those checks separate helps distinguish an electrical contact problem from an engagement, mounting, or wiring problem.

## How to test a adjustable desk open position micro switch safely

The goal is to establish whether the switch changes electrical state when the desk mechanism reaches its open position. Desk motion alone is not proof that the switch contacts changed state, and a switch that changes state when pressed by hand may still fail to engage correctly in the installed mechanism.

Disconnect the desk from power before accessing the switch or measuring its contacts. Secure the desk against unexpected movement while working near the mechanism. Do not probe energized control circuitry. If the switch cannot be accessed without disturbing the mechanism or creating an unsafe condition, stop rather than reach into a moving or powered assembly.

Identify the switch associated with the open-position mechanism without assuming that it has a universal location or layout. The open-position label describes the mechanism’s intended position; it does not establish which contact is closed at rest or when the actuator is moved. The contact state is design-dependent and must be checked against the relevant circuit documentation.

This procedure checks basic switch contact behavior and, separately, whether the mechanism physically changes the actuator state at the intended position. It does not test the control board, prove that the desk will move correctly, or identify every possible fault in the desk circuit.

## Identify the switch terminals and expected open-position state

Locate the switch associated with the desk’s open-position mechanism. Do not assume that its mounting point, actuator direction, or terminal arrangement matches another desk. Identify its terminals from the markings on the switch or the applicable wiring information before connecting meter probes.

In general changeover terminology, COM means common terminal, NO means normally open terminal, and NC means normally closed terminal. Verify that the specific switch uses these markings as expected by checking its schematic or wiring information. These labels do not tell you, by themselves, which contact state the desk circuit requires at the open position.

Use the circuit documentation to determine the intended contact state for the relevant position. Do not assume that open position means the NO contact must be closed or that the NC contact must be open. The normal contact state is design-dependent, and the mechanism’s open position is not necessarily the same thing as the switch’s unoperated position.

Before testing, note the expected state for the documented position and which terminal pairs the circuit uses. This gives you a reference for interpreting the readings. If the wiring information does not establish the expected state, you can still record whether the isolated switch changes state, but you cannot determine from that observation alone whether its state matches the desk design.

## Measure continuity with the actuator released and pressed

With power disconnected, set the meter to continuity or resistance. To avoid misleading readings caused by parallel paths through the desk circuit, disconnect at least one switch lead from the circuit before measuring. Keep track of the lead’s original connection so the test does not leave the wiring state ambiguous.

Measure COM-to-NO and COM-to-NC with the actuator released. Record whether each pair shows continuity or an open circuit according to the meter’s indication. Then move the actuator by hand and repeat both measurements with it pressed. Compare the results across the two positions and with the documented contact state, rather than judging either reading in isolation.

The useful observation is whether the contact readings change as the actuator moves. A change that is consistent with the circuit documentation supports basic contact operation. A reading that does not change, or that is unstable when the actuator is held in one position, may indicate a contact or actuator problem. These readings alone do not identify the exact cause or establish that the switch meets any broader performance requirement.

Do not infer the required open-position state just from COM, NO, or NC labels. Those terminal names describe general changeover terminology; the desk’s wiring information establishes which state is expected for its open-position signal. If the isolated switch changes state correctly by hand but the desk position signal remains incorrect, proceed to check mechanical engagement and the wiring path rather than treating the contact test as a complete diagnosis.

## Check actuator engagement at the desk open position

If the isolated switch changes state when its actuator is moved by hand, inspect whether the installed mechanism actually reaches and moves the actuator at the intended open position. The electrical test and the position check answer different questions: one checks contact-state change, while the other checks whether the desk mechanism produces that change where the circuit expects it.

Observe the actuator and its point of contact with the mechanism. Check for loose mounting, misalignment, obstruction, or insufficient travel. Do not force the actuator or the desk mechanism to obtain a reading. If the mechanism does not reach or move the actuator as intended, the switch may be electrically functional while the open-position signal remains incorrect.

Compare the mechanism’s action with the documented contact state. Determine whether the actuator is released or moved at the intended position, then relate that state to the isolated continuity readings. Do not assume that the actuator must be pressed at the open position: the intended relationship depends on the switch arrangement and circuit documentation.

This check separates failure to engage the actuator from failure of the switch contacts. If hand movement produces a consistent contact change but the mechanism does not, focus on the observed engagement path, including mounting and alignment. If the mechanism does move the actuator but isolated readings do not change consistently, the contact or actuator assembly may be at fault. Neither observation, by itself, establishes whether the control board is functioning.

### Related guides

- [automated guided vehicle guard interlock micro switch intermittent operation](/guides/automated-guided-vehicle-guard-interlock-micro-switch-intermittent-operation/)
- [assembly robot travel limit micro switch failure causes](/guides/assembly-robot-travel-limit-micro-switch-failure-causes/)
- [air compressor travel limit micro switch troubleshooting](/guides/air-compressor-travel-limit-micro-switch-troubleshooting/)
- [boom lift travel limit micro switch symptoms](/guides/boom-lift-travel-limit-micro-switch-symptoms/)

## Interpret results and decide what to check next

A consistent change in isolated COM-to-NO and COM-to-NC readings as the actuator moves supports basic contact operation. Compare the resulting states with the documented open-position circuit state. If the readings do not change or are unstable, the result may indicate contact or actuator damage, but the continuity check alone does not specify the failed component.

If the switch changes state correctly by hand but the desk position signal remains incorrect, check whether the mechanism physically reaches and moves the actuator at the intended position. Inspect the mounting and wiring for the observed fault path. If the isolated switch behavior is correct and the actuator engagement appears correct, inspect connectors and wiring continuity with power disconnected.

Keep the conclusion limited to what the checks establish. A continuity test does not prove control-board function, establish that the complete desk circuit works, or identify every cause of a motion problem. The open-position contact state is design-dependent, so use the applicable wiring information to decide whether the observed state is expected. In short, how to test a adjustable desk open position micro switch is to compare isolated contact readings across actuator states, then separately verify that the mechanism changes the actuator state at the intended position.

### Limits of the result

Record the terminal pairs measured, the actuator state for each reading, and the documented state expected at the open position. This keeps the electrical result distinct from the mechanical observation. If the expected state is undocumented, the test can show whether the switch changes state, but it cannot establish which state the desk requires.

Do not treat an apparent match between the switch readings and the open-position signal as proof that all desk controls operate correctly. The test is limited to basic contact behavior, actuator engagement, and, where checked, wiring continuity with power disconnected. It does not establish control-board function or cover every cause of a desk motion failure.

## Sources and references

- Defense Logistics Agency ASSIST: [MIL-PRF-8805K: Switches and Switch Assemblies, Sensitive, Snap Action, General Specification For](https://quicksearch.dla.mil/qsDocDetails.aspx?ident_number=7196){: rel="nofollow noopener noreferrer" }
- Wikipedia: [Miniature snap-action switch](https://en.wikipedia.org/wiki/Miniature_snap-action_switch){: rel="nofollow noopener noreferrer" }
