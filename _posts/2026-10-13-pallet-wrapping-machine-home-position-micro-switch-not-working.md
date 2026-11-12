---
title: "Pallet Wrapping Machine Home Position Micro Switch Not Working: Actuation, Contacts or Wiring?"
description: "Pallet wrapping machine home position micro switch not working? Split the fault into actuation, contacts and wiring, and check each with the power locked out."
date: 2026-10-13 11:27:16 +0800
category: Troubleshooting
tags:
  - pallet wrapping machine home position micro switch not working
  - micro switches
  - Troubleshooting
author: editorial_team
seo_title: "Pallet Wrapper Home Position Micro Switch Not Working: Fixes"
last_updated: 2026-11-12
---

A pallet wrapper that keeps turning after the wrap cycle, or won't start because it can't find its start position, is waiting on a signal from a home sensor. Quick-fix advice for this fault points to debris, a sensor knocked out of alignment and damaged wiring, and much of that advice is written for a proximity sensor. **When the home sensor is a micro switch, a clear click proves only that the mechanism moved, because the contacts can still fail to pass current.** The sensor type, the lockout, the three places a fault can sit and a check for each follow in order.

## Quick answer

When a pallet wrapping machine's home position micro switch (also called a snap-action switch) fails, the fault sits in one of three places: the cam or roller pressing it, its contacts, or the wiring and controller input. A switch maker's FAQ on basic switch failures splits basic switch failures into mechanical ones, which covers the first place, and electrical ones such as contact failure, which covers the second.

Check each place with the machine locked out, starting with the one you can see.

## Confirm the home sensor is a micro switch

"Home" on a pallet wrapper can mean two positions: the turntable's stopping point and the film carriage's starting height. The two are often sensed by different parts. The user manual for Global Industrial's fully automatic low profile pallet wrapper (model 238509) shows the split. The parts list gives the turntable an NPN proximity switch and the tower two limit switches for the carriage's up and down limits. A micro switch with a roller sits on the film carriage's safety plate.

The same manual says that pressing Reset returns the turntable to its home position and lowers the carriage to its initial position. A home fault on that machine can therefore come from a proximity sensor or from a mechanical limit switch, depending on which motion fails to reach home.

Look at the part before testing it. A micro switch or limit switch has a lever, roller or plunger that something has to push, and usually three screw or spade terminals. A proximity sensor is a threaded or flat body with a cable and no moving actuator. If yours is a proximity sensor, the checks below for cams, levers and contacts don't apply; see the guide on how 2-wire proximity sensors work instead.

Figure 1. On a turntable pallet wrapper, "home" can depend on more than one sensor, and they are not always the same type.

## Lock out the wrapper before you touch the switch

The Global Industrial manual requires all maintenance to be done with the power supply disconnected and limits inspection, troubleshooting and part replacement to qualified personnel. In the US, the lockout rule OSHA 29 CFR 1910.147 applies to servicing where an unexpected start could injure someone, and a turntable or carriage that starts while your hands are at the switch is that hazard.

OSHA's rule also states that push buttons, selector switches and other control circuit devices are not energy isolating devices. The wrapper's stop button and the emergency stop are control circuit devices, so pressing them does not make the machine safe to reach into. Lock the main disconnect instead.

A check of the controller's input display, described below, needs power on. Do that part from the control panel, without reaching into the machine, and do the hands-on work at the switch only after the lockout.

## Split the fault into three places

| Place | What fails | What you'll see | How to confirm |
|---|---|---|---|
| Actuation | Cam, target plate or roller doesn't push the lever far enough, or pushes it too far | Switch doesn't click when the turntable or carriage reaches home, or the lever is bent | Watch and feel the lever's motion with the machine locked out and moved by hand where the manual allows |
| Contacts | Contacts don't close or open even though the lever moves | Switch clicks, but a meter shows no change between terminals | Continuity test across the switch terminals with one wire removed |
| Wiring and input | A broken wire, a loose terminal or a failed input stops the signal | Switch tests good on the bench, but the controller never sees it change | Input indicator on the controller's I/O display, then wire continuity |

The Global Industrial manual points to an I/O display that shows the status of all sensors and switches. Once the meter shows the switch itself changing state, an input that still never changes points to the third place. If the input indicator changes when the switch is pressed, the switch and its wiring are passing the signal, and the fault is in the home logic or settings.

## Check the actuation: cam, roller and lever

A micro switch only changes state after its actuator has moved a set distance, and the cam or target on the turntable or carriage has to provide that motion every cycle. Look for three problems.

A bent lever is the first. The same failure FAQ names deformation of the actuator lever as a relatively common cause, typically after something got caught in the lever. On a wrapper, a torn film tail or a dropped strap can be that something.

