---
title: "Micro Switch Cam Misalignment Explained: How an Off-Line Cam Changes When and How the Switch Trips"
description: "Cam misalignment means a cam meets a micro switch's roller off its plane, at the wrong depth or at the wrong angle. See the signs and how to check it."
date: 2026-10-13 11:27:16 +0800
category: Troubleshooting
tags:
  - micro switch cam misalignment explained
  - micro switches
  - Troubleshooting
author: editorial_team
seo_title: "Micro Switch Cam Misalignment: Causes, Signs and Checks"
last_updated: 2026-11-12
---

A cam-driven micro switch can start missing a stroke, flickering at one spot in the cycle or wearing a groove into its roller, and the switch tends to be the first part replaced. A new switch then fails the same way if the cam that drives it is the part that moved. **Before the switch takes the blame, the place to look is where the cam meets the roller: off to one side, too shallow, too deep or at the wrong moment in the turn.** The cam-and-switch pair is followed here from correct engagement, through each kind of misalignment and the signs it leaves, to a step-by-step check.

## Quick answer

Micro switch cam misalignment means the cam no longer meets the switch's roller or lever where it was designed to. The cam can sit off to one side, push too little or too far, or arrive at the wrong point in its rotation. A switch maker's application bulletin for precision switches says the cam and roller "should lie in the same plane" and that misalignment increases wear on both.

## What a correctly aligned cam does to the switch

One maker's technical bulletin on applying precision switches describes the switch, with a small wheel on its plunger or lever, as "a spring loaded cam follower." The cam is the shaped wheel or bar that pushes that roller as it turns or slides, and the plunger is the button on the switch body that the roller or lever presses. The bulletin's rules for a well-set pair are short:

- The cam and roller lie in the same plane, and the roller ideally stays in contact with the cam at all times.
- The cam's rise angle, the steepness of the slope the roller climbs, stays at or below 30°, so the roller rides up a ramp instead of being struck.
- The cam doesn't let the roller drop off a sharp edge, which the bulletin calls drop-off release.
- The cam doesn't push the plunger with excessive force at full overtravel.

How far the cam pushes matters as much as the angle. The actuator is the part the cam touches, the roller lever or plunger, and overtravel (OT) is the travel it can safely take after the contacts click over. A general-purpose basic switch datasheet says to push the actuator past the click by 70% to 100% of the rated OT. Another maker's technical guide asks for at least 0.5 times the OT and never beyond the total travel position, where the actuator meets its internal stop.

## The ways a cam can sit out of line

### Off to one side

When the cam and roller aren't in the same plane, the roller rides on one edge of the cam face. The precision-switch bulletin states plainly that "misalignment of the roller with the cam increases wear." A push that isn't square to the plunger also creates side thrust, which the same bulletin says wears the plunger's bearing surfaces and reduces the switch's precision. A roller or cam with a wear track along one edge is the usual trace.

### Too shallow

If the cam's high point no longer pushes the actuator far enough, the switch either never reaches its operating point (the point where the contacts snap over) or stops just past it. Contact force is the spring pressure holding closed contacts together, and the same bulletin explains that it falls toward zero as the plunger nears the operating point. A switch maker's FAQ on how far to push a basic switch warns that stopping near the operating position or the release position "may create chattering or bouncing," meaning rapid on-off flicker in the signal. The release position is where the contacts snap back on the return.

### Too deep

A cam that sits too close drives the actuator past its overtravel toward the internal stop. The precision-switch bulletin says excessive force from the cam at full overtravel "can reduce switch life," and that the farther a plunger is pushed, the higher the stress in the spring. One maker's technical guide sets a ceiling it calls the allowable overtravel force, the most force the actuator can take "without incurring deterioration" of the switch.

### At the wrong point in the turn

A cam that has turned on its shaft still reaches the roller at the right depth and in the right plane, but at a different shaft angle. The switch then operates at a different point in the machine's cycle, even though the switch itself tests fine on a meter. This is a timing error rather than a contact or travel problem, so it shows up as a machine doing a step early or late.

## Signs that point to the cam rather than the switch

