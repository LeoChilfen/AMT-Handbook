# The Ohmmeter

> 通用 Ch 12 · The Ohmmeter · 原文 PDF 第 513 页

## 1. 原文

The meter movement used for the ammeter and the voltmeter can also be used for the ohmmeter. The function of the ohmmeter is to measure resistance. A simplified one-stage ohmmeter is illustrated in Figure 12-154, which shows that the basic ohmmeter contains a battery and a variable resistor in series with the meter movement. To measure resistance, the leads of the meter are connected across an external resistance, which is to be measured. By doing this, the ohmmeter circuit is completed. This connection allows the internal battery to produce a current through the movement coil, causing a deflection of the pointer proportional to the value of the external resistance being measured.

When the ohmmeter leads are open, the meter is at a full-scale deflection, indicating an infinite (∞) resistance or an open circuit. [Figure 12-155] When the leads are shorted as shown in figure “zero adjust,” the pointer is at the full right-hand position, indicating a short circuit or zero resistance. The purpose of the variable resistor in this figure is to adjust the current so that the pointer is at exactly zero when the leads are shorted. This is used to compensate for changes in the internal battery voltage due to aging.

Figure 12-156 shows a typical analog ohmmeter scale. Between zero and infinity (∞), the scale is marked to indicate various resistor values. Because the values decrease from left to right, this scale is often called a back-off scale.

In the case of the example given, assume that a certain ohmmeter uses a 50 μA, 1,000 Ω meter movement and has an internal 1.5 volt battery. A current of 50 μA produces a full-scale deflection when the test leads are shorted. To have 50 μA, the total ohmmeter resistance is 1.5 V/50 μA = 30k Ω. Therefore, since the coil resistance is 1k Ω, the variable zero adjustment resistor must be set to 30k Ω – 1k Ω = 29k Ω.

Now consider that a 120k Ω resistor is connected to the ohmmeter leads. Combined with the 30k Ω internal resistance, the total R is 150k Ω. The current is 1.5 V/150k Ω = 10 μA, which is 20 percent of the full-scale current and appears on the scale shown in Figure 12-156.

Now consider further that a 120k Ω resistor is connected to the ohmmeter leads. This results in a current of 1.5 V/75k Ω = 10 μA, which is 40 percent of the full-scale current and marked on the scale. Additional calculations of this type show that the scale is nonlinear. It is more compressed toward the left side than the right side. The center scale point corresponds to the internal meter resistance of 30k Ω. The reason is as follows:

10 V 1 V RM2 180k Ω 19k Ω RM1 0∞ Basic voltmeter 50A, 1k ohm movement [+] [−]

RM With 30k Ω connected to the leads, the current is 1.5 V/60k Ω = 25 μA, which is half of the full-scale current of 50 μA.

### The Multirange Ohmmeter

A practical ohmmeter has several operational ranges. These typically are indicated by R × 1, R × 10, R × 100, R × 1k, R × 100k and R × 1M. These range selections are interpreted in a different manner than that of an ammeter or voltmeter. The reading on the ohmmeter scale is multiplied by the factor indicated by the range setting. For example, if the pointer is set on the scale and the range switch is set at R × 100, the actual resistance measurement is 20 × 100 or 2k Ω.

To measure small resistance values, the technician must use a higher ohmmeter current than is needed for measuring large resistance values. Shunt resistors are needed to provide multiple ranges on the ohmmeter to measure a range of resistance values from the very small to very large. For each range, a different value of shunt resistance is switched in. The shunt resistance increases for higher ohm ranges and is always equal to the center scale reading on any selected range. In some meters, a higher battery voltage is used for the highest ohm range. [Figure 12-157]

### Megger (Megohmmeter)

The megger, or megohmmeter, is a high range ohmmeter containing a hand-operated generator. It is used to measure insulation resistance and other high-resistance values. It is also used for ground, continuity, and short-circuit testing of electrical power systems. The chief advantage of the megger over an ohmmeter is its capacity to measure resistance with a high potential, or “breakdown” voltage. This type of testing ensures that insulation or a dielectric material will not short or leak under potential electrical stress.

