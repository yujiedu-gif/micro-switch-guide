---
title: "How Does an Aircraft Landing Gear Monitor Micro Switch Work? Squat Switches, Limit Switches and Proximity Sensors"
description: "A landing gear micro switch is a snap-action switch moved by the strut or gear leg. How squat switches, limit switches and proximity sensors do the job."
date: 2026-10-13 13:45:35 +0800
category: Applications
tags:
  - how does a aircraft landing gear monitor micro switch work
  - micro switches
  - Applications
author: editorial_team
seo_title: "Aircraft Landing Gear Monitor Micro Switch: How It Works"
last_updated: 2026-11-12
---

On a retractable-gear airplane parked on the ramp, the gear handle will not go to UP, and on final approach three green lights show that each wheel is down and locked. Small switches mounted on the landing gear produce both results. **One switch reads the shock strut to tell the aircraft whether its weight is on the wheels, while a separate set reads each gear leg to report where that leg has stopped.** The snap mechanism inside the switch, the squat switch circuit, the limit switch circuit and the proximity sensors used on many aircraft are covered below in that order.

## Quick answer

A landing gear micro switch, also called a snap-action switch, is a small spring-loaded switch that a moving gear part presses or releases, so its contacts flip at one set point in the gear's travel. The FAA's Aviation Maintenance Technician Handbook lists landing gear among the moving parts whose position micro switches detect.

In the handbook's description, those switches do two jobs on landing gear. A squat switch on the shock strut tells other systems whether the aircraft is on the ground. Limit switches in the wheel wells tell the gear motor and the cockpit lights when each leg is fully up or fully down.

## What the FAA handbook means by a micro switch

The FAA's Aviation Maintenance Technician Handbook, Airframe (FAA-H-8083-31B), the textbook the agency publishes for mechanics preparing for certification, describes micro switches in its electrical chapter. The handbook states that micro switches "require very little pressure to activate," that they're spring loaded, and that their contacts return to the normal position once the pressure is removed. The same passage names landing gear, flaps and spoilers as examples of moving parts whose position these switches detect or whose travel they limit.

The same handbook lists the usual contact arrangement as single pole, double throw (SPDT) or double pole, double throw (DPDT). In an SPDT switch, one moving contact can touch either of two fixed contacts, and the handbook names the three contacts normally open (NO), normally closed (NC) and common (COM). "Normally" refers to the state with nothing pressing the actuator, the plunger or lever that the outside part pushes. Electronic Design's explainer on snap-action switches describes the common contact resting against the NC contact in that free position, then moving over to the NO contact once the plunger reaches its operating point.

A glossary at the back of the handbook adds the history behind the name. The glossary entry for the one-word spelling defines the term as the registered trade name for a precision switch that uses a short throw of the control plunger to actuate the contacts. The same entry says these switches are used primarily as limit switches, meaning switches that signal when a moving part reaches the end of its travel.

## How the snap mechanism turns slow gear movement into a clean signal

A shock strut doesn't compress in an instant as weight settles onto the wheels, and a gear leg swings into its well along an arc. A switch whose contacts followed that slow movement would spend a long time with its contacts barely touching. The snap mechanism removes that in-between stage:

1. A part of the gear, such as a link on the strut or a bracket on the gear leg, pushes the switch's actuator.
2. The actuator loads a spring inside the switch while the contacts stay where they are.
3. At the operating point, the common contact leaves the NC contact without any further plunger movement and lands on the NO contact, a sequence Electronic Design describes as taking a few milliseconds.
4. Electronic Design also states that the common contact "cannot stop partway" between NC and NO, so the circuit sees either one state or the other.

The FAA handbook gives the reason for this design in its section on aircraft switches. A snap-action design is generally preferred, the handbook says, because it opens and closes the contacts rapidly "regardless of the speed of the operating toggle or plunger, thereby minimizing contact arcing." Arcing is the spark that can jump between contacts as they part, and it burns the contact surfaces. On landing gear, that means a strut that settles slowly still produces a single, clean change of state at one point in its travel.

## How a squat switch keeps the gear down on the ground

