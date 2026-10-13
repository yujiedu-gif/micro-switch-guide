---
title: "micro switch changeover contacts selection"
description: "micro switch changeover contacts selection: Understand the operating idea, essential terminology, practical checks, limitations, and evidence needed for."
date: 2026-04-23 10:19:48 +0800
last_modified_at: 2026-10-13 11:46:37 +0800
category: Selection Guides
tags:
  - micro switch changeover contacts selection
  - micro switches
  - Selection Guides
author: editorial_team
---

A micro switch changeover contacts selection is a circuit-matching task: choose a documented switch whose contact arrangement and operating behavior meet the circuit’s defined requirements. A changeover contact can provide different contact states as its actuator moves, but the labels alone do not establish how an installed system will behave. Confirm the specific switch documentation, actual circuit conditions, and mechanical movement before deciding that a design is suitable.

## What changeover contacts mean on a micro switch

Not every micro switch has changeover contacts. For a documented generic changeover arrangement, the terminals may be labeled COM (common), NC (normally closed), and NO (normally open). These names describe contact relationships at a specified reference condition. They do not, by themselves, promise that current will flow in a particular installed circuit or identify the correct terminals on every device. The exact device marking or schematic controls.

For selection, first establish what the switch documentation says about the contact arrangement and reference condition. Then identify the relevant contact state in each required actuator condition. Keep those statements separate: “the contacts are in a specified state” describes the switch; “the equipment is powered, stopped, or signaling” describes the wider circuit and depends on its wiring and control logic.

A miniature snap-action switch can change an electrical contact state in response to mechanical actuator movement and is commonly used for position or limit detection. That general function does not establish that a particular switch has the required contact arrangement or is suitable for a particular circuit. Confirm the exact design rather than inferring features from the term “micro switch.”

## micro switch changeover contacts selection: map circuit states first

Write down the circuit conditions that matter and the contact behavior required in each one. For example, identify the actuator condition in which the circuit requires one documented contact relationship, and the condition in which it requires the other. Do not translate those requirements into an assumed machine response unless the actual circuit documentation establishes that response.

Next, compare the required states with the exact switch’s connection diagram, terminal markings, and documented operating condition. Confirm which terminals are identified as COM, NO, and NC, if those labels apply. Do not infer terminal identity from physical position, appearance, or a generic layout. If the documentation does not establish the terminal arrangement or reference condition, the mapping remains unresolved.

The result should be a circuit-state map, not a guess about what the host equipment will do. It should connect each required actuator condition to the documented contact state and then to the circuit connection shown for the exact design. If the intended response depends on host control logic that has not been documented, leave that response open rather than treating the switch’s contact labels as proof.

## Check electrical limits for the actual load

Compare the circuit’s actual voltage and current with the permissible load documented for the exact switch. Check whether the circuit is AC or DC and identify the load type. Rating values are tied to stated load and test conditions, not universal switching capacities. A value for one condition cannot be carried over to a different current, voltage, AC/DC category, or load type without supporting documentation.

Use the connection diagram, terminal marking, circuit function, and permissible load documented for the exact switch and equipment. A generic contact arrangement does not establish a rating, and a rating that lacks a matching load or test condition is not enough to confirm suitability. Where the circuit conditions and switch documentation do not align clearly, treat the electrical match as unresolved rather than assuming compatibility.

This check concerns the particular circuit and switch documentation, not a general voltage or current capability of micro switches. If a required rating or condition is missing, selection cannot be completed from the available information. Keep any applicable deenergization and qualification requirements in view when examining circuit information; do not turn a selection checklist into an unsupported wiring procedure.

## Check whether the actuator can operate the contacts as intended

Electrical contact matching is only one part of selection. The external mechanism must move the actuator into the documented operating condition, and the design must permit the movement required by the application. Compare the mechanism’s available movement with the switch’s documented operating and travel information. Do not infer a force, travel value, durability figure, or compatibility from the switch category alone.

Where documented, distinguish the operating event from the release event. They are separate events; matching one does not establish that the other occurs at the needed point. Pretravel runs from free position to operating position, while overtravel runs from operating position to the extreme permitted actuator position. Those terms describe different portions of actuator movement. Use them only with the applicable design information, and do not exceed a stated permitted limit.

If the available evidence does not establish the actuator movement or operating and release behavior needed for the application, mechanical compatibility remains unknown. Do not substitute a general assumption about snap action for design-specific information. The contact arrangement may be appropriate on paper while the external mechanism still fails to operate it as required.

## Verify contact behavior without overclaiming what a test proves

A bounded contact check begins with the exact switch documentation: identify the terminals, define the actuator state to be checked, and establish the expected contact behavior at that state. If using continuity measurements, assess the isolated switch at defined actuator states against that documented behavior. Do not treat an ambiguous terminal identification or an unspecified reference condition as a meaningful comparison.

If a result differs from the expected behavior, it does not by itself identify the cause. The issue could concern the mechanical input, internal contacts, terminal identification, wiring, or another part of the equipment. Separate those possibilities rather than labeling the switch as the sole cause. A click can indicate movement of a snap mechanism, but does not prove continuity, contact condition, correct wiring, or suitability for the load.

An isolated continuity result applies to the isolated switch and the tested actuator state. It does not establish installed-circuit safety, confirm the wider circuit’s response, or prove overall suitability. Keep any electrical work within applicable deenergization and qualification requirements; this check is not a substitute for qualified assessment of the installed equipment.

### Related guides

- [spring plunger micro switch selection](/guides/spring-plunger-micro-switch-selection/)
- [micro switch freezing temperature selection](/guides/micro-switch-freezing-temperature-selection/)
- [micro switch contact gap selection](/guides/micro-switch-contact-gap-selection/)
- [micro switch dust ingress selection](/guides/micro-switch-dust-ingress-selection/)

## Selection decision: proceed only when the required facts are documented

Proceed with a selection decision only when the exact switch documentation establishes the relevant contact arrangement, terminal identities, and reference condition; the required circuit states map to that documented behavior; and the permissible load covers the actual voltage, current, AC or DC category, and load type under the stated conditions. The mechanical movement must also reach the documented operating condition without exceeding supported travel limits, with release behavior considered where it matters and is documented.

If any required fact is absent or mismatched, the answer is not to infer a universal terminal assignment, rating, or mechanical capability. Leave that part unresolved until the applicable documentation or qualified assessment establishes it. A contact-state check can support verification of the isolated switch under defined conditions, but it cannot certify the installed circuit or settle every selection constraint.

In short, micro switch changeover contacts selection depends on documented contact behavior, the actual circuit’s load conditions, and supported actuator movement. A decision is justified only within those established boundaries; the switch’s name or labels alone are not enough.

## Sources and references

- Defense Logistics Agency ASSIST: [MIL-PRF-8805K: Switches and Switch Assemblies, Sensitive, Snap Action, General Specification For](https://quicksearch.dla.mil/qsDocDetails.aspx?ident_number=7196){: rel="nofollow noopener noreferrer" }
- Occupational Safety and Health Administration: [29 CFR 1910.333: Selection and Use of Work Practices](https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.333){: rel="nofollow noopener noreferrer" }
- Wikipedia: [Miniature snap-action switch](https://en.wikipedia.org/wiki/Miniature_snap-action_switch){: rel="nofollow noopener noreferrer" }
