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

Operating force is the push a home switch's actuator needs before its contacts snap from the resting state to the operated state. Switch makers' terminology pages list it as a maximum, in newtons, applied at the actuator. On a CNC lathe, a dog on the moving slide supplies that push, and reliable homing also depends on overtravel, approach speed and a force ceiling.

## What operating force means on a switch datasheet

One sealed miniature basic switch datasheet defines operating force (OF) as the force applied to the plunger or actuator "to cause contact 'snap-over'" of the switching mechanism. Snap-over is the moment the moving contact jumps from one side to the other. A switch maker's terminology page gives the same definition and marks OF as a maximum. Read that way, a switch of that part number should trip at or below the listed force. Another maker's basic technical concepts guide measures the same force from the position where nothing touches the actuator to the position where the mechanism trips.

The force isn't steady along the stroke. A switch maker's technical bulletin on applying precision switches plots plunger force against plunger position. Force climbs as the plunger goes down and energy builds up in the mechanism. At the operating point, the bulletin explains, some of that stored energy drives the snap-over, so the force pushing back on the actuating device drops. On the way back, the contacts stay put until the release point, and the bulletin calls the force still holding the plunger there the release force (RF).

Where the force is measured matters as much as its size. The sealed miniature switch datasheet notes that on adjustable actuators the force is measured at the lever's maximum length. The basic technical concepts guide puts its reference point 3 mm in from the end of a flat lever. Because a lever trades force for distance, a dog that meets the lever closer to its pivot needs more force than the datasheet figure.

One general-purpose basic switch datasheet shows how far the actuator style moves the numbers on one switch body. Pretravel (PT) is the travel before the contacts switch, overtravel (OT) is the safe travel after that, and movement differential (MD) is that datasheet's name for the gap between the operating and release points.

| General-purpose basic switch figure | Pin plunger model | Hinge lever model |
|---|---|---|
| Operating force | 3.92 to 6.13 N | 0.69 N max. |
| Release force, min. | 2.79 N | 0.14 N |
| Pretravel, max. | 1.3 mm | 15.9 mm |
| Overtravel, min. | 0.25 mm | 4 mm |
| Movement differential, max. | 0.2 mm | 2.4 mm |

Swap a plunger version for a lever version during a repair and, going by that table, the dog meets a switch that needs a fraction of the force but many times the travel.

## How a lathe's homing cycle puts the switch to work

Fanuc's US patent 4,513,234, on zero-point return for machine tools, describes the classic layout. A zero-point return dog is fixed to the moving table, and a deceleration limit switch sits near the zero point on the fixed part of the machine. When the dog presses the switch, the control slows the axis.

The release matters as much as the press. The same patent states that after the dog leaves the switch, the control "considers the very next grid point encountered to be the zero point" of the axis. Grid points, in the patent's terms, are the positions at which the encoder sends its once-per-revolution pulse. The patent adds that if the switch or dog is shifted by more than one grid pitch, the distance between neighboring grid points, the table won't come to rest at the true zero point.

Fanuc's later US patent 4,680,520 names another weak point of this layout: chattering, a rapid on-off flicker of the limit switch, when the dog strikes its lever without first slowing down. Whether the switch on a given lathe is an enclosed limit switch or a bare basic switch, the dog meets the same set of datasheet limits described next.

## Why the force figure alone doesn't settle a homing fault

### Travel past the operating point

A dog that pushes only to the click leaves the contacts pressed together with almost no force. The precision-switch bulletin explains that contact force falls as the plunger nears the operating or release point and reaches zero at the instant the contacts separate. A switch maker's FAQ on how far to push a basic switch warns that an operating body stopping near either point "may create chattering or bouncing."

Each maker states the target push past the operating point in its own terms:

| Source | How far to push past the operating point, as a share of overtravel (OT, the safe travel past the click) |
|---|---|
| General-purpose basic switch datasheet | 70% to 100% of the rated OT |
| Switch maker's FAQ on pushing distance | 60% to 90% of the specified OT |
| Basic technical concepts guide | At least 0.5 times the OT, without passing the total travel position or the allowable overtravel force |

The figures differ by document, so the datasheet for the exact switch on the lathe is the one to follow.

### The force ceiling

Operating force is the least push that trips the switch, and every switch also has a most push it can take. The basic technical concepts guide defines an allowable overtravel force as the most force the actuator can take "without incurring deterioration" of the switch. The precision-switch bulletin calls it a misapplication to use a switch as the mechanical stop for a moving member. The bulletin notes that dynamic loads "can have disproportionately high static equivalents" on the plunger. The same bulletin adds that the farther the plunger is pushed, the higher the stress in the spring and the shorter the switch's life.

