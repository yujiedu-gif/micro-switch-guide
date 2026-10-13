---
title: "cam follower micro switch selection"
description: "cam follower micro switch selection: Understand the operating idea, essential terminology, practical checks, limitations, and evidence needed for careful."
date: 2026-09-01 19:37:59 +0800
sitemap_omit_lastmod: true
category: Selection Guides
tags:
  - cam follower micro switch selection
  - micro switches
  - Selection Guides
author: editorial_team
---

Selecting a cam follower micro switch selection begins with the motion the cam must detect, not with a presumed roller or lever shape. Define the cam’s approach, travel, dwell, and return, then compare that motion with the candidate switch’s documented actuator limits and required switching events. The cam and follower provide mechanical input; they do not establish the switch’s contact arrangement, electrical rating, or effect on the host equipment.

There is no universal cam profile or switch specification to apply. A defensible choice depends on design-specific mechanical documentation, the circuit’s supply and load, and the installation conditions. If any of these are unknown, treat compatibility as unresolved rather than filling the gap with an assumed profile, travel value, or rating.

## Direct answer: select from cam motion and required switching events

Start by describing what the mechanism must detect: the cam’s direction of approach, the point at which switching is required, any dwell, and the event expected during return. These are requirements to compare with the documented behavior of a particular switch, not properties that can be inferred from a cam-follower arrangement alone.

The cam and follower transmit motion to the switch actuator. The actuator’s movement can change contacts, but the resulting contact state and host-equipment response depend on the switch design and circuit. Do not assume that a particular contact is normally open or normally closed, or that switching will cause a specific machine action, without applicable documentation.

Before choosing, obtain the candidate switch’s actuator geometry and travel boundaries, together with the cam’s movement and mounting geometry. Check that the intended engagement can produce the required events within those documented boundaries. A roller, lever, or other interface should not be selected by shape alone: its suitability depends on the actual motion path and the switch’s specified limits.

## cam follower micro switch selection: map cam motion to actuator travel

Treat cam displacement and switch actuator travel as related but distinct. The cam’s profile, alignment, direction, and contact path determine how motion reaches the actuator. The switch documentation determines the relevant positions and permitted travel. A cam’s physical movement therefore cannot, by itself, establish when a switch operates or releases.

Check the operating point and release point as separate events. Also check pretravel, overtravel, and differential travel as separate documented quantities. Under MIL-PRF-8805K sections 6.5.14 and 6.5.16, pretravel runs from the free position to the operating position, while overtravel runs from the operating position to the extreme permitted actuator position. These terms describe positions and movement; they do not supply values for an unspecified switch or cam arrangement.

The specification’s terminology distinguishes actuating force, releasing force, free position, operating position, movement differential, pretravel, and overtravel. Keep those quantities distinct when reading design documentation. In particular, do not treat the operating event, release event, and permitted actuator endpoint as interchangeable. Nor should one design’s travel information be applied to another without evidence that it is applicable.

Compare the required cam-driven movement with the documented switch positions and limits. The cam must reach the required operating event, and the return motion must be assessed against the documented release behavior. Where the design permits overtravel, verify that the mechanism remains within the specified permitted range. If the documents do not establish a needed boundary or event, the relationship remains unresolved; do not invent a usable travel allowance.

## Check mounting, alignment, and mechanical operating conditions

Compare the proposed mounting arrangement with the specific switch’s installation documentation. Trace the follower’s contact path through approach, dwell, and return, and check whether the arrangement can engage the actuator as intended without exceeding documented travel limits. A geometrically plausible fit is not proof that the mechanism meets its switching requirements.

Alignment matters because it affects how the cam’s motion is transmitted to the actuator. Assess the actual contact path and the positions at which the required operating and release events should occur. If cam position may vary, treat that variation as a requirement to compare with documented switch and installation constraints. Do not assign a tolerance or assume the switch can absorb variation unless the applicable documentation says so.

