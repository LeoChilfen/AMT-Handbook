# Magnetic Amplifiers

> 通用 Ch 12 · Magnetic Amplifiers · 原文 PDF 第 560 页

## 1. 原文

Magnetic amplifiers do not amplify magnetism but use electromagnetism to amplify a signal. Essentially, the magnetic amplifier is a power amplifier with a very limited frequency response. The frequency range most commonly associated with the magnetic amplifier is 100 Hz and less, which places it in the audio range. As a technical point, the magnetic amplifier is a low-frequency amplifier.

Advantages of the magnetic amplifier are:

1. Very high efficiency, on the order of approximately 90 percent 2. High reliability 3. Very rugged, able to withstand vibrations, moisture, and overloads 4. No warm-up time Some of the disadvantages of the magnetic amplifier are:

1. Incapacity to handle low-voltage signals 2. Not usable in high-frequency applications 3. Time delay associated with magnetic affects 4. Poor fidelity The basic operating principles of the magnetic amplifier are fairly simple. Keep in mind that all amplifiers are current control devices. In this particular case, power that is delivered to the load is controlled by a variable inductance.

If an AC voltage is applied to the primary winding of an iron core transformer, the iron core is magnetized and demagnetized at the same frequency as that of the applied voltage. This, in turn, induces a voltage in the transformers secondary winding. The output voltage across the terminals of the secondary depends on the relationship of the number of turns in the primary and the secondary of the transformer.

The iron core of the transformer has a saturation point after which the application of a greater magnetic force produces no change in the intensity of magnetization. Hence, there is no change in transformer output, even if the input is greatly increased. The magnetic amplifier circuit in Figure 12-247 is used to explain how a simple magnetic amplifier functions.

1. Assume that there is 1 ampere of current in coil A, which has 10 turns of wire. If coil B has 10 turns of wire, an output of 1 ampere is obtained if coil B is properly loaded.

2. By applying direct current to coil C, the core of the magnetic amplifier coil can be further magnetized. Assume that coil C has the proper number of turns and, upon the application of 30 milliamperes, that the core Input Transformer coupled amplifier Output Q1 Q2T1 VCC Input Positive feedback Negative feedback Output Input Output is magnetized to the point where 1 ampere on coil A results in only 0.24 ampere output from coil B.

3. By making the DC input to coil C a continuous variable from 0 to 30 milliamperes and by maintaining an input of 1 ampere on coil A, it is possible to control the output of coil B to any point between 0.24 ampere and 1 ampere in this example.

The term “amplifier” is used for this arrangement because, by use of a few milliamperes, control of an output of 1 or more amperes is obtained.

### Saturable-Core Reactor

The same procedure can be used with the circuit shown in Figure 12-248. A saturable-core reactor is a magnetic- core coil whose reactance is controlled by changing the permeability of the core. Varying the unidirectional flux controls the permeability of the core.

By controlling the extent of magnetization of the iron ring, it is possible to control the amount of current flowing to the load, since the amount of magnetization controls the impedance of the AC input winding. This type of magnetic amplifier is called a simple saturable reactor circuit.

Adding a rectifier to such a circuit would remove half the cycle of the AC input and permit DC to flow to the load. The amount of DC flowing in the load circuit is controlled by a DC control winding (sometimes referred to as bias). This type of magnetic amplifier is referred to as being self-saturating.

To use the full AC input power, a circuit such as that shown in Figure 12-249 may be used. This circuit uses a full-wave bridge rectifier. The load receives a controlled DC by using the full AC input. This type of circuit is known as a self- saturating, full-wave magnetic amplifier.

In Figure 12-250, it is assumed that the DC control winding is supplied by a variable source, such as a sensing circuit. To control such a source and use its variations to control the AC output, it is necessary to include another DC winding that has a constant value. This winding, referred to as the reference winding, magnetizes the magnetic core in one direction.

The DC control winding, acting in opposition to the reference winding, either increases (degenerative) or decreases (regenerative) the magnetization of the core to change the amount of current flowing through the load. This is essentially a basic preamplifier.

## 2. 中文翻译

<!-- TODO: 逐段翻译，段数与上面严格一一对应（17 段）。专业术语按行业惯例，数字与缩写保留。 -->

## 3. 专业词汇

<!-- TODO: 用表格 | 英文 | 词性 | 中文 | 本节语境 |，4~8 行。优先选下面 Glossary 里的词（本节原文出现过的）：
- Ampere —— A unit of measure of the rate of electron flow or current in an electrical conductor. One ampere of current represents one coulomb of electrical charge (6.24 × 
- Current —— The flow of electrical charge.
- Direct current (DC) —— Electricity that flows in one direction at all times.
- Force —— The intensity of an impetus, or the intensity of an input.
- Frequency —— The number of cycles (on/off) completed per unit of time. Usually expressed in Hertz.
- Inductance —— The ability of a coil or conductor to oppose a change in current flow.
- Permeability —— Used to refer to the ease with which a magnetic flux can be established in a given magnetic circuit.
- Power (exponent) —— A shorthand method of indicating how many times a number, called the base, is multiplied by itself. For example, in the number 43, 3 is the power, or exponent, 
-->

## 4. 语法解析

<!-- TODO: 2~4 个语法点，格式：
### ① 语法点名称
**原句**：<必须逐字来自第 1 节原文>
**拆解**：主/谓/宾、从句、非谓语等成分分析
**要点**：为什么这样用、易错点、可迁移的搭配
-->
