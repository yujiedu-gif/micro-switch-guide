---
title: "Dock Leveler Guard Interlock Micro Switch Operating Force: Snap Force vs Direct Opening Force"
description: "Operating force is the push that makes an interlock micro switch snap. On a positive-opening safety switch, design for the larger direct opening force."
date: 2026-10-13 11:27:16 +0800
category: Applications
tags:
  - dock leveler guard interlock micro switch operating force
  - micro switches
  - Applications
author: editorial_team
seo_title: "Dock Leveler Guard Interlock Micro Switch Operating Force"
last_updated: 2026-11-12
---

On a loading dock with a door interlock, a switch beside the overhead door decides whether the dock leveler may move, and a bar on the door pushes that switch each time the door opens. The usual answer to how hard that switch must be pushed is that the switch datasheet sets the figure. **On a safety-rated interlock switch, the datasheet lists a second, larger force that drives the contacts apart even if they have welded, and the part pushing the switch has to deliver that one.** Operating force, interlock positions on a dock leveler, the gap between the two forces and a field check follow in order.

## Quick answer

Operating force (OF) is the push on a micro switch's lever, roller or plunger at which its contacts snap to their other state. One safety limit switch datasheet, for a snap-action model with a roller lever, lists an OF of 5 N max. but a direct opening force of 20 N min., so the part operating an interlock must deliver the larger figure.

The OF value belongs to one switch and one actuator. A dock leveler interlock takes its numbers from the datasheet of the switch actually fitted, not from a general rule.

## What operating force means on a micro switch

One limit switch maker's general technical data defines the minimum actuation force as the force applied to the actuator to produce a change in contact position. A general-purpose basic switch datasheet lists OF next to a minimum release force (RF), the force the actuator still holds as the contacts reset, and shows how much the actuator changes the number. The pin-plunger version in that datasheet needs 3.92 to 6.13 N, while the hinge-lever version of the same switch needs only 0.69 N max.

A longer lever lowers the force because it multiplies the push, and it raises the travel by the same trade. Read the OF for the exact actuator on your switch, not the figure for the bare switch body.

Figure 1. The contacts snap at the operating force, but a positive-opening switch only guarantees a forced break once the actuator reaches the direct opening force and travel.

## Where interlock switches sit on a dock leveler

Pentalift describes its overhead door interlock kit for hydraulic dock levelers this way. A rocker-arm limit switch mounts on the inside wall 7 to 8 feet above the floor, beside the door, and a striker bar mounts near the bottom of the door. With the door closed, the switch circuit is open and the leveler's hydraulic power unit gets no supply. When the door opens to about 7 to 8 feet, the striker bar presses the rocker arm and closes the circuit.

Pentalift gives the reason as protecting the overhead door from damage if someone presses the leveler's raise button with the door shut. That interlock protects property, and its contact closes when the door opens.

Interlocks between the leveler and a vehicle restraint, or a switch that confirms the leveler is stored, can use proximity sensors instead. A proximity sensor detects its target without contact, so it has no operating force at all. In the US, the design and testing of built-in dock leveling devices is covered by ANSI MH30.1-2022, and vehicle restraints by ANSI MH30.3-2022, both published by MHI.

## Operating force and direct opening force are different numbers

A switch that guards people works the other way from Pentalift's door interlock: opening the guard has to open a normally closed (NC) contact. A safety limit switch datasheet from another maker says the NC safety contacts are positive-opening, forced open without springs when the actuator moves from its home position. The same datasheet says the switch must be mounted in "positive mode", so that opening the guard moves the actuator and opens the NC contact.

The limit switch technical data cited above defines the two forces side by side. Minimum actuation force is the force needed to change the contact position. Minimum force to achieve positive opening operation is the force needed to guarantee that the NC contact is forced open.

The safety limit switch from the quick answer, a model with a resin roller lever and two NC contacts, shows how far apart those two forces can sit:

| Characteristic (roller lever safety limit switch) | Value in its datasheet | What it tells you |
|---|---|---|
| Operating force (OF) | 5 N max. | The push at which the contacts snap |
| Release force (RF) | 0.5 N min. | The force the lever keeps as it snaps back |
| Pretravel (PT) | 18 to 27° | Lever rotation before the contacts snap |
| Overtravel (OT) | 40° min. | Further rotation allowed after the snap |
| Direct opening force | 20 N min. | The push that guarantees the NC contacts are forced apart |
| Direct opening travel | 50° min. | The rotation that guarantees the forced break |

A switch maker's knowledge base article on direct opening mechanisms explains what the larger figure buys. A direct opening mechanism forces open a welded contact with the force applied by the actuator. The same article describes the check: the direct opening force is applied at the actuator while a 10 N force holds the contacts together, standing in for the weld.

