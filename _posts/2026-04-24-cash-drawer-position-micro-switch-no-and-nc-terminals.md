---
title: "Cash drawer position micro switch NO and NC terminals: what do the labels mean?"
description: "cash drawer position micro switch NO and NC terminals: Understand the operating idea, essential terminology, practical checks, limitations, and evidence."
date: 2026-04-24 11:37:38 +0800
last_modified_at: 2026-10-13 11:46:37 +0800
category: Applications
tags:
  - cash drawer position micro switch NO and NC terminals
  - micro switches
  - Applications
author: editorial_team
---

A **cash drawer position micro switch NO and NC terminals** question is answered by identifying the switch’s documented reference condition, not by assuming that a terminal label means “drawer open” or “drawer closed.” A micro switch is an electromechanical component used in some cash-drawer position arrangements; it is not the drawer or its control system. The switch actuator’s position, the drawer’s position, and the circuit’s response are separate facts unless the specific mechanism and wiring establish a relationship among them.

## Cash drawer position micro switch NO and NC terminals: start with the switch reference state

NO and NC describe contact states relative to a specified reference condition for the particular switch. The reference condition must be established from that switch’s documentation. The labels alone do not identify whether the drawer is open or closed, whether the actuator is pressed, or what the cash-drawer system will do.

Read the switch’s connection diagram and terminal markings together with its stated contact arrangement and reference condition. Do not infer terminal identity from physical location or from a generic layout. If the documentation does not establish which terminals are NO and NC, or what condition is the reference, those details remain unresolved until verified from the exact switch information.

Keep three positions distinct:

- **Drawer position:** where the drawer is in its travel.
- **Actuator position:** where the switch’s mechanically moved part is.
- **Reference condition:** the condition the switch documentation uses to define its contact labels.

A mechanism may relate these positions, but the relationship cannot be assumed from the words NO and NC. Even if the actuator appears to move as the drawer moves, that observation does not by itself establish the documented reference state or electrical contact condition. Likewise, a contact label does not specify the control logic connected to the switch.

The practical interpretation is conditional: first identify the documented reference condition and terminal arrangement; then, if the documentation describes other actuator states, interpret contact behavior in those states as specified. Without that information, do not translate NO or NC into an unqualified claim about drawer position or circuit behavior.

## How the cash-drawer mechanism can relate to a micro switch

In some arrangements, a drawer-related part can move a micro switch actuator. The drawer, a mechanical part associated with it, the actuator, and the switch contacts are distinct components or functions. The actual mechanism determines whether drawer movement reaches the actuator, in which direction it moves it, and when that movement occurs.

That mechanical relationship is design-specific. The presence of a micro switch near a cash drawer does not establish that the drawer directly contacts the actuator, that a particular drawer position corresponds to actuation, or that the switch changes state at a particular point in the drawer’s travel. Those details require information about the actual mechanism and switch.

Nor does the mechanical event determine what the cash-drawer circuit does. A change in the switch’s contact state may be connected to equipment control logic, but the resulting system response depends on the actual wiring and design. The switch’s NO or NC label cannot, by itself, show whether the drawer is reported as open, whether an alarm is triggered, or whether any other action occurs. The controller’s interpretation is outside what the terminal labels alone establish.

A click or visible actuator movement is similarly limited evidence. It may indicate mechanical movement, but it does not establish electrical continuity, correct terminal identification, or the function of an installed circuit. Drawer movement is not a substitute for checking the switch’s documented contact arrangement. Keep observations about motion separate from conclusions about electrical behavior.

This distinction prevents a common reasoning error: treating a drawer position as if it were the switch’s reference condition. The reference belongs to the documented switch contact description. The drawer’s position can be mapped to that condition only when the particular mechanism shows how drawer movement affects the actuator and the documentation identifies the relevant contact state.

## What an isolated continuity check can establish

An isolated continuity check can help assess the switch’s contact behavior, but only within defined limits. Use the particular switch documentation to identify the terminals and the actuator conditions to be checked. The switch must be isolated from the surrounding circuit for the check; a reading taken through installed wiring does not, by itself, identify the switch’s own contact state.

For a meaningful comparison, note the tested terminal pair, the actuator condition, and the documented reference condition. Compare the result with the contact arrangement specified for that switch. If the available documentation does not define the terminal pair or expected behavior for a tested state, the result cannot be confidently interpreted from the NO and NC labels alone.

A reading concerns the isolated switch under the conditions tested. It does not prove that the switch is correctly connected in the cash drawer, that the wiring is intact, or that the host circuit responds as intended. Conversely, an unexpected reading does not by itself identify whether the cause is terminal misidentification, the actuator not being in the assumed state, a contact problem, or some other issue. Further conclusions require the relevant documentation and a suitable verification method.

Do not treat an audible click as a continuity test. A click does not establish that the measured contacts changed state, that the correct terminals were measured, or that the installed circuit performs a particular function. The physical and electrical observations answer different questions.

Electrical work also has a boundary. The cited United States workplace rule generally requires exposed live parts to be deenergized before work, requires a qualified person to verify the deenergized condition with test equipment, and limits work on energized parts to qualified persons. Verify all applicable requirements. This general boundary does not supply a procedure for a particular cash drawer; work must follow the applicable requirements and the equipment’s documented information.

### Related guides

- [bottling machine home position micro switch location](/guides/bottling-machine-home-position-micro-switch-location/)
- [incinerator end of stroke micro switch maintenance](/guides/incinerator-end-of-stroke-micro-switch-maintenance/)
- [rotary indexing table guard interlock micro switch location](/guides/rotary-indexing-table-guard-interlock-micro-switch-location/)
- [security barrier open position micro switch wiring](/guides/security-barrier-open-position-micro-switch-wiring/)

## When terminal labels do not settle the drawer’s behavior

NO and NC labels settle only the contact-state terminology supported by the particular switch documentation. They do not resolve every possible cause of a cash-drawer symptom. Keep the questions separate: Are the terminals correctly identified? Does the mechanism move the actuator as expected? What contact state does the isolated switch show in a defined actuator condition? How is the switch wired? What does the downstream control logic do with that input?

Each question requires evidence suited to it. The switch connection diagram and terminal markings address identification. Information about the actual mechanism is needed to relate drawer position to actuator position. A defined, isolated check can address the switch contact state. The circuit documentation is needed to understand installed wiring and system response. One observation cannot stand in for all of these.

If the specific switch documentation and circuit information are unavailable, leave the drawer-to-actuator mapping and the system response unresolved. Do not infer them from the labels, drawer movement, or a click. The correct boundary is straightforward: NO and NC are interpreted at the switch’s documented reference condition; a mechanical link to drawer position must be established separately; and installed cash-drawer behavior depends on the actual wiring and control design.

This concludes the explanation of cash drawer position micro switch NO and NC terminals.

## Sources and references

- Defense Logistics Agency ASSIST: [MIL-PRF-8805K: Switches and Switch Assemblies, Sensitive, Snap Action, General Specification For](https://quicksearch.dla.mil/qsDocDetails.aspx?ident_number=7196){: rel="nofollow noopener noreferrer" }
- Occupational Safety and Health Administration: [29 CFR 1910.333: Selection and Use of Work Practices](https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.333){: rel="nofollow noopener noreferrer" }
