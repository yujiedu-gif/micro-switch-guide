---
title: "power window limit micro switch NO and NC terminals: Contact States and Testing"
description: "power window limit micro switch NO and NC terminals: Understand the operating idea, essential terminology, practical checks, limitations, and evidence."
date: 2026-07-27 09:00:00 +0800
category: Applications
tags:
  - power window limit micro switch NO and NC terminals
  - micro switches
  - Applications
author: editorial_team
---

A **power window limit micro switch NO and NC terminals** question has two parts: identifying each terminal and understanding how its electrical state changes when the switch is actuated. For a functioning single-pole, double-throw (SPDT) switch, the unactuated position is the reference state: common connects to normally closed, while common is open to normally open. Actuating the switch reverses those connections.

Those contact states describe the switch, not what a vehicle window will do. The circuit arrangement and switch placement determine whether a contact change stops the motor, interrupts another path, or has a different effect. A continuity check can establish the switch’s contact behavior, but it does not by itself explain the whole window system.

## What the power window limit micro switch NO and NC terminals mean

In generic changeover terminology, **COM** means common, **NO** means normally open, and **NC** means normally closed. On an SPDT switch, the common terminal is the contact that changes connection between the NO and NC terminals as the actuator moves. These labels describe the switch’s contact relationship, not the physical location of a terminal or the switch’s position in a vehicle.

“Normally” refers to the switch’s **unactuated state**. This is the reference condition before the actuator is moved to operate the switch. It does not mean the window is in a normal position, that the ignition is off, or that the switch is installed in a particular orientation. Identify the state by whether the switch actuator is being operated, not by assumptions about vehicle operation.

For a functioning SPDT switch, the expected continuity states are:

| Switch condition | COM to NC | COM to NO |
|---|---|---|
| Unactuated | Closed, with continuity | Open, with no continuity |
| Actuated | Open, with no continuity | Closed, with continuity |

Thus, in the unactuated state, COM has continuity to NC and not to NO. When the actuator is moved to the actuated state, those relationships reverse. The table describes the switch contacts themselves. It does not establish which terminal is wired into a motor path or what the window will do when a contact changes.

These expectations apply to the stated SPDT arrangement. Do not assume that every switch used in a power-window design has all three terminals or uses both NO and NC contacts. A design may use a different contact arrangement, or only one contact output. Check the exact switch schematic and terminal markings before treating the table as applicable.

## How the switch contact change relates to window stopping

A limit micro switch changes an electrical path when its actuator moves. The contact-state change is a property of the switch; its effect on a power-window motor depends on how the circuit is arranged and where the switch is placed. A change in continuity alone does not show whether the motor will stop, whether another part of the circuit will be interrupted, or whether the contact change serves another purpose.

For example, a contact opening could interrupt a path only if that contact is used in the relevant path. If the circuit uses a different terminal or contact arrangement, the same switch transition need not have the same effect on motor operation. The switch’s name or location is not enough to infer the system response. The connection diagram and documented circuit function are needed to establish how the contact change relates to window movement.

Nor should the existence of a limit switch be assumed for every power-window system. Some designs may not use a limit micro switch, and a design that does use one may not use both NO and NC terminals. A general explanation of SPDT contacts describes how those contacts behave; it does not identify the circuit design in a particular vehicle or establish that a specific switch controls a window limit.

Keep the questions separate during testing: first, which contacts have continuity in each actuator state? Second, how does the documented circuit use those contacts? The first can be checked at the switch with power isolated. The second requires the applicable connection diagram, terminal marking, circuit function, and permissible load documented for the exact switch and equipment. Do not infer the circuit’s operation from a generic physical layout.

## Verify NO and NC with a continuity meter

A continuity check should test the switch without power applied to the relevant circuit. Follow applicable deenergization and qualification requirements. If the circuit cannot be safely isolated, or you cannot identify the terminals, stop rather than testing a powered circuit or guessing at connections.

Use this sequence:

1. **Isolate power to the relevant circuit and confirm it is de-energized.** Do not rely on window behavior or a wire color as proof that power is absent. Follow the applicable deenergization requirements for the equipment.
2. **Identify the terminals.** Read the terminal markings and check the exact switch schematic or equipment connection diagram. Establish which terminal is COM, NO, and NC before placing meter probes. Do not identify them from a generic physical arrangement.
3. **Record the unactuated state.** Leave the switch actuator unoperated. Set the meter to its continuity function and check between COM and NC, then between COM and NO. For a functioning SPDT switch, COM-to-NC should show continuity and COM-to-NO should be open.
4. **Record the actuated state.** Move the switch actuator to its operated position and repeat both checks. For the same SPDT arrangement, COM-to-NC should become open and COM-to-NO should show continuity.
5. **Compare the observations with the documented design.** Note the actuator state and the result for each terminal pair. If the switch is still connected to other circuitry, account for that before drawing a conclusion from a reading.

Wire color is not conclusive evidence of terminal function. Colors may not identify COM, NO, or NC in a way that can be established from the switch-contact definitions alone. Use the terminal marking and applicable diagram, then verify the contact pairs with power isolated. The meter establishes observed continuity between the probes under the test conditions; it does not establish the complete circuit’s response or permissible load.

### Related guides

- [ball screw actuator home position micro switch replacement](/guides/ball-screw-actuator-home-position-micro-switch-replacement/)
- [bottling machine end of stroke micro switch](/guides/bottling-machine-end-of-stroke-micro-switch/)
- [automated guided vehicle home position micro switch location](/guides/automated-guided-vehicle-home-position-micro-switch-location/)
- [accelerator pedal position stop micro switch operating force](/guides/accelerator-pedal-position-stop-micro-switch-operating-force/)

## Interpret unexpected readings without overdiagnosing

If neither COM-to-NO nor COM-to-NC appears to change state, first check whether the probes make reliable contact and whether the actuator is moving through its operating travel. Then confirm that the component is actually an SPDT design and that the terminals were identified from its marking or schematic. A different contact arrangement should not be judged against the SPDT table.

Readings can also be affected by wiring still connected to the switch. Other paths in the circuit may influence a continuity measurement, so a result that contradicts the expected states does not, by itself, prove that the switch has failed. Isolate connected wiring as required by the applicable procedure before concluding that the observed state belongs to the switch alone. If safe isolation or reliable terminal identification is not possible, leave the result unresolved.

Finally, keep the conclusion limited to what was tested. A de-energized continuity check can document whether the identified contact pairs change state as the actuator moves. It does not diagnose the motor, wiring, or control system, and it does not show how the window responds. To connect a verified switch state to stopping behavior, use the connection diagram and documented circuit function for the exact equipment. The **power window limit micro switch NO and NC terminals** describe contact relationships; the circuit determines what those relationships do in operation.

## Sources and references

- Defense Logistics Agency ASSIST: [MIL-PRF-8805K: Switches and Switch Assemblies, Sensitive, Snap Action, General Specification For](https://quicksearch.dla.mil/qsDocDetails.aspx?ident_number=7196){: rel="nofollow noopener noreferrer" }
- Occupational Safety and Health Administration: [29 CFR 1910.333: Selection and Use of Work Practices](https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.333){: rel="nofollow noopener noreferrer" }
- Wikipedia: [Miniature snap-action switch](https://en.wikipedia.org/wiki/Miniature_snap-action_switch){: rel="nofollow noopener noreferrer" }
