---
title: "Automated guided vehicle end of stroke micro switch continuity test"
description: "automated guided vehicle end of stroke micro switch continuity test: Understand the operating idea, essential terminology, practical checks, limitations,."
date: 2026-10-12 17:55:05 +0800
category: Troubleshooting
tags:
  - automated guided vehicle end of stroke micro switch continuity test
  - micro switches
  - Troubleshooting
author: editorial_team
---

For an automated guided vehicle end of stroke micro switch continuity test, first confirm that the end-of-stroke mechanism actually uses a mechanical micro switch. The procedure below checks whether a selected contact path changes electrical state between the released and manually actuated positions. It does not test a different kind of sensor or establish whether the vehicle’s complete control system works correctly.

Before measuring, identify the switch terminals from their markings or the applicable wiring diagram. Isolate the relevant electrical supply, verify that power is off, and disconnect at least one switch lead. Then compare the selected contact path in the released state with its state while the switch is manually actuated within its permitted travel. If the result is unexpected, check the terminal choice and mechanical travel before concluding that the switch has failed.

## What this automated guided vehicle end of stroke micro switch continuity test checks

This test applies only when a mechanical micro switch detects an end-of-stroke position. It checks whether a selected contact path changes electrical state as the switch operates. It is not a general test for every sensor that may signal position, nor does it determine how the vehicle’s control system responds to that signal.

Start by locating the switch and confirming its identity from the equipment documentation or the switch itself. Do not assume that an end-of-stroke device is a micro switch just because it is mounted near a moving mechanism. If the device is not identified as a mechanical micro switch, this procedure may not apply.

Identify the contact pair to test using the switch markings or wiring diagram. Where the relevant arrangement is documented, COM means common, NO means normally open, and NC means normally closed. These names do not establish the contact state for an unspecified reference condition, and not every switch has the same terminal arrangement. Follow the exact diagram rather than choosing terminals by appearance or assuming a universal layout.

A continuity test compares the electrical state of a selected contact path under defined actuator states. It does not, by itself, establish that the switch is suitable for its circuit, that the wiring is correct, or that the vehicle will respond as intended. Keep the test limited to the isolated switch contact path.

## Isolate the circuit before testing

Stop and secure the vehicle and mechanism according to the applicable service and safety procedure. Isolate the relevant electrical supply and verify absence of voltage using an appropriate method before connecting a meter. If the supply cannot be safely isolated or its absence cannot be verified, do not proceed with resistance or continuity measurements; follow the approved service procedure or have qualified personnel perform the work.

Disconnect at least one switch lead before testing. A connected circuit can provide parallel paths that affect a meter reading, so a reading made with the switch still connected may not represent the selected switch contact alone. Keep track of the conductor and terminal positions so the leads can be reconnected as documented after the test.

These conditions matter to both the measurement and its interpretation: the relevant supply must be isolated, absence of voltage verified, and at least one lead disconnected. A meter result obtained without these conditions does not provide the same basis for assessing the isolated contact path.

## Check released and actuated switch states

Set the meter to its continuity or resistance function. With the switch released, place the probes on the selected terminal pair identified from the marking or diagram. Record the result for that state. Do not apply a universal resistance threshold: the available information does not establish one for every switch or meter.

Next, manually operate the switch only within its permitted travel. Observe whether the selected contact path changes state, and record the result. Compare this reading with the released-state reading. Test the contact paths relevant to the documented switch arrangement; do not assume that a particular pair must behave one way simply because it is labeled COM, NO, or NC without considering the specified reference state and diagram.

The operating point is the point at which the switch changes state. Pretravel runs from the free position to the operating position, while overtravel runs from the operating position to the extreme permitted actuator position. Do not force the actuator beyond its permitted travel to obtain a reading. The purpose is to observe the contact transition within the switch’s allowed mechanical range, not to push the mechanism farther than it is designed to move.

A state change supports the limited conclusion that the tested contact path changed between the two observed actuator states. It does not prove that the installed mechanism reliably reaches those states or that the full vehicle circuit functions correctly.

## Interpret a failed or inconsistent result

If the reading does not change, first confirm that the probes are on the intended terminal pair and that the switch identification and diagram have been interpreted correctly. Then confirm that manual actuation reaches the switch’s trip point within its permitted travel. A failure to observe a change can indicate a contact problem, but it is not enough on its own to distinguish failed contacts from incorrect terminal selection or insufficient actuator travel.

If the switch changes state when operated manually but does not do so in the installed mechanism, investigate the mechanical actuation path separately. The installed mechanism may not move the actuator far enough to reach the operating point. This observation directs attention to travel or alignment; it does not establish a particular adjustment or repair for an unspecified design.

Intermittent or inconsistent readings may point to unstable contacts or loose terminals. Inspect accessible connections only within safe service limits, and do not treat a loose connection and an internal contact problem as the same fault. If the isolated switch changes state consistently when manually actuated but the installed signal remains abnormal, wiring or another part of the circuit may be involved. A continuity check across the switch cannot identify every fault in the harness or vehicle control system.

Keep each conclusion tied to the test condition: the selected terminals, released or actuated state, isolated switch lead, and observed reading. Unexpected results call for checking those conditions and the mechanical input before assigning a cause. No single continuity result establishes that the complete vehicle system is safe or functional.

### Related guides

- [automated guided vehicle guard interlock micro switch intermittent operation](/guides/automated-guided-vehicle-guard-interlock-micro-switch-intermittent-operation/)
- [assembly robot travel limit micro switch failure causes](/guides/assembly-robot-travel-limit-micro-switch-failure-causes/)
- [air compressor travel limit micro switch troubleshooting](/guides/air-compressor-travel-limit-micro-switch-troubleshooting/)
- [boom lift travel limit micro switch symptoms](/guides/boom-lift-travel-limit-micro-switch-symptoms/)

## Restore the connection and verify safe status

After testing, reconnect the conductors according to the documented terminal positions and secure them before restoring power. Do not guess at a connection if the original arrangement or diagram is unclear. Make sure the mechanism and work area are clear, then follow the vehicle’s approved procedure for returning the system to service.

A successful two-state continuity comparison is limited evidence about the tested contact path under the test conditions. It does not verify the whole end-of-stroke mechanism, harness, or control system. If the result remains inconsistent, the mechanism cannot be safely secured, or the system’s approved restoration procedure is unclear, stop and refer the issue to qualified service personnel.

The automated guided vehicle end of stroke micro switch continuity test is complete only when measurements are finished, conductors have been restored as documented, and the approved safe-status procedure has been followed. The result should be reported with its limits: which contact path was tested and whether it changed state between the released and manually actuated positions.

## Sources and references

- Defense Logistics Agency ASSIST: [MIL-PRF-8805K: Switches and Switch Assemblies, Sensitive, Snap Action, General Specification For](https://quicksearch.dla.mil/qsDocDetails.aspx?ident_number=7196){: rel="nofollow noopener noreferrer" }
- Wikipedia: [Miniature snap-action switch](https://en.wikipedia.org/wiki/Miniature_snap-action_switch){: rel="nofollow noopener noreferrer" }
