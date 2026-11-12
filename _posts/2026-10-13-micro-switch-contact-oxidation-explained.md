---
title: "Micro Switch Contact Oxidation: Why Silver Contacts Stop Conducting"
description: "Micro switch contact oxidation is a sulfide or oxide film on silver contacts that a small current cannot break. Why it forms, how to check it and prevent it."
date: 2026-10-13 11:27:16 +0800
category: Troubleshooting
tags:
  - micro switch contact oxidation explained
  - micro switches
  - Troubleshooting
author: editorial_team
seo_title: "Micro Switch Contact Oxidation: Why Silver Contacts Fail"
last_updated: 2026-11-12
---

A micro switch that clicked reliably for months can start to miss: the button goes down, the click is there, and the circuit stays dead. The usual explanation is oxidation, and the usual picture is a contact that simply rusts with age and air. **The film on a silver contact causes trouble mainly when the current through the switch is too small to break it, so the same switch can stay healthy on one circuit and fail on another.** The film's makeup comes first below, then the current that decides whether it matters, then the checks and the fixes.

## Quick answer

Micro switch contact oxidation is a thin film of silver sulfide or oxide that forms on a switch's contacts and blocks current. Panasonic and Omron both describe the film building up on silver contacts over time and causing contact failure when the switch carries too little current, or switches too rarely, to break through it.

## What the film is and where it comes from

Most general-purpose micro switches, also called snap-action switches, use silver or silver-alloy contacts. Crouzet's technical note says its switches are normally fitted with silver or silver-nickel contacts, and Omron's datasheet for its A-20G switch lists a silver alloy.

Silver reacts with the air around it. Panasonic's technical notes for its snap-action switches say silver contact surfaces "are prone to be oxidized and form a sulfide film." The word oxidation is used loosely for this, but both makers name sulfur as a main source. Omron's A-20G datasheet calls the layer a "sulfide coating" and lists the gases that attack contacts: hydrogen sulfide, sulfur dioxide, ammonia, nitric acid gas and chlorine.

The film can start before the switch is ever installed. Panasonic's notes say long storage at high temperature or humidity, or in air with organic or sulfide gases, may form a sulfide or oxide film on the contacts. The same notes ask for switches to be stored in a polyethylene bag or another airtight container, to keep their silver-plated terminals from discoloring through sulfurization.

## Why a small current cannot break through the film

A switch that carries a decent load keeps its contacts usable, because switching that load breaks the film; Omron's FAQ on relay contacts calls this a cleaning effect. When the current is tiny, that cleaning stops. Panasonic's notes describe the sequence: the switch "operates with no problems at the beginning of use," then, as the film grows, "the film may not be broken by the switching operation, causing a conduction failure."

Omron's A-20G datasheet gives two conditions for the same failure. Silver contacts fail when used with microloads, meaning very small currents, or when used "with relatively low frequency for a long time". A switch that sits untouched for weeks and then has to pass a signal faces the second condition. Omron's FAQ on the minimum applicable load (FAQE20025) adds that below that load, the contact surface is more susceptible to a chemical coating from the surrounding air.

Where "too small" begins depends on the maker:

| Source | Where a small load starts | Advice |
|---|---|---|
| Panasonic technical notes (snap-action switches) | 0.1 A or below | Use the gold (Au) contact type |
| Crouzet technical note (its switches) | Below 20 V and/or 100 mA, especially below 0.3 VA | Gold or gold-alloy coating, especially if switched less than about once a week or in a sulfide atmosphere |
| Omron FAQE10082 (relays) | A load of 48 V and 100 mA or more has a cleaning effect | Gold-alloy contacts for microloads |

The 48 V and 100 mA figure appears in some online answers about micro switches, but it comes from Omron's FAQ on relay contacts, and the switch makers above set their own lines in their own terms. For a micro switch, the threshold to trust is the one in that switch's own datasheet. Signal-level switching on a micro switch covers the low-current side in more detail.

## Other films that look like oxidation

Not every insulating layer on a contact is oxidation, and the fixes differ.

- **Silicone deposits.** Omron's A-20G datasheet says that near silicone oil, silicone rubber or silicone wiring, arc energy can deposit silicon oxide on the contacts and cause contact failure. Crouzet's note says silicone-containing substances must be kept away from its switches because they harm contact resistance.
- **Solder flux.** Omron's datasheet for its SS series warns that flux getting inside the switch can cause faulty contact.
- **Grease and oil.** Crouzet's note says grease and oil must never get inside its switches.
- **Corrosive gas.** Omron's A-20G datasheet warns that the gases listed above can cause contact faults or corrosion, a separate problem from the small-current film.

Corrosive atmospheres and micro switches looks at that last case.

## How to check whether the contacts are the problem

Disconnect power before you touch the switch or its wiring. Then check the contacts with a multimeter on continuity or resistance:

