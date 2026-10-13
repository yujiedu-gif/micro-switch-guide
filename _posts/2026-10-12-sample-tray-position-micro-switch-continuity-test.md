---
title: "Sample tray position micro switch continuity test: a practical verification guide"
description: "sample tray position micro switch continuity test: Understand the operating idea, essential terminology, practical checks, limitations, and evidence."
date: 2026-10-12 16:49:35 +0800
category: Troubleshooting
tags:
  - sample tray position micro switch continuity test
  - micro switches
  - Troubleshooting
author: editorial_team
---

A sample tray position micro switch continuity test checks whether the switch contacts change electrical state when the tray mechanism moves between its defined released and actuated positions. It applies only to designs that use a micro switch to sense tray position. The test is performed without powered control logic, so it can provide evidence about contact behavior but cannot establish that the controller or complete tray system operates correctly.

Use the device’s service procedure and documentation to identify the required tray positions, terminal functions, and safe access method. Do not infer terminal locations from pin position alone. If you cannot confirm safe isolation, terminal identity, or the expected tray positions, stop and consult the applicable service information.

## What the sample tray position micro switch continuity test can establish

A continuity or resistance measurement can show whether a selected contact pair is electrically continuous at a particular mechanism position. Comparing readings in both defined positions can show whether the contact state changes as expected according to the device documentation. A single reading, taken without a known position reference, does not establish that the switch is responding correctly to tray movement.

This is an unpowered contact test. It does not measure live voltage, verify a controller input, or prove that the controller interprets the switch signal. Nor does a change in continuity by itself prove that the tray reaches its intended positions or that the complete position-sensing system works. Those conclusions require the device’s approved functional verification procedure.

Before measuring, determine which tray position the documentation identifies as released and which it identifies as actuated. These labels refer to the specified mechanism positions for the device, not to a universal tray location or a presumed electrical state. The expected contact behavior must also come from the device’s documentation or schematic. Without that reference, a meter reading alone cannot establish which state is correct.

The test can help distinguish several fault paths, but only when its observations are kept separate. First consider whether tray movement makes the switch actuator move as intended. Then assess the switch contact behavior at the defined positions. Finally, if the switch readings are correct but the circuit path is not, assess wiring continuity and connections. A fault in one of these areas should not be treated automatically as evidence of a fault in another.

## Prepare the sample tray position micro switch continuity test safely

Follow the equipment’s service procedure to isolate power and prevent unexpected movement before accessing the switch. Do not perform this procedure as a live-voltage check. If safe isolation cannot be confirmed, or if access requires forcing the tray or actuator, stop rather than proceed. Move the mechanism only as directed by its procedure and without exceeding its normal travel.

Access the switch in a way that leaves the tray mechanism and actuator undamaged. Before connecting a meter, identify the relevant terminals from device markings, documentation, or the circuit schematic. In generic changeover terminology, COM means common terminal, NO means normally open terminal, and NC means normally closed terminal. These names do not establish the pin layout or the expected contact state for a particular device. Verify the exact switch schematic before choosing a contact pair.

Set the meter to its continuity function or an appropriate resistance range, following the meter’s instructions. Check the contact pair specified by the device documentation. If the switch remains connected to parallel circuitry that could affect the reading, disconnect a lead as required for a valid measurement. Do not assume that a reading through connected circuitry represents the switch contacts alone.

Keep track of the tray position and contact pair for each measurement. Record whether the meter indicates continuity, no continuity, or a changing or intermittent reading. Use the same identified pair for the comparison unless the documentation directs otherwise. These controls make the released-versus-actuated comparison interpretable; they do not supply an expected result where the device documentation gives none.

## Measure continuity in released and actuated tray positions

With the equipment isolated and the meter connected to the documented contact pair, place the tray mechanism in its defined released position. Take and record the reading. The reading describes that pair’s electrical state at that position only. Compare it with the documented expectation rather than assuming that a specific terminal pair must be open or closed.

Move the tray mechanism to its defined actuated position using the approved method. Take and record a second reading across the same contact pair. Compare the two readings with the device’s specified behavior. The important evidence is the state comparison across the defined positions, not an isolated meter result interpreted without a position reference.

