---
title: "atm cash cassette door micro switch continuity test"
description: "atm cash cassette door micro switch continuity test: Understand the operating idea, essential terminology, practical checks, limitations, and evidence."
date: 2026-09-21 09:00:00 +0800
category: Troubleshooting
tags:
  - atm cash cassette door micro switch continuity test
  - micro switches
  - Troubleshooting
author: editorial_team
---

An **atm cash cassette door micro switch continuity test** checks whether the switch’s contacts change electrical state as its actuator moves. It is a component-level check, not proof that the cassette door, wiring, or complete ATM interlock works correctly. Have qualified personnel isolate power and follow the equipment’s applicable service procedures before making measurements.

The key comparison is the identified contact pair with the actuator released and with it operated directly through its permitted travel. A contact pair may rest open or closed, depending on its documented arrangement. Do not infer terminal layout or expected state from appearance alone.

## What the atm cash cassette door micro switch continuity test can establish

A miniature snap-action switch can change an electrical contact state in response to mechanical actuator movement. In a position-detection arrangement, movement of the cassette door may act on the switch, but the resulting circuit behavior depends on the actual switch and equipment design.

A continuity check compares the electrical state of an identified contact pair at different actuator positions. If the contact changes state during direct operation, that is evidence of a change at the tested contact path under the test conditions. It does not establish that the installed door reliably moves the actuator, that the wiring carries the signal correctly, or that ATM logic responds as intended.

Keep the result within those limits. A static meter beep, by itself, does not show that the contact changes state. Nor does a changing reading prove the complete door-sensing circuit or interlock is functioning. The useful result is a documented comparison between the released and operated actuator states, made on the isolated switch and with the correct terminals identified.

## Safety and preparation before testing the micro switch

Have qualified personnel isolate power and verify de-energization according to applicable equipment service procedures. Use continuity or resistance mode only on an isolated circuit. Do not make a continuity measurement on an energized circuit.

Identify the exact contact pair from switch markings or applicable documentation before connecting the meter. Do not assume that terminals occupy a familiar physical layout. For documented changeover terminology, COM means common, NO means normally open, and NC means normally closed. These symbols are general terminology, not confirmation that a particular switch has those terminals or that they are arranged in a particular way. Check the exact device information.

Disconnect conductors as appropriate to isolate the contact path and avoid misleading readings through parallel circuit paths. Follow the equipment’s service procedure for that work. If the correct terminals, isolation state, or measurement method cannot be established, stop rather than treating an uncertain reading as a diagnosis.

## Measure the contact change across actuator travel

With power isolated and the switch appropriately disconnected, connect the meter to the documented contact pair. First observe and record the reading with the actuator released. Note whether the pair reads open or closed according to the meter’s indication, without assuming that one state is inherently correct for every arrangement.

Then operate the actuator directly through its permitted travel and observe the same contact pair. Record whether the reading changes and whether the change is consistent as the actuator is moved. Operate it slowly enough to notice an unstable or intermittent transition. Do not force the actuator beyond its permitted movement.

For reference, pretravel is the actuator movement from the free position to the operating position. Overtravel is movement after the operating position, up to the extreme permitted actuator position. These terms describe different portions of travel; they do not establish how much travel a particular switch requires. Use the applicable switch information for device-specific limits.

Compare the released and directly operated readings, not just whether the meter sounds once. If the reading does not change, or changes inconsistently, record that result for comparison with the switch documentation and further inspection. A continuity check alone does not establish the cause.

## Interpret readings for normally open and normally closed contacts

For a documented normally open pair, the expected resting state is open and the contact closes when actuated. For a documented normally closed pair, the expected resting state is closed and the contact opens when actuated. These opposite resting states are why the identified contact arrangement matters before interpreting a reading.

A meter’s beep or displayed resistance is an instrument indication, not a universal pass/fail value. Read it in light of the meter’s behavior, the test setup, and the applicable switch information. Do not transfer a reading or expectation from one terminal pair to another, or assume that a result on an isolated contact predicts behavior under operating voltage.

A pair that remains open or closed through direct actuator movement has shown no observed transition in that test. An unstable reading indicates an inconsistent result under the observed conditions. Neither observation alone identifies whether the cause is the contact, a terminal connection, an incorrect terminal choice, or another test limitation. Compare the result with the documented contact data before drawing a component-level conclusion.

## Separate a switch contact fault from door alignment or travel

Compare direct operation of the switch actuator with movement of the cassette door only under approved service procedures. If direct operation changes the measured contact state but installed door movement does not produce the same observed transition, the difference points toward a mechanical actuation question to investigate, such as actuator engagement, positioning, or available travel. It does not by itself identify a specific alignment defect.

If direct operation produces no stable state change, inspect the switch and its terminals for damage or contamination under the applicable procedure, then compare the observation with the specified contact information. A missing or inconsistent transition may be associated with a contact problem, but incorrect terminal identification, a connection issue, or a limitation in the test setup must not be silently ruled out.

Keep the diagnostic paths distinct: direct actuator operation examines the contact response to switch movement, while door movement also depends on the door’s mechanical relationship to the actuator. A component-level continuity result cannot establish that the installed parts engage correctly. Do not adjust or replace parts except as directed by applicable repair procedures.

### Related guides

- [automated guided vehicle guard interlock micro switch intermittent operation](/guides/automated-guided-vehicle-guard-interlock-micro-switch-intermittent-operation/)
- [assembly robot travel limit micro switch failure causes](/guides/assembly-robot-travel-limit-micro-switch-failure-causes/)
- [air compressor travel limit micro switch troubleshooting](/guides/air-compressor-travel-limit-micro-switch-troubleshooting/)
- [boom lift travel limit micro switch symptoms](/guides/boom-lift-travel-limit-micro-switch-symptoms/)

## Limits and next verification steps

An isolated continuity result cannot confirm behavior under operating voltage, controller interpretation, correct wiring in the installed equipment, or operation of the complete interlock circuit. It also cannot establish that the ATM will respond correctly to a door state. A switch can show a contact transition during a bench-style check while another part of the signal path remains unresolved.

Use approved service documentation and qualified procedures for any subsequent circuit-level checks. Do not bypass or defeat the door switch. If the observed state is unexpected or inconsistent, compare it with the exact switch and equipment information rather than substituting a generic terminal convention or assuming a particular ATM response.

The **atm cash cassette door micro switch continuity test** is therefore a bounded comparison: identify the documented contacts, test the isolated switch with the actuator released and directly operated, and record whether the contact state changes consistently. Treat that result as evidence about the tested contact path only, not as verification of the complete door-sensing or safety function.

## Sources and references

- Defense Logistics Agency ASSIST: [MIL-PRF-8805K: Switches and Switch Assemblies, Sensitive, Snap Action, General Specification For](https://quicksearch.dla.mil/qsDocDetails.aspx?ident_number=7196){: rel="nofollow noopener noreferrer" }
- Wikipedia: [Miniature snap-action switch](https://en.wikipedia.org/wiki/Miniature_snap-action_switch){: rel="nofollow noopener noreferrer" }
