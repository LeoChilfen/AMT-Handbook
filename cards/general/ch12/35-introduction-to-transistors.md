# Introduction to Transistors

> 通用 Ch 12 · Introduction to Transistors · 原文 PDF 第 547 页

## 1. 原文

The transistor is a three-terminal device primarily used to amplify signals and control current within a circuit. The basic two-junction semiconductor must have one type of region sandwiched between two of the other type. The three regions in a transistor are the collector (C), which is moderately doped, the emitter (E), which is heavily doped, and the base (B), which is significantly less doped. The alternating layers of semiconductor material type provide the common commercial name for each type of transistor. The interface between the layers is called a junction. Selenium and germanium diodes previously discussed are examples of junction diodes. Note that the sandwiched layer or base is significantly thinner than the collector or the emitter. In general, this permits a “punching through” action for the carriers passing between the collector and emitter terminals.

The transistors are classified as either NPN or PNP according to the arrangement of their N and P-materials. The NPN transistor is formed by introducing a thin region of P-material between two regions of N-type material. The opposite is true for the PNP configuration.

The two basic types of transistors along with their circuit Approx. 0.75"

Schematic symbol General purpose signal diodes Approx. 0.1"

(+) Anode Cathode (−)

(+) Anode Cathode (−)

Cathode (−)(+) Anode Approx. 0.2"

Rectifier diodes 35 ampere silicon rectifier Copper Lead Insulating washer Insulating tube Pressure plate Copper oxide Direction of circuit flow symbols are shown. Note that the two symbols are different. The horizontal line represents the base, and two angular lines represent the emitter and collector. The angular line with the arrow on it is the emitter, while the line without is the collector. The direction of the arrow on the emitter determines whether or not the transistor is a PNP or an NPN type. If the arrow is pointing in, the transistor is a PNP. On the other hand, if the arrow is pointing out, then it is an NPN type.

### Transistor Theory

As discussed in the section on diodes, the movement of the electrons and holes can be considered current. Electron current moves in one direction, while hole current travels in the opposite direction. In transistors, both electrons and holes act as carriers of current.

A forward biased PN junction is comparable to a low-resistance circuit element, because it passes a high current for a given voltage. On the other hand, a reverse-biased PN junction is comparable to a high-resistance circuit element. By using Ohm’s Law formula for power (P = I 2R) and assuming current is held constant through both junctions, it can be concluded that the power developed across the high resistance junction is greater than that developed across a low resistance junction. Therefore, if a crystal were to contain two PN junctions, one forward biased and the other reverse biased, and a low-power signal injected into the forward biased junction, a high-power signal could be produced at the reverse-biased junction.

To use the transistor as an amplifier, some sort of external bias voltage must modify each of the junctions. The first PN junction (emitter-base) is biased in the forward direction. This produces a low resistance. The second junction, which is the collector-base junction, is reverse biased to produce a high resistance.

Schottky diode Step-recovery diode Zener LED Photodiode Varactor With the emitter-base junction biased in the forward direction, electrons leave the negative terminal of the battery and enter the N-material. These electrons pass easily through the emitter, cross over the junction, and combine with the hole in the P-material in the base. For each electron that fills a hole in the P-material, another electron leaves the P-material, which creates a new hole and enters the positive terminal of the battery.

The second PN junction, which is the base-collector junction, is reverse biased. This prevents the majority carriers from crossing the junction, thus creating a high-resistance circuit. It is worth noting that there still is a small current passing through the reversed PN junction in the form of minority carriers—that is, electrons in the P-material and holes in the N-material. The minority carriers play a significant part in the operation of the NPN transistor.

There are two batteries in the circuit used to bias the NPN transistor. Vbb is considered the base voltage supply, rated in this illustration at 1 volt, and the battery voltage Vcc, rated at 6 volts, is called the collector voltage supply.

