# Filtering

> 通用 Ch 12 · Filtering · 原文 PDF 第 553 页

## 1. 原文

One of the more common uses of the capacitor and inductor that the technician may find in the field is that of the filter.

### Filtering Characteristics of Capacitors

The nature of capacitance opposes a voltage change across its terminal by storing energy in its electrostatic field. Whenever the voltage tends to rise, the capacitor converts this voltage change to stored energy. When the voltage tends to fall, the capacitor converts this stored energy back to voltage. The use of a capacitor for filtering the output of a rectifier is illustrated in the figure. The rectifier is shown as a block, and the capacitor C1 is connected in parallel with the load R1.

The capacitor C1 is chosen to offer very low impedance to the AC ripple frequency and very high impedance to the DC component. The ripple voltage is therefore bypassed to ground through the low impedance path of the capacitor, while the DC voltage is applied unchanged to the load. The effect of the capacitor on the output of the rectifier can be seen in the waveshapes shown in the figure. Dotted lines show the rectifier output, while the solid lines show the effect of the capacitor. In this example, full-wave rectifier outputs are shown. The capacitor C1 charges when the rectifier voltage output tends to increase and discharges when the voltage output tends to decrease. In this manner, the voltage across the load R1 is kept fairly constant.

### Filtering Characteristics of Inductors

The inductance provided by an inductor may be used as a filter, because it opposes a change in current through it by storing energy in its electromagnetic field. Whenever the current increases, the stored energy in the electromagnetic field increases. When the current through the inductor decreases, the inductor supplies the energy back into the circuit in order to maintain the existing flow of current. The use of an inductor for filtering the output of a rectifier is shown in the figure. Note that in this network the inductor L1 is in series with the load R1.

The inductance L1 is selected to offer high impedance to the AC ripple voltage and low impedance to the DC component. The result is a very large voltage drop across the inductor and a very small voltage drop across the load R 1. For the DC component, however, a very small voltage drop occurs across the inductor and a very large voltage drop across the load. The effect of an inductor on the output of a full-wave rectifier in the output waveshape is shown in the figure.

### Common Filter Configurations

Capacitors and inductors are combined in various ways to provide more satisfactory filtering than can be obtained with a single capacitor or inductor. These are referred to collectively as LC filters. Several combinations are shown schematically in the figure. Note that the L, or inverted L-type, and the T-type filter sections resemble schematically the corresponding letters of the alphabet. The pi-type filter section resembles the Greek letter pi (π) schematically.

All the filter sections shown are similar in that the inductances are in series and the capacitances are in parallel with the load. The inductances must, therefore, offer very high impedance and the capacitors very low impedance to the ripple frequency. Since the ripple frequency is comparatively low, the inductances are iron core coils having large values of inductance (several henries). Because they offer such high impedance to the ripple frequency, these coils are called chokes. The capacitors must also be large (several microfarads) to offer very little opposition to the ripple frequency. Because the voltage across the capacitor is DC, electrolytic capacitors are frequently used as filter capacitors. Always observe the correct polarity in connecting electrolytic capacitors.

LC filters are also classified according to the position of the capacitor and inductor. A capacitor input filter is one in which the capacitor is connected directly across the output terminals of the rectifier. A choke input filter is one in which a choke precedes the filter capacitor.

If it is necessary to increase the applied voltage to more than a single rectifier can tolerate, the usual solution is to stack them. These rectifiers are similar to resistors added in series. Each resistor drops a portion of the applied voltage rather than the total voltage. The same theory applies to rectifiers added in series or stacked. Series stacking increases the voltage rating. If, for example, a rectifier is destroyed with an applied voltage exceeding 50 volts, and it is to be used in a circuit with an applied voltage of 150 volts, stacking of diodes can be employed. The result is shown in the figure.

### Basic LC Filters

Analog filters are circuits that perform signal processing functions, specifically intended to remove unwanted signal components, such as ripple, and enhance desired signals. The simplest analog filters are based on combinations of inductors and capacitors. The four basic categories of filters discussed are: low-pass, high-pass, band-pass and band-stop. All these types are collectively known as passive filters, because they do not depend on any external power source.

