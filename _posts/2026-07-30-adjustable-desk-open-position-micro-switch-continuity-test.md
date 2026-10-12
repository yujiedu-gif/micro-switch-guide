---
title: "Adjustable desk open position micro switch continuity test"
description: "adjustable desk open position micro switch continuity test: Understand the operating idea, essential terminology, practical checks, limitations, and."
date: 2026-07-30 09:00:00 +0800
category: Troubleshooting
tags:
  - adjustable desk open position micro switch continuity test
  - micro switches
  - Troubleshooting
author: editorial_team
---

# Testing an Adjustable Desk Micro Switch at the Open Position

An **adjustable desk open position micro switch continuity test** checks whether the switch contacts have the expected electrical state when the desk reaches its intended open position. The result depends on two things: the switch’s contact configuration and whether the desk’s mechanism actuates the switch at that position. A continuity reading alone does not show that the desk’s complete control system works.

The switch’s contact diagram or circuit documentation determines which terminals to measure and what state to expect. Disconnect power and isolate the relevant switch terminals before measuring resistance. If the circuit cannot be isolated or the switch cannot be accessed safely, stop rather than trying to interpret a reading from connected equipment.

## What the adjustable desk open position micro switch continuity test checks

First establish what “open position” means for the test: the desk has reached its intended open position, and you have determined from the mechanism or documentation whether that position actuates the switch. Do not assume that an open desk position always presses the actuator. The physical position and the switch’s actual actuator state are part of the test condition.

A micro switch may use a changeover contact arrangement. In generic terminology, COM means common terminal, NC means normally closed terminal, and NO means normally open terminal. “Normally” refers to the switch’s unoperated state, not automatically to the desk being open or closed. The exact device marking or schematic controls; confirm it before choosing a contact pair.

The test asks whether the documented contacts conduct or remain open in the actuator state reached at the desk’s open position. The expected result therefore follows from the switch configuration and its state in that position, not from a universal expectation that a meter should beep. This check concerns the switch contacts. It does not, by itself, establish that other wiring or the desk’s complete control system operates correctly.

## Prepare the desk and identify the micro switch terminals

If the desk can be moved to its intended open position safely, place it there before disconnecting power. Then disconnect power before accessing the switch or measuring its contacts. Do not measure resistance on an energized circuit. If reaching the position or switch requires unsafe disassembly, stop and do not continue with the test.

Identify the relevant terminals from the switch’s contact diagram, terminal markings, or circuit documentation. Generic COM, NO, and NC labels can help explain a changeover arrangement, but they are not a substitute for checking the exact device schematic. Do not infer pin assignments from terminal location or appearance.

Isolate the contact measurement from connected circuitry by disconnecting at least one relevant lead, as appropriate to the documented contact pair. Connected electronics can influence the reading, so a measurement taken through the remaining circuit may not represent the switch contacts alone. If you cannot identify the correct terminals or isolate the switch from the circuit, the result cannot reliably answer whether the contacts themselves change state.

## Measure continuity at the open position

With power disconnected and the relevant contact isolated, set the meter to continuity or resistance. Place the probes across the contact pair identified in the switch documentation. Keep the desk in its intended open position and note whether the actuator is in the state associated with that position. Observe whether the reading is stable; do not treat a momentary or changing indication as a settled result.

Interpret the reading against the contact configuration and actual actuator state. In generic changeover terminology, NC describes the normally closed contact and NO the normally open contact, with COM as the common terminal. Those labels do not tell you, by themselves, what the desk’s open position should produce. Use the documented switching sequence to establish whether the measured pair should conduct or remain open when the actuator is in its current state.

A meter indication consistent with that documented state supports the conclusion that the tested contact pair has the expected continuity state under the test condition. It does not prove the entire desk control system works. Likewise, there is no single expected beep or resistance result that applies to every arrangement. If the documentation does not establish the contact pair and state, the reading remains inconclusive rather than evidence of a failed switch.

## Interpret readings and separate contact, wiring, and actuation faults

If the reading conflicts with the documented contact state, confirm the terminal identification, probe placement, meter mode, and isolation from connected circuitry before attributing the result to the switch. An inconsistent reading may indicate dirty, damaged, or failed contacts, but one unexplained result does not establish which cause is present.

If the contacts behave as documented, test the isolated wiring separately when needed. A contact check and a wiring check answer different questions: the first concerns the switch pair, while the second concerns continuity along the isolated wiring. Do not use a contact reading taken through connected electronics as a substitute for separately checking the wiring.

Also verify that the mechanism actually reaches and holds the switch in its intended actuator state at the open position. If readings change with actuator movement or desk position, that variation may point to a mechanical actuation or alignment issue rather than a contact problem. Confirm that the switch is reached and held as intended before concluding that the contacts are inconsistent. Continuity alone cannot identify a fault in the motor, power supply, or complete control system.

### Related guides

- [automated guided vehicle guard interlock micro switch intermittent operation](/guides/automated-guided-vehicle-guard-interlock-micro-switch-intermittent-operation/)
- [assembly robot travel limit micro switch failure causes](/guides/assembly-robot-travel-limit-micro-switch-failure-causes/)
- [air compressor travel limit micro switch troubleshooting](/guides/air-compressor-travel-limit-micro-switch-troubleshooting/)
- [boom lift travel limit micro switch symptoms](/guides/boom-lift-travel-limit-micro-switch-symptoms/)

## When to stop or compare with the closed-position test

Stop if power cannot be safely isolated, the terminals cannot be identified from reliable documentation, or access requires hazardous disassembly. Do not take a resistance measurement on an energized circuit, and do not continue when the test condition cannot be established. A reading is useful only when the contact pair, actuator state, and electrical isolation are understood.

A closed-position measurement is a separate diagnostic comparison, not the primary procedure here. Use it only if the documented switching sequence calls for comparing the two desk positions. The expected state and any meter interpretation depend on the switch arrangement and documentation; do not assume that a closed-position result must be the opposite without that basis.

In short, the **adjustable desk open position micro switch continuity test** is a position-specific contact check: isolate the switch, identify the documented terminals, measure them while the desk is in its intended open position, and compare the stable reading with the documented contact state. If the result is inconsistent, distinguish contact behavior from wiring and mechanical actuation before drawing a conclusion.

## Sources and references

- Defense Logistics Agency ASSIST: [MIL-PRF-8805K: Switches and Switch Assemblies, Sensitive, Snap Action, General Specification For](https://quicksearch.dla.mil/qsDocDetails.aspx?ident_number=7196){: rel="nofollow noopener noreferrer" }
- Wikipedia: [Miniature snap-action switch](https://en.wikipedia.org/wiki/Miniature_snap-action_switch){: rel="nofollow noopener noreferrer" }
