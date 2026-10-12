---
title: "dpst micro switch: How It Works and How to Test Its Two Poles"
description: "dpst micro switch: Understand the operating idea, essential terminology, practical checks, limitations, and evidence needed for careful selection,."
date: 2026-08-07 09:00:00 +0800
category: Basics
tags:
  - dpst micro switch
  - micro switches
  - Basics
author: editorial_team
---

A **dpst micro switch** has one actuator that controls two electrically separate switching paths. Each path is a pole, and each pole changes the state of its own circuit. Testing the poles individually can show whether their contact paths change as documented, but it does not establish a switch’s ratings, safety suitability, or exact switching timing.

The useful distinction is between shared mechanical operation and electrical connection: the actuator may operate both poles, while the poles remain separate electrical paths. Because terminal layouts and contact behavior depend on the specific switch, identify the terminals from markings or documentation before testing. Then check each pole on its own, in released and actuated states, with the circuit de-energized and the switch isolated from external wiring as needed.

## What a dpst micro switch means electrically

DPST means double pole, single throw. In practical terms, the switch controls two poles, or two separate switching paths, with one throw for each pole. A pole is one circuit path through the switch; a throw describes the contact option that path can connect to or disconnect from. In a DPST arrangement, each pole makes or breaks its own circuit under the switch’s operation.

The two poles share a mechanical actuator, but that does not make them one electrical path. Each pole has its own terminals and contact path. This distinction matters when interpreting a continuity check: a reading across one pole tells you about that path, not automatically about the other.

DPST is also different from DPDT, or double pole, double throw. DPDT has two contact options for each of its two poles, while DPST has one. The labels describe contact configuration, not electrical capacity. Neither DPST nor the number of poles establishes a permissible voltage, current, load type, or safety rating. Those details must be determined from documentation for the exact switch and equipment.

## How the actuator operates both poles

When mechanical input moves the actuator, the switch’s mechanism changes the contact state in each of its two switching paths. In this sense, one mechanical action operates both poles, even though the poles remain electrically separate. Their shared actuator is not evidence that their contacts form a common electrical connection.

Do not assume that both poles change state at precisely the same instant. The configuration describes the number of poles and throws, but does not by itself specify a switching sequence or contact timing. The particular mechanical behavior depends on the switch design and its documentation.

Actuation force, travel, and release behavior are also design-dependent. Release force, also called releasing force, is the force or torque to which force on the actuator must be reduced to permit the contacts to return to the unoperated position after operation. This definition identifies a release condition; it does not supply a numeric force value or establish the behavior of any particular model. Use applicable switch documentation for design-specific values and operating details.

## Identify terminals before testing

First identify the two poles and their terminals from the switch’s markings or its device documentation. Do not infer a universal terminal arrangement from physical appearance, terminal position, or a familiar-looking case. Different designs can arrange or label terminals differently, and appearance alone does not establish which terminals form a pole or contact path.

Use the connection diagram, terminal marking, circuit function, and permissible load documented for the exact switch and equipment rather than a generic physical-layout inference. A diagram is useful only when it belongs to the switch or equipment being checked and its terminal references match the markings present.

For a meaningful pole-by-pole check, disconnect external wiring when needed to prevent parallel paths from affecting meter readings. A connected circuit may provide an alternate electrical route, so a continuity result might not represent only the switch contact being measured. The required isolation depends on the circuit and equipment. Do not proceed with a continuity measurement on an energized circuit; follow applicable de-energization and qualification requirements.

## Test each pole of a dpst micro switch

A continuity check compares the electrical path between identified terminals in different actuator states. It can show whether that path changes between the released and actuated positions. It does not, by itself, prove that the switch is suitable for a load or that the device meets a safety requirement.

Use this bounded, pole-by-pole process:

1. **De-energize the circuit and verify isolation.** Follow the applicable de-energization and qualification requirements before using continuity mode. Do not use a continuity check as a way to determine whether an unknown circuit is safe to touch.
2. **Identify the terminals for the first pole.** Follow the switch marking and documentation to locate that pole’s common and throw terminals. Do not choose terminals based only on their physical position.
3. **Check the first pole in both states.** With the switch isolated from external wiring as needed, measure across the documented contact path in the released state, then repeat with the actuator operated. Note the observed readings and compare the change, or lack of change, with the documented contact arrangement.
4. **Repeat independently for the second pole.** Identify that pole’s common and throw terminals from the same documentation, then measure its path in released and actuated states. Keep the results separate so one pole’s reading is not mistaken for evidence about the other.
5. **Compare observations with the documentation.** Account for the stated contact arrangement and the specific switch design. Do not assume that the poles change state at exactly the same time, or that a particular switching sequence applies.

The check is about the two documented contact paths in two actuator states. It can establish whether each measured path changes as expected under those test conditions. It cannot establish exact timing between poles, permissible load, voltage or current suitability, or a safety certification.

### Related guides

- [dual micro switch](/guides/dual-micro-switch/)
- [touch micro switch](/guides/touch-micro-switch/)
- [no nc micro switch](/guides/no-nc-micro-switch/)
- [normally open micro switch](/guides/normally-open-micro-switch/)

## Interpret results and recognize limits

If a pole’s path does not change as the documentation indicates, the observation may point to a contact issue, a connection issue, or a test setup problem. It is not enough by itself to identify which explanation is correct. Recheck that the correct terminals were selected, the external wiring is not creating a parallel path, and the actuator is being evaluated in the states described by the documentation.

Different readings from the two poles should be recorded and assessed independently. A DPST description does not guarantee identical measurements, simultaneous contact timing, or a specific order of switching. The terminal arrangement, mechanical behavior, and ratings depend on the particular switch design; use its documentation rather than extrapolating from the DPST label.

Continuity testing is limited to the electrical path observed by the meter under the test conditions. It does not establish whether a switch is appropriate for a particular voltage, current, or load, and it does not verify insulation performance or certify safety. For questions involving energized or hazardous circuits, consult qualified help rather than relying on a continuity reading.

The practical method is to identify each pole from exact-switch documentation, isolate the relevant paths, and compare released and actuated readings separately. A **dpst micro switch** provides two mechanically operated but electrically separate poles; testing each one independently can verify a bounded contact-state observation, not ratings or safety suitability.

## Sources and references

- Defense Logistics Agency ASSIST: [MIL-PRF-8805K: Switches and Switch Assemblies, Sensitive, Snap Action, General Specification For](https://quicksearch.dla.mil/qsDocDetails.aspx?ident_number=7196){: rel="nofollow noopener noreferrer" }
- Occupational Safety and Health Administration: [29 CFR 1910.333: Selection and Use of Work Practices](https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.333){: rel="nofollow noopener noreferrer" }
