---
title: "Air compressor travel limit micro switch NO and NC terminals"
description: "air compressor travel limit micro switch NO and NC terminals: Understand the operating idea, essential terminology, practical checks, limitations, and."
date: 2026-09-22 09:00:00 +0800
category: Applications
tags:
  - air compressor travel limit micro switch NO and NC terminals
  - micro switches
  - Applications
author: editorial_team
---

# Understanding NO and NC terminal states on a compressor travel limit switch

An **air compressor travel limit micro switch NO and NC terminals** are interpreted by comparing their contact states before and after the actuator moves. The labels do not, by themselves, show which terminal is powered or how the compressor will respond. For a changeover contact, COM is the common terminal, while NO and NC identify connections relative to the actuator’s unactuated state. The exact switch markings and circuit diagram determine whether that generic description applies to the installed device.

A continuity check can help establish the switch’s terminal behavior, but it should be performed with power isolated and the switch separated from the circuit as needed. The observed electrical transfer is only one part of the system: the switch’s mechanical trip point and the compressor’s resulting control response are distinct. Do not infer a travel limit, wiring arrangement, or compressor behavior from terminal labels alone.

## What NO and NC mean on an air compressor travel limit micro switch NO and NC terminals

NO and NC describe contact state with the switch actuator unactuated. In generic changeover terminology, **NO** means normally open and **NC** means normally closed. “Normally” refers to that unactuated reference state; it does not mean that either terminal is inherently energized. **COM** means common terminal. Where the device is a changeover contact, COM is the shared terminal that connects to one contact path or the other as the switch transfers.

For a changeover configuration, the expected unactuated pattern is continuity between COM and NC, with no continuity between COM and NO. When the switch transfers, that pattern changes: COM-NO closes and COM-NC opens. These are generic contact relationships, not a guarantee about every switch or every marking. The exact device marking or schematic controls, so confirm that the installed switch is a changeover type and identify its terminals from its documentation.

The terminal names also do not identify a complete circuit function. A wiring diagram, terminal marking, circuit function, and permissible load documented for the exact switch and equipment are needed to interpret the connection. A physical layout alone is not enough to establish terminal identity or ratings. Numerical travel limits are requirements of the applicable specification sheet and must not be inferred from the component category.

## How the travel limit micro switch transfers contacts

As the actuator moves, it reaches the switch’s operating point and the contacts transfer, if the switch has the relevant changeover configuration. In the generic pattern, COM-NC is continuous before transfer and COM-NO becomes continuous after transfer. This describes electrical contact behavior, not a universal travel distance or a particular compressor action.

The mechanical trip point is the point in actuator movement at which the switch operates. Its position in an installation depends on the switch’s travel characteristics and how it is mounted and actuated. Mounting, actuator geometry, and circuit design determine the actual travel relationship. Check the applicable specification sheet for device-specific travel limits; do not infer a numerical limit from the component category.

The electrical transfer and the system response are separate events. The switch changes its contact state, while wiring and any intervening circuit components determine what that change causes the equipment to do. A circuit may use the NO path, the NC path, or other control logic. Therefore, a contact transfer does not alone establish whether the compressor starts, stops, or responds in another way. Confirm the installed circuit diagram and switch markings before interpreting the switching point.

## Check NO and NC continuity with power isolated

A continuity check can establish which terminal pairs conduct in the switch’s current mechanical state. Keep the test limited to identifying contact behavior; the test does not establish the complete circuit function or permissible load.

1. Isolate compressor power and verify the circuit is de-energized before testing. Follow applicable deenergization and qualification requirements.
2. Identify COM, NO, and NC from the switch markings and the applicable diagram. Do not assign terminals based only on their physical positions.
3. Disconnect the switch from the circuit as needed to avoid misleading readings through parallel paths. Use the exact switch documentation to guide identification.
4. With the actuator unactuated, use a continuity meter to check COM-NO and COM-NC. Record the observed states rather than assuming the generic changeover pattern applies.
5. Move the actuator gently through its available movement while observing the meter. For a changeover contact, expect COM-NO to close and COM-NC to open when the switch transfers. Avoid forcing the actuator beyond its intended travel.
6. Compare the results with the terminal markings and wiring diagram. If the observations do not agree, do not infer a wiring change or equipment fault from the labels alone.

This sequence verifies contact behavior under the test conditions. It does not establish a numerical travel limit, the installed trip position, or the compressor’s resulting control response. Those details require the relevant switch and equipment documentation.

## Why a travel-limit trip point may not match the compressor response

A mechanical trip point concerns actuator movement and switch operation. The compressor’s response depends on what the circuit does with the resulting contact change. Relays, wiring logic, and circuit configuration can affect that response, so the instant the switch transfers does not necessarily describe the instant or manner in which the motor or controller responds.

NO and NC labels are not a complete description of compressor operation, and they do not establish pressure-control behavior. A travel-limit switch contact state should not be used to infer how a pressure-control system works. Trace the installed circuit diagram to understand the connection between the switch and the equipment response; do not substitute a generic terminal convention for that diagram.

Likewise, do not treat a measured contact transfer as a device-specific travel specification. Numerical travel limits are set by the applicable specification sheet. The measured switching point in an installation depends on the actual device and mechanical arrangement, and a generic contact-state check does not establish whether that point meets a required limit.

### Related guides

- [ball screw actuator home position micro switch replacement](/guides/ball-screw-actuator-home-position-micro-switch-replacement/)
- [bottling machine end of stroke micro switch](/guides/bottling-machine-end-of-stroke-micro-switch/)
- [automated guided vehicle home position micro switch location](/guides/automated-guided-vehicle-home-position-micro-switch-location/)
- [accelerator pedal position stop micro switch operating force](/guides/accelerator-pedal-position-stop-micro-switch-operating-force/)

## When terminal readings or markings do not agree

First confirm from the exact switch documentation whether the device is a changeover contact and where COM is marked. A generic changeover contact may use COM, NO, and NC, but that convention does not establish the configuration or terminal assignment of a particular installed switch. Use its exact markings or schematic.

If a reading is unexpected, isolate the switch from the circuit as needed and repeat the continuity checks with the actuator unactuated and then gently moved. This helps distinguish switch contact behavior from a reading affected by circuit paths. Compare the result with the wiring diagram and the switch documentation rather than relying on the shape or position of the terminals.

If readings remain inconsistent, stop testing and verify the wiring diagram or seek qualified service. Do not test live to resolve uncertain terminal identification. Use the applicable diagram, terminal markings, circuit function, and permissible load for the exact switch and equipment; do not infer those details from a generic physical layout. For this **air compressor travel limit micro switch NO and NC terminals** check, the reliable conclusion is limited to verified contact states and documented circuit interpretation.

## Sources and references

- Defense Logistics Agency ASSIST: [MIL-PRF-8805K: Switches and Switch Assemblies, Sensitive, Snap Action, General Specification For](https://quicksearch.dla.mil/qsDocDetails.aspx?ident_number=7196){: rel="nofollow noopener noreferrer" }
- Occupational Safety and Health Administration: [29 CFR 1910.333: Selection and Use of Work Practices](https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.333){: rel="nofollow noopener noreferrer" }
- Wikipedia: [Miniature snap-action switch](https://en.wikipedia.org/wiki/Miniature_snap-action_switch){: rel="nofollow noopener noreferrer" }
