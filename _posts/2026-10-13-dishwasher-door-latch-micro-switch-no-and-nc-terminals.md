---
title: "Dishwasher Door Latch Micro Switch NO and NC Terminals: What They Mean and How to Read Them"
description: "On a dishwasher door latch micro switch, NO and NC describe the contacts with the plunger released. See how latches use them and how to read your switch."
date: 2026-10-13 11:27:16 +0800
category: Applications
tags:
  - dishwasher door latch micro switch NO and NC terminals
  - micro switches
  - Applications
author: editorial_team
seo_title: "Dishwasher Door Latch Micro Switch NO and NC Terminals"
last_updated: 2026-11-12
---

Pull a dishwasher's door latch out of its housing and the small switch inside it carries terminal letters for normally open and normally closed, often with a third for common. The usual reading is that "normally" means the door is open, so NO is open with the door open and closes when you latch it. **For a micro switch the reference is the plunger, and dishwasher service manuals call their door switches normally closed or normally open depending on how the latch is built.** The letters on the switch, two real latch designs and a meter check on your own switch follow in that order.

## Quick answer

On a dishwasher door latch micro switch, NO (normally open) and NC (normally closed) describe the contacts while nothing presses the plunger, the small button the latch pushes. Daniel Herzog's article in Electronic Design describes that resting state: the NC circuit "can carry current" and the common (COM) terminal is insulated from NO. Whether latching the door closes or opens the circuit depends on which pair the dishwasher uses.

## NO and NC compared

| Terminal pair | Plunger released | Plunger pressed | Typical meter reading, released | Typical meter reading, pressed |
|---|---|---|---|---|
| COM to NO (normally open) | Open | Closed | Open (no continuity) | Near 0 ohms |
| COM to NC (normally closed) | Closed | Open | Near 0 ohms | Open (no continuity) |

COM is the terminal shared by both pairs. Electronic Design's description of the snap action adds that the moving contact "cannot stop partway between the NC and normally open contacts," so at any moment exactly one of the two pairs is closed. Crouzet's explainer on how micro switches work describes the same split from the other side: pressing a normally open switch closes the contact "and current flows," and pressing a normally closed one opens it.

## What "normally" refers to

On a micro switch, "normally" means the actuator is free, with nothing pushing the plunger. Electronic Design calls that state the free position, and a datasheet's NO and NC labels describe the switch in it.

Other door switches use a different reference, which is where the confusion starts. Absolute Automation, which makes magnetic door contacts, defines its NO switch as one where "the internal switch is open when the magnetic module is against the switch module," and it equates that with the door being closed. On that kind of contact, "normally" describes the installed, door-shut condition. On a micro switch it describes the switch on the bench.

In a dishwasher, the latch decides whether a closed door presses the plunger. If the latch pushes the plunger when the door shuts, the NO pair (COM and NO) closes with the door. If the latch releases the plunger when the door shuts, the NC pair (COM and NC) closes with the door. The letters on the switch stay the same either way.

## How two dishwasher latches use the terminals

### GE GLDT690T: normally open contacts closed by the latch

GE's technical service manual for the GLDT690T describes a door switch assembly of "2 switches activated by a spring-loaded plunger." One switch "connects or disconnects the line (hot) side of 120 VAC," and the other does the same for the neutral side. When the door is closed, the manual says, "the door latch presses and holds down the switch plunger," and "the normally open contacts of the door switches are closed." This design matches the usual reading: the NO pair closes when you latch the door.

### Maytag MDBH970AW: normally closed switches in series with the supply

Maytag's service manual for the MDBH970AW describes the other arrangement. "Two Door Switches are used in the Latch Assembly," and "Both switches are normally CLOSED and will open only when engaged by the Door Latch mechanism." The same manual says each switch "is in series with respect to L1 and neutral line operations," L1 being the line or hot side. It adds that "Failure of either or both switches will result in rendering the Dishwasher inoperative."

The GE and Maytag manuals each put a switch in each supply leg, line and neutral, and both use the door latch to operate them. They label the switches from opposite ends, which is why a meter reading with the door open and latched tells you more about your own model than the letters alone.

## Reading the terminals on your own switch

📌 **On safety:** *Switch off the dishwasher's breaker or unplug it before removing the inner door panel. GE's GLDT690T manual warns that "Power remains applied to the controller" at one connector "while the door is open," so an open door doesn't make the wiring safe. Never jumper the door switch terminals to run the machine with the door open.*

