---
title: "ftm micro switch: How to Identify Its Terminals and Check Operation"
description: "ftm micro switch: Understand the operating idea, essential terminology, practical checks, limitations, and evidence needed for careful selection,."
date: 2026-10-12 17:55:05 +0800
category: Basics
tags:
  - ftm micro switch
  - micro switches
  - Basics
author: editorial_team
---

An **ftm micro switch** can be checked by identifying its contact terminals, disconnecting it from the circuit, and observing continuity before and after moving its actuator. The term “FTM” is not defined by the available information, so it does not establish a particular manufacturer, standard, model, or application. Terminal markings and layouts can vary; verify them against documentation for the individual component rather than relying on appearance alone.

A continuity check can show whether the contacts change state as the actuator moves. It does not establish that the switch is suitable for a particular circuit. Keep those two questions separate: first verify the component’s contact behavior, then compare its documented ratings with the application requirements.

## What an ftm micro switch is and what its actuator does

A micro switch is a mechanically actuated electrical component. In a miniature snap-action design, movement of the actuator can transfer an internal contact between electrical states. The actuator is the part moved by an external mechanism; the contact transfer is the electrical response inside the switch. They are related, but they are not the same observation.

This distinction matters during a basic check. An actuator may move, and a mechanism may make an audible click, without that sound proving that the electrical contacts changed state or that the contact path is sound. A meter reading is needed to observe continuity across identified terminals. Conversely, a continuity result describes the tested contact path and state, not the condition of every part of an installed assembly.

“FTM” alone does not tell you how the component is built or where it is used. Do not infer a particular mechanism, circuit role, contact arrangement, or application from those letters. The individual component’s markings and documentation are the relevant references for its terminals and ratings.

The same boundary applies to use. A micro switch can provide an electrical state change in response to actuator movement, but the effect of that change depends on the surrounding circuit. Without information about the specific circuit and component, the switch’s role in a larger device remains unknown.

## How to identify the ftm micro switch terminals

For a changeover contact arrangement, **COM** means common terminal, **NO** means normally open, and **NC** means normally closed. “Normally” refers to the switch’s unactuated state: NO is open relative to COM, while NC is closed relative to COM. These names describe contact relationships in that reference state, not an unconditional promise about current flow in an installed circuit.

Begin with the markings or schematic provided for the individual switch. If the terminals are labeled, use those labels as the starting point and confirm that the component documentation matches the part in hand. Terminal positions and physical layouts can vary, so do not assume that a terminal in a particular location is COM, NO, or NC based on another switch’s appearance.

If markings are absent, unclear, or inconsistent with the documentation, do not guess from geometry. A de-energized continuity check can help map contact behavior, but it only identifies relationships that can be observed under the test conditions. It does not independently establish the component’s identity, ratings, or suitability. Resolve uncertain terminal identification from reliable documentation before connecting the switch to a circuit.

Keep the state reference clear when recording a result. First describe the switch as unactuated, then describe what changes when the actuator is moved. This avoids confusing a contact’s normally open or normally closed designation with its state while the switch is operated.

## How to check an ftm micro switch with a continuity meter

Test the switch only after it is disconnected from the circuit and de-energized. The check is across the isolated switch, not through an installed circuit. If it cannot be safely disconnected and confirmed de-energized, do not proceed with this basic test; the procedure does not establish that an energized or connected assembly is safe to probe.

With the meter set for continuity, check between the documented COM terminal and NO, then between COM and NC, while the actuator is unactuated. Record the readings and the actuator state. For the defined changeover terminology, the expected contact relationship in that state is open between COM and NO and closed between COM and NC.

Next, move the actuator through its operating movement and repeat both checks. The expected behavior is a transfer of the contact relationship: continuity changes from the COM-to-NC path to the COM-to-NO path. Compare the observed readings with this expected pattern and with the component’s own documentation. Do not force or alter the actuator beyond what the available information for that component supports.

A click may accompany movement, but it is not a substitute for these readings. The sound can indicate mechanical movement; by itself it does not verify continuity, confirm that the terminals were identified correctly, or show that the switch will work in a particular circuit. The meter observations are meaningful only for the disconnected switch and the stated actuator positions.

### Related guides

- [dual micro switch](/guides/dual-micro-switch/)
- [touch micro switch](/guides/touch-micro-switch/)
- [no nc micro switch](/guides/no-nc-micro-switch/)
- [normally open micro switch](/guides/normally-open-micro-switch/)

## What test results can and cannot tell you

If the readings consistently change between the two documented contact paths as the actuator moves, that supports basic switching function under the test conditions. It does not prove that the switch is appropriate for an application. Suitability depends on verified component ratings and application requirements, including the relevant voltage, current, environmental, and mechanical conditions. Do not infer any of those limits from a continuity check or from the term “FTM.”

If there is no change in readings, readings are intermittent, or continuity appears on an unexpected path, first recheck the terminal identification, the documented contact arrangement, the actuator state, and the meter setup. A mismatch may reflect an identification or test issue, or a problem with the component; the reading alone does not establish which explanation is correct. Compare the result with the individual switch’s documentation before drawing a conclusion.

A successful isolated check also says nothing conclusive about wiring or other parts of an installed system. The switch may behave as expected on the meter while a circuit problem exists elsewhere. Likewise, a test result that differs from expectation should not be turned into a diagnosis of a specific appliance or vehicle without evidence about that system.

For an **ftm micro switch**, terminal labels and documentation guide identification, and a de-energized, isolated continuity check shows whether the contact relationship changes with actuator movement. Treat that as a limited functional observation, not proof of circuit compatibility or complete system operation. Confirm the individual component’s ratings and the application requirements separately; if terminal identity or safe isolation remains uncertain, leave the result unresolved rather than guessing.

## Sources and references

- Defense Logistics Agency ASSIST: [MIL-PRF-8805K: Switches and Switch Assemblies, Sensitive, Snap Action, General Specification For](https://quicksearch.dla.mil/qsDocDetails.aspx?ident_number=7196){: rel="nofollow noopener noreferrer" }
- Wikipedia: [Miniature snap-action switch](https://en.wikipedia.org/wiki/Miniature_snap-action_switch){: rel="nofollow noopener noreferrer" }
