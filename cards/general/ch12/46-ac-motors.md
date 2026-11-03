# AC Motors

> 通用 Ch 12 · AC Motors · 原文 PDF 第 589 页

## 1. 原文

Because of their advantages, many types of aircraft motors are designed to operate on alternating current. In general, AC motors are less expensive than comparable DC motors. In many instances, AC motors do not use brushes and commutators so sparking at the brushes is avoided. AC motors are reliable and require little maintenance. They are also well suited for constant speed applications and certain types are manufactured that have, within limits, variable speed characteristics. Alternating current motors are designed to operate on polyphase or single-phase lines and at several voltage ratings.

The speed of rotation of an AC motor depends upon the number of poles and the frequency of the electrical source of power:

rpm = 120 × FrequencyNumber of poles Since airplane electrical systems typically operate at 400 cycles, an electric motor at this frequency operates at about seven times the speed of a 60-cycle commercial motor with the same number of poles. Because of this high speed of rotation, 400-cycle AC motors are suitable for operating small, high-speed rotors, through reduction gears, in lifting and moving heavy loads, such as the wing flaps, the retractable landing gear, and the starting of engines. The 400-cycle induction type motor operates at speeds ranging from 6,000 rpm to 24,000 rpm. Alternating current motors are rated in horsepower output, operating voltage, full load current, speed, number of phases, and frequency. Whether the motors operate continuously or intermittently (for short intervals) is also considered in the rating.

### Types of AC Motors

There are two general types of AC motors used in aircraft systems: induction motors and synchronous motors. Either type may be single-phase, two-phase, or three-phase. Three-phase induction motors are used where large amounts of power are required. They operate such devices as starters, flaps, landing gears, and hydraulic pumps. Single-phase induction motors are used to operate devices such as surface locks, intercooler shutters, and oil shutoff valves in which the power requirement is low. Three-phase synchronous motors operate at constant synchronous speeds and are commonly used to operate flux gate compasses and propeller synchronizer systems. Single- phase synchronous motors are common sources of power to operate electric clocks and other small, precision equipment. They require some auxiliary method to bring them up to Below normal speed Normal speed Above normal speed M Rheostat Series filed FastSlow – + + M Rheostat FastSlow – + M Fast Slow – synchronous speeds; that is, to start them. Usually the starting winding consists of an auxiliary stator winding.

### Three-Phase Induction Motor

The three-phase AC induction motor is also called a squirrel cage motor. Both single-phase and three-phase motors operate on the principle of a rotating magnetic field. A horseshoe magnet held over a compass needle is a simple illustration of the principle of the rotating field. The needle takes a position parallel to the magnetic flux passing between the two poles of the magnet. If the magnet is rotated, the compass needle follows. A rotating magnetic field can be produced by a two-or three-phase current flowing through two or more groups of coils wound on inwardly projecting poles of an iron frame. The coils on each group of poles are wound alternately in opposite directions to produce opposite polarity, and each group is connected to a separate phase of voltage. The operating principle depends on a revolving, or rotating, magnetic field to produce torque. The key to understanding the induction motor is a thorough understanding of the rotating magnetic field.

### Rotating Magnetic Field

The field structure shown in Figure 12-307A has poles whose windings are energized by three AC voltages: a, b, and c. These voltages have equal magnitude but differ in phase. [Figure 12-307B] At the instant of time shown as 0, the resultant magnetic field produced by the application of the three voltages has its greatest intensity in a direction extending from pole 1 to pole 4. Under this condition, pole 1 can be considered as a North pole and pole 4 as a South pole. At the instant of time shown as 1, the resultant magnetic field has its greatest intensity in the direction extending from pole 2 to pole 5. In this case, pole 2 can be considered as a North pole and pole 5 as a South pole. Thus, between instant 0 and instant 1, the magnetic field has rotated clockwise. At instant 2, the resultant magnetic field has its greatest intensity in the direction from pole 3 to pole 6, and the resultant magnetic field has continued to rotate clockwise. At instant 3, poles 4 and 1 can be considered as North and South poles, respectively, and the field has rotated still farther. At later instants of time, the resultant magnetic field rotates to other positions while traveling in a clockwise direction, a single revolution of the field occurring in one cycle. If the exciting voltages have a frequency of 60 cps, the magnetic field makes 60 revolutions per second, or 3,600 rpm. This speed is known as the synchronous speed of the rotating field.

