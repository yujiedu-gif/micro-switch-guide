---
title: "Scissor lift home position micro switch NO and NC terminals"
description: "scissor lift home position micro switch NO and NC terminals: Understand the operating idea, essential terminology, practical checks, limitations, and."
date: 2026-08-25 14:44:25 +0800
sitemap_omit_lastmod: true
category: Applications
tags:
  - scissor lift home position micro switch NO and NC terminals
  - micro switches
  - Applications
author: editorial_team
---

A scissor lift home-position signal cannot be interpreted from NO and NC labels alone. The **scissor lift home position micro switch NO and NC terminals** must be understood relative to the switch’s documented actuator reference condition and contact arrangement. Those labels do not, by themselves, say whether the lift is raised, lowered, powered, or recognized as home.

Keep two questions separate: what contact state the isolated switch has in a defined actuator position, and what the lift’s actual circuit does with that state. A continuity check may help identify an isolated switch’s contact behavior under specified conditions, but it does not establish how the installed lift is wired or whether its home-position function is correct.

## What NO and NC mean on a scissor lift home position micro switch NO and NC terminals

NO and NC describe contact states at a specified reference condition. To interpret the labels, first find the reference condition in the documentation for the exact switch: it must state the relevant actuator position or condition. Do not substitute an assumed lift position, such as fully lowered, for that documented reference.

At the stated reference condition, NO means normally open and NC means normally closed. “Normally” is not a universal description of the lift at rest or of a circuit when power is off. It is tied to the switch’s specified reference condition. If the documentation does not establish that condition, the labels alone do not identify the contact state for a particular actuator position.

COM means common only where the switch’s contact configuration and terminal identification establish a COM terminal. Do not infer terminal functions from physical placement, a familiar-looking layout, or the number of terminals. Use the exact switch and equipment documentation, including the connection diagram and terminal markings, to identify the arrangement. If those details are missing or unclear, treat the terminal identities as unresolved rather than guessing.

The labels also do not establish whether a contact carries current in the installed circuit, what the circuit considers “home,” or whether a signal enables or inhibits a function. Those conclusions depend on the documented circuit and its control logic. NO and NC are contact-state descriptions, not promises about the lift’s powered state or physical position.

## How the micro switch can indicate a scissor lift home position

A micro switch can provide a contact change when an external mechanism moves its actuator. In a lift installation, the relationship between that mechanism and a home-position signal must be established from the design documentation. The switch may be part of the sensing arrangement, but its contact label does not independently define the lift’s position or the system’s response.

Keep the mechanical event distinct from the electrical interpretation. A linkage or other external mechanism may move the actuator; the actuator movement may change a documented contact state; and the lift’s circuit may use that state as one input to its home-position logic. These are separate links in the chain. Evidence that one link changes does not, by itself, prove that the next link is wired or interpreted as expected.

For example, knowing that a contact is identified as NO at a documented actuator reference condition does not reveal whether that condition corresponds to the lift being at home. Nor does it show whether the lift control treats an open or closed circuit as the home signal. That interpretation requires the actual circuit and equipment documentation. Do not infer it from the words “normally open” or “normally closed.”

Different lift designs may use different switch arrangements and control logic. A description of one documented arrangement should not be generalized to all scissor lifts. If the particular actuator reference, terminal configuration, or circuit function is not documented, the relationship between the switch and the lift’s home indication remains unknown.

## How to identify NO and NC on an isolated micro switch

Start with the exact switch’s connection diagram and terminal markings. Confirm which terminals the documentation identifies and what actuator condition it uses as the reference. If COM, NO, and NC are not established for that switch, do not assign those functions based only on terminal position or appearance.

A continuity check can address the isolated switch’s contact state only when the switch is isolated from the circuit and the actuator is placed in a defined, documented position. Record the actuator condition and the result for the specific terminal pair being tested. Interpret that result against the switch’s documented contact arrangement and reference condition. Without those details, a reading may describe continuity between two tested points, but it does not reliably identify those points as COM, NO, or NC.

The evidence available here establishes a general boundary for interpreting insulation-resistance tests: insulation resistance is evaluated between specified electrically isolated points using the applicable test method and conditions. It does not supply a particular test voltage, acceptance value, or test procedure for this lift switch. Do not invent those parameters or treat an insulation-resistance measurement as a substitute for identifying contact states.

A click is not a continuity result. It may indicate mechanical movement, but it does not prove which terminals are connected, that contacts are electrically sound, or that the switch is suitable for its installed circuit. Likewise, one reading in one actuator state does not establish behavior in another state. A useful component-level finding is limited to the isolated switch, the defined actuator state, the tested terminal pair, and the measurement performed.

### Related guides

- [bottling machine home position micro switch location](/guides/bottling-machine-home-position-micro-switch-location/)
- [incinerator end of stroke micro switch maintenance](/guides/incinerator-end-of-stroke-micro-switch-maintenance/)
- [rotary indexing table guard interlock micro switch location](/guides/rotary-indexing-table-guard-interlock-micro-switch-location/)
- [security barrier open position micro switch wiring](/guides/security-barrier-open-position-micro-switch-wiring/)

## What a terminal reading can and cannot diagnose

An isolated contact reading can help distinguish the tested switch’s contact behavior from assumptions based on terminal layout. It cannot, by itself, identify every cause of a lift’s home-position symptom. The external mechanism may fail to move the actuator as intended; the terminal identities may be uncertain; wiring may differ from the documentation or have a fault; or the issue may lie elsewhere in the control circuit. These possibilities must not be collapsed into a diagnosis of a bad switch.

A mechanical input problem concerns whether the lift mechanism moves the switch actuator to the relevant documented position. A contact finding concerns the isolated switch under the tested conditions. A wiring or control-system finding concerns the installed circuit and requires evidence from that circuit. A switch continuity result alone does not settle those separate questions, and it does not prove that the lift recognizes home correctly.

The safety boundary matters because installed lifting equipment is not equivalent to an isolated component on a bench. The cited United States workplace rule generally requires exposed live parts to be deenergized before work, requires a qualified person to verify the deenergized condition with test equipment, and limits work on energized parts to qualified persons. Applicable requirements must be verified for the work and jurisdiction. Do not treat an isolated continuity result as proof that the installed lift is safe to operate or that its controls function correctly. Unresolved electrical or safety work on the installed equipment belongs with qualified personnel.

The practical conclusion is narrow: identify NO and NC only against the exact switch’s documented actuator reference condition and terminal arrangement. Verify contact behavior, if appropriate, on the isolated switch in a defined state. Then keep that result separate from the lift’s mechanical input, wiring, and control logic. The **scissor lift home position micro switch NO and NC terminals** do not reveal the lift’s home state without that additional documented context.

## Sources and references

- Defense Logistics Agency ASSIST: [MIL-PRF-8805K: Switches and Switch Assemblies, Sensitive, Snap Action, General Specification For](https://quicksearch.dla.mil/qsDocDetails.aspx?ident_number=7196){: rel="nofollow noopener noreferrer" }
- Occupational Safety and Health Administration: [29 CFR 1910.333: Selection and Use of Work Practices](https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.333){: rel="nofollow noopener noreferrer" }
