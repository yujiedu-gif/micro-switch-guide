---
title: "Self locking micro switch: How its mechanism retains and resets state"
description: "self locking micro switch: Understand the operating idea, essential terminology, practical checks, limitations, and evidence needed for careful selection,."
date: 2026-09-09 09:00:00 +0800
category: Basics
tags:
  - self locking micro switch
  - micro switches
  - Basics
author: editorial_team
---

# How a Self-Locking Micro Switch Retains and Resets Its State

A **self locking micro switch** uses a mechanical feature within the switch to retain a state after the force that initiated the change is removed. That behavior differs from a momentary switch that returns as soon as its actuator force is released. It also differs from an electrical circuit that keeps a relay or other device energized after a momentary input. The distinction matters: a powered output that stays on does not, by itself, show that the switch mechanism is latched.

The set, retention, and reset sequence depends on the switch design. A retaining feature might release through a second push, a separate force, or another specified action. Force, actuator travel, contact state, and reset method therefore need to be evaluated for the particular design, rather than assumed from the words “self-locking.” The following sections explain the mechanism concept and a bounded way to check its behavior without treating any one arrangement as universal.

## What a self locking micro switch means

Mechanical self-locking means the switch mechanism physically retains a changed state after the initiating actuator force is removed. The mechanism does not simply depend on a powered circuit to preserve an output. A retaining feature within the switch holds the mechanism until its specified release or reset condition occurs.

This is a design-specific behavior, not a property to assume for every micro switch. An ordinary momentary micro switch typically returns when the applied force is removed. A switch designed with a self-locking mechanism instead has a retention step in its mechanical sequence. The precise feature and the action that releases it depend on the design documentation.

The relevant state is the switch mechanism’s position and the associated contact state, not merely whether a connected device is operating. A downstream circuit may maintain power after a momentary switch input, even though the switch itself has returned. Conversely, a mechanically retained switch may hold its state without a circuit providing that retention. These behaviors must be distinguished through mechanical observation and, where appropriate, an isolated contact check.

Definitions of actuator travel help describe the sequence but do not establish that a latch exists. Under MIL-PRF-8805K 6.5.16, **pretravel** is the distance or angle through which the actuator moves from free position to operating position. Under MIL-PRF-8805K 6.5.14, **overtravel** is the distance or angle between the operating position and the extreme position to which the actuator may be moved. These terms describe travel; whether a mechanism retains state and how it resets remain design-specific questions.

## How a self locking micro switch sets, retains, and resets

The mechanical sequence can be understood in three stages: set, retain, and reset. First, apply the actuation specified for the design. As the actuator moves through its travel, the mechanism reaches its operating position and may engage a retaining feature. The supplied definitions describe pretravel and overtravel, but they do not specify values or confirm that a particular switch contains a latch.

Second, remove the initiating force and observe the mechanism. In a self-locking design, the retaining feature keeps the mechanism in its changed state rather than allowing an immediate return. The observed contact state may correspond to that mechanically retained position, but the exact contact behavior must be confirmed for the switch. Do not infer it from an external load remaining on or turning off.

Third, perform the specified reset or release action. Depending on the design, this might be a second push, a separate release force, or another deliberate action. There is no universal reset arrangement established here. The reset action should be taken from the applicable design documentation, not guessed from the actuator’s appearance.

The terms **release force** and **releasing force** refer to a defined force or torque, not a universal reset specification. Under MIL-PRF-8805K 6.5.17, release force is the force or torque to which force on the actuator must be reduced to permit the contacts to return to the unoperated position after operation. That definition concerns return of the contacts; it does not establish that a self-locking mechanism is present or explain every design’s reset action. Use it only where the documented design and test context make it applicable.

Keep the steps separate during evaluation. A mechanism that sets correctly may fail to retain after the initiating force is removed. A mechanism that retains may fail to release through its intended reset action. Each transition is a distinct behavior to observe, and none should be treated as established merely because the actuator moved or an attached device changed state.

## Self locking micro switch versus electrical latching

