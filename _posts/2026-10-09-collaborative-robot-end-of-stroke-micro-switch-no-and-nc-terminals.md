---
title: "collaborative robot end of stroke micro switch NO and NC terminals"
description: "collaborative robot end of stroke micro switch NO and NC terminals: Understand the operating idea, essential terminology, practical checks, limitations,."
date: 2026-10-09 18:51:44 +0800
last_modified_at: 2026-10-13 11:46:37 +0800
category: Applications
tags:
  - collaborative robot end of stroke micro switch NO and NC terminals
  - micro switches
  - Applications
author: editorial_team
---

The **collaborative robot end of stroke micro switch NO and NC terminals** describe contact states only in relation to a documented reference condition. They do not, by themselves, tell you what the robot will do at stroke end. That depends first on whether the mechanism actuates a micro switch, then on the switch’s documented contact arrangement, and finally on the circuit and controller logic.

A miniature snap-action switch can change an electrical contact state in response to mechanical actuator movement and is commonly used for position or limit detection. But the presence of a switch near a robot’s travel limit does not establish its terminal arrangement, the point at which it operates, or the system’s response. Use the exact switch and equipment documentation to interpret those details; do not infer them from terminal names or physical layout alone.

## Direct answer: collaborative robot end of stroke micro switch NO and NC terminals

NO and NC are labels for contact states at a specified reference condition. For a documented COM/NO/NC arrangement, the applicable switch documentation identifies that condition and the contact relationships there. If the robot mechanism later actuates the switch, the contacts may change state according to that particular switch’s arrangement and operating event. The labels alone do not establish the state at stroke end.

The end-of-stroke event is therefore not a universal state instruction. A mechanism must actually move the switch actuator, and the switch documentation must establish how the contacts respond to that movement. A robot’s travel reaching its limit does not automatically mean that a particular contact is open or closed. The mechanical relationship and switch arrangement must be known.

Even when a contact change is documented, it is a component-level event. It does not specify whether the controller stops motion, records a status, triggers an alarm, or takes another action. Those outcomes depend on the actual circuit and configured control logic. NO and NC identify contact states in a stated reference context, not unconditional promises about current flow or robot behavior.

## Read NO and NC from the switch’s reference condition

Start by identifying the reference condition specified for the exact switch. Do not assume that “normal” means the robot is at rest, at home, away from the stroke limit, or in any other particular position. The relevant condition is the one defined by the switch documentation. Without it, the terminal labels cannot be mapped reliably to a robot position.

Where the documentation confirms COM, NO, and NC contacts, COM is the common terminal. NO and NC describe their contact relationships at the documented reference condition. In that condition, the documented COM-to-NO pair is open and the documented COM-to-NC pair is closed. This description concerns the contact arrangement in that reference state. It does not claim that current is flowing through either pair in an installed circuit.

That distinction matters because a terminal label is not a complete circuit description. Whether a contact is connected to a source, load, controller input, or another circuit point is a separate matter. Nor does the label alone establish which physical terminal occupies a particular position on a switch body. Use the connection diagram and terminal markings for the exact switch rather than inferring terminal identity from a generic layout.

If the documentation does not specify the contact arrangement or reference condition, leave the terminal-to-state mapping unresolved. Do not fill the gap by assuming a familiar switch configuration. The same restraint applies to the robot’s mechanical reference position: it must be established from the applicable equipment documentation, not inferred from the words “end of stroke.”

## Follow the end-of-stroke actuator event

The useful causal sequence begins with mechanical movement, not with the robot’s position label. If the robot mechanism is documented to move the micro switch actuator as it reaches a stroke limit, that movement can cause the switch’s contact state to change according to the particular arrangement and operating event. If the mechanism does not actuate the switch, reaching the limit alone does not establish a contact change.

Keep the stated reference condition separate from the actuation event. The reference condition tells you what NO and NC mean for the documented contact arrangement in that state. The actuation event describes a later mechanical input and its documented effect on the contacts. Neither fact should be substituted for the other. A switch’s labels do not independently specify the robot position at which operation occurs.

The exact actuation relationship remains design-specific. The switch documentation and robot mechanism documentation must establish whether the actuator is moved, and the relevant switch information must establish the contact response. Without those facts, it is not possible to say which pair is open or closed at stroke end. Do not infer a universal mapping from the robot reaching a travel boundary.

A visible actuator movement or audible click is not enough to prove an electrical contact condition. It may indicate mechanical movement, but it does not establish continuity, correct terminal identification, or the state seen by the robot controller. Likewise, a documented component contact change does not prove that the installed circuit has the expected behavior. Keep each conclusion within the evidence for that particular stage of the sequence.

## Separate contact change from robot control response

A micro switch can provide a contact change, but what that change means to the robot is determined by the circuit and configured control logic. The same component-level description does not establish a particular stop, alarm, reset, or other response. Those outcomes cannot be read from NO or NC alone.

To determine system behavior, consult the applicable switch connection diagram, terminal markings, robot circuit information, and control documentation. These sources answer different questions: the switch information identifies the contact arrangement and its reference condition, while the equipment and control information establish how the contact is used and interpreted. A terminal label cannot replace that system-level explanation.

Do not treat a contact-state description as a wiring instruction or a safety conclusion. A documented open or closed contact in a reference state does not prove that the correct terminals are installed, that the circuit behaves as intended, or that a safety function is established. The required interpretation depends on the exact switch and equipment documentation and the applicable circuit and control logic.

### Related guides

- [bottling machine home position micro switch location](/guides/bottling-machine-home-position-micro-switch-location/)
- [incinerator end of stroke micro switch maintenance](/guides/incinerator-end-of-stroke-micro-switch-maintenance/)
- [rotary indexing table guard interlock micro switch location](/guides/rotary-indexing-table-guard-interlock-micro-switch-location/)
- [security barrier open position micro switch wiring](/guides/security-barrier-open-position-micro-switch-wiring/)

## What terminal labels alone cannot verify

NO and NC labels alone cannot verify installation correctness, continuity under operating conditions, or suitability for a safety function. They also cannot establish the robot’s response at stroke end. Those conclusions require information beyond the terminal names, including the documented contact arrangement, the mechanism’s relationship to the actuator, and the circuit and control configuration.

Do not use a click or apparent actuator motion as proof of electrical contact condition. A component-level contact description is also not proof of an installed circuit’s behavior. If a particular verification is needed, its interpretation must follow the applicable switch and equipment documentation and the required conditions for that verification. A general terminal label is not a test result.

The bounded conclusion is simple: read NO and NC at the switch’s documented reference condition; trace any end-of-stroke contact change only when the mechanism and switch arrangement are documented; and establish the robot’s response from its actual circuit and configured control logic. For a **collaborative robot end of stroke micro switch NO and NC terminals**, the labels explain contact states in context, but they do not independently establish position, wiring correctness, controller behavior, or safety function.

## Sources and references

- Defense Logistics Agency ASSIST: [MIL-PRF-8805K: Switches and Switch Assemblies, Sensitive, Snap Action, General Specification For](https://quicksearch.dla.mil/qsDocDetails.aspx?ident_number=7196){: rel="nofollow noopener noreferrer" }
- Occupational Safety and Health Administration: [29 CFR 1910.333: Selection and Use of Work Practices](https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.333){: rel="nofollow noopener noreferrer" }
- Wikipedia: [Miniature snap-action switch](https://en.wikipedia.org/wiki/Miniature_snap-action_switch){: rel="nofollow noopener noreferrer" }
