---
title: "operating table position micro switch NO and NC terminals"
description: "operating table position micro switch NO and NC terminals: Understand the operating idea, essential terminology, practical checks, limitations, and."
date: 2026-08-16 09:00:00 +0800
category: Applications
tags:
  - operating table position micro switch NO and NC terminals
  - micro switches
  - Applications
author: editorial_team
---

An **operating table position micro switch NO and NC terminals** indicate which electrical contact is connected to the switch’s common terminal as its actuator changes position. The labels describe contact behavior relative to the switch’s unactuated state; they do not, by themselves, name a table position such as raised, lowered, or tilted.

The distinction matters when identifying contacts or interpreting a position signal. A mechanical feature may operate a switch, and the equipment circuit may use the resulting contact change to represent a position. The switch’s contact state and the table’s reported position are related through that circuit, not interchangeable descriptions.

## What operating table position micro switch NO and NC terminals indicate

In generic changeover terminology, **COM** means common terminal, **NC** means normally closed terminal, and **NO** means normally open terminal. “Normally” refers to the switch’s unactuated state. In that state, COM and NC are connected, while COM and NO are not connected.

When the actuator is operated, the contact relationship changes: COM moves from the NC contact to the NO contact. In the resulting actuated state, COM-NC is open and COM-NO is closed. This describes the contact transition, not a universal direction of movement for an operating table. Whether a switch is pressed or released at a particular table position depends on the equipment’s mechanical arrangement.

The terms *pretravel* and *overtravel* describe actuator movement, not table travel. Pretravel is the distance or angle through which the actuator moves from free position to operating position. Overtravel is the distance or angle between the operating position and the extreme position to which the actuator may be moved. These definitions help distinguish switch movement from the larger mechanism’s position; they do not specify where an operating table should be or how far it should move.

A change in COM’s connection can therefore report that the switch actuator has changed state. It does not independently identify a particular table position. That interpretation belongs to the equipment circuit and its documentation.

## How the micro switch state relates to operating table position

A design may use a mechanical position feature to press or release a micro switch. If that happens, the switch changes between its unactuated and actuated contact states. The contact transition is evidence of the actuator’s state; the equipment circuit determines what that state means for the table’s position signal.

For example, an operating table control circuit may interpret a documented contact state as an indication associated with a particular position. The terminal labels alone do not establish that interpretation. The same NO or NC contact state cannot be assigned a universal table direction or position without the relevant circuit information.

Switch count, placement, and logic can vary by table design. A position signal may depend on how a switch is installed and how its contacts are connected within that equipment. Do not infer a switch’s location, the number of switches, or the meaning of an open or closed contact from generic terminal labels.

To understand a position indication, keep three things separate: the physical table position, the micro switch actuator position, and the circuit’s interpretation of the contact state. The switch reports a contact change. The documented equipment circuit provides the context for connecting that change to a position signal.

## Identify NO and NC contacts with a safe continuity check

Before testing, isolate power and follow the applicable equipment service and safety instructions. Do not probe an energized circuit. If the documentation does not describe how to isolate or disconnect the switch safely, do not proceed on the basis of a generic test procedure.

When documentation directs that the switch be disconnected for testing, use a continuity or resistance measurement to compare COM-NC and COM-NO in both actuator states. Record the readings for the unactuated state, then for the actuated state. In generic changeover behavior, COM-NC has continuity and COM-NO does not in the unactuated state; those relationships reverse in the actuated state.

The point of the check is to verify which contacts change state, not to infer a table position or authorize a wiring change. Compare the observations with the exact switch schematic, terminal markings, and equipment circuit documentation. A continuity result by itself does not establish how the table’s control system uses that contact.

Do not use the test as a reason to bypass a switch, test live wiring, or alter connections. If the switch cannot be safely isolated as directed, or the observed contacts do not match the applicable documentation, leave the circuit unchanged and refer the equipment to qualified service personnel.

### Related guides

- [ball screw actuator home position micro switch replacement](/guides/ball-screw-actuator-home-position-micro-switch-replacement/)
- [bottling machine end of stroke micro switch](/guides/bottling-machine-end-of-stroke-micro-switch/)
- [automated guided vehicle home position micro switch location](/guides/automated-guided-vehicle-home-position-micro-switch-location/)
- [accelerator pedal position stop micro switch operating force](/guides/accelerator-pedal-position-stop-micro-switch-operating-force/)

## Interpret a position signal without assuming wiring logic

An open or closed contact may have different significance depending on the documented circuit. After identifying the contact behavior, compare it with the applicable wiring diagram and the documented position sequence. Interpret the signal using that equipment-specific information rather than assuming that NO always means one table position or that NC always means another.

A wiring diagram, terminal marking, circuit function, and permissible load documented for the exact switch and equipment govern identification and interpretation. Physical terminal layout alone is not a reliable basis for assigning a terminal function. Generic COM, NO, and NC terminology is useful for understanding a changeover contact, but the exact device schematic and equipment documentation determine how it applies in a particular installation.

If the measured contact behavior conflicts with the documentation, the signal should not be reinterpreted through guesswork. Likewise, if safe isolation or testing is unclear, do not probe the circuit or make an unverified wiring change. Qualified service personnel can assess the equipment using its applicable documentation and procedures.

The practical conclusion is limited but useful: NO and NC describe contact relationships relative to the switch’s unactuated state, and operating the actuator changes which contact is connected to COM. A position signal is the equipment circuit’s interpretation of that change. For an **operating table position micro switch NO and NC terminals**, verify contact behavior against the exact device and equipment documentation before drawing conclusions about table position.

## Sources and references

- Defense Logistics Agency ASSIST: [MIL-PRF-8805K: Switches and Switch Assemblies, Sensitive, Snap Action, General Specification For](https://quicksearch.dla.mil/qsDocDetails.aspx?ident_number=7196){: rel="nofollow noopener noreferrer" }
- Occupational Safety and Health Administration: [29 CFR 1910.333: Selection and Use of Work Practices](https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.333){: rel="nofollow noopener noreferrer" }
- Wikipedia: [Miniature snap-action switch](https://en.wikipedia.org/wiki/Miniature_snap-action_switch){: rel="nofollow noopener noreferrer" }
