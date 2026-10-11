---
title: "What Is Micro Switch Total Travel?"
description: "Learn what is micro switch total travel, how it differs from pretravel, and what to check when interpreting actuator movement in a switch specification."
date: 2026-10-11 09:00:00 +0800
category: Basics
tags:
  - what is micro switch total travel
  - micro switches
  - Basics
author: editorial_team
---

# What Is Micro Switch Total Travel?

When readers ask **what is micro switch total travel**, they are asking how far the actuator moves across a specified part of its movement. Total travel describes an actuator’s movement between stated reference points. The term is useful only when those endpoints and the measurement conditions are clear; the accepted definitions here do not establish a universal numerical value or one universal endpoint convention for total travel.

A miniature snap-action switch can change an electrical contact state in response to mechanical actuator movement and is commonly used for position or limit detection. In that context, actuator travel helps describe the movement associated with the switch. It should not be treated as a substitute for the separately defined terms pretravel and overtravel. To interpret a stated total-travel value, first establish which points the specification measures between and how the measurement was made.

## What Is Micro Switch Total Travel?

Total travel is a description of the actuator’s movement over an interval whose endpoints must be identified in the applicable technical documentation. In plain English, it tells the reader how much movement is being considered from one specified actuator position to another. The term alone does not say whether the measurement begins at free position, ends at an extreme position, or uses another pair of reference points. Do not assume those endpoints when they are not stated.

That qualification matters because the accepted definitions for pretravel and overtravel identify particular endpoints, while the supplied evidence does not give a standalone definition of total travel. A specification may use total travel to describe a full or broader movement range, but its exact meaning depends on the documentation’s stated reference points. Read the value together with its definition rather than interpreting the label in isolation.

A travel measurement may be expressed as a distance or an angle, depending on the actuator and the documentation. Check the stated unit and the actuator configuration before interpreting the value. A linear displacement and an angular movement are not interchangeable measurements, even when both describe actuator motion. The value also needs to be read under the stated measurement or test conditions; without those conditions, a reader cannot safely assume how the measurement was taken.

There is no universal total-travel value to assume for every micro switch. Travel values vary with switch design, and a number given for one design should not be carried over to another without evidence that the reference points and conditions match. This is a measurement distinction, not a statement that any particular travel amount is suitable for an application.

For example, imagine a specification that reports an actuator movement between two labeled positions but does not identify those labels in the excerpt a reader has. The number alone is not enough to determine what interval it represents. The reader would need the relevant documentation to identify the endpoints, unit, actuator arrangement, and any stated test conditions. This conceptual example uses no dimensions or model-specific claims; it illustrates why the reference points are part of the meaning.

## How Total Travel Differs From Pretravel and Overtravel

Pretravel has a specific definition in MIL-PRF-8805K, Section 6.5.16: it is the distance or angle through which the actuator moves from free position to operating position. In other words, its starting point is free position and its ending point is operating position. A pretravel value should therefore be understood as movement across that defined interval, not as an unspecified measure of all actuator movement.

Overtravel is separately defined in MIL-PRF-8805K, Section 6.5.14. It is the distance or angle between the operating position and the extreme position to which the actuator may be moved. Its interval begins at operating position and extends to the stated extreme position. Because the endpoints differ from those of pretravel, overtravel describes a different portion of actuator movement.

Operating position is the shared reference between these definitions: it is the endpoint of pretravel and the starting point of overtravel. The supplied evidence does not define operating position further, so it should be identified according to the applicable technical documentation rather than assigned an unsupported explanation. The definitions also do not establish a numerical relationship among pretravel, overtravel, and total travel for every switch design.

A useful non-numeric way to keep the terms distinct is to follow the named positions. From free position to operating position is pretravel. From operating position to the extreme position to which the actuator may be moved is overtravel. A total-travel figure must be read according to the endpoints its own specification gives; it should not automatically be equated with either of those intervals or assumed to equal their sum.

