---
title: "Suspension height limit micro switch NO and NC terminals: what do they mean?"
description: "suspension height limit micro switch NO and NC terminals: Understand the operating idea, essential terminology, practical checks, limitations, and."
date: 2026-08-21 16:41:03 +0800
sitemap_omit_lastmod: true
category: Applications
tags:
  - suspension height limit micro switch NO and NC terminals
  - micro switches
  - Applications
author: editorial_team
---

A suspension height limit micro switch NO and NC terminals describe contact states, not the suspension system’s complete behavior. A micro switch is an electromechanical component; it is distinct from the suspension mechanism and the circuit that interprets its contacts. The labels are meaningful only in relation to the switch’s documented reference condition and contact arrangement. They do not, by themselves, show what happens when a suspension reaches a particular height.

## What suspension height limit micro switch NO and NC terminals identify

NO and NC identify contact states at the reference condition specified for the particular switch. NO means normally open at that documented condition; NC means normally closed at that condition. These names describe the contacts, not a guaranteed current path or a universal meaning of “normal” for the suspension system. The reference condition must come from the applicable switch documentation, rather than an assumed vehicle position or a general idea of how suspension should rest.

Use these terms only when the switch’s actual contact arrangement and terminal identification are documented. Do not assume a switch has both NO and NC terminals, or infer terminal identity from physical position or appearance. A wiring diagram and terminal markings for the exact switch and equipment are more reliable than a generic layout. The circuit function and permissible load also need to be established from the applicable documentation; NO or NC alone does not specify either.

The distinction is between a component-level contact state and a system-level state. A contact may be open or closed under the switch’s specified reference condition, but that fact does not establish whether a height limit has been reached. Nor does the label alone establish whether the equipment treats a contact change as a warning, a control input, or some other signal. Those meanings depend on the installed circuit and its documentation.

## How a height-limit mechanism may actuate a micro switch

In a design that uses a micro switch, suspension movement may be related to the switch through a mechanical actuator. A lever, cam, linkage, or another mechanism may move the actuator as position changes. If the design does this, the actuator’s movement can operate the switch and change its contact state. This describes a possible arrangement, not a universal suspension design: the evidence does not establish a particular linkage, mounting position, direction of movement, or normal state for suspension-height systems generally.

The operating point is the point at which the switch changes contact state. In an application, a mechanism’s position and movement matter only insofar as the particular design couples them to the switch actuator. A terminal label cannot reveal that mechanical relationship. Without documentation for the specific design, it is unresolved whether suspension movement operates a switch, which movement does so, or how a stated height corresponds to switch operation.

Even when a mechanical relationship is documented, the contact change is only one step in the signal path. The switch provides a contact condition; the host circuit receives or uses that condition according to its design. The host circuit, not the NO or NC label by itself, determines what the change means to the equipment. A switch might be part of a limit signal in one documented design, but that does not establish a shared arrangement across suspension systems.

Keep the component, actuator mechanism, and host circuit distinct when reading a system description. A diagram may show a mechanical relationship between suspension position and an actuator, then show switch terminals connected to a circuit. Each link needs its own documentation. If a link is not established, do not fill it in by assuming a familiar suspension arrangement or a conventional control response.

## Why NO and NC labels do not identify the suspension system’s response

NO and NC are not shorthand for “suspension low” and “suspension high.” They identify contact states at a specified switch reference condition. The reference condition may not be the same as the system’s resting, unloaded, or safe condition unless the applicable documentation says so. The labels therefore cannot establish whether the switch is operated at a particular suspension height or whether a particular height is the limit.

Installed wiring adds another necessary layer. The connection diagram and terminal markings identify how the specific switch is intended to connect; the equipment wiring documentation shows how it is incorporated into the host circuit. The controller’s logic and documented reference position are also relevant to interpreting a system state. Without those details, the same contact label does not disclose whether the circuit treats an open or closed condition as a limit, warning, or action.

A useful interpretation keeps three questions separate: what contact state the switch has at its documented reference condition; whether the suspension mechanism moves its actuator in the particular design; and what the host circuit does with a contact change. Evidence for one question does not answer the others. For example, knowing that a terminal is marked NO does not prove that a height threshold has been reached, that an alert is sent, or that a control action follows.

Avoid diagnosing the complete suspension system from terminal names alone. The labels do not establish installed wiring, controller behavior, or whether the system is functioning correctly. If documentation leaves any of these relationships unresolved, the response of the system is unresolved too. Interpret only the arrangement documented for the specific switch and equipment.

### Related guides

- [bottling machine home position micro switch location](/guides/bottling-machine-home-position-micro-switch-location/)
- [incinerator end of stroke micro switch maintenance](/guides/incinerator-end-of-stroke-micro-switch-maintenance/)
- [rotary indexing table guard interlock micro switch location](/guides/rotary-indexing-table-guard-interlock-micro-switch-location/)
- [security barrier open position micro switch wiring](/guides/security-barrier-open-position-micro-switch-wiring/)

## How to verify the terminals for the specific design

Start with the specific switch documentation and the equipment wiring diagram. Use them to identify the terminals, the contact arrangement, and the reference condition associated with NO and NC. Follow the documented terminal identification and circuit function rather than inferring a connection from a generic physical layout. Confirm that the documented permissible load applies to the actual circuit before treating a diagram as evidence of suitability.

If the applicable documentation describes an isolated continuity check and that check is appropriate, keep its limits clear: identify the actuator state being checked and the isolation condition, then compare the observed contact state with the documented arrangement. A continuity observation concerns the isolated switch in a defined state. It does not establish what the installed circuit is doing, whether the switch is wired as shown, or whether the suspension system reaches or responds to a height limit as intended.

Do not use an isolated contact reading as proof that the complete system is safe or functional. A mismatch may indicate a question about terminal identification, the switch, its actuation, or the test conditions, but the reading alone does not determine which explanation is correct. Work beyond documented safe procedures belongs to qualified personnel; follow applicable deenergization and qualification requirements.

The practical answer is bounded: NO and NC describe contacts at the specific switch’s documented reference condition. A suspension-height limit interpretation requires separate evidence for the mechanical actuation and the host circuit’s logic. The suspension height limit micro switch NO and NC terminals alone cannot establish the system’s state or response.

## Sources and references

- Defense Logistics Agency ASSIST: [MIL-PRF-8805K: Switches and Switch Assemblies, Sensitive, Snap Action, General Specification For](https://quicksearch.dla.mil/qsDocDetails.aspx?ident_number=7196){: rel="nofollow noopener noreferrer" }
- Occupational Safety and Health Administration: [29 CFR 1910.333: Selection and Use of Work Practices](https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.333){: rel="nofollow noopener noreferrer" }
