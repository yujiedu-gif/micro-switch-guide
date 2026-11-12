---
title: "Bus Door Position Micro Switch Intermittent Operation: How to Find Where the Signal Drops Out"
description: "A bus door position micro switch that works only some of the time usually loses engagement, contact or wiring as the door cycles. How to narrow it down safely."
date: 2026-10-13 11:27:16 +0800
category: Troubleshooting
tags:
  - bus door position micro switch intermittent operation
  - micro switches
  - Troubleshooting
author: editorial_team
seo_title: "Bus Door Position Micro Switch Intermittent Operation"
last_updated: 2026-11-12
---

A bus door motor that sometimes keeps running after the door has closed, or a rear door that looks shut while the brakes stay on, points to a switch that reads the door position only some of the time. The common first check is a multimeter across the switch while it is pressed by hand. **An intermittent door position signal is usually decided at the point where the door linkage presses the switch, so the useful test watches the switch while the door cycles on the bus.** The switch's job, the safety rules around it, the places a signal drops out and the order of checks are covered below.

## Quick answer

A bus door position micro switch is a small snap-action switch, pressed by the door mechanism, that tells the door motor and the bus's interlocks whether the door is fully open or fully closed. In IC Bus's service article on electric entrance doors, one micro switch marks each end of travel and cuts power to the door motor there.

The interlocks are the circuits that hold the brakes while a door is open. When that signal works only some of the time, the sources cited below point to four places to look. They are how firmly the door linkage engages the switch, a bent actuator lever, worn or filmed contacts inside the switch, or the wiring that flexes as the door moves.

## What the door position switch tells the bus

