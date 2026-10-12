---
title: "antenna rotator closed position micro switch continuity test"
description: "antenna rotator closed position micro switch continuity test: Understand the operating idea, essential terminology, practical checks, limitations, and."
date: 2026-08-07 09:00:00 +0800
category: Troubleshooting
tags:
  - antenna rotator closed position micro switch continuity test
  - micro switches
  - Troubleshooting
author: editorial_team
---

# Testing an Antenna Rotator Closed-Position Micro Switch

An **antenna rotator closed position micro switch continuity test** checks whether the switch contacts change electrical state when its actuator moves, and whether the installed mechanism engages that actuator at the closed-position stop. These are separate checks: a switch may change state when pressed by hand yet fail to change state at the mechanism’s closed position.

Keep power isolated during resistance or continuity measurements. Identify the contacts from the switch markings or circuit documentation, compare readings with the actuator released and pressed, then verify the installed action at the stop. A continuity result by itself does not establish that the position is adjusted correctly or that the circuit operates correctly while powered.

## Safety and setup for the antenna rotator closed position micro switch continuity test

Turn off and isolate power before measuring resistance or continuity. Do not take readings on an energized circuit. If the relevant isolation point or circuit is unclear, do not guess; use the equipment’s circuit documentation to identify it before proceeding.

Before disconnecting anything, photograph or label the connections so their original arrangement can be referenced later. Disconnect at least one switch lead for the measurement. Leaving both leads connected can allow parallel circuit paths to affect the reading, making it harder to tell whether the measured path is through the switch contacts alone.

Set the meter to continuity or resistance mode and check the meter leads before testing the switch. A continuity beep is only an indication of the meter’s response to the measured path. It does not identify which switch terminals are being measured, nor does it establish that the installed position detection is correct.

This check is limited to the isolated switch and its mechanical engagement. It does not test the rotator while powered, verify powered operation, or establish positional adjustment. Keep the wiring disconnected as needed to avoid measuring other paths, and use the circuit documentation to guide any later reconnection.

## Identify the micro switch contacts before measuring

Find the common, normally open, and normally closed terminal identities from the switch markings or circuit documentation. Do not infer terminal identity from the actuator’s position, the physical location of a terminal, or whether the meter beeps. Generic changeover terminology uses **COM** for common, **NO** for normally open, and **NC** for normally closed, but the exact device schematic is the reference for the particular switch.

Choose the contact pair relevant to the closed-position circuit based on that documentation. With the actuator released, record the reading between the selected common and normally open or common and normally closed contacts. Then press the actuator and record the corresponding reading again. In general, normally open and normally closed contact pairs show opposite states as the switch changes state: a pair that is open in one actuator state should be closed in the other, and vice versa.

Do not assume a universal terminal arrangement or assign a closed-position function to a particular contact pair without documentation. If the terminal markings are missing or unclear, the reading alone cannot resolve which contact is intended for the circuit. Establish the terminal reference before interpreting the result.

## Test the released and actuated contact states

With power isolated and at least one lead disconnected, measure the selected contact pair while the actuator is released. Record the meter’s indication rather than relying on memory. Press the actuator through its normal travel and take a second reading on the same pair. The key question is whether the electrical state changes between the released and pressed conditions.

Repeat the comparison gently. Keep the contact pair and meter setup consistent from one reading to the next. Normally open and normally closed pairs should behave oppositely, so a change on one pair corresponds to the opposite state on the other pair. This expected contrast helps check whether the terminals were identified correctly, but it does not replace the device schematic.

If the reading remains unchanged, first confirm that the probes are contacting the intended terminals and that the meter leads respond as expected. Confirm the switch lead is disconnected enough to prevent another path from influencing the measurement. Then check that the actuator is actually moving through its normal travel. Do not conclude that the contacts have failed until these measurement and actuation checks are considered.

If readings fluctuate across gentle repetitions, note that instability rather than treating one beep or one resistance reading as conclusive. Check whether the probes remain in contact and whether the actuator is pressed consistently. The comparison identifies contact-state behavior under the test conditions; it does not by itself establish performance in powered operation.

## Verify the closed-position action in the installed mechanism

