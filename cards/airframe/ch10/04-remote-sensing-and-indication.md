# Remote Sensing & Indication

> 机体 Ch 10 · Remote Sensing & Indication · 原文 PDF 第 543 页

## 1. 原文

It is often impractical or impossible to utilize direct reading gauges for information needed to be conveyed in the flight deck. Placing sensors at the most suitable location on the airframe or engine and transmitting the collected data electrically through wires to the displays in the flight deck is a widely used method of remote-sensing and indicating on aircraft. Many remote sensing instrument systems consist simply of the sensing device, transmitter unit, and the flight deck indicator unit connected to each other by wires. For pressure flight instruments, the ADC and pickup devices (pitot tubes, static vents, etc.) comprise the sensing and transmitter unit. Many aircraft collect sensed data in dedicated engine and airframe computers. There, the information can be processed. An output section of the computer then transmits it electrically or digitally to the flight deck for display. Remote-sensing instrument systems operate with high reliability and accuracy. They are powered by the aircraft’s electrical system.

Small electric motors inside the instrument housings are used to position the pointers, instead of direct-operating mechanical linkages. They receive electric current from the output section of the ADC or other computers. They also receive input from sensing transmitters or transducers that are remotely located on the aircraft. By varying the electric signal, the motors are turned to the precise location needed to reflect the correct indication. Direct electric transmission of information from different types of sensors is accomplished with a few reliable and relatively simple techniques. Note that digital flight deck displays receive all of their input from a digital air data computer (DADC) and other computers, via a digital data bus and do not use electric motors. The data packages transmitted via the bus contain the instructions on how to illuminate the display screen.

### Synchro-Type Remote-Indicating Instruments

A synchro system is an electric system used for transmitting information from one point to another. The word “synchro” is a shortened form of the word “synchronous,” and refers to any one of a number of similarly operating two-unit electrical systems capable of measuring, transmitting, and indicating a certain parameter on the aircraft. Most position-indicating instruments are designed around a synchro system, such as the flap position indicator. Fluid pressure indicators also commonly use synchro systems. Synchro systems are used as remote position indicators for landing gear, autopilot systems, radar, and many other remote-indicating applications. The most common types of synchro system are the autosyn, selsyn, and magnesyn synchro systems.

These systems are similar in construction, and all operate by exploiting the consistent relationship between electricity and magnetism. The fact that electricity can be used to create magnetic fields that have definite direction, and that magnetic fields can interact with magnets and other electromagnetic fields, is the basis of their operation.

#### DC Selsyn Systems

On aircraft with direct current (DC) electrical systems, the DC selsyn system is widely used. As mentioned, the selsyn system consists of a transmitter, an indicator, and connecting wires. The transmitter consists of a circular resistance winding and a rotatable contact arm. The rotatable contact arm turns on a shaft in the center of the resistance winding. The two ends of the arm are brushes and always touch the winding on opposite sides. On position indicating systems, the shaft to which the contact arm is fastened protrudes through the end of transmitter housing and is attached to the unit whose position is to be transmitted (e.g., flaps, landing gear). The transmitter is often connected to the moving unit through a mechanical linkage. As the unit moves, it causes the transmitter shaft to turn. The arm is turned so that voltage is applied through the brushes to any two points around the circumference of the resistance winding. The rotor shaft of DC selsyn systems, measuring other kinds of data, operates the same way, but may not protrude outside of the housing. The sensing device, which imparts rotary motion to the shaft, could be located inside the transmitter housing.

Referring to Figure 10-47 , note that the resistance winding of the transmitter is tapped off in three fixed places, usually 120° apart. These taps distribute current through the toroidal windings of the indicator motor. When current flows through these windings, a magnetic field is created. Like all magnetic fields, a definite north and south direction to the field exists.

As the transmitter rotor shaft is turned, the voltage-supplying contact arm moves. Because it contacts the transmitter resistance winding in different positions, the resistance between the supply arm and the various tapoffs changes. This causes the voltage flowing through the tapoffs to change as the resistance of sections of the winding become longer or shorter. The result is that varied current is sent via the tapoffs to the three windings in the indicator motor.

The resultant magnetic field created by current flowing through the indicator coils changes as each receives varied current from the tapoffs. The direction of the magnetic field also changes. Thus, the direction of the magnetic field across the indicating element corresponds in position to the moving arm in the transmitter. A permanent magnet is attached to the centered rotor shaft in the indicator, as is the indicator pointer. The magnet aligns itself with the direction of the magnetic field and the pointer does as well. Whenever the magnetic field changes direction, the permanent magnet and pointer realign with the new position of the field. Thus, the position of the aircraft device is indicated.

