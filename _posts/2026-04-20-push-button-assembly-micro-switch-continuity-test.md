---
title: "Push button assembly micro switch continuity test"
description: "push button assembly micro switch continuity test: Understand the operating idea, essential terminology, practical checks, limitations, and evidence."
date: 2026-04-20 21:43:46 +0800
last_modified_at: 2026-10-13 11:46:37 +0800
category: Troubleshooting
tags:
  - push button assembly micro switch continuity test
  - micro switches
  - Troubleshooting
author: editorial_team
---

A push button assembly micro switch continuity test checks whether the isolated electromechanical micro switch shows the documented contact behavior in defined actuator states. It does not test the entire push-button assembly or prove that its wiring and control circuit operate correctly. The expected result depends on the exact switch’s documented terminal arrangement and contact behavior, so do not infer terminals or readings from the switch’s physical layout.

The useful comparison is between readings taken across identified terminals with the actuator released and actuated. First establish safe isolation and remove circuit effects from the measurement. If you cannot verify isolation or identify the terminals from the applicable documentation, stop and ask a qualified person to perform the work.

## What the push button assembly micro switch continuity test can establish

A micro switch is an electromechanical component. In a push-button assembly, an external button or mechanism may move its actuator, but the assembly and its control circuit are not the switch itself. Some push-button devices may use a micro switch; the name of the host device alone does not establish its internal design.

A continuity check can compare the electrical behavior across a documented pair of switch terminals in a specified actuator state. The relevant states for this procedure are released and actuated. The expected reading in each state must come from the documentation for the particular switch and contact arrangement. There is no universal terminal pair or released-versus-actuated result that can be assumed for every assembly.

The test has a narrow boundary. It can provide evidence about the isolated switch under the states and terminal pair tested. It cannot, by itself, establish that the assembly is wired correctly, that its control logic behaves as intended, or that the complete equipment operates safely. A reading is meaningful only in relation to the identified terminals, actuator state, and test isolation.

A reading that agrees with the documented behavior is not a verdict on the whole assembly. Wiring, connections, the push-button mechanism, and other parts of the host equipment are outside what that isolated reading establishes. Likewise, a reading that does not agree is a reason to verify the test conditions and identification before concluding that the switch has failed.

## Prepare the micro switch for a meaningful continuity reading

Start by confirming which component in the assembly is the micro switch. Do not treat every push button, panel control, or other device called a switch as a micro switch. The test described here concerns the electromechanical micro switch only, not the complete control circuit.

Before measuring, the switch must be safely isolated from power and from circuit connections that could affect the reading. Follow applicable deenergization and qualification requirements. Do not perform a continuity test on a live or energized circuit. If you are unsure whether the assembly is isolated, or if safe isolation is outside your training or authority, stop and have a qualified person handle the work.

Next, identify the switch terminals using its connection diagram and terminal markings. Use documentation for the exact switch and equipment to determine which terminals to measure and what contact behavior is expected in each actuator state. Do not identify terminals by position, shape, or proximity alone. A generic diagram or physical-layout assumption may not match the particular component.

Keep the expected behavior tied to its stated conditions. A rating or specification for a particular current type, load, or test condition does not establish a different rating or condition. For this continuity check, consult the applicable specification or connection documentation rather than assuming that an electrical rating or contact arrangement transfers from another design. If terminal identification or the relevant documentation is unclear, do not guess; seek qualified assistance.

## Measure the micro switch in released and actuated states

Once safe isolation, terminal identification, and expected behavior are established, make the comparison in a controlled sequence:

1. **Record the test basis.** Note the identified terminal pair and the actuator state to be measured. Use the documented pair and expected behavior for that switch, not a presumed common arrangement.
2. **Measure with the actuator released.** With the switch isolated from circuit effects, use a continuity meter across the identified pair. Record the reading and confirm that the actuator is in the released state.
3. **Measure with the actuator actuated.** Move the actuator through the intended mechanical action, then measure across the same identified pair. Record the reading and confirm that the actuator is actuated for this measurement.
4. **Compare with documentation.** Check both readings against the documented contact behavior for the identified terminals in the recorded states. If the documentation does not specify the expected behavior, the readings cannot be judged against an assumed universal pattern.

The state record matters: the released and actuated readings describe different conditions. Do not compare a reading taken in one state with documentation for the other. If the actuator cannot be moved as intended, or its state is uncertain, that makes the electrical comparison inconclusive rather than proving a contact fault.

A click may indicate movement of a snap mechanism, but it does not establish electrical continuity. Conversely, an isolated continuity reading covers only the measured terminal pair and state. Neither a click nor one reading proves that the switch is healthy in every condition, that the assembly wiring is correct, or that the host equipment will operate properly.

### Related guides

- [espresso machine drip tray micro switch troubleshooting](/guides/espresso-machine-drip-tray-micro-switch-troubleshooting/)
- [micro switch condensation troubleshooting](/guides/micro-switch-condensation-troubleshooting/)
- [how to test a extrusion machine home position micro switch](/guides/how-to-test-a-extrusion-machine-home-position-micro-switch/)
- [cash drawer position micro switch intermittent operation](/guides/cash-drawer-position-micro-switch-intermittent-operation/)

## Interpret a continuity result without overdiagnosing

If a reading differs from the documented behavior, first verify the basis of the comparison: Was the switch safely isolated from circuit effects? Were the correct terminals identified from documentation? Was the actuator actually in the recorded state? Were the expected readings taken from the documentation for that same terminal pair and state? A mismatch is not enough on its own to identify the cause.

Different causes remain possible. The actuator may not be reaching the intended state, the internal contacts may not show the documented behavior, the terminals may have been misidentified, or wiring or another part of the host equipment may be involved. These possibilities are distinct; an isolated component reading does not locate a problem elsewhere in the assembly. If the test conditions and terminal identification are confirmed but the reading still differs from documented behavior, have a qualified person assess the switch and assembly rather than inferring a repair from the reading alone.

If both readings agree with the documented behavior, the result supports only that the measured terminal pair behaved as documented in those tested states. It does not prove correct installation, wiring, control logic, or overall operation. Further assessment of those matters is separate and may require qualified work.

The push button assembly micro switch continuity test is therefore a limited, state-based component check: isolate the switch, identify the documented terminals, record released and actuated states, and compare each result with the applicable documentation. Treat the result as evidence about that test, not as a verdict on the complete push-button assembly.

## Sources and references

- Defense Logistics Agency ASSIST: [MIL-PRF-8805K: Switches and Switch Assemblies, Sensitive, Snap Action, General Specification For](https://quicksearch.dla.mil/qsDocDetails.aspx?ident_number=7196){: rel="nofollow noopener noreferrer" }
- Occupational Safety and Health Administration: [29 CFR 1910.333: Selection and Use of Work Practices](https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.333){: rel="nofollow noopener noreferrer" }
