# Logic Circuits

> 通用 Ch 12 · Logic Circuits · 原文 PDF 第 561 页

## 1. 原文

Logic is considered the science of reasoning—the development of a reasonable conclusion based on known information. Human reasoning tells us that certain propositions are true if certain conditions or premises are true. An annunciator being lit in the master warning panel is an example of a proposition, which is either true or false. For example, predetermined and designed conditions must be met in order for an annunciator in a master warning panel to be lit. A “LOW HYDRAULIC PRESS” annunciator may have a simple set of conditions that cause it to be illuminated. If the conditions are met, such as a hydraulic reservoir that is low on fluid causing the line press to be low, then the logic is true and the annunciator lights. Several propositions, when combined, form a logical function. In the example above, the “LOW HYDRAULIC PRESS” annunciator is on if the LED is not burned out and the hydraulic press is low or if the LED is not burned out and the annunciator test is being asserted.

This section on logic circuits only serves as an introduction to the basic concepts. The technician encounters many Inputs Power supply requirements Output +VCC −VEE +VCC −VEE − + Inputs Output − + Inputs Output − + Input/output requirements Feedback situations or problems in everyday life that can be expressed in some form of a logical function. Many problems and situations can be condensed down to simple yes⁄no or true⁄false statements that, if logically ordered, can filter a problem down to a reasonable answer. The digital logic circuits are well suited for this task and have been employed in today’s integrated circuits found in virtually all of the devices that we take for granted in modern aircraft. These logical circuits are used to carry out the logical functions for such things as navigation and communications. There are several fundamental elements that form the building blocks of the complex digital systems found in line replaceable units (LRUs) and avionics card cages. The following is a very basic outline of what those elements are and what logic conditions they process. It is far beyond the scope of this handbook to cover digital logic systems due to the vast body of knowledge that it represents. However, this serves as an introduction and, in some limited cases, is useful in reading system block diagrams that use logic symbols to aid the technician in understanding how a given circuit operates.

Electrical pulses can represent two logic conditions and any two differing voltages can be used for this purpose. For example, a positive voltage pulse could represent a true or 1 condition and a negative voltage pulse could then represent a false or 0 logic condition. The condition in which the voltage changes to represent a true or 1 logic is known as the logic polarity. Logic circuits are usually divided into two broad classes: positive polarity and negative polarity. The voltage levels used and a statement indicating the use of positive or negative logic is usually specified in the logic diagrams provided by the original equipment manufacturers (OEMs).

When a signal that activates a circuit to a 1, true or high condition, has an electrical level that is relatively more positive than the other 0 or false condition, then the logic polarity is said to be positive. An example would be:

Active State: 1 or True = +5 volts direct current (VDC)

When the signal that actives a circuit to a 1, true or high condition, has an electrical level that is relatively more negative than the other 0 or false condition, then the logic polarity is said to be negative. An example would be:

Active State: 1 or True = 0 VDC 0 or False = +5 VDC

Figure 12-251 illustrates the positive and negative pulse in an idealized form. In both forms, the pulse is composed of two edges—one being the leading edge and the other the trailing edge. In the case of the positive pulse logic, the positive transition from a lower state to a higher state is the leading edge and the trailing edge is the opposite. In the case of the negative logic pulse, the negative transition from a higher state to a lower state is the leading edge while the rise from the lower state back to the higher state is the trailing edge.

Figure 12-251 is considered an ideal pulse because the rise and fall times are instantaneous. In reality, these changes take time, although in actual practice, the rise and fall can be assumed as instantaneous. Figure 12-252 shows the non- ideal pulse and its characteristics. The time required for a pulse to go from a low state to a high state is called the rise AC input AC output DC A B C Load AC input DC Load AC DC time, and the time required for the pulse to return to zero is called the fall time. It is common practice to measure the rise and fall time between 10 percent amplitude and 90 percent amplitude. The reason for taking the measurements in these points is due to the non-linear shape of the pulse in the first 10 percent and final 90 percent of the rise and fall amplitudes. The pulse width is defined as the duration of the pulse. To be more specific, it is the time between the 50 percent amplitude point on both the pulse rise and fall.

