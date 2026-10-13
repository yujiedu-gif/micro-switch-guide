---
title: "Dental chair position micro switch NO and NC terminals: what do they mean?"
description: "dental chair position micro switch NO and NC terminals: Understand the operating idea, essential terminology, practical checks, limitations, and evidence."
date: 2026-10-13 09:00:00 +0800
category: Applications
tags:
  - dental chair position micro switch NO and NC terminals
  - micro switches
  - Applications
author: editorial_team
---

The **dental chair position micro switch NO and NC terminals** can be identified only from evidence for the particular switch, such as its own markings or documentation. NO and NC describe contact states at a specified reference condition; they do not, by themselves, identify a chair position or explain what the chair’s controls will do. A dental chair may use a micro switch as part of a mechanism, but not every position sensor or control device is a micro switch.

Keep two questions separate: which terminals the component documentation identifies, and how the chair’s actual circuit uses them. An isolated continuity check can address the switch in a defined actuator state only when its test method and expected behavior are known. It cannot establish installed-circuit safety or prove how the chair operates.

## dental chair position micro switch NO and NC terminals

NO means normally open, and NC means normally closed, relative to the particular switch’s documented reference condition and contact arrangement. These labels describe contact states at that reference condition. They do not mean that a chair is necessarily in a particular position, that a control is in a particular mode, or that the equipment is safe or ready to move.

The reference condition matters. A label must be interpreted using the condition specified for that switch, not an assumed chair position or an informal idea of what “normal” means in the host equipment. The chair’s mechanism might hold an actuator in one state at rest, move it during travel, or use a different arrangement. Without documentation for the component and design, those details remain unknown.

COM means common when that terminal is part of the documented contact arrangement. Do not assume a switch has a COM terminal, or assign a terminal that name, unless its markings or documentation support that identification. Likewise, do not assume that every switch has the same number of terminals or the same physical layout.

These distinctions keep component terminology from being mistaken for system behavior. NO and NC identify documented contact states; they do not establish which state the chair’s control logic treats as a position signal, interlock, or command. That interpretation requires evidence about the actual circuit and design.

## Identify the terminals on the particular micro switch

Start with the terminal markings on the particular switch or its documentation. Use those sources to map terminal names to the contact arrangement, and use the stated reference condition when interpreting NO or NC. A generic drawing or a terminal’s apparent physical location is not enough to establish its identity on an undocumented device.

If the component documentation is unavailable, incomplete, or unclear, leave the terminal mapping unresolved. Do not infer it from a familiar-looking package, the way wires are arranged on the chair, or a diagram for another switch. The physical arrangement and the chair’s wiring do not replace evidence that identifies the terminals on this specific component.

A wiring diagram can be relevant, but it should be the diagram for the exact switch and equipment, and it should be read alongside the terminal markings, circuit function, and permissible load documented for that switch and equipment. A generic layout cannot establish that those details apply. Where the documentation does not settle terminal identity or the reference condition, the correct conclusion is that the mapping is unknown, not that a likely arrangement has been confirmed.

Identification is also distinct from interpretation. Even if a marking identifies an NO contact at the specified reference condition, that fact alone does not say what an open or closed contact causes in the chair. The circuit may use the contact in a way that cannot be inferred from the label. Avoid extending a component-level identification into an unsupported claim about chair logic.

## Relate chair movement to the micro switch actuator cautiously

If a particular chair design uses a micro switch, a position-related linkage or other mechanism may move the switch actuator. The actuator is the part moved by that external mechanism. This describes a possible mechanical relationship, not a confirmed arrangement for every dental chair or every position-sensing device.

The switch’s documented contact state and the chair’s physical position are separate facts. A mechanism may actuate the switch as the chair moves, but the effect of the resulting contact change depends on the actual circuit and design. NO and NC labels alone do not show whether a contact is used to indicate position, enable an action, interrupt a control path, or serve another function. They also do not establish a particular interlock, motion response, or safe state.

For that reason, do not map “normally open” directly to “chair up,” “chair down,” or any other position without specific design evidence. Nor should a change in contact state be treated as proof that the chair’s control system responds as expected. Component documentation can identify a contact; it cannot, by itself, explain the surrounding equipment’s logic.

This boundary is important when interpreting symptoms. A chair that does not respond as expected could involve the mechanical input, the switch, terminal identification, wiring, or another part of the equipment. The NO/NC names do not distinguish among those possibilities. Establishing the switch’s documented identity is a component-level step, not a diagnosis of the chair.

### Related guides

- [bottling machine home position micro switch location](/guides/bottling-machine-home-position-micro-switch-location/)
- [incinerator end of stroke micro switch maintenance](/guides/incinerator-end-of-stroke-micro-switch-maintenance/)
- [rotary indexing table guard interlock micro switch location](/guides/rotary-indexing-table-guard-interlock-micro-switch-location/)
- [security barrier open position micro switch wiring](/guides/security-barrier-open-position-micro-switch-wiring/)

## What an isolated continuity check can verify

A continuity check is meaningful only when the particular switch’s test method and expected contact behavior are documented. If they are, the check must concern the isolated switch, use a defined actuator state, and compare the reading with the expected result for that documented state. Do not substitute an assumed chair position for the specified actuator condition.

The test interpretation is limited to the tested switch and state. A matching reading can support the expected contact behavior under that check; it does not prove the switch is suitable for the chair’s load, establish the wiring, demonstrate that the installed circuit is safe, or confirm complete chair operation. A reading that differs from the documented expectation likewise does not, by itself, identify the cause. Terminal mapping, actuator condition, measurement method, or another issue may remain unresolved.

A click or other audible movement is not a continuity result. It does not establish which terminals are involved, whether the documented contacts have the expected electrical state, or how the chair’s circuit responds. Keep mechanical observation separate from electrical verification.

If the switch’s expected behavior or test method is not documented, do not invent one. Likewise, a test of an installed circuit is not equivalent to a test of an isolated switch. The component’s labels and an isolated reading cannot establish installed-circuit safety or the chair’s control behavior. For a **dental chair position micro switch NO and NC terminals**, the defensible conclusion is limited to what the particular switch’s documentation, markings, and properly bounded component check establish; the chair’s behavior remains a separate question of its actual design and circuit.

## Sources and references

- Defense Logistics Agency ASSIST: [MIL-PRF-8805K: Switches and Switch Assemblies, Sensitive, Snap Action, General Specification For](https://quicksearch.dla.mil/qsDocDetails.aspx?ident_number=7196){: rel="nofollow noopener noreferrer" }
- Occupational Safety and Health Administration: [29 CFR 1910.333: Selection and Use of Work Practices](https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.333){: rel="nofollow noopener noreferrer" }
