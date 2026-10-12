---
title: "4 pole micro switch: Understanding Poles, Contacts, and Circuit Diagrams"
description: "4 pole micro switch: Understand the operating idea, essential terminology, practical checks, limitations, and evidence needed for careful selection,."
date: 2026-10-05 09:00:00 +0800
category: Selection Guides
tags:
  - 4 pole micro switch
  - micro switches
  - Selection Guides
author: editorial_team
---

A **4 pole micro switch** is described by the number of circuit paths its contacts switch, but that phrase alone does not reveal the exact contact arrangement. To understand a particular device, distinguish poles from throws and terminals, then read its circuit diagram and verify the documented contact states. The same checks help prevent a terminal count or physical layout from being mistaken for a wiring instruction.

The steps below focus on interpreting a switch’s contact configuration and checking it against its diagram. They do not establish the suitability of an unidentified switch for a particular circuit or load.

## What does 4 pole micro switch mean?

A **pole** is an independently switched circuit path. In a four-pole switch, the designation indicates four such paths. It does not mean the device necessarily has only four terminals: a contact path may have more than one terminal, depending on its arrangement. Nor does “four pole” specify how many contact alternatives each path provides.

A **throw** refers to a contact alternative available to a pole. Pole count and throw count describe different parts of a contact configuration. Neither term, by itself, tells you the number of terminals or how those terminals are arranged. A terminal count alone therefore cannot establish the number of poles, throws, or contact groups.

For example, a hypothetical four-pole device could switch four separate circuit paths. Each path might have a different contact arrangement, or the paths might share an arrangement; the designation alone does not settle that question. It also does not establish whether all four paths change state together when the actuator moves. Those details depend on the particular design and its documentation.

Treat the pole count as a description of the switched paths, not as a complete wiring diagram. Before interpreting connections, identify the exact switch diagram and any actuator-state markings supplied for it. If those materials do not identify the contact groups or their states, the missing configuration remains unknown rather than something that can be inferred from the device’s terminal layout.

## Read the contact diagram for a four-pole micro switch

Start with the connection diagram for the exact switch and equipment. In generic changeover terminology, **COM** means common terminal, **NO** means normally open terminal, and **NC** means normally closed terminal. These labels describe contact roles, but the diagram for the particular device determines which terminals carry those labels and how each contact group changes state.

Where a diagram shows COM, NO, and NC for a pole, follow the stated actuator condition and identify the indicated connection for that condition. Do not assume that a terminal nearest another terminal is connected to it, or that terminals arranged similarly on the housing have the same function. Physical position is not a substitute for the diagram.

Compare the four contact groups one at a time. Note which terminals belong to each pole, which contact alternatives are shown, and which actuator condition applies to each diagram marking. Then check whether the documentation depicts the groups changing state together or gives separate state information. Four poles do not, by themselves, prove coordinated operation or identical contact behavior.

A useful working record has one row per pole and columns for the terminals identified by the diagram, the actuator condition, and the connection shown. If the diagram does not provide a needed detail, leave it unresolved and consult the applicable device documentation rather than filling the gap with a generic assumption. This approach preserves the difference between a general terminal abbreviation and the verified arrangement of a specific switch.

## Ratings and boundaries a pole count does not tell you

A four-pole designation is not an electrical rating. It does not establish permissible voltage, current, load type, or switching conditions. Rating values are specification-sheet requirements tied to their stated load and test conditions, not universal switching capacities. Check the values and conditions documented for the exact switch and equipment before treating a contact as suitable for a circuit.

Do not infer that all four poles have identical ratings or that any one pole can carry a particular load merely because the device has four poles. The designation identifies the number of switched paths; it does not establish the permitted load for each path. A contact diagram and a rating statement answer different questions, so both must be interpreted within their documented scope.

Likewise, pole count alone does not establish insulation, isolation, or simultaneous operation. Treat those properties as unknown unless the exact device documentation states them. The applicable specification sheet and equipment documentation determine which requirements and conditions apply; a generic configuration description cannot replace them.

Use the connection diagram, terminal markings, circuit function, and permissible load documented for the exact switch and equipment rather than a generic physical-layout inference. Follow applicable deenergization and qualification requirements when inspecting or testing a circuit. If the documentation does not establish a rating or operating condition needed for the intended circuit, do not assume that the pole count supplies that missing information.

### Related guides

- [inline micro switch](/guides/inline-micro-switch-suitability/)
- [access hatch open position micro switch contact rating](/guides/access-hatch-open-position-micro-switch-contact-rating/)
- [micro switch salt spray](/guides/micro-switch-salt-spray/)
- [dpdt micro switch](/guides/dpdt-micro-switch-contact-operation-selection/)

## How to verify a four-pole contact arrangement safely

Before checking contact continuity, disconnect power and isolate the switch, following applicable deenergization and qualification requirements. Use the device diagram to identify the terminals and actuator states to examine. Do not use a continuity result from a switch still connected to an energized circuit as a substitute for the documented contact arrangement.

Prepare a four-path matrix with one row for each pole and separate columns for the actuator released and operated states. For each row, record the terminals identified by the diagram and the continuity-meter result for each documented state. The diagram should guide which terminal pairs to check; the four-pole label and physical terminal positions do not identify those pairs on their own.

Compare each recorded result with the contact state shown for that pole and actuator condition. The matrix makes it possible to check whether each of the four paths matches its documentation and whether the documented relationship among paths is reflected in the observations. Do not presume all poles switch simultaneously: compare observed behavior only with what the exact diagram or other device documentation specifies.

If a reading does not match the documented state, or is intermittent or unexpectedly shows continuity, do not wire from terminal position alone. Recheck that the diagram applies to the exact switch, that the actuator condition is correctly identified, and that the switch is isolated for the test. If the discrepancy remains, the arrangement is not verified; further assessment should follow applicable qualification requirements and the device documentation.

The result of this process is a verified, diagram-based record of the four contact paths under the tested actuator conditions. It does not establish load suitability, ratings, insulation, or other properties not documented by that test. Use the connection diagram, terminal markings, circuit function, and permissible load documented for the exact switch and equipment; the phrase **4 pole micro switch** alone cannot supply those details.

## Sources and references

- Defense Logistics Agency ASSIST: [MIL-PRF-8805K: Switches and Switch Assemblies, Sensitive, Snap Action, General Specification For](https://quicksearch.dla.mil/qsDocDetails.aspx?ident_number=7196){: rel="nofollow noopener noreferrer" }
- Occupational Safety and Health Administration: [29 CFR 1910.333: Selection and Use of Work Practices](https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.333){: rel="nofollow noopener noreferrer" }
- Wikipedia: [Miniature snap-action switch](https://en.wikipedia.org/wiki/Miniature_snap-action_switch){: rel="nofollow noopener noreferrer" }