Current within the external circuit is simply the movement of free electrons originating at the negative terminal of the battery and flowing to the N-material. As the electrons enter the N-material, they become the majority carrier and move through the N-material to the emitter-base PN junction. This emitter-base junction is forward biased at about 0.65 to 0.7 volts positive with respect to the emitter and presents no resistance to the flow of electrons from the emitter into the base, which is composed of P-material. As these electrons move into the base, they drop into available holes. For every electron that drops into a hole, another electron exits the base by way of the base lead and becomes the base current or Ib. Of course, when one electron leaves the base, a new hole is formed. From the standpoint of the collector, these electrons that drop into holes are lost and of no use. To reduce this loss of electrons, the transistor is designed so that the base is very thin in relation to the emitter and collector, and the base is lightly doped.

Most of the electrons that move into the base fall under the influence of the reverse bias of the collector. While collector-base junction is reverse biased with respect to the majority carriers, it behaves as if it is forward biased to the electrons or minority carriers in this case. The electrons are accelerated through the collector-base junction and into the collector. The collector is comprised of the N-type material; therefore, the electrons once again become the majority carrier. Moving easily through the collector, the electrons return to the positive terminal of the collector supply battery Vcc, which is shown as Ic.

Because of the way this device operates to transfer current (and its internal resistances) from the original conduction path to another, its name is a combination of the words “transfer” and “resistor”—transistor.

### PNP Transistor Operation

The PNP transistor generally works the same way as the NPN transistor. The primary difference is that the emitter, base, and collector materials are made of different material than the NPN. The majority and minority current carriers are the opposite in the PNP to that of the NPN. In the case of the PNP, the majority carriers are the holes instead of the electrons in the NPN transistor. To properly bias the PNP, the polarity of the bias network must be reversed.

### Identification of Transistors

The methods of identifying leads vary due to a lack of a standard and require verification using manufacturer information to properly identify. However, a short description of the common methods is discussed below.

The collector lead in this case is identified by the wide space between it and the lead for the base. The final lead at the far left is the emitter. In many cases, colored dots indicate the collector lead, and short leads relative to the other leads indicate the emitter. In a conventional power diode, the collector lead is usually a part of the mounting bases, while the emitter and collector are leads or tines protruding from the mounting surface.

### Field Effect Transistors

Another transistor design that has become more important than the bipolar transistor is the field-effect transistor (FET). The primary difference between the bipolar transistor and the FET is that the bipolar transistor has two PN junctions and P N PEmitter Collector Base PN junctions N P NEmitter Collector Base PN junctions P N P Emitter Collector Base N P N Base Emitter Collector Base Base

The bipolar transistor is a current-controlled device, while the FET has only one PN junction and is a voltage-controlled device. Within the FET family, there are two general categories of components. One category is called the junction FET (JFET), which has only one PN junction. The other category is known as the enhancement-type or metal-oxide JET (MOSFET).

It can be seen that the drain (D) and source (S) are connected to an N-type material, and the gate (G) is connected to the P-type material. With gate voltage Vgg set to 0 volts and drain voltage Vdd set to some positive voltage, a current flows between the source and the drain, through a narrow band of N-material. If then, Vgg is adjusted to some negative voltage, the PN junction is reverse biased, and a depletion zone (no charge carriers) is established at the PN junction. By reducing the region of noncarriers, it has the effect of reducing the dimensions of the N-channel, resulting in a reduction of source to drain current.

Because JFETs are voltage-controlled devices, they have some advantages over the bipolar transistor. One such advantage is that because the gate is reverse biased, the circuit that it is connected to sees the gate as a very high resistance. This means that the JFET has less of an insertion influence in the circuit. The high resistance also means that less current is used.

Like many other solid-state devices, careless handling and static electricity can damage the JFET. Technicians should take all precautions to prevent such damage.

### Metal-Oxide-Semiconductor FET (MOSFET)

The biasing arrangement for the MOSFET is essentially the same as that for the JFET. The term “enhancement” comes from the idea that when there is no bias voltage applied to the gate (G), then there is no channel for current conduction between the source (S) and the drain (D). By applying a greater voltage on the gate (G), the P-channel begins to materialize and grow in size. Once this occurs, the source (S) to drain (D) current Id increases. The schematic symbol reflects this characteristic by using a broken line to indicate that the channel does not exist without a gate bias.

