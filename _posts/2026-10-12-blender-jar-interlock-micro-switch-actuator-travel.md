---
title: "Blender Jar Interlock Micro Switch Actuator Travel: Pretravel, Overtravel and the Jar's Push"
description: "Actuator travel is how far a blender interlock switch's plunger moves when the jar seats. See how pretravel, overtravel and the jar's push fit together."
date: 2026-10-12 16:49:35 +0800
category: Applications
tags:
  - blender jar interlock micro switch actuator travel
  - micro switches
  - Applications
author: editorial_team
seo_title: "Blender Jar Interlock Micro Switch Actuator Travel"
last_updated: 2026-11-12
---

Twist a blender pitcher onto its base, press the lid down until it clicks, and on a Ninja BL682Q the power light stops flashing and goes solid. The usual description of what happens inside is short: a tab on the jar or lid presses the switch's plunger and closes the contacts. **The tab-and-plunger picture is right about the contacts and silent on distance, and distance is where a jar interlock is designed.** The travel terms on a switch datasheet, the path from the jar to the switch, and where the plunger ought to stop are taken in that order below.

## Quick answer

Actuator travel in a blender jar interlock micro switch is how far the switch's plunger or lever moves when the seated jar or lid pushes on it. Switch makers' datasheets split that stroke into pretravel, up to the contact change, and overtravel, the allowed travel beyond it. A jar interlock is built so the push stops the plunger inside the overtravel, past the contact change but short of the end.

## The travel terms on a micro switch datasheet

One maker's general technical data for limit switches labels four actuator positions. The free position has nothing touching the actuator, and the operating position is where the contacts change. The release position, on the way back up, is where they change back, and the maximum travel position ends the allowed stroke. Daniel Herzog's article on snap-action switches in Electronic Design describes the operating position in motion: "As the plunger is depressed, it reaches the operating point (OP)," and the contacts snap across.

Datasheets list the distances between those positions, and a switch maker's explainer on switch travel gives the definitions this way:

- **Pretravel (PT):** "the distance which the actuator moves from its free position to its electrical contact position."
- **Overtravel (OT):** "the distance between the electrical contact position and the full, allowable travel position."
- **Differential travel:** the distance between the "on" position and the "off" position. Other datasheets call the same distance movement differential (MD).

Actuator style changes those numbers sharply. One general-purpose basic switch datasheet shows the spread within a single series:

| General-purpose basic switch, one series (datasheet values) | Pretravel, max. | Overtravel, min. | Movement differential, max. | Operating force |
|---|---|---|---|---|
| Pin plunger version | 1.3 mm | 0.25 mm | 0.2 mm | 3.92 to 6.13 N |
| Long hinge lever version | 15.9 mm | 4 mm | 2.4 mm | 0.69 N max. |

A long lever turns a small, firm press into a long, light one. For a jar interlock, that choice decides how much slop in the jar's position the switch can absorb, and how hard the jar has to push.

## How the jar's push reaches the switch

In a blender described by a US patent assigned to Dualit Limited (US 6,513,966), the jar never touches the switch directly, and the patent lays out the chain in detail. A projection on the lid presses an actuator that slides vertically inside a stalk on the base, and the actuator in turn flexes the leaf-spring arm of the interlock switch. The patent says the switch is "normally in an open condition so that the motor is disabled," and closes only when the container and lid are correctly engaged.

The same patent sets out the travel budget in plain numbers. The actuator first operates the switch when the lid sits 2 mm higher than a fully engaged lid, and it "can move downwardly at least a further 4 mm" after that. Dualit's stated reason is "to accommodate tolerance variations in the container height." The patent also sizes the actuator head so the lid's projection still meets it with the lid off center "by up to 8 mm."

Dualit's figures describe the interlock linkage rather than the switch body, and the patent's switch is a leaf-spring contact rather than a packaged micro switch. A blender that uses a micro switch needs the same allowance, since a micro switch also changes state at one point and accepts only a limited stroke beyond it. The linkage needs extra stroke past the point where the contacts change, so a jar that sits a little high or a little low still lands in the safe range.

Owner's manuals show the result rather than the parts. Ninja's BL682Q owner's guide tells you to press the lid handle down "until you hear a click." Ninja also warns that "the power light will flash and the motor will not work if the pitcher and lid are not installed correctly."

## Where the plunger should stop

Switch makers tell designers not to stop the plunger at the operating point, where the contacts have only just changed. One general-purpose basic switch datasheet puts it as a rule: "The operating stroke must be set to 70% to 100% of the rated OT," and the actuator travel must not exceed the permissible OT position. Put plainly, the push should use most of the rated overtravel but not all of it. Another maker's FAQ on how far to push a basic switch gives a slightly different window, 60% to 90% of the specified OT. The FAQ adds that beyond 90% "the actuator or switch may be damaged."

