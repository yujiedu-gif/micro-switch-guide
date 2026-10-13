---
title: "Stair lift travel limit micro switch NO and NC terminals: what do they mean?"
description: "stair lift travel limit micro switch NO and NC terminals: Understand the operating idea, essential terminology, practical checks, limitations, and."
date: 2026-07-17 19:07:51 +0800
last_modified_at: 2026-10-13 11:46:37 +0800
category: Applications
tags:
  - stair lift travel limit micro switch NO and NC terminals
  - micro switches
  - Applications
author: editorial_team
---

A stair lift travel limit micro switch NO and NC terminals describe contact relationships at a specified actuator reference condition. They do not, by themselves, identify whether the lift is powered, moving, parked, or approaching a travel limit. To interpret the labels, use the exact switch’s markings and documentation, then keep any component-level check separate from conclusions about the lift’s control system.

A micro switch is an electromechanical component. Its actuator is the part moved by an external mechanism; its contacts change relationship according to the switch design and actuator state. The stair lift’s response to that change depends on the lift’s particular control circuit. The terminal labels alone cannot establish what the lift will do.

## Stair lift travel limit micro switch NO and NC terminals: what the labels mean

NO means normally open, and NC means normally closed. These labels describe contact relationships at the switch’s stated reference condition. The reference condition must come from the applicable device documentation or marking. Do not automatically equate it with a lift being powered off, parked, moving, or in any other operating state.

For a documented changeover contact arrangement, common (COM) is the shared terminal, and the NO and NC labels identify the other contacts relative to that arrangement’s stated reference condition. In that condition, the documented relationship distinguishes the normally open contact from the normally closed one. The exact switch marking or schematic controls; not every micro switch necessarily has this terminal set or arrangement.

“Open” and “closed” here describe the contact relationship, not the lift’s mechanical position or a guaranteed system outcome. A contact change may provide an input to a larger circuit, but the circuit determines how that input is used. The labels alone do not say whether the lift stops, continues, signals, or responds in another way.

The key distinction is between the switch’s reference condition and the host equipment’s operating state. A lift’s position or motion cannot be used as a substitute for the reference condition unless the applicable switch and lift documentation explicitly connects those states. Without that information, the contact meaning at a particular point in the lift’s travel remains unresolved.

## How actuator movement changes the contact relationship

A travel-limit arrangement can involve a lift mechanism or linkage moving the switch actuator, but the specific mechanical arrangement must be documented for the lift and switch in question. The actuator is the switch part moved by that external mechanism. When the actuator state changes, a documented switch mechanism may change its contact relationship. That component-level description does not establish the lift’s resulting behavior.

Keep three things distinct: the lift’s physical position, the actuator’s state, and the contact relationship. They are related only as specified by the actual mechanical arrangement and circuit. The NO or NC label refers to the contact at the stated reference condition, not to a universal point along the lift’s route. Nor does the label alone show when a linkage moves the actuator or whether that movement corresponds to a particular travel limit.

Even where a contact changes state as the actuator moves, the system response depends on the lift’s control logic. Without design-specific evidence, do not infer that opening a contact stops motion, that closing it permits motion, or that either state produces an alarm or another response. Those possibilities cannot be resolved from the NO and NC names alone.

This boundary matters because a switch can be understood correctly while the host system remains unknown. The switch labels describe a component relationship. The lift documentation is needed to establish how its mechanism actuates the switch and how its circuit interprets the resulting contact change.

## Identifying NO, NC, and common terminals on the actual switch

Start with the exact switch’s terminal markings and applicable documentation. A connection diagram or schematic can identify the documented contact arrangement and show which terminal is COM, NO, or NC when those terminals are present. Use COM only when the documentation establishes a common terminal for that arrangement.

Do not identify terminals by physical position, apparent similarity to another switch, or an assumed standard layout. A generic changeover contact may use COM, NO, and NC labels, but that does not establish that a particular switch has that arrangement or that its terminals occupy any expected positions. Terminal markings and the exact device documentation take precedence over a generic inference.

