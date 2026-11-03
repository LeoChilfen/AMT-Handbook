# Basic Circuit Analysis & Troubleshooting

> 通用 Ch 12 · Basic Circuit Analysis & Troubleshooting · 原文 PDF 第 520 页

## 1. 原文

Troubleshooting is the systematic process of recognizing the symptoms of a problem, identifying the possible cause, and locating the failed component or conductor in the circuit. To be proficient at troubleshooting, the technician must understand how the circuit operates and know how to properly use the test equipment. There are many ways in which a system can fail and to cover all of the possibilities is beyond the scope of this handbook. However, there are some basic concepts that enable the technician to handle many of the common faults encountered in the aircraft.

Before starting a discussion on basic circuits and troubleshooting, the following definitions are given.

• Short circuit—an unintentional low resistance path between two components in a circuit or between a Applied(0) volts (+) volts Horizontal deflection plates (H)

Vertical deflection plates (V)

(0) volts The horizontal beam position will depend on the applied saw-tooth voltage Voltage starts at a maximum negative value and increases to a maximum positive value, tracing the beam from the left to the right (−) volts Vertical deflection plates (v)

Horizontal deflection plates (h)Screen Beam on center (0) volts (−) volts Electrons repelled down (−) volts Electrons repelled to left (0) volts (0) volts(0) volts (0) volts (+) volts Electrons attracted up (+) volts Electrons attracted to right (0) volts component/conductor and ground. It usually creates high current flow, which burns out or causes damage to the circuit conductor or components.

• Open circuit—a circuit that is not a complete or continuous path. An open circuit represents an infinitely large resistance. Switches are common devices used to open and close a circuit. Sometimes a circuit opens due to a component failure, such as a light bulb or a burned out resistor.

• Continuity—the state of being continuous, uninterrupted or connected together; the opposite of a circuit that is not broken or does not have an open.

• Discontinuity—the opposite of continuity, indicating that a circuit is broken or not continuous.

### Voltage Measurement

V oltage is measured across a component with a voltmeter or the voltmeter position on a multimeter. Usually, there is a DC and an AC selection on the meter. Before the meter is used for measurements, make sure that the meter is selected for the correct type of voltage. When placing the probes across a component to take a measurement, take care to ensure that the polarity is correct. [Figure 12-170] Standard practice is for the red meter lead to be installed in the positive (+) jack and the black meter lead to be installed in the negative meter jack (−). Then when placing the probes across or in parallel with a component to measure the voltage, the leads should match the polarity of the component. The red lead is on the positive Applied Applied (0) volts (+) volts Horizontal deflection plates (h)

(−) volts Vertical deflection plates (v)

(0) volts (–) volts (+) volts (0) volts Input signal side of the component and the black is on the negative side, which prevents damage to the meter or incorrect readings.

All meters have some resistance and will shunt some of the current. This has the effect of changing the characteristic of the circuit because of this change in current. This is typically more of a concern with older analog type meters. If there are any questions about the magnitude of the voltage across a component, then the meter should be set to measure on the highest voltage range. This prevents the meter from “pegging” and possible damage. The range should then be selected to low values until the measured voltage is read at the mid-scale deflection. Readings taken at mid-scale are the most accurate.

### Current Measurement

Current is measured with the ammeter connected in the current path by opening or breaking the circuit and inserting the meter in series. [Figure 12-170] Standard practice is for the red meter lead to be installed in the positive (+) jack and the black meter lead to be installed in the negative meter jack (−). The positive side of the meter is connected towards the positive voltage source. Ideally, the meter should not alter the current and influence the circuit and the measurements. However, the meter does have some effect because of its internal resistance that is connected with the rest of the circuit in series. The resistance is rather small and for most practical purposes, this can be neglected.

### Checking Resistance in a Circuit

The ohmmeter is used to measure the resistance. In its more basic form, the ohmmeter consists of a variable resistor in series with a meter movement and a voltage source. The meter must first be adjusted before use.

