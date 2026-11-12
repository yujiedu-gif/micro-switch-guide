---
title: "Micro Switch Mounting Holes: Hole Sizes, Spacing by Switch Size, and How to Check the Fit"
description: "Micro switch mounting holes by size class, from switch makers' datasheets: hole diameter, center spacing, screw size and how to check a replacement fits."
date: 2026-10-12 16:49:35 +0800
category: Selection Guides
tags:
  - micro switch mounting holes
  - micro switches
  - Selection Guides
author: editorial_team
seo_title: "Micro Switch Mounting Holes: Sizes, Spacing and Fit"
last_updated: 2026-11-12
---

The two holes through the body of a micro switch look like an afterthought next to the button and the terminals. Swap in a switch whose holes line up, though, and the machine can still miss its stop or press the new switch too hard. **The mounting holes are the reference point for where a micro switch triggers, so a replacement has to match the hole spacing, the screw size and the trigger height measured from those holes.** The sections below give datasheet hole patterns for each common switch size, then the checks that confirm a new switch fits.

## Quick answer

Micro switch mounting holes are two through-holes, set a fixed distance apart, that screw the switch to a bracket. The spacing depends on the switch's size class. One switch maker's datasheets list a 22.2 mm center-to-center spacing with 3.1 mm holes for M3 screws on its miniature series, 9.5 mm on its subminiature series, and 6.5 mm on its ultra-subminiature series.

## Mounting hole sizes by switch size class

Micro switches, also called snap-action switches, come in a few size classes, and each class has its own hole pattern. Size names and exact dimensions vary between manufacturers, so the table labels the two makers whose published figures it uses as Maker A and Maker B. Each row comes from one maker's datasheet or product page for a single series.

| Size class | Source | Hole diameter | Screw | Hole center spacing | Screw torque |
|---|---|---|---|---|---|
| General-purpose (large basic) | Maker A datasheet | 4.2 mm | M4 | 25.4 ±0.1 mm | 1.18 to 1.47 N·m |
| General-purpose (large basic) | Maker B product page | not stated | not stated | 25.4 mm | not stated |
| Miniature (V-size) | Maker A datasheet | 3.1 mm | M3 | 22.2 ±0.1 mm | 0.39 to 0.59 N·m |
| Miniature (V-size) | Maker B datasheet, metric version | 3.10 mm +0.10/−0.05 | 3 mm pins or screws | 22.20 ±0.1 mm | not stated |
| Miniature (V-size) | Maker B datasheet, US version | 2.90 mm +0.10/−0.05 | #4 screws | 22.20 ±0.1 mm | not stated |
| Subminiature | Maker A datasheet | 2.4 mm | M2.3 | 9.5 ±0.1 mm | 0.23 to 0.26 N·m |
| Ultra-subminiature | Maker A datasheet | 2.0 mm | M2 | 6.5 ±0.15 mm | 0.08 to 0.1 N·m |

Two patterns in that table have more than one maker behind them. Maker B's product page for its large basic switch gives 25.4 mm centers, the same figure Maker A lists for its general-purpose series. For the miniature V-size, both makers' datasheets draw holes 22.2 mm apart. Maker B's product page for a second V-size series describes the size as a "22,2 mm x 10,3 mm diagonal mount". Maker A's drawing shows the same 10.3 mm second dimension, so the two holes are offset across the body as well as along it.

The table also shows a trap. Maker B's miniature datasheet lists 3.1 mm holes for 3 mm metric screws and, under a letter designator added to the part number, 2.9 mm holes for US #4 screws. Going by that datasheet, two switches from the same series can share the 22.2 mm spacing and still take different screws.

## Why the holes set where the switch triggers

A micro switch triggers when its actuator, the plunger or lever that the machine presses, reaches the operating position (OP). Maker B's datasheet for its sealed miniature switches explains how that position is measured. Linear dimensions for an in-line plunger run from the top of the plunger to a reference line, usually the center of the mounting holes. Maker A's general-purpose datasheet gives the operating position of its pin plunger model as 16.3 ±0.4 mm from the hole centers, where ±0.4 mm is the allowed tolerance.

That measuring convention has a practical consequence. Two switches with identical hole spacing can trigger at different points if their operating positions differ, because the plunger tip sits a different distance from the holes. A replacement that bolts straight on can then fall short of the cam or door that's supposed to press it, or get pressed past its overtravel, the extra distance the plunger can safely move after it switches. Our explainer on micro switch pretravel covers how operating position, pretravel and overtravel relate.

