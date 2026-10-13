---
title: "Collaborative robot guard interlock micro switch NO and NC terminals"
description: "collaborative robot guard interlock micro switch NO and NC terminals: Understand the operating idea, essential terminology, practical checks, limitations,."
date: 2026-10-13 11:27:16 +0800
category: Applications
tags:
  - collaborative robot guard interlock micro switch NO and NC terminals
  - micro switches
  - Applications
author: editorial_team
---

A **collaborative robot guard interlock micro switch NO and NC terminals** describe contact states on a particular switch, not the robot’s complete safety response. NO and NC are defined relative to the switch’s specified reference condition. To identify the terminals, use the exact switch’s markings or documentation, then compare any isolated continuity check with its documented contact table and a defined actuator state.

A micro switch may be part of a guard-interlock design, but not every collaborative robot guard uses one. Even when a micro switch is present, its contact arrangement and how the controller interprets it depend on the specific equipment design. Terminal labels alone do not establish what the robot will do when a guard moves.

## What NO and NC mean on a collaborative robot guard interlock micro switch NO and NC terminals

NO means normally open and NC means normally closed, but “normally” must be tied to the reference condition specified for that switch. The labels describe the documented contact state at that condition. They are not unconditional promises that a circuit will or will not carry current in every installed state.

A switch may document a reference condition such as an actuator state or another stated condition. Use the exact documentation to determine what condition applies. Without that information, do not assume whether the reference condition means the actuator is released, pressed, or positioned in some other way. The contact state can differ when the actuator changes position, but the documented state and operating conditions control the interpretation.

Some micro switches have a changeover contact arrangement with terminals labeled common, normally closed, and normally open. That terminology applies only when the exact switch documentation identifies those contacts. A device’s appearance, the number or position of its terminals, or labels on a different switch do not establish that it has this arrangement. Use COM, NO, and NC only where the specific device’s marking or schematic supports those names.

The distinction is between a contact description and circuit behavior. NO and NC identify a contact state under a specified reference condition; they do not, by themselves, say whether current flows in the robot circuit. That also depends on the wiring, the connected circuit, and the state being considered. Nor do the labels state whether a robot stops, slows, or signals an alarm when a guard opens. Those responses are properties of the actual control design, not meanings carried by the terminal labels.

If the switch uses a snap-action mechanism, actuator movement can change the contact state through that mechanism. Do not assume a particular switching mechanism when it is undocumented, or infer a robot response from the fact that the switch changes state. Keep the switch’s documented contact behavior separate from the guard linkage and the controller’s interpretation.

## Identify the micro switch terminals from the switch’s own documentation

Start with the exact switch’s terminal markings, connection diagram, or other documentation. Match the physical terminals to that documented information rather than relying on a generic layout. The wiring diagram, terminal marking, circuit function, and permissible load documented for the exact switch and equipment are the relevant references; a physical-layout guess cannot substitute for them.

If the documentation identifies COM, NO, and NC, use those labels as shown. If it gives a different arrangement, follow that arrangement instead. If the markings are unclear or the diagram cannot be matched confidently to the installed switch, terminal identity remains unresolved. Do not fill the gap by borrowing a pin position, wire color, or terminal order from another model or from a general drawing.

The guard mechanism does not determine the terminal names. A guard, cam, lever, or linkage may actuate a micro switch in a particular design, but its position does not make a terminal NO or NC. Those labels follow the switch’s documented reference condition and contact arrangement. Likewise, a wire connected to a terminal does not establish the terminal’s contact function unless the connection can be matched to reliable documentation for that switch.

This method identifies the switch terminals, not the whole interlock circuit. The equipment documentation may describe how the switch is connected and what the circuit is intended to do, but a terminal diagram by itself does not establish the controller’s safety logic or prove the guard system’s performance. Keep each conclusion within the evidence that supports it: switch documentation for terminal identity, and appropriate equipment documentation for system behavior.

## What an isolated continuity check can and cannot establish

A continuity check can provide a limited check of the switch’s contacts only when the switch is isolated from the circuit and the actuator state is defined. First identify the applicable contact table and reference condition in the exact switch documentation. Then relate the actuator state being checked to the conditions the documentation describes. Without those details, a meter reading cannot be confidently assigned to an NO or NC label.

Compare the observed continuity with the documented contact state for that same condition. If the switch has a documented COM, NO, and NC arrangement, use the documented contact table to determine which terminals to compare in each defined actuator state. Do not infer that a particular pair should show continuity merely from the terminal positions, wire colors, or a convention applied to another switch.

The result is limited to the isolated switch under the checked condition. It does not establish that the installed wiring is correct, that the controller interprets the contacts as intended, that the guard interlock performs its intended function, or that the robot system is safe. A reading that differs from the documented contact table is an observation requiring further interpretation, not by itself a complete diagnosis of the switch, wiring, or equipment.

Electrical work also has a safety boundary. Under the cited United States workplace rule, exposed live parts generally must be deenergized before work, a qualified person must verify the deenergized condition with test equipment, and work on energized parts is limited to qualified persons. Applicable requirements should be verified for the situation. This boundary does not supply a procedure for working on or testing a robot safety circuit; a continuity reading on an isolated component must not be treated as proof that the installed system is deenergized or safe.

### Related guides

- [aircraft door closed monitor micro switch NO and NC terminals](/guides/aircraft-door-closed-monitor-micro-switch-no-and-nc-terminals/)
- [access control door position micro switch function](/guides/access-control-door-position-micro-switch-function/)
- [ball screw actuator end of stroke micro switch contact rating](/guides/ball-screw-actuator-end-of-stroke-micro-switch-contact-rating/)
- [capping machine guard interlock micro switch actuator travel](/guides/capping-machine-guard-interlock-micro-switch-actuator-travel/)

## Separate the micro switch contacts from the guard and robot response

A guard, cam, or linkage may mechanically actuate a micro switch when that is how a particular interlock is designed. The switch’s contact change is one component behavior. What follows in the robot depends on the actual wiring and control design. Do not infer a particular stop, slowdown, alarm, or other response from the presence of the switch or from an NO or NC label.

The arrangement is design-specific. Some collaborative robot guard interlocks may use a micro switch, while others may not. Even where one is used, the contact arrangement and reference condition must come from the exact switch documentation. Do not generalize one switch’s terminal pattern or one guard’s mechanism to an entire equipment class.

Keep conclusions separate: markings or the switch diagram can identify documented terminals; an isolated continuity check can compare contact behavior with the documented table in a defined actuator state; neither establishes the installed circuit’s behavior or the robot’s safety response. For a **collaborative robot guard interlock micro switch NO and NC terminals**, the reliable interpretation is therefore bounded by the switch’s own documentation and by the distinction between component contacts and system logic.

## Sources and references

- Defense Logistics Agency ASSIST: [MIL-PRF-8805K: Switches and Switch Assemblies, Sensitive, Snap Action, General Specification For](https://quicksearch.dla.mil/qsDocDetails.aspx?ident_number=7196){: rel="nofollow noopener noreferrer" }
- Occupational Safety and Health Administration: [29 CFR 1910.333: Selection and Use of Work Practices](https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.333){: rel="nofollow noopener noreferrer" }
- Wikipedia: [Miniature snap-action switch](https://en.wikipedia.org/wiki/Miniature_snap-action_switch){: rel="nofollow noopener noreferrer" }
