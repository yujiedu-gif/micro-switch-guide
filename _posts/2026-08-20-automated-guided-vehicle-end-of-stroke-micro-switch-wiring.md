---
title: "Automated guided vehicle end of stroke micro switch wiring"
description: "automated guided vehicle end of stroke micro switch wiring: Understand the operating idea, essential terminology, practical checks, limitations, and."
date: 2026-08-20 09:00:00 +0800
category: Applications
tags:
  - automated guided vehicle end of stroke micro switch wiring
  - micro switches
  - Applications
author: editorial_team
---

# End-of-stroke switch contacts and vehicle input behavior

An **automated guided vehicle end of stroke micro switch wiring** question has two parts: which switch contacts change state, and how those contacts connect to the vehicle’s designated input. The switch’s mechanical action can be checked at its terminals, but that check alone does not establish what the controller will do with the input. The actual connection and interpretation must come from the switch documentation and the vehicle’s circuit diagram.

This reference explains how to identify common, normally open, and normally closed contacts; trace their relationship to a vehicle input without assuming a universal pinout or electrical arrangement; and distinguish an isolated contact check from powered system validation. It does not establish a particular vehicle circuit or safety strategy.

## What the end-of-stroke micro switch reports

A micro switch changes its contact state when its actuator reaches the switch’s operating point. In an end-of-stroke arrangement, the switch can provide a signal associated with a mechanism reaching a position. That describes the switch’s mechanical response, not the meaning assigned to the signal by a vehicle controller.

The controller may interpret an input as travel complete, a limit reached, or another condition, depending on the circuit and control logic. Therefore, avoid treating actuator position, terminal continuity, and controller interpretation as interchangeable facts. They are related steps in a signal path, but each requires its own verification.

Travel terminology can also matter when checking the mechanical action. Pretravel runs from the free position to the operating position; overtravel runs from the operating position to the extreme permitted actuator position. These terms describe actuator travel, not terminal identity or the vehicle’s programmed response.

A single end-of-stroke switch does not establish the vehicle’s complete safety strategy. Its role and effect must be determined from the actual vehicle documentation rather than inferred from the switch’s presence or the contact labels alone.

## Automated guided vehicle end of stroke micro switch wiring: identify contacts and states

Start with the markings and schematic for the actual switch. In general changeover terminology, **COM** means common terminal, **NO** means normally open terminal, and **NC** means normally closed terminal. Confirm that these terms match the device’s own documentation before using them to identify connections. Do not infer terminal positions from a generic drawing, physical layout, or wire color.

“Normally open” and “normally closed” refer to contact state with the actuator unoperated, unless the supplied documentation defines another reference condition. In that unoperated state, a normally open contact is open and a normally closed contact is closed. When the actuator operates, the contact arrangement changes. For a changeover contact set, the connection transfers between the common terminal and the normally open or normally closed contact.

This describes the switch contacts, not a controller state. A vehicle input labeled or configured as active may not correspond directly to the actuator being operated: the circuit design and controller logic determine how the electrical input is interpreted. Keep the reference condition explicit when recording a check, for example, whether the actuator was unoperated or operated. Then compare the observed contact state with the switch schematic.

Do not assign a terminal number, connector pin, wire color, or contact arrangement from generic terminology. The terms identify contact functions, while their physical locations and any device-specific details must be verified on the actual switch and its documentation.

## Map the switch contacts to the vehicle input

Trace the circuit from the switch toward the designated vehicle input using the vehicle’s circuit diagram. Conceptually, a circuit source or input reference connects through a selected switch contact to the specified input. The diagram must establish which contact is used, where the circuit begins and returns, and which vehicle input receives the signal. This is a tracing method, not a universal wiring layout.

A design may use normally open or normally closed behavior, but the contact choice alone does not define the controller’s logic. The controller may be configured to interpret the input according to the particular circuit design. Confirm the intended unoperated and operated behavior in vehicle documentation rather than assuming that an open contact means “inactive,” or that a closed contact means “active.”

