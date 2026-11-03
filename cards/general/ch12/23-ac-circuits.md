# AC Circuits

> 通用 Ch 12 · AC Circuits · 原文 PDF 第 501 页

## 1. 原文

### Ohm’s Law for AC Circuits

The rules and equations for DC circuits apply to AC circuits only when the circuits contain resistance alone, as in the case of lamps and heating elements. In order to use effective values of voltage and current in AC circuits, the effect of inductance and capacitance with resistance must be considered.

The combined effects of resistance, inductive reactance, and capacitive reactance make up the total opposition to current flow in an AC circuit. This total opposition is called impedance and is represented by the letter Z. The unit for the measurement of impedance is the ohm.

### Series AC Circuits

If an AC circuit consists of resistance only, the value of the impedance is the same as the resistance, and Ohm’s Law for an AC circuit, I = E/Z, is exactly the same as for a DC circuit. In Figure 12-133, a series circuit containing a lamp with 11 ohms resistance connected across a source is illustrated. To find how much current flows if 110 volts DC is applied and how much current flows if 110 volts AC are applied, the following examples are solved:

I = E R I = (where Z = R) E Z I = 110 V 11 W I = 110 V 11 W I = 10 amperes DC I = 10 amperes AC When AC circuits contain resistance and either inductance or capacitance, the impedance, Z, is not the same as the 110V AC 60 cycles A XL1 XL2 + L2 − L1 resistance, R. The impedance of a circuit is the circuit’s total opposition to the flow of current. In an AC circuit, this opposition consists of resistance and reactance, either inductive or capacitive or elements of both.

Resistance and reactance cannot be added directly, but they can be considered as two forces acting at right angles to each other. Thus, the relation between resistance, reactance, and impedance may be illustrated by a right triangle. [Figure 12-134]

Since these quantities may be related to the sides of a right triangle, the formula for finding the impedance, or total opposition to current flow in an AC circuit, can be found by using the law of right triangles. This theorem, called the Pythagorean theorem, applies to any right triangle. It states that the square of the hypotenuse is equal to the sum of the squares of the other two sides. Thus, the value of any side of a right triangle can be found if the other two sides are known. If an AC circuit contains resistance and inductance, as shown in Figure 12-135, the relation between the sides can be stated as:

Z 2 = R2 + XL2 The square root of both sides of the equation gives Z = R2 + XL2 This formula can be used to determine the impedance when the values of inductive reactance and resistance are known. It can be modified to solve for impedance in circuits containing capacitive reactance and resistance by substituting XC in the formula in place of XL. In circuits containing resistance with both inductive and capacitive reactance, the reactances can be combined, but because their effects in the circuit are exactly opposite, they are combined by subtraction:

X = XL − XC or X = XC − XL (the smaller number is always subtracted from the larger)

In Figure 12-135, a series circuit consisting of resistance and inductance connected in series is connected to a source of 110 volts at 60 cps. The resistive element is a lamp with 6 ohms resistance, and the inductive element is a coil with an inductance of 0.021 henry. What is the value of the impedance and the current through the lamp and the coil?

First, the inductive reactance of the coil is computed:

X L = 2π × f × L X L = 6.28 × 60 × 0.021 X L = 8 ohms inductive reactance Next, the total impedance is computed:

Z = R2 + XL2 Z = 62 + 82 Z = 36 + 64 Z = 100 Z = 10 ohms impedance Then the current flow, I = E Z I = 110 10 I = 11 amperes current XL2XL1 110 V Reactance Resistance Z R Impedance XL − XC The voltage drop across the resistance (ER) is:

E R = I × R E R = 11 × 6 = 66 volts The voltage drop across the inductance (EXL) is:

EXL = I × XL EXL = 11 × 8 = 88 volts The sum of the two voltages is greater than the impressed voltage. This results from the fact that the two voltages are out of phase and, as such, represent the maximum voltage. If the voltage in the circuit is measured by a voltmeter, it is approximately 110 volts, the impressed voltage. This can be proved by the equation: E = (ER)2 + (EXL)2 E = 662 + 882 E = 4,356 + 7,744 E = 12,100 E = 110 volts In Figure 12-136, a series circuit is illustrated in which a capacitor of 200 µf is connected in series with a 10 ohm lamp. What is the value of the impedance, the current flow, and the voltage drop across the lamp?

First, the capacitance is changed from microfarads to farads. Since 1 million microfarads equal 1 farad, then:

