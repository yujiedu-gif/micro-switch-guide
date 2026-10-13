---
title: "SPDT Limit Switch: How Its Contact Paths Change State"
description: "spdt limit switch: Understand how its two contact paths change state during actuator movement and what to verify before interpreting a circuit diagram."
date: 2026-10-11 18:01:49 +0800
category: Basics
tags:
  - spdt limit switch
  - micro switches
  - Basics
author: editorial_team
---

An **spdt limit switch** uses one common contact and two alternative contact paths. As its actuator moves, the switch can change which path is connected. The exact relationship between a particular actuator position and its electrical contacts depends on the switch’s specified reference state and switching description, so a general diagram should not be treated as a device-specific wiring map.

The key is to keep three ideas separate: the SPDT contact arrangement, the actuator’s mechanical position, and the electrical state of the contacts. A state table or circuit diagram can explain the two paths, but it cannot establish a particular switch’s terminal locations or behavior without the exact device documentation.

## What an SPDT limit switch means

SPDT means **single-pole, double-throw**. In general terms, the arrangement has one common contact, called the pole, and two alternative contacts, called the throws. The common connects to one throw or the other according to the switch’s operating state. The two paths are alternatives in this description; SPDT does not, by itself, specify a switch’s physical construction, actuator style, dimensions, ratings, or terminal layout.

A limit switch describes a switching function associated with mechanical movement reaching a position or limit. More broadly, a miniature snap-action switch can change an electrical contact state in response to mechanical actuator movement and is commonly used for position or limit detection. That general use does not establish whether a specific device is suitable for a particular task.

The contact arrangement and the actuator are different parts of the description. SPDT tells you how the switching contacts are arranged electrically. It does not tell you whether the actuator is a lever, plunger, roller, or another form, nor does it establish how much movement is required. Those details require information about the exact switch.

For the basic mental model, picture a common contact that has two possible routes. In one operating state, the common is connected to one route; in the other state, it is connected to the other. This explains the two switching paths without assigning a universal terminal number or physical position to any contact.

## How an SPDT limit switch changes contact paths

At a general level, an SPDT switch has two operating states for interpreting its contact paths. In one state, the common contact is connected to the first throw. In the other state, it is connected to the second throw. Actuator movement can cause the switch to change between these states. The precise actuation behavior and the state used as the reference must be checked in the documentation for the exact switch.

A neutral state table can show the arrangement without presuming terminal numbers or a particular physical layout:

| Operating state | Common-to-throw path 1 | Common-to-throw path 2 |
|---|---|---|
| State A | Connected | Not connected |
| State B | Not connected | Connected |

This table communicates the general idea of alternate paths. It does not identify which physical terminal is the common, which throw is normally open or normally closed, or which actuator position corresponds to State A or State B. Those assignments depend on the device’s markings and documented reference state.

It is also important not to read “changes state” as a guarantee about the timing or details of every device’s operation. The general SPDT description identifies alternative contact paths. It does not provide a model-specific switching sequence, movement threshold, or other operating parameter. Use the exact device documentation for those details rather than filling gaps with assumptions based on the generic term.

## How actuator state differs from contact state

An actuator state is a mechanical description. Terms such as “released” and “actuated” describe the actuator’s position or condition. A contact state is an electrical description: it says which contacts are connected. The two descriptions are related because actuator movement can change the contacts, but they are not interchangeable.

For example, calling an actuator “released” does not, by itself, tell you which two terminals are connected. Nor does the word “actuated” establish which path is closed. To make that connection, you need the switch’s defined reference state and its documented switching behavior. A general SPDT description is not enough to establish a universal relationship between actuator position and contact labels.

A diagram may depict contacts in a defined reference state. That drawing can help explain how the manufacturer represents the contact arrangement, but its meaning depends on the diagram’s conventions and accompanying documentation. Do not assume that a drawing’s reference state is identical to an informal description of the actuator as released or unpressed unless the exact documentation says so.

Keeping the two descriptions separate prevents a common interpretation error: treating mechanical position words as if they were electrical contact labels. First identify the mechanical condition being described. Then determine the contact state associated with it from the exact device information.

## What a circuit diagram can and cannot tell you

A circuit symbol or state table can show that a common contact has two alternative paths and indicate which path is connected in a represented state. This is useful for understanding how the two paths relate. A generic symbol, however, does not establish the physical terminal layout of a particular switch.

Terminal names such as COM, NC, and NO are generic changeover terminology: COM means common terminal, NC means normally closed terminal, and NO means normally open terminal. These names are useful only when interpreted in the context of the exact device’s diagram and reference state. They should not be treated as a guide to where terminals sit on a housing.

In particular, a diagram’s left-to-right or top-to-bottom arrangement does not prove that terminals occupy those same positions on the switch. A symbol represents an electrical relationship, not necessarily the device’s physical geometry. Likewise, a housing shape or apparent terminal order is not enough to establish terminal identity.

A state table can clarify alternate contact states, but it has limits. Unless it is tied to the exact switch and defines its reference state, it cannot tell you which actual terminals are connected for a given actuator position. Use the connection diagram, terminal marking, circuit function, and permissible load documented for the exact switch and equipment rather than inferring those details from a generic physical layout.

### Related guides

- [what is a micro switch actuator](/guides/what-is-a-micro-switch-actuator/)
- [reed contact sensor](/guides/reed-contact-sensor/)
- [electrical switch gear](/guides/electrical-switch-gear/)

## When to verify the exact switch documentation

Before applying the general SPDT concept to a particular device, check its terminal labels, defined reference state, and switching description. Confirm how the device documentation relates actuator movement to the contact paths. A generic diagram can explain the concept, but exact-device markings and documentation determine how that concept applies to the switch in front of you.

Do not infer COM, NO, or NC from terminal position, terminal order, or housing shape alone. The labels refer to contact functions, not guaranteed physical locations. The exact connection diagram and terminal markings are the relevant evidence for identifying the contacts.

This explanation does not establish application ratings, permissible loads, or device-specific wiring. Those decisions require the documentation for the exact switch and equipment. Keeping that boundary clear lets the general two-path model remain useful without turning it into an unsupported wiring or compatibility claim.

In short, an **spdt limit switch** has one common contact that connects to one of two throws as its operating state changes. Actuator movement may cause that change, but the actuator’s mechanical position is not itself a contact-state label. Use the exact device documentation to determine the reference state, terminal identity, and documented switching behavior.

## Sources and references

- Defense Logistics Agency ASSIST: [MIL-PRF-8805K: Switches and Switch Assemblies, Sensitive, Snap Action, General Specification For](https://quicksearch.dla.mil/qsDocDetails.aspx?ident_number=7196){: rel="nofollow noopener noreferrer" }
- Occupational Safety and Health Administration: [29 CFR 1910.333: Selection and Use of Work Practices](https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.333){: rel="nofollow noopener noreferrer" }
- Wikipedia: [Miniature snap-action switch](https://en.wikipedia.org/wiki/Miniature_snap-action_switch){: rel="nofollow noopener noreferrer" }
