---
title: "What Is an Arcade Micro Switch? Where It Sits and How It Clicks"
description: "An arcade micro switch is a small snap-action switch under a button or joystick. See where it sits, how it clicks, and why only COM and NO get wired."
date: 2026-10-13 11:27:16 +0800
category: Applications
tags:
  - arcade micro switch
  - micro switches
  - Applications
author: editorial_team
seo_title: "Arcade Micro Switch: What It Is and How It Works"
last_updated: 2026-11-12
---

Under an arcade button or joystick sits a small switch that registers each press the player makes. Is that switch a special arcade part, or the same small switch found in appliances and machines? **An arcade micro switch is a standard snap-action micro switch, and what makes it an arcade part is the way it is mounted and wired, with push-on tabs and one of its three terminals left empty.** The switch's position under buttons and joysticks, the snap inside its case, its three terminals and the specifications that separate one arcade switch from another each get a section.

## Quick answer

An arcade micro switch is a small snap-action switch that needs very little force and closes a circuit when an arcade button or joystick moves. One arcade input board maker's installation notes tell builders to wire only the terminals marked normally open (NO) and common (COM), so the game sees a closed circuit only while the control is held.

## Where the switch sits in a button and in a joystick

In a push button, the switch sits under the button's plunger, the plastic stem that moves when you press the cap. The plunger moves straight down and presses the small button on top of the switch. One miniature snap switch datasheet calls that actuator type simply "button." A US arcade parts seller's listing says the light-force switch it sells was fitted for years by large arcade control makers to their push buttons and joysticks.

A joystick uses several switches around the base of the lever. One maker's datasheet for an arcade joystick lists four micro switches and a restrictor plate, a plate around the lever that blocks some directions, which sets the stick to 2-way, 4-way or 8-way movement. Each of the four switches faces one direction, and the bottom of the lever presses whichever switch it tilts toward. Because of that layout, a diagonal push leans on two neighboring switches at once, and the game reads the pair as a diagonal, such as up and left together.

Some joysticks mount their switches on a small circuit board instead of clipping them on one by one. A parts retailer's support page for a popular Japanese-style joystick says the switches are soldered to the board. The same page says a five-pin harness, a plug-in cable with one wire per pin, connects that board to the rest of the controller. Board mounting or clip-on mounting decides how a failed switch gets replaced, which the arcade joystick micro switch replacement guide covers step by step.

## What happens inside the switch when you press

The snap inside the switch comes from a spring. A limit switch maker's FAQ on snap-action contacts explains that the actuator, the switch's own small button, pretensions an over-center spring, and the spring tension operates the contact once a certain tension is reached. The steps inside the case run in this order:

1. The button's plunger pushes the switch's own small button down.
2. The switch's button bends the internal spring, and the spring stores energy.
3. At a set point, the spring passes its tipping point and flips.
4. The flip throws the moving contact, a metal piece wired to the common terminal, from one fixed contact to the other.

Electronic Design's article on snap-action switches adds that the common contact can't stop partway between the two fixed contacts. The limit switch FAQ notes that the release works the same way in reverse: the contacts stay put until the spring tension drops below a certain level, then snap back. The Electronic Design article also notes that once the plunger reaches the operating point, the common contact accelerates away without further plunger movement, so a slow press and a fast press end in the same quick flip.

## The three terminals, and why arcade wiring leaves one empty

Most arcade micro switches have three metal tabs. COM connects to the moving contact. NO connects to a fixed contact that stays apart from COM until the switch is pressed. Normally closed (NC) connects to a fixed contact that touches COM until the switch is pressed. "Normally" describes the switch at rest, with nothing pressing it. When the press flips the spring, COM leaves NC and lands on NO. The NO and NC micro switch explainer walks through the two contact states in more detail.

Arcade input boards expect a circuit that closes only while the player holds the control. A USB encoder board maker's installation notes say some switches have three connections, that you should only use the ones marked NO and COM, and that nothing goes on the NC tag. The same notes describe the failure that follows when the inputs go on NC instead: erratic joystick directions and "stuck" keys, because every untouched control reads as pressed.

The COM side of every switch usually shares one wire. Encoder installation notes also tell builders to daisy-chain one side of all switches, running a single wire from switch to switch, and to connect that chain to a ground (GND) terminal on the board. The arcade button micro switch wiring guide shows the full hookup.

