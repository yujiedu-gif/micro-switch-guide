---
title: "5 Amp Micro Switch Load Suitability: Reading the Rating Against Your Load"
description: "A 5 amp micro switch is rated for one load type at one voltage. How to check AC or DC, motor or lamp inrush, and cycle count against the datasheet."
date: 2026-10-12 16:49:35 +0800
category: Selection Guides
tags:
  - 5 amp micro switch
  - micro switches
  - Selection Guides
author: editorial_team
seo_title: "5 Amp Micro Switch Load Suitability: Reading the Rating"
last_updated: 2026-11-12
---

A micro switch stamped with a five-amp, 250-volt rating seems ready for any load under five amps: a heater, a bulb, a 12-volt pump, a small fan. Search answers often read it the same way and say a 5 amp switch can handle close to 5 amps. **The 5 amp figure belongs to one type of load at one voltage, and the same switch can be rated for a small fraction of it on a DC supply or a motor.** Reading a datasheet against a real load means checking the supply, the load type, the number of switching cycles, and the loads that are too small.

## Quick answer

A 5 amp micro switch is a switch whose datasheet allows 5 A of steady current for one stated load type at one stated voltage. Switch makers' datasheets note that these values are steady-state currents under set test conditions. Whether it fits your load depends on AC or DC, the load type, its inrush current and the number of cycles.

## What the "5 A" on a datasheet covers

