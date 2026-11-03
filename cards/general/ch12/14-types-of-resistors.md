# Types of Resistors

> 通用 Ch 12 · Types of Resistors · 原文 PDF 第 466 页

## 1. 原文

Fixed resistors have built into the design a means of opposing current. [Figure 12-48] The general use of a resistor in a circuit is to limit the amount of current flow. There are a number of methods used in construction and sizing of a resistor that control properties, such as resistance value, the precision of the resistance value, and the ability to dissipate heat. While in some applications the purpose of the resistive element is used to generate heat, such as in propeller anti-ice boots, heat typically is the unwanted loss of energy.

### Carbon Composition

The carbon composed resistor is constructed from a mixture of finely grouped carbon/graphite, an insulation material for filler, and a substance for binding the material together. The amount of graphite in relation to the insulation material determines the ohmic or resistive value of the resistor. This mixture is compressed into a rod, which is fitted with axial leads or “pigtails.” The finished product is sealed in an insulating coating for isolation and physical protection.

There are other types of fixed resistors in common use. Included in this group are:

• Metal glaze The construction of a film resistor is accomplished by depositing a resistive material evenly on a ceramic rod. This resistive material can be graphite for the carbon film resistor, nickel chromium for the metal film resistor, metal and glass for the metal glaze resistor, and metal and an insulating oxide for the metal-oxide resistor.

### Resistor Ratings

It is very difficult to manufacture a resistor to an exact standard of ohmic values. Fortunately, most circuit requirements are not extremely critical. For many uses, the actual resistance in ohms can be 20 percent higher or lower than the value marked on the resistor without causing difficulty. The percentage variation between the marked value and the actual value of a resistor is known as the “tolerance” of a resistor. A resistor coded for a 5 percent tolerance is not more than 5 percent higher or lower than the value indicated by the color code.

The resistor color code is made up of a group of colors, numbers, and tolerance values. Each color is represented by a number, and in most cases, by a tolerance value. [Figure 12-49]

When the color code is used with the end-to-center band marking system, the resistor is normally marked with bands of color at one end of the resistor. The body or base color of the resistor has nothing to do with the color code, and in no way indicates a resistance value. To prevent confusion, this body is never the same color as any of the bands indicating resistance value.

Resistor color code Color Number Tolerance Black 0 — Brown 1 1% Red 2 2% Orange 3 3% Yellow 4 4% Green 5 5% Blue 6 6% Violet 7 7% Gray 8 8% White 9 9% Gold — 5% Silver — 10% No color — 20%

### Color Band Decoding

When the end-to-center band marking system is used, either three or four bands mark the resistor.

1. The first color band (nearest the end of the resistor) indicates the first digit in the numerical resistance value. This band is never gold or silver in color.

2. The second color band always indicates the second digit of ohmic value. It is never gold or silver in color. [Figure 12-50]

3. The third color band indicates the number of zeros to be added to the two digits derived from the first and second bands, except in the following two cases:

(a) If the third band is gold in color, the first two digits must be multiplied by 10 percent.

(b) If the third band is silver in color, the first two digits must be multiplied by 1 percent.

4. If there is a fourth color band, it is used as a multiplier for percentage of tolerance, as indicated in the color code chart in Figure 12-49. If there is no fourth band, the tolerance is understood to be 20 percent.

Figure 12-50 illustrates the rules for reading the resistance value of a resistor marked with the end-to-center band system. This resistor is marked with three bands of color, which must be read from the end toward the center.

There is no fourth color band; therefore, the tolerance is understood to be 20 percent. 20 percent of 250,000 Ω, equals 50,000 Ω.

Since the 20 percent tolerance is plus or minus, Maximum resistance = 250,000 Ω + 50,000 Ω = 300,000 Ω Minimum resistance = 250,000 Ω − 50,000 Ω = 200,000 Ω The following paragraphs provide a few extra examples of resistor color band decoding. Figure 12-51 contains a resistor with another set of colors. This resistor code should be read as follows:

