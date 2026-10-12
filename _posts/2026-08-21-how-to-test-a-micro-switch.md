---
title: "How to test a micro switch: a safe continuity procedure"
description: "how to test a micro switch: Understand the operating idea, essential terminology, practical checks, limitations, and evidence needed for careful."
date: 2026-08-21 09:00:00 +0800
category: Troubleshooting
tags:
  - how to test a micro switch
  - micro switches
  - Troubleshooting
author: editorial_team
---

# How to test a micro switch for continuity and reliable actuation

To learn **how to test a micro switch**, use a de-energized, isolated bench setup and compare the switch’s readings before, during, and after actuation. The sequence matters: a reading taken while the switch is still connected to a circuit may reflect other electrical paths rather than the switch alone. First make the circuit safe and disconnect at least one switch connection. Then identify the terminals from their markings or contact diagram, measure the relevant contact pair at rest and while pressing the actuator, and repeat the cycle to look for inconsistent changes.

This procedure checks continuity and observable actuation behavior under the test conditions. It does not establish how the switch performs under a device’s operating load. Interpret each result in light of the identified contact arrangement; do not assume that every switch uses the same terminal layout or has the same expected state.

## How to test a micro switch safely

Before handling the switch, de-energize the circuit and verify that it is not live. Do not perform a continuity or resistance test on an energized circuit. A meter’s continuity or resistance mode is for checking the measured path under the test conditions, not for checking a powered circuit.

Next, electrically isolate the switch from at least part of the surrounding circuit. Disconnect at least one switch connection before testing. If the switch remains connected, parallel paths elsewhere in the circuit may affect the meter reading and make it appear that the switch contact has a state it does not have on its own. This is why a reading taken in circuit can be misleading.

Once the circuit is de-energized and at least one connection is disconnected, select continuity or resistance mode on the meter. Keep track of which contact pair you intend to measure. Do not treat an isolated measurement as proof of performance beyond this bench check: it describes the reading for the selected pair under the test conditions.

## Identify terminals before measuring

Read the terminal labels on the switch or consult its contact diagram or associated documentation before placing the probes. Do not infer terminal identity from physical position. A switch’s layout should not be assumed to follow a universal arrangement.

Where the markings or diagram support the identification, the common terminal is abbreviated **COM**, the normally open terminal is **NO**, and the normally closed terminal is **NC**. These names identify terminals; they do not by themselves tell you which pair you are measuring. Use the diagram or markings to determine the relevant contact pair, then record which pair was checked so the readings can be interpreted correctly.

If the terminals cannot be identified from markings or a contact diagram, treat their identities as unresolved rather than guessing. An incorrect pair can produce a reading that is real for the probes’ placement but does not answer whether the intended contact changes state. Confirming terminal identity is therefore part of the measurement, not an optional labeling step.

## How to test a micro switch at rest and during actuation

With the meter connected across the identified contact pair, begin with the actuator released. Record the reading at rest. Then press the actuator and observe the reading for the same pair. Release the actuator and check whether the reading returns to its prior state. Keep the probe positions and contact pair consistent throughout the sequence so the observations can be compared.

A useful record distinguishes the three observations: released at rest, pressed, and released again. Do not assume in advance that the pair must read open at rest or closed at rest. The expected pattern depends on the contact arrangement identified from the switch markings or diagram. The purpose of the sequence is to see whether the reading changes and returns as expected for that identified pair.

Press and release the actuator in a controlled, repeatable way. Observe the reading while pressing, not only after the actuator has been held in position. If the reading changes during the cycle, note whether it returns after release. A change that does not return to the prior resting reading is different from a repeatable transition and should be recorded as an observation rather than explained by assumption.

## Interpret readings and check for intermittent behavior

A low resistance reading or continuity indication means the measured path is closed under the test conditions. An open indication means that path is not conducting under those conditions. Neither description should be applied to the switch as a whole without specifying the contact pair and actuator state. Compare the observed rest and pressed readings with the identified contact arrangement rather than expecting one universal open-or-closed pattern.

Repeat the press-and-release sequence several times while watching the meter. Look for missed transitions, unstable readings, or a failure to return to the prior state after release. Repeating the cycle helps distinguish a consistent state change from behavior that varies from one actuation to another. Record what the meter shows at rest, during pressing, and after release, including any variation between cycles.

An inconsistent reading is an observation that merits checking, not a diagnosis by itself. First confirm that the switch remains isolated, the probes are on the intended terminals, and the selected meter mode is appropriate. If those conditions are sound, describe the result narrowly: the measured pair did not give a stable or repeatable reading during this bench test. Do not infer a cause that the continuity observations do not establish.

### Related guides

- [automated guided vehicle guard interlock micro switch intermittent operation](/guides/automated-guided-vehicle-guard-interlock-micro-switch-intermittent-operation/)
- [assembly robot travel limit micro switch failure causes](/guides/assembly-robot-travel-limit-micro-switch-failure-causes/)
- [air compressor travel limit micro switch troubleshooting](/guides/air-compressor-travel-limit-micro-switch-troubleshooting/)
- [boom lift travel limit micro switch symptoms](/guides/boom-lift-travel-limit-micro-switch-symptoms/)

## When a continuity test is inconclusive

If readings do not make sense, recheck that the circuit is de-energized and that at least one switch connection has been disconnected. Confirm probe placement, meter mode, and terminal identification before interpreting the result. A connected circuit can introduce parallel paths, and a mistaken contact-pair selection can make a correct meter indication irrelevant to the question being tested.

Mechanical alignment or actuator travel can also affect whether the switch changes state during the test. If the observed reading does not change as expected for the identified contact pair, consider whether the actuator is moving through the required travel during the bench check. The available reading alone does not establish why a transition did or did not occur.

A continuity result is limited to the measured contact pair and the test conditions. Do not use a bench continuity result alone to establish performance under a device’s operating load. The useful conclusion is whether the isolated pair showed the expected, repeatable reading pattern at rest, during actuation, and after release, based on its documented contact arrangement. If isolation, terminal identity, or the observed pattern remains unclear, the continuity test is inconclusive rather than proof of a particular fault.

This concludes the explanation of how to test a micro switch.

## Sources and references

- Defense Logistics Agency ASSIST: [MIL-PRF-8805K: Switches and Switch Assemblies, Sensitive, Snap Action, General Specification For](https://quicksearch.dla.mil/qsDocDetails.aspx?ident_number=7196){: rel="nofollow noopener noreferrer" }
- Wikipedia: [Miniature snap-action switch](https://en.wikipedia.org/wiki/Miniature_snap-action_switch){: rel="nofollow noopener noreferrer" }
