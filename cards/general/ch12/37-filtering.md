# Filtering

> 通用 Ch 12 · Filtering · 原文 PDF 第 553 页

## 1. 原文

One of the more common uses of the capacitor and inductor that the technician may find in the field is that of the filter.

### Filtering Characteristics of Capacitors

The nature of capacitance opposes a voltage change across its terminal by storing energy in its electrostatic field. Whenever the voltage tends to rise, the capacitor converts this voltage change to stored energy. When the voltage tends to fall, the capacitor converts this stored energy back to voltage. The use of a capacitor for filtering the output of a rectifier is illustrated in Figure 12-228. The rectifier is shown as a block, and the capacitor C1 is connected in parallel with the load R1.

The capacitor C1 is chosen to offer very low impedance to the AC ripple frequency and very high impedance to the DC component. The ripple voltage is therefore bypassed to ground through the low impedance path of the capacitor, while the DC voltage is applied unchanged to the load. The effect of the capacitor on the output of the rectifier can be seen in the waveshapes shown in Figure 12-229. Dotted lines show the rectifier output, while the solid lines show the effect of the capacitor. In this example, full-wave rectifier outputs are shown. The capacitor C1 charges when the rectifier voltage output tends to increase and discharges when the voltage output tends to decrease. In this manner, the voltage across the load R1 is kept fairly constant.

### Filtering Characteristics of Inductors

The inductance provided by an inductor may be used as a filter, because it opposes a change in current through it by storing energy in its electromagnetic field. Whenever the current increases, the stored energy in the electromagnetic field increases. When the current through the inductor decreases, the inductor supplies the energy back into the circuit in order to maintain the existing flow of current. The use of an inductor for filtering the output of a rectifier is shown in Figure 12-230. Note that in this network the inductor L1 is in series with the load R1.

The inductance L1 is selected to offer high impedance to the AC ripple voltage and low impedance to the DC component. The result is a very large voltage drop across the inductor and a very small voltage drop across the load R 1. For the DC component, however, a very small voltage drop occurs across the inductor and a very large voltage drop across the load. The effect of an inductor on the output of a full-wave rectifier in the output waveshape is shown in Figure 12-231.

### Common Filter Configurations

Capacitors and inductors are combined in various ways to provide more satisfactory filtering than can be obtained with a single capacitor or inductor. These are referred to collectively as LC filters. Several combinations are shown schematically in Figure 12-232. Note that the L, or inverted L-type, and the T-type filter sections resemble schematically the corresponding letters of the alphabet. The pi-type filter section resembles the Greek letter pi (π) schematically.

All the filter sections shown are similar in that the inductances are in series and the capacitances are in parallel with the load. The inductances must, therefore, offer very high impedance and the capacitors very low impedance to the ripple frequency. Since the ripple frequency is comparatively low, the inductances are iron core coils having large values of inductance (several henries). Because they offer such high impedance to the ripple frequency, these coils are called chokes. The capacitors must also be large (several microfarads) to offer very little opposition to the ripple frequency. Because the voltage across the capacitor is DC, electrolytic capacitors are frequently used as filter capacitors. Always observe the correct polarity in connecting electrolytic capacitors.

LC filters are also classified according to the position of the capacitor and inductor. A capacitor input filter is one in which the capacitor is connected directly across the output terminals of the rectifier. A choke input filter is one in which a choke precedes the filter capacitor.

If it is necessary to increase the applied voltage to more than a single rectifier can tolerate, the usual solution is to stack them. These rectifiers are similar to resistors added in series. Each resistor drops a portion of the applied voltage rather than the total voltage. The same theory applies to rectifiers added in series or stacked. Series stacking increases the voltage rating. If, for example, a rectifier is destroyed with an applied voltage exceeding 50 volts, and it is to be used in a circuit with an applied voltage of 150 volts, stacking of diodes can be employed. The result is shown in Figure 12-233.

### Basic LC Filters

Analog filters are circuits that perform signal processing functions, specifically intended to remove unwanted signal components, such as ripple, and enhance desired signals. The simplest analog filters are based on combinations of inductors and capacitors. The four basic categories of filters discussed are: low-pass, high-pass, band-pass and band-stop. All these types are collectively known as passive filters, because they do not depend on any external power source.

The operation of a filter relies on the characteristic of variable inductive and capacitive reactance based on the applied frequency. In review, the inductor blocks high-frequency signals (high reactance) and conducts low-frequency signals (low reactance), while capacitors do the reverse. A filter in which the signal passes through an inductor, or in which a capacitor provides a path to earth, presents less attenuation (reduction) to a low-frequency signal than to a high-frequency signal and is considered a low-pass filter. If the signal passes through a capacitor, or has a path to ground through an inductor, then the filter presents less attenuation to high-frequency signals than low-frequency signals and is then considered a high-pass filter. Typically after an AC signal is rectified, the pulses of voltage are changed to usable form of DC by way of filtering.