The operation of a filter relies on the characteristic of variable inductive and capacitive reactance based on the applied frequency. In review, the inductor blocks high-frequency signals (high reactance) and conducts low-frequency signals (low reactance), while capacitors do the reverse. A filter in which the signal passes through an inductor, or in which a capacitor provides a path to earth, presents less attenuation (reduction) to a low-frequency signal than to a high-frequency signal and is considered a low-pass filter. If the signal passes through a capacitor, or has a path to ground through an inductor, then the filter presents less attenuation to high-frequency signals than low-frequency signals and is then considered a high-pass filter. Typically after an AC signal is rectified, the pulses of voltage are changed to usable form of DC by way of filtering.

#### Low-Pass Filter

A low-pass filter is a filter that passes low frequencies well, but attenuates (reduces) higher frequencies. The so-called cutoff frequency divides the range of frequencies that are passed and the range of frequencies that are stopped. In other words, the frequency components higher than the cutoff frequency are stopped by a low-pass filter. The actual amount of attenuation for each frequency varies by filter design.

An inductive low-pass filter inserts an inductor in series with the load, where a capacitive low-pass filter inserts a resistor in series and a capacitor in parallel with the load. The former filter design tries to block the unwanted frequency signal while the latter tries to short it out. The figure illustrates this type of circuit and the frequency/current flow response.

#### High-Pass Filter (HPF)

A high-pass filter (HPF) is a filter that passes high frequencies well, but attenuates (reduces) frequencies lower than the cutoff frequency. The actual amount of attenuation for each frequency varies once again depending on filter design. In some cases, it is called a low-cut filter. An HPF is essentially the opposite of a low-pass filter.

It is useful as a filter to block any unwanted low frequency components of a signal while passing the desired higher frequencies. The figure illustrates this type of circuit and the frequency/current flow response.

#### Band-Pass Filter

A band-pass filter is basically a combination of a high-pass and a low-pass. There are some applications where a particular range of frequencies need to be singled out or filtered from a wider range of frequencies. Band-pass filter circuits are designed to accomplish this task by combining the properties of low-pass and high-pass into a single filter. The figure illustrates this type of circuit and the frequency/current flow response.

#### Band-Stop Filter

In signal processing, a band-stop filter or band-rejection filter is a filter that passes most frequencies unaltered, but attenuates those in a range to very low levels. It is the opposite of a band-pass filter. A notch filter is a band-stop filter with a narrow stopband (high Q factor). Notch filters are used in live sound reproduction (public address (PA) systems) and in instrument amplifier (especially amplifiers or preamplifiers for acoustic instruments, such as acoustic guitar, mandolin, bass instrument amplifier, etc.) to reduce or prevent feedback, while having little noticeable effect on the rest of the frequency spectrum. Other names include “band limit filter,” “T-notch filter,” “band-elimination filter,” and “band-rejection filter.”

Typically, the width of the stop-band is less than 1 to 2 decades (that is, the highest frequency attenuated is less than 10 to 100 times the lowest frequency attenuated). In the audio band, a notch filter uses high and low frequencies that may be only semitones apart.

A band-stop filter is the general case. A notch filter is a specific type of band-stop filter with a very narrow range. Also called band-elimination, band-reject, or notch filters, this kind of filter passes all frequencies above and below a particular range set by the component values. Not surprisingly, it can be made out of a low-pass and a high-pass filter, just like the band-pass design, except that this time we connect the two filter sections in parallel with each other instead of in series. The figure illustrates this type of circuit and the frequency/current flow response.

## 2. 中文翻译

技术人员在外场最常遇到的电容器和电感器用途之一，就是用它们构成滤波器。

### 电容器的滤波特性

电容的本性，是靠在自身静电场中储存能量来阻止其两端电压发生变化。每当电压趋于升高时，电容器就把这一电压变化转化为储存起来的能量；当电压趋于下降时，电容器又把储存的能量转换回电压。用一只电容器对整流器输出进行滤波的做法如图所示。图中整流器用方框表示，电容 C1 与负载 R1 并联。

选择电容 C1，是为了让它对交流纹波频率呈现很低的阻抗，而对直流分量呈现很高的阻抗。因此，纹波电压经由电容器这条低阻抗通路被旁路到地，直流电压则原样加到负载上。电容器对整流器输出的作用可以从图中所示的波形看出。虚线表示整流器的输出，实线表示电容器所起的作用。本例给出的是全波整流器的输出。整流器输出电压趋于升高时 C1 充电，输出电压趋于降低时 C1 放电。这样，负载 R1 两端的电压便保持得相当稳定。

