---
title: "Bucket elevator end of stroke micro switch continuity test"
description: "bucket elevator end of stroke micro switch continuity test: Understand the operating idea, essential terminology, practical checks, limitations, and."
date: 2026-10-13 11:27:16 +0800
category: Troubleshooting
tags:
  - bucket elevator end of stroke micro switch continuity test
  - micro switches
  - Troubleshooting
author: editorial_team
---

A bucket elevator end of stroke micro switch continuity test checks whether the isolated switch’s documented contact pair changes state as its actuator moves between defined positions. It does not test the elevator’s complete control system. This procedure applies only when the end-of-stroke arrangement actually uses a micro switch; another design may use a different sensing method.

Treat the end-of-stroke event as an actuator-position input. A moving part or linkage may move the switch actuator, and the surrounding circuit interprets the resulting contact change. The effect depends on the actual design and circuit, so this test does not establish a normal state, shutdown behavior, or contact arrangement.

## When a bucket elevator end-of-stroke input uses a micro switch

Some bucket elevator end-of-stroke arrangements use a micro switch, while others may use a different sensing method. Confirm that the installed device is a micro switch before applying this procedure. The switch is one component in a larger arrangement: elevator motion or a mechanism moves its actuator, and a contact change may provide an input to the surrounding circuit.

That relationship does not establish what the equipment should do at the end of travel. The control logic determines how an input is used, and the switch’s contact arrangement and normal state must come from documentation for the installed switch and equipment. Do not infer that the elevator should stop, signal, or respond in a particular way merely because a switch is present.

The check described here is limited to the switch’s electrical continuity across a documented contact pair in defined actuator states. It can help distinguish contact behavior from a failure of the mechanism to move the actuator, but it cannot by itself locate every fault in the end-of-stroke system.

## Bucket elevator end of stroke micro switch continuity test: safe test boundary

Continuity testing concerns the switch isolated from the circuit. A reading taken while the switch remains connected may include other circuit paths and therefore cannot be interpreted as a switch-only result. Do not probe an energized or connected control circuit as part of this check.

Safe equipment isolation and access are prerequisites. Follow applicable site procedures and requirements. Do not invent an isolation sequence from this general description. Where hazardous isolation is needed, or the required work is uncertain, qualified personnel must handle it. No live probing, repair, or control-system adjustment is part of this test.

The cited United States workplace rule generally requires exposed live parts to be deenergized before work, requires a qualified person to verify the deenergized condition with test equipment, and limits work on energized parts to qualified persons. Verify all applicable requirements. An isolated continuity reading does not establish that the equipment or circuit is safe to work on.

## Identify the contact pair and define actuator states

Before measuring, use the connection diagram, terminal markings, circuit function, and permissible load documented for the exact switch and equipment. Do not identify terminals from physical layout alone, and do not assume the installed switch has COM, NO, or NC terminals. If the contact pair cannot be identified from applicable documentation, do not interpret a reading as a test of a particular contact.

Define the two mechanical conditions to compare. The unactuated state is the switch’s documented state when the external mechanism is not moving its actuator. The actuated state is the documented condition in which the mechanism moves the actuator to the relevant end-of-stroke position. Do not force or reposition the mechanism beyond its documented permitted movement. If the actual state or expected contact behavior is unclear, stop short of drawing a conclusion.

Actuator travel has distinct reference points. Under MIL-PRF-8805K sections 6.5.14 and 6.5.16, pretravel runs from free position to operating position, while overtravel runs from operating position to the extreme permitted actuator position. These terms do not identify the elevator’s end-of-stroke position; use the installed switch and equipment documentation for that relationship.

## Measure continuity across the isolated micro switch

Once the switch is electrically disconnected from the circuit, measure only the documented contact pair. A qualified person should perform the disconnection where needed. Record whether the meter indicates continuity or an open path in each defined actuator state. Do not apply a universal resistance threshold: none is established here.

Compare the two observations with the contact behavior documented for the exact switch. The useful question is whether the reading changes, or does not change, between the specified states as expected from that documentation. A single reading without a defined state and identified contact pair is not enough to establish whether the switch behaves as intended.

Keep the test conditions attached to the result: the switch was isolated, the measured pair was identified from documentation, and the actuator was in a defined state for each observation. If any of these conditions is uncertain, the result is ambiguous rather than evidence of a particular switch fault.

## Interpret results by separating switch, actuator, and circuit faults

If the documented contact pair changes between the defined states as expected, that supports contact switching under the tested conditions. It does not prove that the installed wiring is correct, that the end-of-stroke position is reached at the right time, or that the elevator control system responds as intended.

If the reading does not change as documented, first separate possible causes rather than treating the result as a complete diagnosis. Check whether the mechanism actually moves the actuator to the relevant documented position. Confirm that the tested terminals are the documented contact pair and that the comparison used the correct actuator states. Only then can the switch-only observation be compared meaningfully with the expected contact behavior. This check does not, on its own, prove why the expected change is absent.

If isolated switch behavior matches documentation but the installed signal is absent, the remaining possibilities include wiring or control-circuit faults. Those require separate assessment through qualified procedures; an isolated switch test does not test them. A terminal-identification error can also make an otherwise valid measurement irrelevant to the intended contact pair.

### Related guides

- [espresso machine drip tray micro switch troubleshooting](/guides/espresso-machine-drip-tray-micro-switch-troubleshooting/)
- [micro switch condensation troubleshooting](/guides/micro-switch-condensation-troubleshooting/)
- [how to test a extrusion machine home position micro switch](/guides/how-to-test-a-extrusion-machine-home-position-micro-switch/)
- [cash drawer position micro switch intermittent operation](/guides/cash-drawer-position-micro-switch-intermittent-operation/)

## What the continuity check cannot establish

A click may indicate movement of a snap mechanism, but it does not prove continuity, correct terminal identification, or suitability for the application. Likewise, an isolated continuity result cannot establish circuit safety, correct installation, end-of-stroke timing, or the behavior of the elevator control system.

Do not conclude that the switch is defective or that the equipment is safe solely from an ambiguous reading or one actuator state. If terminal identity, expected behavior, isolation, or actuator position is uncertain, the test has not established a reliable switch-only result. If the expected change is absent under documented test conditions, the observation supports further qualified investigation, not an unsupported conclusion about the cause.

The bucket elevator end of stroke micro switch continuity test therefore has a bounded purpose: compare a documented contact pair in defined actuator states after the switch is isolated. Use the result to distinguish observed switch behavior from unresolved mechanical, wiring, and control-system questions, without treating it as proof of the whole equipment’s condition.

## Sources and references

- Defense Logistics Agency ASSIST: [MIL-PRF-8805K: Switches and Switch Assemblies, Sensitive, Snap Action, General Specification For](https://quicksearch.dla.mil/qsDocDetails.aspx?ident_number=7196){: rel="nofollow noopener noreferrer" }
- Occupational Safety and Health Administration: [29 CFR 1910.333: Selection and Use of Work Practices](https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.333){: rel="nofollow noopener noreferrer" }
