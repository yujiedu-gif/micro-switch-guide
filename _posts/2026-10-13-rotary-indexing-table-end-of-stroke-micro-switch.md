---
title: "Rotary indexing table end of stroke micro switch: what does it detect?"
description: "rotary indexing table end of stroke micro switch: Understand the operating idea, essential terminology, practical checks, limitations, and evidence needed."
date: 2026-10-13 11:27:16 +0800
category: Applications
tags:
  - rotary indexing table end of stroke micro switch
  - micro switches
  - Applications
author: editorial_team
---

In some rotary indexing table designs, a **rotary indexing table end of stroke micro switch** detects actuator movement associated with a mechanically defined table position or stroke endpoint. The switch changes a contact state when its actuator moves, if the design connects table motion to that actuator. It does not, by itself, establish that the table stopped, completed an index, or responded correctly to a control signal.

The mechanical arrangement and the control circuit determine what the indication means. Understanding the signal therefore requires separating three events: the table or linked mechanism reaches a position, the mechanism moves the switch actuator, and the switch contacts change state. Whether that contact change causes a controller or other circuit to act is a separate question.

## What does a rotary indexing table end of stroke micro switch detect?

In a design that uses one, a rotary indexing table end of stroke micro switch detects actuator movement associated with a defined table position or stroke endpoint. The switch provides an electrical contact-state change in response to mechanical actuator movement. The position represented by that change depends on how the particular table’s mechanism operates the switch.

This is an indication, not a direct measurement of every aspect of table motion. A contact change can correspond to an endpoint in the mechanism, but the switch alone does not establish that the table has fully stopped or that an indexing sequence has finished. Those conclusions depend on the machine’s mechanical arrangement and control design, neither of which can be inferred merely from the presence of a micro switch.

The switch also does not define what the control system does with its contact state. Depending on the documented circuit, a state change may be used as an input to control logic. Without that circuit information, it is not possible to say whether the signal initiates a stop, permits another movement, produces an alarm, or serves another purpose. Nor does the switch’s presence establish which contact state is considered normal.

The useful starting point is therefore specific: identify what part moves the actuator and what position that movement is intended to represent. Then treat the contact change as a signal whose meaning must be established from the table’s documentation, rather than as proof of the table’s complete operating state.

## How table motion reaches the micro switch actuator

The causal path depends on the particular table design. If the arrangement includes a cam, stop, linkage, or another linked mechanism, table movement may move that part, which in turn acts on the micro switch actuator. The actuator movement can then produce a contact-state change. This is a conditional description, not a claim that every rotary indexing table has a cam, stop, linkage, or switch in the same location.

Keep the events in that chain distinct. Movement of the table does not necessarily mean the actuator has moved. Actuator movement does not, on its own, prove that the contacts have changed state. And a contact-state change does not prove that the control system received or acted on the signal. Each link depends on the actual mechanical and electrical design.

The switch’s operating event should also not be treated as identical to the table reaching its endpoint. The external mechanism may act on the actuator as the table moves, but the available facts do not establish a universal geometry, adjustment, or exact relationship between actuator operation and the table’s position. Any such relationship must come from the documentation for the specific arrangement.

Travel terminology can help describe actuator motion when it is relevant and documented. Pretravel runs from the actuator’s free position to its operating position; overtravel runs from the operating position to the extreme permitted actuator position. These definitions describe actuator travel, not the distance or angle traveled by the indexing table. They do not establish how far a particular table moves before operating the switch or whether a particular setup is correctly adjusted.

The practical distinction is between the mechanism’s position and the switch’s response to movement. The table may reach a mechanically defined point, the linked mechanism may move the actuator, and the contacts may change. Establishing that sequence for an individual table requires its specific design information; a generic description cannot supply missing geometry or adjustment details.

## What the switch signal does, and does not, prove

A contact-state change can serve as an input to control logic only where the wiring and control design establish that role. The switch is the component that responds mechanically and changes contact state. The control circuit determines whether that state is used and what action, if any, follows. Do not infer a stop command, completed indexing, alarm, or particular normal state from the switch alone.

Likewise, evidence of actuator movement is not evidence of electrical continuity. A click may indicate movement of a snap mechanism, but it does not prove that the contacts have changed state, that the terminals are connected as intended, or that the control system responded. The observation is limited to the movement or sound actually observed.

It helps to keep the possible stages separate: the table moves; a related mechanism acts on the actuator; the switch contacts change state; the wiring carries a signal; and the control design responds. A problem or uncertainty at one stage cannot be assigned to another solely from an endpoint symptom. For example, apparent table movement does not identify a switch-contact problem, and a contact change does not demonstrate that the installed circuit acted on it.

The evidence boundary matters when describing what an endpoint indication establishes. If the documented arrangement shows that a particular contact state is used to represent a position, the switch can provide that indication under the specified conditions. Without that documentation, the safe conclusion is narrower: actuator movement may produce a contact-state change, while the signal’s meaning and downstream effect remain unknown.

### Related guides

- [bottling machine home position micro switch location](/guides/bottling-machine-home-position-micro-switch-location/)
- [incinerator end of stroke micro switch maintenance](/guides/incinerator-end-of-stroke-micro-switch-maintenance/)
- [rotary indexing table guard interlock micro switch location](/guides/rotary-indexing-table-guard-interlock-micro-switch-location/)
- [security barrier open position micro switch wiring](/guides/security-barrier-open-position-micro-switch-wiring/)

## How to verify an endpoint indication without overdiagnosing

Begin by identifying the specific switch, its actuator, the documented terminals, and the reference condition for the contact arrangement. COM, NO, and NC should be used only when those terminal designations are confirmed for that switch. NO and NC describe contact states relative to a specified reference condition; the labels alone do not establish what the rotary table’s controller expects during operation.

For an isolated continuity check, the switch must be isolated from the surrounding circuit, and the actuator state and expected behavior must be defined by the applicable documentation. A reading in one actuator state can provide evidence about the isolated switch contacts under that test condition. It does not prove that the installed wiring is correct, that the controller receives the signal, or that the table operates safely.

A click or visible actuator movement is a separate observation. It can help establish that some mechanical movement occurred, but it does not substitute for a continuity check and does not confirm downstream response. Conversely, an uncertain system response does not by itself show that the switch failed: the cause could lie in the mechanical input, the contact state, terminal identification, wiring, or control system. The available evidence must distinguish those possibilities rather than collapsing them into one diagnosis.

Use the documentation and a defined, safe procedure for any verification. Do not infer an installed circuit’s safety from an isolated switch reading. Electrical checks that are hazardous or outside the documented safe procedure should be left to qualified personnel. The purpose of bounded verification is to establish what was actually observed at each stage, not to declare the entire table or control system good or bad from one test.

In short, a **rotary indexing table end of stroke micro switch** may indicate that a mechanically linked actuator has moved at a defined point in a particular design. That indication is distinct from proof that the table stopped correctly or that its control system received and acted on the signal. The specific mechanism, contact arrangement, and circuit documentation determine how far the conclusion can go.

## Sources and references

- Defense Logistics Agency ASSIST: [MIL-PRF-8805K: Switches and Switch Assemblies, Sensitive, Snap Action, General Specification For](https://quicksearch.dla.mil/qsDocDetails.aspx?ident_number=7196){: rel="nofollow noopener noreferrer" }
- Wikipedia: [Miniature snap-action switch](https://en.wikipedia.org/wiki/Miniature_snap-action_switch){: rel="nofollow noopener noreferrer" }
