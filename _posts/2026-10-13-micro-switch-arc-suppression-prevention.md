---
title: "Micro Switch Arc Suppression: How RC, Diode and Varistor Circuits Protect the Contacts"
description: "Micro switch arc suppression diverts a load's stored energy away from the opening contacts. How RC, diode and varistor circuits work, and where each fits."
date: 2026-10-13 11:27:16 +0800
category: Basics
tags:
  - micro switch arc suppression prevention
  - micro switches
  - Basics
author: editorial_team
seo_title: "Micro Switch Arc Suppression with RC, Diode and Varistor"
last_updated: 2026-11-12
---

A micro switch that cuts power to a solenoid valve or a small DC motor can throw a visible spark at the moment its contacts pull apart. The usual fix is to add an RC snubber, a diode or a varistor, and the usual advice is to mount it close to the load. **Each of those parts gives the load's stored energy a path that avoids the gap between the contacts, and each one fits only certain supplies and costs something in return.** The spark's cause comes first below, then the circuits that divert its energy, then the loads where a suppressor is the wrong fix.

## Quick answer

Micro switch arc suppression means adding a small circuit that absorbs or diverts a load's stored energy, so less of it burns across the opening contacts. Crouzet's technical note for its switches lists three such circuits for inductive loads: a fast diode for DC only, and a varistor or an RC network for AC or DC.

## Why a micro switch arcs when it opens a load

An arc is a spark of current that keeps flowing through the air after two contacts have physically separated. Inside a micro switch, also called a snap-action switch, the contacts sit close together, so the arc has only a short gap to jump. Panasonic's technical notes for its snap-action switches say the design is meant for AC, with "small contact gaps and no arc absorber," meaning no part built to put an arc out. The same notes allow only low-capacity DC use, within each product's rating.

The kind of current decides how long the arc lasts. An Omron FAQ on power relays explains that an AC arc dies each time the current passes through zero, while a DC current never reverses, so its arc carries on until something forces it out. Omron's FAQ on basic switches (FAQE20034) draws the same line for micro switches: in DC switching the arc lasts longer and wears the contacts harder than in AC.

The kind of load decides how strong the arc is. A coil in a relay, solenoid or motor stores energy in its magnetic field while current flows through it. When the switch opens, the magnetic field collapses and the coil pushes back with a high voltage. Sprecher + Schuh's guide to surge suppressors for relay and contactor coils says that, without a suppressor, this spike can reach 8 to 10 times the coil's rated voltage. A voltage that high can push current across the separating contacts as an arc.

Crouzet's technical note calls these inductive loads. The same note states that breaking them creates "powerful arcing that accelerates erosion of contacts".

A resistive load such as a heater has no coil and stores almost no magnetic energy. Crouzet uses it as the reference load for its headline ratings and says switching it causes no specific problem. Our guide to inductive loads on a micro switch covers how these loads are rated.

## How each suppression circuit gives the energy somewhere else to go

Every suppression circuit does the same job: when the contacts open, the coil's current finds an easier route than the gap. The circuits differ in which supplies they suit and what they cost. Omron publishes a selection table for these circuits in its relay FAQ (FAQ02804), and the same contact physics applies to a micro switch driving a coil.

### RC network (snubber)

An RC network is a resistor (R) and a capacitor (C) wired in series. Omron's FAQ explains that the capacitor suppresses the discharge when the contacts open, and the resistor limits the current that flows when the contacts close again. As starting values, the same FAQ lists 0.5 to 1 μF per amp of contact current and 0.5 to 1 Ω per volt of contact voltage, with the final values to be confirmed by testing.

Panasonic's circuit notes for snap-action switches give a smaller example of 0.1 μF with a series resistor above 10 Ω. RC networks work on AC and DC.

The capacitor needs its resistor. Omron's FAQ warns that a capacitor wired alone across the contacts stores energy while the switch is open, and that this energy rushes through the contacts when they close and can weld them. More on how an RC snubber works with a micro switch.

### Diode across the load

A diode is a part that lets current flow one way only. Wired across a DC coil with its striped end (the cathode) toward the positive supply, it carries nothing in normal use. When the switch opens, it lets the coil's current circulate through the diode instead of jumping the contacts.

Omron's FAQ calls a diode generally the most effective protection for a DC load. The same FAQ specifies a reverse breakdown voltage (the voltage the diode can block) of more than 10 times the circuit voltage, plus a forward current rating above the load current. Crouzet's note gives the same placement for DC only, with the diode's reverse voltage above the supply voltage and its forward current about equal to the load current.

A diode cannot be used on AC, because it would conduct on every other half cycle. More on the flyback diode and a micro switch.

The diode has a cost. Omron notes that it slows the release of a relay or solenoid more than an RC network does, because the coil's current dies away slowly through the diode. Sprecher + Schuh's guide puts the increase in a contactor coil's drop-out time at 3 to 10 times.

Adding a Zener diode, a diode that also conducts backward above a set voltage, in series with the diode shortens that delay, according to Omron's FAQ. The two Omron sources differ on the Zener voltage: FAQ02804 puts it at about the supply voltage, while Omron Europe's knowledge-base article on contact welding puts it at about 1.2 times the supply voltage.

### Varistor

A varistor is a part whose resistance drops sharply above a set voltage, so it clamps the spike the coil produces. Omron's FAQ rates it, together with the RC network, as the most effective choice for an AC load. The same FAQ sets its cutoff voltage, the point where it starts to conduct, above 1.5 times the supply voltage, multiplied by 1.41 on AC to allow for the AC peak. A cutoff set too high, the FAQ warns, stops the varistor from doing anything. Crouzet's note lists a varistor for DC or AC, with a voltage slightly higher than the supply.

