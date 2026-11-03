# Amplifier Circuits

> 通用 Ch 12 · Amplifier Circuits · 原文 PDF 第 555 页

## 1. 原文

An amplifier is a device that enables an input signal to control an output signal. The output signal has some or all of the characteristics of the input signal but generally is a greater magnitude than the input signal in terms of voltage, current, or power. Gain is the basic function of all amplifiers. Because of this gain, we can expect the output signal to be greater than the input signal. For example, if we have an input signal of 1 volt and an output signal of 10 volts, then the gain factor can be determined by:

Gain = Signal out /signal in Gain = 10 V/1 V = 10 V oltage gain is usually used to describe the operation of a small gain amplifier. In this type of an amplifier, the output signal voltage is larger than the input signal voltage. Power gain, on the other hand, is usually used to describe the operation of large signal amplifiers. In the case of power gain amplifiers, the gain is not based on voltage but on watts. A power amplifier is an amplifier in which the output signal power is greater than the input signal power. Most power amplifiers are used as the final stage of amplification and drive the output device. The output device could be a flight deck or cabin speaker, an indicator, or antenna. Whatever the device, the power to make it work comes from the final stage of amplification. Drivers for autopilot servos are sometimes contained in line replaceable units (LRUs) called autopilot amplifiers. These units take the low signal commands from the flight guidance system and amplify the signals to a level usable for driving the servo motors.

The classification of a transistor amplifier circuit is determined by the percentage of the time that the current flows through the output circuit in relation to the input signal. There are four classifications of operation: A, AB, B, and C. Each class of operation has a certain use and characteristic. No individual class of amplifiers is considered the best. The best use of an amplifier is a matter of proper selection for the particular operation desired.

150 V 150 V 50 V 50 V 50 V A B C D C1 L-filter Load C1 Inverted L-filter Load T -filter LoadC1 π-filter LoadC1 C2

In the Class A operation, the current in the transistor flows for 100 percent or 360° of the input signal. Class A operation is the least efficient class of operation but provides the best fidelity. Fidelity simply means that the output signal is a good reproduction of the input signal in all respects other than the amplitude, which is amplified. In some cases, there may be some phase shifting between the input signal and the output signal. Typically, the phase difference is 180°. If the output signal is not a good reproduction of the input signal, then the signal is said to be distorted. Distortion is any undesired change to the signal from the input to the output.

The efficiency of an amplifier refers to the amount of power delivered to the output compared to the power supplied to the circuit. Every device in the circuit consumes power in order to operate. If the amplifier operates for 360° of input signal, then it is using more power than if it was using only 180° of input signal. The more power consumed by the amplifier, the less there is available for the output signal. Usually the Class A amplifier is used where efficiency is of little concern and where fidelity in reproduction is desired.

In the Class AB operation, the transistor current flows for more than 50 percent but less than 100 percent of the input signal. Unlike the Class A amplifier, the output signal is distorted. A portion of the output circuit appears to be truncated. This is due to the lack of current through the transistor during this point of operation. When the emitter in this case becomes positive enough, the transistor cannot conduct because the base to emitter junction is no longer forward biased. The input signal going positive beyond this point does not produce any further output and the output remains level.

The Class AB amplifier has a better efficiency and a poorer fidelity than the Class A amplifier. These amplifiers are used when an exact reproduction of the input is not required but both the positive and negative portions of the input signals need to be available on the output.

In Class B operation, the transistor current flows for only 50 percent of the input signal. In this illustration, the base-emitter bias does not allow the transistor to conduct whenever the input signal is greater than zero. In this case, only the negative portion of the input signal is reproduced. Unlike the rectifier, the Class B amplifier does not only reproduce half of the input signal, but it also amplifies it. Class B amplifiers are twice as efficient as the Class A amplifier because the amplifying device only uses power for half of the input signal.

