# Inverters

> 通用 Ch 12 · Inverters · 原文 PDF 第 535 页

## 1. 原文

An inverter is used in some aircraft systems to convert a portion of the aircraft’s DC power to AC. This AC is used mainly for instruments, radio, radar, lighting, and other accessories. These inverters are usually built to supply current at a frequency of 400 cps, but some are designed to provide more than one voltage; for example, 26 volt AC in one winding and 115 volts in another.

There are two basic types of inverters: the rotary and the static. Either type can be single-phase or multiphase. The multiphase inverter is lighter for the same power rating than the single-phase, but there are complications in distributing multiphase power and in keeping the loads balanced.

### Rotary Inverters

There are many sizes, types, and configurations of rotary inverters. Such inverters are essentially AC generators and DC motors in one housing. The generator field, or armature, and the motor field, or armature, are mounted on a common shaft that rotates within the housing. One common type of rotary inverter is the permanent magnet inverter.

### Permanent Magnet Rotary Inverter

A permanent magnet inverter is composed of a DC motor and a permanent magnet AC generator assembly. Each has a separate stator mounted within a common housing. The motor armature is mounted on a rotor and connected to the DC supply through a commutator and brush assembly. The motor field windings are mounted on the housing and connected directly to the DC supply. A permanent magnet rotor is mounted at the opposite end of the same shaft as the motor armature, and the stator windings are mounted on the housing, allowing AC to be taken from the inverter without the use of brushes. The generator rotor has six poles, magnetized to provide alternate North and South poles about its circumference.

When the motor field and armature are excited, the rotor begins to turn. As the rotor turns, the permanent magnet rotates within the AC stator coils, and the magnetic flux developed by the permanent magnets are cut by the conductors in the AC stator coils. An AC voltage is produced in the windings whose polarity changes as each pole passes the windings.

This type inverter may be made multiphase by placing more AC stator coils in the housing in order to shift the phase the proper amount in each coil.

As the name of the rotary inverter indicates, it has a revolving armature in the AC generator section.

The DC motor in this inverter is a four pole, compound wound motor. The four field coils consist of many turns of fine wire, with a few turns of heavy wire placed on top. The fine wire is the shunt field, connected to the DC source through a filter and to ground through a centrifugal governor. The heavy wire is the series field, which is connected in series with the motor armature. The centrifugal governor controls the speed by shunting a resistor that is in series with the shunt field when the motor reaches a certain speed.

The alternator is a three-phase, four-pole, star-connected AC generator. The DC input is supplied to the generator field coils and connected to ground through a voltage regulator. The output is taken off the armature through three slip rings to provide three-phase power. The inverter would be a single-phase inverter if it had a single armature winding and one slip ring. The frequency of this type unit is determined by the speed of the motor and the number of generator poles.

### Inductor-Type Rotary Inverter

Inductor-type inverters use a rotor made of soft iron laminations with grooves cut laterally across the surface to provide poles that correspond to the number of stator poles. The field coils are wound on one set of stationary poles and the AC armature coils on the other set of stationary poles. When DC is applied to the field coils, a magnetic field is produced. The rotor turns within the field coils and, as the poles on the rotor align with the stationary poles, a low reluctance path for flux is established from the field pole through the rotor poles to the AC armature pole and through the housing back to the field pole. In this circumstance, there is a large amount of magnetic flux linking the AC coils.

When the rotor poles are between the stationary poles, there is a high reluctance path for flux, consisting mainly of air; then, there is a small amount of magnetic flux linking the AC coils. This increase and decrease in flux density in the stator induces an alternating current in the AC coils.

The number of poles and the speed of the motor determine the frequency of this type of inverter. The DC stator field current controls the voltage.

The figure is a simplified diagram of a typical aircraft AC power distribution system, utilizing a main and a standby rotary inverter system.

### Static Inverters

In many applications where continuous DC voltage must be converted to alternating voltage, static inverters are used in place of rotary inverters or motor generator sets. The rapid progress made by the semiconductor industry is extending the range of applications of such equipment into voltage and power ranges that would have been impractical a few years ago. Some such applications are power supplies for frequency sensitive military and commercial AC equipment, aircraft emergency AC systems, and conversion of wide frequency range power to precise frequency power. The use of static inverters in small aircraft also has increased rapidly in the last few years, and the technology has advanced to the point that static inverters are available for any requirement filled by rotary inverters. For example, 250 V A emergency AC supplies operated from aircraft batteries are in production, as are 2,500 V A main AC supplies operated from a varying frequency generator supply. This type of equipment has certain advantages for aircraft applications, particularly the absence of moving parts and the adaptability to conduction cooling.

