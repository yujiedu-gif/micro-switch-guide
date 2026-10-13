---
title: "micro switch COM terminal testing: Identify and verify the common terminal"
description: "micro switch COM terminal testing: Understand the operating idea, essential terminology, practical checks, limitations, and evidence needed for careful."
date: 2026-10-12 17:55:05 +0800
category: Troubleshooting
tags:
  - micro switch COM terminal testing
  - micro switches
  - Troubleshooting
author: editorial_team
---

A micro switch COM terminal is identified by how it connects to the other contacts as the actuator moves, not by where the terminal sits on the housing. **Micro switch COM terminal testing** compares continuity across terminal pairs in two controlled actuator states. The method applies to a switch with a changeover contact arrangement; terminal configurations vary, so use the exact switch markings or documentation to confirm the result.

This test checks contact relationships at an isolated switch. It does not establish that the switch is suitable for a particular load or that the surrounding equipment circuit works correctly. If you cannot safely disconnect power and establish a de-energized condition, do not proceed with the measurement.

## What COM means on a micro switch

In a changeover contact arrangement, COM means the common terminal: the shared connection that changes its contact relationship between the other terminals as the switch actuator moves. The other contacts are commonly identified as NO, normally open, and NC, normally closed. These names describe contact states at the specified reference condition; they are not a universal guarantee about current flow in an installed circuit.

For a typical changeover arrangement, COM has continuity to one of the other contacts in one actuator state and to the other contact in the alternate state. The names NO and NC indicate which relationship applies at the documented normal or released reference state. The exact device diagram and markings control. Do not assume that every micro switch has three terminals, uses a changeover arrangement, or places COM, NO, and NC in a standard physical order.

A miniature snap-action switch can change an electrical contact state in response to mechanical actuator movement and is commonly used for position or limit detection. That general function does not establish the contact configuration of an individual switch. Before treating a measured terminal as COM, first establish that the switch has the relevant contact arrangement and compare the observed pattern with its documentation.

## micro switch COM terminal testing: isolate and prepare

1. **Disconnect power to the equipment.** Follow the applicable de-energization and qualification requirements. Confirm the switch is de-energized before connecting a meter in continuity mode. If you cannot establish this safely, stop and seek qualified assistance.
2. **Record the existing connections.** Photograph the wiring or make a clear note of which lead is attached to each terminal. This helps preserve the original connection information without treating wire position as proof of terminal identity.
3. **Consider circuit paths.** When the switch is connected to other components, those paths may affect a continuity reading. Where practical, disconnect at least one lead from the switch so the measurement is less likely to include an alternate path. Keep the disconnected lead identified and isolated from the test points.
4. **Set up the meter.** Select continuity mode according to the meter’s instructions. Touch the probes together and note the meter’s response. This confirms that the meter and probes respond before you test the switch; it does not verify the switch itself.
5. **Identify accessible terminals.** Use the markings or exact switch documentation if available. If terminals are unmarked, label them temporarily as A, B, and C for the pair-by-pair comparison. Do not assign COM based on terminal location or wire color alone.

Continuity mode reports whether the meter detects a conductive path under its test conditions. The precise indication varies by meter, so use its instructions rather than assuming that a beep or display value has the same meaning on every instrument. Keep the actuator state and terminal pair consistent as you compare readings.

## Test terminal pairs in both actuator states

For a switch believed to be a three-terminal changeover type, test every unique terminal pair in the released state, then repeat the same pairs with the actuator operated. Record the pair and the meter result each time. If the actuator cannot be moved safely or does not reach the intended state, the comparison may not identify the contact relationship reliably.

1. With power disconnected and the test lead isolated where practical, leave the actuator released. Place the probes on one terminal pair and record whether the meter indicates continuity. Repeat for the other pairs: A-B, A-C, and B-C when the three terminals are labeled A, B, and C.
2. Move the actuator to its operated state using its normal mechanical movement, without forcing it beyond its permitted travel. Repeat the same pair measurements and record the results. The point is to compare the same pairs across states, not to rely on one reading.
3. Look for the terminal that changes its continuity relationship between the other two terminals. In a functioning changeover pattern, one pair is continuous in one state while the alternate pair is continuous in the other state. The terminal shared by those two pairs is the candidate COM.
4. Compare the candidate pattern with the exact device markings or documentation. Confirm which contact is identified as NO and which as NC at the documented reference state. Do not use the observed pattern alone to override a device diagram or to infer a terminal’s electrical role in the equipment.

