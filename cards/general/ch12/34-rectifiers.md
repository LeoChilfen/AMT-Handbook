# Rectifiers

> 通用 Ch 12 · Rectifiers · 原文 PDF 第 542 页

## 1. 原文

Many devices in an aircraft require high amperage, low voltage DC for operation. This power may be furnished by DC engine-driven generators, motor generator sets, vacuum tube rectifiers, or dry disk or solid-state rectifiers.

In aircraft with AC systems, a special DC generator is not desirable since it would be necessary for the engine accessory section to drive an additional piece of equipment. Motor generator sets, consisting of air-cooled AC motors that drive DC generators, eliminate this objection because they operate directly off the AC power system. Vacuum tube or various types of solid-state rectifiers provide a simple and efficient method of obtaining high voltage DC at low amperage. Dry disk and solid-state rectifiers, on the other hand, are an excellent source of high amperage at low voltage.

A rectifier is a device that transforms AC into DC by limiting or regulating the direction of current flow. The principal types of rectifiers are dry disk and solid state. Solid-state, or semiconductor, rectifiers have replaced virtually all other types; and, since dry disk and motor generators are largely limited to older model aircraft, the major part of the study of rectifiers is devoted to solid-state devices used for rectification. The two methods discussed in this handbook Gear control Flaps Spoiler Wheel master Nose steering relay Yaw trim Altitude gyro Auxiliary battery Normally closed relay Directional gyro Roll trim ADF On (MOM)

Off Gear, flap, spoiler switch Pilot’s audio Copilot’s map light Transceiver On Off Gyros Battery Inverter Right fwd bus Right fwd bus Transceiver light Altitude gyro light Directional gyro light Resonant filter regulator Output keyer Buffer amplifier DC regulator Square wave oscillator DC input AC output are the half-wave rectifier and the full-wave rectifier.

### Half-Wave Rectifier

Figure 12-215 illustrates the basic concept of a half-wave rectifier. When an AC signal is on a positive swing as shown in Figure 12-215A, the polarities across the diode and the load resistor are also positive. In this case, the diode is forward biased and can be replaced with a short circuit as shown in the figure. The positive portion of the input signal appears across the load resistor with no loss in potential across the series diode.

Figure 12-215B now shows the input signal being reversed. Note that the polarities across the diode and the load resistor are also reversed. In this case, the diode is now reverse biased and can be replaced with an equivalent open circuit. The current in the circuit is now 0 amperes and the voltage drop over the load resistor is 0 volts. The resulting waveform for a complete Si Si Si Si SiSi SiSiSi Si A B Electron movement Silicon atom showing one of the electrons in its valence shell Silicon atom in which one electron has broken out of its valence shell and left a hole Electron moving from one silicon atom to another and leaving a hole Hole movement N-typeP-type N-typeDepletion zone Represents electrostatic field P-type sinusoidal input can be seen at the far right of Figure 12-215. The output waveform is a reproduction of the input waveform minus the negative voltage swing of the wave. For this reason, this type of rectifier is called a half-wave rectifier.

### Full-Wave Rectifier

Figure 12-216 illustrates a more common use of the diode as a rectifier. This type of a rectifier is called a full-wave bridge rectifier. The term “full-wave” indicates that the output is a continuous sequence of pulses rather than having gaps that appear in the half-wave rectifier.

Figure 12-216C shows the initial condition, during which, a positive portion of the input signal is applied to the network. Note the polarities across the diodes. Diodes D2 and D4 are reverse biased and can be replaced with an open circuit. Diodes D1 and D3 are forward biased and act as an open circuit. The current path through the diodes is clear to see, and the resulting waveform is developed across the load resistor.

During the negative portion of the applied signal, the diodes reverse their polarity and bias states. The result is a network shown in Figure 12-216D. Current now passes through diodes D4 and D2, which are forward biased, while diodes D1 and D3 are essentially open circuits due to being reverse biased. Note that during both alternations of the input waveform, the current passes through the load resistor in the same direction. This results in the negative swing of the waveform being flipped up to the positive side of the time line.

