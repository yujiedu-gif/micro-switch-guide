---
title: "micro switch SPDT contacts troubleshooting"
description: "micro switch SPDT contacts troubleshooting: Understand the operating idea, essential terminology, practical checks, limitations, and evidence needed for."
date: 2026-09-14 09:00:00 +0800
category: Troubleshooting
tags:
  - micro switch SPDT contacts troubleshooting
  - micro switches
  - Troubleshooting
author: editorial_team
---

# Troubleshooting SPDT Micro Switch Contacts

A repeatable contact test can help distinguish a failed contact path from a measurement or actuator problem. **Micro switch SPDT contacts troubleshooting** starts by identifying the three terminals, then comparing their electrical states with the actuator at rest and while it is operated. Do not infer terminal identity from wire color, and do not rely on an in-circuit reading when other paths may affect the measurement. Use the switch markings or diagram and its documentation to guide the test. The method below focuses on the switch’s contact paths, not on diagnosing the larger appliance or vehicle circuit.

## What SPDT contact behavior should you expect?

A single-pole, double-throw (SPDT) switch has a common terminal and two contact paths, often called the normally open and normally closed throws. COM means common terminal, NO means normally open terminal, and NC means normally closed terminal. “Normally” refers to the switch’s unactuated state, not to a general assumption about how it is wired into equipment.

In a changeover switch, the common connection changes between the two throws as the actuator moves. At rest, the common-to-NC path is the normally closed path, while common-to-NO is the normally open path. When the actuator operates the switch, the contact arrangement changes according to the switch’s specified behavior. Consult the device diagram or documentation for the exact states and transition behavior; do not assume details that are not shown there.

Identify COM, NO, and NC from the switch markings or schematic. If the labels are absent or unclear, use the switch diagram rather than wire color to identify the terminals. Incorrect terminal identification can make a sound switch appear to have the wrong contact state. Keep the same terminal labels throughout the test and record which pair is being measured at each step.

The goal is to compare all three terminal pairs in both conditions. This gives more information than testing only the pair that seems relevant: it can show whether the expected change occurs on one throw, whether readings remain unexpected across pairs, or whether the result changes inconsistently. These observations help narrow the fault path, but a single reading does not by itself establish that the switch has failed.

## micro switch SPDT contacts troubleshooting: prepare for safe testing

De-energize the circuit before disconnecting the switch or taking continuity or resistance measurements. Verify that it is safe to proceed under the equipment’s applicable procedure. Do not make these measurements on an energized circuit. Disconnect enough of the switch wiring to electrically isolate the switch from parallel circuit paths that could distort the meter reading. The required degree of isolation depends on the circuit; if other paths remain connected, treat an unexpected reading as inconclusive until the measurement conditions are corrected.

Set the meter to continuity or resistance, following the meter’s instructions. Confirm that the meter and leads work before interpreting switch readings. For example, check that the test setup responds as expected when the leads are brought together. If the meter does not respond consistently, resolve that issue before using it to judge the switch.

Keep track of the terminal pair under test and whether the actuator is at rest or operated. Use consistent probe placement and actuation from one reading to the next. Avoid forcing the actuator. The purpose is to compare repeatable states, not to push the mechanism beyond its permitted movement. Record the results rather than relying on memory, especially if the readings change during the test.

A measurement taken in the wrong meter mode, through connected circuit paths, or with unreliable leads can look like a contact fault. These setup checks do not prove that the switch is good; they establish whether the subsequent readings are useful for diagnosing its contact paths.

## Measure all three terminal pairs at rest and during actuation

With the switch electrically isolated as needed and the actuator at rest, measure and record these pairs:

- COM to NO
- COM to NC
- NO to NC

Then operate the actuator through its normal travel and measure the same three pairs again. Keep the probe positions and meter setting consistent. Repeat the sequence without forcing the actuator, noting whether each reading is stable and whether the contact arrangement changes as specified for that switch.

In the unactuated state, the labels indicate that NO is normally open and NC is normally closed relative to COM. During actuation, a changeover switch changes the common connection between its throws. Compare the observed readings with the switch’s diagram and documentation rather than treating an assumed pattern as universal for every device. The NO-to-NC measurement is useful to record alongside the two common-to-throw measurements, but its expected result should likewise be checked against the device information.

