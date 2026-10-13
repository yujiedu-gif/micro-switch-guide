---
title: "Material feeder travel limit micro switch NO and NC terminals"
description: "material feeder travel limit micro switch NO and NC terminals: Understand the operating idea, essential terminology, practical checks, limitations, and."
date: 2026-10-13 09:00:00 +0800
category: Applications
tags:
  - material feeder travel limit micro switch NO and NC terminals
  - micro switches
  - Applications
author: editorial_team
---

A **material feeder travel limit micro switch NO and NC terminals** are named by the contacts’ states in the switch’s documented, unactuated reference condition. NO means normally open in that condition; NC means normally closed. When feeder movement shifts the switch actuator, the contact state may change, but the terminal labels alone do not establish how the feeder controller responds or whether the feeder stops.

The distinction is between a component-level state and an equipment-level result. A micro switch’s actuator and contacts provide a mechanical input and electrical contact change. The installed wiring and control design determine what that change means for feeder operation. The following sections explain that boundary and describe what can, and cannot, be established through verification.

## Material feeder travel limit micro switch NO and NC terminals: what the labels mean

Normally open and normally closed describe contact states relative to the documented, unactuated reference condition. In that reference condition, the NO contact is open and the NC contact is closed. These terms name the contacts; they do not by themselves promise that a particular feeder circuit is energized, deenergized, or in a particular operating state.

Use the reference condition supplied for the particular switch. Do not assume that a feeder’s usual position, a travel-limit position, or a controller’s normal state is the same as the switch’s unactuated reference condition. The reference is about the switch’s actuator and contact arrangement, not a general description of the host equipment.

If the contact arrangement is documented, COM means common, with NO and NC identifying the corresponding contacts relative to that reference condition. If the terminal arrangement is not documented, do not infer that the switch has COM, NO, and NC terminals or assign terminal identities from appearance alone. The labels must be tied to the actual documented arrangement.

Actuation relates the reference state to another switch state. When an external mechanism moves the actuator, the switch mechanism can change the contact state. That does not make “normally open” mean “open whenever the feeder is running,” or “normally closed” mean “closed whenever the feeder is stopped.” Those equipment-level descriptions require verified information about how the switch is mounted, what moves it, and how its contacts are used in the circuit.

A contact-state label is therefore a limited but useful description: it identifies a contact in a stated switch condition. To understand a material feeder travel limit, follow the mechanical movement to the actuator, then distinguish the switch’s contact change from the controller’s interpretation of that change.

## How feeder travel actuates the micro switch

At a travel limit, a feeder mechanism may move an external part that contacts or otherwise moves the micro switch actuator. The causal sequence is feeder movement, movement of the external mechanism, actuator movement, and a resulting change in the switch’s contact state. The exact arrangement is design-specific; the labels alone do not identify the part that contacts the actuator or the direction of movement that operates it.

The actuator is the part moved by the external mechanism. Its movement can operate the switch contacts, but the switch’s travel requirements are not established by the general component category. Numerical travel limits are specific to the applicable specification sheet and must not be inferred from the term “micro switch.” Where travel is relevant, check the applicable specification sheet rather than assuming a feeder can move the actuator by a particular amount.

Pretravel runs from the free position to the operating position. Overtravel runs from the operating position to the extreme permitted actuator position. These describe portions of actuator travel, not the distance a feeder should travel or a controller’s programmed stopping point. The distinction matters because feeder movement, linkage movement, and actuator movement are not interchangeable measurements. No conversion among them can be assumed without design-specific information.

The micro switch’s contact change is also distinct from the feeder controller’s response. The switch may provide a contact change to a connected circuit, but the actual wiring and control design determine whether that change is interpreted as a limit indication, a command, or something else. Do not infer that the feeder must stop, reverse, alarm, or continue moving merely because an NO or NC contact is used.

This separates two questions that can otherwise be conflated: what contact state the switch has under a defined actuator condition, and what the feeder does after the installed circuit receives that state. The first depends on the switch’s documented contact arrangement and actuator condition. The second depends on the particular wiring and controller design.

## What NO and NC labels do not tell you about the feeder

NO and NC labels do not identify which terminals are connected in the installed feeder circuit. They do not establish how the switch is mounted, which feeder position corresponds to its unactuated reference condition, or whether the mechanism moves the actuator at the intended travel limit. Those facts require information about the particular switch installation and feeder design.

The labels also do not disclose the controller logic. A contact-state change could be used in different ways by different circuits. Without verified circuit documentation, it is not possible to conclude from the terminal names alone that the feeder will stop, reverse, generate an alarm, or take any other action. Even a documented switch contact state does not, on its own, establish the behavior of the wider assembly.

Nor do the labels establish whether a switch is suitable for a particular electrical load. Use only the rating explicitly stated for the applicable current type, load, and test condition. An AC rating does not establish a DC rating, and a rating for one load or test condition does not establish another. NO and NC describe contact states, not electrical ratings or compatibility with the feeder circuit.

Likewise, a contact label cannot establish that the installed wiring is correct or safe. Terminal identification, wiring, control logic, and the switch’s mechanical action are separate facts to verify. Keep conclusions conditional until the applicable documentation and installation details are known. If those details are missing or conflict, the contact labels alone cannot resolve the uncertainty.

### Related guides

- [bottling machine home position micro switch location](/guides/bottling-machine-home-position-micro-switch-location/)
- [incinerator end of stroke micro switch maintenance](/guides/incinerator-end-of-stroke-micro-switch-maintenance/)
- [rotary indexing table guard interlock micro switch location](/guides/rotary-indexing-table-guard-interlock-micro-switch-location/)
- [security barrier open position micro switch wiring](/guides/security-barrier-open-position-micro-switch-wiring/)

## How to verify the micro switch contact state safely

A contact-state check must be tied to a defined switch condition and a suitable verification procedure. The available information here does not specify a measuring method or expected meter readings for an isolated switch, so no particular continuity-test procedure or result can be stated. Do not treat a click or actuator movement alone as proof of electrical continuity, correct wiring, or feeder operation.

An isolated switch reading, if obtained under an appropriate documented procedure, concerns that switch in the tested actuator state. It does not establish that the switch is correctly installed, that the feeder wiring matches the circuit design, or that the controller responds as intended. Nor does it prove that the complete feeder assembly is functioning correctly. A result should not be extended beyond the condition actually tested.

Electrical work has a separate safety boundary. Under the cited United States workplace rule, exposed live parts generally must be deenergized before work; a qualified person must verify the deenergized condition with test equipment; and work on energized parts is limited to qualified persons. Verify all applicable requirements. Do not use terminal labels or an isolated contact reading as evidence that an installed circuit is safe to work on.

If the reference condition, terminal arrangement, wiring, or expected control response is not documented, the unresolved point remains unresolved. Use applicable switch and feeder documentation to establish component and circuit details. Leave energized-circuit investigation and wiring questions outside the defined verification procedure to qualified personnel. The firm conclusion is limited: NO and NC name contact states relative to the documented unactuated reference condition; they do not, by themselves, specify what the material feeder will do.

This concludes the explanation of material feeder travel limit micro switch NO and NC terminals.

## Sources and references

- Defense Logistics Agency ASSIST: [MIL-PRF-8805K: Switches and Switch Assemblies, Sensitive, Snap Action, General Specification For](https://quicksearch.dla.mil/qsDocDetails.aspx?ident_number=7196){: rel="nofollow noopener noreferrer" }
- Occupational Safety and Health Administration: [29 CFR 1910.333: Selection and Use of Work Practices](https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.333){: rel="nofollow noopener noreferrer" }