Static inverters, referred to as solid-state inverters, are manufactured in a wide range of types and models that can be classified by the shape of the AC output waveform and the power output capabilities. One of the most commonly used static inverters produces a regulated sine wave output. This inverter converts a low DC voltage into higher AC voltage. The AC output voltage is held to a very small voltage tolerance, a typical variation of less than 1 percent with a full input load change. Output taps are normally provided to permit selection of various voltages; for example, taps may be provided for 105, 115, and 125 volt AC outputs. Frequency regulation is typically within a range of one cycle for a 0–100 percent load change. Variations of this type of static inverter are available, many of which provide a square wave output.

Since static inverters use solid-state components, they are considerably smaller, more compact, and much lighter in weight than rotary inverters. Depending on the output power rating required, static inverters that are no larger than a typical airspeed indicator can be used in aircraft systems. Some of the features of static inverters are:

1. High efficiency

2. Low maintenance, long life

3. No warmup period required

4. Capable of starting under load

5. Extremely quiet operation

6. Fast response to load changes Static inverters are commonly used to provide power for such frequency sensitive instruments as the attitude gyro and directional gyro. They also provide power for autosyn and magnesyn indicators and transmitters, rate gyros, radar, and other airborne applications.

## 2. 中文翻译

逆变器用于某些飞机系统，把飞机直流电的一部分转换为交流电。这种交流电主要用于仪表、无线电、雷达、照明及其他附件。这些逆变器通常制造成以 400 cps 的频率供电，但有些设计成能提供一种以上电压；例如，一个绕组输出 26 V 交流，另一个绕组输出 115 V。

逆变器有两种基本类型：旋转式和静止式。两种类型都可以是单相或多相。在相同额定功率下，多相逆变器比单相逆变器轻，但在分配多相功率和保持负载平衡方面存在一些复杂问题。

### 旋转式逆变器

旋转式逆变器有许多尺寸、类型和结构形式。这类逆变器实质上是把交流发电机和直流电动机装在同一壳体内。发电机的励磁绕组（或电枢）与电动机的励磁绕组（或电枢）装在同一根轴上，该轴在壳体内旋转。一种常见的旋转式逆变器是永磁式逆变器。

### 永磁旋转式逆变器

永磁式逆变器由一个直流电动机和一个永磁式交流发电机组件构成。两者各有一个独立的定子，装在同一个壳体内。电动机电枢装在转子上，通过换向器和电刷组件与直流电源相连。电动机励磁绕组装在壳体上，直接与直流电源相连。永磁转子装在电动机电枢同一根轴的另一端，定子绕组装在壳体上，因此可以在不使用电刷的情况下从逆变器取出交流电。发电机转子有六个磁极，沿其圆周交替磁化为 N 极和 S 极。

当电动机的励磁绕组和电枢通电时，转子开始转动。转子转动的过程中，永磁体在交流定子线圈内旋转，永磁体产生的磁通被交流定子线圈中的导体切割。绕组中便产生交流电压，其极性随着每个磁极经过绕组而变化。

这种逆变器可以通过在壳体内增加交流定子线圈、使每个线圈中的相位移动适当的量，而做成多相。

正如旋转式逆变器这一名称所示，它在交流发电机部分有一个旋转的电枢。

这种逆变器中的直流电动机是一台四极复励电动机。四个励磁线圈由许多匝细导线组成，上面绕有几匝粗导线。细导线是并励绕组，通过一个滤波器接到直流电源，并通过离心调节器接地。粗导线是串励绕组，与电动机电枢串联。离心调节器在电动机达到某一转速时，把与并励绕组串联的一个电阻短路，以此控制转速。

该交流发电机是一台三相、四极、星形连接的交流发电机。直流输入送到发电机的励磁线圈，并通过一个电压调节器接地。输出通过三个滑环从电枢上取出，以提供三相电源。如果只有一组电枢绕组和一个滑环，该逆变器就会是单相逆变器。这种机组的频率由电动机转速和发电机磁极数决定。

