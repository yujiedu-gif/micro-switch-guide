---
title: "Motorized valve home position micro switch NO and NC terminals: what do they indicate?"
description: "motorized valve home position micro switch NO and NC terminals: Understand the operating idea, essential terminology, practical checks, limitations, and."
date: 2026-10-13 11:27:16 +0800
category: Applications
tags:
  - motorized valve home position micro switch NO and NC terminals
  - micro switches
  - Applications
author: editorial_team
---

A motorized valve home position micro switch NO and NC terminals describe contact states only in relation to a specified reference condition. They do not, by themselves, establish that the valve is physically at home or show how a controller interprets a signal. To understand a particular installation, trace how valve travel moves the external mechanism, how that mechanism operates the switch actuator, and which documented contact state results.

The labels are useful only when the exact switch’s contact arrangement and the relevant reference condition are known. The valve assembly documentation and circuit documentation are also needed to connect the switch state to a home-position indication. Without that evidence, the state at home cannot be inferred from NO or NC alone.

## Motorized valve home position micro switch NO and NC terminals: what the labels establish

NO and NC are contact-state descriptions, not unconditional statements about current flow. A generic changeover contact may use the labels common, normally closed, and normally open, but the exact device marking or schematic controls. The reference condition for interpreting the particular contact arrangement must also be documented. A label alone does not tell you which contact is closed when a valve is at its home position.

That distinction matters because “home” describes a physical position of the valve, while NO and NC describe electrical contact states under a specified reference condition. To relate them, the installation must provide a documented path from the valve’s position to the switch’s actuator and then to the contacts. The switch’s labels do not supply that missing mechanical or circuit information.

A wiring diagram or terminal layout should not be inferred from the physical placement of terminals. Use the connection diagram, terminal marking, circuit function, and permissible load documented for the exact switch and equipment. These details determine how the contacts are identified and used in the particular installation; a generic terminal arrangement cannot substitute for them.

Therefore, an NO or NC label can help identify a documented contact state, but it is not a standalone home-position indicator. To say what the valve signal means, establish the reference condition, the switch arrangement, the mechanical actuation point, and the circuit’s interpretation.

## Separate valve home position from micro switch actuator position

The relevant physical chain has several distinct parts. The valve travels toward or away from its home position. An external mechanism, such as a cam or linkage if the particular design uses one, may then move the micro switch’s actuator. The actuator movement operates the switch mechanism, which changes the contact state according to the documented arrangement. Each link must be established for the actual valve assembly rather than assumed from the terminal names.

The valve’s physical position and the switch actuator’s position are not interchangeable descriptions. A switch can be actuated at a designed point in the valve’s travel, but the point and the relationship between actuator movement and valve position depend on the particular mechanism and its documentation. A contact transition can therefore indicate that the switch changed state; it does not, by itself, prove the valve reached its physical endpoint.

Pretravel and overtravel are terms for actuator movement, not measures of valve position. Under MIL-PRF-8805K sections 6.5.14 and 6.5.16, pretravel runs from the actuator’s free position to its operating position, while overtravel runs from the operating position to the extreme permitted actuator position. These definitions describe switch-actuator travel within that standard’s scope. They do not establish a motorized valve’s travel, home position, or actuation point.

Do not assume that every motorized valve uses a micro switch, or that valves that do use one share the same linkage, actuation point, or signal arrangement. The assembly documentation must connect valve travel to the switch actuator. If that connection is undocumented, the relationship between the switch state and physical home remains unresolved.

## Interpret NO and NC at the documented reference condition

Interpret NO and NC only after confirming both the particular contact arrangement and the reference condition in the switch documentation. The terms identify contact states relative to that condition. They do not mean that a terminal carries current in every state, nor do they reveal how a control system will respond to a contact change.

