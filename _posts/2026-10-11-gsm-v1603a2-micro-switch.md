---
title: "GSM V1603A2 Micro Switch: What It Is and What to Check Before Replacing It"
description: "GSM-V1603A2 is a miniature snap-action micro switch used in microwave doors and refrigeration. Learn to read its markings and check a replacement."
date: 2026-10-11 18:01:49 +0800
category: Selection Guides
tags:
  - gsm v1603a2 micro switch
  - micro switches
  - Selection Guides
author: editorial_team
seo_title: "GSM-V1603A2 Micro Switch: What It Is and What to Check"
last_updated: 2026-11-12
---

A small black switch printed GSM-V1603A2 usually turns up behind a microwave door latch or inside a commercial cooler, often after the appliance stops responding to the door. Will any door switch with the same shape and the same rating print drop into that spot? **A replacement drops in only if the contacts, terminals and actuator also match, because one microwave can hold look-alike switches that close at opposite door positions.** The switch below is described by where its part number appears, by what its body markings mean, and by the checks that tell a matching replacement from a near miss.

## Quick answer

The GSM-V1603A2 is a miniature micro switch, also called a snap-action switch, used in microwave door and refrigeration circuits. Parts listings sell it under the Gersung name, and Parts Town lists it as Turbo Air part 4415A66600, now obsolete. The rating, contact form and terminal layout of a given switch come from the print on its body.

Replacement listings for the GSM-V1603A2 describe it as a normally open switch, one whose contacts close only while its plunger is pressed, and some sellers describe it as a 16 A switch that swaps with Omron's D3V-16 series. Seller descriptions are a starting point, so the print on your own switch is the record to check.

## Where the GSM-V1603A2 part number shows up

The part number appears in two kinds of equipment in public parts catalogs. Parts Town, a distributor of manufacturers' service parts, carries it as a genuine Turbo Air replacement part, number 4415A66600. Turbo Air builds commercial refrigeration equipment, where a commercial freezer door micro switch tells the controls whether a door is shut. The same listing gives the part as roughly 1.05 by 0.65 by 0.45 inches and flags it as no longer available.

Appliance parts sellers list the same number as a microwave door switch. Several of those listings pair it with GE, Samsung, Sharp and Frigidaire microwaves, where switches of this kind sit behind the door latch.

If the switch in your hand came from a microwave, the oven's own service manual tells you which job that switch does. If it came from a cooler, the Turbo Air part number above is the reference the equipment maker uses.

## What the part number can and can't tell you

A part number is a catalog key. The number lets a parts counter find the switch the equipment maker specified, and it lets you search for that exact part.

Some switch makers publish a legend that turns each part of the number into a feature. Omron's datasheet for its D3V miniature basic switch family is one example. In that legend, the digits after "D3V-" code the current rating, so D3V-16 is the 16 A model. A later digit codes the contact form: 1 for single pole, double throw (SPDT), 2 for single pole, single throw (SPST) normally closed, and 3 for SPST normally open.

"Normally" means at rest, with nothing pressing the plunger. A normally open (NO) contact closes only while the plunger is pressed, and a normally closed (NC) contact opens at that moment. An SPST switch has one such contact, while an SPDT switch has a common (COM) terminal that connects to the NO terminal or the NC terminal.

Omron's legend decodes Omron part numbers only. The "16" and the "03" inside GSM-V1603A2 look similar, but any reading of a Gersung number built on Omron's legend is a guess. Treat the similarity as a hint, then confirm the contact form and rating on the switch itself.

## How to read the markings printed on the switch body

If your switch body carries a rating code or terminal labels, the table below shows how two published sources explain each mark.

| Printed mark | What it means | Who explains it |
|---|---|---|
| 16(3)A | 16 A for resistive loads; the bracketed 3 A is the limit for inductive loads such as motors | Carling Technologies' rating guide uses 16(4)A as its example; Omron's D3V datasheet lists the D3V-16 at 16 (3) A, 250 VAC under its European approval |
| 125/250VAC or 250V~ | The AC voltages the current rating applies to; the ~ sign means AC | Carling Technologies' rating guide |
| 1/2HP | The motor load, in horsepower, the switch is rated to switch at the listed voltage | Omron's D3V datasheet lists the D3V-16 at 16 A, 1/2 HP for 125 VAC and 250 VAC |
| T85 or T105 | The maximum ambient temperature, in °C, the switch is rated for | Carling's guide defines T85; Omron's D3V datasheet gives T105 for the D3V-16 |
| µ | A micro-gap approval, meaning a contact gap under 3 mm | Carling Technologies' rating guide |
| Terminal labels | COM, NO and NC mark which terminal is common, normally open or normally closed; see how NO and NC terminals differ on a micro switch | Omron's D3V terminal drawings use these labels |

Terminal count is the first mark to read. Two terminals mean an SPST switch, either NO or NC, and the label or a continuity test tells you which. Three terminals mean COM, NO and NC, and the pair the original wires were on decides how the switch behaves.

## Why the switch's job in a microwave matters more than its number

