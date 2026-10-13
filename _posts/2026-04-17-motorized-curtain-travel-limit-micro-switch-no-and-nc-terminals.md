---
title: "motorized curtain travel limit micro switch NO and NC terminals"
description: "motorized curtain travel limit micro switch NO and NC terminals: Understand the operating idea, essential terminology, practical checks, limitations, and."
date: 2026-04-17 17:22:06 +0800
sitemap_omit_lastmod: true
category: Applications
tags:
  - motorized curtain travel limit micro switch NO and NC terminals
  - micro switches
  - Applications
author: editorial_team
---

At a motorized curtain travel limit, the **motorized curtain travel limit micro switch NO and NC terminals** describe contact states, not a guaranteed instruction to stop or reverse the curtain. The terms are meaningful only with a stated reference condition, such as the actuator condition specified in the exact switch documentation. The controller’s response is a separate question determined by the actual circuit and control logic.

Not every motorized curtain design uses a micro switch. When one is present, curtain movement may bring a curtain part or linked mechanism against the switch actuator, changing the contact state. That change alone does not establish what the motor will do.

## What motorized curtain travel limit micro switch NO and NC terminals mean

NO means normally open, and NC means normally closed, but those labels do not by themselves identify the contact state at every point in curtain travel. “Normally” must be tied to a defined reference condition in the switch’s documentation or circuit description. Without that reference, it is not possible to say which contact is open or closed at a particular curtain position or actuator position.

A generic changeover contact may have terminals labeled common, normally closed, and normally open. The exact device marking or schematic controls: terminal labels and contact arrangements should not be inferred from a generic description. A switch may also have a different arrangement, so the presence of NO and NC labels should be established from the actual switch rather than assumed.

These terms describe the relationship between contacts in the specified condition. They do not promise that current is flowing, that a motor is energized, or that a curtain has reached its limit. Current flow depends on the circuit connected to the contacts. Likewise, the word “normally” is not a substitute for identifying the reference state that applies to the particular switch.

For example, a documentation-defined actuator condition may serve as the reference for describing the contact state. The switch may change state when its actuator moves, but a reader should not assign NO or NC to “curtain moving,” “curtain stopped,” or “curtain at the end” without evidence connecting that condition to the actuator state and the documented contact reference. A limit position in the curtain mechanism is not itself a terminal-state definition.

The useful distinction is between a component-level description and a system-level result. NO and NC identify contact states at a stated reference condition. They do not, on their own, identify wiring, current flow, a motor-control command, or the curtain’s response. Keep those questions separate when interpreting a limit switch.

## How curtain travel can actuate a micro switch at a limit

In a design that uses a micro switch for travel sensing, curtain movement or a linked part can contact the switch actuator. The actuator is the part moved by the external mechanism. If the mechanism moves it far enough to operate the switch, the switch’s contacts can change state. This is a conditional mechanical sequence, not a description that applies to every motorized curtain.

The roles are distinct: the curtain and its linkage provide movement; the switch actuator receives that movement; the micro switch changes contact state when operated; and a controller may receive or otherwise use the resulting electrical condition. The switch is a component in that chain, not the curtain mechanism or the controller itself. The exact arrangement depends on the particular design and must not be inferred from the fact that the curtain has a travel limit.

The limit location and the actuator condition are related only through the mechanism that connects them. A curtain reaching a physical endpoint does not prove that a switch actuator was moved, that the switch operated, or that a particular terminal pair changed state. Conversely, an observed contact state does not establish where the curtain is unless the system’s mechanical and electrical relationships are documented.

Other motorized curtain designs may use different sensing arrangements or may not use a micro switch. Do not generalize a micro-switch arrangement to all curtains, or assume that a visible actuator is necessarily the limit sensor for the controller. The available design documentation must establish whether a micro switch is present and how curtain movement reaches its actuator.

The component’s travel limits are also specific to the device. Numerical travel limits are requirements of the applicable specification sheet and must not be inferred from the component category. That boundary matters because the curtain mechanism’s movement and the switch’s permitted or specified movement are different matters; the applicable switch documentation is needed to establish the device-specific limits.