An actuator pushed too little or too far is the second problem: too little shows up as no click when the machine reaches home, too far as a lever bent past its stop. The same maker's FAQ on how far to push a basic switch deals with overtravel (OT), the distance the actuator may keep moving after the contacts switch. The FAQ gives 60% to 90% of the specified OT and warns that beyond 90% the actuator or switch may be damaged. A general-purpose switch datasheet gives 70% to 100% of the rated OT instead, so use the figure in the datasheet for your exact part.

A cam that stops the actuator right at the switching point is the third. The pushing FAQ also warns against stopping near the operating position (OP), where the contacts switch on, or the release position (RP), where they switch back, because contact pressure there is low and chattering or bouncing can follow. A turntable that coasts to a stop with the roller balanced on the edge of the cam gives an intermittent home signal.

## Check the contacts with a meter

With the wrapper locked out, remove one wire from the switch so the rest of the circuit doesn't affect the reading. Set a multimeter to continuity and identify the terminals: common (COM), normally open (NO) and normally closed (NC), where "normally" means with the lever at rest.

At rest, COM to NC should read closed and COM to NO open. Press the lever through its stroke and both readings should swap with a click. Release slowly and they should swap back. If the readings don't change, or flicker as you press, the contacts are at fault even when the click sounds normal.

Two contact problems explain a switch that clicks but doesn't conduct. The maker's FAQ on minimum loads says that below a basic switch's minimum applicable load, the contact surface is more susceptible to a chemical coating from the surrounding air, which can eventually cause contact failure. A controller input draws a small current, so a home switch with silver contacts can be exposed to exactly that. The general-purpose datasheet cited above adds a second cause: that switch is generally not built to resist water, and splashing oil, water or dust calls for a protective cover.

📌 **On replacement parts:** *A switch with gold-plated contacts is made for small signal currents. Match the contact material, actuator type and terminal layout of the original, using the wrapper maker's part number where one is listed.*

## Check the wiring and the controller input

If the switch tests good on the meter, follow the wire back to the controller. If the switch rides on the film carriage, its cable flexes every time the carriage moves, so check where the cable bends and where it enters the switch housing. Then check each terminal along the run for tightness.

Reconnect the switch, restore power under your site's procedure, and watch the input on the I/O display from the control panel while a second person, clear of the machine, operates the wrapper's reset or home function. If the input never changes while the switch is being pressed by the machine, the fault lies in the wiring or the input. If it changes but the machine still doesn't stop at home, the home settings or the controller logic need the wrapper maker's service procedure.

Never place a jumper across the home switch or force the input to get the machine running. On the Global Industrial wrapper, a turntable that cannot see home is listed as one that does not stop, which is the condition the switch exists to prevent.

## FAQ

### How do limit switches work?

A limit switch is a switch that a moving part of a machine presses when it reaches a set position. One limit switch maker's technical data describes two kinds of contact element inside. Snap-action contacts switch at a speed independent of the actuator; slow-action contacts move only as fast as the actuator does. On a pallet wrapper, a cam or plate on the turntable or carriage presses the switch's lever or roller.

### Is the home sensor on a pallet wrapper a micro switch or a proximity sensor?

The answer depends on the machine and on which motion the sensor watches. Global Industrial's manual for its model 238509 wrapper lists a proximity switch at the turntable and mechanical limit switches on the tower for the carriage. Check the parts list in your own wrapper's manual before ordering a replacement.

### Why does my wrapper's home switch work sometimes and not others?

An intermittent home signal can point to a roller that stops near the switching point, a loose terminal, or a cable that breaks contact as it flexes. The pushing FAQ ties stopping near the switching point to chattering, because contact pressure there is low, so check where the cam leaves the roller at the end of the cycle.

## What to write down before you call service

Note which motion fails to reach home, what type of sensor sits there, whether the switch clicks, what the meter showed across COM, NO and NC, and whether the input indicator changed. Those five observations narrow the fault to actuation, contacts or wiring before a technician arrives. For more on the parts involved, see the guides on how to test a micro switch with a multimeter, micro switch contact oxidation, cam misalignment on a micro switch and roller plunger micro switch failure.

Home and in-place signals like this one are exactly what some industrial switch lines are built to report. [ZING EAR](https://www.zingear-switch.com/){: rel="nofollow noopener noreferrer" } says its heavy-duty industrial micro switches feed back key status signals such as equipment limit position and station in-place, with the stated aim of reducing unplanned shutdowns. The checks above still sort out whether a given fault sits in the actuation, the contacts or the wiring.

## Sources

- Global Industrial, Fully Automatic Low Profile Pallet Wrapper User Manual, Model 238509
- OSHA, 29 CFR 1910.147, The control of hazardous energy (lockout/tagout)
- ZING EAR, official site home page (industrial heavy-duty line description): https://www.zingear-switch.com/
