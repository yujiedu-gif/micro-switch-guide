---
title: "How a pull cord micro switch works and what to check"
description: "pull cord micro switch: Learn how cord movement actuates a micro switch, which travel and load limits matter, and how to verify repeatable operation safely."
date: 2026-07-22 09:00:00 +0800
category: Applications
tags:
  - pull cord micro switch
  - micro switches
  - Applications
author: editorial_team
---

A **pull cord micro switch** arrangement uses cord movement and a mechanical linkage to operate a switch actuator. The cord does not necessarily move the actuator by the same distance: levers, springs, and other linkage parts can change how force and motion reach the switch. The relevant checks therefore include both the linkage’s mechanical limits and the switch’s documented electrical contact rating.

This scope is a cord linkage that actuates a micro switch. It does not describe every pull cord device, nor does it establish that a particular switch or linkage is suitable for a specific machine. Selection depends on the actual mechanism, the required contact operation, and the conditions documented for the switch and its load.

## How a pull cord micro switch is actuated

Pulling or otherwise moving the cord applies force to the cord linkage. Depending on its design, the linkage may include a lever, spring, or other mechanical connection that transfers movement to the switch actuator. The actuator then moves toward the switch’s operating point. At that point, the contacts operate and change state.

The path matters because cord movement and actuator movement are not automatically equivalent. A lever may change the distance or force delivered at the actuator; other arrangements may behave differently. Do not use cord displacement alone as evidence that the switch has reached its operating point or stayed within its permitted motion. Check the linkage and the switch’s actuator information together.

Release behavior also depends on the mechanism. The switch may reset as the actuator is released, but the cord, linkage, and actuator must be able to return in the actual arrangement. A spring or other return element may affect this behavior, but its presence and performance cannot be assumed without documentation. Confirm that release produces the intended contact-state change rather than presuming that the cord’s return guarantees switch reset.

This distinction keeps the component scope clear: the cord is part of a mechanical actuation path, while the micro switch operates its contacts at a defined point in actuator motion. Pull cord equipment can use other mechanisms, so the presence of a cord does not establish that a micro switch is present. Identify the actual device and linkage from their documentation before applying switch-specific limits.

## pull cord micro switch travel and force limits

A switch’s actuator travel is described in terms that distinguish the motion before and after contact operation. Under MIL-PRF-8805K sections 6.5.14 and 6.5.16, **pretravel** runs from the actuator’s free position to its operating position. **Overtravel** runs from the operating position to the extreme permitted actuator position. These terms refer to actuator movement, not directly to cord displacement.

Compare the linkage’s movement with the switch’s documented operating point and permitted actuator travel. The linkage must be capable of reaching the required operating point, while its motion must not drive the actuator beyond the permitted extreme position. Because the cord may move a different distance from the actuator, measure or verify the relevant motion at the appropriate points in the linkage. Do not infer adequate operation or acceptable overtravel from a cord pull distance alone.

Also distinguish operating force from cord tension. MIL-PRF-8805K section 6.5.1 defines operating force, or actuating force, as the force or torque applied to the actuating mechanism to operate the contacts. Cord tension is applied to the cord and transmitted through the linkage; the force or torque at the switch actuator depends on that arrangement. The switch’s operating-force value therefore cannot, by itself, be treated as the required pull force at the cord.

Selection should account for actuation direction, the intended operating point, available pretravel, permitted overtravel, and release behavior. Check these against the switch and linkage documentation for the actual configuration. If the documentation does not establish the required movement or force relationship, treat that relationship as unresolved rather than assuming that the mechanism will operate reliably.

## Check electrical ratings separately from cord mechanics

Mechanical operation does not establish electrical suitability. A linkage that moves an actuator to its operating point does not show that the contacts are rated for the connected load or circuit conditions. Conversely, a documented contact rating does not establish that the cord mechanism delivers the right direction and amount of actuator movement.

Compare the actual switched load and circuit conditions with the contact rating documented for the switch. Keep the relevant conditions, including whether the circuit is AC or DC and the load type, aligned with the rating information. Do not infer suitability from cord tension, actuator motion, nominal voltage alone, or the fact that contacts change state. If the load or circuit conditions are unknown, the electrical selection cannot be verified from the mechanical behavior.

Treat the mechanical and electrical checks as independent. For the mechanical check, establish that the linkage reaches the operating point and remains within the permitted actuator travel. For the electrical check, establish that the documented contact rating covers the actual load and circuit conditions. Both need support from the appropriate documentation; success on one check does not substitute for the other.

Where the switching function is safety-critical, review it as part of the complete system design and applicable standards. This component-level discussion does not establish that a cord-actuated micro switch is a complete safety device, or that a particular arrangement meets a safety requirement. The system’s role, design, and applicable requirements need qualified review rather than inference from the switch’s mechanical operation or contact rating.

### Related guides

- [ball screw actuator home position micro switch replacement](/guides/ball-screw-actuator-home-position-micro-switch-replacement/)
- [bottling machine end of stroke micro switch](/guides/bottling-machine-end-of-stroke-micro-switch/)
- [automated guided vehicle home position micro switch location](/guides/automated-guided-vehicle-home-position-micro-switch-location/)
- [accelerator pedal position stop micro switch operating force](/guides/accelerator-pedal-position-stop-micro-switch-operating-force/)

## Verify repeatable operation safely

Before inspecting or checking the mechanism, ensure the equipment is isolated and safe to inspect under the applicable procedures. Do not expose yourself to energized circuits to confirm contact operation. If isolation, access, or the appropriate test procedure is uncertain, stop and have a qualified person determine the safe method.

With the equipment in a safe inspection condition, check that the cord and linkage move freely through the intended actuation and release. Observe whether the linkage reaches the switch operating point without forcing the actuator beyond its permitted travel. On release, check whether the mechanism returns and whether the switch produces the intended contact-state change. Repeat the movement as appropriate to determine whether operation is consistent, without treating a single successful movement as proof of suitability under all conditions.

Use appropriate test equipment and procedures to confirm contact-state changes without energizing exposed circuits. The method must fit the equipment and the measurement points; do not assume a particular test instrument or procedure where the documentation does not specify one. Keep the check focused on confirming the intended change of state and the return behavior, not on improvising a live electrical test.

Stop if the operation is inconsistent, the actuator travel appears excessive, the linkage does not return as intended, or relevant ratings and documentation are unknown. Resolve the mechanical and electrical questions separately before relying on the arrangement. The limits of a pull cord micro switch system are established by its documented actuator behavior, its actual linkage, and its contact rating for the load, not by cord movement alone.

## Sources and references

- Defense Logistics Agency ASSIST: [MIL-PRF-8805K: Switches and Switch Assemblies, Sensitive, Snap Action, General Specification For](https://quicksearch.dla.mil/qsDocDetails.aspx?ident_number=7196){: rel="nofollow noopener noreferrer" }
