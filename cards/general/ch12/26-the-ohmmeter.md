# The Ohmmeter

> 通用 Ch 12 · The Ohmmeter · 原文 PDF 第 513 页

## 1. 原文

The meter movement used for the ammeter and the voltmeter can also be used for the ohmmeter. The function of the ohmmeter is to measure resistance. A simplified one-stage ohmmeter is illustrated in the figure, which shows that the basic ohmmeter contains a battery and a variable resistor in series with the meter movement. To measure resistance, the leads of the meter are connected across an external resistance, which is to be measured. By doing this, the ohmmeter circuit is completed. This connection allows the internal battery to produce a current through the movement coil, causing a deflection of the pointer proportional to the value of the external resistance being measured.

When the ohmmeter leads are open, the meter is at a full-scale deflection, indicating an infinite (∞) resistance or an open circuit. When the leads are shorted as shown in figure “zero adjust,” the pointer is at the full right-hand position, indicating a short circuit or zero resistance. The purpose of the variable resistor in this figure is to adjust the current so that the pointer is at exactly zero when the leads are shorted. This is used to compensate for changes in the internal battery voltage due to aging.

The figure shows a typical analog ohmmeter scale. Between zero and infinity (∞), the scale is marked to indicate various resistor values. Because the values decrease from left to right, this scale is often called a back-off scale.

In the case of the example given, assume that a certain ohmmeter uses a 50 μA, 1,000 Ω meter movement and has an internal 1.5 volt battery. A current of 50 μA produces a full-scale deflection when the test leads are shorted. To have 50 μA, the total ohmmeter resistance is 1.5 V/50 μA = 30k Ω. Therefore, since the coil resistance is 1k Ω, the variable zero adjustment resistor must be set to 30k Ω – 1k Ω = 29k Ω.

Now consider that a 120k Ω resistor is connected to the ohmmeter leads. Combined with the 30k Ω internal resistance, the total R is 150k Ω. The current is 1.5 V/150k Ω = 10 μA, which is 20 percent of the full-scale current and appears on the scale shown in the figure.

Now consider further that a 120k Ω resistor is connected to the ohmmeter leads. This results in a current of 1.5 V/75k Ω = 10 μA, which is 40 percent of the full-scale current and marked on the scale. Additional calculations of this type show that the scale is nonlinear. It is more compressed toward the left side than the right side. The center scale point corresponds to the internal meter resistance of 30k Ω. The reason is as follows:

10 V 1 V RM2 180k Ω 19k Ω RM1 0∞ Basic voltmeter 50A, 1k ohm movement [+] [−]

With 30k Ω connected to the leads, the current is 1.5 V/60k Ω = 25 μA, which is half of the full-scale current of 50 μA.

### The Multirange Ohmmeter

A practical ohmmeter has several operational ranges. These typically are indicated by R × 1, R × 10, R × 100, R × 1k, R × 100k and R × 1M. These range selections are interpreted in a different manner than that of an ammeter or voltmeter. The reading on the ohmmeter scale is multiplied by the factor indicated by the range setting. For example, if the pointer is set on the scale and the range switch is set at R × 100, the actual resistance measurement is 20 × 100 or 2k Ω.

To measure small resistance values, the technician must use a higher ohmmeter current than is needed for measuring large resistance values. Shunt resistors are needed to provide multiple ranges on the ohmmeter to measure a range of resistance values from the very small to very large. For each range, a different value of shunt resistance is switched in. The shunt resistance increases for higher ohm ranges and is always equal to the center scale reading on any selected range. In some meters, a higher battery voltage is used for the highest ohm range.

### Megger (Megohmmeter)

The megger, or megohmmeter, is a high range ohmmeter containing a hand-operated generator. It is used to measure insulation resistance and other high-resistance values. It is also used for ground, continuity, and short-circuit testing of electrical power systems. The chief advantage of the megger over an ohmmeter is its capacity to measure resistance with a high potential, or “breakdown” voltage. This type of testing ensures that insulation or a dielectric material will not short or leak under potential electrical stress.

The megger consists of two primary elements, both of which are provided with individual magnetic fields from a common permanent magnet: a hand-driven DC generator, G, which supplies the necessary current for making the measurement; and the instrument portion, which indicates the value of the resistance being measured. The instrument portion is of the opposed coil type. Coils A and B are mounted on the movable member with a fixed angular relationship to each other and are free to turn as a unit in a magnetic field. Coil B tends to move the pointer counterclockwise and coil A, clockwise. The coils are mounted on a light, movable frame that is pivoted in jewel bearings and free to move about axis 0.

