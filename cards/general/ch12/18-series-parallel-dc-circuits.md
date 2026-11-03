# Series-Parallel DC Circuits

> 通用 Ch 12 · Series-Parallel DC Circuits · 原文 PDF 第 484 页

## 1. 原文

Most of the circuits that the technician encounters will not be a simple series or parallel circuit. Circuits are usually a combination of both, known as series-parallel circuits, which are groups consisting of resistors in parallel and in series. An example of this type of circuit can be seen in Figure 12-100. While the series-parallel circuit can initially appear to be complex, the same rules that have been used for the series and parallel circuits can be applied to these circuits.

The voltage source provides a current out to resistor R 1, then to the group of resistors R2 and R3 and then to the next resistor R4 before returning to the voltage source. The first step in the simplification process is to isolate the group R 2 and R3 and recognize that they are a parallel network that can be reduced to an equivalent resistor. Using the formula for parallel resistance, R23 = R2 + R3 R2R3 R2 and R3 can be reduced to R23. Figure 12-101 now shows an equivalent circuit with three series connected resistors. The total resistance of the circuit can now be simply determined by adding up the values of resistors R1, R23, and R4.

### Determining the Total Resistance

A more quantitative example for determining total resistance and the current in each branch in a combination circuit is shown in the following example. [Figure 12-102]

The first step is to determine the current at junction A, leading into the parallel branch. To determine the IT, the total + − R1 R2ES R3 A B R4 + − R1 R23ES R4 resistors.

1k Ω 2k Ω 3k Ω + − R1 R2 ES=24 V R3 A B resistance RT of the entire circuit must be known. The total resistance of the circuit is given as:

RT = R1 + R23 Where R23 = ( ) Parallel network R2 + R3 R2R3 Find REQ R23 = 2k Ω + 3k Ω 2k Ω 3k Ω Solve for REQ R23 = 5k Ω 6,000k Ω R23 = 1.2k Ω Solve for RT RT = 1k Ω + 1.2k Ω RT = 2.2k Ω With the total resistance RT now determined, the total IT can be determined. Using Ohm’s Law:

IT = RT ES Substitute values IT = 2.2k Ω 24 V IT = 10.9 mA The current through the parallel branches of R 2 and R3 can be determined using the current divider rule discussed earlier in this handbook.

Recall Parallel Branch Resistance:

R23 = 5,000 Ω 6,000 Ω R23 = 1.2k Ω Substitute values for I2:

I2 = x (10.9 mA) 2,000 Ω1,200 Ω I2 = 6.54 mA Now using Kirchhoff’s Current Law, the current in the branch with R3 can be determined.

I 2 + I3 = IT Recall that IT = 10.9 mA I T – I2 = I3 Also recall that I2 = 6.54 mA Subtract I2 from IT to get I3 I 3 = 4.36 mA

## 2. 中文翻译

<!-- TODO: 逐段翻译，段数与上面严格一一对应（12 段）。专业术语按行业惯例，数字与缩写保留。 -->

## 3. 专业词汇

<!-- TODO: 用表格 | 英文 | 词性 | 中文 | 本节语境 |，4~8 行。优先选下面 Glossary 里的词（本节原文出现过的）：
- Current —— The flow of electrical charge.
- Ohm’s Law —— Explains the relationship between voltage, current, and resistance in an electrical circuit, and states that current flow in an electrical circuit is directly p
- Parallel circuit —— A circuit in which two or more electrical resistances or loads are connected across the same voltage source.
- Resistance —— The opposition a device or material offers to the flow or current.
-->

## 4. 语法解析

<!-- TODO: 2~4 个语法点，格式：
### ① 语法点名称
**原句**：<必须逐字来自第 1 节原文>
**拆解**：主/谓/宾、从句、非谓语等成分分析
**要点**：为什么这样用、易错点、可迁移的搭配
-->