| What you see | Likely misalignment | Why, and who says so |
|---|---|---|
| Wear track or groove along one edge of the roller or cam | Off to one side | Precision-switch application bulletin: misalignment of roller and cam increases wear |
| Signal flickers while the cam sits at its high point | Too shallow | Maker's FAQ on pushing depth: stopping near the operating or release position causes chattering |
| Switch never trips, but trips when pressed by hand | Too shallow, or off to one side | The cam isn't delivering the travel; the switch works |
| New switches fail early, or the actuator lever is bent | Too deep, or striking too hard | Precision-switch bulletin: excess force at full overtravel; maker's failure FAQ: lever deformation is a common failure |
| Extra pulses right after the cam passes | Sharp drop-off on the cam | Precision-switch bulletin: a lever may oscillate after drop-off release, "giving a series of false operations" |
| Switch trips cleanly but at the wrong moment | Wrong point in the turn | Cam has shifted on its shaft |

A lever that's bent is worth a closer look in its own right. A switch maker's FAQ on what causes basic switch failures calls a deformed actuator lever "a relatively common cause" of failure. The sign it names is a larger bend angle or more play than a new lever.

## How to check cam alignment step by step

Lock out the machine before you touch the cam or the switch: switch off and isolate the power and any stored motion, and lock it so nobody can restart it. OSHA's rule on the control of hazardous energy, 29 CFR 1910.147 covers this kind of servicing. If the switch is part of a guard or door interlock, don't wedge or bypass it while you work.

1. **Test the switch on its own.** Set a meter to continuity and check the common terminal against the normally closed and normally open terminals, first with the actuator free and then pressed by hand past the click. Free, common to normally closed reads closed and common to normally open reads open; pressed, the two swap. If the readings don't swap cleanly, replace the switch before judging the cam.
2. **Look at the pair from above.** Turn the cam slowly by hand and watch the roller. It should run centered on the cam face, with the two in the same plane, as the bulletin requires.
3. **Find where the switch clicks.** Keep turning until you hear or meter the switch operate, and note the cam angle or machine position. Compare it with where the machine needs the signal. A mismatch with good depth and plane points to a cam that has turned on its shaft.
4. **Check the depth at the cam's high point.** Measure how far the actuator travels past the click and compare it with the datasheet overtravel. As a reference, the basic switch datasheet cited above gives 70% to 100% of the rated OT; use the figure on your own switch's datasheet, and make sure the actuator doesn't bottom out.
5. **Check the ramp and the drop.** The roller should climb a gentle rise, no steeper than the bulletin's 30° rule, and roll off the cam without falling off a step.
6. **Re-tighten and recheck.** The same bulletin warns that a warped mounting surface or over-tightened mounting screws can reduce the stability of the operating and release points. Mount the switch on a flat surface, tighten to the maker's torque, then repeat steps 2 to 4.

## FAQ

### How to tell if a micro switch is bad?

Disconnect power and test it on a meter's continuity setting. With nothing pressing the actuator, common to normally closed should read closed and common to normally open should read open, and the readings should swap when you press past the click. A switch maker's FAQ on basic switch failures separates electrical faults, such as contact failure and contact welding, from mechanical ones such as operating failure, so check the actuator for damage too.

### Why are the contacts of a micro switch spring loaded?

The spring supplies the contact force that holds closed contacts together. A maker's technical bulletin on precision switches says contact force affects electrical resistance and the switch's ability to stay closed through vibration and shock. The same spring stores energy as the actuator is pressed and releases it to snap the contacts across, so they can't stop partway between the two sides.

## After the cam is set

Once the cam runs in plane, at the right depth and at the right angle, check it again after a short run. The precision-switch bulletin describes a settling-in period over the first several hundred operations, in which the switch, its actuator and "associated operating cam or linkage" bed in together and the switching points shift slightly. For background on why depth matters, see how movement differential sets the reset point and how a spring lever trades force for travel. If the roller itself is worn, the cam follower failure guide and roller plunger failure guide cover the replacement, and preventing cam misalignment covers keeping it set.

## Sources

- US Occupational Safety and Health Administration, 29 CFR 1910.147, The control of hazardous energy (lockout/tagout)
