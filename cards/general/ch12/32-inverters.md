# Inverters

> 通用 Ch 12 · Inverters · 原文 PDF 第 535 页

## 1. 原文

An inverter is used in some aircraft systems to convert a portion of the aircraft’s DC power to AC. This AC is used mainly for instruments, radio, radar, lighting, and other accessories. These inverters are usually built to supply current at a frequency of 400 cps, but some are designed to provide more than one voltage; for example, 26 volt AC in one winding and 115 volts in another.

There are two basic types of inverters: the rotary and the static. Either type can be single-phase or multiphase. The multiphase inverter is lighter for the same power rating than the single-phase, but there are complications in distributing multiphase power and in keeping the loads balanced.

### Rotary Inverters

There are many sizes, types, and configurations of rotary inverters. Such inverters are essentially AC generators and DC motors in one housing. The generator field, or armature, and the motor field, or armature, are mounted on a common shaft that rotates within the housing. One common type of rotary inverter is the permanent magnet inverter.

### Permanent Magnet Rotary Inverter

A permanent magnet inverter is composed of a DC motor and a permanent magnet AC generator assembly. Each has a separate stator mounted within a common housing. The motor armature is mounted on a rotor and connected to the DC supply through a commutator and brush assembly. The motor field windings are mounted on the housing and connected directly to the DC supply. A permanent magnet rotor is mounted at the opposite end of the same shaft as the motor armature, and the stator windings are mounted on the housing, allowing AC to be taken from the inverter without the use of brushes. Figure 12-201 shows an internal wiring diagram for this type of rotary inverter. The generator rotor has six poles, magnetized to provide alternate North and South poles about its circumference.

When the motor field and armature are excited, the rotor begins to turn. As the rotor turns, the permanent magnet rotates within the AC stator coils, and the magnetic flux developed by the permanent magnets are cut by the conductors in the AC stator coils. An AC voltage is produced in the windings whose polarity changes as each pole passes the windings.

This type inverter may be made multiphase by placing more AC stator coils in the housing in order to shift the phase the proper amount in each coil.

As the name of the rotary inverter indicates, it has a revolving armature in the AC generator section. Figure 12-202 shows the diagram of a revolving armature, three phase inverter.

The DC motor in this inverter is a four pole, compound wound motor. The four field coils consist of many turns of fine wire, with a few turns of heavy wire placed on top. The fine wire is the shunt field, connected to the DC source through a filter and to ground through a centrifugal governor. The heavy wire is the series field, which is connected in series with the motor armature. The centrifugal governor controls the speed by shunting a resistor that is in series with the shunt field when the motor reaches a certain speed.

The alternator is a three-phase, four-pole, star-connected AC generator. The DC input is supplied to the generator field coils and connected to ground through a voltage regulator. The output is taken off the armature through three slip rings to provide three-phase power. The inverter would be a single- phase inverter if it had a single armature winding and one slip ring. The frequency of this type unit is determined by the speed of the motor and the number of generator poles.

### Inductor-Type Rotary Inverter

Inductor-type inverters use a rotor made of soft iron laminations with grooves cut laterally across the surface to provide poles that correspond to the number of stator poles. [Figure 12-203] The field coils are wound on one set of stationary poles and the AC armature coils on the other set of stationary poles. When DC is applied to the field coils, a magnetic field is produced. The rotor turns within the field coils and, as the poles on the rotor align with the stationary poles, a low reluctance path for flux is established from the field pole through the rotor poles to the AC armature pole and through the housing back to the field pole. In this circumstance, there is a large amount of magnetic flux linking the AC coils.

When the rotor poles are between the stationary poles, there is a high reluctance path for flux, consisting mainly of air; then, there is a small amount of magnetic flux linking the AC coils. This increase and decrease in flux density in the stator induces an alternating current in the AC coils.

The number of poles and the speed of the motor determine the frequency of this type of inverter. The DC stator field current controls the voltage. A cutaway view of an inductor- type rotary inverter is shown in Figure 12-204.

