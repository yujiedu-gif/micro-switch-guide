---
title: "Assembly robot travel limit micro switch NO and NC terminals: how contact states work"
description: "assembly robot travel limit micro switch NO and NC terminals: Understand the operating idea, essential terminology, practical checks, limitations, and."
date: 2026-07-24 09:00:00 +0800
category: Applications
tags:
  - assembly robot travel limit micro switch NO and NC terminals
  - micro switches
  - Applications
author: editorial_team
---

# Understanding NO and NC Contacts at a Robot Travel Limit

An **assembly robot travel limit micro switch NO and NC terminals** can indicate a mechanical position through changes in electrical contact state. To interpret that indication correctly, distinguish what the switch contacts do from what a robot controller makes of the resulting input. The terminal labels describe contact relationships in a defined switch state; they do not, by themselves, identify a robot motion command or establish what the controller considers a limit.

The exact switch markings, schematic, and applicable specification sheet govern terminal identity and switching behavior. A general description can explain the contact states, but it cannot establish the ratings, wiring, controller logic, or suitability of a particular switch for a particular machine. The guidance below focuses on interpreting and checking contact states, not designing or validating a robot safeguarding function.

## What NO and NC mean on an assembly robot travel limit micro switch NO and NC terminals

COM, NO, and NC are contact-terminal labels. In general changeover terminology, COM means common, NO means normally open, and NC means normally closed. “Normally” refers to the switch’s unactuated state, not to the robot’s normal operating mode or the controller’s preferred input state. The precise device marking or schematic takes precedence over a generic description.

For a generic changeover contact, the unactuated state is described by COM-to-NC continuity, with COM-to-NO open. When the switch mechanism is operated, the usual changeover behavior is for COM-to-NO to close and COM-to-NC to open. That description is conditional: the applicable switch specification and exact device schematic determine whether it matches a given component and how its terminals are marked.

These labels do not describe robot movement. NO does not mean “robot may move,” and NC does not mean “robot must stop.” They identify contact relationships in the switch’s reference state. Whether operating the switch signals that a travel limit has been reached depends on how the contacts connect to the machine circuit and how the controller interprets its input.

A travel-limit mechanism may operate the switch as a robot reaches a position, but the contact description alone does not establish the exact mechanical arrangement or allowable travel. Numerical travel limits are requirements of the applicable specification sheet; they must not be inferred from the component category. Check the documentation for the exact switch and equipment rather than treating a generic contact explanation as a device specification.

## How switch actuation changes a travel-limit signal

The electrical sequence has two distinct parts. First, mechanical operation changes the switch contact state, subject to the device’s documentation. Second, the connected circuit presents an input condition that a controller may interpret. The contact labels explain the first part. They do not specify the second.

For example, if the machine circuit uses COM and NO, a change from the unactuated state to the operated state may change the circuit from open to closed. If it uses COM and NC, the corresponding change may be from closed to open. This is a description of generic changeover behavior, not a wiring prescription. The exact switch schematic, circuit function, and permissible load must be confirmed for the switch and equipment involved.

A controller can interpret an input according to its own input arrangement and configured logic. Without the relevant controller and machine documentation, it is not possible to say whether an open or closed circuit represents a reached limit, an ordinary position, or another input condition. Do not infer input polarity, a stop command, or a control response from the NO or NC label alone.

This distinction matters when reading a drawing or diagnosing a signal. Ask separately: what contact state does the switch produce when unactuated or operated, and what does the documented controller circuit make of that state? The answer to the first question comes from the switch’s marking, schematic, and specification. The answer to the second comes from the machine’s electrical drawings and control documentation. Keeping those questions separate prevents a contact label from being mistaken for a complete description of robot behavior.

## Check the micro switch terminals before interpreting the limit circuit

Before checking continuity, isolate the switch from energized circuitry and follow applicable deenergization and qualification requirements. Continuity observations made in a connected circuit may not represent the switch alone. Testing should be limited to identifying and checking the contacts; it does not establish that the machine’s limit function or any safety function is validated.