Landing gear contain mechanical devices that lock the gear up, called an up-lock, or down, called a down-lock. When the DC selsyn system is used to indicate the position of the landing gear, the indicator can also show that the up-lock or down-lock is engaged. This is done by again varying the current flowing through the indicator’s coils. Switches located on the actual locking devices close when the locks engage. Current from the selsyn system described above flows through the switch and a small additional circuit. The circuit adds an additional resistor to one of the transmitter winding sections created by the rotor arm and a tapoff. This changes the total resistance of that section. The result is a change in the current flowing through one of the indicator’s motor coils. This, in turn, changes the magnetic field around that coil. Therefore, the combined magnetic field created by all three motor coils is also affected, causing a shift in the direction of the indicator’s magnetic field. The permanent magnet and pointer align with the new direction and shift to the locked position on the indicator dial. Figure 10-48 shows a simplified diagram of a lock switch in a three-wire selsyn system and an indicator dial.

#### AC Synchro Systems

Aircraft with alternating current (AC) electrical power systems make use of autosyn or magnasysn synchro remote indicating systems. Both operate in a similar way to the DC selsyn system, except that AC power is used. Thus, they make use of electric induction, rather than resistance current flows defined by the rotor brushes. Magnasyn systems use permanent magnet rotors such as those found in the DC selsyn system. Usually, the transmitter magnet is larger than the indicator magnet, but the electromagnetic response of the indicator rotor magnet and pointer remains the same. It aligns with the magnetic field set up by the coils, adopting the same angle of deflection as the transmitter rotor.

Autosyn systems are further distinguished by the fact that the transmitter and indicator rotors used are electro-magnets rather than permanent magnets. Nonetheless, like a permanent magnet, an electro-magnet aligns with the direction of the magnetic field created by current flowing through the stator coils in the indicator. Thus, the indicator pointer position mirrors the transmitter rotor position.

AC synchro systems are wired differently than DC systems. The varying current flows through the transmitter and indicator stator coils are induced as the AC cycles through zero and the rotor magnetic field flux is allowed to flow. The important characteristic of all synchro systems is maintained by both the autosyn and magnasyn systems. That is, the position of the transmitter rotor is mirrored by the rotor in the indicator. These systems are used in many of the same applications as the DC systems and more. Since they are usually part of instrumentation for high performance aircraft, adaptations of autosyn and magnasyn synchro systems are frequently used in directional indicators and in autopilot systems.

#### Remote Indicating Fuel & Oil Pressure Gauges

Fuel and oil pressure indications can be conveniently obtained through the use of synchro systems. As stated previously, running fuel and oil lines into the cabin to direct reading gauges is not desirable due to the possibility of leaking fluid. Additionally, there is an increased risk of fire in the cabin.

By locating the transmitter of a synchro system remotely, fluid pressure can be directed into it without a long tubing run. Inside the transmitter, the motion of a pressure bellows can be geared to the transmitter rotor in such a way as to make the rotor turn. As in all synchros, the transmitter rotor turns proportional to the pressure sensed, which varies the voltages set up in the resistor windings of the synchro stator. These voltages are transmitted to the indicator coils that develop the magnetic field that positions the pointer.

Often on twin-engine aircraft, synchro mechanisms for each engine can be used to drive separate pointers on the same indicator. By placing the coils one behind the other, the pointer shaft from the rear indicator motor can be sent through the hollow shaft of the forward indicator motor. Thus, each pointer responds with the magnet’s alignment in its own motor’s magnetic field while sharing the same gauge housing. Labeling the pointer’s engine 1 or 2 removes any doubt about which indicator pointer is being observed. A similar principle is employed in an indicator that has side-by-side indications for different parameters, such as oil pressure and fuel pressure in the same indicator housing. Each parameter has its own synchro motor for positioning its pointer.

Aircraft with digital instrumentation make use of pressure-sensitive solid-state sensors that output digital signals for collection and processing by dedicated engine and airframe computers. Others may retain their analog sensors but may forward this information through an analog to digital converter unit from which the appropriate computer can obtain digital information to process and illuminate the digital display. Many more instruments utilize the synchro remote-indicating systems described in this section or similar synchros. Sometimes simple, more suitable, or less expensive technologies are also employed.

## 2. 中文翻译

TODO

## 3. 专业词汇

| 英文 | 词性 | 中文 | 本节语境 |
| --- | --- | --- | --- |
TODO

## 4. 语法解析

TODO
