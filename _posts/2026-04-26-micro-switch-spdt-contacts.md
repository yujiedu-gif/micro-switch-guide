---
title: "micro switch SPDT contacts: What do COM, NO, and NC mean?"
description: "micro switch SPDT contacts: Understand the operating idea, essential terminology, practical checks, limitations, and evidence needed for careful."
date: 2026-04-26 21:36:23 +0800
last_modified_at: 2026-10-13 11:46:37 +0800
category: Basics
tags:
  - micro switch SPDT contacts
  - micro switches
  - Basics
author: editorial_team
---

A micro switch SPDT contacts description identifies a contact arrangement, but the labels COM, NO, and NC do not by themselves tell you what an appliance will do. Their meanings depend on the specified reference condition for the switch. Read the labels as descriptions of contact relationships in that condition, then treat movement and connected-circuit behavior as separate questions.

This explanation concerns an electromechanical micro switch. It does not apply automatically to every device called a switch, and it does not establish how a particular switch is wired or rated. The key distinction is between the switch’s contact arrangement and the behavior of the larger circuit: labels describe the former, while wiring and equipment design determine the latter.

## micro switch SPDT contacts: the basic contact arrangement

SPDT names a contact arrangement. In an arrangement documented as single-pole, double-throw, one common contact is associated with two alternative contact paths. For a micro switch with this documented arrangement, COM identifies the common terminal; NO and NC identify the other contact terminals by their relationship to COM at a stated reference condition.

The scope matters. The term SPDT should be used only where that contact arrangement is documented for the switch. The labels are not a substitute for confirming the terminal arrangement of an unidentified component. Nor should the terminology be applied to an unrelated wall switch, push-button, sensor, or other device simply because it is also called a switch.

A contact arrangement describes relationships within the component. It does not, on its own, specify the voltage or current in a circuit, the kind of load connected, or the purpose of the switch in a machine. Those are separate facts that require evidence about the particular component and its circuit. Even when a switch has COM, NO, and NC terminals, the names alone do not establish a rating, load suitability, or correct installation.

The phrase “double throw” also should not be read as a complete description of what happens in an appliance. It describes the contact arrangement, not the equipment’s control logic. A circuit may use one contact path, the other, or a broader arrangement involving other components. Without the actual design, the result of a contact change remains unknown.

## What COM, NO, and NC mean at the stated reference condition

COM means common when that terminal is documented as part of the contact arrangement. NO means normally open, and NC means normally closed, but “normally” needs a reference condition. The labels describe contact state relative to that specified condition, not an unconditional promise about whether current is flowing.

At the stated reference condition, the NO contact is open relative to COM, and the NC contact is closed relative to COM. These descriptions concern the contacts inside the switch. “Open” describes a contact relationship; it does not establish that a connected wire or appliance is de-energized. “Closed” describes the contact relationship; it does not prove current is flowing. Current flow also depends on the surrounding circuit and its state.

The reference condition must be explicit in the relevant documentation. Do not silently replace it with an assumed condition such as “unpressed,” “unactuated,” or “machine off” unless that is what the documentation specifies. If the reference condition is not known, the NO and NC labels alone are insufficient to determine the contact state at an arbitrary actuator position.

This distinction prevents a common interpretive error: treating “normally” as a description of normal appliance operation. Here it is a reference for describing the switch’s contacts. It does not say that the host equipment is usually on or off, that a machine is in a safe state, or that a particular alarm or shutdown will occur. Those conclusions require information about the equipment and circuit, not just the terminal names.

## How actuator movement relates to the contact change

A micro switch is an electromechanical component: external mechanical movement acts on its actuator, and the contacts can change state as part of the switch’s operation. The actuator is the part moved by the external mechanism. That mechanical input and the contact transition are related, but they are not interchangeable descriptions. A stated contact condition must still be tied to its documented reference condition.

The terminal labels do not specify which external part moves the actuator, how far it moves, or what event in the host equipment causes that movement. A lever, linkage, cam, or other mechanism may be involved in a particular design, but none should be presumed from the SPDT label. Likewise, the labels do not tell you which contact path a machine’s control logic uses or what that logic does after a contact change.

Keep the causal sequence bounded: an external mechanism may move the actuator; the switch’s contacts may transition; and the connected circuit may respond according to its wiring and design. The first two steps concern the mechanical switch and its contacts. The last concerns the larger electrical system. A contact-state description alone cannot establish that system response.

A click, if heard, would not by itself identify which contact state exists or prove current flow. The arrangement and reference condition still govern the interpretation, while the circuit response remains dependent on the equipment design. Do not use the terminal labels as a shortcut for inferring an unobserved actuator state or an equipment function.

### Related guides

- [micro switch flyback diode causes](/guides/micro-switch-flyback-diode-causes/)
- [panel mount plunger micro switch working principle](/guides/panel-mount-plunger-micro-switch-working-principle/)
- [cam follower micro switch adjustment](/guides/cam-follower-micro-switch-adjustment/)
- [micro switch SPST NC contacts explained](/guides/micro-switch-spst-nc-contacts-explained/)

## What SPDT labels do not tell you

COM, NO, and NC identify contact relationships only within their documented scope. They do not establish that the switch is wired correctly, that a chosen contact path matches an appliance’s design, or that the switch is suitable for a load. Those conclusions require information not contained in the labels, including the relevant component and circuit documentation. No rating, load type, or compatibility claim follows from the SPDT designation alone.

The labels also do not establish the behavior of a connected system. If an equipment function changes when a contact changes, that result depends on how the switch is wired and on the equipment’s control logic. The same label cannot, by itself, show whether a machine starts, stops, signals an alarm, or does something else. Do not infer a particular normal operating state from “NO” or “NC.”

For interpretation, keep three questions separate: What contact arrangement is documented? What reference condition defines the NO and NC descriptions? What does the actual circuit do with those contacts? The first two concern the switch description. The third cannot be answered from terminal labels alone. If any of these facts is missing, preserve that uncertainty rather than filling it with an assumption.

In short, micro switch SPDT contacts describe a documented common terminal and two contact relationships: NO is open to COM and NC is closed to COM at the stated reference condition. The labels describe contact state, not guaranteed current flow, wiring correctness, load suitability, or appliance behavior. The surrounding circuit and equipment design determine what a contact transition means in use.

## Sources and references

- Defense Logistics Agency ASSIST: [MIL-PRF-8805K: Switches and Switch Assemblies, Sensitive, Snap Action, General Specification For](https://quicksearch.dla.mil/qsDocDetails.aspx?ident_number=7196){: rel="nofollow noopener noreferrer" }