### 电感器的滤波特性

电感器所提供的电感可以用作滤波器，因为它靠在自身电磁场中储存能量来阻碍流过它的电流发生变化。每当电流增大时，电磁场中储存的能量就增加；当流过电感器的电流减小时，电感器就把能量送还电路，以维持原有的电流流动。用电感器对整流器输出进行滤波的做法如图所示。注意在这个网络中，电感 L1 与负载 R1 串联。

选择电感 L1，是为了让它对交流纹波电压呈现高阻抗，而对直流分量呈现低阻抗。其结果是电感器上产生很大的电压降，负载 R 1 上的电压降则很小；但对直流分量而言，电感器上的电压降很小，负载上的电压降则很大。电感器对全波整流器输出波形的作用如图所示。

### 常见的滤波器结构

把电容器和电感器以各种方式组合起来，可以获得比单用电容器或单用电感器更令人满意的滤波效果。这类电路统称为 LC 滤波器。若干种组合如图所示。注意 L 型（也称倒 L 型）和 T 型滤波节在电路图形状上分别类似于字母表中对应的字母，π 型滤波节在电路图形状上则类似于希腊字母 π。

所示的各滤波节的共同之处在于：电感串联在电路中，电容与负载并联。因此，对纹波频率而言，电感必须呈现很高的阻抗，电容必须呈现很低的阻抗。由于纹波频率相对较低，这些电感都是电感量很大（数亨）的铁心线圈。正因为它们对纹波频率呈现如此高的阻抗，这类线圈被称为扼流圈（choke）。电容器也必须做得很大（数微法），才能对纹波频率几乎不形成阻碍。由于电容器两端的电压是直流电压，滤波电容常用电解电容。连接电解电容时务必注意极性正确。

LC 滤波器还可按电容和电感的位置来分类。电容输入滤波器，是指电容直接跨接在整流器输出端的滤波器；扼流圈输入滤波器，则是指扼流圈位于滤波电容之前的滤波器。

如果必须把所加电压提高到单只整流器所能承受的电压以上，通常的解决办法是把整流器堆叠起来。这与把电阻串联相似：每只电阻只分担所加电压的一部分，而不是承担全部电压。把整流器串联（堆叠）也是同样的道理。串联堆叠可以提高额定电压。例如，某只整流器在施加电压超过 50 伏时就会损坏，而它又要用于施加电压为 150 伏的电路中，就可以采用二极管堆叠，结果如图所示。

### 基本 LC 滤波器

模拟滤波器是执行信号处理功能的电路，专门用来除去不需要的信号成分（如纹波）并增强所需的信号。最简单的模拟滤波器建立在电感与电容的组合之上。所讨论的滤波器有四种基本类型：低通、高通、带通和带阻。这几类滤波器统称为无源滤波器，因为它们不依赖任何外部电源。

滤波器的工作依赖于感抗和容抗随所加频率而变的特性。回顾一下：电感器阻挡高频信号（感抗大），导通低频信号（感抗小），电容器的行为则正好相反。若信号须经电感器通过，或由电容器提供到地的通路，则该滤波器对低频信号的衰减（削弱）比对高频信号小，属于低通滤波器。若信号须经电容器通过，或经电感器提供到地的通路，则该滤波器对高频信号的衰减比对低频信号小，属于高通滤波器。通常，交流信号经整流之后，其电压脉冲要经过滤波才能转变为可用的直流形式。

#### 低通滤波器

低通滤波器，是指让低频很好地通过、而对较高频率加以衰减（削弱）的滤波器。所谓截止频率，把被通过的频率范围与被阻止的频率范围分开。换言之，高于截止频率的频率成分会被低通滤波器阻止。每个频率的实际衰减量随滤波器设计而异。

电感式低通滤波器把电感器串接在负载上，电容式低通滤波器则把一个电阻串联、一个电容与负载并联。前一种设计试图阻挡不需要的频率信号，后一种设计则试图把它短路掉。图展示了这类电路以及频率/电流的响应。

#### 高通滤波器（HPF）

高通滤波器（HPF），是指让高频很好地通过、而衰减（削弱）低于截止频率的频率的滤波器。每个频率的实际衰减量同样随滤波器设计而异。在某些场合，它被称为低切滤波器（low-cut filter）。高通滤波器本质上是低通滤波器的对立面。