Because the minimum direct opening force is four times the maximum OF on this switch, a door bar or cam that only just makes the switch click has not proved the forced break. The actuating part has to push the lever through the direct opening travel with at least the direct opening force.

## How much force and travel the striker or guard should deliver

The actuating part sits between two limits. At the low end it has to reach the direct opening force and travel on a safety-rated switch, or the OF and a reliable overtravel on a plain one. A switch maker's FAQ on how far to push a basic switch gives 60% to 90% of the specified overtravel for that low end on a standard switch. The same FAQ warns that beyond 90% the actuator or switch may be damaged.

At the high end, the switch must not become a stop. The positive-opening switch datasheet cited above tells installers not to use the safety switch as a mechanical or end-of-travel stop, and warns that damage from that use can leave the switch failing in an unsafe manner. On a dock door, the striker should press the rocker arm and pass or rest against it, while the door's own stops take the door's weight and momentum.

📌 **On replacements:** *Fit a switch with the same actuator and, for a guard interlock, the same positive-opening rating. A switch with a lower operating force may click sooner, but clicking only shows the snap, and without a direct opening rating nothing forces a welded contact apart.*

## How to check the force on an installed interlock

Lock out the dock leveler's power unit before reaching the switch. The US lockout rule, OSHA 29 CFR 1910.147, covers servicing where an unexpected start could injure someone, and it states that push buttons, selector switches and other control circuit devices are not energy isolating devices. The interlock switch itself is one of those control circuit devices.

With the power locked out:

1. Disconnect one wire at the switch and connect a multimeter on continuity across the contact you are checking.
2. Press the actuator with a push-pull force gauge at the point where the striker touches it, pushing in the striker's direction, and note the gauge reading at the moment the meter changes. Compare it with the OF in the datasheet for that model.
3. Move the door or guard slowly through its full stroke and watch how far the actuator travels. On a safety-rated switch, it has to pass the direct opening travel in the datasheet.
4. Check that the actuator is not bottoming out. The lever should stop short of its total travel when the door or guard is at its end position.
5. Reconnect the wire and check the screws on the switch and the striker bracket for tightness.

The safety switch datasheet also lists checks for a designated person at each shift change or setup. They cover breakage of the switch body or actuator, alignment and full engagement, use of the switch as an end stop, and loose mounting hardware.

Never tape, wedge or jumper an interlock switch to keep a leveler running. The same datasheet warns against using spare actuators to bypass a safety switch, and the same reasoning applies to any object that holds an actuator in place.

## FAQ

### What is the purpose of the door interlock switch?

On a loading dock, a door interlock switch stops the dock leveler from operating until the overhead door is open. Pentalift's interlock kit does this with a rocker-arm limit switch that keeps the leveler's power unit circuit open while the door is shut, which protects the door from being struck by the rising leveler.

### What is the purpose of a mechanical interlock?

A mechanical interlock makes one action depend on another physical condition, such as a door being open or a guard being closed. A switch-based interlock turns that physical condition into an electrical one: the actuator's position decides whether a contact is open or closed. The operating force is what the mechanism has to supply to make that change happen.

### What is the purpose of interlocking guards on machines?

An interlocking guard stops hazardous machine motion when the guard opens. A safety limit switch datasheet describes the principle: the switch is mounted so that opening the guard moves the actuator and forces the NC safety contact open. US machine guarding rules in OSHA 29 CFR 1910.212 require one or more methods of guarding to protect operators from hazards such as nip points and rotating parts.

## What to read on the datasheet before you change anything

For the exact switch model, find the operating force, the overtravel and, on a safety-rated switch, the direct opening force and travel. Then check that the door bar or guard delivers more than the direct opening figures without driving the actuator to its stop. Related guides cover operating force on a spring plunger micro switch, the safety function of a micro switch, operating force on a centrifuge guard interlock and how to test a bucket elevator guard interlock micro switch.

Guard switches on a loading dock take knocks, and some industrial switch lines are designed with that in mind. [ZING EAR](https://www.zingear-switch.com/){: rel="nofollow noopener noreferrer" } says its heavy-duty industrial micro switches carry anti-misoperation and impact-resistant designs on a reinforced mechanical structure. For a guard interlock, the datasheet still has to show the direct opening force and the positive opening mark described above, whichever maker supplies the part.

## Sources

- Pentalift, What is a Hydraulic Dock Leveler Overhead Door Interlock Kit and How Does it Work?
- MHI LODEM publications: ANSI MH30.1-2022 and ANSI MH30.3-2022
- OSHA, 29 CFR 1910.147, The control of hazardous energy (lockout/tagout)
- OSHA, 29 CFR 1910.212, General requirements for all machines
- ZING EAR, official site home page (industrial heavy-duty line description): https://www.zingear-switch.com/
- ZING EAR, Industrial Heavy-duty Micro Switch product line page: https://www.zingear-switch.com/industrial-heavy-duty-micro-switch
