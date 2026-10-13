---
title: "How to select a power shear end of stroke micro switch"
description: "how to select a power shear end of stroke micro switch: Understand the operating idea, essential terminology, practical checks, limitations, and evidence."
date: 2026-10-13 11:27:16 +0800
category: Selection Guides
tags:
  - how to select a power shear end of stroke micro switch
  - micro switches
  - Selection Guides
author: editorial_team
---

A micro switch may serve as an end-of-stroke sensor in some power shear designs, but the machine category alone does not establish that it does. How to select a power shear end of stroke micro switch therefore starts with the actual mechanism and circuit, not a generic switch label. Identify what moves the actuator, which machine state is meant to trigger a contact change, and what electrical conditions the switch must handle. Then verify that the candidate’s documented mechanical, electrical, and installation limits fit those requirements. If the machine’s required control response or safety role is unclear, the evidence is not sufficient to complete selection by component specifications alone.

## How to select a power shear end of stroke micro switch: start with the machine’s actual mechanism

First confirm from machine documentation or qualified design information that the shear uses an electromechanical micro switch for end-of-stroke sensing. A miniature snap-action switch can change an electrical contact state in response to mechanical actuator movement and is commonly used for position or limit detection. That general use does not establish that any particular power shear has one, or reveal what its contact change does in the machine.

Trace the physical path of motion. Determine whether a cam, lever, or linkage contacts the switch actuator, and identify the point in the shear’s travel at which that interaction is intended to occur. The machine’s end-of-stroke event is specific to its design; the equipment name does not define the actuator geometry, switching point, or resulting control response.

Use the machine’s control information to establish the relevant operating state and the expected response when the contact changes. Keep that response distinct from the switch itself: a switch supplies a contact change, while the surrounding circuit determines what follows. Do not infer a stop function, contact state, or safety function solely from the presence of a switch.

## Match actuator motion to the end-of-stroke mechanism

Compare the shear’s actual motion with the candidate switch’s documented actuator arrangement. Check the approach direction, point of contact, and whether the mechanism engages the intended part of the actuator. A switch that appears physically similar is not established as suitable unless the documented motion and switching event match.

Where specifications define travel, distinguish the events and limits. Under MIL-PRF-8805K sections 6.5.14 and 6.5.16, pretravel runs from free position to operating position, while overtravel runs from operating position to the extreme permitted actuator position. These terms describe different portions of actuator motion. Use documented operating-point, release-point, pretravel, and permitted-overtravel information only when it applies to the candidate and installation; the available general definitions do not establish the values needed for a particular shear.

Check that the actuator is reached in the intended way and that alignment supports the specified movement. Do not assume that continued machine motion after operation is acceptable: compare it with the documented travel limits and the machine’s actual mechanism. A click may indicate movement of a snap mechanism, but it does not prove that the electrical contact changed as required. Mechanical engagement and electrical operation are separate checks.

## Match the micro switch electrical rating to the real circuit

Identify the actual circuit conditions before comparing ratings. Establish the documented supply, load type, switching duty, and required contact arrangement from the machine design or other qualified information. Do not substitute an assumed control circuit for this evidence, and do not treat a switch’s label as a complete description of its suitability.

Rating values are specification-sheet requirements tied to stated load and test conditions, including under MIL-PRF-8805K section 6.1.1 and applicable specification sheets. Compare the candidate’s documented rating with the circuit conditions that actually apply. AC and DC conditions, or different load types, are not interchangeable unless the relevant documentation establishes that they are. A rating without its load and test conditions does not by itself resolve the match.

Confirm terminal and contact meanings from the exact switch’s connection diagram and markings. COM means common, and NO and NC describe contact states only when the contact arrangement and reference condition are documented. Do not infer terminal identity from physical position or assume a particular normal state from the end-of-stroke application. The expected transition must come from the machine’s control information and the candidate’s documented contact arrangement.

Use the connection diagram, terminal marking, circuit function, and permissible load documented for the exact switch and equipment. If any of these are unavailable or conflict, the electrical selection remains unresolved. This is a selection boundary, not a basis for rewiring or changing the machine circuit.

## Check mounting, travel, and installation conditions

Verify mounting dimensions and actuator access against evidence for the actual shear installation and candidate switch. The available general information does not establish dimensions or mounting compatibility for a particular machine or model. Confirm that the mounting position allows the intended mechanism to reach the actuator without relying on an assumed layout.

Review the full actuator movement at the intended end-of-stroke event against documented travel limits. The operating position and the extreme permitted actuator position are not the same reference. Ensure the installation does not require movement beyond the candidate’s stated limit or hold the actuator in a condition that its documentation does not support. If those limits or the mechanism’s motion are unknown, the match cannot be verified from the switch name alone.

Check environmental constraints using documented limits for the candidate and installation. Do not infer sealing, temperature capability, or a protection level from appearance, equipment category, or a generic switch description. A potentially suitable actuator and electrical rating do not settle whether the installation conditions are within the switch’s specified limits.

### Related guides

- [spring plunger micro switch selection](/guides/spring-plunger-micro-switch-selection/)
- [micro switch freezing temperature selection](/guides/micro-switch-freezing-temperature-selection/)
- [micro switch contact gap selection](/guides/micro-switch-contact-gap-selection/)
- [micro switch dust ingress selection](/guides/micro-switch-dust-ingress-selection/)

## Verify the end-of-stroke function before final selection

Before finalizing a choice, use machine control information to state what contact transition is expected at the specified end-of-stroke state. Confirm that the candidate’s documented contact arrangement and electrical ratings correspond to that requirement and the actual circuit conditions. Also confirm that the mechanical event reaches the intended operating point without exceeding documented travel limits.

Keep the component requirement separate from the machine’s control logic. A micro switch contact change does not, by itself, establish the machine’s response or prove that a separately defined safety function is met. The selection decision depends on evidence for the switch and the machine design together; a component label or mechanical click cannot establish the complete function.

If the circuit conditions, required contact state, installation limits, or safety role remain unclear, pause selection and refer the unresolved requirements to qualified engineering personnel. How to select a power shear end of stroke micro switch cannot be answered reliably by choosing from a generic label when the machine-specific motion and control requirements have not been established.

## Sources and references

- Defense Logistics Agency ASSIST: [MIL-PRF-8805K: Switches and Switch Assemblies, Sensitive, Snap Action, General Specification For](https://quicksearch.dla.mil/qsDocDetails.aspx?ident_number=7196){: rel="nofollow noopener noreferrer" }
- Occupational Safety and Health Administration: [29 CFR 1910.333: Selection and Use of Work Practices](https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.333){: rel="nofollow noopener noreferrer" }
- Wikipedia: [Miniature snap-action switch](https://en.wikipedia.org/wiki/Miniature_snap-action_switch){: rel="nofollow noopener noreferrer" }
