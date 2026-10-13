---
title: "nos micro switch: What Normally Open Means"
description: "nos micro switch: Understand the operating idea, essential terminology, practical checks, limitations, and evidence needed for careful selection,."
date: 2026-10-12 16:49:35 +0800
category: Basics
tags:
  - nos micro switch
  - micro switches
  - Basics
author: editorial_team
---

A **nos micro switch** describes a normally open contact arrangement: the contact is open when the actuator is in its unactuated position. When the actuator is operated, that contact state changes in designs using the NO contact. This describes the switch’s contacts, not whether a connected device is powered or running. The circuit, supply, and other components determine what happens beyond the switch.

Understanding the distinction helps when tracing actuator movement or checking a switch. The contact state can be verified directly, but terminal identification and the measurement setup matter. Do not infer a switch’s state from the behavior of the connected device alone.

## nos micro switch: Normally Open Contact State

“Normally open” refers to the contact state associated with the actuator’s unactuated position. In that position, an NO contact is open. When the actuator is operated, the contact changes state in a design using this arrangement. After the actuator is released, the contact returns toward its unoperated state as the switch’s mechanism permits.

The word “normally” is a reference to the actuator’s position, not a statement that the connected circuit or load is normally off. It does not describe whether voltage is present at the switch, whether current is flowing elsewhere in the circuit, or whether a device is operating. Those are circuit-level conditions, not definitions of the NO contact state.

Some switches use terminals marked COM, NO, and NC. In general changeover terminology, COM means common, NO means normally open, and NC means normally closed. These labels describe terminal roles, but the exact device schematic should be checked before identifying terminals or assuming how they are connected. Do not rely on a label alone when the circuit documentation or device schematic is available.

A useful way to think about NO is to keep three questions separate: What position is the actuator in? What is the contact state? What is happening in the larger circuit? The first two relate to the switch. The third depends on wiring and other circuit conditions. Keeping those questions distinct avoids treating “normally open” as a universal description of a device’s powered state.

## How Actuator Movement Changes Continuity

In an NO contact arrangement, the contact is open with the actuator unoperated. Operating the actuator changes the contact state; in designs using this contact, the contact becomes closed while operated. Releasing the actuator allows the mechanism to return toward the unoperated position, where the NO contact is open again. The exact travel and switching behavior depend on the switch design, so do not assume a particular movement distance or timing.

Snap action is one mechanism term that helps describe how contact movement relates to actuator movement. In the definition in MIL-PRF-8805K section 6.5.21, snap action is contact action in which the speed of the moving contacts is relatively independent of the speed of the actuating mechanism. This definition describes the relationship between contact speed and actuator speed. It does not establish a particular switching speed, travel, or electrical result for an individual switch.

Release force is another defined mechanism term. MIL-PRF-8805K section 6.5.17 defines release force, or releasing force, as the force or torque to which force on the actuator must be reduced to permit the contacts to return to the unoperated position after operation. This concerns the return condition. It should not be treated as a specification for an unidentified switch; no particular value is established here.

The contact transition alone does not show that a load has been energized. A closed contact may form part of a circuit path, but the effect depends on how the switch is wired and on the supply and other components. Likewise, observing that a device is off does not establish that the NO contact is open. The mechanical position, contact state, and circuit outcome must be considered separately.

## Check an NO Micro Switch Safely

A continuity check can compare the contact state with the actuator unoperated and operated, but the circuit must first be made safe for measurement. Isolate circuit power and verify that the circuit is de-energized before testing. Do not measure continuity on an energized circuit.

Identify the relevant terminals from the switch schematic and the circuit documentation. If the device has COM, NO, and NC markings, treat them as general changeover terminology and confirm the exact terminal arrangement from the relevant schematic. Do not guess terminal identity from physical position or assume every switch uses the same layout.

For a meaningful contact check, disconnect the switch appropriately from the circuit so parallel paths do not affect the measurement. With power isolated and the measurement points identified, use a continuity meter across the terminals associated with the NO contact. Compare the indication with the actuator unoperated and then while the actuator is operated. The expected state-based pattern for an NO contact is open when unoperated and a changed, closed contact state when operated. Release the actuator and check whether the contact returns toward its unoperated state.

Interpret the meter result as a check of the measured path, not as a general diagnosis of the whole device or circuit. If the switch is not sufficiently isolated, another circuit path may affect the reading. If terminal identity, circuit isolation, or the measurement result is uncertain, use the circuit documentation and qualified service guidance rather than drawing a conclusion from an ambiguous check.

### Related guides

- [dual micro switch](/guides/dual-micro-switch/)
- [touch micro switch](/guides/touch-micro-switch/)
- [no nc micro switch](/guides/no-nc-micro-switch/)
- [normally open micro switch](/guides/normally-open-micro-switch/)

## Why Contact State Does Not Predict Device Operation

An NO label describes the contact’s state relative to the unoperated actuator position. It does not guarantee that a connected load will be off in that position or on when the actuator is operated. Whether a load operates depends on circuit topology, supply, and other components. The switch’s state is one part of that circuit, not a complete description of its behavior.

For the same reason, a device symptom by itself cannot establish that the switch has failed. A device that does not operate may have causes elsewhere in the circuit; a device that operates does not, by itself, prove that the contact state or wiring is correct. A continuity measurement across identified contacts is more direct evidence of contact state, provided power is isolated and the switch is appropriately disconnected for the test.

Use the relevant wiring diagram and switch schematic to confirm terminal identification and circuit context. If the available documentation does not resolve the wiring or a continuity result, seek qualified service guidance. The term **nos micro switch** identifies a normally open contact arrangement, not a universal promise about circuit voltage, load operation, or device behavior.

## Sources and references

- Defense Logistics Agency ASSIST: [MIL-PRF-8805K: Switches and Switch Assemblies, Sensitive, Snap Action, General Specification For](https://quicksearch.dla.mil/qsDocDetails.aspx?ident_number=7196){: rel="nofollow noopener noreferrer" }
- Wikipedia: [Miniature snap-action switch](https://en.wikipedia.org/wiki/Miniature_snap-action_switch){: rel="nofollow noopener noreferrer" }