If the markings are absent, unclear, or inconsistent with the available documentation, treat the terminal identity as uncertain. Do not guess which terminal serves as common or assign NO and NC based on where a terminal sits. A wrong assumption can confuse component interpretation with the lift’s wiring and circuit function. Resolving the arrangement requires documentation for the exact switch and equipment, not a universal pinout.

The same boundary applies to ratings and permissible loads. Electrical ratings are requirements tied to the stated load and test conditions in the applicable specification; they are not universal switching capacities. Terminal names do not establish that a switch is suitable for a particular circuit or load. Use the exact switch and equipment documentation for connection details and permissible load, and follow applicable deenergization and qualification requirements.

## What an isolated continuity check can and cannot establish

A continuity check is meaningful only for an isolated, disconnected switch, a defined actuator state, and an appropriate safe procedure. The expected contact result must come from the documented terminal arrangement and reference condition. Without those details, a reading cannot resolve which terminal is NO, NC, or COM or whether the switch behaves as the documentation specifies.

Any such check must remain within applicable safe procedures and the person’s qualifications. Work beyond that boundary belongs to qualified personnel. Do not treat a component check as permission to probe or operate an installed lift circuit. The evidence here does not provide a procedure for testing the lift’s wiring or control system.

A continuity result speaks only to the isolated switch under the tested condition. It does not establish that the terminals are correctly connected in the lift, that the installed circuit is safe, or that the lift will respond as intended at a travel limit. It also does not identify a fault elsewhere in the equipment. A component-level reading cannot stand in for system-level verification.

Keep the test conditions attached to any conclusion: which documented terminals were checked, whether the switch was disconnected and isolated, and what actuator state was used. If any of these are unknown, the meaning of the result is limited. If system behavior or installed wiring must be assessed, use the applicable lift documentation and qualified service rather than inferring a diagnosis from NO and NC labels.

### Related guides

- [bottling machine home position micro switch location](/guides/bottling-machine-home-position-micro-switch-location/)
- [incinerator end of stroke micro switch maintenance](/guides/incinerator-end-of-stroke-micro-switch-maintenance/)
- [rotary indexing table guard interlock micro switch location](/guides/rotary-indexing-table-guard-interlock-micro-switch-location/)
- [security barrier open position micro switch wiring](/guides/security-barrier-open-position-micro-switch-wiring/)

## Why the stair lift’s travel-limit response is design-specific

The micro switch may supply an input to a control circuit, but the circuit and equipment design determine what happens next. A contact opening or closing might be used in different ways; without evidence for the specific lift, it cannot be said which state stops motion, triggers an alarm, or serves another function. The NO and NC labels do not encode that system behavior.

For the specific lift, the applicable equipment documentation is the basis for interpreting the switch’s role, its actuator relationship, and the circuit’s response. If that documentation does not resolve the arrangement or the expected travel-limit behavior, the uncertainty remains. Qualified service is the appropriate boundary for system-level interpretation or work beyond a safely isolated component check.

In short, stair lift travel limit micro switch NO and NC terminals identify contact relationships only at the documented actuator reference condition. Use the exact switch markings and documentation to identify terminals, and do not infer lift position, wiring, safety, or travel-limit response from the labels or an isolated continuity result alone.

## Sources and references

- Defense Logistics Agency ASSIST: [MIL-PRF-8805K: Switches and Switch Assemblies, Sensitive, Snap Action, General Specification For](https://quicksearch.dla.mil/qsDocDetails.aspx?ident_number=7196){: rel="nofollow noopener noreferrer" }
- Occupational Safety and Health Administration: [29 CFR 1910.333: Selection and Use of Work Practices](https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.333){: rel="nofollow noopener noreferrer" }
- Wikipedia: [Miniature snap-action switch](https://en.wikipedia.org/wiki/Miniature_snap-action_switch){: rel="nofollow noopener noreferrer" }