### Common Transistor Configurations

A transistor may be connected in one of three different configurations: common-emitter (CE), common-base (CB), and common-collector (CC). The term “common” is used to indicate which element of the transistor is common to both the input and the output. Each configuration has its own characteristics, which makes each configuration suitable for particular applications. A way to determine what configuration you may find in a circuit is to first determine which of the three transistor elements is used for the input signal. Then, determine the element used for the output signal. At that point, the remaining element, (base, emitter, or collector) is the common element to both the input and output, and thus you determine the configuration.

#### Common-Emitter (CE) Configuration

This is the configuration most commonly used in amplifier circuits because they provide good gains for voltage, current, and power. The input signal is applied to the base-emitter junction, which is forward biased (low resistance), and the output signal is taken off the collector-emitter junction, which is reverse biased (high resistance). Then the emitter is the common element to both input and output circuits.

When the transistor is connected in a CE configuration, the input signal is injected between the base and emitter, which is a low-resistance, low-current circuit. As the input signal goes positive, it causes the base to go positive relative to the emitter. This causes a decrease in the forward bias, which in turn reduces the collector current IC and increases the collector voltage (EC being more negative). During the negative portion of the input signal, the voltage on the base is driven more negative relative to the emitter. This increases the forward bias and allows an increase in collector current IC and a decrease in collector voltage (EC being less negative and going positive). The collector current, which flows through the reverse-biased junction, also flows through a high-resistance load resulting in a high level of amplification.

Because the input signal to the CE goes positive when the output goes negative, the two signals are 180° out of phase. This is the only configuration that provides a phase reversal. The CE is the most popular of the three configurations because it has the best combination of current and voltage gain. Gain is a term used to indicate the magnitude of amplification. Each transistor configuration has its unique gain characteristics even though the same transistors are used.

#### Common-Collector (CC) Configuration

This transistor configuration is usually used for impedance matching. It is also used as a current driver due to its high current gain. It is also very useful in switching circuits since it has the ability to pass signals in either direction.

In the CC circuit, the input signal is applied to the base, and the output signal is taken from the emitter, leaving the collector as the common point between the input and the output. The input resistance of the CC circuit is high, while the output resistance is low. The current gain is higher than that in the CE, but it has a lower power gain than either the CE or CB configuration. Just like the CB configuration, the output signal of the CC circuit is in phase with the input signal. The CC is typically referred to as an emitter-follower because the output developed on the emitter follows the input signal applied to the base.

#### Common-Base (CB) Configuration

The primary use of this configuration is for impedance matching because it has low input impedance and high output resistance. Two factors, however, limit the usefulness of this circuit application. First is the low-input resistance and second is its lack of current, which is always below 1. Since the CB configuration gives voltage amplification, there are some applications for this circuit, such as microphone amplifiers.

In the CB circuit, the input signal is applied to the emitter and the output signal is taken from the collector. In this case, both the input and the output have the base as a common element. When an input signal is applied to the emitter, it causes the emitter-base junction to react in the same manner as that in the CE circuit. When an input adds to the bias, it increases the transistor current; conversely, when the signal opposes the bias, the current in the transistor decreases.

The signal adds to the forward bias, since it is applied to the emitter, causing the collector current to increase. This increase in I C results in a greater voltage drop across the load resistor RL, thus lowering the collector voltage E C. The collector voltage, in becoming less negative, swings in a positive direction and is therefore in phase with the incoming positive signal.

## 2. 中文翻译

晶体管是一种三端器件，主要用于放大信号并控制电路中的电流。基本的两结半导体必须有一种类型的区域夹在另外两个同类型区域之间。晶体管中的三个区域是集电极（C）、发射极（E）和基极（B），集电极掺杂适中，发射极掺杂很重，而基极的掺杂则显著较轻。半导体材料类型的交替叠层为每种晶体管提供了常用的商业名称。各层之间的界面称为结。前面讨论过的硒二极管和锗二极管就是结型二极管的例子。请注意，夹在中间的一层即基极，比集电极或发射极都薄得多。一般来说，这使在集电极与发射极端子之间通过的载流子能够产生「穿通」作用。

