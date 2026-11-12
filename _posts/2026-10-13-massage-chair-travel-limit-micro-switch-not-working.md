---
title: "Massage Chair Travel Limit Micro Switch Not Working: Symptoms, Causes and How to Check It"
description: "Rollers stuck at the top or bottom, or an up/down error? How a massage chair travel limit switch works, what service manuals list as causes, and how to test it."
date: 2026-10-13 11:27:16 +0800
category: Troubleshooting
tags:
  - massage chair travel limit micro switch not working
  - micro switches
  - Troubleshooting
author: editorial_team
seo_title: "Massage Chair Travel Limit Micro Switch Not Working"
last_updated: 2026-11-12
---

Massage chair rollers that climb to the top of the backrest and stay there, or stop with an up/down error on the remote, have lost track of where they are. A small switch at the end of the track is the obvious suspect. **On a chair that uses limit switches, the switch tells the motor when to reverse, so a failed switch, a bent lever and a loose wire all leave the same stuck roller.** The sections below cover how the travel limit works, what service manuals list as causes, and how to check the switch with the chair unplugged.

## Quick answer

A massage chair travel limit micro switch sits at one end of the roller track, where the roller carriage, the frame that carries the rollers, presses it to make the motor stop or reverse. US patent 6,974,426 notes that when such a switch fails, the carriage sticks at the top or bottom while the motor keeps turning. Check the error code, wiring and switch lever before replacing it.

## How a massage chair knows where its rollers are

The rollers ride on a carriage that a motor drives up and down the backrest. Something has to tell the control board when the carriage reaches the end of the track, and chairs do that in different ways.

- **Micro switches at each end.** US patent 6,974,426, for a massaging structure with a buffer function, describes a conventional design with a micro switch at the upper end and another at the lower end of a threaded rod, the screw the motor turns to move the carriage. When the moving carriage touches the upper switch, the motor reverses and drives it down; the lower switch reverses it again. A micro switch, also called a snap-action switch, is a small switch that flips its contacts with a click when its lever or button is pressed a set distance.
- **Limit sensors plus a motor counter.** Cozzia's maintenance service manual for its EC-360D chair lists an "up & down limit sensor" and a separate counting sensor on the rolling motor among the parts its self-check tests.
- **A position sensor instead of end switches.** Panasonic's service manual for its EP-MA73 massage lounger describes an up/down sensor driven by a sensor gear, and says the up/down stop position changes if the massage mechanism is removed, so the gear has to be adjusted on reassembly.

So before buying a switch, find out which kind your chair has. The service manual or parts list for your model is the reliable source; a "limit sensor" in one manual may not be a micro switch at all. Our explainer on travel limit micro switches in linear actuators shows the same end-of-travel idea in another motor-driven product.

## Safety before you open the back cover

A massage chair runs on mains power: Panasonic's service manual lists the EP-MA73's supply as 120 V AC at 3.2 A. Turn the chair off and unplug it before you unzip the back cover or touch any wiring. Omron's SS series datasheet gives the same rule for the switches themselves: turn off the power supply before mounting or removing a switch, wiring it, or doing maintenance, because working live can cause electric shock or burns.

Don't run the roller motor with a limit switch disconnected, or bridged with a wire, to see what happens. The patent describes what follows when a limit signal never arrives: the carriage reaches the end of the rod and the motor keeps driving it. Panasonic's manual warns that if the massage mechanism overruns on its EP-MA73, the up/down worm gear cracks. If the chair is under warranty, its maker's service center is the safer route for anything inside the cover.

## Symptoms and error codes that point to the travel limit

- **Rollers stuck at the top or bottom, motor still running or humming.** This matches the failure the patent describes: no signal from the end switch, so the motor never reverses.
- **An up/down error code.** Cozzia's EC-360D manual lists an error when the chair gets no signal from the up limit sensor for more than 40 seconds. It gives three causes: a broken upper limit sensor, disconnected backrest wires, or a broken rolling motor or motor wire. Panasonic's EP-MA73 manual uses code F37 for an up/down sensor fault.
- **Rollers stop short or overshoot.** On a chair with a geared position sensor, Panasonic's manual ties the stop position to the sensor gear, so a stop that has moved after the back was opened points to gear adjustment rather than a switch.

If the chair shows an error code, write it down first. Cozzia's manual explains how its EC-360D enters an auto-check mode by holding three remote buttons for two seconds, after which the display shows the fault code. Panasonic's EP-MA73 has a similar service mode that shows which sensor stopped the massage block, Panasonic's name for the roller unit.

## How to check the switch and its wiring

With the chair unplugged, open the back cover and find the switches at the ends of the roller track. Work through these in order.

