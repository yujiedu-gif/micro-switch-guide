---
title: "2 prong micro switch: What Do Its Two Terminals Do?"
description: "2 prong micro switch: Understand the operating idea, essential terminology, practical checks, limitations, and evidence needed for careful selection,."
date: 2026-10-12 16:49:35 +0800
category: Basics
tags:
  - 2 prong micro switch
  - micro switches
  - Basics
author: editorial_team
---

A **2 prong micro switch** has two accessible electrical terminals. Those terminals provide one switched circuit path, but their number alone does not show whether that path is open or closed when the actuator is released. Identify the contact behavior by checking the specific switch in both actuator states, then assess its voltage, current, and load suitability separately. A contact test identifies whether the path changes state; it does not establish that the switch is appropriate for a particular circuit.

Before testing or handling wiring, disconnect power and prevent the circuit from being energized. If the switch is part of a larger circuit, isolate at least one lead where practical so another circuit path does not affect the measurement. Do not proceed with wiring when the ratings or circuit conditions are unclear.

## What a 2 prong micro switch means electrically

The two prongs are two accessible electrical terminals connected through a contact mechanism. Together, they provide one switched path: the path is either electrically open or closed at a given moment. The switch is not presenting a third terminal as an alternate contact connection.

That is different from a generic changeover contact, which may expose terminals labeled common, normally closed, and normally open. Those labels describe a contact arrangement with a shared connection and two possible contact paths. On a two-terminal switch, there is only one accessible pair to test. Do not assume it corresponds to the normally open or normally closed side of a three-terminal arrangement.

Terminal count does not reveal the pair’s state when the actuator is at rest. Depending on the switch design, the contact path may be open when released and closed when pressed, or closed when released and open when pressed. The actual marking or schematic for the device, if available, is the reference for its terminal arrangement. When that information does not resolve the behavior, test the pair rather than inferring it from appearance or terminal count.

## 2 prong micro switch contact behavior: open or closed?

“Open” and “closed” describe the electrical condition between the two terminals, not the actuator’s physical position. An open path does not provide continuity across the pair; a closed path does. “Released” and “pressed” describe whether the actuator is being operated. These are separate observations, so a released actuator is not automatically an open contact.

A functioning switch changes the contact state as its actuator moves through its operating action. Which state occurs when released depends on the design. For one switch, releasing the actuator may leave the pair open and pressing it may close the path. Another design may have the opposite behavior. Without the switch’s documentation or a test result, the released-state condition remains unknown.

The useful identification is therefore a state pair: note the measured condition with the actuator released, then note it again while pressed. For example, a result that changes from no continuity when released to continuity when pressed indicates an open-at-rest, closed-when-pressed path. The reverse readings indicate a closed-at-rest, open-when-pressed path. These observations describe the tested switch and do not establish its electrical capacity.

## How to test a 2 prong micro switch with a multimeter

1. **Disconnect power.** The test must be performed with the circuit de-energized. Do not measure the switch while it is powered.
2. **Isolate the measurement.** Where practical, disconnect at least one switch lead from the surrounding circuit. Other components or parallel paths can otherwise affect what the meter indicates.
3. **Select continuity or resistance.** Use the multimeter’s continuity setting or a resistance measurement suitable for checking the contact pair.
4. **Measure with the actuator released.** Place one probe on each terminal and record whether the meter indicates a closed path or an open path.
5. **Measure with the actuator pressed.** Keep the probes on the same two terminals, operate the actuator, and record the result again. Compare the two readings to see whether the contact state changes.

Continuity indicates a closed path between the terminals under the test conditions. No continuity indicates an open path. If the readings are inconsistent or unstable, do not guess at the contact state or treat one reading as definitive. Check whether the switch was isolated from other circuit paths, whether the probes remain in contact with the terminals, and whether the actuator is being operated consistently. If the cause remains unclear, the behavior is not confirmed.

This test identifies the contact path in the two actuator states. It does not test whether the switch can safely or reliably interrupt a particular voltage, current, or load. A continuity result is not a substitute for the switch’s ratings or the conditions stated for those ratings.

## Check electrical limits before using or replacing the switch

After identifying the contact behavior, check the switch’s stated voltage and current ratings and the conditions attached to them. Rating values are specification-sheet requirements tied to stated load and test conditions, not universal switching capacities. The relevant limits depend on the actual load type and switching conditions. A rating detached from its stated conditions is not enough to establish suitability.

Do not use terminal count, body size, or a continuity reading as a measure of electrical capacity. Two terminals tell you about the accessible contact arrangement. A meter test tells you whether the tested pair is open or closed in the measured actuator states. Neither establishes an allowable voltage, current, or load.

For hazardous voltages, use an appropriately rated isolation and protection method. If the switch’s ratings, the load conditions, or the wiring are unclear, seek qualified help rather than assuming the contact is suitable. Identification and suitability are separate checks: confirm the contact behavior first, then compare the intended circuit conditions with the switch’s stated rating requirements.

### Related guides

- [dual micro switch](/guides/dual-micro-switch/)
- [touch micro switch](/guides/touch-micro-switch/)
- [no nc micro switch](/guides/no-nc-micro-switch/)
- [normally open micro switch](/guides/normally-open-micro-switch/)

## Common misreadings of a two-terminal micro switch

**“Two terminals means normally open.”** It does not. A two-terminal switch exposes one contact pair, but the pair may be open or closed when the actuator is released. Verify both states rather than assigning a normal state from terminal count.

**“Continuity means it is safe for this circuit.”** It does not. Continuity shows a closed path during a de-energized test. It does not establish voltage, current, load, or switching-condition suitability. Those require the applicable rating information and conditions.

**“No state change means the switch has a particular contact type.”** That conclusion is premature. The switch may be misidentified, damaged, poorly actuated, or still connected to another circuit path that affects the measurement. Recheck isolation and actuator operation; if readings remain inconsistent or the behavior cannot be confirmed, leave the contact state unresolved.

A reliable identification therefore combines two checks: record the open or closed condition with the actuator released and pressed, then assess electrical suitability from the stated ratings and their load and test conditions. Do not infer either result from the fact that the switch has two prongs.

This concludes the explanation of 2 prong micro switch.

## Sources and references

- Defense Logistics Agency ASSIST: [MIL-PRF-8805K: Switches and Switch Assemblies, Sensitive, Snap Action, General Specification For](https://quicksearch.dla.mil/qsDocDetails.aspx?ident_number=7196){: rel="nofollow noopener noreferrer" }
- Wikipedia: [Miniature snap-action switch](https://en.wikipedia.org/wiki/Miniature_snap-action_switch){: rel="nofollow noopener noreferrer" }