Dry disk rectifiers operate on the principle that electric current flows through a junction of two dissimilar conducting materials more readily in one direction than it does in the opposite direction. This is true because the resistance to current flow in one direction is low, while in the other direction it is high. Depending on the materials used, several amperes may flow in the direction of low resistance but only N-type Narrow depletion zone P-type + – Holes Electrons Electron flow e – N-typeWide depletion zoneP-type +– a few milliamperes in the direction of high resistance.

Three types of dry disk rectifiers may be found in aircraft: the copper oxide rectifier, the selenium rectifier, and the magnesium copper-sulfide rectifier. The copper oxide rectifier consists of a copper disk upon which a layer of copper oxide has been formed by heating. [Figure 12-217] It may also consist of a chemical copper oxide preparation spread evenly over the copper surface. Metal plates, usually lead plates, are pressed against the two opposite faces of the disk to form a good contact. Current flow is from the copper to the copper oxide.

The selenium rectifier consists of an iron disk, similar to a washer, with one side coated with selenium. Its operation is similar to that of the copper oxide rectifier. Current flows from the selenium to the iron.

The magnesium copper sulfide rectifier is made of washer- shaped magnesium disks coated with a layer of copper sulfide. The disks are arranged similarly to the other types. Current flows from the magnesium to the copper sulfide.

Today, there are many varieties of diodes that can be grouped into one of several basic categories.

#### Power Rectifier Diodes

The rectifier diode is usually used in applications that require high current, such as power supplies. The range in which the diode can handle current can vary anywhere from one ampere to hundreds of amperes. One common example of diodes is the series of diodes, part numbers 1N4001 to 1N4007. The “1N” indicates that there is only one PN junction, or that the device is a diode. The average current carrying range for these rectifier diodes is about one ampere with a peak inverse voltage between 50 volts to 1,000 volts. Larger rectifier diodes can carry currents up to 300 amperes when forward biased and have a peak inverse voltage of 600 volts. A recognizable feature of the larger rectifier diodes is that they are encased in metal in order to provide a heat sink. [Figure 12-218]

Zener diodes (sometimes called “breakdown diodes”) are designed so that they break down (allow current to pass) when the circuit potential is equal to or in excess of the desired reverse bias voltage. The range of reverse bias breakdown-voltages commonly found can range from 2 volts to 200 volts depending on design. Once a specific reverse bias voltage has been reached, the diode conducts and behaves like a constant voltage source. Within the normal operating range, the zener functions as a voltage regulator, waveform clipper, and other related functions. Below the desired voltage, the zener blocks the circuit like any other diode biased in the reverse direction. Because the zener diode allows free flow in one direction when it is used in an AC circuit, two diodes connected in opposite directions must be used. This takes care of both alternations of current. Power ratings of these devices range from about 250 milliwatts to 50 watts.

#### Special Purpose Diodes

The unique characteristics of semiconductor material have allowed for the development of many specialized types of diodes. A short description of some of the more common diode types is given for general familiarization. [Figure 12-219]

#### Light-Emitting Diode (LED)

In a forward biased diode, electrons cross the junction and fall into holes. As the electrons fall into the valence band, they radiate energy. In a rectifier diode, this energy is dissipated as heat. However, in the light-emitting diode (LED), the energy is dissipated as light. By using elements such as gallium, arsenic, and phosphorous, an LED can be designed to radiate colors, such as red, green, yellow, blue, and infrared light. LEDs that are designed for the visible light portion of the spectrum are useful for instruments, indicators, and even cabin lighting. The advantages of the LED over the incandescent lamps are longer life, lower voltage, faster on and off operations, and less heat.

A B A B RL Forward bias (Short circuit)

+ + − − + − RL + + − − + − Reverse bias (Open circuit)

V– V+ Time 120 v –120 v V– V+ Time 120 v V– V+ Time Input Signal Circuit Depiction Output Wave-form Across Load Resistor Half-wave Rectification 120v 90v 60v 30v 1v 2v 3v 4v 5v 60 mA 50 mA 40 mA 30 mA 20 mA 10 mA 600 Aμ 1200 Aμ Junction diode characteristics