晶体管按其 N 型与 P 型材料的排列方式分为 NPN 型或 PNP 型。NPN 晶体管是在两个 N 型材料区域之间引入一薄层 P 型材料而形成的。PNP 结构的形成方式正好相反。

两种基本类型的晶体管及其电路……

（原文此处为图注碎片，无对应正文）

（原文此处为图注碎片，无对应正文）

（原文此处为图注碎片，无对应正文）

（原文此处为图注碎片，无对应正文）

……符号如图所示。请注意，这两个符号并不相同。水平线代表基极，两条斜线分别代表发射极和集电极。带箭头的斜线是发射极，不带箭头的斜线是集电极。发射极上箭头的方向决定该晶体管是 PNP 型还是 NPN 型。如果箭头向内指，该晶体管就是 PNP 型。另一方面，如果箭头向外指，则为 NPN 型。

### 晶体管理论

正如二极管一节所讨论的，电子和空穴的运动都可以视为电流。电子电流朝一个方向流动，而空穴电流则朝相反方向流动。在晶体管中，电子和空穴都充当电流的载流子。

正向偏置的 PN 结相当于一个低电阻的电路元件，因为在给定电压下它能通过较大的电流。另一方面，反向偏置的 PN 结则相当于一个高电阻的电路元件。利用欧姆定律的功率公式（P = I²R），并假设通过两个结的电流保持恒定，可以得出结论：高阻结上产生的功率大于低阻结上产生的功率。因此，如果一个晶体含有两个 PN 结，一个正向偏置、另一个反向偏置，并有低功率信号注入正向偏置的结，那么在高阻结处就能产生高功率信号。

要把晶体管用作放大器，必须由某种外部偏置电压来改变每个结的状态。第一个 PN 结（发射极-基极结）沿正向偏置，这产生低电阻。第二个结即集电极-基极结，反向偏置以产生高电阻。

在发射极-基极结正向偏置的情况下，电子离开电池负极进入 N 型材料。这些电子容易地通过发射极、越过结，并与基极 P 型材料中的空穴复合。每有一个电子填满 P 型材料中的空穴，就有另一个电子离开 P 型材料，从而产生一个新的空穴，而这个电子则进入电池的正极。

第二个 PN 结即基极-集电极结，处于反向偏置。这阻止多数载流子越过该结，从而形成高电阻电路。值得注意的是，仍有少量电流以少数载流子的形式通过反向偏置的 PN 结，即 P 型材料中的电子和 N 型材料中的空穴。少数载流子在 NPN 晶体管的工作中起着重要作用。

电路中有两组电池用来给 NPN 晶体管加偏置。Vbb 被视为基极电压电源，在图中标为 1 伏；标为 6 伏的电池电压 Vcc 称为集电极电压电源。

外部电路中的电流，其实就是自由电子从电池负极出发、流向 N 型材料的运动。当电子进入 N 型材料时，它们成为多数载流子，并穿过 N 型材料到达发射极-基极 PN 结。该发射极-基极结相对于发射极以约 0.65 至 0.7 伏的正向电压偏置，对电子从发射极流入由 P 型材料构成的基极不呈现任何电阻。当这些电子进入基极时，便落入可用的空穴中。每有一个电子落入空穴，就有另一个电子经由基极引线离开基极，成为基极电流或 Ib。当然，当一个电子离开基极时，就形成一个新的空穴。从集电极的角度来看，这些落入空穴的电子是损耗掉的、毫无用处。为减少这种电子损耗，晶体管的设计使基极相对于发射极和集电极非常薄，并且基极掺杂较轻。

进入基极的大部分电子会受集电极反向偏置的影响。虽然集电极-基极结相对于多数载流子是反向偏置的，但对本例中的电子即少数载流子来说，它表现得好像正向偏置一样。电子被加速穿过集电极-基极结进入集电极。集电极由 N 型材料构成，因此电子又一次成为多数载流子。电子容易地通过集电极，回到集电极电源电池 Vcc 的正极，这部分电流即标为 Ic。

