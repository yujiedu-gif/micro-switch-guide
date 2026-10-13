---
title: "3 pin micro switch wiring: Identify and Connect COM, NO, and NC"
description: "3 pin micro switch wiring: Understand the operating idea, essential terminology, practical checks, limitations, and evidence needed for careful selection,."
date: 2026-10-12 16:49:35 +0800
category: Basics
tags:
  - 3 pin micro switch wiring
  - micro switches
  - Basics
author: editorial_team
---

3 pin micro switch wiring depends on the switch’s contact states, not on the physical order of its terminals. A three-terminal changeover switch has a common connection and two contacts that connect to it in different actuator states. Identifying those terminals first helps you choose the pair that matches the intended circuit behavior.

Use the terminal markings and device documentation as the primary references. If the markings are absent or unclear, a continuity check with the circuit disconnected can help establish which terminals connect in each state. Do not assume that pin positions or wire colors follow a universal convention.

## 3 pin micro switch wiring: what each terminal does

In general changeover terminology, COM means common terminal, NO means normally open terminal, and NC means normally closed terminal. These names describe the contacts’ relationship to COM in the switch’s normal, unactuated state. They do not identify supply polarity.

For the contact arrangement described by these labels, COM is the shared connection. With the actuator released, COM connects to NC, while the connection between COM and NO is open. When the actuator is pressed, the switch changes state: COM connects to NO, and the COM-to-NC path opens. The two contacts are therefore alternatives routed through the common terminal, not three interchangeable connection points.

This state-based description is useful when deciding which pair belongs in a circuit. A circuit intended to connect when the actuator is pressed generally uses COM and NO. One intended to connect when the actuator is released and open when pressed generally uses COM and NC. These choices describe contact behavior only; they do not establish how a supply or load should be arranged in a particular device.

Check the exact switch schematic before relying on the generic labels. Terminal markings and documentation for the device take precedence over assumptions based on a typical arrangement. If the observed contact states do not agree with the markings or schematic, do not proceed on the basis of a guessed pinout.

## Identify COM, NO, and NC before connecting wires

Start by checking the markings on the switch and its documentation. Look for the terminal designations or a contact diagram, and confirm that they refer to the exact device. A diagram can clarify the intended contact arrangement, but physical pin position alone is not proof of terminal identity. Wire color is not universal identification evidence either.

If you need to verify the contacts, first disconnect the circuit from power. Use a continuity meter to check which terminal pairs are connected with the actuator released. For the stated changeover arrangement, the released state should show continuity between COM and NC, while COM and NO should be open. Then press the actuator and check whether continuity transfers: COM should connect to NO, and the COM-to-NC connection should open.

The purpose of this check is to identify the contacts by their behavior, not to infer a pin layout. Compare the results with the switch markings and documentation. If the meter readings conflict with those references, or if the terminal identity remains uncertain, stop and consult the device documentation rather than selecting terminals by guesswork.

Once the contacts are identified, keep their roles distinct when planning the connection. COM is the shared terminal; NO and NC are the two alternate contacts. The selected pair should match the required released and pressed behavior. This verification step does not establish a complete circuit design, a supply arrangement, or compatibility with a particular appliance or vehicle.

## Map the intended circuit to the switch contacts

Choose the contact pair from the state the circuit needs. If the connection should be made when the actuator is pressed, use COM and NO, subject to the circuit design. In the released state, that pair is open; pressing the actuator changes it to a connected path.

If the circuit should be connected with the actuator released and open when it is pressed, use COM and NC. In the released state, that pair is connected; pressing the actuator changes it to an open path. In either case, the remaining contact is not a substitute for COM: the selected path is between the common terminal and one of the two alternate contacts.

These contact-level choices do not specify where a supply, load, or other circuit component goes. There is no universal supply, load, or polarity arrangement implied by the terminal labels. The circuit’s requirements and the switch’s device-specific documentation determine how the contacts are used. Avoid extending a simple contact diagram into instructions for a particular appliance, vehicle, or mains circuit without the relevant documentation.

Before making a connection, check that the terminal identities are verified and that the chosen pair produces the intended state transition. If the intended behavior is unclear, define whether the circuit must connect with the actuator released or pressed before wiring. This keeps the selection grounded in observed contact behavior rather than terminal position or wire color.

## Check ratings and safety before energizing

Confirm that the switch’s voltage and current ratings suit the actual load and circuit type. Rating values are requirements tied to stated load and test conditions, not universal switching capacities. A rating must be considered in the context of those stated conditions; it should not be treated as a general allowance for every circuit.

Also account for the load type. Inductive or other loads may impose switching demands beyond a resistive-load rating. Do not assume that a value stated for one load or test condition establishes suitability for a different one. If the applicable rating or conditions are unclear, consult the switch documentation before connection or energizing.

Keep the circuit disconnected from power while identifying terminals and wiring. Before energizing, check that the connection is appropriate for the actual circuit and that suitable enclosure, insulation, and strain relief are provided. Hazardous voltages require appropriate expertise; seek qualified help when needed. These boundaries matter even when the switch’s contact behavior is simple, because contact-state identification alone does not verify electrical suitability.

### Related guides

- [dual micro switch](/guides/dual-micro-switch/)
- [touch micro switch](/guides/touch-micro-switch/)
- [no nc micro switch](/guides/no-nc-micro-switch/)
- [normally open micro switch](/guides/normally-open-micro-switch/)

## Confirm the wiring by testing both switch states

With power still disconnected, test continuity through the selected terminal pair with the actuator released and then pressed. If the circuit should connect when pressed, the COM-and-NO pair should change from open to connected. If it should connect when released, the COM-and-NC pair should change from connected to open. Compare the observed results with the intended circuit behavior and the device documentation.

If the selected pair does not produce the expected transition, recheck terminal identification against the markings and schematic. Do not resolve a mismatch by relying on pin position or wire color. If the switch state or terminal identity remains uncertain, consult the device documentation rather than energizing the circuit.

The useful sequence is to verify the contact arrangement, choose the pair for the intended actuator state, check ratings against the actual load and circuit conditions, and confirm the state change while power remains disconnected. 3 pin micro switch wiring is complete only when the verified contact behavior matches the intended circuit and the device’s documented electrical limits.

## Sources and references

- Defense Logistics Agency ASSIST: [MIL-PRF-8805K: Switches and Switch Assemblies, Sensitive, Snap Action, General Specification For](https://quicksearch.dla.mil/qsDocDetails.aspx?ident_number=7196){: rel="nofollow noopener noreferrer" }
- Wikipedia: [Miniature snap-action switch](https://en.wikipedia.org/wiki/Miniature_snap-action_switch){: rel="nofollow noopener noreferrer" }
