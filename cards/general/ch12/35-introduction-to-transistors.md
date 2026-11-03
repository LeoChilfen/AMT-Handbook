# Introduction to Transistors

> 通用 Ch 12 · Introduction to Transistors · 原文 PDF 第 547 页

## 1. 原文

The transistor is a three-terminal device primarily used to amplify signals and control current within a circuit. [Figure 12-220] The basic two-junction semiconductor must have one type of region sandwiched between two of the other type. The three regions in a transistor are the collector (C), which is moderately doped, the emitter (E), which is heavily doped, and the base (B), which is significantly less doped. The alternating layers of semiconductor material type provide the common commercial name for each type of transistor. The interface between the layers is called a junction. Selenium and germanium diodes previously discussed are examples of junction diodes. Note that the sandwiched layer or base is significantly thinner than the collector or the emitter. In general, this permits a “punching through” action for the carriers passing between the collector and emitter terminals.

The transistors are classified as either NPN or PNP according to the arrangement of their N and P-materials. The NPN transistor is formed by introducing a thin region of P-material between two regions of N-type material. The opposite is true for the PNP configuration.

The two basic types of transistors along with their circuit Approx. 0.75"

Schematic symbol General purpose signal diodes Approx. 0.1"

(+) Anode Cathode (−)

(+) Anode Cathode (−)

Cathode (−)(+) Anode Approx. 0.2"

Rectifier diodes 35 ampere silicon rectifier Copper Lead Insulating washer Insulating tube Pressure plate Copper oxide Direction of circuit flow symbols are shown in Figure 12-221 . Note that the two symbols are different. The horizontal line represents the base, and two angular lines represent the emitter and collector. The angular line with the arrow on it is the emitter, while the line without is the collector. The direction of the arrow on the emitter determines whether or not the transistor is a PNP or an NPN type. If the arrow is pointing in, the transistor is a PNP. On the other hand, if the arrow is pointing out, then it is an NPN type.

### Transistor Theory

As discussed in the section on diodes, the movement of the electrons and holes can be considered current. Electron current moves in one direction, while hole current travels in the opposite direction. In transistors, both electrons and holes act as carriers of current.

A forward biased PN junction is comparable to a low- resistance circuit element, because it passes a high current for a given voltage. On the other hand, a reverse-biased PN junction is comparable to a high-resistance circuit element. By using Ohm’s Law formula for power (P = I 2R) and assuming current is held constant through both junctions, it can be concluded that the power developed across the high resistance junction is greater than that developed across a low resistance junction. Therefore, if a crystal were to contain two PN junctions, one forward biased and the other reverse biased, and a low-power signal injected into the forward biased junction, a high-power signal could be produced at the reverse-biased junction.

To use the transistor as an amplifier, some sort of external bias voltage must modify each of the junctions. The first PN junction (emitter-base) is biased in the forward direction. This produces a low resistance. The second junction, which is the collector-base junction, is reverse biased to produce a high resistance. [Figure 12-222]

Schottky diode Step-recovery diode Zener LED Photodiode Varactor With the emitter-base junction biased in the forward direction, electrons leave the negative terminal of the battery and enter the N-material. These electrons pass easily through the emitter, cross over the junction, and combine with the hole in the P-material in the base. For each electron that fills a hole in the P-material, another electron leaves the P-material, which creates a new hole and enters the positive terminal of the battery.

The second PN junction, which is the base-collector junction, is reverse biased. This prevents the majority carriers from crossing the junction, thus creating a high-resistance circuit. It is worth noting that there still is a small current passing through the reversed PN junction in the form of minority carriers—that is, electrons in the P-material and holes in the N-material. The minority carriers play a significant part in the operation of the NPN transistor.

Figure 12-223 illustrates the basic interaction of the NPN junction. There are two batteries in the circuit used to bias the NPN transistor. Vbb is considered the base voltage supply, rated in this illustration at 1 volt, and the battery voltage Vcc, rated at 6 volts, is called the collector voltage supply.

Current within the external circuit is simply the movement of free electrons originating at the negative terminal of the battery and flowing to the N-material. [Figure 12-223] As the electrons enter the N-material, they become the majority carrier and move through the N-material to the emitter-base PN junction. This emitter-base junction is forward biased at about 0.65 to 0.7 volts positive with respect to the emitter and presents no resistance to the flow of electrons from the emitter into the base, which is composed of P-material. As these electrons move into the base, they drop into available holes. For every electron that drops into a hole, another electron exits the base by way of the base lead and becomes the base current or Ib. Of course, when one electron leaves the base, a new hole is formed. From the standpoint of the collector, these electrons that drop into holes are lost and of no use. To reduce this loss of electrons, the transistor is designed so that the base is very thin in relation to the emitter and collector, and the base is lightly doped.

