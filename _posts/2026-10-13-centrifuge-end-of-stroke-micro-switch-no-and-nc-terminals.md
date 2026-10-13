---
title: "Centrifuge end of stroke micro switch NO and NC terminals"
description: "centrifuge end of stroke micro switch NO and NC terminals: Understand the operating idea, essential terminology, practical checks, limitations, and."
date: 2026-10-13 09:00:00 +0800
category: Applications
tags:
  - centrifuge end of stroke micro switch NO and NC terminals
  - micro switches
  - Applications
author: editorial_team
---

NO and NC identify contact states by reference to a specified actuator condition; they do not, by themselves, describe what a centrifuge will do. For a centrifuge end of stroke micro switch NO and NC terminals, the essential distinction is between the switch’s contact behavior and the host machine’s control response. The terminal labels alone cannot establish the wiring, the machine’s normal state, or whether an end-of-stroke event causes a stop, alarm, or other action.

## What NO and NC mean on a centrifuge end of stroke micro switch NO and NC terminals

NO and NC are interpreted relative to the documented reference actuator state of the particular switch. At that reference state, the contact arrangement identified as normally open is open, while the arrangement identified as normally closed is closed. These terms describe contact states under that reference condition. They are not unconditional guarantees about current flow in an installed circuit, and they do not name a centrifuge operating mode.

If the actuator moves away from the reference condition and the switch changes state, the contacts may transition. The actual state in a particular actuator condition must be established from the switch documentation and the specified reference condition. Do not assume that an end-of-stroke position is the reference condition, that motion toward the end of travel necessarily actuates the switch, or that every switch has the same contact arrangement. Those details depend on the design and its documentation.

A miniature snap-action switch can change an electrical contact state in response to mechanical actuator movement. Snap action refers to contact action in which the speed of the moving contacts is relatively independent of the speed of the actuating mechanism. This describes the contact mechanism, not the direction of actuator movement, the centrifuge’s sequence, or the result of a control decision.

Thus, NO and NC are useful only when paired with a reference condition and the correct terminal identification. A label does not, on its own, show which terminal is connected to a particular circuit, whether the switch is actuated in the machine’s current position, or what that circuit does.

## How end-of-stroke motion can actuate a micro switch

In a design that uses a micro switch for end-of-stroke detection, the causal path is mechanical: movement of a centrifuge mechanism or its linkage may move the switch actuator, and actuator movement may change the switch’s contact state. This is a possible arrangement, not a claim that every centrifuge uses a micro switch or that every end-of-stroke mechanism operates in the same way.

The exact relationship must be established for the particular centrifuge. The available terminal labels do not identify where the switch is mounted, what component contacts its actuator, which direction of motion operates it, or which machine position corresponds to actuation. Do not infer those details from the words “end of stroke” or from the physical appearance of the switch. They require the equipment’s documented mechanism and the switch’s documented connection information.

The switch’s mechanical input and its electrical contact state are related but distinct. Mechanism travel can provide the input; the switch responds at its actuator. Whether the actuator actually reaches the required position, and whether contact state changes as intended, are separate questions. A click may indicate movement of a snap mechanism, but does not establish continuity, correct terminal identification, correct wiring, or suitability for the circuit.

Keep the description conditional unless the specific design documentation establishes the arrangement. A mechanism reaching an end-of-stroke position may actuate a micro switch only in designs that use one. Even when it does, the contact transition alone does not specify the centrifuge’s response. It supplies an electrical condition for the connected circuit to interpret.

## What the terminal change does, and does not, tell you about the centrifuge

A contact transition describes the switch. The centrifuge’s response depends on the actual wiring and control circuit. A contact change might be used as an input, but the terminal names do not reveal what the machine’s logic assigns to that input. They cannot establish whether the centrifuge stops, signals an alarm, changes operating state, or takes another action.

For that reason, do not translate “NO” into “machine off,” “NC” into “machine on,” or either label into a normal centrifuge state. NO and NC refer to contact arrangement and state at a documented reference actuator condition. A machine’s normal operating condition is a separate system-level description. Its relationship to the switch depends on the specific circuit and equipment design.

Verification also has two distinct parts. First, the switch’s terminal identities, documented reference condition, and permissible load must be established for the exact switch. Second, the equipment documentation must establish how the switch is connected and what the control circuit is intended to do. The applicable connection diagram, terminal marking, circuit function, and permissible load for the exact switch and equipment take priority over a generic inference based on terminal position or appearance.

A contact-state finding cannot, by itself, prove that the end-of-stroke mechanism reaches the actuator, that the installed wiring is correct, or that the centrifuge’s control response works. Likewise, an unexpected machine response does not by itself prove that the micro switch is defective. The cause could involve mechanical actuation, terminal identification, wiring, the control circuit, or another part of the equipment. The relevant documentation and observations are needed to distinguish these possibilities; terminal labels alone do not resolve them.

### Related guides

- [bottling machine home position micro switch location](/guides/bottling-machine-home-position-micro-switch-location/)
- [incinerator end of stroke micro switch maintenance](/guides/incinerator-end-of-stroke-micro-switch-maintenance/)
- [rotary indexing table guard interlock micro switch location](/guides/rotary-indexing-table-guard-interlock-micro-switch-location/)
- [security barrier open position micro switch wiring](/guides/security-barrier-open-position-micro-switch-wiring/)

## How to verify terminal states safely

Use the connection diagram and terminal markings for the exact switch and equipment to identify the terminals and the specified reference actuator condition. Do not rely on a generic physical-layout inference. Any verification must follow applicable deenergization and qualification requirements. If the applicable documentation does not provide a procedure with a defined isolation condition, actuator condition, measuring method, and expected result, those details remain unresolved; do not invent a test from the NO and NC labels alone.

Where a documented procedure calls for an isolated-switch continuity check, interpret the result only for the isolated switch in the stated actuator condition and using the specified measuring method. A continuity result under one condition does not establish behavior in a different condition, correct installation, or the function of the centrifuge’s control circuit. It also does not establish that the installed equipment is safe or fully functional. A click is likewise insufficient evidence of electrical continuity or system operation.

Keep the final conclusion within what was checked. The switch documentation can define terminal identity and reference contact states; equipment documentation can define the intended circuit function and response. If either part is unavailable or unclear, the machine’s end-of-stroke response remains unverified. The practical boundary is simple: NO and NC describe documented switch contact states, while the centrifuge’s behavior must be verified from its own wiring and control documentation. The phrase centrifuge end of stroke micro switch NO and NC terminals does not imply a universal machine arrangement or response.

## Sources and references

- Defense Logistics Agency ASSIST: [MIL-PRF-8805K: Switches and Switch Assemblies, Sensitive, Snap Action, General Specification For](https://quicksearch.dla.mil/qsDocDetails.aspx?ident_number=7196){: rel="nofollow noopener noreferrer" }
- Occupational Safety and Health Administration: [29 CFR 1910.333: Selection and Use of Work Practices](https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.333){: rel="nofollow noopener noreferrer" }
- Wikipedia: [Miniature snap-action switch](https://en.wikipedia.org/wiki/Miniature_snap-action_switch){: rel="nofollow noopener noreferrer" }
