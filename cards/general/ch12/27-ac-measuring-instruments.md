# AC Measuring Instruments

> 通用 Ch 12 · AC Measuring Instruments · 原文 PDF 第 515 页

## 1. 原文

A DC meter, such as an ammeter, connected in an AC circuit indicates zero, because the meter movements used in a d’Arsonval type movement is restricted to DC. Since the field of a permanent magnet in the d’Arsonval type meter remains constant and in the same direction at all times, the moving coil follows the polarity of the current. The coil attempts to move in one direction during half of the AC cycle and in the reverse direction during the other half when the current reverses.

The current reverses direction too rapidly for the coil to follow, causing the coil to assume an average position. Since 20% full-scale 120k Ω Meter movement [+] [−]

− + Adjuster R x 1 Range switch R x 10 R x 100 R x 1k R x 10k 0∞ the current is equal and opposite during each half of the AC cycle, the DC meter indicates zero, which is the average value. Thus, a meter with a permanent magnet cannot be used to measure alternating voltage and current. For AC measurements of current and voltage, additional circuitry is required. The additional circuitry has a rectifier, which converts AC to DC. There are two basic types of rectifiers: the half-wave rectifier and the full-wave rectifier. [Figure 12-159]

Figure 12-159 also shows a simplified block diagram of an AC meter. In this depiction, the full-wave rectifier precedes the meter movement. The movement responds to the average value of the pulsating DC. The scale can then be calibrated to show anything the designer wants. In most cases, it is the root mean square (RMS) value or peak value.

### Electrodynamometer Meter Movement

The electrodynamometer can be used to measure alternating or direct voltage and current. It operates on the same principles as the permanent magnet moving coil meter, except that the permanent magnet is replaced by an air core electromagnet. The field of the electrodynamometer is developed by the same current that flows through the moving coil. [Figure 12-160]

Because this movement contains no iron, the electrodynamometer can be used as a movement for both AC and DC instruments. AC can be measured by connecting the stationary and moving coils in series. Whenever the current in the moving coil reverses, the magnetic field produced by the stationary coil reverses. Regardless of the direction of the current, the needle moves in a clockwise direction. However, for either voltmeter or ammeter applications, the electrodynamometer is too expensive to economically compete with the d’Arsonval-type movement.

### Moving Iron Vane Meter

The moving iron vane meter is another basic type of meter. It can be used to measure either AC or DC. Unlike the d’Arsonval meter, which employs permanent magnets, it depends on induced magnetism for its operation. It utilizes the principle of repulsion between two concentric iron vanes, one fixed and one movable, placed inside a solenoid. A pointer is attached to the movable vane. [Figure 12-161]

When current flows through the coil, the two iron vanes become magnetized with North poles at their upper ends and South poles at their lower ends for one direction of current through the coil. Because like poles repel, the unbalanced component of force, tangent to the movable element, causes it to turn against the force exerted by the springs.

The movable vane is rectangular in shape and the fixed vane is tapered. This design permits the use of a relatively uniform scale.

When no current flows through the coil, the movable vane is positioned so that it is opposite the larger portion of the tapered fixed vane, and the scale reading is zero. The amount of magnetization of the vanes depends on the strength of the field, which, in turn, depends on the amount of current flowing through the coil.

The force of repulsion is greater opposite the larger end of the fixed vane than it is nearer the smaller end. Therefore, the movable vane moves toward the smaller end through an angle that is proportional to the magnitude of the coil current. The movement ceases when the force of repulsion is balanced by the restraining force of the spring.

Because the repulsion is always in the same direction (toward the smaller end of the fixed vane), regardless of the direction of current flow through the coil, the moving iron vane instrument operates on either DC or AC circuits.

Mechanical damping in this type of instrument can be obtained by the use of an aluminum vane attached to the shaft so that, as the shaft moves, the vane moves in a restricted air space.

