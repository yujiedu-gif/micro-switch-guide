---
title: "Rotary indexing table home position micro switch not working: how to troubleshoot it"
description: "rotary indexing table home position micro switch not working: Understand the operating idea, essential terminology, practical checks, limitations, and."
date: 2026-07-22 09:00:00 +0800
category: Troubleshooting
tags:
  - rotary indexing table home position micro switch not working
  - micro switches
  - Troubleshooting
author: editorial_team
---

A **rotary indexing table home position micro switch not working** report does not, by itself, establish that the switch has failed. The home signal passes through several stages: the rotating target reaches the switch actuator, the actuator moves, the switch contacts change state, and the signal travels through wiring to the controller input. A fault at any stage can leave the table without a home indication or make that indication intermittent or mistimed.

This guide applies only to rotary indexing tables whose home-position signal is produced by a micro switch. It follows the signal path to separate target and actuation problems from contact, wiring, and input-path problems. Machine layouts and contact states vary, so identify the actual terminals and diagnostic indicators from the switch markings, documentation, and approved machine procedures rather than assuming a particular arrangement.

## Rotary indexing table home position micro switch not working: trace the signal path

Start by identifying the components that make up the home signal on the specific table: the rotating target, the switch actuator, the switch contacts, the connecting conductors, and the controller input. The target must reach the actuator; actuator movement must change the contact state; and that state must reach and register at the input. This sequence gives you distinct checkpoints instead of treating every no-home condition as a failed switch.

Record what the machine actually does before inspecting it. Does it show no home indication, indicate home intermittently, or indicate home at the wrong position? These observations help focus the inspection, but none proves a particular cause. For example, an incorrect indication could involve target position, actuation, contacts, wiring, or the input path.

The switch’s contact arrangement and the state the controller expects are not established by the general description of the signal path. Determine those details from the switch markings or documentation and the machine’s approved diagnostic information. Keep the diagnosis bounded to the home signal; do not change or reprogram the table’s complete control sequence as a substitute for tracing the fault.

## Make inspection and testing safe before checking the home switch

Before reaching near the table, target, or switch, follow the machine’s isolation and safety procedures. A stationary visual inspection and any test involving table motion are different tasks. Perform inspection only when the machine is in the required safe state. Verify motion only through a permitted guarded functional test; do not defeat guards or safety interlocks to observe the target or actuator.

Electrical measurements also have boundaries. Continuity or resistance checks belong on a de-energized, isolated circuit, with the switch disconnected from parallel circuit paths as needed for a meaningful check. Do not infer that a circuit is safe to measure merely because the table is stopped. Live electrical testing, or work where stored mechanical or pneumatic energy creates a hazard, should be handled by qualified personnel under the applicable machine procedures.

If the switch or target cannot be reached without unsafe access, stop rather than reaching into the mechanism. Likewise, do not bypass a safety control to make the home input change. When a required check depends on hazardous access or live measurements, refer the work to qualified service.

## Check whether the home target physically actuates the micro switch

With the machine safely isolated, inspect the target and switch mounting. Look for a target that has shifted, loose fasteners, debris in the actuation path, visible damage, or a changed gap. These are observable clues, not proof of the fault. A target may appear close to the actuator while still failing to move it as intended.

Next, establish whether the target reaches the actuator at the intended home point and whether the actuator moves freely. A target that passes without moving the actuator suggests an alignment or position issue. An actuator that binds or has visible damage suggests a mechanical problem that should be resolved before drawing conclusions from an electrical test. Do not force the actuator during inspection.

Consider the amount of actuator movement. Insufficient travel can leave the switch short of its operating point; excessive travel can push it beyond the intended movement. Binding, an unexpected gap, or a changed target position can also alter how the actuator is reached. Do not assume a numeric travel limit or adjust the mechanism by guesswork. Consult the switch documentation for permitted travel limits and the machine documentation for the intended target position. The distinction between pretravel and overtravel is defined in some standards, but that definition does not supply the limits for this particular switch or table.