Coil A is connected in series with R3 and the unknown resistance, RX, to be measured. The series combination of coil A, R3, and RX is connected between the + and − brushes of the DC generator. Coil B is connected in series with R2, and this combination is also connected across the generator. There are no restraining springs on the movable member of the instrument portion of the megger. When the generator is not in operation, the pointer floats freely and may come to rest at any position on the scale.

If the terminals are open circuited, no current flows in coil A, and the current in coil B alone controls the movement of the moving element. Coil B takes a position opposite the gap in the core (since the core cannot move and coil B can), and the pointer indicates infinity on the scale. When a resistance is connected between the terminals, current flows in coil A, tending to move the pointer clockwise. At the same time, coil B tends to move the pointer counterclockwise. Therefore, the moving element, composed of both coils and the pointer, comes to rest at a position at which the two forces are balanced. This position depends upon the value of the external resistance, which controls the relative magnitude of current of coil A. Because changes in voltage affect both coils A and B in the same proportion, the position of the moving element is independent of the voltage. If the terminals are short circuited, the pointer rests at zero because the current in A is relatively large. The instrument is not damaged under these circumstances because the current is limited by R3.

There are two types of hand-driven meggers: the variable type and the constant pressure type. The speed of the variable pressure megger is dependent on how fast the hand crank 0 0 Ω ∞ 40% full-scale 45k Ω 50% full-scale 30k Ω Full-scale Simplified Ohmmeter Scale Meter movement [+]

− Open Adjuster 0∞ Meter movement [+]

− Shorted Adjuster Internal battery 0∞ Meter movement [+]

− Test probes 0∞ Meter movement [+]

− External resistor Current Internal battery Internal battery Basic voltmeter Basic voltmeter 0∞ is turned. The constant pressure megger uses a centrifugal governor, or slip clutch. The governor becomes effective only when the megger is operated at a speed above its slip speed, at which speed its voltage remains constant.

## 2. 中文翻译

用于电流表和电压表的表头机构，也可以用于欧姆表。欧姆表的功能是测量电阻。图中示出了一个简化的单级欧姆表，它表明基本欧姆表包含一个电池和一个与表头机构串联的可变电阻。要测量电阻时，把仪表的两根表笔跨接在被测的外部电阻两端。这样做就使欧姆表电路接通。这一连接使内部电池产生通过表头线圈的电流，使指针产生与被测外部电阻值成正比的偏转。

当欧姆表的表笔断开时，仪表处于满刻度偏转，表示无穷大（∞）电阻或开路。当表笔短接时（如图中标有「zero adjust」（调零）所示），指针位于最右端位置，表示短路或零电阻。该图中可变电阻的作用是调节电流，使表笔短接时指针恰好指在零位。这是用来补偿内部电池电压因老化而发生的变化。

图中示出了一种典型的模拟欧姆表刻度。在零与无穷大（∞）之间，刻度上标有各种电阻值。由于数值从左到右递减，这种刻度常称为反向刻度。

就所给例子而言，假设某欧姆表使用 50 μA、1,000 Ω 的表头机构，并有一只内部 1.5 伏电池。当表笔短接时，50 μA 的电流产生满刻度偏转。要得到 50 μA，欧姆表的总电阻为 1.5 V/50 μA = 30k Ω。因此，由于线圈电阻为 1k Ω，可变调零电阻必须调到 30k Ω – 1k Ω = 29k Ω。

现在考虑把一个 120k Ω 的电阻接到欧姆表的表笔上。它与 30k Ω 的内部电阻合计，总电阻 R 为 150k Ω。电流为 1.5 V/150k Ω = 10 μA，即满刻度电流的 20%，在图中所示的刻度上读取。

再进一步考虑把一个 120k Ω 的电阻接到欧姆表的表笔上。这产生 1.5 V/75k Ω = 10 μA 的电流，为满刻度电流的 40%，并标在刻度上。按此方式作更多计算可以看出，该刻度是非线性的。它在左侧比右侧压缩得更紧。刻度中心点对应于 30k Ω 的内部仪表电阻。原因如下：

