---
title: "Drawer Closed Position Micro Switch NO and NC Terminals"
description: "drawer closed position micro switch NO and NC terminals: Understand the operating idea, essential terminology, practical checks, limitations, and evidence."
date: 2026-09-02 18:43:53 +0800
last_modified_at: 2026-10-13 11:46:37 +0800
category: Applications
tags:
  - drawer closed position micro switch NO and NC terminals
  - micro switches
  - Applications
author: editorial_team
---

A drawer’s closed position does not, by itself, tell you which micro switch terminal is NO or NC. The **drawer closed position micro switch NO and NC terminals** relationship depends on the switch’s unactuated reference condition and on how the drawer linkage moves its actuator. First identify the documented contact arrangement; then trace the mechanical movement and consider any contact observation only under a defined test condition. Do not treat a drawer position as the switch’s reference state or infer how the surrounding appliance will behave from terminal names alone.

## What NO and NC mean on a micro switch

Normally open (NO) and normally closed (NC) describe contact states relative to the specified unactuated reference condition. They do not mean, respectively, “open when the drawer is open” and “closed when the drawer is closed.” Those drawer labels describe positions of the surrounding mechanism, not the switch’s reference condition.

A miniature snap-action switch can change an electrical contact state in response to mechanical actuator movement. In a generic changeover contact arrangement, the terminals may be labeled common (COM), normally closed (NC), and normally open (NO). That general description is not a substitute for the exact device’s marking or schematic: use the switch documentation to determine whether those labels and that arrangement apply to the particular switch.

When the arrangement is documented, COM identifies the common terminal in that contact arrangement. NO and NC then identify the respective contact states at the documented reference condition. The labels alone do not establish which pair is continuous in an installed drawer, because drawer closure may or may not move the actuator away from that reference condition. Nor do the labels alone establish what an appliance circuit does with a contact change.

Keep three things distinct: the switch’s reference condition, the actuator’s position, and the drawer’s position. The reference condition provides the basis for the NO and NC names. The actuator’s position depends on the mechanical input to the switch. The drawer’s position affects the actuator only through the particular linkage and installation. The terms do not assign a universal electrical state to a closed drawer.

## Drawer closed position micro switch NO and NC terminals: follow the actuator movement

To relate drawer closure to a switch contact, follow the physical sequence rather than starting with the words “open” or “closed.” The sequence is drawer movement, linkage contact or clearance, actuator movement, and then any resulting contact-state change. A miniature snap-action switch may serve for position or limit detection, but that general use does not specify the arrangement or behavior of a particular drawer mechanism.

When the drawer closes, its linkage may press the actuator or release it. Which occurs depends on the installed geometry. If closure moves the actuator, the switch’s contact state may change in response to that movement. If closure does not move the actuator, the drawer’s position alone does not establish a switch-state change. The supplied facts do not determine the movement for any particular drawer, linkage, or switch.

This distinction prevents a common misreading: “normally” in NO and NC does not mean the drawer’s normal, open, or closed position. It refers to the specified unactuated reference condition for the switch. To say which terminal pair corresponds to a drawer-closed condition, you would need both the documented contact arrangement and evidence of the actuator state at that drawer position. Without those details, assigning the drawer-closed condition to NO or NC would be an unsupported assumption.

Do not infer the linkage’s action from the drawer’s appearance or from the terminal names. The drawer may be closed while the actuator is moved in one direction or another, depending on how the linkage meets the switch. The contact terminology describes the switch; it does not describe the drawer mechanism. The installed circuit’s response is another question, determined by its wiring and control logic rather than by NO or NC labels alone.

## Identify the contact state under a defined test condition

A contact-state observation is useful only when the switch, terminal pair, and actuator state are identified. Start with the exact switch documentation to confirm the terminal markings or schematic and the contact arrangement. Then distinguish the specified unactuated reference condition from any other actuator position you are considering. A test result without a defined state cannot, by itself, show how the NO or NC designation applies.

The accepted information here does not provide a procedure for testing continuity on an isolated switch, specify a measuring method, or state expected readings for particular actuator positions. It therefore does not support step-by-step testing instructions or a prediction of which documented terminal pair will show continuity for a given drawer position. Use the applicable device documentation and test conditions rather than filling in those missing details from the labels alone.

If a contact observation has been made under an appropriate, documented condition, interpret it narrowly: it concerns the tested switch contact and state. It does not establish that the switch is wired correctly in the appliance, reveal the control logic, or show that the whole drawer mechanism or equipment functions as intended. A contact reading is not a substitute for identifying the device’s terminal arrangement and the actuator condition associated with that reading.

In particular, an observation made with the drawer closed is not automatically a test of the switch’s unactuated reference condition. The drawer may move or release the actuator through its linkage. To connect an observation to NO or NC, the relevant actuator state and the documented terminal arrangement must be known. If either is unresolved, the correct conclusion is that the drawer-closed state has not been identified from the available information.

### Related guides

- [bottling machine home position micro switch location](/guides/bottling-machine-home-position-micro-switch-location/)
- [incinerator end of stroke micro switch maintenance](/guides/incinerator-end-of-stroke-micro-switch-maintenance/)
- [rotary indexing table guard interlock micro switch location](/guides/rotary-indexing-table-guard-interlock-micro-switch-location/)
- [security barrier open position micro switch wiring](/guides/security-barrier-open-position-micro-switch-wiring/)

## What the result does and does not establish

A documented terminal label or a defined contact observation can help identify the switch’s contact state within its stated conditions. It does not establish the linkage geometry, whether drawer closure moves the actuator, how the switch is wired, or what the appliance’s control logic does with a contact change. Those are separate facts that must not be inferred from NO and NC terminology.

Keep the decision boundary clear: the switch’s reference state defines its contact names; the linkage determines the actuator movement associated with drawer position; and the surrounding circuit determines how an electrical change is used. A result about one of these does not settle the others. In particular, identifying a switch contact state does not establish that the drawer is safe to use or predict whether an appliance will energize when the drawer is closed.

If the contact arrangement, reference condition, linkage movement, or wiring is unknown, the relationship between the terminals and the closed drawer remains unresolved. Electrical work beyond a supported, documented test boundary should be left to a qualified person. In short, **drawer closed position micro switch NO and NC terminals** can be related only by combining the specific switch’s documented contact arrangement with the actuator movement caused by that drawer’s linkage; the drawer position alone does not identify NO or NC.

Insulation resistance is a separate measurement from identifying NO and NC contact states. Under the MIL-PRF-8805K requirement and referenced test method, it is evaluated between specified electrically isolated points using the applicable test method and conditions. That definition does not supply a drawer-position contact test or establish installed-circuit behavior.

## Sources and references

- Defense Logistics Agency ASSIST: [MIL-PRF-8805K: Switches and Switch Assemblies, Sensitive, Snap Action, General Specification For](https://quicksearch.dla.mil/qsDocDetails.aspx?ident_number=7196){: rel="nofollow noopener noreferrer" }
- Wikipedia: [Miniature snap-action switch](https://en.wikipedia.org/wiki/Miniature_snap-action_switch){: rel="nofollow noopener noreferrer" }
