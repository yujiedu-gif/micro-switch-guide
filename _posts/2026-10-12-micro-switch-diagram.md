---
title: "How to Read a micro switch diagram"
description: "micro switch diagram: Learn to identify the actuator, common, normally open, and normally closed terminals, read contact states, and verify wiring safely."
date: 2026-10-12 16:49:35 +0800
category: Basics
tags:
  - micro switch diagram
  - micro switches
  - Basics
author: editorial_team
---

A **micro switch diagram** is best read as a map of electrical contact behavior, not as a picture of where terminals sit on the switch. Start by identifying the actuator and the contacts, then establish whether the drawing represents the unactuated or actuated state. That state reference determines which paths are closed and which are open.

A miniature snap-action switch can change an electrical contact state in response to mechanical actuator movement and is commonly used for position or limit detection. This general description does not identify the terminals or ratings of a particular switch. Those details must come from the exact switch and equipment documentation.

## What a micro switch diagram represents

A diagram represents the switch symbolically. It can show an operating mechanism and the electrical contacts whose state changes when the mechanism is actuated. Its purpose is to communicate circuit function. It does not necessarily reproduce the switch’s shape, terminal positions, or physical orientation.

A schematic and a physical terminal-layout drawing answer different questions. A schematic shows which terminals connect through the contacts in a given state. A layout drawing, terminal markings, or the switch’s own diagram can help identify where those terminals are physically located. A schematic’s left-to-right or top-to-bottom arrangement is not enough to determine terminal placement.

Before tracing a path, look for a state reference. The drawing may identify the unactuated or actuated condition, or show how the actuator operates the contact. If the reference is unclear, do not assume that the drawing’s visual orientation tells you which contact is closed. Check the exact device schematic or documentation instead.

This distinction matters because symbol conventions can represent the same function in different visual arrangements. The actuator may be shown as a lever, plunger, or another operating form, while the contacts are drawn separately or connected to it by a line or linkage. Treat those features as functional symbols unless the drawing specifically identifies a physical layout.

## Identify the parts in a micro switch diagram

First locate the actuator or operating mechanism. It is the part moved mechanically to operate the switch. Then find the movable contact and the contact points it can connect. Some diagrams make the relationship clear with a linkage; others use a compact symbol. Read the legend or device schematic when a symbol is unfamiliar rather than inferring its meaning from appearance alone.

In generic changeover terminology, **COM** means common terminal, **NC** means normally closed terminal, and **NO** means normally open terminal. These names describe contact relationships in the normal, unactuated state. They do not tell you where the terminals are on a particular switch, and a drawing may use contact symbols without spelling out the names.

For a changeover contact, COM is the shared connection that can be connected to either of the other two terminals as the contact changes state. In the normal, unactuated state, COM is connected to NC and not connected to NO. When the switch is actuated, the contact transfers: COM is connected to NO and not connected to NC. Verify this interpretation against the exact device schematic, because the terms here describe generic changeover terminology, not every possible contact configuration.

Do not treat the actuator symbol as proof of a particular physical mechanism, travel, or terminal arrangement. The drawing’s job is to communicate contact function. The device markings and documentation are needed to identify the actual switch connections.

## Read the micro switch diagram in normal and actuated states

“Normally” refers to the switch’s unactuated state. It does not mean the state that occurs most often during use, nor does it mean the state shown by a switch installed in a particular piece of equipment. Establish the unactuated reference before tracing continuity. Then compare it with the actuated state, in which mechanical movement changes the contact position.

For a generic changeover switch, trace the normal state first. Start at COM and follow the movable contact. The path to NC is closed, so COM and NC have continuity; the path to NO is open, so COM and NO do not have continuity. This describes contact state, not a complete wiring instruction for an appliance or control circuit.

Next trace the actuated state. The contact moves away from NC and toward NO. The COM-to-NC path is open, while the COM-to-NO path is closed. The same terminal names therefore indicate opposite contact relationships across the two states: NC is closed to COM when unactuated, and NO is closed to COM when actuated.

Use the state reference shown by the drawing, not the apparent direction of its lines or symbols. A drawing can be arranged in different ways, and a symbol’s position on the page does not establish whether it depicts the normal or actuated condition. If the state is not stated or is ambiguous, consult the exact switch schematic rather than assuming a convention.

This state-by-state method also prevents a common reading error: confusing a terminal’s name with its current condition. NC does not mean that the path is closed in every state. It identifies the contact that is closed to COM in the normal, unactuated state. Similarly, NO identifies the contact that is open to COM in that state. Actuation changes the connection in a changeover switch.

### Related guides

- [dual micro switch](/guides/dual-micro-switch/)
- [touch micro switch](/guides/touch-micro-switch/)
- [no nc micro switch](/guides/no-nc-micro-switch/)
- [normally open micro switch](/guides/normally-open-micro-switch/)

## Verify the diagram against the actual switch

Do not infer physical terminal location from the schematic’s layout. Compare the diagram with the exact switch’s terminal markings, physical terminal-layout drawing, and equipment documentation. Use the documented connection diagram, circuit function, and permissible load for the exact switch and equipment; a generic physical-layout inference is not a substitute. Follow applicable deenergization and qualification requirements.

For an isolated check, disconnect power and isolate the switch from the circuit before using a continuity tester. Identify COM, NC, and NO from the exact device markings or schematic, not from terminal position alone. Check COM-to-NC and COM-to-NO with the actuator unactuated, then check both paths again while the actuator is operated. For a generic changeover contact, the expected pattern is continuity from COM to NC at rest and from COM to NO while actuated.

Treat this as a check of the isolated switch’s contact behavior, not a test of an energized circuit. Results can vary with contact configuration, so compare observations with the exact switch documentation. If the markings, diagram, or observed behavior do not agree, the diagram may not correspond to that device or configuration; leave the terminal identity unresolved until it can be confirmed from the applicable documentation.

The key is to keep function, state, and physical placement separate. Read the actuator and contacts as symbols, establish whether the reference is unactuated or actuated, and trace the corresponding COM paths. Then verify terminal identity and behavior on the isolated switch using its own documentation. A **micro switch diagram** explains contact relationships; it does not by itself establish the physical terminal arrangement or the permissible load for a particular installation.

## Sources and references

- Defense Logistics Agency ASSIST: [MIL-PRF-8805K: Switches and Switch Assemblies, Sensitive, Snap Action, General Specification For](https://quicksearch.dla.mil/qsDocDetails.aspx?ident_number=7196){: rel="nofollow noopener noreferrer" }
- Occupational Safety and Health Administration: [29 CFR 1910.333: Selection and Use of Work Practices](https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.333){: rel="nofollow noopener noreferrer" }
- Wikipedia: [Miniature snap-action switch](https://en.wikipedia.org/wiki/Miniature_snap-action_switch){: rel="nofollow noopener noreferrer" }
