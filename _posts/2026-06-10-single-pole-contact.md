---
title: "Single pole contact: What It Means in a Micro Switch"
description: "single pole contact: Learn what one pole means in a micro switch, how it differs from a double pole contact, and what to verify before interpreting terminals."
date: 2026-06-10 09:00:00 +0800
last_updated: 2026-10-11 09:00:00 +0800
category: Basics
tags:
  - single pole contact
  - micro switches
  - Basics
author: editorial_team
---

# Single Pole Contact in a Micro Switch

The term **single pole contact** describes how a switch contact arrangement controls a switching path, but the phrase alone is not a complete description of a micro switch. It does not identify the terminals, show their physical positions, or establish the switch’s electrical ratings. Understanding that distinction helps prevent a broad contact term from being treated as a wiring instruction or a promise of application suitability.

In general switch terminology, pole count describes the number of switching paths controlled by the switch. A single-pole arrangement refers to one path; a double-pole arrangement refers to two. That high-level contrast does not, by itself, specify how a particular device’s contacts are arranged or operated. Model-specific details must be confirmed in the device markings and applicable documentation.

## What does single pole contact mean?

In switch contact terminology, a **pole** refers to a switching path or circuit controlled by the switch. With that scope, a **single pole contact** means the contact arrangement is described as controlling one switching path. The term is about contact organization. It is not a complete specification of the switch, and it does not establish every detail of the internal contact arrangement.

The phrase should not be read as a terminal count. It does not tell you how many terminals a device has, what each terminal is called, or where any terminal is physically located. A switch’s terminal layout and contact behavior require device-specific evidence, such as its markings and applicable documentation. Without that evidence, the details remain unresolved.

Pole count also does not tell you the contact’s state in a particular position. It does not establish whether a contact is normally open or normally closed, identify a common terminal, or describe how contacts change state during operation. Those concepts concern terminal identity and switching behavior, not simply the number of poles.

Contact terminology should also be kept distinct from force, travel, and position terminology. In the scope of MIL-PRF-8805K section 6.5, the specification distinguishes actuating force, releasing force, free position, operating position, movement differential, pretravel, and overtravel. Those terms describe other operating characteristics; their presence does not define pole count or establish terminal labels.

## How does a single pole contact differ from a double pole contact?

At a high level, the distinction is the number of switching paths described: a single-pole arrangement has one path, while a double-pole arrangement has two. This is a useful terminology contrast, but it does not provide a complete account of either device’s internal construction or operating sequence.

Pole count should not be confused with throw count. The words “single pole” and “double pole” address the number of poles, not, by themselves, how many contact positions or alternate paths are available. A pole count alone therefore cannot establish a complete contact configuration. Further terms and device-specific information would be needed to describe the arrangement accurately.

Nor does the contrast establish how contacts are coordinated. The term “double pole” alone does not confirm that two paths change state simultaneously, or define the exact sequence or state of either path. Avoid treating the label as evidence for such details unless the applicable documentation specifies them.

| Term | High-level meaning | What the term alone does not establish |
|---|---|---|
| Single pole | One switching path is described. | Terminal labels, physical layout, contact state, or electrical rating. |
| Double pole | Two switching paths are described. | Whether the paths operate simultaneously, their terminal identities, or their ratings. |

The comparison is limited to contact organization. It does not imply that single-pole and double-pole devices have equivalent voltage, current, or load ratings, or that either arrangement is suitable for a particular application. Those questions require evidence for the specific device and intended conditions.

## What single pole contact does not tell you

The phrase does not identify COM, NO, or NC terminals. Those labels refer to terminal roles or contact states, while pole count describes the number of switching paths. A single-pole label is therefore not enough to assign a terminal name, infer which contacts are connected in a given state, or locate a terminal on the device body.

Pole count also does not establish voltage or current ratings. It says nothing by itself about the load type or the conditions under which a device may be used. A contact arrangement and an electrical rating are separate pieces of information. Do not infer application suitability from the words “single pole” or “double pole.”

The term does not verify the internal arrangement of a particular micro switch, either. Two devices described with the same pole count may still require separate documentation to determine their specific terminals, contact behavior, and ratings. Without an exact model and supporting evidence, those details cannot be settled from the general term.

It is equally important not to treat pole count as a wiring diagram. A broad category name cannot show which contacts connect in each position or provide instructions for a particular circuit. Wiring and load decisions are outside what this terminology establishes and require the relevant device information and circuit requirements.

### Related guides

- [what is a micro switch actuator](/guides/what-is-a-micro-switch-actuator/)
- [reed contact sensor](/guides/reed-contact-sensor/)
- [genki force field lite](/guides/genki-force-field-lite/)
- [electrical switch gear](/guides/electrical-switch-gear/)

## How to interpret the term on a micro switch

Start with the switch’s own markings and applicable documentation. Use those sources to establish model-specific terminal identities, contact arrangement, and electrical ratings. If a marking is unclear or the documentation does not resolve a detail, do not fill the gap by assuming that pole count reveals it.

Keep the questions separate: pole count concerns the number of switching paths; terminal identification concerns which device terminals serve particular roles; ratings concern permitted electrical conditions. The phrase **single pole contact** answers only the first question at a high level. It is not, by itself, enough to identify terminals, choose a wiring arrangement, or decide whether a switch is suitable for an application.

For adjacent tasks, consult dedicated guidance on terminal identification and circuit configuration, as well as the documentation for the specific device. Treat each as a separate question rather than extending the general pole-count label beyond what it says. In short, single pole describes one switching path and double pole describes two, but neither phrase alone supplies a complete contact configuration or device specification.

## Sources and references

- Defense Logistics Agency ASSIST: [MIL-PRF-8805K: Switches and Switch Assemblies, Sensitive, Snap Action, General Specification For](https://quicksearch.dla.mil/qsDocDetails.aspx?ident_number=7196){: rel="nofollow noopener noreferrer" }
