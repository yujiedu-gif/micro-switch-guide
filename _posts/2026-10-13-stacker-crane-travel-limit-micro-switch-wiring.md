---
title: "Stacker Crane Travel Limit Micro Switch Wiring: COM, NO, NC and the Fail-Safe Contact"
description: "Wire a stacker crane travel limit micro switch through COM and NC so a cut wire also stops travel, and know why a welded contact needs positive opening."
date: 2026-10-13 11:27:16 +0800
category: Applications
tags:
  - stacker crane travel limit micro switch wiring
  - micro switches
  - Applications
author: editorial_team
seo_title: "Stacker Crane Travel Limit Micro Switch Wiring: COM, NO, NC"
last_updated: 2026-11-12
---

A stacker crane runs along a rail between storage racks, and a switch near each end of the rail tells the drive when the crane has gone far enough. The usual wiring answer for a travel limit is the normally closed contact, so a cut wire stops the crane the same way the switch does. **Normally closed wiring catches a broken wire, but a contact welded shut keeps the circuit closed, and only a switch built to force its contacts apart can open it.** The switch terminals, the stop-circuit contact, the welded-contact gap, the rating check and the test after wiring follow in order.

## Quick answer

On a stacker crane travel limit, the micro switch (also called a snap-action switch) is wired through its common (COM) and normally closed (NC) terminals, in series with the circuit that permits travel. Galil's application note on limit inputs explains why: a normally closed input also trips when a wire opens or disconnects, which makes the input fail-safe.

The NC contact does not catch every fault. A welded contact or a short across the switch wiring holds the circuit closed. Safety-rated limit switches add a mechanism called positive opening for the welded contact; the short needs attention in how the cable is routed and protected.

## Lock out the crane before you open the switch

The US lockout rule, OSHA 29 CFR 1910.147, covers servicing and maintenance where an unexpected start or release of stored energy could injure someone. Rewiring a travel limit on a stacker crane falls inside that scope, because the crane can move under power while your hands are near the rail.

The same rule draws a line that matters for limit wiring. OSHA defines an energy isolating device as a mechanical device that physically blocks energy, such as a disconnect switch or circuit breaker, and states that push buttons, selector switches and other control circuit devices do not qualify. A travel limit switch, an emergency stop button and a PLC stop command all sit in the control circuit, so none of them counts as isolation.

OSHA's sequence ends with verification of isolation, step (d)(6), before work begins. Where you later have to power the crane to test the switch, paragraph (f)(1) of the rule sets the order: clear tools and people, remove the locks, energize and test, then de-energize and relock before work continues.

## Find COM, NO and NC on the switch

A micro switch with three terminals is single pole, double throw (SPDT): one common (COM) terminal that switches between a normally open (NO) terminal and a normally closed (NC) terminal. A switch maker's training module on electromechanical switch technology describes the two states: a normally open switch carries no current at rest and closes when actuated, while a normally closed switch conducts at rest and opens when actuated.

"Normally" refers to the switch at rest, with nothing pressing the actuator. On a crane, the rest state is the crane anywhere short of the limit, so COM to NC is closed during normal travel and opens when the crane's trip cam presses the lever. The meaning has nothing to do with the state the circuit spends most of its time in.

Terminal markings vary between makers, so read the label on the switch body or its datasheet before connecting anything. A continuity check with the switch at rest settles any doubt: COM to NC reads closed and COM to NO reads open.

Figure 1. The same three terminals give a closed path through NC at rest and through NO when the crane's cam presses the actuator.