The squat switch, which the handbook also calls the safety switch, sits on the main landing gear strut. In the handbook's description, it's "positioned to open and close depending on the extension or compression of the main landing gear strut," and it's wired into several aircraft circuits. The handbook's glossary describes it being moved by the landing gear scissors on the oleo strut, the telescoping shock absorber that carries the wheel.

Elsewhere the handbook calls those scissors torque links: hinged arms joining the fixed upper cylinder of the strut to the sliding piston below it, so they fold as the strut compresses and open as it extends.

The handbook's first example is the circuit that blocks gear retraction on the ground. The handbook describes a method found on many aircraft step by step. The method uses a solenoid, an electromagnet that moves a metal shaft when current flows through its coil:

1. With the aircraft on the ground, the strut is compressed and the squat switch is open.
2. With no current in the safety circuit, the solenoid's center shaft pushes a hardened lock-pin through the landing gear control handle, so the handle can't move to UP.
3. At takeoff, the strut extends and the squat switch closes.
4. Current now flows in the safety circuit, the solenoid energizes, and it pulls the lock-pin back out of the handle.
5. With the pin withdrawn, the pilot can raise the gear.

In that design, the switch never touches the handle. All the switch does is open or close a circuit, and the solenoid does the physical blocking. The handbook notes that there are different ways to achieve this lock-out, and its electrical chapter shows another one. In that chapter's example gear diagram, the current for the gear UP solenoid, the electromagnetic switch that powers the gear UP motor, has to flow through the squat switch. An open squat switch therefore leaves the UP motor without power.

Other systems use the same air or ground signal. Squat switches serve antiskid brake systems, landing gear safety circuits and cabin pressurization systems, according to the FAA glossary. In the handbook's anti-skid section, the brakes are kept from applying until the squat switch signals weight on wheels, because brakes applied as the tires touch the runway could cause an immediate tire blowout.

An August 2012 article by Ian J. Twombly in AOPA's Flight Training magazine adds transponders, the radios that report the aircraft to air traffic control, which switch between standby on the ground and altitude mode in the air. SKYbrary, the aviation safety reference, lists thrust reversers, nose wheel steering, trim and autopilot among the systems that use the weight on wheels (WoW) signal.

## How limit switches stop the gear motor and light the three green lights

Limit switches watch the gear legs themselves. The FAA handbook defines a limit switch as "simply a spring-loaded, momentary contact switch that is activated when a gear reaches its limit of travel." In the example system the handbook walks through, six limit switches sit in the wheel wells. Three up-limit switches detect each gear reaching full retract, and three down-limit switches detect each gear reaching full extension. A component of the landing gear assembly moves each switch mechanically.

The same example shows why a switch with both NO and NC contacts suits the job. While a gear is still traveling down, the handbook traces the current to the gear DOWN solenoid through the "NOT DOWN" contacts of the down-limit switches. The DOWN solenoid closes the high-current circuit to the gear motor, which drives the hydraulic pump, so the motor keeps running. When all three gears reach full DOWN, the switches move to their DOWN position, the three green lights illuminate, and the gear motor turns off. For each down-limit switch, the single movement from NOT DOWN to DOWN therefore breaks the motor path and completes the light path.

What those lights mean to the pilot is set out in the handbook's landing gear chapter:

| Cockpit indication | Meaning given in the FAA handbook |
|---|---|
| Green light for a gear | That gear is down and locked |
| Three green lights | Safe to land |
| All lights out | Typically gear up and locked |
| Gear in transit light, barber pole (striped) display or blinking light | Gear is neither up and locked nor down and locked |
| Gear disagree warning | Gear position doesn't match the gear handle (selector), on aircraft that use it |

That chapter also notes that many aircraft monitor gear door position, and that in one common light-aircraft hydraulic system, electric limit switches turn off the pump when all three gears are down and locked.

## Why many aircraft use proximity sensors instead of contact switches

On many aircraft, the gear position job goes to a sensor with no moving contacts. The FAA handbook calls proximity sensors for gear position safety switches "common in high-performance aircraft." The handbook describes an electromagnetic sensor that returns a different voltage to a gear logic unit, the electronic unit that reads the gear sensors, depending on how close a conductive target is.

