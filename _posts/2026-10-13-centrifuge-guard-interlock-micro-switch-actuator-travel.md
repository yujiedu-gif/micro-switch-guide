---
title: "Centrifuge guard interlock micro switch actuator travel: what does it mean?"
description: "centrifuge guard interlock micro switch actuator travel: Understand the operating idea, essential terminology, practical checks, limitations, and evidence."
date: 2026-10-13 00:00:00 +0800
publication_date_only: true
category: Applications
tags:
  - centrifuge guard interlock micro switch actuator travel
  - micro switches
  - Applications
author: editorial_team
---

Actuator travel describes movement of the micro-switch actuator, not the total movement of a centrifuge guard. In a centrifuge guard interlock micro switch actuator travel depends on how guard motion reaches the switch, and it does not by itself establish the interlock’s electrical response or the guard’s safety function. The distinction matters because a guard may move through a linkage before that movement reaches the actuator, and the switch’s operating and release events are not the same event.

## What does centrifuge guard interlock micro switch actuator travel describe?

Actuator travel is the movement of the switch’s actuator between relevant positions. For a guard interlock, the guard may supply the mechanical input, directly or through an intermediate mechanism. The actuator’s movement is therefore only one part of a larger chain: guard movement, any linkage or cam, actuator movement, and the switch’s internal operation. It is not a measurement of total guard movement.

The terms used to describe travel distinguish points in that chain at the switch. Under the terminology in MIL-PRF-8805K sections 6.5.14 and 6.5.16, pretravel runs from the actuator’s free position to its operating position. Overtravel runs from the operating position to the extreme permitted actuator position. These definitions describe actuator movement, not a universal distance or a required guard displacement.

The interlock’s electrical behavior is a separate question. Travel terminology alone does not identify contact arrangement, wiring, control logic, or what the host equipment does when a contact changes state. Nor does actuator position alone establish whether the guard provides effective protection. Those conclusions require evidence about the particular switch and the complete equipment design.

## How guard motion reaches a micro-switch actuator

A possible mechanical path begins when the guard moves. Depending on the design, the guard may move the switch actuator directly, or its motion may be transmitted through a cam, lever, or other linkage. The actuator then moves the switch’s internal mechanism. This is a general description of a possible arrangement, not a claim that every centrifuge uses one particular mechanism.

The difference between guard movement and actuator travel is important when interpreting an observation. A guard can move while a linkage transmits only some of that movement to the actuator; alternatively, the actuator may be moved directly. Without information about the actual mechanism, a measurement of guard displacement cannot be treated as a switch-travel measurement. The path and the relevant measurement points must be established from the equipment documentation.

A micro switch’s presence also does not establish what its contacts do in the interlock. The available travel definitions do not identify whether a particular design uses normally open or normally closed contacts, how terminals are wired, or how the control system responds. Interlock designs differ, so a mechanical description should not be turned into an assumed circuit sequence or safety behavior.

This boundary keeps three questions distinct: how the guard moves, how that motion reaches the actuator, and what the equipment does with the switch’s electrical output. Travel addresses the mechanical portion at the switch. It cannot answer the other questions without design-specific evidence.

## Operating point, release point, and travel terms

The free position is the actuator position before operation in the terminology described by MIL-PRF-8805K section 6.5. Pretravel is the actuator movement from that free position to the operating position. The operating position marks the point associated with switch operation; it should not be confused with the release point, which is a separate event as the actuator returns.

Overtravel is movement after the operating position, extending to the extreme permitted actuator position where the design allows it. It is not an instruction to move the actuator farther, and it does not establish how much movement is permissible for an unidentified switch. The applicable specification sheet supplies device-specific travel requirements; those values must not be inferred from the general category “micro switch.”

The movement differential describes the separation between operating and release events in the terminology of MIL-PRF-8805K section 6.5. Because these are distinct events, a switch may operate at one actuator position and release at another. The difference between them is not the same as pretravel or overtravel. Each term refers to a different interval or event in the actuator’s movement.

The specification also distinguishes actuating force, releasing force, and the free and operating positions, in addition to movement differential, pretravel, and overtravel. These terms identify separate characteristics; naming them does not provide numerical values for a particular switch. Any stated travel figure needs to be tied to the applicable switch documentation and its stated conditions. There is no universal actuator-travel dimension that can be assigned to every micro switch or centrifuge guard arrangement.

## What actuator travel can, and cannot, tell you

Observed actuator movement can help describe the mechanical input reaching the switch, but it does not prove that the contacts changed state correctly. An audible click may indicate movement of a snap mechanism, but a click alone does not prove electrical continuity, correct wiring, or effective guard protection. Likewise, a contact-state observation does not by itself establish that the installed interlock or the equipment’s broader control system functions as intended.

If a system does not behave as expected, possible issue categories remain distinct. The mechanical input path may not deliver the intended movement; the switch contacts may have a problem; terminal identification or wiring may be incorrect; or the cause may lie elsewhere in the equipment. Travel terminology alone cannot distinguish among these possibilities. A symptom should not be treated as proof of one specific failure path without a suitable, documented check.

The same limit applies to an isolated switch check. A continuity observation concerns the isolated switch at a defined actuator state and under a stated test method. It is not a test of the installed circuit or the centrifuge’s complete safety function. Conversely, a switch-level observation that appears consistent with expected operation cannot prove the surrounding linkage, wiring, controls, or guard protection are correct.

For that reason, actuator movement, a click, and a contact observation should be interpreted narrowly. They may describe one part of the mechanism or circuit, but none alone establishes that the complete interlock is functioning safely. Avoid inferring a safe state from a travel value or a single observation.

### Related guides

- [accelerator pedal position stop micro switch actuator travel](/guides/accelerator-pedal-position-stop-micro-switch-actuator-travel/)
- [incinerator end of stroke micro switch maintenance](/guides/incinerator-end-of-stroke-micro-switch-maintenance/)
- [rotary indexing table guard interlock micro switch location](/guides/rotary-indexing-table-guard-interlock-micro-switch-location/)
- [security barrier open position micro switch wiring](/guides/security-barrier-open-position-micro-switch-wiring/)

## How to approach verification safely

Use the centrifuge’s documented service and safety procedures for any inspection or verification. Do not bypass or defeat the guard interlock. The applicable switch specification sheet is the reference for device-specific travel requirements; it should identify the relevant switch and measurement conditions. If those details are unavailable, a numerical travel limit cannot be established from the term “micro switch” alone.

Keep a switch-level check separate from an installed-system check. Any isolated-switch measurement needs a defined actuator state and a documented method, and its result applies to the switch under that test condition. It does not establish how the installed wiring or equipment control system behaves. System-level safety checks should be performed by qualified personnel using the equipment’s documented procedures.

The useful conclusion is limited but clear: actuator travel describes movement at the micro switch, while the route from guard to actuator and the interlock’s electrical and safety behavior depend on the particular design. A travel figure is meaningful only when associated with the identified switch and its specified measurement condition. Neither that figure nor an observed movement proves that the centrifuge guard interlock is safe or functioning as a complete system.

This concludes the explanation of centrifuge guard interlock micro switch actuator travel.

## Sources and references

- Defense Logistics Agency ASSIST: [MIL-PRF-8805K: Switches and Switch Assemblies, Sensitive, Snap Action, General Specification For](https://quicksearch.dla.mil/qsDocDetails.aspx?ident_number=7196){: rel="nofollow noopener noreferrer" }
