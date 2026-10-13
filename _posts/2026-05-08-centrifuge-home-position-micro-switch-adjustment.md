---
title: "Centrifuge Home Position Micro Switch Adjustment: What to Check"
description: "centrifuge home position micro switch adjustment: Understand the operating idea, essential terminology, practical checks, limitations, and evidence needed."
date: 2026-05-08 20:16:17 +0800
last_modified_at: 2026-10-13 11:46:37 +0800
category: Applications
tags:
  - centrifuge home position micro switch adjustment
  - micro switches
  - Applications
author: editorial_team
---

A centrifuge home position micro switch adjustment is appropriate only when the equipment documentation confirms that a micro switch senses home position and identifies an adjustment procedure. The adjustment may change when the switch is actuated relative to a mechanical reference. It does not, by itself, establish that the controller interprets the signal correctly or that the centrifuge is aligned as intended.

Treat the switch, its mechanical actuator path, and the centrifuge’s control system as separate parts of the assessment. Do not adjust or reach into moving or energized equipment. Use the equipment-specific service procedure for safe isolation, inspection, adjustment, and verification. If that procedure or its acceptance criteria are unavailable, stop and use qualified service.

## What centrifuge home position micro switch adjustment can and cannot change

A miniature snap-action switch can change an electrical contact state in response to mechanical actuator movement, and it is commonly used for position or limit detection. That general function does not establish that a particular centrifuge uses a micro switch for home sensing. Apply the guidance here only when the design documentation identifies that sensor and explains the relevant adjustment.

Where the design permits adjustment, it can change the point in the mechanical movement at which the switch is actuated relative to the documented reference. The resulting contact signal is only one link in the sensing path. The controller interprets that signal, and the centrifuge responds according to its specific design. A displayed home state therefore does not prove direct rotor alignment or identify which link produced the indication.

The term “home position” does not provide a universal switch clearance, actuator travel, rotor angle, or other setting. Do not substitute a generic value for the equipment’s documented criteria. Designs that use an encoder, Hall-effect sensor, or another sensing method require different assessment; do not apply micro-switch adjustment guidance to them.

## Establish the equipment-specific reference before touching the switch

Begin with the applicable service instructions. They must identify the sensing method, safe isolation requirements, reference position, any permitted adjustment points, and the method and criteria for verification. Do not infer a safe position, normal contact state, or access procedure from the switch’s presence or from a controller display.

If the procedure requires access to energized equipment, rotor movement, or any condition for which safe steps and qualifications are not documented, do not improvise. Leave that work to qualified service personnel. Do not move or reach into equipment unless the applicable procedure explicitly provides a safe method and the required conditions are met.

Before any adjustment, confirm that the documentation describes the specific switch and mechanism being inspected. A generic diagram or an apparent physical layout is not enough to identify terminals, contact state, or permissible load. Use the connection diagram, terminal markings, circuit function, and permissible load documented for the exact switch and equipment. If any of these details is missing and needed for the check, stop rather than infer it.

## Trace the mechanical actuation path to the micro switch

Within the prescribed safe inspection procedure, trace the documented mechanical path from the rotor or drive reference to the switch actuator. A cam, lever, or linkage may be present, but its existence and arrangement must be established for the specific design. Identify which part is intended to move the actuator and how that movement relates to the documented home reference. Do not assume that the actuator contacts the rotor directly.

Inspect only the parts the procedure permits you to examine. Look for visible displacement, looseness, obstruction, or damage in the mounting and documented linkage. These observations can point to a mechanical issue, but they do not establish the cause of an incorrect home indication. A switch may move at an unexpected point because of its mounting or actuation path; wiring or control-system behavior may also contribute.

Keep observations separate from conclusions. A controller indication reports the system’s interpreted state, not which mechanical or electrical link is responsible. If the documentation does not identify the reference, linkage, or inspection boundary, do not infer them from appearance. Request qualified service instead.

## Make only the adjustment the service procedure specifies

Proceed only if the equipment-specific procedure identifies an adjustment point, explains the permitted change, and states how to verify the result. Follow its criteria exactly. No universal gap, travel, force, or angular value can be inferred from the phrase “home position” or from the general definition of a micro switch.

Do not bend or modify an actuator or linkage unless the specific procedure directs that action. Do not treat a freely moving part, an apparent alignment, or a changed controller indication as proof that the switch was adjusted correctly. The relevant mechanical event is when the documented movement actuates the switch relative to the specified reference. The controller’s programmed interpretation of the resulting signal is a separate matter.

If the procedure provides no adjustment criterion, does not identify the relevant reference, or does not describe a safe way to perform the work, do not create a setting by trial and error. Stop and request qualified service. Adjustment is not a substitute for diagnosing a wiring or control-system problem.

## Verify switch response and centrifuge indication separately

Use the documented method to check switch response, and keep the stated reference condition and required isolation conditions attached to that check. Do not assume a COM, NO, or NC terminal arrangement unless the applicable documentation identifies it. Terminal names and contact states must be read in the documented reference condition, not inferred from the switch’s physical layout.

An audible click may indicate movement of a snap mechanism, but it does not prove continuity, correct wiring, or correct electrical operation. A click also does not establish that the actuator moved at the intended point relative to the equipment’s reference. Use only the procedure’s specified verification method and expected response; do not replace it with an unsupported test.

Separately confirm the centrifuge’s home indication by the prescribed system-level verification procedure. This checks the equipment’s indicated result, not just switch movement. A failure or unexpected result can involve actuation, mounting, wiring, the controller, the drive, or another part of the documented control path. Neither a component-level check nor a displayed state alone proves the full assembly is correct.

### Related guides

- [bottling machine home position micro switch location](/guides/bottling-machine-home-position-micro-switch-location/)
- [incinerator end of stroke micro switch maintenance](/guides/incinerator-end-of-stroke-micro-switch-maintenance/)
- [rotary indexing table guard interlock micro switch location](/guides/rotary-indexing-table-guard-interlock-micro-switch-location/)
- [security barrier open position micro switch wiring](/guides/security-barrier-open-position-micro-switch-wiring/)

## When to stop and request qualified service

Stop if the sensing method, safe isolation procedure, reference position, permitted adjustment, terminal information needed for a check, or acceptable verification result is unknown. These gaps prevent a supported adjustment or conclusion. Do not fill them with a generic setting or an assumption about the switch’s normal state.

If adjustment does not meet the documented verification criteria, do not keep changing the switch or conclude that the switch is necessarily defective. The cause may be elsewhere in the control path, and diagnosing or repairing that path is outside this adjustment guidance. Use qualified service when the procedure does not resolve the documented failure or requires work beyond its stated safe boundary.

Do not return a centrifuge to service based only on actuator movement, an audible click, an isolated continuity result, or a home indication considered on its own. Use the equipment’s documented verification criteria. If those criteria or the safe procedure are unavailable, centrifuge home position micro switch adjustment should stop until qualified service can establish the correct method and decision boundary.

## Sources and references

- Defense Logistics Agency ASSIST: [MIL-PRF-8805K: Switches and Switch Assemblies, Sensitive, Snap Action, General Specification For](https://quicksearch.dla.mil/qsDocDetails.aspx?ident_number=7196){: rel="nofollow noopener noreferrer" }
- Occupational Safety and Health Administration: [29 CFR 1910.333: Selection and Use of Work Practices](https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.333){: rel="nofollow noopener noreferrer" }
- Wikipedia: [Miniature snap-action switch](https://en.wikipedia.org/wiki/Miniature_snap-action_switch){: rel="nofollow noopener noreferrer" }