200 μf = = 0.000200 farads 2001,000,000 XC = 12πfC XC = 16.28 × 60 × 0.000200 farads XC = 10.07536 X C = 13 ohms capacitive reactance To find the impedance, Z = R2 + XC2 Z = 102 + 132 Z = 100 + 169 Z = 269 Z = 16.4 ohms capacitive reactance To find the current, I = E Z I = 110 16.4 I = 6.7 amperes The voltage drop across the lamp (ER) is:

E R = 6.7 × 10 E R = 67 volts The voltage drop across the capacitor (EXC) is EXC = I × XC EXC = 6.7 × 13 EXC = 86.1 volts 110 V AC 60 cycles 10 Ω 200 μf A 110V AC 60 cycles 0.021 henries A 6 Ω The sum of these two voltages does not equal the applied voltage, since the current leads the voltage. To find the applied voltage, use the following formula:

ET = (ER)2 + (EXC)2 ET = 672 + 86.12 ET = 4,489 + 7,413 ET = 11,902 E T = 110 volts When the circuit contains resistance, inductance, and capacitance, the following equation is used to find the impedance:

Z = R2 + (XL – XC)2 Example: What is the impedance of a series circuit, consisting of a capacitor with a reactance of 7 ohms, an inductor with a reactance of 10 ohms, and a resistor with a resistance of 4 ohms? [Figure 12-137]

Z = R2 + (XL – XC)2 Z = 42 + (10 – 7)2 Z = 42 + 32 Z = 25 Z = 5 ohms Assuming that the reactance of the capacitor is 10 ohms and the reactance of the inductor is 7 ohms, then X C is greater than XL. Thus, Z = R2 + (XL – XC)2 Z = 42 + (7 – 10)2 Z = 42 + (–3)2 Z = 16 + 9 Z = 25 Z = 5 ohms

### Parallel AC Circuits

The methods used in solving parallel AC circuit problems are basically the same as those used for series AC circuits. Out of phase voltages and currents can be added by using the law of right triangles. However, in solving circuit problems, the currents through the branches are added since the voltage drops across the various branches are the same and are equal to the applied voltage. In Figure 12-138 , a parallel AC circuit containing an inductance and a resistance is shown schematically. The current flowing through the inductance, I L, is 0.0584 ampere, and the current flowing through the resistance is 0.11 ampere. What is the total current in the circuit?

IT = IL2 + IR2 = (0.0584)2 + (0.11)2 = 0.0155 = 0.1245 ampere Since inductive reactance causes voltage to lead the current, the total current, which contains a component of inductive current, lags the applied voltage. If the current and voltages are plotted, the angle between the two, called the phase angle, illustrates the amount the current lags the voltage.

In Figure 12-139, a 112-volt generator is connected to a load consisting of a 2 µf capacitance and a 10,000-ohm resistance in parallel. What is the value of the impedance and total current flow?

First, find the capacitive reactance of the circuit:

XC = 1 2πfC Changing 2 μf to farads and entering the values into the formula given:

110 V AC 60 cycles 4 Ω 10 Ω 7 Ω capacitance.

= 12 × 3.14 × 60 × 0.000002 = or 1 10,0000.00075360 7.536 = 1,327 XC capacitive reactance To find the impedance, the impedance formula used in a series AC circuit must be modified to fit the parallel circuit:

Z = R2 + XC2 RXC = (10,000)2 + (1,327)2 10,000 × 1,327 = 0.1315 W (approximately)

To find the current through the capacitance:

IC = E XC IC = 110 1,327 = 0.0829 ampere To find the current flowing through the resistance:

IR = E R = 110 10,000 = 0.011 ampere To find the total current in the circuit:

IT2 = IR2 + IC2 IT = IL2 + IR2 = 0.0836 ampere (approximately)

It has been shown that both inductive reactance:

(X L = 2πfL) and capacitive reactance:

XC = 1 2πfC are functions of an AC frequency. Decreasing the frequency decreases the ohmic value of the inductive reactance, but a decrease in frequency increases the capacitive reactance. At some particular frequency, known as the resonant frequency, the reactive effects of a capacitor and an inductor is equal. Since these effects are the opposite of one another, they will cancel, leaving only the ohmic value of the resistance to oppose current flow in a circuit. If the value of resistance is small or consists only of the resistance in the conductors, the value of current flow can become very high.

