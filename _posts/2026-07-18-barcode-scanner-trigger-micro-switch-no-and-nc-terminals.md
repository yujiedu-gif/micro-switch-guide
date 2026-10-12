---
title: "barcode scanner trigger micro switch NO and NC terminals: How the contacts work"
description: "barcode scanner trigger micro switch NO and NC terminals: Understand the operating idea, essential terminology, practical checks, limitations, and."
date: 2026-07-18 09:00:00 +0800
category: Applications
tags:
  - barcode scanner trigger micro switch NO and NC terminals
  - micro switches
  - Applications
author: editorial_team
---

A **barcode scanner trigger micro switch NO and NC terminals** question is easiest to answer by separating the switch’s contact state from the scanner’s interpretation of that state. The labels NO and NC describe contacts relative to the switch’s unactuated, resting position. On a changeover switch, pressing the trigger transfers the common contact from one contact path to the other; releasing it restores the resting state. These labels alone do not identify the scanner’s complete wiring or tell you what electrical signal its controller recognizes as a trigger.

The exact switch’s markings and documentation control. Use its connection diagram, terminal marking, circuit function, and documented permissible load rather than inferring connections from terminal placement or appearance. The available information here does not establish the construction or rating of any particular scanner switch.

## What barcode scanner trigger micro switch NO and NC terminals mean

Normally open (NO) and normally closed (NC) are names for contact relationships in the switch’s unactuated state. In a generic changeover arrangement, **COM** means common, **NC** means normally closed, and **NO** means normally open. COM is the shared terminal in the changeover contact arrangement. The exact device schematic or markings must confirm that these labels apply to the switch being examined.

At rest, the COM-to-NC path is closed and the COM-to-NO path is open. “Normally” refers to this unactuated resting condition, not to a scanner’s usual powered state, a software setting, or the meaning assigned to a signal by the scanner controller. A trigger that is not pressed is therefore the reference condition for reading the generic labels.

A changeover switch may expose all three terminals, but do not assume every trigger switch does. A particular switch could have a different configuration, or its accessible connections may not match a generic three-terminal diagram. Verify its exact marking and documentation before identifying terminals. Physical position alone is not a reliable basis for deciding which connection is COM, NO, or NC.

## Contact states at rest, during a press, and after release

In a changeover contact, actuation transfers the common contact between NO and NC. The state trace below describes the generic relationship; use the exact switch documentation to confirm how the device operates.

| Trigger position | COM to NC | COM to NO | Meaning |
|---|---|---|---|
| Unpressed, at rest | Closed | Open | Resting contact relationship |
| Pressed, actuated | Open | Closed | Common contact has transferred to NO |
| Released, returned to rest | Closed | Open | Resting relationship is restored |

Thus, for this generic changeover arrangement, a press changes which path is closed, and release returns the contacts to their original resting relationship. The table describes contact continuity, not a voltage level, logic level, or scanner command. It also does not specify switching timing or other behavior beyond the stated transfer and return; consult the exact switch documentation for its operation.

The scanner’s controller determines how a contact change is interpreted. The switch can change from one contact path to another while the scanner treats that change according to its own input arrangement. It is not justified to infer from the NO or NC label alone that pressing produces an electrically high or low signal, that a particular path is active, or that the controller starts a scan. Those are scanner-circuit questions, not definitions of the terminal labels.

## How to verify the terminals with a continuity meter

Continuity testing can check contact behavior, but only when the switch is electrically isolated from the scanner circuit. Follow applicable deenergization and qualification requirements. Do not perform a continuity check on a powered circuit. If you cannot establish that the switch is deenergized and isolated, stop and obtain qualified assistance rather than relying on a meter reading.

A basic verification path is:

1. Identify the switch terminals from the exact device markings or schematic. Do not assign COM, NO, or NC based only on where a terminal sits physically.
2. Deenergize the relevant equipment and electrically isolate the switch from the scanner circuit before testing. An in-circuit reading may include paths through the scanner’s electronics rather than only through the switch.
3. Set up the continuity meter according to its instructions. With the trigger unpressed, check the identified COM-to-NC and COM-to-NO pairs. For the generic changeover relationship, COM-to-NC is closed and COM-to-NO is open at rest.
4. While the switch remains isolated, actuate the trigger mechanism and repeat both checks. For the generic changeover relationship, COM-to-NO is closed and COM-to-NC is open while actuated.
5. Release the trigger and check again. The generic relationship returns to COM-to-NC closed and COM-to-NO open.

This test checks whether the isolated contacts show the expected open/closed relationships in the states examined. It does not identify the scanner’s full pinout, establish how its electronics interpret the contact change, or establish that a switch is suitable for a load. Meter results taken through connected electronics can be misleading because other circuit paths may affect the reading. Use the exact switch documentation to resolve unexpected results; do not turn an uncertain reading into an assumed terminal assignment.

### Related guides

- [ball screw actuator home position micro switch replacement](/guides/ball-screw-actuator-home-position-micro-switch-replacement/)
- [bottling machine end of stroke micro switch](/guides/bottling-machine-end-of-stroke-micro-switch/)
- [automated guided vehicle home position micro switch location](/guides/automated-guided-vehicle-home-position-micro-switch-location/)
- [accelerator pedal position stop micro switch operating force](/guides/accelerator-pedal-position-stop-micro-switch-operating-force/)

## Why terminal labels do not reveal the full scanner circuit

NO, NC, and COM describe contact relationships for a changeover switch. They do not, by themselves, show which terminals are connected in the scanner, which input the controller monitors, or what event the controller associates with an input change. Scanner electronics, the switch configuration, and the wiring together determine how the trigger signal is interpreted.

Do not assume that a pressed trigger means a signal is electrically high, low, active, or connected to a particular supply. Nor do the generic labels prove that a particular scanner exposes all three changeover terminals. These conclusions require the exact scanner and switch circuit information, which is not established by terminal names alone.

Before altering wiring, trace the relevant connections using the scanner and switch documentation. Use the connection diagram, terminal marking, circuit function, and permissible load documented for the exact switch and equipment. The practical conclusion is limited but useful: on a verified changeover switch, COM-NC is closed at rest, COM-NO is closed during actuation, and release restores the resting relationship. Those contact states do not, on their own, reveal how the scanner interprets its trigger input.

This concludes the explanation of barcode scanner trigger micro switch NO and NC terminals.

## Sources and references

- Defense Logistics Agency ASSIST: [MIL-PRF-8805K: Switches and Switch Assemblies, Sensitive, Snap Action, General Specification For](https://quicksearch.dla.mil/qsDocDetails.aspx?ident_number=7196){: rel="nofollow noopener noreferrer" }
- Occupational Safety and Health Administration: [29 CFR 1910.333: Selection and Use of Work Practices](https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.333){: rel="nofollow noopener noreferrer" }
- Wikipedia: [Miniature snap-action switch](https://en.wikipedia.org/wiki/Miniature_snap-action_switch){: rel="nofollow noopener noreferrer" }