Refer to Figure 12-171 for meter configurations during adjustments. When the meter leads are not connected (open), the needle points to the full left-hand position, indicating infinite resistance or and open circuit. With the lead placed together, the circuit is shorted as shown with the meter needle to the full right-hand position. When a connection is made, the internal battery is allowed to produce a current through the movement coil, causing a deflection of the needle in proportion to the value of the external resistance. In this case, the resistance is zero because the leads are shorted.

The purpose of the variable resistor in the meter is to adjust the current so that the pointer reads exactly zero when the leads are shorted. This is needed because as the battery continues to be used, the voltage changes, thus requiring an adjustment. The meter should be “zeroed” before each use.

To check the value of a resistor, the resistor must be disconnected from the circuit. This prevents any possible damage to the ohmmeter, and it prevents the possibility of any inaccurate readings due to the circuit being in parallel with the resistor in question. [Figure 12-172]

### Continuity Checks

In many cases, the ohmmeter is not used for measuring the resistance of a component but to simply check the integrity of a connection from one portion of a circuit to another. If there is a good connection, then the ohmmeter reads a near zero resistance or a short. If the circuit is open or has a very poor connection at some point like an over-crimped pin in a connector, then the ohmmeter reads infinity or some very high resistance. Keep in mind that while any measurement is being taken, contact with the circuit or probes should be avoided. Contact can introduce another parallel path and provide misleading indications.

### Capacitance Measurement

Figure 12-173 illustrates a basic test of a capacitor with an ohmmeter. There are usually two common modes of failure for a capacitor. One is a complete failure characterized by short circuit through the capacitor due to the dielectric breaking down or an open circuit. The more insidious failure occurs due to degradation, which is a gradual deterioration of the capacitor’s characteristics.

If a problem is suspected, remove the capacitor from the circuit and check with an ohmmeter. The first step is to short the two leads of the capacitor to ensure that it is entirely discharged. Next, connect the two leads as shown in Figure 12-173 across the capacitor and observe the needle movement. At first, the needle should indicate a short circuit. Then as the capacitor begins to charge, the needle should move to the left or infinity and eventually indicate an open circuit. The capacitor takes its charge from the internal battery of the ohmmeter. The greater the capacitance, the longer it takes to charge. If the capacitor is shorted, then the needle remains at a very low or shorted resistance. If there is some internal deterioration of the dielectric, then the needle never reaches a high resistance but some intermediate value, indicating a current.

### Inductance Measurement

The common mode of failure in an inductor is an open. To check the integrity of an inductor, it must be removed from the circuit and tested as an isolated component just like the capacitor. If there is an open in the inductor, a simple check with an ohmmeter shows it as an open circuit with infinite resistance. If in fact the inductor is in good condition, then the ohmmeter indicates the resistance of the coil.

On occasions, the inductor fails due to overheating. When the inductor is overheated, it is possible for the insulation covering the wire in the coil to melt, causing a short. The effects of a shorted coil are that of reducing the number of turns. At this point, further testing of the inductor must be Ammeter symbol Voltmeter symbol Meter symbols Simplified use of meters Ohmmeter symbol R1 + + − − 3k Ω Open the circuit and insert ammeter in series with the load A R1 + + − −3k Ω Voltage is measured across a component V R1 + + − −3k Ω Resistance is measured across a component Ω A V Ω done with test equipment not covered in this handbook.

### Troubleshooting Open Faults in a Series Circuit

One of the most common modes of failure is the “open” circuit. A component, such as a resistor, can overheat due to the power rating being exceeded. Other more frustrating problems can happen when a “cold” solder joint cracks leaving a wire disconnected from a relay or connector. This type of damage can occur during routine maintenance after a technician has accessed an area for inspections. In many cases, there is no visual indication that a failure has occurred, and the soon-to-be-frustrated technician is unaware that there is a problem until power is reapplied to the aircraft in the final days leading up to aircraft delivery and scheduled operations.

The first example is a simplified diagram shown in Figures 12-174 through 12-176. The circuit depicted in Figure 12-174 is designed to cause current to flow through a lamp, but because of the open resistor, the lamp will not light. To locate this open, a voltmeter or an ohmmeter should be used.

### Tracing Opens with the Voltmeter

