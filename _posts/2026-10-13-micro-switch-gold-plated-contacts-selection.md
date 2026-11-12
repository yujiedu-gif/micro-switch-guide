---
title: "Micro Switch Gold Plated Contacts Selection: When a Circuit Needs Gold"
description: "Gold-plated micro switch contacts are for currents too small to break the film on silver. Where makers draw the line, and what a gold model gives up."
date: 2026-10-13 11:27:16 +0800
category: Selection Guides
tags:
  - micro switch gold plated contacts selection
  - micro switches
  - Selection Guides
author: editorial_team
seo_title: "Micro Switch Gold Plated Contacts Selection: When Gold Fits"
last_updated: 2026-11-12
---

A micro switch wired to a programmable logic controller (PLC) input or a microcontroller pin carries only a trickle of current, and it can start missing presses after weeks of clean clicks. Search answers meet the problem with one rule: below a set current and voltage, use gold. **Each switch maker sets that line for its own parts, and the gold-contact model gives up most of its current rating in return, so the choice comes down to matching the circuit against one datasheet.** Silver's failure at small currents comes first, then each maker's line, the other reasons for gold, its cost and the datasheet entries.

## Quick answer

Gold-plated contacts in a micro switch are contacts with a gold surface, used where the current is too small to break the film that forms on silver. Panasonic's technical notes call for its gold contact type when the load is 0.1 A or below, and Omron says its gold contacts appear mainly in basic switches rated at 0.1 A.

## Why silver contacts fail on small currents

Most general-purpose micro switches, also called snap-action switches, use silver or silver-alloy contacts. Crouzet's technical note says its switches are normally fitted with silver or silver-nickel contacts, which the note describes as a compromise between electrical performance, heat and service life that suits most applications.

Silver has one weakness. Panasonic's technical notes for its snap-action switches say silver contact surfaces are "prone to be oxidized and form a sulfide film". Once the film grows, the same notes say, it "may not be broken by the switching operation, causing a conduction failure". Omron's A-20G datasheet describes the same failure for silver contacts used with microloads, meaning very small currents, and points to a microload switch with gold contacts instead.

Omron's relay FAQ on oxide film gives the reason gold helps: gold is not susceptible to oxidation. Micro switch contact oxidation explains how the film forms.

## Where each maker draws the line for gold

Every maker sets its own threshold for when a load is small enough to need gold, and they do not use the same units.

| Source | When gold is called for | Lower limit or note |
|---|---|---|
| Panasonic technical notes (snap-action switches) | Loads of 0.1 A or below | Gold (Au) contact type |
| Crouzet technical note (its switches) | Below 20 V and/or below 100 mA, especially below 0.3 VA | Works down to about 4 V and 1 mA; below that, consult Crouzet |
| C&K datasheet, MM series | "Low level," defined as switching with no arcing: 0.4 VA max at 20 V AC or DC max | Gold option rated from low level to 1 A at 125 VAC or 30 VDC |
| Omron FAQE20005 | Gold contacts used mainly in its 0.1 A rated basic switches | Lists models such as SS-01, D2F-01 and D2MV-01 |

Some search answers give a single range, such as below 50 to 100 mA and under 20 to 24 V, without naming whose switch it describes. The makers above draw their lines at different points, so the threshold that applies is the one printed for the switch you are about to fit. Signal-level switching on a micro switch covers circuits that sit near those limits.

## Conditions that call for gold beyond current

Current is the main test, but the makers name others:

- **Rare switching.** Crouzet's note asks for gold especially when the switching frequency is low, giving less than about one cycle a week as an example. Omron's A-20G datasheet lists silver contacts used "with relatively low frequency for a long time" as a cause of the sulfide failure.
- **Sulfur and corrosive gas.** Crouzet's note asks for gold in a sulfide atmosphere or other corrosive environments. Panasonic's notes point to its contact sulfurization-prevention products, with gold-clad double-layer contacts, for very small loads or polluted air.
- **A logic-level input.** Honeywell's datasheet for its V15 series offers gold contacts "for controlling logic level/low energy circuits."

A safety or alarm switch that sits untouched for months and then has to pass a signal of a few milliamps meets two of these conditions at once.