Observe the switch actuator during this movement. Confirm separately whether the tray mechanism makes the intended mechanical contact with the actuator and whether the actuator moves through its intended operating point. Do not force the actuator or continue past normal mechanism travel. If the tray does not engage the actuator, that observation concerns mechanical actuation; it does not, by itself, establish that the electrical contacts are faulty.

If needed, repeat the released-to-actuated comparison carefully to see whether the state change is consistent. Note intermittent readings, but do not use repeated cycling to overcome binding or obstruction. A repeatable transition supports the conclusion that the tested contact pair changes state during the observed movement. It does not prove the complete tray system works, and it does not replace the device’s approved functional check.

## Interpret results and separate switch, alignment, and wiring faults

If the contact pair does not change state as specified, first confirm that you identified the correct terminals and used the correct tray positions. Check the exact device schematic and the applicable expected behavior before concluding that the switch has failed. If those references are confirmed and the contact still does not change as specified, the result may indicate a switch contact or switch fault. A continuity test alone does not establish the underlying cause.

If the switch changes state when its actuator is operated directly as allowed by the service procedure, but tray movement does not produce that change, investigate the mechanical path separately. The tray may not be engaging the actuator, or alignment, obstruction, or actuator engagement may require attention. This result points toward a mechanical actuation issue; it should not be described as proof of a contact fault.

If the documented switch contact behavior is correct at the switch but continuity through the circuit is not, inspect the wiring path and connections as a separate step. A lead may need to be disconnected to prevent parallel circuitry from affecting the reading. Compare the switch-terminal result with the disconnected wiring-path result so the two measurements are not confused. The evidence may point to a wiring issue, but do not extend it into a claim about powered controller operation.

These checks have distinct purposes: mechanical observation establishes whether tray movement reaches the actuator; the contact test checks electrical state at the switch; and a wiring continuity check examines the circuit path. Treating them as interchangeable can misidentify the fault. None of them, alone, establishes that a powered controller input responds correctly or that the complete tray system functions.

### Related guides

- [automated guided vehicle guard interlock micro switch intermittent operation](/guides/automated-guided-vehicle-guard-interlock-micro-switch-intermittent-operation/)
- [assembly robot travel limit micro switch failure causes](/guides/assembly-robot-travel-limit-micro-switch-failure-causes/)
- [air compressor travel limit micro switch troubleshooting](/guides/air-compressor-travel-limit-micro-switch-troubleshooting/)
- [boom lift travel limit micro switch symptoms](/guides/boom-lift-travel-limit-micro-switch-symptoms/)

## When to stop and verify the repair

Stop if you cannot confirm safe isolation, the terminal functions, the exact switch schematic, or the device-defined released and actuated positions. Also stop if the mechanism binds, an obstruction prevents normal movement, or the actuator would need to be forced. Do not fill gaps in the service information with assumed pin positions or expected readings.

After any service action, restore electrical connections and guards according to the device procedure. Then verify position sensing using the approved procedure for the equipment. A meter-based continuity check is not a substitute for a powered functional check, and it does not prove controller operation or overall tray performance. If the approved verification procedure or its acceptance criteria are unavailable, do not claim the system has passed based only on contact readings.

The useful conclusion from this test is limited: at the positions and terminals checked, the measured contact did or did not behave as specified. Keep mechanical actuation, switch contact behavior, and wiring continuity as separate findings, and use the device’s approved process for final validation.

This concludes the explanation of sample tray position micro switch continuity test.

## Sources and references

- Defense Logistics Agency ASSIST: [MIL-PRF-8805K: Switches and Switch Assemblies, Sensitive, Snap Action, General Specification For](https://quicksearch.dla.mil/qsDocDetails.aspx?ident_number=7196){: rel="nofollow noopener noreferrer" }
- Wikipedia: [Miniature snap-action switch](https://en.wikipedia.org/wiki/Miniature_snap-action_switch){: rel="nofollow noopener noreferrer" }
