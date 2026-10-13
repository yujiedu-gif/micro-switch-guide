---
title: "How micro switch changeover contacts work"
description: "micro switch changeover contacts: Understand the operating idea, essential terminology, practical checks, limitations, and evidence needed for careful."
date: 2026-10-13 09:00:00 +0800
category: Basics
tags:
  - micro switch changeover contacts
  - micro switches
  - Basics
author: editorial_team
---

A micro switch changeover contacts arrangement describes which terminal pair is connected at a stated actuator condition. It does not, by itself, say whether current is flowing or what an appliance will do. To interpret the labels, first confirm that the particular micro switch has a documented changeover contact arrangement, then compare its terminal diagram at the specified reference and operated positions.

## What micro switch changeover contacts describe

A micro switch is an electromechanical component. The term “changeover contacts” applies here only when the particular switch’s documentation identifies a changeover arrangement. It should not be assumed for every micro switch, much less for every device called a switch. The exact device marking or schematic controls; a generic terminal convention cannot override the documentation for the part in question.

In a documented changeover arrangement, COM means common. NO and NC name the other contact relationships relative to a stated reference condition. That reference matters: the labels describe contact states at a defined actuator condition, not an unconditional guarantee about current flow. A diagram should make clear which condition it uses, such as the stated unactuated reference position. If the reference is not specified or the marks are unclear, the labels alone do not resolve the ambiguity.

The useful question is therefore not simply “Which terminal is normally open?” It is “At the documented reference position, which contact path does the diagram show, and what does it show after the actuator is operated?” Keeping the answer tied to those two states prevents a contact label from being mistaken for a description of the whole circuit.

A changeover description is about the micro switch’s contact relationships. It does not establish how an external mechanism moves the actuator, what force or travel is involved, or what control logic follows the contact change. Those details require documentation for the particular switch and the surrounding equipment. The labels provide a way to read the documented contact arrangement, not a complete account of an application.

## Map COM, NO, and NC at each actuator state

Start with the reference condition named in the switch documentation or diagram. When a documented arrangement identifies COM, NO, and NC, COM is the common terminal in that arrangement. The diagram indicates whether COM is connected to NC or to NO in the stated condition. Read the drawn contact path rather than treating the words “open” and “closed” as predictions about an entire machine.

At the specified reference condition, NC identifies the contact relationship shown as closed relative to COM, and NO identifies the relationship shown as open relative to COM. These terms describe the documented contact state for that reference. They do not mean that current must be present on COM, that an external circuit is powered, or that a machine is in a particular operating mode.

Next, compare the operated condition shown by the same documentation. In a changeover arrangement, the drawing describes the contact relationship as changing between the actuator states. Where the diagram shows the alternate path, use it to identify which terminal pair is connected in that operated state. Keep the state label attached to the path: a reference-state description and an operated-state description are not interchangeable.

A simple reading table can help, provided its entries come from the actual device documentation:

| Actuator condition | What to read in the documented diagram |
| --- | --- |
| Specified reference condition | Identify COM and the contact path shown between COM and NO or NC. |
| Operated condition | Identify the contact path shown for that condition and compare it with the reference. |

This is a reading method, not a universal pinout. The generic claim that a changeover contact may use COM, NO, and NC does not establish that a particular switch has those markings, that its terminals occupy a standard physical layout, or that a particular pair is connected in every reference condition. Confirm the exact switch marking or schematic before assigning meaning to its terminals.

## What changes when the actuator operates

The actuator is the part moved by an external mechanism. In a documented changeover arrangement, changing the actuator state corresponds to a change in the contact relationship shown by the switch diagram. The diagram can be used to compare the contact path at the specified reference position with the path at the operated position. This is the central meaning of “changeover” in this context: the documented relationship between terminal paths differs across actuator states.

That description does not justify adding a precise sequence or timing. Without evidence for a particular switch, do not infer when during actuator motion the contact changes, whether the change is instantaneous, or what happens between the stated positions. Nor does the word “operated” supply a universal mechanical threshold. The applicable positions and any movement details must come from the exact switch documentation.

It is also important to keep actuator movement separate from circuit function. The external mechanism may move the actuator, and the micro switch may change its documented contact path, but those facts alone do not determine what the host equipment does. A connected circuit could use either path as part of its design; the labels do not identify which one is used, what signal or load is present, or whether the equipment starts, stops, or changes state.

Thus, when reading a contact diagram, follow the same sequence each time: identify the stated actuator condition, locate COM if the arrangement documents it, and read the indicated contact path for that condition. Then compare that path with the other documented condition. This preserves the mechanical reference and the electrical relationship without assuming an unprovided operating point, release point, or equipment response.

### Related guides

- [micro switch flyback diode causes](/guides/micro-switch-flyback-diode-causes/)
- [panel mount plunger micro switch working principle](/guides/panel-mount-plunger-micro-switch-working-principle/)
- [cam follower micro switch adjustment](/guides/cam-follower-micro-switch-adjustment/)
- [micro switch SPST NC contacts explained](/guides/micro-switch-spst-nc-contacts-explained/)

## What contact labels do not tell you about a circuit

The switch diagram establishes only what its symbols and labels document about the contact arrangement under the stated conditions. It can help identify a terminal relationship at the reference position and how that relationship differs at the operated position. It cannot, by itself, show whether the installed circuit is energized, whether current is flowing, or what effect a contact change has on the host equipment.

Those outcomes depend on how the switch is wired and on the surrounding circuit design. A contact change may be incorporated into different control arrangements, so the NO or NC label alone does not reveal the system’s normal behavior, intended action, or response to actuation. Do not infer a machine function merely from a terminal name or from the presence of a micro switch.

Likewise, a generic changeover description cannot establish that a particular device is suitable for an application, correctly installed, or compatible with a circuit. The terminal marking or schematic controls the interpretation of that device’s contacts. The wiring diagram and system documentation are needed to understand the installed circuit’s intended behavior; the component contact diagram alone does not provide that answer.

In short, read micro switch changeover contacts as state-specific contact relationships: use the documented reference condition to interpret NO and NC relative to COM, then compare the documented operated condition. Treat the resulting circuit behavior as a separate question, determined by wiring and the host system rather than by the contact labels alone.

## Sources and references

- Defense Logistics Agency ASSIST: [MIL-PRF-8805K: Switches and Switch Assemblies, Sensitive, Snap Action, General Specification For](https://quicksearch.dla.mil/qsDocDetails.aspx?ident_number=7196){: rel="nofollow noopener noreferrer" }
- Wikipedia: [Miniature snap-action switch](https://en.wikipedia.org/wiki/Miniature_snap-action_switch){: rel="nofollow noopener noreferrer" }