### Construction of Induction Motor

The stationary portion of an induction motor is called a stator, and the rotating member is called a rotor. Instead of salient poles in the stator, as shown in Figure 12-307A, distributed windings are used. These windings are placed in slots around the periphery of the stator. It is usually impossible to determine the number of poles in an induction motor by visual inspection, but the information can be obtained from the nameplate of the motor. The nameplate usually gives the number of poles and the speed at which the motor is designed to run. This rated, or nonsynchronous, speed is slightly less than the synchronous speed. To determine the number of poles per phase on the motor, divide 120 times the frequency by the rated speed. Written as an equation, it is:

P = 120 × fN Where: P is the number of poles per phase f is the frequency in cps N is the rated speed in rpm, and 120 is a constant The result is nearly equal to the number of poles per phase. For example, consider a 60-cycle, three-phase motor with a rated speed of 1,750 rpm. In this case:

P = = = 4.1120 × 60 7,2001,750 1,750 Therefore, the motor has four poles per phase. If the number of poles per phase is given on the nameplate, the synchronous speed can be determined by dividing 120 times the frequency by the number of poles per phase. In the example used above, the synchronous speed is equal to 7,200/4, or 1,800 rpm.

The rotor of an induction motor consists of an iron core having longitudinal slots around its circumference in which heavy copper or aluminum bars are embedded. These bars are welded to a heavy ring of high conductivity on either end. The composite structure is sometimes called a squirrel cage, and motors containing such a rotor are called squirrel cage induction motors. [Figure 12-308]

### Induction Motor Slip

When the rotor of an induction motor is subjected to the revolving magnetic field produced by the stator windings, a voltage is induced in the longitudinal bars. The induced voltage causes a current to flow through the bars. This current, in turn, produces its own magnetic field, which combines with the revolving field so that the rotor assumes a position in which the induced voltage is minimized. As a result, the rotor revolves at very nearly the synchronous speed of the stator field, the difference in speed being just sufficient enough to induce the proper amount of current in the rotor to overcome the mechanical and electrical losses in the rotor. If the rotor were to turn at the same speed as the rotating field, the rotor conductors would not be cut by any magnetic lines of force, no EMF would be induced in them, no current could flow, and there would be no torque. The rotor would then slow down. For this reason, there must always be a difference in speed between the rotor and the rotating field. This difference in speed is called slip and is expressed as a percentage of the synchronous speed. For example, if the rotor turns at 1,750 rpm and the synchronous speed is 1,800 rpm, the difference in speed is 50 rpm. The slip is then equal to 50/1,800 or 2.78 percent.

### Single-Phase Induction Motor

The previous discussion has applied only to polyphase motors. A single-phase motor has only one stator winding. This winding generates a field, which merely pulsates, instead of rotating. When the rotor is stationary, the expanding and collapsing stator field induces currents in the rotor. These currents generate a rotor field opposite in polarity to that of the stator. The opposition of the field exerts a turning force on the upper and lower parts of the rotor trying to turn it 180° from its position. Since these forces are exerted through the center of the rotor, the turning force is equal in each direction. As a result, the rotor does not turn. If the rotor starts turning, it continues to rotate in the direction in which it started, since the turning force in that direction is aided by the momentum of the rotor.

### Shaded Pole Induction Motor

The first effort in the development of a self-starting, single-phase motor was the shaded pole induction motor. [Figure 12-309] This motor has salient poles, a portion of each pole being encircled by a heavy copper ring. The presence of the ring causes the magnetic field through the ringed portion of the pole face to lag appreciably behind that through the other part of the pole face. The net effect is the production of a slight component of rotation of the field, sufficient to cause the rotor to revolve. As the rotor accelerates, the torque increases until the rated speed is obtained. Such motors have low starting torque and find their greatest application in small fan motors where the initial torque required is low.

In Figure 12-309 , a diagram of a pole and the rotor is shown. The poles of the shaded pole motor resemble those of a DC motor.

