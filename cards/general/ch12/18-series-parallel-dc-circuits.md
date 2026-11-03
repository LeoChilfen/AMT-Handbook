# Series-Parallel DC Circuits

> 通用 Ch 12 · Series-Parallel DC Circuits · 原文 PDF 第 484 页

## 1. 原文

Most of the circuits that the technician encounters will not be a simple series or parallel circuit. Circuits are usually a combination of both, known as series-parallel circuits, which are groups consisting of resistors in parallel and in series. An example of this type of circuit is shown here. While the series-parallel circuit can initially appear to be complex, the same rules that have been used for the series and parallel circuits can be applied to these circuits.

The voltage source provides a current out to resistor R 1, then to the group of resistors R2 and R3 and then to the next resistor R4 before returning to the voltage source. The first step in the simplification process is to isolate the group R 2 and R3 and recognize that they are a parallel network that can be reduced to an equivalent resistor. Using the formula for parallel resistance, R23 = R2 + R3 R2R3 R2 and R3 can be reduced to R23. An equivalent circuit now has three series connected resistors. The total resistance of the circuit can now be simply determined by adding up the values of resistors R1, R23, and R4.

### Determining the Total Resistance

A more quantitative example for determining total resistance and the current in each branch in a combination circuit is shown in the following example.

The first step is to determine the current at junction A, leading into the parallel branch. To determine the IT, the total + − R1 R2ES R3 A B R4 + − R1 R23ES R4 resistors.

1k Ω 2k Ω 3k Ω + − R1 R2 ES=24 V R3 A B resistance RT of the entire circuit must be known. The total resistance of the circuit is given as:

RT = R1 + R23 Where R23 = ( ) Parallel network R2 + R3 R2R3 Find REQ R23 = 2k Ω + 3k Ω 2k Ω 3k Ω Solve for REQ R23 = 5k Ω 6,000k Ω R23 = 1.2k Ω Solve for RT RT = 1k Ω + 1.2k Ω RT = 2.2k Ω With the total resistance RT now determined, the total IT can be determined. Using Ohm’s Law:

IT = RT ES Substitute values IT = 2.2k Ω 24 VIT = 10.9 mA The current through the parallel branches of R 2 and R3 can be determined using the current divider rule discussed earlier in this handbook.

Recall Parallel Branch Resistance:

R23 = 5,000 Ω 6,000 Ω R23 = 1.2k Ω Substitute values for I2:

I2 = x (10.9 mA) 2,000 Ω1,200 Ω I2 = 6.54 mA Now using Kirchhoff’s Current Law, the current in the branch with R3 can be determined.

I 2 + I3 = IT Recall that IT = 10.9 mA I T – I2 = I3 Also recall that I2 = 6.54 mA Subtract I2 from IT to get I3 I 3 = 4.36 mA

## 2. 中文翻译

技术人员遇到的大多数电路都不是简单的串联或并联电路。电路通常是两者的组合，称为串并联电路，即由并联和串联的电阻构成的组。这类电路的一个例子如图所示。串并联电路乍看可能很复杂，但用于串联电路和并联电路的同样规则都可以应用到这些电路上。

电压源把电流送出到电阻 R1，再送到 R2 与 R3 这一组电阻，然后送到下一只电阻 R4，最后回到电压源。化简过程的第一步，是把 R2 与 R3 这一组单独拿出来，认出它们是一个可化为等效电阻的并联网络。用并联电阻公式 R23 = R2R3/（R2 + R3），R2 与 R3 可化为 R23。于是等效电路由三只串联电阻组成。现在只要把 R1、R23 和 R4 的值相加，就能简单地求出电路的总电阻。

### 确定总电阻

下面这个例子给出一个更定量的组合电路示例，用于确定总电阻和每条支路中的电流。（原文此处为图注碎片，为串并联组合电路的示意图）

第一步是确定汇入并联支路的节点 A 处的电流。要确定 IT，整个电路的总电阻 RT 必须已知。

（原文此处为图注碎片，为 1 kΩ、2 kΩ、3 kΩ 各电阻与 24 V 电源、节点 A、B 的标示图）电路的总电阻由下式给出：

RT = R1 + R23，其中并联网络 R23 = R2R3/（R2 + R3）。求 REQ：R23 =（2 kΩ × 3 kΩ）/（2 kΩ + 3 kΩ）。求解 REQ：R23 = 6,000k Ω/5k Ω，R23 = 1.2 kΩ。求 RT：RT = 1 kΩ + 1.2 kΩ，RT = 2.2 kΩ。总电阻 RT 既已确定，总电流 IT 也就可以求出。用欧姆定律：

IT = ES/RT。代入数值：IT = 24 V/2.2 kΩ，IT = 10.9 mA。R2 与 R3 并联支路中的电流，可以用本手册前面讨论过的分流法则求出。

回顾并联支路电阻：

