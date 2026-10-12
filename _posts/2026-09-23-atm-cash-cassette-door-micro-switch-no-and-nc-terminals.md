---
title: "atm cash cassette door micro switch NO and NC terminals: How to identify them"
description: "atm cash cassette door micro switch NO and NC terminals: Understand the operating idea, essential terminology, practical checks, limitations, and evidence."
date: 2026-09-23 09:00:00 +0800
category: Applications
tags:
  - atm cash cassette door micro switch NO and NC terminals
  - micro switches
  - Applications
author: editorial_team
---

An **atm cash cassette door micro switch NO and NC terminals** check starts with the switch’s own contact states, not with assumptions about the ATM’s door logic. On a changeover switch, COM is the common terminal; NC connects to COM while the actuator is released, and NO connects to COM when the actuator is operated. These are mechanical contact relationships, not fixed high- or low-voltage readings.

The distinction matters because a cassette-door mechanism may press or release an actuator according to its particular mounting geometry, and not every cassette-door design uses this type of switch. Identifying a contact path therefore requires matching the installed device’s markings or diagram and, when appropriate, checking it with the switch isolated from power. A continuity result describes the tested contact pair and actuator state; it does not, by itself, establish how the ATM interprets that state or whether the surrounding circuit works correctly.

## What NO and NC mean on an atm cash cassette door micro switch NO and NC terminals

COM, NC, and NO describe terminals on a changeover contact arrangement. COM is the common terminal. NC means normally closed, and NO means normally open. In this terminology, “normally” refers to the switch’s released, unoperated actuator position, not to a presumed normal condition of the cassette door or ATM.

With the actuator released, the changeover switch’s COM-to-NC contact path is closed, while its COM-to-NO path is open. When the actuator is operated, the contact relationship changes: COM-to-NO becomes closed, and COM-to-NC becomes open. This describes the switch’s contact continuity in each mechanical state. It does not specify a voltage, a powered logic level, or the meaning assigned to that state by the equipment.

A terminal label alone should be read in the context of the exact switch’s markings or connection diagram. The symbols COM, NO, and NC provide general changeover terminology, but the device schematic should be checked before assigning terminals. The physical position of a terminal is not a reliable universal guide: layouts can differ, and the presence of both NO and NC contacts depends on the particular switch design.

This distinction also prevents a common interpretive error. A closed contact path is not synonymous with a high signal, and an open path is not synonymous with a low signal. The connected equipment’s circuit determines how a contact change is used. A continuity check can establish whether a tested pair is open or closed under specified conditions, but it cannot reveal the ATM’s full control logic from the contact state alone.

## How actuator movement changes the contact path

The released and operated states refer to the switch actuator. They do not automatically mean “door open” and “door closed.” A cassette-door linkage may move the actuator in either direction depending on how the switch is mounted and how the mechanism meets it. Thus, a door position cannot be assigned to NO or NC just from the terminal names.

To connect contact behavior to the mechanism, first establish which physical part acts on the actuator and whether that part presses or releases it in the positions being considered. Then describe the switch as actuator released or actuator operated. Only after the installed arrangement is understood can those states be related to a door position. Even then, the contact state does not establish what the ATM does in response; that depends on the equipment’s circuit and design.

The switch may also be mounted or oriented differently from another cassette-door design. A door could act on a lever, plunger, or another actuator arrangement, but the switch’s exact form and the mechanism’s movement should not be inferred without evidence for the installed device. The important identification question is which contact pair changes continuity as the switch actuator moves, not which terminal appears to correspond to an assumed door label.

This mechanism-based distinction is useful when a reading seems contrary to an expectation. If someone expects the contact to be closed with the door shut, that expectation may be based on the equipment’s intended behavior, an assumed mounting direction, or a presumed wiring arrangement. It does not redefine the switch’s released-state convention. First identify the actuator state and terminal pair; treat the relationship between that state and the door or ATM response as a separate, design-specific question.