In Class C operations, transistor current flows for less than 50 percent of the input signal. This class of Low-pass filter Load Current Frequency Frequency response High-pass filter Load Current Frequency Frequency response Band-pass filter Load Band-pass filter Load Current Frequency Frequency response operation is the most efficient. Because the transistor does not conduct except during a small portion of the input signal, this is the most efficient class of amplifier. The distortion of the Class C amplifier is greater (poor fidelity) than the Class A, AB, and B amplifiers because a small portion of the input signal is reproduced on the output. Class C amplifiers are used when the output signal is used for only small portions of time.

### Methods of Coupling

Coupling is used to transfer a signal from one stage on an amplifier to another stage. Regardless of whether an amplifier is a single stage or one in a series of stages, there must be a method for the signal to enter and leave the circuit. Coupling is the process of transferring the energy between circuits. There are a number of ways for making this transfer and to discuss these methods in detail goes beyond the scope of this handbook. However, four methods are listed below with a brief description of their operation.

#### Direct Coupling

Direct coupling is the connection of the output of one stage directly to the input of the next stage. Direct coupling provides a good frequency response because no frequency-sensitive components, such as capacitors and inductors, are used. Yet this method is not used very often due to the complex power supply requirements and the impedance matching problems.

RC coupling is the most common method of coupling and Band-pass filter Load Band-pass filter Load Current Frequency Frequency response uses a coupling capacitor and signal developing resistors. In this circuit, R1 acts as a load resistor for Q1 and develops the output signal for that stage. The capacitor C1 blocks the DC bias signal and passes the AC output signal. R2 then becomes the load over which the passes AC signal is developed as an input to the base of Q2. This arrangement allows for the bias voltage of each stage to be blocked, while the AC signal is passed to the next stage.

#### Impedance Coupling

Impedance coupling uses a coil as a load for the first stage but otherwise functions just as an RC coupling. This method is similar to the RC coupling method. The difference is that R1 is replaced with inductor L1 as the output load. The amount of signal developed on the output load depends on the inductive reactance of the coil. In order for the inductive reactance to be high, the inductance must be large; the frequency must be high or both. Therefore, load inductors should have relatively large amounts of inductance and are most effective at high frequencies.

#### Transformer Coupling

Transformer coupling uses a transformer to couple the signal from one stage to the next. The transformer action of T1 couples the signal from the first stage to the second stage. The primary coil of T1 acts as a load for the output of the first stage while the secondary coil acts as the developing impedance for the second stage Q2. Transformer coupling is very efficient and the transformer can aid in impedance matching.

Feedback occurs when a small portion of the output signal is sent back to the input signal to the amplifier. There are two types of feedback in amplifiers:

1. Positive (regenerative)

2. Negative (degenerative)

The main difference between these two signals is whether the feedback signal adds to the input signal or if the feedback signal diminishes the input signal. When the feedback is positive, the signal being returned to the input is in phase with the input signal and thus interferes constructively. The figure illustrates this concept applied in the amplified circuit through a block diagram. Notice that the feedback signal is in phase with the input signal, which regenerates the input signal. This results in an output signal with amplitude greater than would have been without the constructive, positive feedback. This type of positive feedback is what causes an audio system to squeal.

The figure also illustrates with a block diagram how negative or degenerative feedback occurs. In this case, the feedback signal is out of phase with the input signal. This causes destructive interference and degenerates the input signal. The result is a lower amplitude output signal than would have occurred without the feedback.

### Operational Amplifiers (OP AMP)

An operational amplifier (OP AMP) is designed to be used with other circuit components and performs either computing functions or filtering. Operational amplifiers are usually high-gain amplifiers with the amount of gain governed by the amount of feedback.

Operational amplifiers were originally developed for analog computers and used to perform mathematical functions. Today many devices use the operational amplifier for DC amplifiers, AC amplifiers, comparators, oscillators, and filter circuits. The widespread use is due to the fact that the OP AMP is a versatile device, small, and inexpensive. Built into the integrated chip, the operational amp is used as a basic building block of larger circuits.

