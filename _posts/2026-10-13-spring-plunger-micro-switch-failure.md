---
title: "Spring Plunger Micro Switch Failure: What Goes Wrong and How to Tell Which Part Failed"
description: "A spring plunger micro switch fails at the plunger, the snap mechanism or the contacts. How to tell which one, using Omron and Crouzet datasheet guidance."
date: 2026-10-13 11:27:16 +0800
category: Troubleshooting
tags:
  - spring plunger micro switch failure
  - micro switches
  - Troubleshooting
author: editorial_team
seo_title: "Spring Plunger Micro Switch Failure: Causes and Checks"
last_updated: 2026-11-12
---

A machine door that no longer registers as shut, or a carriage that runs past its stop, often traces back to a small switch with a spring-loaded button on top. Replacing that switch is easy, so is the switch the part that actually failed? **A spring plunger micro switch has two halves that fail in different ways: the plunger that takes the push, and the switch body that turns the push into a contact change.** The checks below follow that split, from the plunger, through the snap mechanism, to the contacts.

## Quick answer

A spring plunger micro switch fails when its plunger sticks or gets pushed sideways, when it's pressed too far or too little, or when its contacts weld (melt and stick together), wear or get coated. Omron's FAQ on basic switch failures splits the causes into electrical ones, such as welding, and mechanical ones, such as external damage. A continuity test, plunger released and then pressed, shows which group you're in.

## What a spring plunger adds to a micro switch

A micro switch, also called a snap-action switch, flips its contacts with a snap once its actuator, the part the machine presses, travels a set distance. The plain version has a pin plunger: a short rod that pushes straight on the internal spring. A spring plunger puts a second spring inside the plunger itself, so the plunger can keep moving after the contacts have switched.

Omron's datasheet for its A series shows what that buys. The pin plunger A-20G-B and the short spring plunger A-20GD-B list the same operating force (OF), the push needed to switch it, of 3.92 to 6.13 N, and the same pretravel (PT), 1.3 mm max. Pretravel is the distance the plunger moves before the contacts switch. The difference is in overtravel (OT), the extra distance the plunger can safely move after switching:

| Omron A series model | Actuator | Pretravel (PT) max. | Overtravel (OT) min. |
|---|---|---|---|
| A-20G-B | Pin plunger | 1.3 mm | 0.25 mm |
| A-20GD-B | Short spring plunger | 1.3 mm | 3 mm |

Going by those two rows, the spring plunger lets the machine part that presses the switch overshoot by about twelve times as much. A margin that large suits a cam (a shaped rotating part), door or slide that doesn't stop at a precise spot. The same design tells you where to look when the switch stops working: the extra spring is one more moving part, and the overtravel it allows still has a limit.

## Before you test: power off and identify the terminals

Omron's SS series datasheet tells installers to turn off the power supply before mounting or removing the switch, wiring it, or doing maintenance, because working live can cause electric shock or burns. On anything plugged into a wall outlet, unplug it; on battery equipment, take the battery out. Don't bypass the switch to keep a machine running while you troubleshoot: if it sits on a door, guard or limit, it's there to stop something moving.

Most of these switches have three terminals, marked common (COM), normally closed (NC) and normally open (NO). Electronic Design's explainer on snap-action switches describes the at-rest state: with the plunger fully released, the common contact rests against the NC contact, so COM to NC conducts. Pressing past the operating point, where the switch clicks, moves the common contact over to NO. "Normally" means "with nothing pressing the plunger," which matters when the switch is installed and the machine holds it pressed. Our guide to [NO and NC terminals on a micro switch](/guides/no-nc-micro-switch/) covers the markings in more detail.

## Step 1: Check the plunger and what presses it

Start with the switch still mounted and the power off. Move the machine part (door, cam, slide) by hand and watch the plunger.

- **Does the part reach the plunger at all?** A bracket that has shifted or a cam that has worn can stop short. Crouzet's technical notes on its micro switches say the actuating device must push the plunger through at least 0.5 times the rated overtravel, and must never stop at the operating point. If the part barely touches the plunger, the switch can't switch reliably.
- **Is the push straight?** The same Crouzet notes say a plunger should be pressed along its axis, and that most of its switches accept a side approach only up to 45° off the plunger's axis. A part that wipes across the plunger at a steep angle loads it sideways, which can bind the plunger or crack the housing over time.
- **Does the plunger come back?** Press it with a fingertip and let go. It should return fully and on its own. A plunger that returns slowly or stops partway points to dirt, grease or a damaged plunger spring. Omron's A series precautions warn against mounting the switch where cutting debris and dust can build up on the actuator. Our article on [why a micro switch plunger sticks](/guides/micro-switch-plunger-sticking-explained/) goes through those causes.

## Step 2: Check how far the plunger is pushed

Too little travel and too much travel both cause failures, in opposite directions.

Omron's FAQ on how far to push a basic switch warns that if the operating part stops near the operating position or the release position, the switch can chatter or bounce. Crouzet explains why: near those points the contact force drops and the contact resistance can rise sharply. The symptom is an intermittent signal that comes and goes with vibration or temperature.

Pushing too far does the opposite kind of damage. The same Omron FAQ sets the pushing distance at 60% to 90% of the rated overtravel, and says that beyond 90% the actuator or switch may be damaged. Omron's A series datasheet gives a slightly different window, 70% to 100% of rated OT, and says travel must never exceed the permissible OT position. Either way, a machine that drives the plunger to the bottom of its stroke on every cycle is wearing the switch out. A spring plunger gives you more room, but a plunger pressed flat against the housing has run out of that room.