## How to verify terminals with a continuity test

A continuity check should be made with the switch isolated from power. Where practical, disconnect the switch from the circuit before testing so that other connected paths do not affect the reading. Follow applicable deenergization and qualification requirements. Do not rely on a powered voltage reading or wire color alone to identify a terminal, and do not treat this procedure as permission to open or access a secured ATM assembly.

Use the switch’s markings or applicable documentation to identify candidate terminals. With a multimeter set to continuity or resistance mode, check a candidate COM-to-NC pair and a candidate COM-to-NO pair while the actuator is released. Record whether each tested pair reads as open or closed. Then operate the actuator, if this can be done safely without disturbing the installed assembly, and repeat the checks. For a changeover arrangement, the expected pattern is COM-to-NC closed and COM-to-NO open when released, followed by COM-to-NO closed and COM-to-NC open when operated.

The useful observation is the change in contact continuity between the two actuator states. A single reading in only one state may not distinguish a correctly identified terminal pair from an incorrect assumption about the pair or state. Record the actuator position and the terminal pair for each result; do not translate a continuity reading into an ATM logic level or a door-status conclusion without the relevant circuit information.

If the terminals cannot be identified from markings or an applicable diagram, do not guess from their physical layout. If the switch cannot be isolated or reached without opening a secured assembly, stop rather than extending the check into ATM access or repair. A test result is limited to the isolated switch, the pair tested, and the actuator state observed. It does not verify wiring, equipment logic, or the operation of the complete cassette-door system.

### Related guides

- [ball screw actuator home position micro switch replacement](/guides/ball-screw-actuator-home-position-micro-switch-replacement/)
- [bottling machine end of stroke micro switch](/guides/bottling-machine-end-of-stroke-micro-switch/)
- [automated guided vehicle home position micro switch location](/guides/automated-guided-vehicle-home-position-micro-switch-location/)
- [accelerator pedal position stop micro switch operating force](/guides/accelerator-pedal-position-stop-micro-switch-operating-force/)

## What can vary between cassette-door switch designs

Terminal arrangement, contact configuration, actuator style, and mounting orientation can vary between switch designs and mechanisms. Some designs may use only one contact path or a different sensing arrangement. Consequently, the presence of a COM, NO, and NC set should not be assumed for every cassette door, nor should one device’s pin layout be applied to another.

Use terminal markings and the applicable documentation for the installed switch and equipment to determine the intended connection. A generic physical-layout inference is not a substitute for the exact connection diagram, terminal marking, circuit function, and permissible load documented for that switch and equipment. Wire color is not a dependable way to establish the switch’s contact designation or the circuit’s meaning.

The scope here is limited to a cassette-door design that uses the stated micro switch. Other designs may use another arrangement or sensing method, and the presence of a door does not prove that a micro switch is installed. Even where a changeover switch is present, identifying its contact states does not identify the equipment’s response to them.

The practical conclusion is narrow: identify COM, NO, and NC from the installed device’s markings or diagram, then verify the relevant contact paths in released and operated actuator states with the switch isolated from power, when that can be done safely. Relate those results to a door position or ATM behavior only when the specific installation and circuit documentation establish that relationship. For **atm cash cassette door micro switch NO and NC terminals**, the actuator state and contact continuity are the reference points; a universal door-position mapping or pinout is not established.

## Sources and references

- Defense Logistics Agency ASSIST: [MIL-PRF-8805K: Switches and Switch Assemblies, Sensitive, Snap Action, General Specification For](https://quicksearch.dla.mil/qsDocDetails.aspx?ident_number=7196){: rel="nofollow noopener noreferrer" }
- Occupational Safety and Health Administration: [29 CFR 1910.333: Selection and Use of Work Practices](https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.333){: rel="nofollow noopener noreferrer" }
- Wikipedia: [Miniature snap-action switch](https://en.wikipedia.org/wiki/Miniature_snap-action_switch){: rel="nofollow noopener noreferrer" }