There are two inputs to the operational amplifier, inverting (−) and non-inverting (+), and there is one output. The polarity NPN Input Class A amplifier Output VCC VEE + − − NPN Input Class AB amplifier Output VCC VEE + − − NPN Input Class B amplifier Output VCC VEE + − − of a signal applied to the inverting input (−) is reversed at the output. A signal applied to the non-inverting (+) input retains its polarity on the output. To be classified as an operational amplifier, the circuit must have certain characteristics:

1. Very high gain

2. Very high input impedance

3. Very high output impedance This type of a circuit can be made up of discrete components, such as resistors and transistors. However, the most common form of an operational amplifier is found in the integrated circuit. This integrated circuit or chip contains the various stages of the operational amplifier and can be treated as if it were a single stage.

The number of applications for OP AMPs is too numerous to detail in this handbook. However, the technician occasionally comes across these devices in modern aircraft and should be able to recognize their general purpose in a circuit. Some of the basic applications are:

1. Go/no-go detectors

2. Square wave circuits

3. Non-inverting amplifier

4. Inverting amplifier

5. Half-wave rectifier Input Impedance coupled amplifier Output Q1 Q2C1 VCC L1 NPN Input Class C amplifier Output VCC VEE + − − Input RC coupled amplifier Output Q1 Q2C1 VCC R1 R2

## 2. 中文翻译

放大器是一种让输入信号得以控制输出信号的装置。输出信号具有输入信号的部分或全部特征，但在电压、电流或功率方面通常比输入信号大。增益是所有放大器的基本功能。正因为有增益，我们才能指望输出信号大于输入信号。例如，若输入信号为 1 伏、输出信号为 10 伏，则增益系数可由下式确定：

增益 = 输出信号/输入信号　　增益 = 10 V/1 V = 10　　电压增益通常用来描述小信号放大器的工作。在这类放大器中，输出信号电压大于输入信号电压。另一方面，功率增益通常用来描述大信号放大器的工作。对功率增益放大器而言，增益不是按电压计算，而是按瓦特计算。功率放大器是输出信号功率大于输入信号功率的放大器。大多数功率放大器用作放大的末级，并驱动输出装置。输出装置可以是驾驶舱或客舱扬声器、指示器或天线。无论是什么装置，使其工作的功率都来自放大的末级。自动驾驶仪舵机的驱动器有时装在一个称为自动驾驶仪放大器的航线可更换单元（LRU）里。这些单元接收来自飞行引导系统的低电平信号指令，并把信号放大到足以驱动伺服电动机的电平。

晶体管放大器电路的分类，取决于输出电路中电流流通的时间相对于输入信号所占的百分比。工作状态分为四类：A、AB、B 和 C。每一类工作都有其特定的用途和特性。没有哪一类放大器可以说是最好的；放大器的最佳用法，取决于针对特定用途作出恰当的选择。

（原文此处为图注碎片，150 V 150 V 50 V 50 V 50 V A B C D C1 L-filter LoadC1 Inverted L-filter Load T-filter LoadC1 π-filter LoadC1 C2，无对应正文）

在 A 类工作中，晶体管中的电流在整个输入信号的 100%（即 360°）内流动。A 类工作是效率最低的一类工作，但保真度最好。保真度简单地说，就是输出信号在除被放大的幅值以外的各个方面都是输入信号的很好复现。某些情况下，输入信号与输出信号之间可能存在一定的相移。通常相位差为 180°。如果输出信号不是输入信号的很好复现，就说该信号失真了。失真是信号从输入到输出过程中发生的任何非预期的变化。

放大器的效率，是指输送到输出的功率与供给电路的功率之比。电路中的每个器件都要消耗功率才能工作。如果放大器在整个 360° 输入信号期间都工作，那么它消耗的功率就比只在 180° 输入信号期间工作时要多。放大器消耗的功率越多，能用于输出信号的功率就越少。A 类放大器通常用于效率无关紧要而要求复现保真的场合。