由于这种器件把电流（以及其内部电阻）从原来的传导路径转移到另一条路径，它的名称就是「transfer」（转移）和「resistor」（电阻）两个词组合而成——transistor。

### PNP 晶体管的工作

PNP 晶体管的工作方式大体上与 NPN 晶体管相同。主要区别在于发射极、基极和集电极所用的材料与 NPN 不同。PNP 中的多数载流子和少数载流子与 NPN 相反。就 PNP 而言，多数载流子是空穴，而不是 NPN 晶体管中的电子。要对 PNP 正确加偏置，偏置网络的极性必须反转。

### 晶体管的识别

引线的识别方法因缺乏统一标准而各不相同，必须借助制造商资料才能正确识别。不过，下面简要介绍一些常用方法。

在这种情况下，集电极引线由它与基极引线之间较宽的间隔来识别。最左边的最后一根引线是发射极。在许多情况下，彩色圆点表示集电极引线，而相对于其他引线较短的引线表示发射极。在常规功率二极管中，集电极引线通常是安装底座的一部分，而发射极和集电极是从安装面伸出的引线或齿片。

### 场效应晶体管

另一种已变得比双极晶体管更重要的晶体管设计是场效应晶体管（FET）。双极晶体管与 FET 之间的主要区别在于：双极晶体管有两个 PN 结，……

……它是一种电流控制器件，而 FET 只有一个 PN 结，是一种电压控制器件。在 FET 这一门类中有两大类元件。一类称为结型 FET（JFET），它只有一个 PN 结。另一类称为增强型或金属氧化物 JET（MOSFET）。

可以看出，漏极（D）和源极（S）接在 N 型材料上，而栅极（G）接在 P 型材料上。当栅极电压 Vgg 设为 0 伏、漏极电压 Vdd 设为某个正电压时，电流便在源极与漏极之间流过一条狭窄的 N 型材料带。若把 Vgg 调到某个负电压，PN 结就反向偏置，并在 PN 结处形成一个耗尽区（无载流子）。通过缩小无载流子的区域，其效果是减小 N 沟道的尺寸，从而使源极到漏极的电流减小。

由于 JFET 是电压控制器件，它们比双极晶体管具有一些优点。其中一个优点是，由于栅极处于反向偏置，与栅极相连的电路把栅极看成非常高的电阻。这意味着 JFET 对电路的插入影响较小。高电阻还意味着所用电流较少。

与许多其他固态器件一样，粗心操作和静电都可能损坏 JFET。技术人员应采取一切预防措施防止这类损坏。

### 金属氧化物半导体 FET（MOSFET）

MOSFET 的偏置方式与 JFET 的基本相同。「增强」一词的由来是：当栅极（G）上没有施加偏置电压时，源极（S）与漏极（D）之间没有导电沟道。通过在栅极（G）上施加更大的电压，P 沟道开始形成并增大。一旦出现这种情况，源极（S）到漏极（D）的电流 Id 就会增大。原理图中的符号用一条虚线来反映这一特性，表示没有栅极偏置时沟道并不存在。

### 常见的晶体管接法

晶体管可以接成三种不同组态之一：共发射极（CE）、共基极（CB）和共集电极（CC）。「共」这个词用来指出晶体管中哪一个元件是输入与输出所共有的。每种组态都有自己的特性，因而各自适合特定的应用。判断电路中可能是哪一种组态的方法是：先确定三个晶体管元件中哪一个用于输入信号，再确定哪一个用于输出信号。此时剩下的那个元件（基极、发射极或集电极）就是输入与输出共有的元件，从而可以确定组态。

#### 共发射极（CE）组态

这是放大器中最常用的……电路，因为它对电压、电流和功率都能提供良好的增益。输入信号加在正向偏置（低电阻）的基极-发射极结上，输出信号取自反向偏置（高电阻）的集电极-发射极结。于是发射极就是输入电路与输出电路共有的元件。