## Verify that the micro switch changes contact state

Only after identifying the terminal arrangement should you check whether the switch changes electrical state. Read the switch markings or documentation to identify the relevant terminals and contact arrangement. Do not assume that the circuit uses normally open or normally closed contacts, or infer the released and actuated states from wire color alone.

With power isolated, check continuity or resistance in the released and actuated states. Isolate the switch from parallel circuit paths as needed so another part of the circuit does not affect the reading. Operate the actuator only in a safe, permitted manner. Compare the two readings with the documented contact arrangement; the expected result depends on that arrangement and cannot be specified generically.

Interpret the result in stages. If the actuator does not move, return to the target and mechanical inspection rather than calling it an internal contact failure. If it moves but the measured state does not change, check that the terminals, isolation, meter setup, and method are correct. If the setup is confirmed and the state still fails to change consistently between released and actuated positions, an internal contact or mechanism fault is a possibility. A symptom alone does not establish the cause.

## Trace the wiring and controller input after the switch test

Once the switch’s contact state is verified, follow the signal toward the controller. Inspect accessible connectors and conductors for looseness, damage, or corrosion. Check wiring continuity only with the circuit safely de-energized and isolated as required. A sound switch reading does not establish that the signal reaches the controller; a loose connection or conductor problem can interrupt the path downstream.

Then compare the verified switch state and wiring path with the controller’s observed input indication, using the machine’s approved diagnostic method. The controller’s expected indication depends on the actual contact arrangement and control circuit. Do not assume a particular input display or state without checking the relevant documentation.

If the switch changes state and the wiring is verified but the controller does not register the home input, investigate the input path or control logic rather than replacing the switch by default. Conversely, a controller indication that changes at the wrong table position should send the diagnosis back through target location and actuator timing as well as the downstream path. Confirm each stage; do not declare a cause from the symptom alone.

### Related guides

- [automated guided vehicle guard interlock micro switch intermittent operation](/guides/automated-guided-vehicle-guard-interlock-micro-switch-intermittent-operation/)
- [assembly robot travel limit micro switch failure causes](/guides/assembly-robot-travel-limit-micro-switch-failure-causes/)
- [air compressor travel limit micro switch troubleshooting](/guides/air-compressor-travel-limit-micro-switch-troubleshooting/)
- [boom lift travel limit micro switch symptoms](/guides/boom-lift-travel-limit-micro-switch-symptoms/)

## Confirm the repair and decide when to stop troubleshooting

After an adjustment or repair, restore guards and use an approved functional test to verify home detection. Confirm that the signal is repeatable at the intended home position. Also check that the target does not create unintended contact or excessive actuator travel. If the signal remains intermittent or mistimed, retrace the stages: target position, actuator movement, contact-state change, wiring, and controller input.

Do not treat a single successful indication as confirmation that every stage is reliable. Verification should establish that the intended home signal registers through the approved test without defeating guards or safety controls. If that verification cannot be done within the machine’s permitted procedures, stop and refer the work to qualified service.

For a **rotary indexing table home position micro switch not working**, the useful conclusion is not that the switch is automatically at fault. Establish whether the target reaches the actuator, whether the actuator moves, whether the contacts change state, whether the wiring carries that state, and whether the controller registers it. Escalate when safe access or qualified electrical work is required.

## Sources and references

- Defense Logistics Agency ASSIST: [MIL-PRF-8805K: Switches and Switch Assemblies, Sensitive, Snap Action, General Specification For](https://quicksearch.dla.mil/qsDocDetails.aspx?ident_number=7196){: rel="nofollow noopener noreferrer" }
- Wikipedia: [Miniature snap-action switch](https://en.wikipedia.org/wiki/Miniature_snap-action_switch){: rel="nofollow noopener noreferrer" }
