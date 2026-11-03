# Voltage Regulation of Alternators

> 通用 Ch 12 · Voltage Regulation of Alternators · 原文 PDF 第 613 页

## 1. 原文

The problem of voltage regulation in an AC system does not differ basically from that in a DC system. In each case, the function of the regulator system is to control voltage, maintain a balance of circulating current throughout the system, and eliminate sudden changes in voltage (anti-hunting) when a load is applied to the system. However, there is one important difference between the regulator system of DC generators and alternators operated in a parallel configuration. The load carried by any particular DC generator in either a two or four generator system depends on its voltage as compared with the bus voltage, while the division of load between alternators depends upon the adjustments of their speed governors, which are controlled by the frequency and droop circuits discussed in the previous section on alternator constant-speed drive systems.

When AC generators are operated in parallel, frequency and voltage must both be equal. Where a synchronizing force is required to equalize only the voltage between DC generators, synchronizing forces are required to equalize both voltage and speed (frequency) between AC generators. On a comparative basis, the synchronizing forces for AC generators are much greater than for DC generators. When AC generators are of sufficient size and are operating at unequal frequencies and terminal voltages, serious damage may result if they are suddenly connected to each other through a common bus. To avoid this, the generators must be synchronized as closely as possible before connecting them together.

Regulating the voltage output of a DC exciter, which supplies current to the alternator rotor field, best controls the output voltage of an alternator. This is accomplished by the regulation of a 28-volt system connected in the field circuit of the exciter. A regulator controls the exciter field current and thus regulates the exciter output voltage applied O P Q R S Latch Oil out Oil in to the alternator field.

### Alternator Transistorized Regulators

Many aircraft alternator systems use a transistorized voltage regulator to control the alternator output. Before studying this section, a review of transistor principles may be helpful.

A transistorized voltage regulator consists mainly of transistors, diodes, resistors, capacitors, and, usually, a thermistor. In operation, current flows through a diode and transistor path to the generator field. When the proper voltage level is reached, the regulating components cause the transistor to cut off conduction to control the alternator field strength. The regulator operating range is usually adjustable through a narrow range. The thermistor provides temperature compensation for the circuitry. The transistorized voltage regulator will be referred to in explaining the operation of this type of regulator.

The AC output of the generator is fed to the voltage regulator, where it is compared to a reference voltage, and the difference is applied to the control amplifier section of the regulator. If the output is too low, field strength of the AC exciter generator is increased by the circuitry in the regulator. If the output is too high, the field strength is reduced.

The power supply for the bridge circuit is CR1, which provides full-wave rectification of the three phase output from transformer T1. The DC output voltages of CR1 are proportional to the average phase voltages. Power is supplied from the negative end of the power supply through point B, R2, point C, zener diode (CR5), point D, and to the parallel hookup of V1 and R1. Takeoff point C of the bridge is located between resistor R2 and the zener diode. In the other leg of the reference bridge, resistors R9, R7, and the temperature compensating resistor RT1 are connected in series with V1 and R1 through points B, A, and D. The output of this leg of the bridge is at the wiper arm of R7.

As generator voltage changes occur, for example, if the voltage lowers, the voltage across R1 and V1 (once V2 starts conducting) remains constant. The total voltage change occurs across the bridge circuit. Since the voltage across the zener diode remains constant (once it starts conducting), the total voltage change occurring in that leg of the bridge is across resistor R2. In the other leg of the bridge, the voltage change across the resistors is proportional to their resistance values. Therefore, the voltage change across R2 is greater than the voltage change across R9 to wiper arm of R7. If the generator output voltage drops, point C is negative with respect to the wiper arm of R7. Conversely, if the generator voltage output increases, the polarity of the voltage between the two points is reversed.

The bridge output, taken between points C and A, is connected between the emitter and the base of transistor Q1. With the generator output voltage low, the voltage from the bridge is negative to the emitter and positive to the base. This is a forward bias signal to the transistor, and the emitter to collector current therefore increases. With the increase of current, the voltage across emitter resistor R11 increases.

This, in turn, applies a positive signal to the base of transistor

Q4, increasing its emitter to collector current and increasing the voltage drop across the emitter resistor R10.

This gives a positive bias to the base of Q2, which increases its emitter to collector current and increase the voltage drop across its emitter resistor R4. This positive signal controls output transistor Q3. The positive signal on the base of Q3 increases the emitter to collector current.

The control field of the exciter generator is in the collector circuit. Increasing the output of the exciter generator increases the field strength of the AC generator, which increases the generator output.

To prevent exciting the generator when the frequency is at a low value, there is an underspeed switch located near the F+ terminal. When the generator reaches a suitable operating frequency, the switch closes and allows the generator to be excited.