US federal rules for microwave ovens, 21 CFR 1030.10, require at least two working safety interlocks plus a means of monitoring them. Each interlock is a door interlock micro switch or a similar device that stops the oven when the door opens. The same section requires that no single failed part can disable every interlock, and that a failed monitored interlock leaves the oven unable to run until it is repaired. Service instructions must say which interlock is primary and which is secondary.

A GE microwave service sheet shows how those roles look at the terminals. In that sheet, the primary interlock reads 0 Ω from COM to NO with the door closed and an open circuit with the door open. The monitor switch reads the opposite way.

The GE readings explain the risk in a look-alike swap. In the GE sheet, the monitor switch is closed while the door is open. A normally open part fitted in that spot would stay open with the door open, so the monitor circuit would never see the change it watches for. The service manual for your oven model is the document that names the job of each switch position.

## Safety before you touch the door switches

GE's service sheet states that its information is meant for people with an adequate electrical background. The same sheet warns that the high-voltage section of the power supply is hazardous and tells technicians to be certain the capacitor is discharged before servicing. Because the sheet asks for that step on top of switching off, unplugging alone is not treated as enough. Unplug the oven first, and leave the capacitor work to someone trained to do it.

Never run a wire across, tape down or bend a door interlock switch to make an oven run. 21 CFR 1030.10 also bars any service adjustment that leaves an interlock inoperative, so a faulty interlock is a reason to repair the oven before using it again.

## How to check a replacement against the original

Compare the old switch and the candidate side by side before any wire goes back on. Each row below is a mismatch that a matching shape can hide.

| Check | Why it matters | How to check it |
|---|---|---|
| Contact form | An NO switch in an NC position closes when the original opened | Count the terminals and read the labels; confirm with a continuity test |
| Current and voltage rating | The replacement must carry the same load at the same voltage | Compare the body prints line by line, including the bracketed motor figure |
| Terminal size | A tab narrower than the connector leaves a loose joint | Quick-connect tabs come in more than one width; Omron's D3V family alone offers #187 and #250 tabs, so match the width on your old switch |
| Actuator | The latch has to press the plunger at the same point | Compare plunger height, or lever length and shape |
| Mounting holes | A shifted switch changes when the contacts close | Hole size varies even within one family, as Omron's D3V datasheet lists 3.1 mm and 2.9 mm options; measure the old switch |
| Body size | The switch has to sit in the original bracket | Measure length, width and height against the old part |

For the continuity test, which the guide on how to test a micro switch covers in more detail, set a multimeter to resistance or continuity and touch the probes to COM and NO. With the plunger at rest, a normally open switch shows no continuity; pressed, it reads close to 0 Ω. Repeat on COM and NC if the switch has a third terminal, where the readings reverse.

Then compare the result with the microwave door interlock continuity test readings that the oven's service manual gives for that position with the door open and closed. A replacement that matches every row of the table and tests the same way as the original is the one that fits.

## FAQ

### Are microwave door switches universal?

Microwave door switches are not interchangeable as a group. US rules in 21 CFR 1030.10 require at least two interlocks plus monitoring, and a GE service sheet shows interlock and monitor switches that close at opposite door positions. A replacement fits only when its contact form, rating, terminals and actuator match the position it goes into.

### What is the purpose of a micro switch?

Crouzet describes a micro switch as an electromechanical device with snap-action or slow-action functionality that opens or closes a circuit when something moves its actuator. In a microwave, the moving part is the door latch, so the switches tell the oven whether the door is shut.

### How do you wire up a micro switch?

In a repair, the wiring follows the old switch. Photograph or label each wire before you remove it, then connect each wire to the terminal with the same label on the replacement: COM to COM, NO to NO, NC to NC. Check the result with the continuity test above before the cover goes back on.

## What to do with the switch in your hand

Read the body print and the terminal labels on the old GSM-V1603A2 first, then find the switch's position, primary, secondary or monitor, in your oven's service manual. A replacement has to match the print, the labels and that position's continuity readings.

Microwave door switches are a high-volume appliance part, and some switch makers publish their work in this area. [ZING EAR](https://www.zingear-switch.com/){:rel="nofollow"} lists microwave ovens among the kitchen appliances its home appliance micro switches are made for, and its success-cases page describes a Galanz microwave oven project for which it provides customized switch solutions. A maker's case page shows what a switch family is designed for, while the print and continuity checks above decide whether a part fits your oven.

## Sources

- US Code of Federal Regulations, 21 CFR 1030.10, Microwave ovens (Legal Information Institute)
- Omron, D3V Miniature Basic Switch datasheet (Cat. No. B103-E1-02A)
- Carling Technologies, Amp Ratings, HP, Volts
- GE microwave mini manual, service sheet hosted by iFixit
- Parts Town, Turbo Air 4415A66600, GSM-V1603A2
- Crouzet, How does a microswitch work?
- ZING EAR, Home Appliance Micro Switch product line page: https://www.zingear-switch.com/home-appliance-micro-switch
- ZING EAR, Success Cases page (Galanz Microwave Oven Project): https://www.zingear-switch.com/success-cases