📌 **On the extra overtravel:** *The spring plunger's larger OT is a margin for an imprecise machine, so it's worth checking whether the mounting or the cam changed before a failure, since that's often what used the margin up.*

## Step 3: Test the contacts with a multimeter

With the power off and the switch's wires disconnected, set a multimeter to continuity or the lowest resistance range. Crouzet defines contact resistance as the resistance measured across the terminals when the contacts are closed. For its micro switches, Crouzet puts it generally under 20 mΩ with the plunger at rest or fully pressed, so a working contact reads as a near-zero short on a hobby meter.

| Plunger | COM to NC | COM to NO |
|---|---|---|
| Released | Continuity | Open |
| Pressed past the click | Open | Continuity |

What the readings point to:

- **No continuity on either pair in either position:** the contacts aren't touching at all, from a broken internal spring, a contact coated with film, or a cracked housing.
- **Continuity that stays on one pair whatever you do:** the contacts may be welded shut, or the mechanism isn't moving. If the plunger moves freely but nothing changes, it's the inside of the switch.
- **A reading that flickers as you press slowly:** check the travel (Step 2) first, then suspect worn or dirty contacts.

Our step-by-step guide on [how to test a spring plunger micro switch](/guides/how-to-test-a-spring-plunger-micro-switch/) shows probe placement on common terminal layouts.

## Why the contacts fail

If the plunger and travel check out but the contact test fails, the cause is usually electrical or environmental.

- **Welding from high inrush.** Crouzet's notes say motors and electromagnets can draw an inrush, a surge at the moment of switch-on, of up to 6 times the rated current when switched on, and lamps and capacitive loads up to 15 times, which greatly increases the risk of welding the contacts. Omron's A series datasheet adds that switching extremely slowly can also lead to contact failure or welding. Our [contact welding troubleshooting guide](/guides/micro-switch-contact-welding-troubleshooting/) covers this case.
- **Film on the contacts from too little current.** Omron's FAQ on the minimum applicable load says that below that load, the contact surface is more open to a chemical coating from the surrounding air, which can cause contact failure. A switch built for a motor circuit and reused on a small signal line can fail this way.
- **Contamination.** Crouzet tells users to keep silicone, grease, oil and cyanoacrylate glue away from its micro switches because they affect contact resistance, and says grease and oil must never get inside. Spraying lubricant at a sticky plunger can turn a mechanical problem into a contact problem.
- **Vibration.** Omron's A series precautions say continuous vibration or shock can cause contact failure from abrasion powder and shorten the switch's life.

## When to replace the switch, when to fix the machine, and what to match

Replace the switch when the plunger moves correctly, the travel is in range, and the contact test still fails. Fix the machine first when the plunger sticks, the push comes in at an angle, or the stroke stops short or bottoms out, because a new switch in the same spot will fail the same way. Match the actuator type, the terminal layout, the mounting holes and the electrical rating of the old part. Omron's A series datasheet, for example, lists the pin plunger and spring plunger versions as separate model numbers with different overtravel.

## FAQ

### What are the symptoms of a bad switch?

A bad spring plunger micro switch shows up as a machine that ignores a door, guard or limit, as a signal that flickers on and off, or as a switch that stays on after the plunger is released. A plunger that sticks down or returns slowly is a mechanical symptom. A continuity test that doesn't change between released and pressed confirms the switch body itself has failed.

### How long do micro switches last?

It depends on the series and the load. Omron's A series datasheet lists 1,000,000 operations minimum for mechanical durability, measured without load, and 500,000 operations minimum for electrical durability at its rated load. A switch on a motor or lamp circuit, or one that's pushed past its overtravel every cycle, will usually wear out sooner than its datasheet figure.

## Where to look next

If the plunger and contacts both test fine, the fault is in the wiring or the controller that reads the switch, and our guide to [diagnosing an intermittent micro switch](/guides/intermittent-micro-switch-diagnosis/) covers that side. If the switch did fail, measure the travel your machine gives the plunger before fitting the new one, and check that it carries the plunger past the click and into the overtravel window on the new switch's datasheet.


## Related guides

- [espresso machine drip tray micro switch troubleshooting](/guides/espresso-machine-drip-tray-micro-switch-troubleshooting/)
- [micro switch condensation troubleshooting](/guides/micro-switch-condensation-troubleshooting/)
- [how to test a extrusion machine home position micro switch](/guides/how-to-test-a-extrusion-machine-home-position-micro-switch/)
- [cash drawer position micro switch intermittent operation](/guides/cash-drawer-position-micro-switch-intermittent-operation/)

## Sources

- Omron, General-purpose Basic Switch A datasheet (CSM_A_DS_E_3_4): operating characteristics of A-20G-B and A-20GD-B, durability, safety precautions
- Omron, SS Miniature Basic Switch (Non-Sealed) catalog pages (B053-E2-11D), hosted by Electrokit: power-off precaution
- Omron FAQ FAQE20047, "What may have caused a basic switch failure?" (reposted on DigiKey TechForum)
- Omron FAQ FAQE20046, "Please advise the appropriate amount of pushing for a basic switch" (reposted on DigiKey TechForum)
- Omron FAQ FAQE20025, "What problems may occur if the set current is below the minimum applicable load for a basic switch?" (reposted on DigiKey TechForum)
- Crouzet, Microswitches: Basic Technical Concepts (12/2020)
- Electronic Design, "Snap-Action Switches Still Rule The Roost."