Most of the electrons that move into the base fall under the influence of the reverse bias of the collector. While collector- base junction is reverse biased with respect to the majority carriers, it behaves as if it is forward biased to the electrons or minority carriers in this case. The electrons are accelerated through the collector-base junction and into the collector. The collector is comprised of the N-type material; therefore, the electrons once again become the majority carrier. Moving easily through the collector, the electrons return to the positive terminal of the collector supply battery Vcc, which is shown in Figure 12-223 as Ic.

Because of the way this device operates to transfer current (and its internal resistances) from the original conduction path to another, its name is a combination of the words “transfer” and “resistor”—transistor.

### PNP Transistor Operation

The PNP transistor generally works the same way as the NPN transistor. The primary difference is that the emitter, base, and collector materials are made of different material than the NPN. The majority and minority current carriers are the opposite in the PNP to that of the NPN. In the case of the PNP, the majority carriers are the holes instead of the electrons in the NPN transistor. To properly bias the PNP, the polarity of the bias network must be reversed.

### Identification of Transistors

Figure 12-224 illustrates some of the more common transistor lead identifications. The methods of identifying leads vary due to a lack of a standard and require verification using manufacturer information to properly identify. However, a short description of the common methods is discussed below.

Figure 12-224D shows an oval-shaped transistor. The collector lead in this case is identified by the wide space between it and the lead for the base. The final lead at the far left is the emitter. In many cases, colored dots indicate the collector lead, and short leads relative to the other leads indicate the emitter. In a conventional power diode, as seen in Figure 12-224E, the collector lead is usually a part of the mounting bases, while the emitter and collector are leads or tines protruding from the mounting surface.

### Field Effect Transistors

Another transistor design that has become more important than the bipolar transistor is the field-effect transistor (FET). The primary difference between the bipolar transistor and the FET is that the bipolar transistor has two PN junctions and P N PEmitter Collector Base PN junctions N P NEmitter Collector Base PN junctions P N P Emitter Collector Base N P N Base Emitter Collector Base BaseFigure 12-220. Transistor.

is a current-controlled device, while the FET has only one PN junction and is a voltage-controlled device. Within the FET family, there are two general categories of components. One category is called the junction FET (JFET), which has only one PN junction. The other category is known as the enhancement-type or metal-oxide JET (MOSFET).

Figure 12-225 shows the basic construction of the JFET and the schematic symbol. In this figure, it can be seen that the drain (D) and source (S) are connected to an N-type material, and the gate (G) is connected to the P-type material. With gate voltage Vgg set to 0 volts and drain voltage Vdd set to some positive voltage, a current flows between the source and the drain, through a narrow band of N-material. If then, Vgg is adjusted to some negative voltage, the PN junction is reverse biased, and a depletion zone (no charge carriers) is established at the PN junction. By reducing the region of noncarriers, it has the effect of reducing the dimensions of the N-channel, resulting in a reduction of source to drain current.

Because JFETs are voltage-controlled devices, they have some advantages over the bipolar transistor. One such advantage is that because the gate is reverse biased, the circuit that it is connected to sees the gate as a very high resistance. This means that the JFET has less of an insertion influence in the circuit. The high resistance also means that less current is used.

Like many other solid-state devices, careless handling and static electricity can damage the JFET. Technicians should take all precautions to prevent such damage.

### Metal-Oxide-Semiconductor FET (MOSFET)

) Figure 12-226 illustrates the general construction and the schematic symbol of the MOSFET transistor. The biasing arrangement for the MOSFET is essentially the same as that for the JFET. The term “enhancement” comes from the idea that when there is no bias voltage applied to the gate (G), then there is no channel for current conduction between the source (S) and the drain (D). By applying a greater voltage on the gate (G), the P-channel begins to materialize and grow in size. Once this occurs, the source (S) to drain (D) current Id increases. The schematic symbol reflects this characteristic by using a broken line to indicate that the channel does not exist without a gate bias.

### Common Transistor Configurations

A transistor may be connected in one of three different configurations: common-emitter (CE), common-base (CB), and common-collector (CC). The term “common” is used to indicate which element of the transistor is common to both the input and the output. Each configuration has its own characteristics, which makes each configuration suitable for particular applications. A way to determine what configuration you may find in a circuit is to first determine which of the three transistor elements is used for the input signal. Then, determine the element used for the output signal. At that point, the remaining element, (base, emitter, or collector) is the common element to both the input and output, and thus you determine the configuration.

#### Common-Emitter (CE) Configuration

This is the configuration most commonly used in amplifier + − + − Emitter Vcc = 6 volts CollectorReverse biased junction Hole [blue]

