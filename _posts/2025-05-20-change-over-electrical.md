---
title: "change over electrical: How Microswitch Changeover Contacts Work"
description: "change over electrical: Learn what changeover contacts do in a microswitch and how to verify their states without guessing terminal identity."
date: 2025-05-20 09:00:00 +0800
last_updated: 2026-10-11 09:00:00 +0800
category: Basics
tags:
  - change over electrical
  - micro switches
  - Basics
author: editorial_team
---

A microswitch can use a changeover contact to switch an electrical connection as its actuator moves. Understanding what “change over electrical” means starts with the contact’s function, not the terminals’ physical positions. The names common, normally open, and normally closed describe relationships between contacts in a specified state; they do not identify a universal terminal layout.

This guide explains those relationships and what a continuity check can establish. It does not identify terminals for a particular device or determine whether a switch is suitable for an application. Exact markings, diagrams, and permissible loads must be verified in the documentation for the switch and equipment.

## What does change over electrical mean in a microswitch?

A changeover contact is an arrangement in which one moving contact changes its electrical connection between two contact paths. In a microswitch, actuator movement can cause a miniature snap-action mechanism to change an electrical contact state. Microswitches are commonly used for position or limit detection, but that general use does not establish the contact arrangement of every microswitch.

In a changeover arrangement, the moving contact is associated with a common connection and can connect to one of two other contacts. When the actuator changes the switch’s mechanical state, the connection changes from one path to the other. “Changeover” describes this switching action. It does not, by itself, say which terminal is physically where, which path is connected in a particular state, or what electrical load the device can handle.

Not every microswitch necessarily has changeover contacts. Some contact arrangements may provide only one switching path. Confirm the contact function from the applicable device marking or schematic rather than assuming that a small snap-action switch has a common, normally open, and normally closed set.

It also helps to separate mechanical action from electrical state. The actuator moves, and the contact mechanism responds by changing the connection. The contact names describe the resulting electrical relationships relative to a stated reference condition. They are not a substitute for the device’s diagram, nor do they specify an electrical rating.

## How do common, normally open, and normally closed contacts relate?

The names common, normally open, and normally closed describe a generic changeover contact in relation to the specified unoperated state. Common, often abbreviated COM, is the shared connection that can connect to either of the other contact paths. Normally closed, or NC, is connected to common in that unoperated reference state. Normally open, or NO, is not connected to common in that state.

When the actuator moves and the switch changes state, the common contact changes connection between the two paths. In the basic changeover relationship, a path that was closed to common in the unoperated state opens, while the other path closes to common. This describes the contact relationship, not a guaranteed timing detail or a universal arrangement of terminals.

The word “normally” needs a clear reference. Here it refers to the specified unoperated state. It should not be read as a prediction about what the switch will do in every installed mechanism or operating condition. If equipment documentation defines the reference condition differently, use that documentation when interpreting its diagram and terminal markings.

Contact function is also distinct from electrical rating. Knowing that a contact is common, normally open, or normally closed does not establish the permissible load or confirm compatibility with a circuit. Those are separate details that must be checked in the applicable documentation for the exact switch and equipment.

## How can you identify the switching state without guessing from position?

Start with the applicable connection diagram and the markings on the device. Use these to identify the terminals and interpret which contact paths are intended to connect in the stated switch condition. Do not infer COM, NO, or NC from a terminal’s physical location, the order of pins, or a general drawing of a different switch. A generic contact diagram explains function; it does not establish the layout of a particular device.

A continuity check can establish whether the tested contact paths are electrically connected or open under the conditions of that check. As a conceptual check, the observed continuity can be compared with the contact states shown in the applicable diagram. This can help distinguish the contact’s observed state without relying on where a terminal sits physically. It does not, by itself, establish a terminal’s identity, the switch’s load rating, or suitability for an application.

Continuity testing is meaningful only when performed under a suitable, de-energized test setup. This is not a procedure for checking a switch while it is part of an energized circuit. Circuit work must follow applicable deenergization and qualification requirements. Where the test setup or interpretation is uncertain, use the relevant equipment documentation and qualified procedures rather than drawing conclusions from a generic contact diagram.

Keep the test result and the terminal assignment separate. A meter observation describes the electrical state of the paths tested under the test conditions. The device marking or schematic supplies the basis for identifying those paths as COM, NO, or NC. Physical position alone supplies neither conclusion.

### Related guides

- [what is a micro switch actuator](/guides/what-is-a-micro-switch-actuator/)
- [reed contact sensor](/guides/reed-contact-sensor/)
- [electrical switch gear](/guides/electrical-switch-gear/)

## What must be verified before applying a changeover contact?

Verify the terminal assignment for the exact switch and configuration using its applicable connection diagram, terminal marking, or other device documentation. A generic changeover diagram is useful for understanding the relationship among contacts, but it cannot confirm which physical terminal serves each function on a specific device. If the device and equipment diagrams differ or leave the assignment unclear, do not resolve the question by guessing from terminal position.

Also check the permissible load and electrical ratings documented for the exact switch and equipment. The contact names describe switching function, not allowable electrical conditions. A continuity result likewise does not show whether a contact can serve a particular load. Applying a contact requires the documented terminal assignment, circuit function, and permissible load to be considered together.

These checks define the boundary between understanding contact action and making an application decision. A changeover contact explains how a connection can transfer between paths as the actuator moves. It does not prove compatibility, suitability, or a particular rating. Use the exact device and equipment documentation, and follow applicable deenergization and qualification requirements for circuit work.

In short, “change over electrical” refers to a contact changing its connection between paths as the actuator moves. Common, normally open, and normally closed describe contact relationships relative to the specified unoperated state, not terminal positions. Identify the actual terminals and limits from the applicable documentation rather than assuming a layout.

## Sources and references

- Defense Logistics Agency ASSIST: [MIL-PRF-8805K: Switches and Switch Assemblies, Sensitive, Snap Action, General Specification For](https://quicksearch.dla.mil/qsDocDetails.aspx?ident_number=7196){: rel="nofollow noopener noreferrer" }
- Occupational Safety and Health Administration: [29 CFR 1910.333: Selection and Use of Work Practices](https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.333){: rel="nofollow noopener noreferrer" }
- Wikipedia: [Miniature snap-action switch](https://en.wikipedia.org/wiki/Miniature_snap-action_switch){: rel="nofollow noopener noreferrer" }