（原文此处为图注碎片，原文无正文）

把 30k Ω 接到表笔上时，电流为 1.5 V/60k Ω = 25 μA，即 50 μA 满刻度电流的一半。

### 多量程欧姆表

实用的欧姆表有几个工作量程。这些量程通常用 R × 1、R × 10、R × 100、R × 1k、R × 100k 和 R × 1M 表示。这些量程选择的解读方式与电流表或电压表不同。欧姆表刻度上的读数要乘以量程选择所指示的倍数。例如，如果指针指在刻度上，而量程开关置于 R × 100，则实际测得的电阻为 20 × 100，即 2k Ω。

要测量小电阻值，技术人员必须使用比测量大电阻值时更大的欧姆表电流。为在欧姆表上提供多个量程、以测量从极小到极大的各种电阻值，需要使用分流电阻。每个量程都切换接入不同阻值的分流电阻。欧姆量程越高，分流电阻越大，并且在任何所选量程上它总是等于刻度中心读数。有些仪表在最高欧姆量程使用更高的电池电压。

### 兆欧表（高阻表）

兆欧表（megohmmeter）是一种带手摇发电机的高量程欧姆表。它用于测量绝缘电阻和其他高电阻值。它也用于电力系统的接地、导通性和短路测试。与普通欧姆表相比，兆欧表的主要优点在于它能用高电位（或称「击穿」电压）来测量电阻。这种测试可确保绝缘材料或电介质在电位电应力下不会短路或漏电。

兆欧表由两个主要部分组成，二者都由同一块永久磁铁分别提供各自的磁场：一个是手摇直流发电机 G，为进行测量提供必要的电流；另一个是仪表部分，用于指示所测电阻的值。仪表部分属于对置线圈式。线圈 A 和线圈 B 安装在可动部件上，彼此成固定角度关系，并可作为一个整体在磁场中自由转动。线圈 B 倾向于使指针逆时针转动，线圈 A 则使其顺时针转动。线圈装在一个轻质可动框架上，框架支承在宝石轴承中，可绕轴 0 自由转动。

线圈 A 与 R3 以及待测的未知电阻 RX 串联。线圈 A、R3 和 RX 的串联组合接在直流发电机的 + 与 − 电刷之间。线圈 B 与 R2 串联，这一组合也接在发电机两端。兆欧表仪表部分的可动部件上没有游丝（复位弹簧）。当发电机不运转时，指针自由浮动，可能停在刻度上的任意位置。

如果端子开路，线圈 A 中没有电流，仅由线圈 B 中的电流控制可动元件的运动。线圈 B 会停在与铁芯缺口相对的位置（因为铁芯不能动而线圈 B 能动），指针便在刻度上指示无穷大。当端子之间接上电阻时，电流流过线圈 A，倾向于使指针顺时针转动。同时，线圈 B 倾向于使指针逆时针转动。因此，由两个线圈和指针组成的可动元件停在两个力相平衡的位置上。这一位置取决于外部电阻的值，而外部电阻控制着线圈 A 电流的相对大小。由于电压变化按相同比例影响线圈 A 和 B，可动元件的位置与电压无关。如果端子短路，由于 A 中电流相对较大，指针停在零位。在这种情况下仪表不会损坏，因为电流受 R3 限制。

手摇兆欧表有两种类型：可变压力型和恒压型。可变压力式兆欧表的速度取决于手摇曲柄

（原文此处为图注碎片，原文无正文）

（原文此处为图注碎片，原文无正文）

（原文此处为图注碎片，原文无正文）

转动的快慢。恒压式兆欧表使用离心调速器或滑动离合器。调速器只有在兆欧表以高于其滑动速度的转速运行时才起作用，在该转速下其电压保持恒定。

## 3. 专业词汇

