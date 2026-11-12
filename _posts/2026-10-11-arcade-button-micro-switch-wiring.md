---
title: "Arcade Button Micro Switch Wiring: Which Two Terminals to Use and How to Share the Ground"
description: "Arcade button micro switch wiring uses two terminals: input wire on NO, ground on COM, NC left empty. Steps, a quick test and the faults a wrong tab causes."
date: 2026-10-11 18:01:49 +0800
category: Applications
tags:
  - arcade button micro switch wiring
  - micro switches
  - Applications
author: editorial_team
seo_title: "Arcade Button Micro Switch Wiring: COM, NO and Ground"
last_updated: 2026-11-12
---

An arcade button's micro switch has three metal tabs printed COM, NO and NC, yet the input board it connects to offers one terminal per button plus a ground. Which two tabs take the wires, and does every button need its own ground wire back to the board? **The button's own wire goes on NO, the ground goes on COM, and one ground wire can hop from COM to COM across every button before it reaches the board.** Identifying the tabs, the wiring steps, a test with the board connected and the faults a wrong tab causes follow in that order.

## Quick answer

Arcade button micro switch wiring uses two of three terminals: the input wire goes on normally open (NO), the ground wire on common (COM). Ultimarc's installation notes for its I-PAC input boards say to leave the normally closed (NC) tab empty and to daisy-chain the ground side of every switch, one wire running from switch to switch, to a single GND terminal.

## Before you start: power and connectors

If the button sits in a full cabinet with a PC, monitor or power supply inside, switch the cabinet off at the wall and unplug it before you reach into the control panel. A stand-alone stick that runs from a USB cable only needs the cable unplugged. Ultimarc's page for the I-PAC 2 says the board plugs into a USB port and needs no separate power, so the button circuit itself is low voltage.

Check the connector size before you buy wire. Push-on connectors have to match the width of the switch's tabs, the flat metal blades the wires slide onto. Ultimarc lists the ready-made wiring harness for its Mini-PAC board with 4.8 mm switch connectors, or with both 4.8 mm and 2.8 mm connectors for its Goldleaf button panels, so both widths turn up on arcade switches. Wikipedia's FASTON terminal article lists those widths as the 187 and 110 families, named for blade widths of 0.187 in and 0.110 in.

## Identify COM, NO and NC on the switch

Most switches print the three labels on the case next to the tabs. Each label tells you what the tab connects to inside:

- **COM (common)** connects to the moving contact, the metal piece that the spring flips when you press.
- **NO (normally open)** stays apart from COM until the button is pressed.
- **NC (normally closed)** touches COM until the button is pressed.

"Normally" means at rest, with nothing pressing the switch. Electronic Design's article on snap-action switches describes the press from that resting state: at the operating point, the common contact accelerates away from the NC contact and comes to rest against the NO contact. The explainer on NO and NC micro switch contacts covers the two states in more depth.

If the labels are worn off, a multimeter on its continuity setting sorts the tabs out with the power off. On that setting, the meter beeps when its two probes touch metal that's connected. Touch the probes to two tabs at a time. The pair that beeps at rest and goes quiet when you press is COM and NC. The pair that stays quiet at rest and beeps when you press is COM and NO. The tab that appears in both pairs is COM.

## Wire the button step by step

1. **Run the input wire to NO.** Take the wire from the board terminal assigned to that button and push its connector fully onto the NO tab. Ultimarc's I-PAC 2 page says some switches have three connections and that only the ones marked NO and COM get used.
2. **Run the ground to COM.** Push a ground wire onto the COM tab.
3. **Chain the ground to the next button.** Run the same ground wire on to the COM tab of the next button, and the next, then end the chain on a GND terminal of the board. Ultimarc's notes call this daisy-chaining the other side of all switches together.
4. **Leave NC empty.** Ultimarc's notes say nothing should go on the NC tag.
5. **Tug each connector gently.** A connector that slides off with a light pull isn't fully seated or doesn't match the tab width.

