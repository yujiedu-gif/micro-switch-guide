---
title: "How a Door Interlock Micro Switch Works: Primary, Secondary and Monitor Switches"
description: "A door interlock micro switch is pressed only when a door is fully shut. See how microwave primary, secondary and monitor switches and the fuse work together."
date: 2026-10-13 11:27:16 +0800
category: Applications
tags:
  - door interlock micro switch
  - micro switches
  - Applications
author: editorial_team
seo_title: "How a Door Interlock Micro Switch Works"
last_updated: 2026-11-12
---

Open a microwave oven while it's running and the cooking stops the moment the latch lets go, before anyone touches the Stop button. One widely repeated explanation says a spare switch then trips your home's circuit breaker if the main door switches ever fail. **Microwave service manuals give that job to a fuse inside the oven, and the spare switch, called the monitor switch, is wired to blow it on purpose.** The latch, the contacts inside each door switch and the fuse are taken below in the order the door moves them, followed by the same contact logic in washer door locks and machine guards.

## Quick answer

A door interlock micro switch is a small snap-action switch that the door or its latch presses only when the door is fully shut. ZING EAR's product page for its [ZINGEAR G5T16-E1Z200](https://www.zingear-switch.com/zingear-group-g5t16-e1z200-home-appliance-micro-switch-micro-switch-supplier.html){: rel="nofollow noopener noreferrer" }, rated 16A at 250VAC, lists safety interlock of kitchen appliance doors among its uses. In a microwave oven, several of these door switches work together so that power reaches the cooking circuit only while the door stays closed.

## What happens inside the switch when the door presses it

Inside the housing, a spring mechanism carries one moving contact between two fixed contacts. The three terminals are marked common (COM), normally closed (NC) and normally open (NO). Daniel Herzog's article on snap-action switches in Electronic Design describes the resting state. With the plunger, the small button the door or latch pushes, in its free position, "the NC circuit of the switch can carry current," and the common terminal is insulated from the NO terminal. "Normally" therefore means the state with nothing pressing the actuator.

Press the plunger far enough and it reaches the operating point, the spot in its travel where the spring flips over and the common contact snaps across to the NO contact. The same article notes that the common contact "cannot stop partway" between NC and NO. A switch maker's explainer on how micro switches work adds that the snap-action mechanism gives "instantaneous switching regardless of the actuation speed." A door that someone pushes shut slowly still moves the contact in one quick jump.

In a door interlock, a shut door is the pressed state. A circuit wired through COM and NO is complete only while the door holds the plunger down. A circuit wired through COM and NC is complete only while the door is open. The monitor switch further down depends on that reversal, so the difference between NO and NC contacts is worth having straight before reading a microwave schematic.

## Why a microwave oven needs more than one door switch

US federal rules for microwave ovens, 21 CFR 1030.10, define a safety interlock as a device or system of devices meant "to prevent generation of microwave energy when access to the cavity is possible." The same section says that "Microwave ovens shall have a minimum of two operative safety interlocks." Under that section, at least one of them must not be operable by any part of the body or by a straight object 10 cm long. A finger or a stick poked at the door frame can't switch it.

The rule then closes the obvious gap. Under paragraph (c)(2)(ii), one failed mechanical or electrical part "shall not cause all safety interlocks to be inoperative." Paragraph (c)(2)(v) names the two required interlocks primary and secondary and requires the service instructions to say which is which. Paragraph (c)(2)(vi) adds a monitor for one or both interlocks, which must make the oven inoperable until it's repaired if an interlock fails.

The Sanyo EM-FL50N service manual names the failure this design has in mind: primary and secondary switches that "stick closed." A switch whose contacts stay closed keeps its circuit complete after the door opens, so power flows as if the door were still shut. If both interlocks stick, nothing in the interlock path breaks the circuit, and the monitor exists for that case.

## How the primary, secondary and monitor switches share the work

The Sanyo EM-FL50N manual describes the sequence in one line: "By closing the door, the primary and secondary interlock switches close and monitor switch opens." With both interlocks closed, the same manual says, household supply voltage flows through that model's 10 amp fuse toward the magnetron circuit, the part that generates the microwaves.

| Switch (Sanyo EM-FL50N service manual) | Door closed | Door open | What it does |
|---|---|---|---|
| Primary interlock | Closed | Open | Breaks power to the cooking circuit when the door opens |
| Secondary interlock | Closed | Open | Breaks the same circuit independently of the primary |
| Monitor | Open | Closed | Shorts the supply if an interlock is still closed with the door open, which blows the 10 amp fuse |

The monitor is the switch that runs backwards. The Sanyo manual calls it the "normally closed safety switch." If the primary and secondary switches stick closed and the door opens, the manual explains, "the circuit would be shorted through the normally closed safety switch." With the door open, the monitor's contacts are closed, so a stuck interlock path plus a closed monitor connects the supply straight across itself. The surge blows the fuse, and the oven goes dead. A dead oven is the intended result, and the household breaker isn't part of the sequence the manual describes.

Appliance standards test for the same behavior. Australia's Electrical Equipment Safety System (EESS) covers it in bulletin 24-071 (2024), on clause 22.106 of AS/NZS 60335.2.25, the microwave oven safety standard used there. The bulletin says the clause requires the supervision device of each door interlock, the part the US rule calls a monitor, to make the oven inoperable if the interlock fails. Fuses are the usual tool, since the requirement "is commonly achieved using fuses," the bulletin adds, and it quotes the test wording: "The internal fuse shall rupture each time."

