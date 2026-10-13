---
title: "vibratory feeder home position micro switch NO and NC terminals"
description: "vibratory feeder home position micro switch NO and NC terminals: Understand the operating idea, essential terminology, practical checks, limitations, and."
date: 2026-10-13 11:27:16 +0800
category: Applications
tags:
  - vibratory feeder home position micro switch NO and NC terminals
  - micro switches
  - Applications
author: editorial_team
---

A vibratory feeder home position micro switch NO and NC terminals are contact labels interpreted relative to the switch’s documented reference condition, not automatically relative to the feeder’s home position. NO means normally open and NC means normally closed in that stated reference condition, when the switch’s documented contact arrangement uses those labels. To verify their behavior, identify the terminals from the exact switch documentation, isolate the switch as permitted by the documented procedure, and check continuity at defined actuator states using an appropriate method. The result describes the isolated contact behavior; it does not establish how the feeder interprets the signal or prove the installed system is operating correctly.

## What “vibratory feeder home position micro switch NO and NC terminals” means

A micro switch is a component that can change electrical contact state when its actuator moves. It is not the feeder’s home-position system itself. The labels NO and NC describe contacts in relation to a specified reference condition for the switch. They do not, by themselves, say what contact state exists when the feeder is at home.

Where the documented contact arrangement identifies a COM terminal, COM is the common terminal for that arrangement. NO and NC identify the contact paths relative to COM and the stated reference condition. Do not assume that a particular terminal is COM, or infer terminal identity from its physical location. Use the terminal markings and connection diagram for the exact switch.

The words “normally open” and “normally closed” require a reference frame. A label is not a guarantee that the contact will remain open or closed through every actuator position. If the switch documentation specifies the reference condition, use it to interpret the labels. If the reference condition or terminal arrangement is not documented, the names alone do not establish the actual terminals or states.

This distinction matters because the switch may be mechanically actuated in the feeder’s home position, or it may be released there. The feeder’s position name does not resolve that mechanical relationship. Nor does a contact label establish whether the feeder controller reads an open or closed circuit as “home.” Those facts depend on the particular mechanism, wiring, and control logic.

## Separate switch state from the feeder’s home position

A feeder mechanism may move a micro switch actuator as the mechanism changes position, but the exact arrangement has to be established for the specific design. The switch actuator’s position and the feeder’s home position are related only through the installed mechanical arrangement. Do not assume that home means the actuator is released, that it is engaged, or that either NO or NC must be closed at home.

Keep three things distinct: the switch’s documented reference condition, the actuator’s actual mechanical state, and the feeder’s home position. The reference condition gives meaning to NO and NC. The actuator state can change the contacts from that reference arrangement. The feeder position is a state of the host mechanism. One does not determine the others without design-specific documentation or observation.

A contact change also does not specify the controller’s response. Depending on the actual wiring and control logic, an open or closed input may be interpreted in different ways. The presence of a micro switch does not establish a particular normal state, signal meaning, alarm, or stopping behavior. Those conclusions require the feeder’s relevant circuit and control documentation.

Accordingly, a report that the feeder is “at home” is not enough to predict NO or NC continuity. To make that prediction, the applicable switch documentation must define the terminal arrangement and reference condition, and the feeder design must establish how its mechanism positions the actuator. The wiring and control logic are separately needed to explain what that contact state means to the equipment.

## Verify NO and NC contact behavior safely

Start with the switch documentation. Identify the terminals from its connection diagram and markings, and find the specified reference condition. Do not use a generic physical-layout assumption to identify terminals. Use the documented safe procedure to isolate the switch before checking continuity; where deenergization or qualification requirements apply, follow them. If isolation cannot be established within the applicable procedure, do not treat an in-circuit observation as an isolated-switch test.

Define the actuator state before each observation. For example, record whether the actuator is in the documented reference condition or in another clearly described position. Then check the specified contact paths with a suitable continuity method. If the arrangement identifies COM, record the observed state of the documented COM-to-NO and COM-to-NC paths as applicable. Compare results with the switch’s documented arrangement and the exact actuator state tested. Do not extend a result from one state to another without evidence.

A useful record states which switch was checked, which terminals were tested, whether it was isolated, what actuator state was used, and what continuity result was observed. These details keep the result tied to its test conditions. If the documentation does not provide an expected behavior for the state tested, the observation alone cannot establish whether the switch is performing as intended.

A click may indicate movement of a snap mechanism, but it does not prove continuity, correct terminal identification, correct wiring, or suitability for the feeder’s circuit. Likewise, a continuity result on an isolated switch describes only the tested contact path and actuator state. It does not verify the feeder wiring, controller interpretation, mechanical positioning, or operation of the complete feeder.

### Related guides

- [aircraft door closed monitor micro switch NO and NC terminals](/guides/aircraft-door-closed-monitor-micro-switch-no-and-nc-terminals/)
- [access control door position micro switch function](/guides/access-control-door-position-micro-switch-function/)
- [ball screw actuator end of stroke micro switch contact rating](/guides/ball-screw-actuator-end-of-stroke-micro-switch-contact-rating/)
- [capping machine guard interlock micro switch actuator travel](/guides/capping-machine-guard-interlock-micro-switch-actuator-travel/)

## Interpret a mismatch without overdiagnosing

If an isolated-switch result differs from the documented expectation, first preserve the test conditions in the record. Check that the terminal identification came from the exact switch documentation and that the actuator state matches the condition being evaluated. A mismatch could involve terminal identification, the relationship between actuator movement and the tested state, internal contact behavior, or a test condition that does not match the documentation. One observation does not establish which explanation applies.

If the isolated contact behavior agrees with the documentation but the feeder does not indicate home as expected, the remaining question concerns the installed system. Wiring, mechanical actuation, and other equipment circuitry can affect the result. The isolated test does not establish the integrity of those parts or identify a fault elsewhere. A controller indication also cannot be inferred from NO or NC labels alone; it depends on the actual circuit and control logic.

Keep any further checks within the documented safe procedure and applicable qualification requirements. Work or testing beyond that boundary, including energized circuit diagnosis, should be left to qualified personnel. Do not infer installed-circuit safety from an isolated continuity reading.

The practical conclusion is limited but clear: interpret NO and NC from the switch’s documented reference condition, verify contact behavior with the switch isolated and the actuator state defined, and treat the feeder’s home indication as a separate system-level question. The vibratory feeder home position micro switch NO and NC terminals do not, on their own, reveal whether the feeder is at home or how its controller interprets the contact change.

## Sources and references

- Defense Logistics Agency ASSIST: [MIL-PRF-8805K: Switches and Switch Assemblies, Sensitive, Snap Action, General Specification For](https://quicksearch.dla.mil/qsDocDetails.aspx?ident_number=7196){: rel="nofollow noopener noreferrer" }
- Occupational Safety and Health Administration: [29 CFR 1910.333: Selection and Use of Work Practices](https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.333){: rel="nofollow noopener noreferrer" }