The shared ground is standard practice in arcade cabinets. Ultimarc's I-PAC 2 page states that most arcade cabinets have one side of all switches commoned, and that the board's button inputs are all referenced to ground, so no button needs its own separate ground run. On the Mini-PAC, which uses a supplied harness, Ultimarc ships the ground as its own daisy-chain harness that plugs into the black wire of the main harness. The guide to why one COM wire can serve every button explains the shared ground in more detail.

## Test the button with the board connected

Ultimarc's basic test for the I-PAC uses a text program such as Notepad. Plug the board in, open Notepad and press the buttons; each press should type a character. Ultimarc suggests trying the player 2 buttons first, because some player 1 inputs are mapped to keys such as ALT that don't print anything.

If a button types nothing, split the fault in two. Ultimarc's notes describe touching one end of a short wire to GND and the other end to an input terminal: a character should appear. The short wire does the switch's job, so a character from that test means the board and its input are fine, so the problem sits in the switch or the wires to it. With the board unplugged, the continuity test from the identification step tells you whether the switch itself still closes between COM and NO when pressed.

📌 **On the self-test light:** *Ultimarc says the LED on an I-PAC stays on in normal use, and flashes a number of times then stays off when the board detects a failure at power-up.*

## Faults that come from the wrong tab or a loose wire

| What you see | Likely cause | What to check |
|---|---|---|
| Buttons read as held down, joystick directions jump, keys stick | Input wires on NC instead of NO, which Ultimarc names as a very common cause | Move each input wire from NC to NO |
| One button does nothing | Loose connector on NO or COM, or a failed switch | Reseat both connectors, then run the continuity test |
| Every button past a certain point does nothing | Break in the ground chain, so every switch after the break loses its ground | Follow the chain from the last working button |
| Connector slides off or won't go on | Connector width doesn't match the tab | Compare the tab with 4.8 mm and 2.8 mm connectors |

The third row follows from how the chain works: ground reaches each switch through the switch before it, so one broken link cuts off every switch further along. Ultimarc's own notes put a related warning in software terms: when inputs sit on NC, the board sees many keys held at once, which is why shift functions stop working.

## FAQ

### How to wire an arcade button micro switch with 2 wires?

Put one wire on the NO tab and the other on the COM tab, and leave NC empty. The NO wire goes to the board's input for that button, and the COM wire goes to ground. Ultimarc's I-PAC notes describe exactly that pairing for every button and joystick switch.

### How to wire arcade buttons?

Wire each button's NO tab to its own input on the board, then run a single ground wire from COM to COM across all the buttons and end it on the board's GND terminal. Ultimarc's I-PAC 2 page notes that most arcade cabinets already have one side of all switches commoned this way.

### How many ohms should a switch have?

Measured across COM and NO with the button held, a closed switch should read close to zero ohms on a multimeter; with the button released, the meter should show an open circuit. For scale, Omron's datasheet for its A-20G basic switch lists contact resistance, the resistance across the closed contacts, of 15 mΩ maximum when new, far below what a hobby meter can show. A reading of several ohms across closed contacts points to dirty or worn contacts or a poor connector.

## After the buttons work

Joystick switches follow the same rule: input on NO, ground on COM, NC empty, with the joystick's switches joining the same ground chain. The arcade joystick micro switch wiring guide covers terminal checks for the direction switches, and the arcade micro switch explainer covers what the switch under each button is.

Switch makers build parts with this use in mind. [ZING EAR](https://www.zingear-switch.com/){:rel="nofollow"} lists game control sticks among the markets on its home page, and its G6 troubleshooting article assigns the ZINGEAR G605-150S06A to gaming joysticks and e-sports peripherals. The COM, NO and NC rule above applies to whichever switch you fit, so read its terminal markings before you crimp the first wire.

## Sources

- Ultimarc, I-PAC 2 product page, installation and testing notes
- Electronic Design, Snap-Action Switches Still Rule The Roost
- Omron, General-purpose Basic Switch A (A-20G) datasheet (third-party mirror)
- Wikipedia, FASTON terminal
- ZING EAR, home page (application markets list): https://www.zingear-switch.com/
- ZING EAR blog, Causes and Troubleshooting Methods for G6 Micro Switch Failures: https://www.zingear-switch.com/causes-and-troubleshooting-methods-for-g6-micro-switch-failures.html