### Approach speed

The general-purpose basic switch datasheet sets an upper operating speed of 1 m/s and also lists a lower limit. The same datasheet warns that at extremely slow speeds the contacts "may not be switched smoothly," which can cause contact failure or welding, and that extremely fast actuation can damage the switch. The precision-switch bulletin states that 5 inches per second usually causes no trouble and singles out impact actuation as a cause of shortened life.

### Vibration and chips

A lathe shakes, and the switch feels it most near the click. The precision-switch bulletin warns that a jar near the operating or release point can snap the mechanism over early, and advises orienting the switch so acceleration can't actuate it. The general-purpose datasheet's precautions say to mount the switch away from cutting debris and to protect the actuator and body from chips that build up.

## Checking a home switch's operating force on the machine

Lock out the lathe before reaching into the axis area. OSHA's rule on the control of hazardous energy, 29 CFR 1910.147, covers servicing where unexpected start-up could injure someone, and it applies to this job.

1. **Read the part number on the switch and pull its datasheet.** Note OF, RF, PT, OT and the movement differential, plus where the force is measured on the actuator. Without that sheet, there's no number to compare a reading against.
2. **Press the actuator at the maker's reference point with a push gauge.** Note the reading at the click. A reading above the datasheet maximum points to binding in the actuator or a bent lever rather than a weak dog.
3. **Inspect the lever.** A switch maker's FAQ on what causes basic switch failures calls a deformed actuator lever "a relatively common cause," often from something caught in it. A larger bend angle or more play than a new lever is the sign it names.
4. **Measure how far the dog pushes the actuator past the click.** Compare it with the overtravel table in the section above. A dog that stops at the click invites on-off flicker, and one that bottoms the actuator overloads it.
5. **Check continuity at the click and at the release with a meter.** In Fanuc's scheme the control takes the next grid point after the release as zero, so a release that wanders moves the home position.

## FAQ

### What is the purpose of a micro switch?

A micro switch turns a small, precise movement into a clean electrical change. The precision-switch bulletin says these switches let designers sense movement "in the order of .001 of an inch" quickly and reliably, without high force or wide differentials. On a lathe, that precision is why a single switch and dog can mark a home position.

### What should the resistance of a closed-on switch be?

Very close to zero. [ZINGEAR G5W11-WZ200-W2](https://www.zingear-switch.com/zingear-micro-switch-g5w11-wz200-w2-explosion-proof-micro-switch.html){: rel="nofollow noopener noreferrer" }, a sealed IP67 model in ZING EAR's industrial heavy-duty line, lists contact resistance of 100 mΩ max. on its product page, a tenth of an ohm that an ordinary meter shows as close to zero. A closed contact that shows a clear resistance on the meter's lowest ohms range, or flickers as you tap the switch, points to contamination or wear.

### What does actuation force mean on a keyboard?

It's the same idea applied to a key. One switch maker's article on actuation or operating force says the two terms "mean the same thing" in the switch world and describes it as how hard you have to press a switch to make it work. The difference on a lathe is that the dog does the pressing, so the force has to be read alongside travel and speed.

## What to compare after the operating force

Once the operating force checks out, set the dog's push against the switch's overtravel and its allowable force, then confirm the approach speed falls inside the datasheet range. If the switch still trips unreliably, the movement differential between the operating and release points and the alignment of the dog or cam with the actuator are the next places to look. For lever-actuated home switches, the spring lever's effect on force and travel explains why a replacement with a different lever behaves differently, and a switch that's pressed too slowly can show the same symptoms as a weak one.

For a manufacturer example of switches built for this duty, [ZING EAR](https://www.zingear-switch.com/){: rel="nofollow noopener noreferrer" } says its heavy-duty industrial micro switches are developed for heavy industrial production lines, lifting equipment and automated machine tools. The company describes the lineup as having a reinforced mechanical structure and as having gone through environmental simulation testing. The force, travel and speed checks above are still what decide whether a given model fits your lathe.

## Sources

- Fanuc, US 4,513,234, Method and apparatus for controlling zero-point return of a movable element
- Fanuc, US 4,680,520, Zero-point return method
- US Occupational Safety and Health Administration, 29 CFR 1910.147, The control of hazardous energy (lockout/tagout)
- ZING EAR, Industrial Heavy-duty Micro Switch product line page: https://www.zingear-switch.com/industrial-heavy-duty-micro-switch
- ZING EAR, ZINGEAR G5W11-WZ200-W2 product page: https://www.zingear-switch.com/zingear-micro-switch-g5w11-wz200-w2-explosion-proof-micro-switch.html
