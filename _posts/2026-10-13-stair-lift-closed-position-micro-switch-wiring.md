---
title: "Stair lift closed position micro switch wiring: how to interpret it"
description: "stair lift closed position micro switch wiring: Understand the operating idea, essential terminology, practical checks, limitations, and evidence needed."
date: 2026-10-13 09:00:00 +0800
category: Applications
tags:
  - stair lift closed position micro switch wiring
  - micro switches
  - Applications
author: editorial_team
---

A stair lift closed position micro switch wiring diagram should be read as documentation for one particular lift design, not as a universal wiring pattern. The switch may respond to a mechanical feature associated with the lift’s closed position, but the lift’s circuit determines what the resulting contact change means. Begin by matching the documented mechanical reference to the switch and then identifying terminals and expected states from the exact diagram. Do not infer terminal function from wire color, physical placement, or another lift’s arrangement. If documentation does not establish the switch’s reference condition, contact states, or circuit role, those details remain unresolved.

## What “closed position” means in stair lift closed position micro switch wiring

“Closed position” refers to the position or condition specified by the documentation for the particular stair-lift design. It is not a universal mechanical state shared by all lifts, nor does the phrase alone identify whether the switch actuator is pressed or released. Those relationships must be established from the relevant design information.

Where a design uses a micro switch for position or limit detection, a mechanical feature can move its actuator and cause the switch to change an electrical contact state. The feature might act directly on the actuator or act through a linkage, but which arrangement applies is design-specific. Identify the actual part or linkage from the lift documentation rather than assuming how a stair lift is built.

Keep three events distinct: the lift reaches the documented closed-position condition; a physical feature moves the switch actuator; and the switch changes a contact state. The lift’s circuit then interprets that change. The switch action does not, by itself, establish what the lift does next.

Before interpreting the wiring, find the documentation that defines the closed-position reference and identifies the switch used in that design. If the documentation names a closed condition but does not show how it relates to actuator movement, do not infer that relationship from the switch’s location or appearance. The reference is unresolved until supported by the design information.

## Map the closed-position mechanism to the micro switch

Trace the mechanical path using the documented parts: start with the feature associated with the specified closed position, follow any identified linkage, and end at the micro-switch actuator. Confirm that the documentation actually connects those parts. This path explains how the switch may be actuated; it does not establish the electrical function assigned to the contact change.

The switch’s operating event and its release event are distinct. The feature may move the actuator in one direction to operate the switch and later move away so the actuator releases. Do not assume the lift’s named closed position corresponds to either event unless the design documentation says so. The exact actuation point, travel, force, or timing is not established here.

If the switch’s actuation point is unclear, compare the mechanical reference, actuator position, and any stated switch-state description in the applicable documentation. A diagram that only labels a switch “closed position” may not show whether that means the lift is closed, the contact is closed, or the actuator is operated. These meanings must not be conflated. If the documents do not resolve the distinction, leave it open rather than assigning a state.

This mechanical trace is also a boundary check. A diagram for a different switch or a different lift design cannot establish the actuator path for the lift being interpreted. Likewise, recognizing a micro switch does not prove that the surrounding mechanism is correctly aligned or that the lift’s circuit responds as intended.

## Interpret terminal labels and contact state from the diagram

Use COM, NO, and NC only when the specific switch documentation or circuit diagram confirms those terminal labels and their reference condition. COM means common when that contact arrangement is documented. NO and NC describe contact states relative to the stated reference condition; they should not be treated as unconditional promises about current flow or lift behavior.

Read the diagram’s state description before assigning a contact state. In particular, do not equate “unactuated” with “lift at closed position” unless the design documentation explicitly makes that connection. If a diagram specifies the switch state with the actuator released or operated, retain that condition when interpreting its contacts. If it does not define the condition, the state cannot be reliably inferred from the labels alone.

Follow the documented connection diagram, terminal markings, circuit function, and permissible load for the exact switch and equipment. Do not identify terminals from wire color, apparent physical order, or the layout of another switch. Physical placement and similar-looking components do not establish terminal identity or contact arrangement.

