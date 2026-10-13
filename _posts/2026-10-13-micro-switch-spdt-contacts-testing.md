---
title: "How to Test micro switch SPDT contacts testing"
description: "micro switch SPDT contacts testing: Understand the operating idea, essential terminology, practical checks, limitations, and evidence needed for careful."
date: 2026-10-13 00:00:00 +0800
publication_date_only: true
category: Troubleshooting
tags:
  - micro switch SPDT contacts testing
  - micro switches
  - Troubleshooting
author: editorial_team
---

Testing the contacts of a micro switch SPDT contacts testing setup can show whether documented contact pairs change state as the actuator moves, but only when the switch is isolated and the reference condition is known. It cannot, by itself, establish that installed wiring or the surrounding equipment is functioning correctly or safe.

A miniature snap-action switch can change an electrical contact state in response to mechanical actuator movement and is commonly used for position or limit detection. The test below is narrower: it concerns the switch’s own contacts, not the complete circuit or the device being controlled.

## What micro switch SPDT contacts testing can establish

SPDT means a single-pole, double-throw contact arrangement. Here, that term is useful only if the particular switch’s documentation identifies a changeover contact and its terminals. A generic changeover contact may be labeled common, normally closed, and normally open, but the exact device marking or schematic controls.

An isolated continuity check can assess whether documented contact pairs are open or closed at particular actuator states. To interpret the result, you need the device’s specified reference condition and the expected contact behavior as the actuator moves. Without those details, a meter reading cannot be confidently compared with an expected result.

The test does not establish whether the switch is suitable for a load, whether the connected circuit is wired correctly, or whether the host equipment responds as intended. Those questions require information beyond an isolated contact observation. Keep the conclusion proportional to what was actually measured: the result describes contact continuity under the recorded test conditions.

## Identify COM, NO, and NC at the reference condition

Use COM, NO, and NC only when the switch’s own marking or schematic documents those terminals. COM is the common terminal in the documented contact arrangement. NO and NC describe contact states relative to a specified reference condition; they are not unqualified promises about current flow in an installed circuit.

Before testing, consult the exact switch documentation and identify the reference condition it specifies. Do not assume that a terminal’s physical location, shape, or position identifies it as COM, NO, or NC. If the markings are absent, unclear, or inconsistent with the documentation, terminal identity remains unresolved until verified from reliable device-specific information.

Record which terminals you identify and the basis for that identification. If the documented arrangement is a changeover contact, the relevant observations concern the documented common terminal and the other identified contact terminals. Do not transfer a generic terminal pattern to a particular switch without supporting documentation.

The reference condition matters because “normally” is tied to a defined state, not a guarantee about how a switch sits in every installation. The switch may be mechanically acted upon by an external part, and the host equipment’s arrangement is separate from the switch’s terminal definitions. Keep the documented reference condition distinct from any installed condition you happen to observe.

## Check isolated contact changes at defined actuator states

A continuity check must be performed on the switch isolated from the circuit. Electrical isolation should follow an approved safe procedure. If that procedure is not available or the work has electrical consequences beyond the isolated component, leave the work to qualified personnel. A reading taken while the switch remains connected may reflect paths elsewhere in the circuit and cannot be treated as a result for the switch alone.

Use the switch documentation to establish the reference condition, terminal identities, and expected contact behavior. Then record the actuator state for each observation, along with the contact pair measured. For example, note whether the actuator is at the documented reference condition or moved from it, rather than recording only that the switch “clicked” or that a pair “tested good.”

Compare each continuity observation with the documented expectation for that specific state and contact pair. The accepted evidence does not specify a universal expected open or closed reading at the reference condition or after actuation. Therefore, do not assume that a particular pair must show continuity in either state. If the switch documentation does not define the expected behavior, the observation can be recorded, but it cannot be classified as a pass or failure from generic terminal names alone.

Keep the actuator state controlled and describe it precisely enough that another person can understand what was measured. A change in continuity between defined states may show that contact behavior changed during the test. It does not independently establish the switch’s performance under a load or prove that the assembly containing it operates correctly.

## Interpret readings without collapsing distinct fault paths

If a documented contact pair does not change state as expected, that observation does not identify a single cause. The mechanical input may not be moving the actuator as intended, or the internal contact behavior may be involved. A continuity observation alone may not distinguish those possibilities. Do not turn an uncertain result into a diagnosis of a particular failed part.

Unexpected readings can also arise because the terminals were identified incorrectly or because the switch was not adequately isolated from the circuit. Recheck the device-specific terminal information and the isolation condition before drawing a conclusion about contact behavior. If either remains uncertain, the result is inconclusive rather than proof that the switch is defective.

An isolated contact test also does not diagnose external wiring, host equipment logic, or other equipment faults. A switch can show the documented contact change in isolation while a separate problem remains in the installed circuit. Conversely, a problem observed in the equipment does not establish that the switch itself is responsible. Keep the component test and the system diagnosis separate.

A continuity result is not a safety determination for the installed circuit. It does not establish that wiring is correct, that a control behaves as intended, or that the whole equipment assembly is functioning. Work that requires evaluating consequential electrical conditions beyond the isolated test belongs with qualified personnel.

### Related guides

- [espresso machine drip tray micro switch troubleshooting](/guides/espresso-machine-drip-tray-micro-switch-troubleshooting/)
- [micro switch condensation troubleshooting](/guides/micro-switch-condensation-troubleshooting/)
- [how to test a extrusion machine home position micro switch](/guides/how-to-test-a-extrusion-machine-home-position-micro-switch/)
- [cash drawer position micro switch intermittent operation](/guides/cash-drawer-position-micro-switch-intermittent-operation/)

## When an SPDT contact test is inconclusive

Treat the test as inconclusive when the terminal designations, reference condition, expected state changes, or isolation condition are unknown. Consult the switch’s own documentation for its terminal designations, the state used as the reference, and the expected behavior for the contact pairs. Do not fill those gaps with an assumed generic arrangement.

If the documentation supports an expected change and a controlled isolated test does not show it, the result indicates that the observed contact behavior did not match that expectation under the recorded conditions. It still does not, by itself, distinguish a mechanical actuation issue from an internal contact issue or explain an equipment-level symptom. If the expected behavior is not documented, a reading alone does not resolve whether the behavior is correct.

Continuity alone also does not establish load suitability, repairability, or replacement compatibility. The useful boundary is specific: this test can document contact observations at identified terminals and defined actuator states, under isolation, when the device’s expected behavior is known. It cannot substitute for device-specific documentation or a separate assessment of installed wiring and equipment.

In short, micro switch SPDT contacts testing is meaningful only when terminal identity, reference condition, actuator state, isolation, and expected behavior are clear. When any of those are unresolved, preserve the uncertainty rather than treating the meter reading as a complete diagnosis.

## Sources and references

- Defense Logistics Agency ASSIST: [MIL-PRF-8805K: Switches and Switch Assemblies, Sensitive, Snap Action, General Specification For](https://quicksearch.dla.mil/qsDocDetails.aspx?ident_number=7196){: rel="nofollow noopener noreferrer" }
- Wikipedia: [Miniature snap-action switch](https://en.wikipedia.org/wiki/Miniature_snap-action_switch){: rel="nofollow noopener noreferrer" }
