---
title: "ATM cash cassette door micro switch actuator travel: how to assess it"
description: "atm cash cassette door micro switch actuator travel: Understand the operating idea, essential terminology, practical checks, limitations, and evidence."
date: 2026-08-26 09:00:00 +0800
category: Applications
tags:
  - atm cash cassette door micro switch actuator travel
  - micro switches
  - Applications
author: editorial_team
---

# Assessing actuator travel at a cash cassette door

The **atm cash cassette door micro switch actuator travel** should be assessed at the switch itself, not inferred from how far the door or latch moves. The goal is to compare the switch actuator’s observed movement and electrical state changes with the limits and test method for that specific switch. There is no universal travel distance that can be assumed for every cassette-door design.

This guidance applies only where a design uses the stated micro switch. Door mechanisms, linkages, mounting arrangements, and actuator forms can differ. Keep switch movement separate from door or latch displacement, and follow the authorized service process for any inspection or test involving cash-handling equipment.

## What does actuator travel mean for an ATM cash cassette door micro switch actuator travel setup?

Actuator travel is the movement of the micro switch’s actuator, measured at the switch interface. It is not necessarily equal to movement of the door, latch, or connecting linkage. A door may move through a larger distance while a lever or another actuator form at the switch moves through a different distance. The relationship depends on the mechanism’s design and mounting.

Several travel terms describe different parts of actuator movement:

- **Free position** is the actuator position before it is operated.
- **Pretravel** is the distance or angle the actuator moves from its free position to its operating position. The operating position is the point associated with the switch changing state under its specified test conditions.
- **Overtravel** is the additional distance or angle from the operating position to the extreme position to which the actuator may be moved. It describes permitted movement after operation, not the movement required to reach the operating position.
- **Release travel** is not defined by the evidence available here. Do not assign it a generic value or use it as a substitute for the documented return or release criteria for the particular switch.

These distinctions matter because a single measurement of total door movement cannot establish whether the switch reached its operating position, whether it remained within its permitted actuator travel, or whether it returned as expected. Observe movement at the actuator and assess each relevant point against the switch’s own documentation.

## Which travel limits matter for the micro switch?

The switch’s technical documentation is the reference for its operating position and permitted movement. Use the documented operating-position information to assess how far the actuator must move before the switch operates. Use the documented maximum permitted travel or overtravel information to assess how far it may move after that point. Do not treat the operating point and the extreme permitted position as interchangeable limits.

No universal distance or angle applies to all switches or cassette-door mechanisms. Actuator style, switch mounting, linkage arrangement, and mechanical tolerances can affect the movement observed at the switch. A measurement taken at the door, latch, or linkage cannot be assumed to represent actuator travel unless the design documentation establishes that relationship.

Before measuring, identify the applicable switch reference and locate the specification that governs its actuator movement. Confirm the specified measurement location, units, operating point, and permitted travel limit. If the applicable documentation or test procedure is unavailable, the limit remains unknown; do not fill the gap with a typical value or a threshold inferred from the door geometry.

Compare observations only under conditions consistent with the specified test method. A switch may change electrical state at its operating position, but that state change does not by itself show that additional movement is within the permitted overtravel. Likewise, staying within a mechanical limit does not alone establish that the circuit changed state and returned correctly. Treat mechanical travel and electrical response as related, separate checks.

## How can you verify actuator travel and switching safely?

Use the site’s approved procedures and remove power where required. Do not bypass an interlock, defeat a security mechanism, or operate restricted equipment to perform a check. If the approved procedure or access authority is unclear, stop and use the authorized service process rather than improvising a test.

A verification sequence should keep the mechanism, actuator, and electrical behavior distinguishable:

