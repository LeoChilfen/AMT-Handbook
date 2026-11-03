# Generator Control Units (GCU)

> 通用 Ch 12 · Generator Control Units (GCU) · 原文 PDF 第 606 页

## 1. 原文

### Basic Functions of a Generator Control Unit (GCU)

The generator control unit (GCU) is more commonly found on turbine power aircraft. The most basic GCU perform a number of functions related to the regulation, sensing, and protection of the DC generation system. [Figure 12-332]

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

<!-- TODO: 逐段翻译，段数与上面严格一一对应（14 段）。专业术语按行业惯例，数字与缩写保留。 -->

## 3. 专业词汇

<!-- TODO: 用表格 | 英文 | 词性 | 中文 | 本节语境 |，4~8 行。优先选下面 Glossary 里的词（本节原文出现过的）：
- Current —— The flow of electrical charge.
- Difference —— The answer to a subtraction problem.
- Power (exponent) —— A shorthand method of indicating how many times a number, called the base, is multiplied by itself. For example, in the number 43, 3 is the power, or exponent, 
- Power —— Power is the time rate at which work is done or energy is transferred.
- Tolerance —— The sum of the plus and minus allowance figures.
-->

## 4. 语法解析

<!-- TODO: 2~4 个语法点，格式：
### ① 语法点名称
**原句**：<必须逐字来自第 1 节原文>
**拆解**：主/谓/宾、从句、非谓语等成分分析
**要点**：为什么这样用、易错点、可迁移的搭配
-->
