---
title: "Material feeder end of stroke micro switch NO and NC terminals: what do they indicate?"
description: "material feeder end of stroke micro switch NO and NC terminals: Understand the operating idea, essential terminology, practical checks, limitations, and."
date: 2026-09-06 08:15:04 +0800
last_modified_at: 2026-10-13 11:46:37 +0800
category: Applications
tags:
  - material feeder end of stroke micro switch NO and NC terminals
  - micro switches
  - Applications
author: editorial_team
---

For a material feeder, NO and NC identify contact states relative to the micro switch’s specified unactuated reference condition. The material feeder end of stroke micro switch NO and NC terminals do not, by themselves, say whether the feeder starts, stops, reverses, or signals an alarm. Those system responses depend on the feeder’s wiring and control design.

A miniature snap-action switch can change an electrical contact state when mechanical movement operates its actuator, including in position or limit detection. To interpret terminal labels, use the contact diagram and documentation for the particular switch. Then keep two questions separate: what contacts the isolated switch presents in a defined actuator state, and how the installed feeder circuit responds to those contacts.

## What material feeder end of stroke micro switch NO and NC terminals indicate

NO means normally open, and NC means normally closed, with “normal” tied to the switch’s specified unactuated reference condition. These labels describe contact relationships in that reference state. They are not universal descriptions of the material feeder’s position, motion, or operating mode. In particular, an end-of-stroke label does not establish that the switch is unactuated or actuated at a particular point in every feeder design.

If the specific switch’s diagram identifies COM, it is the common terminal in that documented contact arrangement. The diagram is the basis for identifying which terminals form the relevant contact paths. Do not assume that a physical terminal’s location, shape, or placement matches a generic layout, or that every switch has the same terminal arrangement. If the diagram does not identify a terminal or contact relationship, that information remains unresolved until the switch documentation is consulted.

The labels also do not determine the feeder’s response. A contact that is open or closed at the switch does not, on its own, establish whether the feeder is commanded to run, stop, reverse, or signal an alarm. That interpretation belongs to the actual circuit and its control logic. The switch describes a component-level contact state; the feeder’s behavior is a system-level result.

For that reason, start with the switch’s specified unactuated reference condition, not with an assumption about what “end of stroke” must mean electrically. Identify the contact arrangement from the exact switch documentation, and use the feeder’s relevant diagram to understand how those contacts are connected and interpreted. Without those references, terminal names alone support only the relative contact-state meaning, not a specific feeder function.

## How end-of-stroke movement changes the micro switch contacts

The general mechanical sequence is conditional: a feeder mechanism reaches a point where its linkage moves the micro switch actuator; if that movement operates the switch, the documented contact arrangement changes state. The end-of-stroke event is the mechanical input. The resulting contact change is the switch’s electrical response. The feeder circuit’s interpretation of that response is a separate step.

The precise relationship between feeder position and switch actuation depends on the arrangement. A linkage may move the actuator as the mechanism approaches an end position, but the end-of-stroke label alone does not establish the linkage, the exact point of actuation, or which switch state corresponds to which feeder position. Different feeder designs may use different linkages and control logic. Do not infer travel, operating force, timing, or a universal contact sequence from the application name.

It is useful to describe the two states without assigning them prematurely to feeder positions. First, record the contact condition in the switch’s documented unactuated reference state. Then identify the condition when the actuator is operated, as specified by the switch documentation. This describes the switch’s transition. To connect that transition to a feeder position, the actual mechanical arrangement must show when the linkage operates the actuator.

Likewise, a contact transition does not itself reveal what the control system does with the changed signal. The circuit may interpret a contact state according to its own wiring and logic, but the supplied terminal labels do not show that logic. A specific stop, reverse, or alarm function must not be attributed to the micro switch unless the feeder documentation establishes it. Keep the explanation at the level supported by each reference: switch documentation for contact behavior, and feeder documentation for position mapping and system response.

