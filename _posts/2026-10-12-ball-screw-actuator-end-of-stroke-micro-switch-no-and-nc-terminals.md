---
title: "ball screw actuator end of stroke micro switch NO and NC terminals"
description: "ball screw actuator end of stroke micro switch NO and NC terminals: Understand the operating idea, essential terminology, practical checks, limitations,."
date: 2026-10-12 16:49:35 +0800
category: Applications
tags:
  - ball screw actuator end of stroke micro switch NO and NC terminals
  - micro switches
  - Applications
author: editorial_team
---

A **ball screw actuator end of stroke micro switch NO and NC terminals** identify alternative contact paths that change state when the switch is actuated. Checking those paths can confirm the switch’s contact behavior, but the terminal names do not specify how a controller interprets its input. Verify the exact switch diagram and equipment wiring rather than inferring connections from terminal position or wire color.

This guide follows the changeover-contact pattern: with the switch unactuated, COM is connected to NC and open to NO; when actuated, COM changes over to connect to NO and open from NC. The exact device schematic controls if its arrangement differs. A continuity check should be performed with electrical power isolated and in accordance with applicable deenergization and qualification requirements.

## What the ball screw actuator end of stroke micro switch NO and NC terminals mean

COM, NO, and NC are contact-terminal labels, not controller voltage labels. In a generic changeover contact, **COM** means common, **NO** means normally open, and **NC** means normally closed. These names describe the contact relationship in the switch’s normal, unactuated state. They do not, by themselves, identify a controller’s signal polarity or establish the voltage present at any terminal.

For a standard changeover arrangement, the unactuated continuity pattern is:

| Terminal pair | Switch unactuated |
|---|---|
| COM–NC | Closed; continuity is present |
| COM–NO | Open; continuity is absent |

When the switch actuator is moved far enough to actuate the switch, the contact changes over:

| Terminal pair | Switch actuated |
|---|---|
| COM–NC | Open; continuity is absent |
| COM–NO | Closed; continuity is present |

The state change is relative to the switch’s own unactuated and actuated conditions. It is not a statement about whether a controller reads a high or low signal, considers the limit active, or stops motion. Those interpretations depend on the wiring and input configuration, which must be checked separately.

Treat this pattern as a general changeover-contact description, not proof that every switch or actuator assembly uses that arrangement. A particular device may have different contacts or markings. Its terminal identification and schematic take precedence over generic NO and NC terminology. Before tracing conductors or testing, use the exact switch documentation and the equipment connection diagram. Do not infer terminal identity from physical layout alone.

## How the switch changes state at the travel limit

The electrical change begins with a mechanical event: a moving part of the actuator reaches and moves the micro switch’s actuator. In an end-of-stroke arrangement, the switch is positioned so that movement at the configured travel limit causes that actuation. The switch then changes the COM contact path according to its contact arrangement. This describes the switch reporting a physical change; it does not establish how a controller uses that change.

The mounting position matters. If the switch is not reached at the intended point, it may not change state when expected. If the mechanism reaches a hard stop before sufficient switch actuation, the actuator may encounter that stop without the intended limit indication. Conversely, a switch can change state before the actuator reaches its final mechanical position. The actual relationship depends on the equipment’s layout and adjustment; the terminal labels alone do not establish it.

Overtravel is the distance or angle between the operating position and the extreme position to which the actuator may be moved. In this context, account for the available movement after the switch’s operating position rather than assuming that any further movement is acceptable. The permitted amount and the mechanism’s limits must come from the exact switch and equipment documentation. Do not use a generic value to set a travel limit.

Not every ball screw actuator necessarily uses a micro switch for its end of stroke. Confirm that the equipment documentation identifies a switch and shows how it is mounted and connected. Keep three questions separate: whether the mechanism physically actuates the switch, which contact path is closed, and what the controller does with the resulting circuit state. A continuity check can help answer the second question, but cannot alone establish the first under operation or the third in the controller.

## How to verify NO and NC continuity safely

