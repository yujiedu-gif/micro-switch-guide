---
title: "3 way micro switch: What Its Three Terminals Do"
description: "3 way micro switch: Learn what its three terminals do, how common, normally open, and normally closed contacts work, and how to verify connections safely."
date: 2026-09-30 09:00:00 +0800
category: Basics
tags:
  - 3 way micro switch
  - micro switches
  - Basics
author: editorial_team
---

A 3 way micro switch usually refers to a three-terminal changeover contact arrangement, not a switch with three operating positions or three independent poles. Its terminals provide one common connection that changes between two contact paths as the actuator moves. You can identify the paths by comparing continuity between terminal pairs in the released and actuated states, with the switch disconnected from power.

The labels COM, NO, and NC describe the terminals and their contact relationship in a specified reference state. Markings and physical layouts can vary, so do not identify a terminal from its location alone. Check the exact switch documentation or verify the contact pattern with an appropriate meter before drawing conclusions about the component. This test identifies contact relationships; it does not establish how the switch should be wired into an appliance or other circuit.

## What does a 3 way micro switch mean?

In this context, “3 way” describes three terminals arranged as a changeover contact: a common terminal and two alternative contact paths. It does not, by itself, mean that the switch has three separate poles or three operating positions. Terminal count, pole count, and actuator positions are different characteristics, and the phrase alone does not settle every detail of a particular switch’s construction.

A miniature snap-action switch can change an electrical contact state in response to mechanical actuator movement and is commonly used for position or limit detection. That general function does not establish a particular switch’s wiring, application, or suitability for a circuit. Confirm that the component actually has the three-terminal changeover arrangement before applying the explanations below. Its documentation or a suitable de-energized test can help verify that arrangement.

For a changeover contact, COM is the common terminal. NO means normally open, and NC means normally closed. “Normally” refers to the contact state at the specified reference condition, usually described for the actuator released in the contact-state mapping below. It is not a general claim about current flow in an installed circuit. The exact device marking or schematic controls if it differs from this generic terminology.

## How the 3 way micro switch terminals connect

In a typical three-terminal changeover arrangement, COM is the shared contact that connects to one of the other two terminals at a time. The contact path changes as the actuator moves. NO and NC name the alternative paths by their relationship to the stated reference condition; they are not names for separate operating positions.

With the actuator released, the expected continuity relationship is between COM and NC. COM and NO are expected not to have continuity in that state. When the actuator is pressed or otherwise actuated, the expected relationship changes: COM and NO have continuity, while COM and NC do not. These are the generic state relationships for the changeover terminology. Verify the specific component’s documentation or test its contacts rather than assume the arrangement from the words “3 way.”

This mapping also explains how to recognize COM by observation: it is the terminal that forms a continuity path with one of the other terminals in one actuator state and with the remaining terminal in the other state. The actuator state matters. A reading taken in only one state shows just one part of the pattern and may not distinguish all three terminals.

## How to identify terminals with a continuity test

Only make continuity measurements with the switch disconnected from power. Where practical, isolate it from other circuit paths so they do not affect the meter’s readings. Do not use continuity mode on an energized circuit. If the component is part of equipment and cannot be safely isolated, stop rather than test it in place.

Use the meter’s continuity or resistance mode and compare the three possible terminal pairs: first-to-second, first-to-third, and second-to-third. Record which pairs show continuity with the actuator released. Then compare the same pairs with the actuator actuated. Keep the two states separate in your notes; the change between them is what identifies the changeover pattern. Do not force the actuator beyond its intended travel.

For a typical changeover contact, one terminal pair has continuity in the released state, and a different pair has continuity in the actuated state. The terminal common to those two pairs is COM. Of the other two terminals, the one connected to COM when the actuator is released is NC; the one connected to COM when the actuator is actuated is NO. This identification depends on observing both states, not on the physical order of the terminals.

Treat this as a way to identify contact relationships, not as a complete assessment of the switch or circuit. A continuity result alone does not establish an intended wiring function, a load capability, or the behavior of the equipment containing the switch. If the observed pattern does not match the expected changeover relationships, do not assign terminals by guesswork. Check the exact switch schematic or documentation and resolve the discrepancy before relying on the result.

### Related guides

- [dual micro switch](/guides/dual-micro-switch/)
- [touch micro switch](/guides/touch-micro-switch/)
- [no nc micro switch](/guides/no-nc-micro-switch/)
- [normally open micro switch](/guides/normally-open-micro-switch/)

## Safety and limits when checking a 3 way micro switch

Never use a continuity meter on an energized circuit. Disconnect the component from power before testing, and isolate it from other circuit paths where practical. A meter reading made while other circuit paths remain connected may not represent the switch contacts alone. If you cannot establish a de-energized, suitable test condition, do not proceed with the measurement.

Operate the actuator only through its intended movement; do not force it beyond its travel. Compare readings in the released and actuated states, and avoid treating a single reading as proof of the terminal arrangement. Markings or terminal placement may offer clues, but the exact device marking or schematic controls. Confirm the contact pattern rather than infer it from appearance.

If the readings remain ambiguous or do not fit the expected pattern, consult the component documentation or a qualified technician. Do not turn a terminal identification result into a wiring instruction for a particular appliance or vehicle. Identifying COM, NO, and NC describes the contact paths under the tested conditions; it does not determine how an external circuit should use them. When that purpose is unknown, leave it unresolved rather than assume a wiring function.

In short, a 3 way micro switch in this usage has a three-terminal changeover arrangement: COM connects to NC with the actuator released and to NO when actuated. Compare all terminal pairs in both states, with the switch disconnected from power, to identify the common terminal and the two paths. Verify the specific component’s documentation, and do not infer an application or wiring function from terminal identification alone.

## Sources and references

- Defense Logistics Agency ASSIST: [MIL-PRF-8805K: Switches and Switch Assemblies, Sensitive, Snap Action, General Specification For](https://quicksearch.dla.mil/qsDocDetails.aspx?ident_number=7196){: rel="nofollow noopener noreferrer" }
- Wikipedia: [Miniature snap-action switch](https://en.wikipedia.org/wiki/Miniature_snap-action_switch){: rel="nofollow noopener noreferrer" }