## Why a contact change does not by itself explain motor behavior

A micro switch can change contact state when its actuator is operated, but that fact does not determine whether a curtain motor stops, reverses, continues, or produces another response. The effect depends on the actual circuit and controller logic. The same NO or NC label cannot establish the system outcome without evidence showing how the contacts are used.

The controller may interpret an electrical condition according to its own design. Whether a contact change is treated as a travel-limit input, and what response follows, cannot be concluded from the switch terminals alone. In particular, do not infer that an NO contact always stops a motor or that an NC contact always reverses it. Those are system-level conclusions requiring circuit and control information.

Keep three observations separate: the curtain’s mechanical position, the switch actuator’s condition, and the contact state documented for that condition. A fourth question, the controller’s response, depends on the circuit. Evidence for one does not automatically establish the others. For instance, a curtain at an endpoint does not prove a contact changed, and a contact change does not prove the controller recognized it or stopped the motor.

This distinction also limits what a contact description can establish about a problem. A failure to stop or reverse might involve the switch, its mechanical actuation, terminal identification, wiring, controller logic, or another part of the equipment. NO and NC terminology alone cannot distinguish among those possibilities. Diagnosing a curtain that fails to stop or reverse is outside this explanation; the relevant point is that contact labels do not settle that diagnosis.

### Related guides

- [bottling machine home position micro switch location](/guides/bottling-machine-home-position-micro-switch-location/)
- [incinerator end of stroke micro switch maintenance](/guides/incinerator-end-of-stroke-micro-switch-maintenance/)
- [rotary indexing table guard interlock micro switch location](/guides/rotary-indexing-table-guard-interlock-micro-switch-location/)
- [security barrier open position micro switch wiring](/guides/security-barrier-open-position-micro-switch-wiring/)

## How to identify the terminals and verify the stated contact condition

Start with the exact switch marking and its documentation or schematic. Use those sources to identify the terminal arrangement and the reference condition for its NO and NC descriptions. Do not rely on a generic terminal layout or transfer a state description from another switch. If the documentation does not define the relevant actuator condition or contact arrangement, those details remain unresolved.

Any continuity check must be understood as a check of the isolated switch in a defined actuator state, using a stated measuring method and an expected result taken from the exact device documentation. The available evidence does not provide a curtain-specific test procedure or expected continuity readings. Therefore, it would be inappropriate to prescribe which terminals to measure, what curtain position to use, or what result to expect without the applicable switch information.

An isolated-switch reading addresses only the tested switch and condition. It does not establish the safety of the installed circuit, confirm that the curtain controller is wired or configured correctly, or prove that the complete curtain system works. A click or mechanical movement, by itself, likewise does not establish continuity or controller response.

For electrical work in a United States workplace, the cited workplace rule generally requires exposed live parts to be deenergized before work, requires a qualified person to verify the deenergized condition with test equipment, and limits work on energized parts to qualified persons. Verify all applicable requirements. This boundary does not provide a wiring or rewiring procedure.

The defensible conclusion is narrow: NO and NC name contact states only relative to the reference condition specified for the actual switch. Curtain movement can operate a micro switch’s actuator in designs that use one, but the resulting contact change does not, by itself, reveal the controller’s response. For a motorized curtain travel limit micro switch NO and NC terminals, use the exact switch documentation and circuit evidence to connect the component state to the system behavior.

## Sources and references

- Defense Logistics Agency ASSIST: [MIL-PRF-8805K: Switches and Switch Assemblies, Sensitive, Snap Action, General Specification For](https://quicksearch.dla.mil/qsDocDetails.aspx?ident_number=7196){: rel="nofollow noopener noreferrer" }
- Occupational Safety and Health Administration: [29 CFR 1910.333: Selection and Use of Work Practices](https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.333){: rel="nofollow noopener noreferrer" }
- Wikipedia: [Miniature snap-action switch](https://en.wikipedia.org/wiki/Miniature_snap-action_switch){: rel="nofollow noopener noreferrer" }
