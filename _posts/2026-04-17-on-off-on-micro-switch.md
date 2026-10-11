---
title: "On Off On Micro Switch: How Its Three Positions Work"
description: "Learn how an on off on micro switch behaves in each position, what its circuit states mean, and which details to verify before applying it in a circuit."
date: 2026-04-17 09:00:00 +0800
last_updated: 2026-10-11 09:00:00 +0800
category: Basics
tags:
  - on off on micro switch
  - micro switches
  - Basics
author: editorial_team
---

An **on off on micro switch** description refers to three operating positions: one ON end position, a center OFF position, and another ON end position. Electrically, those labels describe the contact state associated with each position, not a universal arrangement of terminals. A switch’s actual contact behavior must be confirmed from documentation for that specific device and the equipment in which it is used.

The distinction matters because the actuator’s location and the terminals’ physical positions do not, by themselves, identify which contacts are connected. The same operating description is not enough to determine a wiring arrangement, permissible load, or compatibility with a circuit. The sections below explain what the three-position description communicates and what it leaves unresolved.

## What does on off on micro switch mean?

ON-OFF-ON is a description of three operating positions. The first end position is described as ON, the center position as OFF, and the other end position as ON. In general, ON and OFF refer to electrical states: a miniature snap-action switch can change an electrical contact state in response to mechanical actuator movement. The labels do not, on their own, specify which terminals connect in any position.

The two ON labels indicate that the two end positions are both described as ON states. They do not establish that the same contacts are connected in both positions, or that different contacts are connected. Those details depend on the contact arrangement documented for the exact switch. Likewise, the center OFF label does not establish a universal terminal layout or identify a particular terminal as open or disconnected.

Treat the words as an operating description, not a complete connection diagram. They identify a sequence of states as the actuator moves between positions, but they do not define terminal numbers, terminal locations, or a standard physical layout. A drawing that places terminals in a particular order cannot be inferred from the phrase ON-OFF-ON alone.

A switch may be described this way in a particular equipment context, but that description is not enough to determine how it functions in that equipment. The relevant reference is the applicable connection diagram and documentation for the exact switch and equipment. Those materials identify the intended circuit function and the permissible load, where documented.

In general background, miniature snap-action switches can be used for position or limit detection by changing an electrical contact state in response to mechanical actuator movement. That general use does not establish that a particular ON-OFF-ON switch is suitable for a particular position-detection task or circuit.

## How the three positions differ

The three positions can be understood as a sequence of operating states, without assigning terminal numbers:

| Actuator position | Description | What the description establishes |
|---|---|---|
| One end position | ON | This position is designated as an ON state. The connected contacts are not identified by the label alone. |
| Center position | OFF | This position is designated as an OFF state. The label alone does not identify a terminal arrangement. |
| Other end position | ON | This position is also designated as an ON state. Its contact connections must be checked in the applicable documentation. |

The table restates the operating description; it is not a contact chart. It does not show which terminal is common, normally open, or normally closed, and it does not say whether either end position uses the same contacts as the other. Those facts require device-specific evidence.

Keep actuator position and electrical connection separate when reading a diagram. The actuator position tells you where the mechanism is. The contact representation in the applicable diagram tells you which connections are made in that position. A terminal’s location on a housing or drawing is not enough to identify its function, and the visual order of the three positions does not supply missing contact information.

Also check how the documentation defines the operating positions. A diagram may use its own symbols, labels, or reference conditions. Read those definitions before interpreting a state as a particular contact connection. If the equipment documentation and switch documentation appear to describe different functions, the phrase ON-OFF-ON does not resolve the discrepancy; the applicable device and equipment documentation must do so.

## How to verify contact behavior safely

Start with the connection diagram, terminal markings, and documentation applicable to the exact switch and equipment. Use those references to identify the documented circuit function and permissible load. Do not substitute a generic diagram or infer terminal functions from physical layout. A terminal’s position, shape, or apparent similarity to a terminal in another device does not establish its electrical role.

The ON-OFF-ON label alone cannot tell you which terminal is common, normally open, or normally closed. It also does not establish which contacts change state as the actuator moves. If you need to understand a circuit, compare the documented contact states with the equipment’s circuit diagram and the switch’s terminal markings. If those references do not identify the behavior clearly, the available description is insufficient to determine the connections.

This is a documentation-based explanation, not a procedure for wiring or testing a particular circuit. The applicable safety and qualification requirements still govern any work. Do not treat the operating description as permission to handle, disconnect, or test a circuit. The source documentation and the conditions under which the equipment may be examined determine what steps are appropriate.

A general continuity-check procedure is not specified here. The supplied operating description does not establish a test method, instrument setup, or test condition for a particular switch. Avoid treating an assumed test result as a substitute for the correct diagram or applicable documentation. Where contact behavior remains uncertain, the general label cannot fill in the missing device-specific details.

### Related guides

- [what is a micro switch actuator](/guides/what-is-a-micro-switch-actuator/)
- [how long do micro switches last](/guides/how-long-do-micro-switches-last/)
- [how to wire a micro switch](/guides/how-to-wire-a-micro-switch/)
- [micro switch com](/guides/micro-switch-com/)

## What this switch description does not tell you

ON-OFF-ON describes operating states, but it does not establish a switch’s voltage or current rating, load suitability, certification, environmental protection, or compatibility with an appliance or circuit. Those details require separate documentation applicable to the exact switch and equipment. A general description of snap-action operation or position-detection use does not supply any of those specifications.

Nor does the phrase establish a universal terminal layout, the identity of a particular model, or an intended application. No terminal assignment or connection can be derived solely from the order of the words ON, OFF, and ON. The exact connection diagram, terminal marking, circuit function, and permissible load documented for the device and equipment are the relevant references.

If your next question concerns a particular appliance or circuit, the operating description alone is not enough to answer how to connect it. Questions about selecting a switch by voltage, current, load type, or environmental rating also require their own applicable specifications. Keep those tasks separate from interpreting the three-position description, and do not fill evidence gaps with assumptions based on appearance or terminology.

In short, the three positions describe two ON end states with a center OFF state, while leaving the actual terminal connections unresolved. For the **on off on micro switch** in your equipment, rely on its applicable documentation rather than a presumed universal layout.

## Sources and references

- Defense Logistics Agency ASSIST: [MIL-PRF-8805K: Switches and Switch Assemblies, Sensitive, Snap Action, General Specification For](https://quicksearch.dla.mil/qsDocDetails.aspx?ident_number=7196)
- Occupational Safety and Health Administration: [29 CFR 1910.333: Selection and Use of Work Practices](https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.333)
- Wikipedia: [Miniature snap-action switch](https://en.wikipedia.org/wiki/Miniature_snap-action_switch)
