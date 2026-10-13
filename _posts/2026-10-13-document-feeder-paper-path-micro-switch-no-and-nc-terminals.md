---
title: "document feeder paper path micro switch NO and NC terminals"
description: "document feeder paper path micro switch NO and NC terminals: Understand the operating idea, essential terminology, practical checks, limitations, and."
date: 2026-10-13 11:27:16 +0800
category: Applications
tags:
  - document feeder paper path micro switch NO and NC terminals
  - micro switches
  - Applications
author: editorial_team
---

A **document feeder paper path micro switch NO and NC terminals** question has two parts: what the terminal labels mean on the specific switch, and what the feeder does with the resulting contact change. NO and NC describe contact states relative to a documented reference condition and actuator state. They do not, by themselves, identify a paper-present, paper-absent, or jam condition. The feeder’s wiring and control logic determine how a contact transition is interpreted.

The switch’s connection diagram and markings are the starting point. A generic changeover contact may have common, normally closed, and normally open terminals, but not every switch or feeder arrangement should be assumed to use that configuration. For a check, isolate the switch from its circuit, establish the actuator state being tested, and compare the observed continuity with the exact switch documentation. That check describes the isolated contacts, not the complete feeder.

## What NO and NC mean on a document feeder paper path micro switch NO and NC terminals

NO means “normally open,” and NC means “normally closed,” but “normally” is meaningful only relative to the reference condition specified for the particular switch and its actuator. These labels describe contact states at that reference condition. They do not name the feeder’s normal paper condition, the switch’s location in the paper path, or the result that the feeder will produce.

If the documented device has a changeover contact, COM is the common terminal, while NO and NC identify the two contact paths in relation to the documented reference state. The exact terminal markings or schematic control; a generic terminal layout is not enough to identify a particular device. Do not infer which physical terminal is COM, NO, or NC from its position, shape, or apparent similarity to another switch.

Actuator movement can change a micro switch’s electrical contact state. To describe that transition accurately, first establish the reference condition and the actuator state to which the documentation assigns the terminal labels. Then describe the contact paths in those states using the documented terminal arrangement. A label alone does not establish which actuator position is being called normal, and an assumed paper-path position cannot substitute for that reference.

This distinction matters because “normally open” is not a synonym for “paper absent,” and “normally closed” is not a synonym for “paper present.” Either mapping would require evidence about the specific mechanism and circuit. The terminal labels identify contact behavior under a defined reference condition; the document feeder’s interpretation is a separate question.

## How the micro switch relates to paper-path sensing

A miniature snap-action switch can change an electrical contact state in response to mechanical actuator movement and is commonly used for position or limit detection. In a feeder arrangement that uses one, a paper-path mechanism or another moving part may move the actuator when it reaches a defined position. The switch then provides a contact transition to the surrounding circuit. That describes a possible component relationship, not a claim that every document feeder contains a micro switch or uses the same arrangement.

Keep the causal steps separate: a mechanical part moves; the actuator responds; the switch contacts change state; and the feeder’s circuit or control logic interprets the resulting signal. The terminal labels describe the contact paths at the documented reference condition. They do not specify what the control logic considers paper present, paper absent, or a jam, nor whether the logic stops motion, continues operation, or signals an error.

Document feeder designs vary. A particular design may use a micro switch for a position or limit signal, may use a different sensing arrangement, or may not use a micro switch. Confirm the presence, placement, contact arrangement, and mechanical relationship from evidence for that specific design. Do not generalize from the fact that a switch is commonly used for position or limit detection to a claim about all feeders.

The distinction also prevents a misleading shortcut: seeing a switch near a paper path does not establish what it senses. Its actuator may be moved by a feeder part, but the part’s role and the electrical meaning of the resulting transition depend on the actual design. Without that design-specific information, the contact change can be described, but its paper-state meaning remains unresolved.

## How to verify NO and NC contacts on an isolated switch

A continuity check is meaningful only when the switch is isolated from the circuit and the actuator state being tested is defined. First consult the exact switch documentation to identify the terminals and the stated reference condition. Then record the actuator state for the check, such as the documented reference state or a documented actuated state. Compare the continuity observations between the documented terminals with the expected contact arrangement in that state.

Do not treat a generic physical layout as a substitute for the connection diagram or terminal markings. If the device documentation does not establish its terminal arrangement or reference condition, the labels cannot be verified reliably by assumption. The evidence available here does not specify a meter setting, numerical reading, or model-specific test sequence; those details remain dependent on the exact switch and its documentation.

The check is limited to the isolated switch and the defined actuator state. It does not establish that installed wiring is correct, that a feeder circuit interprets the contact as intended, or that the complete feeder is functioning properly. An isolated contact result also does not establish electrical suitability for a feeder load. Use the permissible load and circuit function documented for the exact switch and equipment rather than inferring suitability from NO, NC, or COM labels.

A click may indicate movement of a snap mechanism, but it does not prove continuity, correct terminal identification, correct wiring, or suitability for a load. Likewise, a continuity observation in one actuator state does not establish the result in another state or explain the feeder’s behavior. Keep the tested terminals and actuator state attached to any conclusion.

### Related guides

- [bottling machine home position micro switch location](/guides/bottling-machine-home-position-micro-switch-location/)
- [incinerator end of stroke micro switch maintenance](/guides/incinerator-end-of-stroke-micro-switch-maintenance/)
- [rotary indexing table guard interlock micro switch location](/guides/rotary-indexing-table-guard-interlock-micro-switch-location/)
- [security barrier open position micro switch wiring](/guides/security-barrier-open-position-micro-switch-wiring/)

## Why terminal labels do not tell you what the feeder will do

The contact transition belongs to the switch; its operational meaning belongs to the feeder’s actual wiring and control logic. A circuit could interpret a transition in different ways, so terminal labels alone cannot establish which state corresponds to paper present or absent, whether a jam is detected, or whether the feeder stops or reports an error. Those conclusions require design-specific evidence about the mechanism, connections, and control behavior.

If observed feeder behavior differs from expectation, do not collapse the possibilities into a single switch diagnosis. The issue could involve mechanical input to the actuator, an internal contact, terminal identification, wiring, or another part of the equipment. The terminal labels and an isolated continuity check can address only limited questions about the documented contact arrangement and tested state. They cannot, by themselves, distinguish every possible installed-system cause.

For a defensible interpretation, establish the exact switch’s markings and connection diagram, the documented reference condition, the actuator state under consideration, and the feeder’s relevant wiring and control logic. If any of these are unknown, leave the paper-state interpretation or system response unresolved. In short, **document feeder paper path micro switch NO and NC terminals** describe switch contacts only within their documented reference and actuator conditions; the feeder’s behavior cannot be read from those labels alone.

## Sources and references

- Defense Logistics Agency ASSIST: [MIL-PRF-8805K: Switches and Switch Assemblies, Sensitive, Snap Action, General Specification For](https://quicksearch.dla.mil/qsDocDetails.aspx?ident_number=7196){: rel="nofollow noopener noreferrer" }
- Occupational Safety and Health Administration: [29 CFR 1910.333: Selection and Use of Work Practices](https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.333){: rel="nofollow noopener noreferrer" }
- Wikipedia: [Miniature snap-action switch](https://en.wikipedia.org/wiki/Miniature_snap-action_switch){: rel="nofollow noopener noreferrer" }
