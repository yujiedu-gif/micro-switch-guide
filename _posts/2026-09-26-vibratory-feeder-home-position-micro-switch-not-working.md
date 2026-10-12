---
title: "vibratory feeder home position micro switch not working: How to Diagnose It"
description: "vibratory feeder home position micro switch not working: Understand the operating idea, essential terminology, practical checks, limitations, and evidence."
date: 2026-09-26 09:00:00 +0800
category: Troubleshooting
tags:
  - vibratory feeder home position micro switch not working
  - micro switches
  - Troubleshooting
author: editorial_team
---

A **vibratory feeder home position micro switch not working** symptom can come from several different points in the signal path. The target may not actuate the switch correctly, the switch contacts may not change state, or a valid switch signal may fail to reach or register at the control input. Separating these possibilities prevents a displayed home-position fault from being mistaken for proof that the switch itself has failed.

First confirm that the feeder’s home-position design actually uses a micro switch. Then use the equipment documentation to identify the home target, switch terminals, expected contact state, and control-input behavior. Do not infer these details from a switch’s shape or terminal arrangement. Follow the equipment-specific safety and isolation requirements before inspection or testing.

## Vibratory feeder home position micro switch not working: Start with safe fault isolation

A micro switch is a miniature snap-action switch that can change an electrical contact state in response to mechanical actuator movement. Such switches are commonly used for position or limit detection, but that general use does not establish that a particular feeder uses one for home detection. Confirm the installed design from the feeder documentation and identify the relevant target and input before applying this diagnostic path.

Follow the feeder’s applicable shutdown, deenergization, isolation, and stored-energy precautions before hands-on inspection. Do not bypass interlocks or defeat guards to make a test easier. If a check requires energized operation, use only the equipment’s approved procedure and qualification requirements; do not improvise an exposed or unguarded test.

Record what the feeder does before changing anything. Does it never indicate home, indicate home intermittently, or indicate home at the wrong time? Note the circumstances and any displayed status. These observations help focus checks, but they do not establish whether the mechanical actuation, switch contacts, wiring, or control input is responsible.

Use the connection diagram and equipment documentation to identify the circuit function, terminal markings, permissible load, and expected input state. The normal contact state and signal polarity are circuit-specific. A generic assumption about normally open or normally closed contacts, or about physical terminal layout, can lead to an incorrect test or interpretation.

## Check whether the home target actuates the micro switch correctly

With the equipment isolated as required, inspect the target and switch mounting. Look for visible damage, looseness, an obstruction, or a position that would prevent the target from reaching the actuator. Check whether the target appears aligned with the actuator path. Do not change an adjustment merely because it looks different from an assumed standard; use the feeder and switch documentation for the intended relationship.

Check whether the actuator moves and returns freely, without visible binding or interference. A target that misses the actuator, or an actuator that cannot move or return as intended, can prevent reliable switching even if the electrical contacts are functional. Conversely, observing movement alone does not prove that the switch reaches its operating position or changes electrical state.

Compare the actual actuator travel with the limits documented for the exact switch and equipment. In switch terminology, pretravel runs from the free position to the operating position. Overtravel runs from the operating position to the extreme permitted actuator position. Overtravel is the distance or angle between the operating position and the extreme position to which the actuator may be moved. These definitions describe travel relationships, not a universal feeder gap or adjustment value.

Use the documented operating and overtravel limits to assess whether the target’s movement is sufficient and whether the actuator is being driven beyond its permitted range. Do not invent a clearance, force, or adjustment dimension. If alignment or travel cannot be judged from the available documentation, leave the setting unresolved and seek qualified review rather than making an unsupported adjustment.

## Test whether the micro switch contacts change state

Identify the relevant contact terminals and their expected state from the exact switch documentation and the feeder wiring diagram. Confirm that the proposed test method is appropriate for the circuit and that applicable deenergization and qualification requirements are followed. Do not assume the switch’s physical layout identifies its contacts or circuit function.

Compare the contact state before and during actuator movement using an appropriate meter and the documented safe test method. The purpose is to observe the switch at the switch, not to infer its behavior from a lamp, display, or controller status elsewhere in the feeder. Interpret the result against the documented normal state and the mechanical position being tested.

