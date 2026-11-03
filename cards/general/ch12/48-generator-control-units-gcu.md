# Generator Control Units (GCU)

> 通用 Ch 12 · Generator Control Units (GCU) · 原文 PDF 第 606 页

## 1. 原文

### Basic Functions of a Generator Control Unit (GCU)

The generator control unit (GCU) is more commonly found on turbine power aircraft. The most basic GCU perform a number of functions related to the regulation, sensing, and protection of the DC generation system.

### Voltage Regulation

The most basic of the GCU functions is that of voltage regulation. Regulation of any kind requires the regulation unit to take a sample of an output and to compare that sample with a controlled reference. If the sample taken falls outside of the limits set by the reference, then the regulation unit must provide an adjustment to the unit generating the output so as to diminish or increase the output levels. In the case of the GCU, the output voltage from a generator is sensed by the GCU and compared to a reference voltage. If there is any difference between the two, the error is usually amplified and then sent back to the field excitation control portion of the circuit. The field excitation control then makes voltage⁄excitation adjustments in the field winding of the generator in order to bring the output voltage back into required bus tolerances.

### Overvoltage Protection

Like the voltage regulation feature of the GCU, the overvoltage protection system compares the sampled voltage to reference voltage. The output of the overvoltage protection circuit is used to open the relay that controls the output for the field excitation. These types of faults can occur for a number of reasons. The most common, however, is the failure of the voltage regulation circuit in the GCU.

### Parallel Generator Operations

The paralleling feature of the GCU allows for two or more GCU/generator systems to work in a shared effort to provide current to the aircraft electrical system. Comparing voltages between the equalizer bus and the interpole/compensator voltage, and amplifying the differences accomplishes the control of this system. The difference is then sent to the voltage regulation circuit, where adjustments are then made in the regulation output. These adjustments continue until all of the busses are equalized in their load sharing.

### Over-Excitation Protection

When a GCU in a paralleled system fails, a situation can occur where one of the generators becomes overexcited and tries to carry more than its share of the load, if not all of the loads. When this condition is sensed on the equalizing bus, the faulted generation control system shuts down by receiving a de-excitation signal. This signal is then transmitted to the overvoltage circuit, and then opens the field excitation output circuit.

### Differential Voltage

When the GCU allows the logic output to close the generator line contactor, the generator voltage must be within a close tolerance of the load bus. If the output is not within the specified tolerance, then the contactor is not allowed to connect the generator to the bus.

### Reverse Current Sensing

If the generator is unable to maintain the required voltage level, it eventually begins to draw current instead of providing it. In this case, the faulty generator is seen as a load to the other generators and will need to be removed from the bus. Once the generator is off-line, it is not permitted to be reconnected to the bus until such time that the generator faults are cleared and the generator is capable of providing a current to the bus. In most cases, the differential voltage circuit and the reverse current sensing circuit are one in the same.

## 2. 中文翻译

### 发电机控制组件（GCU）的基本功能

发电机控制组件（GCU）更常见于涡轮动力飞机。最基本的 GCU 执行与直流发电系统的调节、检测和保护有关的若干功能。

### 电压调节

GCU 最基本的功能是电压调节。任何形式的调节都要求调节单元取输出样本，并把该样本与受控基准进行比较。如果所取样本超出基准设定的限值，调节单元就必须对产生输出的单元进行调节，以减小或增大输出水平。就 GCU 而言，发电机的输出电压由 GCU 检测并与基准电压比较。如果两者之间存在任何差异，该误差通常被放大，然后送回电路的励磁控制部分。励磁控制随后对发电机励磁绕组进行电压/励磁调节，使输出电压回到所需的汇流条容差范围内。

### 过压保护

与 GCU 的电压调节功能类似，过压保护系统把取样电压与基准电压进行比较。过压保护电路的输出用于断开控制励磁输出的继电器。这类故障可能因多种原因发生。然而最常见的是 GCU 内电压调节电路的失效。

### 并联发电机运行

GCU 的并联功能使两套或更多 GCU/发电机系统协同工作，向飞机电气系统提供电流。通过比较均衡汇流条与极间/补偿绕组电压之间的差值，并对差值进行放大，实现对该系统的控制。差值随后送往电压调节电路，在调节输出中作出调整。这些调整持续进行，直到所有汇流条在负载分配上达到均衡。

### 过励磁保护

当并联系统中的某台 GCU 失效时，可能出现一台发电机过励磁并试图承担超过其应分担份额（甚至全部）负载的情况。当在均衡汇流条上检测到这一状态时，故障的发电控制系统通过接收去励磁信号而关断。该信号随后被送往过压电路，进而断开励磁输出电路。

