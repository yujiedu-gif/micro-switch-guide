---
title: "Boom lift end of stroke micro switch NO and NC terminals: contact states and checks"
description: "boom lift end of stroke micro switch NO and NC terminals: Understand the operating idea, essential terminology, practical checks, limitations, and."
date: 2026-10-07 09:00:00 +0800
category: Applications
tags:
  - boom lift end of stroke micro switch NO and NC terminals
  - micro switches
  - Applications
author: editorial_team
---

A **boom lift end of stroke micro switch NO and NC terminals** should be understood from the switch’s own contact diagram and reference state, not from a generic assumption about how a lift is wired. Normally open and normally closed describe contact relationships when the switch actuator is released; they do not, by themselves, say what the lift controller will do. To verify those contacts, isolate the equipment according to applicable requirements and compare continuity readings in the released and actuated states with the exact switch documentation.

The component-level check answers whether the contacts change state as documented. It does not establish that the switch is correctly adjusted, that its wiring is intact, or that the lift will stop as intended. Those are separate checks that depend on the equipment’s approved service information.

## Boom lift end of stroke micro switch NO and NC terminals: what the labels mean

Normally open (NO) and normally closed (NC) describe a contact’s relationship to the common terminal in the switch’s unactuated, released state. In a documented changeover contact, the common terminal is often labeled COM, with separate NO and NC terminals. In the released state, the common-to-NC path is closed and the common-to-NO path is open. When the actuator operates the switch, the contact paths change: the common-to-NO path closes and the common-to-NC path opens.

These labels describe the switch contacts, not current flow through the complete lift circuit. Whether a controller sees an input, changes an output, or stops motion depends on the actual circuit and control logic. A terminal marked NO does not inherently mean “motion enabled,” and NC does not inherently mean “motion stopped.” The lift’s circuit diagram and documented function are needed to interpret those effects.

Confirm the terminal arrangement on the actual component before testing or tracing conductors. A general changeover-contact diagram may show COM, NO, and NC, but a particular device may use different markings or a different arrangement. Use its exact schematic and terminal labels; do not identify terminals by physical position or appearance alone. The equipment diagram is also needed to determine how the switch is connected in the lift.

The useful reference is therefore two-part: identify the switch’s released-state contacts from its documentation, then confirm whether those contacts change when the actuator is operated. Keep that component-level result separate from the question of how the lift interprets the change.

## How end-of-stroke actuation changes the micro switch contacts

At an end of travel, a mechanical part of the equipment may move the micro switch actuator. When actuator movement reaches the switch’s operating point, the contacts change state as defined by the switch documentation. For a changeover contact, the released common-to-NC path opens and the common-to-NO path closes when operated. This explains the switch’s contact action; it does not identify which boom movement or machine function the contact controls.

The position at which the equipment engages the actuator is an installation matter as well as a switch matter. The switch’s operating point and any permitted movement beyond that point depend on the particular switch and installation. Do not assume a universal travel distance, operating position, or adjustment for boom lifts. The supplied component information and approved equipment service information must establish the relevant conditions for the exact installation.

Contact operation also does not prove that the lift’s end-of-travel function is working. A functioning switch can still be connected incorrectly, have a problem elsewhere in its circuit, or be interpreted differently by the controller than a reader might expect from NO or NC alone. Conversely, a machine symptom does not by itself establish that the switch contacts are faulty. The switch’s state change and the machine’s response are related by the equipment’s wiring and control design, which must be checked independently.

For this reason, use the physical end-of-stroke context only to identify the intended mechanical interaction. Do not infer a particular normal position, stopping action, contact arrangement, or controller strategy from the fact that a lift has an end-of-stroke switch. The exact switch marking, wiring diagram, and equipment documentation set those boundaries.

## Verify NO and NC continuity with power isolated

A continuity check is a component-level test of the switch in defined actuator states. Follow applicable equipment isolation and qualification requirements before accessing the switch. Prevent unintended movement using the equipment’s approved procedures. If the equipment cannot be safely isolated or positioned, do not proceed with the check; use qualified service support.

