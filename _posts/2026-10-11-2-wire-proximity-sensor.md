---
title: "How Does a 2 Wire Proximity Sensor Work? Leakage, Voltage Drop and PLC Inputs"
description: "A 2 wire proximity sensor shares one pair of wires for power and signal, so it leaks current when off and drops volts when on. See how to wire and check it."
date: 2026-10-11 18:01:49 +0800
category: Basics
tags:
  - 2 wire proximity sensor
  - micro switches
  - Basics
author: editorial_team
seo_title: "How a 2 Wire Proximity Sensor Works: Leakage and Wiring"
last_updated: 2026-11-12
---

A 2 wire proximity sensor is wired like a limit switch, in series between the supply and the load, so it is often described as acting like a normal mechanical switch. Does it then behave like one once the power is on? **Only up to a point, because the sensor has no supply wire and must power itself through the load, so current trickles through when it is off and a few volts remain across it when it is on.** The sensing coil, the leakage and voltage-drop figures, the PLC input check and the limits on chaining sensors follow.

## Quick answer

A 2 wire proximity sensor is a non-contact sensor whose two wires carry both its power and its switching signal, so it always sits in series with a load. A sensor maker's proximity sensor guide states that the power and signal lines are combined and a load must always be inserted. Fed through that load, the sensor leaks a little current when off and holds a few volts when on.

## How a 2 wire proximity sensor detects metal, and why it needs power to do it

The same guide describes the inductive type this way: the sensor drives an AC magnetic field from a detection coil, and a metal object in that field develops eddy currents. The guide explains that those eddy currents cause a magnetic loss, which shows up as a change in the coil's impedance. The sensor's electronics detect that change and switch the output. The output itself is a semiconductor, and the same guide notes that proximity sensors use semiconductor outputs, so there are no contacts to wear out.

Contact is the main split from a micro switch or other contact-based switch. The guide contrasts the two directly: a limit switch detects an object by touching it, while a proximity sensor detects it electrically. A micro switch also needs no power to work, and its contacts can be checked with an ohmmeter on the bench. A proximity sensor's coil and output stage do nothing until they're powered, and in a 2 wire version that power can only arrive through the load.

That technical guide also counts magnet-operated sensors as proximity sensors, but those use a reed switch with real contacts, so the powered-electronics point applies to the inductive and capacitive types.

## Why a 2 wire sensor leaks current when off and drops voltage when on

The cause sits in the wiring. An automation maker's application note on digital inputs for 2-wire and 3-wire sensors explains that a 2-wire sensor carries its signal and its supply on the same wire. In practice the supply, the sensor and the load then form one series loop. To keep the sensor's electronics alive, the note says, a permanent minimum current, called the quiescent or residual current, has to flow through the wires and through whatever input or coil the sensor drives. Sensor datasheets list that off-state current as the leakage current.

The chain runs like this:

1. The sensor has no separate supply, so its own detection coil and electronics take their power from the loop that also contains the load.
2. In the off state, the sensor still needs a little power, so a small current keeps flowing through the load.
3. In the on state, the sensor still needs a little voltage across its own terminals to keep running, so it never drops all the way to zero volts. One sensor datasheet calls this the residual voltage, and another calls it the voltage drop.
4. Also in the on state, the sensor needs enough current through the load to power itself. One inductive sensor catalog defines this minimum output current as the smallest load current required for the switch to function when on.

The application note sets out the design limit that follows from step 2: the residual current must stay below the switching threshold of the coil or input that follows, while still keeping the sensor working. A PLC input or relay that switches on at a lower current than the sensor leaks can't settle into its off state.

Here's what those three numbers look like on two real datasheets. The figures below come from the datasheet for one standard inductive sensor series (Datasheet A, DC 2-wire models) and from the product data for a second inductive sensor that can run in 2-wire mode (Datasheet B).

