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

"Movement differential" is Omron's name for a distance that Honeywell and Crouzet call differential travel. Summaries of the term describe it as the gap between where a switch turns on and where it turns back off, a gap that stops small vibrations from flicking the contacts. **The gap is designed into the snap mechanism, and it blocks only one kind of flicker: a switch resting near either end of it can still chatter, because its contact force there is near zero.** The distance is followed here through its names, a single press-and-release cycle, the design reason behind it and what makes it grow.

## Quick answer

Movement differential is the distance between the actuator position where a micro switch's contacts snap over on the way in and the position where they snap back on the way out. Panasonic's terminology page lists it as a maximum value, in millimeters for a straight-line actuator or degrees for one that rotates. Honeywell and Crouzet call the same distance differential travel.

## One distance, several names

Every maker measures the same thing: how far the actuator has to back off after the switch operates before the contacts return. The names and abbreviations differ, and one abbreviation means opposite things depending on whose datasheet you're reading.

| Maker and document | Name and abbreviation | How the document defines it |
|---|---|---|
| Omron, A-20G datasheet | Movement differential (MD), listed as max. | Gap between the operating position (OP) and the release position (RP) |
| Panasonic, technical terminology page | Movement differential (MD), max. | "The distance or degree from operating position to release position of the actuator" |
| Honeywell, SE/XE datasheet | Differential travel (D.T.), max. | Actuator travel "from point where contacts 'snap-over' to point where they 'snap-back'" |
| Crouzet, Basic Technical Concepts | Differential travel (DT) | "Distance between the operating position OP and the release position RLP" |

The trap is the letters RP. Panasonic's page and Omron's FAQE20046 use RP for the release position, the point where the contacts snap back. Crouzet uses RP for the rest position, where the actuator sits with nothing touching it, and writes RLP for the release position. When two datasheets disagree about RP, read each one's own legend before comparing numbers.

## How the gap appears in one press and release

Honeywell's General Technical Bulletin #14, Applying Precision Switches, walks through a full cycle of a plunger switch:

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

The gap is where the snap gets its energy. Honeywell's Bulletin #14 plots force against plunger position and explains that energy stored in the switch mechanism on the way in is partly spent snapping the contact over. On the way out, the mechanism spends energy again snapping it back. On the bulletin's force-against-position graph, that energy is the area enclosed "as the plunger moves through the differential travel."

The same bulletin explains the design trade. Building a mechanism with very high, constant contact force at any plunger position is "relatively easy," the bulletin says. The catch is that it "entails a wide differential travel and force differential, neither of which is desirable." Makers settle on contact force that's high enough for good performance without an unduly wide gap. The force differential it mentions is the difference between the operating force and the release force. Omron's A-20G datasheet, for example, lists 3.92 to 6.13 N of operating force on the pin plunger model against a release force of at least 2.79 N.

## What the gap protects against, and what it doesn't

Once a switch has operated, its contacts don't return until the actuator backs off past the release point. A wobble smaller than the movement differential therefore can't switch the contacts back, which is the protection summaries of the term point to.

The protection stops at the edges of the gap. Honeywell's Bulletin #14 explains that contact force falls as the plunger nears the operating or release point and is zero the instant the contacts separate. Near either point, the bulletin adds, a jar "may cause the switch mechanism to snap over prematurely." The bulletin describes the effect as a shift of the operating or release point that narrows the differential travel. Omron's FAQE20046 on how far to push a basic switch gives the practical rule: an actuator that stops near the operating or release position "may create chattering or bouncing."

In practice the gap and the push depth work together. The gap stops a switch that has already operated from releasing on a small wobble. A push well past the operating point, which Omron's A-20G datasheet sets at 70% to 100% of the rated overtravel, keeps the contacts away from the low-force zone in the first place.

## What makes the gap bigger or smaller

