---
title: "Electric linear actuator home position micro switch wiring: how the signal works"
description: "electric linear actuator home position micro switch wiring: Understand the operating idea, essential terminology, practical checks, limitations, and."
date: 2026-06-15 13:03:42 +0800
last_modified_at: 2026-10-13 11:46:37 +0800
category: Applications
tags:
  - electric linear actuator home position micro switch wiring
  - micro switches
  - Applications
author: editorial_team
---

When an electric linear actuator design uses a micro switch at its home position, the switch can provide a position-dependent contact signal. The **electric linear actuator home position micro switch wiring** therefore describes a relationship between a mechanical position, the switch’s contacts, and the host circuit. It does not, by itself, identify the actuator’s motor-power wiring or explain what the controller does with the signal.

The exact arrangement depends on the actuator and switch documentation. Some actuators may use another homing method, and even when a micro switch is present, its terminal labels, contact state, and role in the circuit cannot be inferred from its appearance or from wire colors. The useful starting point is to trace the documented signal path while keeping the switch, actuator, and controller distinct.

## What electric linear actuator home position micro switch wiring represents

A micro switch is a mechanically actuated electrical component. In a design that uses one to mark an actuator’s home position, movement of the actuator’s external mechanism reaches the switch and changes a contact state. The host circuit can use that change as a position signal. This is a conditional description of the arrangement, not a claim that every electric linear actuator includes a micro switch or uses the same homing method.

Three parts have different roles. The actuator produces linear movement. A mechanical feature associated with that movement contacts the switch actuator at the documented position. The switch changes its electrical contact state, and the host circuit receives or uses that state. The switch is not the actuator itself, and its presence does not establish how the actuator is powered or controlled.

In particular, a home-position signal should not be equated with motor supply wiring. The switch’s contact path may be part of a control or indication circuit, but the available description does not establish which circuit the design uses. Nor does the position signal alone establish that the actuator will stop, reverse, or indicate a condition. Those effects depend on the actual circuit and its logic.

This distinction matters when reading a wiring diagram: identify the documented switch connection separately from actuator power and controller connections. Do not assume a terminal that appears near the switch in a drawing carries motor current, or that a switch wire has a particular function based on its color. The diagram and markings for the exact design, rather than a generic layout, determine those relationships.

## How actuator motion changes the micro switch contact state

The mechanical-to-electrical sequence begins with actuator movement. Where the documented design uses a mechanical feature to contact the switch actuator at home, that contact moves the switch actuator. The switch’s contacts then change state according to its construction and the position of the actuator. This describes the signal’s origin without assuming that the switch is open or closed at home.

The home position is a position in the actuator’s movement. It is not, by itself, a definition of a switch’s electrical state. To know which contacts connect at that position, the documentation must identify the contact arrangement and the reference condition used to describe it. A drawing that shows a switch symbol without sufficient terminal or state information may not establish the specific connection at home.

The switch also remains distinct from the external mechanism that moves it. The actuator’s moving part provides the mechanical input; the switch responds to that input. The exact contact point and arrangement are design-specific. Without documentation, it is not possible to determine how the external mechanism contacts the switch or whether a depicted position corresponds to an operated or unoperated state.

Consequently, a contact-state change supports a limited conclusion: the switch can provide a position-dependent signal in a design that uses it. It does not, without the rest of the circuit information, prove how the host circuit interprets the signal or what the actuator will do next. Keep the physical event, the switch state, and the system response as separate steps when following the diagram.

## Reading COM, NO, and NC in a documented wiring diagram

A generic changeover contact may use the labels COM, NO, and NC. COM means common when that terminal arrangement is documented for the exact switch. NO and NC describe contact relationships relative to a specified reference condition. They should not be treated as unconditional promises about current flow in every actuator position or circuit.

The reference condition matters because the labels describe the switch’s contact arrangement under a stated condition, while the actuator’s movement may operate the switch. To determine the state at home, consult the exact switch documentation and the actuator’s diagram for how the switch is mechanically related to that position. Do not assume that “home” necessarily corresponds to either NO or NC being connected to COM.