If the contacts do not change state when the actuator reaches the documented operating point, record that observation. It may indicate a switch or actuator-related problem, but first confirm that the test terminals, method, and actual actuator travel are correct. A test made at the wrong terminals or without reaching the operating point cannot establish switch failure.

If the contacts change state only intermittently, or do not return to the expected state consistently, distinguish that behavior from a steady state that simply does not match an assumed polarity. Compare repeated observations only as permitted by the approved procedure. Do not condemn the switch based solely on the feeder’s reported home status or on an unverified circuit test.

A clear, repeatable contact change at the switch establishes that the switch-side state is changing under the observed conditions. It does not establish that the signal reaches the control input. Continue downstream if the feeder still fails to recognize home.

## Trace the home signal from the switch to the control input

Use the wiring diagram to follow the home-position circuit from the identified switch terminals through the relevant wiring and connectors to the control input. Under safe conditions, inspect accessible connections for looseness or visible damage. Do not assume that a wire’s color, a connector position, or a terminal’s physical location establishes its function; follow the documented circuit.

Determine the expected signal polarity and control-input behavior from the feeder documentation. The controller may be expected to see a particular state in the home position, but that state cannot be inferred generically. Compare the documented expectation with the observed contact state at the switch and the documented status at the input, using only an approved test method.

If the switch changes state correctly but the corresponding state is absent at the control input, focus the investigation on the intervening signal path. A loose connection, damaged wiring, or another documented circuit issue may prevent the signal from arriving. Inspect and verify the relevant path rather than replacing the switch on the basis of the controller symptom alone.

If the documented switch-side state is present through the signal path but the input does not register it as expected, the remaining issue may be at the control input or in its documented configuration. That observation separates a downstream control issue from a contact that never changed state; it does not identify a specific control fault without supporting checks. If the expected input behavior or test point is unclear, stop and obtain qualified assistance.

### Related guides

- [automated guided vehicle guard interlock micro switch intermittent operation](/guides/automated-guided-vehicle-guard-interlock-micro-switch-intermittent-operation/)
- [assembly robot travel limit micro switch failure causes](/guides/assembly-robot-travel-limit-micro-switch-failure-causes/)
- [air compressor travel limit micro switch troubleshooting](/guides/air-compressor-travel-limit-micro-switch-troubleshooting/)
- [boom lift travel limit micro switch symptoms](/guides/boom-lift-travel-limit-micro-switch-symptoms/)

## Confirm the repair with repeatable home-position checks

Correct only a verified fault, using approved procedures and the limits documented for the equipment and exact switch. A mechanical correction should be based on documented target alignment and actuator travel, not a generic gap. A wiring correction should follow the circuit diagram. Do not bypass the switch or alter the control circuit to mask an unresolved cause.

Before operating the feeder, restore guards and safety devices and follow the equipment’s approved operating procedure. Verify that the home position is detected repeatably under that procedure. A single successful indication does not by itself resolve an intermittent symptom; confirm the expected behavior without defeating safeguards or extending beyond the approved test conditions.

If home detection remains absent or inconsistent, or if the switch state, signal path, or input behavior cannot be verified from the documentation, stop and refer the issue for qualified evaluation. This sequence separates mechanical actuation, contact switching, and downstream signal recognition without presuming a universal setting or circuit polarity. For a **vibratory feeder home position micro switch not working** symptom, the useful conclusion is the last point in the documented path where the expected state can be confirmed, not an unverified guess about the failed component.

## Sources and references

- Defense Logistics Agency ASSIST: [MIL-PRF-8805K: Switches and Switch Assemblies, Sensitive, Snap Action, General Specification For](https://quicksearch.dla.mil/qsDocDetails.aspx?ident_number=7196){: rel="nofollow noopener noreferrer" }
- Occupational Safety and Health Administration: [29 CFR 1910.333: Selection and Use of Work Practices](https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.333){: rel="nofollow noopener noreferrer" }
- Wikipedia: [Miniature snap-action switch](https://en.wikipedia.org/wiki/Miniature_snap-action_switch){: rel="nofollow noopener noreferrer" }
