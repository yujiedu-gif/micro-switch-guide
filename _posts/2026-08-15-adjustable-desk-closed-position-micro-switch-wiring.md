---
title: "adjustable desk closed position micro switch wiring"
description: "adjustable desk closed position micro switch wiring: Understand the operating idea, essential terminology, practical checks, limitations, and evidence."
date: 2026-08-15 09:00:00 +0800
category: Applications
tags:
  - adjustable desk closed position micro switch wiring
  - micro switches
  - Applications
author: editorial_team
---

**Adjustable desk closed position micro switch wiring** is a way to provide a controller with an endpoint signal when a desk reaches its closed position, if that desk design uses a micro switch for this purpose. The switch’s COM, NO, and NC labels identify contact terminals; they do not, by themselves, specify which terminals belong in a particular desk circuit. That choice depends on the controller’s documented input logic and on the contact state observed at rest and when the actuator is operated.

Treat the switch circuit as a position signal, not as a presumed motor-power connection. Desk designs differ, so there is no universal wiring diagram or guaranteed terminal choice. Before accessing or testing the circuit, isolate power and make sure unexpected desk movement is prevented. Then verify the switch’s contact behavior while unpowered and compare it with the desk’s controller documentation before making or interpreting a connection.

## What adjustable desk closed position micro switch wiring does

In a desk design that uses a micro switch at the closed endpoint, the switch changes an electrical contact state as its actuator is operated. The controller can use that change as a signal that the desk has reached the specified position. This describes the switch’s signaling role, not a claim that every adjustable desk uses this arrangement or that a switch is present at every endpoint.

The mechanical event and the electrical event are related but distinct. The desk mechanism must reach the endpoint and operate the switch actuator; the switch contacts must then change state in a way the controller recognizes. A correctly placed switch that does not change contact state cannot provide the expected signal. Conversely, a contact change alone does not establish that the desk’s controller interprets it as “closed.”

Do not assume that the micro switch carries motor current. In the conceptual arrangement addressed here, its role is an endpoint signal to a controller input. The motor supply and motor leads are a separate part of the desk circuit unless the desk’s own documentation states otherwise. Switch terminal labels do not reveal the controller input’s voltage, polarity, or electrical behavior.

## Identify COM, NO, and NC before wiring

COM means common terminal, NO means normally open terminal, and NC means normally closed terminal in general changeover terminology. These are contact names, not instructions that “NO is always correct for closed” or “NC is always correct for closed.” Check the markings on the actual switch and verify them against its schematic, because the exact device schematic governs the terminal identification.

A continuity check helps establish what the contacts do in the switch’s two relevant mechanical conditions. With power isolated and the switch disconnected from any circuit as required for a valid measurement, check continuity between COM and each candidate terminal while the actuator is at rest. Then operate the actuator and repeat the measurements. Record which pair is continuous at rest and which pair is continuous when actuated. Do not infer those results from a desk’s endpoint name.

The selected contact pair depends on the controller’s input logic and the state it expects when the desk is away from or at the closed endpoint. Determine that expectation from the desk’s circuit or controller documentation, then compare it with the measured switch states. Without that information, the terminal labels and continuity results alone cannot establish which pair should be connected.

## Trace the closed-position signal path

Conceptually, trace the documented position-signal circuit from the controller input, through the selected switch contact, and back through the circuit’s documented return. The switch contact is the point where the endpoint condition changes the signal path. This is a functional description, not a pinout: the available evidence does not establish a universal desk connector, wire color, terminal order, or return arrangement.

Keep this signal path distinct from motor supply conductors and motor leads. Do not treat a motor wire as a switch return, or connect the switch to a motor conductor, based only on proximity or a terminal label. The physical routing and connection points must come from the desk’s circuit documentation. Likewise, COM, NO, and NC do not identify an input voltage, polarity, or fail-safe behavior. Those characteristics vary and must not be guessed.

If the controller documentation identifies the input and return and explains the expected contact state, use that information to assess the measured contact pair. If it does not identify them, the correct connection remains unresolved. Do not substitute a generic diagram for missing desk-specific information; a plausible-looking connection can still produce no endpoint signal or a signal the controller interprets differently than intended.

## Safely verify adjustable desk closed position micro switch wiring

Before access, disconnect power and confirm that unexpected desk movement is prevented. Keep the continuity test unpowered; a continuity measurement is not a method for testing a live controller input. If the switch is connected to other circuitry, follow the desk documentation for how to isolate it sufficiently to obtain a meaningful measurement.

Use this basic sequence:

1. Identify the switch’s COM, NO, and NC markings from the device schematic.
2. With power isolated, place the actuator at rest and check continuity between COM and each candidate contact.
3. Operate the actuator by hand, where appropriate, and repeat the checks. Note which contact state changes.
4. Compare the observed states with the controller documentation’s description of the closed-position input and return.
5. Confirm that the switch is mechanically operated at the desk’s closed endpoint, without assuming that the observed electrical state proves controller recognition.

A change in continuity confirms a contact-state change under the test conditions; it does not verify the controller’s input voltage, polarity, or interpretation. Do not reconnect or test desk operation until the documented circuit supports the proposed connection. If the controller information is missing or unclear, consult the desk’s manufacturer-specific circuit documentation or a qualified technician rather than guessing.

### Related guides

- [ball screw actuator home position micro switch replacement](/guides/ball-screw-actuator-home-position-micro-switch-replacement/)
- [bottling machine end of stroke micro switch](/guides/bottling-machine-end-of-stroke-micro-switch/)
- [automated guided vehicle home position micro switch location](/guides/automated-guided-vehicle-home-position-micro-switch-location/)
- [accelerator pedal position stop micro switch operating force](/guides/accelerator-pedal-position-stop-micro-switch-operating-force/)

## When a closed-position signal does not behave as expected

Start by separating mechanical actuation from electrical contact behavior. At the closed endpoint, check whether the mechanism actually operates the switch actuator and whether the switch is mounted so that this occurs. Then repeat the unpowered continuity check and confirm that the selected pair matches the measured state and the controller’s documented expectation.

If the actuator moves but the measured contacts do not change state, the switch or its contact path may not be providing the expected transition. If the contacts change state but the controller does not recognize the endpoint, that observation alone cannot identify the cause. The remaining issue could be in the documented signal path, the controller input, or an adjustment fault; do not treat a continuity result as proof that the controller or desk adjustment is correct.

Stop if the supply or input characteristics are unknown. Use the desk’s circuit documentation to distinguish a switch/contact-path issue from a controller-input or adjustment issue. If the documentation does not resolve the connection or safe test conditions, consult a qualified technician. The conclusion is specific: select and assess a contact pair by its measured state and the controller’s documented logic, while keeping endpoint signaling separate from motor power wiring.

This concludes the explanation of adjustable desk closed position micro switch wiring.

## Sources and references

- Defense Logistics Agency ASSIST: [MIL-PRF-8805K: Switches and Switch Assemblies, Sensitive, Snap Action, General Specification For](https://quicksearch.dla.mil/qsDocDetails.aspx?ident_number=7196){: rel="nofollow noopener noreferrer" }
- Wikipedia: [Miniature snap-action switch](https://en.wikipedia.org/wiki/Miniature_snap-action_switch){: rel="nofollow noopener noreferrer" }
