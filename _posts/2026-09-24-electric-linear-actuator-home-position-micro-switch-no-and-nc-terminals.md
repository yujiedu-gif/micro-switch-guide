---
title: "electric linear actuator home position micro switch NO and NC terminals"
description: "electric linear actuator home position micro switch NO and NC terminals: Understand the operating idea, essential terminology, practical checks,."
date: 2026-09-24 13:38:01 +0800
sitemap_omit_lastmod: true
category: Applications
tags:
  - electric linear actuator home position micro switch NO and NC terminals
  - micro switches
  - Applications
author: editorial_team
---

An **electric linear actuator home position micro switch NO and NC terminals** describe a possible mechanical position-sensing arrangement and the contact labels on its switch. They do not, by themselves, tell you which contact is closed when the actuator is home or what the controller will do with a signal. Those details depend on the documented switch arrangement, its reference condition, and the actuator’s actual design.

Only electric linear actuators that use a mechanically actuated micro switch are in scope here. The switch is a component in a sensing path, not the actuator itself or its control logic. To interpret a home-position signal, trace the movement that operates the switch, then check terminal labels against the specified reference state and the relevant design documentation.

## What the electric linear actuator home position micro switch NO and NC terminals describe

An electric linear actuator produces linear movement. A design that uses a micro switch for home indication adds a mechanical sensing arrangement: a moving part can interact with the switch, and the switch can change an electrical contact state in response to actuator movement. Micro switches are also commonly used for position or limit detection, but that general use does not establish that every actuator uses one or explain how a particular actuator is built.

Keep the parts of the arrangement distinct. The actuator provides movement. A mechanical feature associated with that movement may reach the switch actuator. The micro switch responds by changing its contact state. A connected controller may then interpret an electrical input according to its own design. The switch does not, on its own, define what “home” means to the actuator system or prescribe a controller response.

The term “home position” identifies the position being sensed in the particular design. It is not a universal reference condition for the switch contacts. The switch’s reference condition and the actuator’s home position may be related in a documented design, but they are not interchangeable terms. Without that documentation, do not infer that the switch is operated at home, that a particular terminal pair is closed there, or that the controller treats a contact change as a stop, start, or other command.

A miniature snap-action switch uses contact action in which the speed of the moving contacts is relatively independent of the speed of the actuating mechanism. That definition describes the switch mechanism, not the whole actuator’s motion or its control sequence. The switch’s mechanical operating event can be part of a home-sensing chain, but the actuator’s moving parts and controller behavior remain design-specific.

## How home-position motion can transfer micro switch contacts

In a design that uses a micro switch, the causal path can begin as the actuator moves toward the position identified as home. A mechanical part associated with the moving actuator may contact or otherwise move the switch actuator. If that movement reaches the switch’s operating point, the switch can operate and its contacts can transfer. The contact change is the switch’s electrical response to mechanical movement; it is not, by itself, a complete explanation of the actuator’s home-position logic.

Each link must be established for the actual design. The available description may identify which moving part interacts with the switch, the direction of movement, the relevant switch actuator, and the condition under which the switch operates. If those details are not documented, the general mechanism does not reveal which part makes contact or when contact transfer occurs. Do not assume a particular cam, stop, linkage, or other mechanism from the fact that an actuator has a home position.

The switch’s operating event also differs from the controller’s interpretation. A contact change could be presented as an input to a controller, but the meaning assigned to that input depends on the actual circuit and control design. A reader cannot determine from the NO and NC labels alone whether the controller recognizes home, changes direction, inhibits movement, or takes any other action. Those behaviors are outside what the terminal names establish.

This separation helps avoid a common diagnostic shortcut: observing a position change does not prove that the switch has transferred, and observing a switch contact change does not prove that the controller has interpreted it as home. Each is a distinct point in the causal chain. Documentation or a bounded test may establish a fact about one point without establishing the rest of the actuator system’s behavior.

## Read NO and NC only against the documented reference state

COM means common only when the switch’s contact arrangement documents a COM terminal. NO and NC describe contact states relative to a specified reference condition. They are not unconditional promises about continuity in every position, and neither label independently identifies the actuator’s home state.

