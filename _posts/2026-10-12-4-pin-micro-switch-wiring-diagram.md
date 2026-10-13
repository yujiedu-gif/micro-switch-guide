---
title: "4 pin micro switch wiring diagram: identify terminals and verify contacts"
description: "4 pin micro switch wiring diagram: Understand the operating idea, essential terminology, practical checks, limitations, and evidence needed for careful."
date: 2026-10-12 17:55:05 +0800
category: Basics
tags:
  - 4 pin micro switch wiring diagram
  - micro switches
  - Basics
author: editorial_team
---

A 4 pin micro switch wiring diagram cannot be decoded from pin count or physical position alone. Identify the contact functions from the exact switch’s markings or documentation, then verify the relevant terminal pairs with the switch unpowered and disconnected. Four terminals do not, by themselves, establish that the device has a particular contact arrangement or explain the purpose of every terminal.

For a changeover arrangement, the key is the contact state as the actuator moves: COM connects to NC with the actuator released and to NO when actuated. The sections below show how to use that state logic to make a terminal map without assigning unsupported functions to an unexplained pin.

## 4 pin micro switch wiring diagram: what four terminals can mean

A diagram with four terminal positions shows that the switch has four connection points; it does not establish what each point does. Pin numbering, spacing, orientation, and location are not reliable substitutes for a terminal marking or a device-specific connection diagram. A drawing can also show the switch from a different viewing direction than the physical part, so apparent left-to-right correspondence may be misleading.

A common changeover contact arrangement uses COM, NO, and NC. In that arrangement, the common contact connects to one of two other contacts depending on actuator state. However, four pins do not prove that a particular switch uses that arrangement. The fourth terminal’s role is not established by its count or position, and it should not be assigned a function by guesswork.

Keep two tasks separate. First, establish what each terminal does on the exact switch. Second, decide how those contacts fit a particular circuit. A terminal map describes contact behavior; it does not supply the equipment’s wiring plan or establish that a load can be connected safely.

## Map COM, NO, and NC by contact state

For a documented changeover arrangement, COM means the common terminal. NO means normally open, and NC means normally closed. These names describe contact states at the reference condition in which the actuator is released. They do not identify fixed pin positions, wire colors, or a universal current path for every installed circuit.

With the actuator released, COM and NC are closed to each other, while COM and NO are open. When the actuator is pressed, the changeover contact moves: COM and NO become closed, while COM and NC become open. This state comparison is the functional basis for a terminal map. A marking or schematic may show the same relationship in a device-specific format, so interpret it using the exact device documentation rather than assuming a standard drawing orientation.

The names apply only when the changeover arrangement and its reference state are documented for the device. Do not label an unexplained fourth pin as COM, NO, or NC simply because the other terminals appear to form a familiar pattern. If markings or documentation do not identify the arrangement, treat the function as unresolved until it can be verified.

## Verify the four terminals with a continuity test

A continuity check can help verify a terminal map only when the switch is completely disconnected from power and the surrounding circuit. Connected wiring can create other paths that affect a meter reading. Do not use a continuity test on an energized switch or interpret a reading taken through the equipment as proof of the switch’s isolated contact state.

Use a continuity meter and compare candidate terminal pairs in two states:

1. Confirm that the switch is unpowered and fully disconnected from the surrounding circuit. If that condition cannot be established, do not proceed with the isolated test.
2. Record the terminal markings or identifiers visible on the switch and consult its connection diagram or documentation, if available. Avoid inventing labels for unmarked pins.
3. With the actuator released, check candidate pairs and record which pairs show continuity and which do not.
4. Press the actuator and repeat the same pair checks. Compare the results with the released-state observations.
5. For a documented changeover contact, look for COM-to-NC continuity in the released state and COM-to-NO continuity in the actuated state. The opposite pair should change accordingly.
6. Leave any terminal whose function is not established unassigned. If readings conflict with the markings or documentation, stop rather than drawing a diagram from an uncertain map.

The purpose of the two-state comparison is to distinguish contact behavior, not to certify the switch or the surrounding assembly. A result that does not match the documented contact states may reflect an incorrect terminal assumption, an unsuitable test condition, or a switch issue. The available information may not distinguish among those possibilities; recheck the identification and test conditions rather than forcing a conclusion.

## Draw a simple circuit from the verified terminal map

Once the contact map is established, a basic diagram can show the selected contact pair as a switch symbol. For a circuit intended to use the contact that is open with the actuator released and closed when actuated, the documented COM–NO pair is the relevant pair. For a circuit intended to use the contact that is closed with the actuator released and open when actuated, the documented COM–NC pair is relevant. These descriptions explain contact behavior only; they do not specify the complete supply, load, or equipment arrangement.

Before drawing a connection, use the exact switch’s connection diagram, terminal markings, circuit function, and permissible load documented for that switch and equipment. Do not add a wire-color convention or infer a pin position from a generic illustration. Do not treat the contact-state map as evidence that a particular supply or load is suitable.

If the fourth terminal remains unexplained, show it as unidentified or leave it out of the circuit drawing until documentation establishes its purpose. A simple diagram should represent only verified terminals and the intended circuit behavior. It should not silently turn an unknown terminal into a connection point.

### Related guides

- [dual micro switch](/guides/dual-micro-switch/)
- [touch micro switch](/guides/touch-micro-switch/)
- [no nc micro switch](/guides/no-nc-micro-switch/)
- [normally open micro switch](/guides/normally-open-micro-switch/)

## Safety and wiring limits for a micro switch

Keep continuity testing unpowered and perform it only with the switch completely disconnected from the surrounding circuit. Follow applicable deenergization and qualification requirements. A meter check of an isolated switch does not establish that an installed circuit is safe, correctly wired, or suitable for its load.

Check the exact switch and equipment documentation for terminal markings, the connection diagram, and the permissible load before making a circuit drawing or connection. Do not infer ratings, compatibility, or an accessory-terminal function from the fact that the switch has four pins. If documentation and measured contact states disagree, pause and resolve the discrepancy rather than guessing.

Mains or other hazardous-voltage wiring requires qualified handling and must follow applicable rules and the documented ratings. This guidance is limited to identifying contact functions and translating a verified map into a basic diagram approach; it does not provide a device-specific wiring plan.

In short, use the exact switch’s markings and documentation, then compare candidate terminal pairs in released and actuated states while the switch is unpowered and disconnected. A verified contact map can support a diagram, but pin count alone cannot identify every terminal or establish how the switch should be wired in particular equipment.

This concludes the explanation of 4 pin micro switch wiring diagram.

## Sources and references

- Defense Logistics Agency ASSIST: [MIL-PRF-8805K: Switches and Switch Assemblies, Sensitive, Snap Action, General Specification For](https://quicksearch.dla.mil/qsDocDetails.aspx?ident_number=7196){: rel="nofollow noopener noreferrer" }
- Occupational Safety and Health Administration: [29 CFR 1910.333: Selection and Use of Work Practices](https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.333){: rel="nofollow noopener noreferrer" }
- Wikipedia: [Miniature snap-action switch](https://en.wikipedia.org/wiki/Miniature_snap-action_switch){: rel="nofollow noopener noreferrer" }
