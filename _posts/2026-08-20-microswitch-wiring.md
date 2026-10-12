---
title: "microswitch wiring: Identify Terminals and Verify Connections"
description: "microswitch wiring: Understand the operating idea, essential terminology, practical checks, limitations, and evidence needed for careful selection,."
date: 2026-08-20 09:00:00 +0800
category: Basics
tags:
  - microswitch wiring
  - micro switches
  - Basics
author: editorial_team
---

# Identify and verify micro switch terminals

Microswitch wiring begins with identifying the terminals from the switch’s markings or printed schematic, then checking the contact paths before connecting circuit wires. The terminal labels describe electrical states, not assumed wire colors or a universal pin layout. This guide covers terminal identification and basic continuity verification; it does not establish that any particular switch is suitable for an application.

Disconnect power before wiring or continuity testing. A continuity reading is meaningful only when the switch is isolated from powered circuits and other connections that could affect the result. Check the device documentation for its actual terminal arrangement and electrical ratings before making a connection.

## microswitch wiring: identify COM, NO, and NC

Use the markings on the switch or its own printed circuit diagram as the primary guide. Do not identify COM, NO, or NC by wire color, terminal position, or an assumed pin order. Layouts vary, so a diagram for another switch is not a reliable substitute for the diagram on the device being checked.

In general changeover terminology, **COM** means common terminal, **NO** means normally open, and **NC** means normally closed. “Normally” refers to the actuator’s released state. In a standard changeover arrangement, COM is the shared terminal that connects to one contact path or the other as the actuator moves. With the actuator released, COM is connected to NC; with the actuator pressed, COM is connected to NO.

These terms describe contact states rather than physical locations. A drawing may show terminals in a different order from the switch body, and the names alone do not reveal where each terminal sits. Read the device’s schematic and match its labels to the actual terminals before testing or wiring.

Not every switch provides both NO and NC paths. Some versions have only one contact path, so do not assume that every device is a changeover switch. If the markings or schematic do not make the arrangement clear, treat the terminal identity as unresolved rather than inferring it from appearance.

## Read contact changes in released and actuated states

For a standard changeover contact arrangement, the expected state transition is:

| Actuator state | COM-to-NC path | COM-to-NO path |
|---|---|---|
| Released | Connected | Open |
| Pressed | Open | Connected |

This table describes the change in contact paths, not a universal terminal layout. The switch’s own diagram takes precedence if its arrangement differs or if it does not show a standard changeover contact.

The actuator state matters when interpreting a reading. A path that is connected with the actuator released is the normally closed path; a path that is open in that state is the normally open path in a standard changeover arrangement. Pressing the actuator should change which COM path is connected. Do not apply those expectations to a device with only one contact path without first checking its diagram.

This distinction also prevents a common identification error: NO and NC do not name wires, colors, or fixed terminal positions. They name contact behavior relative to the released state. Confirm the released and pressed states directly, and use the schematic to relate the observed paths to the marked terminals.

## Verify micro switch terminals with a continuity test

Before testing, disconnect power and isolate the switch from circuit connections that could influence the meter reading. Do not perform a continuity check on an energized circuit. If the switch remains connected to other components, those paths can make a reading difficult to interpret, so disconnect the circuit connections needed to test the switch by itself.

Set a multimeter to continuity or resistance. Follow the device diagram to identify COM, NO, and NC, then test COM against each indicated contact in both actuator states. Record what the meter shows with the actuator released and again with it pressed. For a standard changeover contact arrangement, compare the readings with the expected transition: COM-to-NC connected when released and COM-to-NO connected when pressed, with the other path open in each state.

A reading that does not match the diagram and expected state transition is a reason to pause before wiring. Recheck the terminal identification, confirm that the switch is isolated, and repeat the measurement in each actuator state. If the paths remain unexpected, do not assign terminal functions by guesswork; the contact condition or the assumed arrangement has not been verified.

The test confirms observed contact paths under the test conditions. It does not establish that the switch is rated for a proposed circuit, that it is suitable for a particular use, or that it meets requirements for mains or safety-critical work. Those questions require device-specific documentation and an appropriate assessment beyond a continuity check.

### Related guides

- [dual micro switch](/guides/dual-micro-switch/)
- [touch micro switch](/guides/touch-micro-switch/)
- [no nc micro switch](/guides/no-nc-micro-switch/)
- [normally open micro switch](/guides/normally-open-micro-switch/)

## Connect the micro switch only within its electrical rating

After identifying and checking the contacts, select the path according to the required circuit behavior: a circuit that should be connected in the released state uses the relevant normally closed path in a standard changeover arrangement; a circuit that should be connected in the pressed state uses the relevant normally open path. Verify that choice against the switch diagram and the observed readings before attaching wires.

Check the switch documentation for its electrical ratings and compare them with the circuit’s voltage, current, AC or DC supply, and load characteristics. Rating values are specification-sheet requirements tied to stated load and test conditions, not universal switching capacities. A voltage or current figure without its stated conditions is not enough to establish suitability. If the documentation does not cover the intended conditions, suitability remains unresolved.

Use suitable insulation and secure connections. This general terminal guide does not establish suitability for mains or safety-critical circuits. Refer work involving those circuits to a qualified professional rather than treating terminal identification or a continuity test as proof that the installation is appropriate.

The reliable sequence is to read the device’s own schematic, identify the contact paths by their released and actuated states, verify those paths with the switch isolated, and check the documented rating conditions before connection. **Microswitch wiring** should proceed only when the terminal arrangement and the circuit requirements have both been established; if either remains unclear, do not infer the missing information from color, layout, or a generic diagram.

## Sources and references

- Defense Logistics Agency ASSIST: [MIL-PRF-8805K: Switches and Switch Assemblies, Sensitive, Snap Action, General Specification For](https://quicksearch.dla.mil/qsDocDetails.aspx?ident_number=7196){: rel="nofollow noopener noreferrer" }
- Wikipedia: [Miniature snap-action switch](https://en.wikipedia.org/wiki/Miniature_snap-action_switch){: rel="nofollow noopener noreferrer" }
