# Series DC Circuits

> 通用 Ch 12 · Series DC Circuits · 原文 PDF 第 475 页

## 1. 原文

The series circuit is the most basic electrical circuit and provides a good introduction to basic circuit analysis. The series circuit represents the first building block for all of the circuits to be studied and analyzed. Figure 12-81 shows this simple circuit with nothing more than a voltage source or battery, a conductor, and a resistor. This is classified as a series circuit because the components are connected end-to- end, so that the same current flows through each component equally. There is only one path for the current to take and the battery and resistor are in series with each other. Next is to make a few additions to the simple circuit in Figure 12-81.

Figure 12-82 shows an additional resistor and a little more a guard.

A B detail regarding the values. With these values, we can now begin to learn more about the nature of the circuit. In this configuration, there is a 12-volt DC source in series with two resistors, R1 = 10 Ω and R2 = 30 Ω. For resistors in a series configuration, the total resistance of the circuit is equal to the sum of the individual resistors. The basic formula is:

R T = R1 + R2 + R3 + ………RN For Figure 12-82, this will be: R T = 10 Ω + 30 Ω R T = 40 Ω Now that the total resistance of the circuit is known, the current for the circuit can be determined. In a series circuit, the current cannot be different at different points within the circuit. The current through a series circuit is always the same through each element and at any point. Therefore, the current in the simple circuit can now be determined using Ohm’s Law:

Solve for current, ERI = The variables, E = 12 V and RT = 40 Ω Substitute variables, 12 V40 ΩI = Current in circuits, I = 0.3 A Ohm’s Law describes a relationship between the variables of voltage, current, and resistance that is linear and easy to illustrate with a few extra calculations. First is the act of changing the total resistance of the circuit while the other two remain constant. In this example, the R T of the circuit in Figure 12-82 is doubled. The effects on the total current in the circuit are:

Solve for current, ERI = The variables, E = 12 V and RT = 80 Ω Substitute variables, 12 V80 ΩI = Current in circuits, I = 0.15 A It can be seen quantitatively and intuitively that when the resistance of the circuit is doubled, the current is reduced by half the original value.

Next, reduce the RT of the circuit in Figure 12-82 to half of its original value. The effects on the total current are:

Multiple poles Schematic Symbol for a Relay Relay Illustration A2 B2 A3 A1 B3 B1 C C X1 X2 Normally closed (NC)

Magnetic field Common (C) or Arm Electromagnet pulls contact down NC NO NC NO X1 X2 X1 X2 (+)

N S + − + 12V 30Ω R2 10Ω R1 − Formula, E = I (R)

Solve for current, ERI = The variables, E = 12 V and RT = 20 Ω Substitute variables, 12 V20 ΩI = Current in circuits, I = 0.6 A

### Voltage Drops & Further Application of Ohm’s Law

The example circuit in Figure 12-83 is used to illustrate the idea of voltage drop. It is important to differentiate between voltage and voltage drop when discussing series circuits. V oltage drop refers to the loss in electrical pressure or emf caused by forcing electrons through a resistor. Because there are two resistors in the example, there are separate voltage drops. Each drop is associated with each individual resistor. The amount of electrical pressure required to force a given number of electrons through a resistance is proportional to the size of the resistor.

In Figure 12-83 , the values used to illustrate the idea of voltage drop are:

Current, I = 1 mA R 1 = 1 kΩ R 2 = 3 kΩ R 3 = 5 kΩ The voltage drop across each resistor is calculated using Ohm’s Law. The drop for each resistor is the product of each resistance and the total current in the circuit. Keep in mind that the same current flows through series resistor.

V oltage across R1: E1 = IT (R1)

E1 = 1 mA (1 kΩ) = 1 volt V oltage across R2: E2 = IT (R2)

E2 = 1 mA (3 kΩ) = 3 volt V oltage across R3: E3 = IT (R3)

E3 = 1 mA (5 kΩ) = 5 volt The source voltage can now be determined, which can then be used to confirm the calculations for each voltage drop. Using Ohm’s Law:

Source voltage = current × the total resistance ES = I (RT)

+ 5 kΩ R3 1 kΩ R1IT 1 mA 3 kΩ R2 − RT = 1 kΩ + 3 kΩ + 5 kΩ RT = 9 kΩ Now: ES = I (RT)

Substitute ES = 1 mA (9 kΩ)

ES = 9 volts Simple checks to confirm the calculation and to illustrate the concept of the voltage drop add up the individual values of the voltage drops and compare them to the results of the above calculation.

1 volt + 3 volts + 5 volts = 9 volts

### Voltage Sources in Series

A voltage source is an energy source that provides a constant voltage to a load. Two or more of these sources in series equals the algebraic sum of all the sources connected in series. The significance of pointing out the algebraic sum is to indicate that the polarity of the sources must be considered when adding up the sources. The polarity is indicated by a plus or minus sign depending on the source’s position in the circuit.