With the switch isolated, use a meter to compare COM-to-NO and COM-to-NC continuity in both the unactuated and operated states. Record which pairs show continuity in each state, then compare the observations with the exact switch markings and schematic. The generic changeover pattern is COM-to-NC closed and COM-to-NO open when unactuated, with those relationships changing when operated. The device specification controls if its documented behavior differs.

Do not identify terminals from physical position or wire color alone. Use the connection diagram, terminal marking, circuit function, and permissible load documented for the exact switch and equipment. These are the relevant checks when interpreting wiring; a generic physical-layout inference cannot establish which terminal is COM, NO, or NC on a particular device.

If continuity does not match the expected documented states, stop treating the generic description as sufficient. Recheck that the device is isolated, that the actuator state is understood, and that the correct schematic applies. The available evidence does not establish a cause for a mismatch. Resolve terminal identity and switching behavior from the exact switch documentation and, where needed, qualified review before connecting it to a robot input.

## How NO and NC wiring affect fault interpretation

An open or shorted wire can affect a circuit using NO differently from one using NC because the two contact paths have different states when the switch is unactuated and when it is operated. The resulting input condition also depends on the circuit and controller logic. Therefore, a wire fault cannot be assigned one universal meaning based only on the contact label.

In a generic NO arrangement, the selected contact path is open in the unactuated state and closes when the mechanism operates. A break in that path may leave it open, but what the controller then indicates is not established by the contact state alone. A short may create an electrical condition different from the intended open state, but its interpretation likewise depends on the documented circuit and input logic.

In a generic NC arrangement, the selected path is closed in the unactuated state and opens when the mechanism operates. A break can interrupt a path that would otherwise be closed, while a short can alter the intended switching behavior. These observations describe possible electrical differences, not guaranteed fault detection or a defined machine response. The machine drawings and controller documentation determine how such conditions are handled.

Neither arrangement should be called universally fail-safe on this basis. That conclusion would require information about controller logic, circuit design, and the required safety architecture, none of which can be inferred from COM, NO, and NC labels. Use machine-specific electrical drawings and qualified review for changes, and do not substitute a generic contact-state explanation for an assessment of fault response.

### Related guides

- [ball screw actuator home position micro switch replacement](/guides/ball-screw-actuator-home-position-micro-switch-replacement/)
- [bottling machine end of stroke micro switch](/guides/bottling-machine-end-of-stroke-micro-switch/)
- [automated guided vehicle home position micro switch location](/guides/automated-guided-vehicle-home-position-micro-switch-location/)
- [accelerator pedal position stop micro switch operating force](/guides/accelerator-pedal-position-stop-micro-switch-operating-force/)

## Limits of a micro switch travel-limit explanation

A travel-limit contact is not, by itself, proof of a validated safety function or safe stopping performance. Contact-state guidance explains how a generic changeover contact may behave; it does not establish the switch’s ratings, the robot’s stopping response, the suitability of a circuit, or the integrity of a safeguarding design. Those matters require the applicable equipment documentation and appropriate qualified review.

Do not bypass, adjust, or rewire a robot limit circuit based solely on terminal-state guidance. For installation, circuit interpretation, or safeguarding questions, consult the machine-specific electrical documentation and qualified personnel. Any change must be assessed in the context of the exact switch and equipment, including the documented circuit function and permissible load.

In short, identify the switch’s unactuated and operated contact states from its markings and exact schematic, then interpret the resulting input using the machine documentation. The **assembly robot travel limit micro switch NO and NC terminals** describe contact relationships, not a complete robot control or safety function. This article is educational guidance, not a robot safeguarding design or wiring prescription.

## Sources and references

- Defense Logistics Agency ASSIST: [MIL-PRF-8805K: Switches and Switch Assemblies, Sensitive, Snap Action, General Specification For](https://quicksearch.dla.mil/qsDocDetails.aspx?ident_number=7196){: rel="nofollow noopener noreferrer" }
- Occupational Safety and Health Administration: [29 CFR 1910.333: Selection and Use of Work Practices](https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.333){: rel="nofollow noopener noreferrer" }
- Wikipedia: [Miniature snap-action switch](https://en.wikipedia.org/wiki/Miniature_snap-action_switch){: rel="nofollow noopener noreferrer" }
