---
title: "What Does Micro Switch NC Mean?"
description: "micro switch nc: Understand the operating idea, essential terminology, practical checks, limitations, and evidence needed for careful selection,."
date: 2026-09-06 09:00:00 +0800
category: Basics
tags:
  - micro switch nc
  - micro switches
  - Basics
author: editorial_team
---

# Understanding the NC Contact State of a Micro Switch

A **micro switch nc** contact is closed when the switch is in its normal, unactuated state. In a changeover switch, this means there is a closed contact path between the common terminal and the normally closed terminal before the switch is actuated. The name describes the contact state, not whether a machine is powered or where an installed mechanism happens to rest.

That distinction matters when checking a switch. A switch that is held down by an installed part may be actuated even if that is the mechanism’s resting position. Its NC path can therefore be open in the installed condition. To check the switch itself, identify the correct contact pair and test it with power disconnected, comparing the unactuated and actuated states.

## What does micro switch nc mean?

NC means “normally closed.” For a micro switch, the term identifies a contact pair that is closed in the switch’s normal, unactuated state. In the common changeover terminology, COM is the common terminal and NC is the normally closed terminal. The NC path is the connection between those two terminals; it is not a statement that every terminal on the switch is connected at once.

“Normal” refers to the switch’s unactuated state. It does not necessarily mean the position that a lever, door, cam, or other part occupies when a complete mechanism is at rest. Installation can press or otherwise actuate the switch. If that happens, the switch has changed contact state even though the surrounding mechanism may not be moving.

Contact state also differs from circuit power. A closed contact pair describes an electrical connection through the switch. It does not, by itself, establish whether the surrounding circuit is energized, what voltage is present, or whether current is flowing. Those questions depend on the circuit and its power conditions.

Terminal markings and diagrams can help identify the pair, but symbols and terminal arrangements should be checked against the exact device schematic. Do not assume that physical terminal position alone identifies COM or NC. Once the pair is identified, the defining check is whether COM and NC are closed with the switch unactuated.

## How the NC contacts change when a micro switch is actuated

A changeover micro switch has a common contact that connects through one path in the unactuated state and changes to the alternate path when the switch is actuated. The NC path is closed in the unactuated state. When the switch changes over, that NC path opens; where an alternate contact is present, the common contact changes to that path.

This describes the contact transition, not the position of an installed machine part. The actuator can be held in the actuated condition by the surrounding mechanism. In that case, the switch’s NC path is open while the mechanism remains stationary. Conversely, a component that looks mechanically at rest does not establish the switch’s electrical state without confirming whether the actuator is actually unactuated.

Snap action is defined as contact action in which the speed of the moving contacts is relatively independent of the speed of the actuating mechanism. This definition describes the relationship between contact motion and actuator motion. It does not supply a particular switching point, travel distance, or operating speed for an unspecified switch.

The switching point and mechanical travel depend on the switch design. No exact travel, force, or changeover position can be inferred from the NC designation alone. The useful interpretation is limited: the NC contact pair is closed in the unactuated state and opens when the switch changes over. If a test gives a different result, first confirm the contact pair and the switch’s actual mechanical state before interpreting the observation.

## How to verify a micro switch NC contact pair

For a component-level check, disconnect power and isolate the switch from the circuit before testing. This avoids treating circuit power or connected wiring as part of the switch’s own contact state. Use a continuity tester only after the circuit has been made power-free and the switch is isolated from other circuit paths.

Identify COM and NC from the markings or documentation for the specific switch. Generic changeover terminology describes COM as common and NC as normally closed, but the exact device schematic should be checked. Do not select terminals just because they occupy an expected physical location. The test is meaningful only when the probes are across the intended COM and NC pair.

With the switch unactuated, check the COM-to-NC pair. The NC definition predicts a closed path in this state. Then actuate the switch and check the same pair again. When the switch changes over, the NC path opens. If an alternate contact is present, its state can be considered separately, but the essential NC check is the change in the identified COM-to-NC path.

If the NC pair appears open while the switch is unactuated, do not immediately conclude that the switch has failed. The terminals may have been misidentified, the switch may still be actuated, or the test setup may not be checking the intended pair. A switch fault is another possible explanation, but the observation alone does not establish which cause applies. Reconfirm the device schematic, actuator condition, isolation, and probe placement before drawing a conclusion.

### Related guides

- [dual micro switch](/guides/dual-micro-switch/)
- [touch micro switch](/guides/touch-micro-switch/)
- [no nc micro switch](/guides/no-nc-micro-switch/)
- [normally open micro switch](/guides/normally-open-micro-switch/)

## Why an installed circuit may not appear normally closed

An installed mechanism can hold the actuator down or otherwise actuate the switch. In that condition, the NC path is open because the switch is no longer in its unactuated state. The mechanism may be stationary, but its resting position does not redefine the switch’s normal contact state. This is why it helps to separate the mechanical condition of the installation from the contact condition of the switch.

A powered-circuit measurement is also different from a component-level continuity check. Wiring and external power can affect what is observed in the circuit, while the NC definition concerns the contact pair’s state in the switch. A voltage or current observation therefore does not, by itself, confirm whether the isolated COM-to-NC contacts are closed. Do not equate a circuit reading with a direct check of the switch contacts.

To interpret an unexpected result, confirm the terminals and the actuator state before drawing conclusions. For a direct check, disconnect power, isolate the switch, and compare the identified COM-to-NC pair with the switch unactuated and actuated. This keeps three separate questions from being confused: which terminals form the NC pair, whether the switch is being actuated, and what the surrounding circuit is doing.

In short, **micro switch nc** describes a contact path that is closed in the switch’s unactuated state and opens when the switch changes over. The installed mechanism may hold the actuator in a different state, and circuit wiring or external power may affect circuit measurements. Verify the identified contact pair with power disconnected and the switch isolated to determine its own contact state.

## Sources and references

- Defense Logistics Agency ASSIST: [MIL-PRF-8805K: Switches and Switch Assemblies, Sensitive, Snap Action, General Specification For](https://quicksearch.dla.mil/qsDocDetails.aspx?ident_number=7196){: rel="nofollow noopener noreferrer" }
- Wikipedia: [Miniature snap-action switch](https://en.wikipedia.org/wiki/Miniature_snap-action_switch){: rel="nofollow noopener noreferrer" }