A general procedure to follow in this case is to measure the voltage drop across each component in the circuit, keeping in mind the following points. If there is an open in a series circuit, then the voltage drops on sides of the component. In this case, the total voltage must appear across the open resistor as per Kirchhoff’s V oltage Law.

If a voltmeter is connected across the lamp, as shown in Figure 12-175, the voltmeter reads zero. Since no current can flow in the circuit because of the open resistor, there is no voltage drop across the lamp indicating that the lamp is good.

Next, the voltmeter is connected across the open resistor, as shown in Figure 12-176. The voltmeter has closed the circuit by shunting (paralleling) the burned out resistor, allowing current to flow. Current flows from the negative terminal of the battery, through the switch, through the voltmeter and the lamp, back to the positive terminal of the battery. However, the resistance of the voltmeter is so high that only a very small current flows in the circuit. The current is too small to light the lamp, but the voltmeter reads the battery voltage.

### Tracing Opens with the Ohmmeter

A simplified circuit, as shown in Figures 12-177 and 12-178, illustrates how to locate an open in a series circuit using the ohmmeter. A general rule to keep in mind when troubleshooting with an ohmmeter is: when an ohmmeter is properly connected across a circuit component and a resistance reading is obtained, the component has continuity and is not open.

When an ohmmeter is used, the circuit component to be tested must be isolated and the power source removed from the circuit. In this case, these requirements can be met by opening the circuit switch as shown in Figure 12-177. The ohmmeter is zeroed and across all good components is zero. The voltage drop across the open component equals the total voltage across the series combination. This condition happens because the open component prevents current to pass through the series circuit. With there being no current, there can be no voltage drop across any of the good components. Because the current is zero, it can be determined by Ohm’s Law that E = IR = 0 volts across a component. The voltage is the same on both places across (in parallel with) the lamp. In this testing configuration, some value of resistance is read indicating that the lamp is in good condition and is not the source of the open in the circuit.

Now the technician should move to the resistor and place the ohmmeter probe across it as shown in Figure 12-178. When the ohmmeter is connected across the open resistor, it indicates infinite resistance, or a discontinuity. Thus, the circuit open has now been located.

+ − Black lead Open circuit Red lead 0 Simplified ohmmeter ∞ + − Black lead Shorted circuit Red lead 0 Simplified ohmmeter ∞ + − Black lead R1 Red lead Isolate from circuit connect across resistor 0 Simplified ohmmeter ∞ R2 R3 + −

### Troubleshooting Shorting Faults in a Series Circuit

An open fault can cause a component or system not to work, which can be critical and hazardous. A shorting fault can potentially be more of a severe nature than the open type of fault. A short circuit, or “short,” causes the opposite effect. A short across a series circuit produces a greater than normal current flow. Faults of this type can develop slowly when a wire bundle is not properly secured and is allowed to chafe against the airframe structure or other systems, such as hydraulic lines. Shorts can also occur due to a careless technician using incorrect hardware when installing an interior. If screws that are too long are used to install trim, it is possible to penetrate a wire bundle immediately causing numerous shorts. Worse yet, are the shorts that are not immediately seen but “latent” and do not show symptoms until the aircraft is in service. Another point to keep in mind is when closing panels. Wires can become pinched between the panel and the airframe causing either a short or a latent, intermittent short. The simplified circuit, shown in Figures 12-179 through 12-182 is used to illustrate troubleshooting a short in a series circuit.

In Figure 12-179, a circuit is designed to light a lamp. A resistor is connected in the circuit to limit current flow. If the resistor is shorted, as shown in the illustration, the current flow increases and the lamp becomes brighter. If the applied voltage were high enough, the lamp would burn out, but in this case the fuse would protect the lamp by opening first.

Usually a short circuit produces an open circuit by either blowing (opening) the fuse or burning out a circuit component. But in some circuits, there may be additional resistors which do not allow one shorted resistor to increase the current flow enough to blow the fuse or burn out a component. [Figure 12-180] Thus, with one resistor shorted out, the circuit still functions since the power dissipated by the other resistors does not exceed the rating of the fuse.

### Tracing Shorts with the Ohmmeter

The shorted resistor can be located with an ohmmeter. [Figure 12-181] First the switch is opened to isolate the Break Break V + − Black lead Needle moves full-scale (short)