Make a simple record with columns for terminal pair, actuator condition, and reading. If a result is unexpected, repeat that particular measurement after confirming the terminal labels, probe contact, meter setup, isolation, and actuator position. A repeatable sequence makes it easier to separate a stable state from a momentary reading caused by a loose lead or inconsistent actuation.

The actuator must reach the switch’s operating point for the contact transition to occur. If it does not, the switch may remain in its unactuated state even if its electrical contacts are functional. The documented distinction between pretravel and overtravel can help describe the actuator’s movement: pretravel runs from free position to operating position, while overtravel runs from operating position to the extreme permitted actuator position. Use the applicable device information when assessing travel, and do not force the actuator to reach a reading.

## Interpret open, intermittent, or unexpected contact readings

If both common-to-throw pairs appear open, first check that COM, NO, and NC were identified correctly. Confirm the meter setting and leads, ensure the switch is isolated sufficiently from other circuit paths, and verify that the actuator is in the intended position. Then repeat the readings. Only after those checks should the common path be considered a possible source of the unexpected result; the readings alone do not establish a specific internal failure.

If one throw does not change state while the other readings behave as expected, focus the next check on that contact path. Confirm the terminal pair and compare its rest and operated readings with the device’s specified behavior. Also confirm that the actuator reaches its operating point without being forced. A switch that is not actuated far enough may not make the expected transition, so actuator travel must be considered before attributing the result to a failed contact.

If readings fluctuate, repeat gentle, consistent actuation while keeping the meter leads steady. Check for loose test leads or connections before concluding that the contacts are intermittent. If the same contact-path reading remains inconsistent under repeatable measurement conditions, that is evidence of unreliable behavior, but first rule out instability in the measurement setup and wiring.

An unexpected NO-to-NC reading should also be checked against the device diagram rather than interpreted in isolation. Reconfirm which terminals are being measured and whether other circuit paths have been disconnected. The useful diagnostic distinction is whether the results repeat consistently across all three pairs and both actuator conditions, and whether the observed transitions match the specified switch behavior.

### Related guides

- [automated guided vehicle guard interlock micro switch intermittent operation](/guides/automated-guided-vehicle-guard-interlock-micro-switch-intermittent-operation/)
- [assembly robot travel limit micro switch failure causes](/guides/assembly-robot-travel-limit-micro-switch-failure-causes/)
- [air compressor travel limit micro switch troubleshooting](/guides/air-compressor-travel-limit-micro-switch-troubleshooting/)
- [boom lift travel limit micro switch symptoms](/guides/boom-lift-travel-limit-micro-switch-symptoms/)

## Decide whether the switch is unreliable and what to do next

Use the switch documentation for acceptable electrical limits. Do not apply a universal resistance cutoff: the available evidence does not establish one for every switch. Compare readings taken with the same meter, setup, terminal pair, and actuator condition, and interpret them in light of the device’s specified behavior.

A repeatable failed transition or unreliable contact behavior is a reason to treat the switch as unreliable and replace it in accordance with the equipment’s safety procedure. Do not open or attempt to repair a sealed switch. If the isolated switch behaves as specified during repeatable testing, investigate associated wiring or mechanical travel rather than assuming the contact mechanism is faulty. The test can identify whether the measured contact paths behave consistently under the tested conditions; it does not by itself diagnose the rest of the equipment.

The practical endpoint is a documented comparison: all three terminal pairs, at rest and while the actuator is operated, checked against the switch information and under consistent, isolated measurement conditions. **Micro switch SPDT contacts troubleshooting** is most useful when an unexpected reading is repeated only after meter setup, leads, wiring, terminal identity, and actuator travel have been checked. If a failed transition or unstable contact behavior persists, replace the switch rather than attempting an internal repair.

## Sources and references

- Defense Logistics Agency ASSIST: [MIL-PRF-8805K: Switches and Switch Assemblies, Sensitive, Snap Action, General Specification For](https://quicksearch.dla.mil/qsDocDetails.aspx?ident_number=7196){: rel="nofollow noopener noreferrer" }
- Wikipedia: [Miniature snap-action switch](https://en.wikipedia.org/wiki/Miniature_snap-action_switch){: rel="nofollow noopener noreferrer" }
