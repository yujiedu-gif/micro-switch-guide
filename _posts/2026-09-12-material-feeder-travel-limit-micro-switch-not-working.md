---
title: "Material feeder travel limit micro switch not working: how to diagnose it"
description: "material feeder travel limit micro switch not working: Understand the operating idea, essential terminology, practical checks, limitations, and evidence."
date: 2026-09-12 09:00:00 +0800
category: Troubleshooting
tags:
  - material feeder travel limit micro switch not working
  - micro switches
  - Troubleshooting
author: editorial_team
---

A material feeder travel limit micro switch not working does not identify a single cause. In a feeder design that uses a micro switch for travel detection, the failure can occur because the moving part does not reach the actuator, the actuator moves without transferring the contacts, the contacts do not change state, or the changed state does not reach the control input. Separating these stages helps keep a mechanical problem, switch problem, wiring fault, and control-path fault from being treated as the same diagnosis.

This guide applies only when the feeder’s documented travel-limit design uses a micro switch. Feeder arrangements vary, so the applicable circuit diagram, service procedure, and switch specification govern terminal identification, expected states, and allowable travel. Do not bypass the limit switch or make undocumented adjustments to keep the feeder running.

## What “material feeder travel limit micro switch not working” can mean

Treat the reported symptom as a chain to investigate: the feeder reaches its travel limit, the limit target engages the actuator, the switch contacts change state, and the control input responds. A break at any stage can look like a nonworking limit switch from outside the equipment, but each points to a different area for checking.

First establish whether this feeder actually uses a micro switch for the travel limit. If it does, identify the relevant target, actuator, switch, wiring, and receiving control input from the equipment documentation. The switch’s role is to change electrical contact state when its actuator is operated; the equipment’s circuit determines what that change means to the control system. Do not assume a particular feeder design, contact arrangement, or control response from the equipment name alone.

The useful question is not simply whether the switch clicks. It is where the documented sequence stops. If the feeder never reaches the target, begin with the mechanical travel path. If the target reaches the actuator but the contacts do not transfer, verify the switch state. If the contact state changes as expected but the control does not respond, investigate the wiring and receiving input rather than assuming the switch itself has failed.

## Make the feeder safe before checking the limit switch

Before inspecting or testing, isolate electrical power and prevent unexpected restart. Account for moving parts and stored energy according to the applicable service procedure. A feeder may present a motion hazard even when its electrical supply has been isolated, so do not reach into a hazardous path merely to observe or manipulate an actuator.

Use the equipment’s service instructions and appropriate meter safety practices. The procedure for isolating energy, accessing the switch, or measuring a control circuit depends on the actual feeder and its design. If the required isolation is unclear, the stored-energy hazard cannot be controlled, or a check would require exposure to energized circuitry or hazardous motion, stop and have qualified personnel perform it.

Do not run the feeder with the travel limit switch bypassed. A bypass removes the documented limit function and cannot establish that the feeder or its control system is safe to operate. Do not use a temporary jumper or other undocumented workaround as a diagnostic shortcut.

## Check whether feeder travel reaches and engages the micro switch

With the equipment in the safe condition required by its service procedure, inspect the mechanical path from the feeder’s moving part to the switch actuator. Confirm from the documentation which moving part serves as the limit target and how it is intended to engage the actuator. The first question is whether the target reaches the switch at all, not whether an assumed universal gap or position looks correct.

Look for an obstruction along the documented travel path, a loose switch mounting, misalignment between target and actuator, or an actuator part that appears bent or worn. Also look for evidence that the mechanism travels beyond its intended limit. These observations can help explain a missed or abnormal engagement, but they do not establish a correct adjustment by themselves.

Do not infer a numerical travel limit, clearance, or adjustment from the component category. Device-specific travel limits belong to the applicable specification sheet. Use the feeder and switch documentation for the intended geometry and travel; if those limits are unavailable or the mechanism’s condition is uncertain, do not reposition parts by guesswork.

If the target does not reach or properly engage the actuator, the electrical contact test alone will not resolve that mechanical cause. Address the mechanical path only within documented service limits. If the target appears to engage the actuator, continue by checking whether the switch’s electrical state changes.

