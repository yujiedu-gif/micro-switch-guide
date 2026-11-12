---
title: "Micro Switch Movement Differential Explained: Why the Switch Turns Off Later Than It Turns On"
description: "Movement differential is the gap between where a micro switch turns on and where it turns off. See why it exists, what widens it and how to read it."
date: 2026-10-13 13:45:35 +0800
category: Basics
tags:
  - micro switch movement differential explained
  - micro switches
  - Basics
author: editorial_team
seo_title: "Micro Switch Movement Differential (Differential Travel)"
last_updated: 2026-11-12
---

"Movement differential" is the name some basic-switch datasheets give a distance that other makers' datasheets and technical guides call differential travel. Summaries of the term describe it as the gap between where a switch turns on and where it turns back off, a gap that stops small vibrations from flicking the contacts. **The gap is designed into the snap mechanism, and it blocks only one kind of flicker: a switch resting near either end of it can still chatter, because its contact force there is near zero.** The distance is followed here through its names, a single press-and-release cycle, the design reason behind it and what makes it grow.

## Quick answer

Movement differential is the distance between the actuator position where a micro switch's contacts snap over on the way in and the position where they snap back on the way out. One switch maker's technical terminology page lists it as a maximum value, in millimeters for a straight-line actuator or degrees for one that rotates. Other makers' datasheets and technical guides call the same distance differential travel.

## One distance, several names

Every maker measures the same thing: how far the actuator has to back off after the switch operates before the contacts return. The names and abbreviations differ, and one abbreviation means opposite things depending on whose datasheet you're reading.

| Type of document | Name and abbreviation | How the document defines it |
|---|---|---|
| General-purpose basic switch datasheet | Movement differential (MD), listed as max. | Gap between the operating position (OP) and the release position (RP) |
| Switch maker's technical terminology page | Movement differential (MD), max. | "The distance or degree from operating position to release position of the actuator" |
| Sealed miniature basic switch datasheet | Differential travel (D.T.), max. | Actuator travel "from point where contacts 'snap-over' to point where they 'snap-back'" |
| Switch maker's basic technical concepts guide | Differential travel (DT) | "Distance between the operating position OP and the release position RLP" |

The trap is the letters RP. Both the terminology page in the table and one maker's FAQ on how far to push a basic switch use RP for the release position, the point where the contacts snap back. In the basic technical concepts guide, RP stands for the rest position, where the actuator sits with nothing touching it, and RLP for the release position. When two datasheets disagree about RP, read each one's own legend before comparing numbers.

## How the gap appears in one press and release

A switch maker's technical bulletin on applying precision switches walks through a full cycle of a plunger switch:

1. With nothing pressing the plunger, the common contact rests on the normally closed contact.
2. The plunger travels down through the pretravel to the operating point. There the common contact snaps across to the normally open contact.
3. The plunger can keep going through the overtravel, and the contacts stay where they are.
4. On the way back up, the plunger passes the operating point again, and the bulletin notes that "this does not cause the position of the common contact to change."
5. Only at the release point does the common contact snap back to the normally closed side.

The distance between the operating point in step 2 and the release point in step 5 is the differential travel. Because the contacts snap back before the plunger gets home, the release point sits between the operating point and the free position. The bulletin adds that these positions are usually measured from the center line of the switch's mounting holes.

Movement differential is easy to mix up with the two travels next to it:

| Term | Runs from | What it tells you |
|---|---|---|
| Pretravel | Free position to the operating point | How far the actuator moves before the switch operates |
| Overtravel | Operating point onward, as far as is safe | How much room is left after the switch operates |
| Movement differential | Operating point back to the release point | How far the actuator must retreat before the switch resets |

## Why a snap mechanism has a gap at all

The gap is where the snap gets its energy. In that precision-switch bulletin, a plot of force against plunger position comes with the explanation that energy stored in the switch mechanism on the way in is partly spent snapping the contact over. On the way out, the mechanism spends energy again snapping it back. On the bulletin's force-against-position graph, that energy is the area enclosed "as the plunger moves through the differential travel."

The same bulletin explains the design trade. Building a mechanism with very high, constant contact force at any plunger position is "relatively easy," the bulletin says. The catch is that it "entails a wide differential travel and force differential, neither of which is desirable." Makers settle on contact force that's high enough for good performance without an unduly wide gap. The force differential it mentions is the difference between the operating force and the release force. One general-purpose basic switch datasheet, for example, lists 3.92 to 6.13 N of operating force on its pin plunger model against a release force of at least 2.79 N.

## What the gap protects against, and what it doesn't