1. **Identify the exact switch and terminals.** Use the switch’s markings and documentation to locate the relevant contacts and establish which state is released and which is actuated. Do not rely on terminal position or a generic diagram.
2. **Isolate the switch from misleading circuit paths.** With power isolated, disconnect or otherwise isolate the switch circuit as needed so connected components or parallel paths do not affect the continuity reading. Follow the equipment’s service information for access and disconnection.
3. **Check the released state.** With the actuator released, measure the documented contact pairs. For a documented COM/NO/NC changeover arrangement, the expected reference is continuity from COM to NC and no continuity from COM to NO.
4. **Check the actuated state.** Operate the actuator only within the conditions permitted by the switch and equipment documentation. Measure the same contact pairs again. The expected change for that changeover arrangement is no continuity from COM to NC and continuity from COM to NO.
5. **Compare, then restore according to procedure.** Compare both readings with the exact switch documentation and equipment service information. Restore any disconnected connections only under the applicable procedure. Do not use an isolated reading as proof that the installed circuit or lift function is safe or correct.

The stated continuity pattern applies to a documented changeover contact and the specified released and actuated states. If the component has different markings, the documentation controls; do not force the COM/NO/NC pattern onto an undocumented device. A reading that differs from the documented pattern is a reason to investigate the switch and test setup, not by itself a complete diagnosis of the lift.

### Related guides

- [ball screw actuator home position micro switch replacement](/guides/ball-screw-actuator-home-position-micro-switch-replacement/)
- [bottling machine end of stroke micro switch](/guides/bottling-machine-end-of-stroke-micro-switch/)
- [automated guided vehicle home position micro switch location](/guides/automated-guided-vehicle-home-position-micro-switch-location/)
- [accelerator pedal position stop micro switch operating force](/guides/accelerator-pedal-position-stop-micro-switch-operating-force/)

## Separate a switch fault from wiring or controller behavior

If the isolated switch readings match its documentation in both states, that result supports only the conclusion that the tested contacts changed as documented under those test conditions. It does not verify the conductors, connectors, controller input, installation position, or end-of-travel response. Continue only through the approved service information for the specific equipment, treating each part of the signal path as a separate diagnostic stage.

If a reading does not match, first confirm that the correct terminals and actuator states were tested and that the switch was isolated from other circuit paths as needed. Then compare the result with the exact component documentation. The evidence available here does not establish model-specific repair steps, adjustment values, or replacement requirements, so those should not be inferred from a continuity result.

Do not use terminal labels alone to conclude that a boom lift should stop, continue, or respond in a particular way. That behavior depends on the lift’s actual wiring and controller logic. A correct switch contact change can coexist with a wiring or controller issue, while a controller symptom can have causes outside the switch. Likewise, a component test cannot establish that the complete lift system is functioning properly.

Use the switch schematic to identify the contact states, verify them with power isolated in the documented released and actuated positions, and use the equipment’s approved information to interpret the connected circuit. If safe isolation, access, or positioning is uncertain, stop and seek qualified service support. The **boom lift end of stroke micro switch NO and NC terminals** identify contact relationships; they do not, by themselves, define the lift’s stopping behavior.

## Sources and references

- Defense Logistics Agency ASSIST: [MIL-PRF-8805K: Switches and Switch Assemblies, Sensitive, Snap Action, General Specification For](https://quicksearch.dla.mil/qsDocDetails.aspx?ident_number=7196){: rel="nofollow noopener noreferrer" }
- Occupational Safety and Health Administration: [29 CFR 1910.333: Selection and Use of Work Practices](https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.333){: rel="nofollow noopener noreferrer" }
- Wikipedia: [Miniature snap-action switch](https://en.wikipedia.org/wiki/Miniature_snap-action_switch){: rel="nofollow noopener noreferrer" }
