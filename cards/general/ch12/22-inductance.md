# Inductance

> 通用 Ch 12 · Inductance · 原文 PDF 第 498 页

## 1. 原文

### Characteristics of Inductance

Michael Faraday discovered that by moving a magnet through a coil of wire, a voltage was induced across the coil. If a complete circuit was provided, then a current was also induced. The amount of induced voltage is directly proportional to the rate of change of the magnetic field with respect to the coil. The simplest of experiments can prove that when a bar magnet is moved through a coil of wire, a voltage is induced and can be measured on a voltmeter. This is commonly known as Faraday’s Law or the Law of Electromagnetic Induction, which states that the induced emf or electromagnetic force in a closed loop of wire is proportional to the rate of change of the magnetic flux through a coil of wire.

Conversely, current flowing through a coil of wire produces a magnetic field. When this wire is formed into a coil, it then becomes a basic inductor. The magnetic lines of force around each loop or turn in the coil effectively add to the lines of force around the adjoining loops. This forms a strong magnetic field within and around the coil. Figure 12-125A shows a coil of wire strengthening a magnetic field. The magnetic lines of force around adjacent loops are deflected into an outer path when the loops are brought close together. This happens because the magnetic lines of force between adjacent loops are in opposition with each other. The total magnetic field for the two loops is shown in Figure 12-125B. As more loops are added close together, the strength of the magnetic field increases. Figure 12-125C illustrates the combined effects of many loops of a coil. The result is a strong electromagnet.

The primary aspect of the operation of a coil is its property to oppose any change in current through it. This property is called inductance. When current flows through any conductor, a magnetic field starts to expand from the center of the wire. As the lines of magnetic force grow outward through the conductor, they induce an emf in the conductor itself. The induced voltage is always in the direction opposite to the direction of the current flow. The effects of this countering emf are to oppose the immediate establishment of the maximum current. This effect is only a temporary condition. Once the current reaches a steady value in the conductor, the lines of magnetic force no longer expand and the countering emf is no longer present.

At the starting instant, the countering emf nearly equals the applied voltage, resulting in a small current flow. However, as the lines of force move outward, the number of lines cutting the conductor per second becomes progressively smaller, resulting in a diminished counter emf. Eventually, the counter emf drops to zero and the only voltage in the circuit is the applied voltage and the current is at its maximum value.

### The RL Time Constant

Because the inductors basic action is to oppose a change in its current, it then follows that the current cannot change instantaneously in the inductor. A certain time is required for the current to make a change from one value to another. The rate at which the current changes is determined by a time constant represented by the Greek letter τ. The time constant for the RL circuit is:

τ = R L Where τ = seconds L = inductance (H)

In a series RL circuit, the current increases to 63 percent of its full value in 1 time constant after the circuit is closed. This buildup is similar to the buildup of voltage in a capacitor when charging an RC circuit. Both follow an exponential curve and reach 99 percent value after the 5th time constant. [Figure 12-126]

### Physical Parameters

Some of the physical factors that affect inductance are:

Current and voltage in phase Effect of inductance Effect of capacitance A B C 0° 180° 360° emf 0° Lag 180°90° 360°270° emf 0° Lead 180°90° 360°270° emf 1. The number of turns: Doubling the number of turns in a coil produces a field twice as strong if the same current is used. As a general rule, the inductance varies as the square of the number of turns.

2. The cross-sectional area of the coil: The inductance of a coil increases directly as the cross-sectional area of the core increases. Doubling the radius of a coil increases the inductance by a factor of four.

3. The length of a coil: Doubling the length of a coil, while keeping the same number of turns, halves the value of inductance.

4. The core material around which the coil is formed: Coils are wound on either magnetic or nonmagnetic materials. Some nonmagnetic materials include air, copper, plastic, and glass. Magnetic materials include nickel, iron, steel, or cobalt, which have a permeability that provides a better path for the magnetic lines of force and permit a stronger magnetic field.

The characteristic of self-inductance was summarized by German physicist Heinrich Lenz in 1833, and gives the direction of the induced emf resulting from electromagnetic induction. This is commonly known as Lenz’s Law, which states: The emf induced in an electric circuit always acts in such a direction that the current it drives around a closed circuit produces a magnetic field, which opposes the change in magnetic flux.

Self-inductance is the generation of a voltage in an electric circuit by a changing current in the same circuit. Even a straight piece of wire has some degree of inductance because current in a conductor produces a magnetic field. When the current in a conductor changes direction, there is a corresponding change in the polarity of the magnetic field around the conductor. Therefore, a changing current produces a changing magnetic field around the wire. To further intensify the magnetic field, the wire can be rolled into a coil, which is called an inductor. The changing magnetic field around the inductor induces a voltage across the coil. This induced emf is called self-inductance and tends to oppose any change in current within the circuit. This property is usually called inductance and symbolized with the letter L.

### Types of Inductors

Inductors used in radios can range from a straight wire at UHF to large chokes and transformers used for filtering the ripple from the output of power supplies and in audio amplifiers. Figure 12-127 shows the schematic symbols for common inductors. Values of inductors range from nano-henries to tens of henries.

