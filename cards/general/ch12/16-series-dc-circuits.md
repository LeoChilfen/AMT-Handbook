# Series DC Circuits

> 通用 Ch 12 · Series DC Circuits · 原文 PDF 第 475 页

## 1. 原文

The series circuit is the most basic electrical circuit and provides a good introduction to basic circuit analysis. The series circuit represents the first building block for all of the circuits to be studied and analyzed. This simple circuit has nothing more than a voltage source or battery, a conductor, and a resistor. This is classified as a series circuit because the components are connected end-to-end, so that the same current flows through each component equally. There is only one path for the current to take and the battery and resistor are in series with each other. Next is to make a few additions to the simple circuit.

An additional resistor and a little more detail are added to the circuit.

Detail regarding the values. With these values, we can now begin to learn more about the nature of the circuit. In this configuration, there is a 12-volt DC source in series with two resistors, R1 = 10 Ω and R2 = 30 Ω. For resistors in a series configuration, the total resistance of the circuit is equal to the sum of the individual resistors. The basic formula is:

R T = R1 + R2 + R3 + ………RN For this circuit, this will be: R T = 10 Ω + 30 Ω R T = 40 Ω Now that the total resistance of the circuit is known, the current for the circuit can be determined. In a series circuit, the current cannot be different at different points within the circuit. The current through a series circuit is always the same through each element and at any point. Therefore, the current in the simple circuit can now be determined using Ohm’s Law:

Solve for current, ERI = The variables, E = 12 V and RT = 40 Ω Substitute variables, 12 V40 ΩI = Current in circuits, I = 0.3 A Ohm’s Law describes a relationship between the variables of voltage, current, and resistance that is linear and easy to illustrate with a few extra calculations. First is the act of changing the total resistance of the circuit while the other two remain constant. In this example, the R T of the circuit is doubled. The effects on the total current in the circuit are:

Solve for current, ERI = The variables, E = 12 V and RT = 80 Ω Substitute variables, 12 V80 ΩI = Current in circuits, I = 0.15 A It can be seen quantitatively and intuitively that when the resistance of the circuit is doubled, the current is reduced by half the original value.

Next, reduce the RT of the circuit to half of its original value. The effects on the total current are:

Multiple poles Schematic Symbol for a Relay Relay Illustration A2 B2 A3 A1 B3 B1 C C X1 X2 Normally closed (NC)

Magnetic field Common (C) or Arm Electromagnet pulls contact down NC NO NC NO X1 X2 X1 X2 (+)

N S + − + 12V 30Ω R2 10Ω R1 − Formula, E = I (R)

Solve for current, ERI = The variables, E = 12 V and RT = 20 Ω Substitute variables, 12 V20 ΩI = Current in circuits, I = 0.6 A.

### Voltage Drops & Further Application of Ohm’s Law

The example circuit is used to illustrate the idea of voltage drop. It is important to differentiate between voltage and voltage drop when discussing series circuits. V oltage drop refers to the loss in electrical pressure or emf caused by forcing electrons through a resistor. Because there are two resistors in the example, there are separate voltage drops. Each drop is associated with each individual resistor. The amount of electrical pressure required to force a given number of electrons through a resistance is proportional to the size of the resistor.

The values used to illustrate the idea of voltage drop are:

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

All of the sources are in the same direction in terms of their polarity. All of the voltages have the same sign when added up. In this case, three cells of a value of 1.5 volts are in series with the polarity in the same direction. The addition is simple enough:

ET = 1.5v + 1.5v + 1.5v = +4.5 volts However, one of the three sources has been turned around, and the polarity opposes the other two sources. Again the addition is simple:

ET = + 1.5v − 1.5v + 1.5v = +1.5 volts

### Kirchhoff’s Voltage Law

A law of basic importance to the analysis of an electrical circuit is Kirchhoff’s V oltage Law. This law simply states that the algebraic sum of all voltages around a closed path or loop is zero. Another way of saying it: the sum of all the voltage drops equals the total source voltage. A simplified formula showing this law is shown below:

