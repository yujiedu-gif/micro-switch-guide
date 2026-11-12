---
title: "How a Water Heater Thermal Cutoff Switch Works: ECO, TCO and the Reset Button"
description: "A water heater thermal cutoff switch opens a circuit when heat passes a fixed limit. Learn how electric and gas cutoffs work, trip, and reset."
date: 2026-10-11 18:01:49 +0800
category: Applications
tags:
  - thermal cutoff switch water heater
  - micro switches
  - Applications
author: editorial_team
seo_title: "Water Heater Thermal Cutoff Switch: How ECO and TCO Work"
last_updated: 2026-11-12
---

When an electric water heater stops making hot water, the usual advice is to remove the upper access panel and press the small red reset button. On a gas heater, the part called a thermal switch may have no button at all, or it may sit on the burner door and react to heat the water never feels. **Every one of these switches opens only after something upstream has already overheated, so pressing reset brings the heat back while the cause is still there.** The electric high-limit switch, the gas thermostat's cutoff and the gas burner-door switch each sense a different heat, trip at a different point and reset differently.

## Quick answer

A water heater thermal cutoff switch is a temperature-operated safety switch that opens a circuit and shuts the heater down when heat passes a fixed limit. A.O. Smith's residential training manual describes it on electric models as a high-limit switch that cuts power to the heating elements, and on gas models as a switch that stops the gas.

Manufacturers use several names for the same family of parts. Rheem's technical service bulletin and State Water Heaters' service handbook both call the water-temperature version an energy cut-off (ECO). The State handbook calls the version that watches the burner's combustion chamber a thermal cut-off switch (TCO). The electric control circuit in A.O. Smith's manual has the ECO as its only thermal cutoff. The same manual notes that ANSI now requires residential gas water heaters to be flammable vapor ignition resistant (FVIR). An FVIR heater is built so that vapors from something like spilled gasoline burn inside the combustion chamber, and it carries both switches.

## Which thermal cutoff your water heater has

The type of heater decides which switch you're dealing with. The figures in this table come from the manufacturer documents named in each cell, and they apply to those models; the data plate and manual for your own heater give its exact values.

| Heater | Switch | What it senses | Opens at (manufacturer figure) | What it shuts off | Reset |
|---|---|---|---|---|---|
| Electric tank | ECO, also called the high-limit switch, mounted with the upper thermostat | Tank wall temperature | 170°F (77°C) in White-Rodgers' 754-1 limit control and A.O. Smith's training manual | Power to the heating elements | Manual red button |
| Gas tank | ECO inside the thermostat's temperature probe | Water temperature in the tank | About 180°F in A.O. Smith's training manual; 188°F (87°C) in Bradford White's RG2F service manual | The small current that holds the gas valve open | None on standard gas valves: State's handbook says the whole control is replaced |
| Gas tank, FVIR design | TCO on the burner or inner door | Combustion chamber heat | 240°, 270° or 290° by color code in Bradford White's FVIR service manual | Pilot and main burner | Manual red button on the switch |

## How the snap disc inside a thermal cutoff opens the circuit and stays open

Inside an electric ECO, the part that does the switching is a small metal plate that changes shape with heat. Rheem's bulletin on electric thermostats walks through the trip this way:

1. Heat from the inner tank wall reaches a metal plate pressed against it.
2. The plate expands until it inverts from convex to concave, bowing the other way.
3. The inverted plate pushes a pin outward.
4. The pin forces the contacts under the red RESET button apart, and current can no longer pass through the ECO to the rest of the heater.

The contacts don't creep apart as the tank warms. Senasys, which makes bimetal snap-disc thermostats, says its discs "snap" on a temperature change, "providing positive and instantaneous opening of the electric circuit."

Electronic Design's explainer on snap-action switches describes a micro switch storing energy in a spring as its button-like plunger is pressed and releasing it at a set point in the travel, so the contacts change state at once. A thermal cutoff gets the same kind of sudden contact change from heat acting on the disc instead of a finger on a plunger. Temperature-triggered switching of this kind is the subject of how a snap-action thermal switch changes state.

