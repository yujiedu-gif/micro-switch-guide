---
title: "Rotary indexing table guard interlock micro switch NO and NC terminals"
description: "rotary indexing table guard interlock micro switch NO and NC terminals: Understand the operating idea, essential terminology, practical checks,."
date: 2026-10-13 09:00:00 +0800
category: Applications
tags:
  - rotary indexing table guard interlock micro switch NO and NC terminals
  - micro switches
  - Applications
author: editorial_team
---

A micro switch’s NO and NC labels describe contact states at a documented reference condition; they do not, by themselves, say whether a rotary indexing table guard is open or closed. The phrase “rotary indexing table guard interlock micro switch NO and NC terminals” therefore involves two separate questions: which contacts change state on the isolated switch, and what the equipment’s interlock circuit does with that change. The first may be checked using the exact switch documentation and an appropriate isolated test. The second requires the actual equipment circuit documentation and cannot be established by a continuity result alone.

## What NO and NC mean on a micro switch

NO means normally open, and NC means normally closed, with “normally” tied to the reference condition specified for that particular switch and its documentation. These labels describe the contact arrangement in that reference state. They do not define a machine condition, such as a guard being open, a guard being closed, or a table being ready to index.

A micro switch may change an electrical contact state in response to mechanical actuator movement. For a documented contact arrangement, NO and NC distinguish the contacts according to their state at the specified reference condition. When the actuator moves, the contact state may change as the design specifies. The labels alone do not establish the actuator’s position, the direction of its movement, or the point at which a particular contact changes state. Those details must come from documentation for the exact switch and equipment.

This distinction matters in a guard interlock. “Normally” in NO or NC is not a synonym for “guard normally open” or “guard normally closed.” A guard’s physical position is part of the host mechanism, while NO and NC describe switch contacts under a specified reference condition. To relate one to the other, the switch documentation must identify the reference condition and the equipment documentation must show how the guard or its linkage acts on the switch.

Do not infer a terminal’s identity from its physical position or from a familiar-looking layout. Use the connection diagram and terminal markings documented for the exact switch. If those do not establish the contact arrangement or reference condition, treat the identification as unresolved rather than assigning NO or NC by assumption.

## How a micro switch may be actuated by a rotary indexing table guard

Some equipment designs may use a micro switch as part of a guard interlock. In such an arrangement, the guard or a linkage may move the switch actuator as the guard moves. This is a conditional mechanical relationship, not a feature that can be assumed for every rotary indexing table or every guard design.

The mechanical direction also cannot be presumed. Depending on the documented arrangement, opening or closing a guard could move the actuator in either direction. Consequently, it is not valid to conclude from the words NO and NC alone which contact state corresponds to a guard-open or guard-closed condition. The switch’s reference condition and the actual relationship among guard, linkage, and actuator must be established from the relevant documentation.

Keep the component action separate from the machine’s control function. A switch contact changes state as specified by the switch design and actuation. The effect of that change on the interlock depends on the actual circuit and equipment design. The presence of a micro switch does not, by itself, establish that a guard is monitored in a particular way, that the table will stop, or that indexing will be prevented. Those outcomes are not properties of the NO or NC labels alone.

A concise way to frame the application is: first identify the switch contacts under the documented reference condition; then consult the equipment documentation to determine how the mechanism actuates them and how the circuit uses their states. Do not replace either step with an assumption about what a guard interlock usually does.

## Rotary indexing table guard interlock micro switch NO and NC terminals: identify contact states

Start with the connection diagram, terminal markings, and reference condition supplied for the exact switch and equipment. The documentation should establish which terminals correspond to the relevant contacts and what actuator condition defines the stated NO or NC reference. A generic physical-layout inference is not a substitute. If terminal names, contact arrangement, or reference condition are not documented, the evidence does not support a definite identification.

If documentation permits an isolated contact check, the switch must be tested separately from the installed circuit, with the applicable deenergization and qualification requirements followed. The test needs a defined actuator state and a meter method appropriate to the documented procedure. Compare the observed continuity or open condition with the contact state expected for that documented reference condition. A reading without a stated actuator condition or a clear reference is not enough to assign a terminal confidently.

The test is limited to the isolated switch and the tested state. It can help determine whether the documented contacts show the expected state under that condition, but it does not identify every possible cause of a machine symptom. An unexpected reading may leave questions about the test setup, terminal identification, switch condition, or the actuator state. It also does not establish how the installed equipment is wired or what its interlock logic will do.

Keep the record of the check specific: note the terminals as identified by documentation, the actuator state used, the applicable test method, and the observed contact state. Do not extend a result from one state to a different guard position unless the switch documentation establishes the relationship. If the required information or safe isolation is unavailable, the contact state remains unverified; do not proceed by guessing at terminals or wiring.

### Related guides

- [bottling machine home position micro switch location](/guides/bottling-machine-home-position-micro-switch-location/)
- [incinerator end of stroke micro switch maintenance](/guides/incinerator-end-of-stroke-micro-switch-maintenance/)
- [rotary indexing table guard interlock micro switch location](/guides/rotary-indexing-table-guard-interlock-micro-switch-location/)
- [security barrier open position micro switch wiring](/guides/security-barrier-open-position-micro-switch-wiring/)

## Why terminal state does not prove the interlock response

An isolated switch test answers a narrow question about contact state under a defined condition. It does not show how those contacts are connected in the installed machine, how other circuit elements affect the signal, or what response the control system assigns to a change. The actual circuit and equipment documentation determine that behavior. A continuity result alone therefore cannot establish that the guard interlock responds as intended or determine the machine’s safety status.

This boundary is especially important when interpreting a guard position. Even if the switch’s NO and NC contacts are correctly identified, the observed state does not independently prove that the guard is open or closed, that the table is stopped, or that a particular interlock response has occurred. Those conclusions require equipment-specific evidence beyond the isolated contact check.

For safety-related questions, use the applicable equipment documentation and have the installed system assessed by qualified personnel. Do not infer a safe response from a contact label, and do not use an isolated test as a basis for changing, bypassing, or repairing the interlock. This article does not establish a wiring design, compliance status, or the behavior of any particular table.

The practical decision boundary is straightforward: identify NO and NC only against the exact switch’s documented reference condition; verify contact state only under an appropriate isolated test with actuator state specified; and determine the machine’s interlock behavior from its actual circuit and equipment documentation. The phrase “rotary indexing table guard interlock micro switch NO and NC terminals” names a component-and-application context, not proof of a particular guard position or machine response.

## Sources and references

- Defense Logistics Agency ASSIST: [MIL-PRF-8805K: Switches and Switch Assemblies, Sensitive, Snap Action, General Specification For](https://quicksearch.dla.mil/qsDocDetails.aspx?ident_number=7196){: rel="nofollow noopener noreferrer" }
- Occupational Safety and Health Administration: [29 CFR 1910.333: Selection and Use of Work Practices](https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.333){: rel="nofollow noopener noreferrer" }
- Wikipedia: [Miniature snap-action switch](https://en.wikipedia.org/wiki/Miniature_snap-action_switch){: rel="nofollow noopener noreferrer" }
