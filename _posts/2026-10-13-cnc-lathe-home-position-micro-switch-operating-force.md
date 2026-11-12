---
title: "CNC Lathe Home Position Micro Switch Operating Force: What the Number Covers in a Homing Cycle"
description: "Operating force is the push a home switch needs before its contacts snap over. See how it relates to dog travel, overtravel and speed on a CNC lathe."
date: 2026-10-13 13:45:35 +0800
category: Applications
tags:
  - cnc lathe home position micro switch operating force
  - micro switches
  - Applications
author: editorial_team
seo_title: "CNC Lathe Home Position Micro Switch Operating Force"
last_updated: 2026-11-12
---

Press the home button on a CNC lathe and each axis creeps toward one end until a switch clicks and the slide settles at zero. Switch datasheets put a number on that click, the operating force, and it's the figure people reach for when homing turns unreliable. **That number only says how hard the dog on the slide must push; clean homing also depends on how far past the click it pushes, how fast it arrives and how much force the switch can take.** The operating force is traced here from its datasheet definition, through the dog-and-switch homing sequence, to checks you can make on the machine.

## Quick answer

Operating force is the push a home switch's actuator needs before its contacts snap from the resting state to the operated state. Panasonic's switch terminology page lists it as a maximum, in newtons, applied at the actuator. On a CNC lathe, a dog on the moving slide supplies that push, and reliable homing also depends on overtravel, approach speed and a force ceiling.

## Where ZING EAR fits a CNC lathe home switch