Keep electrical details unresolved until verified. Do not infer supply voltage, polarity, input type, protection, wire sizing, terminal numbers, or pinout from the switch contact names. Use the vehicle diagram and applicable switch documentation for those details. If the diagram and device markings do not agree or do not identify the connection clearly, the circuit cannot be established from generic contact terminology alone.

The useful result of tracing is a documented path: the common contact, the selected normally open or normally closed contact, and the designated vehicle input, interpreted under the conditions specified by the vehicle documentation. That path helps separate the switch’s physical state from the input signal and from the controller’s response.

## Verify wiring and switch action safely

Begin with power isolated. Follow the vehicle’s lockout and service procedure before making a continuity check. With the circuit in the state required by that procedure, identify the switch terminals from its documentation and check the relevant contact with the actuator unoperated. Operate the actuator as permitted by the service procedure and check again. Compare both observations with the switch schematic and the vehicle circuit drawing.

A continuity result answers a limited question: whether the checked contacts are open or closed in the tested mechanical state. It does not, by itself, confirm that the conductors reach the intended vehicle input, that the input is configured as expected, or that the controller produces the intended response. Record the actuator condition and the contact pair tested so the result has a clear reference.

Powered input validation is a separate step. Restore power and check input behavior only through the vehicle’s approved safe test procedure. Use the documented procedure to establish what to observe and how to perform the test; do not assume a voltage, test point, or controller indication. Never bypass a safety-related limit function to force a response or make a test easier.

Keep the two verification results distinct: an isolated contact check verifies switch contact behavior under the test conditions, while approved powered validation checks the vehicle input behavior. Neither should be presented as proof of the other. The actual wiring, permitted test method, and significance of an input depend on the circuit design and vehicle documentation.

### Related guides

- [ball screw actuator home position micro switch replacement](/guides/ball-screw-actuator-home-position-micro-switch-replacement/)
- [bottling machine end of stroke micro switch](/guides/bottling-machine-end-of-stroke-micro-switch/)
- [automated guided vehicle home position micro switch location](/guides/automated-guided-vehicle-home-position-micro-switch-location/)
- [accelerator pedal position stop micro switch operating force](/guides/accelerator-pedal-position-stop-micro-switch-operating-force/)

## Common wiring interpretation errors

One common error is confusing contact labels with either actuator position or controller state. COM, NO, and NC identify terminal functions in general changeover terminology. Normally open and normally closed describe the contact state at the unoperated actuator position unless the device documentation specifies another reference. Neither label, on its own, says how the controller interprets the input.

Another error is treating a continuity result as proof that the complete vehicle input path works. A contact can show the expected isolated state while the connection to the designated input, the input configuration, or the controller’s interpretation remains unverified. Use the circuit drawing and approved powered validation to examine those separate parts.

A further error is assuming that end-of-stroke wiring is the same across vehicle designs. Contact selection and input mapping are specific to the actual circuit. A generic description cannot supply a pinout, voltage, polarity, or programmed response.

For an **automated guided vehicle end of stroke micro switch wiring** check, establish the switch’s documented contact functions, trace the chosen contact to the designated input on the vehicle diagram, and keep passive contact testing separate from approved powered validation. This supports a bounded conclusion about the verified switch and circuit; it does not establish a universal vehicle arrangement or complete safety strategy.

## Sources and references

- Defense Logistics Agency ASSIST: [MIL-PRF-8805K: Switches and Switch Assemblies, Sensitive, Snap Action, General Specification For](https://quicksearch.dla.mil/qsDocDetails.aspx?ident_number=7196){: rel="nofollow noopener noreferrer" }
- Wikipedia: [Miniature snap-action switch](https://en.wikipedia.org/wiki/Miniature_snap-action_switch){: rel="nofollow noopener noreferrer" }