Conventional current Initial charging of capacitor behaves like a shorted circuit.

Red lead 0 Simplified ohmmeter ∞ + − +− Black lead Needle moves full-scale (open)

Full charge no current Once charged, the capacitor behaves like an open circuit.

Red lead 0 Simplified ohmmeter ∞ circuit components. In Figure 12-181, this circuit is shown with an ohmmeter connected across each of the resistors. Only the ohmmeter connected across the shorted resistor shows a zero reading, indicating that this resistor is shorted.

### Tracing Shorts with the Voltmeter

To locate the shorted resistor while the circuit is functioning, a voltmeter can be used. Figure 12-182 illustrates that when a voltmeter is connected across any of the resistors that are not shorted, a portion of the applied voltage is indicated on the voltmeter scale. When it is connected across the shorted resistor, the voltmeter reads zero.

### Troubleshooting Open Faults in a Parallel Circuit

The procedures used in troubleshooting a parallel circuit are sometimes different from those used in a series circuit. Unlike a series circuit, a parallel circuit has more than one path in which current flows. A voltmeter cannot be used, since, when it is placed across an open resistor, it reads the voltage drop in a parallel branch. But an ammeter or the modified use of an ohmmeter can be employed to detect an open branch in a parallel circuit.

If the open resistor shown in Figure 12-183 was not visually apparent, the circuit might appear to be functioning properly, because current would continue to flow in the other two branches of the circuit. To determine that the circuit is not operating properly, a determination must be made as to how the circuit should behave when working properly. First, the total resistance, total current, and the branch currents of the circuit should be calculated as if there were no open in the circuit. In this case, the total resistance can be simply determined by:

RT = RN Where RT is the total circuit resistance N is the number of resistors R is the resistor value Break V Break Ω Break Ω component.

RT = = 10 Ω30 Ω3 The total current of the circuit can now be determined by using Ohm’s Law: IT = ESRT Where IT is the total current ES is the source voltage across the parallel branch RT is the total resistance of the parallel branch IT = = 3 amperes (total current)30 v10 Ω Each branch current should be determined in a similar manner. For the first branch, the current is: I1 = ESR1 Where I1 is the current in the first branch ES is the source voltage across the parallel branch R1 is the resistance of the first branch I1 = = 1 ampere30 v30 Ω Because the other two branches are of the same resistive value, then the current in each of those branches is 1 ampere also. Adding up the amperes in each branch confirms the initial calculation of total current being 3 amperes.

### Tracing an Open with an Ammeter

If the technician now places an ammeter in the circuit, the total current would be indicated as 2 amperes as shown in Figure 12-183 instead of the calculated 3 amperes. Since 1 ampere of current should be flowing through each branch, it is obvious that one branch is open. If the ammeter is then connected into the branches, one after another, the open branch is eventually located by a zero ammeter reading.

### Tracing an Open with an Ohmmeter

A modified use of the ohmmeter can also locate this type of open. If the ohmmeter is connected across the open resistor, as shown in Figure 12-184, an erroneous reading of continuity would be obtained. Even though the circuit switch is open, the open resistor is still in parallel with R 1 and R2, and the ohmmeter would indicate the open resistor had a resistance of 15 ohms, the equivalent resistance of the parallel combination of R 1 and R2.

Therefore, it is necessary to open the circuit as shown in Figure 12-185 in order to check the resistance of R3. In this way, the resistor is not shunted (paralleled) by R1 and R2. The reading on the ohmmeter now indicates infinite resistance, which means the open component has been isolated.

### Troubleshooting Shorting Faults in Parallel Circuits