A low resistance, short-circuited coil or copper band is placed across one tip of each small pole from which the motor gets the name of shaded pole. The rotor of this motor is the squirrel cage type. As the current increases in the stator winding, the flux increases. A portion of this flux cuts the low resistance shading coil. This induces a current in the shading coil, and by Lenz’s Law, the current sets up a flux that opposes the flux inducing the current. Hence, most of the flux passes through the unshaded portion of the poles. [Figure 12-310]

When the current in the winding and the main flux reaches a maximum, the rate of change is zero; thus, no emf is induced in the shading coil. A little later, the shading coil current, which causes the induced emf to lag, reaches zero, and there is no opposing flux. Therefore, the main field flux a a 0 1 2 3 4 5 6 a 1 2 3 6 5 4 b b b c c c180° Time A B of three-phase voltages.

passes through the shaded portion of the field pole. The main field flux, which is now decreasing, induces a current in the shading coil. This current sets up a flux that opposes the decrease of the main field flux in the shaded portion of the pole. The effect is to concentrate the lines of force in the shaded portion of the pole face. In effect, the shading coil retards, in time phase, the portion of the flux passing through the shaded part of the pole. This lag in time phase of the flux in the shaded tip causes the flux to produce the effect of sweeping across the face of the pole, from left to right in the direction of the shaded tip. This behaves like a very weak rotating magnetic field, and sufficient torque is produced to start a small motor. The starting torque of the shaded pole motor is exceedingly weak, and the power factor is low. Consequently, it is built in sizes suitable for driving such devices as small fans.

### Split-Phase Motor

There are various types of self-starting motors, known as split-phase motors. Such motors have a starting winding displaced 90 electrical degrees from the main or running winding. In some types, the starting winding has a fairly high resistance, which causes the current in this winding to be out of phase with the current in the running winding. This condition produces, in effect, a rotating field and the rotor revolves. A centrifugal switch disconnects the starting winding automatically after the rotor has attained approximately 25 percent of its rated speed.

### Capacitor Start Motor

With the development of high-capacity electrolytic capacitors, a variation of the split-phase motor known as the capacitor start motor, has been made. Nearly all fractional horsepower motors in use today on refrigerators and other similar appliances are of this type. [Figure 12-311] In this adaptation, the starting winding and running winding have the same size and resistance value. The phase shift between currents of the two windings is obtained by using capacitors connected in series with the starting winding.

Capacitor start motors have a starting torque comparable to their torque at rated speed and can be used in applications where the initial load is heavy. Again, a centrifugal switch is required for disconnecting the starting winding when the rotor speed is approximately 25 percent of the rated speed.

Although some single-phase induction motors are rated as high as 2 horsepower (hp), the major field of application is 1 hp, or less, at a voltage rating of 115 volts for the smaller sizes and 110 to 220 volts for one-fourth hp and up. For even larger power ratings, polyphase motors generally are used, since they have excellent starting torque characteristics.

### Direction of Rotation of Induction Motors

The direction of rotation of a three-phase induction motor can be changed by simply reversing two of the leads to the motor. The same effect can be obtained in a two-phase motor by reversing connections to one phase. In a single-phase motor, reversing connections to the starting winding reverses the direction of rotation.

Most single-phase motors designed for general application have provision for readily reversing connections to the starting winding. Nothing can be done to a shaded pole motor to reverse the direction of rotation because the direction is determined by the physical location of the copper shading ring. If, after starting, one connection to a three-phase motor is broken, the motor continues to run but delivers only one-third the rated power. Also, a two-phase motor runs at one-half its rated power if one phase is disconnected. Neither A B Aluminum or copper bars Shaft Weld at all jointsWelds holding copper or aluminum bars to end ring Aluminum or copper end ring Iron core Shaded poles Shaded poles motor starts under these abnormal conditions.

### Synchronous Motor

