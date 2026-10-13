---
title: "Collaborative robot end of stroke micro switch not working: how to diagnose it"
description: "collaborative robot end of stroke micro switch not working: Understand the operating idea, essential terminology, practical checks, limitations, and."
date: 2026-10-13 11:27:16 +0800
category: Troubleshooting
tags:
  - collaborative robot end of stroke micro switch not working
  - micro switches
  - Troubleshooting
author: editorial_team
---

A **collaborative robot end of stroke micro switch not working** symptom means the expected end-of-stroke signal is missing or unexpected; it does not, by itself, prove that the switch has failed. The signal depends on a chain: robot travel must bring the mechanism into engagement with the actuator, the switch contacts must change as documented, and the wiring and controller input must convey and interpret that change. A fault or mismatch at any point can produce a similar report.

Some end-of-stroke designs use a micro switch, but the equipment documentation must confirm that this is the arrangement in the robot being checked. Use that documentation to identify the mechanism, circuit, safe-state procedure, and expected input behavior. Do not infer a contact arrangement, normal state, or control response from the switch’s presence alone.

## What “collaborative robot end of stroke micro switch not working” does, and does not, tell you

The symptom describes an observation: the expected end-of-stroke indication did not occur, or the indication differed from what was expected. It does not identify the cause. Possible points to distinguish are whether the mechanism reaches the actuator, whether the switch contacts behave as documented, whether the terminals and wiring are correctly identified, and whether the controller input changes as the equipment documentation specifies.

A micro switch is one component in that chain, not a diagnosis of the robot’s overall control behavior. The external mechanism supplies motion to the actuator; the switch’s contact change is only one step between mechanical travel and a controller indication. A problem elsewhere in the input path or control logic can therefore resemble a switch problem.

First verify from the equipment documentation that the end-of-stroke detector is a micro switch and identify its documented role. Some designs use one; others may use a different arrangement. This article addresses diagnosis of a documented micro-switch input, not robot motion faults unrelated to that input, programming of end-of-stroke logic, or replacement selection and compatibility.

## Put the robot and circuit in the documented safe state first

Before approaching moving parts, inspecting a linkage, or making electrical measurements, follow the equipment-specific safe-state and isolation procedure. This article cannot establish the correct procedure for a particular robot. If the procedure, isolation points, or permitted access are unclear, stop rather than improvise.

Do not bypass an interlock or make an exposed-live measurement as an improvised diagnostic step. The cited United States workplace rule generally requires exposed live parts to be deenergized before work, requires a qualified person to verify the deenergized condition with test equipment, and limits work on energized parts to qualified persons. Verify all applicable requirements; this general boundary is not a robot-specific isolation procedure.

If you cannot establish the required safe state or determine whether an inspection or test is permitted, refer the work to qualified personnel. Keep the safety prerequisite in place throughout the checks. A diagnostic result is not a reason to defeat a safety function or proceed outside the documented procedure.

## Check whether end-of-stroke motion actually reaches the micro switch actuator

With the mechanism in the required safe state and the permitted inspection procedure followed, trace the mechanical input: does the documented end-of-stroke motion reach and engage the actuator? Check for an apparent obstruction, looseness, misalignment, or insufficient engagement only where the equipment documentation supports that inspection. Do not adjust the mechanism beyond documented limits or assume a particular travel requirement.

If motion does not reach the actuator as documented, the symptom may arise before the switch’s contacts are tested. That observation points to an input or engagement question; it does not establish that the internal switch is sound or faulty. Conversely, visible engagement does not prove that the contacts change electrically.

A click, if one is heard or felt, is not proof of continuity, correct wiring, or a working controller input. It may indicate movement, but electrical behavior still requires a separate check under defined conditions. Keep the mechanical observation distinct from the later electrical measurement so that one is not mistaken for evidence about the other.

## Test the isolated micro switch in a defined actuator state

An isolated continuity check can address switch contact behavior only when the test setup is defined. Identify the contact arrangement and terminal names from the documentation for the exact switch and equipment. Do not assume that COM, NO, or NC terminals are present, infer terminal identity from physical layout, or guess which pair should conduct.

If the approved procedure permits the check, isolate or disconnect the switch as required. Test only the documented terminal pair, and identify the actuator state for each reading, such as the documented unactuated state and actuated state. Compare the observations with the switch’s documented contact behavior for those states. If the arrangement, reference state, or expected behavior is not documented, the reading cannot be interpreted reliably from a generic assumption.

An isolated reading applies to the tested switch, terminal pair, actuator state, and test conditions. It does not establish that the switch is suitable under load, that installed wiring is correct, or that the controller input works. Do not extend a continuity result to conditions the check did not test.

## Separate switch, wiring, and controller-input possibilities

If isolated behavior conflicts with the documented state table, first confirm the test setup, terminal identification, and mechanical state. A discrepancy may implicate the switch or its actuation, but a single reading does not settle which. Preserve the distinction between a mechanical engagement issue and a contact result.

If isolated behavior agrees with the documented contact behavior, that result supports only the isolated check. It does not clear the installed signal path. Under the approved safe procedure, verify terminal identification and trace wiring against the connection diagram for the exact switch and equipment. Use the documented circuit function and permissible load rather than a generic layout inference. If the diagram or markings are unavailable or ambiguous, do not guess at connections.

Then use the equipment’s available diagnostics to determine whether the controller input changes as documented. A missing indication at the controller, despite a matching isolated check, leaves wiring, the input path, or control logic as possibilities. Do not infer the controller’s normal state or logic merely because a micro switch is present. Programming and general robot-motion diagnosis are outside this check; use the equipment’s documented diagnostic process for those questions.

### Related guides

- [espresso machine drip tray micro switch troubleshooting](/guides/espresso-machine-drip-tray-micro-switch-troubleshooting/)
- [micro switch condensation troubleshooting](/guides/micro-switch-condensation-troubleshooting/)
- [how to test a extrusion machine home position micro switch](/guides/how-to-test-a-extrusion-machine-home-position-micro-switch/)
- [cash drawer position micro switch intermittent operation](/guides/cash-drawer-position-micro-switch-intermittent-operation/)

## Decide what the checks establish, and when to stop

An actuator inspection establishes only what was observed about mechanical engagement under the permitted inspection conditions. An isolated continuity check establishes only the tested switch behavior for the identified terminals, actuator state, and test conditions. Neither proves that the installed wiring, controller input, or complete robot assembly works correctly.

Use the evidence to keep the possibilities separate: failure to reach the actuator is a mechanical-input question; a mismatch in isolated behavior is a switch-or-actuation question to verify; a matching isolated result with a missing controller indication leaves the installed signal path or documented control response unresolved. These are diagnostic boundaries, not conclusions that one component must be at fault.

Stop and refer unresolved safety, wiring, or controller work to qualified personnel. The phrase **collaborative robot end of stroke micro switch not working** identifies a symptom to investigate, not permission to bypass a safety function, improvise a repair, or treat one test as proof that the whole assembly is good or bad.

## Sources and references

- Defense Logistics Agency ASSIST: [MIL-PRF-8805K: Switches and Switch Assemblies, Sensitive, Snap Action, General Specification For](https://quicksearch.dla.mil/qsDocDetails.aspx?ident_number=7196){: rel="nofollow noopener noreferrer" }
- Occupational Safety and Health Administration: [29 CFR 1910.333: Selection and Use of Work Practices](https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.333){: rel="nofollow noopener noreferrer" }
