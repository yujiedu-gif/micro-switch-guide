---
title: "micro switch DPDT contacts selection: How to choose the contact arrangement"
description: "micro switch DPDT contacts selection: Understand the operating idea, essential terminology, practical checks, limitations, and evidence needed for careful."
date: 2026-10-13 09:00:00 +0800
category: Selection Guides
tags:
  - micro switch DPDT contacts selection
  - micro switches
  - Selection Guides
author: editorial_team
---

Selecting a micro switch DPDT contacts selection starts with the circuit’s required contact paths, then checks whether the exact switch documentation identifies those paths and supports the intended electrical conditions. DPDT describes a contact arrangement: two poles, each associated with two throws. It does not establish voltage, current, load capacity, or compatibility with a particular circuit. A miniature snap-action switch can change an electrical contact state in response to mechanical actuator movement and is commonly used for position or limit detection, but that general use does not establish suitability for a specific application.

The practical decision is therefore conditional. First identify how many circuits must be switched and which contact paths each circuit needs. Next confirm the switch’s terminal identification and contact states from its own documentation. Finally, compare the documented ratings and conditions with the actual circuit requirements. If any necessary terminal, state, or rating information is missing, the arrangement or suitability cannot be confirmed from the DPDT designation alone.

## micro switch DPDT contacts selection: What the designation tells you

DPDT means two poles and double throw. A pole is a contact group that can make a connection through one of its available paths; double throw indicates two possible contact paths associated with each pole. In a documented arrangement, this describes the contact options available for switching, not the circuit’s behavior once installed. The exact contact configuration must still be established from the switch’s documentation.

The designation does not provide a complete electrical specification. It does not state the permissible voltage or current, identify a supported load type, or prove that the switch is suitable for a particular circuit. Contact count alone establishes none of those limits. A DPDT label is therefore useful for understanding the type of contact arrangement being considered, but it cannot substitute for the terminal diagram, contact-state information, or rating data.

Keep the component separate from the host system. A micro switch’s contact state can change in response to actuator movement, but the resulting circuit behavior depends on the actual wiring and circuit design. DPDT by itself does not say whether equipment will start, stop, signal, or change operating modes. Those effects cannot be inferred from the contact-arrangement label.

## Map documented poles, throws, and terminal states

Before assigning circuit wires to contact paths, consult the exact switch’s connection diagram and terminal markings. Use those sources to identify which terminals form each documented pole and which paths are associated with its throws. Do not derive terminal positions from a generic DPDT drawing or from the physical layout of pins: the available evidence does not establish a universal terminal layout.

Contact-state labels also need a reference condition. Where the documentation identifies NO or NC, interpret those labels in relation to the specified reference condition, not as an unqualified promise about current flow in an installed circuit. If the reference condition is not stated, or the terminal diagram does not identify the relevant paths, the contact mapping cannot be confirmed. Do not fill that gap by assuming a familiar pin order or state.

The useful result of this step is a documented map, not a wiring recipe. Record which terminals the documentation assigns to each contact path and the condition under which any stated contact state applies. If the diagram, markings, or state reference are unavailable or unclear, stop short of assigning terminals. The connection diagram, terminal marking, circuit function, and permissible load documented for the exact switch and equipment are the appropriate basis for interpretation; a generic physical-layout inference is not.

## Match the contact arrangement to the circuit requirement

Describe the circuit requirement before deciding whether the contact arrangement fits. Identify how many circuits must be switched independently and which contact path each circuit requires. Then compare those requirements with the poles and throws actually documented for the candidate switch. This checks whether the described arrangement provides the needed contact paths without assuming anything about terminal order or installed behavior.

The circuit’s required state matters as well as its path count. The switch documentation must identify the relevant contact state at a reference condition, and the circuit documentation must establish what that state needs to accomplish. DPDT alone does not establish whether a path should be open or closed for a particular system state, nor does it determine what the equipment will do when the actuator moves. The result depends on the actual circuit design.

If the circuit function is not documented, or the switch’s contact paths cannot be mapped, the match remains unresolved. Do not treat a two-pole, double-throw description as proof that the switch will perform a particular control function. This selection step concerns only whether the documented arrangement corresponds to the circuit’s required number and type of contact paths. It does not establish electrical suitability or application compatibility.

## Check ratings separately from contact count

After the contact arrangement appears to meet the circuit’s path requirements, check the electrical limits separately. Find the documented values and conditions that apply to the intended voltage, current, and load. Compare the actual requirements with those limits only when the documentation covers the relevant conditions. A DPDT designation contains no voltage or current rating and does not identify a permissible load.

Rating values are specification-sheet requirements tied to stated load and test conditions, not universal switching capacities. A value detached from its specified load or test condition cannot establish suitability for a different condition. Likewise, the existence of two poles and two throws does not show that every contact path can carry the circuit’s required load. Do not transfer a documented value beyond the load and conditions to which it applies.

If the applicable documentation does not establish the required electrical limits or conditions, the selection cannot be completed on the basis of contact count. Keep the unresolved items explicit: the needed voltage, current, or load information, the relevant specification conditions, or the switch’s applicable rating may still be unknown. In that situation, DPDT confirms only the stated type of contact arrangement, not suitability for the intended circuit.

### Related guides

- [spring plunger micro switch selection](/guides/spring-plunger-micro-switch-selection/)
- [micro switch freezing temperature selection](/guides/micro-switch-freezing-temperature-selection/)
- [micro switch contact gap selection](/guides/micro-switch-contact-gap-selection/)
- [micro switch dust ingress selection](/guides/micro-switch-dust-ingress-selection/)

## Selection checklist and decision boundary

Use this sequence to make a bounded contact-selection decision:

1. **State the circuit requirement.** Identify how many circuits must be switched and which contact paths each requires.
2. **Confirm the documented arrangement.** Check that the exact switch documentation identifies the poles and throws needed for those paths.
3. **Map terminals and states.** Use the switch’s own diagram, terminal markings, and documented reference condition. Do not infer terminal layout or contact state from a generic diagram.
4. **Compare electrical requirements.** Check the documented voltage, current, and load conditions against the actual circuit requirements. Treat ratings as applicable only within their stated conditions.
5. **Mark unresolved information.** If a terminal, reference state, circuit function, rating, or required condition is missing, do not treat the selection as confirmed.

The decision boundary is straightforward: select the contact arrangement only when its documented paths match the circuit’s stated requirement. Then establish electrical suitability from ratings that apply to the intended conditions. The complete connection diagram, terminal identification, circuit function, and permissible load for the exact switch and equipment must support the conclusion, with applicable deenergization and qualification requirements followed. If documentation leaves a necessary detail unknown, the DPDT label alone cannot resolve it.

In short, micro switch DPDT contacts selection is a two-part check: match documented poles and throws to the circuit’s needed paths, then verify the separate electrical limits under their stated conditions. Neither the contact designation nor a generic terminal layout establishes how an appliance behaves or whether a switch is suitable for its load.

## Sources and references

- Defense Logistics Agency ASSIST: [MIL-PRF-8805K: Switches and Switch Assemblies, Sensitive, Snap Action, General Specification For](https://quicksearch.dla.mil/qsDocDetails.aspx?ident_number=7196){: rel="nofollow noopener noreferrer" }
- Occupational Safety and Health Administration: [29 CFR 1910.333: Selection and Use of Work Practices](https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.333){: rel="nofollow noopener noreferrer" }
- Wikipedia: [Miniature snap-action switch](https://en.wikipedia.org/wiki/Miniature_snap-action_switch){: rel="nofollow noopener noreferrer" }