The synchronous motor is one of the principal types of AC motors. Like the induction motor, the synchronous motor makes use of a rotating magnetic field. Unlike the induction motor, however, the torque developed does not depend on the induction of currents in the rotor. Briefly, the principle of operation of the synchronous motor is as follows: A multiphase source of AC is applied to the stator windings, and a rotating magnetic field is produced. A direct current is applied to the rotor winding, and another magnetic field is produced. The synchronous motor is so designed and constructed that these two fields react to each other in such a manner that the rotor is dragged along and rotates at the same speed as the rotating magnetic field produced by the stator windings.

An understanding of the operation of the synchronous motor can be obtained by considering the simple motor of clockwise by some mechanical means in order to produce a rotating magnetic field. They induce poles of opposite polarity in the soft iron rotor, and forces of attraction exist between corresponding North and South poles.

Consequently, as poles A and B rotate, the rotor is dragged along at the same speed. However, if a load is applied to the rotor shaft, the rotor axis momentarily falls behind that of the rotating field but, thereafter, continues to rotate with the field at the same speed as long as the load remains constant. If the load is too large, the rotor pulls out of synchronism with the rotating field and, as a result, no longer rotates with the field at the same speed. Thus, the motor is said to be overloaded.

Such a simple motor as shown in Figure 12-312 is never used. The idea of using some mechanical means of rotating the poles is impractical because another motor would be required to perform this work. Also, such an arrangement is unnecessary because a rotating magnetic field can be produced electrically by using phased AC voltages. In this respect, the synchronous motor is similar to the induction motor.

The synchronous motor consists of a stator field winding similar to that of an induction motor. The stator winding produces a rotating magnetic field. The rotor may be a permanent magnet, as in small, single-phase synchronous motors used for clocks and other small precision equipment, or it may be an electromagnet, energized from a DC source of power and fed through slip rings into the rotor field coils, as in an alternator. In fact, an alternator may be operated either as an alternator or a synchronous motor.

Shaded pole Rotor Since a synchronous motor has little starting torque, some means must be provided to bring it up to synchronous speed. The most common method is to start the motor at no load, allow it to reach full speed, and then energize the magnetic field. The magnetic field of the rotor locks with the magnetic field of the stator and the motor operates at synchronous speed.

The magnitude of the induced poles in the rotor shown in Figure 12-313 is so small that sufficient torque cannot be developed for most practical loads. To avoid such a limitation on motor operation, a winding is placed on the rotor and energized with DC. A rheostat placed in series with the DC source provides the operator of the machine with a means of varying the strength of the rotor poles, thus placing the motor under control for varying loads.

The synchronous motor is not a self-starting motor. The rotor is heavy and, from a dead stop, it is impossible to bring the rotor into magnetic lock with the rotating magnetic field. For this reason, all synchronous motors have some kind of starting device. One type of simple starter is another motor, either AC or DC, which brings the rotor up to approximately 90 percent of its synchronous speed. The starting motor is then disconnected, and the rotor locks in step with the rotating field. Another starting method is a second winding of the squirrel cage type on the rotor. This induction winding brings the rotor almost to synchronous speed, and when the DC is connected to the rotor windings, the rotor pulls into step with the field. The latter method is the more commonly used.

An AC-series motor is a single-phase motor, but is not an induction or synchronous motor. It resembles a DC motor in that it has brushes and a commutator. The AC-series motor operates on either AC or DC circuits. Remember that the direction of rotation of a DC-series motor is independent of the polarity of the applied voltage, provided the field and armature connections remain unchanged. Hence, if a DC-series motor is connected to an AC source, a torque is developed that tends to rotate the armature in one direction. However, a DC-series motor does not operate satisfactorily from an AC supply for the following reasons:

1. The alternating flux sets up large eddy current and hysteresis losses in the unlaminated portions of the magnetic circuit and causes excessive heating and reduced efficiency.

2. The self-induction of the field and armature windings causes a low power factor.

3. The alternating field flux establishes large currents in the coils, which are short circuited by the brushes; this action causes excessive sparking at the commutator.

To design a series motor for satisfactory operation on AC, the following changes are made:

1. The eddy current losses are reduced by laminating the field poles, frame, and armature.

2. Hysteresis losses are minimized by using high permeability, transformer-type, silicon steel laminations.