With three resistors in the circuit: E S – E1 – E2 – E3 … –EN = 0 volts Notice that the sign of the source is opposite that of the individual voltage drops. Therefore, the algebraic sum equals zero. Written another way:

E S = E1 + E2 + E3 … +EN The source voltage equals the sum of the voltage drops. The polarity of the voltage drop is determined by the direction of the current flow. When going around the circuit, notice that the polarity of the resistor is opposite that of the source voltage. The positive on the resistor is facing the positive on the source, and the negative on the resistor is facing the negative on the source.

The very basic idea of Kirchhoff’s V oltage Law is illustrated here. There are two resistors in this example. One has a drop of 14 volts and the other has a drop of 10 volts. The source voltage must equal the sum of the voltage drops around the circuit. By inspection, it is easy to determine the source voltage as 24 volts.

A series circuit has three voltage drops and one voltage source rated at 24 volts. Two of the voltage drops are known. However, the third is not known. Using Kirchhoff’s V oltage Law, the third voltage drop can be determined.

With three resistors in the circuit: E S – E1 – E2 – E3 = 0 volts Substitute the known values:

24v – 12v – 10v − E3 = 0 Collect known values: 2v – E3 = 0 Solve for the unknown: E3 = 2 volts Determine the value of E4. For this example, I = 200mA. First, the voltage drop across each of the individual resistors must be determined.

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

Series circuits are used for voltage dividers. The voltage divider rule allows the technician to calculate the voltage across one or a combination of series resistors without having to first calculate the current in the circuit. Because the current flows through each resistor, the voltage drops are proportional to the ohmic values of the constituent resistors. To understand how a voltage divider works, examine the voltage divider carefully and observe the following:

Each load draws a given amount of current: I 1, I 2, I 3. In + + 100 Ω R3 10 Ω R1 50 Ω R2 − + − − +− ?

R4 +− 100 VES C B A R1 R2R3 addition to the load currents, some bleeder current (IB) flows. The current (IT) is drawn from the power source and is equal to the sum of all currents.

The voltage at each point is measured with respect to a common point. Note that the common point is the point at which the total current (IT) divides into separate currents (I1, I2, I3). Each part of the voltage divider has a different current flowing in it. The current distribution is as follows:

Through R1 — bleeder current (IB) Through R2 — IB + I1 Through R3 — IB + I1, + I2 The voltage across each resistor of the voltage divider is:

90 volts across R1 60 volts across R2 50 volts across R3 The voltage divider circuit discussed up to this point has had one side of the power supply (battery) at ground potential. The common reference point (ground symbol) has been moved to a different point on the voltage divider. The voltage drop across R1 is 20 volts; however, since tap A is connected to a point in the circuit that is at the same potential as the negative side of the battery, the voltage between tap A and the reference point is a negative (−) 20 volts. Since resistors R2 and R3 are connected to the positive side of the battery, the voltages between the reference point and tap B or C are positive.

The following rules provide a simple method of determining negative and positive voltages: (1) If current enters a resistance flowing away from the reference point, the voltage drop across that resistance is positive in respect to the reference point; (2) if current flows out of a resistance toward the reference point, the voltage drop across that resistance is negative in respect to the reference point. It is the location of the reference point that determines whether a voltage is negative or positive.

Tracing the current flow provides a means for determining the voltage polarity. The same circuit is shown with the polarities of the voltage drops and the direction of current flow indicated.

The current flows from the negative side of the battery to R1. Tap A is at the same potential as the negative terminal of the battery since the slight voltage drop caused by the resistance of the conductor is disregarded; however, 20 volts of the source voltage are required to force the current through R 1 and this 20-volt drop has the polarity indicated. Stated another way, there are only 80 volts of electrical pressure left in the circuit on the ground side of R1.