它可用作滤波器，阻挡信号中任何不需要的低频成分，同时让所需的高频通过。图展示了这类电路以及频率/电流的响应。

#### 带通滤波器

带通滤波器基本上是高通与低通的组合。有些应用需要从较宽的频率范围中单挑出某一特定频段（或把它滤除）。带通滤波器电路正是把低通和高通的特性结合到一只滤波器中来完成这一任务的。图展示了这类电路以及频率/电流的响应。

#### 带阻滤波器

在信号处理中，带阻滤波器（band-stop filter）或称带除滤波器，是一种让大多数频率原样通过、而只把某一频段内的频率衰减到极低电平的滤波器。它是带通滤波器的对立面。陷波滤波器（notch filter）是阻带很窄（Q 值很高）的带阻滤波器。陷波滤波器用于现场扩声（public address（PA）系统）以及乐器放大器（尤其是原声吉他、曼陀林、贝司音箱等原声乐器所用的放大器或前置放大器）中，用来减少或防止回授，同时对频谱的其余部分几乎没有明显影响。其他名称还有“band limit filter（限带滤波器）”“T-notch filter（T 形陷波滤波器）”“band-elimination filter（带除滤波器）”和“band-rejection filter（带阻滤波器）”。

通常，阻带的宽度小于 1 到 2 个十倍频程（即被衰减的最高频率不到被衰减的最低频率的 10 到 100 倍）。在音频频段内，陷波滤波器所用的高、低频率可能只相差半音。

带阻滤波器是一般情形，陷波滤波器则是带阻滤波器中范围很窄的一种特例。这类滤波器也叫带除滤波器、带阻滤波器或陷波滤波器，它让由元件数值所设定的某一特定范围之上和之下的所有频率通过。不出所料，它可以像带通设计那样由一只低通和一只高通滤波器构成，只是这一次我们把两个滤波节并联而不是串联。图展示了这类电路以及频率/电流的响应。

## 3. 专业词汇

| 英文 | 词性 | 中文 | 本节语境 |
| --- | --- | --- | --- |
| filter | n. | 滤波器 | 本节主题，指用电抗随频率变化的元件滤除纹波、分离频段的电路 |
| ripple | n. | 纹波 | 整流器输出的交流脉动成分，即滤波器要旁路或阻挡的对象 |
| impedance | n. | 阻抗 | 电容对纹波频率呈低阻抗、电感呈高阻抗，这是滤波的物理基础 |
| capacitance | n. | 电容（量） | 电容的储能本性使电容器两端的电压不能突变，故能吸收纹波 |
| electrolytic capacitor | n. | 电解电容 | 容量大（数微法）的滤波电容，连接时极性不可接反 |
| choke | n. | 扼流圈 | 电感量数亨的铁心线圈，因对纹波频率呈高阻抗而得名 |
| cutoff frequency | n.phr. | 截止频率 | 划分通带与阻带的分界频率，高于它即被低通滤波器阻止 |
| band-pass filter | n.phr. | 带通滤波器 | 高通与低通的组合，只让某一频段通过 |
| band-stop filter | n.phr. | 带阻滤波器 | 让大多数频率通过、只衰减某一频段，为陷波滤波器的一般情形 |
| notch filter | n.phr. | 陷波滤波器 | 阻带极窄（高 Q）的带阻滤波器，用于抑制声回授 |
| passive filter | n.phr. | 无源滤波器 | 不依赖外部电源、仅由电感电容构成的滤波器类别 |
| attenuation | n. | 衰减 | 滤波器对某一频段信号的削弱程度，随设计而异 |

## 4. 语法解析