Another item of interest is the line containing resistors R27, R28, and R29 in series with the normally closed contacts of the K1 relay. The operating coil of this relay is found in the lower left part of the schematic. Relay K1 is connected across the power supply (CR4) for the transistor amplifier. When the generator is started, electrical energy is supplied from the 28-volt DC bus to the exciter generator field to “flash the field” for initial excitation. When the field of the exciter generator has been energized, the AC generator starts to produce, and as it builds up, relay K1 is energized, opening the “field flash” circuit.

R11 K1 T1 T2T3 T1 Y- R10 R4 R6 R29 R28 R27 K1 R9 R7 R1 RT1 A A F F+ A– A+ N Switch underspeed +28V Special bus AC gen.

exciter Gen. neg. bus R G C B D V1 CR5 R2 R3 R8 Q1 Q4 Q2 Q3 CR3 CR2 CR4 CR1 CR4

## 2. 中文翻译

交流系统中的电压调节问题与直流系统并无本质区别。在两种情况下，调节器系统的功能都是控制电压、保持整个系统中环流平衡，并在系统加上负载时消除电压的突然变化（防振荡）。然而，直流发电机的调节器系统与并联运行的交流发电机的调节器系统之间存在一个重要差别。在两台或四台发电机系统中，任一台直流发电机所承担的负载取决于其电压与汇流条电压的比较，而交流发电机之间的负载分配取决于其调速器的调整，调速器由上一节交流发电机恒速传动系统中讨论的频率和下垂电路控制。

当交流发电机并联运行时，频率和电压都必须相等。对于直流发电机，只需同步力来平衡电压；而对于交流发电机，则需要同步力同时平衡电压和转速（频率）。相比之下，交流发电机的同步力比直流发电机大得多。当交流发电机容量足够大且以不相等的频率和端电压运行时，如果突然通过公共汇流条把它们连接起来，可能造成严重损坏。为避免这种情况，必须在把发电机连接在一起之前尽可能精确地同步。

调节向交流发电机转子磁场供电的直流励磁机的输出电压，是对交流发电机输出电压最有效的控制。这通过调节接在励磁机励磁回路中的 28 伏系统来实现。调节器控制励磁机励磁电流，从而调节加到交流发电机磁场上的励磁机输出电压。

### 交流发电机晶体管调节器

许多飞机交流发电机系统使用晶体管电压调节器来控制交流发电机输出。在学习本节之前，复习一下晶体管原理可能会有帮助。

晶体管电压调节器主要由晶体管、二极管、电阻器、电容器组成，通常还有热敏电阻。工作时，电流经二极管和晶体管通路流向发电机磁场。当达到规定的电压水平时，调节元件使晶体管截止导通，以控制交流发电机磁场强度。调节器的工作范围通常可在较窄范围内调整。热敏电阻为电路提供温度补偿。在解释这类调节器的工作时，将提到该晶体管电压调节器。

发电机的交流输出送往电压调节器，在那里与基准电压比较，差值加到调节器的控制放大部分。如果输出过低，调节器中的电路使交流励磁机发电机的磁场强度增大。如果输出过高，磁场强度则减小。

桥式电路的电源是 CR1，它把变压器 T1 的三相输出进行全波整流。CR1 的直流输出电压与各相平均电压成正比。电源从负端经 B 点、R2、C 点、稳压二极管（CR5）、D 点，供到 V1 与 R1 的并联连接处。桥路的取出点 C 位于电阻器 R2 与稳压二极管之间。在基准桥路的另一臂上，电阻器 R9、R7 和温度补偿电阻器 RT1 经 B、A、D 点与 V1 和 R1 串联。该桥臂的输出取自 R7 的滑臂。

随着发电机电压发生变化，例如电压降低时，R1 和 V1 两端的电压（一旦 V2 开始导通）保持恒定。总的电压变化发生在桥式电路两端。由于稳压二极管两端的电压（一旦其开始导通）保持恒定，该桥臂中发生的总电压变化落在电阻器 R2 上。在桥路的另一臂上，各电阻器上的电压变化与其阻值成正比。因此，R2 上的电压变化大于 R9 到 R7 滑臂上的电压变化。如果发电机输出电压下降，C 点相对于 R7 滑臂为负。反之，如果发电机输出电压升高，两点之间电压的极性反转。

取自 C 点和 A 点之间的桥路输出，接在晶体管 Q1 的发射极与基极之间。当发电机输出电压低时，来自桥路的电压对发射极为负、对基极为正。这是给晶体管的正确偏置信号，因此发射极到集电极的电流增大。随着电流增大，发射极电阻器 R11 两端的电压升高。

这一电压反过来又把正信号加到晶体管

Q4 的基极，使其发射极到集电极电流增大，并增大其发射极电阻器 R10 上的电压降。

这给 Q2 的基极加上正偏置，增大其发射极到集电极电流，并增大其发射极电阻器 R4 上的电压降。该正信号控制输出晶体管 Q3。Q3 基极上的正信号增大发射极到集电极电流。

励磁机发电机的控制磁场接在集电极电路中。增大励磁机发电机的输出，会增大交流发电机的磁场强度，从而提高发电机输出。

