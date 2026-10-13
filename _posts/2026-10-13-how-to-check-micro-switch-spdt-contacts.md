---
title: "How to Check Micro Switch SPDT Contacts"
description: "how to check micro switch SPDT contacts: Understand the operating idea, essential terminology, practical checks, limitations, and evidence needed for."
date: 2026-10-13 11:27:16 +0800
category: Troubleshooting
tags:
  - how to check micro switch SPDT contacts
  - micro switches
  - Troubleshooting
author: editorial_team
---

A continuity check can compare an isolated SPDT micro switch’s contacts in two documented actuator states. How to check micro switch SPDT contacts depends on first identifying the terminals and the reference condition from the switch documentation, then recording readings state by state. A meter result from an isolated switch does not establish that the installed equipment or circuit is safe or working correctly.

## How to check micro switch SPDT contacts safely

Before testing, isolate the switch from the circuit. The continuity check described here is for the switch itself, not for an energized or connected circuit. Follow the applicable equipment procedure for deenergization and safe access. If isolation is uncertain, access is hazardous, or the work would require contact with energized parts, stop and have qualified personnel handle it.

For United States workplace work, the cited rule generally requires exposed live parts to be deenergized before work. It requires a qualified person to verify the deenergized condition with test equipment, and limits work on energized parts to qualified persons. Verify all applicable requirements for the work and setting.

Once the switch is safely isolated, keep the test boundary clear: an isolated continuity reading describes a contact path under a defined actuator condition. It does not show whether the switch is correctly wired in the equipment, whether another component is functioning, or whether the equipment is safe to operate. Do not use this test result alone as a decision to return equipment to service.

## Identify the SPDT terminals and reference state

SPDT means single-pole, double-throw: within a documented arrangement, one common connection is associated with either of two contact paths as the switch changes state. That term does not identify the physical location of any terminal, guarantee a particular contact arrangement on an undocumented switch, or establish how the surrounding equipment uses the contacts.

Use the switch’s connection diagram or terminal markings to identify COM, NO, and NC, and confirm that the documentation applies to the switch being tested. Do not infer terminal identity from location, shape, or a generic diagram. If documentation does not confirm the labels, treat the terminal identities as unknown rather than assigning them by assumption.

NO and NC describe contact state at a specified reference condition. The reference condition must come from the documentation; do not assume that a particular actuator position is the unactuated or normal state for the switch. Before taking readings, write down the documented reference condition and the actuator condition you will use for each observation. If the documentation does not define the relevant state or terminal pairs, there is no supported expected reading to compare against.

This identification step matters because a continuity result is meaningful only for the pair of terminals and actuator condition actually tested. A reading on the wrong pair, or one interpreted against an unstated reference state, cannot establish that the contacts have failed.

## How to check micro switch SPDT contacts in two actuator states

With the switch isolated and the terminals identified from documentation, use the meter’s continuity procedure. Record the actuator condition and the terminal pair for every observation. Do not apply a numerical threshold or expected result that the switch documentation does not provide.

1. Choose the first defined actuator state. It must be a state described by the switch documentation, not an assumed “released” or “pressed” condition. Check continuity between the documented terminal pairs relevant to the SPDT arrangement, and record each result alongside the state and pair tested.
2. Change to the second defined actuator state described by the documentation. Check the same relevant pairs again, then record the results with this second state clearly identified.
3. Compare the two sets of readings with the documented contact arrangement and reference condition. The purpose is to see whether the isolated switch’s observed contact paths agree with that documentation in those states. If the expected behavior is not documented, report the readings as observations rather than labeling them correct or faulty.

Keep the comparison state-specific. A result from one actuator condition cannot stand in for a result from the other, and a reading without a recorded terminal pair is difficult to interpret. The check also remains limited to the switch while isolated. It does not trace the equipment wiring or test the behavior of the complete circuit.

## Interpret readings without overdiagnosing

If an isolated reading differs from documented behavior, the mismatch is a finding, not a complete diagnosis. Possible distinctions include incorrect terminal identification, a different actuator condition from the documented reference, incomplete actuator travel, a contact problem, or another issue in the test setup. The reading alone does not determine which explanation applies. Confirm that the terminal pair and actuator state were identified correctly before drawing a conclusion about the contacts.

A click may indicate movement of a snap mechanism, but it does not prove electrical continuity or confirm that the correct contacts were tested. Treat the mechanical observation and the meter reading as different evidence. Do not use the sound or feel of actuation as a substitute for a documented, state-by-state contact check.

If the isolated readings match the documented contact behavior but the equipment still malfunctions, the switch test has not resolved the system problem. Wiring, terminal identification in the installed circuit, or other equipment may be involved. An isolated switch result cannot establish the condition or safety of those parts. Keep component findings separate from conclusions about installed wiring and equipment behavior.

### Related guides

- [espresso machine drip tray micro switch troubleshooting](/guides/espresso-machine-drip-tray-micro-switch-troubleshooting/)
- [micro switch condensation troubleshooting](/guides/micro-switch-condensation-troubleshooting/)
- [how to test a extrusion machine home position micro switch](/guides/how-to-test-a-extrusion-machine-home-position-micro-switch/)
- [cash drawer position micro switch intermittent operation](/guides/cash-drawer-position-micro-switch-intermittent-operation/)

## When to stop and seek qualified help

Stop if you cannot safely isolate the switch, cannot identify the terminals from applicable documentation, cannot establish the actuator reference states, or would need energized access to continue. Do not guess at terminal assignments or expected readings to complete the test. If the required test conditions are unclear or the work falls outside your qualifications, have qualified personnel assess the situation.

The continuity check is a limited verification of documented contact behavior in defined actuator states. It is not a repair procedure, a wiring diagnosis, or authorization to energize or return equipment to service. For how to check micro switch SPDT contacts, the reliable boundary is the evidence actually collected: identified terminals, recorded actuator states, isolated readings, and comparison with applicable switch documentation. Anything beyond those observations requires separate assessment.

## Sources and references

- Defense Logistics Agency ASSIST: [MIL-PRF-8805K: Switches and Switch Assemblies, Sensitive, Snap Action, General Specification For](https://quicksearch.dla.mil/qsDocDetails.aspx?ident_number=7196){: rel="nofollow noopener noreferrer" }
- Occupational Safety and Health Administration: [29 CFR 1910.333: Selection and Use of Work Practices](https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.333){: rel="nofollow noopener noreferrer" }
