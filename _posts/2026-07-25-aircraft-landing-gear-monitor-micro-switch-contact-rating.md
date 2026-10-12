---
title: "aircraft landing gear monitor micro switch contact rating: How to Interpret It"
description: "aircraft landing gear monitor micro switch contact rating: Understand the operating idea, essential terminology, practical checks, limitations, and."
date: 2026-07-25 09:00:00 +0800
category: Applications
tags:
  - aircraft landing gear monitor micro switch contact rating
  - micro switches
  - Applications
author: editorial_team
---

# Interpreting a Landing Gear Monitor Switch Rating

An **aircraft landing gear monitor micro switch contact rating** is meaningful only when read alongside the electrical conditions for which that rating is specified. It is not, by itself, proof that a switch is suitable for a particular aircraft circuit or installation. The relevant comparison is between the contact’s documented duty in the actual circuit and the conditions attached to the stated rating.

A monitoring circuit may use a contact to change an indication signal, but the name of the monitored equipment does not establish what electrical load the contact switches. The circuit documentation must identify that duty. If the load type, contact voltage, current, or other required conditions are not documented, applicability remains unresolved rather than something that can be inferred from a generic rating.

## What an aircraft landing gear monitor micro switch contact rating means

A contact rating states electrical limits under specified conditions. It should be read as a conditional specification, not as a universal safe operating value for every circuit. Voltage and current values alone are not enough to establish applicability if the stated rating also depends on load type, switching conditions, or endurance qualifications.

MIL-PRF-8805K 6.1.1 and applicable specification sheets treat micro switch electrical rating values as specification-sheet requirements tied to stated load and test conditions. In practical terms, a rating applies within the scope of its stated conditions. It does not automatically apply to a different load or operating duty merely because the voltage and current appear comparable.

Read the rating together with the applicable specification sheet and its notes. Establish what load type the rating covers, which voltage and current conditions it states, and whether it includes relevant switching or endurance qualifications. Do not fill gaps in those details with assumptions.

The rating belongs to the switch contact’s specified electrical duty. It does not, on its own, establish aircraft installation approval or demonstrate that the switch performs the required monitoring function in a particular system. Those are separate questions governed by the applicable circuit and maintenance documentation.

## Why load type changes how to read the contact rating

A resistive-load rating describes a stated contact duty for a resistive load. It should not be treated as interchangeable with a rating for an inductive or other load condition. The load type is part of the conditions that give a rating meaning, not a minor label that can be ignored when making a comparison.

With an inductive load, switching can involve transients. Therefore, a rating stated for a resistive load does not establish the contact’s applicable limit under an inductive load. The same caution applies when the actual load condition differs in another way from the one named in the specification. The supplied rating alone does not support a conversion factor or an assumed equivalent value for a different load.

The practical step is to identify the exact load condition stated in the applicable rating and compare it with documented circuit conditions. If the specification sheet gives separate ratings or qualifications, keep those distinctions intact. If the load type is absent, ambiguous, or unlike the stated condition, the comparison cannot establish applicability.

This is why a bare current and voltage marking should not be read as an all-purpose capacity. The conditions attached to those values determine what they support. A rating is evidence about a defined switch-contact duty, not a substitute for evidence about the circuit in which the contact operates.

## Identify the monitored circuit conditions before comparing ratings

Start with the contact path shown in the applicable circuit documentation. Determine whether the micro switch contact changes a low-current indication signal or switches another load. A signal that reports a landing gear state is not necessarily the same electrical duty as the equipment whose state is being monitored. Do not infer the switch contact’s load from the actuator, motor, or other monitored equipment.

For the contact itself, establish the documented voltage, current, and load characteristics. Record any documented switching frequency or other switching conditions that are relevant to the rating. These values and descriptions must come from the circuit evidence, not from assumptions based on the system’s function or on a generic description of a monitoring circuit.

Keep the distinction between the signal and the switched load clear. Calling a path a monitoring signal does not establish its contact current, voltage, or load type. Conversely, the fact that the circuit monitors landing gear does not establish that the micro switch carries actuator or motor current. The documentation must resolve what the contact actually switches.

If the available circuit information does not identify the contact-side conditions, stop short of concluding that a rating matches. Missing information is an unresolved input, not evidence that the circuit is a low-current signal or that the stated rating is sufficient.

## A verification path for aircraft landing gear monitor micro switch contact rating

Use a documentation-led comparison:

1. **Identify the applicable contact rating.** Consult the relevant specification sheet and preserve its stated voltage, current, load type, and any switching or endurance qualifications.
2. **Establish the actual contact duty.** Use the applicable circuit documentation to identify what the contact switches and the documented contact-side voltage, current, and load characteristics. Include switching frequency where documented and relevant.
3. **Compare like conditions.** Check whether the documented circuit conditions fall within the conditions attached to the rating. Do not substitute a resistive-load rating for an inductive or other condition without supporting documentation.
4. **Check governing aircraft documentation.** Consult applicable aircraft maintenance and circuit documentation for approved limits and verification steps. A generic rating comparison does not establish aircraft-level approval.
5. **Record unresolved details.** If a required load condition or rating qualification is missing or ambiguous, leave applicability unresolved and follow the governing documentation rather than inventing a value or procedure.

This path separates a component-level rating comparison from an aircraft-level decision. It does not prescribe installation, adjustment, troubleshooting, or a replacement. Those actions are outside what a generic contact-rating comparison can establish.

### Related guides

- [ball screw actuator home position micro switch replacement](/guides/ball-screw-actuator-home-position-micro-switch-replacement/)
- [bottling machine end of stroke micro switch](/guides/bottling-machine-end-of-stroke-micro-switch/)
- [automated guided vehicle home position micro switch location](/guides/automated-guided-vehicle-home-position-micro-switch-location/)
- [accelerator pedal position stop micro switch operating force](/guides/accelerator-pedal-position-stop-micro-switch-operating-force/)

## Limits of a contact-rating comparison

A rating comparison can address whether documented electrical conditions correspond to the conditions stated for a contact rating. Even a match does not, by itself, establish functional reliability, environmental suitability, or aircraft approval. Those conclusions require evidence beyond a rating comparison and must come from the applicable governing documentation.

A defensible conclusion therefore depends on both sides of the comparison: the exact rating conditions and the actual documented contact duty. It also depends on any relevant aircraft limits and verification steps. If either side is unclear, the evidence does not support a determination of applicability.

For an **aircraft landing gear monitor micro switch contact rating**, the key is to verify the contact’s actual documented circuit conditions against the rating’s stated load and test conditions. Keep load type and signal duty explicit, and do not treat a generic rating or the monitored equipment’s identity as proof of system suitability.

## Sources and references

- Defense Logistics Agency ASSIST: [MIL-PRF-8805K: Switches and Switch Assemblies, Sensitive, Snap Action, General Specification For](https://quicksearch.dla.mil/qsDocDetails.aspx?ident_number=7196){: rel="nofollow noopener noreferrer" }
