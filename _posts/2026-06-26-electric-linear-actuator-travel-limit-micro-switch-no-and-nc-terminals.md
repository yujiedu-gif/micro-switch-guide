---
title: "Electric linear actuator travel limit micro switch NO and NC terminals"
description: "electric linear actuator travel limit micro switch NO and NC terminals: Understand the operating idea, essential terminology, practical checks,."
date: 2026-06-26 13:45:45 +0800
last_modified_at: 2026-10-13 11:46:37 +0800
category: Applications
tags:
  - electric linear actuator travel limit micro switch NO and NC terminals
  - micro switches
  - Applications
author: editorial_team
---

In an electric linear actuator travel limit micro switch NO and NC terminals describe contact states that may be used in a travel-limit arrangement. The labels do not, by themselves, say what the actuator will do when a limit is reached. That result depends on the switch’s mechanical arrangement and the actuator’s actual control circuit.

The causal path has distinct steps: actuator motion moves a mechanism, that mechanism actuates the micro switch, the switch changes contact state, and the circuit responds according to its design. A micro switch can serve as a position or limit detector, but not every electric linear actuator uses one. Terminal labels alone cannot establish that a motor stops, reverses, or triggers another action.

## What electric linear actuator travel limit micro switch NO and NC terminals mean

NO and NC describe contact states relative to a specified reference condition. A normally open contact is open in that reference condition; a normally closed contact is closed in it. The terms identify a state, not an unconditional description of the contact at every point in actuator movement. To interpret them, first determine the reference condition given in the switch documentation.

A generic changeover contact may have three terminals: common, normally closed, and normally open. COM means common only when the actual switch has that documented contact arrangement. The device’s own markings or schematic control; the labels should not be assumed from appearance or from a different switch’s terminal layout.

In a travel-limit arrangement, a moving mechanism may cause the switch to transfer from one contact state to another. That transition can provide an input to a control circuit. The labels do not specify which contact is used, which state exists at a travel endpoint, or how the circuit responds. Those details depend on the particular switch and system.

This distinction matters because a contact description and a control command are different things. NO and NC name contact states at a reference condition. They do not mean “run,” “stop,” or “reverse.” Nor do they establish whether a particular contact is electrically active in an installed circuit. That interpretation requires the circuit diagram and the documented switch arrangement.

## How actuator travel can operate a micro switch

The mechanical path begins with movement of the electric linear actuator or a linked mechanism. As the mechanism reaches a limit feature, it may move the micro switch’s actuator. If that switch design uses snap action, the movement can change an electrical contact state. The switch is the sensing component in this sequence; it is not the actuator, linkage, motor, or control circuit.

Actuator travel and switch-actuator travel are related through the mechanism, but they are not automatically the same motion or distance. In the terminology used by MIL-PRF-8805K sections 6.5.14 and 6.5.16, pretravel runs from the switch actuator’s free position to its operating position. Overtravel runs from the operating position to the extreme permitted actuator position. These terms describe portions of switch-actuator movement, not the electric linear actuator’s full stroke.

A limit feature can therefore cause a switch transition at a point in the larger mechanical travel, but the available information does not establish where that point is for a particular actuator. The relationship depends on the actual mechanism and design. Do not infer a limit position, switch travel, or adjustment from the terminal names.

Not every electric linear actuator uses a micro switch for travel limiting. Implementations vary, and the switch’s presence and role must be confirmed for the specific design. Where a micro switch is used, its contact change is one event in a chain: mechanical movement reaches the switch, the switch changes state, and the control circuit receives or responds to that change.

## Why NO and NC do not determine actuator behavior by themselves

A contact transition affects the actuator only through the actual electrical arrangement. The circuit may use a contact as an input to control logic, but terminal names alone do not reveal what device receives that input or what action follows. The available information does not establish whether a given actuator stops, reverses, interrupts power, signals an alarm, or behaves in another way at a travel limit.

Keep three descriptions separate. First, the switch has a contact state relative to its documented reference condition. Second, mechanical movement may operate the switch and change that state. Third, the host circuit determines what the resulting electrical change means to the actuator system. Treating these as one step can lead to an unsupported conclusion, such as assuming that NC necessarily means the motor will stop when the mechanism reaches an endpoint.

The switch’s reference state is also not the same as the mechanism’s current position. A label such as NO or NC does not, by itself, identify whether the actuator is currently extended, retracted, or at a limit. Nor does it establish the installed circuit’s electrical state. The reference condition and the relevant mechanical position must be understood separately.

For the same reason, a contact label cannot establish the control logic when the wiring is unknown. A switch may change state mechanically while the system’s response depends on connections or other control components. Do not infer a wiring scheme or operational result from the fact that a micro switch is present.

### Related guides

- [bottling machine home position micro switch location](/guides/bottling-machine-home-position-micro-switch-location/)
- [incinerator end of stroke micro switch maintenance](/guides/incinerator-end-of-stroke-micro-switch-maintenance/)
- [rotary indexing table guard interlock micro switch location](/guides/rotary-indexing-table-guard-interlock-micro-switch-location/)
- [security barrier open position micro switch wiring](/guides/security-barrier-open-position-micro-switch-wiring/)

## What to verify before interpreting the limit-switch terminals

Begin with the documentation for the actual switch. Confirm its terminal arrangement, any markings or schematic, and the reference condition used to define NO and NC. If a changeover arrangement is not documented for that device, do not assume that it has COM, NO, and NC terminals merely because those labels are common on some switches.

Then consult the electric linear actuator’s actual circuit documentation. Trace where the switch contact change goes and identify the device or control function that receives it. This is the evidence needed to interpret the system response; terminal names by themselves are not enough. If the circuit documentation does not establish a behavior, leave that behavior unresolved rather than infer it.

Keep the mechanical and electrical questions distinct as well. The switch documentation identifies its contact arrangement and reference state. The actuator or system documentation explains how its mechanism reaches the switch and how the circuit uses the resulting change. Neither description should be substituted for the other.

A click or apparent movement does not establish the terminal arrangement or the circuit response. Likewise, a wire color alone does not identify a terminal or prove how the control system is configured. Use the documented switch and circuit information; when either is missing or ambiguous, the terminal’s role and the actuator’s resulting behavior remain unknown.

The practical conclusion is bounded: NO and NC can identify contacts used in a travel-limit arrangement, and mechanical movement can cause a micro switch to change contact state. Only the actual switch documentation and control-circuit diagram establish which terminals are present and what the system does with that change. An electric linear actuator travel limit micro switch NO and NC terminals therefore describe a possible contact role, not a universal wiring scheme or guaranteed actuator response.

## Sources and references

- Defense Logistics Agency ASSIST: [MIL-PRF-8805K: Switches and Switch Assemblies, Sensitive, Snap Action, General Specification For](https://quicksearch.dla.mil/qsDocDetails.aspx?ident_number=7196){: rel="nofollow noopener noreferrer" }
- Wikipedia: [Miniature snap-action switch](https://en.wikipedia.org/wiki/Miniature_snap-action_switch){: rel="nofollow noopener noreferrer" }