When the current reaches tap B, 30 more volts have been used to move the electrons through R 2, and in a similar manner the remaining 50 volts are used for R 3. But the voltages across R2 and R3 are positive voltages, since they are above ground potential.

The voltage divider used previously is shown again. The voltage drops across the resistances are the same; however, the reference point (ground) has been changed. The voltage between ground and tap A is now a negative 100 volts, or the applied voltage.

The voltage between ground and tap B is a negative 80 volts, and the voltage between ground and tap C is a negative 50 volts.

### Determining the Voltage Divider Formula

The example network consists of four resistors and a voltage source. With a few simple calculations, a formula for determining the voltage divisions in a series circuit can be determined.

The voltage drop across any particular resistor shall be called EX, where the subscript x is the value of a particular resistor (1, 2, 3, or 4). Using Ohm’s Law, the voltage drop across any C B A 100 V R3=100 Ω R2=60 Ω R1=40 Ω 50 V 30 V 20 V C B A 100 V R3 R2 R1 +50 V + − + − + − +30 V −20 V 200v 150v 90v IT IT IB I1 I2 I3 R1 R2E R3 Load Load Load C B A 100 V R3 R2 R1 50 V 30 V 20 V resistor can be determined.

Ohm’s Law: EX = I (RX)

As seen earlier in the handbook, the current is equal to the source voltage divided by the total resistance of the series circuit.

Current: ESRTI = The current equation can now be substituted into the equation for Ohm’s Law.

Substitute: ES RT EX = ( )(RX) Algebraic rearrange: RX RT EX = ( )(ES) This equation is the general voltage divider formula. The explanation of this formula is that the voltage drop across any resistor or combination of resistors in a series circuit is equal to the ratio of the resistance value to the total resistance, divided by the value of the source voltage. A network of three resistors and one voltage source illustrates this.

RX RT EX = ( ) ES R T = 100 Ω + 300 Ω + 600 Ω = 1,000 Ω E S = 10 V V oltage drop over 100 Ω resistor is:

100 Ω 1,000 ΩEX = ( ) 100 V E 100Ω = 10 V V oltage drop over 300 Ω resistor is:

300 Ω 1,000 ΩEX = ( ) 100 V E 100 Ω = 30 V V oltage drop over 600 Ω resistor is:

600 Ω 1,000 ΩEX = ( ) 100 V E 100Ω = 60 V + − + − + − + − + − R1 R2 ES R3 R4 E3 E4 E2 E1 100 Ω 300 Ω 600 Ω + − + − + − + − R1 R2ES100 v R3 Checking work E T = 10 V + 30 V + 60 V = 100 V

## 2. 中文翻译

串联电路是最基本的电气电路，是学习基本电路分析的良好入门。串联电路是后续所有要学习和分析的电路的第一块构建基础。这个简单电路只有电压源或电池、一根导线和一只电阻。之所以归为串联电路，是因为各元件首尾相连，使同一电流等量流过每个元件。电流只有一条通路，电池与电阻互为串联。接下来，要给这个简单电路做几处增补。

在电路中又增加了一只电阻，并补充了更多细节。

关于数值的细节。有了这些数值，我们现在可以开始更多地了解这个电路的性质。在这种配置中，12 V 直流电源与两只电阻 R1 = 10 Ω、R2 = 30 Ω 串联。对于串联配置的电阻，电路的总电阻等于各电阻之和。基本公式为：

R T = R1 + R2 + R3 + ………RN。对这个电路而言，即为：R T = 10 Ω + 30 Ω，R T = 40 Ω。既然电路的总电阻已知，就可以确定电路中的电流。在串联电路中，电流不可能在电路内不同点上有差异。串联电路中的电流在每个元件、每个点上始终相同。因此，用欧姆定律就可以确定这个简单电路中的电流：