Once the reference condition is known, the documentation can establish which contact transition occurs as the actuator moves. That transition can then be compared with the valve assembly’s documented actuation point. Do not convert this comparison into a universal statement that a valve’s home position corresponds to NO, NC, an open circuit, or a closed circuit. The supplied information must establish that relationship for the specific arrangement.

Also keep the contact description separate from the circuit signal. The circuit documentation determines how the contact is incorporated into the control logic. A change in contact state may be used as an indication, but its meaning depends on the actual circuit and its interpretation. The NO or NC label alone cannot establish whether the controller treats a particular state as home, travel, a fault, or something else.

If the documentation identifies a common, normally closed, and normally open contact, use those exact terminal markings and the specified reference condition. If the device instead has different markings or an unclear schematic, do not infer a changeover arrangement from a generic convention. The exact device marking or schematic controls.

## What evidence confirms the home-position signal in a particular installation?

Start with the exact switch documentation. Confirm the terminal identification, the documented contact arrangement, and the reference condition for the stated contact states. If those details are absent or ambiguous, the NO and NC labels alone are insufficient to identify which terminal relationship represents the state of interest.

Next, consult the valve or assembly documentation for the physical relationship between valve travel and switch operation. It needs to establish how the external mechanism operates the actuator and where in travel that occurs. Any stated mechanism adjustment or travel conditions are part of that relationship; do not supply them by assumption. A switch may change state at a point associated with travel without that state proving the valve has reached its physical home position.

Then consult the circuit or control documentation. It is needed to determine how the contact is used and what the control system is configured to infer from it. A contact change alone does not prove that the signal is correctly wired or that the controller interprets it as intended. Avoid treating a terminal label as evidence of the entire signal path.

Observations should be compared with those documents, keeping the valve position, mechanism movement, actuator state, and contact state distinct. If the documents do not connect these states, report the limit plainly: the home-position signal cannot be inferred from NO and NC labels alone. This evidence path is an interpretation boundary, not a universal wiring procedure or a repair method.

### Related guides

- [bottling machine home position micro switch location](/guides/bottling-machine-home-position-micro-switch-location/)
- [incinerator end of stroke micro switch maintenance](/guides/incinerator-end-of-stroke-micro-switch-maintenance/)
- [rotary indexing table guard interlock micro switch location](/guides/rotary-indexing-table-guard-interlock-micro-switch-location/)
- [security barrier open position micro switch wiring](/guides/security-barrier-open-position-micro-switch-wiring/)

## What a contact indication does not prove

A reported NO or NC state does not alone establish the valve’s physical position. It also does not establish that the external mechanism moved as intended, that the terminals are correctly identified or wired, that the wider equipment functions correctly, or that the control system produces its intended response. Those are separate facts requiring evidence from the relevant switch, assembly, and circuit documentation.

Keep the micro switch’s role separate from the valve and control logic. The switch can report a documented contact state after its actuator is operated. Whether that state corresponds to home depends on the mechanical relationship, and what the state means to the system depends on the circuit. Without evidence for those links, do not claim that a contact indication confirms home position.

The practical conclusion is narrow: identify NO and NC from the exact switch documentation at its stated reference condition, then trace the documented mechanical actuation and circuit interpretation. If any link is missing, the contact state alone does not establish the motorized valve’s home position.

This concludes the explanation of motorized valve home position micro switch NO and NC terminals.

## Sources and references

- Defense Logistics Agency ASSIST: [MIL-PRF-8805K: Switches and Switch Assemblies, Sensitive, Snap Action, General Specification For](https://quicksearch.dla.mil/qsDocDetails.aspx?ident_number=7196){: rel="nofollow noopener noreferrer" }
- Occupational Safety and Health Administration: [29 CFR 1910.333: Selection and Use of Work Practices](https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.333){: rel="nofollow noopener noreferrer" }
- Wikipedia: [Miniature snap-action switch](https://en.wikipedia.org/wiki/Miniature_snap-action_switch){: rel="nofollow noopener noreferrer" }