In a circuit where the inductor and capacitor are in series, and the frequency is the resonant frequency, or frequency of resonance, the circuit is said to be “in resonance” and is referred to as a series resonant circuit. The symbol for resonant frequency is Fn.

If, at the frequency of resonance, the inductive reactance is equal to the capacitive reactance, then:

XL = XC, or 2πfL = 1 2πfC Dividing both sides by 2 fL, Fn2 = 1 (2π) 2LC Extracting the square root of both sides gives:

Fn = 1 2π LC Where Fn is the resonant frequency in cps, C is the capacitance in farads, and L is the inductance in henries. With this formula, the frequency at which a capacitor and inductor is resonant can be determined.

To find the inductive reactance of a circuit use:

XL = 2πfL The impedance formula used in a series AC circuit must be modified to fit a parallel circuit.

2 μf110VG 10,000 Ω resistance.

ILG IR5 henries 1000 Ω resistance.

Z = R2 = XL2 XL To find the parallel networks of inductance and capacitive reactors, use:

X = XL + XC XL + XC To find the parallel networks with resistance capacitive and inductance, use:

Z = XL2 XC2 + (RXL – RXC)2 R XL XC Since at the resonant frequency XL cancels XC, the current can become very large, depending on the amount of resistance. In such cases, the voltage drop across the inductor or capacitor is often higher than the applied voltage.

In a parallel resonant circuit, the reactances are equal and equal currents flow through the coil and the capacitor. [Figure 12-140]

Since the inductive reactance causes the current through the coil to lag the voltage by 90°, and the capacitive reactance causes the current through the capacitor to lead the voltage by 90°, the two currents are 180° out of phase. The canceling effect of such currents would mean that no current would flow from the generator and the parallel combination of the inductor and the capacitor would appear as infinite impedance. In practice, no such circuit is possible, since some value of resistance is always present, and the parallel circuit, sometimes called a tank circuit, acts as very high impedance. It is also called an antiresonant circuit, since its effect in a circuit is opposite to that of a series resonant circuit, in which the impedance is very low.

### Power in AC Circuits

In a DC circuit, power is obtained by the equation, P = EI, (watts equal volts × amperes). Thus, if 1 ampere of current flows in a circuit at a pressure of 200 volts, the power is 200 watts. The product of the volts and the amperes is the true power in the circuit.

### True Power Defined

True power of any AC circuit is commonly referred to as the working power of the circuit. True power is the power consumed by the resistance portion of the circuit and is measured in watts. True power is symbolized by the letter P and is indicated by any wattmeter in the circuit. True power is calculated by the formula:

#### Apparent Power Defined

Apparent power in an AC circuit is sometimes referred to as the reactive power of a circuit. Apparent power is the power consumed by the entire circuit, including both the resistance and the reactance. Apparent power is symbolized by the letter S and is measured in volt-amps (V A). Apparent power is a product of the effective voltage multiplied by the effective current. Apparent power is calculated by the formula:

S = I2 × Z Only when the AC circuit is made up of pure resistance is the apparent power equal to the true power. [Figure 12-141] When there is capacitance or inductance in the circuit, the current and voltage are not exactly in phase, and the true power is less than the apparent power. The true power is obtained by a wattmeter reading. The ratio of the true power to the apparent power is called the power factor and is usually expressed in percent. In equation form, the relationship is:

Power Factor (PF) = 100 × watts (True Power)volts × amperes (Apparent Power)

Example: A 220-volt AC motor takes 50 amperes from the line, but a wattmeter in the line shows that only 9,350 watts are taken by the motor. What are the apparent power and the power factor?

Apparent power = V olts × Amperes Apparent power = 220 × 50 = 11,000 watts or volt-amperes.

(PF) = Watts (True Power) × 100V A (Apparent Power)

(PF) = 9,350 × 10011,000 (PF) = 85, or 85%

A transformer changes electrical energy of a given voltage into electrical energy at a different voltage level. It consists of two coils that are not electrically connected, but are arranged so that the magnetic field surrounding one coil cuts through the other coil. When an alternating voltage is applied to (across) one coil, the varying magnetic field set up around that coil creates an alternating voltage in the other coil by mutual induction. A transformer can also be used with pulsating DC, but a pure DC voltage cannot be used, since only a varying voltage creates the varying magnetic field that is the basis of the mutual induction process.