Inductors are classified by the type of core and the method of winding them. The number of turns in the inductor winding and the core material determine the capacity of the inductor. Cores made of dielectric material like ceramics, wood, and paper provide small amounts of stored energy while cores made of ferrite substances have a much higher degree of stored energy. The core material is usually the most important aspect of the inductors construction. The conductors typically used in the construction of an inductor offer little resistance to the flow of current. However, with the introduction of a core, resistance is introduced in the circuit and the current now builds up in the windings until the resistance of the core is overcome. This buildup is stored as magnetic energy in the core. Depending on the core resistance, the buildup soon reaches a point of magnetic saturation, and it can be released when necessary. The most common core materials are: air, solid ferrite, powdered ferrite, steel, toroid, and ferrite toroid.

63% 100% 90% 80% 70% 60% 50% 40% 30% 20% 10% 86% 95% 98% Applied voltage Current 1t Counter emf Current, counter emf, and applied voltage in an inductive circuit.

2t 3t 4t 5t 99% Opposing magnetic fields Combined magnetic fields Coils with some separationA Coils without separationB Strong magnetic field in a coilC Current eee eee Current eee eee Current eee eee SouthNorth

### Units of Inductance

The henry is the basic unit of inductance and is symbolized with the letter H. An electric circuit has an inductance of one henry when current changing at the rate of one ampere per second induces a voltage of one volt into the circuit. In many practical applications, millihenries (mH) and microhenries (μH) are more common units. The typical symbol for an inductor is shown in Figure 12-127.

### Inductors in Series

If we connect two inductors in series, the same current flows through both inductors and, therefore, both are subject to the same rate of change of current. [Figure 12-128] When inductors are connected in series, the total inductance LT, is the sum of the individual inductors. The general equation for n number of inductors in series is:

LT = L1 + L2 + L3 + … LN

### Inductors in Parallel

When two inductors are connected in parallel, each must have the same potential difference between the terminals. [Figure 12-129] When inductors are connected in parallel, the total inductance is less than the smallest inductance. The general equation for n number of inductors in parallel is:

LT = + +1L1 1L2 1L3 1LN 1 + . . .

A simple example would be:

L 1 = 10 mH, L2 = 5 mH, L3 = 2 mH LT = + +110 mH 15 mH 12 mH 1 LT = 0.8 mH 1 L T = 1.25 mH

### Inductive Reactance

Alternating current is in a constant state of change; the effects of the magnetic fields are a continuously inducted voltage opposition to the current in the circuit. This opposition is called inductive reactance, symbolized by X L, and is measured in ohms just as resistance is measured. Inductance is the property of a circuit to oppose any change in current and is measured in henries. Inductive reactance is a measure of how much the countering emf in the circuit opposes current Inductor + L1 L2 − variations.

The inductive reactance of a component is directly proportional to the inductance of the component and the applied frequency to the circuit. By increasing either the inductance or applied frequency, the inductive reactance likewise increases and presents more opposition to current in the circuit. This relationship is given as:

X L = 2πfL Where: XL = inductive reactance in ohms f = frequency in cycles per second π = 3.1416 L = inductance In Figure 12-130, an AC series circuit is shown in which the inductance is 0.146 henry and the voltage is 110 volts at a frequency of 60 cps. Inductive reactance is determined by the following method.

X L = 2π × f × L X L = 6.28 × 60 × 0.146 X L = 55 ohm In any circuit where there is only resistance, the expression for the relationship of voltage and current is given by Ohm’s Law: I = E/R. Similarly, when there is inductance in an AC circuit, the relationship between voltage and current can be expressed as:

Current = or I = V oltage E Reactance XL Where:

XL = inductive reactance of the circuit in ohms I = E XL I = 110 55 I = 2 amperes In AC series circuits, inductive reactances are added like resistances in series in a DC circuit. [Figure 12-131] Thus, the total reactance in the illustrated circuit equals the sum of the individual reactances.

The total reactance of inductors connected in parallel is found the same way as the total resistance in a parallel circuit. [Figure 12-132] Thus, the total reactance of inductances connected in parallel, as shown, is expressed as:

(XL)T = + +1(XL)1 1(XL)2 1(XL)3 1

## 2. 中文翻译

<!-- TODO: 逐段翻译，段数与上面严格一一对应（41 段）。专业术语按行业惯例，数字与缩写保留。 -->

## 3. 专业词汇

<!-- TODO: 用表格 | 英文 | 词性 | 中文 | 本节语境 |，4~8 行。优先选下面 Glossary 里的词（本节原文出现过的）：
- Alternating current —— An electric current that reverses direction in a circuit at regular intervals.
- Ampere —— A unit of measure of the rate of electron flow or current in an electrical conductor. One ampere of current represents one coulomb of electrical charge (6.24 × 
- Capacitance (C) —— The property of an electric conductor that characterizes its ability to store an electric charge.
- Capacitor —— An electrical component that stores an electric charge.
- Conductor —— A material that will carry electric current.
- Current —— The flow of electrical charge.
- Difference —— The answer to a subtraction problem.
- Energy —— The capacity of a physical system to perform work. There are two types of energy, kinetic and potential.
-->

## 4. 语法解析

<!-- TODO: 2~4 个语法点，格式：
### ① 语法点名称
**原句**：<必须逐字来自第 1 节原文>
**拆解**：主/谓/宾、从句、非谓语等成分分析
**要点**：为什么这样用、易错点、可迁移的搭配
-->
