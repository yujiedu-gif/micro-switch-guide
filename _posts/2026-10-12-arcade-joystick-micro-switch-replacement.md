---
title: "Arcade Joystick Micro Switch Replacement: Find the Failed Switch, Match It and Swap It"
description: "Arcade joystick micro switch replacement: confirm which switch failed, tell clip-on switches from a switch board, match tabs and force, then swap and test."
date: 2026-10-12 16:49:35 +0800
category: Applications
tags:
  - arcade joystick micro switch replacement
  - micro switches
  - Applications
author: editorial_team
seo_title: "Arcade Joystick Micro Switch Replacement, Step by Step"
last_updated: 2026-11-12
---

One direction on an arcade joystick stops registering while the other directions still work, and the micro switch for that direction is the first suspect. Can that single switch be replaced on its own? **A joystick that holds each switch separately on push-on tabs lets you swap the one bad switch, while a joystick whose switches are soldered to a small board makes the board the part you replace.** Confirming the failed switch, telling the two constructions apart, matching a replacement, the swap itself and the final test follow in that order.

## Quick answer

Arcade joystick micro switch replacement starts by confirming which direction's switch has failed, then swapping that switch or the small circuit board that carries all four. A US arcade parts distributor's support page recommends replacing the entire board on one widely used Japanese-style joystick, because its switches are soldered on. Separate switches unplug from their wires one at a time.

## Before you start

Unplug the controller. In a full cabinet with a PC, monitor or power supply inside, switch the cabinet off at the wall and unplug it before you open the control panel. Take a photo of the wiring under the joystick before you pull anything off, so each wire can go back on the same tab.

## Confirm that the switch is the part that failed

A dead direction can come from the switch, the wire to it, or the input on the board, so test before you buy a part. An arcade input board maker's notes describe a test that skips the switch entirely. With a text program such as Notepad open, touch one end of a short wire to a GND terminal and the other end to an input terminal, and a character should appear. The short wire does the switch's job, so a character means the board input works and the fault sits in the switch or its wires.

Then test the switch itself with the controller unplugged. Set a multimeter to continuity, which beeps when the two probes touch connected metal, and probe the switch's common (COM) and normally open (NO) tabs, the metal blades printed with those labels. COM is wired to the contact that moves, and NO only touches it while the switch is pressed. The pair should stay silent at rest and beep when you press the switch's actuator, its small button or lever, by hand. A switch that never beeps, or beeps only some of the time, is the failed part. The micro switch continuity test guide covers the meter readings in more detail.

A third check needs no meter. Pull the two wires off the dead direction's switch and the two off a working direction's switch, then put each pair on the other switch. If the dead direction moves to the other direction in the game, the fault travelled with the switch, so the switch is bad. If the same direction stays dead, the fault sits in its wiring or its board input.

## Separate switches or a switch board: tell them apart

Turn the joystick over and look at the base. One electronics supplier's joystick datasheet, for example, lists four micro switches on its stick, one for each direction. What matters for replacement is how those four are held.

- **Separate switches:** each switch has its own metal tabs with wires pushed onto them. One switch comes off without touching the others.
- **Switch board:** all four switches sit on one small circuit board, and a single plug connects the board to the controller. The distributor's support page cited in the quick answer says that joystick's switches are soldered to the board, and that a five-pin harness, a plug-in cable with one wire per pin, connects it. The harness carries one shared ground wire plus one wire per direction.

Melting the solder to free a single switch is possible with the right tools, but the distributor's advice for that joystick is to replace the board in its entirety. The guide to soldering micro switches covers terminal types and soldering limits if you go that route.

## Match the replacement to the switch you remove

Read the markings on the old switch's case first, then check each point below against the new switch's datasheet. The datasheet for one miniature snap switch family, quoted in the table as the family datasheet, is a useful example of the options a single family offers.