A transformer consists of three basic parts. [Figure 12-142] These are an iron core, which provides a circuit of low reluctance for magnetic lines of force; a primary winding, which receives the electrical energy from the source of applied voltage; and a secondary winding, which receives electrical energy by induction from the primary coil.

The primary and secondary of this closed core transformer are wound on a closed core to obtain maximum inductive effect between the two coils.

There are two classes of transformers: voltage transformers, used for stepping up or stepping down voltages; and

### Current Transformers

used in instrument circuits. In voltage transformers, the primary coils are connected in parallel across the supply voltage. [Figure 12-143A] The primary windings of current transformers are connected in series in the primary circuit. [Figure 12-143B] Of the two types, the voltage transformer is the more common.

There are many types of voltage transformers. Most of these are either step-up or step-down transformers. The factor that determines whether a transformer is a step-up or step- down type is the “turns” ratio. The turns ratio is the ratio of the number of turns in the primary winding to the number of turns in the secondary winding. For example, the turns ratio of the step-down transformer is 5 to 1, since there are five times as many turns in the primary as in the secondary. [Figure 12-144A] The step-up transformer has a 1 to 4 turns ratio. [Figure 12-144B]

The ratio of the transformer input voltage to the output voltage is the same as the turns ratio if the transformer is 100 percent efficient. Thus, when 10 volts are applied to the primary of the transformer, two volts are induced in the secondary. [Figure 12-144A] If 10 volts are applied to the primary of the transformer, the output voltage across the terminals of the secondary is 40 volts. [Figure 12-144B]

No transformer can be constructed that is 100 percent efficient, although iron core transformers can approach this figure. This is because all the magnetic lines of force set up in the primary do not cut across the turns of the secondary coil. A certain amount of the magnetic flux, called leakage flux, leaks out of the magnetic circuit. The measure of how well the flux of the primary is coupled into the secondary is called the “coefficient of coupling.” For example, if it is assumed that the primary of a transformer develops 10,000 lines of force and only 9,000 cut across the secondary, the coefficient of coupling would be 0.9. Stated another way, the transformer would be 90 percent efficient.

When an AC voltage is connected across the primary terminals of a transformer, an AC flows and self induces a voltage in the primary coil that is opposite and nearly equal to the applied voltage. The difference between these two voltages allows just enough current in the primary to magnetize its core. This is called the exciting, or magnetizing, current. The magnetic field caused by this exciting current cuts across the secondary coil and induces a voltage by mutual induction.

If a load is connected across the secondary coil, the load current flowing through the secondary coil produces a magnetic field that tends to neutralize the magnetic field produced by the primary current. This reduces the self-induced (opposition) voltage in the primary coil and allows more primary current Primary coil Secondary coil S P Iron core Reactive power Watts True power Apparent power volts x amperes to flow. The primary current increases as the secondary load current increases, and decreases as the secondary load current decreases. When the secondary load is removed, the primary current is again reduced to the small exciting current sufficient only to magnetize the iron core of the transformer.

If a transformer steps up the voltage, it steps down the current by the same ratio. This should be evident if the power formula is considered, for the power (I × E) of the output (secondary) electrical energy is the same as the input (primary) power minus that energy loss in the transforming process. Thus, if 10 volts and 4 amps (40 watts of power) are used in the primary to produce a magnetic field, there is 40 watts of power developed in the secondary (disregarding any loss). If the transformer has a step-up ratio of 4 to 1, the voltage across the secondary is 40 volts and the current is 1 amp. The voltage is 4 times greater and the current is one-fourth the primary circuit value, but the power (I × E value) is the same.

When the turns ratio and the input voltage are known, the output voltage can be determined as follows:

E2 E1 = N2 N1 Where E is the voltage of the primary, E2 is the output voltage of the secondary, and N1 and N2 are the number of turns of the primary and secondary, respectively.

Transposing the equation to find the output voltage gives:

E2 = E1 N2 N1 The most commonly used types of voltage transformers are:

1. Power transformers are used to step up or step down voltages and current in many types of power supplies. They range in size from the small power transformer [Figure 12-145] used in a radio receiver to the large transformers used to step down high power line voltage to the 110–120 volt level used in homes.

Figure 12-146 shows the schematic symbol for an iron core transformer. In this case, the secondary is made up of three separate windings. Each winding supplies a different circuit with a specific voltage, which saves the weight, space, and expense of three separate transformers. Each secondary has a midpoint connection called a “center tap,” which provides a selection of half the voltage across the whole winding. The leads from the various windings are color coded by the manufacturer. [Figure 12-146] This is a standard color code, but other codes or numbers may be used.

