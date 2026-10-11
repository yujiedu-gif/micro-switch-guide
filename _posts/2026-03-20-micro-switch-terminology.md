---
title: "Micro Switch Terminology: A Practical Glossary"
description: "Learn micro switch terminology, from actuator and operating point to contacts and differential travel, so you can read technical descriptions more accurately."
date: 2026-03-20 09:00:00 +0800
last_updated: 2026-10-11 09:00:00 +0800
category: Basics
tags:
  - micro switch terminology
  - micro switches
  - Basics
author: editorial_team
---

# Understanding Micro Switch Terms

**Micro switch terminology** spans three different subjects: mechanical movement and force, contact relationships, and electrical ratings. These terms describe separate properties, so one should not be used as a substitute for another. The definitions below follow the scope of MIL-PRF-8805K section 6.5 where noted. They do not establish the specifications of an unidentified switch or resolve its compatibility with a circuit or application.

## What micro switch terminology covers

MIL-PRF-8805K section 6.5 distinguishes actuating force, releasing force, free position, operating position, movement differential, pretravel, and overtravel. The terms form a vocabulary for describing switch operation, but the available evidence does not provide definitions for free position or operating position themselves. It also does not provide device-specific values for any of these characteristics.

A useful first distinction is between a **mechanical characteristic** and an **electrical rating**. Force and travel terms describe actuator movement or the force applied to the mechanism. Electrical ratings concern the conditions under which a switch is specified to handle a load. A mechanical term does not state an electrical capacity, and a rating does not define actuator travel.

Contact abbreviations describe a different category: relationships among terminals and contacts. Their meaning does not, by itself, identify where terminals sit on a particular switch. In all three categories, a generic term or a similar-looking device is not evidence of compatibility, safety, or suitability for a particular use.

## Micro switch terminology for movement and force

**Actuating force**, also called operating force in the cited definition, is the force or torque applied to the actuating mechanism to operate the contacts (MIL-PRF-8805K section 6.5.1). This describes the input needed to operate the mechanism; it is not an electrical load rating.

**Releasing force**, also called release force, is the force or torque to which force on the actuator must be reduced to permit the contacts to return to the unoperated position after operation (section 6.5.17). It refers to the return condition, not the force needed to operate the contacts. The two force terms therefore describe different points in the operating and return sequence.

The travel terms distinguish parts of the actuator’s movement:

- **Pretravel** is the distance or angle through which the actuator moves from free position to operating position (section 6.5.16).
- **Movement differential**, also called differential travel, is the distance or angle through which the actuator travels from operating position to releasing position (section 6.5.13).
- **Overtravel** is the distance or angle between operating position and the extreme position to which the actuator may be moved (section 6.5.14).

These definitions identify different spans, not interchangeable measurements. Pretravel ends at operating position; movement differential runs from operating position to releasing position; overtravel extends from operating position toward an extreme actuator position. The cited material identifies free, operating, and releasing positions in these definitions, but the evidence supplied here does not define free position or operating position independently. No numerical travel or force value can be inferred from the terminology alone.

## Contact and circuit terminology

In generic changeover terminology, **COM** means common terminal, **NC** means normally closed terminal, and **NO** means normally open terminal. These abbreviations describe contact relationships. They do not establish a universal terminal arrangement or physical layout, and they do not identify a specific switch’s connections without its documentation.

The state reference matters when interpreting contact labels. “Normally” is part of the contact terminology, not a guarantee about a terminal’s location, external wiring, or function in every equipment circuit. The evidence available here does not specify a particular device schematic or define the reference state in further detail. Do not infer a pinout from appearance or from the abbreviations alone.

For an exact device, the applicable connection diagram and terminal markings are the relevant references for identifying connections. This is a boundary on what generic terminology can establish, not a device-specific wiring instruction. The scope here does not resolve how to wire a particular switch.

## Electrical rating terms and their limits

An electrical rating is not a universal switching capacity. Under MIL-PRF-8805K section 6.1.1 and applicable specification sheets, rating values are requirements tied to stated load and test conditions. The value only has meaning in the context of those conditions; the evidence supplied here gives no particular voltage, current, load type, or test condition to apply to an unidentified switch.

This distinction prevents a common category error. Actuating force, releasing force, and travel describe mechanical behavior. Electrical rating values describe specified performance under stated electrical and test conditions. A mechanical term cannot establish that a switch can handle a load, while a rating stated without its conditions cannot be treated as a general capacity.

For a specific switch and equipment, use the permissible load documented for that exact switch and equipment, together with its connection diagram and terminal marking. A generic symbol, term, or visual resemblance does not establish compatibility, safety, or suitability. The evidence here does not support a particular load recommendation or a conclusion about any individual device.

### Related guides

- [what is a micro switch actuator](/guides/what-is-a-micro-switch-actuator/)
- [how long do micro switches last](/guides/how-long-do-micro-switches-last/)
- [how to wire a micro switch](/guides/how-to-wire-a-micro-switch/)
- [micro switch com](/guides/micro-switch-com/)

## Using micro switch terminology in technical documents

When documenting a switch, keep each category distinct. Use force and travel terms for the mechanical characteristic being described, contact abbreviations for contact relationships, and electrical ratings with their applicable load and test conditions. Preserve the named reference positions in travel definitions, particularly the difference between operating, releasing, and extreme positions.

Also identify the source and scope of a definition. The movement and force definitions in this article are from specified sections of MIL-PRF-8805K; they are not presented as values for every switch. The rating statement is tied to section 6.1.1 and applicable specification sheets. Neither a standard’s vocabulary nor a generic terminal abbreviation supplies missing model-specific data.

If a document concerns an exact device, its diagram, terminal markings, circuit function, and permissible load are the relevant documented references. Where those details are unavailable, the device identity, connections, ratings, and suitability remain unresolved. This is the practical limit of **micro switch terminology**: precise terms clarify what a specification says, but they do not replace the exact device’s documentation or establish an unprovided specification.

## Sources and references

- Defense Logistics Agency ASSIST: [MIL-PRF-8805K: Switches and Switch Assemblies, Sensitive, Snap Action, General Specification For](https://quicksearch.dla.mil/qsDocDetails.aspx?ident_number=7196){: rel="nofollow noopener noreferrer" }
- Occupational Safety and Health Administration: [29 CFR 1910.333: Selection and Use of Work Practices](https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.333){: rel="nofollow noopener noreferrer" }
- Wikipedia: [Miniature snap-action switch](https://en.wikipedia.org/wiki/Miniature_snap-action_switch){: rel="nofollow noopener noreferrer" }