In Figure 12-84, all of the sources are in the same direction in terms of their polarity. All of the voltages have the same sign when added up. In the case of Figure 12-84, three cells of a value of 1.5 volts are in series with the polarity in the same direction. The addition is simple enough:

ET = 1.5v + 1.5v + 1.5v = +4.5 volts However, in Figure 12-85, one of the three sources has been turned around, and the polarity opposes the other two sources. Again the addition is simple:

ET = + 1.5v − 1.5v + 1.5v = +1.5 volts

### Kirchhoff’s Voltage Law

A law of basic importance to the analysis of an electrical circuit is Kirchhoff’s V oltage Law. This law simply states that the algebraic sum of all voltages around a closed path or loop is zero. Another way of saying it: the sum of all the voltage drops equals the total source voltage. A simplified formula showing this law is shown below:

With three resistors in the circuit: E S – E1 – E2 – E3 … –EN = 0 volts Notice that the sign of the source is opposite that of the individual voltage drops. Therefore, the algebraic sum equals zero. Written another way:

E S = E1 + E2 + E3 … +EN The source voltage equals the sum of the voltage drops. The polarity of the voltage drop is determined by the direction of the current flow. When going around the circuit, notice that the polarity of the resistor is opposite that of the source voltage. The positive on the resistor is facing the positive on the source, and the negative on the resistor is facing the negative on the source.

Figure 12-86 illustrates the very basic idea of Kirchhoff’s V oltage Law. There are two resistors in this example. One has a drop of 14 volts and the other has a drop of 10 volts. The source voltage must equal the sum of the voltage drops around the circuit. By inspection, it is easy to determine the source voltage as 24 volts.

Figure 12-87 shows a series circuit with three voltage drops and one voltage source rated at 24 volts. Two of the voltage drops are known. However, the third is not known. Using Kirchhoff’s V oltage Law, the third voltage drop can be determined.

With three resistors in the circuit: E S – E1 – E2 – E3 = 0 volts Substitute the known values:

24v – 12v – 10v − E3 = 0 Collect known values: 2v – E3 = 0 Solve for the unknown: E3 = 2 volts Determine the value of E4 in Figure 12-88. For this example, I = 200mA. First, the voltage drop across each of the individual resistors must be determined.

E1 = (200 mA) (10 Ω)

1.5V 1.5V + 1.5V − +−+− 1.5V 1.5V + ES=24V − 14V 10V +− +− + 10V E224VES − + − + 12V E1 − + ?

V oltage drop across R1 E1 = 2 volts E2 = I (R2)

E2 = (200 mA) (50 Ω)

V oltage drop across R2 E2 = 10 volts E3 = I (R3)

E3 = (200 mA) (100 Ω)

V oltage drop across R3 E3 = 20 volts Kirchhoff’s V oltage Law is now employed to determine the voltage drop across E4.

With four resistors in the circuit E S – E1 – E2 – E3 – E4 = 0 volts Substituting values:

100v – 2v – 10v – 20v – E4 = 0 Combine: 68v – E4 = 0 Solve for unknown: E4 = 68v Using Ohm’s Law and substituting in E 4, the value for R 4 can now be determined.

Ohm’s Law: EIR = Specific application: E4IR4 = Substitute values: 68 V200 mAR4 = Value for R4: R 4 = 340 Ω

### Voltage Dividers

V oltage dividers are devices that make it possible to obtain more than one voltage from a single power source. A voltage divider usually consists of a resistor, or resistors connected in series, with fixed or movable contacts and two fixed terminal contacts. As current flows through the resistor, different voltages can be obtained between the contacts.

Series circuits are used for voltage dividers. The voltage divider rule allows the technician to calculate the voltage across one or a combination of series resistors without having to first calculate the current in the circuit. [Figure 12-89] Because the current flows through each resistor, the voltage drops are proportional to the ohmic values of the constituent resistors. To understand how a voltage divider works, examine Figure 12-90 carefully and observe the following:

Each load draws a given amount of current: I 1, I 2, I 3. In + + 100 Ω R3 10 Ω R1 50 Ω R2 − + − − +− ?

R4 +− 100 VES C B A R1 R2R3 addition to the load currents, some bleeder current (IB) flows. The current (IT) is drawn from the power source and is equal to the sum of all currents.

The voltage at each point is measured with respect to a common point. Note that the common point is the point at which the total current (IT) divides into separate currents (I1, I2, I3). Each part of the voltage divider has a different current flowing in it. The current distribution is as follows:

Through R1 — bleeder current (IB) Through R2 — IB + I1 Through R3 — IB + I1, + I2 The voltage across each resistor of the voltage divider is:

90 volts across R1 60 volts across R2 50 volts across R3 The voltage divider circuit discussed up to this point has had one side of the power supply (battery) at ground potential. In Figure 12-91, the common reference point (ground symbol) has been moved to a different point on the voltage divider. The voltage drop across R1 is 20 volts; however, since tap A is connected to a point in the circuit that is at the same potential as the negative side of the battery, the voltage between tap A and the reference point is a negative (−) 20 volts. Since resistors R2 and R3 are connected to the positive side of the battery, the voltages between the reference point and tap B or C are positive.

