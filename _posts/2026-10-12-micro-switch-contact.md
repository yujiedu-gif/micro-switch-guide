---
title: "Micro switch contact: How its electrical states work"
description: "micro switch contact: Understand the operating idea, essential terminology, practical checks, limitations, and evidence needed for careful selection,."
date: 2026-10-12 16:49:35 +0800
category: Basics
tags:
  - micro switch contact
  - micro switches
  - Basics
author: editorial_team
---

A **micro switch contact** is an electrical path controlled by movement of a switch’s actuator. Its state can change as the actuator moves, but the available paths and their terminal labels depend on the switch’s configuration. A continuity check can show whether a tested path is open or closed under the conditions of that check. It does not show whether the switch can safely carry a particular load.

To verify contact behavior, first identify the switch’s contact diagram and the terminals it provides. Then disconnect power, isolate the switch or the relevant circuit path, and check the expected terminal pairs in both the released and actuated conditions. Compare the readings with the device documentation. Keep this test separate from any decision to connect a load: electrical ratings and test conditions are specific to the switch and its documentation.

## What a micro switch contact controls

A contact is the conductive path, or one of the paths, whose electrical state is controlled by movement of the actuator. The actuator is the part moved from outside the switch. It operates the mechanism that changes the contact state. The actuator and mechanism are not themselves the contact terminals, and a continuity reading concerns an electrical path between terminals rather than the mechanism’s movement.

The exact contact arrangement varies. A switch may provide a normally open path, a normally closed path, or a changeover arrangement. Do not assume that every switch contains all of these paths. The contact diagram for the specific switch is the reference for which terminals exist and which pair forms each path.

Actuator movement changes the electrical connection made by the contacts. That change can be described as a path becoming closed or open, or as a connection transferring between paths where a changeover arrangement is present. The arrangement and its state labels describe the contact behavior; they do not, by themselves, specify the switch’s electrical capacity or suitability for a connected load.

## Micro switch contact states: normally open, normally closed, and changeover

Normally open and normally closed describe contact state in the unoperated, released condition. A normally open path is open before actuation and closes when the switch operates. A normally closed path is closed before actuation and opens when the switch operates. These terms refer to the switch’s state, not an assumption about whether the surrounding circuit is energized.

A changeover arrangement provides a common terminal and alternate paths. In generic changeover terminology, COM means common, NC means normally closed, and NO means normally open. Before actuation, the common connection is associated with the normally closed path; as the switch operates, the connection transfers toward the normally open path. Verify the exact device schematic rather than relying on generic terminal symbols alone. A switch may have a different arrangement or may not provide all three terminals.

State names are meaningful only when the reference condition is clear. Here, “normally” refers to the unoperated condition, with the actuator released. Once the mechanism is operated, the contacts may change state. When the actuator is released again, the intended return is to the unoperated condition, but a continuity check establishes only the readings observed on the tested path and under the test conditions.

## How contact state changes during actuation and release

Start with the actuator released. In that condition, a normally open path is open and a normally closed path is closed. In a changeover arrangement, the common terminal is associated with the normally closed path. Those descriptions identify the initial electrical state, not the full sequence of movement.

As the actuator moves, the mechanism brings about a contact change. The point at which the switch operates is not necessarily the same physical position at which the contacts return during release. The operating point and reset point should therefore be treated as distinct parts of the movement, not as interchangeable labels or as a single assumed position. The available evidence does not specify universal travel distances or positions for either point.

The mechanism in a snap-action switch has a specific definition: the moving contacts’ speed is relatively independent of the actuating mechanism’s speed. This describes contact action, not a universal timing value or a guarantee about every switch. Do not infer a particular travel, timing, or transition pattern from the general term alone; those details depend on the design and its documentation.

When the actuator is released, the contacts return toward the unoperated state. A practical state check can compare readings before and after actuation, then confirm the released reading again after release. This sequence makes the state transition observable without assuming that the operating and reset points coincide. The contact diagram remains necessary to interpret which terminal pairs should be checked.

## How to verify a micro switch contact safely

Use a de-energized continuity check. Disconnect power and isolate the switch or the relevant circuit path before using a meter’s continuity function. This prevents the test from being performed on an energized path and helps ensure that the reading concerns the switch rather than another connected path. Do not use a continuity result from a connected circuit as though it necessarily identifies the switch’s own contact state.

First consult the contact diagram to identify the terminals and expected pairs. With the actuator released, place the meter probes across one expected pair and note whether the path reads open or closed. If the switch has other documented paths, check those pairs separately. Then operate the actuator and repeat the checks using the same pairs. Release the actuator and check again. Compare each result with the contact diagram and the stated unoperated and operated conditions.

For generic changeover terminology, COM is the common terminal, while NO and NC identify the normally open and normally closed terminals. Those symbols do not replace the exact device schematic. Confirm terminal identification before interpreting readings, because the available paths and their arrangement vary by switch.

A reading describes only the tested path, in the conditions in which it was measured. An open reading means the meter did not detect continuity through that tested path under the test conditions; a closed reading means it did. Neither result, on its own, proves that the switch can carry a rated load. A continuity function is a bounded check of contact state, not a load test or a full assessment of switch performance.

### Related guides

- [dual micro switch](/guides/dual-micro-switch/)
- [touch micro switch](/guides/touch-micro-switch/)
- [no nc micro switch](/guides/no-nc-micro-switch/)
- [normally open micro switch](/guides/normally-open-micro-switch/)

## What a continuity result cannot establish

A continuity reading does not establish the voltage or current a switch can handle, contact resistance under load, or service life. It also does not establish that a switch is suitable for a particular application. Do not infer a load limit from the terminals, the state reading, or the fact that a contact changes state during the check.

Contact resistance is a measured switch requirement. Its method, connection points, and limit must come from the applicable specification and test procedure. A simple continuity result is not a substitute for those specified measurements. Likewise, electrical rating values are specification-sheet requirements tied to stated load and test conditions, not universal switching capacities.

Before connecting a load, consult the documentation for the specific switch, including its applicable ratings and connection limits. Use the stated load and test conditions when interpreting any rating. If readings do not match the contact diagram, first confirm terminal identification, isolation, and test setup; do not treat a basic continuity reading as proof of the cause or of load capability.

A **micro switch contact** check is useful for observing whether a particular path changes between open and closed as the actuator is operated and released. Its conclusion should remain limited to that path and those test conditions. Use the switch’s own diagram to interpret the states, and its documentation to establish ratings before applying a load.

## Sources and references

- Defense Logistics Agency ASSIST: [MIL-PRF-8805K: Switches and Switch Assemblies, Sensitive, Snap Action, General Specification For](https://quicksearch.dla.mil/qsDocDetails.aspx?ident_number=7196){: rel="nofollow noopener noreferrer" }
- Wikipedia: [Miniature snap-action switch](https://en.wikipedia.org/wiki/Miniature_snap-action_switch){: rel="nofollow noopener noreferrer" }