| Parameter | What it limits | Datasheet A: standard inductive sensor, DC 2-wire models (12 to 24 VDC) | Datasheet B: inductive sensor in 2-wire operation (10 to 30 VDC) |
|---|---|---|---|
| Leakage current (off state) | Whether the load or input can stay off | 0.8 mA max. | 0.5 mA max. |
| Residual voltage / voltage drop (on state) | How much voltage the load actually gets | 3 V max. at 100 mA load, 2 m cable | 2.8 V max. |
| Load current range (on state) | Smallest and largest current the load may draw | 3 to 100 mA | 2 mA min., 100 mA max. |

The two sets of figures sit close together, but they belong to two specific sensors, so the datasheet for the exact part in front of you is the number to use. Datasheet A also flags an outlier: its models without polarity have a 5 V residual voltage, and the catalog warns you to check that against the connected device, such as a PLC's ON voltage.

AC 2-wire sensors leak more. In the same series datasheet (Datasheet A), the AC 2-wire models (24 to 240 VAC) list 1.7 mA max. leakage current, roughly twice the DC 2-wire figure.

## How to check a 2 wire proximity sensor against a PLC input

Datasheet A gives a separate procedure for one kind of load, a PLC input, because that's where leakage and residual voltage cause trouble. If the sensor's leakage current is larger than the current the input needs to leave its guaranteed off range, the input is no longer sure to read "off" with no target in front of the sensor.

That datasheet sets out three conditions for connecting a DC 2-wire sensor to a PLC:

| Condition | In plain terms |
|---|---|
| PLC ON voltage ≤ supply voltage − sensor residual voltage | With the sensor on, the input still gets enough voltage to read "on" |
| PLC OFF current ≥ sensor leakage current | With the sensor off, its leakage stays below what the input treats as "off" |
| Sensor minimum load current ≤ PLC ON current ≤ sensor maximum load current | The input draws enough current to keep the sensor powered, and no more than the sensor can carry |

The datasheet works one example through with one of its DC 2-wire normally open models on a 24 V supply. In that example, the PLC's OFF current, the largest current at which the input still reads off, is 1.3 mA, above the sensor's 0.8 mA leakage. The datasheet then calculates the PLC's ON current at roughly 4.5 mA from a 20.4 V supply, the sensor's 3 V residual voltage, a 4 V drop inside the PLC and a 3 kΩ input impedance. The calculated 4.5 mA is above the sensor's 3 mA minimum load, so the connection works.

The same datasheet adds that if a PLC's input specifications don't list an OFF current, you should take it to be 1.3 mA.

The PLC side has its own classes. IEC 61131-2, the international standard for programmable controller equipment, sorts 24 VDC current-sinking inputs, the kind that take current in from the sensor, into Type 1, Type 2 and Type 3. The application note cited above, written against the EN edition of that standard, describes them like this:

| Input type | Intended for, per the application note | Current an input needs to leave its off range, per the note's table |
|---|---|---|
| Type 1 | Mechanical contacts and 3-wire sensors | 0.5 mA |
| Type 2 | 2-wire sensors with semiconductor outputs | 2 mA |
| Type 3 | 2-wire and 3-wire sensors, with lower power use | 1.5 mA |

The note states that Type 1 inputs suit 2-wire sensors only to a very limited extent or not at all. Reading the table against the 0.8 mA leakage in Datasheet A shows why. That leakage sits above the 0.5 mA figure the note lists for Type 1, so a Type 1 input may sit in its undefined transition band. The same leakage is below the Type 2 and Type 3 figures.

## Wiring 2 wire sensors in series or in parallel

Two or more 2 wire sensors can share one load, but each arrangement runs into either the residual voltage or the leakage current. One sensor maker's FAQ on series and parallel connections of proximity sensors gives the limits for DC 2-wire models.

**In series (an AND circuit)**, every sensor that's on keeps its residual voltage across itself, and that voltage is taken away from the load. The FAQ's rule is that the supply voltage minus the number of sensors times the residual voltage must stay at or above the voltage the load needs to operate.

Taking the 3 V maximum residual voltage that Datasheet A lists, three sensors in series on a 24 V supply would still leave the load at least 15 V in the worst case. The FAQ also warns that sensors in series may not get their rated supply, so indicators may not light correctly and error pulses of about 1 ms may appear.

