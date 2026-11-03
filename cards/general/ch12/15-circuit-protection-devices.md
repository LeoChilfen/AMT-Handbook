# Circuit Protection Devices

> 通用 Ch 12 · Circuit Protection Devices · 原文 PDF 第 469 页

## 1. 原文

Perhaps the most serious trouble in a circuit is a direct short. The term “direct short” describes a situation in which some point in the circuit, where full system voltage is present, comes in direct contact with the ground or return side of the circuit. This establishes a path for current flow that contains no resistance other than that present in the wires carrying the current, and these wires have very little resistance.

Most wires used in aircraft electrical circuits are small gauge, and their current carrying capacity is quite limited. The size of the wires used in any given circuit is determined A B 1 2 3 Load Shaft Terminals Resistive strip Wiper Rotary potentiometer construction 1 2 3 A 25% 70 Ω 30 Ω 100 Ω B 50% 30 Ω 70 Ω 100 Ω C 75% 10 Ω 90 Ω 100 Ω AB 1 2 3 by the amount of current the wires are expected to carry under normal operating conditions. Any current flow in excess of normal, such as the case of a direct short, would cause a rapid generation of heat. If the excessive current flow caused by the short is left unchecked, the heat in the wire could cause a portion of the wire to melt and at the very least, open the circuit.

To protect aircraft electrical systems from damage and failure caused by excessive current, several kinds of protective devices are installed in the systems. Fuses, circuit breakers, thermal protectors, and arc fault circuit breakers are used for this purpose.

Circuit protective devices, as the name implies, all have a common purpose—to protect the units and the wires in the circuit. Some are designed primarily to protect the wiring and to open the circuit in such a way as to stop the current flow when the current becomes greater than the wires can safely carry. Other devices are designed to protect a unit in the circuit by stopping the current flow to it when the unit becomes excessively warm.

Fuses are used to protect the circuit from over current conditions. [Figure 12-67A] The fuse is installed in the circuit so that all the current in the circuit passes through it. In most fuses, the strip of metal is made of an alloy of tin and bismuth, which melts and opens the circuit when the current exceeds T A 25% 70 Ω 30 Ω 100 Ω B 50% 30 Ω 70 Ω 100 Ω C 75% 10 Ω 90 Ω 100 Ω the rated capacity of the fuse. For example, if a 5-amp fuse is placed into a circuit, the fuse allows currents up to 5 amps to pass. Because the fuse is intended to protect the circuit, it is quite important that its capacity match the needs of the circuit in which it is used.

When replacing a fuse, consult the applicable manufacturer’s instructions to be sure a fuse of the correct type and capacity is installed. Fuses are installed in two types of fuse holders in aircraft. “Plug-in holders” or in-line holders are used for small and low capacity fuses. “Clip” type holders are used for heavy high capacity fuses and current limiters.

The current limiter is very much like the fuse. However, the current limiter link is usually made of copper and will stand a considerable overload for a short period of time. Like the fuse, it opens up in an over current condition in heavy current circuits such as 30 amp or greater. These are used primarily to sectionalize an aircraft circuit or bus. Once the limiter is opened, it must be replaced. The schematic symbol for the current limiter shows two triangles pointing to each other with a line on both sides of the triangles. [Figure 12-67B].

The circuit breaker is commonly used in place of a fuse and is designed to break the circuit and stop the current flow when the current exceeds a predetermined value. Unlike the fuse, the circuit breaker can be reset; whereas the fuse or current limiter must be replaced. [Figure 12-68] There are several types of circuit breakers in general use in aircraft systems. One is a magnetic type. When excessive current flows in the circuit, it makes an electromagnet strong enough to move a small armature, which trips the breaker. Another type is the thermal overload switch or breaker. This consists of a bimetallic strip which, when it becomes overheated from excessive current, bends away from a catch on the switch lever and permits the switch to trip open.

Most circuit breakers must be reset by hand. If the overload condition still exists, the circuit breaker trips again to prevent damage to the circuit. At this point, it is usually not advisable to continue resetting the circuit breaker, but to initiate troubleshooting to determine the cause. Repeated resetting of a circuit breaker can lead to circuit or component damage or worse, the possibility of a fire or explosion. Automatic reset type circuit breakers are not allowed in aircraft. Circuit breakers are commonly grouped on a circuit breaker panel that is accessible to the flight crew. Figure 12-69 shows a circuit breaker and a circuit breaker panel.

#### Arc Fault Circuit Breaker

