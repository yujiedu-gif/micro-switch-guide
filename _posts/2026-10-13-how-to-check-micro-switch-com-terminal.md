---
title: "How to check micro switch COM terminal"
description: "how to check micro switch COM terminal: Understand the operating idea, essential terminology, practical checks, limitations, and evidence needed for."
date: 2026-10-13 11:27:16 +0800
category: Troubleshooting
tags:
  - how to check micro switch COM terminal
  - micro switches
  - Troubleshooting
author: editorial_team
---

Identifying the COM terminal on a micro switch starts with the switch’s markings or applicable documentation, not its physical position or a meter reading alone. To understand **how to check micro switch COM terminal**, first confirm that the device has a documented changeover contact arrangement and identify its reference actuator state. A continuity check can then help verify the documented contact behavior while the switch is isolated from the circuit. It does not, by itself, identify an unknown terminal or diagnose the surrounding equipment.

## How to check micro switch COM terminal

Look for terminal markings on the switch and compare them with the applicable documentation or schematic for that exact device. In a documented changeover arrangement, COM means the common terminal. The labels NO and NC identify the other contact terminals by their state at a specified reference condition. The device’s own markings or schematic take precedence over assumptions based on a generic layout.

Do not identify COM solely by where a terminal sits on the housing. Terminal position is not enough evidence to establish its electrical role. Likewise, a continuity reading between two terminals does not prove which one is COM unless the contact arrangement and actuator reference state are known. A reading only describes the tested pair’s behavior under the test conditions; it does not supply missing terminal identification.

If a marking is absent, unclear, or inconsistent with the documentation, the COM terminal cannot be confirmed from appearance alone. Check the exact device documentation for a terminal diagram or contact arrangement. If that information is unavailable, leave the identity unresolved rather than assigning COM by guesswork. A generic changeover diagram can explain terminology, but it cannot establish the terminal layout of an undocumented switch.

Keep identification separate from verification. Identification uses the device markings or applicable documentation to determine which physical terminal is COM. Verification checks whether the isolated switch behaves as documented in a defined actuator state. These are related tasks, but one does not replace the other: a behavior check cannot establish the terminal labels when the contact arrangement and state are unknown.

## What COM, NO, and NC mean at a defined reference state

For a documented changeover contact, COM is the common terminal. NO means normally open, and NC means normally closed. These labels describe contact states at a specified reference condition. They should not be treated as an unconditional promise about current flow in every actuator position or installed circuit.

The reference condition matters because the actuator’s position or state can affect which contacts are connected. A statement that a contact is normally open or normally closed is incomplete if the relevant reference state is not established. Use the reference state stated in the switch documentation when interpreting the labels or comparing a test result. Do not substitute an assumed resting position for a documented condition.

The names also do not independently establish how the switch is wired into equipment or what the equipment will do when a contact changes state. COM identifies a terminal role in the documented contact arrangement; it does not establish the surrounding circuit’s connections, logic, or response. The meaning of a contact label and the effect of that contact in an appliance are separate questions.

This distinction is especially important when documentation is incomplete. If the switch’s diagram does not establish a changeover arrangement, or does not identify its reference condition, do not assume that the labels apply in a particular way. Confirm the exact device information first. Until then, the terminal identity and expected contact state remain unverified.

## Verify contact behavior with the switch isolated

A continuity check is bounded to the switch, the terminal pair being checked, and the actuator state during the test. Before interpreting a result, the switch must be isolated from the circuit, and the actuator state must be defined. Compare the observed behavior only with the applicable documentation for that switch and that state.

The sequence is therefore: confirm the terminal arrangement and reference state from documentation; isolate the switch from the circuit; define the actuator state; then check the documented terminal pair for continuity. If the arrangement or state is unknown, there is no supported expected result to compare against. Do not invent a pass or fail criterion from the labels alone.

An isolated result can indicate whether the tested pair behaves as documented in that particular state. It cannot establish the condition of external wiring, identify a fault elsewhere in the equipment, or prove that an installed circuit is safe. A reading obtained while the switch remains connected to surrounding circuitry does not meet the isolation boundary described here, so it should not be treated as a switch-only result.

Do not use the meter reading to work backward to an unsupported terminal map. The result depends on the terminals selected and the actuator state. Without documentation connecting those details to COM, NO, and NC, the reading does not resolve which terminal is common. Keep the test record tied to the terminal pair and state actually checked.

### Related guides

- [espresso machine drip tray micro switch troubleshooting](/guides/espresso-machine-drip-tray-micro-switch-troubleshooting/)
- [micro switch condensation troubleshooting](/guides/micro-switch-condensation-troubleshooting/)
- [how to test a extrusion machine home position micro switch](/guides/how-to-test-a-extrusion-machine-home-position-micro-switch/)
- [cash drawer position micro switch intermittent operation](/guides/cash-drawer-position-micro-switch-intermittent-operation/)

## Separate a terminal question from a circuit fault

A result that does not match the documentation does not identify a single cause on its own. The issue may involve incorrect terminal identification, the actuator input or state, an internal contact, external wiring, or another fault in the equipment. Those possibilities concern different parts of the system and should not be collapsed into a diagnosis based only on one continuity check.

First keep the question narrow: are the terminals identified from the exact device information, and does the isolated switch behave as documented in the defined state? If either point is unknown, the switch-level result cannot be interpreted confidently. A mismatch may justify further assessment, but it does not establish that wiring or another equipment component is faulty.

A click is not a substitute for the defined check. It may indicate movement of a snap mechanism, but it does not prove continuity, correct terminal identification, correct wiring, or suitability for a load. Similarly, a single isolated meter reading concerns only the tested switch state and terminal pair. Neither observation establishes the condition or safety of an installed circuit.

Keep the decision boundary clear: markings or applicable documentation identify COM; a continuity check can verify documented behavior only when the switch is isolated and the actuator state is defined. If the documentation is missing or the result is unclear, the appropriate conclusion is that identification or behavior remains unresolved. An isolated switch check does not assess the surrounding circuit or determine whether the installed equipment is safe.

This concludes the explanation of how to check micro switch COM terminal.

## Sources and references

- Defense Logistics Agency ASSIST: [MIL-PRF-8805K: Switches and Switch Assemblies, Sensitive, Snap Action, General Specification For](https://quicksearch.dla.mil/qsDocDetails.aspx?ident_number=7196){: rel="nofollow noopener noreferrer" }
- Wikipedia: [Miniature snap-action switch](https://en.wikipedia.org/wiki/Miniature_snap-action_switch){: rel="nofollow noopener noreferrer" }
