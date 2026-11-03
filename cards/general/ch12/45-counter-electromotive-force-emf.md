# Counter Electromotive Force (emf)

> 通用 Ch 12 · Counter Electromotive Force (emf) · 原文 PDF 第 584 页

## 1. 原文

The armature resistance of a small, 28-volt DC motor is extremely low, about 0.1 ohm. When the armature is connected across the 28-volt source, current through the armature is apparently:

I = = = 280 amperesE 28R 0.1 This high value of current flow is not only impracticable but also unreasonable, especially when the current drain, during normal operation of a motor, is found to be about 4 amperes. This is because the current through a motor armature during operation is determined by more factors than ohmic resistance.

When the armature in a motor rotates in a magnetic field, a voltage is induced in its windings. This voltage is called the back or counter emf and is opposite in direction to the voltage applied to the motor from the external source.

Counter emf opposes the current, which causes the armature to rotate. The current flowing through the armature, therefore, decreases as the counter emf increases. The faster the armature rotates, the greater the counter emf. For this reason, a motor connected to a battery may draw a fairly high current on starting, but as the armature speed increases, the current flowing through the armature decreases. At rated speed, the counter emf may be only a few volts less than the battery voltage. Then, if the load on the motor is increased, the motor slows down, less counter emf is generated, and the current drawn from the external source increases. In a shunt motor, the counter emf affects only the current in the armature, since End frame Field coils Armature Brush rigging Bearing Cover Commutator Tube type brush Box type brush the field is connected in parallel across the power source. As the motor slows down and the counter emf decreases, more current flows through the armature, but the magnetism in the field is unchanged. When the series motor slows down, the counter EMF decreases and more current flows through the field and the armature, thereby strengthening their magnetic fields. Because of these characteristics, it is more difficult to stall a series motor than a shunt motor.

Electric motors are called upon to operate under various conditions. Some motors are used for intermittent operation;

Commutator Armature Shunt field Shunt field A B Diagrammatic Schematic Commutator Armature Wire A B Diagrammatic Schematic others operate continuously. Motors built for intermittent duty can be operated for short periods only and, then, must be allowed to cool before being operated again. If such a motor is operated for long periods under full load, the motor becomes overheated. Motors built for continuous duty may be operated at rated power for long periods.

### Reversing Motor Direction

By reversing the direction of current flow in either the armature or the field windings, the direction of a motor’s rotation may be reversed. This reverses the magnetism of either the armature or the magnetic field in which the armature rotates. If the wires connecting the motor to an external source are interchanged, the direction of rotation is not reversed, since changing these wires reverses the magnetism of both field and armature and leaves the torque in the same direction as before.

One method for reversing direction of rotation employs two field windings wound in opposite directions on the same pole. This type of motor is called a split field motor. [Figure 12-303] The single pole, double throw switch makes it possible to direct current through either of the two windings. When the switch is placed in the lower position, current flows through the lower field winding, creating a North pole at the lower field winding and at the lower pole piece, and a South pole at the upper pole piece. When the switch is placed in the upper position, current flows through the upper field winding, the magnetism of the field is reversed, and the armature rotates in the opposite direction. Some split field motors are built with two separate field windings wound on alternate poles. The armature in such a motor, a four pole reversible motor, rotates in one direction when current flows through the windings of one set of opposite pole pieces, and in the opposite direction when current flows through the other set of windings.

Another method of direction reversal, called the switch method, employs a double pole, double throw switch which changes the direction of current flow in either the armature or the field. In the illustration of the switch method shown in Figure 12-304, current direction may be reversed through the field but not through the armature. When the switch is thrown to the “up” position, current flows through the field winding to establish a North pole at the right side of the motor and a South pole at the left side of the motor. When the switch is thrown to the “down” position, this polarity is reversed and the armature rotates in the opposite direction.

Shunt field + – Series field M Output power or load0 100% 100%Speed of rotation Series connection Differential compounding Shunt connection Cumulative compounding

Motor speed can be controlled by varying the current in the field windings. When the amount of current flowing through the field windings is increased, the field strength increases, but the motor slows down since a greater amount of counter EMF is generated in the armature windings. When the field current is decreased, the field strength decreases, and the motor speeds up because the counter EMF is reduced. A motor in which speed can be controlled is called a variable speed motor. It may be either a shunt or series motor.

In the shunt motor, speed is controlled by a rheostat in series with the field windings. [Figure 12-305] The speed depends on the amount of current that flows through the rheostat to the field windings. To increase the motor speed, the resistance in the rheostat is increased, which decreases the field current. As a result, there is a decrease in the strength of the magnetic field and in the counter EMF. This momentarily increases the armature current and the torque. The motor then automatically speeds up until the counter EMF increases and causes the armature current to decrease to its former value. When this occurs, the motor operates at a higher fixed speed than before.

To decrease the motor speed, the resistance of the rheostat is decreased. More current flows through the field windings and increases the strength of the field; then, the counter EMF increases momentarily and decreases the armature current. As a result, the torque decreases and the motor slows down until the counter EMF decreases to its former value; then the motor operates at a lower fixed speed than before.

In the series motor, the rheostat speed control is connected either in parallel or in series with the motor field, or in parallel with the armature. When the rheostat is set for maximum resistance, the motor speed is increased in the parallel armature connection by a decrease in current. When the rheostat resistance is maximum in the series connection, motor speed is reduced by a reduction in voltage across the motor. For above normal speed operation, the rheostat is in parallel with the series field. Part of the series field current is bypassed and the motor speeds up. [Figure 12-306]

#### Energy Losses in DC Motors

Losses occur when electrical energy is converted to mechanical energy (in the motor), or mechanical energy is converted to electrical energy (in the generator). For the machine to be efficient, these losses must be kept to a minimum. Some losses are electrical; others are mechanical. Electrical losses are classified as copper losses and iron losses; mechanical losses occur in overcoming the friction of various parts of the machine.