In recent years, the arc fault circuit breaker has begun to provide an additional layer of protection beyond that of the thermal protection already provided by conventional circuit breakers. The arc fault circuit breaker monitors the circuit for an electrical arcing signature, which can indicate possible wiring faults and unsafe conditions. These conditions can lead to fires or loss of power to critical systems. The arc fault circuit breaker is only beginning to make an appearance in the aircraft industry and is not widely used like the thermal type of circuit breaker.

### Thermal Protectors

A thermal protector, or switch, is used to protect a motor. It is designed to open the circuit automatically whenever the temperature of the motor becomes excessively high. It has two positions—open and closed. The most common use for a thermal switch is to keep a motor from overheating. If a A B malfunction in the motor causes it to overheat, the thermal switch breaks the circuit intermittently.

The thermal switch contains a bimetallic disk, or strip, that bends and breaks the circuit when it is heated. This occurs because one of the metals expands more than the other when they are subjected to the same temperature. When the strip or disk cools, the metals contract and the strip returns to its original position and closes the circuit.

Components in the electrical circuits are typically not all intended to operate continuously or automatically. Most of them are meant to operate at certain times, under certain conditions, to perform very definite functions. There must be some means of controlling their operation. Either a switch, or a relay, or both may be included in the circuit for this purpose.

Switches control the current flow in most aircraft electrical circuits. A switch is used to start, to stop, or to change the direction of the current flow in the circuit. The switch in each circuit must be able to carry the normal current of the circuit and must be insulated heavily enough for the voltage of the circuit. Figure 12-70 shows various switches used in aircraft electrical systems.

An understanding of some basic definitions of the switch is necessary before any of the switch types are discussed. The number of poles, throws, and positions they have designates

es, as well as some other type of switches.

Pole—the switch’s movable blade or contactor. The number of poles is equal to the number of circuits, or paths for current flow, that can be completed through the switch at any one time.

Throw—indicates the number of circuits, or paths for current, that it is possible to complete through the switch with each pole or contactor.

Positions—indicates the number of places at which the operating device (toggle, plunger, and so forth) comes to rest and at the same time open or close one or more circuits.

Toggle Switch Single-Pole, Single-Throw (SPST)

The single-pole, single-throw (SPST) switch allows a connection between two contacts. One of two conditions exist. Either the circuit is open in one position or closed in the other position. [Figure 12-71]

Single-Pole, Double-Throw (SPDT)

The single-pole, double-throw (SPDT) switch is shown in can be made between one contact and the other.

Double-Pole, Single-Throw (DPST)

The double-pole, single-throw (DPST) switch connection can be made between one set of contacts and either of two other sets of contacts. [Figure 12-73]

Double-Pole, Double-Throw (DPDT)

The schematic symbol for the double-pole, double-throw (DPDT) switch is shown in Figure 12-74. This type of switch makes a connection from one set of contacts to either of two other sets of contacts.

A toggle switch that is spring-loaded to the OFF position system.

and must be held in the ON position to complete the circuit is a momentary contact two-position switch. One that comes to rest at either of two positions, opening the circuit in one position and closing it in another, is a two-position switch. A toggle switch that comes to rest at any one of three positions is a three-position switch.

A switch that stays open, except when it is held in the closed position, is a normally open switch (usually identified as NO). One that stays closed, except when it is held in the open position is a normally closed switch (NC). Both kinds are spring loaded to their normal position and return to that position as soon as they are released.

Locking toggles require the operator to pull out on the switch toggle before moving it in to another position. Once in the new position, the switch toggle is release back into a lock, which then prevents the switch from inadvertently being moved.

A microswitch opens or closes a circuit with a very small movement of the tripping device ( 1⁄16 inch or less). This is what gives the switch its name, since micro means small.

Microswitches are usually pushbutton switches. They are used primarily as limit switches to provide automatic control of landing gears, actuator motors, and the like. Figure 12-75 shows a normally closed microswitch in cross-section and illustrates how these switches operate. When the operating plunger is pressed in, the spring and the movable contact are pushed, opening the contacts and the circuit. Figure 12-76 shows a pushbutton microswitch.

#### Rotary Selector Switches

A rotary selector switch takes the place of several switches. When the knob of the switch is rotated, the switch opens one circuit and closes another. Ignition switches and voltmeter selector switches are typical examples of this kind of switch. [Figure 12-77]

#### Pushbutton Switches