Not every interlock position is a micro switch. The DCS MO-24SS technical service manual calls its primary interlock a relay, an electrically operated switch, and pairs it with a secondary interlock switch and a monitor switch. That manual also packages the monitor switch with a 20 ampere fuse as one assembly.

## The same contact logic in other doors

### Washer door locks

LG's online training manual for its front-load washer describes a door lock assembly, driven by a heated bimetal and a solenoid, that "locks the door during the wash cycle." The board learns the door is locked through a contact: "The lock is detected by the main board when terminals 4 and 5 are closed." As in the microwave, a closed contact between those terminals is how the control learns the door is in its safe position.

### Machine guards

Safety switches on machine guards are judged against a stricter idea called positive opening. One maker's general technical data for limit switches defines it as an actuator that "ensures full contact opening" of the normally closed contact. For that part of the travel, the same document allows "no resilient member (e.g. springs)" between the moving contacts and the point where force is applied. Electronic Design's description of snap action relies on "a plunger and spring," so a standard micro switch has the very spring that definition excludes.

The document also notes that positive opening "does not deal with N.O. contacts," meaning normally open ones. A guard circuit built this way runs through a contact that the opening guard forces apart. The function of a safety micro switch covers where specially rated parts come in.

## Checking a door interlock switch without defeating it

📌 **On safety:** *Unplug the appliance before opening any panel. A microwave oven's high-voltage capacitor is the part its service manuals tell technicians to discharge before testing, so if you aren't trained to do that, leave the work to a qualified appliance technician.*

The DCS MO-24SS manual starts its interlock tests by having you disconnect the power supply cord before removing the outer case. Its next step reads "Discharge high voltage capacitor," which drains the charge the capacitor can hold after the cord is pulled. Never jumper, tape down or bridge a door switch to see whether the oven runs. Federal rules for microwave ovens require that service adjustments or procedures not leave the interlocks inoperative. A bypassed interlock removes the protection the rest of the circuit was built around.

The Sanyo EM-FL50N manual checks the monitor switch with an ohmmeter, on an oven that's unplugged and discharged. "As the door is opened, your meter should show a short," the manual says, and with the door closed it should show an open circuit. The primary and secondary switches should read the opposite way. A step-by-step continuity test for a microwave door interlock micro switch walks through the meter settings, and the general method for testing a micro switch with a multimeter applies to any door switch.

A blown fuse is a symptom, and the switches are the cause to look for. The DCS manual warns, "BEFORE REPLACING A BLOWN MONITOR FUSE, TEST THE PRIMARY INTERLOCK." If improper switch operation blew the fuse, the same manual has the monitor fuse and monitor switch replaced together, "even if the monitor switch operates normally."

## FAQ

**What is the purpose of a micro switch?**
A micro switch turns a small mechanical movement into a definite contact change. In a door interlock, that movement is the door or latch reaching the fully shut position. One basic switch catalog lists both appliance door lights and door interlocks as applications for its switch series.

**Can you bypass a microwave door switch?**
No. US federal rules (21 CFR 1030.10) require at least two working interlocks plus a monitor, and require that service work not leave the interlocks inoperative. If a door switch has failed, the service manual for that model names the part and test procedure for replacing it.

**How does a micro switch work?**
A spring mechanism holds a moving contact against the NC contact until the actuator is pressed to the operating point. Past that point, the contact snaps across to the NO contact, and the switch maker's explainer cited above describes this switching as independent of how fast the actuator moves. Releasing the actuator lets the spring snap the contact back.

## What to look at before replacing a door switch

Start with the service manual or wiring diagram for your exact model, since it names which switch is primary, which is secondary and which is the monitor. Match the replacement's contact form and electrical rating to the part it replaces, because a normally open switch fitted in the monitor position reverses the logic the fuse depends on. If the fuse blew, test every switch in the interlock set before fitting a new fuse.

Door interlock switches come from appliance switch makers, and some describe where their parts are used. [ZING EAR](https://www.zingear-switch.com/){: rel="nofollow noopener noreferrer" } lists microwave ovens, range hoods and coffee machines among the kitchen appliances its home appliance micro switches cover. Whichever maker built the original, the service manual still names the position each switch fills, and a replacement has to match that position's contact form.

## Sources

- US Code of Federal Regulations, 21 CFR 1030.10, Microwave ovens (Legal Information Institute)
- Sanyo EM-FL50N service manual, Electrical Operation and Door & Interlock Adjustments (ManualsLib copy)
- DCS MO-24SS technical service manual, Component Test and Blown Monitor Fuse Test (ManualsLib copy)
- EESS Information Bulletin 24-071, Microwave oven clause 22.106 (AS/NZS 60335.2.25), 2024
- Daniel Herzog, "Snap-Action Switches Still Rule The Roost," Electronic Design, 2012
- LG Online Training Manual, Door Lock (front-load washer, hosted by Reliable Parts)
- ZING EAR, ZINGEAR G5T16-E1Z200 product page: https://www.zingear-switch.com/zingear-group-g5t16-e1z200-home-appliance-micro-switch-micro-switch-supplier.html
- ZING EAR, Home Appliance Micro Switch product line page: https://www.zingear-switch.com/home-appliance-micro-switch
