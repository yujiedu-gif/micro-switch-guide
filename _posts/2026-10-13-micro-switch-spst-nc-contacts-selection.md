---
title: "micro switch SPST NC contacts selection: a practical checklist"
description: "micro switch SPST NC contacts selection: Understand the operating idea, essential terminology, practical checks, limitations, and evidence needed for."
date: 2026-10-13 09:00:00 +0800
category: Selection Guides
tags:
  - micro switch SPST NC contacts selection
  - micro switches
  - Selection Guides
author: editorial_team
---

Selecting a micro switch SPST NC contacts selection for a defined application means confirming more than the contact label. First establish that the required contact arrangement is single-pole, single-throw with a normally closed state at the documented reference condition. Then check terminal identification, actuator fit, and electrical evidence as separate requirements. A match in one area does not establish suitability in the others.

A miniature snap-action switch can change an electrical contact state in response to mechanical actuator movement and is commonly used for position or limit detection. That general role does not establish that a particular switch fits a mechanism or is suitable for a circuit. The checks below keep the contact-state decision distinct from mechanical and electrical decisions.

## What micro switch SPST NC contacts selection means

For this selection, SPST identifies one pole and one throw: one contact circuit with a single switching path. NC describes the documented contact state at a specified reference condition. It does not promise that the contacts remain closed through every actuator position or installed operating state. The required reference condition must therefore be identified in the documentation for the switch being considered.

The contact arrangement is a component characteristic. It is not a description of the host equipment's control logic or of what the equipment will do when the contacts change state. The effect depends on the actual circuit and equipment design. Do not infer an alarm, stop, start, or other response solely from an NC designation.

Treat the contact requirement as the first filter, not the complete selection decision. If the application needs a particular contact state under a defined condition, confirm that the switch documentation describes SPST NC contacts at that condition. If the reference condition is missing or unclear, the contact-state match remains unresolved. Do not substitute an assumed resting position or an assumed installed state for documented evidence.

The designation also does not establish the actuator style, how the switch will be moved, or whether its electrical ratings cover the intended circuit. Those are independent checks. A switch that meets the contact-arrangement requirement may still lack evidence for the mechanism or electrical load in the application.

## Confirm the NC reference state and terminal identification

Locate the contact diagram and the stated reference condition in documentation for the exact switch. Read NC in relation to that condition, rather than treating it as an unqualified promise about installed behavior. Check that the documented arrangement matches the required one-pole, one-throw path and the required NC state.

Identify terminals from the switch-specific diagram and terminal markings. Do not infer terminal identity from physical location, appearance, or a layout remembered from another switch. Use the connection diagram, terminal marking, circuit function, and permissible load documented for the exact switch and equipment. A generic physical-layout inference cannot establish which terminal serves which role.

Keep component identification separate from application wiring. The contact diagram can help establish the switch's documented arrangement, but it does not by itself specify how the host equipment is wired or what its control logic does. The equipment's circuit documentation is needed to understand that relationship. This selection discussion does not provide wiring instructions for a particular appliance or control circuit.

If documentation is incomplete, record the uncertainty rather than assigning a terminal name or reference state by assumption. The contact arrangement is not fully verified until both the state reference and terminal identities are supported by the relevant documentation. A label alone cannot fill gaps in either.

## Check actuator fit and mechanical operating range

After confirming the contact requirement, assess how the external mechanism will move the switch actuator. Compare the mechanism's contact point and direction of movement with the actuator arrangement documented for the switch. The SPST NC designation says nothing about whether those parts meet correctly or whether the mechanism can operate the switch as required.

Use documented operating information to compare the available movement with the switch's operating position and permitted actuator range. In the terminology of the cited specification, pretravel runs from free position to operating position, while overtravel runs from operating position to the extreme permitted actuator position. These definitions distinguish portions of motion; they do not supply a travel value for an unspecified switch. Do not invent a force or travel requirement when the relevant parameters are not documented.

The mechanism must be assessed against the actual switch information and the movement available in the application. If the operating point, permitted range, or relevant actuator details are unknown, mechanical fit is unresolved. Do not conclude that a switch fits merely because its contact designation is correct, or infer suitability from a general description of position detection.

## Match electrical evidence to the actual circuit

Check the documented rating against the intended circuit's voltage, current, and load conditions. Rating values are specification-sheet requirements tied to stated load and test conditions, not universal switching capacities. A value without its conditions is not enough to establish suitability for a different circuit or load.

Keep the documented conditions intact. Do not transfer a rating between AC and DC, or from one named load type to another. Compare the actual circuit conditions with the applicable specification-sheet evidence for the switch. If the circuit's conditions, load type, or needed rating evidence are unknown, mark electrical suitability unresolved rather than guessing.

This check is distinct from confirming SPST NC contacts. A documented contact arrangement establishes neither the permissible electrical load nor the switch's fit for the intended circuit. Likewise, an apparently suitable rating does not establish that the required contact state, terminal identities, or mechanical interface are correct. Each requirement needs its own supporting evidence.

Use the connection diagram, terminal marking, circuit function, and permissible load documented for the exact switch and equipment. Where those sources do not establish the needed relationship or rating conditions, do not extend a rating or assume compatibility. This is a boundary for selection evidence, not a procedure for testing an installed circuit's safety.

### Related guides

- [spring plunger micro switch selection](/guides/spring-plunger-micro-switch-selection/)
- [micro switch freezing temperature selection](/guides/micro-switch-freezing-temperature-selection/)
- [micro switch contact gap selection](/guides/micro-switch-contact-gap-selection/)
- [micro switch dust ingress selection](/guides/micro-switch-dust-ingress-selection/)

## Decide whether the micro switch is adequately specified

A bounded selection decision requires evidence for the contact arrangement and NC reference condition, terminal identities, actuator interface and operating range, and electrical conditions relevant to the application. Keep the evidence for each item distinct. Confirming one item does not compensate for missing information about another.

If the contact designation is documented but the actuator movement is not, the mechanical match remains unresolved. If the mechanism appears to fit but the documented rating conditions do not cover the actual circuit and load, electrical suitability remains unresolved. If terminal identities or the NC reference condition are unclear, do not treat the contact requirement as verified.

An NC contact designation also does not determine the resulting equipment behavior. That depends on the actual circuit and control logic, which must be understood from the relevant equipment documentation. Do not infer a system response from the switch's contact arrangement alone.

Pause the selection when a necessary fact is missing. Missing documentation is a reason to leave that part of the decision unresolved, not proof that the switch is unsuitable. Conversely, a contact-arrangement match alone is not proof that the switch is adequately specified. The micro switch SPST NC contacts selection is adequately supported only when the contact state, terminal information, mechanical interface, and applicable electrical evidence have each been checked within their documented conditions.

## Sources and references

- Defense Logistics Agency ASSIST: [MIL-PRF-8805K: Switches and Switch Assemblies, Sensitive, Snap Action, General Specification For](https://quicksearch.dla.mil/qsDocDetails.aspx?ident_number=7196){: rel="nofollow noopener noreferrer" }
- Occupational Safety and Health Administration: [29 CFR 1910.333: Selection and Use of Work Practices](https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.333){: rel="nofollow noopener noreferrer" }
- Wikipedia: [Miniature snap-action switch](https://en.wikipedia.org/wiki/Miniature_snap-action_switch){: rel="nofollow noopener noreferrer" }