On a power-operated entrance door, the switch's first job is to stop the door motor. IC Bus's service knowledge article IK2200116, "Bus Door Adjustment procedure for Electric and Air" (revision 8, published through NHTSA's service bulletin database), applies to its BE, CE and RE bus models built from September 15, 2011. The article states that the closed micro switch "should disengage power to the motor as the door achieves the full closed position," and that the open micro switch does the same at full open.

The same article adds that "it is important that the motor is not running when door is in stopped positions," and lists "motor gets hot" among the symptoms of a door out of adjustment.

On many transit buses, the door state also feeds a brake and accelerator interlock. California's bus equipment rule, 13 CCR § 1267(e)(3), requires passenger doors not adjacent to the driver on the buses it classes as Type 1 (school buses excepted) to be interlocked so that "the brakes cannot be released nor the accelerator applied while the doors are open." Florida's rule for public-sector buses, Fla. Admin. Code 14-90.007(3)(c), requires Type I buses with a rear exit door to apply the brake when the driver opens that door and to keep it applied until the driver deactivates it "and the rear exit door returns to the closed position."

School bus emergency doors carry a federal warning requirement. FMVSS No. 217 (49 CFR 571.217), in S5.3.3.1, requires a continuous warning sound at the driver's seat and near the door whenever the emergency door's release mechanism isn't in the closed position and the ignition is on.

None of these rules names the type of sensor. Each one only works if something on the bus knows reliably whether the door is open or closed, and on doors like the IC Bus design, that something is a micro switch. When that switch drops out, the bus reads a closed door as open, or an open door as closed. An intermittent switch therefore shows up as a motor that runs on, an interlock that won't release, or a warning that sounds with the door shut.

## Safety before you work on a bus door switch

Bus doors and their interlocks protect passengers, so the checks below are diagnostic steps for a qualified technician working from the bus maker's service information:

- Secure the bus first. New Flyer's service instruction ITS60634 for a Masats entrance door, also published through NHTSA, begins with "Set park brake and chock wheels."
- Expect the door to move. Power-operated doors close with real force, and the IC Bus procedure switches between power-off and power-on steps for that reason.
- Don't bypass or jumper an interlock, meaning wire around the switch so the bus always reads the door as closed, to keep a bus in service. California's rule allows only a remote override "not accessible from the driver's seated position" that turns on an audible warning and a red "Warning--Interlock Deactivated" light, and Florida's rule says its override switch "shall not be located within reach of the seated driver."
- Don't bend the switch to make it work. The IC Bus article, which calls these door switches limit switches, warns that "a bent limit switch, even bending the switch blade as slightly as shown below, can cause other problems," and says the switches "should not be modified."

## Where an intermittent door signal comes from

An intermittent signal means the switch sometimes changes state and sometimes doesn't, or changes and then drops back. The sources below point to four places where that happens:

| Where | What goes wrong | Who describes it |
|---|---|---|
| Engagement between door linkage and switch | The door stops at the end of travel with the switch only partly pressed, so it trips on some cycles and not others | IC Bus IK2200116: switch position or tie-rods (the adjustable rods between the door actuator and the door) are adjusted "to gain good contact with switch," with illustrations of good and bad engagement |
| Actuator lever | A bent lever no longer reaches its operating point, or needs too much force | IC Bus IK2200116 (bent limit switches); Omron's basic switch FAQ calls lever deformation "a relatively common cause of switch failure" |
| Contacts inside the switch | Abrasion powder from vibration, or a sulfide film on silver contacts at very low current | Omron's A-20G basic switch datasheet, Safety Precautions |
| Wiring and connectors | Insulation wears where the harness flexes or rubs | Florida 14-90.007(3)(b) requires wiring be kept from moving parts and from "chafing or abrasion which may cause insulation to become worn" |

The door itself can also change where the linkage stops. The IC Bus article lists bent adjustment rods, poor link arm clearance and header box fit among the symptoms of a door out of adjustment, and each of those changes where the linkage ends up when the door stops.

## How to narrow it down, step by step

The order below goes from the checks that need no disassembly to the ones that do. Each step says what the result tells you.

1. **Identify the switch and the contact it uses.** A door may carry separate open and closed switches, as the IC Bus design does. On a three-terminal switch, the terminals are common (COM), normally open (NO) and normally closed (NC), where "normally" means with nothing pressing the actuator, the lever or plunger that the door mechanism pushes. The bus wiring diagram shows which pair is in the circuit. *What it tells you:* which state, pressed or released, the circuit expects at each end of travel.
2. **Watch the switch while the door cycles.** Because the open and closed switches cut motor power, IC Bus's procedure puts a test light on the motor, or uses a digital multimeter, to see whether power is cut at each stop. The article states that the "test light should only be ON as the door is in transition." *What it tells you:* a light that stays on, or flickers, at a stopped position means the switch didn't fully trip on that cycle.
3. **Check engagement at each stop.** IC Bus's illustrations show the gear arm meeting the switch roller at its center or slightly past it. *What it tells you:* a roller met at its edge points to door or tie-rod adjustment, and the fix is adjustment, made with the slots or tie-rods the manufacturer provides.
4. **Inspect the actuator lever.** Omron describes a deformed lever as one whose bending angle or backlash (play) has increased, often because something got caught in it. *What it tells you:* a bent lever explains a switch that trips on some cycles and misses on others, and the IC Bus article calls for replacement with its current service part.
5. **Flex the harness while watching the signal.** With the door stopped and the test light or meter still connected, move the bundle of wires where it passes the door hinge or the header above the door. *What it tells you:* a signal that changes as the wire moves points to wiring or a connector, which a switch replacement won't fix.
6. **Test the removed switch.** With the switch out of circuit, check COM to NC (closed at rest) and COM to NO (closed when pressed) several times, pressing slowly. *What it tells you:* a switch that fails here has an internal fault; a switch that passes points back to engagement, lever or wiring.

The guide to checking a micro switch for intermittent continuity covers the bench test in step 6 in more detail.

## Why a switch can pass a bench test and still drop out on the bus

A bench test checks the switch at rest and fully pressed, with steady hands and no vibration. On the bus, three conditions change that picture.

Vibration is the first. Omron's A-20G datasheet warns that "continuous vibration or shock may result in contact failure or faulty operation due to abrasion powder," the fine wear particles that rubbing parts shed. The same datasheet rates that switch for vibration of 10 to 55 Hz at 1.5 mm double amplitude, and it sets the malfunction limit for that test at "1 ms max." A brief loss of contact under vibration is exactly the fault that test looks for.

A switch that's only partly pressed sits closer to its operating point, the position where the contacts flip, so road vibration has less margin to work with. The explanation of mechanical vibration in micro switches goes further into that mechanism.

Contact film is the second. Omron's datasheet states that if silver contacts "are used with relatively low frequency for a long time or are used with microloads, the sulfide coating produced on the contact surface will not be broken down and contact faults will result," and it points to gold-contact microload switches for those circuits. A door switch that feeds a low-current controller input, rather than the motor itself, is the kind of circuit where that applies. The article on micro switch contact oxidation explains the film in more depth.

Adjustment is the third. The IC Bus article says door adjustment is part of the dealer's pre-delivery inspection and "a maintenance item in the Operators manual." A door that drifts out of adjustment changes where the linkage stops, so a switch that tested good on the bench can still be pressed too little once it's back on the door.

📌 **On replacing the switch:** *A new switch fitted to a door that's still out of adjustment can show the same intermittent fault, so the engagement check in the step-by-step list belongs before the replacement as well as after it.*

## Questions people ask about door sensors

### How can I disable the door ajar sensor?

On a bus, the door position switch feeds safety functions: in IC Bus's design it stops the door motor, and under California's and Florida's rules the door state holds the brakes on transit buses until the door closes. Disabling it removes that protection, and both state rules limit interlock overrides, the controls that release the interlock in an emergency, to places the seated driver can't reach. The fix for a sensor that reports a closed door as open is to find which of the causes above is at work, and the overview of door interlock micro switches explains how the same kind of switch guards doors on other machines.

## What to write down before replacing the switch

Record which stop the fault appears at (open or closed), whether the test light flickered or stayed on, how the gear arm meets the roller, and whether flexing the harness changed the signal. Notes on all four points separate an adjustment problem from a switch problem, and the bus maker's service information gives the adjustment values for that door.

Door sensing on public transport is one application switch makers report on. In an August 2026 news post, [ZING EAR](https://www.zingear-switch.com/){:rel="nofollow"} reported that its ZINGEAR G304 micro switch had entered the rail transit sector for sensing and control on high-speed train lifting doors. A train door isn't a bus door, so the bus maker's service information still sets the adjustment values for yours.

## Sources

- IC Bus (Navistar), service knowledge article IK2200116, "Bus Door Adjustment procedure for Electric and Air," revision 8, last modified March 12, 2019, as published by NHTSA. static.nhtsa.gov
- New Flyer, Instruction to Service ITS60634, "D45CRT Single Leaf Masats Entrance Door," February 10, 2023, as published by NHTSA. static.nhtsa.gov
- California Code of Regulations, Title 13, § 1267, Bus Entrances and Exits. law.cornell.edu
- Florida Administrative Code, Rule 14-90.007, Vehicle Equipment Standards and Procurement Criteria. law.cornell.edu
- 49 CFR 571.217, Federal Motor Vehicle Safety Standard No. 217, Bus emergency exits and window retention and release. ecfr.gov
- Omron, General-purpose Basic Switch A (A-20G) datasheet, CSM_A_DS_E_3_4, Safety Precautions. static.chipdip.ru
- Omron basic switch FAQ, "What may have caused a basic switch failure?", as reposted on DigiKey TechForum. forum.digikey.com
- ZING EAR news, "ZINGEAR G304 Micro Switch Debuts in Rail Transit Sector, Enabling Precise Sensing and Reliable Control for High-Speed Train Lifting Doors" (2026-08-18), listed on: https://www.zingear-switch.com/
