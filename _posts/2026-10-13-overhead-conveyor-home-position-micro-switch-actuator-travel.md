---
title: "Overhead conveyor home position micro switch actuator travel"
description: "overhead conveyor home position micro switch actuator travel: Understand the operating idea, essential terminology, practical checks, limitations, and."
date: 2026-10-13 13:45:35 +0800
category: Applications
tags:
  - overhead conveyor home position micro switch actuator travel
  - micro switches
  - Applications
author: editorial_team
---

An overhead conveyor home position is a reference defined by the conveyor’s own mechanical arrangement or control design. In an installation that uses a micro switch, overhead conveyor home position micro switch actuator travel describes only part of the relationship: conveyor movement must be transmitted through a target or linkage to the switch actuator, and the control system must interpret the resulting contact change. The switch’s actuator travel is not automatically the conveyor’s travel or its home-position tolerance.

## What overhead conveyor home position means when a micro switch is used

“Home position” refers to a position that the host system defines as a reference. Its meaning depends on the particular conveyor’s mechanism and control design. A micro switch may provide an input used to identify that reference in some designs, but the term does not imply that every overhead conveyor uses one or that the switch itself defines the reference.

The switch is one component in a possible chain of events. A conveyor feature may move a target, cam, lever, or linkage; that part may then move the switch actuator. If the actuator reaches the switch’s operating position, the contacts change state. The conveyor’s control system may use that change as an input, but what the input means depends on the actual control design.

Keep these parts distinct when interpreting a home signal:

- The **conveyor reference** is the position or condition defined by the host system.
- The **target or linkage** transfers motion from a conveyor feature to the switch actuator, if the installation has one.
- The **micro switch** responds to actuator movement and changes contact state at its operating point.
- The **control system** interprets the input according to its circuit and logic.

These elements are related, but they are not interchangeable. A switch contact change alone does not define what the conveyor’s controller calls home, nor does it establish what action the controller takes. Those details require the applicable design documentation.

## Overhead conveyor home position micro switch actuator travel

To relate actuator travel to a conveyor reference, trace the motion in order. First, identify the feature or position that the conveyor design treats as its reference. Next, determine how movement of that feature reaches the target or linkage. Then follow how that part moves the actuator and where the actuator reaches the switch’s operating position. Only after that can the contact change be related to the control system’s interpretation of the signal.

This chain is conditional on the installed arrangement. A target may move directly with a conveyor feature, or a linkage may transfer or alter motion. The available claims do not establish which arrangement a particular conveyor uses, how far its target moves, or what control response follows a contact change. Those facts must remain specific to the design rather than inferred from the words “home position” or “micro switch.”

The switch’s operating point is the actuator position at which operation occurs. It is not, by definition, the conveyor’s home position. The conveyor’s reference may be established by the mechanical feature’s location, the point at which the control input changes, or another element of the system design. Without documentation showing how these points correspond, one cannot conclude that the operating point marks the intended conveyor reference.

The contact change is also not a complete description of system behavior. Its meaning depends on the control circuit and logic. A contact change could be used as an input in a sequence, but the supplied information does not establish a particular sequence, state, or resulting action. Do not infer a stopping, indexing, or positioning response merely because a micro switch is present.

For a specific installation, the relevant question is therefore not simply how much the actuator moves. It is how the defined conveyor reference, moving feature, target or linkage, switch operating point, and control interpretation relate in that design. The relationship must be established from the applicable drawings and procedures.

## Actuator motion is not the same as conveyor travel

Switch travel terminology describes actuator motion, not the distance traveled by an overhead conveyor. Under MIL-PRF-8805K sections 6.5.14 and 6.5.16, pretravel runs from the free position to the operating position, while overtravel runs from the operating position to the extreme permitted actuator position. The specification’s section 6.5 also distinguishes actuating force, releasing force, free position, operating position, movement differential, pretravel, and overtravel. These are switch operating-characteristic terms; they do not state a conveyor’s home-position tolerance.

The operating point is where operation occurs. The release point is a distinct event, and movement differential describes the separation between operating and releasing positions. Consequently, the position at which a switch changes state during motion toward operation need not be the same actuator position at which it changes state during return motion. The switch terminology identifies these events; it does not, by itself, establish their locations relative to the conveyor’s reference.

A direct conversion from actuator travel to conveyor distance is not supported without the specific geometry. The relevant relationship depends on how the conveyor feature moves the target, how the target or linkage moves the actuator, and where the switch is mounted. A movement along one part of that chain cannot simply be treated as an equal movement along another part. The available claims provide no dimensions or geometry for a particular installation, so no numerical conversion can be stated.

Overtravel also has a defined boundary: it extends from the operating position to the extreme permitted actuator position. It is not a measure of how far the conveyor can continue moving, nor does it establish an acceptable stopping distance. Whether the actuator can move beyond its operating point, and how that motion relates to the host mechanism, must be determined from the design and applicable documentation.

Keep three ideas separate: switch travel, the conveyor’s defined home reference, and the conveyor’s stopping or positioning behavior. The specification’s travel terms describe the switch; system tolerance and stopping behavior belong to the conveyor design and control sequence. The supplied evidence does not give a universal relationship among them.

### Related guides

- [accelerator pedal position stop micro switch NO and NC terminals](/guides/accelerator-pedal-position-stop-micro-switch-no-and-nc-terminals/)
- [industrial boiler travel limit micro switch maintenance](/guides/industrial-boiler-travel-limit-micro-switch-maintenance/)
- [access control door position micro switch NO and NC terminals](/guides/access-control-door-position-micro-switch-no-and-nc-terminals/)
- [capping machine guard interlock micro switch actuator travel](/guides/capping-machine-guard-interlock-micro-switch-actuator-travel/)

## What to verify before interpreting a home-position signal

Begin with the documentation for the actual installation. Identify the switch and actuator arrangement, the conveyor feature used as the reference, and any target or linkage between that feature and the actuator. Confirm how the design identifies the operating position and how the control documentation defines and interprets the home-position input. Do not assume these relationships from a generic conveyor description.

The applicable drawings and approved procedures should also establish the intended target alignment, relevant mechanical limits, and control sequence. These details determine whether actuator operation corresponds to the intended system reference. This article does not provide an adjustment method or a tolerance for an unspecified conveyor; neither can be derived from the switch’s travel terminology alone.

A click may indicate movement of a snap mechanism, but it does not establish that the installed conveyor is at its defined home position. Likewise, an isolated contact check does not establish the target’s alignment, the control system’s interpretation, or correct system behavior. A switch observation is one part of the motion and signal chain, not proof of the whole assembly’s condition.

Use the documentation and procedures applicable to the specific conveyor and switch arrangement. Do not treat a general description of actuator travel as permission to adjust or test an installation. Electrical work beyond the procedure supplied for that system should be left to qualified personnel.

The relationship is established only when the design shows how the conveyor reference leads through target or linkage motion to the switch’s operating point and how the control system interprets the contact change. Overhead conveyor home position micro switch actuator travel describes that relationship, not a universal distance or tolerance. Without the installation-specific geometry and control documentation, the conversion and system response remain unresolved.

## Sources and references

- Defense Logistics Agency ASSIST: [MIL-PRF-8805K: Switches and Switch Assemblies, Sensitive, Snap Action, General Specification For](https://quicksearch.dla.mil/qsDocDetails.aspx?ident_number=7196){: rel="nofollow noopener noreferrer" }
