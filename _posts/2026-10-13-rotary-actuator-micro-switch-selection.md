---
title: "Rotary actuator micro switch selection: how to choose for an application"
description: "rotary actuator micro switch selection: Understand the operating idea, essential terminology, practical checks, limitations, and evidence needed for."
date: 2026-10-13 09:00:00 +0800
category: Selection Guides
tags:
  - rotary actuator micro switch selection
  - micro switches
  - Selection Guides
author: editorial_team
---

Selecting a rotary actuator micro switch selection begins by tracing how the rotating mechanism moves the switch actuator and identifying the contact event the circuit requires. The component is an electromechanical micro switch, not a rotary switch as a separate device. A cam, lever, or linkage may transfer rotary motion to a micro switch in some designs, but the arrangement and resulting behavior depend on the actual assembly.

Do not treat a rotary shape, visible movement, or audible click as proof of compatibility. Compare the mechanism’s movement with documented operating, release, and travel requirements, then check mounting geometry and the circuit’s actual load conditions. If those requirements or the interface remain undocumented, suitability is unresolved.

## What rotary actuator micro switch selection means

A micro switch is an electromechanical component whose actuator is moved by an external mechanism. In a rotary-actuated arrangement, the rotating input may contact the switch actuator directly or transmit movement through a cam, lever, or linkage. These are possible design arrangements, not features of every rotary mechanism or micro switch.

Selection therefore involves more than matching two component names. Trace four distinct elements: the rotating input, the motion delivered at the switch actuator, the switch’s operating and release events, and the circuit state required at those events. The host equipment’s control logic determines what a contact change does in the larger system; the presence of a micro switch alone does not establish that behavior.

Begin with the assembly’s actual documentation and geometry. Identify where the rotating part engages, what direction it moves the actuator, and which point in the rotation is intended to cause operation or release. Then compare the resulting actuator movement with the switch’s documented operating behavior and permitted travel. Do not infer a fixed relationship between rotation angle and actuator travel from the word “rotary.”

A complete decision also has an electrical side. The documented contact arrangement must correspond to the circuit’s required state at the relevant reference condition, and the electrical rating must apply to the circuit’s actual voltage, current, and load type under the stated conditions. Mechanical engagement cannot establish electrical suitability, and an electrical label cannot establish that the mechanism will operate correctly.

## Map the rotary motion to the micro switch actuator

First identify the rotating part that supplies movement and the surface or linkage that contacts the switch actuator. Record the contact path, direction, and range from the actual design or its documentation. Establish whether the input acts directly on the actuator or whether a cam, lever, or linkage changes the direction or amount of motion. Without that information, the relationship between rotation and actuator movement is unknown.

Next, determine which part of that movement is intended to operate the switch and which event is intended to release it. Operating and release are separate events. They should not be collapsed into a single assumed angle or position unless the switch and mechanism documentation establish that relationship. Where the documentation specifies operating and release behavior, compare the mechanism’s intended contact points with those requirements.

Travel terminology helps make this comparison precise. Under MIL-PRF-8805K sections 6.5.14 and 6.5.16, pretravel runs from the free position to the operating position, while overtravel runs from the operating position to the extreme permitted actuator position. These definitions describe actuator movement; they do not provide a travel value for an unspecified switch or establish how a particular rotary mechanism transfers motion.

Do not assume that rotation maps directly to a particular amount of actuator travel. A linkage, cam profile, contact location, or alignment may affect the movement delivered, but the applicable relationship must come from the actual design or documentation. If the available information gives only a rotary input and a switch name, it is not enough to establish that the actuator will reach its operating point, release as intended, or remain within permitted travel.

## Check mounting, operating events, and travel margin

Assess the installed geometry at the point of engagement. The rotating mechanism and switch must be positioned so that the intended parts meet along the documented contact path. Check the direction of approach and whether the parts remain aligned through the relevant portion of movement. A nominally similar actuator form does not prove that the mechanism can engage it correctly.