求解电流，I = E/R。已知变量，E = 12 V，RT = 40 Ω。代入变量，I = 12 V/40 Ω。电路中的电流，I = 0.3 A。欧姆定律描述了电压、电流、电阻三者之间的线性关系，用几次额外计算就很容易说明。首先是保持另外两个量不变而改变电路总电阻的做法。在本例中，电路的总电阻 RT 加倍。对电路总电流的影响为：

求解电流，I = E/R。已知变量，E = 12 V，RT = 80 Ω。代入变量，I = 12 V/80 Ω。电路中的电流，I = 0.15 A。可以定量而直观地看出：电路电阻加倍时，电流减小为原值的一半。

接下来，把电路的总电阻 RT 减小到原值的一半。对总电流的影响为：

（原文此处为图注碎片，为继电器的原理图符号与实物图例：多极触点、线圈端子 X1 与 X2、常闭 NC 触点等）

（原文此处为图注碎片，为继电器内部结构标注：磁场、公共端 C 或衔铁、电磁铁吸下触点、常闭 NC 与常开 NO 触点、线圈端子 X1 与 X2 及正极标记）

（原文此处为图注碎片，为 12 V 电源与 R1 = 10 Ω、R2 = 30 Ω 串联的示意图，并标有磁极 N、S 与极性符号）公式：E = I（R）

求解电流，I = E/R。已知变量，E = 12 V，RT = 20 Ω。代入变量，I = 12 V/20 Ω。电路中的电流，I = 0.6 A。

### 电压降与欧姆定律的进一步应用

示例电路用来说明电压降的概念。讨论串联电路时，必须把电压与电压降区分开来。电压降是指迫使电子通过电阻时造成的电压力或电动势的损失。由于示例中有两只电阻，因此有各自独立的电压降。每个电压降都与各自的电阻相关联。迫使给定数量的电子通过电阻所需的电压力大小与电阻的大小成正比。

用以说明电压降概念的数值为：

电流 I = 1 mA，R1 = 1 kΩ，R2 = 3 kΩ，R3 = 5 kΩ。每只电阻上的电压降都用欧姆定律计算。每只电阻的电压降等于该电阻与电路总电流的乘积。要记住，同一电流流过串联的每一只电阻。

R1 上的电压：E1 = IT (R1)

E1 = 1 mA（1 kΩ）= 1 V。R2 上的电压：E2 = IT (R2)

E2 = 1 mA（3 kΩ）= 3 V。R3 上的电压：E3 = IT (R3)

E3 = 1 mA（5 kΩ）= 5 V。现在可以求出电源电压，再用它来验证各电压降的计算。用欧姆定律：

电源电压 = 电流 × 总电阻，ES = I (RT)

（原文此处为图注碎片，为串联电路示意：R1 = 1 kΩ、R2 = 3 kΩ、R3 = 5 kΩ，电流 IT = 1 mA）RT = 1 kΩ + 3 kΩ + 5 kΩ，RT = 9 kΩ。现在：ES = I (RT)

代入，ES = 1 mA（9 kΩ）

ES = 9 V。用于验证计算、并说明电压降概念的简单检查方法，是把各电压降的值相加，再与上面计算的结果比较。

1 V + 3 V + 5 V = 9 V

### 串联的电压源

电压源是向负载提供恒定电压的能量源。两个或更多这样的电源串联，等于所有串联电源的代数和。指出“代数和”的意义在于：把各电源相加时必须考虑其极性。极性由正号或负号表示，取决于电源在电路中的位置。

在所有电源的极性方向相同时，相加时所有电压取相同的符号。本例中，三节 1.5 V 的电池按同一极性方向串联。相加很简单：

ET = 1.5v + 1.5v + 1.5v = +4.5 V。然而在下一种情形中，三个电源中的一个被反接，其极性与另外两个相反。相加同样简单：

ET = + 1.5v − 1.5v + 1.5v = +1.5 V

### 基尔霍夫电压定律

对电路分析具有根本重要性的一条定律是基尔霍夫电压定律。这条定律简单地说：沿闭合路径或回路的所有电压的代数和为零。换句话说：所有电压降之和等于电源总电压。表示这一定律的简化公式如下：

