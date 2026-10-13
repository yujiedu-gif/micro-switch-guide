---
title: "Vibratory feeder end of stroke micro switch not working: how to diagnose it"
description: "vibratory feeder end of stroke micro switch not working: Understand the operating idea, essential terminology, practical checks, limitations, and evidence."
date: 2026-10-13 11:27:16 +0800
category: Troubleshooting
tags:
  - vibratory feeder end of stroke micro switch not working
  - micro switches
  - Troubleshooting
author: editorial_team
---

A **vibratory feeder end of stroke micro switch not working** is a symptom to investigate, not proof that the switch itself has failed. The feeder may not be moving the actuator, the isolated switch contact state may differ from its documented behavior, or a terminal, wiring, or downstream control issue may account for the missing response. These possibilities need separate checks.

First confirm that the specific feeder design uses an electromechanical micro switch for end-of-stroke detection. A micro switch is a component; it is not the feeder or its control logic. The switch’s contact change and the system’s response depend on the actual design and circuit. Do not assume a particular switch location, contact arrangement, normal state, or feeder action from the symptom alone.

## What “vibratory feeder end of stroke micro switch not working” does, and does not, tell you

A missing expected end-of-stroke response establishes only that the observed result differs from what someone expected. It does not identify which part of the detection and control path is responsible. The mechanical input, switch contacts, terminal identification, wiring, and downstream control behavior are distinct points to consider.

Begin by confirming that this particular feeder uses a micro switch in the end-of-stroke function. Equipment designs vary, and the presence of a feeder or an end-of-stroke symptom does not establish that a micro switch is installed. If the design documentation identifies another sensing method, the micro-switch checks in this article do not apply to that component.

If documentation confirms a micro switch, establish what the actual circuit is intended to detect and what response is expected. Do not infer that an end-of-stroke contact must stop, start, or signal the feeder. The switch may change contact state, but the resulting system behavior depends on how it is connected and how the control circuit interprets that change.

This distinction prevents a common diagnostic error: treating the absence of a machine response as direct evidence of an internal contact failure. A control response can be absent even when the switch operates, and a switch may fail to receive the mechanical input it needs. The next check is therefore whether the feeder’s mechanism reaches and moves the switch actuator.

## Check whether feeder movement reaches the micro switch actuator

Under safe conditions, observe the external mechanism that is supposed to operate the actuator. Determine whether it reaches the relevant point and actually moves the actuator. If it does not, the symptom may originate in the mechanical input path rather than in the switch contacts. The observation does not, by itself, establish why the mechanism failed to reach or move the actuator.

Keep the component and the surrounding mechanism distinct. The actuator is the part of the micro switch moved by the external mechanism. A mechanism that stops short, misses the actuator, or does not move it presents a different diagnostic possibility from an actuator that is moved but whose contacts do not behave as documented. Do not assume a particular linkage, cam, mounting arrangement, or adjustment method for a feeder whose design has not been established.

Operation and release are separate events. Operation occurs when the actuator causes the switch to change from its unoperated state; release is the return after the actuating input is reduced sufficiently. The release force, or releasing force, is the force or torque to which force on the actuator must be reduced to permit the contacts to return to the unoperated position after operation. That definition does not supply a force value or a feeder-specific adjustment limit.

Accordingly, observe the relevant state transition without inventing a required travel distance, force, or position. If the mechanism moves the actuator through the expected event, that supports moving on to a state-specific contact check, but does not prove that the contacts are good. If movement does not reach the actuator, the input path remains a plausible source of the symptom. A click may indicate movement, but it cannot settle either question electrically.

## Verify the isolated micro switch contact state

A continuity check can help assess the switch contacts only when the switch is safely isolated and the actuator state is defined. Identify the switch and its documented contact arrangement and reference condition first. Then compare the measured contact behavior in the stated actuator state with the behavior documented for that exact switch. Without that information, there is no supported basis for assuming which terminals should show continuity.

Use the switch’s own terminal markings or documentation to identify connections. Do not infer terminal function from physical position, appearance, or a generic layout. COM means common only when that contact arrangement is documented; NO and NC describe contact state at a specified reference condition, not an unconditional promise about current flow. The applicable reference state matters when interpreting a reading.

