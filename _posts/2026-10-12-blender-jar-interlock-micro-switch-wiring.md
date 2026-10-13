---
title: "Blender jar interlock micro switch wiring: how the contacts work"
description: "blender jar interlock micro switch wiring: Understand the operating idea, essential terminology, practical checks, limitations, and evidence needed for."
date: 2026-10-12 16:49:35 +0800
category: Applications
tags:
  - blender jar interlock micro switch wiring
  - micro switches
  - Applications
author: editorial_team
---

Blender jar interlock micro switch wiring depends on the appliance’s own circuit design, so terminal labels and wiring information matter more than wire colors or physical position. The micro switch is one mechanically actuated component in a broader interlock system. Its contacts may change state as the jar or a related actuator reaches its intended position, but that change alone does not establish that the complete appliance circuit is working.

This guide explains the common, normally open, and normally closed contact relationships and outlines a bounded continuity check with the switch isolated and power disconnected. It does not provide a universal appliance schematic. Confirm the exact switch configuration and consult the appliance’s wiring information before interpreting connections.

## Blender jar interlock micro switch wiring: what the switch controls

A micro switch is a mechanically actuated contact. In a jar-presence interlock, movement of the jar or a related actuator can operate the switch, changing a contact path that signals the interlock circuit. The switch is one element in that arrangement, not the whole control circuit and not, by itself, proof that the appliance recognizes the jar correctly.

Interlock designs can differ. A design may use a normally open contact, a normally closed contact, or other control components alongside the switch. The appliance’s circuit may also include wiring and control electronics. The available information here does not establish which contact type a particular blender uses, how its wider circuit is arranged, or which switch terminal connects to which circuit point.

Do not infer a wiring diagram from a switch’s appearance. Wire colors and terminal positions are not universal identifiers, and no universal color scheme or one-size-fits-all appliance schematic can be established here. Use the exact appliance wiring information and the markings or documentation for the installed switch. If those references are unavailable or unclear, the circuit connections remain unresolved rather than something to guess.

## Identify common, normally open, and normally closed contacts

COM means common terminal, NO means normally open terminal, and NC means normally closed terminal. “Normally” refers to the switch’s unactuated state: the state with its actuator released. These names describe contact relationships, not a guarantee about how a particular appliance uses those contacts.

For a switch configured with COM, NO, and NC contacts, the unactuated state provides the reference for checking the pairs. In that state, COM-NC is the normally closed pair, while COM-NO is the normally open pair. When the actuator is pressed, the contact relationship changes: COM-NO is expected to become continuous and COM-NC is expected to become open, subject to the switch’s specified configuration. Confirm the actual configuration against the switch markings or documentation rather than treating these relationships as universal for every device.

A simple state table can help keep the check organized:

| Switch state | COM-NO relationship | COM-NC relationship |
|---|---|---|
| Actuator released, unactuated | Normally open | Normally closed |
| Actuator pressed, actuated | Expected to become continuous | Expected to become open |

The table describes the contact state, not the blender’s full interlock logic. A terminal’s physical location does not establish whether it is COM, NO, or NC. Read the terminal labels and applicable documentation first; do not identify terminals by wire color or position alone.

## Trace the interlock path without assuming a universal diagram

When the jar or related actuator reaches its intended position, the micro switch may open or close a signal path. That is the switch’s role in the interlock: changing a contact state that forms one part of a larger electrical arrangement. The contact change does not, on its own, explain what the rest of the appliance does with that signal.

Keep three parts distinct when following the circuit: the switch contacts, the wiring connected to them, and downstream control components or other interlock conditions. A continuity change at the switch concerns the contacts being checked. It does not identify the complete route through the appliance, establish how its electronics respond, or show that every other condition is satisfied.

For that reason, follow the appliance’s own wiring information rather than drawing a circuit based on a generic blender arrangement. Confirm the switch terminal identities and trace only connections supported by the appliance documentation. If the diagram or switch configuration does not resolve a connection, do not fill the gap by assuming a standard topology. The available evidence does not establish a universal circuit path, wire-color convention, or terminal-to-circuit assignment.

## Verify the micro switch safely with continuity testing

Continuity testing can check whether the relevant contacts change state as the actuator is released and pressed. This is a check of the isolated switch, not a test of the complete interlock circuit. Disconnect power and isolate the switch from the circuit before using a meter’s continuity function. Do not treat a reading taken through connected appliance circuitry as a definitive measurement of the switch contacts.

First identify COM, NO, and NC using the switch markings or documentation. With the switch isolated and its actuator released, check the relevant pair, such as COM-NO or COM-NC, and note the result. Press the actuator and check the same pair again. Compare the readings in both states with the contact labels and the specified switch configuration. If the appliance documentation calls for a particular contact path, use that information to identify which pair is relevant to the circuit.

The actuator must be tested in both mechanical states for the comparison to be meaningful: released and pressed. Keep the test focused on the labeled contacts and the change between those states. Do not infer an appliance-wide fault or connection from a single pair’s reading, and do not bridge contacts to make the appliance operate. If results do not match the switch’s stated configuration, inspect the switch and its connections without defeating the interlock.

### Related guides

- [ball screw actuator home position micro switch replacement](/guides/ball-screw-actuator-home-position-micro-switch-replacement/)
- [bottling machine end of stroke micro switch](/guides/bottling-machine-end-of-stroke-micro-switch/)
- [automated guided vehicle home position micro switch location](/guides/automated-guided-vehicle-home-position-micro-switch-location/)
- [accelerator pedal position stop micro switch operating force](/guides/accelerator-pedal-position-stop-micro-switch-operating-force/)

## What a switch test does not prove

A continuity change confirms only the contact behavior tested, under the conditions of that check. It does not prove that the jar or related actuator reaches and operates the switch as intended. It also does not establish that the connected wiring, control electronics, or other interlock elements function correctly. A switch can show the expected contact change while a separate part of the wider interlock path remains unverified.

Likewise, an unexpected reading is not permission to bridge terminals or bypass the interlock. Do not operate the appliance with the interlock defeated. If diagnosis would require energized testing, seek qualified service rather than extending an isolated contact check into an energized procedure. The safe conclusion from this method is limited: it can help verify the labeled switch contacts with power disconnected and the switch isolated; it cannot certify the appliance’s complete interlock circuit.

In short, blender jar interlock micro switch wiring must be understood from the specific switch markings and appliance wiring information. Identify contacts by their labels, compare their state with the actuator released and pressed, and keep that result separate from any conclusion about the full appliance circuit.

## Sources and references

- Defense Logistics Agency ASSIST: [MIL-PRF-8805K: Switches and Switch Assemblies, Sensitive, Snap Action, General Specification For](https://quicksearch.dla.mil/qsDocDetails.aspx?ident_number=7196){: rel="nofollow noopener noreferrer" }
- Wikipedia: [Miniature snap-action switch](https://en.wikipedia.org/wiki/Miniature_snap-action_switch){: rel="nofollow noopener noreferrer" }