The resistance of this resistor is 86,000 ±10 percent ohms. The maximum resistance is 94,600 ohms, and the minimum resistance is 77,400 ohms.

Another example is the resistance of the resistor in Figure 12-52 is 960 ±5 percent ohms. The maximum resistance is 1,008 ohms, and the minimum resistance is 912 ohms. Sometimes circuit considerations dictate that the tolerance must be smaller than 20 percent. Figure 12-53 shows an example of a resistor with a 2 percent tolerance. The resistance value of this resistor is 2,500 ±2 percent ohms. The maximum resistance is 2,550 ohms, and the minimum resistance is 2,450 ohms.

Figure 12-54 contains an example of a resistor with a black third color band. The color code value of black is zero, and the third band indicates the number of zeros to be added to the first two digits.

In this case, a zero number of zeros must be added to the first two digits; therefore, no zeros are added. Thus, the resistance value is 10 ±1 percent ohms. The maximum resistance is 10.1 ohms, and the minimum resistance is 9.9 ohms. There are two exceptions to the rule stating the third color band indicates the number of zeros. The first of these exceptions is illustrated in Figure 12-55. When the third band is gold in color, it indicates that the first two digits must be multiplied by 10 percent. The value of this resistor in this case is:

10 × 0.10 ±2% = 1 = 0.02 ohms When the third band is silver, as is the case in Figure 12-56, the first two digits must be multiplied by 1 percent. The value Gray Blue Orange Silver 8 6 000 10% White Blue Brown Gold 9 6 0 5% Red Green Red Red 2 5 00 2% Brown Black Black Brown 1 0 1% 1st Band 2nd Band 3rd Band Red Green Yellow Color Numerical Value Significance 1st band — red 2 1st digit 2nd band — green 5 2nd digit 3rd band — yellow 4 No. of zeroes to add Yellow Green Silver (Multiplier)

Silver 4 5 1% 10% Brown Black Gold (Multiplier)

Red 1 0 10% 2% of the resistor is 0.45 ±10 percent ohms.

Wire-wound resistors typically control large amounts of current and have high power ratings. Resistors of this type are constructed by winding a resistance wire around an insulating rod usually made of porcelain. The windings are coated with an insulation material for physical protection and heat conduction. Both ends of the windings are connected to terminals, which are used to connect the resistor to a circuit. [Figure 12-57]

A wire-wound resistor with tap is a special type of fixed resistor that can be adjusted. These adjustments can be made by moving a slide bar tap or by moving the tap to a preset incremental position. While the tap may be adjustable, the adjustments are usually set at the time of installation to a specific value and then operated in service as a fixed resistor. Another type of wire-wound resistor is constructed of Manganin wire, used when high precision is needed.

### Variable Resistors

Variable resistors are constructed so that the resistive value can be changed easily. This adjustment can be manual or automatic, and the adjustments can be made while the system that it is connected to is in operation. There are two basic types of manual adjustors: the rheostat and the potentiometer.

A rheostat is a variable resistor used to vary the amount of current flowing in a circuit. [Figure 12-58] Figure 12-59 shows a rheostat connected in series with an ordinary resistance in a series circuit. As the slider arm moves from point A to B, the amount of rheostat resistance (AB) is increased. Since the rheostat resistance and the fixed resistance are in series, the total resistance in the circuit also increases, and the current in the circuit decreases. On the other hand, if the slider arm is moved toward point A, the total resistance decreases and the current in the circuit increases.

The potentiometer is considered a three-terminal device. [Figure 12-60] As illustrated, terminals 1 and 2 have the entire value of the potentiometer resistance between them. Terminal 3 is the wiper or moving contact. Through this wiper, the resistance between terminals 1 and 3 or terminals 2 and 3 can be varied. While the rheostat is used to vary the current in a circuit, the potentiometer is used to vary the voltage in a circuit. A typical use for this component can be found in the volume controls on an audio panel and input devices for flight data recorders, among many other applications.

