---
title: "Assembly robot travel limit micro switch wiring: connections and checks"
description: "assembly robot travel limit micro switch wiring: Understand the operating idea, essential terminology, practical checks, limitations, and evidence needed."
date: 2026-09-01 09:00:00 +0800
category: Applications
tags:
  - assembly robot travel limit micro switch wiring
  - micro switches
  - Applications
author: editorial_team
---

# Wiring and verifying a robot travel-limit micro switch

**Assembly robot travel limit micro switch wiring** connects a switch’s changing contact state to a controller input so the system can register a travel-limit signal. The switch’s physical contact behavior and the controller’s interpretation are separate: a contact may open or close when operated, while the input response depends on how the controller is designed and configured. This guide covers general low-voltage input wiring, not the design of a safety circuit. Check the equipment documentation for the applicable input voltage, wiring arrangement, and configuration before making connections.

## What the assembly robot travel limit micro switch wiring must signal

A micro switch provides a discrete contact that changes state when its actuator is operated. At a robot travel limit, that change can provide an indication to a controller input. The switch does not, by itself, define what the controller will do with the indication. Input polarity, configuration, and response belong to the controller system and must be verified in its documentation.

Keep three parts of the signal path distinct: the switch contact, the conductors between the switch and controller, and the controller input with its common. The general path runs from the controller input common, through the selected switch contact, to the digital input, subject to the controller’s design. Do not infer a terminal connection, voltage, or input behavior from the switch’s physical position alone.

A travel-limit input is not automatically a safety-rated stop. This wiring description does not establish a safety function or provide a complete robot-cell design. Treat the intended function and the applicable system requirements as matters to confirm in equipment documentation. The practical goal here is narrower: identify the contact state, connect it according to the controller’s documented input arrangement, and confirm that the controller indication changes when the switch is operated.

## Identify the micro switch contacts before connecting wires

Find the COM, NO, and NC markings on the switch, if present. In generic changeover terminology, COM means common terminal, NC means normally closed terminal, and NO means normally open terminal. These names identify contact relationships; they do not establish how a particular controller input must be wired. Verify the exact device schematic rather than assuming terminal position or function from appearance.

The contact state is described with the actuator released or operated. For an NO contact, continuity is absent in the released state and present when the switch is operated. For an NC contact, continuity is present in the released state and absent when the switch is operated. COM is the common terminal that participates in the selected contact path. Confirm these states on the actual device before choosing a connection.

A continuity check can confirm which terminals are connected in each actuator state, but perform it with the switch isolated from the circuit. Do not use a continuity result from a connected or energized circuit to infer the switch’s standalone contact behavior. If markings are missing, unclear, or inconsistent with the device schematic, leave the terminal identity unresolved until the correct documentation or a reliable isolated check establishes it.

Do not identify terminals merely by their location on the housing. Physical arrangements can vary, and the accepted terminal meanings do not establish a universal layout. Record which terminals were confirmed as COM, NO, and NC, along with the released and operated continuity states. That record helps distinguish a switch-contact problem from a conductor or controller-input problem during verification.

## Choose normally open or normally closed input logic

Select the contact path only after checking the controller’s input voltage, sourcing or sinking arrangement, and input configuration in the system documentation. The general signal path is from the controller input common, through the chosen contact, to the digital input, but the controller design determines the applicable connection. Do not assume that a switch contact can be connected directly to an input without confirming the specified arrangement.

With an NO path, the contact is open while the actuator is released and closes when operated. With an NC path, the contact is closed while released and opens when operated. Either contact may be relevant to a limit indication, depending on the controller configuration and the intended signal state. A switch’s contact labels alone do not establish the controller’s interpretation of an open or closed input.

Normally closed wiring may reveal an open-circuit fault because a broken conductor can also leave the circuit open. That observation does not guarantee that the controller will detect the fault or respond safely. The input polarity, configured response, and meaning of an open input depend on the controller system. Confirm those details in its documentation; do not treat contact choice as a substitute for a defined safety function.