When the gear is in its designed position, the metal target sits close to the inductor in the sensor and reduces the return voltage. The handbook's example drawing lists the detector output as 0.3 V for logic 0 and 13 V for logic 1, the two states the logic unit reads.

The handbook gives the reason for the change. Switches with moving parts, it says, "can become contaminated with dirt and moisture from runways and taxi ways." Aircraft parts makers build sensors for this job: Crane Aerospace & Electronics, which makes ELDEC sensors, lists self-contained proximity sensors for landing gear, including weight on wheels, among its products. SKYbrary's article on weight on wheels systems states the trade-off. Mechanical switches are easier to test but fail more often because they rely on mechanical contacts, and proximity sensors are more reliable but harder to troubleshoot.

| | Micro switch (contact type) | Proximity sensor (non-contact) |
|---|---|---|
| What moves it | A gear part presses the actuator (FAA handbook) | A metal target comes near the sensor face (FAA handbook) |
| What the logic receives | Contacts open or closed | A voltage level; 0.3 V and 13 V in the FAA handbook's example |
| Setting it up | Actuator travel and mounting position | Target gap, often set with go/no-go gauges (FAA handbook) |
| Weak point named in the sources | Dirt and moisture on moving parts (FAA handbook); fails more often (SKYbrary) | Can read partly open and partly closed if the gap is wrong (SKYbrary) |
| Testing | Easier to test (SKYbrary) | Harder to troubleshoot (SKYbrary) |

SKYbrary adds a caution about the gap between target and sensor: a proximity sensor that's known to be good but set to an incorrect clearance can cause very erratic behavior in the systems that use its signal. The comparison of micro switches and proximity sensors covers the two sensing methods outside aviation.

## Questions people ask about landing gear switches

### What does a squat switch do?

A squat switch tells the aircraft whether its weight is on the wheels. The FAA handbook describes it opening and closing as the main gear strut compresses and extends. One circuit it controls stops the gear from retracting on the ground, and other circuits use the same signal for anti-skid braking and pressurization.

### What is the purpose of the landing gear system in an aircraft?

The FAA handbook's landing gear chapter opens with its purpose: landing gear "supports the entire weight of an aircraft during landing and ground operations." On retractable gear, the switches and sensors described above report where that gear is and whether the aircraft is on the ground.

### How do you check a micro switch?

On a bench, a micro switch is usually checked for continuity: COM to NC should be closed at rest and COM to NO closed when the actuator is pressed, as covered in the step-by-step micro switch continuity test. On an aircraft, the switch is part of a certified system, and the FAA handbook points to the aircraft manufacturer's maintenance manual for the full description of the gear indication system. Checks and adjustments there belong to a certificated mechanic working from that manual.

## Where the switch logic for one aircraft is written down

Whether a squat switch is open or closed on the ground, how many limit switches a gear leg carries, and which circuits share them all vary by aircraft type. The FAA handbook itself sends readers to the manufacturer's maintenance and operating manuals for the complete description. The wiring diagram in that manual shows which contact, NO or NC, each switch uses. The guide to NO, NC and COM terminals explains how to read those terminal names, and the aircraft flap position micro switch article covers another job the same kind of switch does on an airframe.

## Sources

- Federal Aviation Administration, *Aviation Maintenance Technician Handbook, Airframe* (FAA-H-8083-31B, 2023): Chapter 9 (aircraft switches, precision micro switches, landing gear electrical diagrams), Chapter 13 (landing gear safety switch, proximity sensors, position indicators, anti-skid touchdown protection) and Glossary (Microswitch, Squat switch). faa.gov PDF
- Electronic Design, "Snap-Action Switches Still Rule the Roost." www.electronicdesign.com
- SKYbrary Aviation Safety, "Weight on Wheels (WoW) Systems." skybrary.aero
- Ian J. Twombly, "How it works," AOPA Flight Training, August 2012. www.aopa.org
- Crane Aerospace & Electronics, proximity sensing products. www.craneae.com