Electrical ratings also require their stated conditions. Under MIL-PRF-8805K 6.1.1 and applicable specification sheets, rating values are specification-sheet requirements tied to stated load and test conditions, not universal switching capacities. A diagram or label that does not establish the applicable load and conditions does not support a general capacity claim. Do not transfer a rating to a different load or infer suitability from terminal labels.

## Relate the contact change to the lift circuit without assuming its function

A micro switch can change an electrical contact state in response to mechanical actuator movement. That local action is separate from the host lift’s circuit logic. The circuit diagram and applicable equipment documentation must establish how the contact change is used before assigning it a system-level meaning.

For example, the contact change alone does not show whether the circuit enables movement, stops motion, triggers an alarm, or serves another function. Those outcomes are not established merely by calling the switch a closed-position switch. Do not infer a normal state, safety function, or response from the component name or from the fact that a switch is present.

Keep closed-position documentation distinct from stair lift open position micro switch wiring. Similar position labels do not establish that two switches have matching terminal assignments, actuator states, circuit connections, or functions. Use the documentation for the specific switch and position under review; do not substitute an open-position diagram for missing closed-position information.

If the diagram shows a contact connected to a circuit but does not explain the circuit’s behavior, state only what the diagram establishes: the documented connection and, if specified, the contact state under its reference condition. The resulting lift behavior remains unresolved. This distinction prevents a component-level observation from being mistaken for a conclusion about the whole lift.

### Related guides

- [bottling machine home position micro switch location](/guides/bottling-machine-home-position-micro-switch-location/)
- [incinerator end of stroke micro switch maintenance](/guides/incinerator-end-of-stroke-micro-switch-maintenance/)
- [rotary indexing table guard interlock micro switch location](/guides/rotary-indexing-table-guard-interlock-micro-switch-location/)
- [security barrier open position micro switch wiring](/guides/security-barrier-open-position-micro-switch-wiring/)

## Verify the switch state safely and recognize the limits

Follow the applicable documented deenergization and qualification requirements. Do not improvise a test, repair, bypass, adjustment, or replacement procedure from a wiring diagram. Work that falls outside the applicable documented procedure belongs with qualified personnel.

An isolated continuity check requires a defined actuator condition and the documented terminal pair. Compare the observation with the expected state given for that same condition in the switch or equipment documentation. Without those references, a reading cannot be interpreted reliably. Do not assume a pair of terminals or an expected open or closed state based on wire color, physical location, or another lift’s diagram.

A continuity result concerns the isolated switch under the tested condition. It does not establish that the installed wiring is correct, that the host circuit interprets the contact as intended, or that the lift works as a whole. A click may indicate movement of a snap mechanism, but does not prove continuity, contact condition, correct wiring, or suitability for a load.

Contact resistance is also not a generic field-test value. Under MIL-PRF-8805K 3.10 and 4.7.6, contact resistance is a measured switch requirement whose method, connection points, and limit must come from the applicable specification and test procedure. Without those details, do not use an assumed resistance limit to judge the switch.

The practical boundary is documentary: establish the closed-position reference and mechanical path, identify terminals and state conditions from the exact diagram, and relate the contact change to lift behavior only where the circuit documentation supports that conclusion. If any link is missing, keep it unresolved. stair lift closed position micro switch wiring can be interpreted only as far as the particular design’s mechanical, terminal, and circuit documentation allows.

## Sources and references

- Defense Logistics Agency ASSIST: [MIL-PRF-8805K: Switches and Switch Assemblies, Sensitive, Snap Action, General Specification For](https://quicksearch.dla.mil/qsDocDetails.aspx?ident_number=7196){: rel="nofollow noopener noreferrer" }
- Occupational Safety and Health Administration: [29 CFR 1910.333: Selection and Use of Work Practices](https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.333){: rel="nofollow noopener noreferrer" }
- Wikipedia: [Miniature snap-action switch](https://en.wikipedia.org/wiki/Miniature_snap-action_switch){: rel="nofollow noopener noreferrer" }