| 英文 | 词性 | 中文 | 本节语境 |
| --- | --- | --- | --- |
| ohmmeter | n. | 欧姆表 | 自带电池、用于测量电阻的仪表，表笔接被测电阻即成回路 |
| megohmmeter (megger) | n. | 兆欧表（高阻表） | 带手摇直流发电机的高量程欧姆表，用于测绝缘电阻 |
| infinite resistance | n.phr. | 无穷大电阻 | 表笔断开时欧姆表满刻度所指，代表开路 |
| short circuit | n.phr. | 短路 | 表笔短接时指针指零位所表示的状态 |
| zero adjust | n.phr. | 调零 | 可变电阻的调节作用，使表笔短接时指针恰在零位 |
| back-off scale | n.phr. | 反向刻度 | 数值从左向右递减的欧姆表刻度 |
| nonlinear | adj. | 非线性的 | 欧姆表刻度左密右疏、读数不均等的特性 |
| multirange | adj. | 多量程的 | 具有 R × 1、R × 10、R × 100k 等多个倍率档位 |
| insulation resistance | n.phr. | 绝缘电阻 | 兆欧表以高电位测量的高阻值，反映绝缘是否漏电 |
| opposed coil | n.phr. | 对置线圈 | 兆欧表仪表部分的结构，两线圈力矩相反、平衡时读数 |
| jewel bearing | n.phr. | 宝石轴承 | 支承兆欧表可动框架的轴承，摩擦力极小 |
| centrifugal governor | n.phr. | 离心调速器 | 恒压式兆欧表中使转速与电压保持恒定的装置 |

## 4. 语法解析

### ① allow sb/sth to do + 现在分词作结果状语 + being measured
**原句**：This connection allows the internal battery to produce a current through the movement coil, causing a deflection of the pointer proportional to the value of the external resistance being measured.
**拆解**：主句 This connection allows the internal battery to produce a current；through the movement coil 为后置定语修饰 current；causing a deflection… 为现在分词短语作结果状语；proportional to the value of the external resistance 为形容词短语作后置定语修饰 deflection；being measured 为现在分词被动式作后置定语修饰 the resistance。
**要点**：allow + 宾语 + to do 是固定搭配，不能省略 to；分词作结果状语时逻辑主语是前面整句的动作；being measured 表示「正在被测的」，区别于 to be measured（待测）。

### ② When 引导的被动时间从句 + 分词状语 + 倒装的原因插入
**原句**：When the leads are shorted as shown in figure “zero adjust,” the pointer is at the full right-hand position, indicating a short circuit or zero resistance.
**拆解**：When 引导时间状语从句，从句为被动 are shorted，as shown in figure “zero adjust,” 为方式状语；主句 the pointer is at the full right-hand position；indicating a short circuit or zero resistance 为现在分词短语作伴随状语。
**要点**：as shown 是「如……所示」的省略式，完整为 as it is shown；indicate 在此表示「指示、表示某一状态」，常用于仪表读数；the full right-hand position 中 right-hand 为复合形容词，作定语时用连字符。

### ③ so that 目的状语从句 + 被动时间从句
**原句**：The purpose of the variable resistor in this figure is to adjust the current so that the pointer is at exactly zero when the leads are shorted.
**拆解**：主语 The purpose of the variable resistor in this figure，谓语 is，表语 to adjust the current；so that 引导目的状语从句，从句主语 the pointer，谓语 is，表语 at exactly zero；when 引导时间状语从句，为被动 are shorted。
**要点**：so that 表目的时从句常含 can/could/may 或直接用一般现在时表功能；the purpose of…is to do 是定义器件作用的常用句型；exactly 修饰 at zero 而非动词，位置在介词短语前。

### ④ advantage over 比较结构 + its capacity to do
**原句**：The chief advantage of the megger over an ohmmeter is its capacity to measure resistance with a high potential, or “breakdown” voltage.
**拆解**：主语 The chief advantage of the megger over an ohmmeter，其中 of 引出所属、over 引出比较对象；谓语 is，表语 its capacity to measure resistance with a high potential；or “breakdown” voltage 为同位语补充说明 a high potential。
**要点**：advantage over 表示「相对于……的优势」，不可写成 advantage than；capacity to do 意为「做……的能力」，与 ability to do 同构；with + 名词表示所用手段。

### ⑤ Because 原因状语从句 + be independent of
**原句**：Because changes in voltage affect both coils A and B in the same proportion, the position of the moving element is independent of the voltage.
**拆解**：Because 引导原因状语从句，主语 changes in voltage，谓语 affect，宾语 both coils A and B，in the same proportion 为方式状语；主句主语 the position of the moving element，谓语 is，表语 independent of the voltage。
**要点**：be independent of 意为「不受……影响」，介词固定用 of，不能换成 from；both…and 连接的两项在句中作并列宾语；in the same proportion 是「按同一比例」的固定表达。
