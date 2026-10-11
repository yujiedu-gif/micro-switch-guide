---
title: "Micro Switch COM: What the Common Terminal Means"
description: "Learn what micro switch com means, how the common terminal relates to switch contacts, and what to verify before identifying terminals in your device."
date: 2026-10-11 09:00:00 +0800
category: Basics
tags:
  - micro switch com
  - micro switches
  - Basics
author: editorial_team
---

# What COM Means on a Micro Switch

The term **micro switch com** usually refers to the common terminal of a changeover switch. COM identifies a contact’s role in the switch’s contact arrangement; it does not, by itself, identify a power input or prescribe how the switch should be wired. To identify that terminal without guessing, use the switch’s terminal markings and the connection diagram documented for the exact switch and equipment. Do not rely on where a terminal sits on the body.

The labels COM, NO, and NC are useful when a switch provides a changeover contact arrangement, but their meaning should be read in context. The terminals’ physical layout and markings can vary. A continuity check may help confirm a documented contact relationship, but it is not a substitute for the diagram, equipment service procedure, or applicable requirements. Any such check should be performed only with the relevant equipment disconnected from power and in accordance with its service procedure.

## What does micro switch com mean?

In a changeover switch, **COM** means the common terminal. It is the shared contact that changes its connection between the normally closed (NC) and normally open (NO) contacts as the switch changes state. This describes a contact role, not a universal location on the switch and not an instruction to connect a particular supply or load to it.

The word “common” can be misleading if read as a wiring direction. It does not establish that COM must be connected to a power source, nor does the label alone say what load the switch can control. The documented circuit function and permissible load for the exact switch and equipment determine what the terminals do in a particular application. A general terminal label cannot establish those details.

The changeover definition applies when the device actually provides both NO and NC contacts around a common contact. Not every switch has that arrangement. A device may have a different contact configuration, and a generic description cannot establish which configuration a particular switch uses. Check its terminal markings and documentation before interpreting COM, NO, or NC.

Also keep terminal identity separate from actuator behavior. A basic sensitive micro switch uses snap action, with moving-contact speed relatively independent of actuating-mechanism speed, in the terminology of MIL-PRF-8805K. That operating principle does not identify COM, reveal a terminal layout, or establish a specific switch’s ratings. Contact labels and the documented diagram remain the relevant references for identifying terminals.

## How COM relates to NO and NC

The labels NO and NC describe contact relationships relative to the switch’s **unactuated state**. For a changeover configuration, COM is connected to NC in the unactuated state, while NO is open. When the actuator changes the switch to its actuated state, COM transfers its connection to NO, and the COM-to-NC path opens. These descriptions concern electrical contact state, not the terminals’ physical positions.

“Normally” refers to the unactuated state used to describe the contact arrangement. It does not mean a terminal is normally located on one side of the body, nor does it identify how a switch is installed in equipment. The state descriptions should be applied only when the documented switch configuration supports this COM-NO-NC relationship. They should not be extended to a switch that does not provide both NO and NC contacts.

A useful way to read a documented changeover diagram is to follow the contact paths in each shown state. Find the terminal labeled COM, then note which contact the diagram shows connected to it in the unactuated state and which contact it shows connected after actuation. This lets you interpret the symbols without inferring terminal functions from a drawing’s apparent orientation or from a physical arrangement that may differ between devices.

The diagram and markings need to be specific to the switch and equipment in question. A generic symbol can explain the usual terminology, but it cannot establish the contact arrangement, ratings, or permissible load of an exact device. If the equipment documentation uses different notation or shows a different contact configuration, use that documentation rather than assuming the generic changeover relationship applies.

## How to identify COM without guessing

Start with the markings on the switch and the connection diagram or other documentation for the exact switch and equipment. The applicable diagram, terminal marking, circuit function, and permissible load are the references for identifying and interpreting terminals. Physical position alone is not reliable: do not identify COM from whether a terminal is above, below, beside, or between other terminals. Shape or resemblance to another switch is not proof either.

If the switch has clear COM, NO, and NC markings, compare them with its documented connection diagram. Confirm that the diagram applies to the device and equipment being examined. A terminal that appears to occupy a familiar position on another switch may serve a different role here. Likewise, a label should be interpreted with the documented contact arrangement, not as a complete wiring instruction.

A continuity check can be used as a way to examine a documented contact relationship when such a check is appropriate. In a changeover arrangement, the expected relationship is continuity between COM and NC in the unactuated state, with the COM-to-NO path open; in the actuated state, that relationship transfers to COM and NO. This description is limited to that changeover configuration. It does not provide a device-specific test procedure or establish that a particular switch is functioning correctly.

Perform continuity checks only with the relevant equipment disconnected from power, and follow its service procedure and applicable deenergization and qualification requirements. Do not treat a conceptual contact-state description as instructions for accessing or testing a particular appliance or circuit. If the markings or documentation do not establish the terminal roles, do not resolve the uncertainty by guessing from layout; the documented information for the exact switch and equipment is needed.

Keep the identification question separate from wiring and selection decisions. Knowing that COM is the common contact in a documented changeover switch does not determine how that switch should be connected in a specific circuit, whether it is suitable for a load, or whether it can replace another device. Those matters require the exact equipment documentation and applicable ratings. The central answer remains straightforward: COM names the common contact where a changeover arrangement applies, and its identity should be established from the exact device’s markings and documentation, not its physical position.

### Related guides

- [what is a micro switch actuator](/guides/what-is-a-micro-switch-actuator/)
- [how long do micro switches last](/guides/how-long-do-micro-switches-last/)
- [how to wire a micro switch](/guides/how-to-wire-a-micro-switch/)
- [micro switch differential travel](/guides/micro-switch-differential-travel/)

## In short

**Micro switch com** generally means the common contact in a changeover switch. In that configuration, COM is connected to NC when unactuated and transfers to NO when actuated. Identify the terminal from the exact switch’s markings and documented connection diagram, not from its location. Any continuity check must be performed only with the relevant equipment disconnected from power and in accordance with its service procedure.

## Sources and references

- Defense Logistics Agency ASSIST: [MIL-PRF-8805K: Switches and Switch Assemblies, Sensitive, Snap Action, General Specification For](https://quicksearch.dla.mil/qsDocDetails.aspx?ident_number=7196)
- Occupational Safety and Health Administration: [29 CFR 1910.333: Selection and Use of Work Practices](https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.333)
- Wikipedia: [Miniature snap-action switch](https://en.wikipedia.org/wiki/Miniature_snap-action_switch)
