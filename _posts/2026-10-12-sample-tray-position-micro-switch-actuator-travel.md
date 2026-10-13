---
title: "Sample Tray Position Micro Switch Actuator Travel: Measurement and Verification"
description: "sample tray position micro switch actuator travel: Understand the operating idea, essential terminology, practical checks, limitations, and evidence."
date: 2026-10-12 17:55:05 +0800
category: Applications
tags:
  - sample tray position micro switch actuator travel
  - micro switches
  - Applications
author: editorial_team
---

A sample tray position micro switch actuator travel check should measure motion at the switch, not assume that tray displacement equals actuator movement. In designs that use a micro switch, the tray or its linkage moves the actuator; the switch’s operating and release positions are distinct checkpoints, and any movement beyond operation must remain within the permitted overtravel for that specific design. Measure from a fixed switch reference, then verify tray insertion and removal through repeated cycles. The applicable positions and travel limits must come from documentation for the particular switch design; no universal travel value can be inferred here.

## What sample tray position micro switch actuator travel means

Tray position detection describes the relationship between a tray’s location and a switch state change in a design that uses a micro switch. It does not mean that the switch directly measures tray position. The tray may contact the actuator itself, or its motion may pass through a lever, cam, or other linkage when the design includes one. Those parts transfer motion, so tray displacement and actuator travel are separate measurements.

Pretravel is the distance or angle through which the actuator moves from its free position to its operating position. Operating position is the point at which the switch operates. Overtravel is the distance or angle from the operating position to the extreme position to which the actuator may be moved. These definitions distinguish the movement that reaches operation from the additional movement permitted afterward. They do not supply a numerical travel limit for an unspecified switch.

Release behavior is a separate checkpoint. Release force is the force or torque to which force on the actuator must be reduced to permit the contacts to return to the unoperated position after operation. The return point therefore should not be treated as identical to the operating point. When checking tray detection, record insertion and withdrawal behavior separately rather than using the tray’s final stop as proof that both transitions occur as intended.

## Measure actuator travel from a fixed switch reference

Start by identifying a stable mounting datum on the switch and the point on the actuator where the tray mechanism applies motion. Also identify a repeatable tray reference position, such as its defined position before engagement and its intended seated position. The exact datum and reference locations depend on the assembly; the measurement should make them explicit rather than assume a tray-to-actuator ratio.

With the tray mechanism in its initial position, record the actuator’s free position relative to the switch datum. Move the tray slowly toward its intended position and observe the actuator at the point the switch operates. Record that actuator position and the tray position separately. The difference in actuator position from free position to operation is pretravel; it is not automatically the same distance as the tray moved.

Continue only through the mechanism’s intended movement, and record the actuator position at the intended mechanical stop. Compare its movement after operation with the documented permitted overtravel for the specific switch. If a lever, cam, or other motion-transfer part is present, note its position and contact point as well. Do not convert tray displacement into actuator travel unless the relationship is established for that mechanism.

Use a consistent measuring method and reference for each observation. The supplied evidence does not specify a measuring instrument, numeric tolerance, or universal mounting datum, so these must be determined from the assembly and the applicable switch documentation. The purpose is to distinguish free position, operating position, and the intended stop, not to infer an unsupported dimension.

## Set the detection point without exceeding permitted travel

Use the documented operating position and permitted overtravel for the particular switch design when assessing where detection should occur. The tray should cause the required actuator movement to reach operation, while the mechanism’s subsequent movement must remain within the switch’s documented travel limits. A tray that reaches its stop has not, by that fact alone, established that the actuator operated at the intended point or stayed within its permitted movement.

Account for the actual mounting, tray, and linkage tolerances in the assembly. Their combined variation can affect where the actuator reaches operation and how far it moves afterward. The accepted evidence supplies no universal tolerance allowance or numeric setting, so do not invent one. Use the relevant documentation and measured range for the specific mechanism to determine whether the operating point and end position remain acceptable across the expected variation.

