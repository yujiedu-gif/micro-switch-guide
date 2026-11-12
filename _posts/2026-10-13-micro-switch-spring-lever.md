---
title: "Spring Lever Micro Switch: How the Lever Carries Motion to the Snap Spring Inside"
description: "A spring lever micro switch uses a springy arm to push the plunger, while a separate spring inside snaps the contacts. See what the lever changes."
date: 2026-10-13 11:27:16 +0800
category: Basics
tags:
  - micro switch spring lever
  - micro switches
  - Basics
author: editorial_team
seo_title: "Spring Lever Micro Switch: How the Lever Works"
last_updated: 2026-11-12
---

Some micro switches carry a thin metal arm over the button, so a door edge or a cam can press them from the side. Push the end of that arm slowly and it bends or pivots for a while, then the switch clicks. **The arm and the click come from two different springs: the lever outside only moves the plunger, and a separate blade inside the switch decides the instant the contacts change over.** The lever's push is followed here from the outside in, then through what it changes on the datasheet and how to check a switch that seems dead.

## Quick answer

A spring lever micro switch is a micro switch, also called a snap-action switch, fitted with a springy arm that presses its plunger, the small button on the switch body. Honeywell's application bulletin for precision switches says such leaf springs and levers are added to allow extra travel and to lower the push needed. The contacts themselves are flipped by a separate snap-action spring inside the housing.

## Two springs, two jobs: the lever outside and the blade inside

Crouzet's [Basic Technical Concepts](https://zoro.com/static/cms/enhanced_pdf/Waldom%20Electronics_SWxxbasicxxtechnicalxxconceptsxxENxx679897.pdf){: rel="nofollow noopener noreferrer" } document draws the parts inside the housing: a plunger, a snap-acting blade, a return spring, a moving contact and fixed contacts. The plunger is the button the lever presses, and the moving contact rides on the blade, touching one fixed contact or the other. The snap-acting blade is the spring that makes the click. The blade stores energy as the plunger goes down and releases it all at once.

