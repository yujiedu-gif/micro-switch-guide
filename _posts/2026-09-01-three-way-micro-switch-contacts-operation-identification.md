---
title: "Three way micro switch: contacts, operation, and identification"
description: "three way micro switch: Understand the operating idea, essential terminology, practical checks, limitations, and evidence needed for careful selection,."
date: 2026-09-01 09:00:00 +0800
category: Basics
tags:
  - three way micro switch
  - micro switches
  - Basics
author: editorial_team
---

# Understanding a micro switch with three-way contacts

The phrase **three way micro switch** can describe a single miniature snap-action switch with a common terminal and two selectable contacts. It does not, by itself, say that two switches control a load from separate locations. The distinction matters: one phrase can refer either to the contacts inside one component or to the behavior of a larger circuit.

A micro switch can change an electrical contact state in response to mechanical actuator movement and is commonly used for position or limit detection. To identify its terminals, focus on the contact diagram and on how continuity changes between the actuator’s released and operated states. Terminal position or appearance alone is not enough to establish function.

## What does three way micro switch mean?

In this context, “three way” may refer to a changeover contact with three terminals: common (COM), normally closed (NC), and normally open (NO). The common terminal is the shared connection that changes between the other two contacts as the actuator moves. “Three way” is therefore a description of a possible contact arrangement, not a complete account of how a load is controlled.

A single switch with this arrangement provides a choice of contact path within the component. A circuit that controls a load from separate locations is a different matter: its behavior depends on the complete circuit and the use of multiple switches. The term alone does not establish that such a circuit exists or explain how it is wired.

The applicable switch diagram determines whether a particular device has this arrangement and how its terminals are marked. Generic COM, NC, and NO terminology can help interpret a changeover contact, but the exact device marking or schematic controls. Do not identify a terminal solely by where it sits on the housing, by its shape, or by an assumed standard layout.

## Three way micro switch contacts and switching states

“Normally” describes the contact condition with the actuator unoperated, or released. In a generic changeover contact, COM is the common terminal. NC is connected to COM in the released state; NO is not connected to COM in that state. When the actuator is operated, the contact changes over: the COM-NC path opens and the COM-NO path closes. Releasing the actuator returns the contact toward its unoperated state.

| Actuator state | COM-NC | COM-NO |
|---|---|---|
| Released (unoperated) | Continuity expected | No continuity expected |
| Operated (pressed) | No continuity expected | Continuity expected |

This table describes the expected behavior of a generic changeover contact, not a guarantee about every switch. A device’s own diagram takes precedence, and a different contact configuration may not provide both an NO and an NC path. The actuator’s released and operated positions are the relevant state references; the terminal’s physical location is not.

The state change is the useful identifying feature. If COM is correctly identified, the two other terminals show complementary behavior in a typical changeover arrangement: one path conducts in the released state, and the other conducts in the operated state. That pattern helps distinguish the contacts without relying on appearance, while the applicable documentation confirms whether the observed arrangement matches the device.

## How to identify and verify the terminals safely

Before checking contacts, disconnect power and isolate the switch from parallel circuit paths. A connection elsewhere in the circuit can affect what a meter reads, so the switch must be isolated from those paths for the result to reflect its own contacts. Do not use readings from an energized circuit as a substitute for this de-energized identification process.

With power disconnected and the switch isolated, use a continuity meter to check candidate terminal pairs with the actuator released, then operated. For a generic changeover contact, look for continuity between COM and NC when released, and between COM and NO when operated. The other COM path should show the opposite state. If the terminal labels are present, compare the readings with those markings and the contact diagram rather than assuming that a particular physical position is COM, NO, or NC.

Interpret the change across both actuator states, not just one reading. A single reading may not distinguish a normally open path from a normally closed one unless the actuator state is known. Record which state was checked and whether the actuator was released or operated. If the readings conflict with the switch’s markings or documentation, stop and resolve that discrepancy before treating a terminal as identified.

This is a bounded contact-identification check, not a method for establishing suitability for a load or explaining how to wire a fixed circuit. The exact device diagram and the observed state changes are the evidence for terminal identification. If those do not agree, the available information is insufficient to assign the terminals confidently.

## A changeover micro switch versus two-location control

A single changeover contact inside one micro switch selects between two contact paths through its common terminal. That component-level arrangement is not automatically the same as a circuit that allows a load to be controlled from separate locations. Two-location control concerns the topology of the complete circuit, not merely the number of terminals on one switch or the phrase “three way.”

This distinction prevents a common identification error: seeing three terminals and assuming they describe a two-location control setup. The terminals describe contact relationships within the switch, while multi-location behavior depends on how the complete circuit is arranged and on the switches it contains. The switch’s contact diagram can identify its own configuration, but it does not establish the topology or behavior of a larger circuit.

No household wall-switch wiring procedure follows from identifying COM, NO, and NC on a micro switch. This explanation is limited to contact states and component identification. Questions involving energized or fixed wiring fall outside that scope and should be handled with qualified help rather than inferred from a generic contact description.

### Related guides

- [dual micro switch](/guides/dual-micro-switch/)
- [touch micro switch](/guides/touch-micro-switch/)
- [no nc micro switch](/guides/no-nc-micro-switch/)
- [normally open micro switch](/guides/normally-open-micro-switch/)

## When the contact readings do not match expectations

If the readings do not follow the expected pattern, first confirm that the circuit is isolated from other current paths and that the actuator reaches both its released and operated states. A switch that has not fully returned may not be in the state being assumed. Recheck the terminal markings and the applicable contact diagram before drawing a conclusion from the meter readings.

Do not force a COM-NC or COM-NO assignment to fit the generic table. Different contact configurations may not provide both NO and NC paths, and the exact switch documentation controls. If the observed readings still conflict with the markings or diagram, leave the terminal identities unresolved until the discrepancy is clarified. The key is to base identification on the documented configuration and the change in continuity across known actuator states, not on terminal layout or the phrase “three way” alone.

In short, a three-way description may refer to a single changeover micro switch with COM, NC, and NO contacts, but the phrase is ambiguous. Confirm the actual configuration from the device diagram, then compare the isolated contact paths with the actuator released and operated. That identifies the component’s contact behavior without confusing it with a two-location circuit.

This concludes the explanation of three way micro switch.

## Sources and references

- Defense Logistics Agency ASSIST: [MIL-PRF-8805K: Switches and Switch Assemblies, Sensitive, Snap Action, General Specification For](https://quicksearch.dla.mil/qsDocDetails.aspx?ident_number=7196){: rel="nofollow noopener noreferrer" }
- Wikipedia: [Miniature snap-action switch](https://en.wikipedia.org/wiki/Miniature_snap-action_switch){: rel="nofollow noopener noreferrer" }