On a crane rail, the terminals are usually behind a housing cover. A general-purpose basic switch datasheet warns that switches are generally not built to resist water and calls for a protective cover where oil, water or dust can reach them. For a travel limit on a crane rail, that points to an enclosed limit switch, with the snap-action element sealed inside a housing and driven by an external lever or plunger. Sealed elements are also made for this kind of duty: ZING EAR rates the [ZINGEAR G5W11-WZ200-W2](https://www.zingear-switch.com/zingear-micro-switch-g5w11-wz200-w2-explosion-proof-micro-switch.html){: rel="nofollow noopener noreferrer" }, a plunger switch in its industrial heavy-duty line, at IP67 and lists travel limiting on industrial dust removal equipment among its uses.

## Why the stop circuit uses the NC contact

The NC contact is wired in series with the circuit that permits travel, whether that circuit is a safety relay input, a drive enable or a PLC input. As long as the crane is short of the limit, current flows through COM and NC. When the cam presses the actuator, NC opens, the circuit loses its signal and the drive stops travel in that direction.

Galil's note frames this as fail-safe behavior: the input reacts the same way to an open switch and to a disconnected wire. An NO contact is already open at rest, so with NO wiring a broken wire looks exactly like a crane that has not reached the limit, so the fault stays hidden until the crane drives past the switch.

| Event | NC contact in series (COM to NC) | NO contact (COM to NO) |
|---|---|---|
| Crane short of the limit | Circuit closed, travel allowed | Circuit open, controller reads "not at limit" |
| Crane at the limit | Circuit opens, travel stops | Circuit closes, controller reads "at limit" |
| Wire cut or terminal loose | Circuit opens, travel stops | Circuit stays open, limit can no longer be seen |
| Contacts welded shut | Circuit stays closed, travel continues | Circuit stays closed, controller reads "at limit" |
| Short across the two switch wires | Circuit stays closed, travel continues | Circuit closed, controller reads "at limit" |

A welded contact and a shorted cable both leave the NC path closed, so NC wiring alone does not finish the job.

📌 **On NO contacts:** *An NO contact on the same switch can still feed a separate PLC input that reports the limit to the operator screen. That signal is information; the stop itself should come from the NC path.*

## Where NC wiring stops protecting the crane

A standard micro switch opens its NC contact with a spring. If an overload has welded the contact, the spring may not be strong enough to pull it apart, and the circuit stays closed while the crane runs on. A short between the two wires feeding the switch has the same effect, because current flows around the contact.

Safety-rated limit switches answer the welded-contact case with positive opening, also called direct opening action. One limit switch maker's general technical data describes the requirement. For the part of the travel that separates the contacts, there must be a positive drive with no resilient member, such as a spring, between the moving contact and the point where force is applied. In plain terms, the actuator pushes the contact open through solid parts, so a stuck contact still gets moved. The same document notes that positive opening applies to NC contacts only and that such switches carry a dedicated symbol on the housing.

A safety-products knowledge base from another switch maker describes the result: the actuator's own force pushes a welded contact open. The description uses a 10 N force on the contacts to stand in for the weld, and states that once forced open, the gap withstands the impulse voltage stipulated in EN 60947-5-1. The international version of that standard is [IEC 60947-5-1](https://webstore.iec.ch/en/publication/65935){: rel="nofollow noopener noreferrer" }, whose current fifth edition was published in 2024.

Because positive opening requires no spring in the opening path, a general-purpose micro switch that opens its NC contact by spring alone does not meet it. Only switches marked and documented for positive opening do.

Stacker cranes built to the European standard for this equipment, [EN 528:2021+A1:2022](https://standards.iteh.ai/catalog/standards/sist/5c5a5903-9339-41f3-90b7-9e39f0b2d24a/sist-en-528-2021a1-2022){: rel="nofollow noopener noreferrer" }, sit inside a wider set of travel controls. The standard's table of contents gives the speed reducing system (clause 4.5.2) and limitation of travel (clause 4.5.3) separate clauses, and adds verification of the mechanical limits of travel as a test (clause 5.1.4). Which physical switch handles slowdown and which one is the final limit is set in the crane maker's electrical drawings, and those drawings decide which contact each switch uses.

## Check the switch rating against the control circuit

If the crane's control circuit runs on DC, a micro switch's DC rating is the one that applies, and it can sit far below the AC rating. The general-purpose basic switch datasheet cited above shows the gap: for a resistive load, the switch is rated 20 A at 250 VAC, 6 A at 30 VDC and only 0.5 A at 125 VDC. The same datasheet lists lower values again for inductive loads such as relay and contactor coils.

A relay coil in the stop circuit is an inductive load, so the inductive DC column is the one to read. If the switch's rating at your control voltage is lower than the coil current, the contact can arc and weld, which brings back the failure that NC wiring cannot see.

## Set the actuator travel and test the wiring

The cam or ramp on the rail has to press the actuator far enough to switch reliably without crushing it. Overtravel (OT) is how far the actuator may keep moving after the contacts switch. The same basic switch datasheet says the actuator must not go past its permissible OT position, and that the cam should push the actuator past the switching point by 70% to 100% of the rated OT.

With the crane locked out, test the switch itself first:

1. Disconnect one wire from the switch so the rest of the circuit doesn't affect the reading.
2. Set a multimeter to continuity and check COM to NC with the actuator at rest. It should read closed.
3. Press the actuator by hand through its full stroke. COM to NC should open with an audible snap, and COM to NO should close.
4. Release the actuator slowly. NC should close again a little before the actuator reaches its rest position, because a snap-action switch resets at a slightly different point than it trips.
5. Reconnect the wire and confirm the terminal screws are tight and the wire ends sit fully under the clamps.

A powered test then follows the crane maker's commissioning procedure and the OSHA (f)(1) sequence. EN 528:2021+A1:2022 lists verification of the mechanical limits of travel among its required examinations, so a crane built to that standard has a documented way to prove each limit stops the crane.

## Wiring faults that show up on a travel limit

| Symptom | Likely cause in the wiring | What to check |
|---|---|---|
| Crane won't travel in one direction, limit not reached | NC path open: loose terminal, broken wire, or switch stuck in the actuated state | Continuity COM to NC at rest; wire continuity back to the controller |
| Crane passes the limit without stopping | Wiring landed on NO instead of NC, welded NC contact, or a jumper left across the switch | Which terminal each wire is on; COM to NC must open when pressed |
| Limit trips at random during normal travel | Loose terminal or a cable flexing at the moving carriage | Terminal tightness; cable condition where it bends |
| Controller shows the limit but the crane keeps moving | The switch reports to a PLC input only and is not in the stop circuit | Crane electrical drawings for where the stop signal comes from |

A jumper across a travel limit defeats the protection completely. Remove any temporary jumper before the crane goes back into service, and never use one to keep a crane running past a faulty switch.

## FAQ

### How to tell if a switch is NO or NC?

Check the markings next to the terminals first, because most limit switches label them COM, NO and NC or show a small contact diagram. If the markings are worn, use a multimeter on continuity. One terminal reads closed to a second terminal at rest and to the third when the actuator is pressed: that terminal is COM. The one it connects to at rest is NC, and the one it connects to when pressed is NO.

### What are the different types of limit switch sensors?

On cranes the two common families are mechanical limit switches and inductive proximity sensors. A mechanical limit switch has a snap-action switch inside that a cam or ramp physically presses, which is the type this wiring guide covers. A proximity sensor detects a metal target without touching it and has its own wiring scheme and supply terminals, so the COM, NO and NC logic above doesn't carry over directly.

### Should a travel limit switch be wired normally open or normally closed?

For the stop function, wire it normally closed. Galil's application note describes NC inputs as fail-safe because they also trip when a wire opens. An NO contact can still serve as a status signal to a PLC or display.

## What to check next on your own crane

Pull the crane's electrical drawings and confirm that every travel limit in the stop path uses the NC contact. Then look at the switch body or datasheet for the positive opening symbol, and compare the switch's DC inductive rating with the coil it switches. Related guides cover what NO and NC mean on a micro switch, how to test a micro switch with a multimeter, why micro switch contacts weld and what causes a stacker crane home position switch to fail.

Some micro switch makers build a separate line for this kind of machinery. [ZING EAR](https://www.zingear-switch.com/){: rel="nofollow noopener noreferrer" }, for instance, lists lifting equipment among the scenarios its heavy-duty industrial micro switches are developed for, alongside heavy production lines and automated machine tools. Whichever maker supplies the part, the NC wiring, positive opening and DC rating checks above still decide whether it belongs in the crane's stop circuit.

## Sources

- OSHA, 29 CFR 1910.147, The control of hazardous energy (lockout/tagout)
- Galil Motion Control, Application Note #1436, Using Normally Closed Switch for Inputs (2014)
- [IEC 60947-5-1:2024, Low-voltage switchgear and controlgear, Part 5-1: Control circuit devices and switching elements, Electromechanical control circuit devices (edition 5.0), also published in Europe as EN 60947-5-1](https://webstore.iec.ch/en/publication/65935){: rel="nofollow noopener noreferrer" }
- [EN 528:2021+A1:2022, Rail dependent storage and retrieval equipment, Safety requirements for S/R machines (preview with table of contents)](https://standards.iteh.ai/catalog/standards/sist/5c5a5903-9339-41f3-90b7-9e39f0b2d24a/sist-en-528-2021a1-2022){: rel="nofollow noopener noreferrer" }
- ZING EAR, Industrial Heavy-duty Micro Switch product line page: https://www.zingear-switch.com/industrial-heavy-duty-micro-switch
- ZING EAR, ZINGEAR G5W11-WZ200-W2 sealed plunger micro switch product page: https://www.zingear-switch.com/zingear-micro-switch-g5w11-wz200-w2-explosion-proof-micro-switch.html
