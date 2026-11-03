# Capacitance

> 通用 Ch 12 · Capacitance · 原文 PDF 第 492 页

## 1. 原文

Another important property in AC circuits, besides resistance and inductance, is capacitance. While inductance is represented in a circuit by a coil, capacitance is represented by a capacitor. In its most basic form, the capacitor is constructed of two parallel plates separated by a nonconductor called a dielectric. In an electrical circuit, a capacitor serves as a reservoir or storehouse for electricity.

### Capacitors in Direct Current

When a capacitor is connected across a source of DC, such as a storage battery in the circuit shown in Figure 12-114A, and the switch is then closed, the plate marked B becomes positively charged, and the A plate negatively charged. Current flows in the external circuit during the time the electrons are moving from B to A. The current flow in the circuit is at a maximum the instant the switch is closed, but continually decreases thereafter until it reaches zero. The current becomes zero as soon as the difference in voltage of A and B becomes the same as the voltage of the battery. If the switch is opened as shown in Figure 12-114B, the plates remain charged. Once the capacitor is shorted, it discharges quickly as shown Figure 12-114C.

It should be clear that during the time the capacitor is being charged or discharged, there is current in the circuit, even though the circuit is broken by the gap between the capacitor plates. Current is present only during the time of charge and discharge, and this period of time is usually short.

### The Resistor/Capacitor (RC) Time Constant

The time required for a capacitor to attain a full charge is proportional to the capacitance and the resistance of the circuit. The resistance of the circuit introduces the element of time into the charging and discharging of a capacitor.

When a capacitor charges or discharges through a resistance, a certain amount of time is required for a full charge or discharge. The voltage across the capacitor does not change instantaneously. The rate of charging or discharging is determined by the time constant of the circuit. The time constant of a series resistor/capacitor (RC) circuit is a time interval that equals the product of the resistance in ohms and the capacitance in farad and is symbolized by the Greek letter tau (τ).

τ = RC The time in the formula is the time required to charge to 63 percent of the voltage of the source. The time required to bring the charge to about 99 percent of the source voltage is approximately 5 τ. [Figure 12-115] The measure of a capacitor’s ability to store charge is its capacitance. The symbol used for capacitance is the letter C.

As can be seen from Figure 12-115, there can be no continuous movement of DC through a capacitor. A good capacitor blocks DC and passes the effects of pulsing DC or AC.

### Units of Capacitance

Electrical charge, which is symbolized by the letter Q, is measured in units of coulombs. The coulomb is given by the letter C, as with capacitance. Unfortunately, this can be confusing. One coulomb of charge is defined as a charge having 6.28 × 1018 electrons. The basic unit of capacitance is the farad and is given by the letter f. By definition, one A B Equal heat dissipation in both circuits + − RVrms=Vdc RVrms farad is one coulomb of charge stored with one volt across the plates of the capacitor. The general formula for capacitance in terms of charge and voltage is:

Where C = E Q C = capacitance measured in farads E = applied voltage measured in volts Q = charge measured in coulombs In practical terms, one farad is a large amount of capacitance. Typically, in electronics, much smaller units are used. The two more common smaller units are the microfarad (μF), which is 10-6 farad, and the picofarad (pF), which is 10-12 farad.

### Voltage Rating of a Capacitor

Capacitors have their limits as to how much voltage can be applied across the plates. The aircraft technician must be aware of the voltage rating, which specifies the maximum DC voltage that can be applied without the risk of damage to the device. This voltage rating is typically called the breakdown voltage, the working voltage, or simply the voltage rating. If the voltage applied across the plates is too great, the dielectric breaks down and arcing occurs between the plates. The capacitor is then short circuited, and the possible flow of DC through it can cause damage to other parts of the equipment.

A capacitor that can be safely charged to 500 volts DC cannot be safely subjected to AC or pulsating DC whose effective values are 500 volts. An alternating voltage of 500 volts (RMS) has a peak voltage of 707 volts, and a capacitor to which it is applied should have a working voltage of at least 750 volts. The capacitor should be selected so that its working voltage is at least 50 percent greater than the highest voltage to be applied.

The voltage rating of the capacitor is a factor in determining the actual capacitance, because capacitance decreases as the thickness of the dielectric increases. A high-voltage capacitor that has a thick dielectric must have a larger plate area in order to have the same capacitance as a similar low voltage capacitor having a thin dielectric.

### Factors Affecting Capacitance

1. The capacitance of parallel plates is directly proportional to their area. A larger plate area produces a larger capacitance and a smaller area produces less capacitance. If we double the area of the plates, there is room for twice as much charge. The charge that a capacitor can hold at a given potential difference is doubled, and since C = Q/E, the capacitance is doubled.

