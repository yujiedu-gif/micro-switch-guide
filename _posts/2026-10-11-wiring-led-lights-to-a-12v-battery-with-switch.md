---
title: "Wiring LED Lights to a 12V Battery With Switch and Fuse, Step by Step"
description: "Run battery positive through a fuse and a switch to the LED, then back to negative. Fuse placement, resistor sizing for bare LEDs and DC switch ratings."
date: 2026-10-11 18:01:49 +0800
category: Applications
tags:
  - wiring led lights to a 12v battery with switch
  - micro switches
  - Applications
author: editorial_team
seo_title: "Wiring LED Lights to a 12V Battery With Switch and Fuse"
last_updated: 2026-11-12
---

Connect a single LED from a hobby kit straight across a 12-volt battery and it can burn out in moments, yet a 12-volt LED strip hooked up the same way lights normally. **The strip survives because it carries its own current-limiting resistors, and a bare LED has nothing between it and the battery until you add one.** A working circuit runs from the battery's positive terminal through a fuse and a switch to the light, then back to the negative terminal, and each link in that loop gets a check below.

## Quick answer

To wire LED lights to a 12-volt battery with a switch, run the battery's positive terminal to a fuse and the fuse to the switch. Connect the switch to the LED's positive lead, and the LED's negative lead back to the battery's negative terminal. US Coast Guard wiring rules for boats ([33 CFR 183.455](https://www.law.cornell.edu/cfr/text/33/183.455){: rel="nofollow noopener noreferrer" }) require that fuse at the power source.

LED strips, bulbs and fixtures sold for 12-volt use already limit their own current. A bare LED does not, so it also needs a series resistor sized from its datasheet.

## Safety checks before the battery goes on

A battery has no off position of its own, so every wire attached to its positive terminal stays live until a fuse or a switch breaks the path. The US Coast Guard's electrical rules for boats with gasoline engines ([33 CFR 183.401](https://www.law.cornell.edu/cfr/text/33/183.401){: rel="nofollow noopener noreferrer" } sets that scope) require each ungrounded current-carrying conductor to be protected by a fuse or circuit breaker. In a battery circuit whose negative side is the ground, that conductor is the positive wire. Section 183.455 of the same rules places that fuse at the source of power, or within seven inches of it, measured along the wire, when the source itself is physically impractical.

The Coast Guard rules are written for boats, but the reasoning carries over to a van, a shed or a bench project. If the stretch of wire between the battery and the fuse rubs through and touches metal tied to the negative side, current runs straight back to the battery with nothing to stop it. So the fuse goes on first, next to the positive terminal.

In practice, build the whole circuit with the fuse pulled out of its holder, and push the fuse in only after every other connection is finished and checked. Keep metal tools away from the battery, because a wrench resting across both terminals gives the battery that same direct path, with no fuse in it.

## Check which kind of LED you have, and whether it needs a resistor

### 12-volt strips, bulbs and fixtures

Inspired LED, a US maker of LED strip, [describes its 12-volt strip](https://www.inspiredled.com/why-led-lighting/inspired-led-101-easy-guide-to-led-strip-part-1/){: rel="nofollow noopener noreferrer" } as a row of short, side-by-side paths, and in its words each path comprises three LEDs and a resistor. The same guide says the resistor serves to limit the flow of current along the strip. Each path is a complete unit, which is why that guide places the cut points every three LEDs.

A product built that way connects to the battery with nothing extra except the fuse and the switch, as long as its label says 12-volt DC. Note the power in watts from the same label too, because the wiring steps below use it.

### Bare LEDs from a kit or a salvaged board

A bare LED has no resistor inside, and [ROHM's LED manual](https://fscdn.rohm.com/en/products/databook/applinote/opto/led/led_manual-e.pdf){: rel="nofollow noopener noreferrer" } describes how sharply its current responds to voltage. For the sample LED charted in that manual, current rises from 1 mA (a thousandth of an amp) at about 1.8 V to 20 mA at about 2.2 V. The same manual's derating chart lists a cap of 20 mA for that LED at room temperature. Your LED's own datasheet has its own figures, but a 12-volt battery sits many volts past curves like this one, so a bare LED wired straight across it has nothing to hold the current down.

[Sharp's application note on visible LED circuits](https://static.elitesecurity.org/uploads/1/8/1865204/SHARP.pdf){: rel="nofollow noopener noreferrer" } describes the fix: a resistor in series with the LED, meaning in the same wire, one after the other. In that note, the LED current (IF) equals the supply voltage (VCC) minus the LED's forward voltage (VF, the voltage the LED drops while lit), divided by the resistance (R). Turned around, the resistor you need is R = (VCC − VF) / IF, with VF and IF taken from the LED's datasheet. The same note treats VF as roughly constant when choosing R.

The supply voltage in that formula is higher than the label suggests. [Power-Sonic's datasheet for its PS-1230](https://www.power-sonic.com/wp-content/uploads/datasheets/ps-1230.pdf){: rel="nofollow noopener noreferrer" }, a 12-volt sealed lead-acid battery, specifies a charging voltage of 14.1 to 14.7 V for cyclic use, at 20°C. [Battery University](https://batteryuniversity.com/article/bu-403-charging-lead-acid){: rel="nofollow noopener noreferrer" }, published by the battery-analyzer maker Cadex, gives a charge limit of 2.30 to 2.45 V for each lead-acid cell; a 12-volt lead-acid battery has six cells, so that works out to 13.8 to 14.7 V.

A resistor sized at exactly 12 V therefore lets too much current through while the battery is on charge. The worked example below uses the 2.0 V and 20 mA figures from ROHM's manual:

| Resistor sized for | Calculation | Resistor | Current at 12.0 V | Current at 14.7 V (on charge) |
|---|---|---|---|---|
| 12.0 V | (12.0 − 2.0) / 0.020 | 500 Ω | 20 mA | about 25 mA, above the 20 mA limit |
| 14.7 V | (14.7 − 2.0) / 0.020 = 635 Ω, rounded up | 680 Ω | about 15 mA | about 19 mA |

Resistors also have a power rating. In the example above, the 680 Ω resistor drops 12.7 V while passing 0.019 A, and multiplying those gives about 0.24 W of heat, so a resistor rated 0.5 W or more leaves room. If you run several bare LEDs side by side, ROHM's manual and its [LED circuit configuration page](https://techweb.rohm.com/product/opto-electronics/led/23825/){: rel="nofollow noopener noreferrer" } recommend one resistor per LED. ROHM's manual explains that LEDs with slightly different forward voltages draw uneven current through a shared resistor and glow at different brightness.

## How to wire LED lights to a 12-volt battery with a switch, step by step

Each step below ends with the thing to check before you move on.

1. **Work out the current.** For lights labeled 12-volt, divide the total watts listed on the labels by 12 to get amps; a 24 W strip draws about 2 A. Check: the switch, the wire and the fuse all have to cover this figure.
2. **Pick the wire, then the fuse.** Choose wire whose ampacity, the current it is rated to carry, covers that figure, using a wire chart that also accounts for the length of the run. The Coast Guard rule in 33 CFR 183.455 sizes the fuse to the wire it is protecting, capping it at 150% of the wire's listed ampacity for circuits under 50 V. Check: the fuse rating sits above the LED current and below that cap.
3. **Mount the fuse holder at the positive terminal.** Leave the fuse out. Check: the unfused wire between battery and holder is as short as you can make it.
4. **Run the fused wire to the switch.** Connect the fuse holder's output to one switch terminal and the other switch terminal to the LED's positive lead or pad. Putting the switch in the positive wire means the LED wiring is dead whenever the switch is off. Check: a multimeter on its continuity setting, which beeps when current has a path, beeps across the two switch terminals only in the on position.
5. **Return the negative side.** Run the LED's negative lead to the battery's negative terminal. In a vehicle whose battery negative is bolted to the metal body, a clean bolt on that body works as the return. Check: the copper solder pads at the strip's end, marked + and −, match the wires feeding them.
6. **Fit the fuse and test.** Push the fuse in and turn the switch on. Check: across the LED's two terminals, a multimeter reads battery voltage with the switch on and zero with it off.

If the fuse blows the moment it goes in, something on the positive side is touching negative or metal; pull the fuse and find the short before trying again. If the LED stays dark in both switch positions, check polarity first. Sharp's application note shows why from the AC side: an LED fed with AC emits only in half of each wave, and the note adds a diode to protect the LED against reverse voltage. On a battery, an LED wired backward stays dark, so switch off and swap the + and − connections.

A switch with three or more terminals may use the extras for a built-in indicator light or a second circuit. Wire that kind of switch from its maker's diagram for the exact part number, rather than from the terminal layout of another switch.

## Choosing a switch that can carry 12-volt DC

A switch printed with a large AC rating can still be a poor match for a 12-volt DC circuit. [Omron's FAQ on switching DC with its basic switches](https://forum.digikey.com/t/how-do-i-open-and-close-dc-using-a-basic-switch/35412){: rel="nofollow noopener noreferrer" } explains that the arc, the spark that jumps between the switch's contacts as they separate, lasts longer on DC. The same FAQ says this causes more severe contact wear than on AC, and it advises choosing a switch with a DC rating.

[Omron's datasheet for its A-20G basic switch](https://static.chipdip.ru/lib/275/DOC011275390.pdf){: rel="nofollow noopener noreferrer" } shows how far the columns can differ:

| Load and voltage (Omron A-20G datasheet) | Rated current |
|---|---|
| Resistive load, 250 VAC | 20 A |
| Resistive load, 250 VDC | 0.25 A |
| Resistive load, 14 VDC | 20 A |
| Lamp load, 14 VDC | 3 A on the normally closed side, 1.5 A on the normally open side |

The lamp-load figures sit lower, and the same datasheet's notes define a lamp load as drawing an inrush current, a brief surge at switch-on, of 10 times its steady-state current, the current once it's running. The datasheet gives no such multiple for LEDs, so that figure can't be carried over to an LED's surge. For your LED circuit, read the DC column at or just above your system voltage. If the LED maker publishes an inrush figure, compare it with the switch's inrush rating too; Omron lists 75 A max for the A-20G. The same rating check applies to [a 5 amp micro switch on a low-voltage load](/guides/5-amp-micro-switch-rating-load-suitability/).

## Using a micro switch to turn LEDs on with a door or lid

A micro switch, also called a snap-action switch, lets a door, lid or drawer work the lights for you. Omron's A-20G datasheet labels its three terminals common (COM), normally closed (NC) and normally open (NO), with an SPDT (single pole, double throw) contact form: one moving contact that connects COM to either NC or NO. [Electronic Design](https://www.electronicdesign.com/markets/energy/article/21789793/snap-action-switches-still-rule-the-roost){: rel="nofollow noopener noreferrer" } describes the rest state: with the actuator, the button or lever that gets pushed, at its free position, the common contact sits against the normally closed contact.

For a cabinet light that comes on when the door opens, run the fused positive wire to COM and connect NC to the LED's positive lead. Mount the switch where the closed door presses its actuator. The closed door then holds the actuator down, which opens the COM to NC path and keeps the LEDs off. Open the door and the actuator springs back, closing COM to NC, and the LEDs light.

The switch sits in the same place in the loop as any other switch, after the fuse on the positive wire, and its DC rating has to cover the LED current you worked out in step 1. For more on reading the terminals, see [what normally open and normally closed mean on a micro switch](/guides/no-nc-micro-switch/). [How a cabinet door position micro switch detects door movement](/guides/cabinet-door-position-micro-switch/) covers the mechanical side, and [wiring and load checks for a micro switch on an LED load](/guides/micro-switch-led-wiring-load-checks/) covers the electrical side.

## FAQ

### What happens if you connect a LED directly to a 12V DC?

The answer depends on the LED. A product sold for 12-volt use, such as the strips Inspired LED describes, has a resistor in each path and lights normally. A bare LED has no current limit of its own. The sample LED in ROHM's manual reaches its 20 mA limit at only about 2.2 V, so a 12-volt battery drives that kind of LED far past its limit.

### What happens if you connect an LED directly to a battery without a resistor?

The current is then set only by the LED's own voltage-current curve and the battery, and on ROHM's sample curve a few tenths of a volt make the difference between 1 mA and 20 mA. Sharp's application note adds a resistor in the same wire as the LED, which takes up the extra voltage and holds the current at a value you choose.

### Do 12V LED lights need a transformer?

A transformer changes the voltage of AC, the kind of power a wall outlet supplies, and a battery supplies DC. A light labeled 12-volt DC runs straight from a 12-volt battery through a fuse and a switch, with no transformer or adapter in between.

### What cable for 12V LED lights?

Choose a wire whose rated current, its ampacity, covers what the lights draw, allowing for the length of the run. The fuse comes second: under 33 CFR 183.455, the fuse for a circuit under 50 V may not exceed 150% of the ampacity listed for the wire it protects.

## What to measure once a bare LED is lit

For a bare LED with its own resistor, measure the battery voltage while the battery is on charge, because that's when the LED current peaks. Work out IF = (VCC − VF) / R with that voltage and confirm the result stays under the LED's datasheet limit, as the 680 Ω row in the table does.


## Related guides

- [emergency shut off switch](/guides/emergency-shut-off-switch/)
- [generator switch over](/guides/generator-switch-over/)
- [what is a micro switch](/guides/what-is-a-micro-switch/)

## Sources

- US Coast Guard, 33 CFR 183.455, Overcurrent protection: general (Electrical Systems, boats with gasoline engines; scope in 33 CFR 183.401); 33 CFR 183.401
- ROHM, LED Manual, Rev.003, Jan. 9, 2018 (Characteristics data: IF-VF chart, derating chart; LED operation circuit)
- ROHM TechWeb, LED Circuit Configuration
- Sharp, Opto Application Note, "Visible" Light-Emitting Diode Application Circuits (third-party copy)
- Inspired LED, Inspired LED 101: Part 1, Components of an LED Strip
- Power-Sonic, PS-1230 sealed lead-acid battery datasheet
- Battery University (Cadex), BU-403: Charging Lead Acid
- Omron, General-purpose Basic Switch A (A-20G) datasheet, CSM_A_DS_E_3_4 (third-party copy)
- Omron FAQ, How do I open and close DC using a basic switch? (republished by DigiKey TechForum; original FAQE20034)
- Electronic Design, Snap-Action Switches Still Rule The Roost