#### Low-Pass Filter

A low-pass filter is a filter that passes low frequencies well, but attenuates (reduces) higher frequencies. The so-called cutoff frequency divides the range of frequencies that are passed and the range of frequencies that are stopped. In other words, the frequency components higher than the cutoff frequency are stopped by a low-pass filter. The actual amount of attenuation for each frequency varies by filter design.

An inductive low-pass filter inserts an inductor in series with the load, where a capacitive low-pass filter inserts a resistor in series and a capacitor in parallel with the load. The former filter design tries to block the unwanted frequency signal while the latter tries to short it out. Figure 12-234 illustrates this type of circuit and the frequency/current flow response.

#### High-Pass Filter (HPF)

A high-pass filter (HPF) is a filter that passes high frequencies well, but attenuates (reduces) frequencies lower than the cutoff frequency. The actual amount of attenuation for each frequency varies once again depending on filter design. In some cases, it is called a low-cut filter. A HPF is essentially the opposite of a low-pass filter.

It is useful as a filter to block any unwanted low frequency components of a signal while passing the desired higher frequencies. Figure 12-235 illustrates this type of circuit and the frequency/current flow response.

#### Band-Pass Filter

A band-pass filter is basically a combination of a high- pass and a low-pass. There are some applications where a particular range of frequencies need to be singled out or filtered from a wider range of frequencies. Band-pass filter circuits are designed to accomplish this task by combining the properties of low-pass and high-pass into a single filter. Figure 12-236 illustrates this type of circuit and the frequency/current flow response.

#### Band-Stop Filter

In signal processing, a band-stop filter or band-rejection filter is a filter that passes most frequencies unaltered, but attenuates those in a range to very low levels. It is the opposite of a band- pass filter. A notch filter is a band-stop filter with a narrow stopband (high Q factor). Notch filters are used in live sound reproduction (public address (PA) systems) and in instrument DC C1 R1 AC input Rectifier Voltage across C1 withlarge load circuit Voltage across C1 withsmall load circuit L1 R1 AC input Rectifier Load capacitor filter.

amplifier (especially amplifiers or preamplifiers for acoustic instruments, such as acoustic guitar, mandolin, bass instrument amplifier, etc.) to reduce or prevent feedback, while having little noticeable effect on the rest of the frequency spectrum. Other names include “band limit filter,” “T-notch filter,” “band- elimination filter,” and “band-rejection filter.”

Typically, the width of the stop-band is less than 1 to 2 decades (that is, the highest frequency attenuated is less than 10 to 100 times the lowest frequency attenuated). In the audio band, a notch filter uses high and low frequencies that may be only semitones apart.

A band-stop filter is the general case. A notch filter is a specific type of band-stop filter with a very narrow range. Also called band-elimination, band-reject, or notch filters, this kind of filter passes all frequencies above and below a particular range set by the component values. Not surprisingly, it can be made out of a low-pass and a high-pass filter, just like the band-pass design, except that this time we connect the two filter sections in parallel with each other instead of in series. Figure 12-237 illustrates this type of circuit and the frequency/current flow response.

## 2. 中文翻译

<!-- TODO: 逐段翻译，段数与上面严格一一对应（28 段）。专业术语按行业惯例，数字与缩写保留。 -->

## 3. 专业词汇

<!-- TODO: 用表格 | 英文 | 词性 | 中文 | 本节语境 |，4~8 行。优先选下面 Glossary 里的词（本节原文出现过的）：
- Capacitance (C) —— The property of an electric conductor that characterizes its ability to store an electric charge.
- Capacitive reactance (X c) —— The measure of a capacitor’s opposition to alternating current.
- Capacitor —— An electrical component that stores an electric charge.
- Current —— The flow of electrical charge.
- Electrostatic field —— A field of force that exists around a charged body.
- Energy —— The capacity of a physical system to perform work. There are two types of energy, kinetic and potential.
- Frequency —— The number of cycles (on/off) completed per unit of time. Usually expressed in Hertz.
- Inductance —— The ability of a coil or conductor to oppose a change in current flow.
-->

## 4. 语法解析

<!-- TODO: 2~4 个语法点，格式：
### ① 语法点名称
**原句**：<必须逐字来自第 1 节原文>
**拆解**：主/谓/宾、从句、非谓语等成分分析
**要点**：为什么这样用、易错点、可迁移的搭配
-->