在 AB 类工作中，晶体管电流的流通时间超过输入信号的 50%，但不到 100%。与 A 类放大器不同，其输出信号是失真的，输出波形的一部分看起来像是被截掉了。这是由于在这一工作点上晶体管中没有电流。在此情形下，当发射极变得足够正时，晶体管便不能导通，因为基极—发射极结不再是正向偏置。输入信号越过这一点继续变正，也不会产生任何进一步的输出，输出保持不变。

AB 类放大器的效率比 A 类高，保真度则比 A 类差。这类放大器用于不要求精确复现输入、但输出上需要同时具备输入信号正、负两部分的场合。

在 B 类工作中，晶体管电流只在输入信号的 50% 时间内流动。在此图示中，只要输入信号大于零，基极—发射极偏置就不允许晶体管导通。这样，只有输入信号的负半部分被复现。与整流器不同，B 类放大器不只是复现输入信号的一半，它还对这一半进行放大。B 类放大器的效率是 A 类的两倍，因为放大器件只在输入信号的一半时间内消耗功率。

在 C 类工作中，晶体管电流的流通时间不到输入信号的 50%。这一工作类别是效率最高的一类（原文此处为图注碎片：Low-pass filter Load Current Frequency Frequency response High-pass filter Load Current Frequency Frequency response Band-pass filter Load Band-pass filter Load Current Frequency Frequency response，混入正文，无对应正文）。由于晶体管只在输入信号的一小部分时间内导通，这是效率最高的一类放大器。C 类放大器的失真比 A、AB 和 B 类都大（保真度差），因为输出上只复现了输入信号的一小部分。C 类放大器用于输出信号只在很短时间使用的场合。

### 耦合方式

耦合用来把信号从放大器的一级传递到另一级。无论放大器是单级还是多级串联中的一级，都必须有让信号进出电路的方式。耦合就是在电路之间传递能量的过程。实现这种传递的方法有很多，详细讨论这些方法超出了本手册的范围。不过，下面列出四种方法，并简要说明其工作原理。

#### 直接耦合

直接耦合是把一级的输出直接接到下一级的输入。直接耦合能提供良好的频率响应，因为不使用电容器和电感器这类对频率敏感的元件。然而，由于电源要求复杂以及阻抗匹配困难，这种方法并不常用。

RC 耦合是最常用的耦合方式，它使用一只耦合电容和一些信号形成电阻（原文此处为图注碎片：Band-pass filter Load Band-pass filter Load Current Frequency Frequency response，混入正文，无对应正文）。在此电路中，R1 充当 Q1 的负载电阻，并形成该级的输出信号。电容 C1 隔断直流偏置信号，让交流输出信号通过。R2 则成为负载，通过它的交流信号在其上形成，作为输入加到 Q2 的基极。这种安排使各级的偏置电压得以隔断，同时交流信号被送到下一级。

#### 阻抗耦合

阻抗耦合用一只线圈作为第一级的负载，除此之外的功能与 RC 耦合完全相同。这种方法与 RC 耦合法相似，区别在于用电感 L1 替换 R1 作为输出负载。输出负载上形成的信号大小，取决于线圈的感抗。要使感抗高，电感必须大、频率必须高，或者两者兼有。因此，负载电感应有较大的电感量，并且在高频时最为有效。

#### 变压器耦合

变压器耦合用一只变压器把信号从一级耦合到下一级。T1 的变压作用把第一级的信号耦合到第二级。T1 的初级线圈充当第一级输出的负载，而次级线圈则充当第二级 Q2 形成信号所需的阻抗。变压器耦合效率很高，而且变压器有助于阻抗匹配。

当输出信号的一小部分被送回放大器的输入端时，就产生了反馈。放大器中的反馈有两种类型：

1. 正反馈（再生）

2. 负反馈（衰减）

这两种信号的主要区别在于：反馈信号是加到输入信号上，还是削弱输入信号。当反馈为正时，送回输入端的信号与输入信号同相，因而发生相长干涉。图以框图形式展示了这一概念在放大电路中的应用。注意反馈信号与输入信号同相，对输入信号起再生作用。其结果是输出信号的幅值比没有这种相长的正反馈时更大。这种正反馈正是音响系统产生啸叫的原因。

