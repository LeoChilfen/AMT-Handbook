# DC Measuring Instruments

> 通用 Ch 12 · DC Measuring Instruments · 原文 PDF 第 509 页

## 1. 原文

Understanding the functional design and operation of electrical measuring instruments is very important, since they are used in repairing, maintaining, and troubleshooting electrical circuits. The best and most expensive measuring instrument is of no use unless the technician knows what is Red Red Red - Yellow Yellow Black Iron core High-voltage winding 5-volt winding 6-volt winding Secondary windings Black Primary Yellow Green Green Green - Yellow Yellow - Blue 1 2 Input Output 3 Primary 1–2 1–2 1–3 1–3 2–3 2–3 used with “ ”

Secondary 1–3 2–3 1–2 2–3 1–3 1–2 A B transformer.

being measured and what each reading indicates. The purpose of the meter is to measure quantities existing in a circuit. For this reason, when a meter is connected to a circuit, it must not change the characteristics of that circuit.

Meters are either self-excited or externally excited. Those that are self-excited operate from a power source within the meter. Externally-excited meters get their power source from the circuit that they are connected to. The most common analog meters in use today are the voltmeter, ammeter, and ohmmeter. All of which operate on the principles of electromagnetism. The fundamental principle behind the operation of the meter is the interaction between magnetic fields created by a current gathered from the circuit in some manner. This interaction is between the magnetic fields of a permanent magnet and the coils of a rotating magnet. The greater the current through the coils of the rotating magnet, the stronger the magnetic field produced. A stronger field produces greater rotation of the coil. While some meters can be used for both DC and AC circuit measurement, only those used as DC instruments are discussed in this section. The meters used for AC, or for both AC and DC, are discussed in the study of AC theory and circuitry.

### D’Arsonval Meter Movement

This basic DC type of meter movement—first employed by the French scientist, d’Arsonval, in making electrical measurement—is a current measuring device, which is used in the ammeter, voltmeter, and ohmmeter. The pointer is deflected in proportion to the amount of current through the coil. Basically, both the ammeter and the voltmeter are current measuring instruments, the principal difference being the method in which they are connected in a circuit. While an ohmmeter is also basically a current measuring instrument, it differs from the ammeter and voltmeter in that it provides its own source (self-excited) of power and contains other auxiliary circuits.

### Current Sensitivity and Resistance

The current sensitivity of a meter movement is the amount of current required to drive the meter movement to a full-scale deflection. A simple example would be a meter movement that has 1 mA sensitivity. What this indicates is that meter movement requires 1 mA of current to move the needle to a full-scale indication. Likewise, a half-scale deflection requires only 0.5 mA of current. Additionally, what is called movement resistance is the actual DC resistance of the wire used to construct the meter coil.

In a standard d’Arsonval meter, movement may have a current sensitivity of 1 mA and a resistance of 50 Ω. If the meter is going to be used to measure more than 1 mA, then additional circuitry is required to accomplish the task. This additional circuitry is a simple shunt resistor. The purpose of the shunt resistor is to bypass current that exceeds the 1 mA limitation of the meter movement. To illustrate this, assume that the 1 mA meter in question is needed to measure 10 mA. The shunt resistor used should carry 9 mA while the remaining 1 mA is allowed to pass through the meter. [Figure 12-149]

To determine the proper shunt resistance for this situation: R SH = Shunt resistance R M = Meter resistance = 50 Ω Because the shunt resistance and the 50 Ω meter resistance are in parallel, the voltage drop across both of them is the same.

E SH = EM Using Ohm’s Law, this relationship can be rewritten as:

E SH = ISH × RSH E M = IM × RM I SH × RSH = IM × RM Simply solve for RSH RSH = IM × RMISH Substituting the values RSH = = 5.56 ΩImA × 50 Ω9 mA

To make meter readings quickly and accurately, it is desirable that the moving pointer overshoot its proper position only a small amount and come to rest after not more than one or two small oscillations. The term “damping” is applied to methods used to bring the pointer of an electrical meter to rest after it has been set in motion. Damping may be accomplished by electrical means, by mechanical means, or by a combination of both.

### Electrical Damping

