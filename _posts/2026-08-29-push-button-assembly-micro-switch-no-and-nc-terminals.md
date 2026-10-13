---
title: "Push Button Assembly Micro Switch NO and NC Terminals"
description: "push button assembly micro switch NO and NC terminals: Understand the operating idea, essential terminology, practical checks, limitations, and evidence."
date: 2026-08-29 15:07:30 +0800
last_modified_at: 2026-10-13 11:46:37 +0800
category: Basics
tags:
  - push button assembly micro switch NO and NC terminals
  - micro switches
  - Basics
author: editorial_team
---

A push button assembly may use a micro switch to convert button movement into a change in electrical contact state, but the assembly and the switch are not the same component. The **push button assembly micro switch NO and NC terminals** can be interpreted only against the switch’s documented contact arrangement and reference condition. Do not infer their identities from terminal position, a button’s appearance, or the behavior of the equipment.

First establish whether the assembly contains a micro switch and how its button or linkage moves the switch actuator. Then use documentation to identify the contact pair and stated reference state. An isolated continuity check at defined actuator states can check that pair’s behavior; it does not establish that the installed circuit or equipment is functioning correctly.

## What push button assembly micro switch NO and NC terminals describe

A push button is the external part a person presses. In some assemblies, its movement is transmitted through a plunger, lever, or other mechanical connection to an electromechanical micro switch. Other assemblies may use a different mechanism or component. Without documentation for the particular assembly, the presence of a micro switch, its terminal arrangement, and its role in the host equipment remain unknown.

When the particular switch has documented normally open (NO) and normally closed (NC) contacts, those labels describe contact state relative to a specified reference condition. The reference might be identified in the switch or assembly documentation as unactuated, but do not assume that condition if the documentation does not say so. “Normally” does not, by itself, establish how the assembly is installed or what the equipment does.

NO and NC are contact-state labels, not guarantees about current flow in an installed circuit. Whether a contact carries current depends on the actual wiring and circuit. A diagram or marking that applies to the exact switch or assembly is the basis for identifying terminals; terminal location or appearance alone is not.

This distinction matters because several questions can sound alike but are different: whether the button moves, whether that movement reaches the switch actuator, which terminals form a documented contact pair, and whether the equipment responds. A finding about one does not automatically answer the others. The task here is limited to interpreting and checking documented contact behavior, not determining the assembly’s control logic.

## How button movement reaches the micro switch actuator

The button’s mechanical path depends on the assembly design. Pressing the button may move a linkage or other part that, in turn, moves the micro switch actuator. The actuator is the part of the switch moved by the external mechanism. Do not assume a particular linkage, direction of motion, or amount of travel without design information.

If the button is stuck, obstructed, or misaligned, its movement may not reach or release the actuator as intended. That is a mechanical-input question, distinct from whether the switch’s contacts change state. Conversely, a button can appear to move while an internal contact problem or a separate equipment-side fault remains possible. Observing button motion alone does not prove contact operation.

The switch’s operating point is the point at which operation occurs; the release point is a different event. Pretravel is motion from the free position to the operating position, and overtravel is motion after the operating position up to the extreme permitted actuator position. These terms describe actuator movement, not a universal movement distance for every design. Do not use them to infer an undocumented travel requirement or to diagnose a particular assembly without its information.

A click may accompany snap action in a design that uses that mechanism, but sound alone does not identify terminals or prove electrical continuity. Likewise, the equipment’s response to pressing a button does not establish which contact pair changed state. Its behavior depends on the actual circuit and equipment design, which are outside the scope of a terminal-state check.

## Identify NO and NC behavior at a defined reference state

Start with the documentation for the exact switch or assembly. Use its connection diagram, terminal markings, and stated contact reference condition to identify the documented contact pair. If the reference condition, terminal identities, or pair arrangement is missing or unclear, those details remain unresolved. Do not substitute a generic physical layout or a presumed terminal position.

For a documented NO/NC arrangement, interpret each label only relative to the documented reference state. If the documentation defines the unactuated condition as the reference, then the labels describe contact state in that condition. The state when the actuator is moved must be established from the documented arrangement and a check, not guessed from the labels alone. If another reference condition is specified, follow that condition rather than silently treating the unactuated state as the reference.

A bounded check concerns the isolated switch, the identified terminal pair, and a defined actuator state. With the switch isolated from the equipment circuit, use an appropriate continuity-measuring method across the documented pair. Record the actuator state for each observation, such as the documented unactuated reference condition and a specified actuated condition, and compare the observed continuity behavior with the switch documentation. The method and expected behavior must be defined for the switch being checked; the available information here does not specify a meter setting or a universal expected reading.

Keep each observation tied to what was actually tested: the terminal pair, isolation condition, actuator state, and measurement method. A click is not a continuity result. Nor does an apparent open or closed reading identify an undocumented terminal pair; first establish terminal identity from documentation. If the result does not match the documented arrangement, it is evidence about that isolated check under those conditions, not a complete diagnosis of the assembly.

### Related guides

- [micro switch flyback diode causes](/guides/micro-switch-flyback-diode-causes/)
- [panel mount plunger micro switch working principle](/guides/panel-mount-plunger-micro-switch-working-principle/)
- [cam follower micro switch adjustment](/guides/cam-follower-micro-switch-adjustment/)
- [micro switch SPST NC contacts explained](/guides/micro-switch-spst-nc-contacts-explained/)

## What a continuity result can and cannot establish

A continuity observation can describe the behavior of the isolated switch across the documented pair in the tested actuator state and under the chosen measurement method. It cannot, by itself, show that the button linkage moves correctly through its full intended path, that every contact in the switch has been checked, or that the installed equipment circuit is correct. It also cannot establish load suitability, installed current flow, or equipment behavior.

Keep possible causes separate when a symptom remains. A mechanical input problem concerns whether button motion reaches or releases the actuator. An internal contact problem concerns the switch’s contact behavior under a defined check. Terminal identification uncertainty means the tested pair may not be the documented pair. A wiring issue concerns the connections in the installed circuit. A fault elsewhere concerns another part of the equipment. One observation should not collapse these into a single diagnosis.

If the documentation does not establish the reference state, contact pair, or terminal identities, do not infer those facts from physical layout, a click, or installed behavior. If the isolated check conflicts with documentation, the observation does not by itself identify why. The connection diagram, terminal marking, circuit function, and permissible load for the exact switch and equipment govern their respective questions; ratings are tied to stated load and test conditions, not universal switching capacities.

The **push button assembly micro switch NO and NC terminals** describe contact states only when the documented reference condition and terminal arrangement are known. A defined, isolated continuity check can compare a documented contact pair across stated actuator states. Its conclusion remains limited to that check and does not prove the installed circuit, control logic, or complete assembly function.

## Sources and references

- Defense Logistics Agency ASSIST: [MIL-PRF-8805K: Switches and Switch Assemblies, Sensitive, Snap Action, General Specification For](https://quicksearch.dla.mil/qsDocDetails.aspx?ident_number=7196){: rel="nofollow noopener noreferrer" }
- Occupational Safety and Health Administration: [29 CFR 1910.333: Selection and Use of Work Practices](https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.333){: rel="nofollow noopener noreferrer" }
- Wikipedia: [Miniature snap-action switch](https://en.wikipedia.org/wiki/Miniature_snap-action_switch){: rel="nofollow noopener noreferrer" }
