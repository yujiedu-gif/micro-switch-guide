---
title: "dumbwaiter closed position micro switch NO and NC terminals"
description: "dumbwaiter closed position micro switch NO and NC terminals: Understand the operating idea, essential terminology, practical checks, limitations, and."
date: 2026-05-26 18:56:04 +0800
sitemap_omit_lastmod: true
category: Applications
tags:
  - dumbwaiter closed position micro switch NO and NC terminals
  - micro switches
  - Applications
author: editorial_team
---

The labels on a dumbwaiter closed position micro switch NO and NC terminals describe contact states relative to the switch’s specified actuator reference condition. They do not, by themselves, tell you which terminal is connected when the dumbwaiter is physically closed. That mapping depends on how the equipment’s mechanical linkage moves or releases the actuator.

A micro switch can change an electrical contact state in response to actuator movement, including in position or limit detection. To interpret its terminals, first establish the contact arrangement and the documented reference condition. Then keep that component-level behavior separate from the dumbwaiter’s position and from the controller’s response.

## What NO and NC mean on a dumbwaiter closed position micro switch NO and NC terminals

NO and NC are labels for contact states relative to a defined actuator reference condition. In a documented changeover arrangement, COM is the common terminal, and NO and NC identify the two contacts in relation to that reference. The exact switch marking or schematic controls; do not assume every micro switch has COM, NO, and NC terminals.

“Normally” does not mean “when the dumbwaiter is normally used,” nor does it automatically mean when its door or platform is closed. It refers to the specified reference condition for the switch. To identify which contact is associated with that condition, consult the exact switch documentation and its terminal markings. Without that information, the terminal arrangement and reference state remain unresolved.

The closed position is a condition of the dumbwaiter. The reference condition is a condition of the switch actuator. They are not interchangeable descriptions. A linkage might leave an actuator in its reference condition when the dumbwaiter is closed, or it might move the actuator from that condition. The terminal labels alone do not establish which arrangement is present.

This distinction is useful even before considering a particular circuit: it prevents “closed position” from being treated as another name for NO, NC, or “normally.” Identify the switch’s documented reference state first. Only then can a specific actuator condition be related to the contact state, and only if the mechanical arrangement is known.

## Why the closed position does not identify the active contact by itself

A position-detection arrangement has several separate links: the dumbwaiter reaches a physical position, a mechanical part acts on the switch actuator, the switch changes or maintains a contact state, and the equipment circuit interprets that state. Terminal labels describe only the contact relationship to the switch’s reference condition. They do not describe every link in that chain.

The linkage determines whether reaching the closed position releases the actuator or moves it. That is a design-specific relationship, not something that can be inferred from the words “closed position.” The switch may therefore be in its reference condition at that position, or it may be actuated. The available terminal labels do not settle which is true for a particular dumbwaiter.

The equipment circuit adds another distinct question: what does it do with the contact state? A controller might use a signal in a particular way, but NO and NC do not establish whether the system enables operation, stops it, or reports a condition. Do not infer an interlock, alarm, shutdown, or other control response without evidence about the actual equipment design.

Some dumbwaiter designs use a micro switch for position detection; others may use another sensing arrangement. The presence of a closed-position indication does not prove that a micro switch supplies it. If the switch type, actuator linkage, or circuit interpretation is not documented, keep each point open rather than assigning a terminal state or system behavior.

## How to verify terminal states without testing the installed circuit

A continuity comparison can be limited to the isolated switch, provided the switch can be safely isolated and its terminals and documented contact arrangement are established. Use the exact switch documentation to identify the terminals and the actuator reference condition. Do not identify terminals by guessing from a generic layout.

With the switch isolated, record the actuator condition being checked and compare continuity for each defined actuator state. Keep the observation tied to those conditions: the result describes the tested switch under the test conditions, not the dumbwaiter’s position or the controller’s response. A click or a change in actuator feel would not, by itself, establish the electrical contact state.

This is not a procedure for testing the installed circuit, bypassing equipment controls, or deciding that the dumbwaiter is safe to operate. An isolated reading cannot establish the condition of wiring or other equipment, and it does not show how the controller responds. If safe isolation, terminal identification, or the applicable test procedure is uncertain, stop and refer the work to qualified personnel.

Do not extend a contact-state check into an adjustment or repair conclusion. The test can compare observed continuity with documented switch behavior for defined actuator conditions. It cannot establish that the linkage reaches the intended position, that the actuator is correctly positioned, or that the equipment’s control logic functions as intended.

### Related guides

- [bottling machine home position micro switch location](/guides/bottling-machine-home-position-micro-switch-location/)
- [incinerator end of stroke micro switch maintenance](/guides/incinerator-end-of-stroke-micro-switch-maintenance/)
- [rotary indexing table guard interlock micro switch location](/guides/rotary-indexing-table-guard-interlock-micro-switch-location/)
- [security barrier open position micro switch wiring](/guides/security-barrier-open-position-micro-switch-wiring/)

## What this terminal check can and cannot establish

A documented, isolated comparison can help identify the contact behavior of the particular switch under the actuator states tested. Its meaning depends on the terminal identification, the documented reference condition, and the conditions of the check. If any of those are unknown, the result should not be treated as a definitive mapping of NO and NC for that device.

Even a clear contact reading does not establish that the dumbwaiter is physically closed. It does not establish that the linkage moves the actuator as intended, that the installed wiring is correct, or that the controller recognizes the signal in a particular way. Those are separate mechanical and system questions, and the terminal labels cannot answer them.

The practical boundary is narrow: use the switch documentation to understand the terminals, relate contact behavior only to a defined actuator condition, and avoid translating that result directly into an equipment-state or safety conclusion. A micro switch may be part of a dumbwaiter’s position-detection arrangement, but the arrangement and its system effect are design-specific. The phrase dumbwaiter closed position micro switch NO and NC terminals does not supply the missing linkage or circuit details.

## Sources and references

- Defense Logistics Agency ASSIST: [MIL-PRF-8805K: Switches and Switch Assemblies, Sensitive, Snap Action, General Specification For](https://quicksearch.dla.mil/qsDocDetails.aspx?ident_number=7196){: rel="nofollow noopener noreferrer" }
- Wikipedia: [Miniature snap-action switch](https://en.wikipedia.org/wiki/Miniature_snap-action_switch){: rel="nofollow noopener noreferrer" }