### Basic Logic Circuits

Boolean logic is a symbolic system used in representing the truth value of statements. It is employed in the binary system used by digital computers primarily because the only truth values (true and false) can be represented by the binary digits 1 and 0. A circuit in computer memory can be open or closed, depending on the value assigned to it. The fundamental operations of Boolean logic, often called Boolean operators, are “and,” “or,” and “not;” combinations of these make up 13 other Boolean operators. Six of these operators are discussed.

#### The Inverter Logic

The inverter circuit performs a basic logic function called inversion. The purpose of the inverter is to convert one logic state into the opposite state. In terms of a binary digit, this would be like converting a 1 to a 0 or a 0 to a 1. When a high voltage is applied to the inverter input, low voltage is the output. When a low voltage is applied to the input, a high voltage is on the output. This operation can be put into what is known as a logic or truth table. The standard logic symbol is shown in Figure 12-253. Figure 12-254 shows the possible logic states for this gate. This is the common symbol for an amplifier with a small circle on the output. This type of logic can also be considered a NOT gate.

The AND gate is made up of two or more inputs and a single output. The logic symbol is shown in Figure 12-255. Inputs are on the left and the output is on the right in each of the depictions. Gates with two, three, and four inputs are shown; however, any number of inputs can be used in the AND logic as long as the number is greater than one. The operation of the AND gate is such that the output is high only when all of the inputs are high. If any of the inputs are low, the output is also low. Therefore, the basic purpose of an AND gate is to determine when certain conditions have been met at the same time. A high level on all inputs produces a high level on the output. Figure 12-256 shows a simplified diagram of the AND logic with two switches and a light bulb. Notice that both switches need to be closed in order for the light bulb to turn on. Any other combination of switch positions is an open circuit and the light does not turn on. An example of AND logic could possibly be engage logic found in an autopilot. In this case, the autopilot would not be allowed to be engaged unless certain conditions are first met. Such conditions could be: Vertical gyro is valid AND directional gyro is valid AND all autopilot control knobs are in detents AND servo circuits are operational. Only when these conditions are met does the Load AC DC Ref DC Control autopilot engage. [Figure 12-257]

The OR gate has two or more inputs and one output and is normally represented by the standard logic symbol and truth table. [Figure 12-258] Note that the OR gate can have any number of inputs as long as it is greater than one. The operation of the OR gate is such that a high on any one of the inputs produces a high on the output. The only time that a low is produced on the output is if there are no high levels on any input. Figure 12-259 is a simplified circuit that illustrates the OR logic. The example used is a “DOOR UNSAFE” annunciator. Let’s say in this case that the plane has one cabin door and a baggage door. In order for the annunciator light on the master warning panel to extinguish, both doors must be closed and locked. If any one of the doors is not secured properly, the baggage door OR the cabin door, then the “DOOR UNSAFE” annunciator illuminates. In this case, two switches are in parallel with each other. If either one of the two switches is closed, the light bulb lights up. The lamp is off only when both switches are open.

The term NAND is a combination of the NOT-AND gate and indicates an AND function with an inverted output. A standard logic symbol for a two input NAND gate is shown in Figure 12-260. Notice that an equivalent AND gate with an inverter is also shown. The logical operation of the NAND gate is such that a low output occurs only if all inputs are high. If any of the inputs are low, the output is high. An example of a two input NAND gate and its corresponding truth table are shown in Figure 12-261.

The term NOR is a combination of the NOT and OR and indicates an OR function with an inverted output. The standard logic symbol for a two-inputs NOR gate is shown in Figure 12-263. Notice that an equivalent AND gate with an inverter is also shown. The logical operation of the NOR gate is such that a low output happens when any of its inputs are high. Only when all of its inputs are low is the output high. The logic of this gate produces resultant outputs that are the opposite of the OR gate. In the NOR gate, the low output is the active output level. Figure 12-263 illustrates the logical operation of a two-input NOR gate for all of its possible combinations and the truth table.