📌 **On slotted brackets:** *A bracket with slots instead of round holes lets the switch slide toward or away from the machine part. Since the operating position is measured from the hole centers, sliding the switch moves its trigger point by the same amount.*

## How to measure the holes and body of a switch you already have

When the old switch has no readable part number, three measurements identify its pattern.

1. **Hole diameter.** Measure across each hole with calipers. Compare with the datasheet figures in the table: about 4.2 mm, 3.1 mm, 2.9 mm, 2.4 mm or 2.0 mm points to a likely size class and screw.
2. **Center spacing.** Measure from the inside edge of one hole to the inside edge of the other, then add one hole diameter. For two holes of equal size, that sum is the center-to-center distance. Measuring edge to edge on the same side of each hole (left edge to left edge) gives the same number.
3. **Offset.** Check whether the holes sit on one line or diagonally. A V-size switch with holes on a diagonal, as Maker B describes for its second V-size series (22.2 mm × 10.3 mm), needs a bracket drilled on the same diagonal.

Then measure the body (length, height, thickness) and note which way the terminals point. A switch that matches the holes but has a longer body or terminals on a different side may not fit the space.

## Checks before and after you tighten the screws

Disconnect power before you remove or mount the switch. Maker A's subminiature datasheet tells installers to turn off the power supply before mounting or removing the switch, wiring it, or doing maintenance, because working live can cause electric shock or burns. On a plug-in appliance, unplug it; on battery equipment, take the battery out.

- **Use the specified screw and washers.** Maker A's miniature, subminiature and ultra-subminiature datasheets all call for mounting screws with plain washers or spring washers, at the screw size listed in the table above.
- **Don't overtighten.** The torques in Maker A's datasheets are small: the ultra-subminiature datasheet lists 0.08 to 0.1 N·m, which is a light twist with a small screwdriver, so a torque screwdriver or a gentle hand matters more on small switches.
- **Mount on a flat surface.** The same subminiature datasheet warns that mounting on an uneven surface can deform the switch, causing faulty operation or a broken housing.
- **Keep live terminals clear of a metal bracket.** That datasheet also cites EN 61058-1 for a minimum 1.6 mm clearance between live terminals and the mounting plate, and says to add a separator or insulation guard if that can't be met.
- **Mind lever weight.** Maker A's datasheet for another miniature series says to mount a lever switch so the lever's weight doesn't rest on the switch, because the small reset force may not return it. Our guide to hinge lever micro switch installation covers the extra alignment a lever needs.

After the screws are tight, move the machine part by hand and listen for the click. Then check with a multimeter that the contacts change state at the point where the machine part should trigger them. Our step-by-step guide on how to test a micro switch covers the meter setup.

## When a switch mounts without screw holes

Some switches are held another way. Maker A's general-purpose series includes panel mount plunger models that mount through a panel with an M12 × 1 threaded bushing and two hex nuts. The datasheet says not to use the M12 mounting and the screw holes at the same time. Our article on the panel mount plunger micro switch explains how that type works.

## FAQ

### What are the different types of micro switches?

By size, the usual classes run from general-purpose (large basic) through miniature and subminiature to ultra-subminiature; the Maker A datasheets cited here cover one series in each. By actuator, Maker A's general-purpose datasheet lists pin plunger, short spring plunger and panel mount plunger models, and its miniature datasheet adds hinge lever, hinge roller lever and simulated roller lever versions. Our overview of micro switch actuator types compares them.

### What screws are in a switch?

For the series in the table, Maker A's datasheets call for M4 screws on the general-purpose series, M3 on the miniature, M2.3 on the subminiature and M2 on the ultra-subminiature. Maker B's V-size datasheet covers a metric version for 3 mm screws and a US version for #4 screws. Check the hole diameter before buying screws: going by Maker A's subminiature datasheet and its 2.4 mm hole, an M2.5 screw won't pass through it.

## Matching a replacement to the old part

Before ordering, write down the hole diameter, center spacing, offset, body size, terminal direction and actuator type of the old switch, and compare them with the dimension drawing on the new part's datasheet. Offset here means how far one hole sits across the body from the other, the 10.3 mm figure on a V-size switch. The figure that's easiest to miss is the operating position measured from the hole centers, so check that last number before you assume a switch that bolts on will also trigger in the right place.

## Sources

- [IEC 61058-1:2026, Switches for appliances, Part 1: General requirements (IEC webstore; EN 61058-1 is the European adoption)](https://webstore.iec.ch/en/publication/115499){: rel="nofollow noopener noreferrer" }
