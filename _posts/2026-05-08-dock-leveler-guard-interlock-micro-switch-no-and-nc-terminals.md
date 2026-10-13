---
title: "Dock leveler guard interlock micro switch NO and NC terminals"
description: "dock leveler guard interlock micro switch NO and NC terminals: Understand the operating idea, essential terminology, practical checks, limitations, and."
date: 2026-05-08 21:24:40 +0800
sitemap_omit_lastmod: true
category: Applications
tags:
  - dock leveler guard interlock micro switch NO and NC terminals
  - micro switches
  - Applications
author: editorial_team
---

A dock leveler guard interlock micro switch NO and NC terminals describe contact states at a specified reference condition. They do not, by themselves, identify what happens when a guard opens or closes. To determine the terminal behavior, use the exact switch documentation, identify the actuator state being checked, and keep an isolated component test separate from the dock leveler’s wiring and control logic.

This distinction matters because the guard and its linkage act on the switch, while the switch is only one component in the host equipment. A terminal label, a mechanical click, or a continuity observation cannot independently establish how the complete interlock behaves. The method below focuses on identifying the switch’s documented contact state without making assumptions about the equipment’s design.

## What NO and NC mean on a dock leveler guard interlock micro switch NO and NC terminals

NO and NC describe contact states relative to the reference condition specified for the particular switch and contact arrangement. NO means the contact is open at that documented reference condition; NC means it is closed at that condition. These names are not universal descriptions of the contacts with the guard open or closed. The applicable reference condition must come from the switch documentation.

If the documented arrangement includes COM, it identifies the common terminal for that arrangement. Do not assume that a switch has a COM terminal, or infer which physical terminal is COM from its location. Use the terminal markings and connection diagram for the exact switch. The documentation must establish both the terminal identities and the condition under which its NO and NC descriptions apply.

The reference condition is important because the actuator may be in a different state when installed or when the guard moves. A contact described as NO at the documented reference condition may not remain open after the actuator changes state. Likewise, an NC description does not mean the contact is closed in every position. The labels provide a reference for interpreting the contact arrangement; they do not specify every actuator state or the timing of a change.

Do not substitute the guard’s apparent position for the documented switch reference condition. “Guard open” and “guard closed” describe equipment positions. They do not, without further documentation, define the state in which the switch’s NO and NC labels were assigned. First establish the switch’s reference condition and terminal arrangement; only then can a particular actuator state be compared with the documented behavior.

## Keep switch actuator state separate from guard position

A guard, cam, lever, or linkage may move a micro switch actuator. That mechanical relationship depends on the actual arrangement. The guard may move the actuator directly or through a mechanism, but the available information does not establish which arrangement a particular dock leveler uses. Nor does it establish which actuator position corresponds to either guard position. Those relationships must not be inferred from the equipment name or from NO and NC labels alone.

For a meaningful comparison, describe the switch’s actuator state explicitly, using the condition identified by the switch documentation or the condition being checked. Then consult the relevant documentation to determine whether that actuator state corresponds to a contact change. If the relationship between guard movement and actuator movement is not documented, it remains unresolved. Do not label an observation “guard-open state” as though that automatically identifies the switch’s actuator state.

Contact behavior is also distinct from the dock leveler’s control logic. Even if the switch’s contact state is known, that fact alone does not establish how the equipment circuit interprets it or what response follows. The wiring diagram and circuit function are needed to understand that system-level relationship. The same contact state cannot be assigned a particular equipment response merely because the switch is described as a guard interlock.

Use the applicable diagram and documentation rather than generic assumptions about terminal layout or interlock behavior. The documented permissible load and ratings also matter when evaluating the switch in its circuit: rating values are tied to stated load and test conditions, not universal switching capacities. This page does not establish a rating or suitability for any particular dock leveler, circuit, or load.

## Verify terminal behavior on an isolated micro switch

A component-level continuity check can help identify contact behavior only when the switch is isolated, the terminals are documented, and the actuator state is explicitly defined. Start by confirming the terminal identities from the exact switch’s markings and connection diagram. Define the actuator state to be checked by reference to the switch documentation. Do not use an assumed guard position as a substitute when the guard-to-actuator relationship is unknown.

The continuity observation must apply to the isolated switch, not to an installed circuit whose other connections may affect what is measured. Follow the applicable deenergization and qualification requirements before any work. Within a documented, safe procedure, take the measurement in the defined actuator state and compare the observation with the switch documentation. If that documentation does not specify the expected contact behavior for the state being checked, the observation cannot be interpreted as a documented pass or failure.

Keep the conclusion narrow. An isolated reading describes the switch under the tested condition. It does not establish that the terminal identification is correct if the documentation was not checked, that the switch is wired correctly in the equipment, or that the interlock circuit works. A result in one actuator state also does not establish behavior in every other state. Record the state and the applicable documentation when describing what the measurement shows.

Do not infer an installed-system result from an isolated component reading. The dock leveler’s circuit may include wiring and other components beyond the switch, and this evidence does not define that circuit. A system-level conclusion therefore requires the relevant equipment documentation and checks beyond this bounded component verification.

### Related guides

- [bottling machine home position micro switch location](/guides/bottling-machine-home-position-micro-switch-location/)
- [incinerator end of stroke micro switch maintenance](/guides/incinerator-end-of-stroke-micro-switch-maintenance/)
- [rotary indexing table guard interlock micro switch location](/guides/rotary-indexing-table-guard-interlock-micro-switch-location/)
- [security barrier open position micro switch wiring](/guides/security-barrier-open-position-micro-switch-wiring/)

## What a click or continuity result does not establish

A click can indicate movement of a snap mechanism, but it does not prove electrical continuity, correct terminal identification, correct wiring, or suitability for the circuit’s load. A switch may produce an audible or tactile event without that observation resolving the contact state. Treat the click as a mechanical observation, not as a substitute for documented terminal identification or an appropriate component test.

Similarly, a continuity result is limited to the isolated switch, the defined actuator state, and the test conditions. It does not diagnose a wiring fault, establish the control logic, or show that the complete interlock operates as intended. If the observation differs from the documented behavior, it identifies a discrepancy for further evaluation; it does not by itself identify the cause or justify a repair, adjustment, or replacement conclusion.

Electrical work has a defined safety boundary. The cited United States workplace rule generally requires exposed live parts to be deenergized before work, requires a qualified person to verify the deenergized condition with test equipment, and limits work on energized parts to qualified persons. Verify all applicable requirements. Do not extend a component-level continuity check into system-level electrical work without the appropriate documentation and qualifications.

The reliable interpretation is therefore bounded: NO and NC refer to the documented reference condition, while a continuity observation applies only to an isolated switch in a defined actuator state. Neither the labels nor a click establishes how a guard position maps to contact behavior or how the dock leveler responds. Leave system-level interlock evaluation or work outside the documented procedure to qualified personnel.

This concludes the explanation of dock leveler guard interlock micro switch NO and NC terminals.

## Sources and references

- Defense Logistics Agency ASSIST: [MIL-PRF-8805K: Switches and Switch Assemblies, Sensitive, Snap Action, General Specification For](https://quicksearch.dla.mil/qsDocDetails.aspx?ident_number=7196){: rel="nofollow noopener noreferrer" }
- Occupational Safety and Health Administration: [29 CFR 1910.333: Selection and Use of Work Practices](https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.333){: rel="nofollow noopener noreferrer" }
