---
title: "switch schematic: How to Read Switch Symbols and Contact States"
description: "switch schematic: Understand the operating idea, essential terminology, practical checks, limitations, and evidence needed for careful selection,."
date: 2026-10-11 18:01:49 +0800
category: Basics
tags:
  - switch schematic
  - micro switches
  - Basics
author: editorial_team
---

# How to Read a Switch Schematic Without Guessing Terminal Locations

A **switch schematic** represents electrical relationships and contact states; it is not necessarily a picture of the switch’s shape or terminal layout. Reading the drawing means following its symbols, lines, and stated reference conditions. It does not mean that the symbol’s position reveals where a terminal sits on the physical component.

This distinction matters when a schematic shows a changeover contact with labels such as COM, NO, and NC. Those labels describe contact roles in the drawing’s terminology, but exact markings and the device documentation control how a particular switch is identified. The diagram alone does not establish ratings, compatibility, or a complete installation procedure. The sections below explain how to interpret the represented path and states while keeping those limits clear.

## What a switch schematic shows

A schematic is a symbolic representation of circuit relationships. It indicates how the drawn parts connect and, where shown, how a switch contact can interrupt or complete a represented path. The symbols are not necessarily drawn to scale, and their arrangement on the page does not need to match the component’s physical construction.

A switch symbol should therefore be read as diagram information, not as a photograph or terminal map. A line leading to a contact identifies a connection in the represented circuit. The contact symbol indicates the relationship between the parts of that circuit under the state the drawing depicts. Neither fact, by itself, tells you which physical screw, blade, pin, or other terminal occupies a particular location on a housing.

Read symbols in the context of the complete drawing. A legend, notation, or accompanying equipment documentation may define conventions or explain which state is illustrated. If the drawing does not make a convention clear, do not assume that a familiar-looking symbol has a particular meaning beyond what the documentation supports. Different diagrams can use different conventions or show different views of a circuit.

The drawing’s purpose also matters. A circuit schematic can explain electrical relationships without showing component shape, mounting, dimensions, or terminal orientation. A physical illustration may show a component’s appearance while omitting internal contact behavior. When a document includes both, use each for the information it actually provides rather than treating one as a substitute for the other.

In short, separate three questions: what path the schematic represents, what contact state it depicts, and where the corresponding terminals are physically located. The first two may be described by the diagram. The third requires verified device-specific information.

## How to read switch schematic contact states

An open contact is represented as a break in the circuit path at that contact. A closed contact is represented as a connected path through the contact. These are circuit states in the schematic. They describe whether the represented path is interrupted or continuous in the state being shown; they do not, on their own, identify a physical terminal position.

The terms “normally open” and “normally closed” need a reference condition. Do not infer that condition from the words alone if the drawing or its documentation does not specify it. Use the applicable reference condition stated by the diagram or equipment documentation, and interpret the contact state in that context. If the document distinguishes a rest state from an actuated state, keep those states separate: the represented contact relationship may differ between them.

For a generic changeover contact, COM means common terminal, NO means normally open terminal, and NC means normally closed terminal. A generic changeover contact may be labeled common, normally closed, and normally open, but the exact device marking or schematic controls. These terms help describe the relationship shown in the drawing; they are not a universal physical layout. Confirm the particular device’s notation in its exact documentation before assigning a physical terminal identity.

When a schematic shows more than one state, compare the contact relationships in each state rather than assuming that the first drawing is the only possible condition. Follow any state labels, notes, or legend entries supplied with the drawing. If it shows only one state and does not define the reference condition, the state reference remains unresolved. Do not fill that gap by guessing whether the switch is at rest, actuated, or otherwise positioned.

A useful reading sequence is to identify the stated state, locate the contact symbol, and then determine whether the represented path is open or closed at that point. This answers what the diagram depicts. It does not establish what a particular switch will do under an unspecified condition, nor does it replace the device’s documentation.

## Trace the circuit path without guessing terminal locations

To follow a represented path, start at a point identified in the drawing and trace its lines through the symbols. At a switch contact, note whether the path is continuous or interrupted in the state shown. Continue tracing only where the diagram depicts a connection. If the drawing provides multiple states, repeat the trace for each state rather than carrying one state’s path into another.

Treat line placement as a way to make the circuit readable. A contact drawn above, below, or beside another symbol is not thereby a physical position on the component. Likewise, the direction a symbol faces or the order in which labels appear on the page does not, by itself, identify terminal locations on a housing. A schematic can be rearranged for clarity while preserving the represented electrical relationships.

If the drawing labels a contact as COM, NO, or NC, read that label as part of the schematic’s notation. Do not translate it directly into “left terminal,” “upper pin,” or another physical location unless the exact device documentation makes that mapping. A generic symbol can explain a contact arrangement while leaving the actual terminal positions unspecified.

For physical identification, consult the equipment-specific documentation and verify the markings on the exact device. The documentation or device schematic should control when it differs from a generic convention. If the available material does not connect a schematic label to a physical terminal, that identity has not been established. Appearance or terminal position alone is not a substitute for verification.

This approach keeps two tasks distinct: trace the electrical path represented on paper, then use verified device information to determine physical identity. The first is diagram interpretation. The second cannot be completed from symbol orientation alone.

### Related guides

- [what is a micro switch actuator](/guides/what-is-a-micro-switch-actuator/)
- [reed contact sensor](/guides/reed-contact-sensor/)
- [electrical switch gear](/guides/electrical-switch-gear/)

## What a switch schematic cannot confirm

A switch symbol alone does not establish the component’s voltage or current rating, load suitability, compatibility, or certification. Those are device-specific matters that require applicable documentation. A contact drawing may show a relationship or state without providing any of those specifications.

The schematic also cannot, by itself, confirm which physical terminal is COM, NO, or NC on a particular switch. Do not infer terminal identity from position on the page, housing appearance, or a generic contact drawing. Use the exact device marking or schematic and its documentation; where these do not resolve identity, leave it unresolved rather than assuming.

Nor is a schematic by itself a complete wiring procedure. It may omit information needed to identify a component, evaluate an installation, or make a replacement decision. For those decisions, use applicable equipment documentation and procedures rather than relying on symbol interpretation alone. This explanation does not determine how to wire a specific appliance or installation.

The practical boundary is simple: use the drawing to understand the circuit path and the contact state it actually identifies. Use verified, equipment-specific information for physical terminal identification and other device-specific decisions. A **switch schematic** is useful for interpreting represented relationships, but it should not be treated as a physical terminal map or a complete source of component specifications.

## Sources and references

- Defense Logistics Agency ASSIST: [MIL-PRF-8805K: Switches and Switch Assemblies, Sensitive, Snap Action, General Specification For](https://quicksearch.dla.mil/qsDocDetails.aspx?ident_number=7196){: rel="nofollow noopener noreferrer" }
- Wikipedia: [Miniature snap-action switch](https://en.wikipedia.org/wiki/Miniature_snap-action_switch){: rel="nofollow noopener noreferrer" }