Not every device uses the same contact arrangement or terminal labeling. A generic changeover diagram can help explain terminology, but it cannot identify terminals on an undocumented device. Terminal markings and the applicable schematic control. Physical location, terminal order, wire color, or resemblance to a generic drawing is not adequate evidence of terminal identity.

When a diagram does identify COM, NO, and NC, read those labels in the context of its stated reference condition and circuit. That makes it possible to follow the documented contact path without extending the labels beyond their scope. If the reference condition, terminal identification, or contact arrangement is missing or unclear, the home-position state remains unresolved from the information available.

## Why the home signal does not define the actuator’s full wiring

The micro switch’s contact path and the actuator’s motor-power wiring are separate things to identify. A switch may provide a position signal, but the presence of that signal does not show how motor power is connected, what controller inputs are used, or how the system responds. Those details require the wiring documentation for the actual actuator and its associated control circuit.

A host circuit could use a contact change for different purposes. Depending on the design, the response might involve stopping, reversing, indication, or other logic. Switch presence alone does not establish which response applies. It also does not establish polarity, voltage, load suitability, or whether a particular contact is used by the controller. These are design-specific facts, not consequences of the words “home-position switch.”

For that reason, a switch diagram and an actuator wiring diagram should not be collapsed into one generic wiring pattern. The switch documentation identifies its terminals and contact arrangement. The equipment documentation identifies how those contacts relate to the controller and the rest of the circuit. Each document answers a different part of the wiring question, and neither should be replaced by assumptions based on color or physical layout.

If those documents do not show how the contact connects to the host circuit, that connection should be treated as unknown. A contact label alone cannot establish the controller’s behavior, and a controller symbol alone may not identify the switch’s terminal arrangement. The conclusion must remain limited to the documented relationships.

### Related guides

- [bottling machine home position micro switch location](/guides/bottling-machine-home-position-micro-switch-location/)
- [incinerator end of stroke micro switch maintenance](/guides/incinerator-end-of-stroke-micro-switch-maintenance/)
- [rotary indexing table guard interlock micro switch location](/guides/rotary-indexing-table-guard-interlock-micro-switch-location/)
- [security barrier open position micro switch wiring](/guides/security-barrier-open-position-micro-switch-wiring/)

## What to verify before interpreting or changing wiring

Start by confirming that the documentation for the exact actuator identifies a micro switch as part of its homing arrangement. If it does, find the switch’s terminal diagram, the contact arrangement, and any reference condition used to define contact state. Then locate the actuator or equipment wiring diagram that shows how the switch connects to the host circuit. A micro switch’s wiring diagram, terminal marking, circuit function, and permissible load must be documented for the exact switch and equipment; a generic physical-layout inference is not a substitute.

Compare the diagram with the actual terminal markings and documented wiring. Do not identify terminals from wire colors, terminal position, or a generic example. If labels do not match, the reference condition is absent, or the diagram does not establish a connection, do not guess what the wiring means. The available information is not enough to establish terminal identity or circuit behavior.

This verification path is for interpreting documentation, not a procedure for probing or modifying an electrical circuit. Electrical work must follow applicable deenergization and qualification requirements. Do not probe or modify undocumented or hazardous wiring; have qualified personnel handle work outside a safe, documented procedure. The wiring relationship can be understood only to the extent that the exact switch and equipment documentation establish it. In short, **electric linear actuator home position micro switch wiring** can describe a position-dependent contact signal, but it does not by itself define motor power, terminal identity, or the controller’s response.

## Sources and references

- Defense Logistics Agency ASSIST: [MIL-PRF-8805K: Switches and Switch Assemblies, Sensitive, Snap Action, General Specification For](https://quicksearch.dla.mil/qsDocDetails.aspx?ident_number=7196){: rel="nofollow noopener noreferrer" }
- Occupational Safety and Health Administration: [29 CFR 1910.333: Selection and Use of Work Practices](https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.333){: rel="nofollow noopener noreferrer" }
- Wikipedia: [Miniature snap-action switch](https://en.wikipedia.org/wiki/Miniature_snap-action_switch){: rel="nofollow noopener noreferrer" }
