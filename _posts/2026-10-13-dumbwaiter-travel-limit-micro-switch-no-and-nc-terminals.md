---
title: "dumbwaiter travel limit micro switch NO and NC terminals: What Do They Mean?"
description: "dumbwaiter travel limit micro switch NO and NC terminals: Understand the operating idea, essential terminology, practical checks, limitations, and."
date: 2026-10-13 11:27:16 +0800
category: Applications
tags:
  - dumbwaiter travel limit micro switch NO and NC terminals
  - micro switches
  - Applications
author: editorial_team
---

A dumbwaiter travel limit micro switch NO and NC terminals describe contact states only in relation to a defined reference condition. The labels do not, by themselves, say what the switch contacts are doing at every point in travel or what the dumbwaiter will do when a contact changes. To interpret them, first identify the switch’s documented contact arrangement and the actuator state used as its reference.

A miniature snap-action switch can change an electrical contact state in response to mechanical actuator movement and is commonly used for position or limit detection. In a dumbwaiter design that uses one, travel-related movement may operate the switch. That component-level change is separate from the controller’s response and from the system’s safety function. Terminal labels alone establish none of those application details.

## Dumbwaiter travel limit micro switch NO and NC terminals: Read the labels in context

NO means “normally open,” and NC means “normally closed,” but “normally” needs a reference. These labels describe the documented contact state at a specified reference condition, not an unconditional statement about current flow in every operating state. The reference may be stated in the switch documentation in relation to whether the actuator is operated or released. Do not assume which condition applies unless the documentation identifies it.

First establish that the particular switch has the documented contact arrangement being interpreted. Then find the terminal diagram and the stated reference condition. If the documentation identifies a contact as NO or NC at that condition, use that definition for that contact. When the actuator moves away from the reference state, the contact state may change according to the switch design. The labels alone do not give the contact state at every actuator position.

This distinction matters in a travel-limit application because “normally” does not necessarily mean the dumbwaiter’s ordinary operating position, its usual travel state, or a safe state. Those are descriptions of the equipment and its control logic, not definitions supplied by the NO and NC labels. Without the switch’s stated reference condition, translating the labels into an assumed position or operating state would be guesswork.

If the documentation does not identify the contact arrangement or reference condition, the labels cannot be interpreted reliably from the equipment’s travel position alone. Numerical travel limits are device-specific requirements of the applicable specification sheet; they must not be inferred from the component category. A terminal label is not a travel measurement or a statement of the point at which the switch operates.

## How a micro switch can respond to travel movement

The actuator is the part of a switch moved by an external mechanism. In a design using a micro switch for position or limit detection, a mechanical part associated with travel may move the actuator near a travel position. That movement can change the switch’s electrical contact state. This describes a possible component relationship, not a claim about a particular dumbwaiter’s arrangement.

The exact mechanical relationship is design-specific. The available facts do not establish which dumbwaiter part moves the actuator, the direction of movement, the point at which a contact changes, or whether movement occurs at a particular end of travel. They also do not establish that every dumbwaiter uses a micro switch. A switch’s documented operating and travel information, where relevant, belongs to the applicable device specification, not to a general assumption about the equipment class.

Keep the two states conceptually separate: the external mechanism moves the actuator, and the switch changes a contact state according to its design. The contact change is the component-level event. It is not, by itself, proof that the dumbwaiter has reached a particular position or that the travel limit has been handled in a specific way.

This conditional description is useful when reading documentation: look for the switch’s contact-state definition and the equipment documentation’s account of the mechanism that actuates it. Do not infer the mapping from NO or NC to a particular direction, position, or trip point. The terminal labels describe contact states at a reference condition; they do not identify the mechanical arrangement that produces movement.

## Why terminal labels do not tell you what the dumbwaiter will do

A micro switch contact change and a controller response are different things. The switch can provide a change in electrical contact state in response to actuator movement. The dumbwaiter’s circuit and controller determine how that contact is used. The NO and NC labels do not reveal the installed wiring, the controller’s interpretation, or the resulting equipment behavior.

For example, the labels alone do not establish whether a contact change stops travel, affects a control signal, or has another role. They do not establish whether a travel limit is part of a safety function, how that function is designed, or what state the equipment treats as safe. Those conclusions require the relevant equipment documentation; they cannot be derived from terminal names.

Do not read “normally” as a guarantee about what happens when power is present or absent, or as a description of the dumbwaiter’s normal operation. The reference condition belongs to the switch’s contact definition. The equipment’s operating state and response belong to its circuit and controller. Without documentation connecting these layers, the relationship remains unknown.

This boundary also prevents a contact description from being mistaken for a complete system assessment. A stated NO or NC state can help identify a documented contact, but it cannot confirm that the installed wiring matches a diagram, that the controller responds as intended, or that the overall system performs a safety function. Terminal labels alone do not establish suitability for a particular dumbwaiter or application.

### Related guides

- [bottling machine home position micro switch location](/guides/bottling-machine-home-position-micro-switch-location/)
- [incinerator end of stroke micro switch maintenance](/guides/incinerator-end-of-stroke-micro-switch-maintenance/)
- [rotary indexing table guard interlock micro switch location](/guides/rotary-indexing-table-guard-interlock-micro-switch-location/)
- [security barrier open position micro switch wiring](/guides/security-barrier-open-position-micro-switch-wiring/)

## What to verify in the relevant documentation

Use the switch documentation to identify the terminal arrangement and the exact reference condition for its NO and NC descriptions. Read the terminal diagram as a component definition, not as a complete dumbwaiter wiring diagram. If the reference condition or contact arrangement is not stated, leave the terminal behavior unresolved rather than assigning it from the equipment’s position or customary operation.

Then consult the dumbwaiter’s own circuit documentation to determine how the documented contact is connected and how the controller uses it. That information is needed to establish the relationship between a contact change and equipment behavior. Do not assume the switch is wired as NO or NC merely because a terminal bears that label; the label describes the documented contact state, not which terminals are installed in a circuit.

Keep the verification question bounded: the switch documentation explains its contact states under stated conditions, while the equipment documentation explains the installed circuit’s use of those contacts. Neither a terminal label nor an isolated contact description, on its own, proves the installed system’s condition or safety function. Numerical travel limits likewise require the applicable device specification sheet and must not be inferred from the general category “micro switch.”

Electrical work has an additional boundary. Under the cited United States workplace rule, exposed live parts generally must be deenergized before work; a qualified person must verify the deenergized condition with test equipment, and work on energized parts is limited to qualified persons. Verify all applicable requirements. This article does not provide a wiring, bypass, repair, or certification procedure.

In short, dumbwaiter travel limit micro switch NO and NC terminals identify contact states only when their documented reference condition and contact arrangement are known. They do not, by themselves, specify the travel position, installed wiring, controller response, or safety function. Use the switch documentation for the component definition and the equipment documentation for the system behavior.

## Sources and references

- Defense Logistics Agency ASSIST: [MIL-PRF-8805K: Switches and Switch Assemblies, Sensitive, Snap Action, General Specification For](https://quicksearch.dla.mil/qsDocDetails.aspx?ident_number=7196){: rel="nofollow noopener noreferrer" }
- Occupational Safety and Health Administration: [29 CFR 1910.333: Selection and Use of Work Practices](https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.333){: rel="nofollow noopener noreferrer" }
- Wikipedia: [Miniature snap-action switch](https://en.wikipedia.org/wiki/Miniature_snap-action_switch){: rel="nofollow noopener noreferrer" }