**In parallel (an OR circuit)**, every sensor that's off still passes its leakage current, and the currents add up in the load. The FAQ's rule is that the number of sensors times the leakage current must stay at or below the load's reset current, the current below which the load drops out. The FAQ's worked example states a maximum of four sensors when the load is a general-purpose relay with a 24 VDC coil. For AC 2-wire models, the same FAQ says parallel connection is generally not possible, and that the combined leakage makes reset failures frequent.

## How to connect and test a 2 wire proximity sensor

Turn off the supply before you touch the wiring. The proximity sensor technical guide warns that if a 2-wire sensor's leads are connected straight across the power line with no load, its internal elements may be damaged. The no-load rule is the practical difference from wiring a 3-wire sensor, whose separate supply leads do go directly to the supply.

1. **Find the polarity.** Datasheet A shows its DC 2-wire leads as brown and blue, and lists both polarized models and models with no polarity. On a polarized model, follow the wiring diagram on the datasheet for which lead faces +V.
2. **Put the load in the loop.** The same datasheet notes that the load can be connected on either the +V side or the 0 V side. A PLC input, relay coil or other load goes in series with the sensor.
3. **Check the load against the table above.** The load's ON current has to fall inside the sensor's load current range, and the load's off threshold has to sit above the sensor's leakage current.
4. **Power up and watch the sensor's operation indicator** as a metal target approaches and moves away.

Testing follows from the same chain. Because the output is a semiconductor that only switches when powered, an unpowered continuity check of the kind used on a micro switch's normally open and normally closed terminals says little about a 2-wire sensor. A powered check says more. With the sensor on, the voltage across its two leads should be no more than the residual voltage on its datasheet, the few volts the sensor keeps for itself. With it off, most of the supply voltage should appear across the sensor, because the small leakage current makes only a small drop across the load.

📌 **On a PLC input that won't turn off:** *Compare the sensor's leakage current with the input's OFF current before suspecting the sensor. A leakage figure above the OFF current explains the symptom without any fault in the sensor.*

## FAQ

### What's the difference between 2-wire and 3-wire?

A 2-wire sensor carries its power and its signal on the same two wires and sits in series with the load. The automation maker's application note explains that a 3-wire sensor has a separate supply, so the input it drives doesn't have to carry the sensor's operating current. Datasheet A from the table above lists the trade-off from the other side: its DC 2-wire models need about two thirds of the wiring of DC 3-wire models. Their own current consumption, the same datasheet says, is less than 10% of the 3-wire figure.

### How to check two wire proximity sensor?

Check it powered and wired to its load. Datasheet A lists a 3 V maximum residual voltage for its DC 2-wire models, so the voltage the sensor keeps across itself when switched on should not exceed the figure on your sensor's datasheet. Watch the operation indicator as you move a metal target in and out of the sensing range.

### What is the output of a proximity sensor?

The proximity sensor technical guide cited above states that proximity sensors switch with semiconductor outputs instead of contacts. The output still has a normally open (NO) or normally closed (NC) mode: Datasheet A lists one group of its models as NO and another as NC, with the state described for a target approaching the sensor.

### Two-wire sensors should typically be connected to which terminals in an electrical system?

One lead goes toward the supply and the other goes to the load, so the sensor and load form one series loop. Datasheet A shows the load on either the +V or the 0 V side. On a PLC, the automation maker's application note points 2-wire sensors to inputs of Type 2 or Type 3 under IEC 61131-2, which tolerate more off-state current than Type 1.

## What to read on a 2 wire sensor's datasheet before you wire it

Look for three lines: the leakage current that flows when the sensor is off, the residual voltage it keeps when on, and the load current range it needs. Then hold them against the OFF current, ON voltage and ON current of the input or coil it will drive. If any of the three falls outside, the input type or the sensor type has to change before the wiring does.

## Sources

- IEC 61131-2:2017, Industrial-process measurement and control: Programmable controllers, Part 2: Equipment requirements and tests (IEC webstore). https://webstore.iec.ch/publication/31007