Once tripped, a manual-reset disc stays inverted after the tank cools. A Therm-O-Disc patent for a trip-free manual reset thermostat (US 4,480,246, granted 1984) explains that the disc stays in its operating condition until someone pushes it back. The same patent defines trip-free: the reset member can't close the contacts while the disc is still above its operating temperature. Senasys lists a related limit for its own manual-reset discs, which can be reset only after the temperature has dropped at least 25°F from the trip.

## Why the electric high-limit trips at 170°F and opens both power wires

An electric heater's thermostats and its ECO sit in the same housing, but they do two different jobs. A.O. Smith's training manual describes the upper thermostat heating the top third of the tank, then passing power to the lower element, with the high-limit switch tripping above 170°F to shut off both elements.

White-Rodgers' installation instructions for its 754-1, 755-1 and 756-1 electric water heater controls state the two jobs plainly. The temperature control adjusts from 90°F to 150°F. The 754-1 limit control is a normally closed double-pole switch, meaning it conducts until heat opens it and it opens two wires at once. The same document lists it with a fixed 170°F (77°C) setting and manual reset, rated 40 A at 120 to 250 VAC for resistive loads. White-Rodgers' wiring diagrams show the 240 VAC circuit as a "full power disconnect through both power conductors."

A 240-volt heater has two live supply wires. Opening only one would stop the heating but leave the element connected to the other live wire, which is why the limit control opens both.

UL 174, the US safety standard for household electric storage tank water heaters published by UL Standards & Engagement (ULSE), also limits how hot the everyday thermostat can be set. Intertek's update notice on the November 1, 2024 revision summarizes a new clause: a user-adjustable thermostat or electronic setpoint can't be set above 77°C (171°F).

Above the ECO, one more safety device waits. A.O. Smith's training manual notes that the temperature and pressure relief (T&P) valve opens and discharges water if the tank reaches 210°F, and that such a discharge for excess temperature could point to a problem in the control circuit.

## On a gas heater, two different switches answer to "thermal cutoff"

A standard gas water heater's safety circuit runs on power made by its own pilot flame. State Water Heaters' service handbook explains that the flame heats a thermocouple, a sensor that turns heat into a tiny voltage. The same handbook puts a working thermocouple's output at 20 to 30 millivolts and says that small current holds the gas valve open.

Both gas cutoffs work by breaking that current:

- **The ECO in the thermostat probe.** The State handbook describes a metal probe on the back of the gas control that sits in the tank water. If the water gets excessively hot, an ECO switch in the probe opens, gas flow stops, and the handbook states that the ECO is not resettable, so the entire control must be replaced.
- **The TCO on the burner door.** The same handbook describes a resettable thermal switch that shuts off the gas after high combustion chamber temperatures caused by flammable vapors, a blocked vent or too little combustion air. A.O. Smith's training manual calls it the main difference between an FVIR heater and an older gas heater: a resettable thermal cutoff added to the thermocouple circuit.

Bradford White's FVIR service manual lists what usually trips the TCO and what each cause calls for. Insufficient combustion air means checking the air supply, clearing the air slots in the outer jacket and cleaning the flame arrestor plate, the louvered plate under the burner that keeps flames inside the chamber. A switch that opens too easily, or one with the wrong color code and so the wrong opening temperature, means replacing the switch. A flammable vapor incident means replacing the water heater.

## What a tripped thermal cutoff is telling you, and what to leave alone

A cutoff that has opened is reporting heat that got past the heater's normal controls. Rheem's bulletin states that frequent ECO trips indicate additional problems and tells owners to call a water heater professional. Bradford White's service manual says the overheating condition must be determined before the heater goes back in service.

Opening the panel to see the button means working near live parts. White-Rodgers' instructions tell installers to disconnect power at the main fuse or circuit breaker box first. On a gas heater, State's handbook starts its control-replacement steps by turning off the gas at the manual shut-off valve beside the heater.

