---
title: "adjustable desk open position micro switch NO and NC terminals: How to Interpret Contact States"
description: "adjustable desk open position micro switch NO and NC terminals: Understand the operating idea, essential terminology, practical checks, limitations, and."
date: 2026-10-05 09:00:00 +0800
category: Applications
tags:
  - adjustable desk open position micro switch NO and NC terminals
  - micro switches
  - Applications
author: editorial_team
---

An adjustable desk’s open-position signal is determined by the desk’s mechanism and circuit, not by a micro switch terminal label alone. The adjustable desk open position micro switch NO and NC terminals identify contact paths; they do not, by themselves, say which desk position the controller will report. To interpret the signal, distinguish the switch actuator’s released or actuated state from the desk’s position state, then verify which contacts change and how the circuit uses them.

## What “open position” means in an adjustable desk circuit

“Open position” is a state defined by the desk’s mechanism or controller. The phrase does not specify the micro switch’s actuator position or whether a particular contact is open or closed. A switch may change state when the desk mechanism reaches a point associated with an open-position signal, but the relationship depends on where the switch is placed and how the mechanism actuates it.

Keep three observations separate: the desk mechanism’s position, the actuator’s position, and the contact state. The actuator is the part moved by an external mechanism. Whether it is released or actuated describes the switch’s mechanical condition. The contact state describes the electrical connection between terminals under that condition. The controller’s interpretation is another step: it depends on which contact path is connected to the relevant input and how the circuit is designed.

Consequently, seeing a switch near a desk mechanism, or seeing its actuator move, does not establish that the desk has reached a controller-defined open position. Nor does the word “open” in a position description mean that the switch’s contacts are electrically open. Switch placement, linkage, and circuit mapping determine what state change corresponds to the desk’s open-position signal. Confirm those relationships from the exact switch and equipment information rather than inferring them from location or terminology.

## adjustable desk open position micro switch NO and NC terminals: read the contact states

For a typical changeover micro switch, COM means common terminal, NC means normally closed terminal, and NO means normally open terminal. These terms describe contact relationships at the specified reference condition, not a promise about what the desk controller will report. In generic changeover terminology, the reference condition is the actuator released: COM-NC is closed, while COM-NO is open.

When the actuator is pressed on a typical changeover switch, the contact state reverses: COM-NC opens and COM-NO closes. This describes the switch’s contact behavior, not the desk’s position logic. A desk circuit may use either the NO or NC path, depending on its design. The controller’s interpretation therefore cannot be read from NO or NC alone.

For example, an observed closed COM-NO path with the actuator actuated establishes that contact relationship at that switch state. It does not establish, by itself, whether the controller treats that path as an open-position signal. That conclusion requires knowing which terminals the circuit uses and how the relevant input is interpreted. Likewise, an open COM-NC path does not prove that the desk is in a particular position.

Treat “typical changeover” as a limit on this explanation, not as confirmation of every device’s configuration. Check the exact switch marking or schematic before assigning terminal identities or expected states. If markings or documentation do not confirm a changeover arrangement, do not assume it. The equipment connection diagram and documented circuit function control; physical terminal layout alone is not enough to identify a connection or its role.

## Verify which terminals change state

Before inspecting or measuring, isolate power to the desk and prevent unintended movement. Do not test live terminals or move the desk while inspecting the switch. If the applicable deenergization requirements cannot be met, or the terminal identification is uncertain, stop and have the work handled by someone qualified. This check concerns the isolated switch; it is not a test of the complete desk circuit.

With power isolated, identify COM, NO, and NC from the exact switch marking or schematic. Do not guess from their physical positions. Set a continuity meter to the appropriate continuity measurement, then check COM-NO and COM-NC with the actuator released. Record each result. Repeat both checks with the actuator actuated, using only a safe means of changing its position and without moving the desk during inspection.

For a documented typical changeover switch, the expected pattern is COM-NC closed and COM-NO open with the actuator released, followed by COM-NC open and COM-NO closed when it is actuated. Compare the actual readings in both states with the switch documentation. If the device’s documented arrangement differs or does not establish this behavior, use that documentation rather than treating the typical pattern as a specification for that device.

A single reading is not enough to show which contact path changes between states. Record the released and actuated results together, and note the condition under which each was measured. A continuity result identifies a contact relationship for the isolated switch in that tested state. It does not establish the circuit’s wiring, controller interpretation, or the behavior of the desk when powered. If the result is unclear, do not bridge terminals or apply power as an improvised test.

## Interpret the result as an open-position signal

Once terminal identity and state changes are established, the next question is which path the desk circuit uses for its open-position input. Where it is accessible and safe to inspect, trace the connection against the equipment wiring information. Alternatively, consult the diagram and circuit function documented for the exact desk and switch. A generic terminal arrangement cannot substitute for that information.

Either NO or NC may be used according to the circuit’s design. The switch terminal name describes a contact state relative to COM when the actuator is released; it does not name a desk position or specify the controller’s logic polarity. Do not infer that a particular terminal must mean “open,” or that a given contact state necessarily makes the controller report that position. Those relationships remain unresolved until the circuit mapping is confirmed.

If the isolated switch changes contact state as documented but the desk reports the open-position state incorrectly, the switch reading alone does not identify the cause. Wiring, mechanical alignment or actuation, and controller interpretation are separate possibilities to check against the equipment information. A continuity check cannot establish which of them is responsible, and it cannot prove the complete assembly is working or faulty. Keep the diagnosis limited to what was observed and verified.

### Related guides

- [ball screw actuator home position micro switch replacement](/guides/ball-screw-actuator-home-position-micro-switch-replacement/)
- [bottling machine end of stroke micro switch](/guides/bottling-machine-end-of-stroke-micro-switch/)
- [automated guided vehicle home position micro switch location](/guides/automated-guided-vehicle-home-position-micro-switch-location/)
- [accelerator pedal position stop micro switch operating force](/guides/accelerator-pedal-position-stop-micro-switch-operating-force/)

## How this differs from a closed-position signal

The same contact-state distinctions apply when a micro switch is associated with a closed-position signal: NO and NC describe contact relationships, not the position reported by the desk. The reported position depends on switch placement, the point at which the mechanism actuates it, and the circuit mapping. Do not treat a closed-position input as a separate meaning inherent in either terminal label. For this question, focus verification on the specific open-position input and consult its circuit information before drawing a conclusion.

This concludes the explanation of adjustable desk open position micro switch NO and NC terminals.

## Sources and references

- Defense Logistics Agency ASSIST: [MIL-PRF-8805K: Switches and Switch Assemblies, Sensitive, Snap Action, General Specification For](https://quicksearch.dla.mil/qsDocDetails.aspx?ident_number=7196){: rel="nofollow noopener noreferrer" }
- Occupational Safety and Health Administration: [29 CFR 1910.333: Selection and Use of Work Practices](https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.333){: rel="nofollow noopener noreferrer" }
- Wikipedia: [Miniature snap-action switch](https://en.wikipedia.org/wiki/Miniature_snap-action_switch){: rel="nofollow noopener noreferrer" }