当电路中有三只电阻时：ES – E1 – E2 – E3 … –EN = 0 V。注意电源的符号与各电压降的符号相反，因此代数和为零。也可以写成：

ES = E1 + E2 + E3 … +EN。电源电压等于各电压降之和。电压降的极性由电流方向决定。绕电路一周时注意，电阻的极性与电源电压的极性相反。电阻的正极朝向电源的正极，电阻的负极朝向电源的负极。

这一例子说明了基尔霍夫电压定律最基本的思想。本例中有两只电阻。一只上的电压降为 14 V，另一只为 10 V。电源电压必须等于绕电路各电压降之和。只需一看便可确定电源电压为 24 V。

一个串联电路有三处电压降和一个额定 24 V 的电源。其中两处电压降已知，第三处未知。用基尔霍夫电压定律可以求出第三处电压降。

当电路中有三只电阻时：ES – E1 – E2 – E3 = 0 V。代入已知值：

24v – 12v – 10v − E3 = 0。合并已知值：2v – E3 = 0。求解未知量：E3 = 2 V。求 E4 的值。本例中 I = 200 mA。首先必须求出各只电阻上的电压降。

E1 =（200 mA）（10 Ω）

（原文此处为图注碎片，为 1.5 V 电池组、电源 ES = 24 V 及 14 V、10 V、12 V 电压降的标示图）

R1 上的电压降，E1 = 2 V。E2 = I (R2)

E2 =（200 mA）（50 Ω）

R2 上的电压降，E2 = 10 V。E3 = I (R3)

E3 =（200 mA）（100 Ω）

R3 上的电压降，E3 = 20 V。现在用基尔霍夫电压定律求 E4 上的电压降。

当电路中有四只电阻时：ES – E1 – E2 – E3 – E4 = 0 V。代入数值：

100v – 2v – 10v – 20v – E4 = 0。合并：68v – E4 = 0。求解未知量：E4 = 68v。用欧姆定律并代入 E4，即可求出 R4 的值。

欧姆定律：R = E/I。具体应用：R4 = E4/I。代入数值：R4 = 68 V/200 mA。R4 的值：R4 = 340 Ω。

### 分压器

分压器是能够从单一电源获得不止一个电压的装置。分压器通常由一只电阻或若干串联的电阻构成，带有固定或可动的触点以及两个固定端子触点。电流流过电阻时，各触点之间便可取得不同的电压。

串联电路用于构成分压器。分压器法则使技术人员无需先计算电路中的电流，就能算出一只或若干只串联电阻上的电压。因为电流流过每只电阻，各电压降与各组成电阻的欧姆值成正比。要理解分压器如何工作，应仔细研究下面的分压器并注意以下几点：

每只负载吸取给定的电流：I1、I2、I3。（原文此处为图注碎片，为分压器示意图及抽头 A、B、C 的标示）

（原文此处为图注碎片，为 100 V 电源 ES 与 R1、R2、R3 的标示）除各负载电流之外，还有一部分泄放电流（IB）流过。总电流（IT）取自电源，等于所有电流之和。

每一点的电压都是相对于一个公共点测量的。注意公共点就是总电流（IT）分成各分电流（I1、I2、I3）的那一点。分压器的每一部分流过的电流各不相同。电流分配如下：

流过 R1 的为泄放电流（IB）；流过 R2 的为 IB + I1；流过 R3 的为 IB + I1 + I2。分压器各电阻上的电压为：

R1 上为 90 V；R2 上为 60 V；R3 上为 50 V。到此为止讨论的分压器电路，电源（电池）的一侧处于地电位。在这个电路中，公共参考点（接地符号）已移到分压器上的另一位置。R1 上的电压降为 20 V；但由于抽头 A 接在电路上与电池负极电位相同的一点，抽头 A 与参考点之间的电压为负（−）20 V。由于电阻 R2 和 R3 接在电池的正极侧，参考点与抽头 B 或 C 之间的电压为正。

