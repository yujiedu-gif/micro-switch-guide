---
title: "bottling machine end of stroke micro switch continuity test"
description: "bottling machine end of stroke micro switch continuity test: Understand the operating idea, essential terminology, practical checks, limitations, and."
date: 2026-10-12 16:49:35 +0800
category: Troubleshooting
tags:
  - bottling machine end of stroke micro switch continuity test
  - micro switches
  - Troubleshooting
author: editorial_team
---

A bottling machine end of stroke micro switch continuity test can help determine whether a mechanically actuated switch changes electrical state at the end of machine travel. This procedure applies only when the machine’s end-of-stroke signal uses a micro switch. Other sensor types require different test methods, so confirm the device and signal path in the machine’s documentation before proceeding.

A continuity result alone does not identify the cause of a missing end-of-stroke signal. The switch may not receive enough actuator travel, its mounting or linkage may be misaligned, or a connection or conductor may be faulty. In-circuit paths can also affect meter readings. The useful approach is to verify the mechanical sequence, test the documented contact in both actuator states, and isolate the contact circuit when needed to confirm an ambiguous result.

## When this bottling machine end of stroke micro switch continuity test applies

Use this procedure only after confirming that a micro switch operates the bottling machine’s end-of-stroke input. A micro switch is a mechanically actuated electrical contact: movement of its actuator changes the contact’s electrical state. In this machine, the switch is part of a signal path that indicates an end-of-stroke condition. The test checks the switch contact; it does not, by itself, establish that the machine controller or the entire signal path functions correctly.

Trace the sequence that should produce the signal. As the relevant machine part approaches the end of its travel, it must move the switch actuator far enough to reach the switch’s operating point. If it does not, the contact may remain in its released state even though the switch itself is functional. Before interpreting a meter result, determine whether the machine mechanism actually reaches and operates the actuator as intended.

Use the exact switch documentation or circuit diagram to identify the contact terminals and expected states. A generic changeover contact may use terminals labeled common, normally closed, and normally open, but the device’s actual markings or schematic control. Do not assume that every switch has this arrangement, or infer a terminal’s function from its position. The contact configuration also determines what readings to expect with the actuator released and operated.

## Isolate the machine and prepare the meter

Shut down the machine and isolate relevant energy sources according to the site’s procedures. Verify that the circuit is de-energized before measuring resistance or continuity. Do not begin electrical testing if isolation cannot be confirmed, or if reaching the switch would expose you to an unsafe condition. If safe shutdown, isolation, or access is uncertain, stop and seek qualified service.

Consult the circuit documentation and switch markings before connecting the meter. Identify the specific contact pair used by the end-of-stroke signal and determine the expected state for each actuator position. Do not select terminals based on a presumed common, normally closed, or normally open arrangement. If the documentation is unavailable or the terminal function remains uncertain, the test cannot reliably establish whether the intended contact changed state.

Set the meter to continuity or resistance only after verifying that the circuit is de-energized. An in-circuit measurement may be influenced by other electrical paths connected to the contact. If those paths could make the result ambiguous, isolate the contact circuit by disconnecting one conductor after safe isolation. Label the connection first so it can be restored to its original terminal. Do not disconnect or reconnect conductors while the circuit is energized.

## Check the switch contact in both actuator states

With the selected contact pair identified, place the actuator in its released position and measure continuity or resistance across that pair. Record the result and compare it with the state specified by the switch documentation or circuit diagram. A reading should not be judged against a generic expectation, because the relevant contact configuration determines whether the contact is expected to conduct when released.

Next, move the actuator mechanically through its intended motion and measure the same contact pair again. Compare the operated-state reading with the documented expected state. For a changeover contact, the common, normally closed, and normally open labels describe a possible terminal arrangement, but the exact marking or schematic remains the reference for which pair should change state. The significant observation is whether the selected, correctly identified contact behaves as documented between released and operated positions.