## What a gold-contact model gives up

A gold-contact model carries a far lower maximum current. C&K's MM datasheet rates its fine-silver version at 7 A for 125 and 250 VAC. The same datasheet rates its 24K gold version from low level, which C&K defines as switching with no arcing, up to 1 A at 125 VAC or 30 VDC. Omron's FAQE20005 places its gold contacts mainly in switches rated at 0.1 A. A gold model therefore suits the signal side of a circuit and leaves the load side to a silver part or a relay.

Surges matter even inside the rating. Omron's datasheet for its SS series warns that a model for ordinary loads may give faulty contact on a microload circuit. Inrush current, the same datasheet says, can increase contact wear and shorten life even within a microload model's range, so a contact protection circuit may be needed. How a 5 amp rating compares with a real load covers the high-current side.

One part can sometimes cover both ends. Crouzet's note describes gold-plated silver-nickel contacts, possibly in a crossbar arrangement, that cover a very wide operating range so a single part number can serve different applications.

## How to read a datasheet for gold contacts

The contact material line is where gold shows up, and makers word it differently. C&K writes "24K Gold"; Panasonic writes "Au contact" or "Au-clad"; Honeywell's V15 datasheet lists "silver, gold-plated" as contact materials. Next to the material, look for these entries:

1. **The rating range.** C&K's MM datasheet writes it as "from low level to 1 AMP," which gives both ends at once.
2. **The minimum applicable load.** Omron's SS datasheet calls it a reference value at the N reliability level, an estimated malfunction rate below 1 in 2,000,000 operations at 60% reliability. Omron treats it as a reference figure rather than a guarantee.
3. **The contact resistance.** Read it together with the test current it was measured at; contact resistance explains how the figure is measured.

Then compare the circuit's current and voltage with the maker's low-level line, check that the gold model's maximum covers any surge at switch-on, and note how often the switch will operate and in what air.

## FAQ

### Why is gold used in electronics?

On switch contacts, gold is used because it does not tarnish the way silver does. Omron's relay FAQ notes that gold is not susceptible to oxidation and points to gold-alloy contacts for microloads, meaning very small currents.

### What does 24k gold plating mean?

24K is the label for pure gold. C&K's MM datasheet lists 24K gold on a copper alloy for its low-level contact option, as opposed to fine silver for its higher-current option.

## What to decide before ordering a gold-contact micro switch

Find the smallest and the largest current the switch will ever carry, including any surge. If the smallest sits below the maker's low-level line and the largest fits under the gold model's rating, the gold model is the match. If the largest does not fit, split the job: a gold switch for the signal, a silver switch or relay for the load.

Gold is also offered as a build option on small switches. In its article on customizing small micro switches for home appliances, [ZING EAR](https://www.zingear-switch.com/){:rel="nofollow"} says its ultra small micro switch supports customized gold-plated contacts to reduce contact resistance and improve corrosion resistance. The current limits above still decide whether that option suits your circuit.

## Sources

- Panasonic Industry, *Micro Switches & Detection Switches: Technical Terminology & Cautions for Use*
- Crouzet, *Microswitches: Basic Technical Concepts* (12/2020), "Choice of contact material"
- C&K, MM Series Mini Size Precision Snap-acting Switches datasheet (third-party mirror)
- Omron, FAQE20005, "Which basic switches have gold-plated contacts?", republished on DigiKey TechForum
- Omron, FAQE10082, "What could cause contact failure due to oxide film during microload switching?" (relays), republished on DigiKey TechForum
- Omron, General-purpose Basic Switch A (A-20G) datasheet, CSM_A_DS_E_3_4 (third-party mirror)
- Omron, Miniature Basic Switch SS datasheet, Cat. No. B053-E2-11D (third-party mirror)
- Honeywell, MICRO SWITCH V15 Series Standard Basic Switches datasheet, 004945 Issue 12 (RS Components)
- [ZING EAR blog, Customization of Small Micro Switches for the Home Appliance Industry](https://www.zingear-switch.com/customization-of-small-micro-switches--flexible-solutions-and-zingear-mode-analysis-for-the-home-appliance-industry.html){:rel="nofollow"}
