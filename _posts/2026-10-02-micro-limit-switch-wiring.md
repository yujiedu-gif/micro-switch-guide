---
title: "Micro limit switch wiring: identify terminals and connect contacts"
description: "micro limit switch wiring: Understand the operating idea, essential terminology, practical checks, limitations, and evidence needed for careful selection,."
date: 2026-10-02 09:00:00 +0800
category: Basics
tags:
  - micro limit switch wiring
  - micro switches
  - Basics
author: editorial_team
---

A **micro limit switch wiring** job starts with contact behavior, not terminal position or wire color. Identify which terminals are connected with the actuator released, verify how that changes when the actuator is pressed, and then connect the switch according to its schematic and the circuit’s intended function. The exact device diagram controls; there is no universal terminal layout.

The steps below describe a general identification and verification method. They do not establish whether a particular switch is suitable for a circuit. That depends on its documented contact ratings and the circuit’s voltage, current, and load type. If those details are unavailable, do not infer them from the switch’s appearance.

## Micro limit switch wiring: what the terminals mean

A micro limit switch is a miniature snap-action switch that can change an electrical contact state in response to mechanical actuator movement. It is commonly used for position or limit detection. Some switches use a changeover contact with three terminals; others may have only two terminals or use different markings. Check the exact device’s labels and schematic before identifying connections.

For a generic changeover contact, **COM** means common, **NO** means normally open, and **NC** means normally closed. “Normally” refers to the actuator’s unactuated, or released, state. In that state, COM and NC are connected, while COM and NO are not connected. When the actuator is operated, the contact changes state: COM and NO connect, and COM and NC disconnect.

These terms describe contact behavior, not a guaranteed physical arrangement. COM, NO, and NC may appear in different positions on different devices, and a two-terminal switch may not provide both changeover paths. The exact marking or device schematic takes precedence over a generic description. Do not use wire color or terminal location as a substitute for checking the documentation and confirming the contact states.

## Identify terminals with a continuity test

First isolate the circuit from its power source. Before using a continuity meter, verify that the circuit is deenergized. A meter reading or an assumption that a control is off is not a substitute for verifying the isolated condition. The cited United States workplace rule generally requires exposed live parts to be deenergized before work and requires a qualified person to verify the deenergized condition with test equipment. Work on energized parts is limited to qualified persons.

With power isolated, consult the switch diagram and identify candidate terminal pairs. Use the meter’s continuity function to compare the terminals with the actuator released, then operate the actuator and repeat the measurements. On a generic three-terminal changeover contact, the pair connected in the released state identifies the COM-to-NC path; the pair that connects when the actuator is pressed identifies the COM-to-NO path. The terminal common to those two paths is COM.

Treat this measurement as a verification step, not permission to disregard the device diagram. Compare the observed states with the exact switch markings or schematic. If the results do not agree, stop and resolve the discrepancy rather than guessing. Do not infer terminal identity from physical position or wire color. If the device has different markings, only two terminals, or no usable diagram, its exact contact arrangement remains unresolved until its documentation or identification is established.

## Connect the switch for the required circuit behavior

Once the terminals are identified, decide which contact behavior the circuit requires. Use COM and NO when the circuit should close upon actuation, or COM and NC when it should open upon actuation, subject to the circuit design. These descriptions state how the switch contact behaves; they do not establish whether the complete circuit should be on or off in a particular machine state.

Follow the supplied switch schematic and the circuit diagram. Connect conductors to the intended terminals using the connection method specified for the device. Do not assume that a familiar arrangement, another switch’s wiring, or a wire’s color applies here. If the diagram and the circuit’s intended behavior cannot be reconciled, do not energize the circuit until the correct connection is established.

For a changeover switch, use the required contact path and leave the unused contact insulated and secured as appropriate. Do not allow an unused conductor or terminal to make an unintended connection. This is a general connection sequence, not a universal wiring diagram: terminal identification, circuit function, and the supplied schematic govern the actual connections.

## Check ratings and circuit conditions before energizing

Before making or restoring a connection, compare the switch’s documented contact ratings with the circuit voltage, current, and load type. Contact ratings are distinct from the circuit’s requirements; identifying COM, NO, and NC does not show that the switch can directly control the load. Do not assume a rating or suitability when the exact device documentation is unavailable.

Inductive loads can create switching stresses and may need a suitable protective or interface arrangement. Whether direct switching is appropriate, or an interface is needed, depends on the documented ratings and the circuit conditions. The available information here does not specify a rating, a particular load, or a protective arrangement, so it cannot determine that choice for a specific circuit.

Keep mains and hazardous-voltage work to qualified people. Before restoring power, check that connections follow the diagrams, conductors are secured at their intended terminals, and the enclosure and wiring have been safely reassembled. The United States workplace rule described above generally calls for deenergizing exposed live parts before work, verification of the deenergized condition by a qualified person using test equipment, and limiting work on energized parts to qualified persons. Verify all applicable requirements for the work and jurisdiction.

### Related guides

- [dual micro switch](/guides/dual-micro-switch/)
- [touch micro switch](/guides/touch-micro-switch/)
- [no nc micro switch](/guides/no-nc-micro-switch/)
- [normally open micro switch](/guides/normally-open-micro-switch/)

## Verify operation after wiring

Keep power isolated and check continuity again in the intended released and actuated states. Confirm that the selected contact path matches the circuit’s required behavior and the switch diagram. This check validates the contact logic; it does not by itself establish that the circuit or load is correctly rated.

After safe reassembly, test the circuit under controlled conditions and confirm the expected state change. If its behavior differs, isolate power and recheck the schematic, terminal identification, and circuit logic before making another change. Do not troubleshoot exposed energized parts unless qualified to do so and permitted under applicable requirements.

The reliable method for micro limit switch wiring is to verify contact states with power isolated, connect according to the exact device and circuit diagrams, and confirm ratings before energizing. If terminal identity, contact behavior, or suitability remains uncertain, leave it unresolved rather than relying on a generic layout or an assumed rating.

## Sources and references

- Defense Logistics Agency ASSIST: [MIL-PRF-8805K: Switches and Switch Assemblies, Sensitive, Snap Action, General Specification For](https://quicksearch.dla.mil/qsDocDetails.aspx?ident_number=7196){: rel="nofollow noopener noreferrer" }
- Occupational Safety and Health Administration: [29 CFR 1910.333: Selection and Use of Work Practices](https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.333){: rel="nofollow noopener noreferrer" }
- Wikipedia: [Miniature snap-action switch](https://en.wikipedia.org/wiki/Miniature_snap-action_switch){: rel="nofollow noopener noreferrer" }
