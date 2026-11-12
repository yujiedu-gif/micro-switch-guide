---
title: "How to Test a Bucket Elevator Guard Interlock Micro Switch: Meter Check, Control Check and Lockout"
description: "Test a bucket elevator guard interlock micro switch in two parts: a meter check of its NC contacts under lockout, then a check that the elevator won't start."
date: 2026-10-13 11:27:16 +0800
category: Troubleshooting
tags:
  - how to test a bucket elevator guard interlock micro switch
  - micro switches
  - Troubleshooting
author: editorial_team
seo_title: "How to Test a Bucket Elevator Guard Interlock Micro Switch"
last_updated: 2026-11-12
---

When a bucket elevator's inspection door or guard carries an interlock switch, opening it should stop the belt, buckets and drive inside the casing. Testing that switch usually means a meter check of its contacts with the power locked out, followed by a live check that the elevator stops or won't start with the guard open. **A pass on both checks proves the interlock works, and a bucket elevator manufacturer still treats locking out the motor, not the interlock, as the protection for anyone who opens the casing.** The lockout, the type of switch, the meter check, the control check and what a failed result means follow in that order.

## Quick answer

To test a bucket elevator guard interlock micro switch, lock out the elevator, then check the switch's normally closed (NC) safety contacts with a multimeter: closed with the guard shut, open with the guard open. Then, under the lockout rule's testing sequence, confirm from outside the guard that the elevator's control refuses to start while the guard is open.

The micro switch inside the interlock, also called a snap-action switch, is only one part of the safety function. KWS Manufacturing's bucket elevator manual states that other devices should not be used as a substitute for locking out the power before guards or covers are removed.

## Lock out the elevator before the first check

KWS's Bucket Elevator Safety, Operation and Maintenance Manual (revision 1, issued 2013) covers opening the elevator for inspection, cleaning or observation. The manual says the motor is then to be locked out electrically so that nobody can restart it, however remote from the area. The same manual says locking out the power gives the only real protection against injury, and warns that secondary devices can give employees a false sense of security. In OSHA's terms below, the lock goes on an energy isolating device such as the motor's disconnect switch.

The US lockout rule, OSHA 29 CFR 1910.147, matches that view. It defines an energy isolating device as a mechanical device that physically blocks energy, such as a disconnect switch, and states that push buttons, selector switches and other control circuit devices are not energy isolating devices. A guard interlock switch is a control circuit device, so an open guard doesn't mean the elevator is isolated.

The KWS manual also places the owner's obligations under ANSI B20.1, the US safety standard for conveyors. The current edition is [ASME B20.1-2024](https://knowledge.bsigroup.com/products/safety-standard-for-conveyors-and-related-equipment-2){:rel="nofollow"}, published in September 2024.

## Identify the interlock switch before you test it

A guard interlock can be a limit switch with a lever or plunger that the guard presses, a switch with a separate actuator fixed to the door, or a non-contact switch. A meter check of contacts applies to the first two kinds; a non-contact switch is checked by its maker's procedure instead.

