---
title: "Air Fryer Basket Micro Switch NO and NC Terminals: What They Mean"
description: "air fryer basket micro switch NO and NC terminals: Understand the operating idea, essential terminology, practical checks, limitations, and evidence."
date: 2026-10-12 16:49:35 +0800
category: Applications
tags:
  - air fryer basket micro switch NO and NC terminals
  - micro switches
  - Applications
author: editorial_team
---

The **air fryer basket micro switch NO and NC terminals** describe contact states at the switch, not whether the basket is inserted or removed. In generic changeover terminology, COM is the common terminal, NC is normally closed, and NO is normally open. These names refer to the switch’s unactuated state. Operating the actuator changes the contact connection, but the appliance’s mechanism determines when that happens relative to basket position.

A careful check therefore separates two questions: which contacts connect in each switch state, and what those states mean in the appliance circuit. Do not infer the expected reading from the basket position alone. Identify the exact switch terminals from its markings and schematic, and consult the appliance’s service documentation for its circuit. Testing should be done with the appliance disconnected from power, at the switch terminals, and in accordance with the component’s specifications.

## Air fryer basket micro switch NO and NC terminals: contact states

COM is the common terminal in generic changeover terminology. NC means normally closed, and NO means normally open. “Normally” refers to the switch’s unactuated condition, not to a basket position, the appliance’s usual operating mode, or whether the appliance is plugged in. The exact switch schematic and terminal markings should be checked to confirm that these symbols apply to the component being tested.

In the unactuated state, the expected continuity pairing is COM–NC; COM–NO is expected to be open. When the actuator is operated, the changeover action reverses those pairings: COM–NO is expected to show continuity, while COM–NC is expected to be open. These are generic contact-state expectations, not a guarantee about every switch or every measurement setup. The specific component’s specifications govern its expected behavior and test conditions.

For a basic state comparison, record which of the two COM pairs shows continuity with the actuator released, then operate the actuator and compare the readings. The switch’s markings or schematic must identify COM, NO, and NC before interpreting results. A terminal’s physical location alone is not enough to identify it: use the connection diagram and terminal marking documented for the exact switch, rather than inferring the terminal function from a generic layout.

If the observed pairings do not match the component documentation, the result is not enough by itself to identify a cause. Confirm that the terminals have been identified correctly, that the actuator is in the intended state, and that the test is made at the switch rather than through connected appliance circuitry. Do not use the basket’s installed or removed position as a substitute for identifying the switch’s unactuated or actuated state.

## Why basket position does not define NO or NC

NO and NC describe the micro switch’s contacts relative to its own actuator state. They do not name the basket-in or basket-out state. The mechanism linking the basket to the actuator determines whether inserting the basket presses the actuator, releases it, or otherwise changes the switch state. The air fryer’s circuit design then determines how that switch state relates to the appliance’s interlock behavior.

Consequently, the same NO and NC labels can be used in different appliance designs without establishing that a removed basket should produce continuity at a particular terminal pair. It would be an unsupported inference to conclude that COM–NO must connect whenever the basket is inserted, or that COM–NC must connect whenever it is removed. The terminal labels remain tied to the switch’s unactuated state regardless of how the appliance positions or operates it.

To interpret basket position, the switch contact state must be considered alongside the mechanism and the appliance circuit. A contact-state check can establish which pair connects when the actuator is released or operated, but it cannot, on its own, establish what the basket position should do in a particular appliance. Use the appliance’s service documentation to determine its specific circuit and intended relationship between mechanism movement and switch operation.

This distinction also limits what can be concluded from a reading. A continuity result at one pair does not by itself show that the basket mechanism is correctly positioned or that the appliance’s circuit is behaving as intended. Keep the finding narrow: report the pair measured and whether the actuator was released or operated. Avoid translating that result into a universal statement about basket status or appliance operation.

### Related guides

- [ball screw actuator home position micro switch replacement](/guides/ball-screw-actuator-home-position-micro-switch-replacement/)
- [bottling machine end of stroke micro switch](/guides/bottling-machine-end-of-stroke-micro-switch/)
- [automated guided vehicle home position micro switch location](/guides/automated-guided-vehicle-home-position-micro-switch-location/)
- [accelerator pedal position stop micro switch operating force](/guides/accelerator-pedal-position-stop-micro-switch-operating-force/)

## How to verify the terminals safely

Disconnect the appliance from power before accessing or testing the switch. Do not probe an energized appliance. Follow applicable deenergization and qualification requirements, and consult service documentation for the appliance’s specific circuit. If testing requires service procedures beyond the available documentation or qualifications, leave the work to qualified service personnel.

With the appliance disconnected, identify COM, NO, and NC from the exact switch’s markings or schematic. Use an appropriate continuity meter across COM–NC and COM–NO, first with the switch released and then with its actuator operated. Follow the component’s specifications for the test. Compare the results with the generic expected states: COM–NC continuity and COM–NO open when unactuated; COM–NO continuity and COM–NC open when actuated. The switch documentation takes precedence if it specifies different details or test conditions.

Connected appliance circuitry can affect an in-circuit reading. Parallel paths or connected electronics may produce a reading that does not represent the switch contacts alone. Therefore, a result taken through the assembled circuit should not automatically be treated as a direct measurement of the switch. Isolated continuity verification means checking the contacts without those connected paths affecting the result; achieving that may require qualified service procedures. Do not assume that an in-circuit reading settles whether the switch itself has the expected contact states.

Do not bypass the interlock to obtain a reading or to operate the appliance. A contact-state check is for identifying the switch’s behavior, not for defeating the appliance’s circuit. If the reading is unclear, the terminal identity is uncertain, or the result must be interpreted in relation to basket position, stop short of guessing and refer to the appliance’s service documentation or qualified service personnel.

In short, COM–NC and COM–NO are interpreted from the micro switch’s unactuated and actuated states, while the basket’s position depends on the appliance mechanism and circuit. For the **air fryer basket micro switch NO and NC terminals**, verify the contact pairs at the identified switch terminals with power disconnected, and do not infer basket logic from terminal labels alone.

## Sources and references

- Defense Logistics Agency ASSIST: [MIL-PRF-8805K: Switches and Switch Assemblies, Sensitive, Snap Action, General Specification For](https://quicksearch.dla.mil/qsDocDetails.aspx?ident_number=7196){: rel="nofollow noopener noreferrer" }
- Occupational Safety and Health Administration: [29 CFR 1910.333: Selection and Use of Work Practices](https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.333){: rel="nofollow noopener noreferrer" }
- Wikipedia: [Miniature snap-action switch](https://en.wikipedia.org/wiki/Miniature_snap-action_switch){: rel="nofollow noopener noreferrer" }