图同样以框图形式展示了负反馈（衰减反馈）是如何产生的。在这种情况下，反馈信号与输入信号反相，因而发生相消干涉并削弱输入信号。结果得到比没有反馈时幅值更低的输出信号。

### 运算放大器（OP AMP）

运算放大器（OP AMP）被设计成与其他电路元件配合使用，执行运算功能或滤波功能。运算放大器通常是高增益放大器，其增益量由反馈量决定。

运算放大器最初是为模拟计算机研制的，用来执行数学运算。如今许多装置把运算放大器用于直流放大器、交流放大器、比较器、振荡器和滤波电路。它之所以被广泛使用，是因为运算放大器这种器件通用性强、体积小、价格低。运算放大器被集成在集成电路芯片中，用作构成更大电路的基本积木单元。

运算放大器有两个输入端——反相输入端（−）和同相输入端（+），还有一个输出端。（原文此处为图注碎片：The polarity NPN Input Class A amplifier Output VCC VEE NPN Input Class AB amplifier Output VCC VEE NPN Input Class B amplifier Output VCC VEE，混入正文，无对应正文）加在反相输入端（−）上的信号，其极性在输出端被倒转。加在同相输入端（+）上的信号，在输出端保持其极性。要归类为运算放大器，该电路必须具备某些特性：

1. 极高的增益

2. 极高的输入阻抗

3. 极高的输出阻抗 这类电路可以由分立元件（如电阻和晶体管）构成。然而，运算放大器最常见的形式是做在集成电路里。这种集成电路（芯片）包含运算放大器的各个级，可以当作单个级来处理。

运算放大器的应用多得不胜枚举，本手册无法一一详述。不过，技术人员在现代飞机上偶尔会遇到这类器件，应当能在电路里认出它们的大致用途。一些基本应用是：

1. 通/不通检测器

2. 方波电路

3. 同相放大器

4. 反相放大器

5. 半波整流器（原文此处为图注碎片：Input Impedance coupled amplifier Output Q1 Q2C1 VCC L1 NPN Input Class C amplifier Output VCC VEE Input RC coupled amplifier Output Q1 Q2C1 VCC R1 R2，混入正文，无对应正文）

## 3. 专业词汇

| 英文 | 词性 | 中文 | 本节语境 |
| --- | --- | --- | --- |
| amplifier | n. | 放大器 | 本节主题：用输入信号控制输出信号、并把信号幅度放大的装置 |
| gain | n. | 增益 | 输出与输入之比（如 10 V/1 V = 10），是放大器的基本功能 |
| voltage gain | n.phr. | 电压增益 | 小信号放大器的描述方式，输出信号电压高于输入信号电压 |
| power gain | n.phr. | 功率增益 | 大信号放大器的描述方式，按瓦特而非电压计算 |
| fidelity | n. | 保真度 | 输出对输入复现的忠实程度，A 类最好、C 类最差 |
| distortion | n. | 失真 | 信号从输入到输出发生的任何非预期变化 |
| coupling | n. | 耦合 | 在级与级之间传递能量的过程，本节介绍直接、RC、阻抗、变压器四种方式 |
| coupling capacitor | n.phr. | 耦合电容 | RC 耦合中隔断直流偏置、让交流信号通过的电容器 |
| impedance matching | n.phr. | 阻抗匹配 | 直接耦合不常用的原因之一，变压器耦合可协助实现 |
| operational amplifier (OP AMP) | n.phr. | 运算放大器 | 可执行运算或滤波功能的高增益集成电路，有反相与同相两个输入端 |
| feedback | n. | 反馈 | 把输出信号的一部分送回输入端，分正反馈与负反馈两种 |
| line replaceable unit (LRU) | n.phr. | 航线可更换单元 | 自动驾驶仪放大器等可在外场整件更换的机载单元 |

## 4. 语法解析