Before wiring, match the selected switch contact path to the documented input circuit and common. If the documentation does not establish a compatible arrangement, do not fill the gap by assuming a standard controller circuit. Resolve the input design and configuration first. This boundary keeps the switch’s mechanical contact logic separate from the electronics that receive and interpret the signal.

## Wire and verify the travel-limit signal safely

Before handling conductors, isolate power as required by the equipment procedure. The cited United States workplace rule generally requires exposed live parts to be deenergized before work, requires a qualified person to verify the deenergized condition with test equipment, and limits work on energized parts to qualified persons. Follow applicable requirements and the equipment procedure rather than treating a switch-state check as permission to work on an energized circuit.

Once the documented circuit is established and the work area is in the required state, connect the confirmed contact terminals to the controller input path and common specified for that input. Use secure terminations. Route conductors so they do not interfere with moving robot parts. The available information does not establish wire type, terminal torque, or a specific controller terminal assignment, so obtain those details from the applicable equipment documentation rather than guessing.

For functional verification, keep the area controlled and disable motion as appropriate under the system procedure. Manually operate the switch without allowing robot travel, then observe whether the expected controller input indication changes. Compare the observed state with the documented configuration and the known released and operated contact states. This checks the signal at the controller input; it does not, by itself, verify robot motion programming or establish a safety-rated stop.

Restore operation only after confirming the signal and the travel response using the system’s procedure. If the input indication is unexpected, do not allow travel on the assumption that the switch is working because it clicks or changes continuity. Recheck the contact state, selected terminals, conductor path, common, and documented input configuration. Keep the verification focused on a controlled manual test before allowing robot travel.

### Related guides

- [ball screw actuator home position micro switch replacement](/guides/ball-screw-actuator-home-position-micro-switch-replacement/)
- [bottling machine end of stroke micro switch](/guides/bottling-machine-end-of-stroke-micro-switch/)
- [automated guided vehicle home position micro switch location](/guides/automated-guided-vehicle-home-position-micro-switch-location/)
- [accelerator pedal position stop micro switch operating force](/guides/accelerator-pedal-position-stop-micro-switch-operating-force/)

## Troubleshoot a limit input that does not change state

Trace the failure from the actuator toward the controller rather than replacing parts by assumption. First check whether the actuator engages the switch at the intended travel point. Then, with the switch isolated as required, check whether continuity changes between the confirmed contact terminals as the actuator moves from released to operated. If it does not, the failure is at the mechanical engagement or switch-contact stage; the available information does not determine which component is at fault.

If the switch changes state independently, inspect the terminal selection and conductor continuity through the signal path. Confirm that the selected contact is the one intended by the controller documentation and that the path includes the documented input common. A wire break, incorrect terminal, or common-path issue can prevent the controller input from reflecting the switch state. Do not infer the controller’s response from the switch’s standalone continuity result.

If the switch and conductors show the expected behavior but the controller indication does not change, consult the controller wiring and configuration documentation. Recheck the documented input voltage, sourcing or sinking arrangement, input assignment, and configured logic. The available information does not support a universal diagnostic voltage, controller terminal number, or input test procedure, so use the specific system documentation for those details.

Stop short of enabling travel when the signal path or input behavior remains unexplained. The useful fault boundary is whether the actuator operates the switch, whether the switch contact changes, whether that change reaches the documented input and common, and whether the controller displays the expected state. **Assembly robot travel limit micro switch wiring** is verified only to the extent that this controlled input-state check agrees with the applicable system procedure; it does not by itself establish a safety function.

## Sources and references

- Defense Logistics Agency ASSIST: [MIL-PRF-8805K: Switches and Switch Assemblies, Sensitive, Snap Action, General Specification For](https://quicksearch.dla.mil/qsDocDetails.aspx?ident_number=7196){: rel="nofollow noopener noreferrer" }
- Occupational Safety and Health Administration: [29 CFR 1910.333: Selection and Use of Work Practices](https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.333){: rel="nofollow noopener noreferrer" }
- Wikipedia: [Miniature snap-action switch](https://en.wikipedia.org/wiki/Miniature_snap-action_switch){: rel="nofollow noopener noreferrer" }
