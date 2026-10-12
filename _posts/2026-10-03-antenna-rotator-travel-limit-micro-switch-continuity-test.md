---
title: "Antenna rotator travel limit micro switch continuity test"
description: "antenna rotator travel limit micro switch continuity test: Understand the operating idea, essential terminology, practical checks, limitations, and."
date: 2026-10-03 09:00:00 +0800
category: Troubleshooting
tags:
  - antenna rotator travel limit micro switch continuity test
  - micro switches
  - Troubleshooting
author: editorial_team
---

An antenna rotator travel limit micro switch continuity test checks whether the switch’s contacts change state when its actuator is operated at the intended limit. The useful result is a comparison across the disconnected switch itself, not a resistance reading through the rotator’s wiring. A reading that does not change is not, by itself, proof that the switch has failed: the mechanism may not be moving the actuator, or a lead or connection may be open.

The test is limited to the switch and its contact-state change. It does not test the rotator motor, controller, antenna feed line, or travel calibration. Keep the rotator unpowered and do not force its travel or bypass the limit switch. If the wiring, circuit documentation, or safe isolation cannot be established, stop rather than guessing at terminals or testing an energized circuit.

## Safety and isolation before the antenna rotator travel limit micro switch continuity test

Turn off and isolate power to the rotator before accessing or measuring the switch. Prevent accidental operation while the test is underway. Electrical work on exposed live parts is outside this procedure. A United States workplace rule generally requires exposed live parts to be deenergized before work; a qualified person must verify the deenergized condition with test equipment, and work on energized parts is limited to qualified persons. Verify all applicable requirements for the work setting.

With power isolated, disconnect at least one switch lead before measuring. This separates the switch from parallel paths in the rotator circuit that could affect a continuity reading. Use the meter’s continuity mode only on the unpowered, isolated circuit, and place the probes directly across the selected switch terminals. Do not infer that an installed circuit is safe from a meter reading across the switch.

If you cannot identify a way to isolate power or disconnect a lead without creating uncertainty about the circuit, do not proceed. The test requires a known, unpowered condition and a measurement across the switch rather than through connected equipment.

## Identify the micro switch terminals and expected contact states

Read the terminal markings or consult the circuit documentation before choosing probe points. Do not assume that terminals occupy a universal physical position or that a particular antenna rotator uses a specific wiring arrangement. Where the device uses changeover terminology, COM means common, NC means normally closed, and NO means normally open. Confirm the exact device schematic before relying on those labels.

For the contact-state comparison, note whether the actuator is at rest or has been operated. “Normally” refers to the contact state at the unoperated reference condition; it is not a guarantee about current flow in the installed rotator. Across the relevant pair, an NO contact is open at rest and closed when actuated; an NC contact is closed at rest and open when actuated. These opposite patterns provide the expected change to compare with the meter reading.

Select the documented contact pair and keep the same pair for both measurements. If markings or documentation do not establish which terminals form the relevant pair, do not guess based on terminal location or a presumed rotator circuit.

## Perform the continuity test at rest and at the travel limit

Keep rotator power isolated and the switch lead disconnected. Place the meter probes across the selected contact pair. First record the continuity indication with the actuator at rest. Then, only if the mechanism can be moved safely within its intended travel, observe the reading as the mechanism reaches the point where it operates the switch. Do not energize the rotator or force the mechanism to reach that point.

Compare the two states. For an NO pair, expect no continuity at rest and continuity when actuated. For an NC pair, expect continuity at rest and no continuity when actuated. The relevant finding is the change between states, not a universal numeric threshold. This procedure does not establish a particular resistance specification or prove the switch suitable for a load.

If the mechanism cannot safely reach the switch’s operating point while power is isolated, the state comparison is incomplete. Do not substitute a powered run or forced travel for the test. Record which states were actually measured so that an absent actuation state is not mistaken for a failed contact.

## Interpret no change: contact, wiring, or mechanical actuation

If the meter indication does not change, first determine whether the actuator physically operates the switch. Observe whether the mechanism reaches and moves the actuator at the intended point without forcing travel. If it does not, the result may reflect missed mechanical actuation; it does not establish that the contacts have failed. Numerical travel limits are device-specific requirements of the applicable specification sheet and must not be inferred from the component category.

If the actuator is operated but the selected contact pair shows no expected state change, a contact or switch fault is a possibility. That result alone does not identify the cause conclusively. Recheck that the probes are on the documented pair and that the two stated conditions were actually reached.

Keep wiring diagnosis separate from the switch test. Check disconnected leads and connections separately for an open lead or poor connection, rather than measuring through the connected rotator circuit and treating that reading as a switch result. A fault in a lead or connection can interrupt the circuit even when the switch’s own contact state changes. The continuity comparison across the isolated switch and separate lead checks answer different questions.

### Related guides

- [automated guided vehicle guard interlock micro switch intermittent operation](/guides/automated-guided-vehicle-guard-interlock-micro-switch-intermittent-operation/)
- [assembly robot travel limit micro switch failure causes](/guides/assembly-robot-travel-limit-micro-switch-failure-causes/)
- [air compressor travel limit micro switch troubleshooting](/guides/air-compressor-travel-limit-micro-switch-troubleshooting/)
- [boom lift travel limit micro switch symptoms](/guides/boom-lift-travel-limit-micro-switch-symptoms/)

## Restore the circuit and verify safe operation

After testing, reconnect the lead as documented and secure the connections before restoring power. Do not bypass the limit switch, and do not energize the rotator as part of the isolated continuity test. If the mechanism can be checked safely without exceeding its intended travel, verify that it can actuate the switch; do not force travel to obtain a result.

The test supports a bounded conclusion: whether the selected contact pair changed continuity between the measured rest and actuated states under the isolated test conditions. A state change does not establish that the wiring, controller, motor, or complete rotator assembly works correctly. No change calls for distinguishing contact behavior from terminal identification, lead continuity, and mechanical actuation rather than declaring a single cause.

In short, an antenna rotator travel limit micro switch continuity test is meaningful when power is isolated, a lead is disconnected, the documented contact pair is measured directly, and rest and safely actuated states are compared. If any of those conditions is uncertain, the result cannot reliably identify the switch as the fault.

## Sources and references

- Defense Logistics Agency ASSIST: [MIL-PRF-8805K: Switches and Switch Assemblies, Sensitive, Snap Action, General Specification For](https://quicksearch.dla.mil/qsDocDetails.aspx?ident_number=7196){: rel="nofollow noopener noreferrer" }
- Occupational Safety and Health Administration: [29 CFR 1910.333: Selection and Use of Work Practices](https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.333){: rel="nofollow noopener noreferrer" }
- Wikipedia: [Miniature snap-action switch](https://en.wikipedia.org/wiki/Miniature_snap-action_switch){: rel="nofollow noopener noreferrer" }
