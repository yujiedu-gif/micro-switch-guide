---
title: "micro switch changeover contacts explained"
description: "micro switch changeover contacts explained: Understand the operating idea, essential terminology, practical checks, limitations, and evidence needed for."
date: 2026-10-13 09:00:00 +0800
category: Basics
tags:
  - micro switch changeover contacts explained
  - micro switches
  - Basics
author: editorial_team
---

A micro switch can use changeover contacts to provide two contact paths controlled by one actuator, but this arrangement is not present on every design. **Micro switch changeover contacts explained** means reading COM, NO, and NC in relation to the switch’s documented, unactuated reference condition. The labels describe the contact arrangement and state; they do not, by themselves, say what a connected load will do.

The key is to keep three things separate: the actuator’s position, the switch’s contact state, and the response of the surrounding circuit. A contact label alone does not establish current flow, correct wiring, or application suitability. The exact switch’s marking or schematic, together with the equipment’s connection diagram and circuit function, controls how its terminals should be identified and interpreted.

## Micro switch changeover contacts explained: identify the contact arrangement

A changeover contact arrangement is one documented design option for a micro switch. When the exact switch provides terminals marked COM, NO, and NC, COM means common, and NO and NC identify the other contacts relative to the specified, unactuated reference condition. These terms describe a switch’s contact relationships, not the behavior of every device called a switch.

In that reference condition, NC names the contact path identified as normally closed, while NO names the path identified as normally open. “Normally” refers here to the stated unactuated condition. It is not a promise about current flow in an installed circuit: whether current flows also depends on the wiring, connected components, and circuit state. The terminal labels alone do not establish whether a load is energized or what an equipment control system will do.

Do not assume every micro switch has a changeover arrangement or these three terminals. A particular design may have a different contact configuration, and terminal position or physical layout should not be used to infer identity. The exact device marking or schematic is the authority for the terminal arrangement. If documentation does not establish which terminal is COM, NO, or NC, that identification remains unresolved rather than something to guess from a generic drawing or appearance.

This reference-condition definition also keeps the terms from being mistaken for permanent terminal properties. The labels describe the documented relationship between the contacts at a defined actuator condition. Moving the actuator can change that relationship, as described below, but the names themselves do not specify what happens elsewhere in the circuit.

## How the contacts change as the micro switch actuator moves

A miniature snap-action switch can change an electrical contact state in response to mechanical actuator movement. In a documented changeover design, the contact relationship changes as the actuator moves from its unactuated reference condition. This is the switch-level meaning of changeover: the actuator movement is associated with a change in the contact state, rather than a guaranteed outcome for a connected load.

The same distinction applies when the actuator is released. Release is a separate return event: the actuator moves back toward its unactuated condition, and the contact relationship is considered against that reference again. The supplied contact labels do not establish the timing, force, travel, or detailed behavior of a particular switch during actuation or release. Those details cannot be inferred from COM, NO, and NC alone.

It is useful to describe the sequence without overstating it: first, identify the documented unactuated reference condition; next, consider the actuator’s movement and the resulting contact-state change for the documented arrangement; then consider release as the return movement. This explains the relationship among the labels and actuator state without claiming that a contact is electrically perfect or that a particular circuit must respond in a specific way.

The contact arrangement is therefore a property of the particular switch design, while actuator movement is the mechanical input associated with the state change. Neither fact, by itself, establishes that the switch is correctly connected, that a load receives current, or that the host equipment behaves as expected. Those questions depend on the actual wiring and circuit function, not just on the changeover terminology.

## Contact labels are not the same as circuit behavior

COM, NO, and NC explain the documented switch contact arrangement relative to the unactuated reference. They do not tell you, by themselves, what a machine, control system, or connected load will do when the actuator moves. A contact-state change is the component-level event; the electrical and operational result depends on the surrounding circuit and its control logic.

For example, the labels alone cannot establish whether a circuit is energized in the unactuated condition, whether actuation starts or stops an operation, or whether the equipment signals a position change. Those outcomes require information about the actual wiring, circuit function, and equipment configuration. Do not infer a normal operating state or control response simply from the presence of a changeover contact arrangement.

For a specific device, use its connection diagram and terminal markings to identify the contacts. Interpret them alongside the equipment’s connection diagram, circuit function, and the permissible load documented for that exact switch and equipment. A generic terminal layout is not a substitute for this documentation. The terminal arrangement also does not establish whether the switch is suitable for a particular load.

This boundary matters because a correct description of the switch does not prove a correct installation. The contact labels can be understood at the component level even when the circuit response is unknown. Conversely, knowing what the equipment is intended to do does not establish which physical terminal serves as COM, NO, or NC. Keep terminal identification, contact state, and system behavior as separate questions.

### Related guides

- [micro switch flyback diode causes](/guides/micro-switch-flyback-diode-causes/)
- [panel mount plunger micro switch working principle](/guides/panel-mount-plunger-micro-switch-working-principle/)
- [cam follower micro switch adjustment](/guides/cam-follower-micro-switch-adjustment/)
- [micro switch SPST NC contacts explained](/guides/micro-switch-spst-nc-contacts-explained/)

## What a click or continuity check can and cannot establish

A click may indicate that a mechanism moved, but it does not prove electrical continuity, identify terminals, confirm correct wiring, or establish that the installed equipment operates as intended. A mechanical sound is not an electrical test. Likewise, the contact-state explanation for a documented changeover arrangement does not certify the condition of an individual switch or its suitability in an application.

A continuity reading can be interpreted only with the switch isolated, the actuator in a defined state, and the terminal arrangement known. The reading concerns the isolated switch under those conditions. Without a known arrangement and reference state, a result cannot be reliably matched to the COM, NO, or NC labels. This is a boundary for interpreting a check, not a procedure for diagnosing or repairing a particular installation.

Even an isolated reading does not establish that the installed circuit is safe or operates as intended. Wiring, circuit function, and the equipment’s response remain separate questions. Applicable deenergization and qualification requirements must be followed; the exact switch and equipment documentation governs terminal identification and permissible load. Do not treat a click or a single continuity observation as proof of the whole assembly’s condition.

In short, **micro switch changeover contacts explained** is a switch-level description: COM is common, and NO and NC are defined relative to the documented unactuated reference condition on a design that provides those contacts. Actuator movement is associated with a change in contact state, while release is a distinct return event. What that change means for current flow or equipment behavior depends on the documented circuit, and a click or isolated reading cannot establish correct installed operation.

## Sources and references

- Defense Logistics Agency ASSIST: [MIL-PRF-8805K: Switches and Switch Assemblies, Sensitive, Snap Action, General Specification For](https://quicksearch.dla.mil/qsDocDetails.aspx?ident_number=7196){: rel="nofollow noopener noreferrer" }
- Occupational Safety and Health Administration: [29 CFR 1910.333: Selection and Use of Work Practices](https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.333){: rel="nofollow noopener noreferrer" }
- Wikipedia: [Miniature snap-action switch](https://en.wikipedia.org/wiki/Miniature_snap-action_switch){: rel="nofollow noopener noreferrer" }