Mechanical retention occurs within the switch mechanism. Electrical self-holding occurs in a circuit that maintains an output after a momentary input. These can produce a similar visible result, such as a device remaining on, but they are not the same mechanism.

For example, if a powered device continues operating after a momentary switch is released, that observation alone cannot establish that the switch itself is mechanically locked. The circuit may be maintaining the output. To distinguish the cases, consider the switch’s return and reset behavior separately from the behavior of the powered equipment.

A bounded check focuses on two observations: whether the mechanism remains in its changed position after the initiating force is removed, and whether it returns when the specified reset action is applied. Contact continuity can also be checked with power isolated, provided the contact positions and test points are known from applicable documentation. Do not use a powered output as a substitute for checking the switch mechanism or its contacts.

This distinction does not require an explanation of how to wire an electrical latching circuit. It is enough to recognize that an external circuit can preserve an output independently of mechanical retention inside the switch. If the intended behavior is unclear, the switch documentation and circuit description must be considered separately.

## Parameters and limits to verify

Evaluate force and travel using design-specific documentation. Check the specified operating force and release or reset force, along with pretravel, overtravel, and permitted actuator travel. The definitions of pretravel, overtravel, and release force do not provide universal values, tolerances, or a confirmation that a given design is self-locking. Do not substitute assumed numbers for the applicable specifications.

Confirm the contact configuration and the contact state associated with the intended set and reset positions. The mechanical position and contact transition should be treated as related observations, not assumed to be identical across designs. If the documentation does not identify the expected states or reset method, those details remain unresolved rather than inferred.

Also distinguish documented operating conditions from an improvised test. Apply only the stated actuation and reset actions, and avoid moving the actuator beyond its specified travel. A failure to latch, retain, or reset consistently can indicate a problem that needs assessment, but this information alone cannot identify a cause or establish a repair method.

A retained state should not be presumed safe or suitable for a safety function. That judgment requires an applicable assessment of the system, not merely confirmation that a switch appears to hold its position. The switch’s mechanical behavior is one component-level fact; it does not establish system-level suitability.

### Related guides

- [dual micro switch](/guides/dual-micro-switch/)
- [touch micro switch](/guides/touch-micro-switch/)
- [no nc micro switch](/guides/no-nc-micro-switch/)
- [normally open micro switch](/guides/normally-open-micro-switch/)

## How to check retention and reset safely

Before continuity checks or mechanical inspection, isolate power and confirm that the circuit is de-energized. This separates the switch’s mechanical behavior from an energized circuit’s output and avoids treating the operation of connected equipment as proof of a latch. Use the applicable documentation to identify the contact configuration, expected states, and permitted test actions.

Then apply only the documented actuation. Remove the initiating force and observe whether the mechanism retains its changed position. Next, perform the specified release or reset action and observe whether the mechanism returns as expected. If continuity is checked, do so with power isolated and compare the result with the documented contact states. These observations should be recorded separately: set, retention after force removal, and reset.

Do not force the actuator or invent a reset action if the documentation does not specify one. The available definitions describe travel and a release-force concept, but they do not supply a universal force, travel limit, contact arrangement, or reset method. Where those details are missing, the behavior cannot be verified against an assumed standard from the information here.

If the mechanism sticks, fails to retain, or does not reset consistently, stop the check rather than repeatedly forcing it. Inspect for damage, contamination, misalignment, or operation beyond specified travel as possible failure clues; these are not confirmed causes. Further assessment should follow the applicable documentation and test conditions.

In short, a **self locking micro switch** is distinguished by mechanical retention inside the switch, followed by a design-specific release or reset action. Verify those steps directly with power isolated, and keep them separate from any electrical circuit that may independently maintain an output.

## Sources and references

- Defense Logistics Agency ASSIST: [MIL-PRF-8805K: Switches and Switch Assemblies, Sensitive, Snap Action, General Specification For](https://quicksearch.dla.mil/qsDocDetails.aspx?ident_number=7196){: rel="nofollow noopener noreferrer" }