### 电压差

当 GCU 允许逻辑输出闭合发电机线路接触器时，发电机电压必须处于负载汇流条的严格容差范围内。如果输出不在规定容差内，则不允许该接触器把发电机接到汇流条上。

### 逆流检测

如果发电机无法维持所需电压水平，它最终会开始吸取电流而不是提供电流。在这种情况下，故障发电机被视为其他发电机的负载，需要从汇流条上切除。发电机一旦离线，在故障被清除且发电机能够向汇流条提供电流之前，不允许重新接到汇流条上。在大多数情况下，电压差电路与逆流检测电路是同一个电路。

## 3. 专业词汇

| 英文 | 词性 | 中文 | 本节语境 |
| --- | --- | --- | --- |
| generator control unit (GCU) | n. | 发电机控制组件 | 对直流发电系统进行调节、检测和保护的控制组件 |
| voltage regulation | n. | 电压调节 | 取样端电压与基准比较后调节励磁，使电压回到容差内 |
| overvoltage protection | n. | 过压保护 | 比较取样电压与基准电压，断开励磁输出继电器 |
| field excitation | n. | 励磁 | 发电机磁场绕组的励磁电流及其控制电路 |
| equalizer bus | n. | 均衡汇流条 | 并联运行时用于比较各发电机负载分配的汇流条 |
| line contactor | n. | 线路接触器 | 把发电机接到负载汇流条上的主接触器 |
| reverse current | n. | 逆流 | 发电机电压不足时从汇流条反向流入发电机的电流 |
| tolerance | n. | 容差 | 允许的电压偏差范围，即上下允差之和 |
| over-excitation | n. | 过励磁 | 并联系统中某台发电机励磁过大、承担过多负载的状态 |
| de-excitation | n. | 去励磁 | 故障时切除励磁输出的信号与动作 |
| load sharing | n. | 负载分配 | 并联发电机之间按比例分担负载 |
| reference voltage | n. | 基准电压 | 调节与保护电路比较用的受控基准 |

## 4. 语法解析

### ① that of 替代前文名词
**原句**：The most basic of the GCU functions is that of voltage regulation.
**拆解**：主语 The most basic of the GCU functions；is 后 that 为指示代词，替代前文出现的 function，of voltage regulation 作后置修饰。
**要点**：that of 用于避免重复单数名词，复数用 those of；不能写成 the one of。

### ② 过去分词短语作后置定语
**原句**：If the sample taken falls outside of the limits set by the reference, then the regulation unit must provide an adjustment to the unit generating the output so as to diminish or increase the output levels.
**拆解**：taken 为过去分词后置修饰 sample；set by the reference 修饰 limits；generating the output 为现在分词短语修饰 unit；so as to 引导目的状语。
**要点**：单个分词短语作定语须后置；so as to 表目的，其逻辑主语应与主句主语一致。

### ③ require sb. to do 与并列不定式
**原句**：Regulation of any kind requires the regulation unit to take a sample of an output and to compare that sample with a controlled reference.
**拆解**：主语 Regulation of any kind；谓语 requires；宾语 the regulation unit；宾补为并列不定式 to take… and to compare…。
**要点**：require 后接名词 + 不定式作宾补；并列不定式第二个 to 保留，结构更清晰。

### ④ once 与 not…until such time that
**原句**：Once the generator is off-line, it is not permitted to be reconnected to the bus until such time that the generator faults are cleared and the generator is capable of providing a current to the bus.
**拆解**：Once 引导时间状语从句；主句为被动结构 is not permitted to be reconnected；until such time that 引导时间状语从句，从句内两个并列分句由 and 连接。
**要点**：be permitted to do 表示“被允许做”；not…until 强调“直到……才”，such time that 为其书面变体。

### ⑤ where 引导的定语从句
**原句**：When a GCU in a paralleled system fails, a situation can occur where one of the generators becomes overexcited and tries to carry more than its share of the load, if not all of the loads.
**拆解**：When 引导时间状语从句；主句 a situation can occur；where 引导定语从句修饰 situation；if not all of the loads 为插入的让步性补充。
**要点**：抽象地点名词（situation、case、point）后常用 where 引导定语从句；if not 意为“即使不是”。

### ⑥ 动名词并列作主语
**原句**：Comparing voltages between the equalizer bus and the interpole/compensator voltage, and amplifying the differences accomplishes the control of this system.
**拆解**：Comparing… 与 amplifying… 两个动名词短语由 and 并列作主语，谓语为单数 accomplishes。
**要点**：动名词短语作主语视为单数；长主语后谓语仍用第三人称单数，勿被靠近的复数名词 differences 干扰。
