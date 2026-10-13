---
title: "micro switch: How It Works and How to Verify Its Terminals"
description: "micro switch: Understand the operating idea, essential terminology, practical checks, limitations, and evidence needed for careful selection,."
date: 2026-10-12 17:55:05 +0800
category: Basics
tags:
  - micro switch
  - micro switches
  - Basics
author: editorial_team
---

A micro switch changes contact state when movement at its actuator triggers an internal switching mechanism. In a snap-action design, the contacts move rapidly relative to the actuator, so the electrical transition is not simply a gradual copy of the external motion. You can verify the contact behavior with an unpowered continuity check, provided the switch is safely disconnected and isolated from other circuit paths. The result describes the tested switch and actuator states; it does not, by itself, establish how an entire appliance or control system behaves.

## What a micro switch is and what snap action means

A micro switch is a compact electromechanical switch. The term is often used for a miniature basic switch, and “snap action” describes a particular contact mechanism rather than every device called a switch. In a snap-action mechanism, contact speed is relatively independent of the speed of the actuating mechanism. This means that slow actuator movement can trigger a comparatively rapid contact transition.

The external actuator is the part moved by a lever, cam, button, or other mechanical input. Its movement operates the switch mechanism, which changes the contacts’ electrical relationship. The actuator and the contacts are related, but they do not move as one continuous electrical measure: the mechanism determines when the contact transition occurs.

The component must also be distinguished from the equipment around it. A machine or appliance may use a micro switch as one part of a larger control arrangement, but the switch’s contact change does not establish what the system will do. The surrounding circuit and control design determine the result. Nor does the presence of a moving door, pedal, or other input prove that a particular equipment category uses a micro switch; arrangements vary.

## How a micro switch changes contact state

The switching sequence begins when an external mechanism moves the actuator. Force applied to the actuating mechanism to operate the contacts is called operating force. As the actuator travels, it reaches an operating position where the mechanism changes the contact state. In a snap-action design, that contact change occurs rapidly relative to the actuator’s movement.

The actuator’s movement before reaching the operating position is pretravel. It is the distance or angle from the free position to the operating position. If the design permits the actuator to move farther, overtravel is the distance or angle between the operating position and the extreme position to which the actuator may be moved. These terms describe different portions of travel; neither gives a universal value for all switches.

When the applied force is reduced after operation, the contacts can return to the unoperated position. The force or torque to which force on the actuator must be reduced to permit that return is called release force. Release behavior is a separate part of the switching cycle, not simply another name for operating force. A standard definition of snap action does not supply a particular switch’s operating position, release behavior, force, or travel values.

The operating and return transitions may occur at different actuator positions. Their separation is associated with differential movement, but the supplied definitions do not establish a release-point specification or a numerical differential value. Do not infer either from the component name or from seeing the actuator move. Exact travel and force depend on the particular design and its documentation.

## Common, normally open, and normally closed terminals

On a documented changeover arrangement, COM means common, NC means normally closed, and NO means normally open. “Normally” refers to the contact state with the actuator in its unoperated condition. It does not mean a fixed wire color, and it is not an unconditional statement about current flow in an installed circuit.

In that reference condition, the common terminal is associated with the contact arrangement that provides the normally closed path. When the mechanism operates, the common terminal may instead connect to the normally open terminal. This describes the switch’s contact states, not the function of the equipment. The actual circuit determines what an open or closed contact causes elsewhere.

Markings and terminal layouts are not universal. A label or apparent physical position should not be treated as proof of the terminal identity for an unidentified switch. Check the specific switch’s markings and schematic, when available, and compare them with a direct test. If the actual contact arrangement is undocumented or the readings do not make sense, leave the identity unresolved rather than assuming a standard pinout.

## How to verify a micro switch with a continuity check

A continuity check can compare contact pairs in the switch’s unoperated and operated states. The switch must be disconnected from power and isolated from parallel circuit paths before the measurement. Do not use a meter’s continuity mode on an energized circuit. If you cannot safely disconnect and isolate the switch, stop rather than testing it in place.

With the switch isolated, use a continuity tester or a multimeter set to continuity. First record the actuator’s unoperated state, then check the terminal pairs and note which pair shows continuity. Move the actuator through its operating action and check the same pairs again. The useful observation is which pair changes state between the two defined actuator conditions. Avoid treating an unspecified meter reading as a universal pass or fail threshold.

Compare the observed change with the switch’s markings or relevant circuit information. The test can help identify a common terminal and the contacts associated with normally open and normally closed states when the arrangement and readings support that interpretation. If markings, documentation, and measurements conflict, do not force an identification from wire color or terminal location alone.

This procedure verifies only the isolated switch under the tested conditions. It does not test the rest of the circuit, establish that an installed system is safe, or show that the switch is suitable for a particular electrical load. A continuity result also does not supply missing ratings or prove performance under operating conditions. Keep the measured actuator state and isolation condition attached to any conclusion.

## What varies between micro switch designs

Operating force and travel are design-specific. Pretravel describes movement from free position to operating position; overtravel describes permitted movement beyond the operating position to the actuator’s stated extreme position. Release force concerns the force or torque reduction that permits the contacts to return to the unoperated position. These definitions do not provide universal numerical limits, and one switch’s values cannot be assigned to another based only on the shared term “micro switch.”

Electrical ratings and load suitability also require evidence for the actual switch and circuit. A continuity check identifies a contact-state change under the test conditions; it does not determine an electrical rating or establish compatibility with a load. Likewise, environmental protection is construction-specific. The component name alone does not establish sealing or protection against a particular environment.

Use the documentation for the exact switch to resolve its terminal arrangement and specified mechanical or electrical parameters. If the identity or applicable conditions are unknown, those details remain unknown. A general explanation of snap action cannot substitute for model-specific information.

### Related guides

- [dual micro switch](/guides/dual-micro-switch/)
- [touch micro switch](/guides/touch-micro-switch/)
- [no nc micro switch](/guides/no-nc-micro-switch/)
- [normally open micro switch](/guides/normally-open-micro-switch/)

## What to check before interpreting or selecting a micro switch

Start by confirming the contact behavior needed for the task. Use the individual switch’s schematic or markings, and, when safe, compare them with the isolated continuity results for unoperated and operated actuator states. Do not infer a contact arrangement from colors, a similar-looking component, or the behavior of unrelated equipment.

Next, check whether the mechanical interaction is documented for the actual design. The external actuator must reach the operating position, and any movement beyond it must be considered against the design’s permitted overtravel. Operating force, pretravel, operating position, and release behavior are not interchangeable measures. If the relevant values are absent, the suitability of the mechanical interaction cannot be concluded from the general switch description.

Finally, compare the actual switch’s electrical ratings and environmental protection information with the intended use conditions. The test described here does not answer those questions. A micro switch changes contact state through its mechanism, but its role and effect depend on the specific component and the surrounding circuit. Confirm those details before interpreting its behavior or selecting it for an application.

## Sources and references

- Defense Logistics Agency ASSIST: [MIL-PRF-8805K: Switches and Switch Assemblies, Sensitive, Snap Action, General Specification For](https://quicksearch.dla.mil/qsDocDetails.aspx?ident_number=7196){: rel="nofollow noopener noreferrer" }
- Wikipedia: [Miniature snap-action switch](https://en.wikipedia.org/wiki/Miniature_snap-action_switch){: rel="nofollow noopener noreferrer" }
