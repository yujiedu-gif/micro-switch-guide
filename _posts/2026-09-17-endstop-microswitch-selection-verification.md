---
title: "Endstop microswitch: How to Select and Verify a Travel-Limit Switch"
description: "endstop microswitch: Understand the operating idea, essential terminology, practical checks, limitations, and evidence needed for careful selection,."
date: 2026-09-17 09:00:00 +0800
category: Selection Guides
tags:
  - endstop microswitch
  - micro switches
  - Selection Guides
author: editorial_team
---

An **endstop microswitch** detects when a moving mechanism reaches a defined travel boundary. Selecting one involves more than matching its actuator to the moving part: the mounting geometry, operating and release behavior, and electrical ratings must all suit the actual setup. Verification should check both the switch’s contact changes and the installed mechanism’s movement in both directions. The switch detects a condition; the surrounding circuit or control system determines how the machine responds. Keep those roles distinct when setting a travel limit.

## What an endstop microswitch does

An endstop microswitch is a micro switch used to detect a mechanical travel limit. As a moving part contacts the actuator, the switch’s contacts change state. That change can provide an input to a surrounding circuit or control system, but it does not, by itself, define how or when the machine stops. Stopping behavior depends on the surrounding circuit or control system.

First determine which contact arrangement the circuit requires: normally open, normally closed, or changeover. For generic changeover terminology, **COM** means common, **NO** means normally open, and **NC** means normally closed. These symbols do not establish the exact terminal layout of a particular device, so check its schematic rather than assuming a terminal position from a label alone.

The selection boundary is therefore twofold: the switch must change state at the intended mechanical boundary, and its contacts must suit the circuit that reads or uses that change. Neither the switch’s physical action nor a terminal label alone establishes the machine’s complete stopping response.

## Choose an endstop microswitch actuator and mounting approach

Match the actuator to the moving part’s contact surface and approach direction. A lever, roller, or plunger presents a different contact geometry; the suitable choice depends on how the moving part meets the actuator and whether that contact can be aligned repeatably. The component category alone does not establish which geometry fits a particular mechanism.

Plan the mounting so the moving part reaches the actuator as intended rather than striking it or pushing it from the side. Check alignment through the approach, secure the mounting, and consider whether the actuator can be inspected. Allow physical clearance for the mechanism and access for inspection, but do not assume a particular clearance dimension without the applicable device and mechanism specifications.

During setup, observe whether the mechanism actuates the switch consistently and whether reverse movement allows the actuator to return. Contact geometry and approach direction influence that physical interaction, while the device’s permitted travel remains a separate specification to verify. Do not treat a visually aligned actuator as proof that its travel limits are satisfied.

The mounting approach should let the switch detect the intended boundary before the mechanism reaches its hard stop. That timing must be checked against the switch’s operating behavior and the mechanism’s usable travel, not inferred from actuator shape alone.

## Endstop microswitch travel limits and operating points

Travel terms describe different parts of switch action. **Pretravel** is the distance or angle the actuator moves from its free position to its operating position. The operating position is where actuation occurs. **Overtravel** is the distance or angle between that operating position and the extreme position to which the actuator may be moved. It describes permitted actuator movement beyond operation, not additional machine travel that is automatically safe or usable.

After operation, the switch releases when the actuator returns far enough for the contacts to return to the unoperated position. The **release point** refers to that return point. **Differential travel**, also called movement differential, is the distance or angle the actuator travels from the operating position to the releasing position. Release force is different: it is the force or torque to which force on the actuator must be reduced to permit the contacts to return to the unoperated position after operation.

These distinctions matter when setting the machine’s usable travel limit. Arrange the mechanism so actuation occurs before the machine reaches its hard stop, and ensure the actuator is not driven beyond the device’s permitted travel. Numerical travel limits are device-specific requirements of the applicable specification sheet; do not infer them from the component category.

Check operation in both directions: approach the limit and note where the contacts change state, then move back and confirm where they return to the unoperated state. The operating and release points need not coincide, so checking only the approach does not establish return behavior. Confirm that the switch releases reliably through the intended return movement and that the mechanism does not exceed permitted actuator travel.

## Check electrical ratings against the circuit

Compare the switch’s electrical ratings with the circuit’s actual voltage, current, and load type. A rating alone does not guarantee suitability: the circuit conditions must be checked against the applicable rating for the switch and the load being switched. Do not assume that matching a voltage or current value in isolation establishes that the device is appropriate for the complete circuit.

Identify whether the load is resistive or inductive. Inductive loads can impose different switching demands than resistive loads, so load type belongs in the comparison rather than being treated as interchangeable. If the applicable rating or conditions are not established, electrical suitability remains unresolved; do not fill that gap by inference.

Also verify that the required contact configuration matches the circuit and check any electrical-isolation requirements before installation. Confirm the exact device schematic and specifications rather than relying on generic COM, NO, or NC terminology to establish device-specific connections. The switch’s mechanical suitability and its electrical suitability are separate checks; passing one does not establish the other.

### Related guides

- [inline micro switch](/guides/inline-micro-switch-suitability/)
- [access hatch open position micro switch contact rating](/guides/access-hatch-open-position-micro-switch-contact-rating/)
- [micro switch salt spray](/guides/micro-switch-salt-spray/)
- [dpdt micro switch](/guides/dpdt-micro-switch-contact-operation-selection/)

## Verify an endstop microswitch before use

Begin with the circuit de-energized and isolated before performing a continuity check. Use a multimeter to check the expected contact states at rest and during manual actuation. Identify the relevant terminals from the device schematic, then observe whether the contacts change state as the actuator moves and return to the unoperated state when it releases. Do not infer exact contact behavior or terminal placement from generic symbols alone.

Next, verify the installed mechanical interaction through the intended travel range. Move the mechanism toward the limit and check that the switch actuates before the hard stop. Move it back and check release behavior as well as the return contact state. Confirm that the actuator remains within its specified travel and that the mounting holds the intended alignment during this movement. The applicable specification sheet supplies device-specific travel limits; the component category does not.

Finally, confirm that the surrounding control circuit responds as designed to the switch-state change. This system check is distinct from the manual continuity test: continuity verifies contact behavior, while the installed check covers the mechanical interaction and the surrounding circuit’s response. If either the switch action or the system response is not as intended, the verification is incomplete. An endstop microswitch can indicate a travel boundary, but the surrounding circuit or control system determines the machine’s stopping behavior.

## Sources and references

- Defense Logistics Agency ASSIST: [MIL-PRF-8805K: Switches and Switch Assemblies, Sensitive, Snap Action, General Specification For](https://quicksearch.dla.mil/qsDocDetails.aspx?ident_number=7196){: rel="nofollow noopener noreferrer" }
- Wikipedia: [Miniature snap-action switch](https://en.wikipedia.org/wiki/Miniature_snap-action_switch){: rel="nofollow noopener noreferrer" }
