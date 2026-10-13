---
title: "How to Test Micro Switch"
description: "how to test micro switch: Understand the operating idea, essential terminology, practical checks, limitations, and evidence needed for careful selection,."
date: 2026-10-12 16:49:35 +0800
category: Basics
tags:
  - how to test micro switch
  - micro switches
  - Basics
author: editorial_team
---

To learn **how to test micro switch** continuity and switching action, begin with the power isolated and the switch electrically separated from at least one connected lead. A continuity reading can show whether contacts change state as the actuator moves, but it does not establish that the switch will perform correctly under load or that the surrounding circuit is sound. The procedure below focuses on switch-level checks with a multimeter and on interpreting results without treating them as a complete equipment diagnosis.

## How to test micro switch safely with a multimeter

Switch off and isolate the equipment before making resistance or continuity measurements. Before testing, verify absence of voltage using an appropriate method. Continuity and resistance measurements are for a de-energized circuit; do not use a meter’s continuity mode on a live circuit.

Disconnect at least one switch lead before measuring. Leaving the switch connected can allow other circuit paths to affect the reading, so the meter may not be measuring only the switch contacts. Keep track of the disconnected connection so the test remains limited to the switch and can be returned to its original state after measurement.

Use the meter’s continuity or resistance mode only after the switch is de-energized and isolated as described. A continuity beeper is an indication based on the meter’s threshold, not a universal definition of a good contact. Resistance mode can provide a numerical reading, but the result still depends on probe contact and the meter’s measurement conditions. Record what the meter displays rather than relying only on whether it beeps.

Stop if access would require working around an unsafe condition, if stored energy may remain, or if you cannot establish that the switch is isolated. Do not proceed on the assumption that switching equipment off alone proves an absence of voltage. If you are uncertain about isolation or the appropriate verification method, leave the measurement undone until that uncertainty is resolved. This procedure does not cover energized voltage checks, which are distinct from isolated continuity testing.

## Identify the micro switch terminals and actuator states

Look for terminal markings on the switch. In generic changeover terminology, **COM** means common, **NO** means normally open, and **NC** means normally closed. The exact device schematic takes precedence: terminal labels and physical arrangements can vary, and a switch may not have all three terminals. If markings are absent or unclear, consult the device documentation rather than guessing from terminal position.

Before probing, note the actuator’s released position and the position it reaches when pressed. Do not assume that every design has the same actuator direction or that pressing it corresponds to a particular installed condition. Keep the physical state explicit in your notes, for example, “released” and “pressed,” so each meter reading can be tied to the state actually observed.

For a switch with the relevant marked terminals, prepare to measure across COM and NC, then across COM and NO. These are separate contact-pair checks. Do not infer the terminal identities solely from a reading, and do not interpret a change across one pair as proof that every terminal or connection is correct. If the schematic does not match the available markings or the terminal identity remains uncertain, stop and resolve that uncertainty before interpreting results.

## Measure continuity in released and pressed positions

With the switch de-energized and at least one lead disconnected, place the probes across COM and NC. Note the meter mode and the reading with the actuator released. Then press the actuator and record the reading again. Repeat the same released-to-pressed sequence across COM and NO where those terminals exist. Keep the probe pair unchanged during each comparison.

Record the meter’s displayed result, including an open indication, a continuity indication, or a resistance value. Meter continuity thresholds and lead resistance can affect what appears on the display, so avoid treating the beeper alone as a precise resistance measurement. If using resistance mode, a consistent reading across repeated measurements is more useful than an isolated value without its terminal pair and actuator state.

Repeat the actuator movement and take the readings again. A repeatable change between the released and pressed states is more informative than a single transition. Keep the actuator movement and probe contact steady enough to distinguish a state change from a momentary loss of contact at the probes. If a reading changes while the actuator is held in one position, record that behavior rather than choosing only the most favorable result.

A simple record can include the terminal pair, actuator state, meter mode, displayed reading, and whether the result repeated. For example, keep separate entries for COM–NC released, COM–NC pressed, COM–NO released, and COM–NO pressed. This ties the result to both electrical terminals and mechanical position. If the switch has fewer marked terminals, document only the pairs that can be identified from its markings or schematic; do not fill in missing terminal information by assumption.

### Related guides

- [dual micro switch](/guides/dual-micro-switch/)
- [touch micro switch](/guides/touch-micro-switch/)
- [no nc micro switch](/guides/no-nc-micro-switch/)
- [normally open micro switch](/guides/normally-open-micro-switch/)

## Interpret micro switch test results and limits

A typical change between continuity and an open-circuit indication across a relevant terminal pair as the actuator moves is consistent with switching action. It is not, by itself, proof that the switch meets a particular electrical rating or works correctly under load. A continuity test is a low-level switch check, not a test of performance in the operating circuit.

A stable open or stable closed reading may be consistent with the contact state for that terminal pair and actuator position. Whether it is expected depends on the terminal identities, the device schematic, and the observed actuator state. Do not label a stable reading as a failure or a pass without that context. Generic COM, NO, and NC terminology helps organize the measurements, but the exact device schematic should guide interpretation.

An unchanged reading between released and pressed positions may indicate a switch issue, but other possibilities include incorrect terminal identification, poor probe contact, or a test setup problem. Intermittent or unstable readings can likewise reflect a contact or switch problem, probe contact, or setup issue. Unexpectedly high resistance is not conclusive by itself; check that the probes contact the intended terminals and that the switch is isolated before drawing a switch-level conclusion. These observations identify reasons to investigate further, not a definitive diagnosis.

Even a repeatable change does not verify performance under load, establish that wiring or connectors are sound, or prove the surrounding circuit operates correctly. Circuit wiring, connectors, and load behavior require separate checks. Keep the conclusion narrow: record whether the isolated switch changed its measured state with actuator movement, and preserve any uncertainty about terminal identity or inconsistent readings. If safe isolation cannot be established, stop rather than continuing the test.

This concludes the explanation of how to test micro switch.

## Sources and references

- Defense Logistics Agency ASSIST: [MIL-PRF-8805K: Switches and Switch Assemblies, Sensitive, Snap Action, General Specification For](https://quicksearch.dla.mil/qsDocDetails.aspx?ident_number=7196){: rel="nofollow noopener noreferrer" }
- Wikipedia: [Miniature snap-action switch](https://en.wikipedia.org/wiki/Miniature_snap-action_switch){: rel="nofollow noopener noreferrer" }