In Figure 12-61A, a potentiometer is used to obtain a variable voltage from a fixed voltage source to apply to an electrical load. The voltage applied to the load is the voltage between points 2 and 3. When the slider arm is moved to point 1, the entire voltage is applied to the electrical device (load); when the arm is moved to point 3, the voltage applied to the load is zero. The potentiometer makes possible the application of any voltage between zero and full voltage to the load.

The current flowing through the circuit of Figure 12-61 leaves the negative terminal electron flow of the battery and divides one part flowing through the lower portion of the potentiometer (points 3 to 2) and the other part through the load. Both parts combine at point 2 and flow through the upper portion of the potentiometer (points 2 to 1) back to the positive terminal of the battery. In View B of Figure 12-61, a potentiometer and its schematic symbol are shown.

In choosing a potentiometer resistance, the amount of current drawn by the load should be considered, as well as the current flow through the potentiometer at all settings of the slider arm. The energy of the current through the potentiometer is dissipated in the form of heat.

It is important to keep this wasted current as small as possible by making the resistance of the potentiometer as large as practicable. In most cases, the resistance of the potentiometer can be several times the resistance of the load. Figure 12-62 shows how a potentiometer can be wired to function as a rheostat.

Linear Potentiometers In a linear potentiometer, the resistance between both terminal and the wiper varies linearly with the position of the wiper. To illustrate, one quarter of a turn on the potentiometer results in one quarter of the total resistance. The same relationship exists when one-half or three-quarters of potentiometer movement. [Figure 12-63] Tapered Potentiometers Resistance varies in a nonlinear manner in the case of the tapered potentiometer. [Figure 12-64] Keep in mind that one-half of full potentiometer travel does not necessarily correspond to one-half the total resistance of the potentiometer.

The thermistor is a type of a variable resistor that is temperature sensitive. [Figure 12-65] This component has a negative temperature coefficient, which means that as the sensed temperature increases, the resistance of the thermistor decreases.

### Photoconductive Cells

The photoconductive cell is similar to the thermistor. Like the thermistor, it has a negative temperature coefficient. Unlike the thermistor, the resistance is controlled by light intensity. This kind of component can be found in radio control heads where the intensity of the ambient light is sensed through the photoconductive cell resulting in the backlighting of the control heads to adjust to the flight deck lighting conditions. [Figure 12-66]

## 2. 中文翻译

<!-- TODO: 逐段翻译，段数与上面严格一一对应（42 段）。专业术语按行业惯例，数字与缩写保留。 -->

## 3. 专业词汇

<!-- TODO: 用表格 | 英文 | 词性 | 中文 | 本节语境 |，4~8 行。优先选下面 Glossary 里的词（本节原文出现过的）：
- Conduction —— The transfer of heat which requires physical contact between an object that has a large amount of heat energy and one that has a smaller amount of heat energy.
- Current —— The flow of electrical charge.
- Energy —— The capacity of a physical system to perform work. There are two types of energy, kinetic and potential.
- Percentage —— Used to express a number as a fraction of 100. Using the percentage sign, %, 90 percent is expressed as 90%.
- Potentiometer —— A variable tapped resistor that can be used as a voltage divider.
- Power (exponent) —— A shorthand method of indicating how many times a number, called the base, is multiplied by itself. For example, in the number 43, 3 is the power, or exponent, 
- Power —— Power is the time rate at which work is done or energy is transferred.
- Product —— The result of multiplication.
-->

## 4. 语法解析

<!-- TODO: 2~4 个语法点，格式：
### ① 语法点名称
**原句**：<必须逐字来自第 1 节原文>
**拆解**：主/谓/宾、从句、非谓语等成分分析
**要点**：为什么这样用、易错点、可迁移的搭配
-->
