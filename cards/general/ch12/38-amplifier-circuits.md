# Amplifier Circuits

> 通用 Ch 12 · Amplifier Circuits · 原文 PDF 第 555 页

## 1. 原文

An amplifier is a device that enables an input signal to control an output signal. The output signal has some or all of the characteristics of the input signal but generally is a greater magnitude than the input signal in terms of voltage, current, or power. Gain is the basic function of all amplifiers. Because of this gain, we can expect the output signal to be greater than the input signal. For example, if we have an input signal of 1 volt and an output signal of 10 volts, then the gain factor can be determined by:

Gain = Signal out /signal in Gain = 10 V/1 V = 10 V oltage gain is usually used to describe the operation of a small gain amplifier. In this type of an amplifier, the output signal voltage is larger than the input signal voltage. Power gain, on the other hand, is usually used to describe the operation of large signal amplifiers. In the case of power gain amplifiers, the gain is not based on voltage but on watts. A power amplifier is an amplifier in which the output signal power is greater than the input signal power. Most power amplifiers are used as the final stage of amplification and drive the output device. The output device could be a flight deck or cabin speaker, an indicator, or antenna. Whatever the device, the power to make it work comes from the final stage of amplification. Drivers for autopilot servos are sometimes contained in line replaceable units (LRUs) called autopilot amplifiers. These units take the low signal commands from the flight guidance system and amplify the signals to a level usable for driving the servo motors.

The classification of a transistor amplifier circuit is determined by the percentage of the time that the current flows through the output circuit in relation to the input signal. There are four classifications of operation: A, AB, B, and C. Each class of operation has a certain use and characteristic. No individual class of amplifiers is considered the best. The best use of an amplifier is a matter of proper selection for the particular operation desired.

150 V 150 V 50 V 50 V 50 V A B C D C1 L-filter Load C1 Inverted L-filter Load T -filter LoadC1 π-filter LoadC1 C2

In the Class A operation, the current in the transistor flows for 100 percent or 360° of the input signal. [Figure 12-238] Class A operation is the least efficient class of operation but provides the best fidelity. Fidelity simply means that the output signal is a good reproduction of the input signal in all respects other than the amplitude, which is amplified. In some cases, there may be some phase shifting between the input signal and the output signal. Typically, the phase difference is 180°. If the output signal is not a good reproduction of the input signal, then the signal is said to be distorted. Distortion is any undesired change to the signal from the input to the output.

The efficiency of an amplifier refers to the amount of power delivered to the output compared to the power supplied to the circuit. Every device in the circuit consumes power in order to operate. If the amplifier operates for 360° of input signal, then it is using more power than if it was using only 180° of input signal. The more power consumed by the amplifier, the less there is available for the output signal. Usually the Class A amplifier is used where efficiency is of little concern and where fidelity in reproduction is desired.

In the Class AB operation, the transistor current flows for more than 50 percent but less than 100 percent of the input signal. [Figure 12-239] Unlike the Class A amplifier, the output signal is distorted. A portion of the output circuit appears to be truncated. This is due to the lack of current through the transistor during this point of operation. When the emitter in this case becomes positive enough, the transistor cannot conduct because the base to emitter junction is no longer forward biased. The input signal going positive beyond this point does not produce any further output and the output remains level.

The Class AB amplifier has a better efficiency and a poorer fidelity than the Class A amplifier. These amplifiers are used when an exact reproduction of the input is not required but both the positive and negative portions of the input signals need to be available on the output.

In Class B operation, the transistor current flows for only 50 percent of the input signal. [Figure 12-240] In this illustration, the base-emitter bias does not allow the transistor to conduct whenever the input signal is greater than zero. In this case, only the negative portion of the input signal is reproduced. Unlike the rectifier, the Class B amplifier does not only reproduce half of the input signal, but it also amplifies it. Class B amplifiers are twice as efficient as the Class A amplifier because the amplifying device only uses power for half of the input signal.

In Class C operations, transistor current flows for less than 50 percent of the input signal. [Figure 12-241] This class of Low-pass filter Load Current Frequency Frequency response High-pass filter Load Current Frequency Frequency response Band-pass filter Load Band-pass filter Load Current Frequency Frequency response operation is the most efficient. Because the transistor does not conduct except during a small portion of the input signal, this is the most efficient class of amplifier. The distortion of the Class C amplifier is greater (poor fidelity) than the Class A, AB, and B amplifiers because a small portion of the input signal is reproduced on the output. Class C amplifiers are used when the output signal is used for only small portions of time.

### Methods of Coupling

Coupling is used to transfer a signal from one stage on an amplifier to another stage. Regardless of whether an amplifier is a single stage or one in a series of stages, there must be a method for the signal to enter and leave the circuit. Coupling is the process of transferring the energy between circuits. There are a number of ways for making this transfer and to discuss these methods in detail goes beyond the scope of this handbook. However, four methods are listed below with a brief description of their operation.

#### Direct Coupling

Direct coupling is the connection of the output of one stage directly to the input of the next stage. Direct coupling provides a good frequency response because no frequency-sensitive components, such as capacitors and inductors, are used. Yet this method is not used very often due to the complex power supply requirements and the impedance matching problems.