### 电感式旋转式逆变器

电感式逆变器使用由软铁叠片制成的转子，其表面横向切出若干槽，以形成与定子磁极数相对应的磁极。励磁线圈绕在一组固定磁极上，交流电枢线圈绕在另一组固定磁极上。当直流电加到励磁线圈上时，就产生磁场。转子在励磁线圈内旋转，当转子上的磁极与固定磁极对齐时，就建立起一条从励磁磁极经转子磁极到交流电枢磁极、再经壳体回到励磁磁极的低磁阻磁通路径。在这种情况下，有大量磁通链过交流线圈。

当转子磁极处于固定磁极之间时，磁通路径的磁阻很高，主要由空气构成；此时只有少量磁通链过交流线圈。定子中磁通密度的这种增减在交流线圈中感应出交流电。

磁极数和电动机转速决定这种逆变器的频率。直流定子励磁电流则控制电压。

是一幅典型飞机交流电源配电系统的简化图，该系统采用一台主用和一台备用旋转式逆变器。

### 静止式逆变器

在许多需要把连续直流电压转换为交流电压的应用中，都使用静止式逆变器代替旋转式逆变器或电动发电机组。半导体工业的迅速发展正把此类设备的应用范围扩展到几年前还很不现实的电压和功率范围。此类应用包括：为对频率敏感的军用和商用交流设备供电的电源、飞机应急交流系统，以及把宽频范围的电源转换为精确频率电源。近几年来，静止式逆变器在小型飞机上的使用也迅速增加，技术已进步到静止式逆变器可以满足原先由旋转式逆变器承担的任何要求。例如，由飞机蓄电池供电的 250 V A 应急交流电源已投入生产，由变频发电机电源供电的 2,500 V A 主交流电源也是如此。这类设备在飞机应用上具有某些优点，特别是没有运动部件，并且易于采用传导冷却。

静止式逆变器又称固态逆变器，其类型和型号繁多，可按交流输出波形的形状和输出功率能力分类。最常用的一种静止式逆变器产生经调节的正弦波输出。这种逆变器把低直流电压转换为较高的交流电压。交流输出电压保持在很小的电压容差范围内，在输入负载全变时典型变化小于 1%。通常设有输出抽头，以便选择各种电压；例如，可为 105、115 和 125 V 交流输出设置抽头。在负载变化 0–100% 时，频率调节典型地在一个周期的范围内。这类静止式逆变器还有多种变型，其中许多提供方波输出。

由于静止式逆变器使用固态元件，它们比旋转式逆变器小得多、紧凑得多，重量也轻得多。视所需的输出功率额定值而定，尺寸不大于典型空速表的静止式逆变器即可用于飞机系统。静止式逆变器的部分特点是：

1. 效率高

2. 维护量小、寿命长

3. 无需预热时间

4. 能在带载情况下启动

5. 运行极为安静

6. 对负载变化响应快 静止式逆变器通常用于为姿态陀螺仪和航向陀螺仪等对频率敏感的仪表供电。它们也为自整角（autosyn）和磁同步（magnesyn）指示器与传感器、速率陀螺、雷达及其他机载应用供电。

## 3. 专业词汇

| 英文 | 词性 | 中文 | 本节语境 |
| --- | --- | --- | --- |
| inverter | n. | 逆变器 | 本节主题：把飞机直流电的一部分转换为交流电 |
| rotary inverter | n. | 旋转式逆变器 | 由直流电动机与交流发电机构成、装在同一壳体内的逆变器 |
| static inverter | n. | 静止式逆变器 | 又称固态逆变器，用半导体器件把直流变换为交流，无运动部件 |
| permanent magnet | n. | 永磁体 | 永磁式逆变器中提供励磁磁场的转子部件 |
| armature | n. | 电枢 | 电动机与发电机中产生感应电动势或在磁场中受力的转动部分 |
| commutator | n. | 换向器 | 与电刷组件配合，把直流电引入电动机转子 |
| brush | n. | 电刷 | 与换向器或滑环滑动接触的导电部件，永磁转子结构可省去 |
| slip ring | n. | 滑环 | 把旋转电枢的三相输出引到外电路 |
| stator | n. | 定子 | 装在壳体上的静止部分，其上绕有励磁或电枢绕组 |
| field winding | n. | 励磁绕组 | 建立主磁场的线圈；文中分并励（细线）与串励（粗线） |
| reluctance | n. | 磁阻 | 磁通路径的阻力，转子磁极对齐时磁阻低、磁通多 |
| solid-state | adj. | 固态的 | 用半导体器件代替运动部件，故体积小、重量轻 |

