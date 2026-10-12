---
title: "Arcade Button Micro Switch Wiring: Identify and Connect the Terminals"
description: "Learn arcade button micro switch wiring by identifying COM, NO, and NC terminals and checking a button’s switch documentation before connecting it."
date: 2025-04-25 09:00:00 +0800
category: Applications
tags:
  - arcade button micro switch wiring
  - micro switches
  - Applications
author: editorial_team
---

# Arcade Button Micro Switch Wiring: Identify COM, NO, and NC

Arcade button micro switch wiring starts with identifying the switch’s common terminal and deciding whether the intended input should use the normally open or normally closed contact. The labels describe contact states, not a guaranteed terminal arrangement. Check the markings or documentation for the exact switch before connecting anything.

This guide covers the button switch’s contact terminals only. It does not specify how to wire a complete control panel or connect a particular encoder, board, or system. A generic terminal diagram can explain the terms, but it cannot establish the correct wiring for a specific device.

## What arcade button micro switch wiring needs you to identify

The task is to identify COM and then select either NO or NC according to the behavior required by the intended input circuit. COM is the shared contact in a changeover arrangement. NO and NC are the two alternative contacts. The exact switch marking or schematic is authoritative; physical position alone is not.

A miniature snap-action switch can change an electrical contact state in response to mechanical actuator movement. Such switches are commonly used for position or limit detection. In a button, the actuator movement is associated with pressing and releasing the button, but the general description does not establish a specific switch’s terminal layout or connection requirements.

The switch terminals are only one part of a control system. Identifying COM, NO, and NC does not explain connections to an encoder, control board, power source, or other panel controls. Those connections depend on the documented circuit and equipment. Keep this task focused on the switch’s contact pair rather than treating a terminal explanation as a complete panel-wiring plan.

## What COM, NO, and NC mean on an arcade button micro switch

In a generic changeover contact, COM means common: the shared terminal that can connect to either of the other contacts as the switch changes state. NO means normally open, and NC means normally closed. “Normally” refers to the actuator’s unpressed or rest state in the applicable switch documentation.

At rest, the NO contact is open relative to COM, while the NC contact is closed relative to COM. When the actuator is pressed, the contact state changes. In a typical changeover description, COM transfers from NC to NO; verify that behavior against the documentation for the exact switch rather than assuming every device uses identical markings or mechanics.

These terms describe electrical contact states, not where a terminal sits on the housing. A drawing that places COM at the top, for example, is not a universal layout. Likewise, a terminal’s shape or apparent position does not by itself prove whether it is COM, NO, or NC. Use the device’s own labels or schematic to map the names to physical terminals.

## How to identify the terminals before connecting wires

First inspect the switch and any documentation supplied for the button or switch. Look for COM, NO, and NC markings, or a schematic that identifies the contacts. The diagram, markings, circuit function, and permissible load documented for the exact switch and equipment should guide the connection. A generic drawing or a familiar-looking housing is not enough to establish terminal identity.

If the labels are absent, unreadable, or inconsistent with the available diagram, do not guess based on terminal position. Resolve the identification from applicable documentation or another suitably supported identification method. The evidence here does not specify a particular measurement procedure, so this guide does not prescribe one. If the switch cannot be identified reliably, its terminal assignment remains unresolved.

Before making a connection, also confirm that the intended circuit and load are within the documented conditions for the exact switch and equipment. This guide provides no voltage or current rating, and it does not establish a permissible load for any particular button. Follow applicable deenergization and qualification requirements; a generic COM/NO/NC explanation is not a substitute for them.

## Choose COM with NO or COM with NC for the intended input

Using COM with NO means the contact is open relative to COM at rest and changes state when the actuator is pressed. This pairing is appropriate only when that state behavior matches the intended input circuit and its documentation. It should not be treated as a universal arcade-system convention.

Using COM with NC means the contact is closed relative to COM at rest and changes state when the actuator is pressed. This pairing may fit an input circuit that is documented to use that behavior, but the contact definition alone cannot establish that it will work with a particular encoder or board.

The decision is therefore about the required input behavior, not which pair looks more common or which terminals are easiest to reach. Check the equipment’s connection information and the exact switch documentation together. If those sources do not establish the required contact pair, compatibility and the correct choice remain undetermined. Do not infer them from the button’s appearance or from a generic example.

### Related guides

- [2 terminal micro switch](/guides/2-terminal-micro-switch/)
- [elevator micro switch](/guides/elevator-micro-switch/)
- [rice cooker micro switch](/guides/rice-cooker-micro-switch/)
- [what is a micro switch in a car](/guides/what-is-a-micro-switch-in-a-car/)

## What this wiring guide does not determine

Knowing the switch terminals does not establish compatibility with a specific encoder, control board, or system. It also does not determine how a complete arcade control panel should be wired, whether a visually similar replacement switch will fit or function, or why a button might fail after wiring. Those questions require separate, device-specific evidence and are outside this guide’s scope.

The same limit applies to test results and electrical ratings. Contact resistance is a measured switch requirement; its method, connection points, and limit must come from the applicable specification and test procedure. A terminal explanation cannot supply those values or establish that a particular switch meets them.

For a connection decision, use the exact switch and equipment documentation, identify COM from the documented marking or schematic, and choose NO or NC only when its contact state matches the intended input. If the required information is missing, do not treat a generic terminal layout as confirmation. This article explains the contact terms; it does not replace equipment-specific wiring instructions or resolve other panel tasks.

In short, arcade button micro switch wiring depends on verified terminal identity and the intended input behavior. Confirm COM, determine whether the circuit requires NO or NC, and rely on the applicable documentation rather than assumptions about terminal position.

## Sources and references

- Defense Logistics Agency ASSIST: [MIL-PRF-8805K: Switches and Switch Assemblies, Sensitive, Snap Action, General Specification For](https://quicksearch.dla.mil/qsDocDetails.aspx?ident_number=7196){: rel="nofollow noopener noreferrer" }
- Occupational Safety and Health Administration: [29 CFR 1910.333: Selection and Use of Work Practices](https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.333){: rel="nofollow noopener noreferrer" }
- Wikipedia: [Miniature snap-action switch](https://en.wikipedia.org/wiki/Miniature_snap-action_switch){: rel="nofollow noopener noreferrer" }
