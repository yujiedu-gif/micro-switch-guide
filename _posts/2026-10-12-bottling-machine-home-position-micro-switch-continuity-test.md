---
title: "bottling machine home position micro switch continuity test"
description: "bottling machine home position micro switch continuity test: Understand the operating idea, essential terminology, practical checks, limitations, and."
date: 2026-10-12 16:49:35 +0800
category: Troubleshooting
tags:
  - bottling machine home position micro switch continuity test
  - micro switches
  - Troubleshooting
author: editorial_team
---

A bottling machine home position micro switch continuity test checks whether the switch’s contacts change electrical state as its actuator moves. It applies only if the machine uses a micro switch to sense home position. A successful contact test does not, by itself, confirm that the machine’s home position is correctly aligned or that its controller receives the signal.

Use the machine and switch documentation to identify the wiring, required isolation steps, and approved verification procedure. Do not infer terminal locations, acceptable travel, or a universal resistance threshold. The procedure below separates the switch’s contact behavior from the machine’s mechanical positioning and downstream input circuit.

## When this bottling machine home position micro switch continuity test applies

First confirm from the machine documentation or installed sensor information that home position is detected by a micro switch. Other sensor designs require a different test. A miniature snap-action switch can change an electrical contact state in response to mechanical actuator movement, and switches of this type are commonly used for position or limit detection. That general description does not establish that any particular machine uses one.

Keep the scope narrow: this procedure checks the switch contacts. It is not a method for calibrating or programming the machine, and a controller status display is not a substitute for an isolated contact test. A machine may fail to indicate home even when the switch contacts change state, for example if the actuator does not engage as intended or a signal path beyond the contacts has a problem.

Before starting, consult the machine’s wiring information and safety procedure. Confirm the contact arrangement and how the actuator is intended to move during the check. If the documentation does not make the test setup clear, do not guess at wiring or operating conditions. Follow the approved procedure for the specific machine.

## Isolate power and identify the micro switch contacts

Stop the machine and isolate energy before handling wiring or testing contacts. Follow applicable lockout procedures, then verify that the circuit is de-energized before disconnecting a lead or connecting a meter. Do not rely on a stopped machine or an inactive display as proof that the circuit is de-energized.

Record the existing wiring arrangement before changing it. Identify COM, NC, and NO from the switch markings, its schematic, or the machine’s wiring information. A generic changeover contact may use those labels for common, normally closed, and normally open, but the exact device marking or schematic controls. Do not assume terminal positions or identify terminals by appearance alone.

For an isolated contact reading, disconnect at least one relevant lead as required by the wiring and documentation. Other circuit paths can affect an in-circuit measurement, so a reading taken with the switch still connected may not represent the contact alone. Keep track of the disconnected lead so it can be restored to its documented terminal after testing.

Set the meter to continuity or resistance mode, following the meter instructions. Check that the selected function and test leads are working as intended. Do not treat a reading from an unverified setup as a definitive result. The switch must remain disconnected from the circuit for the contact readings described below.

## Run the bottling machine home position micro switch continuity test

With the switch isolated, test between COM and NC while the actuator is released. Then test between COM and NO in the same released state. Record what the meter indicates for each pair. Interpret the readings against the switch’s markings or documentation, rather than assuming a particular display, beep, or resistance value is universal.

Next, move the actuator through its intended operating movement without forcing it. Test COM-to-NC and COM-to-NO again with the actuator actuated, and record the results. Use the mechanism as intended for the check; do not push past its normal movement or infer a required travel distance from this procedure.

Compare the released and actuated readings. The relevant observation is whether the contact state changes in the way specified for that switch. Repeat the release-and-actuation check several times and note whether the change is clean and consistent each time. Do not declare a switch acceptable solely because it changes state once. If the documentation specifies a test condition or expected result, use that requirement.

A continuity test describes contact behavior under the test conditions. It does not establish that the machine’s home position is correctly set, that the actuator engages at the right point, or that the controller receives a valid input. Keep those questions separate when interpreting the result.

## Interpret continuity results without confusing alignment and switch faults

If the isolated contacts fail to change state as specified, or the readings vary from one actuation to the next, the switch or its terminals may have a problem. This result identifies an electrical contact concern for further checking; it does not establish a particular cause or authorize a replacement decision without the relevant documentation.

If the isolated switch changes state consistently but the machine misses its home indication, the contact test alone does not point to a failed switch. Check whether the intended mechanism engages the actuator, and inspect mounting and wiring using approved procedures. The machine’s input circuit may also need checking. These are distinct points in the path from mechanical movement to an indicated home position.

In-circuit readings can be misleading because other connected paths may influence the meter. If a reading seems inconsistent, verify the documented test arrangement and repeat the contact check with the relevant lead disconnected. Do not use a machine status signal to claim that the isolated contacts are sound, or use good contact readings to claim that alignment is correct.

Do not infer a universal acceptable travel distance or resistance threshold. Use the switch documentation and machine specifications for the applicable expected results. If those requirements are unavailable, report the observed readings and uncertainty rather than inventing a pass/fail limit.

### Related guides

- [automated guided vehicle guard interlock micro switch intermittent operation](/guides/automated-guided-vehicle-guard-interlock-micro-switch-intermittent-operation/)
- [assembly robot travel limit micro switch failure causes](/guides/assembly-robot-travel-limit-micro-switch-failure-causes/)
- [air compressor travel limit micro switch troubleshooting](/guides/air-compressor-travel-limit-micro-switch-troubleshooting/)
- [boom lift travel limit micro switch symptoms](/guides/boom-lift-travel-limit-micro-switch-symptoms/)

## Restore the wiring and verify the home-position signal safely

When the contact check is complete, reconnect the wiring to the documented terminals and secure it as specified. Replace covers and guards, remove tools, and follow the machine’s approved procedure before restoring power. Do not operate the machine with guards removed or interlocks defeated.

Use the machine’s approved test or diagnostic procedure to check whether home detection is repeatable after reassembly. This is a separate machine-level verification from the isolated continuity check. If the home signal remains unreliable, stop and follow the applicable machine procedure for further investigation. Do not bypass or bridge the switch to make the machine run, and do not treat a repeatable bench-style contact change as proof that the full home-position signal path works.

A bottling machine home position micro switch continuity test can establish whether the isolated contacts change state consistently with actuator movement. It cannot establish alignment or controller response by itself. Keep the electrical result and machine-level result distinct, restore the wiring and guarding, and leave the machine stopped if reliable home detection has not been confirmed through the approved procedure.

## Sources and references

- Defense Logistics Agency ASSIST: [MIL-PRF-8805K: Switches and Switch Assemblies, Sensitive, Snap Action, General Specification For](https://quicksearch.dla.mil/qsDocDetails.aspx?ident_number=7196){: rel="nofollow noopener noreferrer" }
- Wikipedia: [Miniature snap-action switch](https://en.wikipedia.org/wiki/Miniature_snap-action_switch){: rel="nofollow noopener noreferrer" }