## How to verify NO and NC states on an isolated micro switch

A bounded check concerns the switch by itself, with its terminals identified from the switch’s own connection diagram. The switch must be isolated from the feeder circuit for the check. Use a continuity method supported by the switch documentation, and note the actuator condition for every observation. An observation without a defined reference or actuator state is difficult to interpret against the NO and NC labels.

Record the result in at least the documented unactuated reference condition and the documented actuated condition. Compare the observed contact paths with the contact arrangement and expected behavior stated for that particular switch. If COM, NO, and NC are documented, use those documented terminal identities when recording which paths are continuous or open. Do not substitute a generic terminal layout or assume that every switch presents the same arrangement.

The comparison is meaningful only within those stated conditions: the identified switch, the documented terminals, isolation from the feeder circuit, the continuity method, and the actuator state. If the result does not match the switch documentation, the observation indicates a discrepancy to investigate, but it does not by itself identify the cause. Terminal identification, test setup, actuator condition, or the switch itself may need to be considered; the evidence given here does not resolve which explanation applies.

A contact check also has a narrow conclusion. It can provide evidence about the isolated switch’s contact behavior under the tested actuator conditions. It does not show that feeder wiring is correct, that a controller reads the signal as intended, or that the feeder will respond properly at its end-of-stroke position. An isolated result should not be presented as proof that the complete installed assembly works or fails.

### Related guides

- [bottling machine home position micro switch location](/guides/bottling-machine-home-position-micro-switch-location/)
- [incinerator end of stroke micro switch maintenance](/guides/incinerator-end-of-stroke-micro-switch-maintenance/)
- [rotary indexing table guard interlock micro switch location](/guides/rotary-indexing-table-guard-interlock-micro-switch-location/)
- [security barrier open position micro switch wiring](/guides/security-barrier-open-position-micro-switch-wiring/)

## What the contact check cannot establish about a material feeder

An isolated contact transition does not establish that the switch is connected to the intended feeder terminals, that the controller interprets the signal correctly, or that the linkage operates the actuator at the intended point. Those are distinct questions about installation, control logic, and mechanical relationship. Each requires the relevant documentation or observation; none follows automatically from the NO and NC labels.

Use the switch’s connection diagram to identify its documented contact arrangement and terminal identities. Use the applicable feeder schematic or other relevant equipment documentation to trace how those contacts enter the circuit and how the control system treats them. The feeder documentation is also needed to relate the linkage’s motion to the switch’s actuator. Without that information, the mapping from contact state to feeder state remains uncertain.

This boundary matters when a feeder does not behave as expected. A contact-state result and an installed feeder symptom are not interchangeable evidence. A switch can show a documented transition when tested in isolation while an installation, linkage, wiring, or control issue remains unexamined. Conversely, an unexpected system response does not by itself establish that the isolated switch has failed. The available facts support separating these possibilities, not selecting one without further evidence.

Accordingly, the material feeder end of stroke micro switch NO and NC terminals indicate contact states relative to the switch’s specified unactuated reference condition. The documented contact arrangement establishes how actuation relates to those contacts; the feeder schematic and control documentation establish how the circuit uses them. Neither terminal labels nor an isolated continuity check establishes a universal stop, reverse, alarm, or overall feeder function.

## Sources and references

- Defense Logistics Agency ASSIST: [MIL-PRF-8805K: Switches and Switch Assemblies, Sensitive, Snap Action, General Specification For](https://quicksearch.dla.mil/qsDocDetails.aspx?ident_number=7196){: rel="nofollow noopener noreferrer" }
- Occupational Safety and Health Administration: [29 CFR 1910.333: Selection and Use of Work Practices](https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.333){: rel="nofollow noopener noreferrer" }
- Wikipedia: [Miniature snap-action switch](https://en.wikipedia.org/wiki/Miniature_snap-action_switch){: rel="nofollow noopener noreferrer" }
