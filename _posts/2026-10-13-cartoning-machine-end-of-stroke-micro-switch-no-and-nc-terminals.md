---
title: "cartoning machine end of stroke micro switch NO and NC terminals"
description: "cartoning machine end of stroke micro switch NO and NC terminals: Understand the operating idea, essential terminology, practical checks, limitations, and."
date: 2026-10-13 09:00:00 +0800
category: Applications
tags:
  - cartoning machine end of stroke micro switch NO and NC terminals
  - micro switches
  - Applications
author: editorial_team
---

A cartoning machine end of stroke micro switch NO and NC terminals describe contact states at a defined actuator reference condition. They do not, by themselves, say whether the machine is stopped, running, or at its stroke endpoint. To interpret them, first establish which contact arrangement and reference condition are documented for the actual switch, then determine whether the endpoint mechanism has moved its actuator from that condition.

A miniature snap-action switch can change an electrical contact state in response to mechanical actuator movement and is commonly used for position or limit detection. In this context, the switch is a component that may provide an endpoint input; it is not the cartoning machine’s control system. The contact transition and the machine’s response are separate matters.

## What the cartoning machine end of stroke micro switch NO and NC terminals describe

NO means normally open and NC means normally closed, but “normally” requires a stated reference condition. For a documented contact arrangement, NO and NC identify the contacts’ relationship at the switch’s specified unactuated or other reference state. They do not name a machine state. In particular, an NO terminal is not automatically a “machine running” terminal, and an NC terminal is not automatically a “machine stopped” terminal.

The reference condition must come from documentation for the actual switch or equipment. If that documentation identifies an unactuated state, interpret the labels relative to that state. If it specifies another reference condition, use that instead. Without a documented contact arrangement and reference condition, the terminal names alone are not enough to establish which contacts are open or closed in a particular actuator position.

The endpoint is a position in the machine mechanism, whereas NO and NC describe the switch contacts relative to a reference. Those descriptions become related only after the switch’s installation and mechanical relationship to the endpoint are established. A switch mounted so that the endpoint mechanism moves its actuator may change contact state there, but the labels alone do not prove the switch is mounted or adjusted that way.

## How endpoint movement changes the micro switch contact state

The relevant sequence is mechanical: a machine mechanism moves as it approaches a stroke endpoint; if that mechanism engages the switch actuator, the actuator moves; and the switch may then change its contact state. This explains how an endpoint can produce an electrical input without making NO or NC synonyms for “at endpoint.” The endpoint’s contact state depends on how the actuator is positioned relative to its documented reference condition.

For example, the switch may be at its reference condition before the endpoint mechanism engages it, or the installation may leave it already actuated. Which state applies cannot be determined from the fact that a switch is used for end-of-stroke detection. It must be established from the switch and equipment documentation and the actual mechanical arrangement. Do not assume that travel toward an endpoint always actuates the switch in the same way across installations.

It is also important to distinguish the switch’s operating event from the control system’s response. The switch can change a contact state when its actuator moves, but that fact alone does not establish what the cartoning machine does next. A contact transition is an input condition; the connected circuit determines how that condition is used.

## What NO and NC do not tell you about cartoning machine behavior

NO and NC do not, by themselves, tell you whether a contact transition stops motion, raises an alarm, permits a restart, or serves another control purpose. Those outcomes depend on the actual wiring and control logic. The switch’s terminal names describe a contact arrangement at a reference condition, not the function assigned to that contact in the host equipment.

To describe the machine’s response, information about the actual connection diagram, terminal identification, circuit function, and documented permissible load would be needed. Even then, a statement about operation must remain within what that documentation establishes. Do not infer stop behavior or safety function merely because a micro switch is placed near a stroke endpoint.

This distinction also prevents a common interpretation error: describing a machine state from a terminal label alone. The endpoint may correspond to an operated or released actuator state depending on installation. The control circuit may interpret the resulting contact state in a way that cannot be inferred from the switch’s NO or NC marking. Keep the mechanical position, switch contact state, and control-system action as separate facts unless the equipment documentation connects them.

### Related guides

- [bottling machine home position micro switch location](/guides/bottling-machine-home-position-micro-switch-location/)
- [incinerator end of stroke micro switch maintenance](/guides/incinerator-end-of-stroke-micro-switch-maintenance/)
- [rotary indexing table guard interlock micro switch location](/guides/rotary-indexing-table-guard-interlock-micro-switch-location/)
- [security barrier open position micro switch wiring](/guides/security-barrier-open-position-micro-switch-wiring/)

## How to verify terminal state without overinterpreting the result

Begin with the connection diagram and terminal markings for the exact switch and equipment, and identify the documented contact arrangement and actuator reference condition. Do not infer terminal function from physical layout alone. If those details are unavailable or do not establish the arrangement, treat the state as unknown rather than assigning NO or NC from appearance.

A continuity check, if appropriate to the documented procedure, concerns the isolated switch and a defined actuator state. The switch must be considered separately from the installed circuit; the reference condition and the actuator position during the check must be clear. An isolated reading can describe the contacts under that test condition, but it does not establish that the equipment is wired correctly or reveal how its control logic responds.

A click may indicate movement of a snap mechanism, but it does not prove continuity, contact condition, correct terminal identification, or suitability for the connected load. Likewise, an isolated contact result does not prove the whole cartoning machine is operating correctly or safely. Follow applicable deenergization and qualification requirements; do not use a component-level observation as a substitute for evaluating the machine and its documented circuit.

The practical boundary is straightforward: use NO and NC to describe the documented contact states relative to the documented reference condition. Establish how endpoint movement positions the actuator, then consult the actual circuit documentation before assigning a machine-level meaning. The cartoning machine end of stroke micro switch NO and NC terminals alone cannot establish what the machine will do at the endpoint.

## Sources and references

- Defense Logistics Agency ASSIST: [MIL-PRF-8805K: Switches and Switch Assemblies, Sensitive, Snap Action, General Specification For](https://quicksearch.dla.mil/qsDocDetails.aspx?ident_number=7196){: rel="nofollow noopener noreferrer" }
- Occupational Safety and Health Administration: [29 CFR 1910.333: Selection and Use of Work Practices](https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.333){: rel="nofollow noopener noreferrer" }
- Wikipedia: [Miniature snap-action switch](https://en.wikipedia.org/wiki/Miniature_snap-action_switch){: rel="nofollow noopener noreferrer" }