Copper losses occur when electrons are forced through the copper windings of the armature and the field. These losses are proportional to the square of the current. They are sometimes called I2R losses, since they are due to the power dissipated in the form of heat in the resistance of the field and armature windings.

Iron losses are subdivided in hysteresis and eddy current losses. Hysteresis losses are caused by the armature revolving in an alternating magnetic field. It, therefore, becomes magnetized first in one direction and then in the other. The residual magnetism of the iron or steel of which the armature is made causes these losses. Since the field magnets are always magnetized in one direction (DC field), they have no hysteresis losses.

Eddy current losses occur because the iron core of the armature is a conductor revolving in a magnetic field. This sets up an EMF across portions of the core, causing currents to flow within the core. These currents heat the core and, if they become excessive, may damage the windings. As far as the output is concerned, the power consumed by eddy currents is a loss. To reduce eddy currents to a minimum, a laminated Double pole Double throw switch Down Up A B core usually is used. A laminated core is made of thin sheets of iron electrically insulated from each other. The insulation between laminations reduces eddy currents, because it is “transverse” to the direction in which these currents tend to flow. However, it has no effect on the magnetic circuit. The thinner the laminations, the more effectively this method reduces eddy current losses.

### Inspection and Maintenance of DC Motors

Use the following procedures to make inspection and maintenance checks:

1. Check the operation of the unit driven by the motor in accordance with the instructions covering the specific installation.

2. Check all wiring, connections, terminals, fuses, and switches for general condition and security.

3. Keep motors clean and mounting bolts tight.

4. Check brushes for condition, length, and spring tension. Minimum brush lengths, correct spring tension, and procedures for replacing brushes are given in the applicable manufacturer’s instructions.

5. Inspect commutator for cleanness, pitting, scoring, roughness, corrosion, or burning. Check for high mica (IF the copper wears down below the mica, the mica insulates the brushes from the commutator.) Clean dirty commutators with a cloth moistened with the recommended cleaning solvent. Polish rough or corroded commutators with fine sandpaper (000 or finer) and blow out with compressed air. Never use emery paper since it contains metallic particles that may cause shorts. Replace the motor if the commutator is burned, badly pitted, grooved, or worn to the extent that the mica insulation is flush with the commutator surface.

6. Inspect all exposed wiring for evidence of overheating. Replace the motor if the insulation on leads or windings is burned, cracked, or brittle.

7. Lubricate only if called for by the manufacturer’s instructions covering the motor. Most motors used in today’s airplanes require no lubrication between overhauls.

8. Adjust and lubricate the gearbox, or unit which the motor drives, in accordance with the applicable manufacturer’s instructions covering the unit.

When trouble develops in a DC motor system, check first to determine the source of the trouble. Replace the motor only when the trouble is due to a defect in the motor itself. In most cases, the failure of a motor to operate is caused by a defect in the external electrical circuit or by mechanical failure in the mechanism driven by the motor.

Check the external electrical circuit for loose or dirty Rheostat Frame Pole Commutator Armature Shunt led connections and for improper connection of wiring. Look for open circuits, grounds, and shorts by following the applicable manufacturer’s circuit testing procedure. If the fuse is not blown, failure of the motor to operate is usually due to an open circuit. A blown fuse usually indicates an accidental ground or short circuit. A low battery usually causes the chattering of the relay switch, which controls the motor. When the battery is low, the open circuit voltage of the battery is sufficient to close the relay, but with the heavy current draw of the motor, the voltage drops below the level required to hold the relay closed. When the relay opens, the voltage in the battery increases enough to close the relay again. This cycle repeats and causes chattering, which is very harmful to the relay switch due to the heavy current causing an arc which burns the contacts.

Check the unit driven by the motor for failure of the unit or drive mechanism. If the motor has failed as a result of a failure in the driven unit, the fault must be corrected before installing a new motor. If it has been determined that the fault is in the motor itself (by checking for correct voltage at the motor terminals and for failure of the driven unit), inspect the commutator and brushes. A dirty commutator or defective or binding brushes may result in poor contact between brushes and commutator. Clean the commutator, brushes, and brush holders with a cloth moistened with the recommended cleaning solvent. If brushes are damaged or worn to the specified minimum length, install new brushes in accordance with the applicable manufacturer’s instructions covering the motor. If the motor still fails to operate, replace it with a serviceable motor.

## 2. 中文翻译

<!-- TODO: 逐段翻译，段数与上面严格一一对应（33 段）。专业术语按行业惯例，数字与缩写保留。 -->

## 3. 专业词汇

<!-- TODO: 用表格 | 英文 | 词性 | 中文 | 本节语境 |，4~8 行。优先选下面 Glossary 里的词（本节原文出现过的）：
- Conductor —— A material that will carry electric current.
- Corrosion —— The deterioration of metal by chemical or electrochemical attack.
- Current —— The flow of electrical charge.
- Direct current (DC) —— Electricity that flows in one direction at all times.
- Electrical energy —— Electrical energy is converted to heat energy when an electric current flows through any form of resistance such as an electric iron, electric light, or an elec
- Energy —— The capacity of a physical system to perform work. There are two types of energy, kinetic and potential.
- Friction —— The opposition to movement between objects.
- Maintenance —— This includes inspection, overhaul, repair, preservation, and the replacement of parts, but excludes preventive maintenance.
-->

## 4. 语法解析

<!-- TODO: 2~4 个语法点，格式：
### ① 语法点名称
**原句**：<必须逐字来自第 1 节原文>
**拆解**：主/谓/宾、从句、非谓语等成分分析
**要点**：为什么这样用、易错点、可迁移的搭配
-->
