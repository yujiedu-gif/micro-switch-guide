---
title: "Air Fryer Basket Micro Switch Wiring: Which Terminals Are Used and How to Check Them"
description: "An air fryer basket micro switch closes or opens a circuit when the basket is pushed home. Learn to read COM, NO and NC and test which pair your fryer uses."
date: 2026-10-12 16:49:35 +0800
category: Applications
tags:
  - air fryer basket micro switch wiring
  - micro switches
  - Applications
author: editorial_team
seo_title: "Air Fryer Basket Micro Switch Wiring: Terminals and Tests"
last_updated: 2026-11-12
---

Slide the basket out of an air fryer mid-cook and the fan winds down, then slide it back and, on some models, cooking picks up again. A common answer to how that switch is wired says the basket closes a normally open contact that feeds the heater and fan, and leaves the third terminal unused. **That answer fits some air fryers, and the two wires on your switch, plus where they lead, decide whether it fits yours.** The terminal markings, the two jobs a basket switch can do and a meter test that tells them apart come next, in the order you'd meet them with the cover off.

## Quick answer

An air fryer basket micro switch is a small snap-action switch that the basket presses when it's pushed fully home. The owner's manual for air fryer model CM-17034 says its internal micro switch "automatically shuts down the fan and heating element when the Outer Basket is removed." Its wires show whether it cuts heater power itself or reports the basket to a control board.

## Before you open the housing

📌 **On safety:** *Unplug the air fryer and let it cool fully before removing any cover. The switch and its wires can carry mains voltage, and the heating element stays hot after cooking ends. Never bridge the switch wires to see whether the fryer runs, since that defeats the only thing stopping the heater with the basket out.*

Every test below is done with the plug out of the wall. If the fryer is still under warranty, the CM-17034 manual's advice is direct: "Never attempt a home repair." The same manual warns that skipping the warranty procedure "could render your warranty null and void."

## What the terminals on the switch mean

A three-terminal micro switch is marked common (COM), normally open (NO) and normally closed (NC), and some bodies print C for common. COM is the terminal that's always part of the circuit. NC is joined to COM when nothing presses the actuator, the button or lever on the switch that the basket pushes. NO is joined to COM only while the actuator is pressed. Daniel Herzog's article on snap-action switches in Electronic Design describes the resting state the same way. With the plunger free, "the NC circuit of the switch can carry current," and the common terminal is insulated from the NO terminal.

For an air fryer, "pressed" means the basket is in. So a circuit wired through COM and NO is complete only with the basket home, and a circuit through COM and NC is complete only with the basket out. Crouzet's explainer on how micro switches work describes the same pair of outcomes: in a normally open switch, pressing closes the contact "and current flows"; in a normally closed one, it opens and interrupts the current.

The body of the switch also carries its rating. Carling Technologies describes the common European format with the example "16(4)A 250V~ T85." In Carling's reading, 16 A is the resistive load current and the 4 in brackets is the inductive load current. Crouzet's Basic Technical Concepts document counts motors, solenoids and relay coils as inductive loads. The ~ means AC, and T85 is the maximum operating temperature in degrees Celsius. A switch in the heater path has to be rated for the heater's current, which is why the rating on the old switch belongs on your shopping list.

## Two jobs a basket switch can do

Owner's manuals describe two different behaviors when the basket comes out, and each points to a different wiring role.

### Cutting power to the heater and fan

The CM-17034 manual says the micro switch itself "shuts down the fan and heating element when the Outer Basket is removed." For the switch to do that itself, it has to sit in the same wire run that feeds the heater and fan, so pulling the basket opens that circuit directly. The same manual rates that fryer at 1500 watts on 120 V, which works out to about 12.5 A (1500 divided by 120) through anything in the heater path. A replacement switch for that position needs a resistive rating above that figure.

### Telling the control board where the basket is

Tower's user manual for its T17169 digital air fryer describes something different. When the basket is removed during cooking, "the unit will automatically stop working and the display will show 'OUt'," and when it's re-inserted, "the air fryer will resume operation on the latest selected setting." A fryer that remembers its setting and shows a message is reading the switch as a signal. The switch wires run to the control board, and the board, rather than the switch, turns the heater on and off. In that layout, whether the board expects COM and NO or COM and NC is a design choice you can only learn by testing.

The quickest way to tell which job your switch does is to follow its two wires. If they lead to the timer, thermostat or heater terminals, the switch is in the power path. If they end at a plug on the circuit board, it's a position signal.

## How to check which terminals your fryer uses

