---
title: "spst micro switch: How Its Single Circuit Path Works"
description: "spst micro switch: Understand the operating idea, essential terminology, practical checks, limitations, and evidence needed for careful selection,."
date: 2026-08-26 09:00:00 +0800
category: Basics
tags:
  - spst micro switch
  - micro switches
  - Basics
author: editorial_team
---

An **spst micro switch** controls one circuit path: its contacts either leave that path open or complete it, depending on the switch design and actuator state. To identify what a particular switch does, trace the path through its common terminal and the switched contact, then verify the contact state with the switch unpowered. The SPST description identifies the electrical contact arrangement. It does not identify the switch’s physical shape, actuator, mounting, or electrical capacity.

## What an spst micro switch means

SPST means single-pole, single-throw. In contact terms, one pole is one circuit path being controlled, and one throw is the single switched connection available for that path. The arrangement therefore makes or breaks one path rather than selecting between multiple switched paths.

An SPST switch may be normally open or normally closed. “Normally” refers to the switch’s resting, unactuated state. In a normally open design, the path is open at rest and closes when the mechanism changes the contact state. In a normally closed design, the path is closed at rest and opens when the contact state changes. Which behavior applies depends on the switch design; SPST alone does not specify it.

This description concerns the contacts, not the switch’s external form. A small body, a particular mounting shape, or a particular actuator does not establish whether the contacts are SPST, normally open, or normally closed. Use the marking or documentation for the exact switch to identify its contact arrangement.

## How the SPST micro switch opens or closes one path

Trace the controlled path from the common terminal, often marked COM, to the one switched contact used by the design. COM means common terminal. NO means normally open terminal, and NC means normally closed terminal. These are general changeover terms, so verify the exact device schematic rather than assuming every switch has the same terminal layout or uses the same contacts.

When the switch is at rest, the relevant contact pair has its normal state. Actuator movement may change that state when the switch is designed to operate that way. The path is then either completed or interrupted. The movement changes the contact state; it does not turn an SPST arrangement into multiple controlled paths.

| Contact design | At rest | When actuated to change state |
|---|---|---|
| Normally open (NO) | Path open | Path closes |
| Normally closed (NC) | Path closed | Path opens |

The table describes the contact behavior for the stated NO or NC design, not a guarantee about when a particular actuator will operate or release. Confirm the device’s markings and documentation to determine which contact is present and how its specified operating motion changes state. Do not infer the path from the body shape or actuator alone.

## Identify terminals and verify contact state

Start with the switch’s terminal markings and schematic or other device documentation. COM identifies the common terminal; NO and NC identify normally open and normally closed terminals where those designations apply. The exact schematic matters because generic terminal terminology does not establish the layout of an individual switch.

To compare contact states, first isolate the switch from energized power. With the switch unpowered, use a continuity meter to check the relevant terminal pair at rest and again with the actuator in the intended actuated state. For an NO contact, the expected state is open at rest and closed when actuated to change state. For an NC contact, the expected state is closed at rest and open when actuated to change state. The comparison helps identify the contact behavior without relying on appearance.

An in-circuit measurement can be misleading because other connected paths may affect the reading. If the meter’s result does not match the expected contact state, do not treat that result alone as proof of the switch’s configuration or condition. Check the device schematic and the measurement setup. Testing should not involve energized terminals. This method verifies contact state; it does not establish electrical suitability for a particular load.

## Check ratings before using an SPST micro switch

The SPST label describes the contact arrangement, not how much voltage or current the switch can handle. Before using a switch in a circuit, compare the circuit’s voltage, current, and load type with the published rating for that exact switch and the stated test conditions. A rating is not a universal switching capacity: rating values are specification-sheet requirements tied to stated load and test conditions.

Use only the rating explicitly stated for the applicable current type, load, and test condition. An AC rating does not establish a DC rating, and a rating for one load or test condition does not establish another. Check the applicable specification sheet for the conditions that match the intended circuit. Load type matters as well as voltage and current; the SPST contact description alone does not establish suitability for a particular load.

Do not infer electrical capacity from the number of poles or throws, terminal appearance, actuator form, or mounting style. Those features do not substitute for the stated electrical ratings. If the available documentation does not establish a rating for the intended current type, load, and conditions, suitability remains unresolved rather than implied by the SPST designation.

### Related guides

- [dual micro switch](/guides/dual-micro-switch/)
- [touch micro switch](/guides/touch-micro-switch/)
- [no nc micro switch](/guides/no-nc-micro-switch/)
- [normally open micro switch](/guides/normally-open-micro-switch/)

## Separate contact arrangement from actuator and mounting

Contact arrangement, actuator style, and mounting describe different attributes. SPST says that one pole controls one switched path. An actuator is the part or mechanism that moves to operate the contacts. A lever, plunger, or another actuator form does not by itself determine whether the contacts are normally open or normally closed. Identify that behavior from the device markings or documentation.

Mounting describes how the switch is mechanically installed. It does not change the pole-and-throw definition. Likewise, a switch that fits a physical location is not thereby shown to have the needed contact behavior or electrical rating. Keep mechanical fit, actuator operation, and circuit ratings as separate checks.

For mechanical integration, consult the specific switch documentation for operating travel and limits. Do not assume those details from the general SPST description or from the actuator’s visible shape. A useful identification sequence is to establish the contact arrangement and normal state, trace the single path through its documented terminals, verify the unpowered contact states, and then compare the intended circuit conditions with the stated ratings. Each step answers a different question; none should be substituted for another.

This concludes the explanation of spst micro switch.

## Sources and references

- Defense Logistics Agency ASSIST: [MIL-PRF-8805K: Switches and Switch Assemblies, Sensitive, Snap Action, General Specification For](https://quicksearch.dla.mil/qsDocDetails.aspx?ident_number=7196){: rel="nofollow noopener noreferrer" }
- Wikipedia: [Miniature snap-action switch](https://en.wikipedia.org/wiki/Miniature_snap-action_switch){: rel="nofollow noopener noreferrer" }