1. **Photograph the wires on the switch before removing them.** Note which wire sits on COM and which on NO or NC.
2. **Take the wires off the switch.** Testing the switch out of circuit keeps the rest of the dishwasher out of the reading.
3. **Put the meter probes on COM and NO.** With the plunger released, a good switch reads open. Press the plunger and it should read near zero ohms.
4. **Move the probe from NO to NC.** The readings should flip: near zero ohms released, open when pressed.
5. **Check which pair the harness used.** If the wires were on COM and NO, the circuit closes when the plunger is pressed. If they were on COM and NC, it closes when the plunger is released.

A switch that reads the same in both plunger positions, or flickers while held down, has failed. The general method for [testing a micro switch with a multimeter](/guides/how-to-test-a-micro-switch/) covers meter settings, and [routine care of a dishwasher door latch micro switch](/guides/dishwasher-door-latch-micro-switch-maintenance/) covers the latch side.

## Can you swap NO and NC on a replacement?

No, not without changing what the dishwasher sees. Moving a wire from NO to NC reverses the switch's logic, so a circuit that was meant to close with the door latched would close with it open. In a design like the GE or Maytag latch, where the switches sit in the line and neutral legs, that reversal decides whether the supply reaches the dishwasher with the door open. Match the replacement's contact form, meaning whether it offers NO, NC or both, to the original, and wire it to the same terminals shown in your photo or in the model's wiring diagram.

The [difference between NO and NC contacts](/guides/no-nc-micro-switch/) is covered in general terms in a separate guide, and the same contact logic in microwave ovens appears in [how a door interlock micro switch works](/guides/door-interlock-micro-switch/).

## FAQ

**Why won't my dishwasher start even though the door is closed?**
One common cause is a door latch switch that no longer reports a closed door. GE's GLDT690T manual describes the latch pressing the switch plunger to close the door switch contacts, and Maytag's MDBH970AW manual says failure of either door switch leaves the dishwasher inoperative. A meter test on the switch, with power off, shows whether its contacts still change when the plunger moves.

**How to wire up a micro switch?**
Put each wire back on the terminal it came off, using a photo taken before removal. COM joins NO when the plunger is pressed and joins NC when it's released, so the dishwasher's design decides which pair is used. Match the replacement's rating and contact form to the original.

**What are the symptoms of a bad micro switch?**
In a dishwasher latch, a failing switch can leave the machine dead with the door latched, or make it stop when the door is nudged. On a meter, a bad switch reads the same with the plunger pressed and released, or reads unsteadily while pressed. Check that the latch is actually reaching the plunger before replacing the switch.

## What to note before ordering a replacement switch

Record which terminals were wired, the rating printed on the switch body, and whether the latch presses or releases the plunger when the door shuts. Those three facts decide whether a replacement will behave like the original. If the service manual for your model names the switches as normally open or normally closed, check that label against your meter readings before ordering.

Dishwasher door switches are a regular catalog item for appliance switch makers. [ZING EAR](https://www.zingear-switch.com/){:rel="nofollow"} lists dishwashers among the applications of its ZINGEAR G905-150F05W1 and ZINGEAR G9105-150R00F1 switches, and its article on the G3 waterproof series names dishwasher door interlocks among that series' uses. Whichever switch your dishwasher carries, the service manual's continuity table is still what tells you which contact is NO and which is NC.


## Related guides

- [bottling machine home position micro switch location](/guides/bottling-machine-home-position-micro-switch-location/)
- [incinerator end of stroke micro switch maintenance](/guides/incinerator-end-of-stroke-micro-switch-maintenance/)
- [rotary indexing table guard interlock micro switch location](/guides/rotary-indexing-table-guard-interlock-micro-switch-location/)
- [security barrier open position micro switch wiring](/guides/security-barrier-open-position-micro-switch-wiring/)

## Sources

- GE GLDT690T Technical Service Manual, Door Switch Assembly, p.18 (ManualsLib copy)
- Maytag MDBH970AW service manual, Door Latch & Switch Holder Assembly (16021814 Rev. 0, ManualsOnline copy)
- Daniel Herzog, "Snap-Action Switches Still Rule The Roost," Electronic Design, 2012
- Crouzet, How does a microswitch work?
- Absolute Automation, What is the difference between your NO and NC door switches?
- ZING EAR, G905-150F05W1 product page: https://www.zingear-switch.com/g905-150f05w1-compact-waterproof-and-dustproof-micro-switch--switch-button-for-disinfection-cabinet--dishwasher.html
- ZING EAR, ZINGEAR G9105-150R00F1 product page: https://www.zingear-switch.com/zingear-group-g9105-150r00f1-industrial-equipment-micro-switch.html
- ZING EAR blog, The G3 Waterproof Micro Switch: A Miniature Sealed Solution: https://www.zingear-switch.com/the-g3-waterproof-micro-switch-a-miniature-sealed-solution.html
