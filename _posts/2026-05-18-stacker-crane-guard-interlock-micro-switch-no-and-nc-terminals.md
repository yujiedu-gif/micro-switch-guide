---
title: "stacker crane guard interlock micro switch NO and NC terminals: What Do They Mean?"
description: "stacker crane guard interlock micro switch NO and NC terminals: Understand the operating idea, essential terminology, practical checks, limitations, and."
date: 2026-05-18 08:18:39 +0800
last_modified_at: 2026-10-13 11:46:37 +0800
category: Applications
tags:
  - stacker crane guard interlock micro switch NO and NC terminals
  - micro switches
  - Applications
author: editorial_team
---

A **stacker crane guard interlock micro switch NO and NC terminals** label describes contact states at a specified reference condition. The labels do not, by themselves, identify which guard position is normal, show how the crane responds, or establish that the interlock is safe. To interpret them, first find the reference condition and terminal mapping in documentation for the exact switch and equipment. Then keep the switch’s contact behavior separate from the surrounding circuit’s logic.

A micro switch can change an electrical contact state in response to mechanical actuator movement and is commonly used for position or limit detection. That general function does not reveal how a particular guard is wired or what the control system does after a contact changes. The boundaries below explain what the labels establish, what a bounded contact check can show, and where equipment documentation is necessary.

## stacker crane guard interlock micro switch NO and NC terminals: Read the labels in context

NO and NC are contact-state labels tied to a specified reference condition. NO means the identified contact is open at that condition; NC means the identified contact is closed at that condition. These definitions describe contact state, not an unconditional promise about current flow in the installed equipment. The reference condition matters: without it, the labels alone do not tell you which actuator position is being described.

The applicable switch documentation must establish both the reference condition and the terminal mapping. Do not assume that the reference condition means the guard is open, the guard is closed, or the mechanism is in a particular position. Those relationships depend on the documented switch arrangement and how the external mechanism actuates it.

The equipment documentation also matters because a terminal label does not describe the complete guard circuit. A contact identified as NO or NC tells you how that contact is classified at the stated reference condition; it does not say what input the crane control system receives, how that input is interpreted, or what operational response follows. Establish the component-level facts first, without substituting an assumed guard state or machine response for missing documentation.

For terminal identification, use the connection diagram and terminal markings documented for the exact switch and equipment. A generic physical-layout inference is not a reliable basis for identifying contacts. If the available documentation does not map the terminals or specify the reference condition, the label alone is insufficient to resolve the contact arrangement.

## How actuator movement changes the documented contact state

A micro switch’s actuator is moved by an external mechanism. As that mechanism moves the actuator, the switch’s contacts may change state according to the documented arrangement. This describes a mechanical input and a component-level contact response; it does not establish what a stacker crane guard or its control system does with that response.

The relationship must be read in the correct direction: documented mechanism position, actuator state, and contact state. A guard’s visible position is not itself a terminal-state definition. Nor does a contact label tell you whether the external mechanism is pressing, releasing, or otherwise moving the actuator in a particular installation. To map those states, consult the applicable switch and equipment documentation rather than inferring the linkage from the labels.

Operation and release are distinct events in switch behavior. If the applicable documentation describes them, keep those events separate when relating actuator movement to a contact change. Do not treat one observed position or transition as proof of every other state or transition. The available general description does not establish specific operating or release positions for a stacker crane installation.

Likewise, the contact transition is not the same as the control-system response. A changed contact could be used in different circuit arrangements, and the circuit determines how that change is handled. Without the actual circuit and its documentation, do not infer a normal guard state, an alarm, a shutdown, or any other equipment response from NO and NC alone.

## Verify terminal identity and contact state without overreading a test

Begin with the applicable connection diagram, terminal markings, circuit function, and permissible load documented for the exact switch and equipment. Do not identify terminals by wire color or physical position alone. If terminal identity is unresolved, a continuity result cannot be confidently assigned to NO or NC. Keep that uncertainty explicit instead of treating a plausible meter reading as a confirmed mapping.

An isolated continuity check is limited to the switch itself. Before interpreting a result, define the actuator state being checked and the expected contact behavior from the applicable documentation. The isolation condition must also be established for the test. Under those defined conditions, a reading can help show whether the identified contact is open or closed in that tested state. It does not, by itself, verify the installed wiring, the circuit function, or the full guard system.

A click during actuator movement may indicate movement of a snap mechanism, but it does not prove continuity, contact condition, correct wiring, or suitability for the circuit. A click and a continuity reading answer different, limited questions. Neither should be expanded into a conclusion about the crane’s installed interlock or safety performance.

If interpreting a rating as part of the circuit check, use only the rating explicitly stated for the applicable current type, load, and test condition. A rating for one condition does not establish another; check the applicable specification sheet. The wiring diagram, terminal identification, circuit function, and permissible load must all apply to the exact switch and equipment. A component-level check cannot replace review of those documented circuit requirements.

### Related guides

- [bottling machine home position micro switch location](/guides/bottling-machine-home-position-micro-switch-location/)
- [incinerator end of stroke micro switch maintenance](/guides/incinerator-end-of-stroke-micro-switch-maintenance/)
- [rotary indexing table guard interlock micro switch location](/guides/rotary-indexing-table-guard-interlock-micro-switch-location/)
- [security barrier open position micro switch wiring](/guides/security-barrier-open-position-micro-switch-wiring/)

## What the labels cannot tell you about the guard circuit

The control circuit determines what a contact change means to the host equipment. NO and NC do not reveal whether the guard is considered open or closed by the crane, whether operation is permitted, or whether a particular response occurs. Those are system-level questions requiring the applicable equipment documentation. Do not infer normal guard state, shutdown behavior, or safety performance from terminal labels alone.

Keep three questions separate: which terminals the documentation identifies, what contact state is expected at a specified actuator state, and how the installed circuit responds to that contact. Evidence for one does not automatically answer the others. For example, a documented isolated reading may describe a contact in one defined state without showing that the terminals are wired as intended or that the control system responds correctly.

If the terminal mapping, reference condition, installed wiring, or circuit behavior is uncertain, the labels do not resolve that uncertainty. Use the equipment documentation and qualified personnel for safety-related diagnosis. This article does not establish whether a particular guard circuit is safe or compliant, identify a compatible replacement, or provide instructions to bypass or repair an interlock.

In short, **stacker crane guard interlock micro switch NO and NC terminals** identify contact states only in the switch’s specified reference condition. Establish that condition and the terminal mapping from applicable documentation, relate actuator movement to contact behavior only as documented, and do not treat an isolated check as proof of installed-system safety or function.

## Sources and references

- Defense Logistics Agency ASSIST: [MIL-PRF-8805K: Switches and Switch Assemblies, Sensitive, Snap Action, General Specification For](https://quicksearch.dla.mil/qsDocDetails.aspx?ident_number=7196){: rel="nofollow noopener noreferrer" }
- Occupational Safety and Health Administration: [29 CFR 1910.333: Selection and Use of Work Practices](https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.333){: rel="nofollow noopener noreferrer" }
- Wikipedia: [Miniature snap-action switch](https://en.wikipedia.org/wiki/Miniature_snap-action_switch){: rel="nofollow noopener noreferrer" }
