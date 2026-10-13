---
title: "Laboratory centrifuge lid micro switch NO and NC terminals: what do they mean?"
description: "laboratory centrifuge lid micro switch NO and NC terminals: Understand the operating idea, essential terminology, practical checks, limitations, and."
date: 2026-10-13 00:00:00 +0800
publication_date_only: true
category: Applications
tags:
  - laboratory centrifuge lid micro switch NO and NC terminals
  - micro switches
  - Applications
author: editorial_team
---

A laboratory centrifuge lid micro switch NO and NC terminals describe contact states at a defined reference condition; they do not, by themselves, say what the centrifuge will do when its lid opens or closes. Identify the terminals from markings or reliable documentation for the exact switch, then interpret any contact check only for the isolated switch and a clearly specified actuator state. This separates what the component’s contacts do from how the centrifuge’s wiring and control logic use them.

A centrifuge lid mechanism may actuate a micro switch in some designs, but the presence and role of such a switch are design-specific. The terminal labels alone cannot establish the machine’s lid logic, operating permission, or safety.

## What do laboratory centrifuge lid micro switch NO and NC terminals mean?

NO and NC describe contact states relative to the switch’s documented reference actuator condition. They are not universal labels for lid-open and lid-closed states. The reference condition must come from reliable documentation for the particular switch or be otherwise specified for that design.

In a documented contact arrangement that includes COM, COM is the common terminal. NO and NC identify the other contact terminals in relation to that arrangement and its reference condition. Do not assume every micro switch has the same number of terminals or the same contact arrangement. If COM, NO, and NC are not documented for the specific switch, their physical positions cannot be safely inferred from a generic layout.

The labels describe the switch contacts, not the complete centrifuge circuit. A contact state does not reveal whether the equipment uses that contact to enable, inhibit, signal, or otherwise affect operation. Nor does NO or NC establish which state corresponds to an open lid or a closed lid. Those relationships depend on the particular mechanical design and circuit.

For identification, use the switch’s own terminal markings or reliable documentation that applies to the exact switch and equipment. A wiring diagram and the documented circuit function help place the component in context; permissible load information also matters to the circuit application. A generic physical-layout inference cannot substitute for those details. If the markings or documentation do not resolve the terminal identity, treat it as unknown rather than assigning labels based on terminal position, wire color, or an assumed centrifuge convention.

## How actuator state changes the micro switch contacts

The lid’s mechanical arrangement and the switch’s actuator are separate parts. In a design that uses a micro switch, some part of the lid mechanism may move the actuator. That mechanical relationship does not establish that every laboratory centrifuge uses a micro switch, or that lid closure produces a particular contact state.

For a switch with a snap-action mechanism, actuator movement can change the contact state. Interpret that change against the documented reference condition and the particular switch’s operating sequence. Do not equate the point at which contacts operate with the point at which they return. Operation and release are distinct events; the release force is the force or torque to which force on the actuator must be reduced to permit contacts to return to the unoperated position after operation. The definition clarifies that returning is a separate event, but it does not supply a force value or identify a lid position for a particular centrifuge.

A lid may press, release, or otherwise move an actuator depending on the design. Without documentation of that arrangement, it is not possible to say whether an open lid corresponds to the switch’s unoperated condition, whether a closed lid operates it, or which contact state the machine uses. The useful distinction is between the switch’s actuator condition and the lid’s position: the former is the reference for interpreting NO and NC, while the connection between the two must be established for the specific mechanism.

Likewise, an observed contact transition at the switch does not show how the centrifuge responds. The installed wiring, control logic, and other components determine that response. Do not convert a component-level state change into a claim that the machine is enabled, inhibited, or safe to operate.

## How to verify NO and NC on an isolated micro switch

Begin with markings or reliable documentation for the exact switch. Use them to identify the terminals and the specified reference actuator condition. Do not guess from physical position or wire color. If identification remains unresolved, a continuity reading without a reliable terminal map may not establish which contact is NO or NC.

A continuity check, if used, concerns the isolated switch rather than the installed centrifuge circuit. The switch must be disconnected from the surrounding circuit, and the actuator condition being checked must be defined. Compare the observed contact condition with the documentation for that switch and that state. A result in one actuator condition is only an observation for that condition; it does not establish every state or the behavior of the equipment. Use an appropriate measuring method, and do not treat an unspecified reading as a complete diagnosis.

A click may indicate movement of a snap mechanism, but it does not prove continuity, identify a terminal, confirm correct wiring, or establish suitability for the circuit. Similarly, an isolated continuity result does not show that the switch is correctly connected in the centrifuge or that the circuit behaves as intended. The test is bounded: it can help verify a documented contact state under a defined condition, not certify the installed system.

Keep the isolation and state conditions attached to the interpretation. A reading from a switch still connected to other circuit components is not the same as an isolated switch reading. A reading taken without specifying actuator state cannot be compared reliably with a reference state. If the switch cannot be isolated or the proper test conditions are unclear, do not infer a result from an ambiguous measurement.

### Related guides

- [accelerator pedal position stop micro switch actuator travel](/guides/accelerator-pedal-position-stop-micro-switch-actuator-travel/)
- [incinerator end of stroke micro switch maintenance](/guides/incinerator-end-of-stroke-micro-switch-maintenance/)
- [rotary indexing table guard interlock micro switch location](/guides/rotary-indexing-table-guard-interlock-micro-switch-location/)
- [security barrier open position micro switch wiring](/guides/security-barrier-open-position-micro-switch-wiring/)

## What terminal readings cannot tell you about a centrifuge lid

NO and NC labels, even when correctly identified, do not disclose the centrifuge’s control logic. They cannot establish whether the lid is considered open or closed by the equipment, whether operation is permitted, what an indicator or alarm will do, or whether the assembly is safe. The switch arrangement, wiring, other components, and equipment design determine those outcomes.

A discrepancy between a documented isolated contact state and an expected state may warrant further evaluation, but the terminal reading alone does not identify the cause. The issue could involve the mechanical input, the switch contacts, terminal identification, wiring, or another part of the equipment. Distinguishing among these possibilities requires evidence about the particular design and the installed circuit; do not collapse them into a single diagnosis.

The practical boundary is therefore component identification versus equipment-level interpretation. Use exact-switch documentation to identify terminals and understand the contact state at its stated actuator condition. Use equipment-specific documentation and qualified service evaluation for questions about lid logic, wiring, faults, or permission to operate. Do not infer a universal lid-closed state or bypass, defeat, or improvise a repair to an interlock from terminal labels or a continuity observation.

In short, laboratory centrifuge lid micro switch NO and NC terminals name contact states relative to a documented reference condition. They do not name universal lid positions or determine centrifuge behavior. A state-defined check on an isolated, correctly identified switch can verify only that limited contact observation; it cannot establish installed wiring correctness or equipment safety.

## Sources and references

- Defense Logistics Agency ASSIST: [MIL-PRF-8805K: Switches and Switch Assemblies, Sensitive, Snap Action, General Specification For](https://quicksearch.dla.mil/qsDocDetails.aspx?ident_number=7196){: rel="nofollow noopener noreferrer" }
- Occupational Safety and Health Administration: [29 CFR 1910.333: Selection and Use of Work Practices](https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.333){: rel="nofollow noopener noreferrer" }
