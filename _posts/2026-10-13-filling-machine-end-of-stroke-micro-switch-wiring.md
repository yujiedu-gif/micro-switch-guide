---
title: "Filling machine end of stroke micro switch wiring"
description: "filling machine end of stroke micro switch wiring: Understand the operating idea, essential terminology, practical checks, limitations, and evidence."
date: 2026-10-13 11:27:16 +0800
category: Applications
tags:
  - filling machine end of stroke micro switch wiring
  - micro switches
  - Applications
author: editorial_team
---

A filling machine end of stroke micro switch wiring question starts with identifying the exact switch connections, not guessing from where a terminal sits on the housing. In some filling-machine designs, a micro switch responds to mechanical actuator movement and changes an electrical contact state. The machine’s documentation must establish how that change is used. The same arrangement should not be assumed for every filling machine.

To identify a connection, compare the markings on the switch with the applicable connection diagram and machine circuit documentation. Then check that the documented connection is permissible for the circuit’s current type, load, and test condition. A terminal label or an end-of-stroke description alone does not establish the complete circuit function or what the machine will do.

## What end-of-stroke micro switch wiring does, and does not establish

A micro switch is a component that may form part of a filling machine’s end-of-stroke sensing arrangement. It is not a universal feature of filling machines. In a design that uses one, a moving mechanism may reach a cam, lever, or other linkage that moves the switch actuator. The switch can then change an electrical contact state, and the machine’s circuit may use that change. The machine’s actual documentation is needed to establish the relationship and downstream behavior.

This signal path has distinct stages: stroke position, mechanical transmission to the actuator, contact change within the switch, and the circuit response. A problem at one stage does not identify a problem at another. For example, a mechanism that does not move the actuator raises a different question from a terminal connection that does not match the documented diagram. Neither observation, by itself, establishes the machine’s control logic.

The end-of-stroke label describes an intended relationship in the equipment documentation, not a universal contact state. It does not show whether the circuit is intended to stop motion, signal an event, or initiate another action. Those outcomes depend on the particular machine and circuit. Do not infer them from the presence of a micro switch or from a terminal label.

## Filling machine end of stroke micro switch wiring: identify the documented terminals

Start with the exact switch markings and its applicable connection diagram. Compare those with the machine’s circuit documentation and the stated circuit function. Do not infer terminal identity from physical layout, terminal order, wire color, or the words “end of stroke.” A generic diagram cannot establish the connections for a particular switch and machine.

If the documented contact arrangement uses COM, NO, and NC, COM means common. NO and NC describe contact state at a specified reference condition. That reference condition must be stated in the applicable documentation; the labels are not an unqualified promise about current flow in every operating state. Do not assume that every micro switch has these terminals or that a particular arrangement applies to the switch in front of you.

Use the connection diagram, terminal marking, circuit function, and permissible load documented for the exact switch and equipment. Check the applicable specification sheet for the rating that applies to the current type, load, and test condition. An AC rating does not establish a DC rating, and a rating for one load or test condition does not establish another. If the documentation does not resolve a terminal or rating, treat it as unknown rather than filling the gap by inference.

A mismatch between the switch markings and the equipment diagram is a reason to resolve identification before changing connections. The machine’s end-of-stroke function does not make an otherwise undocumented terminal choice correct. If the applicable information is unavailable or unclear, do not treat a presumed pinout as established.

## Trace the stroke mechanism before interpreting a contact change

Follow the documented mechanical path from the moving part through any cam, lever, or linkage to the micro switch actuator, where present. The relevant question is whether the stroke mechanism reaches and moves that actuator as the machine design specifies. The switch is mechanically actuated; its electrical connection is a separate part of the signal path.

If the mechanism does not reach or move the actuator, a contact reading may not answer whether the switch would change state when actuated. That observation points first to the mechanical path or its relationship to the actuator, not automatically to incorrect wiring or failed contacts. Conversely, movement of the actuator does not by itself establish that the contact is electrically sound or that the terminals are connected as documented.

Keep three questions separate: Does the mechanism move the actuator? Do the documented contacts behave as expected at a defined actuator state? Do the installed connections match the machine’s circuit documentation? Evidence about one question does not settle the others. In particular, neither actuator movement nor a contact change establishes whether the machine stops, signals, or begins another cycle. That behavior belongs to the documented control circuit, which is outside what terminal identification alone can determine.

## Verify switch contacts only under a defined and safe test condition

A continuity check is meaningful only for an isolated switch and a defined actuator state, using an established safe procedure and suitable documentation. The expected contact condition must come from the applicable switch documentation. If the switch cannot be isolated or the required state and procedure are not established, an assumed reading is not a reliable basis for identifying its contacts.

Keep component checking distinct from testing the installed machine circuit. An isolated-switch reading can provide information about the component’s contacts under that test condition, but it does not validate installed wiring, establish the machine’s control logic, or prove that the whole machine functions. The surrounding circuit may have other causes or dependencies that a component check does not examine.

A click can indicate movement of a snap mechanism, but it does not prove continuity, correct terminal identification, correct wiring, or suitability for the circuit’s load. Do not use the sound or feel of actuation as a substitute for the documented connection information or a defined component check.

Follow applicable deenergization and qualification requirements. Work beyond an established safe procedure or the available documentation should be left to qualified personnel. An isolated reading must not be treated as evidence that the installed circuit is safe.

### Related guides

- [bottling machine home position micro switch location](/guides/bottling-machine-home-position-micro-switch-location/)
- [incinerator end of stroke micro switch maintenance](/guides/incinerator-end-of-stroke-micro-switch-maintenance/)
- [rotary indexing table guard interlock micro switch location](/guides/rotary-indexing-table-guard-interlock-micro-switch-location/)
- [security barrier open position micro switch wiring](/guides/security-barrier-open-position-micro-switch-wiring/)

## Decide what the observed result can support

If markings, the switch diagram, and the machine circuit documentation do not agree, resolve terminal identification before rewiring. Do not choose a connection based only on physical position, an assumed standard arrangement, or the machine’s end-of-stroke label. The exact switch and equipment documentation must support the terminal choice and the applicable rating.

If the actuator is not moved by the stroke mechanism, investigate that mechanical relationship separately from contact behavior. If the actuator moves but a defined isolated check does not match the documented contact state, that result narrows the question to the switch under the test condition; it does not identify every possible cause in the installed circuit. If a component check is consistent with its documentation, it still does not prove correct installed wiring or overall machine operation.

The practical limit of filling machine end of stroke micro switch wiring identification is therefore clear: documentation identifies the permitted connections, the mechanical trace establishes whether the actuator is reached, and a defined isolated check can assess contacts within its test boundary. None of those steps alone establishes the machine’s complete control behavior or safety. Use the equipment’s circuit documentation and qualified service support for installed-system diagnosis.

## Sources and references

- Defense Logistics Agency ASSIST: [MIL-PRF-8805K: Switches and Switch Assemblies, Sensitive, Snap Action, General Specification For](https://quicksearch.dla.mil/qsDocDetails.aspx?ident_number=7196){: rel="nofollow noopener noreferrer" }
- Occupational Safety and Health Administration: [29 CFR 1910.333: Selection and Use of Work Practices](https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.333){: rel="nofollow noopener noreferrer" }
- Wikipedia: [Miniature snap-action switch](https://en.wikipedia.org/wiki/Miniature_snap-action_switch){: rel="nofollow noopener noreferrer" }