当晶体管接成 CE 组态时，输入信号注入基极与发射极之间，这是一个低电阻、小电流的电路。当输入信号变正时，基极相对于发射极也变正。这使正向偏置减小，进而使集电极电流 IC 减小、集电极电压升高（EC 变得更负）。在输入信号的负半周，基极电压相对于发射极被推得更负。这使正向偏置增大，允许集电极电流 IC 增大、集电极电压降低（EC 变得不那么负，即向正方向变化）。流过反向偏置结的集电极电流也流过一个大电阻负载，从而获得很高的放大倍数。

由于 CE 的输入信号变正时输出变负，两个信号相差 180°。这是唯一能提供相位反转的组态。CE 是三种组态中最常用的一种，因为它对电流和电压的增益配合最佳。增益是用来表示放大量的术语。即使使用同一只晶体管，每种组态也各有其独特的增益特性。

#### 共集电极（CC）组态

这种晶体管组态通常用于阻抗匹配。由于其电流增益高，也用作电流驱动级。由于它能够在两个方向上通过信号，在开关电路中也很有用。

在 CC 电路中，输入信号加在基极上，输出信号取自发射极，集电极则成为输入与输出之间的公共点。CC 电路的输入电阻高，而输出电阻低。其电流增益高于 CE，但功率增益低于 CE 或 CB 组态。与 CB 组态一样，CC 电路的输出信号与输入信号同相。CC 通常被称为射极跟随器，因为发射极上产生的输出跟随加在基极上的输入信号。

#### 共基极（CB）组态

这种组态的主要用途是阻抗匹配，因为它输入阻抗低而输出电阻高。然而，有两个因素限制了这种电路应用的价值。第一是输入电阻低，第二是电流增益不足，其值总在 1 以下。由于 CB 组态能提供电压放大，这种电路也有一些应用，例如传声器放大器。

在 CB 电路中，输入信号加在发射极上，输出信号取自集电极。在这种情况下，输入和输出都以基极作为公共元件。当输入信号加在发射极上时，它使发射极-基极结的反应方式与 CE 电路相同。当输入信号与偏置叠加时，晶体管电流增大；反之，当信号与偏置相反时，晶体管中的电流减小。

由于信号加在发射极上，它与正向偏置叠加，使集电极电流增大。I C 的这一增大使负载电阻 RL 上的电压降加大，从而使集电极电压 E C 降低。集电极电压因变得不那么负而向正方向摆动，因此与输入的正信号同相。

## 3. 专业词汇

| 英文 | 词性 | 中文 | 本节语境 |
| --- | --- | --- | --- |
| transistor | n. | 晶体管 | 三端器件，由 transfer 与 resistor 两词合成 |
| collector (C) | n. | 集电极 | 掺杂适中、与基极结成反向偏置结、收集载流子 |
| emitter (E) | n. | 发射极 | 掺杂最重，发射极-基极结正向偏置 |
| base (B) | n. | 基极 | 夹在中间、很薄且轻掺杂，以减少电子损耗 |
| junction | n. | 结 | 两种半导体材料层之间的界面 |
| NPN / PNP | n. | NPN 型 / PNP 型 | 按 N、P 材料交替排列方式区分的两类晶体管 |
| bias | n./v. | 偏置 | 外加电压设定两个结的正/反向状态 |
| amplifier | n. | 放大器 | 晶体管的主要用途之一，把低功率信号放大 |
| majority carrier | n. | 多数载流子 | N 型中的电子，本节用其说明基极损耗 |
| depletion zone | n. | 耗尽区 | 反向偏置后在结处形成的无载流子区域 |
| FET | n. | 场效应晶体管 | 只有一个 PN 结的电压控制器件 |
| JFET | n. | 结型场效应晶体管 | 仅一个 PN 结，栅极加负压使沟道变窄 |
| MOSFET | n. | 金属氧化物半导体 FET | 无栅极偏置时无沟道，符号用虚线表示 |
| drain / source / gate | n. | 漏极 / 源极 / 栅极 | FET 的三个端子，D、S 接 N 型，G 接 P 型 |
| impedance matching | n. | 阻抗匹配 | CC 与 CB 组态的主要用途 |

## 4. 语法解析