Check release behavior independently. The actuator must be able to return to the unoperated position as the tray is withdrawn, according to the documented behavior for that switch design. Record the point at which the switch releases rather than assuming it releases at the same position at which it operated. If the tray or linkage prevents the required return, a successful insertion transition alone does not establish reliable position detection.

Do not use the switch as a mechanical hard stop unless the specific switch documentation permits the resulting actuator movement and loading. In particular, compare the measured actuator position at the assembly stop with the documented extreme permitted position. If that comparison cannot be made because the applicable limit is unknown, the travel boundary has not been verified.

## Verify sample tray detection through repeated movement

Use the same datum and measurement method for each cycle. Begin with the tray withdrawn and the actuator at its free position. Move the tray slowly toward its intended seated position, observing the tray reference and actuator separately. Record the actuator position at operation and the tray position at that event. Continue to the intended stop only as the mechanism’s documented limits allow, then record the actuator’s final position.

Withdraw the tray and observe the actuator’s return. Record the point at which the switch releases, keeping that observation separate from the insertion operating point. Repeat the insertion and withdrawal sequence. A single successful cycle does not show whether the operating and release points are consistent, whether the actuator returns each time, or whether the intended stop stays within permitted overtravel.

Where expected alignment or tolerance conditions can be checked from the assembly documentation, repeat the measurements across those conditions and record the results. Compare each observed operating position, release behavior, and final actuator position with the specific switch and mechanism requirements. The evidence provided does not define universal acceptable variation, a required number of cycles, or a test instrument; those details must not be assumed.

Finally, inspect the motion path for unintended mechanical loading, including whether the tray or linkage continues to force the actuator after operation. Relate that observation to the documented permitted overtravel. These checks establish what was observed during the measured movement; they do not prove every aspect of the switch or the surrounding equipment.

### Related guides

- [ball screw actuator home position micro switch replacement](/guides/ball-screw-actuator-home-position-micro-switch-replacement/)
- [bottling machine end of stroke micro switch](/guides/bottling-machine-end-of-stroke-micro-switch/)
- [automated guided vehicle home position micro switch location](/guides/automated-guided-vehicle-home-position-micro-switch-location/)
- [accelerator pedal position stop micro switch operating force](/guides/accelerator-pedal-position-stop-micro-switch-operating-force/)

## Common travel and positioning errors

A common error is treating the tray’s seated position as the switch’s operating position. They are different references: the tray reaches its position through the mechanism, while the actuator reaches its operating position through the motion transferred to it. Measure and record both rather than assuming that one establishes the other.

Another error is checking insertion only. The release point is distinct from operation, so a tray that produces an insertion transition may still fail to return the actuator as expected when withdrawn. Record the return behavior and compare it with the applicable documentation. Do not infer a required release distance or force when the specific value has not been supplied.

A single cycle also provides limited evidence. Repeated movement can reveal variation in observed operating or release positions, but the evidence pack does not set a universal cycle count or acceptance threshold. Use the documented requirements for the particular design to judge the measurements; do not turn an observed successful cycle into a general compatibility or reliability claim.

Finally, do not assume that a switch can serve as the tray’s stop. If the mechanism drives the actuator beyond its documented permitted movement, the intended tray position does not make that movement acceptable. When the applicable operating, release, or overtravel limits are unavailable, treat the travel assessment as unresolved rather than assigning a generic limit. For a sample tray position micro switch actuator travel assessment, the defensible conclusion comes from measured actuator positions, observed insertion and release behavior, and the specific design documentation together.

## Sources and references

- Defense Logistics Agency ASSIST: [MIL-PRF-8805K: Switches and Switch Assemblies, Sensitive, Snap Action, General Specification For](https://quicksearch.dla.mil/qsDocDetails.aspx?ident_number=7196){: rel="nofollow noopener noreferrer" }
