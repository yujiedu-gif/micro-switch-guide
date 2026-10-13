---
title: "micro switch SPST NO contacts selection"
description: "micro switch SPST NO contacts selection: Understand the operating idea, essential terminology, practical checks, limitations, and evidence needed for."
date: 2026-10-13 09:00:00 +0800
category: Selection Guides
tags:
  - micro switch SPST NO contacts selection
  - micro switches
  - Selection Guides
author: editorial_team
---

Selecting a micro switch SPST NO contacts selection begins by treating the label as a statement about contact arrangement, not as proof that a switch suits a particular circuit or mechanism. SPST means one pole and one throw: one switched circuit path. NO, or normally open, means the contacts are open in the reference condition specified by the applicable documentation. That definition narrows the contact arrangement, but leaves load suitability, actuator fit, and installation requirements to be checked separately.

A sound selection process starts with the circuit behavior the application requires, then checks the reference state, load conditions, actuator interface, and mounting constraints. The final decision depends on documentation for the exact candidate and its stated conditions. If a required detail is missing, suitability remains unresolved rather than implied by the SPST NO designation.

## What micro switch SPST NO contacts selection establishes

SPST NO combines two contact-configuration terms. Single-pole, single-throw describes one switched circuit path. Normally open describes the contact condition in a documented reference state. For a micro switch, mechanical movement of the actuator can change an electrical contact state; this is why such switches can be used for position or limit detection. That general function does not establish how a particular installed circuit behaves.

The reference condition matters. “Normally open” is not an unconditional promise that current will be absent in every operating state, wiring arrangement, or surrounding circuit. Read the reference state and contact-state information from the relevant documentation. Do not infer installed-circuit behavior from the label alone.

The designation also does not specify whether the contacts are suitable for a particular electrical load. Rating values are requirements tied to stated load and test conditions, not universal switching capacities. SPST NO does not identify the actuator form, motion requirements, mounting arrangement, or life. Those are separate selection questions, and their answers depend on documentation for the candidate and application.

## Start with the circuit function and required reference state

First identify the circuit path that must change state and the behavior required in the documented reference condition. State the requirement in functional terms: which path needs an open contact at that reference state, and what change of state is required when the actuator moves? This establishes whether an SPST NO arrangement matches the requested contact behavior without assuming what the host equipment does with that change.

Next, confirm the reference condition in the candidate’s documentation. Do not treat “normally” as a substitute for a defined state, or assume that the unactuated condition is the relevant reference unless documentation establishes it. The required circuit behavior and the documented contact state must be compared directly.

Keep terminal identification separate from the contact arrangement. SPST NO alone does not establish terminal names, their physical positions, or a layout. Use the documented connection diagram and terminal markings for the exact switch and equipment. Do not infer a connection from a generic drawing or the apparent physical arrangement of terminals.

The result of this step is a functional requirement, not a complete selection. If the required reference state or contact behavior cannot be established from the circuit and candidate documentation, pause: the designation alone cannot resolve that uncertainty.

## Check load and operating conditions separately

Once the required contact behavior is clear, check whether the documented electrical ratings apply to the actual load and operating conditions. Do not infer a permissible load from SPST NO. A contact configuration describes how a path is arranged, not the voltage, current, load category, or test conditions under which it may be switched.

Use rating information that matches the relevant load type and conditions. Keep AC and DC distinctions, load categories, and test conditions within the scope actually stated in the applicable documentation. A value established for one condition cannot be carried over to a different load or condition without supporting documentation. Rating values are specification-sheet requirements tied to stated load and test conditions, not universal switching capacities.

The practical decision rule is limited: if the documented rating covers the actual load and operating conditions, the electrical-fit question can be evaluated within that scope. If the load type, operating conditions, or applicable rating is missing or ambiguous, mark suitability unresolved. Do not fill a gap with the SPST NO label, a presumed similarity to another switch, or an unstated AC/DC equivalence.

This check concerns electrical fit only. Passing it does not establish that the actuator can be operated correctly or that the switch can be mounted in the required position. Those questions need their own evidence.

## Match the actuator interface and installation constraints

Check how the external mechanism is intended to move the candidate’s actuator. Compare the documented actuator interface and motion requirements with the actual mechanism, rather than treating the contact arrangement as evidence of mechanical compatibility. A micro switch can change contact state in response to actuator movement, but that general mechanism does not establish that a particular switch will reach the needed state in a particular installation.

Where relevant and documented, examine operating point, release point, pretravel, and overtravel as design-specific parameters. These terms describe distinct aspects of movement and state change; their values and applicability must come from documentation for the candidate. Do not assume that a switch with the right contact arrangement has the travel or operating characteristics needed by the surrounding mechanism.

Then check mounting constraints and the relationship between the switch and its actuator mechanism. Separate whether the switch can be mounted as required from whether the external part moves the actuator as required. The mechanism’s alignment and available travel are not specified by SPST NO, and a contact label cannot establish that these installation conditions are met.

If the documentation does not describe a required actuator or mounting detail, treat mechanical fit as unverified. Do not infer fit from the general use of micro switches for position or limit detection. That use is background, not a suitability claim for a particular application.

### Related guides

- [spring plunger micro switch selection](/guides/spring-plunger-micro-switch-selection/)
- [micro switch freezing temperature selection](/guides/micro-switch-freezing-temperature-selection/)
- [micro switch contact gap selection](/guides/micro-switch-contact-gap-selection/)
- [micro switch dust ingress selection](/guides/micro-switch-dust-ingress-selection/)

## Use documentation to make the final selection decision

Bring the checks together as a requirement list: the needed contact behavior and reference state; the actual load and operating conditions; the actuator interface and required motion; and the mounting constraints. A candidate is supported only to the extent that its documentation addresses these requirements under the stated conditions.

For the exact switch and equipment, use the connection diagram, terminal markings, circuit function, and permissible load documented for that combination. Check ratings and mechanical parameters against the same candidate’s documentation rather than relying on terminal layout, a generic contact label, or details from another design. The configuration label does not independently identify terminals or establish a permissible load.

The decision boundary is straightforward. If the documented contact behavior, electrical conditions, actuator interface, and mounting requirements match the stated needs, the available information supports those specific aspects of selection. It does not establish any condition that was not documented. If a required rating, reference state, terminal identification, actuator detail, or mounting constraint is absent or ambiguous, do not claim a match. Obtain the missing specification or leave selection unresolved.

In short, micro switch SPST NO contacts selection establishes a contact-configuration requirement, not a complete specification. Use the documented reference condition to verify the required open-contact state, then assess load, actuator, and installation separately. The designation alone cannot prove suitability for a circuit or mechanism.

## Sources and references

- Defense Logistics Agency ASSIST: [MIL-PRF-8805K: Switches and Switch Assemblies, Sensitive, Snap Action, General Specification For](https://quicksearch.dla.mil/qsDocDetails.aspx?ident_number=7196){: rel="nofollow noopener noreferrer" }
- Occupational Safety and Health Administration: [29 CFR 1910.333: Selection and Use of Work Practices](https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.333){: rel="nofollow noopener noreferrer" }
- Wikipedia: [Miniature snap-action switch](https://en.wikipedia.org/wiki/Miniature_snap-action_switch){: rel="nofollow noopener noreferrer" }