Once a switch has operated, its contacts don't return until the actuator backs off past the release point. A wobble smaller than the movement differential therefore can't switch the contacts back, which is the protection summaries of the term point to.

The protection stops at the edges of the gap. According to the precision-switch bulletin, contact force falls as the plunger nears the operating or release point and is zero the instant the contacts separate. Near either point, the bulletin adds, a jar "may cause the switch mechanism to snap over prematurely." The bulletin describes the effect as a shift of the operating or release point that narrows the differential travel. A switch maker's FAQ on how far to push a basic switch gives the practical rule: an actuator that stops near the operating or release position "may create chattering or bouncing."

In practice the gap and the push depth work together. The gap stops a switch that has already operated from releasing on a small wobble. A push well past the operating point, which the general-purpose basic switch datasheet cited above sets at 70% to 100% of the rated overtravel, keeps the contacts away from the low-force zone in the first place.

## What makes the gap bigger or smaller

| Factor | What happens | Who says so |
|---|---|---|
| Lever or leaf actuator | Differential travel measured at the free end of a lever "often is considerably greater" than at the plunger; a ratio as high as 20 to 1 is "not unusual" | Precision-switch technical bulletin |
| Actuator style on one switch body | One general-purpose basic switch lists a movement differential of 0.2 mm max. with a pin plunger and 2.4 mm max. with a hinge lever | General-purpose basic switch datasheet |
| Electrical load on the normally open (NO) circuit | From cycle to cycle, some release points move in the direction that widens the gap; operating points stay put | Precision-switch technical bulletin |
| Electrical load on the normally closed (NC) circuit | From cycle to cycle, some operating points move in the direction that widens the gap; release points stay put | Precision-switch technical bulletin |
| Lower switched current | Less cycle-to-cycle spread, and fewer cycles with a widened gap | Precision-switch technical bulletin |
| Settling in during the first several hundred operations | With a negligible load at room conditions, operating and release points shift together, by perhaps 0.0005 in, and the gap stays fairly constant | Precision-switch technical bulletin |
| Vibration or shock near the switching points | Premature snap-over, which narrows the gap | Precision-switch technical bulletin |

For anyone reading a datasheet, the table has a practical side. The listed figure is a maximum on the terminology page and the general-purpose datasheet above, so a measured gap smaller than that is within spec. A figure for a plunger model doesn't carry over to the lever model of the same series, as the plunger and hinge lever pair in the table shows.

## Reading movement differential on a datasheet

On that general-purpose basic switch datasheet, the pin plunger model shows how the numbers fit together. The datasheet gives an operating position of 16.3 ± 0.4 mm on its dimension drawing and a movement differential of 0.2 mm max. The release position therefore sits no more than 0.2 mm toward the free position from wherever that particular switch actually operates.

Don't add the travel limits together to get a total stroke. Pretravel is given as a maximum, overtravel as a minimum and movement differential as a maximum, so stacking them describes no single real switch. If your application needs the switch to reset within a set distance, measure the operating and release points on a sample and compare the gap with the datasheet maximum.

## FAQ

### What is the purpose of a micro switch?

A micro switch turns a very small, repeatable movement into a clean electrical change. A maker's bulletin on applying precision switches says these switches let designers sense movement "in the order of .001 of an inch" quickly and reliably, without high force or wide differentials. The movement differential is part of what makes that repeatable.

### What is a switch lever?

A switch lever is an arm fitted over the plunger so a cam, door or slide can operate the switch with less force but more travel. The lever also widens the movement differential: The general-purpose basic switch datasheet cited above lists 2.4 mm max. for the hinge lever version against 0.2 mm max. at the bare plunger. The spring lever guide covers the lever in detail.

### How does a differential pressure switch work?

A pressure switch maker's introduction to differential pressure switches describes a spring-loaded diaphragm between two pressure inputs that moves and pushes on a snap switch. Its example switch trips as pressure rises to 3-1/2 inches of water column and resets only when pressure falls to about 2.4, a gap the introduction calls the dead band. In the same document's words, the "dead band is inherent in a snap switch," and the document traces it partly to the de-actuation travel of the switch lever, which is the movement differential seen as a pressure gap.

## Where movement differential matters when you set up a switch

Check the movement differential whenever the switch has to reset at a known position, such as a CNC lathe home switch whose release point sets the zero. Compare it with the pretravel and overtravel on the same sheet, and remember that a lever version, a heavier load or a cam that meets the actuator off-line can each move the reset point. If a wider or narrower gap is the goal, the hysteresis selection guide covers choosing for it.