The megger consists of two primary elements, both of which are provided with individual magnetic fields from a common permanent magnet: a hand-driven DC generator, G, which supplies the necessary current for making the measurement; and the instrument portion, which indicates the value of the resistance being measured. The instrument portion is of the opposed coil type. Coils A and B are mounted on the movable member with a fixed angular relationship to each other and are free to turn as a unit in a magnetic field. Coil B tends to move the pointer counterclockwise and coil A, clockwise. The coils are mounted on a light, movable frame that is pivoted in jewel bearings and free to move about axis 0. [Figure 12-158]

Coil A is connected in series with R3 and the unknown resistance, RX, to be measured. The series combination of coil A, R3, and RX is connected between the + and − brushes of the DC generator. Coil B is connected in series with R2, and this combination is also connected across the generator. There are no restraining springs on the movable member of the instrument portion of the megger. When the generator is not in operation, the pointer floats freely and may come to rest at any position on the scale.

If the terminals are open circuited, no current flows in coil A, and the current in coil B alone controls the movement of the moving element. Coil B takes a position opposite the gap in the core (since the core cannot move and coil B can), and the pointer indicates infinity on the scale. When a resistance is connected between the terminals, current flows in coil A, tending to move the pointer clockwise. At the same time, coil B tends to move the pointer counterclockwise. Therefore, the moving element, composed of both coils and the pointer, comes to rest at a position at which the two forces are balanced. This position depends upon the value of the external resistance, which controls the relative magnitude of current of coil A. Because changes in voltage affect both coils A and B in the same proportion, the position of the moving element is independent of the voltage. If the terminals are short circuited, the pointer rests at zero because the current in A is relatively large. The instrument is not damaged under these circumstances because the current is limited by R3.

There are two types of hand-driven meggers: the variable type and the constant pressure type. The speed of the variable pressure megger is dependent on how fast the hand crank 0 0 Ω ∞ 40% full-scale 45k Ω 50% full-scale 30k Ω Full-scale Simplified Ohmmeter Scale Meter movement [+]

− Open Adjuster 0∞ Meter movement [+]

− Shorted Adjuster Internal battery 0∞ Meter movement [+]

− Test probes 0∞ Meter movement [+]

− External resistor Current Internal battery Internal battery Basic voltmeter Basic voltmeter 0∞ is turned. The constant pressure megger uses a centrifugal governor, or slip clutch. The governor becomes effective only when the megger is operated at a speed above its slip speed, at which speed its voltage remains constant.

## 2. 中文翻译

<!-- TODO: 逐段翻译，段数与上面严格一一对应（21 段）。专业术语按行业惯例，数字与缩写保留。 -->

## 3. 专业词汇

<!-- TODO: 用表格 | 英文 | 词性 | 中文 | 本节语境 |，4~8 行。优先选下面 Glossary 里的词（本节原文出现过的）：
- Ammeter —— An instrument for measuring electric current in amperes.
- Current —— The flow of electrical charge.
- Ohmmeter —— A current measuring instrument that provides its own source (self-excited) of power.
- Power (exponent) —— A shorthand method of indicating how many times a number, called the base, is multiplied by itself. For example, in the number 43, 3 is the power, or exponent, 
- Power —— Power is the time rate at which work is done or energy is transferred.
- Pressure —— The amount of force acting on a specific amount of surface area, typically measured in pounds per square inch or psi.
- Proportion —— A proportion is a statement of equality between two or more ratios. The example of A is to B as C is to D can be represented A:B = C:D or A/B = C/D.
- Resistance —— The opposition a device or material offers to the flow or current.
-->

## 4. 语法解析

<!-- TODO: 2~4 个语法点，格式：
### ① 语法点名称
**原句**：<必须逐字来自第 1 节原文>
**拆解**：主/谓/宾、从句、非谓语等成分分析
**要点**：为什么这样用、易错点、可迁移的搭配
-->