Before interpreting a terminal pair, identify the actual arrangement and its stated reference condition in applicable documentation. Then determine whether the documentation defines that condition as the switch unoperated, operated, or another specified state. Do not supply a reference condition by assumption. In particular, “home” cannot be substituted for the specified reference condition unless the design documentation explicitly connects them.

Once the arrangement and reference condition are known, use the labels only within that scope. If documentation establishes the contact state for the reference condition, that information can be compared with a reading taken in that same defined state. If it does not establish the home-position state, the labels alone cannot tell you whether COM has continuity with NO or NC at home. The expected pattern remains unresolved until the design-specific arrangement and state are verified.

The distinction is practical as well as terminological. A switch’s mechanical state and its contact state are related through the switch mechanism, while the controller’s interpretation is a separate matter. Even a correctly identified contact pair and a matching reading in one state do not specify what an installed controller will do. Keep statements about contacts, actuator position, and system response separate.

## Verify the isolated switch in defined actuator states

Start with applicable documentation for the actuator and switch. Identify the switch, its documented contact arrangement, terminal labels, reference condition, and any stated expected behavior for the states you intend to check. If those details are unavailable, do not guess the terminal pattern from “home,” “NO,” or “NC.” The verification is only interpretable when the tested state can be defined and compared with documented expectations.

A bounded check concerns the isolated switch, not an energized actuator circuit. With the switch isolated and the actuator state clearly defined, check the relevant contacts using a suitable continuity method. Record which state was tested and which documented terminal pair was checked. Compare the result only with expected behavior specified for that arrangement and state. A reading taken with the switch connected to other circuitry is not the same evidence as a reading of the isolated switch.

If the design documentation specifies a home state and expected contact behavior, the isolated reading can indicate whether the tested switch contacts match that documented behavior under the defined test conditions. If the expected behavior is not documented, a continuity result alone does not establish which contact pattern is correct for home. Nor does a matching result establish that the mechanical sensing arrangement operates at the intended position or that the system recognizes the position as home.

An isolated reading also does not establish installed wiring, controller logic, overall actuator function, or electrical safety. It is evidence about the switch in the tested state and isolation condition. Do not expand that evidence into a conclusion about the complete assembly. Work beyond an applicable documented safe test procedure, including energized-circuit diagnosis, belongs to qualified personnel.

### Related guides

- [bottling machine home position micro switch location](/guides/bottling-machine-home-position-micro-switch-location/)
- [incinerator end of stroke micro switch maintenance](/guides/incinerator-end-of-stroke-micro-switch-maintenance/)
- [rotary indexing table guard interlock micro switch location](/guides/rotary-indexing-table-guard-interlock-micro-switch-location/)
- [security barrier open position micro switch wiring](/guides/security-barrier-open-position-micro-switch-wiring/)

## What a contact reading can and cannot establish

A reading that differs from documented behavior may indicate a problem with switch actuation or contact condition, but it does not identify the cause by itself. Terminal identification, the selected actuator state, the isolation condition, and the test setup also affect how the reading should be interpreted. Check those facts against the documentation before concluding that the switch has failed.

Likewise, a reading that agrees with the documented behavior establishes only that the measured contacts matched that expectation in the tested state. It does not prove that the switch is mechanically reached at the correct position, that another state behaves as expected, or that the controller receives and interprets the signal correctly. The remaining parts of the sensing and control path require evidence specific to those parts.

The decision boundary is therefore narrow: use terminal labels only with a documented contact arrangement and reference condition; use continuity only for an isolated switch in a defined actuator state; and limit the conclusion to the behavior actually documented and measured. If the expected home-position pattern or the system’s interpretation is unknown, leave it unresolved rather than treating NO or NC as a guarantee. In an **electric linear actuator home position micro switch NO and NC terminals** arrangement, contact state can contribute to home sensing, but the labels alone do not establish home behavior or the controller’s response.

## Sources and references

- Defense Logistics Agency ASSIST: [MIL-PRF-8805K: Switches and Switch Assemblies, Sensitive, Snap Action, General Specification For](https://quicksearch.dla.mil/qsDocDetails.aspx?ident_number=7196){: rel="nofollow noopener noreferrer" }
- Wikipedia: [Miniature snap-action switch](https://en.wikipedia.org/wiki/Miniature_snap-action_switch){: rel="nofollow noopener noreferrer" }
