---
title: "Dumbwaiter open position micro switch continuity test: how to check it"
description: "dumbwaiter open position micro switch continuity test: Understand the operating idea, essential terminology, practical checks, limitations, and evidence."
date: 2026-10-13 11:27:16 +0800
category: Troubleshooting
tags:
  - dumbwaiter open position micro switch continuity test
  - micro switches
  - Troubleshooting
author: editorial_team
---

A **dumbwaiter open position micro switch continuity test** checks the isolated switch’s contact behavior in a defined actuator state. It does not test the dumbwaiter’s full control system. The key is to establish whether the open-position mechanism actually moves the switch actuator, identify the contact path from documentation, and compare the measurement with the documented behavior for that state. A door or platform that appears open does not, by itself, show that the switch actuator has moved or that the switch contacts are in a particular state.

## What the dumbwaiter open position micro switch continuity test can establish

The test can establish whether an identified contact path on an electrically isolated micro switch shows continuity in a specified actuator state. That is a switch-level observation. The result is meaningful only when the tested state, terminal identification, and applicable contact documentation are clear.

“Open position” describes the dumbwaiter mechanism’s intended position for this test, not a guaranteed electrical state. Depending on the particular mechanism and documented contact arrangement, the mechanism may act on the switch in a particular way; the name of the position alone does not establish which contacts should show continuity. Do not assume that the switch uses a particular terminal arrangement or that its contacts change state in a particular direction.

The switch is one component in the equipment. Its contact state is distinct from the wiring and control logic connected to it. A continuity result therefore does not establish that the dumbwaiter’s installed circuit or overall operation is correct.

## Define the open-position actuator state before measuring

First identify the mechanism’s action on the switch actuator. Define the test state by the mechanism reaching the position at which it is intended to contact or move that actuator, as established by the applicable equipment documentation or other reliable, specific information. Do not substitute “the door looks open” or “the platform appears at the open position” for evidence of actuator movement.

If it is not clear whether the mechanism reaches the actuator, or whether the actuator moves, the state has not been established well enough to interpret a reading as the open-position result. Keep the observation specific: note the mechanism’s position and whether it contacts or moves the actuator. Do not infer an electrical contact state from that mechanical observation.

Actuator travel terms can help describe motion when the relevant design information uses them. Pretravel runs from the free position to the operating position; overtravel runs from the operating position to the extreme permitted actuator position. These definitions do not supply travel values or prove that a particular dumbwaiter mechanism reaches either point. Use them only to describe a documented or observed condition, not to create a missing specification.

## Isolate the micro switch and identify its terminals

Continuity testing requires electrical isolation. Follow the applicable documented isolation procedure, and do not measure continuity on an energized circuit. The appropriate procedure depends on the equipment and work conditions; this article does not establish how to isolate a particular dumbwaiter.

In the United States workplace context, the cited rule generally requires exposed live parts to be deenergized before work. It also requires a qualified person to verify the deenergized condition with test equipment and limits work on energized parts to qualified persons. Verify all applicable requirements. If the documented isolation and verification steps are not available or cannot be performed within the worker’s qualifications, stop and refer the work to qualified personnel.

Identify the terminals using the connection diagram and terminal markings applicable to the exact switch and equipment. Do not infer terminal function from physical position or appearance. Use documented contact labels and circuit function; do not assume that COM, NO, or NC labels apply unless they are documented for that switch. The documented permissible load is relevant to circuit applicability, but it does not replace terminal identification or establish the result of an isolated continuity test.

## Measure continuity in the defined open-position state

With the switch isolated and its terminals identified, place or retain the mechanism in the defined open-position actuator state using the applicable procedure. Measure only the documented contact path for that state. Record which terminals were tested, the actuator condition, and the observed continuity result. The reading should be interpreted against the contact arrangement and behavior documented for the specific switch and reference condition, not against a generic expectation for an “open position.”

If documentation describes contact behavior at a specified reference condition, compare the measurement with that condition. If the reference condition or expected behavior is absent, the result cannot be classified as matching or mismatching on the basis of the position name alone. Do not invent an expected continuity reading, infer one terminal’s function from another, or treat the meter’s indication as proof of the switch’s suitability for an installed load.

Keep the mechanical and electrical observations separate. The mechanism may appear to reach its intended position without moving the actuator as expected; alternatively, the actuator may move while the measured contact result differs from the documented behavior. These are distinct observations that call for checking the relevant documentation and conditions, not jumping to a conclusion about the whole dumbwaiter.

## Interpret a mismatch without blaming the whole dumbwaiter

If the isolated result differs from documented contact behavior, check the basis of the comparison first: was the correct actuator state established, were the correct terminals identified, and does the documentation specify the same reference condition as the test? A mismatch may involve the mechanism’s ability to reach or move the actuator, the switch’s contact behavior, or an error in terminal identification. The available observation does not by itself determine which explanation is correct.

A result that agrees with the documented behavior in one defined state is limited to that switch-level observation. It does not rule out a wiring fault, a problem in the control system elsewhere, or another issue in the equipment. Likewise, an unexpected installed-system symptom cannot be attributed to the switch solely because the switch is present. Wiring and control-system causes are separate possibilities and require their own verification under the applicable procedure.

Keep the diagnostic conclusion narrow: state what was isolated, which documented terminals were measured, what actuator state was established, and whether the reading agreed with the applicable documentation. If any of those elements is unknown, say so rather than declaring the switch or dumbwaiter good or bad.

### Related guides

- [espresso machine drip tray micro switch troubleshooting](/guides/espresso-machine-drip-tray-micro-switch-troubleshooting/)
- [micro switch condensation troubleshooting](/guides/micro-switch-condensation-troubleshooting/)
- [how to test a extrusion machine home position micro switch](/guides/how-to-test-a-extrusion-machine-home-position-micro-switch/)
- [cash drawer position micro switch intermittent operation](/guides/cash-drawer-position-micro-switch-intermittent-operation/)

## What an isolated continuity result does not prove

An isolated continuity result does not prove that the switch is correctly installed, that the wiring is correct, that the control logic behaves as intended, or that the dumbwaiter is safe to operate. Nor does one result prove the equipment works or identify every possible fault. The test addresses only the documented contact path under the tested, defined actuator state.

Do not use the result as permission to restore power, operate the equipment, or bypass other required checks. Work beyond the documented isolation and test procedure, including assessment of installed wiring or the larger control system, belongs to qualified personnel following applicable requirements. A defensible conclusion is limited to whether the isolated switch’s measured contact behavior matches its documentation in the established open-position actuator state. That boundary is what makes a dumbwaiter open position micro switch continuity test useful without mistaking it for a complete system diagnosis.

## Sources and references

- Defense Logistics Agency ASSIST: [MIL-PRF-8805K: Switches and Switch Assemblies, Sensitive, Snap Action, General Specification For](https://quicksearch.dla.mil/qsDocDetails.aspx?ident_number=7196){: rel="nofollow noopener noreferrer" }
- Occupational Safety and Health Administration: [29 CFR 1910.333: Selection and Use of Work Practices](https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.333){: rel="nofollow noopener noreferrer" }
