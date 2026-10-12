---
title: "How a dual micro switch works"
description: "dual micro switch: Understand the operating idea, essential terminology, practical checks, limitations, and evidence needed for careful selection,."
date: 2026-07-25 09:00:00 +0800
category: Basics
tags:
  - dual micro switch
  - micro switches
  - Basics
author: editorial_team
---

A **dual micro switch** arrangement uses two micro switches together, but the phrase does not identify one standard package or circuit. The switches may be mounted separately and operated independently, or a shared lever or mechanism may move both. That mechanical arrangement does not, by itself, establish how the switches are electrically connected or when their contacts change state.

To understand the arrangement, consider each switch as a separate component. Check how its actuator moves, identify its terminals from markings or documentation, and establish its contact state on its own. A shared actuator may coordinate movement, but it does not prove that the switches share terminals, switch at the same point, or change state together.

## What a dual micro switch means

A dual micro switch means two micro switches used together. It does not guarantee a single housing, a particular terminal layout, or a standard electrical relationship between the switches. Construction and linkage can vary, so treat the mechanical and electrical questions separately.

With **independent actuation**, each switch has an actuator that can be operated without moving the other. Their states can therefore be checked separately, and movement of one actuator does not establish the state of the other.

With **shared mechanical actuation**, a lever or other mechanism moves both switches. The link changes how force or movement reaches the actuators. It does not, by itself, connect the electrical contacts. Nor does shared movement establish that both switches change state at the same moment. Their switching points and contact forms may differ.

This distinction matters when interpreting the arrangement. A physical link is evidence of coordinated movement, not proof of a shared electrical circuit or identical behavior. Conversely, two switches located together are not necessarily mechanically linked. Identify the actual actuators and terminal markings before interpreting either relationship.

## How a dual micro switch changes state

Each switch responds to movement at its own actuator. In a snap-action mechanism, contact action is defined as movement in which the speed of the moving contacts is relatively independent of the speed of the actuating mechanism. This describes the contact action; it does not specify a particular travel distance, switching point, or timing relationship for a pair of switches.

For terminal markings that use changeover terminology, **COM** means common, **NC** means normally closed, and **NO** means normally open. These names describe terminal roles, but do not establish the exact layout or behavior of an unidentified device. Check the device schematic or documentation rather than assuming that every switch uses the same arrangement.

As an actuator moves, the contact state of that switch may change. In a two-switch arrangement, the switches may change state simultaneously, sequentially, or independently, depending on the mechanism. A shared lever alone does not show which behavior applies. It also does not establish that the switches have identical contact forms or switching points.

When the actuator is released after operation, the release force is the force or torque to which force on the actuator must be reduced to permit the contacts to return to the unoperated position. This definition describes the return condition; it does not provide a value for a particular switch or establish how a second switch will respond. Determine each switch’s state from its own actuator and contacts.

## How to check each switch separately

Use a de-energized continuity check to establish the contact state of each switch. Disconnect power and isolate the circuit before testing. A continuity result from a connected circuit may reflect other electrical paths, so do not treat it as proof of a switch’s own contact state. This procedure is for checking the switches individually, not for determining how a particular circuit is wired.

1. **Identify the two switches and their terminals.** Use the markings on each switch or its documentation to identify terminals. Where a schematic is available, use it to confirm the terminal meanings for that device. Do not assign COM, NO, or NC based only on physical position or the appearance of the pair.
2. **Check the first switch in its released position.** With power disconnected and the circuit isolated, test continuity between the identified terminals and record the result. Note the actuator position so the observation is tied to a known state.
3. **Operate that actuator and check again.** Move the first actuator through its available travel, then record continuity at the same terminals in the actuated position. Do not use the movement of a linked actuator as a substitute for observing this switch’s state.
4. **Repeat for the second switch.** Test and record the second switch separately, in its released and actuated positions. If the switches have a shared mechanism, observe which actuator moves and which contact state is being measured rather than assuming that the first result applies to both.
5. **Compare the records.** Compare each switch’s released and actuated results, then compare the two switches with one another. The comparison can show whether their observed states change at the same or different points during the tested movement. One switch’s result does not establish the other’s state.

If terminal identification is unclear, the evidence does not establish which contacts are being tested. Resolve that identification from the markings or documentation before interpreting a continuity result. Likewise, a check of one pair of terminals does not establish the state of every contact in a switch.

### Related guides

- [touch micro switch](/guides/touch-micro-switch/)
- [no nc micro switch](/guides/no-nc-micro-switch/)
- [normally open micro switch](/guides/normally-open-micro-switch/)
- [float switch mechanism micro switch contact rating](/guides/float-switch-mechanism-micro-switch-contact-rating/)

## Common misunderstandings about a dual micro switch

**“They move together, so they share contacts.”** A shared actuator is a mechanical relationship. It does not prove an electrical connection between the switches. Establish the terminal arrangement for each switch separately.

**“One output changed, so both switches changed state.”** A result from one switch cannot establish the other switch’s contact state. Test each switch at its own identified terminals in both released and actuated positions.

**“A shared lever means both switches switch at once.”** Shared movement does not establish identical switching points or timing. The pair may change state simultaneously or sequentially, and separate actuation may allow independent changes. Observe and record each switch rather than inferring timing from the linkage.

**“The terminal positions tell me which contact is COM, NO, or NC.”** Terminal layout is not established by a general description of a dual arrangement. Use markings or documentation, and verify the exact device schematic where applicable.

The reliable interpretation is component by component: identify each switch, establish whether its actuator is independent or linked, and verify its contact state separately under de-energized conditions. A dual micro switch describes two switches used together; the physical link and electrical relationship must each be established from the specific arrangement.

## Sources and references

- Defense Logistics Agency ASSIST: [MIL-PRF-8805K: Switches and Switch Assemblies, Sensitive, Snap Action, General Specification For](https://quicksearch.dla.mil/qsDocDetails.aspx?ident_number=7196){: rel="nofollow noopener noreferrer" }
- Wikipedia: [Miniature snap-action switch](https://en.wikipedia.org/wiki/Miniature_snap-action_switch){: rel="nofollow noopener noreferrer" }