Bypassing a thermal cutoff removes the only part that would stop a runaway heater. State's handbook warns: "Do not attempt to disable or modify this feature in any way. Use only factory authorized replacement parts." A replacement has to match the original's opening temperature and reset type, which Bradford White ties to the switch's color code. A qualified water heater technician should make that match, and gas-side work belongs with a licensed gas technician.

📌 **On a protective switch's place in the circuit:** *A thermal cutoff is one input to the heater's protective circuit, the same role described in how a safety switch works within a protective circuit. The switch opening shows that heat crossed a limit, and the reason it crossed has to be found elsewhere.*

## FAQ

### What is a water heater thermal switch?

A water heater thermal switch is a heat-operated safety switch that shuts the heater down when a temperature passes a fixed limit. On an electric heater it's the ECO, or high-limit switch, with a red reset button above the upper thermostat, according to A.O. Smith's training manual. On a newer flammable-vapor-resistant gas heater it usually means the resettable switch on the burner door, which State Water Heaters' handbook describes as shutting off the gas after combustion chamber overheating.

### Is 130 too hot for a water heater?

Hot water at 130°F burns skin in seconds rather than minutes. State Water Heaters' handbook lists about 30 seconds to produce second- and third-degree burns on adult skin at 130°F, and A.O. Smith's training manual lists 20 seconds for a first-degree burn. Each document lists more than 5 minutes for a burn at 120°F, and the State handbook gives 120°F as its recommended setting.

### Can a water heater thermal cutoff switch be bypassed?

Manufacturers say no. State Water Heaters' handbook tells service providers not to disable or modify the resettable thermal switch and to use only factory authorized replacement parts. A cutoff that keeps opening is reporting a fault, and Bradford White's manual calls for finding the overheating condition before the heater runs again.

## Where to look before you call for service

The model number on the heater's data plate leads to the manual for that exact unit, and the manual's ECO or thermal switch section gives the opening temperature and reset method for your switch. If you have an RV unit, identifying what an RV electric water heater switch controls starts from the same labels. Knowing whether you have an electric ECO, a gas probe ECO or a burner-door TCO tells the technician which circuit to check first.

## Sources

- A.O. Smith, *Residential Water Heater Training* (January 2016), pages 6, 10, 18, 20–23, 25 and 34–35
- State Water Heaters (A.O. Smith), *Service Handbook for Standard Residential FVIR Gas Water Heaters*, 316876-000 (06/09), pages 3, 10–12, 20 and 23
- Bradford White, *Service Manual: Flammable Vapor Ignition Resistant Water Heater*, 238-44943-00A, pages 3, 4 and 20
- Bradford White, *Service Manual* 238-51617-00C (10/20), RG2F high EF atmospheric vent gas models, page 5
- Rheem Technical Service Department, *Technical Service Bulletin: How An Electric Thermostat Works*
- White-Rodgers, *754-1, 755-1, 756-1 Electric Water Heater Control Installation Instructions*, part no. 37-5787B
- US Patent 4,480,246, *Trip-free manual reset thermostat*, Donald J. Schmitt, assigned to Therm-O-Disc, granted October 30, 1984
- Electronic Design, *Snap-Action Switches Still Rule The Roost*
- Senasys (STEMCO), *1/2" Manual Reset Snap Disc Thermostats*
- UL Standards & Engagement, UL 174, *Household Electric Storage Tank Water Heaters*, Edition 11 (2004), last revised April 28, 2025: https://www.shopulstandards.com/ProductDetail.aspx?productId=UL174
- Intertek, *Standards Update Notice: UL 174* (issued April 22, 2025), covering UL 174:2004 Ed.11+R:01Nov2024: https://w3inte.intertek.com.mx/siteassets/resources/sun/2025/ul-174-sun-rev-11-1-2024-ed-11-1-2026.pdf