Figure 12-205 is a simplified diagram of a typical aircraft AC power distribution system, utilizing a main and a standby rotary inverter system.

### Static Inverters

In many applications where continuous DC voltage must be converted to alternating voltage, static inverters are used in place of rotary inverters or motor generator sets. The rapid progress made by the semiconductor industry is extending the range of applications of such equipment into voltage and power ranges that would have been impractical a few years ago. Some such applications are power supplies for frequency sensitive military and commercial AC equipment, aircraft emergency AC systems, and conversion of wide frequency range power to precise frequency power. [Figure 12-206] The use of static inverters in small aircraft also has increased rapidly in the last few years, and the technology has advanced to the point that static inverters are available for any requirement filled by rotary inverters. For example, 250 V A emergency AC supplies operated from aircraft batteries are in production, as are 2,500 V A main AC supplies operated from a varying frequency generator supply. This type of equipment has certain advantages for aircraft applications, particularly the absence of moving parts and the adaptability to conduction cooling.

Static inverters, referred to as solid-state inverters, are manufactured in a wide range of types and models that can be classified by the shape of the AC output waveform and the power output capabilities. One of the most commonly used static inverters produces a regulated sine wave output. A block diagram of a typical regulated sine wave static inverter is shown in Figure 12-207. This inverter converts a low DC voltage into higher AC voltage. The AC output voltage is held to a very small voltage tolerance, a typical variation of less than 1 percent with a full input load change. Output taps are normally provided to permit selection of various voltages; for example, taps may be provided for 105, 115, and 125 volt AC outputs. Frequency regulation is typically within a range of one cycle for a 0–100 percent load change. Variations of this type of static inverter are available, many of which provide a square wave output.

Since static inverters use solid-state components, they are considerably smaller, more compact, and much lighter in weight than rotary inverters. Depending on the output power rating required, static inverters that are no larger than a typical airspeed indicator can be used in aircraft systems. Some of the features of static inverters are:

1. High efficiency 2. Low maintenance, long life 3. No warmup period required 4. Capable of starting under load 5. Extremely quiet operation 6. Fast response to load changes Static inverters are commonly used to provide power for such frequency sensitive instruments as the attitude gyro and directional gyro. They also provide power for autosyn and magnesyn indicators and transmitters, rate gyros, radar, and other airborne applications. Figure 12-208 is a schematic of a typical small jet aircraft auxiliary battery system. It shows the battery as input to the inverter and the output inverter circuits to various subsystems.

## 2. 中文翻译

<!-- TODO: 逐段翻译，段数与上面严格一一对应（21 段）。专业术语按行业惯例，数字与缩写保留。 -->

## 3. 专业词汇

<!-- TODO: 用表格 | 英文 | 词性 | 中文 | 本节语境 |，4~8 行。优先选下面 Glossary 里的词（本节原文出现过的）：
- Alternating current —— An electric current that reverses direction in a circuit at regular intervals.
- Circumference (of a circle) —— The linear measurement of the distance around a circle. The circumference is calculated by multiplying the diameter of the circle by 3.1416.
- Conduction —— The transfer of heat which requires physical contact between an object that has a large amount of heat energy and one that has a smaller amount of heat energy.
- Current —— The flow of electrical charge.
- Density —— The weight of a substance per unit volume.
- Frequency —— The number of cycles (on/off) completed per unit of time. Usually expressed in Hertz.
- Inductor —— A coil of wire that produces inductance in an electrical circuit.
- Maintenance —— This includes inspection, overhaul, repair, preservation, and the replacement of parts, but excludes preventive maintenance.
-->

## 4. 语法解析

<!-- TODO: 2~4 个语法点，格式：
### ① 语法点名称
**原句**：<必须逐字来自第 1 节原文>
**拆解**：主/谓/宾、从句、非谓语等成分分析
**要点**：为什么这样用、易错点、可迁移的搭配
-->