### ① 过去分词短语作后置定语 + 并列不定式
**原句**：The transistor is a three-terminal device primarily used to amplify signals and control current within a circuit.
**拆解**：主句 The transistor is a three-terminal device 为系表结构；primarily used to amplify signals and control current within a circuit 为过去分词短语作 device 的后置定语，其中 used 后接两个并列的不定式 to amplify 与（to）control，第二个不定式省略 to。
**要点**：过去分词作定语含被动意义，等于 which is used to…，比定语从句简洁，是定义句的常用写法；两个不定式并列时第二个 to 常省略，但表对比时须保留；primarily 修饰 used，说明这是该器件的主要用途而非唯一用途。

### ② 三个非限制性定语从句并列 + 被动语态
**原句**：The three regions in a transistor are the collector (C), which is moderately doped, the emitter (E), which is heavily doped, and the base (B), which is significantly less doped.
**拆解**：主语 The three regions in a transistor，系动词 are，表语为三个并列名词短语 the collector (C)、the emitter (E)、the base (B)，每个名词后跟一个 which 引导的非限制性定语从句；三个从句均为被动语态 is doped，程度副词分别为 moderately、heavily、significantly less。
**要点**：并列成分较长时用逗号加 and 收尾，阅读时应先抓三个 the… 核心名词再看从句；dope 意为「掺杂」，其被动形式 is doped 在半导体文献中专指掺入杂质；比较级 less doped 前加 significantly 表示「明显更轻」，注意 less 修饰的是 doped 而非名词。

### ③ by 动名词 + it can be concluded that + 比较结构
**原句**：By using Ohm’s Law formula for power (P = I 2R) and assuming current is held constant through both junctions, it can be concluded that the power developed across the high resistance junction is greater than that developed across a low resistance junction.
**拆解**：By using … and assuming … 为方式状语，介词 by 后接两个并列动名词，assuming 后带省略 that 的宾语从句 current is held constant；主句 it 为形式主语，真正主语是 that 从句，can be concluded 为被动谓语；that 从句中 the power developed across … 为主语（developed 为过去分词后置定语），is greater than that developed across … 为比较结构，that 替代 the power。
**要点**：by 后两个动名词共用一个 by，第二个不再重复介词；it can be concluded that 是科技英语中表达推理的固定句式，译文用「可以得出结论」；比较句中的 that 是代词，替代前面出现过的不可数名词 power，不能用 one。

### ④ 虚拟条件句（were to）+ 分词独立结构
**原句**：Therefore, if a crystal were to contain two PN junctions, one forward biased and the other reverse biased, and a low-power signal injected into the forward biased junction, a high-power signal could be produced at the reverse-biased junction.
**拆解**：Therefore 为连接副词；if 引导与将来事实相反的虚拟条件句，从句谓语 were to contain；one forward biased and the other reverse biased 与 a low-power signal injected into the forward biased junction 均为「名词 + 过去分词」的独立主格结构，补充说明条件；主句 a high-power signal could be produced at the reverse-biased junction 为被动语态。
**要点**：were to do 表示「假如将来发生」，比 should 更正式，句中常省略 if 而倒装为 Were a crystal to contain；独立主格中过去分词表被动，forward biased 即 which is forward biased；主句用 could 与从句 were to 呼应，构成虚拟语气。

### ⑤ 表语从句嵌套原因从句与定语从句
**原句**：One such advantage is that because the gate is reverse biased, the circuit that it is connected to sees the gate as a very high resistance.
**拆解**：主句 One such advantage is that…；that 引导表语从句，从句内 because the gate is reverse biased 为原因状语从句，主句为 the circuit sees the gate as a very high resistance，其中 that it is connected to 为定语从句修饰 the circuit，介词 to 后置。
**要点**：see A as B 意为「把 A 看作 B」，此处主语是电路，属拟人化表达，翻译时可译为「电路把栅极视为……」；that it is connected to 中介词 to 留在句末，because 从句插在表语从句开头，阅读时先跳过它找到主谓；reverse biased 为复合形容词，由副词 + 过去分词构成。
