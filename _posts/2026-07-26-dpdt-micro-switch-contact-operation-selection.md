---
title: "DPDT Micro Switch: Contact Operation and Selection"
description: "dpdt micro switch: Understand the operating idea, essential terminology, practical checks, limitations, and evidence needed for careful selection,."
date: 2026-07-26 09:00:00 +0800
category: Selection Guides
tags:
  - dpdt micro switch
  - micro switches
  - Selection Guides
author: editorial_team
---

A **dpdt micro switch** routes two separate electrical paths through one mechanically actuated changeover mechanism. DPDT means “double-pole, double-throw”: each pole has a common contact that can connect to either of two contacts. To understand what the switch does, follow each pole separately, then verify its terminals and ratings using documentation for the specific device. The DPDT label describes a contact arrangement, not a guaranteed terminal layout or universal switching capacity.

## What a DPDT micro switch means

“Double-pole” means the switch contains two poles, or two contact sets. “Double-throw” means each pole can change its connection between two throws. In a changeover arrangement, each pole has a common terminal, a normally closed contact, and a normally open contact. The common is the moving electrical connection for that pole; it connects to one throw or the other as the actuator changes position.

This is more than a single-pole changeover switch with an extra wire. A single-pole changeover arrangement has one common and two selectable contacts. A DPDT arrangement has two such contact sets, each able to route a separate circuit. The two poles share mechanical actuation, but are electrically separate unless the external circuit connects them.

DPDT does not identify where terminals sit on the switch body, how they are marked, or which way a particular device is oriented. Symbols such as COM, NO, and NC are general changeover terminology: COM means common, NO means normally open, and NC means normally closed. Confirm the exact device schematic and markings before assigning terminals. A generic drawing or physical resemblance to another switch is not enough to establish the terminal map.

## How a dpdt micro switch changes contact state

Each pole's common terminal changes between its NC and NO contacts as the actuator moves. In the unoperated state, the common is associated with the normally closed contact; in the operated state, it is associated with the normally open contact. “Normally” refers to the actuator's unoperated state, not to a preferred circuit condition. The actual contact behavior should be verified against the specific switch documentation and by checking the device.

The mechanism coordinates the two poles because the same actuator operates both contact sets. That mechanical coordination does not make their electrical paths one circuit. Each pole has its own common and two throws, and the poles remain electrically separate unless wiring outside the switch joins them. Do not assume that a shared actuator means a shared electrical common.

The changeover description identifies the available contact relationships, but it does not establish every detail of the switching sequence. For example, the label alone does not say when a contact changes relative to actuator movement or provide a timing specification. If sequence details matter to a circuit, use the switch's specific documentation rather than extrapolating from the DPDT designation.

Actuator travel terminology can help interpret that documentation. Pretravel is the movement from the free position to the operating position. Overtravel is the movement from the operating position to the extreme permitted actuator position. These terms describe portions of travel, not terminal identities. Do not use an assumed travel value or actuator position as a substitute for identifying the contacts on the device.

## Identify terminals and verify both poles

Begin with the switch de-energized and isolated from the circuit before checking continuity. Do not test continuity on an energized circuit. If the switch remains connected to other circuit paths, those connections may affect readings; use the device documentation to establish how to isolate it appropriately.

With the actuator unoperated, check continuity between candidate terminals to identify the common-to-NC path for the first pole. Operate the actuator and check whether the common instead connects to the other throw. Record the terminal pairs and observed actuator state. Then repeat the checks independently for the second pole, rather than assuming its terminals mirror the first pole's physical arrangement.

A useful record names the terminals by their verified functions, not just by their locations. For each pole, note the common, the contact connected in the unoperated state, and the alternate contact connected in the operated state. Compare those observations with the switch's schematic or markings. If the readings do not fit the expected changeover pattern, repeat the isolation and actuator checks and consult the specific documentation before drawing conclusions.

Continuity checks establish observed contact connections under the test conditions; they do not establish the switch's electrical rating, suitability for a load, or full operating sequence. Keep terminal identification separate from those other selection questions. Likewise, do not treat a terminal layout in a generic wiring diagram as confirmation that an individual switch has the same layout.

## Selection checks beyond the DPDT label

Contact configuration is only one part of selection. Compare the specified voltage and current ratings with the circuit requirements and the load type. Electrical ratings are specification-sheet requirements tied to stated load and test conditions, not universal switching capacities. A rating without its relevant conditions does not establish that the switch is suitable for every circuit at that voltage or current. Use the applicable specification sheet and its stated conditions when comparing a switch with the intended load.

Check the actuator requirements and travel information against the mechanism that will operate the switch. Relevant documentation can describe actuator force, operating position, and travel. Pretravel runs from the free position to the operating position, while overtravel runs from the operating position to the extreme permitted actuator position. Compare the available device details with the intended mechanical arrangement instead of assuming that the actuator will reach or remain at a required position.

Also check expected mechanical life, environmental constraints, and mounting constraints in the switch documentation. The DPDT designation alone does not establish any of these properties. Keep the checks distinct: pole and throw count describe the contact arrangement; the specified ratings and conditions address electrical use; and the actuator and installation details address mechanical fit. If a required property is not stated in the available documentation, treat it as unresolved rather than inferring it from the contact label.

### Related guides

- [inline micro switch](/guides/inline-micro-switch-suitability/)
- [access hatch open position micro switch contact rating](/guides/access-hatch-open-position-micro-switch-contact-rating/)
- [micro switch salt spray](/guides/micro-switch-salt-spray/)
- [adjustable desk closed position micro switch contact rating](/guides/adjustable-desk-closed-position-micro-switch-contact-rating/)

## Common mistakes and safe next steps

Do not identify COM, NO, or NC solely by terminal position, and do not copy a generic wiring diagram without confirming the particular switch's schematic. Terminal symbols have general meanings, but the exact terminal arrangement must be verified for the device. A plausible physical layout is not proof that the two poles are arranged in a particular order.

Do not infer electrical suitability from “DPDT,” or treat a stated rating as independent of its load and test conditions. Compare the documented voltage and current ratings with the intended circuit and load type. Do not check continuity on an energized circuit. Keep both poles' observations separate, even though the actuator moves them together.

If readings are inconsistent, repeat the checks with the switch de-energized and isolated, and confirm which actuator position is being tested. Consult the specific switch documentation if the terminal map or behavior remains uncertain. The sound basis for using a DPDT contact arrangement is a verified terminal map for each pole plus documented ratings and operating conditions, not the label alone.

This concludes the explanation of dpdt micro switch.

## Sources and references

- Defense Logistics Agency ASSIST: [MIL-PRF-8805K: Switches and Switch Assemblies, Sensitive, Snap Action, General Specification For](https://quicksearch.dla.mil/qsDocDetails.aspx?ident_number=7196){: rel="nofollow noopener noreferrer" }
- Wikipedia: [Miniature snap-action switch](https://en.wikipedia.org/wiki/Miniature_snap-action_switch){: rel="nofollow noopener noreferrer" }