#### Liquid Crystal Displays (LCD)

The liquid crystal display (LCD) has an advantage over the LED in that it requires less power to operate. Where LEDs commonly operate in the milliwatt range, the LCD operates in the microwatt range. The liquid crystal is encapsulated between two glass plates. When voltage is not applied to the LCD, the display is clear. However, when a voltage is applied, the result is a change in the orientation of the atoms of the crystals. The incident light is then reflected in a different direction. A frosted appearance results in the regions that have voltage applied and permits distinguishing of numeric values.

Thermal energy produces minority carriers in a diode. The higher the temperature, the greater the current in a reverse current diode. Light energy can also produce minority carriers. By using a small window to expose the PN junction, a photodiode can be built. When light falls upon the junction of a reverse-biased photodiode, electrons-hole pairs are created inside the depletion layer. The stronger the light, the greater the number of light-produced carriers, which in turn causes a greater magnitude of reverse-current. Because of this characteristic, the photodiode can be used in light detecting circuits.

The varactor is simply a variable-capacitance diode. The reverse voltage applied controls the variable-capacitance of the diode. The transitional capacitance decreases as the reverse voltage is increasingly applied. In many D BA C RL D2D1 D3D4 + − + − RL D1 D3 + − + + +− − − RL D2 D4 + − + + + − − − V– V+ Time 120 v –120 v Input signal V– V+ Time 120 v 120 v Output wave-form Across load resistorCircuit depiction Current Current Current Current applications, the varactor has replaced the old mechanically tuned capacitors. Varactors can be placed in parallel with an inductor and provide a resonant tank circuit for a tuning circuit. By simply varying the reverse voltage across the varactor, the resonant frequency of the circuit can be adjusted.

#### Schottky Diodes

Schottky diodes are designed to have metal, such as gold, silver, or platinum, on one side of the junction and doped silicon, usually an N-type, on the other side of the junction. This type of a diode is considered a unipolar device because free electrons are the majority carrier on both sides of the junction. The Schottky diode has no depletion zone or charge storage, which means that the switching time can be as high as 300 MHz. This characteristic exceeds that of the bipolar diode.

#### Diode Identification

Figure 12-218 illustrates a number of methods employed for identifying diodes. Typically manufacturers place some form of an identifier on the diode to indicate which end is the anode and which end is the cathode. Dots, bands, colored bands, the letter ‘k’ or unusual shapes indicate the cathode end of the diode.

## 2. 中文翻译

<!-- TODO: 逐段翻译，段数与上面严格一一对应（34 段）。专业术语按行业惯例，数字与缩写保留。 -->

## 3. 专业词汇

<!-- TODO: 用表格 | 英文 | 词性 | 中文 | 本节语境 |，4~8 行。优先选下面 Glossary 里的词（本节原文出现过的）：
- Ampere —— A unit of measure of the rate of electron flow or current in an electrical conductor. One ampere of current represents one coulomb of electrical charge (6.24 × 
- Capacitance (C) —— The property of an electric conductor that characterizes its ability to store an electric charge.
- Current —— The flow of electrical charge.
- Electrostatic field —— A field of force that exists around a charged body.
- Energy —— The capacity of a physical system to perform work. There are two types of energy, kinetic and potential.
- Frequency —— The number of cycles (on/off) completed per unit of time. Usually expressed in Hertz.
- Inductor —— A coil of wire that produces inductance in an electrical circuit.
- Power (exponent) —— A shorthand method of indicating how many times a number, called the base, is multiplied by itself. For example, in the number 43, 3 is the power, or exponent, 
-->

## 4. 语法解析

<!-- TODO: 2~4 个语法点，格式：
### ① 语法点名称
**原句**：<必须逐字来自第 1 节原文>
**拆解**：主/谓/宾、从句、非谓语等成分分析
**要点**：为什么这样用、易错点、可迁移的搭配
-->