A common method of damping by electrical means is to wind the moving coil on an aluminum frame. As the coil moves in the field of the permanent magnet, eddy currents are set up in the aluminum frame. The magnetic field produced by the eddy currents opposes the motion of the coil. The pointer therefore swings more slowly to its proper position and comes to rest quickly with very little oscillation.

### Mechanical Damping

Air damping is a common method of damping by mechanical means. As shown in Figure 12-150, a vane is attached to the shaft of the moving element and enclosed in an air chamber. The movement of the shaft is retarded because of the resistance that the air offers to the vane. Effective damping is achieved if the vane nearly touches the walls of the chamber.

### A Basic Multirange Ammeter

Building upon the basic meter previously discussed is the more complex and useful multirange meter, which is more practical. The basic idea of a multirange ammeter is to make the meter usable over a wide range of voltages. In order to accomplish this, each range must utilize a different shunt resistance. The example given in this handbook is that of a two-range meter. However, once the basics of a two-range multirange ammeter are understood, the concepts can easily be transferred to the design of meters with many selectable ranges.

Figure 12-151 shows the schematic of an ammeter with two selectable ranges. This example builds upon the previous 10 mA range meter by adding a 100 mA range. With the switch selected to the 10 mA range, the meter indicates 10 mA when the needle is deflected to full-scale and likewise indicates 100 mA at full-scale when selected to 100 mA. The value of the 100 mA shunt resistor is determined the same way the 10 mA shunt resistor was determined. Recall that the meter movement can only carry 1 mA. This means that in a 100 mA range the remaining current of 99 mA must pass through the shunt resistor.

RSH = IM × RMISH Substituting the values:

RSH = = 0.51 ΩImA × 50 Ω99 mA

The precautions to observe when using an ammeter are summarized as follows:

1. Always connect ammeter in series with the element Meter movement [+] [−]

RSH ISH IMM Meter movement Basic ammeter [+] [−]

RSH ISH 1 mA 10 mA 9 mA through which the current flow is to be measured.

2. Never connect an ammeter across a source of voltage, such as a battery or generator. Remember that the resistance of an ammeter, particularly on the higher ranges, is extremely low and that any voltage, even a volt or so, can cause very high current to flow through the meter, causing damage to it.

3. Use a range large enough to keep the deflection less than full-scale. Before measuring a current, form some idea of its magnitude. Then switch to a large enough scale or start with the highest range and work down until the appropriate scale is reached. The most accurate readings are obtained at approximately half-scale deflection. Many milliammeters have been ruined by attempts to measure amperes. Therefore, be sure to read the lettering either on the dial or on the switch positions and choose proper scale before connecting the meter in the circuit.

4. Observe proper polarity in connecting the meter in the circuit. Current must flow through the coil in a definite direction in order to move the indicator needle up scale. Current reversal because of incorrect connection in the circuit results in a reversed meter deflection and frequently causes bending of the meter needle. Avoid improper meter connections by observing the polarity markings on the meter.

## 2. 中文翻译

<!-- TODO: 逐段翻译，段数与上面严格一一对应（29 段）。专业术语按行业惯例，数字与缩写保留。 -->

## 3. 专业词汇

<!-- TODO: 用表格 | 英文 | 词性 | 中文 | 本节语境 |，4~8 行。优先选下面 Glossary 里的词（本节原文出现过的）：
- Ammeter —— An instrument for measuring electric current in amperes.
- Current —— The flow of electrical charge.
- Difference —— The answer to a subtraction problem.
- Ohm’s Law —— Explains the relationship between voltage, current, and resistance in an electrical circuit, and states that current flow in an electrical circuit is directly p
- Ohmmeter —— A current measuring instrument that provides its own source (self-excited) of power.
- Power (exponent) —— A shorthand method of indicating how many times a number, called the base, is multiplied by itself. For example, in the number 43, 3 is the power, or exponent, 
- Power —— Power is the time rate at which work is done or energy is transferred.
- Proportion —— A proportion is a statement of equality between two or more ratios. The example of A is to B as C is to D can be represented A:B = C:D or A/B = C/D.
-->

## 4. 语法解析

<!-- TODO: 2~4 个语法点，格式：
### ① 语法点名称
**原句**：<必须逐字来自第 1 节原文>
**拆解**：主/谓/宾、从句、非谓语等成分分析
**要点**：为什么这样用、易错点、可迁移的搭配
-->