When the moving iron vane meter is used as an ammeter, the coil is wound with relatively few turns of large wire in order to carry the rated current. When the moving iron vane meter is used as a voltmeter, the solenoid is wound with many turns of small wire. Portable voltmeters are made with self-contained series resistance for ranges up to 750 volts. Higher ranges are obtained by the use of additional external multipliers.

Hand generator Ohmmeter Axis O − + R2 R3 RX 0 Inf.

M M G ACB Half-wave rectifier Full-wave rectifier Simple AC voltmeter Full-wave rectifier AC In Pulsing DC AC In Pulsing DC AC In0 0 0 0 0 AC converted to pulsing DC on every positive half-cycle AC converted to pulsing DC on both positive and negative half-cycle The moving iron vane instrument may be used to measure DC but has an error due to residual magnetism in the vanes. Reversing the meter connections and averaging the readings may minimize the error. When used on AC circuits, the instrument has an accuracy of 0.5 percent. Because of its simplicity, relatively low cost, and the fact that no current is conducted to the moving element, this type of movement is used extensively to measure current and voltage in AC power circuits. However, because the reluctance of the magnetic circuit is high, the moving iron vane meter requires much more power to produce full-scale deflection than is required by a d’Arsonval meter of the same range. Therefore, the moving iron vane meter is seldom used in high-resistance low-power circuits.

### Inclined Coil Iron Vane Meter

The principle of the moving iron vane mechanism is applied to the inclined coil type of meter, which can be used to measure both AC and DC. The inclined coil, iron vane meter has a coil mounted at an angle to the shaft. Attached obliquely to the shaft, and located inside the coil, are two soft iron vanes. When no current flows through the coil, a control spring holds the pointer at zero, and the iron vanes lie in planes parallel to the plane of the coil. When current flows through the coil, the vanes tend to line up with magnetic lines passing through the center of the coil at right angles to the plane of the coil. Thus, the vanes rotate against the spring action to move the pointer over the scale.

The iron vanes tend to line up with the magnetic lines regardless of the direction of current flow through the coil. Therefore, the inclined coil, iron vane meter can be used to measure either AC or DC. The aluminum disk and the drag magnets provide electromagnetic damping.

Like the moving iron vane meter, the inclined coil type requires a relatively large amount of current for full-scale deflection and is seldom used in high-resistance low-power circuits.

As in the moving iron vane instruments, the inclined coil instrument is wound with few turns of relatively large wire when used as an ammeter and with many turns of small wire when used as a voltmeter.