This distinction prevents a common interpretation error: treating all travel labels as if they referred to the same span of motion. If a document gives pretravel, overtravel, and total travel, inspect each definition and its reference points independently. If it gives only a travel number without defining the interval, the number’s relationship to operating position remains unresolved until the applicable documentation clarifies it.

## How to Interpret a Total-Travel Specification

Start by locating the definition attached to the stated total-travel value. Identify the starting and ending positions, then note whether the movement is specified as a distance or an angle. Confirm the actuator configuration described by the document and read any stated measurement or test conditions. These details establish what the value represents; the label alone does not supply them.

Next, keep the reference points consistent when comparing values. A measurement from free position to operating position is the defined pretravel interval, while a measurement from operating position to an extreme position is the defined overtravel interval. If another document uses different endpoints for its total-travel figure, the numbers do not describe the same interval merely because both use a travel label. Comparisons require matching reference points, units, actuator configuration, and stated conditions.

Also preserve the distinction between a value and its scope. The accepted evidence gives definitions for pretravel and overtravel, but it does not provide a universal total-travel definition, numerical range, tolerance, or test procedure. Do not infer those details from the two related definitions. Look to the applicable technical documentation for the meaning of a particular total-travel specification and for any additional parameters it states.

Switch designs can have different travel values, so one documented figure should not be treated as a general benchmark. Nor does a travel value by itself establish that a switch is appropriate for a particular use or compatible with a particular setup. Those conclusions require evidence beyond the movement measurement. Keeping the interpretation limited to the stated interval avoids turning a dimensional description into an unsupported suitability claim.

A practical reading sequence is simple: find the endpoints; verify distance or angle units; confirm the actuator configuration; check the stated conditions; then interpret or compare the value only within that scope. If one of these details is missing, describe the uncertainty rather than filling it in by assumption. For related questions, consult material that specifically addresses operating force, operating position, or how to read a datasheet; those topics are not established by a total-travel figure alone.

### Related guides

- [what is a micro switch actuator](/guides/what-is-a-micro-switch-actuator/)
- [how long do micro switches last](/guides/how-long-do-micro-switches-last/)
- [how to wire a micro switch](/guides/how-to-wire-a-micro-switch/)
- [micro switch com](/guides/micro-switch-com/)

## What Is Micro Switch Total Travel Useful For?

Total travel is useful as a way to describe an amount of actuator movement when the specification clearly states the interval. It gives readers a measurement to interpret alongside the defined positions and conditions in the relevant documentation. In a miniature snap-action switch, mechanical actuator movement can change an electrical contact state, and such switches are commonly used for position or limit detection. This general context does not establish that a particular travel value suits a particular application.

The measurement can also help readers distinguish a broad movement description from the narrower, defined intervals of pretravel and overtravel. Pretravel runs from free position to operating position; overtravel runs from operating position to the extreme position to which the actuator may be moved. A total-travel value may use endpoints that are not specified in the term alone, so its role is to describe the documented interval, not to replace those definitions.

For a clear interpretation, retain the reference points, units, actuator arrangement, and stated measurement conditions whenever recording or discussing a travel value. Without them, a number can be detached from the measurement it was meant to describe. Avoid assuming that two figures are comparable just because both concern actuator movement, and do not infer performance or application fit from travel alone.

In short, **what is micro switch total travel** depends on the endpoints specified for that measurement. It describes actuator movement across a documented interval, while pretravel and overtravel each have their own defined reference points. Check the applicable technical documentation before assigning a meaning to a total-travel value, and do not assume a universal number or endpoint convention.

## Sources and references

- Defense Logistics Agency ASSIST: [MIL-PRF-8805K: Switches and Switch Assemblies, Sensitive, Snap Action, General Specification For](https://quicksearch.dla.mil/qsDocDetails.aspx?ident_number=7196)
- Wikipedia: [Miniature snap-action switch](https://en.wikipedia.org/wiki/Miniature_snap-action_switch)