2. The capacitance of parallel plates is inversely proportional to their spacing.

3. The dielectric material affects the capacitance of parallel plates. The dielectric constant of a vacuum is defined as 1, and that of air is very close to 1. These values are used as a reference, and all other materials have values specified in relation to air (vacuum).

The strength of some commonly used dielectric materials is listed in Figure 12-116. The voltage rating also depends on frequency because the losses, and the resultant heating effect, increase as the frequency increases.

### Types of Capacitors

Capacitors come in all shapes and sizes and are usually marked with their value in farads. They may also be divided into two groups: fixed and variable. The fixed capacitors, which have approximately constant capacitance, may then be further divided according to the type of dielectric used. Some varieties are: paper, oil, mica, electrolytic and ceramic capacitors. Figure 12-117 shows the schematic symbols for a fixed and variable capacitor.

#### Fixed Capacitors

Mica Capacitors The fixed mica capacitor is made of metal foil plates that are separated by sheets of mica, which form the dielectric. The whole assembly is covered in molded plastic, which keeps out moisture. Mica is an excellent dielectric and withstands higher voltages than paper without allowing arcing between the plates. Common values of mica capacitors range from approximately 50 microfarads to about 0.02 microfarads. [Figure 12-118]

The ceramic capacitor is constructed with materials, such as titanium acid barium for a dielectric. Internally these 63% 100% 90% 80% 70% 60% 50% 40% 30% 20% 10% 86% 95% 98% Voltage Current 1t Charging curve for a capacitor 2t 3t 4t 5t 99% A B C + − ++++ −−−− Open B A Capacitor being charged Capacitor retains charge Capacitor discharges + − ++++ −−−− Close Charge B A + − ++ −− Close ShortRemoved B A capacitors are not constructed as a coil, so they are well suited for use in high-frequency applications. They are shaped like a disk, available in very small capacitance values, and very small sizes. This type is fairly small, inexpensive, and reliable. Both the ceramic and the electrolytic are the most widely available and used capacitor.

Two kinds of electrolytic capacitors are in use: wet electrolytic and dry electrolytic. The wet electrolytic capacitor is designed of two metal plates separated by an electrolyte with an electrolyte dielectric, which is basically conductive salt in solvent. For capacitances greater than a few microfarads, the plate areas of paper or mica capacitors must become very large; thus, electrolytic capacitors are usually used instead. These units provide large capacitance in small physical sizes. Their values range from 1 to about 1,500 microfarads. Unlike the other types, electrolytic capacitors are generally polarized, with the positive lead marked with a “+” and the negative lead marked with a “−” and should only be subjected to direct voltage or pulsating direct voltage only.

The electrolyte in contact with the negative terminal, either in paste or liquid form, comprises the negative electrode. The dielectric is an exceedingly thin film of oxide deposited on the positive electrode of the capacitor. The positive electrode, which is an aluminum sheet, is folded to achieve maximum area. The capacitor is subjected to a forming process during manufacture in which current is passed through it. The flow of current results in the deposit of the thin coating of oxide on the aluminum plate.

The close spacing of the negative and positive electrodes gives rise to the comparatively high-capacitance value, but allows greater possibility of voltage breakdown and leakage of electrons from one electrode to the other.

The electrolyte of the dry electrolytic unit is a paste contained in a separator made of an absorbent material, such as gauze or paper. The separator not only holds the electrolyte in place but also prevents it from short circuiting the plates. Dry electrolytic capacitors are made in both cylindrical and rectangular block form and may be contained either within cardboard or metal covers. Since the electrolyte cannot spill, the dry capacitor may be mounted in any convenient position. [Figure 12-119]

Similar to the electrolytic, these capacitors are constructed with a material called tantalum, which is used for the electrodes. They are superior to electrolytic capacitors, having better temperature and frequency characteristics. When tantalum powder is baked in order to solidify it, a crack forms inside. This crack is used to store an electrical charge. Like electrolytic capacitors, the tantalum capacitors are also polarized and are indicated with the “+” and “−” symbols.

In this capacitor, a thin polyester film is used as a dielectric. These components are inexpensive, temperature stable, and widely used. Tolerance is approximately 5–10 percent. It Fixed Variable Dielectric K Dielectric Strength (volts per .001 inch)

Air 1.0 80 Paper (1) Paraffined 2.2 1,200 (2) Beeswaxed 3.1 1,800 Glass 4.2 200 Castor Oil 4.7 380 Bakelite 6.0 500 Mica 6.0 2,000 Fiber 6.5 50 can be quite large depending on capacity or rated voltage.