为防止频率低时激励发电机，在 F+ 端子附近装有一个欠速开关。当发电机达到合适的工作频率时，开关闭合，允许发电机励磁。

另一个值得注意的部分是包含串联电阻器 R27、R28、R29 与 K1 继电器常闭触点的线路。该继电器的动作线圈位于原理图的左下部分。继电器 K1 跨接在晶体管放大器的电源（CR4）两端。发电机起动时，电能从 28 伏直流汇流条送往励磁机发电机磁场，以“闪磁”进行初始励磁。当励磁机发电机的磁场通电后，交流发电机开始发电，随着电压建立，继电器 K1 通电，断开“磁场闪磁”电路。

（原文此处为图注碎片，原文无正文）

（原文此处为图注碎片，原文无正文）

## 3. 专业词汇

| 英文 | 词性 | 中文 | 本节语境 |
| --- | --- | --- | --- |
| voltage regulation | n. | 电压调节 | 控制交流发电机输出电压、消除负载突变引起的电压波动 |
| transistorized voltage regulator | n. | 晶体管电压调节器 | 用晶体管、二极管等控制交流发电机磁场强度的调节器 |
| reference voltage | n. | 基准电压 | 与发电机交流输出比较的受控基准 |
| bridge circuit | n. | 桥式电路 | 比较端电压与基准、输出误差信号的桥路 |
| zener diode | n. | 稳压二极管 | 导通后两端电压保持恒定的基准元件（CR5） |
| thermistor | n. | 热敏电阻 | 为调节器电路提供温度补偿的元件（RT1） |
| synchronize | v. | 同步 | 并联前使频率、电压和相位尽可能一致 |
| excitation | n. | 励磁 | 向交流发电机转子磁场供电的励磁机输出 |
| conduction | n. | 导通 | 晶体管或二极管允许电流通过的状态 |
| frequency | n. | 频率 | 交流发电机输出频率，与转速成正比，须与汇流条一致 |
| droop circuit | n. | 下垂电路 | 与频率电路一起控制调速器、决定负载分配的电路 |
| bus | n. | 汇流条 | 并联发电机共同连接的公共供电母线和比较基准 |

## 4. 语法解析

### ① that 替代前文名词 + differ from
**原句**：The problem of voltage regulation in an AC system does not differ basically from that in a DC system.
**拆解**：主语 The problem of voltage regulation；谓语 does not differ… from；that 替代前文的 the problem，in a DC system 为后置修饰。
**要点**：differ from 表示“与……不同”；that 替代可数名词单数以避免重复，复数用 those。

### ② be of + 抽象名词 与条件从句
**原句**：When AC generators are of sufficient size and are operating at unequal frequencies and terminal voltages, serious damage may result if they are suddenly connected to each other through a common bus.
**拆解**：When 引导时间状语从句，从句由 are of sufficient size 与 are operating… 并列；主句 serious damage may result；if 引导条件从句，其中 are connected 为被动。
**要点**：be of + 名词（size、importance、value）表示性质；result 在此为不及物动词，意为“产生、导致”。

### ③ 动名词短语作主语 + 非限制性定语从句
**原句**：Regulating the voltage output of a DC exciter, which supplies current to the alternator rotor field, best controls the output voltage of an alternator.
**拆解**：动名词短语 Regulating the voltage output 作主语；which 引导非限制性定语从句，修饰 a DC exciter；谓语 best controls；宾语 the output voltage。
**要点**：动名词短语作主语时谓语用单数；插入的定语从句不影响动名词与谓语的搭配关系。

### ④ Where 引导对比性地点/抽象状语从句
**原句**：Where a synchronizing force is required to equalize only the voltage between DC generators, synchronizing forces are required to equalize both voltage and speed (frequency) between AC generators.
**拆解**：Where 引导抽象地点状语从句，相当于“在……的场合”；主句为被动结构 synchronizing forces are required to equalize…。
**要点**：equalize 为及物动词，意为“使相等”；where 从句在此表对比，不是真实地点。

### ⑤ with 复合结构
**原句**：With the generator output voltage low, the voltage from the bridge is negative to the emitter and positive to the base.
**拆解**：With + 宾语 the generator output voltage + 形容词补语 low 构成 with 复合结构，作条件状语；主句 the voltage is negative… and positive…。
**要点**：with 复合结构中补语可由形容词、分词、介词短语充当；negative to / positive to 表示相对于某电极的极性。

### ⑥ since 原因从句 + 现在分词后置定语
**原句**：Since the voltage across the zener diode remains constant (once it starts conducting), the total voltage change occurring in that leg of the bridge is across resistor R2.
**拆解**：Since 引导原因状语从句；括号内 once 引导时间状语从句；主句主语 the total voltage change 由现在分词短语 occurring… 后置修饰，is 后 across resistor R2 作表语。
**要点**：once 引导的从句用一般现在时表将来；分词短语 occurring in that leg 修饰 change，而非 voltage。
