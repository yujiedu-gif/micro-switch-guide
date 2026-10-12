---
title: "Aircraft Landing Gear Monitor Micro Switch Wiring: Circuit Logic and Checks"
description: "aircraft landing gear monitor micro switch wiring: Understand the operating idea, essential terminology, practical checks, limitations, and evidence."
date: 2026-08-23 09:00:00 +0800
category: Applications
tags:
  - aircraft landing gear monitor micro switch wiring
  - micro switches
  - Applications
author: editorial_team
---

# Aircraft landing gear monitor micro switch wiring

Aircraft landing gear monitor micro switch wiring is best understood as a documented signal path, not as a universal pinout. In a design that uses a mechanically actuated switch, the switch supplies an electrical input associated with a defined gear position. The contact state is one part of the system; the aircraft’s circuit and indication logic determine what that state means to the pilot or monitoring system.

This distinction matters because a contact labeled normally open or normally closed does not, by itself, say whether the landing gear is up or down. The exact aircraft wiring diagram, switch marking, and maintenance procedure govern interpretation and testing. Other aircraft designs may use different sensing arrangements, so the explanation below describes a general way to read documented switch logic rather than a universal aircraft circuit.

## What the aircraft landing gear monitor micro switch wiring represents

A micro switch used in a landing-gear monitoring circuit acts as a mechanically actuated electrical input in some designs. Movement associated with the landing gear can cause the switch to change contact state at a mechanically defined position. The circuit can then use that state as an input to an indication system. The precise position being sensed and the resulting indication depend on the aircraft design and its documentation.

Keep three things separate when interpreting the circuit:

1. **Mechanical position:** where the gear mechanism and switch actuator are in relation to one another.
2. **Electrical contact state:** which switch contacts are connected or open in that mechanical condition.
3. **System indication:** what the aircraft’s circuit and indication logic present to the crew or another system.

These are related, but they are not interchangeable descriptions. A particular contact state is not automatically equivalent to a displayed “gear down,” “gear up,” or other status. The documented circuit establishes how the switch input is used.

Nor should a switch-based arrangement be assumed for every aircraft. The monitoring method and its circuit architecture must be established from aircraft-specific documentation. Without that information, the sensed position, signal path, and displayed meaning remain unresolved.

## Trace contacts through the aircraft landing gear monitor micro switch wiring

A generic changeover contact may have terminals labeled **COM**, **NC**, and **NO**. These abbreviations mean common terminal, normally closed terminal, and normally open terminal. “Normally” refers to the switch’s unactuated state in the generic contact description: the normally closed contact is connected to common, while the normally open contact is not connected to common. The exact device marking or schematic controls if it differs from that generic description.

To trace a documented circuit, start with the aircraft wiring diagram and the switch’s own markings or schematic. Identify which terminal the diagram uses as common and whether the circuit uses the normally open or normally closed contact. Then follow the documented conductors from those contacts toward the relevant indication input. The diagram, rather than the apparent physical layout of terminals, establishes the intended connections.

At a high level, the path is: mechanical actuation changes a switch contact state; the connected circuit receives or loses the documented electrical path; and the indication logic interprets that input. The contact alone does not encode a universal gear-up or gear-down message. For example, the diagram might show a selected contact feeding an indication input, but the contact label cannot reveal how the complete aircraft circuit interprets that input. Read the circuit function and indication logic rather than assigning a gear status from COM, NC, or NO alone.

Do not infer terminal assignments, wire destinations, or voltages from a generic drawing or from the physical arrangement of pins. Use the connection diagram, terminal marking, circuit function, and permissible load documented for the exact switch and equipment. This keeps the explanation tied to the actual circuit instead of an assumed layout.

## What determines the switch transition point

The switch changes contact state as its actuator moves in response to the associated mechanism. For a landing-gear monitor, the important relationship is between the mechanically defined gear position and the switch’s electrical transition. A monitoring circuit can report only the state produced by its sensing arrangement; the label on a contact does not establish where in the gear’s movement the switch changes state.

Mounting geometry, actuator travel, and operating position affect that relationship. If the mechanical position and switch transition do not correspond as specified for the aircraft, the electrical state may not represent the intended gear position. This is why a state change observed at an arbitrary point in movement cannot, on its own, establish correct indication behavior.

The relevant transition point and any adjustment criteria must come from approved aircraft-specific data. No universal dimension, travel value, or adjustment instruction follows from the terms COM, NC, and NO. Do not treat a general explanation of contact logic as a substitute for the applicable maintenance procedure.

## How to verify the documented circuit safely

Begin with the applicable aircraft wiring diagram and maintenance procedure. Use them to identify the switch, the documented terminal connections, the relevant test points, the mechanically defined position, and the expected contact or circuit states. The procedure also determines whether a check is authorized and what conditions apply. Testing must follow applicable deenergization and qualification requirements.

Where the approved procedure permits it, a continuity or state-change check can establish whether the documented switch contacts change state as the mechanism reaches the specified position. Compare the observed result with the expected states in the procedure and diagram. A generic continuity result is not enough to establish that the aircraft indication is correct: the result must be interpreted in the context of the complete documented circuit and the system’s expected indication.

If the expected indication is absent or inconsistent, the circuit has more than one possible point of concern. The issue could involve a switch contact, an open or short in wiring, a connector problem, or a downstream indication fault. A check at the switch alone does not rule out faults elsewhere, and a downstream symptom does not identify the switch as the cause. Approved troubleshooting steps define how to distinguish these possibilities.

### Related guides

- [ball screw actuator home position micro switch replacement](/guides/ball-screw-actuator-home-position-micro-switch-replacement/)
- [bottling machine end of stroke micro switch](/guides/bottling-machine-end-of-stroke-micro-switch/)
- [automated guided vehicle home position micro switch location](/guides/automated-guided-vehicle-home-position-micro-switch-location/)
- [accelerator pedal position stop micro switch operating force](/guides/accelerator-pedal-position-stop-micro-switch-operating-force/)

## Limits, faults, and interpretation cautions

A stuck or intermittent contact can produce an absent or misleading status indication, depending on the circuit logic. The effect cannot be determined from the terminal labels alone: it depends on which contact is used and how the aircraft circuit interprets its state. Similarly, a plausible indication does not by itself establish the mechanical condition of the gear.

Do not treat this general wiring explanation as a repair procedure or as authority to alter a circuit. Do not bypass or defeat a warning or indication circuit, and do not use one indication alone as proof of mechanical gear security. For aircraft-specific interpretation, testing, and maintenance decisions, follow the approved aircraft documentation and applicable procedures, with qualified personnel where required.

The practical reading sequence is to identify the documented switch and its mechanically defined position, trace its marked contacts through the aircraft diagram to the indication input, and compare any permitted test results with the expected states in the approved procedure. The terminal labels explain contact relationships; the aircraft documentation establishes what those relationships mean in the landing-gear monitoring circuit.

This concludes the explanation of aircraft landing gear monitor micro switch wiring.

## Sources and references

- Defense Logistics Agency ASSIST: [MIL-PRF-8805K: Switches and Switch Assemblies, Sensitive, Snap Action, General Specification For](https://quicksearch.dla.mil/qsDocDetails.aspx?ident_number=7196){: rel="nofollow noopener noreferrer" }
- Occupational Safety and Health Administration: [29 CFR 1910.333: Selection and Use of Work Practices](https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.333){: rel="nofollow noopener noreferrer" }
- Wikipedia: [Miniature snap-action switch](https://en.wikipedia.org/wiki/Miniature_snap-action_switch){: rel="nofollow noopener noreferrer" }