3. The reactance of the field windings is kept satisfactorily low by using shallow pole pieces, few turns of wire, low frequency (usually 25 cycles for large motors), low flux density, and low reluctance (a short air gap).

4. The reactance of the armature is reduced by using a compensating winding embedded in the pole pieces. If the compensating winding is connected in series with the armature, as shown in Figure 12-314, the armature is conductively compensated.

If the compensating winding is designed as shown in Figure 12-315 , the armature is inductively compensated. If the motor is designed for operation on both DC and AC circuits, the compensating winding is connected in series with the armature. The axis of the compensating winding is displaced from the main field axis by an angle of 90°. This arrangement is similar to the compensating winding used in some DC motors and generators to overcome armature reaction. The compensating winding establishes a counter magnetomotive force, neutralizing the effect of the armature magnetomotive force, preventing distortion of the main field flux, and reducing the armature reactance. The inductively compensated armature acts like the primary of a transformer, the secondary N S SNAlternator Centrifugal switch Winding 2 (Running winding)

Winding 1 (Starting winding)

Capacitor Rotating pole structure Rotating pole structure Rotor Rotor axis B S N A S N Induced poles Rotor shaft of which is the shorted compensating winding. The shorted secondary receives an induced voltage by the action of the alternating armature flux, and the resulting current flowing through the turns of the compensating winding establishes the opposing magnetomotive force, neutralizing the armature reactance.

5. Sparking at the commutator is reduced by the use of preventive leads P1, P2, P3, and so forth, as shown in Figure 12-316, where a ring armature is shown for simplicity. When coils at A and B are shorted by the brushes, the induced current is limited by the relatively high resistance of the leads. Sparking at the brushes is also reduced by using armature coils having only a single turn and multipolar fields. High torque is obtained by having a large number of armature conductors and a large diameter armature. Thus, the commutator has a large number of very thin commutator bars and the armature voltage is limited to about 250 volts.

Fractional horsepower AC series motors are called universal motors. They do not have compensating windings or preventive leads. They are used extensively to operate fans and portable tools, such as drills, grinders, and saws.

### Maintenance of AC Motors

The inspection and maintenance of AC motors is very simple. The bearings may or may not need frequent lubrication. If they are the sealed type, lubricated at the factory, they require no further attention. Be sure the coils are kept dry and free from oil or other abuse. The temperature of a motor is usually its only limiting operating factor. A good rule of thumb is that a temperature too hot for the hand is too high for safety. Next to the temperature, the sound of a motor or generator is the best trouble indicator. When operating properly, it should hum evenly. If it is overloaded it “grunts.” A three-phase motor Three-phase winding produces a rotating magnetic field Slip rings + N N S S – with one lead disconnected refuses to turn and “growls.” A knocking sound generally indicates a loose armature coil, a shaft out of alignment, or armature dragging because of worn bearings. In all cases, the inspection and maintenance of all AC motors should be performed in accordance with the applicable manufacturer’s instructions.

## 2. 中文翻译

<!-- TODO: 逐段翻译，段数与上面严格一一对应（58 段）。专业术语按行业惯例，数字与缩写保留。 -->

## 3. 专业词汇

<!-- TODO: 用表格 | 英文 | 词性 | 中文 | 本节语境 |，4~8 行。优先选下面 Glossary 里的词（本节原文出现过的）：
- Alternating current —— An electric current that reverses direction in a circuit at regular intervals.
- Capacitor —— An electrical component that stores an electric charge.
- Circumference (of a circle) —— The linear measurement of the distance around a circle. The circumference is calculated by multiplying the diameter of the circle by 3.1416.
- Current —— The flow of electrical charge.
- Density —— The weight of a substance per unit volume.
- Diameter (circle) —— The length of a line passing directly through the center of a circle. Twice the radius of the circle.
- Difference —— The answer to a subtraction problem.
- Direct current (DC) —— Electricity that flows in one direction at all times.
-->

## 4. 语法解析

<!-- TODO: 2~4 个语法点，格式：
### ① 语法点名称
**原句**：<必须逐字来自第 1 节原文>
**拆解**：主/谓/宾、从句、非谓语等成分分析
**要点**：为什么这样用、易错点、可迁移的搭配
-->