Also consider the mounting and mechanical constraints of the host mechanism. The evidence available here does not establish allowable side load, durability, repeatability, tolerance, or service life for an unspecified switch. Those characteristics must come from the documentation for the exact design and installation. If the needed constraint is absent, record it as an open selection item rather than assuming that a familiar follower shape or a successful static fit resolves it.

## Verify contact and load requirements independently

Mechanical fit and electrical suitability are separate checks. Identify the intended supply, load type, and circuit conditions, then compare them with the rating documented for the applicable switch and equipment. Use only a rating explicitly stated for the applicable current type, load, and test condition. An AC rating does not establish DC suitability, and a value stated for one load or condition does not establish suitability for another.

Confirm the contact arrangement and its reference condition from the switch documentation. The cam’s action does not identify terminals, establish a normal contact state, or specify the host circuit’s response. Use the documented connection diagram, terminal markings, circuit function, and permissible load for the exact switch and equipment rather than inferring terminal identity from physical layout.

Keep this check separate from the mechanical travel comparison. A switch may appear to engage the cam as intended while the documented electrical rating remains unknown or insufficiently matched to the stated circuit conditions. Conversely, an electrical rating alone does not establish that the cam can actuate the switch within its permitted mechanical limits. Resolve both evidence paths before treating the choice as supported.

## Validate the choice without overreading a test

Use a documented procedure to inspect the mechanical interface and assess actuator movement against the limits specified for the candidate design. The procedure and the applicable documentation determine what is a valid check. Do not substitute an assumed travel value or an informal impression of movement for a specified boundary.

If an isolated continuity test is supported by the applicable procedure, define the tested contact pair, the actuator state, the isolation condition, and the expected contact behavior from documentation. An isolated reading concerns the switch under those stated conditions. It does not establish correct installed wiring, permissible loading, or correct operation of the host mechanism.

A click may indicate movement, but it does not prove continuity, contact condition, correct terminal identification, or suitability for the circuit. Likewise, a continuity result at one defined state does not prove that the cam reaches the required operating and release events throughout its motion. Keep component observations separate from conclusions about the installed system. Circuit checks beyond the documented component procedure require qualified personnel.

### Related guides

- [spring plunger micro switch selection](/guides/spring-plunger-micro-switch-selection/)
- [micro switch freezing temperature selection](/guides/micro-switch-freezing-temperature-selection/)
- [micro switch contact gap selection](/guides/micro-switch-contact-gap-selection/)
- [micro switch dust ingress selection](/guides/micro-switch-dust-ingress-selection/)

## Selection information to gather before deciding

Record the cam’s direction and path of motion, required operating and release events, dwell, return motion, and relevant position variation. Document the mounting arrangement and follower contact path so they can be compared with the specific switch’s actuator geometry and travel limits. Obtain the applicable values and conditions for operating position, release position, pretravel, overtravel, and differential travel where specified.

Separately record the intended supply, load type, circuit conditions, required contact behavior, and operating environment. Obtain the applicable connection diagram, terminal markings, permissible-load information, and installation constraints for the exact switch and equipment. Do not transfer ratings across current types, loads, or test conditions.

A cam follower micro switch selection is supported only when the motion requirements, mechanical limits, electrical conditions, and installation environment can be compared with applicable documentation. If a required motion, contact behavior, rating, or environmental condition is unknown, defer the decision rather than infer compatibility. The unresolved item is a limit of the available evidence, not a reason to assume that a particular switch will work.

## Sources and references

- Defense Logistics Agency ASSIST: [MIL-PRF-8805K: Switches and Switch Assemblies, Sensitive, Snap Action, General Specification For](https://quicksearch.dla.mil/qsDocDetails.aspx?ident_number=7196){: rel="nofollow noopener noreferrer" }
- Occupational Safety and Health Administration: [29 CFR 1910.333: Selection and Use of Work Practices](https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.333){: rel="nofollow noopener noreferrer" }