📌 **On the empty tab:** *Leaving NC unconnected is normal for arcade wiring. The tab is still part of the switch, and some non-arcade uses do wire it.*

## What separates one arcade micro switch from another

Arcade micro switches look alike, but their datasheets differ on the points that change feel and fit. The light-force switch in that arcade parts listing carries a part number that its maker's miniature snap switch datasheet decodes. The number stands for a 10 A, single pole, double throw (SPDT) switch with light operating force, 4.8 mm quick-connect tabs and a plain button actuator. SPDT means one common terminal that switches between two others. The same datasheet lists the other options a switch in that series can carry:

| What differs | What one miniature snap switch datasheet lists | What it changes in an arcade control |
|---|---|---|
| Operating force (the press needed to flip the switch) | 45 to 400 cN, model dependent, with a choice of standard or light force | How hard the player has to press before the switch flips |
| Terminal width | Quick-connect tabs 4.8 mm (0.187 in) or 6.3 mm (0.250 in) wide | Which push-on connector fits the tab |
| Contact material | Gold cross point on the 0.1 A version, silver or silver alloy on higher ratings | How reliably the contacts carry a very small signal current |
| Electrical life | 50,000 operations at rated load and 85 °C | How many presses the switch is tested for at its full current rating |

Terminal width is the item that most often stops a swap. Wikipedia's FASTON terminal article lists the common push-on families by blade width in thousandths of an inch: 110 (about 2.8 mm), 187 (about 4.8 mm) and 250 (about 6.3 mm). One encoder maker lists the harness for its compact board with 4.8 mm switch connectors, or with 4.8 mm and 2.8 mm connectors for its own button panels, so both widths turn up in arcade builds. A connector made for one width won't grip a tab of another.

Life ratings need their conditions read alongside them. The 50,000 figure in that datasheet's table is for switching the full rated current, which runs from 0.1 A to 21 A across the series. One maker's USB encoder board takes its power from the USB port with no separate supply, so the current through each arcade switch is a signal current far below those ratings. A press count from a product listing that doesn't say which load, meaning the current switched during the test, it was measured at can't be compared with a datasheet figure that does.

Some product pages give both a mechanical-life count and an electrical-life count. Compare the two only when the test load and contact arrangement are stated; neither count by itself confirms that a switch fits an arcade control.

## FAQ

### What is the purpose of a micro switch?

A micro switch turns a small physical movement into an open or closed circuit. In arcade controls, that movement is a button press or a joystick push, and the circuit tells the input board which control the player used. Installation notes for a USB encoder board treat every button, joystick direction and coin switch the same way: one side to an input, the other to ground.

### What is inside a micro switch?

Inside the plastic case sit a small actuator button, a spring, one moving contact and two fixed contacts. A limit switch maker's FAQ describes the spring as an over-center mechanism that the actuator loads until it trips the contacts. The three outside tabs, COM, NO and NC, connect to the moving contact and the two fixed contacts.

### How to wire up a micro switch?

In an arcade control, connect the input wire to NO and the ground wire to COM, and leave NC empty, as a USB encoder board's installation notes instruct. With several controls, one ground wire can run from COM to COM across every switch. Check that the connector width matches the tab before pushing it on.

## What to check before you replace one

Start with the switch already in the control: read the markings on its case, measure the width of its metal terminal tabs, and note whether it clips on or is soldered to a board. Those three facts decide which replacement fits, and the operating force on the new switch's datasheet tells you whether the button will feel the same. For wiring the replacement, the guide to how one COM wire serves every button explains the shared ground.

Game controls are a regular market for micro switch makers. [ZING EAR](https://www.zingear-switch.com/){: rel="nofollow noopener noreferrer" } lists game control sticks among the markets on its home page. Whichever brand you choose, the contact arrangement, markings, tab width and operating force checks above still decide whether a replacement fits.

## Sources

- Electronic Design, Snap-Action Switches Still Rule The Roost
- Wikipedia, FASTON terminal
- Google AI Overview for "what is an arcade micro switch" (US, 2026-10-30)
- ZING EAR, home page (application markets list): https://www.zingear-switch.com/