| Factor | What happens | Who says so |
|---|---|---|
| Lever or leaf actuator | Differential travel measured at the free end of a lever "often is considerably greater" than at the plunger; a ratio as high as 20 to 1 is "not unusual" | Honeywell GTB #14 |
| Actuator style on one switch body | Omron's A-20G lists a movement differential of 0.2 mm max. with a pin plunger and 2.4 mm max. with a hinge lever | Omron A-20G datasheet |
| Electrical load on the normally open (NO) circuit | From cycle to cycle, some release points move in the direction that widens the gap; operating points stay put | Honeywell GTB #14 |
| Electrical load on the normally closed (NC) circuit | From cycle to cycle, some operating points move in the direction that widens the gap; release points stay put | Honeywell GTB #14 |
| Lower switched current | Less cycle-to-cycle spread, and fewer cycles with a widened gap | Honeywell GTB #14 |
| Settling in during the first several hundred operations | With a negligible load at room conditions, operating and release points shift together, by perhaps 0.0005 in, and the gap stays fairly constant | Honeywell GTB #14 |
| Vibration or shock near the switching points | Premature snap-over, which narrows the gap | Honeywell GTB #14 |

For anyone reading a datasheet, the table has a practical side. The listed figure is a maximum on Panasonic's and Omron's sheets, so a measured gap smaller than that is within spec. A figure for a plunger model doesn't carry over to the lever model of the same series, as the A-20G pair shows.

## Reading movement differential on a datasheet

Omron's A-20G-B pin plunger model shows how the numbers fit together. The datasheet gives an operating position of 16.3 ± 0.4 mm on its dimension drawing and a movement differential of 0.2 mm max. The release position therefore sits no more than 0.2 mm toward the free position from wherever that particular switch actually operates.

Don't add the travel limits together to get a total stroke. Pretravel is given as a maximum, overtravel as a minimum and movement differential as a maximum, so stacking them describes no single real switch. If your application needs the switch to reset within a set distance, measure the operating and release points on a sample and compare the gap with the datasheet maximum.

## FAQ

### What is the purpose of a micro switch?

A micro switch turns a very small, repeatable movement into a clean electrical change. Honeywell's Bulletin #14 says these switches let designers sense movement "in the order of .001 of an inch" quickly and reliably, without high force or wide differentials. The movement differential is part of what makes that repeatable.

### What is a switch lever?

A switch lever is an arm fitted over the plunger so a cam, door or slide can operate the switch with less force but more travel. The lever also widens the movement differential: Omron's A-20G datasheet lists 2.4 mm max. for the hinge lever version against 0.2 mm max. at the bare plunger. The spring lever guide covers the lever in detail.

### How does a differential pressure switch work?

Dwyer's introduction to differential pressure switches describes a spring-loaded diaphragm between two pressure inputs that moves and pushes on a snap switch. Its example switch trips as pressure rises to 3-1/2 inches of water column and resets only when pressure falls to about 2.4, a gap Dwyer calls the dead band. Dwyer states the "dead band is inherent in a snap switch" and traces it partly to the de-actuation travel of the switch lever, which is the movement differential seen as a pressure gap.

## Where movement differential matters when you set up a switch

Check the movement differential whenever the switch has to reset at a known position, such as a CNC lathe home switch whose release point sets the zero. Compare it with the pretravel and overtravel on the same sheet, and remember that a lever version, a heavier load or a cam that meets the actuator off-line can each move the reset point. If a wider or narrower gap is the goal, the hysteresis selection guide covers choosing for it.

## Sources

- Honeywell MICRO SWITCH, General Technical Bulletin #14, Applying Precision Switches
- Honeywell, MICRO SWITCH SE/XE Series Sealed Miniature Basic Switches datasheet
- Omron, General-purpose Basic Switch A (A-20G) datasheet
- Omron FAQE20046, Please advise the appropriate amount of pushing for a basic switch (DigiKey TechForum reprint)
- Panasonic Industry, Micro Switches & Detection Switches Technical Terminology
- Crouzet, Microswitches: Basic Technical Concepts (12/2020)
- Dwyer Instruments, Introduction to Precision Low Range Differential Pressure Switches