On a contact switch, look on the housing or datasheet for the positive opening symbol defined in [IEC 60947-5-1](https://webstore.iec.ch/en/publication/65935){:rel="nofollow"}. Banner's datasheet for its SI-LM40 safety limit switch describes what the symbol promises: the NC safety contacts are forced open, without the use of springs, when the actuator moves from its home position. ABB's general technical data for limit switches adds that positive opening applies to NC contacts only.

A general-purpose micro switch opens its NC contact with a spring, and a spring may not be strong enough to pull a welded contact apart, so it lacks that guarantee. If you find one fitted to a personnel guard, flag it for the person responsible for the machine's safety design rather than treating the test result as the whole answer.

Note the contact arrangement printed on the switch. Omron's D4N-2220 safety limit switch, for example, has two NC contacts, and each one needs its own check.

## Inspect the switch and actuator

Banner's SI-LM40 datasheet lists checks a designated person should make at each shift change or machine setup:

- breakage of the switch body or actuator
- good alignment and full engagement of the actuator
- confirmation that the safety switch isn't being used as an end stop
- loosening of the switch or actuator mounting hardware
- confirmation that no hazard can be reached through an opened guard before motion has stopped

The same datasheet adds periodic checks for a qualified person, among them contamination in the wiring chamber and the condition of the electrical wiring. A bucket elevator handling grain, cement or other dusty material is a place where those checks matter, because dust can build up inside a switch housing whose cover or cable gland has loosened.

## Check the contacts with a multimeter

With the elevator locked out and the absence of power verified:

1. Open the switch cover and disconnect one wire from the contact you are testing, so other parts of the circuit don't affect the reading.
2. Set the multimeter to continuity and connect it across that NC contact.
3. Close the guard fully. The meter should read closed.
4. Open the guard slowly. The meter should change to open, and it should stay open with the guard fully open.
5. Repeat for each NC contact on the switch, and for any normally open (NO) auxiliary contact, which should read the opposite way.
6. Reconnect the wires, tighten the terminals and refit the cover and cable gland.

A reading that flickers as the guard moves, or that only changes when the guard is pushed hard, points to a worn contact, a misaligned actuator or a guard that no longer reaches the switch properly.

On a positive-opening switch, the guard also has to move the actuator far enough to force the contacts open. Omron's datasheet for the D4N-2220 lists a direct opening travel of 50° min. and a direct opening force of 20 N min. for its roller lever. If the guard opens but the lever swings less than the direct opening travel listed for your switch, a healthy contact still reads open today, but a contact that welds later would not be forced apart.

Figure 1. With the guard shut the NC safety contact reads closed; opening the guard moves the actuator through its direct opening travel and the contact reads open.

## Check that the control refuses to run with the guard open

The meter check proves the switch. A second check proves that the elevator's control acts on it, and that check needs power. OSHA's lockout rule sets the sequence for testing in paragraph (f)(1). Clear tools and materials, make sure everyone is clear, remove the locks, energize and test, then de-energize and relock before work continues.

Run the check from outside the guarded area, with nobody reaching into the casing:

1. With the elevator stopped, open the guard.
2. Look at the safety relay indicators or the controller's input display. The input for that guard should show open.
3. Give a start command from the normal operator station. The elevator should not start.
4. Close the guard. If the circuit uses a safety relay with a manual reset, the elevator should still not start until the reset button is pressed.

Whether a guard may ever be opened with the elevator running, as part of a test, is set by the plant's written procedure and the qualified person who owns it. The switch test itself doesn't need the elevator running.

Where several guards are wired in series, test each guard on its own. Banner's datasheet warns that a series connection of multiple safety interlock switches is not a Category 4 application under [ISO 13849-1](https://www.iso.org/standard/73481.html){:rel="nofollow"}, because a single failure can be masked or not detected at all. Opening two guards at once can hide a welded contact on one of them, because the other guard's open contact already breaks the circuit.

## What a failed test means

| Result | Likely cause | Next step |
|---|---|---|
| NC contact reads open with the guard closed | Actuator not reaching the switch, broken contact, loose wire | Check alignment and engagement, then retest; replace the switch if the contact stays open |
| NC contact reads closed with the guard open | Welded contact, actuator jammed in the pressed position, or a jumper in the circuit | Take the elevator out of service and replace the switch; remove any jumper |
| Meter passes, but the elevator starts with the guard open | Wiring fault, a bypass in the control panel, or a control logic fault | Treat as a failed safety function; the elevator stays out of service until the control circuit is corrected |
| Reading flickers as the guard moves | Worn contacts, loose actuator, contamination in the housing | Clean or replace, then retest |

Banner's datasheet tells users not to attempt repairs on its safety switch and to return a defective unit, and Omron's European knowledge base describes the direct opening mechanism as the way a welded contact gets forced open. Rule out a jammed actuator and any jumper first. After that, a switch whose NC contact reads closed with the guard open has failed at the job that mechanism exists for, and replacement is safer than adjustment.

Never tape, wedge, jumper or use a spare actuator to hold an interlock closed. Banner's datasheet warns against using spare actuators to bypass a safety switch, and KWS's manual warns that relying on a secondary device such as an interlock, instead of lockout, can end in serious injury if that device fails.

## FAQ

### What is a safety interlock switch?

A safety interlock switch is a switch that a guard, door or cover operates, wired so that opening the guard stops the hazardous motion or prevents it from starting. On a machine guard it typically uses NC contacts that open when the guard opens. Banner's SI-LM40 datasheet describes the positive-opening version: the contacts are forced open without relying on springs when the actuator leaves its home position.

### Can a guard interlock replace lockout on a bucket elevator?

No. KWS's bucket elevator manual says other devices should not be used as a substitute for locking out the power before guards or covers are removed. OSHA's lockout rule likewise excludes control circuit devices, which include interlock switches, from the devices that isolate energy.

### How often should a guard interlock switch be checked?

Banner's SI-LM40 datasheet calls for a designated person to check the switch at each shift change or machine setup. A qualified person makes deeper checks on a schedule set by the environment and how often the switch operates. Your plant's procedure and the elevator maker's manual set the schedule for your own equipment.

## Keep the test record with the elevator

Write down the guard tested, the date, both meter readings (guard closed and guard open), whether the elevator refused to start and who performed it. A record that shows a contact reading closed with the guard open, even once, is the signal to replace that switch. Related guides cover how to test a micro switch with a multimeter, the safety function of a micro switch, operating force on a dock leveler guard interlock and NO and NC terminals on a bucket elevator end-of-stroke switch.

Bucket elevators run in dusty plants, a condition industrial switch makers design for. [ZING EAR](https://www.zingear-switch.com/){:rel="nofollow"} describes its heavy-duty industrial micro switches as designed for workshop conditions with high dust and continuous operation. Dust tolerance doesn't replace the lockout and test steps above, which apply to any guard switch on the elevator.

## Sources

- KWS Manufacturing, Bucket Elevator Safety, Operation & Maintenance Manual (Revision 1, issued 5/18/2013)
- OSHA, 29 CFR 1910.147, The control of hazardous energy (lockout/tagout)
- [ASME B20.1-2024, Safety Standard for Conveyors and Related Equipment (BSI Knowledge listing: current, published 10 Sep 2024)](https://knowledge.bsigroup.com/products/safety-standard-for-conveyors-and-related-equipment-2){:rel="nofollow"}
- Banner Engineering, SI-LM40 Series Safety Limit Switch datasheet (P/N 50159 Rev. H)
- ABB, Limit switches: General technical data (1SXU000023C0202)
- Omron, D4N-2220 Safety Limit Switch, ratings and performance (product page, as of October 23, 2025)
- Omron Europe knowledge base, What is a direct opening mechanism (forcibly opened contacts)?
- [IEC 60947-5-1:2024, Low-voltage switchgear and controlgear, Part 5-1: Control circuit devices and switching elements, Electromechanical control circuit devices](https://webstore.iec.ch/en/publication/65935){:rel="nofollow"}
- [ISO 13849-1, Safety of machinery, Safety-related parts of control systems, Part 1: General principles for design (cited in Banner's datasheet)](https://www.iso.org/standard/73481.html){:rel="nofollow"}
- ZING EAR, Industrial Heavy-duty Micro Switch product line page: https://www.zingear-switch.com/industrial-heavy-duty-micro-switch