In radio and radar transmitters, voltages high enough to cause arcing, or breakdown, of paper dielectrics are often used. Consequently, in these applications capacitors that use oil or oil impregnated paper for the dielectric material are preferred. Capacitors of this type are considerably more expensive than ordinary paper capacitors, and their use is generally restricted to radio and radar transmitting equipment. [Figure 12-120]

#### Variable Capacitors

Variable capacitors are mostly used in radio tuning circuits, and they are sometimes called “tuning capacitors.” They have very small capacitance values, typically between 100 pF and 500 pF.

The trimmer is actually an adjustable or variable capacitor, which uses ceramic or plastic as a dielectric. Most of them are color coded to easily recognize their tunable size. The ceramic type has the value printed on them. Colors are: yellow (5 pF), blue (7 pF), white (10 pF), green (30 pF), and brown (60 pF).

A voltage-variable capacitor or varactor is also known as a variable capacitance diode or a varicap. This device utilizes the variation of the barrier width in a reversed-biased diode. Because the barrier width of a diode acts as a non-conductor, a diode forms a capacitor when reversed biased. Essentially, the N-type material becomes one plate and the junctions are the dielectric. If the reversed-bias voltage is increased, then the barrier width widens, effectively separating the two capacitor plates and reducing the capacitance.

### Capacitors in Series

When capacitors are placed in series, the effective plate separation is increased and the total capacitance is less than that of the smallest capacitor. Additionally, the series combination is capable of withstanding a higher total potential difference than any of the individual capacitors. Figure 12-121 is a simple series circuit. The bottom plate of C 1 and the top plate of C 2 is charged by electrostatic induction. The capacitors charge as current is established through the circuit. Since this is a series circuit, the current must be the same at all points. Since the current is the rate of flow of charge, the amount of charge (Q) stored by each capacitor is equal to the total charge.

Q T = Q1 + Q2 + Q3 According to Kirchhoff’s V oltage Law, the sum of the voltages across the charged capacitors must equal the total voltage, ET. This is expressed as:

E T = E1 + E2 + E3 Equation E = Q/C can now be substituted into the voltage equation where we now get:

= + + CT C1 C2 C3 QT Q1 Q2 Q3 Since the charge on all capacitors is equal, the Q terms can be factored out, leaving us with the equation:

= + + CT C1 C2 C3 1 1 1 1 Consider the following example:

If C1 = 10 μF, C2 = 5 μF and C3 = 8 μF Then = + + CT 10 μF 5 μF 8 μF 1 1 1 1 CT = = 2.35 μF 0.425 μF 1

### Capacitors in Parallel

When capacitors are connected in parallel, the effective plate area increases, and the total capacitance is the sum of the individual capacitances. Figure 12-122 shows a simplified parallel circuit. The total charging current from the source divides at the junction of the parallel branches. There is a separate charging current through each branch so that a different charge can be stored by each capacitor. Using Kirchhoff’s Current Law, the sum of all of the charging currents is then equal to the total current. The sum of the charges (Q) on the capacitors is equal to the total charge. The voltages (E) across all of the parallel branches are equal. With all of this in mind, a general equation for capacitors in parallel can be determined as:

Q T = Q1 + Q2 + Q3 Because Q = CE: CTET = C1E1 + C2E2 + C3E3 V oltages can be factored out because:

E T = E1 + E2 + E3 Leaving us with the equation for capacitors in parallel:

C T = C1 + C2 + C3 Consider the following example:

If C1 = 330 μF, C2 = 220 μF Then CT = 330 μF + 220 μF = 550 μF

### Capacitors in Alternating Current

If a source of AC is substituted for the battery, the capacitor acts quite differently than it does with DC. When AC is applied in the circuit, the charge on the plates constantly changes. [Figure 12-123] This means that electricity must flow first from Y clockwise around to X, then from X counterclockwise around to Y , then from Y clockwise around to X, and so on. Although no current flows through the insulator between the plates of the capacitor, it constantly flows in the remainder of the circuit between X and Y . In a circuit where there is only capacitance, current leads the applied voltage as contrasted with a circuit in which there is inductance, where the current lags the voltage.

### Capacitive Reactance Xc

