---
title: "Drawer Closed Position Micro Switch Replacement: How to Confirm the Fault, Match the Part and Set It Up"
description: "How to confirm a drawer closed position micro switch has failed, choose a replacement that suits the signal and terminal pair, and set it to read closed."
date: 2026-10-13 11:27:16 +0800
category: Troubleshooting
tags:
  - drawer closed position micro switch replacement
  - micro switches
  - Troubleshooting
author: editorial_team
seo_title: "Drawer Closed Position Micro Switch Replacement"
last_updated: 2026-11-12
---

A cash drawer that shows "open" on the register screen while it sits shut, or an appliance drawer that won't run because it thinks the drawer is out, usually points to the small switch behind the drawer. Swapping that switch is quick. **A new switch reports "closed" only if the drawer presses it far enough, its contacts suit the signal it carries, and its wires go back on the same pair of terminals.** The sections below cover the safety limits, the checks that confirm the old switch failed, and how to choose, fit and test the replacement.

## Quick answer

A drawer closed position micro switch is pressed by the drawer as it shuts and tells a controller whether the drawer is closed. To replace it, disconnect power, confirm the drawer presses the switch, test the old switch with a multimeter, then fit a matching part wired to the same terminal pair. Microwave drawers differ: their switches are safety interlocks, a job for qualified service.

## What the closed-position switch does

A micro switch, also called a snap-action switch, is a small switch that flips its contacts with a click once its button or lever is pushed a set distance. In a drawer, the drawer itself is the thing that pushes it.

US patent 8,224,701, for a detecting device for a cash drawer and point-of-sale system, shows a typical arrangement. The cash drawer housing holds an electromagnetic release and a micro switch, and a cable to the point-of-sale host carries the signals. In that design, the micro switch is open-circuit while the drawer is closed; when the drawer opens, the switch closes, the host's input reads a low logic level, and the host reports the drawer as open. Another drawer could be wired the other way round, which is why the terminal pair matters when you replace the switch.

The switch's job sets how much care the replacement needs:

- **Status switches** on cash drawers and similar equipment report a position to a controller over a low-voltage signal line, as in the patent above. A wrong reading there causes a nuisance rather than a hazard.
- **Safety interlocks** stop something dangerous when the drawer opens. A microwave drawer is a microwave oven, and US federal rules for microwave ovens (21 CFR 1030.10) require at least two safety interlocks plus a means of monitoring them, and say service procedures must not leave the interlocks inoperative. Replacing those switches is a job for qualified service using the manufacturer's procedure; our guide to the microwave door interlock continuity test explains how those switch sets are checked.

## Before you start: power and safety

Omron's SS series datasheet tells installers to turn off the power supply before mounting or removing a switch, wiring it, or doing maintenance, because working live can cause electric shock or burns. For a cash drawer, that means unplugging its cable from the register, terminal or receipt printer, since the patent above describes the drawer's electromagnetic release drawing its power over that cable. For a plug-in appliance, unplug it from the wall.

Don't tape the switch down, join its terminals with a wire, or bend its lever to make the equipment run while you wait for a part. On a status switch that hides real drawer openings; on an interlock it defeats the safety function the 21 CFR 1030.10 rules exist to protect.

## Step 1: Confirm the drawer is pressing the switch

A drawer that no longer closes far enough looks exactly like a failed switch. With the power off, find the switch at the back or side of the drawer opening. If you lift the drawer off its slides to see it, put the drawer back for this check.

- **Push the drawer fully shut by hand and watch the switch.** You should see the plunger or lever move and, in a quiet room, hear a click. If the drawer stops short because of a bent slide, a jammed item or debris, fix that first. Our article on drawer closed position micro switch actuator travel covers how far the drawer needs to push.
- **Check the lever.** Omron's FAQ on basic switch failures names a deformed actuator lever as a relatively common cause, and says a lever that sits at a larger angle or has more play than before has deformed.
- **Check the bracket.** A switch that has shifted on loose screws or a cracked bracket can sit out of reach of the drawer.

## Step 2: Test the old switch

Disconnect the switch's wires, photograph which terminals they came from, and set a multimeter to continuity. Most micro switches have three terminals: common (COM), normally closed (NC) and normally open (NO). Electronic Design's explainer on snap-action switches describes the at-rest state: with the plunger fully released, the common contact rests against the NC contact, so COM to NC conducts.

| Switch plunger or lever | COM to NC | COM to NO |
|---|---|---|
| Released (drawer out) | Continuity | Open |
| Pressed past the click (drawer shut) | Open | Continuity |

A switch that reads the same in both positions, or that flickers as you press it slowly, has failed. If it tests good and the drawer presses it fully, the fault is in the cable, the connector or the controller instead. Our guide to why a cash drawer position micro switch is not working follows that path on point-of-sale equipment.

## Step 3: Choose a replacement that matches

The manufacturer's part number is the surest match. When you're choosing a generic micro switch instead, compare it with the old one on each point below.