| Circuit | AC | DC | Selection rule (Omron FAQ02804) | Trade-off |
|---|---|---|---|---|
| RC network | Yes | Yes | C: 0.5 to 1 μF per A; R: 0.5 to 1 Ω per V | Lets a small current reach the load while the switch is open |
| Diode | No | Yes | Reverse voltage over 10 × circuit voltage; forward current above load current | Slowest release of a relay or solenoid |
| Diode + Zener | No | Yes | Zener voltage about the supply voltage (1.2 × in Omron Europe's article) | Shorter release delay than a diode alone |
| Varistor | Yes | Yes | Cutoff voltage over 1.5 × supply voltage (× 1.41 on AC) | Some release delay |

## Where to connect the suppressor: across the load or across the contacts

Omron ties the position to the supply voltage. For a varistor, FAQ02804 says connecting across the load works at 24 to 48 V, and connecting across the contacts works at 100 to 240 V. For an RC network, Omron Europe's article on contact welding gives across the load at 24 or 48 V and across the contacts at 100 to 200 V. A diode always goes across the DC coil itself.

An RC network across the contacts has a side effect on AC. Omron's FAQ notes that when the contacts are open, current flows to the load through the RC network, and that the load's impedance must be much smaller than the RC network's for the circuit to work. In practice, a switch with an RC network across it does not fully cut the load off. A guard or door interlock relies on its open switch to make a machine safe, so an RC network across an interlock's contacts works against the interlock's purpose.

## What arc suppression does not fix

Suppression acts on the moment the contacts open. Some damage happens at the moment they close. Crouzet's note says lamps and capacitive loads can draw an inrush current of up to 15 times the rated current when switched on, which raises the risk of contact welding. Breaking those loads, the same note says, is no harder than breaking a resistive one. A suppressor that acts when the contacts open does little for a surge that happens when they close, so the answer is a switch rated for lamp loads.

Panasonic's notes add a rule for capacitive loads: put a series resistor in front of each one to limit that surge. Contact welding and its causes covers what happens when the contacts fuse.

A suppressor also does not raise a switch's DC rating on paper. Omron's FAQ on DC switching tells you to select a switch with a DC rating and use it within that rating. The same FAQ points to its X series, which has a built-in magnet that blows the arc away from the contacts.

Crouzet's note lists the other ways of raising DC breaking capacity: an arc reduction circuit, a double-break switch, a switch with magnetic blow-out, or several switches in series operated together. If the load draws more than the switch can break, Omron's guidance on contact welding is to switch the load with a relay or contactor. The micro switch then drives the relay's coil, which is itself an inductive load and needs its own diode or RC network. How a 5 amp rating compares with a real load walks through that check.

Two environments call for more than a suppressor. Omron's datasheet for its A-20G switch says a switch must not be used on its own in flammable or explosive gas, because arcing and heat can start a fire. The same datasheet notes that arc energy near silicone oil, silicone rubber or silicone wiring can deposit silicon oxide on the contacts, and it calls for both a contact protection circuit and removal of the silicone source.

## FAQ

### Are relays considered inductive loads?

Yes. A relay coil is a winding that stores energy in a magnetic field, and Omron's relay FAQ lists relays and solenoids among the inductive loads whose release slows when a suppressor is added. A micro switch that drives a relay coil therefore needs the same protection as one that drives a motor.

### Are limit switches AC or DC?

A limit switch is often built around a basic micro switch, and the datasheet for that switch can list AC and DC ratings side by side. Omron's A-20G datasheet, for example, rates the same switch at 20 A for 250 VAC and 0.25 A for 250 VDC on a resistive load. The DC figure is the one to check whenever the supply is a battery or a DC power supply.

## What to check before adding a suppressor

Check whether the supply is AC or DC, because that rules the diode in or out. Check whether the load is a coil, a lamp or a capacitor, because suppression helps the first and does little for the other two. Check the switch's own DC rating, because no suppressor can stand in for it.

Switch makers also work on the arc inside the switch body. [ZING EAR](https://www.zingear-switch.com/){:rel="nofollow"} describes its new energy micro switches, used for functions such as charging gun insertion and removal detection, as having enhanced arc resistance and high insulation compared with basic micro switches. That is a property of the switch itself, so the supply, load and DC rating checks above still apply to the circuit around it.

## Sources

- Crouzet, *Microswitches: Basic Technical Concepts* (12/2020), sections "Influence of load type," "Choice of contact material" and "Electrical recommendations"
- Omron, FAQ02804, General Purpose Relays: "Choosing from among CR elements, diodes, varistors, and other kinds of surge suppressor elements, which is the most effective for protecting contacts?"
- Omron, FAQE20034, "How do I open and close DC using a basic switch?", republished on DigiKey TechForum
- Omron, power relay FAQ "Explain to me the mechanism that interrupts the arc", republished on DigiKey TechForum
- Omron, "What Causes Contact Welding And What Can Be Done About It?", Omron Europe automation knowledge base
- Omron, General-purpose Basic Switch A (A-20G) datasheet, CSM_A_DS_E_3_4, Safety Precautions (third-party mirror)
- Sprecher + Schuh, *Selecting Surge Suppressors for Relays, Contactors and Starters*
- Panasonic Industry, *Micro Switches & Detection Switches: Technical Terminology & Cautions for Use*, "Technical Notes on Electrical Characteristics" and "Cautions in a Circuit"
- ZING EAR, New Energy Micro Switch product line description (official site): https://www.zingear-switch.com/
