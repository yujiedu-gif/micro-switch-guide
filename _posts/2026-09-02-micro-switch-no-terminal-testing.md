---
title: "micro switch NO terminal testing: How to Check Normally Open Contacts"
description: "micro switch NO terminal testing: Understand the operating idea, essential terminology, practical checks, limitations, and evidence needed for careful."
date: 2026-09-02 09:00:00 +0800
category: Troubleshooting
tags:
  - micro switch NO terminal testing
  - micro switches
  - Troubleshooting
author: editorial_team
---

# Testing the NO Terminals of a Micro Switch

Micro switch NO terminal testing checks whether the normally open contact pair changes from an open state to a closed state when the actuator is operated. The key is to verify the pair by its contact behavior, not by assuming that terminals in a particular physical position are NO. Use the exact switch documentation, including its markings or schematic, to identify terminals; then compare meter readings with the actuator released and operated. This is a contact-state check, not a complete assessment of the switch’s performance under a rated load.

## What NO means in micro switch NO terminal testing

“Normally open” describes the contact state with the switch unactuated. For an NO pair, the contacts are open in that reference state. When the actuator is operated, the pair is expected to close. The word “normally” therefore refers to the unactuated state, not to a terminal’s location or appearance.

A generic changeover contact may have terminals marked common, normally closed, and normally open. Those labels are not a substitute for checking the exact device. Use its documentation, markings, or schematic to identify the relevant pair. Do not infer that a terminal is NO because it is on a particular side, sits in a particular position, or resembles a terminal on another switch.

The test depends on comparing the same two terminals in both actuator states. A reading across the identified NO pair should indicate an open circuit with the actuator released and a closed path when it is operated. This expected change gives a practical check of whether the selected pair behaves as NO. It does not establish other switch characteristics, and a single reading in only one state cannot confirm the expected transition.

## Prepare the micro switch and meter safely

Disconnect power to the circuit before connecting a meter for continuity or resistance measurements. Verify that the circuit is de-energized before proceeding. Do not take a continuity or resistance reading on an energized circuit. If the switch is installed in a larger circuit, disconnect at least one relevant lead when practical. This helps avoid a parallel path that could affect the reading and make it appear that the switch contacts have a different state.

Identify the NO terminal pair from the exact switch documentation, markings, or schematic rather than terminal position alone. If the identification is uncertain, do not treat a meter reading as proof that the pair is NO; a different pair can show different behavior. Keep the test focused on the switch terminals rather than interpreting readings elsewhere in the circuit.

Set the meter to continuity mode or a suitable resistance range. Check the meter leads before testing so that you know how the meter indicates a connected path. Follow the meter’s own display or sound indication when interpreting continuity; do not assume that every meter uses the same signal. Keep the probes on the same two identified terminals for both measurements, and avoid changing the actuator state or probe points while recording each result.

## Test the NO terminal pair in both actuator states

1. With power disconnected and de-energization verified, connect the meter probes across the identified NO pair. If practical, ensure that at least one relevant lead is disconnected from the surrounding circuit to limit parallel paths.
2. Leave the actuator released, which is the unactuated reference state. Observe the meter. The NO pair is expected to indicate an open circuit in this state.
3. Operate the actuator while keeping the probes on the same terminals. Hold the actuator in its changed state and observe the meter again. The pair is expected to indicate continuity or a low resistance when closed.
4. Release the actuator and check that the reading returns to an open indication. Repeat the release-and-press cycle to see whether the reading changes consistently between the two states.

The useful result is the transition, not simply a continuity beep or a number viewed by itself. The expected pattern is open with the actuator released and closed when operated, followed by a return to open when released again. Keep the test unloaded: do not apply circuit power as part of this meter check.

If the actuator does not appear to reach its changed state, the measurement may not represent the intended operated condition. Switch terminology distinguishes pretravel, from free position to operating position, from overtravel, from operating position to the extreme permitted actuator position. These are distinct travel references. The cited terminology does not establish travel values for a particular switch, so use exact device documentation for any device-specific interpretation.

## Interpret unexpected micro switch NO terminal testing results

A closed reading while the actuator is released does not match the expected NO state. First consider whether the wrong pair was identified or whether a parallel path remains connected. If those test setup issues are addressed and the reading still conflicts with the expected state, a contact fault is one possible explanation. The reading alone does not identify which explanation applies.

An open reading while the actuator is operated also fails to show the expected change. Possible explanations include incomplete actuator travel, incorrect terminal identification, or a contact fault. Confirm that the pair was identified from the exact documentation and that the actuator reached the operated condition before drawing a conclusion. Do not assume a specific fault solely from the meter indication.

Unstable readings can result from poor probe contact, intermittent switching, or mechanical actuation issues. Keep the probes steady, use the same pair, and repeat the release-and-press check. If the readings remain inconsistent, the test indicates that the expected state change has not been verified; it does not by itself pinpoint the cause. Avoid extending this focused terminal check into a diagnosis of the entire circuit.

### Related guides

- [automated guided vehicle guard interlock micro switch intermittent operation](/guides/automated-guided-vehicle-guard-interlock-micro-switch-intermittent-operation/)
- [assembly robot travel limit micro switch failure causes](/guides/assembly-robot-travel-limit-micro-switch-failure-causes/)
- [air compressor travel limit micro switch troubleshooting](/guides/air-compressor-travel-limit-micro-switch-troubleshooting/)
- [boom lift travel limit micro switch symptoms](/guides/boom-lift-travel-limit-micro-switch-symptoms/)

## What a continuity test cannot establish

A continuity or resistance check verifies a contact-state change under the conditions of the meter test. It does not establish that the switch can carry a rated current or voltage under load. A closed indication is not proof of switching capacity, and an open indication is not a measurement of insulation performance.

This test also does not assess contact heating or long-term reliability. It cannot establish whether a switch is suitable for a particular rated load or application. Those questions require the relevant ratings and separate application-specific checks; do not infer them from an unloaded continuity result.

The conclusion should stay narrow: the identified NO pair either did or did not show the expected open-to-closed change as the actuator moved from unactuated to operated, and returned to open on release. Micro switch NO terminal testing is useful for verifying that contact-state behavior, but it is not a substitute for evaluating rated performance or other characteristics.

## Sources and references

- Defense Logistics Agency ASSIST: [MIL-PRF-8805K: Switches and Switch Assemblies, Sensitive, Snap Action, General Specification For](https://quicksearch.dla.mil/qsDocDetails.aspx?ident_number=7196){: rel="nofollow noopener noreferrer" }
- Wikipedia: [Miniature snap-action switch](https://en.wikipedia.org/wiki/Miniature_snap-action_switch){: rel="nofollow noopener noreferrer" }
