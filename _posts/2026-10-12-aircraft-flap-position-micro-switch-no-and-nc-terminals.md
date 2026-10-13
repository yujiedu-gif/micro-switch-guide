---
title: "aircraft flap position micro switch NO and NC terminals"
description: "aircraft flap position micro switch NO and NC terminals: Understand the operating idea, essential terminology, practical checks, limitations, and evidence."
date: 2026-10-12 16:49:35 +0800
category: Applications
tags:
  - aircraft flap position micro switch NO and NC terminals
  - micro switches
  - Applications
author: editorial_team
---

An **aircraft flap position micro switch NO and NC terminals** describe contact relationships inside a switch, not flap positions by themselves. The switch responds to mechanical actuator movement; the installation and aircraft circuit determine which actuator state corresponds to a particular flap position or indication. A terminal marked NO is therefore not automatically a flap-up contact, and NC is not automatically flap-down.

To interpret the signal, first establish what the switch contacts do when its actuator is unoperated and when it is operated. Then use the aircraft-specific wiring diagram and maintenance documentation to connect those contact states to the indicated flap states. This distinction matters because switch behavior, linkage movement, wiring, and indication logic are separate parts of the signal path.

## What NO and NC mean on an aircraft flap position micro switch NO and NC terminals

For a changeover switch, **COM** means common, **NO** means normally open, and **NC** means normally closed. “Normally” refers to the switch actuator’s unoperated state. It does not mean the aircraft’s normal operating condition, nor does it identify a specific flap position.

In the unoperated state, COM-to-NC is the closed contact path, while COM-to-NO is open. When the actuator operates, the changeover contact state reverses: COM-to-NC opens and COM-to-NO closes. Thus, continuity describes the electrical relationship between terminals at a particular actuator state. It does not, on its own, establish whether the flaps are up, down, or between positions.

The distinction is essential when reading an indication circuit. A switch can change state as a linkage moves, but the terminal labels only describe the switch’s contact arrangement. The linkage’s direction, switch placement, and circuit design establish what that transition means for the aircraft. Do not infer those details from NO or NC alone.

Confirm the terminal symbols against the exact switch’s schematic and the applicable equipment documentation. A generic terminal layout is not a reliable substitute for the documented connection diagram, terminal markings, circuit function, and permissible load for the exact switch and equipment. The same caution applies when interpreting diagrams: identify the specific contact and circuit rather than relying on an assumed physical arrangement.

## How a micro switch contact state can represent flap position

A miniature snap-action switch can change an electrical contact state in response to mechanical actuator movement and is commonly used for position or limit detection. In a flap-position installation, however, the contact change represents flap position only through the installed mechanism and electrical circuit. The switch’s basic action does not define which flap position the aircraft will indicate.

Linkage geometry and switch placement determine when the actuator moves between its unoperated and operated states. For example, the documentation may associate one of those states with a position threshold or a particular indication. The circuit may then use the corresponding contact state as an input to indication logic. Those relationships must be established from the aircraft-specific documentation, not inferred from the words “normally open” or “normally closed.”

Keep three questions separate: What is the actuator state? Which contact path is closed in that state? What flap indication does the documented circuit assign to that input? The first two concern switch operation; the third concerns the installation and circuit. Combining them prematurely can produce a mistaken flap-up or flap-down interpretation even when the switch contacts operate as designed.

A position indication is therefore a system-level meaning, not an intrinsic label on the switch terminal. The applicable wiring diagram and maintenance documentation should show how the switch, relevant wiring, and indication circuit relate. If the documented mapping is unavailable or unclear, the flap position associated with either contact state remains unresolved rather than safely inferable from terminal names.

## Verify NO and NC behavior using the applicable diagram

Begin with the aircraft-specific wiring diagram and maintenance documentation. Use them to identify the relevant switch, its terminal designations, the circuit function, and the required test conditions. Do not substitute a generic switch diagram for aircraft documentation, or assume that a familiar terminal layout establishes the exact device’s connections or permissible load.

Under the specified safe test conditions, identify COM, NO, and NC from the terminal markings and the exact switch schematic. Check continuity between COM and NC with the actuator unoperated, then check COM and NO. Operate the actuator as specified by the applicable procedure and check the contact paths again. The expected change is that COM-to-NC opens and COM-to-NO closes. Compare the observations with the device and aircraft documentation; do not extend a continuity result into an unverified claim about flap position.

Next, follow the documented circuit to determine how the relevant contact state is used by the indication system. Compare the switch’s observed state with the documented signal path and flap-indication logic. This circuit-diagram-first approach separates a local contact check from the broader question of what the aircraft should display for a given flap position.

Testing conditions and methods must come from the applicable documentation and procedures. Follow applicable deenergization and qualification requirements. Aircraft-specific work, including any decision about return to service, must follow applicable approved maintenance procedures. A general description of contact behavior cannot replace those requirements or establish an aircraft-specific test method.

### Related guides

- [ball screw actuator home position micro switch replacement](/guides/ball-screw-actuator-home-position-micro-switch-replacement/)
- [bottling machine end of stroke micro switch](/guides/bottling-machine-end-of-stroke-micro-switch/)
- [automated guided vehicle home position micro switch location](/guides/automated-guided-vehicle-home-position-micro-switch-location/)
- [accelerator pedal position stop micro switch operating force](/guides/accelerator-pedal-position-stop-micro-switch-operating-force/)

## Interpreting a mismatch without assuming the switch is at fault

A mismatch can occur at different points in the signal path. If the contact does not change as expected between actuator states, that is a different observation from a contact that changes correctly but fails to produce the documented indication. The latter does not, by itself, show that the switch is defective; interpretation depends on the rest of the documented circuit.

Keep the relevant checks distinct. The documented linkage travel and switch actuation concern how mechanical movement reaches the actuator. The switch contacts concern the local electrical change. Wiring and downstream indication logic concern how that change is carried and interpreted. A discrepancy in the final display cannot identify which point is responsible without the applicable aircraft procedures and evidence.

Compare observations with the diagram and maintenance documentation rather than assigning a fault from terminal labels. In particular, do not treat NO as a universal flap-up signal or NC as a universal flap-down signal. The mapping depends on the installed linkage, switch placement, and circuit logic. If those documented relationships do not explain the observed behavior, the cause remains unresolved in this general discussion.

The practical boundary is straightforward: terminal names establish contact relationships, while aircraft documentation establishes how those relationships participate in flap indication. Use the applicable approved maintenance procedures for aircraft-specific evaluation and return-to-service decisions. The **aircraft flap position micro switch NO and NC terminals** can be interpreted accurately only in that documented installation context.

## Sources and references

- Defense Logistics Agency ASSIST: [MIL-PRF-8805K: Switches and Switch Assemblies, Sensitive, Snap Action, General Specification For](https://quicksearch.dla.mil/qsDocDetails.aspx?ident_number=7196){: rel="nofollow noopener noreferrer" }
- Occupational Safety and Health Administration: [29 CFR 1910.333: Selection and Use of Work Practices](https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.333){: rel="nofollow noopener noreferrer" }
- Wikipedia: [Miniature snap-action switch](https://en.wikipedia.org/wiki/Miniature_snap-action_switch){: rel="nofollow noopener noreferrer" }