2. Audio transformers resemble power transformers. They have only one secondary and are designed to operate over the range of audio frequencies (20 to 20,000 cps).

3. RF transformers are designed to operate in equipment that functions in the radio range of frequencies. The symbol for the RF transformer is the same as for an RF choke coil. It has an air core as shown in Figure 12-147.

4. Autotransformers are normally used in power circuits; however, they may be designed for other uses. Two different symbols for autotransformers used in power or audio circuits are shown in Figure 12-148 . If used in an RF communication or navigation circuit [Figure 12-148B], it is the same, except there is no symbol for an iron core. The autotransformer uses part of a winding as a primary; and, depending on whether it is step up or step down, it uses all or part of the same winding as the secondary. For example, the autotransformer shown in Figure 12-148A could use the following possible choices for primary and secondary terminals.

AC power supply Load AC power supply Meter To load A B 10 turns primary 2 turns secondary 8 turns secondary 2 turns primary A B Current Transformers Current transformers are used in AC power supply systems to sense generator line current and to provide a current, proportional to the line current, for circuit protection and control devices.

The current transformer is a ring-type transformer using a current carrying power lead as a primary (either the power lead or the ground lead of the AC generator). The current in the primary induces a current in the secondary by magnetic induction. The sides of all current transformers are marked “H1” and “H2” on the unit base. The transformers must be installed with the “H1” side toward the generator in the circuit in order to have proper polarity. The secondary of the transformer should never be left open while the system is being operated; to do so could cause dangerously high voltages and could overheat the transformer. Therefore, the transformer output connections should always be connected with a jumper when the transformer is not being used but is left in the system.

### Transformer Losses

In addition to the power loss caused by imperfect coupling, transformers are subject to “copper” and “iron” losses. The resistance of the conductor comprising the turns of the coil causes copper loss. The iron losses are of two types: hysteresis loss and eddy current loss. Hysteresis loss is the electrical energy required to magnetize the transformer core, first in one direction and then in the other, in step with the applied alternating voltage. Eddy current loss is caused by electric currents (eddy currents) induced in the transformer core by the varying magnetic fields. To reduce eddy current losses, cores are made of laminations coated with an insulation, which reduces the circulation of induced currents.

### Power in Transformers

Since a transformer does not add any electricity to the circuit but merely changes or transforms the electricity that already exists in the circuit from one voltage to another, the total amount of energy in a circuit must remain the same. If it were possible to construct a perfect transformer, there would be no loss of power in it; power would be transferred undiminished from one voltage to another.

Since power is the product of volts times amperes, an increase in voltage by the transformer must result in a decrease in current and vice versa. There cannot be more power in the secondary side of a transformer than there is in the primary. The product of amperes times volts remains the same.

The transmission of power over long distances is accomplished by using transformers. At the power source, the voltage is stepped up in order to reduce the line loss during transmission. At the point of utilization, the voltage is stepped down, since it is not feasible to use high voltage to operate motors, lights, or other electrical appliances.

## 2. 中文翻译

<!-- TODO: 逐段翻译，段数与上面严格一一对应（92 段）。专业术语按行业惯例，数字与缩写保留。 -->

## 3. 专业词汇

<!-- TODO: 用表格 | 英文 | 词性 | 中文 | 本节语境 |，4~8 行。优先选下面 Glossary 里的词（本节原文出现过的）：
- Addition —— The process in which the value of one number is added to the value of another.
- Ampere —— A unit of measure of the rate of electron flow or current in an electrical conductor. One ampere of current represents one coulomb of electrical charge (6.24 × 
- Apparent power —— That power apparently available for use in an AC circuit containing a reactive component. It is the product of effective voltage times the effective current, ex
- Capacitance (C) —— The property of an electric conductor that characterizes its ability to store an electric charge.
- Capacitive reactance (X c) —— The measure of a capacitor’s opposition to alternating current.
- Capacitor —— An electrical component that stores an electric charge.
- Conductor —— A material that will carry electric current.
- Current —— The flow of electrical charge.
-->

## 4. 语法解析

<!-- TODO: 2~4 个语法点，格式：
### ① 语法点名称
**原句**：<必须逐字来自第 1 节原文>
**拆解**：主/谓/宾、从句、非谓语等成分分析
**要点**：为什么这样用、易错点、可迁移的搭配
-->
