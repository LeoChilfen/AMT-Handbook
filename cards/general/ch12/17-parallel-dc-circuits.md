# Parallel DC Circuits

> 通用 Ch 12 · Parallel DC Circuits · 原文 PDF 第 482 页

## 1. 原文

A circuit in which two of more electrical resistances or loads are connected across the same voltage source is called a parallel circuit. The primary difference between the series circuit and the parallel circuit is that more than one path is provided for the current in the parallel circuit. Each of these parallel paths is called a branch. The minimum requirements for a parallel circuit are the following:

• A resistance or load for each current path

• Two or more paths for current flow Figure 12-96 depicts the most basic parallel circuit. Current flowing out of the source divides at point A in the diagram and goes through R1 and R2. As more branches are added to the circuit, more paths for the source current are provided.

The first point to understand is that the voltage across any branch is equal to the voltage across all of the other branches.

### Total Parallel Resistance

The parallel circuit consists of two or more resistors connected in such a way as to allow current flow to pass through all of the resistors at once. This eliminates the need for current to pass one resistor before passing through the next. When resistors are connected in parallel, the total resistance of the circuit decreases. The total resistance of a parallel combination is always less than the value of the smallest resistor in the circuit. In the series circuit, the current has to pass through the resistors one at a time. This gave a resistance to the current equal the sum of all the resistors. In the parallel circuit, the current has several resistors that it can pass through, actually reducing the total resistance of the circuit in relation to any one resistor value.

The amount of current passing through each resistor varies according to its individual resistance. The total current of the circuit is the sum of the current in all branches. It can be determined by inspection that the total current is greater than that of any given branch. Using Ohm’s Law to calculate the total resistance based on the applied voltage and the total current, it can be determined that the total resistance is less than any branch.

An example of this is if there was a circuit with a 100 Ω resistor and a 5 Ω resistor; while the exact value must be calculated, it still can be said that the combined resistance between the two is less than the 5 Ω.

### Resistors in Parallel

The formula for the total parallel resistance is as follows:

1 RT = + + + ... 1R1 1 R2 1R3 1RN If the reciprocal of both sides is taken, then the general formula for the total parallel resistance is:

RT = + + + ... 1R1 1 R2 1R3 1RN 1

### Two Resistors in Parallel

Typically, it is more convenient to consider only two resistors at a time because this setup occurs in common practice. Any number of resistors in a circuit can be broken down into pairs. Therefore, the most common method is to use the formula + − + − + − R1 A B R2ES for two resistors in parallel.

RT = + 1R1 1 R2 1 Combining the terms in the denominator and rewriting:

RT = R1 + R2 R1R2 Put in words, this states that the total resistance for two resistors in parallel is equal to the product of both resistors divided by the sum of the two resistors. In the formula below, calculate the total resistance.

General formula RT = R1 + R2 R1R2 Known values R1 = 500 Ω R2 = 400 Ω RT = 500 Ω + 400 Ω 500 Ω 400 Ω RT = 900 Ω 200,000 Ω RT = 222.22 Ω

A current source is an energy source that provides a constant value of current to a load even when the load changes in resistive value. The general rule to remember is that the total current produced by current sources in parallel is equal to the algebraic sum of the individual sources.

### Kirchhoff’s Current Law

Kirchhoff’s Current Law can be stated as: the sum of the currents into a junction or node is equal to the sum of the currents flowing out of that same junction or node. A junction can be defined as a point in the circuit where two or more circuit paths come together. In the case of the parallel circuit, it is the point in the circuit where the individual branches join.

General formula IT = I1 + I2 + I3 Refer to Figure 12-97 for an example. Point A and point B represent two junctions or nodes in the circuit with three resistive branches in between. The voltage source provides a total current IT into node A. At this point, the current must divide, flowing out of node A into each of the branches according to the resistive value of each branch. Kirchhoff’s Current Law states that the current going in must equal that going out. Following the current through the three branches and back into node B, the total current I T entering node B and leaving node B is the same as that which entered node A. The current then continues back to the voltage source.

Figure 12-98 shows that the individual branch currents are:

I 1 = 5 mA I 2 = 12 mA The total current flow into the node A equals the sum of the branch currents, which is: IT = I1 + I2 Substitute IT = 5 mA + 12 mA IT = 17 mA The total current entering node B is also the same.

Figure 12-99 illustrates how to determine an unknown current in one branch. Note that the total current into a junction of the three branches is known. Two of the branch currents are known. By rearranging the general formula, the current in branch two can be determined.

General formula IT = I1 + I2 + I3 Substitute 75 mA = 30 mA + I2 + 20 mA Solve I2 I2 = 75 mA – 30 mA – 20 mA I2 = 25 mA

### Current Dividers

It can now be easily seen that the parallel circuit is a current divider. As shown in Figure 12-96, there is a current through each of the two resistors. Because the same voltage is applied across both resistors in parallel, the branch currents are inversely proportional to the ohmic values of the resistors. Branches with higher resistance have less current than those with lower resistance. For example, if the resistive value of R2 is twice as high as that of R1, the current in R2 is half of that of R1. All of this can be determined with Ohm’s Law.

By Ohm’s Law, the current through any one of the branches can be written as:

+ − + − + − + − R1 R2 A B R3ES IT IT I1 I3 + − + − + − + − A B ES I1=30 mA I3=20 mA I2=?

IT=75 mA IT=75 mA + − + − + − A B ES I2=12 mA R2R1 IT=17 mA IT=17 mA I1=5 mA I X = ES/RX The voltage source appears across each of the parallel resistors and RX represents any one the resistors. The source voltage is equal to the total current times the total parallel resistance.

E S = ITRT Substituting ITRT for ES ITRT RX IX = Rearranging RT RX IX = ( ) IT R2 RT I2 = ( ) IT And R1 RT I1 = ( ) IT This formula is the general current divider formula. The current through any branch equals the total parallel resistance divided by the individual branch resistance, multiplied by the total current.

## 2. 中文翻译

<!-- TODO: 逐段翻译，段数与上面严格一一对应（31 段）。专业术语按行业惯例，数字与缩写保留。 -->

## 3. 专业词汇

<!-- TODO: 用表格 | 英文 | 词性 | 中文 | 本节语境 |，4~8 行。优先选下面 Glossary 里的词（本节原文出现过的）：
- Current —— The flow of electrical charge.
- Denominator —— The lower part of a fraction (represented by the letter D in N⁄D), the quantity by which the numerator is divided.
- Difference —— The answer to a subtraction problem.
- Energy —— The capacity of a physical system to perform work. There are two types of energy, kinetic and potential.
- Ohm’s Law —— Explains the relationship between voltage, current, and resistance in an electrical circuit, and states that current flow in an electrical circuit is directly p
- Parallel circuit —— A circuit in which two or more electrical resistances or loads are connected across the same voltage source.
- Product —— The result of multiplication.
- Resistance —— The opposition a device or material offers to the flow or current.
-->

## 4. 语法解析

<!-- TODO: 2~4 个语法点，格式：
### ① 语法点名称
**原句**：<必须逐字来自第 1 节原文>
**拆解**：主/谓/宾、从句、非谓语等成分分析
**要点**：为什么这样用、易错点、可迁移的搭配
-->