#### Exclusive OR Gate

The exclusive OR gate is a modified OR gate that produces a 1 output when only one of the inputs is a 1. The abbreviation often used is X-OR. It is different from the standard OR gate in that when both inputs are a 1, then the output remains at a 0. The standard symbol and truth table for the X-OR gate are shown in Figure 12-264.

#### Exclusive NOR Gate

The exclusive NOR (X-NOR) gate is nothing more than an X-OR gate with an inverted output. It produces a 1 output when all inputs are 1s and also when all inputs are 0s. The standard symbol is shown in Figure 12-265.

### The Integrated Circuit

All of the logic functions so far discussed plus many other components are available in some form of an integrated circuit. The digital systems found in today’s aircraft owe their existence to a large extent to the design of the integrated circuit (IC). In most cases, the IC has an advantage over the use of discrete components in that they are smaller, consume less power, are very reliable, and are inexpensive. The most noticeable characteristic of the IC is its size and in comparison to the discrete semiconductor component, can easily be on the order of thousands of times smaller. [Figure 12-266]\ A monolithic integrated circuit is an electronic circuit that is constructed entirely on a single chip or wafer of semiconductor material. All of the discrete components, such as resistors, transistors, diodes, and capacitors, can be constructed on these small pieces of semiconductor material and are an integral part of the chip. There are a number of levels of integration. Those levels are: small-scale integration, medium-scale integration, large- scale integration, and microprocessors. The small-scale integration is considered the least complex design of the digital ICs. These ICs contain the basic components, such as the AND, OR, NOT, NOR and NAND gates. [Figure 12-267] The medium-scale integration can contain High Leading edge Low Trailing edge Positive logic pulse Negative logic pulse Trailing edge High Leading edge Low Pulse width Pulse characteristic from a databus Rise time 50% 5 V Pulse amplitude (10 volts)

90% 9 V 10% 1 V Fall time Input = 1 (High)

A X X X B A B A B C C D Input Output High Low Low High the same components as found in the small-scale design but in larger numbers ranging from 12 to 100. The medium- scale designs are house circuits that are more complex, such as encoders, decoders, registers, counters, multiplexers, smaller memories, and arithmetic circuits. [Figure 12-268] The large-scale integrated circuits contain even more logic gates, larger memories than the medium-scale circuits, and in some cases microprocessors.

The microprocessor is a device that can be programmed to perform arithmetic and logical operations and other functions in a preordered sequence. The microprocessor is usually used as the central processing unit (CPU) in today’s computer systems when it is connected to other components, such as memory chips and input/output circuits. The basic arrangement and design of the circuits residing in the microprocessor is called the architecture.

## 2. 中文翻译

<!-- TODO: 逐段翻译，段数与上面严格一一对应（26 段）。专业术语按行业惯例，数字与缩写保留。 -->

## 3. 专业词汇

<!-- TODO: 用表格 | 英文 | 词性 | 中文 | 本节语境 |，4~8 行。优先选下面 Glossary 里的词（本节原文出现过的）：
- Block diagrams —— Used to show a simplified relationship of a more complex system of components.
- Current —— The flow of electrical charge.
- Direct current (DC) —— Electricity that flows in one direction at all times.
- Power (exponent) —— A shorthand method of indicating how many times a number, called the base, is multiplied by itself. For example, in the number 43, 3 is the power, or exponent, 
- Power —— Power is the time rate at which work is done or energy is transferred.
- Semiconductor —— Any device based on either preferred conduction through a solid in one direction, as in rectifiers, or on a variation in conduction characteristics through a pa
-->

## 4. 语法解析

<!-- TODO: 2~4 个语法点，格式：
### ① 语法点名称
**原句**：<必须逐字来自第 1 节原文>
**拆解**：主/谓/宾、从句、非谓语等成分分析
**要点**：为什么这样用、易错点、可迁移的搭配
-->
