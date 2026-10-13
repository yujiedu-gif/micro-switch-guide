---
title: "Sample tray position micro switch NO and NC terminals"
description: "sample tray position micro switch NO and NC terminals: Understand the operating idea, essential terminology, practical checks, limitations, and evidence."
date: 2026-10-04 11:44:10 +0800
sitemap_omit_lastmod: true
category: Applications
tags:
  - sample tray position micro switch NO and NC terminals
  - micro switches
  - Applications
author: editorial_team
---

A sample tray position micro switch NO and NC terminals describe contact states at a defined reference condition, not universal tray-in and tray-out labels. The tray's physical position matters only through the mechanism that moves the switch actuator and the contact arrangement documented for that particular design. A sample-tray application uses a micro switch only when the design documentation identifies one; the presence of a tray does not establish that a micro switch is used.

To interpret the labels, keep four things separate: tray position, movement of any lever or linkage, the switch's actuator state, and the response of the surrounding circuit. Documentation for the specific switch and equipment establishes how those relate. Without it, the terminal labels do not reveal which contact is open at a particular tray position or what the equipment will do.

## What NO and NC mean on a sample tray position micro switch NO and NC terminals

NO and NC identify contact states relative to the reference condition specified for the particular switch arrangement. At that condition, NO means normally open and NC means normally closed. The reference condition must come from the applicable switch or equipment documentation; do not substitute an assumed tray position for it.

A tray may be in or out while a lever, cam, or other linkage is in a design-specific position. That mechanism may move the switch actuator, but the labels alone do not say when the actuator reaches the operating point. Nor do they establish whether a particular contact changes state as the tray moves inward or outward. That mapping requires evidence about the actual mechanical arrangement and reference condition.

The contact-state description is not, by itself, a promise about current flow in the equipment. Current and equipment response depend on the documented circuit and its operation. Do not infer a COM terminal, terminal layout, powered behavior, or electrical rating from NO and NC labels or from the switch's physical appearance. Use the connection diagram, terminal markings, circuit function, and permissible load documented for the exact switch and equipment rather than a generic physical-layout inference.

## How tray motion reaches the micro switch

In a design documented to use a micro switch, the mechanical path can be understood as a sequence: tray movement acts on any intervening lever or linkage; that part moves the switch actuator; and actuator movement may bring the switch to its operating event. Each step is specific to the design. The tray's location is not itself the actuator state, and the actuator state does not identify a contact terminal without the documented arrangement.

For example, documentation might describe how a tray-associated part contacts a lever, but that description would apply only to the documented design. Do not assume that all trays use a lever, that every tray has a position switch, or that the switch is contacted at a particular point in tray travel. Some designs may use a different mechanism or no micro switch at all.

This distinction matters when interpreting a reported indication. A tray can occupy a physical position without the available evidence showing that the actuator moved as intended. Conversely, actuator movement alone does not establish what the circuit sensed or how the equipment responded. A conclusion about detection needs support at each link: the tray-to-mechanism relationship, the mechanism-to-actuator relationship, the documented contact state, and the circuit's response.

## How to identify the documented terminal states

Start with the connection diagram or other documentation for the exact switch and equipment. Identify the terminal markings and the stated reference condition, then read NO and NC only against that condition. If the documentation does not identify the arrangement or reference condition, the labels alone are insufficient to assign an open or closed state for a particular tray position. Do not guess based on terminal placement or a generic diagram.

Any continuity verification must follow a documented method and apply to a defined actuator state. The relevant interpretation concerns the isolated switch, not an assumed reading through installed equipment wiring. If the documentation does not give a test method or expected behavior for the defined condition, do not invent one. A single reading cannot establish the tray mechanism, installed wiring, or full equipment operation.

A click may indicate movement of a snap mechanism, but it does not prove electrical continuity, contact condition, correct wiring, or suitability for the circuit. Likewise, a continuity result under one defined condition speaks only to the isolated switch and tested state; it does not prove that the installed circuit is connected correctly or that the equipment responds as intended. Keep those limits close to the observation rather than treating either observation as a complete diagnosis.

Terminal identification and any verification must also remain within the documented safe test conditions. The applicable connection information should establish the contact arrangement, circuit function, and permissible load for the exact equipment. If the test boundary or safe isolation is unclear, the labels are not a basis for improvising a test or wiring change.

### Related guides

- [bottling machine home position micro switch location](/guides/bottling-machine-home-position-micro-switch-location/)
- [incinerator end of stroke micro switch maintenance](/guides/incinerator-end-of-stroke-micro-switch-maintenance/)
- [rotary indexing table guard interlock micro switch location](/guides/rotary-indexing-table-guard-interlock-micro-switch-location/)
- [security barrier open position micro switch wiring](/guides/security-barrier-open-position-micro-switch-wiring/)

## What the terminal state does not prove

An NO or NC label does not prove that a tray is present, seated, or correctly sensed. Those are conclusions about the tray and the host equipment, not just about a contact label. A contact state can be interpreted only in its documented reference condition, and a mechanical position can be connected to that state only when the actual actuator or linkage relationship is known.

Nor does a contact change specify what the equipment does. The resulting behavior depends on the actual circuit and control logic. Do not infer an alarm, interlock, start, stop, or other response merely because a sample-tray position switch is present. The micro switch is a component in an arrangement; the surrounding equipment determines how its contact state is used.

If terminal identity, reference condition, mechanism, or safe test conditions are unclear, leave the relationship unresolved rather than assigning a tray position to NO or NC. The sound conclusion is limited: the labels describe documented contact states, while the tray-position mapping and system response require separate evidence. A sample tray position micro switch NO and NC terminals therefore cannot, on their own, confirm tray position or explain equipment behavior.

## Sources and references

- Defense Logistics Agency ASSIST: [MIL-PRF-8805K: Switches and Switch Assemblies, Sensitive, Snap Action, General Specification For](https://quicksearch.dla.mil/qsDocDetails.aspx?ident_number=7196){: rel="nofollow noopener noreferrer" }
- Occupational Safety and Health Administration: [29 CFR 1910.333: Selection and Use of Work Practices](https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.333){: rel="nofollow noopener noreferrer" }
