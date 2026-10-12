---
title: "no nc micro switch: What Normally Open and Normally Closed Mean"
description: "no nc micro switch: Understand the operating idea, essential terminology, practical checks, limitations, and evidence needed for careful selection,."
date: 2026-07-26 09:00:00 +0800
category: Basics
tags:
  - no nc micro switch
  - micro switches
  - Basics
author: editorial_team
---

The phrase **no nc micro switch** refers to the normally open (NO) and normally closed (NC) contact behavior associated with a switch. These terms describe electrical contact states relative to the switch’s unactuated, or resting, condition. They do not mean that every switch has both contacts, or that NO and NC are separate kinds of switches. To identify the actual terminals and confirm how they behave, use the device’s schematic and check continuity with power disconnected.

A switch may provide a changeover arrangement with a common terminal and NO and NC terminals. Other contact configurations are possible, and the terminal layout is not universal. The basic interpretation is state-based: first note the contact condition at rest, then operate the actuator and compare the condition. This distinction helps prevent a common error: reading “normally” as a description of the switch after it has been operated.

## What “no nc micro switch” means

“Normally” refers to the switch’s unactuated state. In that resting condition, a normally open contact has an open electrical path. A normally closed contact has a closed electrical path. In practical terms, open means the contact path does not provide continuity; closed means it does. These labels describe contact behavior, not the physical appearance of a terminal or the name of a particular switch type.

In a changeover arrangement, the common terminal can connect to one contact path at rest and to the other after the switch changes state. The common terminal is identified as COM, the normally closed terminal as NC, and the normally open terminal as NO. These are common markings, not a guarantee that every switch uses those labels or offers all three terminals. Check the exact device schematic rather than assuming a universal layout.

The terms also should not be treated as complete descriptions of every switch. A device may have a different contact configuration, and the available evidence does not establish that every micro switch includes both NO and NC contacts. The useful question is narrower: what is the contact condition in the unactuated state, and what condition follows when the switch is operated? The markings and schematic help identify the intended terminals, while a continuity check can verify the actual behavior.

## How a micro switch changes NO and NC contact states

When the actuator is pressed or otherwise operated, the switch changes the electrical state of its contacts. For a normally open contact, the path is open at rest and changes to closed when the switch is actuated. For a normally closed contact, the path is closed at rest and changes to open when the switch is actuated. In a changeover arrangement, the common connection changes from one contact path to the other.

This description concerns the electrical contacts, not a particular mechanical design. “Actuated” means the switch has been operated; it does not specify a required force, travel distance, actuator shape, or application. Those details vary and cannot be inferred from the NO or NC label alone. The terms identify how a contact behaves around the unactuated reference state, not what physical motion produces that transition.

Keep the state reference consistent when interpreting labels or test results. At rest, NO is open and NC is closed. After actuation, their contact states change. Calling a contact “normally open” does not mean it stays open in every position, and “normally closed” does not mean it stays closed after operation. The names refer to the normal, unactuated condition rather than an unconditional state.

## How to identify and verify NO and NC terminals

Use a continuity meter only with power disconnected and the switch isolated from connected circuitry. Isolation matters because other circuit paths can affect a reading. Do not infer the terminal arrangement from appearance alone: consult the exact device schematic or terminal markings, and treat them as specific to that switch.

A bounded check is:

1. Disconnect power and isolate the switch from connected circuitry.
2. Set the meter to continuity mode and identify the terminals using the switch’s schematic or markings.
3. Leave the actuator unoperated. Check the suspected contact paths and note which path has continuity and which is open.
4. Operate the actuator, then check the same paths again.
5. Compare the two readings. A normally open path is open at rest and closed when actuated; a normally closed path is closed at rest and open when actuated.

For a changeover arrangement, use the documented COM terminal as the reference when checking the NO and NC paths. Do not assume that a particular terminal is COM based only on its position. The labels COM, NO, and NC are common changeover terminology, but the exact schematic is the relevant reference for an individual device.

A continuity check confirms the observed open or closed behavior under the test conditions. It does not establish a universal terminal layout or identify an undocumented contact configuration. If the switch’s schematic is unavailable or the terminals cannot be identified, the test results alone may not establish which terminal is intended to be NO or NC. Describe the observed behavior by state rather than assigning unsupported terminal names.

### Related guides

- [dual micro switch](/guides/dual-micro-switch/)
- [touch micro switch](/guides/touch-micro-switch/)
- [normally open micro switch](/guides/normally-open-micro-switch/)
- [float switch mechanism micro switch contact rating](/guides/float-switch-mechanism-micro-switch-contact-rating/)

## Common interpretation errors with NO and NC micro switches

The first common error is confusing the unactuated state with the actuated state. NO and NC are defined relative to rest. A reading taken only while the actuator is pressed cannot, by itself, show which path is normally open or normally closed. Compare both states and keep the resting condition as the reference.

Another error is assuming every switch has the same contact arrangement or terminal placement. COM, NO, and NC are common markings in changeover terminology, not proof that every device has three terminals or uses that layout. Appearance alone is not enough to assign terminal functions. Use the device schematic where available, then verify the contact behavior with the switch isolated and unpowered.

If the readings do not change as expected, do not immediately conclude that the switch has failed. Check that power is disconnected, the switch is isolated from connected circuitry, the meter is in continuity mode, and the actuator is actually being operated. Then compare the observations with the documented contact configuration. These checks keep the conclusion limited to interpreting NO and NC contact states rather than diagnosing a larger device.

The essential distinction is simple: NO is open at rest and closes when actuated; NC is closed at rest and opens when actuated. Terminal labels can help, but layouts and contact configurations vary. For a **no nc micro switch**, identify terminals from its schematic and verify both resting and actuated conditions with an unpowered continuity check.

## Sources and references

- Defense Logistics Agency ASSIST: [MIL-PRF-8805K: Switches and Switch Assemblies, Sensitive, Snap Action, General Specification For](https://quicksearch.dla.mil/qsDocDetails.aspx?ident_number=7196){: rel="nofollow noopener noreferrer" }
- Wikipedia: [Miniature snap-action switch](https://en.wikipedia.org/wiki/Miniature_snap-action_switch){: rel="nofollow noopener noreferrer" }