For a typical changeover switch, COM-to-NC is continuous and COM-to-NO is open in the released reference state; when the actuator operates, the expected relationships reverse. The actual reference state and pattern must be confirmed for the specific switch. A switch may use a different arrangement, and a test that does not show this pattern is not enough by itself to establish that the switch is defective.

## Read the continuity results without overdiagnosing

A pattern that alternates between the two pairs supports the identification of a common terminal in a changeover arrangement. For example, if A-B is continuous while released and A-C is continuous while operated, A is the candidate common terminal. This example describes the relationship only; it does not identify a particular terminal layout or guarantee the NO and NC labels without the switch’s reference state and documentation.

If a pair remains open in both states, check whether the probes are making contact, whether a lead remains connected to circuitry that could affect the reading, and whether the actuator reached the intended state. Also check whether the switch is actually a changeover type. A persistent open reading may be a useful finding, but it does not alone prove a contact failure or identify the cause.

If a pair shows continuity in both states, first consider whether another circuit path remains connected and whether the meter is contacting the intended terminals. Then compare the full set of pair readings across both states with the exact switch diagram. A single persistent reading cannot establish which terminal is COM or show that the switch is faulty.

Intermittent or unstable results also need context. Check that the probes remain in contact and that the actuator is held in a repeatable state. If the reading changes as the actuator moves, record the states and conditions rather than treating a momentary indication as a definitive diagnosis. The continuity comparison concerns the isolated switch contact relationship; it does not prove the wiring, control logic, or complete equipment circuit is functioning correctly.

### Related guides

- [automated guided vehicle guard interlock micro switch intermittent operation](/guides/automated-guided-vehicle-guard-interlock-micro-switch-intermittent-operation/)
- [assembly robot travel limit micro switch failure causes](/guides/assembly-robot-travel-limit-micro-switch-failure-causes/)
- [air compressor travel limit micro switch troubleshooting](/guides/air-compressor-travel-limit-micro-switch-troubleshooting/)
- [boom lift travel limit micro switch symptoms](/guides/boom-lift-travel-limit-micro-switch-symptoms/)

## Confirm terminal identity when readings differ

When the observed pattern does not match the expected changeover pattern, consult the exact switch markings and documentation. The documented connection diagram and terminal markings take precedence over generic assumptions about physical layout. Use the connection diagram, terminal marking, circuit function, and permissible load documented for the exact switch and equipment; do not infer these from a generic terminal arrangement.

The mismatch may mean the switch is not a changeover type, the actuator did not reach the relevant switching point, or the measurement was affected by probe contact or an alternate circuit path. These are possibilities to check, not conclusions from the continuity reading alone. A test result that differs from the diagram should remain unresolved until the switch type, state, isolation, and terminal identities are confirmed.

This procedure identifies a candidate COM terminal by comparing contact relationships in two actuator states. It cannot establish suitability for a load, diagnose unrelated wiring, or prove that the full equipment assembly is operational. **Micro switch COM terminal testing** is conclusive only to the extent that the switch configuration, isolation, actuator states, and documented terminal references are known. If safe isolation cannot be established or terminal identity remains unclear, stop and seek qualified assistance.

## Sources and references

- Defense Logistics Agency ASSIST: [MIL-PRF-8805K: Switches and Switch Assemblies, Sensitive, Snap Action, General Specification For](https://quicksearch.dla.mil/qsDocDetails.aspx?ident_number=7196){: rel="nofollow noopener noreferrer" }
- Occupational Safety and Health Administration: [29 CFR 1910.333: Selection and Use of Work Practices](https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.333){: rel="nofollow noopener noreferrer" }
- Wikipedia: [Miniature snap-action switch](https://en.wikipedia.org/wiki/Miniature_snap-action_switch){: rel="nofollow noopener noreferrer" }