The effectiveness of a capacitor in allowing an AC flow to pass depends upon the capacitance of the circuit and the applied frequency. To what degree a capacitor allows an AC flow to pass depends largely upon the capacitive value of the capacitor given in farads (f). The greater the capacitance of the capacitor, the greater the number of electrons, measured in Coulombs, necessary to bring the capacitor to a fully charged state. Once the capacitor approaches or actually reaches a fully charged condition, the polarity of the capacitor opposes the polarity of the applied voltage, essentially acting then as an open circuit. To further illustrate this characteristic and how it manifests itself in an AC circuit, consider the following. If a capacitor has a large capacitive value, meaning that it requires a relatively large number of electrons to bring it to a fully charged state, + − + − + − + − C1 C2 C3 + − + − + − + − C1 C2 C3 then a rather high-frequency current can alternate through the capacitor without the capacitor ever reaching a full charge. In this case, if the frequency is high enough and the capacitance large enough that there is never enough time for the capacitor to ever reach a full charge, it is possible that the capacitor may offer very little or no resistance to the current. However, the smaller the capacitance, the fewer electrons are required to bring it up to a full charge and it is more likely that the capacitor will build up enough of an opposing charge that it can present a great deal of resistance to the current if not to the point of behaving like an open circuit. In between these two extreme conditions lies a continuum of possibilities of current opposition depending on the combination of applied frequency and the selected capacitance. Current in an AC circuit can be controlled by changing the circuit capacitance in a similar manner that resistance can control the current. The actual AC reactance Xc, which just like resistance, is measured in ohms (Ω). Capacitive reactance Xc is determined by the following:

Xc = 2πfC 1 Where Xc = capacitive reactance f = frequency in cps C = capacity in farads 2π = 6.28

A series circuit is assumed in which the impressed voltage is 110 volts at 60 cps, and the capacitance of a condenser is 80 Mf. Find the capacitive reactance and the current flow.

To find capacitive reactance, the equation Xc = 1/(2πfC) is used. First, the capacitance, 80 Mf, is changed to farads by dividing 80 by 1,000,000, since 1 million microfarads is equal to 1 farad. This quotient equals 0.000080 farad. This is substituted in the equation and:

Xc = 6.28 × 60 × 0.000080 1 Xc = 33.2 ohms reactance Once the reactance has been determined, Ohm’s Law can then be used in the same manner as it is used in DC circuits to determine the current.

Current = , orCapacitive reactance V oltage I = Xc E Find the current flow:

I = Xc E I = 33.2 110 I = 3.31 amperes

### Capacitive Reactances in Series and in Parallel

When capacitors are connected in series, the total reactance is equal to the sum of the individual reactances. Thus, Xct = (Xc)1 + (Xc)2 The total reactance of capacitors connected in parallel is found in the same way total resistance is computed in a parallel circuit:

(Xc)t = + +1(Xc)1 1(Xc)2 1(Xc)3 1

### Phase of Current and Voltage in Reactive Circuits

Unlike a purely resistive circuit, the capacitive and inductive reactance has a significant effect on the phase relationship between the applied AC voltage and the corresponding X YAC generator current in the circuit.

In review, when current and voltage pass through zero and reach maximum value at the same time, the current and voltage are said to be in phase. [Figure 12-124A] If the current and voltage pass through zero and reach the maximum values at different times, the current and voltage are said to be out of phase. In a circuit containing only inductance, the current reaches a maximum value later than the voltage, lagging the voltage by 90°, or one-fourth cycle. [Figure 12-124B]

In a circuit containing only capacitance, the current reaches its maximum value ahead of the voltage and the current leads the voltage by 90°, or one-fourth cycle. [Figure 12-124C] The amount the current lags or leads the voltage in a circuit depends on the relative amounts of resistance, inductance, and capacitance in the circuit.

## 2. 中文翻译

<!-- TODO: 逐段翻译，段数与上面严格一一对应（68 段）。专业术语按行业惯例，数字与缩写保留。 -->

## 3. 专业词汇

<!-- TODO: 用表格 | 英文 | 词性 | 中文 | 本节语境 |，4~8 行。优先选下面 Glossary 里的词（本节原文出现过的）：
- Alternating current —— An electric current that reverses direction in a circuit at regular intervals.
- Capacitance (C) —— The property of an electric conductor that characterizes its ability to store an electric charge.
- Capacitive reactance (X c) —— The measure of a capacitor’s opposition to alternating current.
- Capacitor —— An electrical component that stores an electric charge.
- Conductor —— A material that will carry electric current.
- Coulomb —— A measure of electrical output. One coulomb is 6.24 × 1018 electrons.
- Current —— The flow of electrical charge.
- Difference —— The answer to a subtraction problem.
-->

## 4. 语法解析

<!-- TODO: 2~4 个语法点，格式：
### ① 语法点名称
**原句**：<必须逐字来自第 1 节原文>
**拆解**：主/谓/宾、从句、非谓语等成分分析
**要点**：为什么这样用、易错点、可迁移的搭配
-->