Account for variation in the assembled positions and movements using the dimensions and tolerances supplied for that design. Check for binding, missed engagement, or contact outside the intended path. The evidence here does not provide mounting dimensions, a universal tolerance, or a prescribed clearance. If the drawing or specification does not define the needed geometry, do not invent a fit or declare compatibility from appearance alone.

Compare the mechanism’s intended operating and release events with the switch’s documented behavior. The point at which the contacts operate is not the same event as the point at which they release. Where specifications describe the separation between these events or differential travel, consider it when evaluating whether the mechanism can both operate and release the switch in its intended cycle. Do not substitute an assumed rotation angle for documented event information.

Also check movement after operation. If the mechanism continues to move after the operating event, establish whether that movement remains within the switch’s documented permitted travel. The defined overtravel extends from the operating position to the extreme permitted actuator position, but no numerical limit is supplied here. Do not create a travel margin or assume that extra movement is harmless. If the available documentation does not resolve the post-operation movement, the mechanical selection remains unverified.

## Match contacts and electrical conditions to the circuit

Start from the circuit’s required state at the relevant mechanism position. Identify the switch’s contact arrangement only from documentation for the specific switch. COM means common when that terminal is documented; NO and NC describe contact state at a specified reference condition, not an unqualified promise about current flow. Do not infer terminal identity or state from appearance, a generic diagram, or the host equipment’s intended behavior.

Then compare the documented electrical rating with the circuit’s actual conditions, including voltage, current, and load type. MIL-PRF-8805K section 6.1.1 and applicable specification sheets treat rating values as requirements tied to stated load and test conditions, not universal switching capacities. Keep those conditions attached to the rating. A value specified for one load or test condition does not establish suitability for a different load or an unstated condition.

The switch’s contact action and the equipment’s response are separate questions. A contact change may feed into a control circuit, but the resulting behavior depends on that circuit and the equipment design. Do not infer a particular shutdown, alarm, or control response just because a rotary mechanism actuates a micro switch. Confirm that the documented contact state and rating match the actual circuit requirement, and leave unresolved circuit behavior to the applicable equipment documentation or qualified review.

### Related guides

- [spring plunger micro switch selection](/guides/spring-plunger-micro-switch-selection/)
- [micro switch freezing temperature selection](/guides/micro-switch-freezing-temperature-selection/)
- [micro switch contact gap selection](/guides/micro-switch-contact-gap-selection/)
- [micro switch dust ingress selection](/guides/micro-switch-dust-ingress-selection/)

## Verify rotary actuator micro switch selection in the intended assembly

Use the assembly documentation to define what should happen at the intended operating and release positions. Verification should address the motion delivered to the actuator, whether the documented events occur, and whether movement stays within documented limits. The available evidence does not establish a universal test procedure or authorize an improvised test on an installed circuit. If the safe test conditions or method are unclear, do not treat an informal check as proof of suitability.

A click or visible actuator movement can indicate motion, but it does not prove continuity, correct contact identification, correct wiring, or installed-system function. If an isolated-switch continuity test is appropriate, its meaning depends on a defined actuator state, correct terminal identification, and an appropriate measurement method. An isolated reading alone cannot establish that the switch is wired correctly or that the complete equipment operates as intended.

Keep the decision bounded by the evidence. A documented motion path, permitted travel, operating and release behavior, mounting geometry, contact arrangement, and rating under applicable load conditions can support a selection assessment when they match the intended assembly. Missing specifications or unresolved compatibility leave the conclusion open; obtain the needed documentation or qualified verification rather than assuming that a rotary form factor or click confirms a match. In short, rotary actuator micro switch selection depends on the documented interface and circuit conditions, not on the actuator description alone.

## Sources and references

- Defense Logistics Agency ASSIST: [MIL-PRF-8805K: Switches and Switch Assemblies, Sensitive, Snap Action, General Specification For](https://quicksearch.dla.mil/qsDocDetails.aspx?ident_number=7196){: rel="nofollow noopener noreferrer" }