1. Measure between the common (COM) terminal and the normally open (NO) terminal with the actuator pressed all the way down. The normally open contact is the one that closes when the switch is pressed.
2. Measure between COM and the normally closed (NC) terminal with the actuator fully released.
3. Press and release several times and watch whether the reading stays steady.

The full press matters. Omron's FAQ on contact resistance specifies measuring the NC contact at the free position (fully released) and the NO contact at total travel (fully pressed). The same FAQ notes that contact pressure falls almost to zero near the points where the contacts change over. Crouzet's note says the same: near those points the contact force drops and resistance "may increase substantially". A reading that flickers at half press is therefore normal, and does not prove a film.

A healthy closed contact reads very low. Omron's A-20G datasheet lists 15 mΩ (thousandths of an ohm) maximum contact resistance for a new switch, and Crouzet's note gives generally less than 20 mΩ for its switches. Panasonic's notes say their figures are measured by voltage drop at 6 to 8 VDC and 1 A, so a handheld meter reading is only a rough comparison with those figures. A reading of several ohms, or one that jumps around at full press, points at the contacts. How to test a micro switch walks through the full test, and contact resistance explains the figure.

## How contact oxidation is prevented

The makers' answers follow from the cause:

- **Gold contacts for small loads.** Omron's A-20G datasheet calls for a microload switch with gold contacts, and Panasonic's notes call for the gold contact type at 0.1 A or below. Omron's relay FAQ notes that gold is not susceptible to oxidation. When a circuit needs gold-plated contacts covers that choice.
- **A little more current.** For very low-energy circuits below 1 mA and 4 V, Crouzet's note asks for the circuit to pass at least a few mA through the contacts, at least while they close, and says a higher voltage across the open contacts improves reliability.
- **Sulfur-resistant parts.** For air with hydrogen sulfide or other corrosive gases, Panasonic's notes ask users to consult the maker and point to its contact sulfurization-prevention products, which use gold-clad double-layer contacts.
- **A clean environment.** Remove silicone sources, keep flux, grease and oil out, and store spare switches sealed, as the Omron, Crouzet and Panasonic documents above describe.

## FAQ

### How to test a micro switch?

Disconnect power, then use a multimeter to check continuity from COM to NO with the actuator fully pressed and from COM to NC with it fully released. Omron's contact resistance FAQ specifies those two positions, because readings taken partway through the press are unreliable.

### Does contact cleaner remove corrosion?

The switch makers cited here do not list contact cleaner as a remedy. Crouzet's note says grease and oil must never get inside its switches, and Crouzet, Omron and Panasonic all warn against silicone near the contacts, so check what a spray contains before using it. On a switch that carries a very small load, a cleaned silver contact meets the same conditions that formed the film, and a gold-contact model removes the cause.

### How does a micro switch work?

A spring inside the switch snaps the moving contact from one position to another once the actuator passes a set point, so the contacts change over quickly however slowly you press.

### How many ohms should a switch have?

A closed switch in good condition reads close to zero. Omron lists 15 mΩ maximum initial contact resistance for its A-20G, and Crouzet gives less than 20 mΩ for its switches, both a small fraction of one ohm. A reading of whole ohms at full press points at the contacts.

## What to look at first on a switch that has started to miss

Look at the current the switch carries. If it feeds a logic input or another signal circuit, the cause is likely the film this article describes, and a gold-contact switch is the lasting fix. If it carries a motor or heater, look at the rating instead: Crouzet's note ties heavier loads to arc erosion and contact welding, which are different failures.

Switch makers address the same film in their own guidance. In its article on poor contact in mini micro switches, [ZING EAR](https://www.zingear-switch.com/){:rel="nofollow"} lists sealed housings rated IP65 or IP67 as its countermeasure for contact oxidation and sulfidation. The same ZING EAR article describes gold-plated brass contacts with a plating thickness of at least 0.5 μm and contact resistance of 10 mΩ or less.

## Sources

- Panasonic Industry, *Micro Switches & Detection Switches: Technical Terminology & Cautions for Use*
- Omron, General-purpose Basic Switch A (A-20G) datasheet, CSM_A_DS_E_3_4, Specifications and Safety Precautions (third-party mirror)
- Omron, Miniature Basic Switch SS datasheet, Cat. No. B053-E2-11D, Precautions (third-party mirror)
- Omron, FAQE20025, "What kind of problems may occur if the set current is below the minimum applicable load for a basic switch?", republished on DigiKey TechForum
- Omron, FAQE10082, "What could cause contact failure due to oxide film during microload switching?" (relays), republished on DigiKey TechForum
- Omron, FAQ "What is the contact resistance of a basic switch?", republished on DigiKey TechForum
- Crouzet, *Microswitches: Basic Technical Concepts* (12/2020)
- [ZING EAR blog, Solutions for Poor Contact in Mini Micro Switches](https://www.zingear-switch.com/solutions-for-poor-contact-in-mini-micro-switches.html){:rel="nofollow"}