Multiplying the volts by the amperes in an AC circuit gives the apparent power: the combination of the true power (which does the work) and the reactive power (which does no work and is returned to the line). Reactive power is measured in units of vars (volt-amperes reactive) or kilovars (kilovolt- amperes reactive (kV AR). When properly connected,

s measure the reactive power. As such, they are called varmeters. [Figure 12-162]

Fixed coils Shunt Movable coils A A B C B C Pointer Control spring Cylindrical coil Moving iron segment Stationary iron segment movement. Figure 12-161. Moving iron vane meter.

Wattmeter Electric power is measured by means of a wattmeter. Because electric power is the product of current and voltage, a wattmeter must have two elements, one for current and the other for voltage. For this reason, wattmeters are usually of the electrodynamometer type. [Figure 12-163]

The movable coil with a series resistance forms the voltage element, and the stationary coils constitute the current element. The strength of the field around the potential coil depends on the amount of current that flows through it. The current, in turn, depends on the load voltage applied across the coil and the high resistance in series with it. The strength of the field around the current coils depends on the amount of current flowing through the load. Thus, the meter deflection is proportional to the product of the voltage across the potential coil and the current through the current coils. The effect is almost the same (if the scale is properly calibrated) as if the voltage applied across the load and the current through the load were multiplied together.

If the current in the line is reversed, the direction of current in both coils and the potential coil is reversed, the net result is that the pointer continues to read up scale. Therefore, this type of wattmeter can be used to measure either AC or DC power.

### Frequency Measurement/Oscilloscope

The oscilloscope is by far one of the more useful electronic measurements available. The viewing capabilities of the oscilloscope make it possible to see and quantify various waveform characteristics, such as phase relationships, amplitudes, and durations. While oscilloscopes come in a variety of configurations and presentations, the basic operation is typically the same. Most oscilloscopes in general bench or shop applications use a cathode-ray tube (CRT), which is the device or screen that displays the waveforms. The CRT is a vacuum instrument that contains an electron gun, which emits a very narrow and focused beam of electrons. A phosphorescent coat applied to the back of the screen forms the screen. The beam is electronically aimed and accelerated so that the electron beam strikes the screen. When the electron beam strikes the screen, light is emitted at the point of impact.

Figure 12-164 shows the basic components of the CRT with a block diagram. The heated cathode emits electrons. The magnitude of voltage on the control grid determines the actual flow of electrons and thus controls the intensity of the electron beam. The acceleration anodes increase the speed of the electrons, and the focusing anode narrows the beam down to a fine point. The surface of the screen is also an anode and assists in the acceleration of the electron beam.

LoadCurrent coil Varmeter Reactor Voltage coil M The purpose of the vertical and horizontal deflection plates is to bend the electron beam and position it to a specific point of the screen. [Figure 12-165] By providing a neutral or zero voltage to a deflection plate, the electron beam is unaffected. By applying a negative voltage to a plate, the electron beam is repelled and driven away from the plate. Finally, by applying a positive voltage, the electron beam is drawing to the plate. Figure 12-165 provides a few possible plate voltage combinations and the resultant beam position.

### Horizontal Deflection

To get a visual representation of the input signal, an internally generated saw-tooth voltage is generated and then applied to the horizontal deflection plates. Figure 12-166 illustrates that the saw-tooth is a pattern of voltage applied, which begins at a negative voltage and increases at a constant rate to a positive voltage. This applied varying voltage draws or traces the electron beam from the far left of the screen to the far right side of the screen. The resulting display is a straight line, if the sweep rate is fast enough. This saw-tooth applied voltage is a repetitive signal so that the beam is repeatedly swept across the tube. The rate at which the saw-tooth voltage goes from negative to positive is determined by the frequency. This rate then establishes the sweep rate of the beam. When the saw-tooth reaches the end of its sweep from left to right, the beam then rapidly returns to the left side and is ready to make another sweep. During this time, the electron beam is stopped or blanked out and does not produce any kind of a trace. This period of time is called flyback.

### Vertical Deflection

If this same signal were applied to the vertical plates, it would also produce a vertical line by causing the beam to trace from the down position to the up position.

### Tracing a Sine Wave

Reproducing the sine wave on the oscilloscope combines both the vertical and horizontal deflection patterns. [Figure 12-167] If the sine wave voltage signal is applied across the vertical deflection plates, the result will be the vertical beam oscillation up and down on the screen. The amount that the beam moves above the centerline depends on the peak value of the voltage.

While the beam is being swept from the left to the right by the horizontal plates, the sine wave voltage is being applied to the vertical plates, causing the form of the input signal to be traced out on the screen.

### Control Features on an Oscilloscope

While there are many different styles of oscilloscopes, which range from the simple to the complex, they all have some controls in common. Apart from the screen and the ON/OFF switch, some of these controls are listed as follows:

• Horizontal Position—allows for the adjustment of the neutral horizontal position of the beam. Use this control to reposition the waveform display in order to have a better view of the wave or to take measurements.

• Vertical Position—moves the traced image up or down allowing better observations and measurements.

• Focus—controls the electron beam as it is aimed and converges on the screen. When the beam is in sharp focus, it is narrowed down to a very fine point and does not have a fuzzy appearance.

• Intensity—essentially the brightness of the trace.

Controlling the flow of electrons onto the screen varies the intensity. Do not keep the intensity too high for extended testing or when the beam is motionless and forms a dot on the screen. This can damage the screen.

• Seconds/Division—a time-based control that sets the horizontal sweep rate. Basically, the switch is used to select the time interval that each division on the horizontal scale represents. These divisions can be seconds, milliseconds, or even microseconds. A simple example would be if the technician had the seconds/ division control set to 10 μS. If this technician is viewing a waveform that has a period of 4 divisions on the screen, then the period would be 40 μS. The frequency of this waveform can then be determined by taking the inverse of the period. In this case, 1⁄40 μS equals a frequency of 25 kHz.

• V olts/Division—used to select the voltage interval that each division on the vertical scale represents. For example, suppose each vertical division was set to equal 10 mV . If a waveform was measured and had a peak value of 4 divisions, then the peak value in voltage would be 40 mV .

• Trigger—The trigger control provides synchronization between the saw-tooth horizontal sweep and the applied signal on the vertical plates. The benefit is that the waveform on the screen appears to be stationary and fixed and not drifting across the screen. A triggering circuit is used to initiate the start of a sweep rather than CRT base Anode ScreenMatingconnector Horizontal deflection plates (H)Preaccelerating anode (A1)

Cathode (K) & heater Control grid Vertical deflection plates (V)

Accelerating anode (A3)

Electron gun e e e e e e e e e e e e e e e e e e e e R Current coil M Potential coil Load the fixed saw-tooth sweep rate. In a typical oscilloscope, this triggering signal comes from the input signal itself at a selected point during the signal’s cycle. The horizontal signal goes through one sweep, retraces back to the left side and waits there until it is triggered again by the input signal to start another sweep.

### Flat Panel Color Displays for Oscilloscopes

While the standard CRT design of oscilloscope is still in service, the technology of display and control has evolved into use of the flat panel monitors. Furthermore, the newer oscilloscopes can even be integrated with the common personal computer (PC). [Figure 12-168] Some of the features of this technology include easy data capture, data transfer, documentation, and data analysis. Hand-held oscilloscopes are now available that can perform the functions of larger bench type equipment but are mobile and great tools for trouble shooting. [Figure 12-169]

### Digital Multimeter

Traditionally, the meters that technicians have used have been the analog voltmeter, ammeter, and the ohmmeter. These have usually been combined into the same instrument and called a multimeter or a VOM (volt-ohm-milliammeter). This approach has been both convenient and economical. Digital multimeters (DMM) and digital voltmeters (DVM) are more common due to their ease of use. These meters are easier to read and provide greater accuracy when compared to the older analog units with needle movement. The multimeter’s single-coil movement requires a number of scales, which are not always easy to read accurately. In addition, the loading characteristics due to the internal resistance sometimes affect the circuit and the measurements. Not only does the DVM offer greater accuracy and less ambiguity, but also higher input resistance, which has less of a loading effect and influence on a circuit.

## 2. 中文翻译

<!-- TODO: 逐段翻译，段数与上面严格一一对应（57 段）。专业术语按行业惯例，数字与缩写保留。 -->

## 3. 专业词汇

<!-- TODO: 用表格 | 英文 | 词性 | 中文 | 本节语境 |，4~8 行。优先选下面 Glossary 里的词（本节原文出现过的）：
- Addition —— The process in which the value of one number is added to the value of another.
- Ammeter —— An instrument for measuring electric current in amperes.
- Apparent power —— That power apparently available for use in an AC circuit containing a reactive component. It is the product of effective voltage times the effective current, ex
- Current —— The flow of electrical charge.
- Division —— The process of finding how many times one number (the divisor) is contained in another number (the dividend).
- Force —— The intensity of an impetus, or the intensity of an input.
- Frequency —— The number of cycles (on/off) completed per unit of time. Usually expressed in Hertz.
- Ohmmeter —— A current measuring instrument that provides its own source (self-excited) of power.
-->

## 4. 语法解析

<!-- TODO: 2~4 个语法点，格式：
### ① 语法点名称
**原句**：<必须逐字来自第 1 节原文>
**拆解**：主/谓/宾、从句、非谓语等成分分析
**要点**：为什么这样用、易错点、可迁移的搭配
-->
