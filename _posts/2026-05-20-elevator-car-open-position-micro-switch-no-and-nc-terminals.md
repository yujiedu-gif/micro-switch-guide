---
title: "elevator car open position micro switch NO and NC terminals"
description: "elevator car open position micro switch NO and NC terminals: Understand the operating idea, essential terminology, practical checks, limitations, and."
date: 2026-05-20 17:39:43 +0800
last_modified_at: 2026-10-13 11:46:37 +0800
category: Applications
tags:
  - elevator car open position micro switch NO and NC terminals
  - micro switches
  - Applications
author: editorial_team
---

An **elevator car open position micro switch NO and NC terminals** label describes contact states, not door positions. NO and NC refer to whether contacts are open or closed at a specified reference condition for the particular switch. The labels alone do not show whether an elevator car door is open, closed, or operating correctly. To connect a contact state with door position, the particular switch’s documentation and the elevator mechanism’s arrangement must establish how actuator movement corresponds to door movement.

That distinction matters because the switch is one component in a larger mechanical and electrical system. A contact change may be used by installed circuitry, but the terminal labels do not identify the wiring, controller interpretation, or resulting behavior. An isolated contact check can describe the switch under a defined test condition; it cannot establish the condition or safety of the installed elevator system.

## What elevator car open position micro switch NO and NC terminals mean

For a documented changeover contact, common, normally closed, and normally open may be used as terminal labels. NO and NC describe contact states relative to a specified reference condition for that contact arrangement. They are not shorthand for “door open” and “door closed.” The device’s exact markings or schematic control, so do not assume that every switch has the same terminal arrangement or that a label on one device defines another.

The reference condition is essential to interpreting the words “normally open” and “normally closed.” Without knowing the condition specified by the applicable documentation, the labels alone do not tell you the contact state at every actuator position. Nor do they establish which mechanical position the elevator calls open or closed. A switch might be actuated by a mechanism associated with a door, but that possibility does not identify the switch’s reference condition or the door position at which its contacts change.

Keep three questions separate: what contact arrangement the switch documentation specifies; what actuator state the switch is in; and what position the car door is in. NO and NC address contact states relative to the documented reference condition. The actuator state requires evidence about the switch and its movement. The door position requires evidence connecting that actuator movement to the car-door mechanism. A terminal label by itself answers none of the mechanical mapping question.

This page concerns a switch associated with an elevator car open position. It does not establish the arrangement of an elevator landing-door switch. Car-door and landing-door applications are distinct contexts, and a label or arrangement documented for one must not be transferred to the other without evidence. Likewise, a phrase such as “open position” identifies an intended position-detection role, but does not by itself document the contact state or the mechanical event that produces it.

## Relate the micro switch actuator state to the car door position

A mechanical part such as a door mechanism, cam, lever, or linkage may move a micro switch actuator. That describes a possible mechanical relationship, not a confirmed arrangement for a particular elevator. To say that a particular contact state corresponds to the car door being open, the evidence must connect the door’s movement to the switch actuator and specify the actuator state associated with the contact state.

The mapping therefore depends on two links. First, the installed mechanism must move the actuator in a documented way as the car door moves. Second, the switch documentation must identify the relevant contact state for the actuator condition being considered. If either link is unknown, the door position cannot be inferred from NO or NC alone. The switch may change state during the door’s movement, but the label does not locate that change in the door’s travel.

Do not infer which actuator state means that the car door is open. The supplied information does not identify a particular elevator, switch, linkage, reference condition, or point in door movement. It also does not establish whether the switch is operated directly by the door or through another mechanical part. Those details remain unresolved unless the applicable documentation or an authorized assessment supplies them.

This is why “open position micro switch” should not be treated as a complete state diagram. It may describe the intended role of a component, but it does not prove that one terminal is closed whenever the door is open, that the other terminal is closed whenever the door is closed, or that the contact changes at a specific point. Such statements require evidence for the specific switch and mechanism rather than interpretation of the component name.

The distinction also prevents a false transfer between car and landing doors. A landing-door switch may have its own mechanism and application-specific relationship to door position. Its terminal labels do not establish how a car-door switch behaves, and a car-door arrangement does not establish landing-door behavior. The question here is limited to the car door; landing-door states require their own documentation and should not be inferred from this discussion.

