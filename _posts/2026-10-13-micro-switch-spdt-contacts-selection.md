---
title: "micro switch SPDT contacts selection: How to Choose for a Circuit"
description: "micro switch SPDT contacts selection: Understand the operating idea, essential terminology, practical checks, limitations, and evidence needed for careful."
date: 2026-10-13 09:00:00 +0800
category: Selection Guides
tags:
  - micro switch SPDT contacts selection
  - micro switches
  - Selection Guides
author: editorial_team
---

SPDT describes a contact arrangement, not a complete circuit function. For a micro switch SPDT contacts selection, confirm what the switch documentation says about its terminals and contact states, then match the circuit’s actual electrical conditions and the mechanism’s movement to documented limits. The label alone does not establish that a switch suits a particular circuit or installation.

Treat selection as two separate checks: electrical compatibility and mechanical fit. Verify terminal identity from the applicable marking or schematic rather than terminal position or appearance. If a safe, isolated continuity check is appropriate, use defined actuator states and compare the readings with the documented contact arrangement. That check can clarify switch-terminal behavior, but it cannot establish installed wiring, load suitability, or the safety of the complete equipment.

## What SPDT contacts mean on a micro switch

SPDT means single-pole, double-throw: one common contact can connect to either of two contacts as the mechanism changes state. On a generic changeover contact, the terminals may be labeled COM, NO, and NC. Those names describe a contact arrangement; they do not, by themselves, tell you what a host machine or circuit will do.

Use COM, NO, and NC only when the particular switch’s documentation identifies those terminals. The exact device marking or schematic controls. Do not assign terminal identities from their physical positions, appearance, or a familiar-looking layout. If the documentation does not establish which terminal is which, the contact arrangement has not been verified sufficiently for selection.

NO and NC also need a reference condition. Their state labels refer to the specified reference condition, not to an unqualified promise about whether a circuit is energized or what a connected device will do. Confirm the reference condition in the applicable documentation before interpreting an open or closed path. A circuit’s behavior depends on its wiring and control design as well as on the switch contacts.

Keep this distinction in view throughout selection: SPDT identifies how contacts are arranged to change over, while the documented terminal identities and reference condition establish how to interpret them. Neither fact establishes electrical ratings or mechanical suitability. Those are separate requirements that need their own evidence.

## micro switch SPDT contacts selection: Match the circuit requirements

Write down the conditions the circuit presents at the switch: whether its supply is AC or DC, the relevant voltage and current, and the load type. These are not interchangeable details. The applicable rating must be documented for the current type, load, and test condition that match the intended use.

Compare the circuit conditions with the particular switch’s applicable specification sheet. A rating stated for AC does not establish a DC rating, and a rating for one load type or test condition does not establish a rating for another. Do not treat an SPDT designation as evidence of a voltage, current, or load capacity. Contact configuration and electrical rating answer different questions.

If the documentation lists several ratings, identify which one applies to the actual circuit conditions rather than selecting a convenient or higher-looking value without its conditions. Preserve any stated test condition when interpreting the rating. If the current type, load, or test condition is missing or unclear, electrical suitability remains unresolved; do not fill the gap by transferring a rating from another condition.

This is a compatibility check, not a general claim that a switch is suitable whenever its nominal figures appear to match. The available evidence must cover the relevant circuit conditions. Where it does not, obtain the applicable documentation or have the unresolved circuit requirements assessed by a qualified person. Do not proceed on the assumption that the SPDT contact arrangement itself supplies the missing evidence.

## Check terminal identification and contact states

First confirm COM, NO, and NC, if those labels apply, from the exact switch marking or schematic. Do not infer them from terminal location alone. Also confirm the reference condition used for the NO and NC descriptions. Without both terminal identity and a defined reference state, a continuity result may be misinterpreted.

An isolated continuity check may help verify terminal behavior when the check is appropriate and can be performed safely. Identify the actuator state being checked, then compare each expected open or closed path with the documented contact arrangement for that state. Avoid treating a click or actuator movement as proof of electrical continuity: movement alone does not establish the contact reading.

Keep the limits of this check explicit. A switch-only result concerns the isolated switch in the tested state. It does not establish that installed wiring is correct, that the circuit load is within the applicable rating, or that the complete equipment is safe. If the switch cannot be isolated safely, or the circuit state and expected behavior are uncertain, do not improvise a test; seek qualified assessment.

A mismatch between a documented state and an isolated reading is a reason to investigate the discrepancy, not by itself a diagnosis of the whole equipment. Terminal identification, actuator state, the test setup, and the switch itself are distinct considerations. The selection decision still depends on the documented electrical and mechanical requirements.

## Match actuator movement to the mechanism

A contact arrangement does not specify how the host mechanism must move the actuator. Check how the relevant part contacts and moves the particular switch’s actuator. Do not assume that every micro switch has the same actuator geometry or that a mechanically familiar layout will fit the intended mechanism.

Where documentation provides operating position and permitted actuator travel, compare those details with the mechanism’s movement. Pretravel runs from the free position to the operating position. Overtravel runs from the operating position to the extreme permitted actuator position. These describe different portions of movement, so do not treat one as a substitute for the other.

The mechanism must be considered independently of the SPDT contacts. A switch with the desired contact arrangement is not thereby shown to actuate at the required point or to remain within its documented travel. If the relevant operating point, release point, or permitted travel information is absent or ambiguous, mechanical fit has not been established. Do not infer force, life, or other actuator specifications from contact configuration.

This check is about whether the documented movement requirements match the actual mechanical interface. It does not prove electrical compatibility, and an electrical rating match does not prove mechanical fit. Both checks need supporting information for the particular switch and intended circuit or mechanism.

### Related guides

- [spring plunger micro switch selection](/guides/spring-plunger-micro-switch-selection/)
- [micro switch freezing temperature selection](/guides/micro-switch-freezing-temperature-selection/)
- [micro switch contact gap selection](/guides/micro-switch-contact-gap-selection/)
- [micro switch dust ingress selection](/guides/micro-switch-dust-ingress-selection/)

## Decide when the selection is not established

A selection is not established if any essential part of the match remains uncertain: the applicable AC or DC rating, load type or test condition; the terminal identities and reference state; or the actuator movement and permitted travel. Do not resolve those gaps by assuming that all SPDT micro switches share the same ratings, terminal layout, or mechanical behavior.

Review the exact switch documentation and the circuit requirements together. If the documentation does not resolve terminal identity, rating conditions, or relevant travel limits, seek authoritative information. Questions involving unresolved circuit or safety conditions require qualified assessment rather than conclusions from an isolated continuity check.

The decision is conditional: the documented contact arrangement must be identified, the electrical rating must apply to the circuit’s actual current type, load, and test condition, and the actuator movement must fit the mechanism within documented limits. SPDT alone establishes none of those matches. A micro switch SPDT contacts selection is supportable only when the needed electrical and mechanical evidence is available; otherwise, compatibility remains unknown.

## Sources and references

- Defense Logistics Agency ASSIST: [MIL-PRF-8805K: Switches and Switch Assemblies, Sensitive, Snap Action, General Specification For](https://quicksearch.dla.mil/qsDocDetails.aspx?ident_number=7196){: rel="nofollow noopener noreferrer" }
- Wikipedia: [Miniature snap-action switch](https://en.wikipedia.org/wiki/Miniature_snap-action_switch){: rel="nofollow noopener noreferrer" }
