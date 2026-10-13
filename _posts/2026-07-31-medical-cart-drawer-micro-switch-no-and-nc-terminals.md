---
title: "Medical cart drawer micro switch NO and NC terminals: how to identify them"
description: "medical cart drawer micro switch NO and NC terminals: Understand the operating idea, essential terminology, practical checks, limitations, and evidence."
date: 2026-07-31 19:59:21 +0800
last_modified_at: 2026-10-13 11:46:37 +0800
category: Applications
tags:
  - medical cart drawer micro switch NO and NC terminals
  - micro switches
  - Applications
author: editorial_team
---

A medical cart drawer may use a micro switch to detect movement, but the drawer’s position alone does not identify which contacts are open or closed. The **medical cart drawer micro switch NO and NC terminals** must be interpreted from the switch’s documented reference condition and actuator state, not from an assumption about what “open” or “closed” means for the cart. A micro switch is a component; the cart’s wiring and control logic determine what any contact change does in the larger system.

## What NO and NC mean on a medical cart drawer micro switch NO and NC terminals

NO and NC describe contact states relative to a specified reference condition. They are not universal descriptions of what happens when a drawer opens or closes. To interpret a label, first find the reference condition in the documentation for the particular switch. Then determine the actuator state that corresponds to that condition. Without those details, the labels alone do not establish the state of a terminal pair in a particular drawer position.

COM means common when that contact arrangement is documented. NO and NC identify contact relationships to COM only when the switch documentation establishes that arrangement and its reference condition. Do not infer that a terminal marked or assumed to be NO is open in every physical state, or that an NC terminal is closed in every state. The state can depend on actuator position, and the relevant reference condition must be stated.

This distinction matters in a cart because the switch’s contact state is not the same thing as the cart’s response. A contact change may be connected to control logic, but the effect of that connection is specific to the equipment design. These labels do not, by themselves, reveal whether a cart signals, inhibits, or otherwise responds to drawer movement.

## How drawer movement reaches the micro switch actuator

A drawer may move a micro switch through a direct contact, cam, lever, or linkage if that particular design uses one. The external mechanism moves the switch actuator; the actuator’s movement can change the switch contacts. That mechanical sequence does not establish which contact is used or how the cart interprets it.

The relationship between drawer position and actuator state must be determined from the actual arrangement. A linkage may be positioned or arranged in a way that is not evident from the drawer’s appearance alone. Therefore, neither “drawer open” nor “drawer closed” is a documented switch reference condition unless the switch or equipment documentation says so.

Keep three observations separate: the drawer’s position, the actuator’s position, and the electrical state of the contacts. They are related only through the specific mechanical and electrical design. A click may indicate movement of a snap mechanism, but it does not prove continuity, correct terminal use, or correct operation of the cart. Likewise, seeing the drawer move does not show that the actuator moved as intended or that the contacts changed state.

## Identify terminals from the switch documentation, not drawer position

Use the connection diagram and terminal markings documented for the exact switch and equipment. Confirm the specified reference condition and identify the actuator state associated with it. If the documentation describes COM, NO, and NC, follow those assignments rather than relying on physical terminal location, wire color, or a generic terminal layout. A physical arrangement should not be treated as universal.

The equipment’s circuit function also matters when interpreting how the switch is connected. The wiring diagram and permissible load documented for the exact switch and equipment set the applicable boundaries. A generic diagram cannot establish the actual wiring or function of an unspecified cart. A rating stated for one current type, load, or test condition does not establish a rating for another; consult the applicable specification sheet rather than transferring a value across conditions.

If the relevant documentation is missing or does not state the reference condition, terminal function remains unresolved. Do not assign NO or NC from the drawer’s position or from an undocumented terminal layout. The appropriate next step is to obtain the documentation for the exact switch and cart, or have the equipment assessed by qualified service personnel under the applicable procedure.

## What an isolated continuity check can and cannot show

A continuity check can help evaluate the switch contacts only when the switch is isolated and the test follows the switch documentation. The check needs a defined actuator state and an expected contact behavior drawn from that documentation. Record the state tested and the observed result; do not treat a reading without those details as a complete identification or diagnosis.

For example, documentation may describe a contact state at a specified actuator condition. In that case, compare the isolated measurement with the documented expectation for that condition. Do not substitute drawer-open or drawer-closed for the specified actuator state unless the equipment documentation establishes that relationship. If the expected behavior is not documented, the measurement cannot resolve which terminal pair should be open or closed.

An isolated reading concerns the switch under the tested condition. It does not verify the installed wiring, the cart’s control logic, or the system’s response. A click and a single continuity reading likewise do not prove that the switch or the complete cart assembly is functioning correctly. Overtravel is the distance or angle between the operating position and the extreme position to which the actuator may be moved; that definition does not establish a permitted travel value for an unspecified switch or drawer mechanism.

### Related guides

- [bottling machine home position micro switch location](/guides/bottling-machine-home-position-micro-switch-location/)
- [incinerator end of stroke micro switch maintenance](/guides/incinerator-end-of-stroke-micro-switch-maintenance/)
- [rotary indexing table guard interlock micro switch location](/guides/rotary-indexing-table-guard-interlock-micro-switch-location/)
- [security barrier open position micro switch wiring](/guides/security-barrier-open-position-micro-switch-wiring/)

## Separate a switch finding from a cart-system diagnosis

A mismatch between expected and observed behavior can have several possible sources: the mechanical path may not move the actuator as intended; the contacts may not behave as documented; the terminal assignment may be misunderstood; the wiring may differ from the diagram; or the issue may lie elsewhere in the equipment. These possibilities are not interchangeable diagnoses. A component-level observation does not identify which one applies without the appropriate documentation and verification.

Keep any work within applicable deenergization and qualification requirements. Under the cited United States workplace rule, exposed live parts generally must be deenergized before work; a qualified person must verify the deenergized condition with test equipment; and work on energized parts is limited to qualified persons. Verify all applicable requirements. Energized-circuit diagnosis and safety-critical service should be left to qualified personnel using the cart’s service procedure.

The **medical cart drawer micro switch NO and NC terminals** can be interpreted only from the documented reference condition, terminal assignment, and actuator state. Drawer position, a click, or an isolated reading alone does not establish the cart’s wiring or behavior. When documentation or test expectations are unavailable, keep the conclusion limited and seek the exact equipment information or qualified service assessment.

## Sources and references

- Defense Logistics Agency ASSIST: [MIL-PRF-8805K: Switches and Switch Assemblies, Sensitive, Snap Action, General Specification For](https://quicksearch.dla.mil/qsDocDetails.aspx?ident_number=7196){: rel="nofollow noopener noreferrer" }
- Occupational Safety and Health Administration: [29 CFR 1910.333: Selection and Use of Work Practices](https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.333){: rel="nofollow noopener noreferrer" }
