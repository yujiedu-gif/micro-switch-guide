---
title: "Electric micro switches: How They Work and What Their Ratings Mean"
description: "electric micro switches: Understand the operating idea, essential terminology, practical checks, limitations, and evidence needed for careful selection,."
date: 2026-09-21 09:00:00 +0800
category: Basics
tags:
  - electric micro switches
  - micro switches
  - Basics
author: editorial_team
---

Electric micro switches use mechanical movement to change an electrical contact state. Understanding how **electric micro switches** transfer contacts requires following actuator travel through an operating point and a separate release point. This matters because a switch does not necessarily reset at the same position where it first changes state. Terminal labels and ratings also need to be read in context: the contact arrangement identifies possible circuit paths, while electrical ratings apply under specified load and test conditions.

The sections below explain the snap-action mechanism, the relationship between travel and reset, and how to interpret contact states. They also distinguish electrical ratings from mechanical operating parameters and outline a bounded way to verify switching behavior with the circuit isolated. No universal terminal layout, rating, or compatibility can be assumed without checking the particular device’s markings or documentation.

## Electric micro switches: the snap-action mechanism

An electric micro switch is a mechanically actuated switch: movement applied to its actuator operates electrical contacts. Its role is to translate a physical input into a change in circuit continuity. The term “micro” does not, by itself, establish the dimensions, contact arrangement, rating, or construction of a particular switch.

In a snap-action mechanism, the contact movement is not simply a scaled copy of the actuator’s movement. The supplied definition of snap action describes contact action in which the speed of the moving contacts is relatively independent of the speed of the actuating mechanism. In practical terms, actuator movement brings the mechanism toward an operating point; contact transfer then occurs as a distinct action rather than necessarily following the actuator at the same speed.

This distinction helps explain why slow actuator movement does not necessarily mean slow contact movement. The mechanism’s contact action is characterized by snap action, while the actuator can be moving through its travel at a different rate. The exact internal construction and actuator form vary by design, so the general description does not identify a particular mechanism or imply a particular terminal arrangement.

It is useful to keep three things separate: the physical input applied to the actuator, the actuator’s position, and the resulting electrical contact state. Those are related, but they are not interchangeable descriptions. A switch can reach a contact-changing point and later require a different position or force condition before the contacts return.

## How actuator travel changes contact state

Actuator travel describes movement through defined positions. **Pretravel** is the distance or angle through which the actuator moves from its free position to its operating position. The **operating force** is the force or torque applied to the actuating mechanism to operate the contacts. These terms describe different properties: one concerns movement, and the other concerns applied force or torque.

At the operating position, the contacts operate. If the actuator then returns, the contacts do not necessarily reset at that same position. **Movement differential**, also called differential travel, is the distance or angle through which the actuator travels from the operating position to the releasing position. This separation between operating and releasing positions is why the switch’s state should be understood across its travel rather than as a single on/off point.

The **release force**, or releasing force, is the force or torque to which force on the actuator must be reduced to permit the contacts to return to the unoperated position after operation. Operating force and release force therefore refer to different points in the action: one describes the force applied to operate the contacts, and the other describes the reduced force condition that permits their return.

These definitions do not provide universal travel or force values. The values and allowable movement for a particular switch must be established from its applicable documentation. Applying excessive force or travel beyond specified limits may damage a switch; the supplied information does not establish a safe amount of overtravel for any particular device. Avoid treating a general mechanism description as permission to push an actuator beyond its specified limits.

## Read terminals and normally open or normally closed states

Common changeover terminology uses **COM** for the common terminal, **NO** for the normally open terminal, and **NC** for the normally closed terminal. “Normally” refers to the unactuated state in this terminology. For a device with these contact relationships, the COM-to-NC path is closed and the COM-to-NO path is open when unactuated; when the contact changes state under actuation, those paths change accordingly.

