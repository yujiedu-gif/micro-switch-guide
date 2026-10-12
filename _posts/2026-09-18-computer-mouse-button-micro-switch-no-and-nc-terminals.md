---
title: "computer mouse button micro switch NO and NC terminals"
description: "computer mouse button micro switch NO and NC terminals: Understand the operating idea, essential terminology, practical checks, limitations, and evidence."
date: 2026-09-18 09:00:00 +0800
category: Basics
tags:
  - computer mouse button micro switch NO and NC terminals
  - micro switches
  - Basics
author: editorial_team
---

A computer mouse button micro switch NO and NC terminals describe the switch’s contact states, not the meaning of a click to the mouse controller. NO is open with the switch actuator at its unpressed rest state and closes when the actuator is pressed. NC is closed at rest and opens on actuation. To identify the contacts, check the specific switch’s markings or diagram, then compare terminal pairs with the switch unpowered and isolated from powered circuitry. Do not assume every mouse switch exposes both contacts: a two-terminal design may provide only one contact pair, while a changeover design may provide three terminals.

## What NO and NC mean on a computer mouse button micro switch NO and NC terminals

NO and NC name contact behavior relative to a defined mechanical reference state. For a computer mouse button micro switch, use the actuator’s unpressed, unactuated rest state as that reference. The mouse button may move the actuator, but the label describes the switch contacts themselves.

At rest, the normally open contact pair is open. When the actuator is pressed and the switch changes state, that pair closes. The normally closed contact pair has the opposite pattern: it is closed at rest and opens when the actuator is pressed. These terms describe whether the specified contacts are connected in those states. They do not, by themselves, establish what signal the mouse circuit sees or whether a click is registered.

Keep the reference state attached to the labels. Saying only that a contact is “open” or “closed” is incomplete unless the actuator state is clear. For identification, compare the same terminal pair first at rest and then while the switch is actuated. The state change, rather than the physical location of a pin or the apparent effect of a mouse click, is the useful evidence.

## Two-terminal and three-terminal mouse switch configurations

A mouse button switch may expose only two terminals. That arrangement provides one contact pair; it does not necessarily make both the normally open and normally closed contacts available to the person identifying terminals. Do not infer that an NC terminal exists merely because NO/NC terminology applies to changeover switches.

A three-terminal changeover switch may expose a common terminal, an NO terminal, and an NC terminal. In that arrangement, the common terminal connects to one of the other contacts at rest and changes connection as the actuator moves. Which pair is closed at rest, and which pair closes on actuation, must be established for the actual switch.

Terminal count and contact arrangement are not reliably determined by package shape or by how the switch is wired on a mouse circuit board. Check the specific device’s terminal marking or connection diagram where available. If those markings do not resolve the contact arrangement, compare the isolated switch’s terminal pairs in both actuator states. A physical pin’s location alone is not a dependable basis for assigning COM, NO, or NC.

This distinction also limits what can be concluded from a two-terminal reading. If only one pair is exposed, a change in its measured state can identify that pair’s behavior relative to rest and actuation. It does not reveal an unexposed contact or establish that the switch is a three-terminal changeover design.

## Identify the terminals with an unpowered continuity test

First disconnect the mouse from its power source and isolate the switch from powered circuitry before testing. The reading must concern the switch contacts, not a path through powered or connected circuitry. Use a continuity or resistance measurement and compare the same terminal pair with the actuator at rest, then pressed.

For a two-terminal switch, measure the available pair in both states. If the pair is open at rest and closes on actuation, it behaves as an NO pair. If it is closed at rest and opens on actuation, it behaves as an NC pair. This identifies the observed pair’s behavior; it does not establish the presence of another contact that the switch does not expose.

For a three-terminal changeover switch, compare the available terminal pairs in both states. The common terminal is the one that alternates continuity between the other two as the actuator moves. Record which pair is closed with the actuator at rest and which pair closes when it is pressed. The pair closed at rest is the NC path; the pair that closes on actuation is the NO path. Confirm this pattern on the actual isolated switch rather than assigning names based on pin position.

If readings are ambiguous, do not force a terminal assignment. Connected circuit paths can affect measurements if the switch is not isolated, and contact condition may also complicate interpretation. Recheck that the mouse is disconnected and that the switch is isolated from powered circuitry. If the measurement still does not clearly show the expected state change, leave the contact identification unresolved rather than inferring it from the mouse’s behavior.

### Related guides

- [dual micro switch](/guides/dual-micro-switch/)
- [touch micro switch](/guides/touch-micro-switch/)
- [no nc micro switch](/guides/no-nc-micro-switch/)
- [normally open micro switch](/guides/normally-open-micro-switch/)

## Interpret readings without confusing switch contacts with mouse logic

An NO contact closing during a button press establishes a switch-level contact change. It does not, by itself, establish how the mouse controller interprets that change or whether the mouse reports a click. The board connections and surrounding circuit affect device behavior, so mouse response is not a substitute for identifying the switch contacts.

Base terminal identification on the specific switch’s markings or diagram and, where needed, its unpowered contact readings at rest and while actuated. Use COM, NO, and NC only when the actual contact arrangement supports those designations. A two-terminal switch may expose only one pair, and the mouse’s wiring does not prove that an NC contact is available.

The useful conclusion is limited but clear: NO is open at the unpressed rest state and closes on actuation; NC is closed at rest and opens on actuation. Identify which contacts are present from the actual switch, and do not transfer that switch-level result into an assumption about the mouse controller. The phrase computer mouse button micro switch NO and NC terminals names contact behavior, not a universal terminal layout or a guarantee about mouse operation.

## Sources and references

- Defense Logistics Agency ASSIST: [MIL-PRF-8805K: Switches and Switch Assemblies, Sensitive, Snap Action, General Specification For](https://quicksearch.dla.mil/qsDocDetails.aspx?ident_number=7196){: rel="nofollow noopener noreferrer" }
- Occupational Safety and Health Administration: [29 CFR 1910.333: Selection and Use of Work Practices](https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.333){: rel="nofollow noopener noreferrer" }
- Wikipedia: [Miniature snap-action switch](https://en.wikipedia.org/wiki/Miniature_snap-action_switch){: rel="nofollow noopener noreferrer" }