R23 =（5,000 Ω × 6,000 Ω）/（5,000 Ω + 6,000 Ω），R23 = 1.2 kΩ。代入 I2 的数值：

I2 =（1,200 Ω/2,000 Ω）×（10.9 mA），I2 = 6.54 mA。现在用基尔霍夫电流定律，可求出 R3 所在支路中的电流。

I2 + I3 = IT。记得 IT = 10.9 mA，IT – I2 = I3。又记得 I2 = 6.54 mA，从 IT 中减去 I2 得 I3：I3 = 4.36 mA

## 3. 专业词汇

| 英文 | 词性 | 中文 | 本节语境 |
| --- | --- | --- | --- |
| series-parallel circuit | n. | 串并联电路 | 串联与并联组合而成的电路，由并联和串联的电阻构成 |
| combination circuit | n. | 组合电路 | 既非纯串联也非纯并联的电路，串并联电路的同义说法 |
| equivalent resistor | n. | 等效电阻 | 并联网络可化为一只电阻替代，如 R23 |
| parallel network | n. | 并联网络 | 由 R2 与 R3 构成的并联部分，可用并联电阻公式化简 |
| total resistance | n. | 总电阻 | 化简后由 R1、R23、R4 相加求得，记作 RT |
| simplification | n. | 化简 | 把复杂电路逐步化为串联体的过程 |
| junction | n. | 节点 | 电流分为并联支路之处，如节点 A、B |
| current divider rule | n. | 分流法则 | 由总电流求各并联支路电流的方法 |
| Kirchhoff’s Current Law | n. | 基尔霍夫电流定律 | 用于由 IT 与 I2 反推 I3 |
| branch | n. | 支路 | 并联网络中每条电流通路，如 R2、R3 所在支路 |
| voltage source | n. | 电压源 | 向 R1 送出电流、经 R4 后电流返回的电源 |
| REQ | n. | 等效电阻值 | 求解并联网络时使用的等效电阻符号 |

## 4. 语法解析

### ① that 定语从句 + 否定谓语
**原句**：Most of the circuits that the technician encounters will not be a simple series or parallel circuit.
**拆解**：主语中心词 Most of the circuits，后接 that 引导的定语从句 the technician encounters；主句谓语 will not be，表语 a simple series or parallel circuit。
**要点**：that 在定语从句中作 encounters 的宾语，可省略；most of the + 复数名词作主语时谓语用复数；will not be 用将来时表一般判断，比 is not 语气缓和。

### ② While 让步从句 + 被动谓语 + appear to be
**原句**：While the series-parallel circuit can initially appear to be complex, the same rules that have been used for the series and parallel circuits can be applied to these circuits.
**拆解**：While 引导让步状语从句，从句谓语 appear to be 表“看起来”的判断；主句主语 the same rules 后接 that 定语从句（have been used for…），谓语 can be applied to 为被动。
**要点**：while 在此表让步“虽然”，与表时间的“当……时”要区分；appear to be + 形容词意为“看起来……”；apply A to B 变被动后为 A can be applied to B，介词 to 不能丢。

### ③ 不定式作表语并列 + that 宾语从句套定语从句
**原句**：The first step in the simplification process is to isolate the group R2 and R3 and recognize that they are a parallel network that can be reduced to an equivalent resistor.
**拆解**：主语 The first step in the simplification process，谓语 is，表语为两个并列不定式 to isolate… and recognize…；recognize 后接 that 宾语从句，从句中 a parallel network 又带 that 定语从句（can be reduced to an equivalent resistor）。
**要点**：主语为 step 时表语常用不定式，说明“该做的是”；isolate 意为“隔离出来”；be reduced to 是“被化简为”，与上文 reduce 呼应。

### ④ with 独立主格 + 被动谓语
**原句**：With the total resistance RT now determined, the total IT can be determined.
**拆解**：With + 名词 + 过去分词（now determined）构成独立主格，作时间/条件状语；主句主语 the total IT，谓语 can be determined 为被动。
**要点**：独立主格中 determine 与 RT 是被动关系，故用过去分词 determined；主句的 can be determined 与独立主格中的 determined 同词不同语法功能，注意区分；with 结构可改写为 Now that the total resistance RT has been determined。

### ⑤ provide A to B + before + 动名词
**原句**：The voltage source provides a current out to resistor R1, then to the group of resistors R2 and R3 and then to the next resistor R4 before returning to the voltage source.
**拆解**：主句谓语 provides a current out to…，then to… and then to… 为并列的方向状语；before returning 为介词 + 动名词，逻辑主语与主句主语 the voltage source 一致。
**要点**：provide A to B 意为“把 A 提供给 B”，out 为副词表“送出”；then to 承前省略了 provides a current；before doing 表示“在……之前”，主语相同时不能用 before it returns 之外的从句形式随意替换语序。