These labels describe contact relationships, not a guaranteed physical terminal layout. Check the markings or documentation for the particular switch and verify its schematic before interpreting terminals. The exact device schematic matters, and the generic labels alone do not establish which physical terminal is which or whether a particular device has a changeover arrangement.

For a basic state check, consider each path separately and compare continuity in the unactuated and actuated states. A normally closed path should show continuity in the unactuated state, while a normally open path should not; the contact state changes when the switch is actuated. This description concerns contact continuity, not whether a complete appliance circuit will operate. Wiring and other circuit components can affect what is observed in an assembled device.

## Separate electrical ratings from mechanical limits

Electrical ratings and mechanical operating parameters answer different questions. Electrical ratings concern the voltage and current associated with switching a specified load under stated test conditions. They are specification-sheet requirements tied to stated load and test conditions, not universal switching capacities. A rating cannot be interpreted independently of its stated conditions.

Load type and switching conditions matter alongside voltage and current. A rating established for one stated load or test condition does not, by itself, establish suitability for a different load or condition. Inductive or other demanding loads can affect contact life, so the relevant load and switching conditions must be checked in the applicable documentation. Do not infer a general capacity from a voltage or current number without its context.

Mechanical parameters instead describe how the actuator moves and what force or torque is associated with operation and release. Pretravel, movement differential, operating force, and release force are not electrical load ratings. Conversely, an electrical rating does not specify actuator travel or operating force. These parameters need to be evaluated separately; meeting one category does not establish that the other is suitable.

The available definitions and rating principle do not supply universal numerical limits. They also do not establish an exact rating for an unidentified switch. For an actual device, consult its specification sheet and applicable documentation for voltage, current, load type, switching conditions, and mechanical limits. Keep each stated condition with the value it qualifies, and do not extend a rating beyond those stated conditions.

### Related guides

- [dual micro switch](/guides/dual-micro-switch/)
- [touch micro switch](/guides/touch-micro-switch/)
- [no nc micro switch](/guides/no-nc-micro-switch/)
- [normally open micro switch](/guides/normally-open-micro-switch/)

## Verify electric micro switches safely

A basic continuity check is limited to an isolated, de-energized circuit. Before checking continuity, de-energize and isolate the circuit. Do not use a continuity check as a live-circuit test. The supplied information does not specify a meter model, procedure for a particular appliance, or additional safety steps for a specific installation, so those details cannot be generalized here.

With the circuit isolated, identify the switch terminals from its markings or documentation. Check the expected contact path in the unactuated state, then actuate the switch and check again. For a documented COM/NO/NC arrangement, compare the COM-to-NC and COM-to-NO paths with their expected unactuated and actuated states. The check is about whether the relevant contacts show continuity in each state; it does not establish that the rest of the circuit is correctly wired or functioning.

If readings do not match expectations, the result alone does not identify a cause. Wiring, contact configuration, or switch condition may affect the readings and require further diagnosis. Confirm the device’s actual schematic and circuit context before drawing conclusions. A continuity result can show a state difference under the check conditions, but it does not establish a switch’s electrical-load suitability, mechanical limits, or performance under operating conditions.

The core distinction is between actuator movement and contact state: snap action transfers contacts at an operating point, while release behavior and differential travel describe how the switch returns. Interpret terminals from the specific device documentation, and evaluate electrical ratings separately from mechanical limits. A continuity check can verify expected isolated contact states, but **electric micro switches** still require device-specific documentation to establish their ratings and operating limits.

## Sources and references

- Defense Logistics Agency ASSIST: [MIL-PRF-8805K: Switches and Switch Assemblies, Sensitive, Snap Action, General Specification For](https://quicksearch.dla.mil/qsDocDetails.aspx?ident_number=7196){: rel="nofollow noopener noreferrer" }
- Wikipedia: [Miniature snap-action switch](https://en.wikipedia.org/wiki/Miniature_snap-action_switch){: rel="nofollow noopener noreferrer" }