## 4. 语法解析

### ① where 引导定语从句 + 情态动词被动语态
**原句**：In many applications where continuous DC voltage must be converted to alternating voltage, static inverters are used in place of rotary inverters or motor generator sets.
**拆解**：In many applications 为状语，where 引导定语从句修饰 applications（主语 continuous DC voltage，谓语 must be converted，状语 to alternating voltage）；主句主语 static inverters，谓语 are used（被动），in place of … 为介词短语作方式状语。
**要点**：where 在此等于 in which，用来说明「场合、应用」，不是表地点的疑问副词，翻译时译为「在……的应用中」；must be converted 为情态动词的被动式，因为转换对象作从句主语；in place of 是「代替」，后接名词，不能写成 instead 单独使用（instead 是副词）。

### ② 比较级 + for 短语限定范围 + there be 句型
**原句**：The multiphase inverter is lighter for the same power rating than the single-phase, but there are complications in distributing multiphase power and in keeping the loads balanced.
**拆解**：前一分句主语 The multiphase inverter，系动词 is，表语 lighter，for the same power rating 限定比较的前提，than the single-phase 为比较状语（the single-phase 后省略 inverter）；but 连接后一分句 there are complications，in distributing … and in keeping … 为两个并列介词短语作后置定语/方面状语。
**要点**：比较级前用 for + 名词短语表示「就同一额定功率而言」，使比较条件明确；than 后的名词可承前省略重复部分；there be 结构后接两个并列的动名词短语，介词 in 必须重复出现，不可省略为 in distributing … and keeping …。

### ③ 现在分词短语作结果状语 + 被动不定式
**原句**：A permanent magnet rotor is mounted at the opposite end of the same shaft as the motor armature, and the stator windings are mounted on the housing, allowing AC to be taken from the inverter without the use of brushes.
**拆解**：and 连接两个被动分句；第二个分句主语 the stator windings，谓语 are mounted；逗号后 allowing AC to be taken from the inverter without the use of brushes 为现在分词短语作结果状语，其中 to be taken 为不定式被动，作 allow 的宾语补足语。
**要点**：allowing 的逻辑主语是前面整个「定子绕组装在壳体上」这一事实，而非某一个名词，因此可译作「从而可以……」；allow 的宾语补足语用不定式被动 to be taken，表示交流电「被取出」；without the use of 是名词化表达，比 without using 更正式，技术文本常用。

### ④ such … as 表示列举
**原句**：Static inverters are commonly used to provide power for such frequency sensitive instruments as the attitude gyro and directional gyro.
**拆解**：主句 Static inverters are commonly used（被动）to provide power for … instruments（不定式作目的状语）；for 的宾语 instruments 被 such … as 结构修饰，as 后 the attitude gyro and directional gyro 为列举，as 是关系代词性质，不是比较。
**要点**：such + 名词 + as + 列举项 相当于「诸如……之类的」，不能用 like 代替 such as 中的 as；列举项须与前面的名词同类，如仅举一例则用 such as 后接单项；此处 frequency sensitive 为复合形容词，意为「对频率敏感的」，修饰 instruments。

### ⑤ 过去分词并列作后置定语 + 比较结构
**原句**：Since static inverters use solid-state components, they are considerably smaller, more compact, and much lighter in weight than rotary inverters.
**拆解**：Since 引导原因状语从句（主语 static inverters，谓语 use，宾语 solid-state components）；主句主语 they（指静止式逆变器），系动词 are，三个并列的比较级表语 considerably smaller、more compact、much lighter in weight，than rotary inverters 为比较状语。
**要点**：considerably、much 均可修饰比较级且位置在比较级之前，不能换成 very；三个比较级并列时只在最后一个前加 and，前面用逗号分隔；lighter in weight 中 in weight 是限定比较方面的介词短语，与 lighter 构成「在某方面更轻」的固定搭配。
