---
title: "postal scale platform micro switch NO and NC terminals"
description: "postal scale platform micro switch NO and NC terminals: Understand the operating idea, essential terminology, practical checks, limitations, and evidence."
date: 2026-08-12 09:00:00 +0800
category: Applications
tags:
  - postal scale platform micro switch NO and NC terminals
  - micro switches
  - Applications
author: editorial_team
---

A **postal scale platform micro switch NO and NC terminals** are understood by comparing their contact states with the switch released and actuated. The terminal names describe electrical contact behavior, not whether the scale itself is powered. In a scale design that uses a platform switch, movement may press the switch actuator and change a discrete signal. That signal is distinct from the scale’s load measurement function.

The actual switch arrangement and purpose vary by scale. Use the equipment’s connection diagram and the switch’s terminal markings to identify the intended connections; do not infer terminal function from physical position or wire color. If the switch can be safely isolated, an unpowered continuity test can check how its contacts change state.

## What the postal scale platform micro switch NO and NC terminals mean

COM means common terminal, NC means normally closed terminal, and NO means normally open terminal. These names describe the contact arrangement in the switch’s released state. They do not identify whether the scale is powered, and the exact device schematic should be checked because terminal arrangements can vary.

With a typical changeover switch, the COM-to-NC path has continuity while the switch is released, and the COM-to-NO path is open. When the switch is actuated, those paths change: COM-to-NC opens and COM-to-NO has continuity. In this context, “released” means the switch actuator is not being pressed; “actuated” means it is being pressed far enough to operate the contacts. The state names refer to the switch, not to platform weight or scale power.

COM is the shared contact through which the switch connects to either the NC or NO path. To interpret a diagram, follow the circuit connection from COM to the named contact and confirm the terminal symbols against the exact switch schematic. A generic physical-layout inference is not a reliable substitute for documented terminal identification. A switch may also have a different contact arrangement, so do not assume that every device has both a usable NO and NC path merely because those terms are common in changeover terminology.

Contact labels also do not determine the electrical rating or permissible load. Those depend on the exact switch and equipment documentation. A continuity result identifies contact behavior under the test conditions; it does not establish whether the switch is suitable for a particular circuit.

## How platform movement can actuate the micro switch

Some postal scale designs may use a linkage, stop, or other platform-associated part to press a micro switch actuator as the platform moves. If the mechanism operates the switch, the contact state changes when the actuator reaches its operating position. That can provide a discrete position or movement signal to the circuit.

This possible mechanism should not be treated as universal. Platform construction, switch placement, and the purpose of a switch differ by scale design. Without the equipment diagram or direct inspection of a safely accessible mechanism, the relationship between platform travel and switch actuation remains uncertain. Do not assume that a particular amount of platform movement, direction, or position corresponds to a specific contact state.

A platform switch’s discrete signal is also separate from the function that measures load. A scale may use a load cell or another load-sensing arrangement to determine weight, while a switch indicates a discrete mechanical state. Testing the switch therefore does not test the load sensor, calibrate the scale, or establish weighing accuracy. Keep those functions separate when interpreting a contact test.

When a diagram is available, trace the documented switch connections and circuit function rather than guessing from the platform’s appearance. If the mechanism is not documented or cannot be observed safely, limit the conclusion to the switch contact behavior verified in isolation. That establishes what the contacts do, not how the entire scale uses their signal.

## Test NO and NC contacts safely with power isolated

A continuity check should be made only with the scale disconnected from power and the switch leads isolated from the rest of the circuit. Follow applicable deenergization and qualification requirements. Do not test a live circuit. If reaching the switch requires unsafe disassembly, or the circuit cannot be isolated, stop rather than proceeding with the measurement.

With the switch isolated, use a continuity meter to check the contact pairs. First leave the actuator released and measure between COM and NC, then between COM and NO. Next press the actuator far enough to operate it and measure those same pairs again. Compare the released and actuated readings. The test is based on whether each path is continuous or open in each state, not on wire color or an assumed terminal position.

For a typical changeover switch, the expected pattern is continuity from COM to NC and an open path from COM to NO when released. When actuated, the expected pattern reverses: COM to NC is open, and COM to NO is continuous. This comparison helps identify the terminals by behavior, provided the device is a changeover switch and the actuator has operated fully.

A continuity test can be misread if the switch remains connected to other circuitry, because other circuit paths may affect the measurement. Isolating the switch leads helps make the result specific to its contacts. Confirm the terminal markings and schematic before assigning a verified contact path to equipment wiring. Do not use wire color alone as proof of terminal function.

The test does not authorize reconnecting the switch to a circuit with an assumed load or rating. For the intended circuit, use the connection diagram, terminal marking, circuit function, and permissible load documented for the exact switch and equipment. If those details are unavailable, the wiring application remains unresolved even if the contact states are clear.

### Related guides

- [ball screw actuator home position micro switch replacement](/guides/ball-screw-actuator-home-position-micro-switch-replacement/)
- [bottling machine end of stroke micro switch](/guides/bottling-machine-end-of-stroke-micro-switch/)
- [automated guided vehicle home position micro switch location](/guides/automated-guided-vehicle-home-position-micro-switch-location/)
- [accelerator pedal position stop micro switch operating force](/guides/accelerator-pedal-position-stop-micro-switch-operating-force/)

## Interpret results and recognize design limits

A typical changeover switch alternates continuity between COM-NC and COM-NO as it is actuated. If the measured result differs, first make sure the switch is isolated, the correct terminals are being measured, and the actuator has moved far enough to operate the contacts. The test does not establish how far the platform should travel or what point in its movement should trigger the switch.

Other explanations are possible. The device may not be a changeover switch, contact wear may affect operation, or the mechanism may not fully press the actuator. The available information does not determine which explanation applies to a particular scale. Check the exact switch schematic and equipment documentation before concluding that the switch has failed or assigning a circuit function.

A passing contact test confirms only the observed contact behavior in the released and actuated states. It does not verify the platform mechanism, the scale’s load measurement, calibration, or weighing accuracy. Likewise, a different result does not by itself diagnose the load-sensing system. Keep conclusions within what the isolated test actually measures.

For the **postal scale platform micro switch NO and NC terminals**, use the device documentation to establish identity and circuit role, then compare COM-to-NC and COM-to-NO continuity with the switch isolated in both states. Treat platform actuation as design-dependent, and do not infer wiring function from color, physical layout, or a contact test alone.

## Sources and references

- Defense Logistics Agency ASSIST: [MIL-PRF-8805K: Switches and Switch Assemblies, Sensitive, Snap Action, General Specification For](https://quicksearch.dla.mil/qsDocDetails.aspx?ident_number=7196){: rel="nofollow noopener noreferrer" }
- Occupational Safety and Health Administration: [29 CFR 1910.333: Selection and Use of Work Practices](https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.333){: rel="nofollow noopener noreferrer" }
- Wikipedia: [Miniature snap-action switch](https://en.wikipedia.org/wiki/Miniature_snap-action_switch){: rel="nofollow noopener noreferrer" }
