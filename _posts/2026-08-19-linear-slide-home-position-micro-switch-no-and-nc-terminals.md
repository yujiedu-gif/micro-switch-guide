---
title: "linear slide home position micro switch NO and NC terminals"
description: "linear slide home position micro switch NO and NC terminals: Understand the operating idea, essential terminology, practical checks, limitations, and."
date: 2026-08-19 09:00:00 +0800
category: Applications
tags:
  - linear slide home position micro switch NO and NC terminals
  - micro switches
  - Applications
author: editorial_team
---

# Reading NO and NC terminals for a slide home signal

A **linear slide home position micro switch NO and NC terminals** can provide an electrical indication of slide position, but neither terminal means “home” by itself. The meaning depends on the switch’s unactuated state, how the slide moves its actuator, and how the circuit uses the contact. Separate the switch’s electrical condition from the slide’s mechanical location, then verify the installed behavior against the exact switch and equipment documentation.

The checks below explain the contact states, trace how slide movement can change them, and give a bounded method for verifying the transfer. Follow applicable deenergization and qualification requirements. Use the documented wiring diagram, terminal markings, circuit function, and permissible load for the exact switch and equipment; a generic terminal layout is not enough to establish applicability.

## What NO and NC mean on a linear slide home position micro switch NO and NC terminals

NO and NC describe contact conditions relative to the switch’s **unactuated** state. In generic changeover terminology, **COM** means common, **NC** means normally closed, and **NO** means normally open. “Normally” here refers to the switch mechanism before it is operated, not to a standard location of the slide. Thus, NO does not inherently mean that the slide is away from home, and NC does not inherently mean that it is at home.

A generic changeover contact has a common terminal and two possible contact paths, one associated with NC and one with NO. In the unactuated condition, the terminal labels identify the normally closed and normally open paths. When the actuator is operated, the contact arrangement changes. The exact device marking or schematic controls: confirm that the switch is a changeover type and identify its terminals from its own documentation rather than relying on a familiar-looking physical layout.

Keep two references distinct when interpreting the signal:

- **Unactuated switch state:** the contact condition used to define NO and NC.
- **Slide home position:** a mechanical location established by the slide, its adjustment, and the point at which it operates the switch.

Those references may coincide in an installation, but the terminal labels alone do not establish that they do. A slide could actuate the switch at its home position, or the switch might be actuated at another point in its travel. The circuit diagram and installed arrangement determine which contact state is used to report home.

## How slide movement changes the home switch signal

Start with the actuator released and identify the corresponding contact state from the switch diagram. As the slide moves, it may contact and operate the actuator at an installed trip point. Once operated, the changeover contact changes its connection between the common terminal and the NO and NC paths. As the slide moves away and releases the actuator, the contacts can return to the unoperated condition.

This sequence explains why a home signal must be interpreted through motion, not inferred from NO or NC alone. The relevant question is not simply “Which terminal is NO?” It is: “At the slide’s intended home position, is the switch actuator released or operated, and which documented contact path does the circuit use in that state?” The answer depends on the switch’s mounting and adjustment, the direction in which the slide reaches the actuator, and the circuit’s chosen logic.

For example, if the slide operates the switch as it reaches its intended home location, the contact state at that location is the operated state. If the slide instead releases the actuator at home, the home indication corresponds to the unactuated state. These are conditional interpretations, not universal wiring rules. Establish the actual sequence by observing the slide and actuator together and comparing the resulting states with the equipment diagram.

A contact change can indicate that the actuator has reached its trip point; it does not, by itself, prove that the slide is at the intended mechanical home position. The trip point must correspond to that position in the installed mechanism. If the point is displaced, a genuine change in contact state could still report a location other than the required home position.

## Verify NO and NC continuity with power isolated

Use the exact switch documentation to identify COM, NO, and NC before checking the wiring. Follow applicable deenergization and qualification requirements, and isolate circuit power before using resistance or continuity mode. Do not infer safety from the terminal names or from the fact that the slide is stationary.

A bounded check is:

1. With power isolated, identify the switch terminals from its marking or schematic and compare them with the equipment wiring diagram.
2. Observe and record the slide position and whether the switch actuator is released or operated. Begin with the actuator released if the mechanism permits it.
3. Check continuity from COM to NC and from COM to NO in the released condition.
4. Move the slide so that it operates the actuator, observing the movement and the point at which the switch changes state. Repeat the COM-to-NC and COM-to-NO checks in the operated condition.
5. Compare the observed transfer and trip point with the documented circuit function and the required mechanical home position. If the readings or movement conflict with the documentation, stop and resolve the discrepancy rather than assigning a home meaning by assumption.

This sequence checks the contact behavior in both actuator states and connects that behavior to an observed slide position. It does not establish a universal expected reading for every device: the exact switch schematic and installed wiring control. Nor does a continuity result alone establish that the circuit uses the contact as a home signal. Compare the wiring diagram, terminal identification, circuit function, and permissible load documented for the exact switch and equipment.

### Related guides

- [ball screw actuator home position micro switch replacement](/guides/ball-screw-actuator-home-position-micro-switch-replacement/)
- [bottling machine end of stroke micro switch](/guides/bottling-machine-end-of-stroke-micro-switch/)
- [automated guided vehicle home position micro switch location](/guides/automated-guided-vehicle-home-position-micro-switch-location/)
- [accelerator pedal position stop micro switch operating force](/guides/accelerator-pedal-position-stop-micro-switch-operating-force/)

## When the electrical state does not match slide home

If the observed state does not match the expected home indication, first compare the slide’s movement with the switch’s actuation path. Check whether the slide reaches the actuator in the intended direction and at the intended point. A switch can transfer correctly while its trip point is not aligned with the required mechanical home location, so a contact change alone does not settle the position question.

Next, check terminal identification and wiring against the applicable circuit diagram. A mismatch between the observed COM-to-NO or COM-to-NC state and the expected indication may reflect how the circuit is connected or which actuator state the design uses. Do not treat the names NO and NC as a complete description of circuit logic, and do not change connections based on a generic diagram.

Finally, distinguish among an incorrectly placed trip point, wiring that does not match the diagram, and a switch that does not transfer between contact paths as expected. Compare the released and operated observations with the exact device schematic and equipment documentation. The purpose is to identify which part of the relationship is uncertain, not to assume the slide itself is at fault.

In short, **linear slide home position micro switch NO and NC terminals** indicate the switch’s contact paths relative to its unactuated condition. To interpret them as a home signal, establish whether the slide operates or releases the actuator at home, verify the observed contact transfer with power isolated, and confirm that the trip point and wiring agree with the exact equipment documentation.

## Sources and references

- Defense Logistics Agency ASSIST: [MIL-PRF-8805K: Switches and Switch Assemblies, Sensitive, Snap Action, General Specification For](https://quicksearch.dla.mil/qsDocDetails.aspx?ident_number=7196){: rel="nofollow noopener noreferrer" }
- Occupational Safety and Health Administration: [29 CFR 1910.333: Selection and Use of Work Practices](https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.333){: rel="nofollow noopener noreferrer" }
- Wikipedia: [Miniature snap-action switch](https://en.wikipedia.org/wiki/Miniature_snap-action_switch){: rel="nofollow noopener noreferrer" }
