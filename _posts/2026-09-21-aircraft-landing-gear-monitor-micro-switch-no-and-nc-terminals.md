---
title: "Aircraft landing gear monitor micro switch NO and NC terminals: Understanding Contact States"
description: "aircraft landing gear monitor micro switch NO and NC terminals: Understand the operating idea, essential terminology, practical checks, limitations, and."
date: 2026-09-21 09:00:00 +0800
category: Applications
tags:
  - aircraft landing gear monitor micro switch NO and NC terminals
  - micro switches
  - Applications
author: editorial_team
---

An **aircraft landing gear monitor micro switch NO and NC terminals** describe contact paths, not gear positions by themselves. On a switch with this documented contact arrangement, NO and NC identify states relative to the switch’s unactuated condition. When the actuator moves, the contact paths change according to the switch design. The aircraft’s wiring and monitor logic determine what an resulting electrical state represents.

The key distinction is between the switch’s contact state and the aircraft indication. An isolated continuity check can assess a contact path under the test conditions, but it does not establish what the installed monitor displays or prove the position of the landing gear. Interpret the complete path only with the applicable approved aircraft documentation and qualified maintenance practices.

## What aircraft landing gear monitor micro switch NO and NC terminals mean

Normally open (NO) and normally closed (NC) describe contact states in relation to the switch’s unactuated state. In a documented changeover arrangement, a common terminal may connect through one path in that reference state. When the actuator is operated, the contact paths change. Which path is open or closed in each state must be confirmed from the exact switch’s marking or schematic; the terminal names alone are not a substitute for that documentation.

These terms describe the switch, not the landing gear. “Normally” does not mean gear-up, gear-down, safe, or unsafe. It refers to the switch’s unactuated reference condition. The actuator’s position is a mechanical input to the switch, while the gear indication is an output of the aircraft’s monitor circuit. The relationship between those two states depends on how the switch is actuated and how the circuit is designed.

A generic changeover contact may use common, NO, and NC labels, but not every switch has that arrangement. A generic physical layout is not enough to identify terminals. Use the exact switch documentation and the aircraft connection diagram to establish which terminals are present and how they are assigned. If the marking or schematic is unavailable or unclear, the terminal function remains unresolved rather than something to infer from location or appearance.

This distinction prevents a common mistake: seeing an NO terminal and assuming it is the gear-down signal, or seeing NC and assuming it means gear-up. Either assignment might be used in a particular design, but the labels alone establish neither. They identify contact behavior relative to a reference state, not an aircraft condition.

## How NO and NC paths can represent a monitored gear state

A monitor circuit may use one contact path to convey a switch state, or it may use both paths as part of its logic. In either case, the switch supplies contact behavior; the aircraft circuit interprets that behavior. Wiring, other components, and monitor logic determine whether a resulting signal corresponds to a particular gear condition or indication.

For example, the terms NO and NC can help describe which contact path changes as the actuator moves. They do not tell a reader what the aircraft’s indicator will show. That conclusion requires tracing the relevant connections and logic in the applicable aircraft diagram and procedures. Do not translate a contact label directly into a gear-up, gear-down, locked, warning, or other monitor state without that circuit-specific basis.

The same caution applies when both contact paths are present. Their complementary behavior at the switch does not by itself establish how the aircraft uses them. The monitor may interpret one path, both paths, or additional circuit inputs. Without aircraft-specific documentation, the signal mapping is unknown. A statement about one documented design should not be generalized to every aircraft or every landing gear monitor.

The switch’s mechanical input also matters to interpretation. A contact transition says that the switch actuator has moved through a designed state change; it does not, on its own, verify the complete mechanical condition of the gear. The relationship between gear movement and actuator movement belongs to the particular installation. This article does not establish how a particular aircraft positions or operates its monitor switch.

Accordingly, separate three questions: which contacts change state at the switch, what the installed circuit does with those contacts, and what the aircraft indication means. The first is a component-level question answered by switch documentation and an appropriate check. The second and third require the aircraft-specific circuit information and maintenance context. Keeping these questions separate avoids treating a contact label as a universal gear-status code.