Both documents set a lower limit, and the FAQ gives the reason. The FAQ explains that if an operating body, the part doing the pushing, stops near the operating position or the release position, "it may create chattering or bouncing and cause problems." Chattering contacts in a motor circuit would show up as a motor that stutters or won't start.

In a blender, the plunger's resting point is set by the jar, the lid and the linkage, so wear moves it. A worn lid tab, a slightly short replacement jar or a linkage that has slipped shortens the stroke, and the plunger can end up parked near the operating point. Following that FAQ's guidance, that's the zone where chattering starts, which fits a blender that starts on the second or third try or stops when the jar is nudged. An opposite fault, a stroke driven past the overtravel limit, loads the actuator against its stop on every use.

## Why a nudged jar doesn't always cut the motor

Movement differential gives the interlock a margin on the way back up. Once the contacts have changed at the operating point, they don't change back until the plunger rises to the release position, which sits above the operating point by the movement differential. The basic switch datasheet in the table above lists that gap as 0.2 mm max. for the pin-plunger version and 2.4 mm max. for the hinge-lever version.

A jar that lifts slightly while running keeps the motor enabled until the plunger passes the release position. The same gap means a stroke that ends just past the operating point leaves little room before the contacts let go. A separate article on movement differential in a micro switch covers the snap-back side in more detail, and micro switch pretravel covers the first leg of the stroke.

## Checking actuator travel without defeating the interlock

📌 **On safety:** *Unplug the blender before inspecting the base, and never hold, tape or prop the interlock to make the motor run. Ninja's BL682Q guide says "DO NOT try to defeat the interlock mechanism," and an exposed blade on a running base is the injury the interlock is there to prevent.*

Ninja's same guide states that "This appliance has no serviceable parts" and directs owners to return it to SharkNinja, so on that brand the checks open to an owner stop at the outside. Look for a cracked or worn lid tab, debris in the actuator opening on the base, and alignment marks that don't line up when the lid clicks. On the BL682Q, a power light that keeps flashing with everything seated means the base hasn't registered the pitcher and lid, so the tab-to-switch chain is the first suspect.

For a technician with the base open and unplugged, the questions follow the datasheet. Does the plunger travel past the operating point when the jar seats, and where does it stop compared with the rated overtravel? Does it rise back past the release position when the jar comes off? A meter across the switch terminals shows the contact change, and the method for testing a micro switch with a multimeter applies. Force, the other half of the same push, is covered in blender jar interlock micro switch operating force.

## FAQ

**How does a micro switch work?**
A spring mechanism holds the contacts in their resting state until the plunger reaches the operating point. Electronic Design describes the plunger reaching that point and the contacts snapping across. The contacts snap back only when the plunger rises past the release position.

**What is the actuation force for switches?**
Actuation force, which many datasheets list as operating force (OF), is the push needed to make the contacts change. The general-purpose basic switch datasheet in the table above gives 3.92 to 6.13 N for the pin-plunger version and 0.69 N max. for the long hinge lever. In a blender, the jar or lid linkage has to deliver at least that force at the end of its travel.

**What are the symptoms of a bad micro switch?**
In a blender interlock, the usual signs are a motor that won't start with the jar seated, or one that starts only after the jar is pressed or wiggled. The same signs come from a worn tab or a stroke that ends near the operating point, so check the jar and lid before blaming the switch. A meter test on the switch itself settles it.

## What to compare before replacing an interlock switch

Read the old switch's markings and find its datasheet, then compare its pretravel, overtravel and operating force with the replacement's. A replacement with less overtravel or a higher operating force can leave the plunger short of a reliable position on the same jar. If the figures match and the fault stays, the jar, lid and linkage are the next places to look.

Appliance switch makers often tune the switch to the appliance it goes into. [ZING EAR](https://www.zingear-switch.com/){: rel="nofollow noopener noreferrer" }'s home appliance line page says the company supports customized adjustment of operating force and terminal styles to suit the structure of different home appliances. That kind of tuning is why the pretravel and overtravel figures above belong to the specific switch fitted in your blender, not to blender switches in general.

## Sources

- Daniel Herzog, "Snap-Action Switches Still Rule The Roost," Electronic Design, 2012
- US Patent 6,513,966 B1, Electric blender with safety interlock arrangement (Dualit Limited)
- Ninja BL682Q Series Owner's Guide (QVC copy)
- ZING EAR, Home Appliance Micro Switch product line page: https://www.zingear-switch.com/home-appliance-micro-switch