以下规则提供了确定负电压与正电压的简便方法：（1）若电流离开参考点流入某一电阻，则该电阻上的电压降相对参考点为正；（2）若电流从某一电阻流出、流向参考点，则该电阻上的电压降相对参考点为负。决定电压是正是负的，是参考点的位置。

追踪电流的流向是确定电压极性的手段。同一电路给出了各电压降的极性和电流方向。

电流从电池负极流向 R1。由于导线电阻引起的微小电压降可忽略，抽头 A 与电池负极端的电位相同；然而，电源电压中有 20 V 用于迫使电流通过 R1，这 20 V 的电压降具有所示的极性。换句话说，在 R1 的接地侧，电路中只剩下 80 V 的电压力。

当电流到达抽头 B 时，又有 30 V 用于推动电子通过 R2，同样地，剩余的 50 V 用于 R3。但 R2 和 R3 上的电压是正电压，因为它们处于地电位之上。

前面用过的分压器再次给出。各电阻上的电压降相同，但参考点（地）已改变。此时地与抽头 A 之间的电压为负 100 V，即所加电压。

地与抽头 B 之间的电压为负 80 V，地与抽头 C 之间的电压为负 50 V。

### 推导分压器公式

本例的网络由四只电阻和一个电压源组成。经过几项简单计算，就可以得出用于确定串联电路各分压的公式。

任一只电阻上的电压降称为 EX，其中下标 x 为某只电阻的编号（1、2、3 或 4）。用欧姆定律即可求出任一只电阻上的电压降。（原文此处为图注碎片，为各分压器示例的电路标示图）

欧姆定律：EX = I (RX)

如手册前文所述，电流等于电源电压除以串联电路的总电阻。

电流：I = ES/RT。现在可以把电流方程代入欧姆定律的方程。

代入：EX =（ES/RT）（RX）。代数整理：EX =（RX/RT）（ES）。这个方程就是通用的分压器公式。该公式的含义是：串联电路中任一只电阻或任意电阻组合上的电压降，等于该电阻值与总电阻之比乘以电源电压的值。用三只电阻和一个电压源组成的网络可以说明这一点。

EX =（RX/RT）ES，RT = 100 Ω + 300 Ω + 600 Ω = 1,000 Ω，ES = 10 V。100 Ω 电阻上的电压降为：

EX =（100 Ω/1,000 Ω）（100 V），E100Ω = 10 V。300 Ω 电阻上的电压降为：

EX =（300 Ω/1,000 Ω）（100 V），E100Ω = 30 V。600 Ω 电阻上的电压降为：

EX =（600 Ω/1,000 Ω）（100 V），E100Ω = 60 V。（原文此处为图注碎片，为三只电阻串联电路的各电压降标示）验算：ET = 10 V + 30 V + 60 V = 100 V

## 3. 专业词汇

| 英文 | 词性 | 中文 | 本节语境 |
| --- | --- | --- | --- |
| series circuit | n. | 串联电路 | 元件首尾相连、同一电流等量流过每个元件，只有一条电流通路 |
| total resistance | n. | 总电阻 | 串联电路中等于各分电阻之和，记作 RT |
| voltage drop | n. | 电压降 | 迫使电子通过电阻时损失的电压力或电动势 |
| voltage source | n. | 电压源 | 向负载提供恒定电压的能量源，串联时取代数和 |
| algebraic sum | n. | 代数和 | 相加时必须计入正负极性，故称代数 |
| Kirchhoff’s Voltage Law | n. | 基尔霍夫电压定律 | 沿闭合回路所有电压的代数和为零 |
| voltage divider | n. | 分压器 | 从单一电源取得多个电压的电阻网络，带固定或可动触点 |
| voltage divider rule | n. | 分压器法则 | 无需先求电流即可算出串联电阻上的电压，EX =（RX/RT）ES |
| bleeder current | n. | 泄放电流 | 除各负载电流外流过分压器的附加电流，记作 IB |
| tap | n. | 抽头 | 分压器上取出电压的接点，如抽头 A、B、C |
| common point | n. | 公共点 | 测量各点电压所参照的点，总电流在此分为各分电流 |
| end-to-end | adv. | 首尾相连 | 描述串联元件的连接方式 |

