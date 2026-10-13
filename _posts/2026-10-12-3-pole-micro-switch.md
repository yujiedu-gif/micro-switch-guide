---
title: "3 pole micro switch: What Three Poles Mean and How to Check Them"
description: "3 pole micro switch: Understand the operating idea, essential terminology, practical checks, limitations, and evidence needed for careful selection,."
date: 2026-10-12 17:55:05 +0800
category: Basics
tags:
  - 3 pole micro switch
  - micro switches
  - Basics
author: editorial_team
---

A 3 pole micro switch has three mechanically linked switching paths, but the pole count alone does not tell you how many terminals it has or which contacts are present. To identify each pole, use the device documentation and verify its contact states separately with the switch de-energized and isolated. The three contact paths move together mechanically; their electrical arrangements and ratings still need to be established for the specific switch.

## What a 3 pole micro switch means

A pole is a separately switched circuit path within a switch. A three-pole micro switch therefore has three such paths. Pole count is not throw count, and neither number is the same as terminal count. A throw describes a contact option within a pole, while terminals are the physical connection points. The exact arrangement must be confirmed from documentation or markings for the particular device.

In a common changeover arrangement, each pole has a common terminal and normally open and normally closed contacts. That terminology does not establish that every three-pole switch uses this arrangement. Some designs may have a different contact configuration, and terminal layout varies. Do not assume that three poles mean three terminals, or that each pole has the same terminal positions as another design.

A micro switch can change an electrical contact state in response to mechanical actuator movement and is commonly used for position or limit detection. In a three-pole design, the actuator mechanically operates the poles together. This describes their mechanical relationship, not permission to treat their circuit paths as electrically interchangeable. Each path must be identified and considered on its own evidence.

## How a 3 pole micro switch changes contact states

For a documented changeover pole, COM means common terminal, NO means normally open terminal, and NC means normally closed terminal. Normally open and normally closed describe contact states at the specified reference condition. They do not, by themselves, establish a particular circuit’s behavior or guarantee current flow in an installation. Check the exact device schematic and state reference before assigning terminals.

A state table can help keep the three paths distinct. The following is a recording format, not a claim that every device has this arrangement. Use the switch’s documentation to confirm whether each pole actually has COM, NO, and NC contacts, then fill in observations for that device.

| Pole | Unactuated: COM to NC | Unactuated: COM to NO | Actuated: COM to NC | Actuated: COM to NO |
|---|---|---|---|---|
| 1 | Record result | Record result | Record result | Record result |
| 2 | Record result | Record result | Record result | Record result |
| 3 | Record result | Record result | Record result | Record result |

For a documented changeover contact, the table records the expected and observed relationship between each pole’s common terminal and its other contacts. If the documentation does not specify a changeover arrangement, do not fill in a presumed COM-NO-NC pattern. If markings or results do not agree with the available documentation, the arrangement remains unresolved.

Mechanical linkage means movement is shared; it does not prove that all contacts have equal ratings, that the paths are electrically isolated from one another, or that they are suitable for the same load. Verify those properties from the switch’s applicable documentation rather than inferring them from synchronized movement.

## Identify terminals and verify each pole safely

First locate the documentation or terminal markings for the exact switch. Use its schematic to identify candidate terminals and contact pairs for each pole. COM, NO, and NC have the meanings stated in the schematic; do not assign terminal functions solely from physical position, wire color, or another switch’s layout.

Before checking contact states, disconnect power and isolate the switch. Continuity testing of an installed, energized circuit is outside this procedure. If you cannot establish that the switch is safely de-energized and isolated, stop and seek qualified electrical help.

With the switch isolated, check the documented contact pairs for pole 1 in the unactuated state and record the results. Move the actuator through its intended movement and check again, noting the actuated state. Repeat the same process separately for poles 2 and 3. Keep results in three separate records; a result for one path does not verify either of the others. Use the documentation’s reference condition and contact arrangement to interpret the observations.

This procedure verifies observed contact behavior only under the conditions of the check. It does not establish voltage or current capability, performance with a particular load, electrical isolation, or correct operation of a surrounding machine. Stop if results conflict with the documentation, contacts appear damaged, or safe isolation is uncertain. Do not resolve a mismatch by guessing at terminal functions or altering the device. Have a qualified person investigate when the observations cannot be reconciled with the documented configuration.

## Choose a 3 pole micro switch using configuration and ratings

Start with the required circuit behavior. Confirm the contact arrangement, terminal mapping, and operating conditions in authoritative documentation for the specific switch. Compare the required states with the state table, pole by pole. If the documented arrangement does not match the required behavior, pole count alone does not make it suitable.

Next, check the electrical ratings for the actual load and test conditions that apply. Rating values are specification-sheet requirements tied to stated load and test conditions, not universal switching capacities. A voltage or current value without its associated conditions does not establish suitability for another load or operating situation. Do not transfer a rating across AC and DC, or from one load type to another, without applicable documentation supporting that use.

Consider isolation only where the applicable documentation specifies it. Three mechanically linked poles do not by themselves guarantee independent electrical isolation, and the pole count cannot establish an isolation rating or safety function. If a design or application requires a particular isolation property, confirm that requirement against the relevant documentation; otherwise, treat it as unknown.

Before specifying a switch, make sure its documented contact configuration matches the needed circuit states, its terminal mapping is clear, and its ratings cover the intended conditions. Where any of those points cannot be confirmed, the evidence is insufficient to conclude suitability. Do not substitute a generic description of a three-pole switch for the exact device’s specification.

### Related guides

- [dual micro switch](/guides/dual-micro-switch/)
- [touch micro switch](/guides/touch-micro-switch/)
- [no nc micro switch](/guides/no-nc-micro-switch/)
- [normally open micro switch](/guides/normally-open-micro-switch/)

## Common misunderstandings about three-pole switches

Three poles do not mean three terminals. A pole is a switched circuit path; a terminal is a connection point, and the number of terminals depends on the documented arrangement. Three poles also do not necessarily mean three throws. Confirm both contact configuration and terminal mapping rather than reading either count into the other.

Linked actuation does not make the paths interchangeable. The contacts move together mechanically, but that fact does not establish equal electrical ratings, isolation between paths, or suitability for unrelated circuits or a safety function. Those properties require evidence for the specific configuration and conditions.

Finally, a continuity result does not establish that a switch can carry a particular load or that an entire circuit or machine is safe. It records contact behavior for a defined pole, state, and isolated test. For a 3 pole micro switch, identify and verify all three paths separately, then rely on documented configuration and ratings to judge whether the device fits the required conditions. If documentation is missing or results conflict, treat suitability as unresolved rather than inferring it from pole count.

## Sources and references

- Defense Logistics Agency ASSIST: [MIL-PRF-8805K: Switches and Switch Assemblies, Sensitive, Snap Action, General Specification For](https://quicksearch.dla.mil/qsDocDetails.aspx?ident_number=7196){: rel="nofollow noopener noreferrer" }
- Wikipedia: [Miniature snap-action switch](https://en.wikipedia.org/wiki/Miniature_snap-action_switch){: rel="nofollow noopener noreferrer" }