For a manufacturer example of switches built for this duty, [ZING EAR](https://www.zingear-switch.com/){:rel="nofollow"} says its heavy-duty industrial micro switches are developed for heavy industrial production lines, lifting equipment and automated machine tools. The company describes the lineup as having a reinforced mechanical structure and as having gone through environmental simulation testing. The force, travel and speed checks in this guide are still what decide whether a given model fits your lathe.

Start with ZING EAR's [industrial heavy-duty micro switch range](https://www.zingear-switch.com/industrial-heavy-duty-micro-switch){: rel="nofollow noopener noreferrer" } when screening a candidate for an automated machine tool. Its category page describes the intended applications and construction; it does not give one operating-force figure for every model or confirm a particular part for your lathe. Ask for the exact model's operating force, release force, pretravel, overtravel, allowable overtravel force, actuator reference point and environmental rating. Then compare those figures with the homing dog and the machine's chip and coolant exposure. The Omron numbers below illustrate why actuator choice matters; they are not specifications for a ZING EAR switch.

## What operating force means on a switch datasheet

Honeywell's datasheet for its [SE/XE sealed miniature basic switches](https://docs.rs-online.com/588c/A700000015332771.pdf){: rel="nofollow noopener noreferrer" } defines operating force (OF) as the force applied to the plunger or actuator "to cause contact 'snap-over'" of the switching mechanism. Snap-over is the moment the moving contact jumps from one side to the other. [Panasonic's terminology page](https://industry.panasonic.com/global/en/products/control/switch/micro/explain_term){: rel="nofollow noopener noreferrer" } gives the same definition and marks OF as a maximum. Read that way, a switch of that part number should trip at or below the listed force. Crouzet's [Basic Technical Concepts](https://zoro.com/static/cms/enhanced_pdf/Waldom%20Electronics_SWxxbasicxxtechnicalxxconceptsxxENxx679897.pdf){: rel="nofollow noopener noreferrer" } document measures the same force from the position where nothing touches the actuator to the position where the mechanism trips.

The force isn't steady along the stroke. Honeywell's General Technical Bulletin #14, [Applying Precision Switches](https://prod-edam.honeywell.com/content/dam/honeywell-edam/sps/siot/ja/products/switches/basic-switches/common/documents/sps-ast-applying-precision-switches-technical-note.pdf){: rel="nofollow noopener noreferrer" }, plots plunger force against plunger position. Force climbs as the plunger goes down and energy builds up in the mechanism. At the operating point, the bulletin explains, some of that stored energy drives the snap-over, so the force pushing back on the actuating device drops. On the way back, the contacts stay put until the release point, and the bulletin calls the force still holding the plunger there the release force (RF).

Where the force is measured matters as much as its size. Honeywell's SE/XE datasheet notes that on adjustable actuators the force is measured at the lever's maximum length, and Crouzet puts its reference point 3 mm in from the end of a flat lever. Because a lever trades force for distance, a dog that meets the lever closer to its pivot needs more force than the datasheet figure.

Omron's [datasheet for its A-20G general-purpose basic switch](https://static.chipdip.ru/lib/275/DOC011275390.pdf){: rel="nofollow noopener noreferrer" } shows how far the actuator style moves the numbers on one switch body. Pretravel (PT) is the travel before the contacts switch, overtravel (OT) is the safe travel after that, and movement differential (MD) is Omron's name for the gap between the operating and release points.

| Omron A-20G figure | Pin plunger (A-20G-B) | Hinge lever (A-20GV-B) |
|---|---|---|
| Operating force | 3.92 to 6.13 N | 0.69 N max. |
| Release force, min. | 2.79 N | 0.14 N |
| Pretravel, max. | 1.3 mm | 15.9 mm |
| Overtravel, min. | 0.25 mm | 4 mm |
| Movement differential, max. | 0.2 mm | 2.4 mm |

Swap a plunger version for a lever version during a repair and, going by Omron's table, the dog meets a switch that needs a fraction of the force but many times the travel.

## How a lathe's homing cycle puts the switch to work

Fanuc's US patent 4,513,234, on [zero-point return for machine tools](https://patents.google.com/patent/US4513234A/en){: rel="nofollow noopener noreferrer" }, describes the classic layout. A zero-point return dog is fixed to the moving table, and a deceleration limit switch sits near the zero point on the fixed part of the machine. When the dog presses the switch, the control slows the axis.

The release matters as much as the press. The same patent states that after the dog leaves the switch, the control "considers the very next grid point encountered to be the zero point" of the axis. Grid points, in the patent's terms, are the positions at which the encoder sends its once-per-revolution pulse. The patent adds that if the switch or dog is shifted by more than one grid pitch, the distance between neighboring grid points, the table won't come to rest at the true zero point.

Fanuc's later US patent 4,680,520 names another weak point of this layout: chattering, a rapid on-off flicker of the limit switch, when the dog strikes its lever without first slowing down. Whether the switch on a given lathe is an enclosed limit switch or a bare basic switch, the dog meets the same set of datasheet limits described next.

## Why the force figure alone doesn't settle a homing fault

### Travel past the operating point

A dog that pushes only to the click leaves the contacts pressed together with almost no force. Honeywell's Bulletin #14 explains that contact force falls as the plunger nears the operating or release point and reaches zero at the instant the contacts separate. Omron's FAQ on [how far to push a basic switch](https://forum.digikey.com/t/please-advise-the-appropriate-amount-of-pushing-for-a-basic-switch/35452){: rel="nofollow noopener noreferrer" } (FAQE20046, reprinted on DigiKey's forum) warns that an operating body stopping near either point "may create chattering or bouncing."

Each maker states the target push past the operating point in its own terms:

| Source | How far to push past the operating point, as a share of overtravel (OT, the safe travel past the click) |
|---|---|
| Omron A-20G datasheet | 70% to 100% of the rated OT |
| Omron FAQE20046 | 60% to 90% of the specified OT |
| Crouzet Basic Technical Concepts | At least 0.5 times the OT, without passing the total travel position or the allowable overtravel force |

The figures differ by document, so the datasheet for the exact switch on the lathe is the one to follow.

### The force ceiling

Operating force is the least push that trips the switch, and every switch also has a most push it can take. Crouzet defines an allowable overtravel force as the most force the actuator can take "without incurring deterioration" of the switch. Honeywell's Bulletin #14 calls it a misapplication to use a switch as the mechanical stop for a moving member. The bulletin notes that dynamic loads "can have disproportionately high static equivalents" on the plunger. The same bulletin adds that the farther the plunger is pushed, the higher the stress in the spring and the shorter the switch's life.

### Approach speed

Omron's datasheet for the A-20G sets an upper operating speed of 1 m/s and also lists a lower limit. The same datasheet warns that at extremely slow speeds the contacts "may not be switched smoothly," which can cause contact failure or welding, and that extremely fast actuation can damage the switch. Honeywell's bulletin states that 5 inches per second usually causes no trouble and singles out impact actuation as a cause of shortened life.

### Vibration and chips

A lathe shakes, and the switch feels it most near the click. Honeywell's bulletin warns that a jar near the operating or release point can snap the mechanism over early, and advises orienting the switch so acceleration can't actuate it. Omron's A-20G precautions say to mount the switch away from cutting debris and to protect the actuator and body from chips that build up.

## Checking a home switch's operating force on the machine

Lock out the lathe before reaching into the axis area. OSHA's rule on the [control of hazardous energy, 29 CFR 1910.147](https://www.ecfr.gov/current/title-29/subtitle-B/chapter-XVII/part-1910/subpart-J/section-1910.147){: rel="nofollow noopener noreferrer" }, covers servicing where unexpected start-up could injure someone, and it applies to this job.

1. **Read the part number on the switch and pull its datasheet.** Note OF, RF, PT, OT and the movement differential, plus where the force is measured on the actuator. Without that sheet, there's no number to compare a reading against.
2. **Press the actuator at the maker's reference point with a push gauge.** Note the reading at the click. A reading above the datasheet maximum points to binding in the actuator or a bent lever rather than a weak dog.
3. **Inspect the lever.** Omron's FAQ on [what causes basic switch failures](https://forum.digikey.com/t/what-may-have-caused-a-basic-switch-failure/35453){: rel="nofollow noopener noreferrer" } calls a deformed actuator lever "a relatively common cause," often from something caught in it. A larger bend angle or more play than a new lever is the sign it names.
4. **Measure how far the dog pushes the actuator past the click.** Compare it with the overtravel table in the section above. A dog that stops at the click invites on-off flicker, and one that bottoms the actuator overloads it.
5. **Check continuity at the click and at the release with a meter.** In Fanuc's scheme the control takes the next grid point after the release as zero, so a release that wanders moves the home position.

## FAQ

### What is the purpose of a micro switch?

A micro switch turns a small, precise movement into a clean electrical change. Honeywell's Bulletin #14 says these switches let designers sense movement "in the order of .001 of an inch" quickly and reliably, without high force or wide differentials. On a lathe, that precision is why a single switch and dog can mark a home position.

### What should the resistance of a closed-on switch be?

Very close to zero. Omron's A-20G datasheet lists contact resistance of 15 mΩ max. as an initial value, which an ordinary meter shows as a reading of essentially zero ohms. A closed contact that shows a clear resistance on the meter's lowest ohms range, or flickers as you tap the switch, points to contamination or wear.

### What does actuation force mean on a keyboard?

It's the same idea applied to a key. E-Switch's article on [actuation or operating force](https://www.e-switch.com/news-events/blog/switches-simplified/what-is-actuation-or-operating-force/){: rel="nofollow noopener noreferrer" } says the two terms "mean the same thing" in the switch world and describes it as how hard you have to press a switch to make it work. The difference on a lathe is that the dog does the pressing, so the force has to be read alongside travel and speed.

## What to compare after the operating force

Once the operating force checks out, set the dog's push against the switch's overtravel and its allowable force, then confirm the approach speed falls inside the datasheet range. If the switch still trips unreliably, the [movement differential between the operating and release points](/guides/micro-switch-movement-differential-explained/) and the [alignment of the dog or cam with the actuator](/guides/micro-switch-cam-misalignment-explained/) are the next places to look. For lever-actuated home switches, the [spring lever's effect on force and travel](/guides/micro-switch-spring-lever/) explains why a replacement with a different lever behaves differently, and a [switch that's pressed too slowly](/guides/micro-switch-slow-actuation-explained/) can show the same symptoms as a weak one.

## Related guides

- [accelerator pedal position stop micro switch NO and NC terminals](/guides/accelerator-pedal-position-stop-micro-switch-no-and-nc-terminals/)
- [industrial boiler travel limit micro switch maintenance](/guides/industrial-boiler-travel-limit-micro-switch-maintenance/)
- [access control door position micro switch NO and NC terminals](/guides/access-control-door-position-micro-switch-no-and-nc-terminals/)
- [capping machine guard interlock micro switch actuator travel](/guides/capping-machine-guard-interlock-micro-switch-actuator-travel/)

## Sources

- Honeywell, MICRO SWITCH SE/XE Series Sealed Miniature Basic Switches datasheet (operating characteristics definitions)
- Honeywell MICRO SWITCH, General Technical Bulletin #14, Applying Precision Switches
- Panasonic Industry, Micro Switches & Detection Switches Technical Terminology
- Crouzet, Microswitches: Basic Technical Concepts (12/2020)
- Omron, General-purpose Basic Switch A (A-20G) datasheet
- Omron FAQE20046, Please advise the appropriate amount of pushing for a basic switch (DigiKey TechForum reprint)
- Omron FAQ, What may have caused a basic switch failure? (DigiKey TechForum reprint)
- Fanuc (Fujitsu Fanuc), US 4,513,234, Method and apparatus for controlling zero-point return of a movable element
- Fanuc, US 4,680,520, Zero-point return method
- E-Switch, What is Actuation or Operating Force? How is it Measured?
- US Occupational Safety and Health Administration, 29 CFR 1910.147, The control of hazardous energy (lockout/tagout)
- ZING EAR, Industrial Heavy-duty Micro Switch product line page: https://www.zingear-switch.com/industrial-heavy-duty-micro-switch