| What to match | What the datasheets show | What goes wrong if it doesn't match |
|---|---|---|
| Tab width (the metal blades the wire connectors push onto) | The family datasheet lists 4.8 mm and 6.3 mm quick-connect tabs; the input board maker lists harness connectors in 4.8 mm and 2.8 mm | The existing connectors won't grip the new tabs |
| Contact form | The family datasheet offers single pole, single throw (SPST) with a normally open contact, SPST with a normally closed (NC) contact, and single pole, double throw (SPDT) | An SPST switch with only an NC contact has no NO contact, so the joystick input never closes on a press |
| Operating force (the press needed to flip the switch) | The family datasheet offers standard or light operating force, from 45 to 400 cN (centinewtons, roughly 46 to 408 grams of force) depending on the model | The new direction feels lighter or heavier than the other three |
| Body and actuator (the switch's button or lever) | The family datasheet lists a plain button actuator and a range of levers and rollers | The joystick shaft may miss the new switch or hold it pressed |

Contact form has more leeway than it looks. Arcade boards only use the COM and NO tabs, which the input board maker's notes state directly, so an SPDT switch and an SPST switch with a normally open contact both work in a joystick. The NC tab on an SPDT switch simply stays empty.

A replacement with a different force than the three switches you keep makes one direction feel different, so match the force figure on the old switch's datasheet where you can find it.

## Swap a separate switch

1. **Pull the connectors straight off the old switch's tabs.** Grip the connector, not the wire.
2. **Remove the switch from its mount.** Note which way it faced, so the new one points its actuator at the joystick shaft the same way.
3. **Fit the new switch in the same position and orientation.** Tighten any screw only until the switch stops moving.
4. **Push the connectors back on.** The input wire goes on NO and the ground wire on COM, as the input board maker's notes instruct for every joystick switch.
5. **Move the stick by hand toward the new switch** and listen for the click before you close up the controller.

## Swap a switch board

The distributor's support page describes the board swap on that Japanese-style joystick as removing the restrictor guide, unplugging the five-pin harness and switching out the board for a new one. The restrictor guide is the plastic gate around the shaft that limits the stick to four directions or lets it reach the four diagonals as well.

Before plugging the harness into the new board, check the wire order. An arcade parts shop's listing for the same joystick gives the order with the connector facing forward. Viewed from the top, it runs black for ground, then green for up, yellow for down, orange for left and red for right. A harness built for a different stick can use another order, so compare it with the board's markings.

## Test after the swap

Run the continuity test on the new switch with the controller unplugged: COM to NO should be silent at rest and beep when the stick pushes the switch. Then plug the controller in and check every direction, including the diagonals. A diagonal presses two neighboring switches at once, so it confirms the new switch works together with the switch beside it. For the input board in the earlier test, its maker suggests Notepad and the player 2 inputs, because some player 1 inputs are mapped to keys such as ALT that don't type a character.

📌 **On a direction that still fails:** *If the new switch tests good on the meter but the direction still does nothing, go back to the wire-swap check. A dead direction that stays put when the switches trade wires points to a loose connector, a break in the ground chain or the board input.*

## FAQ

### What are the symptoms of a bad micro switch?

In a joystick, a bad switch shows up as one direction that never registers, registers only some of the time, or stays on after the stick returns to center. A continuity check between COM and NO confirms it: the pair should be open at rest and closed when pressed, every time.

### How to wire up a micro switch?

For an arcade joystick, wire the direction's input to NO and the ground to COM, and leave NC empty. A USB encoder board's installation notes describe that pairing for every button and joystick switch, with the ground side of all switches chained to one GND terminal. The arcade joystick micro switch wiring guide covers the terminals in more detail.

## Keep the old switch until the new one is proven

Hold on to the removed switch until every direction tests clean in a game, since its markings are the quickest way to reorder the same part. The arcade micro switch explainer explains the snap mechanism inside the switch you just replaced.

If you are weighing replacement brands, [ZING EAR](https://www.zingear-switch.com/){: rel="nofollow noopener noreferrer" } lists game control sticks among the markets on its home page. That market listing does not establish which model fits your joystick. Compare the exact switch's contact arrangement, terminal width and operating force with the old switch before fitting it.

## Sources

- ZING EAR, home page (application markets list): https://www.zingear-switch.com/