Keep the test narrowly bounded. A click alone does not prove continuity, contact condition, correct wiring, or suitability for a load. Likewise, a continuity result is evidence about the isolated switch in the defined test state; it does not establish that the installed circuit is safe or that the whole feeder assembly works correctly. One reading cannot certify the complete mechanical, electrical, and control path.

If the isolated contact behavior differs from the documented expectation, that is a contact-state discrepancy to investigate. It does not automatically explain the system symptom or authorize an adjustment or repair. Confirm that the switch identity, terminal identification, actuator state, and isolation condition were all correct before drawing even that limited conclusion. If those conditions cannot be established safely, stop rather than improvise a test.

## Separate terminal, wiring, and control-response faults

If the isolated contact behavior matches the documented expectation, the missing feeder response may lie elsewhere. Terminal identification, wiring, and downstream control behavior are separate possibilities. Trace the actual connection diagram, terminal markings, circuit function, and permissible load documented for the exact switch and equipment. Do not replace those records with a generic assumption about switch layout or end-of-stroke wiring.

An installed response that does not match expectations does not alone show that the micro switch caused the problem. A switch can have the expected isolated contact behavior while the relevant terminal has been misidentified, the wiring differs from the documented circuit, or another element affects the system response. Conversely, a discrepancy in a switch check does not establish that no other issue exists. The symptom can have more than one contributing point in the path.

Keep the circuit’s intended behavior unresolved until the applicable equipment documentation establishes it. Do not assume which actuator state should correspond to an end-of-stroke condition, whether the circuit should stop or continue feeder operation, or how a controller should signal the state. Those conclusions depend on the actual design and control logic, not simply on the presence of a micro switch.

The useful diagnostic distinction is therefore between what has been observed and what remains unverified: whether the mechanism moves the actuator; whether the isolated contacts behave as documented in a defined state; whether terminals and wiring match the documented circuit; and whether the remaining control path produces its intended response. These checks narrow possibilities, but do not turn one observation into proof about the entire system.

### Related guides

- [industrial sewing machine end of stroke micro switch not working](/guides/industrial-sewing-machine-end-of-stroke-micro-switch-not-working/)
- [laser cutting machine end of stroke micro switch symptoms](/guides/laser-cutting-machine-end-of-stroke-micro-switch-symptoms/)
- [windshield wiper park position micro switch troubleshooting](/guides/windshield-wiper-park-position-micro-switch-troubleshooting/)
- [industrial boiler end of stroke micro switch failure causes](/guides/industrial-boiler-end-of-stroke-micro-switch-failure-causes/)

## Decide what the checks establish, and when to stop

Use the findings as limited evidence. If the external mechanism does not move the actuator as expected, a mechanical input issue is plausible. If the safely isolated switch does not show its documented contact behavior in a defined actuator state, there is a contact-state discrepancy to resolve. If the isolated behavior matches expectations, terminal identification, wiring, or downstream control behavior remain possible explanations for the missing response. None of these observations alone certifies the whole feeder or identifies every contributing fault.

Do not probe energized equipment or infer installed-circuit safety from an isolated switch reading. Follow applicable deenergization and qualification requirements. If safe isolation, switch identification, the documented reference state, or the actual circuit cannot be established, do not continue with improvised tests or adjustments; work beyond safe, documented checks belongs to qualified personnel.

The practical conclusion is conditional: confirm the component is present, establish whether the mechanism reaches and moves its actuator, compare isolated contact behavior with the exact switch documentation, and keep terminal, wiring, and control questions separate. The phrase **vibratory feeder end of stroke micro switch not working** names the symptom under investigation, not a confirmed diagnosis. A cause is supportable only to the extent that the relevant state and path have been verified.

## Sources and references

- Defense Logistics Agency ASSIST: [MIL-PRF-8805K: Switches and Switch Assemblies, Sensitive, Snap Action, General Specification For](https://quicksearch.dla.mil/qsDocDetails.aspx?ident_number=7196){: rel="nofollow noopener noreferrer" }
- Occupational Safety and Health Administration: [29 CFR 1910.333: Selection and Use of Work Practices](https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.333){: rel="nofollow noopener noreferrer" }
