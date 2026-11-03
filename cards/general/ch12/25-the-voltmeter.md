# The Voltmeter

> 通用 Ch 12 · The Voltmeter · 原文 PDF 第 512 页

## 1. 原文

The voltmeter uses the same type of meter movement as the ammeter but employs a different circuit external to the meter movement.

As shown before, the voltage drop across the meter coil is a function of current and the coil resistance. In another example, 50 μA × 1,000 Ω = 50 mV . In order for the meter to be used to measure voltages greater than 50 mV , there must be added a series resistance to drop any excess voltage greater than that which the meter movement requires for a full-scale deflection. The case of the voltmeter, this resistance is called multiplier resistance and is designated as RM. [Figure 12-152] The voltmeter only has one multiplier resistor for use in one range. In this example, the full-scale reading is 1 volt. RM is determined in the following way:

The meter movement drops 50 mV at a full-scale deflection of 50 μA. The multiplying resistor RM must drop the remaining voltage of 1 V − 50 mV = 950 mV . Since RM is in series with the movement, it also carries 50 μA at full scale.

RM = = 19k Ω 950 mV50 μA Therefore, for 1 volt full-scale deflection, the total resistance of the voltmeter is 20k Ω. That is, the multiplier resistance and the coil resistance.

### Voltmeter Sensitivity

V oltmeter sensitivity is defined in terms of resistance per volt (Ω/V). The meter used in the previous example has a sensitivity of 20k Ω and a full-scale deflection of 1 volt.

### Multiple Range Voltmeters

The simplified voltmeter in Figure 12-152 has only one range (1 volt), which means that it can measure voltages from 0 volts to 1 volt. In order for the meter to be more useful, additional multiplier resistors must be used. One resistor must be used for each desired range.

For a 50 μA movement, the total resistance required is 20k Ω for each volt of full-scale reading. In other words, the sensitivity for a 50 μA movement is always 20k Ω regardless of the selected range. The full-scale meter current is 50 μA at any range selection. To find the total meter resistance, multiply the sensitivity by the full-scale voltage for that particular range. For example for a 10 volt range, RT = (20k Ω/V) (10V) = 200k Ω. The total resistance for the 1 volt range is 20k Ω, so RM for a 10 V range is 200k Ω − 20k Ω = 180k Ω. [Figure 12-153]

Closed air chamber Light vane swinging in chamber with small clearance 1mA, 50 ohm movement [+]

10mA 100mA 5.56Ω 5.51Ω

### Voltmeter Circuit Connections

When voltmeters are used, they are connected in parallel with a circuit. If unsure about the voltage to be measured, take the first reading at the high value on the meter and then progressively move down through the range until a suitable read is obtained. Observe that the polarity is correct before connecting the meter to the circuit or damage occurs by driving the movement backwards.

### Influence of the Voltmeter in the Circuit

When a voltmeter is connected across two points in a circuit, current is shunted. If the voltmeter has low resistance, it draws off a significant amount of current. This lowers the effective resistance of the circuit and change the voltage readings. When making a voltage measurement, use a high resistance voltmeter to prevent shunting of the circuit.

## 2. 中文翻译

<!-- TODO: 逐段翻译，段数与上面严格一一对应（15 段）。专业术语按行业惯例，数字与缩写保留。 -->

## 3. 专业词汇

<!-- TODO: 用表格 | 英文 | 词性 | 中文 | 本节语境 |，4~8 行。优先选下面 Glossary 里的词（本节原文出现过的）：
- Ammeter —— An instrument for measuring electric current in amperes.
- Current —— The flow of electrical charge.
- Resistance —— The opposition a device or material offers to the flow or current.
- Voltmeter —— A current-measuring instrument, designed to indicate voltage by measuring the current flow through a resistance of known value.
-->

## 4. 语法解析

<!-- TODO: 2~4 个语法点，格式：
### ① 语法点名称
**原句**：<必须逐字来自第 1 节原文>
**拆解**：主/谓/宾、从句、非谓语等成分分析
**要点**：为什么这样用、易错点、可迁移的搭配
-->
