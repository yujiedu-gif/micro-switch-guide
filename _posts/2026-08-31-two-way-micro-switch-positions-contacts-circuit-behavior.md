---
title: "Two Way Micro Switch: Positions, Contacts, and Circuit Behavior"
description: "two way micro switch: Understand the operating idea, essential terminology, practical checks, limitations, and evidence needed for careful selection,."
date: 2026-08-31 09:00:00 +0800
category: Basics
tags:
  - two way micro switch
  - micro switches
  - Basics
author: editorial_team
---

A **two way micro switch** can describe a switch with two actuator positions, a changeover contact arrangement, or both. Those ideas are related, but they are not interchangeable: actuator position describes a mechanical condition, while terminal labels describe electrical contact relationships. The exact meaning for a particular component depends on its contact diagram and documentation.

Understanding that distinction helps map what a switch does without assuming that every device has the same terminal layout. In a changeover arrangement, the common terminal connects to one contact in one actuator state and may connect to another contact in the alternate state. A de-energized continuity check can help confirm those relationships, but its readings must be interpreted against the component’s diagram and the limits of the test.

## What does a two way micro switch mean?

The phrase “two way” is ambiguous without context. It may refer to two positions of the actuator, or it may refer to a changeover contact configuration. A switch can have two actuator positions without the phrase alone establishing its terminal arrangement. Likewise, seeing a changeover arrangement does not, by itself, describe every mechanical detail of the actuator.

An actuator position is the physical state reached by the part that moves or is pressed. A contact state is the electrical relationship between terminals in that position. A change in actuator position can change which terminals are connected, but the mechanical and electrical descriptions answer different questions: where is the actuator, and which contacts are continuous?

For generic changeover terminology, **COM** means common terminal, **NC** means normally closed terminal, and **NO** means normally open terminal. These labels identify terminal roles, not a universal physical layout. The supplied terminology applies to generic changeover arrangements; the exact device schematic should be checked before applying it to a particular switch.

The word “normally” also needs to be read in the context of the device’s contact definition and diagram. It should not be treated as a substitute for identifying the actuator state being tested. A diagram or documentation can establish how the manufacturer describes the states and which contacts correspond to them. If “two way” is used without that context, do not infer a specific terminal arrangement from the wording alone.

## Two way micro switch contact states and terminals

In a changeover contact arrangement, COM is the common terminal, and the circuit relationship from COM can change as the actuator moves between positions. In one state, COM may have continuity with NC; in the alternate state, COM may have continuity with NO. This is a conceptual description of the changeover relationship, not a claim that every switch has all three terminals or uses the same configuration.

The terminal labels are not names for the actuator positions. “NO” and “NC” describe contact relationships under the terminology used for the device, while a position describes where the actuator is. To map the states accurately, pair the documented actuator condition with the contact relationship shown in the diagram. Do not rename one actuator position “NO” or “NC” without checking that documentation.

A simple state record can keep the two kinds of information distinct:

| Actuator condition | Contact relationship to record |
|---|---|
| One documented position | Whether COM has continuity with NC, NO, or neither, as shown by the device diagram and confirmed by testing |
| Alternate documented position | Whether the COM relationship changes, and which terminal is continuous, according to the diagram and test |

This table is a recording method, not a universal switch specification. The available terminals, contact arrangement, and physical placement vary by design. Some devices may not use the generic three-terminal changeover arrangement described here. The terminal positions on a housing cannot be assumed from the labels alone.

A contact diagram is therefore central to interpreting a switch. Use it to identify the intended terminal relationships and state references. If the markings are unclear, or the diagram is unavailable, the terminal arrangement remains uncertain. A continuity check can provide observations, but it cannot establish an undocumented design intention or replace the device’s specifications.

## How to check a two way micro switch safely

A continuity check should be performed with power disconnected. Do not use a continuity measurement on an energized circuit. If the switch remains connected to other circuit paths, those paths may affect the meter reading. Isolate the switch from parallel circuit paths when needed so the observation reflects the switch rather than an alternate route through the surrounding circuit.

With the circuit de-energized and the switch suitably isolated, use the meter’s continuity mode to record the terminal pairs that show continuity in each actuator position. Identify the terminals from their markings or the device diagram; do not guess based on their physical location. Record the actuator position separately from the measured terminal pair so that mechanical state and electrical state are not conflated.

For a changeover arrangement with COM, NC, and NO terminals, check the relationship between COM and each other identified terminal in one documented actuator position, then repeat in the alternate position. Compare the results with the contact diagram. The expected mapping is the one documented for that device, not a generic assumption about how its terminals are laid out.

In-circuit readings can be misleading because another connected path may provide continuity even when the switch contacts being checked are not the path responsible for the reading. If the observation does not fit the diagram, the surrounding circuit may need to be separated from the measurement before drawing a conclusion. This is a limitation of the reading, not proof by itself that the switch has failed.

A continuity test also has a limited purpose: it records whether the meter detects continuity under the test conditions. It does not establish the switch’s full specification, suitability for a particular circuit, or condition under every operating circumstance. Treat it as one way to compare observed contact states with documented states. When terminal names, state references, or the diagram are unclear, consult the component documentation rather than infer the intended mapping from a single reading.

### Related guides

- [dual micro switch](/guides/dual-micro-switch/)
- [touch micro switch](/guides/touch-micro-switch/)
- [no nc micro switch](/guides/no-nc-micro-switch/)
- [normally open micro switch](/guides/normally-open-micro-switch/)

## When the observed behavior does not match the diagram

First confirm that the terminals were identified correctly and that the actuator reaches both positions used in the test. A mistaken terminal identification or an incomplete actuator movement can make a valid contact arrangement appear inconsistent. Recheck the diagram and keep the position descriptions separate from the terminal labels.

Next consider the test setup. Power must be disconnected, and parallel circuit paths may need to be isolated. A reading taken through connected components can reflect another route rather than the switch’s own contact relationship. Repeat the observation under appropriate de-energized test conditions and compare each result with the device diagram.

If the mismatch remains, worn, contaminated, or damaged contacts are possible causes, but one continuity reading is not enough to diagnose which condition is present. The observation establishes only that the measured behavior did not match the reference under the test conditions. It does not identify a specific fault or prove the switch’s overall condition.

When the readings remain inconsistent after terminal identification and test-path issues are checked, assess or replace the component according to the equipment’s service guidance. Keep the conclusion bounded to the evidence: document the actuator position, the terminals tested, the observed continuity, and the reference diagram. That record distinguishes a confirmed mismatch from an assumed explanation and avoids treating “two way” as a complete description of the switch.

This concludes the explanation of two way micro switch.

## Sources and references

- Defense Logistics Agency ASSIST: [MIL-PRF-8805K: Switches and Switch Assemblies, Sensitive, Snap Action, General Specification For](https://quicksearch.dla.mil/qsDocDetails.aspx?ident_number=7196){: rel="nofollow noopener noreferrer" }
- Wikipedia: [Miniature snap-action switch](https://en.wikipedia.org/wiki/Miniature_snap-action_switch){: rel="nofollow noopener noreferrer" }