Use the equipment and switch documentation before disconnecting conductors or testing. Isolate electrical power and follow applicable deenergization and qualification requirements. Do not use a continuity or resistance measurement as a live-circuit check. If the documentation does not establish how to make the switch safe to test, do not guess at a procedure.

With power isolated, use a multimeter’s continuity or resistance mode to check the relevant contact pairs. Identify COM, NO, and NC from the exact switch diagram or markings. In the unactuated condition, check COM–NO and COM–NC. For a standard changeover contact, COM–NO should be open and COM–NC should be closed. Record what the meter indicates for each pair rather than treating a sound from a continuity function as a controller signal.

If it is safe to do so, actuate the switch manually according to the device documentation and repeat the measurements. For the standard changeover pattern, COM–NO should then be closed and COM–NC open. Release the actuator and check whether the contacts return to their unactuated pattern. Do not force the actuator beyond its documented movement or infer that manual operation reproduces the actuator’s installed travel geometry.

Compare the observed contact states with the exact switch schematic. If results do not match, first verify that the terminals were identified correctly, that the switch was in the intended unactuated or actuated condition, and that the test was made as the documentation specifies. The evidence supplied here does not establish expected meter readings for every device, nor does it determine whether connected equipment should remain attached during a test. Follow the exact device procedure rather than making those assumptions.

A de-energized contact check verifies contact continuity under the conditions tested. It does not prove that the controller will interpret the circuit as a limit, that the switch is mounted at the correct travel position, or that the complete actuator will stop as intended. Keep contact verification separate from controller-input verification and from mechanical limit validation.

### Related guides

- [ball screw actuator home position micro switch replacement](/guides/ball-screw-actuator-home-position-micro-switch-replacement/)
- [bottling machine end of stroke micro switch](/guides/bottling-machine-end-of-stroke-micro-switch/)
- [automated guided vehicle home position micro switch location](/guides/automated-guided-vehicle-home-position-micro-switch-location/)
- [accelerator pedal position stop micro switch operating force](/guides/accelerator-pedal-position-stop-micro-switch-operating-force/)

## Wiring and end-stop checks before operation

Match conductors to the intended COM–NO or COM–NC path using the equipment wiring diagram and the controller input requirements. Do not choose a contact path based only on a general assumption about which state should mean “limit reached.” The same physical contact state can be interpreted differently depending on how the circuit is wired and how the controller input is configured. Terminal labels describe contacts, not controller logic.

Before operation, compare the installed wiring with the documented connections and check that terminations are secure. Confirm the switch is aligned with the moving mechanism and that the mechanism actuates it at the intended travel limit. The switch should operate before the actuator reaches a damaging hard stop. A successful continuity check alone does not demonstrate that the switch is positioned to do so; that relationship must be checked against the equipment’s documented arrangement and approved procedure.

If the contact measurements disagree with the device diagram, or the mechanism does not actuate the switch as documented, do not substitute an assumed wiring interpretation. Resolve the discrepancy using the exact device and equipment information. Avoid changing controller input logic as a way to compensate for an unverified terminal connection or mechanical position.

Restore power only after the wiring and enclosure are safe and the required checks are complete. Then verify limit response using the equipment’s approved procedure. That operational check addresses the installed system, while the isolated continuity check addresses the switch contacts. **For a ball screw actuator end of stroke micro switch NO and NC terminals**, the reliable verification path is to establish the exact terminal diagram, confirm the unactuated and actuated contact states, and separately validate the documented mechanical and controller behavior.

## Sources and references

- Defense Logistics Agency ASSIST: [MIL-PRF-8805K: Switches and Switch Assemblies, Sensitive, Snap Action, General Specification For](https://quicksearch.dla.mil/qsDocDetails.aspx?ident_number=7196){: rel="nofollow noopener noreferrer" }
- Occupational Safety and Health Administration: [29 CFR 1910.333: Selection and Use of Work Practices](https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.333){: rel="nofollow noopener noreferrer" }
- Wikipedia: [Miniature snap-action switch](https://en.wikipedia.org/wiki/Miniature_snap-action_switch){: rel="nofollow noopener noreferrer" }