RC coupling is the most common method of coupling and Band-pass filter Load Band-pass filter Load Current Frequency Frequency response uses a coupling capacitor and signal developing resistors. [Figure 12-242] In this circuit, R1 acts as a load resistor for Q1 and develops the output signal for that stage. The capacitor C1 blocks the DC bias signal and passes the AC output signal. R2 then becomes the load over which the passes AC signal is developed as an input to the base of Q2. This arrangement allows for the bias voltage of each stage to be blocked, while the AC signal is passed to the next stage.

#### Impedance Coupling

Impedance coupling uses a coil as a load for the first stage but otherwise functions just as an RC coupling. [Figure 12-243] This method is similar to the RC coupling method. The difference is that R1 is replaced with inductor L1 as the output load. The amount of signal developed on the output load depends on the inductive reactance of the coil. In order for the inductive reactance to be high, the inductance must be large; the frequency must be high or both. Therefore, load inductors should have relatively large amounts of inductance and are most effective at high frequencies.

#### Transformer Coupling

Transformer coupling uses a transformer to couple the signal from one stage to the next. [Figure 12-244] The transformer action of T1 couples the signal from the first stage to the second stage. The primary coil of T1 acts as a load for the output of the first stage while the secondary coil acts as the developing impedance for the second stage Q2. Transformer coupling is very efficient and the transformer can aid in impedance matching.

Feedback occurs when a small portion of the output signal is sent back to the input signal to the amplifier. There are two types of feedback in amplifiers:

1. Positive (regenerative)

2. Negative (degenerative)

The main difference between these two signals is whether the feedback signal adds to the input signal or if the feedback signal diminishes the input signal. When the feedback is positive, the signal being returned to the input is in phase with the input signal and thus interferes constructively. Figure 12-245 illustrates this concept applied in the amplified circuit through a block diagram. Notice that the feedback signal is in phase with the input signal, which regenerates the input signal. This results in an output signal with amplitude greater than would have been without the constructive, positive feedback. This type of positive feedback is what causes an audio system to squeal.

Figure 12-245 also illustrates with a block diagram how negative or degenerative feedback occurs. In this case, the feedback signal is out of phase with the input signal. This causes destructive interference and degenerates the input signal. The result is a lower amplitude output signal than would have occurred without the feedback.

### Operational Amplifiers (OP AMP)

An operational amplifier (OP AMP) is designed to be used with other circuit components and performs either computing functions or filtering. [Figure 12-246] Operational amplifiers are usually high-gain amplifiers with the amount of gain governed by the amount of feedback.

Operational amplifiers were originally developed for analog computers and used to perform mathematical functions. Today many devices use the operational amplifier for DC amplifiers, AC amplifiers, comparators, oscillators, and filter circuits. The widespread use is due to the fact that the OP AMP is a versatile device, small, and inexpensive. Built into the integrated chip, the operational amp is used as a basic building block of larger circuits.

There are two inputs to the operational amplifier, inverting (−) and non-inverting (+), and there is one output. The polarity NPN Input Class A amplifier Output VCC VEE + − − NPN Input Class AB amplifier Output VCC VEE + − − NPN Input Class B amplifier Output VCC VEE + − − of a signal applied to the inverting input (−) is reversed at the output. A signal applied to the non-inverting (+) input retains its polarity on the output. To be classified as an operational amplifier, the circuit must have certain characteristics:

1. Very high gain 2. Very high input impedance 3. Very high output impedance This type of a circuit can be made up of discrete components, such as resistors and transistors. However, the most common form of an operational amplifier is found in the integrated circuit. This integrated circuit or chip contains the various stages of the operational amplifier and can be treated as if it were a single stage.

The number of applications for OP AMPs is too numerous to detail in this handbook. However, the technician occasionally comes across these devices in modern aircraft and should be able to recognize their general purpose in a circuit. Some of the basic applications are:

1. Go/no-go detectors 2. Square wave circuits 3. Non-inverting amplifier 4. Inverting amplifier 5. Half-wave rectifier Input Impedance coupled amplifier Output Q1 Q2C1 VCC L1 NPN Input Class C amplifier Output VCC VEE + − − Input RC coupled amplifier Output Q1 Q2C1 VCC R1 R2

## 2. 中文翻译

<!-- TODO: 逐段翻译，段数与上面严格一一对应（31 段）。专业术语按行业惯例，数字与缩写保留。 -->

## 3. 专业词汇

<!-- TODO: 用表格 | 英文 | 词性 | 中文 | 本节语境 |，4~8 行。优先选下面 Glossary 里的词（本节原文出现过的）：
- Capacitor —— An electrical component that stores an electric charge.
- Current —— The flow of electrical charge.
- Difference —— The answer to a subtraction problem.
- Energy —— The capacity of a physical system to perform work. There are two types of energy, kinetic and potential.
- Frequency —— The number of cycles (on/off) completed per unit of time. Usually expressed in Hertz.
- Inductance —— The ability of a coil or conductor to oppose a change in current flow.
- Inductive reactance —— The opposition to the flow of current which inductances put in a circuit.
- Inductor —— A coil of wire that produces inductance in an electrical circuit.
-->

## 4. 语法解析

<!-- TODO: 2~4 个语法点，格式：
### ① 语法点名称
**原句**：<必须逐字来自第 1 节原文>
**拆解**：主/谓/宾、从句、非谓语等成分分析
**要点**：为什么这样用、易错点、可迁移的搭配
-->
