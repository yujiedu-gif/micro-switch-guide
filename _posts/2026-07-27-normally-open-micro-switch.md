---
title: "Normally Open Micro Switch: What Its Contact State Means"
description: "normally open micro switch: Learn what open and closed mean at rest and during actuation, how terminals change state, and how to verify contact behavior safely."
date: 2026-07-27 09:00:00 +0800
category: Basics
tags:
  - normally open micro switch
  - micro switches
  - Basics
author: editorial_team
---

# Normally Open Micro Switch Contact States

A **normally open micro switch** is defined by the electrical state of a contact pair when the switch is unactuated: the pair is open. When the switch is actuated, that pair changes to closed if the switch is designed for that operation. “Normally” refers to the switch’s unactuated state, not necessarily to the actuator’s position in the equipment where the switch is installed.

That distinction matters when identifying contacts. An actuator can rest pressed because of the surrounding equipment’s geometry, even though the switch’s reference state is unactuated. A continuity check can help establish how an identified pair behaves, but it does not by itself establish whether the switch is suitable for a particular load or application. Confirm terminal identification against the exact switch documentation, and test only with the circuit de-energized.

## What a normally open micro switch means

“Normally open” describes the contact pair’s electrical state in the switch’s unactuated state. For that pair, open means there is no continuity between the two terminals under the test conditions. Closed means there is continuity. These terms describe an electrical connection, not whether the switch body, lever, or button looks pressed or released after installation.

The reference state can be easy to confuse with the installed position. Equipment may hold an actuator down at rest, or its geometry may otherwise place the actuator in a position that looks pressed. That does not change the definition of normally open. The definition concerns the switch’s unactuated state; the equipment’s arrangement determines what position the actuator occupies when the equipment itself is at rest.

A common changeover contact may use three terminals: common, normally closed, and normally open. The symbols COM, NC, and NO are commonly used for these terminal names. However, labels and contact arrangements are not a substitute for checking the exact device marking or schematic. A switch may have more than one contact pair, so do not assume that the state of one pair describes every terminal on the device.

Keep the definition narrow: for the relevant pair, normally open means open in the unactuated state. It does not, on its own, tell you the switch’s full internal configuration, how it is mounted, or how an equipment circuit uses it. Those details require the switch documentation and, where appropriate, observation of the contact state.

## How a normally open micro switch changes state

For a contact pair intended to operate as normally open, the expected transition is open in the unactuated state and closed when actuated. In practical terms, the pair has no continuity at rest and shows continuity after the switch is actuated. This describes the expected behavior of that pair, not an assumption that every switch or every pair follows the same operation.

Actuation means operating the switch’s actuator. It is not necessarily the same as moving the equipment into a particular named position. A lever may be held in, a button may be released, or an actuator may be contacted by a part of the equipment. The physical relationship depends on the installation. To interpret the contact state correctly, distinguish what is happening to the actuator from the equipment’s position and from the switch’s unactuated reference state.

A changeover contact may provide common, normally closed, and normally open terminals. In that generic arrangement, the exact device marking or schematic controls which terminals are which. A switch can also contain multiple contact pairs, and each pair has its own state. Do not infer the behavior of an untested pair from the state change observed on another pair.

The expected open-to-closed change gives a specific check for the pair under examination. If measurement shows a different pattern, the observation does not justify relabeling terminals or assuming a different design. Recheck terminal identification and the switch documentation, and report the measured states as observed. The precise contact configuration and intended behavior remain unresolved unless the exact device information establishes them.

## How to verify the normally open contact pair

A continuity check is useful only when the switch is not energized by its circuit. Disconnect power before measuring, and isolate the switch from parallel circuit paths where needed so other components do not affect the reading. If the circuit cannot be safely de-energized, do not proceed with this check.

First, consult the exact switch documentation and device markings to identify the terminals to test. For a generic changeover contact, COM may identify common and NO may identify normally open, but the exact device marking or schematic controls. Do not identify terminals by wire color alone. If terminal identity remains uncertain, do not treat a guessed pair as the normally open contact.

Set a meter to its continuity function or use a resistance measurement, then place the probes across the identified common and normally open terminals. Observe the reading with the actuator in its unactuated state. For the relevant normally open pair, the expected result is no continuity in that state. Record what the meter actually shows rather than assuming that the markings guarantee a particular reading on the individual device.

Next, actuate the switch and measure the same pair again. If the pair is designed for that operation, the expected result is continuity while actuated. Compare the two observations: open at rest and closed when actuated. The state change is more informative than a single reading because it shows how the identified pair behaves in both states.

Keep the test bounded. Do not measure a powered circuit, and do not let a reading from other connected paths stand in for a measurement of the switch itself. Where isolation is needed to separate parallel paths, use the exact circuit and switch documentation to determine what can be isolated safely. If that cannot be done confidently, stop rather than interpreting an uncertain reading.

### Related guides

- [dual micro switch](/guides/dual-micro-switch/)
- [touch micro switch](/guides/touch-micro-switch/)
- [no nc micro switch](/guides/no-nc-micro-switch/)
- [float switch mechanism micro switch contact rating](/guides/float-switch-mechanism-micro-switch-contact-rating/)

## What the test can and cannot establish

A reading that changes from no continuity in the unactuated state to continuity when actuated supports the conclusion that the tested pair showed the expected normally open behavior during the check. It establishes an observed state change for that pair under those test conditions. It does not establish the switch’s suitability for a load or application, nor does it identify every contact in a device with multiple pairs.

Interpret the result alongside the exact switch documentation. Generic terminal names such as COM, NC, and NO can help describe a changeover contact, but the device’s own markings or schematic control. If labels, schematic, and measured behavior do not align clearly, preserve that uncertainty. Do not infer terminal identity from wire color, actuator appearance, or the way the switch is mounted.

A continuity check also has limits when the switch remains connected to other circuit paths. Those paths can affect what the meter observes, which is why the switch should be isolated as needed. If the measurement cannot be made on the identified pair under suitable conditions, the result is inconclusive rather than proof of a particular contact configuration.

The practical conclusion is specific: normally open means the relevant pair is electrically open in the switch’s unactuated state, and a designed pair is expected to close when actuated. Confirm the terminals from the exact documentation and compare meter readings at rest and during actuation. Stop if the circuit cannot be safely de-energized or terminal identification is uncertain. This verifies observed contact behavior without extending the test into wiring, fault diagnosis, or application suitability.

This concludes the explanation of normally open micro switch.

## Sources and references

- Defense Logistics Agency ASSIST: [MIL-PRF-8805K: Switches and Switch Assemblies, Sensitive, Snap Action, General Specification For](https://quicksearch.dla.mil/qsDocDetails.aspx?ident_number=7196){: rel="nofollow noopener noreferrer" }
- Wikipedia: [Miniature snap-action switch](https://en.wikipedia.org/wiki/Miniature_snap-action_switch){: rel="nofollow noopener noreferrer" }