1. **Look at the lever.** A travel limit switch usually has a lever that the carriage pushes. Omron's FAQ on basic switch failures names a deformed actuator lever as a relatively common cause; in its example, something caught on the lever and bent it. The same FAQ says a lever that sits at a larger angle or has more play has deformed.
2. **Check that the carriage reaches the lever.** Move the carriage by hand only if your service manual allows it. A switch bracket that has shifted, or a carriage tab that has bent, can miss the lever. Our article on micro switch cam misalignment covers how a pressing part that's out of line stops a switch from operating.
3. **Check the connectors.** Cozzia's manual lists a disconnected backrest wire as a cause for both up and down limit errors. Reseat every connector between the switch and the control board.
4. **Test the switch with a multimeter.** Disconnect the switch's wires and set the meter to continuity. Most micro switches have three terminals: common (COM), normally closed (NC) and normally open (NO). Electronic Design's explainer on snap-action switches describes the at-rest state: with the actuator released, the common contact rests against the NC contact.

| Switch lever | COM to NC | COM to NO |
|---|---|---|
| Released | Continuity | Open |
| Pressed past the click | Open | Continuity |

A switch that reads the same in both positions, or that flickers as you press the lever slowly, has failed. Our guide on how to test a micro switch covers meter setup and probe placement, and our explainer on NO and NC terminals explains why the chair may use only one pair.

📌 **On clicking but not reversing:** *If the switch clicks and tests good but the rollers still won't reverse, the fault is past the switch, in the wiring, the control board or the motor, which Cozzia's manual also lists among the causes.*

## Replacing and refitting a limit switch

Order the replacement by the part number in your chair's service manual or parts list where one is available. A generic micro switch has to match the old one's size, mounting holes, lever shape and length, and terminal style, or the carriage will press it at a different point. Before you fit the new one, photograph the wiring and note which terminal pair the chair uses.

When refitting, follow the order your model's manual gives. Sanyo's HEC-DR7700 manual has technicians tape down the micro switch lever before refitting the massage unit, so an accidental hit doesn't bend it, and remove the tape afterward. Panasonic's EP-MA73 manual has the massage block moved to its lowest position before removal and before reinstallation. Otherwise, the manual warns, the block overruns and its gears crack because the chair doesn't recognize the up/down positions. After refitting, run the rollers through their full travel once and watch that they reverse at both ends.

## FAQ

### My massage chair remote isn't working. What could be the problem?

Cozzia's EC-360D manual lists a broken or disconnected remote control wire, and a key held down for too long, among the remote faults its self-check reports. Check the remote's cable and connector at the chair, and if your chair has a self-check mode, run it to see whether it reports a remote fault or a different one, such as a limit sensor.

### Why are my massage chair rollers stuck at the top?

On a chair that reverses its rollers with end switches, a failed upper switch, a bent lever or a loose wire leaves the motor with no signal to reverse. That's the stuck carriage US patent 6,974,426 describes. On a chair with a position sensor, Panasonic's EP-MA73 manual points instead to the up/down sensor and its gear. The error code, if your chair shows one, tells you which part the control board is complaining about.

## What to note before calling for service

Write down the chair's model number, the error code, which end the rollers stop at, and whether the motor keeps running there. Those four details tell a technician, or you with the service manual open, whether to start at the limit switch, the wiring, the position sensor or the motor.

Limit and position switches inside household appliances are a regular product for switch makers. [ZING EAR](https://www.zingear-switch.com/){:rel="nofollow"}'s home appliance line page says the company supports customized adjustment of operating force and terminal styles to suit the structure of different home appliances. A replacement therefore has to match the chair's original part, which its model number and service manual identify.

## Sources

- US Patent 6,974,426 B2, "Massaging structure with a buffer function" (Google Patents)
- Panasonic, Massage Lounger EP-MA73 Service Manual (Order No. HPD1405U01CE), hosted by Parts Town
- Cozzia, EC-360D Maintenance Service Manual, page 4 (ManualsHive)
- Cozzia, EC-360D Maintenance Service Manual, page 5 (ManualsHive)
- Sanyo, HEC-DR7700 Service Manual, page 22 (ManualsLib)
- Omron FAQ FAQE20047, "What may have caused a basic switch failure?" (reposted on DigiKey TechForum)
- Omron, SS Miniature Basic Switch (Non-Sealed) catalog pages (B053-E2-11D), hosted by Electrokit
- Electronic Design, "Snap-Action Switches Still Rule The Roost"
- [ZING EAR, Home Appliance Micro Switch product line page](https://www.zingear-switch.com/home-appliance-micro-switch){:rel="nofollow"}
