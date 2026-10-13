---
title: "How Do Material Feeder Home Position Micro Switch NO and NC Terminals Relate?"
description: "material feeder home position micro switch NO and NC terminals: Understand the operating idea, essential terminology, practical checks, limitations, and."
date: 2026-05-16 20:44:13 +0800
last_modified_at: 2026-10-13 11:46:37 +0800
category: Applications
tags:
  - material feeder home position micro switch NO and NC terminals
  - micro switches
  - Applications
author: editorial_team
---

A material feeder home position micro switch NO and NC terminals describe contact behavior under a specified reference condition; they do not, by themselves, identify whether the feeder is at home. To interpret a terminal state, establish how the feeder mechanism moves the switch actuator, which actuator position represents feeder home, and how the circuit uses the resulting contact state. The micro switch is one component in that chain, not the feeder’s complete sensing or control system.

## How Do material feeder home position micro switch NO and NC terminals Relate?

The feeder’s physical home position, the micro switch actuator’s position, the switch’s contact state, and the controller’s interpretation are related but distinct facts. A documented mechanism may move the actuator as the feeder reaches a designated position. The actuator movement may then change a contact state in a switch design that supports that operation. A circuit can use that state as an input, but the meaning assigned to the input depends on the actual wiring and control logic.

Accordingly, a label such as NO or NC is not a direct home-position indicator. It does not establish that the feeder is home, that a controller recognizes home, or that the machine will take any particular action. Those conclusions require documentation for the particular switch and feeder arrangement.

## Trace the feeder’s home position to the micro switch actuator

Start with the mechanical relationship. A feeder mechanism may use a linkage or another arrangement to move the micro switch actuator as a part reaches a designated position. Whether that occurs, and which actuator position corresponds to the feeder’s home position, must be established from the relevant equipment documentation. The same general idea does not prove that every feeder uses this arrangement.

Keep three observations separate:

- **Feeder position:** the physical position designated as home by the feeder’s documentation.
- **Actuator position:** the position of the switch’s actuator when the feeder mechanism acts on it.
- **Contact state:** the electrical relationship of the documented switch contacts at that actuator position.

The sequence matters. A feeder can be physically near its designated position without the available information establishing that the actuator has reached a particular position. Likewise, knowing an actuator position does not establish the contact state unless the switch’s reference condition and contact arrangement are known. Do not infer precise actuator travel or a switching point from the name of the feeder position. For a documented switch, pretravel runs from the free position to the operating position, while overtravel runs from the operating position to the extreme permitted actuator position; those terms describe actuator motion, not the feeder controller’s definition of home.

Only after the mechanical relationship and switch behavior are documented can the contact change be considered as a possible home-position signal. That still leaves the circuit’s interpretation to establish.

## Interpret NO and NC only at the stated reference condition

NO and NC describe contact state relative to a specified reference condition. The reference condition is essential: a label without that condition does not say what the contacts are doing at an arbitrary actuator position. If the particular contact arrangement documents a common terminal, COM means common; do not assume a COM terminal exists or infer its location from a generic layout.

In a design with documented snap action, actuator movement may change the contact state. That general mechanism does not establish which contact is connected in a particular feeder, which state corresponds to home, or whether the controller interprets the state as a home signal. Those details depend on the switch’s documented terminal identification, actuator position, and the feeder circuit.

Terminal names also do not, by themselves, establish current flow through an installed circuit. The connection diagram, terminal markings, circuit function, and permissible load documented for the exact switch and equipment are the relevant boundaries. Avoid transferring a state description into a claim about controller response without the circuit information that connects them.

## Follow the contact change through the feeder control circuit

A contact state becomes meaningful to the feeder only through the circuit that uses it. The applicable wiring or control documentation must identify which switch contacts are connected and how the control system interprets their states. One design could assign a particular contact state to a home-position input; another circuit could use a contact differently. The terminal labels alone do not distinguish those possibilities.

This is why the same NO or NC label cannot be translated universally as “at home” or “not at home.” The label concerns the contact at its specified reference condition. The feeder’s mechanical arrangement determines actuator position, and the control logic determines what an input state means to the system. Each link must be documented before stating the overall meaning.

Do not infer an alarm, stop, motion command, or other response from the presence of a micro switch. Such behavior belongs to the feeder’s particular control design, not to the terminal name itself. If the available documentation does not establish the switch-to-controller connection or the logic assigned to it, the control response remains unresolved.

### Related guides

- [bottling machine home position micro switch location](/guides/bottling-machine-home-position-micro-switch-location/)
- [incinerator end of stroke micro switch maintenance](/guides/incinerator-end-of-stroke-micro-switch-maintenance/)
- [rotary indexing table guard interlock micro switch location](/guides/rotary-indexing-table-guard-interlock-micro-switch-location/)
- [security barrier open position micro switch wiring](/guides/security-barrier-open-position-micro-switch-wiring/)

## What must be verified before calling a terminal state “home”?

A bounded interpretation requires evidence for each link in the chain:

1. **Identify the switch and terminals.** Use applicable documentation and markings for the exact switch and equipment. Do not rely on physical layout alone; terminal identification and permissible load should come from the documented connection information.
2. **Establish the mechanical reference.** Determine which feeder position is designated home and what actuator position the mechanism produces there, if the arrangement is documented.
3. **Establish the contact reference.** Determine the specified reference condition for the NO and NC labels and identify COM only if it is documented in the actual contact arrangement.
4. **Establish the circuit interpretation.** Consult the feeder wiring or control documentation to determine which contact is used and what the control system assigns to its state.

If a continuity check is supported by the applicable documentation, interpret it only as a check of an isolated switch in a defined actuator state against a specified expected result. A switch-only reading does not establish the installed circuit’s wiring, controller interpretation, or overall safety. Insulation resistance is a separate test concept: under the cited standard’s scope, it is evaluated between specified electrically isolated points using the applicable test method and conditions. It is not a substitute for establishing the feeder’s home-position logic.

The decision boundary is straightforward: call a contact state “home” only when the documented mechanical position, actuator condition, terminal behavior, and circuit interpretation support that meaning. Without those links, NO and NC identify contact terminology, not the feeder’s home state. The material feeder home position micro switch NO and NC terminals cannot establish that state by labels alone.

## Sources and references

- Defense Logistics Agency ASSIST: [MIL-PRF-8805K: Switches and Switch Assemblies, Sensitive, Snap Action, General Specification For](https://quicksearch.dla.mil/qsDocDetails.aspx?ident_number=7196){: rel="nofollow noopener noreferrer" }
- Occupational Safety and Health Administration: [29 CFR 1910.333: Selection and Use of Work Practices](https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.333){: rel="nofollow noopener noreferrer" }