## Test the micro switch state and its documented terminals

Identify the terminals from the exact switch’s connection diagram, terminal markings, and equipment documentation. In generic changeover terminology, COM means common, NC means normally closed, and NO means normally open. Those symbols do not establish a universal physical terminal layout or the expected state for a particular feeder. Confirm the exact diagram before connecting meter leads or interpreting a reading.

With power isolated and suitable access, use a meter to check continuity across the documented common and normally open or normally closed terminals. Compare readings in the released and actuated states with the expected contact states and control logic for that circuit. The reference state matters: a reading is useful only when the switch’s actuator state and the terminals being measured are known.

A mechanical click can indicate actuator movement, but it does not prove that the contacts transferred or that the measured terminals are the correct ones. If the reading does not change as expected, first verify the terminal identification and the test states against the documentation. If those are correct and the contact state still does not change, the switch may require service or replacement according to its applicable specifications; the reading alone does not authorize an undocumented repair.

## Trace wiring and control response after the switch changes state

If the switch changes continuity in the documented released and actuated states, inspect the accessible wiring path before concluding that the feeder’s limit function works. Look for visibly damaged or disconnected conductors, loose connectors, or problems with strain relief. Follow the circuit diagram to determine which conductors connect the switch to the control input; do not infer connections from wire position or color without documentation.

A correct isolated contact-state change does not prove that the control input receives or recognizes the signal. The fault may lie in a conductor, connector, or receiving part of the circuit. Use the applicable diagram to trace the path beyond the switch. Energized control-circuit measurements may require qualified personnel and the equipment’s specified procedures; do not improvise a live test.

Keep the switch test separate from the control-path diagnosis. The continuity check concerns the isolated switch in defined actuator states. It cannot, by itself, establish that wiring is intact, that the control input responds, or that the complete feeder assembly is safe or functional.

### Related guides

- [automated guided vehicle guard interlock micro switch intermittent operation](/guides/automated-guided-vehicle-guard-interlock-micro-switch-intermittent-operation/)
- [assembly robot travel limit micro switch failure causes](/guides/assembly-robot-travel-limit-micro-switch-failure-causes/)
- [air compressor travel limit micro switch troubleshooting](/guides/air-compressor-travel-limit-micro-switch-troubleshooting/)
- [boom lift travel limit micro switch symptoms](/guides/boom-lift-travel-limit-micro-switch-symptoms/)

## Decide what the test results mean and what to do next

Use the point where the documented sequence stops to choose the next step:

- **The target misses the actuator:** Investigate the documented mechanical travel path, obstructions, mounting, alignment, and signs of wear or overtravel. Do not set a gap or travel value without the applicable documentation.
- **The target engages, but the expected contact change is absent:** Confirm the exact terminal diagram and released and actuated test states. If those are correct, have the switch serviced or replaced according to its applicable specifications.
- **The contacts change, but the control does not respond:** Follow the documented wiring path toward the receiving input. Do not replace the switch by assumption; a connection or downstream control-path issue remains possible.
- **The design, state, or test boundary is unclear:** Stop rather than bypassing the limit, making an undocumented adjustment, or testing through a hazardous energized circuit. Seek qualified service when the motion hazard or circuit behavior cannot be established from the applicable documentation.

These results narrow the fault area; they do not certify the whole feeder. Return the equipment to service only under its applicable procedure, with the limit function and associated control response verified as required by that procedure. A material feeder travel limit micro switch not working is a useful symptom description, but the next action should follow the observed failure stage, not an assumption that the switch is always the cause.

## Sources and references

- Defense Logistics Agency ASSIST: [MIL-PRF-8805K: Switches and Switch Assemblies, Sensitive, Snap Action, General Specification For](https://quicksearch.dla.mil/qsDocDetails.aspx?ident_number=7196){: rel="nofollow noopener noreferrer" }
- Occupational Safety and Health Administration: [29 CFR 1910.333: Selection and Use of Work Practices](https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.333){: rel="nofollow noopener noreferrer" }
- Wikipedia: [Miniature snap-action switch](https://en.wikipedia.org/wiki/Miniature_snap-action_switch){: rel="nofollow noopener noreferrer" }
