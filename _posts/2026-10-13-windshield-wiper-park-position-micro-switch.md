---
title: "How a windshield wiper park position micro switch signals park"
description: "windshield wiper park position micro switch: Understand the operating idea, essential terminology, practical checks, limitations, and evidence needed for."
date: 2026-10-13 11:27:16 +0800
category: Applications
tags:
  - windshield wiper park position micro switch
  - micro switches
  - Applications
author: editorial_team
---

A windshield wiper park position micro switch, in a system designed to use one, provides a change in electrical contact state associated with a position in the wiper mechanism. It does not move the wiper blades or determine the system’s control logic by itself. Instead, mechanical movement can operate the switch, and the surrounding circuit interprets the resulting state according to that system’s design.

The switch must therefore be understood as one component in a chain: movement of the wiper mechanism, movement of the switch actuator, a contact-state change, and interpretation by the circuit. The exact mechanism, contact arrangement, and resulting park behavior cannot be established from the presence of a micro switch alone.

## What a windshield wiper park position micro switch does

A micro switch is an electromechanical component whose contacts change state when its actuator is moved. In a windshield wiper system that uses one for park-position signaling, the switch provides a contact-state change associated with a defined position of the wiper mechanism. That signal is an input to the host system; it is not the wiper system as a whole.

The motor supplies motion to the wiper mechanism, while the linkage transfers that motion toward the blades. A controller or other circuit may use a switch’s contact state as part of its operation. These roles are distinct: the switch reports a condition through its contacts, while the motor, linkage, blades, and control circuit have separate functions. The precise way they interact depends on the system design.

“Park position” describes a position or condition recognized by the particular system. The switch’s operation can be associated with such a condition, but the phrase does not establish a universal blade location or stopping sequence. Nor does it mean that the switch itself stops the motor. Whether a contact-state change leads to a particular motor response depends on how the actual circuit is arranged and interpreted.

This distinction matters because a component’s signal is not the same as the system action that follows it. A contact-state change may convey information about mechanism position, but the signal’s meaning and effect belong to the host design. Without evidence about that design, the switch’s role can be described only at this general level.

## How the wiper mechanism actuates the micro switch

A system may use a cam, linkage, or another mechanical feature to move the switch actuator as the wiper mechanism moves. These are possible arrangements, not a claim that every windshield wiper system uses a cam or a particular linkage shape. The mechanism’s movement provides the physical input; the actuator is the part of the switch moved by that input.

The causal sequence is mechanical. As the wiper mechanism changes position, a part of it may contact or otherwise move the switch actuator. Actuator movement can then operate the switch and change the contact state. The position at which this occurs depends on the particular mechanical arrangement and switch design. The switch does not independently measure the blades’ location; its operation reflects the mechanical input it receives.

A switch specification may define overtravel as “the distance or angle between the operating position and the extreme position to which the actuator may be moved.” That definition describes actuator movement after the operating position within the specified context. It does not identify a windshield wiper’s park position, establish the switch’s operating point in a particular assembly, or explain how the linkage is shaped.

The mechanical association between switch operation and a wiper position is therefore design-specific. A switch may be positioned so that its actuator moves at a selected point in the mechanism’s motion, but the available evidence does not establish where that point is, how it is set, or whether it corresponds to a blade endpoint. Those details cannot be inferred from the component name.

## How the park signal relates to the wiper control circuit

Once mechanical input operates the switch, the contact-state change becomes an electrical input to the surrounding circuit. A controller or circuit may interpret that input as part of its wiper operation. The switch supplies the contact change; it does not, by itself, define what the circuit does with it.

The complete path has separate stages. First, the wiper mechanism reaches a position that moves the actuator. Second, the switch contacts change state. Third, the host circuit responds according to its own design. The switch’s mechanical action can explain how a signal originates, but it does not reveal the circuit’s interpretation or the motor’s resulting behavior.

For that reason, it is not justified to conclude from the switch alone that the motor will stop, continue, or behave in any other particular way when the contacts change. Nor can the switch alone establish that the blades will stop at a particular location. The outcome depends on the mechanism and circuit together, including how the system uses the contact state. Those design details are not established by a general explanation of a micro switch.

The distinction also prevents a common conceptual error: treating a park-position switch as though it were the controller. A switch can provide a signal associated with mechanism position, while the circuit determines whether and how that signal affects operation. Describing the switch as a signal source does not imply a particular control sequence, contact state, or motor response.

### Related guides

- [aircraft door closed monitor micro switch NO and NC terminals](/guides/aircraft-door-closed-monitor-micro-switch-no-and-nc-terminals/)
- [access control door position micro switch function](/guides/access-control-door-position-micro-switch-function/)
- [ball screw actuator end of stroke micro switch contact rating](/guides/ball-screw-actuator-end-of-stroke-micro-switch-contact-rating/)
- [capping machine guard interlock micro switch actuator travel](/guides/capping-machine-guard-interlock-micro-switch-actuator-travel/)

## Why park behavior varies between designs

Windshield wiper systems do not all use a micro switch in the same way, and some may not use one at all. Where a micro switch is present, its function depends on how the mechanical parts move its actuator and how the electrical circuit uses the resulting contact state. A general component description cannot identify the arrangement in a particular system.

The contact arrangement is design-dependent. The presence of a switch does not establish which contacts are used, what state they occupy at a particular wiper position, or how those contacts connect to the rest of the circuit. It also does not establish the system’s normal state or wiring. Those facts require evidence about the specific design and should not be inferred from the label “park switch” or from the switch’s physical presence.

Mechanical position and control logic are separate variables as well. A switch might be actuated by a cam or linkage, but that fact alone would not establish the exact blade position at actuation. Likewise, knowing that a contact state changes at a mechanism position would not show what the controller does next. The mechanical relationship and circuit response must both be understood before describing a system’s particular parking behavior.

The reliable general conclusion is limited: in designs that use a windshield wiper park position micro switch for this purpose, movement of the wiper mechanism can move the switch actuator, changing the contacts and providing a signal for the host circuit to interpret. The switch is not the motor, linkage, or controller, and its presence alone does not prove a particular normal state, wiring arrangement, or blade-stopping behavior.

## Sources and references

- Defense Logistics Agency ASSIST: [MIL-PRF-8805K: Switches and Switch Assemblies, Sensitive, Snap Action, General Specification For](https://quicksearch.dla.mil/qsDocDetails.aspx?ident_number=7196){: rel="nofollow noopener noreferrer" }