1. **Confirm the applicable reference.** Identify the switch reference and its documentation or approved test procedure. Note the stated operating position, permitted travel or overtravel, specified terminals, and relevant test conditions. Do not assume an unidentified switch has a particular limit.
2. **Inspect without forcing movement.** Visually check the switch mounting and actuator alignment, along with the visible linkage or contact area. Note apparent looseness, obstruction, or binding, but treat these as observations rather than confirmed causes. Check whether the actuator appears to return freely without pushing it beyond its limits.
3. **Measure at the actuator.** Use a suitable method to observe movement at the switch actuator, following the specified measurement location and procedure. Record the observed operating point and the extent of movement after operation only if it can be assessed without forcing the actuator beyond documented limits. Do not convert door or latch travel into switch travel without a supported relationship.
4. **Check the state transition with the circuit safely isolated.** Use the switch’s specified terminals and test procedure to verify the expected contact-state change as the actuator reaches the operating position, then verify return to the unoperated state as required by that procedure. Do not assume terminal assignments or expected electrical states that are not documented for the switch and circuit.
5. **Compare and record.** Compare measured movement and observed state changes with the applicable specification and approved test conditions. Record any mismatch or uncertainty rather than adjusting the mechanism or exceeding a travel limit to make the switch operate.

The aim is to verify both movement and state behavior without confusing them. If motion appears correct but the state transition is absent or inconsistent, record that distinction. If the electrical transition occurs but the actuator approaches or exceeds its documented permitted travel, record that separately. Neither observation alone identifies the underlying cause.

## What can inadequate or excessive travel indicate?

Actuator movement that does not reach the documented operating position may be consistent with insufficient engagement. Possible contributors include misalignment, looseness, wear, or obstruction in the mechanism. These are diagnostic clues, not definitive diagnoses. Compare the actuator’s movement and mounting with the documented limits and inspect the relevant linkage before concluding that a particular part has failed.

Movement beyond the operating position must be compared with the permitted overtravel for the specific switch. Excess compression can exceed that limit or stress the actuator. Do not treat continued movement as harmless simply because the contacts have already changed state. If the observed motion reaches or appears to pass the documented limit, stop the check as required by the approved procedure and record the discrepancy.

Inconsistent switching or failure to return to the unoperated state can be associated with binding, poor mechanical return, contact issues, or a linkage problem. The switch behavior and the mechanism behavior should be evaluated separately. For example, apparent binding at the actuator does not establish an internal switch fault, and a missing state transition does not by itself establish a door-alignment fault. Compare observations with the specified test conditions and escalate unresolved discrepancies.

A return-force definition may also help clarify what a force-based specification means: release force is the force or torque to which force on the actuator must be reduced to permit the contacts to return to the unoperated position after operation. This definition does not supply a value for a particular switch or establish a release-travel distance. Use only the applicable switch documentation for any required limit.

### Related guides

- [ball screw actuator home position micro switch replacement](/guides/ball-screw-actuator-home-position-micro-switch-replacement/)
- [bottling machine end of stroke micro switch](/guides/bottling-machine-end-of-stroke-micro-switch/)
- [automated guided vehicle home position micro switch location](/guides/automated-guided-vehicle-home-position-micro-switch-location/)
- [accelerator pedal position stop micro switch operating force](/guides/accelerator-pedal-position-stop-micro-switch-operating-force/)

## What should be recorded after checking travel?

Make the check reproducible by recording the switch reference, measurement location, method, and relevant specification limits. Note the observed operating point and any post-operation movement assessed against the documented permitted travel. Record the test conditions required by the approved procedure, including whether the circuit was safely isolated for the state check.

Document whether the expected electrical state changed at operation and returned consistently under the approved test conditions. Keep the recorded mechanical observations separate from the electrical result. If a measurement could not be made safely or a required specification was unavailable, record that limitation instead of supplying an assumed value.

Cassette-door designs differ, and these points apply only where the design uses the stated micro switch. Escalate discrepancies through the authorized service process. Do not adjust or defeat a security mechanism outside approved procedures. A clear record of the switch reference, observed movement, state transition, return behavior, and comparison basis lets qualified service personnel investigate the specific mechanism without relying on a generic travel threshold. Use the **atm cash cassette door micro switch actuator travel** reference only with the applicable switch documentation and approved test conditions.

## Sources and references

- Defense Logistics Agency ASSIST: [MIL-PRF-8805K: Switches and Switch Assemblies, Sensitive, Snap Action, General Specification For](https://quicksearch.dla.mil/qsDocDetails.aspx?ident_number=7196){: rel="nofollow noopener noreferrer" }
