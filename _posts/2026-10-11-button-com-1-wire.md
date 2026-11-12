---
title: "Button COM 1 Wire: How One Common Wire Serves Every Button"
description: "Button COM 1 wire means a shared common: one wire links every button's COM terminal to ground while each button keeps its own signal wire. How and why it works."
date: 2026-10-11 18:01:49 +0800
category: Basics
tags:
  - button com 1 wire
  - micro switches
  - Basics
author: editorial_team
seo_title: "Button COM 1 Wire: One Common Wire for Every Button"
last_updated: 2026-11-12
---

A panel of arcade buttons wired to an input board usually shows a single wire looping from button to button, while each button also gets a wire of its own. Why can the common (COM) side get by with one wire when every button still needs its own? **The board tells buttons apart by their own input wires, so the side every button shares only has to reach ground once, and one wire chained through all the COM terminals does that.** The switch's terminals, why the shared wire works, how to run it, when a button needs two wires, and other meanings of "1 wire" follow in that order.

## Quick answer

Button COM 1 wire describes a shared common: one wire links every button's COM terminal to ground, while each button keeps its own signal wire on its normally open (NO) terminal. Ultimarc, which makes arcade input boards, tells builders to daisy-chain one side of all switches, running a single wire from switch to switch, and connect that chain to a ground (GND) terminal on the board.

## What COM means on a button's switch

The micro switch under an arcade button has up to three terminals:

- **COM** connects to the moving contact inside the switch.
- **NO** touches COM only while the button is pressed.
- **Normally closed (NC)** touches COM only while the button is at rest.

"Normally" means at rest, with nothing pressing the switch. Electronic Design's article on snap-action switches describes the press from that resting state: at the operating point, the common contact accelerates away from the NC contact and comes to rest against the NO contact. A button wired across COM and NO therefore closes its circuit only while it's held. The guide to a micro switch's three terminals shows how to find each terminal with a meter.

Ultimarc's notes for its I-PAC 2 board say that on switches with three connections, you only use the ones marked NO and COM, and nothing goes on the NC tag. That leaves the COM terminals of all the buttons as the side that can share one wire.

## Why one common wire can serve every button

The input board has one terminal per button, and each of those terminals watches for a connection to ground, the board's reference point for zero volts. Ultimarc's I-PAC 2 page states that all button inputs are referenced to ground, with no need to re-wire separate grounds to each button. The steps from a press to the key code, the keyboard or gamepad signal the computer receives, run like this:

1. Every button's COM terminal sits on the same chained wire, which ends at the board's GND terminal.
2. Pressing a button connects its COM to its NO inside the switch.
3. That button's NO wire, and only that one, now connects to ground through the chain.
4. The board sees which input terminal went to ground and sends the code assigned to it.

Because the board identifies the button at step 4 from the input terminal, the shared side carries no information about which button was pressed. One wire is enough for that shared side, while the input side still needs a wire per button. Ultimarc's page adds that most arcade cabinets already have one side of all switches commoned, meaning joined on one wire, this way.

## How to run the shared COM wire

1. **Start at the board's GND terminal** and run the wire to the COM tab of the nearest button.
2. **Continue to the next button's COM tab**, then the next, until every button and joystick switch is on the chain.
3. **Give each button its own wire from NO** to the input terminal you want that button to trigger.
4. **Leave NC empty**, as Ultimarc's notes instruct.

Some boards ship the shared wire ready-made. On the Mini-PAC, Ultimarc supplies the ground as a separate daisy-chain harness that plugs into the black wire of the main harness, then connects to every switch.

Some boards label their own terminals COM, 1, 2, 3 and so on, and the same pattern applies. The chained wire from the buttons' COM tabs goes to the board's COM or ground terminal, and button 1's NO wire goes to terminal 1. Check the board's own manual for which terminal is the common one before you connect anything.

A chained wire has one weak point. Ground reaches each button along the wire that passes the buttons before it, so a break in the chain cuts off every button further along while the earlier ones keep working. If a whole run of buttons dies at once, follow the chain from the last working button. The arcade button micro switch wiring guide covers testing and the other faults that show up after wiring.

## When each button needs two wires of its own

The shared common depends on a board that reads every input against ground. Ultimarc's I-PAC 2 page contrasts that with wiring arcade buttons into a hacked keyboard, where the buttons have to be wired across the keyboard's key switches. Ultimarc says that approach takes ages because two wires need to be run to each switch, and that you have to re-wire a cabinet whose switches already share one side.

The same page names a second cost of the keyboard approach: key ghosting, or phantom key presses, which Ultimarc attributes to the matrix nature of keyboard encoders. A board built with one input per button and a common ground avoids that, and Ultimarc lists the I-PAC as not using a matrix and having no ghost keys.

## If "1 wire" meant something else near a button

### The 1-Wire bus and iButton keys

1-Wire is a communication system for small chips, written with a capital W and a hyphen. Analog Devices' overview of 1-Wire technology describes it as a serial protocol, a way of sending data one bit at a time, using a single data line plus ground reference. The same overview says each device carries a unique, factory-programmed 64-bit identification number. The same overview describes the iButton, a 16 mm stainless steel can that holds such a chip and protects it in harsh environments. A 1-Wire device has nothing to do with a COM terminal on a push button; it's a data connection.

### The one-wire push button switch

A one-wire push button is a small momentary switch, one that stays on only while pressed, with a single wire coming out of it, sold for custom vehicle wiring. Retrocycle's listing for a mini chrome push button one-wire switch describes a 12 mm button with one wire, suggested for a turn signal, starter or horn. A switch needs two connections to complete a circuit, so with only one wire the second connection has to come through the switch's body or mounting. Check the product's instructions for how that body connection is made before you mount it.

## FAQ

### How to wire a single switch?

For one arcade button, put the input wire from the board on the switch's NO terminal and a ground wire on COM, and leave NC empty. With more buttons, the ground wire carries on from COM to COM instead of running back to the board each time, as Ultimarc's I-PAC notes describe.

### How to wire up a micro switch?

Identify COM, NO and NC from the markings on the case or with a meter's continuity setting. Then pick the pair that matches the job: COM and NO for a circuit that closes while pressed, COM and NC for one that opens while pressed. The explainer on NO and NC micro switch contacts walks through both states.

## Before you connect the chain

Check two things on the switch first: that its terminals are marked COM, NO and NC, and that the connectors on your wire fit the width of its tabs. With those confirmed, the shared COM wire and one input wire per button are all the wiring a panel of buttons needs.

Switches for buttons and sticks are a catalog item in their own right. [ZING EAR](https://www.zingear-switch.com/){:rel="nofollow"} lists game control sticks among the markets on its home page, and its G6 troubleshooting article assigns the ZINGEAR G605-150S06A to gaming joysticks and e-sports peripherals. As with any switch, confirm its terminal markings before you join it to the shared COM wire.

## Sources

- Ultimarc, I-PAC 2 product page, installation notes and comparison with keyboard hacks
- Electronic Design, Snap-Action Switches Still Rule The Roost
- Analog Devices, Overview of 1-Wire Technology and Its Use (2008)
- Retrocycle, Mini Chrome Push Button One-Wire Switch listing
- ZING EAR, home page (application markets list): https://www.zingear-switch.com/
- ZING EAR blog, Causes and Troubleshooting Methods for G6 Micro Switch Failures: https://www.zingear-switch.com/causes-and-troubleshooting-methods-for-g6-micro-switch-failures.html