1. **Photograph the switch before unplugging anything.** Note which colored wire sits on which terminal. The photo is your wiring diagram, since owner's manuals such as the CM-17034 and Tower manuals don't print one.
2. **Pull the push-on spade connectors off the switch.** Testing the switch out of circuit keeps other components from showing up in the reading.
3. **Set a multimeter to continuity or the lowest resistance range.** Put one probe on COM and the other on NO.
4. **Press the actuator the way the basket does.** With the actuator pressed, COM to NO should read near zero ohms. Released, it should read open. Repeat on COM and NC, where the readings should be the reverse.
5. **Compare with the photo.** If the wires were on COM and NO, the circuit was meant to close with the basket in. If it used COM and NC, it was meant to close with the basket out, and the replacement has to be wired the same way.

A switch that reads open in both positions, reads closed in both, or flickers while you hold it pressed has failed. The general method for testing a micro switch with a multimeter covers meter settings in more detail, and the difference between NO and NC contacts explains why the two pairs read opposite each other.

## Common faults that look like a bad switch

Tower's T17175 manual describes a "safety switch in the cooking basket" that keeps the fryer from turning on "whenever the cooking basket is not properly situated inside the appliance." A fryer that won't start, or one that cuts out when the basket is bumped, can therefore be a basket that isn't reaching the switch.

- **Basket not fully home.** Anything that stops the basket short, such as baked-on grease on the rails, keeps the basket from pressing the actuator. Check this before opening the housing.
- **Worn or broken pressing part.** Whatever part of the basket or drawer reaches the switch, a chipped or bent one gives the same symptom as a dead switch.
- **Switch moved in its mount.** If the switch has shifted, the tab or rib on the basket may press it only part way. Electronic Design's description of snap action has the contacts change only once the plunger reaches the operating point, so a partial press can leave them unchanged.
- **Switch failed.** Only the meter test above confirms this one.

If the switch tests good and the basket seats properly, the fault lies elsewhere in the fryer. A step-by-step air fryer basket micro switch replacement covers removal and fitting once the switch is confirmed bad.

## FAQ

**What is the purpose of a micro switch?**
A micro switch turns a small movement into a definite contact change. In an air fryer, that movement is the basket reaching its fully inserted position. The CM-17034 manual describes its switch shutting down the fan and heating element when the basket is removed.

**How to wire up a micro switch?**
Put the wires back on the same terminals they came off, using your photo. In general, COM is joined to NO when the actuator is pressed and to NC when it's released, so the wires go on COM plus whichever of NO or NC gives the right state with the basket in. Match the replacement's rating to the original before fitting it.

**What are the symptoms of a bad micro switch?**
In an air fryer, a failed basket switch usually shows up as a fryer that won't start with the basket in, or one that stops when the basket is touched. On a meter, a bad switch reads the same in both actuator positions or reads unsteadily while pressed. Check that the basket seats fully first, since that produces the same symptom.

## What to record before you order a replacement

Write down three things from the old switch: which two terminals were wired, the rating printed on the body, and the actuator style, whether a plain plunger or a lever. The terminals and rating match the replacement to the circuit, and the actuator style matches it to the part of the basket that presses it. If the old switch carried the heater current, the new one's resistive rating has to cover the fryer's wattage divided by the supply voltage.

Air fryers come up in switch makers' own application notes. In a blog post on micro switch applications, [ZING EAR](https://www.zingear-switch.com/){:rel="nofollow"} lists air fryer temperature safety, with a bimetal strip and a micro switch working as two layers of overheat protection. Its home appliance line page adds that operating force and terminal style can be customized to each appliance's structure, which is one reason the basket switch in your fryer has to be matched to the original part rather than to a generic one.

## Sources

- Owner's Manual, 3.4 QT Air Fryer, Model CM-17034 (QVC item K47107)
- Tower, 6 Litre Vortx Digital Air Fryer User Manual, Model T17169 (Next listing G27102)
- Tower, 6 Litre Vortx Air Fryer User Manual, Model T17175
- Daniel Herzog, "Snap-Action Switches Still Rule The Roost," Electronic Design, 2012
- Crouzet, How does a microswitch work?
- Carling Technologies, Amp Ratings, HP, Volts
- ZING EAR blog, Micro Switches: The Silent Guardians of Precision Control: https://www.zingear-switch.com/micro-switches-the-silent-guardians-of-precision-control.html
- ZING EAR, Home Appliance Micro Switch product line page: https://www.zingear-switch.com/home-appliance-micro-switch