A micro switch, also called a snap-action switch, is tested by its maker with a specific load, voltage and switching rate, and the current rating on its datasheet (the maker's specification sheet) holds only for that test.

Two load words come up in rating tables. A resistive load, such as a heater element, draws a steady current. An inductive load is a coil, such as a motor, a solenoid or a relay; one switch maker's technical note names electromagnets and motors as the typical examples. A datasheet for a general-purpose basic switch rated up to 20 A states that its rating values are steady-state currents, meaning the current once the load is running. That datasheet measures them at 20 ±2°C, 65 ±5% relative humidity and 20 operations per minute.

Two switches sold as "5 A" show how much the label leaves out. A miniature basic switch datasheet rates its 5 A model at 5 A for 125 VAC and 3 A for 250 VAC on a resistive load, and lists no DC rating for that model. A second maker's datasheet for a standard basic switch series lists rating code 05 under two approvals. The series' Underwriters Laboratories (UL) listing lists 5 A of general-purpose (inductive) current at 125/250 VAC and 0.1 A resistive at 48 VDC. The series' ENEC (European Norms Electrical Certification) listing lists "5 (2.5) A" at 125/250 VAC.

| Switch and listing | Load type | AC rating | DC rating | Cycles at that rating |
|---|---|---|---|---|
| Miniature basic switch, 5 A model | Resistive | 5 A at 125 VAC; 3 A at 250 VAC | None listed | Not given in the ratings table |
| Standard basic switch, code 05, UL listing | General purpose (inductive, 75% to 80% power factor) | 5 A at 125/250 VAC | 0.1 A resistive at 48 VDC | 10,000 |
| Standard basic switch, code 05, ENEC listing | 5 A resistive, 2.5 A inductive | 5 (2.5) A at 125/250 VAC | Not listed | 50,000 (contacts A and F) |

The standard basic switch datasheet explains the bracket format: the number outside the brackets is the maximum resistive current, and the number inside is the maximum inductive current. A "5 A" label, in other words, can mean a resistive rating at one maker and an inductive rating at another. How AC load ratings on a micro switch are written covers more of these formats.

## Check 1: is your supply AC or DC?

DC is the harder job for the contacts. An arc is the spark that keeps current flowing across contacts that have just pulled apart. A switch maker's FAQ on opening and closing DC with a basic switch says the arc lasts longer in DC switching and wears the contacts more than in AC. The same FAQ tells you to pick a switch with a DC rating and use it within that rating. Another maker's technical notes say its snap-action switches are designed for AC and may be used for low-capacity DC.

The table above shows the size of the gap. The standard basic switch that carries 5 A at 125/250 VAC is rated 0.1 A at 48 VDC, and the miniature 5 A model has no DC rating in its datasheet at all. If the datasheet has no DC rating for your model, that model has not been rated for your DC load. Micro switch arc suppression explains why DC arcs last longer and what a suppression circuit can and cannot do about it.

## Check 2: what kind of load is it?

Loads differ in how much current they draw at the instant the switch closes and how much energy they release when it opens. The extra current at switch-on is called inrush current. The general-purpose basic switch datasheet defines the test loads behind its separate rating columns this way:

- **Lamp load:** inrush of 10 times the steady-state current.
- **Motor load:** inrush of 6 times the steady-state current.
- **Inductive load:** a coil such as a solenoid or relay, with a power factor of 0.4 or more on AC and a time constant of 7 ms or less on DC.

A resistive load, such as a heater element, is the simplest case. Per the technical note on basic micro switch concepts, it is the reference load used to set a switch's nominal rating, and switching it causes no specific problem.

That note comes from a different maker than the 20 A datasheet, and it gives a similar picture. Inductive loads can draw up to 6 times the rated current at switch-on, the note says, and lamps and capacitive loads up to 15 times, which raises the risk of the contacts welding shut. Breaking an inductive load, the same note says, "creates powerful arcing that accelerates erosion of contacts."

Motors are sometimes rated in horsepower instead of amps. For code 05, the standard basic switch datasheet gives a motor rating of 1/10 HP at 125/250 VAC. A motor larger than the horsepower figure is outside the rating, even if its running current reads below 5 A. What happens with inductive loads on a micro switch goes into coils and motors in more detail.

## Check 3: how many times will it switch?

A current rating comes with a cycle count. The standard basic switch datasheet ties the same code 05 rating to 10,000 cycles under its UL listing and 50,000 cycles under its ENEC listing. In the technical note on basic concepts, a nominal rating is defined as the current a switch can make and break for a given number of cycles, typically 100,000, and a maximum rating as the current it can switch for at least 6,000 cycles.

Lower current buys longer life. For checking a specific load, the general-purpose basic switch datasheet includes a chart of electrical durability against switching current. When the power is very low, the technical note on basic concepts says, electrical life comes close to mechanical life, the number of presses with no current at all. Mechanical life on a micro switch explains that second figure.

Some answers online give a fixed margin, such as staying below 80% of the rating. The manufacturer documents cited here do not give a fixed percentage. Instead, the general-purpose basic switch datasheet says life varies with switching speed and frequency, and that the reliable way to know the life in your use is a durability test on samples under actual conditions.

## Check 4: is the load too small for a 5 amp switch?

A 5 amp switch can fail on a load that is far too small, such as the input pin of a microcontroller, which only senses a voltage and draws a few thousandths of an amp. The general-purpose basic switch datasheet says that silver contacts used with microloads, or switched rarely, build up a sulfide coating that the current cannot break down, and it calls for a microload switch with gold contacts instead.

For that maker's switches, the technical notes that call snap-action switches AC devices draw a line at 0.1 A: for a load of 0.1 A or below, the notes call for the gold contact type. When a circuit needs gold-plated contacts covers that end of the range.

## Example loads checked against a 5 amp switch

The figures below apply the datasheet entries quoted above. Steady current is the load's power divided by its voltage.

| Load | Supply | Steady current | Load type | Datasheet entry that applies | Result |
|---|---|---|---|---|---|
| 500 W heater element | 120 VAC | About 4.2 A | Resistive | Miniature basic switch, 5 A model: 5 A at 125 VAC, resistive | Within the rating |
| 60 W incandescent bulb | 120 VAC | About 0.5 A | Lamp | Needs a lamp rating; the general-purpose basic switch datasheet's lamp test assumes 10 times steady current at switch-on | Check for a lamp rating before using it |
| 3 A pump motor | 12 VDC | 3 A, before the start-up surge | DC motor | Standard basic switch code 05: 0.1 A resistive at 48 VDC; miniature 5 A model: no DC rating | Outside both ratings |
| Microcontroller input | 5 VDC | A few mA | Signal | Technical notes cited above: gold contacts at 0.1 A or below | Use a gold-contact model |

## When the load is bigger than the switch

A switch that fails the supply, load or cycle check can still control the load through a relay, a switch whose small coil, once energized, closes a separate set of heavier contacts. A switch maker's knowledge-base article on contact welding gives switching the load with a relay or contactor as the countermeasure for a load beyond the switch's capacity. The micro switch then carries only the relay's coil current. The coil is itself an inductive load, so on a DC coil the switch still needs a DC rating, and a diode across the coil protects its contacts, as the arc suppression guide linked above explains.

## FAQ

### Are switches rated for 20 amps?

Some micro switches are. The general-purpose basic switch datasheet cited above rates its 20 A model at 20 A for 125 and 250 VAC on a resistive load. The same datasheet rates it at 0.25 A for 250 VDC, so the 20 A figure applies to AC only.

### How much current can a relay handle?

A relay's contacts carry their own rating, written the same way as a micro switch's: a current for a stated load type and voltage, with separate AC and DC lines. Read it with the same checks: supply, load type, inrush and cycles.

## What to write down before choosing a switch

Write down the supply voltage and whether it is AC or DC, the load type and its inrush, and how many times the switch will operate over the product's life. Then find the datasheet line that matches all of them. A switch with no matching line has no rating for your load.

Ratings also vary inside a single maker's catalog. [ZING EAR](https://www.zingear-switch.com/){: rel="nofollow noopener noreferrer" } lists its ZINGEAR G5W11-WZ200-W2 at a rated current of 5A with operating voltages of 125/250VAC and 30VDC, and its ZINGEAR G5T16-E1Z200 at a rated current of 16A at 250VAC. Both product pages give the current and the voltages as separate lines, so for a DC or motor load, the datasheet for the exact model is where to confirm the matching line.

## Sources

- ZING EAR, ZINGEAR G5W11-WZ200-W2 product page: https://www.zingear-switch.com/zingear-micro-switch-g5w11-wz200-w2-explosion-proof-micro-switch.html
- ZING EAR, ZINGEAR G5T16-E1Z200 product page: https://www.zingear-switch.com/zingear-group-g5t16-e1z200-home-appliance-micro-switch-micro-switch-supplier.html
