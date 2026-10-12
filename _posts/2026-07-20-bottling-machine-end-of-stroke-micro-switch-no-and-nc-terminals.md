---
title: "bottling machine end of stroke micro switch NO and NC terminals: How to Verify Contact States"
description: "bottling machine end of stroke micro switch NO and NC terminals: Understand the operating idea, essential terminology, practical checks, limitations, and."
date: 2026-07-20 09:00:00 +0800
category: Applications
tags:
  - bottling machine end of stroke micro switch NO and NC terminals
  - micro switches
  - Applications
author: editorial_team
---

A bottling machine’s end-of-stroke switch can be checked by comparing its contact continuity before and after the mechanism actuates it. The **bottling machine end of stroke micro switch NO and NC terminals** must be identified from the machine’s wiring diagram and the exact switch’s markings or documentation, not guessed from terminal position. The switch’s contact state is only one part of the signal path: it does not, by itself, show how the controller interprets the input.

## What NO and NC mean on a micro switch

Normally open (NO) and normally closed (NC) describe contact relationships in the switch’s unactuated, or released, state. In a generic changeover contact, a common (COM) terminal connects to NC while the switch is released, and to NO when the switch is actuated. The names refer to that reference state, not necessarily to what a machine operator sees at a particular moment.

A micro switch may use a changeover contact, but its exact terminal arrangement cannot be established from a generic layout. A device’s markings or schematic control, and the machine’s wiring diagram identifies which terminals are relevant to the endpoint circuit. Use those documents rather than assuming that a terminal’s physical location or a familiar label proves its function.

For a changeover contact, the expected continuity relationship is therefore relative: COM-to-NC is closed in the released state, and COM-to-NO is closed after actuation. This describes the contact mechanism, not the controller’s displayed or interpreted input state. It also does not establish which contact the machine uses to signal the end of a stroke. That depends on the documented circuit.

## bottling machine end of stroke micro switch NO and NC terminals: What changes at stroke end

At the machine’s designed stroke endpoint, the mechanism should reach the position that actuates the switch. The relevant sequence is mechanical: the mechanism moves toward its defined endpoint, contacts or otherwise operates the switch actuator as designed, and the switch’s contact relationship changes. For a changeover contact, that means the common terminal changes connection from the NC side to the NO side. The exact endpoint and how the mechanism operates the switch are machine-specific; do not infer them from switch terminology alone.

Which contact carries the endpoint signal is also a machine-specific design choice. The circuit may use the NO or NC contact, and the switch’s contact transition does not reveal how the rest of the circuit is wired. Consult the machine wiring diagram and the exact switch documentation to identify the intended terminals and circuit function. Do not treat either contact as a universal end-of-stroke signal.

A machine may appear to reach its endpoint without the controller indicating the expected state. That observation alone does not show whether the switch, wiring, or control interpretation is responsible. First distinguish the switch’s mechanical transition and contact continuity from the downstream signal. This keeps a contact-state check from turning into an unsupported conclusion about the entire machine.

## How to verify the micro switch terminals safely

Use the machine’s applicable safety procedure and required de-energization and qualification requirements before accessing or testing the switch. Do not probe an energized circuit as a generic diagnostic step. Identify the switch and relevant terminals using the machine wiring diagram, the terminal markings, and the exact switch documentation. If those sources do not establish the terminal identity or permissible test method, treat that information as unresolved and follow the approved service procedure.

For a continuity comparison, the circuit must be safely de-energized, and the switch should be isolated as appropriate under the applicable procedure. Check the identified contact pairs in the released position, then compare them with the readings when the mechanism places the switch in its actuated position. For a documented COM-NO-NC changeover contact, the expected pattern is continuity from COM to NC when released, then continuity from COM to NO when actuated. Record what was tested and the position of the mechanism; do not assume that an unverified terminal pair follows this pattern.

The test should distinguish two mechanical states: released and actuated at the designed stroke endpoint. Avoid forcing the mechanism beyond its intended position or improvising a test method. If it is not possible to establish the safe access, isolation, terminal identification, or test conditions from applicable documentation and procedure, stop and use the machine’s approved diagnostic process rather than guessing.

## Why the controller signal may not match a simple NO/NC assumption

Contact continuity describes the switch contacts under the tested conditions. It does not, on its own, establish the controller input state or whether the machine has recognized the stroke endpoint. The signal seen by a controller also depends on how the circuit is wired, the input configuration, and machine-specific control logic. Those details are not determined by the NO or NC label.

If the measured contacts change state but the machine’s behavior or indication does not match expectations, compare the measured terminal pair and mechanical state with the wiring diagram and the applicable qualified service procedure. Do not infer that the controller should interpret an open or closed contact in one universal way. Resolving the input interpretation may require machine-specific information beyond a continuity check, and programming or changing end-of-stroke logic is outside the scope of this contact verification.

Keep the two questions separate: did the identified switch contacts change continuity between released and actuated positions, and does the documented machine circuit use that change as expected? The first is a bounded contact check. The second depends on the circuit and configuration, so it must be evaluated against the machine’s documentation and approved procedure.

### Related guides

- [ball screw actuator home position micro switch replacement](/guides/ball-screw-actuator-home-position-micro-switch-replacement/)
- [bottling machine end of stroke micro switch](/guides/bottling-machine-end-of-stroke-micro-switch/)
- [automated guided vehicle home position micro switch location](/guides/automated-guided-vehicle-home-position-micro-switch-location/)
- [accelerator pedal position stop micro switch operating force](/guides/accelerator-pedal-position-stop-micro-switch-operating-force/)

## What to record when results differ from the expected stroke-end state

If results differ from the documented expectation, record the terminal identification source, the contact pairs tested, and continuity in both the released and actuated positions. Note the mechanical state during each reading, including whether the switch was actuated at the machine’s designed stroke endpoint. This makes the observation specific and helps distinguish a contact-state result from a controller interpretation.

Do not bypass the switch or change control logic to force an endpoint signal. A continuity result that conflicts with an expected state should be compared with the exact switch documentation, machine wiring diagram, and approved diagnostic procedure. If those references do not resolve the discrepancy, defer to the machine’s qualified service process rather than treating a generic NO/NC pattern as proof of a fault or a repair.

The useful conclusion is limited but clear: verify the identified contacts in released and actuated states under the applicable de-energized procedure, then interpret those results using the machine’s circuit documentation. The bottling machine end of stroke micro switch NO and NC terminals describe contact relationships; they do not alone establish the controller’s response.

## Sources and references

- Defense Logistics Agency ASSIST: [MIL-PRF-8805K: Switches and Switch Assemblies, Sensitive, Snap Action, General Specification For](https://quicksearch.dla.mil/qsDocDetails.aspx?ident_number=7196){: rel="nofollow noopener noreferrer" }
- Occupational Safety and Health Administration: [29 CFR 1910.333: Selection and Use of Work Practices](https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.333){: rel="nofollow noopener noreferrer" }
- Wikipedia: [Miniature snap-action switch](https://en.wikipedia.org/wiki/Miniature_snap-action_switch){: rel="nofollow noopener noreferrer" }