lb Vbb = 1 volt Forward biased junction le lc N P N Base + − + − circuits because they provide good gains for voltage, current, and power. The input signal is applied to the base-emitter junction, which is forward biased (low resistance), and the output signal is taken off the collector-emitter junction, which is reverse biased (high resistance). Then the emitter is the common element to both input and output circuits. [Figure 12-227]

When the transistor is connected in a CE configuration, the input signal is injected between the base and emitter, which is a low-resistance, low-current circuit. As the input signal goes positive, it causes the base to go positive relative to the emitter. This causes a decrease in the forward bias, which in turn reduces the collector current IC and increases the collector voltage (EC being more negative). During the negative portion of the input signal, the voltage on the base is driven more negative relative to the emitter. This increases the forward bias and allows an increase in collector current IC and a decrease in collector voltage (EC being less negative and going positive). The collector current, which flows through the reverse-biased junction, also flows through a high-resistance load resulting in a high level of amplification.

Because the input signal to the CE goes positive when the output goes negative, the two signals are 180° out of phase. This is the only configuration that provides a phase reversal. The CE is the most popular of the three configurations because it has the best combination of current and voltage gain. Gain is a term used to indicate the magnitude of amplification. Each transistor configuration has its unique gain characteristics even though the same transistors are used.

#### Common-Collector (CC) Configuration

This transistor configuration is usually used for impedance matching. It is also used as a current driver due to its high current gain. It is also very useful in switching circuits since it has the ability to pass signals in either direction. [Figure 12-227]

In the CC circuit, the input signal is applied to the base, and the output signal is taken from the emitter, leaving the collector as the common point between the input and the output. The input resistance of the CC circuit is high, while the output resistance is low. The current gain is higher than that in the CE, but it has a lower power gain than either the CE or CB configuration. Just like the CB configuration, the output signal of the CC circuit is in phase with the input signal. The CC is typically referred to as an emitter-follower because the output developed on the emitter follows the input signal applied to the base.

#### Common-Base (CB) Configuration

The primary use of this configuration is for impedance matching because it has low input impedance and high output resistance. Two factors, however, limit the usefulness of this circuit application. First is the low-input resistance and second is its lack of current, which is always below 1. Since the CB configuration gives voltage amplification, there are some applications for this circuit, such as microphone amplifiers. [Figure 12-227]

In the CB circuit, the input signal is applied to the emitter and the output signal is taken from the collector. In this case, both the input and the output have the base as a common element. When an input signal is applied to the emitter, it causes the emitter-base junction to react in the same manner as that in the CE circuit. When an input adds to the bias, it increases the transistor current; conversely, when the signal opposes the bias, the current in the transistor decreases.

The signal adds to the forward bias, since it is applied to the emitter, causing the collector current to increase. This increase in I C results in a greater voltage drop across the + Gate (G)

ID IS VGG VDD Source (S)

N-material P-material Charge free or depletion zone P-channelN-channel JFET symbol JFET construction Drain (D) Source (S)

− + − + + − Color dot Color dot E E E BB C C B C E B C A B C D E E B load resistor RL, thus lowering the collector voltage E C. The collector voltage, in becoming less negative, swings in a positive direction and is therefore in phase with the incoming positive signal.

## 2. 中文翻译

<!-- TODO: 逐段翻译，段数与上面严格一一对应（48 段）。专业术语按行业惯例，数字与缩写保留。 -->

## 3. 专业词汇

<!-- TODO: 用表格 | 英文 | 词性 | 中文 | 本节语境 |，4~8 行。优先选下面 Glossary 里的词（本节原文出现过的）：
- Ampere —— A unit of measure of the rate of electron flow or current in an electrical conductor. One ampere of current represents one coulomb of electrical charge (6.24 × 
- Conduction —— The transfer of heat which requires physical contact between an object that has a large amount of heat energy and one that has a smaller amount of heat energy.
- Current —— The flow of electrical charge.
- Difference —— The answer to a subtraction problem.
- Ohm’s Law —— Explains the relationship between voltage, current, and resistance in an electrical circuit, and states that current flow in an electrical circuit is directly p
- Power (exponent) —— A shorthand method of indicating how many times a number, called the base, is multiplied by itself. For example, in the number 43, 3 is the power, or exponent, 
- Power —— Power is the time rate at which work is done or energy is transferred.
- Pressure —— The amount of force acting on a specific amount of surface area, typically measured in pounds per square inch or psi.
-->

## 4. 语法解析

<!-- TODO: 2~4 个语法点，格式：
### ① 语法点名称
**原句**：<必须逐字来自第 1 节原文>
**拆解**：主/谓/宾、从句、非谓语等成分分析
**要点**：为什么这样用、易错点、可迁移的搭配
-->