### ① 定语从句 + enable sb/sth to do
**原句**：An amplifier is a device that enables an input signal to control an output signal.
**拆解**：主句：主语 An amplifier + 系动词 is + 表语 a device；that 引导定语从句修饰 a device，从句中 enables 的宾语是 an input signal，不定式 to control an output signal 作宾语补足语。
**要点**：enable 的句型是 enable sb/sth to do sth，不能写成 enable sb doing 或 enable that…；这里的宾语是“输入信号”而不是人，属于拟物化表达，译成“让输入信号得以控制输出信号”。that 从句把定义与功能压在一句里，是手册下定义的标准写法。
### ② be determined by + 名词 + that 定语从句
**原句**：The classification of a transistor amplifier circuit is determined by the percentage of the time that the current flows through the output circuit in relation to the input signal.
**拆解**：主语 The classification（of a transistor amplifier circuit 为后置定语）+ 谓语 is determined by（被动）+ 宾语 the percentage of the time；that the current flows… 为定语从句修饰 the time；in relation to the input signal 为介词短语，说明“相对于输入信号”这一比较基准。
**要点**：be determined by 意为“由……决定”，其后的长名词短语中心词是 percentage，后面的 of the time that… 层层修饰，翻译时要先抓中心词再顺次展开。in relation to 是“相对于、与……相比”，不能译成“与……有关”。被动语态在此避免了指明“谁来决定”。
### ③ the + 比较级 …, the + 比较级 …
**原句**：The more power consumed by the amplifier, the less there is available for the output signal.
**拆解**：前一分句 The more power consumed by the amplifier 中，consumed by the amplifier 为过去分词短语作后置定语，修饰 power，谓语 is 省略；后一分句 the less there is available for the output signal 为 there be 句型的比较级形式，available 作后置定语。
**要点**：“the + 比较级”连用表示“越……越……”，两个 the 缺一不可；后半句常省略谓语，只保留比较级与核心成分。power consumed 是“被消耗的功率”，不是“消耗功率”；available for 意为“可用于……的”，作后置定语时不能前置成 available power 而改变含义。
### ④ when 从句 + enough + because 从句
**原句**：When the emitter in this case becomes positive enough, the transistor cannot conduct because the base to emitter junction is no longer forward biased.
**拆解**：When 引导时间状语从句（主语 the emitter，系动词 becomes，表语 positive，enough 修饰 positive 后置）；主句主语 the transistor + 谓语 cannot conduct；because 引导原因状语从句，其中 no longer 否定 forward biased（过去分词作表语）。
**要点**：enough 修饰形容词时必须后置（positive enough），不能写成 enough positive。no longer 表示状态的中断（“不再是”），与 not any longer 同义；forward biased 是电子学固定搭配“正向偏置”，作表语时省略了 is being。翻译时原因从句宜前置或加“因为”，使中文因果更清楚。
### ⑤ that 宾语从句 + 非限定性 which 从句
**原句**：Notice that the feedback signal is in phase with the input signal, which regenerates the input signal.
**拆解**：祈使句 Notice + that 引导的宾语从句（主语 the feedback signal，系动词 is，表语 in phase with the input signal）；逗号后 which 引导非限定性定语从句，指代整个宾语从句所述的事实。
**要点**：which 前有逗号时为非限定性定语从句，先行词不是紧邻的 the input signal，而是前面整件事（反馈信号与输入同相），译成“这就对输入信号起再生作用”。in phase with 是“与……同相”，反义为 out of phase with，本节后文即用后者描述负反馈。
### ⑥ in order for sb/sth to be + 分号连接的并列句
**原句**：In order for the inductive reactance to be high, the inductance must be large; the frequency must be high or both.
**拆解**：In order for the inductive reactance to be high 为不定式复合结构（for + 名词 + to be）作目的状语；主句由分号连接的两个并列分句构成：the inductance must be large 与 the frequency must be high or both。
**要点**：in order for sth to be 中的 for 引出不定式的逻辑主语，不能省略；or both 表示“或者两者兼有”，是对前面两条途径的补充，翻译时不能漏。分号在此表示并列关系，比 and 更能体现“两个条件各自独立成立”。