Pushbutton switches have one stationary contact and one movable contact. The movable contact is attached to the pushbutton. The pushbutton is either an insulator itself or is insulated from the contact. This switch is spring loaded and designed for momentary contact.

#### Lighted Pushbutton Switches

Another more common switch found in today’s aircraft is the lighted pushbutton switch. This type of switch takes the form of a 5⁄8-inch to 1-inch cube with incandescent or LED lights to indicate the function of the switch. Switch designs come in a number of configurations; the two most common are the alternate action and momentary action and usually have a two-pole or four-pole switch body. Other less common switch actions are the alternate and momentary holding coil configurations. The less known holding or latching coil switch bodies are designed to have a magnetic coil inside the switch body that is energized through two contacts in the base of the switch. When the coil is energized and the switch is pressed, the switch contacts remain latched until power is removed from the coil. This type of design allows for some degree of remote control over the switch body. [Figure 12-78] The display optics of the lighted pushbutton switch provide the crew with a clear message that is visible under a wide range of lighting conditions with very high luminance and wide viewing angles. While some displays are simply a transparent screen that is backlit by an incandescent light, the higher quality and more reliable switches are available in sunlight readable displays and night vision (NVIS) versions. Due to the sunlight environment of the flight deck, displays utilizing standard lighting techniques “washout” when viewed in direct sunlight. Sunlight readable displays are designed to minimize this effect.

Lighted pushbutton switches can also be used in applications where a switch is not required and the optics are only for indications. This type of an indicator is commonly called an annunciator.

Stationary contact Moveable contact Operating plunger Grooved anchor Three-bladed spring

#### Dual In-Line Parallel (DIP) Switches

The acronym “DIP” switch is defined as Dual In-Line Parallel switch in reference to the physical layout. DIP switches are commonly found in card cages, and line replaceable units (LRU) and are used in most cases to adjust gains, control configurations, and so forth. Each one of the switches is generally an SPST slide or rocker switch. The technician may find this switch in packages ranging in size from DIP2 through DIP32. Some of the more common sizes are DIP4 and DIP8.

Switch guards are covers that protect a switch from unintended operation. Prior to the operation of the switch, the guard is usually lifted. Switch guards are commonly found on systems such as fire suppression and override logics for various systems. Figure 12-79A shows a traditional switch with a guard while Figure 12-79B shows a pushbutton switch with a guard. The guard needs to be moved before the switch can be pushed.

A relay is simply an electromechanical switch where a small amount of current can control a large amount of current. [Figure 12-80] When a voltage is applied to the coil of the relay, the electromagnet is energized due to the current. When energized, an electromagnetic field pulls the common (C) or arm of the relay down. When the arm or common is pulled down, the circuit between the arm and the normally closed (NC) contacts is opened and the circuit between the arm and the normally open (NO) contacts are closed. When the energizing voltage is removed, the spring returns the arm contacts back to the normally closed (NC) contacts. The relay usually has two connections for the coil. The (+) side is designated as X1 and the ground-side of the coil is designated as X2.

## 2. 中文翻译

<!-- TODO: 逐段翻译，段数与上面严格一一对应（47 段）。专业术语按行业惯例，数字与缩写保留。 -->

## 3. 专业词汇

<!-- TODO: 用表格 | 英文 | 词性 | 中文 | 本节语境 |，4~8 行。优先选下面 Glossary 里的词（本节原文出现过的）：
- Current —— The flow of electrical charge.
- Insulator —— A material that does not conduct electrical current very well or not at all. Examples are glass, ceramic, and plastic.
- Lever —— The simplest machine. There are three basic parts in all levers: the fulcrum “F,” a force or effort “E,” and a resistance “R.”
- Potentiometer —— A variable tapped resistor that can be used as a voltage divider.
- Power (exponent) —— A shorthand method of indicating how many times a number, called the base, is multiplied by itself. For example, in the number 43, 3 is the power, or exponent, 
- Power —— Power is the time rate at which work is done or energy is transferred.
- Resistance —— The opposition a device or material offers to the flow or current.
- Voltmeter —— A current-measuring instrument, designed to indicate voltage by measuring the current flow through a resistance of known value.
-->

## 4. 语法解析

<!-- TODO: 2~4 个语法点，格式：
### ① 语法点名称
**原句**：<必须逐字来自第 1 节原文>
**拆解**：主/谓/宾、从句、非谓语等成分分析
**要点**：为什么这样用、易错点、可迁移的搭配
-->