## Checking continuity at the isolated micro switch

A continuity check at an isolated switch concerns the switch’s contact paths under a defined actuator state. It is not a test of the complete installed monitor circuit. The switch must be isolated as required by the applicable documentation, and the circuit must be de-energized. Follow the approved aircraft-specific maintenance procedures and suitable test instructions; do not infer a test setup from terminal labels alone.

For a meaningful comparison, identify the exact switch and its documented terminal functions, then relate the measured contact behavior to the documented actuator state. The expected result must come from the switch documentation, including any relevant state or test conditions. Do not assume that a particular terminal pair should show continuity merely because it is labeled NO or NC, or because an aircraft indicator displays a particular state.

The result is limited. It can indicate whether a contact path behaves as documented during the isolated check. It cannot establish how the wiring, connectors, other circuit components, or monitor logic behave when installed. Nor does it establish landing gear position or aircraft airworthiness. A contact reading is one bounded observation, not a complete aircraft-level diagnosis.

If the observed result does not match the applicable documentation, that difference warrants interpretation under the approved maintenance process. It does not, by itself, identify the cause. Avoid turning a component reading into an adjustment, repair, or replacement instruction; those tasks are outside the scope of this explanation and require the relevant aircraft procedures and qualified maintenance practices.

### Related guides

- [ball screw actuator home position micro switch replacement](/guides/ball-screw-actuator-home-position-micro-switch-replacement/)
- [bottling machine end of stroke micro switch](/guides/bottling-machine-end-of-stroke-micro-switch/)
- [automated guided vehicle home position micro switch location](/guides/automated-guided-vehicle-home-position-micro-switch-location/)
- [accelerator pedal position stop micro switch operating force](/guides/accelerator-pedal-position-stop-micro-switch-operating-force/)

## Why an aircraft indication may not match a simple NO or NC reading

An isolated switch check and an installed aircraft indication answer different questions. The isolated check concerns a contact path at the switch under the test conditions. The installed indication reflects the aircraft monitor circuit as a whole. Wiring, connectors, other circuit components, and monitor logic can affect the installed result, so a simple NO or NC reading does not necessarily predict what the aircraft display or warning system will show.

Use the applicable approved wiring diagram and maintenance procedures to interpret the complete monitor path. The switch’s connection diagram and terminal marking establish its documented contact arrangement; the aircraft documentation establishes how that arrangement connects to the monitor. A general terminal description cannot replace either source, and a generic wiring layout cannot establish the function of a specific installation.

If an indication appears inconsistent with an isolated contact reading, do not conclude from that difference alone that the switch is defective, that the wiring is at fault, or that the gear is in a particular position. Those are distinct possibilities requiring aircraft-specific verification. Likewise, continuity alone cannot establish landing gear position or whether an aircraft is safe to fly.

The useful boundary is straightforward: interpret NO and NC as switch contact terminology referenced to the unactuated state; verify the switch only under documented, de-energized and isolated test conditions; and use approved aircraft-specific information to understand the installed monitor. This applies only to monitor designs that use the stated micro switch. It does not presume that every landing gear monitor uses one or that every installation maps its contacts in the same way.

This concludes the explanation of aircraft landing gear monitor micro switch NO and NC terminals.

## Sources and references

- Defense Logistics Agency ASSIST: [MIL-PRF-8805K: Switches and Switch Assemblies, Sensitive, Snap Action, General Specification For](https://quicksearch.dla.mil/qsDocDetails.aspx?ident_number=7196){: rel="nofollow noopener noreferrer" }
- Occupational Safety and Health Administration: [29 CFR 1910.333: Selection and Use of Work Practices](https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.333){: rel="nofollow noopener noreferrer" }
- Wikipedia: [Miniature snap-action switch](https://en.wikipedia.org/wiki/Miniature_snap-action_switch){: rel="nofollow noopener noreferrer" }