A hand-pressed switch check is not the same as verifying the rotator’s closed-position action. With power still isolated, move the mechanism safely to its closed-position stop and observe whether and when the switch actuator is engaged. Compare this installed action with the released-versus-pressed readings from the separate actuator check.

The switch should only be credited with changing state at the closed position if the installed mechanism actually moves its actuator into the state that produced the corresponding contact reading. If it changes state when pressed by hand but is not engaged at the stop, the contact test alone does not show that closed-position detection occurs there. The difference points to a mechanical engagement or timing question, not automatically to a failed contact.

Keep the measurement focused on the documented closed-position contact path. Do not infer the intended position from a continuity beep, or assume that a switch state observed away from the stop represents the mechanism’s closed position. The relevant comparison is between the documented contact pair, its released and pressed readings, and the actuator’s observed engagement at the closed-position stop.

This installed check does not verify positional adjustment or operation while powered. It establishes only what can be observed with the mechanism at the stop and power isolated. If those observations do not agree with the expected position-specific circuit behavior, continue through the electrical and mechanical checks rather than treating continuity as a complete system test.

## Interpret unexpected readings and choose the next check

If the state never changes, work through possible causes before judging the switch faulty. Recheck that the meter leads make contact, the selected terminals match the markings or circuit documentation, and at least one switch lead is disconnected. Confirm that the actuator moves through its normal travel. If these checks do not account for the reading, examine the wiring and relevant circuit path for a cause outside the isolated contact measurement.

If readings fluctuate, repeat the test while holding the probes steady and pressing the actuator consistently. Consider whether the contact indication changes reproducibly between released and pressed states. A variable reading should not be treated as a reliable state change simply because the meter beeps on one attempt.

If the switch changes state in the actuator check but the closed position is not detected, compare the installed engagement with the separate test. Check whether the actuator is reached at the stop and whether the observed actuator travel is sufficient to produce the tested state. Also consider the stop position and adjustment, and check circuit continuity beyond the switch as directed by the circuit documentation. These are distinct possible causes; a contact-state result alone does not identify which one applies.

The useful conclusion is limited: the isolated measurement can show whether a selected contact pair changes state under the tested actuator conditions. It cannot alone prove correct positional adjustment, establish the cause of a wiring problem, or confirm operation while powered. Resolve discrepancies by checking terminal selection, measurement contact, wiring, actuator movement, and mechanical engagement in that order of evidence.

### Related guides

- [automated guided vehicle guard interlock micro switch intermittent operation](/guides/automated-guided-vehicle-guard-interlock-micro-switch-intermittent-operation/)
- [assembly robot travel limit micro switch failure causes](/guides/assembly-robot-travel-limit-micro-switch-failure-causes/)
- [air compressor travel limit micro switch troubleshooting](/guides/air-compressor-travel-limit-micro-switch-troubleshooting/)
- [boom lift travel limit micro switch symptoms](/guides/boom-lift-travel-limit-micro-switch-symptoms/)

## How the open-position test differs

An open-position check may involve a separate micro switch or a separate contact path. Do not assume it shares the closed-position switch or uses the same terminal pair. Identify the relevant switch, position, and terminals from the circuit documentation before taking measurements.

The same isolated contact-state method can clarify whether the identified contacts change state with the actuator released and pressed. This is only a contrast to the main closed-position check, not a substitute for identifying the specific open-position circuit. Keep the interpretation tied to the documented terminals and the position being checked.

For the closed position, the decisive comparison remains the contact state under actuator movement and the actuator’s engagement at the installed closed-position stop. Neither that comparison nor an open-position reading proves correct positional adjustment or powered operation.

This concludes the explanation of antenna rotator closed position micro switch continuity test.

## Sources and references

- Defense Logistics Agency ASSIST: [MIL-PRF-8805K: Switches and Switch Assemblies, Sensitive, Snap Action, General Specification For](https://quicksearch.dla.mil/qsDocDetails.aspx?ident_number=7196){: rel="nofollow noopener noreferrer" }
- Wikipedia: [Miniature snap-action switch](https://en.wikipedia.org/wiki/Miniature_snap-action_switch){: rel="nofollow noopener noreferrer" }