The following rules provide a simple method of determining negative and positive voltages: (1) If current enters a resistance flowing away from the reference point, the voltage drop across that resistance is positive in respect to the reference point; (2) if current flows out of a resistance toward the reference point, the voltage drop across that resistance is negative in respect to the reference point. It is the location of the reference point that determines whether a voltage is negative or positive.

Tracing the current flow provides a means for determining the voltage polarity. Figure 12-92 shows the same circuit with the polarities of the voltage drops and the direction of current flow indicated.

The current flows from the negative side of the battery to R1. Tap A is at the same potential as the negative terminal of the battery since the slight voltage drop caused by the resistance of the conductor is disregarded; however, 20 volts of the source voltage are required to force the current through R 1 and this 20-volt drop has the polarity indicated. Stated another way, there are only 80 volts of electrical pressure left in the circuit on the ground side of R1.

When the current reaches tap B, 30 more volts have been used to move the electrons through R 2, and in a similar manner the remaining 50 volts are used for R 3. But the voltages across R2 and R3 are positive voltages, since they are above ground potential.

Figure 12-93 shows the voltage divider used previously. The voltage drops across the resistances are the same; however, the reference point (ground) has been changed. The voltage between ground and tap A is now a negative 100 volts, or the applied voltage.

The voltage between ground and tap B is a negative 80 volts, and the voltage between ground and tap C is a negative 50 volts.

### Determining the Voltage Divider Formula

Figure 12-94 shows the example network of four resistors and a voltage source. With a few simple calculations, a formula for determining the voltage divisions in a series circuit can be determined.

The voltage drop across any particular resistor shall be called EX, where the subscript x is the value of a particular resistor (1, 2, 3, or 4). Using Ohm’s Law, the voltage drop across any C B A 100 V R3=100 Ω R2=60 Ω R1=40 Ω 50 V 30 V 20 V C B A 100 V R3 R2 R1 +50 V + − + − + − +30 V −20 V 200v 150v 90v IT IT IB I1 I2 I3 R1 R2E R3 Load Load Load C B A 100 V R3 R2 R1 50 V 30 V 20 V resistor can be determined.

Ohm’s Law: EX = I (RX)

As seen earlier in the handbook, the current is equal to the source voltage divided by the total resistance of the series circuit.

Current: ESRTI = The current equation can now be substituted into the equation for Ohm’s Law.

Substitute: ES RT EX = ( )(RX) Algebraic rearrange: RX RT EX = ( )(ES) This equation is the general voltage divider formula. The explanation of this formula is that the voltage drop across any resistor or combination of resistors in a series circuit is equal to the ratio of the resistance value to the total resistance, divided by the value of the source voltage. Figure 12-95 illustrates this with a network of three resistors and one voltage source.

RX RT EX = ( ) ES R T = 100 Ω + 300 Ω + 600 Ω = 1,000 Ω E S = 10 V V oltage drop over 100 Ω resistor is:

100 Ω 1,000 ΩEX = ( ) 100 V E 100Ω = 10 V V oltage drop over 300 Ω resistor is:

300 Ω 1,000 ΩEX = ( ) 100 V E 100 Ω = 30 V V oltage drop over 600 Ω resistor is:

600 Ω 1,000 ΩEX = ( ) 100 V E 100Ω = 60 V + − + − + − + − + − R1 R2 ES R3 R4 E3 E4 E2 E1 100 Ω 300 Ω 600 Ω + − + − + − + − R1 R2ES100 v R3 Checking work E T = 10 V + 30 V + 60 V = 100 V

## 2. 中文翻译

<!-- TODO: 逐段翻译，段数与上面严格一一对应（72 段）。专业术语按行业惯例，数字与缩写保留。 -->

## 3. 专业词汇

<!-- TODO: 用表格 | 英文 | 词性 | 中文 | 本节语境 |，4~8 行。优先选下面 Glossary 里的词（本节原文出现过的）：
- Addition —— The process in which the value of one number is added to the value of another.
- Conductor —— A material that will carry electric current.
- Current —— The flow of electrical charge.
- Energy —— The capacity of a physical system to perform work. There are two types of energy, kinetic and potential.
- Force —— The intensity of an impetus, or the intensity of an input.
- Ohm’s Law —— Explains the relationship between voltage, current, and resistance in an electrical circuit, and states that current flow in an electrical circuit is directly p
- Power (exponent) —— A shorthand method of indicating how many times a number, called the base, is multiplied by itself. For example, in the number 43, 3 is the power, or exponent, 
- Power —— Power is the time rate at which work is done or energy is transferred.
-->

## 4. 语法解析

<!-- TODO: 2~4 个语法点，格式：
### ① 语法点名称
**原句**：<必须逐字来自第 1 节原文>
**拆解**：主/谓/宾、从句、非谓语等成分分析
**要点**：为什么这样用、易错点、可迁移的搭配
-->