| Check | Why it matters |
|---|---|
| Size and mounting hole spacing | The new switch has to bolt into the same holes; our guide to micro switch mounting holes lists datasheet spacings by size. |
| Actuator type and lever length | A longer or shorter lever changes where the drawer trips the switch. |
| Terminal style | Quick-connect tabs, solder lugs and PCB pins aren't interchangeable without rewiring. |
| Contact type for small signals | A switch built for heavy loads may not reliably switch a logic-level signal, the few-volt on/off signal an electronic input reads. |

That last row is easy to miss on a status switch. Omron's VX datasheet warns that using a switch model meant for ordinary loads on a micro-load circuit may result in faulty contact. Omron's FAQ on the minimum applicable load explains why: below that load, the contact surface is more open to a chemical film from the surrounding air, which can cause contact failure. A cash drawer's status line, which the patent above describes as a logic-level input, falls on the small-signal side, so check the replacement's datasheet for a micro-load rating or a minimum applicable load low enough for it.

## Step 4: Fit, wire and adjust the new switch

1. **Mount it the same way round as the old one,** on a flat surface. Omron's SS datasheet warns that mounting on an uneven surface can deform the switch, causing faulty operation or a broken housing.
2. **Wire it to the same terminal pair.** If the old switch used COM and NO, the new one must too. Swapping to COM and NC reverses the signal, so a drawer that's shut would read as open. Our explainer on drawer closed position micro switch NO and NC terminals covers how to tell which pair your equipment uses.
3. **Set how far the drawer presses the switch.** Close the drawer and check that it presses the switch past the click with some movement to spare. Omron's FAQ on how far to push a basic switch warns that stopping near the operating point can cause chattering. The same FAQ sets the pushing distance at 60% to 90% of the switch's rated overtravel, the extra distance the plunger can safely move after it clicks. A slotted bracket, if your equipment has one, lets you slide the switch to get there.
4. **Mind the lever's weight.** Omron's VX datasheet says to mount a lever switch so the lever's weight doesn't rest on the switch, because its small reset force may not spring the lever back.

## Step 5: Test before you put the drawer back in service

With the power still off, check continuity across the pair you wired while you open and close the drawer: the reading should switch between continuity and open each time. Then reconnect power and confirm that the controller agrees: the register, display or appliance should show the drawer as closed when it's shut and open when it's out. Open and close it several times, slowly and firmly, since a switch that's only just pressed can flicker on a slow close.

## FAQ

### What is inside a micro switch?

A micro switch holds a plunger or lever, a spring mechanism and a set of contacts behind its three terminals. Electronic Design's explainer describes how it works: energy builds up in the spring as the plunger is pressed until the plunger can't hold it. The spring then releases, and within a few milliseconds the common contact leaves the NC contact and comes to rest against the NO contact.

### How to install a micro switch?

Disconnect power and mount the switch with the screws and washers its datasheet specifies. Wire it to the same terminal pair the equipment expects, and adjust it so the moving part presses it past the click without bottoming it out. Then test continuity in both positions before restoring power.

## When the new switch still reads wrong

Suppose a new switch tests good on the bench and the drawer still reads incorrectly. Check the terminal pair against your photo first, then the cable and connector, then whether the drawer still travels far enough to press the switch. Each of those can make a good switch report the wrong state.

Drawer closing detection is a listed use for appliance switches. [ZING EAR](https://www.zingear-switch.com/){:rel="nofollow"} names large-capacity disinfection cabinet drawer closing verification among the applications of its ZINGEAR G905-150F06W1, and disinfection cabinet drawer closing monitoring among those of its ZINGEAR G9105-150S00D1. Whichever switch you fit, match its terminal pair to your photo of the old wiring.

## Sources

- US Patent 8,224,701 B2, "Detecting device for a cash drawer and a point of sales system" (Google Patents)
- 21 CFR 1030.10, Microwave ovens (Legal Information Institute)
- Omron, SS Miniature Basic Switch (Non-Sealed) catalog pages (B053-E2-11D), hosted by Electrokit
- Omron, VX Miniature Basic Switch datasheet
- Omron FAQ FAQE20047, "What may have caused a basic switch failure?" (reposted on DigiKey TechForum)
- Omron FAQ FAQE20046, "Please advise the appropriate amount of pushing for a basic switch" (reposted on DigiKey TechForum)
- Omron FAQ FAQE20025, "What problems may occur if the set current is below the minimum applicable load for a basic switch?" (reposted on DigiKey TechForum)
- Electronic Design, "Snap-Action Switches Still Rule The Roost"
- [ZING EAR, ZINGEAR G905-150F06W1 product page](https://www.zingear-switch.com/g905-150f06w1-built-in-rolling-linked-status-sensing-control-component--switch--button-for-large-and-medium-kitchen--amp-bathroom-appliances.html){:rel="nofollow"}
- [ZING EAR, ZINGEAR G9105-150S00D1 product page](https://www.zingear-switch.com/zingear-g9105-150s00d1-waterproof-and-dustproof-micro-switch-micro-switch-manufacturer.html){:rel="nofollow"}