## Why terminal labels do not reveal elevator control behavior

A micro switch contact state is not the same thing as an elevator control-system state. Installed wiring connects components according to the actual circuit, and a controller interprets inputs according to the system design. The NO or NC marking does not disclose those connections or interpretations. It therefore cannot establish what the elevator will do when a contact changes state.

In particular, do not infer a stop, alarm, permission to move, door response, or safety function from the terminal names. Those outcomes depend on the actual installed circuit and elevator design, neither of which is specified by the labels. Even if the switch’s isolated contact state is known, that result does not show that the wiring is correct, that the controller receives the expected input, or that the elevator behaves as intended.

The same boundary applies to apparent agreement between a contact reading and a door position. Observing a door in one position and measuring a contact does not, by itself, establish the full system logic. It may describe the observed switch under that condition, but it does not prove the controller’s interpretation, behavior at other positions, or safe operation. A conclusion about the elevator requires system-specific evidence beyond terminal identification.

The component must also be distinguished from the surrounding equipment. A micro switch is an electromechanical component; the elevator door mechanism supplies its movement, and the installed control system determines how the electrical signal is used. Naming the application does not establish a particular switch design, wiring arrangement, or control response. Do not treat a generic terminal label as a complete description of the elevator installation.

### Related guides

- [bottling machine home position micro switch location](/guides/bottling-machine-home-position-micro-switch-location/)
- [incinerator end of stroke micro switch maintenance](/guides/incinerator-end-of-stroke-micro-switch-maintenance/)
- [rotary indexing table guard interlock micro switch location](/guides/rotary-indexing-table-guard-interlock-micro-switch-location/)
- [security barrier open position micro switch wiring](/guides/security-barrier-open-position-micro-switch-wiring/)

## What a contact-state check can and cannot establish

A contact-state check is meaningful only when the switch is isolated from the installed circuit, the actuator condition is defined, and the expected contact behavior comes from the applicable switch documentation. Under those conditions, a check can help describe the isolated switch’s contacts at that actuator condition. It cannot establish how the elevator circuit is wired or interpreted, whether the mechanical linkage maps correctly to door position, or whether the elevator is safe to operate.

The available evidence does not provide a model-specific test procedure, expected readings for a particular actuator position, or a mapping between actuator travel and car-door position. Do not fill those gaps by assuming that NO must be open or NC must be closed in an unspecified test state. First identify the exact switch documentation and its reference condition. If that information is unavailable, the terminal names alone are insufficient to define an expected result.

Electrical work has a separate boundary. Under the cited United States workplace rule, exposed live parts generally must be deenergized before work; a qualified person must verify the deenergized condition with test equipment; and work on energized parts is limited to qualified persons. Verify all applicable requirements. This general boundary does not provide an elevator-specific inspection or repair procedure.

An isolated reading is not a diagnosis of the installed elevator. If the question concerns wiring, control logic, door behavior, or safe operation, those matters require assessment of the actual elevator system by qualified personnel. Do not use a terminal label or a single contact reading as proof that the car door is open, that the elevator’s control input is correct, or that the system is safe.

The practical conclusion is narrow: **elevator car open position micro switch NO and NC terminals** identify contact states only relative to the specified reference condition for the documented contact arrangement. They do not, by themselves, identify the car-door position. That relationship requires evidence linking the actuator to the car-door mechanism, while any conclusion about installed behavior requires evidence about the elevator’s wiring and control system.

## Sources and references

- Defense Logistics Agency ASSIST: [MIL-PRF-8805K: Switches and Switch Assemblies, Sensitive, Snap Action, General Specification For](https://quicksearch.dla.mil/qsDocDetails.aspx?ident_number=7196){: rel="nofollow noopener noreferrer" }
- Occupational Safety and Health Administration: [29 CFR 1910.333: Selection and Use of Work Practices](https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.333){: rel="nofollow noopener noreferrer" }
- Wikipedia: [Miniature snap-action switch](https://en.wikipedia.org/wiki/Miniature_snap-action_switch){: rel="nofollow noopener noreferrer" }