Avoid forcing the actuator beyond its designed travel. The distinction between operating point and extreme permitted travel matters: pretravel runs from free position to operating position, while overtravel runs from operating position to the extreme permitted actuator position, as described in MIL-PRF-8805K sections 6.5.14 and 6.5.16. Do not use extra force or movement beyond the permitted travel to try to obtain a different reading.

If access and machine design permit a safe test, repeat the released-to-operated comparison carefully to check whether the reading changes consistently. Intermittent or inconsistent readings warrant further diagnosis rather than an immediate conclusion that the switch alone has failed. Keep the test tied to the actuator’s intended movement and the documented contact pair.

## Interpret readings and separate switch faults from linkage faults

A contact that does not change state as documented may indicate a switch problem, but the result is not conclusive until the test conditions are confirmed. First check that the correct terminals were selected and that the actuator reached the operating point. If machine travel does not move the actuator sufficiently, a working contact may never change state during the machine cycle. Insufficient travel or misalignment therefore needs to be distinguished from an electrical contact failure.

Inspect the mechanical path separately: check whether the mounting and alignment allow the machine mechanism to operate the actuator, and whether the linkage moves through the intended range. Do not compensate for a suspected alignment problem by forcing the actuator beyond its permitted travel. If mechanical movement is insufficient or uncertain, resolve that issue through the appropriate machine-service process before drawing a conclusion from the contact reading.

Also consider connection and wiring faults. Check for loose terminals, and assess conductor continuity as a separate question from the switch-contact test. A missing signal may arise from a connection or wire fault even when the contact changes state correctly. Conversely, a contact reading that appears to show continuity in circuit may reflect another parallel path rather than the selected contact alone. When such paths could affect the result, isolate the contact circuit after safe isolation and repeat the contact measurement.

Interpret the result only in light of the documented contact configuration, the actuator’s actual state, and whether the measurement was made in circuit or with the contact circuit isolated. If these conditions are unknown, the reading cannot reliably distinguish a failed contact from an invalid test setup or another fault in the signal path.

### Related guides

- [automated guided vehicle guard interlock micro switch intermittent operation](/guides/automated-guided-vehicle-guard-interlock-micro-switch-intermittent-operation/)
- [assembly robot travel limit micro switch failure causes](/guides/assembly-robot-travel-limit-micro-switch-failure-causes/)
- [air compressor travel limit micro switch troubleshooting](/guides/air-compressor-travel-limit-micro-switch-troubleshooting/)
- [boom lift travel limit micro switch symptoms](/guides/boom-lift-travel-limit-micro-switch-symptoms/)

## Restore connections and verify the end-of-stroke signal

After testing, restore any disconnected conductor to its labeled original terminal and secure the connection. Inspect the wiring so that it is clear of moving parts. Restore guards and follow site procedures before any functional check. Do not bypass safeguards to make the switch operate or to test the signal.

If the machine can be returned to service safely under site procedures, perform a controlled functional check of the end-of-stroke signal. Observe whether the mechanism reaches the intended position and whether the signal responds as expected. This checks the complete signal path at the machine level, while the resistance or continuity measurement checks the selected switch contact under the test conditions. Neither observation should be used to claim more than it verifies.

Stop and seek qualified service if safe isolation or access is uncertain, if the circuit remains energized, if the switch cannot be tested without an unsafe condition, or if the machine behaves unpredictably. A failed or unclear reading should not be treated as permission to bypass the switch. The bottling machine end of stroke micro switch continuity test is useful for locating a contact-state problem, but sound diagnosis also requires checking actuator travel, alignment, connections, and wiring as distinct parts of the signal path.

## Sources and references

- Defense Logistics Agency ASSIST: [MIL-PRF-8805K: Switches and Switch Assemblies, Sensitive, Snap Action, General Specification For](https://quicksearch.dla.mil/qsDocDetails.aspx?ident_number=7196){: rel="nofollow noopener noreferrer" }
- Wikipedia: [Miniature snap-action switch](https://en.wikipedia.org/wiki/Miniature_snap-action_switch){: rel="nofollow noopener noreferrer" }
