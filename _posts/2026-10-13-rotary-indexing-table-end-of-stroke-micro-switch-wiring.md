---
title: "Rotary indexing table end of stroke micro switch wiring"
description: "rotary indexing table end of stroke micro switch wiring: Understand the operating idea, essential terminology, practical checks, limitations, and evidence."
date: 2026-10-13 09:00:00 +0800
category: Applications
tags:
  - rotary indexing table end of stroke micro switch wiring
  - micro switches
  - Applications
author: editorial_team
---

A **rotary indexing table end of stroke micro switch wiring** question is best approached by tracing the signal from the table’s motion to the switch contacts, then separately tracing those contacts into the equipment circuit. The switch alone does not reveal what the table will do when it changes state. Only table designs that use an electromechanical micro switch are in scope; the arrangement and control logic depend on the particular equipment.

Start with the switch’s documentation and the table’s circuit diagram. Identify the terminals and the specified reference condition before interpreting a contact state. If a procedure permits an isolated continuity check, record the actuator state and compare the result with the documented contact arrangement. That check concerns the switch, not the complete wiring or table operation.

## What end-of-stroke means at the micro switch

“End of stroke” describes a position in the table’s movement, not a universal micro switch terminal function or a guaranteed control response. In a design that uses a micro switch for this signal, the table mechanism may move the switch actuator at a defined position. Actuator movement can change the switch’s contact state, and the contacts can provide an input to the surrounding circuit. That sequence is the useful starting point: table movement, actuator engagement, contact change, then circuit response.

The physical arrangement is design-specific. A rotary indexing table may use a mechanism that engages an actuator, but the switch’s presence, mounting, actuator type, and exact engagement point cannot be assumed for every table. Consult the equipment documentation to establish whether a micro switch is used and how the mechanism acts on it. Do not treat “end-of-stroke” as proof that the actuator is engaged, that a particular contact is closed, or that motion must stop at that point.

The micro switch is a component in a larger electrical system. Its contact change may be used as a signal, but the table’s control circuit determines how that input is interpreted. The switch by itself does not establish whether the circuit stops motion, advances an index, signals a controller, or produces another response. Those outcomes remain unresolved until the actual circuit and its documented function are traced.

## Rotary indexing table end of stroke micro switch wiring: identify contacts before tracing

Use the terminal markings and connection information for the exact switch and equipment. If the contact arrangement documents COM, NO, and NC, identify those terminals from the markings or documentation. COM means common for that documented arrangement; NO and NC describe contact states at a specified reference condition. They are not interchangeable labels for “the wire that stops the table” or for an assumed unpowered, home, or end-of-stroke state.

The reference condition matters. Record the condition attached to the documentation, such as whether the actuator is unoperated or operated, and use that condition when interpreting the stated contact arrangement. Do not infer the terminal function from wire color, the physical position of a terminal, or an assumed normal state. A generic physical-layout inference is not a substitute for the connection diagram and terminal markings of the particular switch.

Then trace the conductors from the identified terminals through the equipment wiring diagram. Follow the documented circuit function rather than assuming the switch contacts directly carry a motor-control load or directly stop table motion. The permissible load and ratings must come from documentation for the exact switch and equipment. A contact label alone does not establish electrical suitability for a load, and a switch rating cannot be transferred to a different load or installation without supporting documentation.

Keep the component trace separate from the control-logic interpretation. The first task is to determine which documented terminals connect to which conductors. The second is to follow those conductors through the table circuit to understand what the signal is intended to do. Without that circuit information, the downstream response cannot be inferred from the switch wiring alone.

## Verify the isolated micro switch separately

An isolated continuity check, when permitted by a documented procedure, addresses the switch’s contacts under a defined actuator condition. First establish that the switch is isolated from the circuit as required by that procedure. Identify the documented contact arrangement and reference condition, move or hold the actuator in the specified state, and compare the measured continuity with the expected state for that arrangement. The meaning of a result depends on those conditions; an unspecified reading is not enough to diagnose the table.

Keep a record of which terminals were tested and whether the actuator was in the documented operated or unoperated state. If the expected behavior is not available in the switch documentation, do not invent it from the terminal layout or the table’s apparent position. A discrepancy could reflect an incorrect terminal identification, an actuator that did not reach the intended state, a contact problem, or another issue. The isolated check can help distinguish a contact-state question from an installed-circuit question, but it does not identify every possible cause.

A click may indicate movement of a snap mechanism, if the particular design has one, but it does not prove electrical continuity, correct wiring, load suitability, or proper table operation. Likewise, an isolated continuity result does not prove that the conductors are correctly connected, that the circuit responds as documented, or that the table reaches its intended position. Treat the check as one bounded observation about the isolated switch, not as approval of the entire assembly.

### Related guides

- [bottling machine home position micro switch location](/guides/bottling-machine-home-position-micro-switch-location/)
- [incinerator end of stroke micro switch maintenance](/guides/incinerator-end-of-stroke-micro-switch-maintenance/)
- [rotary indexing table guard interlock micro switch location](/guides/rotary-indexing-table-guard-interlock-micro-switch-location/)
- [security barrier open position micro switch wiring](/guides/security-barrier-open-position-micro-switch-wiring/)

## What the switch check cannot establish

A mismatch between observed and expected behavior does not point to one cause by itself. The physical chain may not be engaging the actuator as intended; the contact state may differ from the documented expectation; a terminal may have been misidentified; wiring may not match the diagram; or the issue may be elsewhere in the control system. Separate those possibilities by comparing the observed condition with the equipment documentation and the result of any permitted isolated check. Do not collapse them into a single diagnosis.

The switch check cannot establish what the table’s controller or other circuit elements do with the input. To interpret downstream behavior, trace the actual equipment diagram and its stated circuit function. If the diagram, terminal information, expected contact state, or safe test procedure is unavailable, that part of the diagnosis remains unresolved. Do not substitute a generic wiring pattern for missing equipment-specific information.

Electrical work must stay within the applicable deenergization and qualification requirements and a documented safe procedure. Do not proceed with energized measurements or other work beyond that procedure based only on an isolated continuity result. Leave work outside the documented procedure to qualified personnel.

The practical conclusion is limited but useful: identify the switch terminals from the exact documentation, relate their contact states to the stated reference condition, and trace the conductors through the actual table circuit. An isolated check can verify a documented contact state under its test condition; it cannot, by itself, establish correct installed wiring or explain the table’s control response. That is the boundary for **rotary indexing table end of stroke micro switch wiring**.

## Sources and references

- Defense Logistics Agency ASSIST: [MIL-PRF-8805K: Switches and Switch Assemblies, Sensitive, Snap Action, General Specification For](https://quicksearch.dla.mil/qsDocDetails.aspx?ident_number=7196){: rel="nofollow noopener noreferrer" }
- Occupational Safety and Health Administration: [29 CFR 1910.333: Selection and Use of Work Practices](https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.333){: rel="nofollow noopener noreferrer" }
