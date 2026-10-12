---
title: "Normally Open Float Switch: What Its Contact State Means"
description: "normally open float switch: Understand what “normally open” means at a float switch’s reference state and how to interpret its level-triggered contact behavior."
date: 2026-04-03 09:00:00 +0800
last_updated: 2026-10-11 09:00:00 +0800
category: Basics
tags:
  - normally open float switch
  - micro switches
  - Basics
author: editorial_team
---

A **normally open float switch** is described by the electrical state of its contact at a defined normal reference condition: the contact is open in that condition. As liquid level moves the float, the device may actuate and change contact state. The term alone does not tell you which physical float position corresponds to open or closed, or whether the installed resting position is the stated reference condition. Those details depend on the particular device and its documentation.

This article explains the terminology and the general relationship between float movement and contact state. It does not cover circuit wiring, device selection, or fault diagnosis. Wiring, ratings, and application suitability must be determined from device-specific evidence.

## What does normally open float switch mean?

“Normally open” refers to a contact that is electrically open under the applicable normal reference condition. The word “open” describes the contact state, not a physical opening in the float body. In the open state, the contact does not form a closed electrical path through that contact pair. The label describes a state, not the switch’s overall physical appearance.

The reference condition matters. “Normal” should not automatically be taken to mean the float’s visible resting position after installation, its position before liquid enters a tank, or a condition in which power is absent. The relevant normal condition is the one specified for the particular switch. If the documentation does not define it clearly, the label alone is not enough to establish which installed position corresponds to the open state.

A normally open description also does not, by itself, identify the contact terminals. In generic changeover terminology, COM means common, NO means normally open, and NC means normally closed. A generic changeover contact may use those labels, but the exact device marking or schematic controls. Do not assume that every float switch has all three terminals or that a marking convention applies without checking the specific documentation.

Keep the state reference separate from the physical float position. A float can be positioned or mounted in different ways, and its movement can operate the switch. The normally open label alone does not specify the orientation, movement direction, or mechanism that produces a state change. Those are device-specific details.

## How liquid level changes the float switch contact state

A float switch relates a liquid-level change to movement of a float and, through the device’s actuation design, to a change in electrical contact state. As the liquid level moves the float, the switch may change from open to closed or from closed to open. That general relationship explains how the contact can indicate a level-related condition; it does not establish a particular switching direction for every device.

The direction of float movement that actuates the switch depends on the design and installation. A rising level might move a particular float in one direction, while a different arrangement could place or move the float differently. Without device-specific evidence, it is not possible to say that rising liquid always closes a normally open contact, or that falling liquid always opens it. The term “normally open” identifies the contact state at its reference condition, not a universal response to a rising or falling level.

The state change also cannot be assigned a switching threshold from the label alone. The point at which a float actuates, and the positions associated with each contact state, require information for the specific device and its setup. No particular mechanism, threshold, or amount of float travel follows from the words “normally open.”

For interpretation, keep three ideas distinct: liquid level is the condition being sensed; float position or movement is part of the actuation; and open or closed describes the electrical contact state. The device’s design connects these ideas, but the relationship between them is not universal. A drawing or description for the exact switch is needed to determine how they correspond.

## Normally open float switch versus normally closed behavior

At the same applicable reference condition, a normally open contact is open, while a normally closed contact is closed. These terms describe contrasting contact states. They do not independently tell you the float’s physical orientation, the direction in which it moves, or the level at which the contact changes state.

The difference is about contact behavior, not a guarantee of a particular installation result. A normally closed label does not, by itself, explain how a float will respond to a particular liquid-level change. Likewise, a normally open label does not mean the contact must be open whenever the float appears to be resting. The relevant reference condition and actuation behavior must come from the device’s documentation.

The phrase “normally open normally closed float switch” may refer to a comparison of these two contact descriptions, but the wording alone does not establish that a particular switch provides both contact states or has a changeover arrangement. Confirm the contact structure from the exact device marking or schematic rather than inferring it from terminology.

This distinction is enough to clarify the terminology question. Broader implications for circuits or choosing between contact behaviors are outside this article’s scope; consult dedicated wiring or selection guidance for those topics. Neither contact label should be treated as a complete description of an installation.

## What to verify before interpreting a particular float switch

Start with the documentation for the exact device. Check how it defines the normal reference condition and how liquid-level changes actuate the float and contact. If a schematic is provided, use it to interpret the contact symbols and terminal labels. Generic changeover terminology can help explain COM, NO, and NC, but the exact device marking or schematic takes precedence.

Do not infer terminal identity, wiring, electrical ratings, or application suitability from the normally open label alone. The label establishes only a contact state at a stated reference condition. It does not supply enough evidence to determine how to connect a device, what electrical conditions it supports, or whether it is appropriate for a particular tank, liquid, or load. Those matters require device-specific information and are outside this article’s scope.

If the documentation does not clearly state the reference condition or level-actuation behavior, the relationship between a particular float position and contact state remains unresolved. Avoid filling that gap with assumptions based on the float’s apparent resting position, a generic diagram, or another device’s behavior. Use dedicated wiring, selection, and troubleshooting resources for those separate tasks, while relying on the exact device documentation for its characteristics.

### Related guides

- [what is a micro switch actuator](/guides/what-is-a-micro-switch-actuator/)
- [reed contact sensor](/guides/reed-contact-sensor/)
- [electrical switch gear](/guides/electrical-switch-gear/)

## Normally open float switch: the key state reference

A normally open float switch has an open contact at its applicable, documented normal reference condition. “Open” names an electrical contact state, not a physical opening in the float. Liquid-level movement can move the float and actuate the contact, but the physical position and direction associated with each state depend on the device and its installation.

Therefore, do not equate “normally open” with a particular resting orientation or assume a universal response to rising or falling liquid. Verify the reference condition and actuation behavior in the exact device documentation. The terminology defines the contact state; it does not, by itself, establish wiring, ratings, or application suitability.

## Sources and references

- Defense Logistics Agency ASSIST: [MIL-PRF-8805K: Switches and Switch Assemblies, Sensitive, Snap Action, General Specification For](https://quicksearch.dla.mil/qsDocDetails.aspx?ident_number=7196){: rel="nofollow noopener noreferrer" }
- Wikipedia: [Miniature snap-action switch](https://en.wikipedia.org/wiki/Miniature_snap-action_switch){: rel="nofollow noopener noreferrer" }
