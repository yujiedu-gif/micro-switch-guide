---
title: "Micro switch contact rating: How to interpret the limits"
description: "micro switch contact rating: Understand the operating idea, essential terminology, practical checks, limitations, and evidence needed for careful."
date: 2026-10-12 17:55:05 +0800
category: Basics
tags:
  - micro switch contact rating
  - micro switches
  - Basics
author: editorial_team
---

A **micro switch contact rating** describes an electrical limit for the switch contacts under specified conditions. It is not a universal safe-current value that can be applied to any circuit. To interpret it, match the stated voltage, AC or DC supply, and load type to the actual circuit, then account for the load’s operating and switching behavior. If those conditions do not match, the printed number alone cannot establish suitability.

## What a micro switch contact rating specifies

A contact rating states the electrical conditions under which the contacts are rated to carry or switch a load. Read voltage and current together, and retain the conditions attached to both. A current value by itself is incomplete: it does not say which voltage, supply type, or load behavior the rating covers. A rating for one set of conditions should not be treated as a general allowance for another.

Check whether the specification identifies AC or DC. Do not assume that a value given for AC also applies to DC, or the reverse. The applicable rating may differ between them, so the supply type and voltage in the circuit need to correspond to the documented rating conditions.

A contact rating concerns the electrical contacts, not every property of the switch. It does not by itself establish how much actuator force is needed, how far an actuator moves, or how long the switch will last in a particular application. Those are separate characteristics requiring their own applicable information.

The relevant evidence is the documentation for the exact switch and equipment. Use the connection diagram, terminal markings, circuit function, and permissible load documented for that switch rather than inferring its arrangement or limits from a generic physical layout. If the rating conditions or terminal function are not clear, the rating cannot be reliably matched based on appearance alone.

## How micro switch contact rating changes with load type

The load category matters because loads can behave differently when switched. A resistive-load rating does not automatically establish a suitable rating for a motor, solenoid, lamp, or capacitive load. Those categories should not be treated as interchangeable without documentation that covers the actual load.

Some loads draw more current at startup than during steady operation. Motor starting current and lamp inrush can therefore exceed what a comparison with ordinary running current suggests. Looking only at the steady-state value may miss a more demanding switching condition.

Inductive loads, such as motors or solenoids, can also create switching stress when the circuit is interrupted. The energy associated with an inductive load affects the contact-interruption condition. A simple comparison of the load’s normal current with a current figure on a switch does not show whether that switching behavior is covered.

Capacitive loads also require a matching specification rather than an assumption based on a resistive rating. The key question is not whether a load’s current happens to be below one printed number, but whether the published rating covers the load category and the voltage and switching conditions involved.

Keep each rating tied to its stated conditions. If documentation gives a value for one load type, do not transfer it to a different load type without supporting data. When a datasheet does not identify the relevant load category or switching conditions, treat that part of the comparison as unresolved rather than filling the gap with a general current comparison.

## Compare the rating with an application

Use a consistent comparison sequence. First identify the circuit supply and load; next find the rating that covers those conditions; then compare the demanding operating values and switching duty with the documented limits. A match in one parameter does not resolve a mismatch or unknown in another.

1. **Identify the supply.** Record the circuit voltage and whether it is AC or DC. Do not substitute one for the other when reading the switch specification.
2. **Identify the load.** Determine whether the switched load is resistive, a motor, a solenoid, a lamp, capacitive, or another type. Use the load category identified in the equipment or component documentation rather than guessing from a current value.
3. **Gather the load conditions.** Determine the normal current, relevant peak or inrush current, and switching frequency. Include the way the contacts operate in the circuit, especially where the load is interrupted. If a required value is unavailable, note that it is unknown; do not assume it is negligible.
4. **Find the matching rating conditions.** Check whether the switch documentation specifies the same supply type, voltage, and load category, along with applicable operating or test conditions. A rating for an unmatched condition is not evidence that the actual condition is covered.
5. **Compare the demanding values with the applicable limits.** Consider worst-case operating values and switching duty, not just nominal steady-state current. Also check any documented environmental or life constraints that apply to the intended use.
6. **Resolve gaps before deciding.** If the load category, peak behavior, supply, or other required condition is missing or ambiguous, the comparison is incomplete. Seek qualified technical review or an appropriately rated switching approach for the actual conditions.

This sequence is a way to organize evidence, not a promise that a single number proves the complete circuit suitable. The applicable documentation must cover the conditions that matter to the actual load and its switching behavior. Do not infer an operating margin where the supplied rating information does not establish one.

## What the contact rating does not tell you

The contact rating is separate from mechanical operating characteristics. It does not specify actuator force or travel, and those mechanical details cannot be deduced from an electrical current or voltage value. Likewise, a contact rating alone does not state the electrical life expected under every application duty.

An electrical operation count, where published, must be read with its stated load, operating sequence, and test conditions. A count established under one set of conditions should not be presented as a guaranteed life under a different load or switching pattern. Mechanical endurance and electrical endurance are not interchangeable measures.

A specification may state a rating without answering every application question. It may not make clear whether a peak or inrush condition is covered, whether the load category matches, or how the switching sequence relates to the intended circuit. Do not silently treat missing information as confirmation.

The switch documentation and equipment documentation should be considered together where both are relevant. The connection diagram, terminal marking, circuit function, and permissible load for the exact switch and equipment are more useful than assumptions based on a generic terminal layout. This does not turn the rating into a wiring guide; it sets a boundary on what can be concluded from the rating.

If conditions are uncertain or unmatched, the available rating does not establish that the switch is suitable. The appropriate next step is technical verification by someone qualified to assess the actual circuit, or use of a switching approach documented for those conditions. A single steady-state current comparison cannot settle unresolved voltage, load, inrush, interruption, frequency, or service-life questions.

### Related guides

- [dual micro switch](/guides/dual-micro-switch/)
- [touch micro switch](/guides/touch-micro-switch/)
- [no nc micro switch](/guides/no-nc-micro-switch/)
- [normally open micro switch](/guides/normally-open-micro-switch/)

## Micro switch contact rating: questions to verify before use

Before relying on a rating, confirm that the stated voltage and AC/DC supply match the circuit. Then check whether the documentation covers the actual load type and its starting, inrush, or interruption behavior. Confirm that switching frequency and any stated environmental or life conditions also fit the intended duty.

A concise review should answer these questions:

- Is the supply voltage and AC/DC type within the conditions stated for the rating?
- Does the rating cover the actual load category, rather than only a different load such as a resistive one?
- Have normal current and relevant peak or inrush behavior been considered?
- Does the documented switching condition cover how often the contacts operate and interrupt the load?
- Are the applicable operating, environmental, and electrical-life conditions clear?
- Are the diagram, terminal markings, circuit function, and permissible load documented for the exact switch and equipment?

If a necessary answer is unknown, do not treat a nominal current figure as confirmation. The **micro switch contact rating** supports a conclusion only when the documented conditions correspond to the circuit conditions being assessed. Where that correspondence cannot be established, obtain qualified technical review or use an appropriately rated switching approach rather than assuming the rating transfers.

## Sources and references

- Defense Logistics Agency ASSIST: [MIL-PRF-8805K: Switches and Switch Assemblies, Sensitive, Snap Action, General Specification For](https://quicksearch.dla.mil/qsDocDetails.aspx?ident_number=7196){: rel="nofollow noopener noreferrer" }
- Occupational Safety and Health Administration: [29 CFR 1910.333: Selection and Use of Work Practices](https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.333){: rel="nofollow noopener noreferrer" }