### ① by + 动名词短语表手段
**原句**：The nature of capacitance opposes a voltage change across its terminal by storing energy in its electrostatic field.
**拆解**：主句：主语 The nature of capacitance（of 短语作后置定语）+ 谓语 opposes + 宾语 a voltage change（across its terminal 为介词短语后置修饰 a voltage change）；by storing energy in its electrostatic field 为介词 by + 动名词短语，作方式状语。
**要点**：by + 动名词回答“靠什么手段/方式”，逻辑主语须与主句主语一致，此处 storing 的执行者就是 the nature of capacitance。技术文本常用它把“机制”压缩进一句，译成“靠……来……”。注意不要与 by + 名词（表示被动施动者）混淆；动名词还可换成 through + 名词以示同样含义。
### ② be chosen to do 与 offer sth to sth
**原句**：The capacitor C1 is chosen to offer very low impedance to the AC ripple frequency and very high impedance to the DC component.
**拆解**：主语 The capacitor C1 + 谓语 is chosen（被动语态）+ 不定式 to offer 作目的状语；offer 后接两个并列宾语 very low impedance 与 very high impedance，各自用 to + 对象说明“对谁而言”。
**要点**：is chosen to do 把设计者的意图隐含在被动结构里，是手册说明选型理由的固定说法，可译为“选择 C1，是为了让它……”。offer 搭配 offer sth to sb/sth 表“对……呈现/提供……”；两个并列宾语若一个带 to 短语一个不带，容易在阅读时丢掉第二个 to 的对象，本句中第二个 to the DC component 同样必须译出。
### ③ because 引导原因状语从句 + 被动语态
**原句**：Because they offer such high impedance to the ripple frequency, these coils are called chokes.
**拆解**：Because 引导原因状语从句（主语 they，谓语 offer，宾语 such high impedance，to the ripple frequency 说明对象）；主句主语 these coils + 谓语 are called + 主语补足语 chokes，为被动结构。
**要点**：such + 形容词 + 名词中的 such 强调程度，可译为“如此高的”，比 very high 更带因果意味。are called X 中的 X 是主语补足语而非宾语，译成“被称为……”；术语首次出现时，中文宜在该句后补出英文原词，便于对照原文。
### ④ “介词 + which”定语从句 + less…than 比较
**原句**：A filter in which the signal passes through an inductor, or in which a capacitor provides a path to earth, presents less attenuation (reduction) to a low-frequency signal than to a high-frequency signal and is considered a low-pass filter.
**拆解**：主语 A filter 带两个并列的“介词 + which”定语从句（in which the signal passes through an inductor / in which a capacitor provides a path to earth）；主句谓语为并列的 presents… 与 is considered…；less attenuation…than… 为比较结构，比较对象分别是 to a low-frequency signal 与 to a high-frequency signal。
**要点**：in which 相当于 where 或“在……中”，两个并列定语从句先用逗号与 or 连接，再把主句谓语推后，阅读时要先跳过从句找谓语 presents。less A than B 表示“A 比 B 少”，本句比较的是衰减量；并列谓语第二个前省略了主语 A filter，但 is considered 的主语仍是它。
### ⑤ it 作形式主语 + 表语为不定式
**原句**：If it is necessary to increase the applied voltage to more than a single rectifier can tolerate, the usual solution is to stack them.
**拆解**：If 引导条件状语从句，从句中 it 为形式主语，真正主语是 to increase the applied voltage…；more than a single rectifier can tolerate 为比较从句，tolerate 后省略了 the applied voltage；主句主语 the usual solution + 系动词 is + 表语 to stack them（不定式作表语）。
**要点**：it is necessary to do 是形式主语句型，不能写成 it is necessary that do；不定式作表语说明主语的具体内容（“解决办法就是……”，前后是对等关系，故用 is 而非 are）。more than 后接完整从句时，从句常省略与前面重复的宾语；them 指前文的 rectifiers，复数代词不可省。
### ⑥ that 定语从句 + pass sth + 形容词补语
**原句**：In signal processing, a band-stop filter or band-rejection filter is a filter that passes most frequencies unaltered, but attenuates those in a range to very low levels.
**拆解**：In signal processing 为地点/领域状语；主语 a band-stop filter or band-rejection filter（or 连接两个近义术语）+ 系动词 is + 表语 a filter；that 引导定语从句修饰 a filter，从句谓语为并列的 passes… 与 attenuates…；unaltered 为过去分词作宾语补足语，those in a range 指 those frequencies。
**要点**：pass sth unaltered 这种“动词 + 宾语 + 形容词”结构表示“使宾语保持某状态”，unaltered 修饰的是 frequencies，不是 filter，译成“让大多数频率原样通过”。attenuate sth to + 程度是固定搭配（“把……衰减到……”）；that 从句中并列两个谓语时，第二个前加 but 表示转折对比，主语 that 仍指 a filter。