## 4. 语法解析

### ① be classified as + because + so that 结果从句
**原句**：This is classified as a series circuit because the components are connected end-to- end, so that the same current flows through each component equally.
**拆解**：主句 This is classified as a series circuit 为被动；because 引导原因状语从句，从句谓语 are connected 亦为被动；so that 引导结果状语从句，主语 the same current，谓语 flows，through each component 为地点状语，equally 为方式状语。
**要点**：be classified as 意为“被归类为”，as 后接名词而非形容词；so that 表结果时从句常含情态动词，此处用陈述语气表示事实结果；end-to-end 是复合副词，作方式状语，不能拆成 in end to end。

### ② 否定 + 比较级短语的谓语
**原句**：In a series circuit, the current cannot be different at different points within the circuit.
**拆解**：In a series circuit 为地点状语；主语 the current，谓语 cannot be，表语 different；at different points within the circuit 为地点状语，within 短语修饰 points。
**要点**：cannot be different 是“不可能不同”的强势否定，比 is the same 语气更绝对；different 后接 at 表示“在……方面不同”；这句话是串联电路的核心结论，后一句 always the same 是其正面表述。

### ③ it 形式主语 + when + 动名词
**原句**：It is important to differentiate between voltage and voltage drop when discussing series circuits.
**拆解**：it 为形式主语，真正主语是 to differentiate between voltage and voltage drop；between…and… 引出区分对象；when discussing 为“连词 + 动名词”，其逻辑主语与主句一致。
**要点**：differentiate between A and B 意为“把 A 与 B 区分开”，A 与 B 须为同类名词；when doing 相当于 when we discuss，比 when we discuss 更简洁；it is important to do 中的 to do 不可换成 that 从句而语义不变。

### ④ 过去分词短语作后置定语 + be proportional to
**原句**：The amount of electrical pressure required to force a given number of electrons through a resistance is proportional to the size of the resistor.
**拆解**：主语中心词 the amount of electrical pressure，后接过去分词短语 required to force… 作后置定语（相当于 that is required）；谓语 is proportional to；宾语 the size of the resistor。
**要点**：required to do 是“被要求/所需的”，过去分词表被动，与 a given number（给定的数量）同理；be proportional to 意为“与……成正比”，反义为 be inversely proportional to；主干很长时要先抓 is proportional to 这个谓语。

### ⑤ that 宾语从句 + around 介词短语作定语
**原句**：This law simply states that the algebraic sum of all voltages around a closed path or loop is zero.
**拆解**：主句 This law simply states；that 引导宾语从句，从句主语 the algebraic sum of all voltages，around a closed path or loop 为介词短语后置修饰 voltages，谓语 is，表语 zero。
**要点**：states that… 是定义定律的固定说法；around 短语紧跟被修饰的 voltages，不能误读为修饰 sum；a closed path or loop 用 or 引出同义解释，译为“闭合路径或回路”。

### ⑥ opposite that of 的替代用法
**原句**：Notice that the sign of the source is opposite that of the individual voltage drops.
**拆解**：祈使句 Notice 后接 that 宾语从句；从句主语 the sign of the source，谓语 is，表语 opposite that of the individual voltage drops，其中 that 替代 the sign，of 短语补出比较对象。
**要点**：opposite 作形容词时直接接名词，不能加 to；that of 用来避免重复前文名词（此处替代 the sign），单数用 that，复数用 those；这句与后文 equals zero 共同说明基尔霍夫电压定律的符号规则。