As in a series circuit, a short in a parallel circuit usually causes an open circuit by blowing the fuse. But, unlike a series circuit, one shorted component in a parallel circuit stops current flow by causing the fuse to open. Refer to the circuit in Figure 12-186. If resistor R3 is shorted, a path of almost zero resistance is offered the current, and all the circuit current flows through the branch containing the shorted resistor. Since this is practically the same as connecting a wire between the terminals of the battery, the current rises to an excessive value, and the fuse opens. Since the fuse opens almost as soon as a resistor shorts out, there is no time to V V Some voltage Short Zero voltage Ω Ω Ω Ω 40 Ω 50 Ω R1 R3 R2 R4 10 Ω 100 V 0 Ω perform a current or voltage check. Thus, troubleshooting a parallel DC circuit for a shorted component should be accomplished with an ohmmeter. But, as in the case of checking for an open resistor in a parallel circuit, a shorted resistor can be detected with an ohmmeter only if one end of the shorted resistor is disconnected and isolated from the rest of the circuit.

### Troubleshooting Shorting Faults in Series-Parallel Circuits

#### Logic in Tracing an Open

Troubleshooting a series-parallel resistive circuit involves locating malfunctions similar to those found in a series or a parallel circuit. Figures 12-187 through 12-189 illustrate three points of failure in a series-parallel circuit and their generalized effects.

1. In the circuit shown in Figure 12-187, an open has occurred in the series portion of the circuit. When the open occurs anywhere in the series portion of a series-parallel circuit, current flow in the entire circuit stops. In this case, the circuit does not function, and the lamp, L1, is not lit.

2. If the open occurs in the parallel portion of a series- parallel circuit, as shown in Figure 12-188, part of the circuit continues to function. In this case, the lamp continues to burn, but its brightness diminishes, since the total resistance of the circuit has increased and the total current has decreased.

3. If the open occurs in the branch containing the lamp, as shown in Figure 12-189, the circuit continues to function with increased resistance and decreased current, but the lamp does not light.

### Tracing Opens with the Voltmeter

To explain how the voltmeter and ohmmeter can be used to troubleshoot series-parallel circuits, the circuit shown in Figure 12-190 has been labeled at various points. A point- to-point description is listed below with expected results:

1. By connecting a voltmeter between points A and D, the battery and switch can be checked for opens.

2. By connecting the voltmeter between points A and B, the voltage drop across R 1 can be checked. This voltage drop is a portion of the applied voltage.

3. If R1 is open, the reading between B and D is zero.

4. By connecting a voltmeter between A and E, the continuity of the conductor between the positive terminal of the battery and point E, as well as the fuse, 30 Ω 30 Ω R130 V R2 30 Ω R3 A 2a Break 30 Ω 30 Ω R1 R2 30 Ω R3 Break can be checked. If the conductor or fuse is open, the voltmeter reads zero.

5. If the lamp is burning, it is obvious that no open exists in the branch containing the lamp, and the voltmeter could be used to detect an open in the branch containing R2 by removing lamp, L1, from the circuit.

Troubleshooting the series portion of a series-parallel circuit presents no difficulties, but in the parallel portion of the circuit, misleading readings can be obtained.

## 2. 中文翻译

<!-- TODO: 逐段翻译，段数与上面严格一一对应（79 段）。专业术语按行业惯例，数字与缩写保留。 -->

## 3. 专业词汇

<!-- TODO: 用表格 | 英文 | 词性 | 中文 | 本节语境 |，4~8 行。优先选下面 Glossary 里的词（本节原文出现过的）：
- Ammeter —— An instrument for measuring electric current in amperes.
- Ampere —— A unit of measure of the rate of electron flow or current in an electrical conductor. One ampere of current represents one coulomb of electrical charge (6.24 × 
- Capacitance (C) —— The property of an electric conductor that characterizes its ability to store an electric charge.
- Capacitor —— An electrical component that stores an electric charge.
- Conductor —— A material that will carry electric current.
- Current —— The flow of electrical charge.
- Degradation —— The alteration of material properties (e.g., strength, modulus, coefficient of expansion) which may result from deviations in manufacturing or from repeated loa
- Discontinuity —— An interruption in the normal physical structure or configuration of a part, such as a crack, forging lap, seam, inclusion, porosity, and the like. A discontinu
-->

## 4. 语法解析

<!-- TODO: 2~4 个语法点，格式：
### ① 语法点名称
**原句**：<必须逐字来自第 1 节原文>
**拆解**：主/谓/宾、从句、非谓语等成分分析
**要点**：为什么这样用、易错点、可迁移的搭配
-->