The lever sits outside that housing. Omron's [A-20G basic switch datasheet](https://static.chipdip.ru/lib/275/DOC011275390.pdf){: rel="nofollow noopener noreferrer" } lists hinge lever, short hinge lever and hinge roller lever versions, each with a stainless-steel lever hinged over the plunger. Honeywell's [SE/XE datasheet](https://docs.rs-online.com/588c/A700000015332771.pdf){: rel="nofollow noopener noreferrer" } lists add-on "straight leaf" and "roller leaf" actuators, which are flat springs fixed at one end. Either way, the lever's only job is to press the plunger.

The terminals tell you which way the contacts sit. Honeywell's General Technical Bulletin #14, [Applying Precision Switches](https://prod-edam.honeywell.com/content/dam/honeywell-edam/sps/siot/ja/products/switches/basic-switches/common/documents/sps-ast-applying-precision-switches-technical-note.pdf){: rel="nofollow noopener noreferrer" }, explains that with nothing pressing the plunger, the common (COM) contact rests against the normally closed (NC) contact. "Normally" means the untouched state, so the normally open (NO) contact is the one that's disconnected until the switch operates.

## How the lever carries motion to the snap, step by step

The sequence below follows Honeywell's Bulletin #14 description of a plunger switch, with the lever added in front of it.

1. A cam (a shaped wheel or block that pushes as it turns or slides), a door or a slide pushes on the end of the lever.
2. The lever pivots on its hinge, or a leaf bends, and its underside presses the plunger.
3. The plunger bends the snap-action blade inside and loads it with energy.
4. At the operating point, the blade passes its tipping point and throws the moving contact from NC to NO. The bulletin says this happens "without further movement of the plunger" and that the contact "cannot stop part way" between the two.
5. Within a few milliseconds, according to the same bulletin, the contact strikes, bounces and settles on NO.
6. The lever can keep moving past that point. The bulletin calls this extra travel overtravel, and the contacts stay switched through it.
7. On the way back, the contacts don't flip at the operating point. The contacts wait until the plunger reaches the release point, then snap back to NC.

Step 4 is where the lever's job ends and the blade's job begins. However slowly the lever moves, the blade sets the speed of the contact change, which is why Crouzet's document describes switching as "largely independent of actuating speed."

## What the lever changes: force, travel and the gap between on and off

A lever trades force for distance. Pressing near the free end of a long arm takes less force than pressing the plunger directly, but the end has to travel farther to move the plunger the same amount.

Omron's A-20G datasheet shows the trade on one switch body. Operating force (OF) is the push needed to make the contacts switch. Pretravel (PT) is the travel before they switch, and overtravel (OT) is the safe travel after. Movement differential (MD) is Omron's name for the gap between the operating and release points.

| Omron A-20G figure | Pin plunger (A-20G-B) | Hinge lever (A-20GV-B) |
|---|---|---|
| Operating force | 3.92 to 6.13 N | 0.69 N max. |
| Pretravel, max. | 1.3 mm | 15.9 mm |
| Overtravel, min. | 0.25 mm | 4 mm |
| Movement differential, max. | 0.2 mm | 2.4 mm |

A leaf doesn't always cut the force as sharply. Honeywell's SE/XE datasheet lists its 1SE1 plunger switch at 142 to 482 grams-force of operating force and the same switch with the JE-1 straight leaf at 340 grams-force max. The leaf's bigger effect in Honeywell's table is on travel, with maximum pretravel growing from 1.27 mm to 3.81 mm. The same table lists maximum differential travel, Honeywell's name for the on-off gap Omron calls movement differential, growing from 0.1 mm to 0.64 mm.

Honeywell's Bulletin #14 explains why the gap between on and off grows. Differential travel measured at the free end of a leaf or lever "often is considerably greater" than at the plunger. The bulletin calls a ratio as high as 20 to 1 "not unusual" for that comparison. The same lever also magnifies any drift, meaning small shifts over time in where the switch turns on and off. The bulletin states that the greatest precision comes from pressing the plunger directly, along its axis.

The force figure that applies to your switch also depends on these details:

- **Where the force is measured.** Honeywell's SE/XE datasheet measures force on adjustable actuators at the lever's maximum length, and Crouzet's document puts its reference point 3 mm in from the end of a flat lever. Pressing nearer the hinge takes more force.
- **Which way the switch is mounted.** Omron's [SS miniature basic switch datasheet](https://electrokit.com/upload/quick/d7/22/4fba_41011077-tds.pdf){: rel="nofollow noopener noreferrer" } gives separate reference values for lever models mounted so the lever's own weight doesn't rest on the plunger.

## Leaf, hinge and roller versions of the lever

| Lever style | What it looks like | Where makers point it |
|---|---|---|
| Hinge lever | Metal arm on a pivot over the plunger | Omron lists it on both the A-20G and SS series |
| Hinge roller lever | Hinge lever with a wheel at the tip | Honeywell's Bulletin #14 suggests a roller lever, "especially for cam actuation" |
| Simulated roller lever | Arm tip bent into a rounded shape that doesn't spin | Listed on Omron's SS series |
| Straight leaf | Flat spring strip fixed at one end | Honeywell's JE-1 add-on actuator for the SE switch |
| Roller leaf | Leaf spring with a roller at the tip | Honeywell's JE-4 and JE-5 add-on actuators |

A roller matters when the pushing object slides across the lever instead of pressing straight down. Honeywell's bulletin explains that a push at an angle to the plunger causes side thrust that wears the plunger's bearing surfaces, and it names roller plungers and roller levers as the way around that. Crouzet's document adds that when the movement is fast, the ramp that meets the roller should be shaped to avoid "violent impact or abrupt release."

## How to check a spring lever micro switch

Unplug the appliance or lock out the machine first, and never tape or wedge a lever that serves as a safety interlock, such as on a door.

1. **Look at the lever.** Omron's FAQ on [what causes basic switch failures](https://forum.digikey.com/t/what-may-have-caused-a-basic-switch-failure/35453){: rel="nofollow noopener noreferrer" } calls a deformed actuator lever "a relatively common cause" of failure, usually from something getting caught in it. A larger bend angle or more play than a new lever means it's deformed.
2. **Press the lever end slowly and listen.** A click means the blade inside snapped. It doesn't prove the contacts carry current, because the same Omron FAQ lists contact failure as a separate electrical fault.
3. **Test with a meter on continuity.** With the lever free, the common terminal to the normally closed terminal should read closed, and common to normally open should read open. With the lever held past the click, the readings should swap.
4. **Let the lever back slowly.** The readings should swap back a little later than they switched on the way down, because the release point sits above the operating point.

If the meter readings are right but the machine still misbehaves, look at how the lever is being pushed. Too little travel past the click, a cam that meets the lever at an angle and a shifted mounting all show up this way.

## Two common readings of the lever that go too far

**"A long lever makes the switch more sensitive."** One widely repeated summary of how a lever switch works calls the lever's effect "amplified sensitivity." The lighter push is real, as Omron's A-20G figures show. The switch also becomes less precise, though: Honeywell's bulletin ties levers to wider differential travel and magnified drift, and puts the greatest precision at the plunger.

**"A snap-action mechanism prevents arcing."** The same summary credits the fast snap with preventing sparking at the contacts. The snap does keep the contacts from lingering partly open, but it doesn't stop an arc from forming. Honeywell's Bulletin #14 states that the arc between opening contacts "may persist for a few milliseconds after the contacts are completely open," and says this is normal and that switches are designed for it.

## FAQ

### How does a micro switch work?

A micro switch loads a spring as its plunger is pressed, and at a set point the spring flips the moving contact from one fixed contact to the other. Honeywell's Bulletin #14 says the contact can't stop partway and settles within a few milliseconds. A lever, when fitted, only supplies the push on the plunger.

### What is inside a micro switch?

Crouzet's Basic Technical Concepts shows a plunger, a snap-acting blade, a return spring, a moving contact and fixed contacts, all in one housing. The changeover (SPDT) version in that document has three terminals: COM, NO and NC.

### How does a lever switch work?

A lever switch is a micro switch with an arm that presses the plunger for you. The arm lets something moving sideways, like a cam or a door, operate the switch with less force but more travel. Omron's A-20G datasheet shows the hinge lever version needing 0.69 N max. against 3.92 to 6.13 N at the bare plunger.

### How to check a micro switch?

Disconnect power, then use a meter on continuity: COM to NC closed and COM to NO open with nothing pressed, and the reverse when the actuator is pressed past the click. Check the lever for bending or extra play, which Omron's FAQ lists as a common cause of failure.

## Matching a replacement lever switch

When you replace a spring lever micro switch, match the lever style and length as well as the switch body, because Omron's and Honeywell's tables show the lever changing force, travel and differential travel. If the original is a [leaf lever micro switch](/guides/leaf-lever-micro-switch-working-principle/), a hinge lever of a different length won't trip at the same point. The [actuator types guide](/guides/micro-switch-actuator-types/) compares the other options, and the [movement differential explainer](/guides/micro-switch-movement-differential-explained/) covers why a lever switch turns off later than it turns on. Where the lever is driven by a cam, [cam misalignment](/guides/micro-switch-cam-misalignment-explained/) and a [bent hinge lever](/guides/hinge-lever-micro-switch-failure/) are the usual next suspects.


## Related guides

- [micro switch mechanical vibration testing](/guides/micro-switch-mechanical-vibration-testing/)
- [flexible rod micro switch travel](/guides/flexible-rod-micro-switch-travel/)
- [what is micro switch contact bounce](/guides/what-is-micro-switch-contact-bounce/)
- [push on push off micro switch](/guides/push-on-push-off-micro-switch/)

## Sources

- Honeywell MICRO SWITCH, General Technical Bulletin #14, Applying Precision Switches
- Honeywell, MICRO SWITCH SE/XE Series Sealed Miniature Basic Switches datasheet (incl. JE series auxiliary actuators)
- Crouzet, Microswitches: Basic Technical Concepts (12/2020)
- Omron, General-purpose Basic Switch A (A-20G) datasheet
- Omron, Miniature Basic Switch SS datasheet (Cat. No. B053-E2-11D)
- Omron FAQ, What may have caused a basic switch failure? (DigiKey TechForum reprint)
