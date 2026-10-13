---
title: "Railway point machine limit micro switch continuity test: what does it show?"
description: "railway point machine limit micro switch continuity test: Understand the operating idea, essential terminology, practical checks, limitations, and."
date: 2026-10-13 11:27:16 +0800
category: Troubleshooting
tags:
  - railway point machine limit micro switch continuity test
  - micro switches
  - Troubleshooting
author: editorial_team
---

A railway point machine limit micro switch continuity test can indicate whether the switch’s tested contacts change state under a defined actuator condition. It cannot, by itself, establish that the installed wiring, control circuit, or railway equipment is functioning correctly. The result is meaningful only when the switch is isolated under the applicable procedure, its terminals are identified from its documentation, and the actuator state is defined.

A micro switch is one component within a railway point machine and its surrounding control circuit. The component’s contact behavior is distinct from the behavior of the wiring and equipment connected to it. An isolated reading therefore answers a narrower question than a measurement through installed wiring or a check of the machine’s operation.

## What a railway point machine limit micro switch continuity test can establish

An isolated continuity check can indicate whether the particular contacts being measured are conducting or not conducting in the specified actuator state. If readings are taken in more than one defined state, they may indicate whether those contacts change state as documented. The conclusion applies to the contacts and conditions actually tested, not automatically to the switch’s full performance.

The test does not establish that a point machine has reached a required mechanical position, that its installed wiring is intact, or that its control circuit interprets a contact correctly. Nor does it prove the operation of the complete machine, an interlocking, or a signaling function. A continuity result concerns the isolated switch under the test conditions; the surrounding apparatus requires its own equipment-specific assessment.

Interpret the result against the switch’s exact terminal marking or schematic and the applicable test procedure. Do not infer an expected reading merely from the fact that the switch is used as a limit detector. The switch’s contact arrangement and the documented actuator reference state determine what reading to expect.

## Why actuator state and terminal identification determine the reading

A contact reading has meaning only in relation to which terminals are measured and what actuator state is being tested. A generic changeover contact may use the labels COM, NO, and NC, but those labels and their state convention must be confirmed for the actual device. The exact switch marking or schematic controls; a generic convention is not a substitute for device documentation.

Likewise, the expected state cannot be assigned from the railway application alone. The available information does not establish a universal normal position for a point-machine limit switch, a universal contact arrangement, or which actuator position should correspond to a particular continuity result. Use the reference condition specified for the actual switch and test procedure rather than assuming how the machine’s limit detector is configured.

Actuator movement also needs a precise description. Operating and release are different events, so a reading taken while the actuator is moving may not correspond to either specified reference state. Overtravel is the distance or angle between the operating position and the extreme position to which the actuator may be moved. Numerical travel limits are device-specific requirements that must be checked in the applicable specification sheet; they cannot be inferred from the micro-switch category.

A click can indicate movement of a snap mechanism, but it does not prove that the tested contacts have electrical continuity or that the correct terminals were selected. The electrical reading, terminal identification, and actuator state must be considered together.

## A safe, limited interpretation sequence for an isolated switch

A valid interpretation begins with the applicable equipment-specific isolation and test procedure, not with a generic field method. Railway point-machine and signaling equipment may have installation and work requirements that are not established by an isolated switch description. Access, isolation, and testing of that equipment must be handled by qualified personnel following applicable procedures.

Within that boundary, the conceptual checks are limited: establish that the switch is isolated as required by the procedure; identify the terminals from the exact device marking or schematic; determine the defined actuator reference state; and compare the measured continuity with the documented contact behavior for those terminals and that state. The test method and expected readings must come from the applicable procedure and device documentation. This article does not supply railway-specific isolation steps or instructions for testing an installed signaling circuit.

If contact resistance, rather than a simple continuity indication, is being evaluated, the result also depends on the specified method, connection points, and limit. Those requirements must come from the applicable specification and test procedure. A continuity observation should not be treated as a substitute for a contact-resistance requirement or as proof that every electrical performance criterion has been met.

Electrical work has a firm boundary. Under the cited United States workplace rule, exposed live parts generally must be deenergized before work; a qualified person must verify the deenergized condition with test equipment; and work on energized parts is limited to qualified persons. Applicable requirements must be verified for the work. Do not infer that an isolated-component check establishes that the installed equipment is safe to work on.

## If the continuity result is unexpected: separate the possible causes

An unchanged or unexpected reading is a diagnostic clue, not proof of a single failure. Consider distinct possibilities in light of the documented test conditions:

- **Actuator state:** The actuator may not have reached the specified position, or the observation may have been made during movement rather than at a defined reference state. That possibility does not establish the machine’s alignment or railway safety.
- **Terminal identification or state assumption:** The measured terminals may not be the intended pair, or the expected reading may rely on an undocumented assumption about COM, NO, NC, or the actuator reference state. Check the exact device marking or schematic and applicable procedure.
- **Measurement setup:** The setup or method may not match the required test conditions. Without the specified method and connections, an unexpected indication cannot be attributed confidently to the switch contacts.
- **Contact condition:** An internal contact issue is one possible explanation if the terminal pair, actuator state, isolation, and measurement method have been established. The observation alone does not identify a specific internal fault.
- **Other equipment:** If the isolated switch behaves as documented but the installed indication differs, the cause may be in wiring, control logic, or other equipment. The isolated test cannot localize that problem.

These possibilities should remain separate until the evidence distinguishes them. A switch-level reading cannot establish whether the point machine’s control circuit, wiring, or other apparatus is responsible for an installed-system symptom. Do not turn a component-level observation into a conclusion about machine position or railway operation.

### Related guides

- [espresso machine drip tray micro switch troubleshooting](/guides/espresso-machine-drip-tray-micro-switch-troubleshooting/)
- [micro switch condensation troubleshooting](/guides/micro-switch-condensation-troubleshooting/)
- [how to test a extrusion machine home position micro switch](/guides/how-to-test-a-extrusion-machine-home-position-micro-switch/)
- [cash drawer position micro switch intermittent operation](/guides/cash-drawer-position-micro-switch-intermittent-operation/)

## What this railway point machine limit micro switch continuity test cannot prove

A continuity test of an isolated micro switch cannot prove that the complete point machine, installed circuit, interlocking, or signaling function is correct. It cannot establish a fault location in the installed system, and it cannot demonstrate safe operation or suitability for a particular railway function without the relevant device information and equipment-specific evidence.

Its defensible conclusion is narrower: under the stated isolation, terminal, measurement, and actuator-state conditions, the tested contacts did or did not show the documented continuity behavior. If those conditions are unknown, the reading is not enough to diagnose the switch. If the switch result matches its documentation but an installed indication remains unexpected, the cause lies beyond what this component-level check can determine.

Stop at that boundary and leave further railway equipment assessment to qualified personnel following applicable procedures. A railway point machine limit micro switch continuity test is one limited observation of a component, not proof of the condition or safety of the surrounding system.

## Sources and references

- Defense Logistics Agency ASSIST: [MIL-PRF-8805K: Switches and Switch Assemblies, Sensitive, Snap Action, General Specification For](https://quicksearch.dla.mil/qsDocDetails.aspx?ident_number=7196){: rel="nofollow noopener noreferrer" }
- Occupational Safety and Health Administration: [29 CFR 1910.333: Selection and Use of Work Practices](https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.333){: rel="nofollow noopener noreferrer" }
- Wikipedia: [Miniature snap-action switch](https://en.wikipedia.org/wiki/Miniature_snap-action_switch){: rel="nofollow noopener noreferrer" }
