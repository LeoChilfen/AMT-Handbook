# Fire Detection/Overheat Systems

> 机体 Ch 17 · Fire Detection/Overheat Systems · 原文 PDF 第 974 页

## 1. 原文

A fire detection system should signal the presence of a fire. Units of the system are installed in locations where there are greater possibilities of a fire. Three detector system types in common use are the thermal switch, thermocouple, and the continuous loop.

### Thermal Switch System

A number of detectors, or sensing devices, are available. Many older-model aircraft still operating have some type of thermal switch system or thermocouple system. A thermal switch system has one or more lights energized by the aircraft power system and thermal switches that control operation of the light(s). These thermal switches are heat-sensitive units that complete electrical circuits at a certain temperature. They are connected in parallel with each other but in series with the indicator lights. If the temperature rises above a set value in any one section of the circuit, the thermal switch closes, completing the light circuit to indicate a fire or overheat condition. No set number of thermal switches is required; the exact number is usually determined by the aircraft manufacturer. On some installations, all the thermal detectors are connected to one light; on others, there may be one thermal switch for each indicator light.

Some warning lights are push-to-test lights. The bulb is tested by pushing it in to check an auxiliary test circuit. The circuit shown in Figure 17-1 includes a test relay. With the relay contact in the position shown, there are two possible paths for current flow from the switches to the light. This is an additional safety feature. Energizing the test relay completes a series circuit and checks all the wiring and the light bulb. Also included in the circuit shown in Figure 17-1 is a dimming relay. By energizing the dimming relay, the circuit is altered to include a resistor in series with the light. In some installations, several circuits are wired through the dimming relay, and all the warning lights may be dimmed at the same time.

### Thermocouple System

The thermocouple fire warning system operates on an entirely different principle from the thermal switch system. A thermocouple depends on the rate of temperature rise and does not give a warning when an engine slowly overheats or a short circuit develops. The system consists of a relay box, warning lights, and thermocouples. The wiring system of these units may be divided into the following circuits: 1. Detector circuit. 2. Alarm circuit. 3. Test circuit.

These circuits are shown in Figure 17-2. The relay box contains two relays, the sensitive relay and the slave relay, and the thermal test unit. Such a box may contain from one to eight identical circuits, depending on the number of potential fire zones. The relays control the warning lights. In turn, the thermocouples control the operation of the relays. The circuit consists of several thermocouples in series with each other and with the sensitive relay.

The thermocouple is constructed of two dissimilar metals, such as chromel and constantan. The point at which these metals are joined and exposed to the heat of a fire is called a hot junction. There is also a reference junction enclosed in a dead air space between two insulation blocks. A metal cage surrounds the thermocouple to give mechanical protection without hindering the free movement of air to the hot junction. If the temperature rises rapidly, the thermocouple produces a voltage because of the temperature difference between the reference junction and the hot junction. If both junctions are heated at the same rate, no voltage results. In the engine compartment, there is a normal, gradual rise in temperature from engine operation; because it is gradual, both junctions heat at the same rate and no warning signal is given. If there is a fire, however, the hot junction heats more rapidly than the reference junction. The ensuing voltage causes a current to flow within the detector circuit. Any time the current is greater than 4 milliamperes (0.004 ampere), the sensitive relay closes. This completes a circuit from the aircraft power system to the coil of the slave relay. The slave relay then closes and completes the circuit to the warning light to give a visual fire warning.

The total number of thermocouples used in individual detector circuits depends on the size of the fire zones and the total circuit resistance, which usually does not exceed 5 ohms. As shown in Figure 17-2, the circuit has two resistors. The resistor connected across the slave relay terminals absorbs the coil’s self-induced voltage to prevent arcing across the points of the sensitive relay. The contacts of the sensitive relay are so fragile that they burn, or weld, if arcing is permitted.

When the sensitive relay opens, the circuit to the slave relay is interrupted and the magnetic field around its coil collapses. The coil then gets a voltage through self-induction but, with the resistor across the coil terminals, there is a path for any current flow as a result of this voltage, eliminating arcing at the sensitive relay contacts.

### Continuous-Loop Systems

Transport aircraft almost exclusively use continuous thermal sensing elements for powerplant and wheel well protection. These systems offer superior detection performance and coverage, and they have the proven ruggedness to survive in the harsh environment of modern turbofan engines.

A continuous-loop detector or sensing system permits more complete coverage of a fire hazard area than any of the spot-type temperature detectors. Two widely used types of continuous-loop systems are the thermistor type detectors, such as the Kidde and the Fenwal systems, and the pneumatic pressure detector, such as the Lingberg system. (Lindberg system is also known as Systron-Donner and, more recently, Meggitt Safety Systems.)

#### Fenwal System

The Fenwal system uses a slender Inconel tube packed with thermally sensitive eutectic salt and a nickel wire center conductor. Lengths of these sensing elements are connected in series to a control unit. The elements may be of equal or varying length and of the same or different temperature settings. The control unit, operating directly from the power source, impresses a small voltage on the sensing elements. When an overheat condition occurs at any point along the element length, the resistance of the eutectic salt within the sensing element drops sharply, causing current to flow between the outer sheath and the center conductor. This current flow is sensed by the control unit, which produces a signal to actuate the output relay and activate the alarms. When the fire has been extinguished or the critical temperature lowered below the set point, the Fenwal system automatically returns to standby alert, ready to detect any subsequent fire or overheat condition. The Fenwal system may be wired to employ a loop circuit. In this case, should an open circuit occur, the system still signals fire or overheat. If multiple open circuits occur, only that section between breaks becomes inoperative.

#### Kidde System

In the Kidde continuous-loop system, two wires are embedded in an Inconel tube filled with a thermistor core material. Two electrical conductors go through the length of the core. One conductor has a ground connection to the tube, and the other conductor connects to the fire detection control unit. As the temperature of the core increases, electrical resistance to the ground decreases. The fire detection control unit monitors this resistance. If the resistance decreases to the overheat set point, an overheat indication occurs in the flight deck. Typically, a 10-second time delay is incorporated for the overheat indication. If the resistance decreases more to the fire set point, a fire warning occurs. When the fire or overheat condition is gone, the resistance of the core material increases to the reset point and the flight deck indications disappear. The rate of change of resistance identifies an electrical short or a fire. The resistance decreases more quickly with an electrical short than with a fire. In some aircraft, in addition to fire and overheat detection, the Kidde continuous-loop system can supply nacelle temperature data to the airplane condition monitoring function of the aircraft in-flight monitoring system (AIMS).

Sensing Element The resistance of a sensor varies inversely as it is heated; as sensor temperature is increased, its resistance decreases. Each sensor is composed of two wires embedded in thermistor material that is encased in a heavy wall Inconel tube for high strength at elevated temperatures. The electrical connectors at each end of the sensor are ceramic insulated. The Inconel tubes are shrouded in a perforated stainless-steel tube and supported by Teflon-impregnated asbestos bushings at intervals. The shroud protects the sensor from breakage due to vibration, abrasion against airplane structure, and damage from maintenance activity.

The resistance of a sensor also varies inversely with its length, the increments of length being resistances in parallel. The heating of a short length of sensor out of a given length requires that the short length be heated above the temperature alarm point, so the total resistance of the sensor decreases to the alarm point. This characteristic permits integration of all temperatures throughout the length of the installation rather than sensing only the highest local temperature. The two wires encased within the thermistic material of each Inconel tube form a variable resistance network between themselves, between the detector wire and the Inconel tube, and between each adjacent incremental length of sensor. These variable resistance networks are monitored by the application of 28 volts direct current (DC) to the detector wire from the detector control unit.

Combination Fire & Overheat Warning The analog signal from the thermistor-sensing element permits the control circuits to be arranged to give a two-level response from the same sensing element loop. The first is an overheat warning at a temperature level below the fire warning indicating a general engine compartment temperature rise, such as would be caused by leakage of hot bleed air or combustion gas into the engine compartment. It could also be an early warning of fire and would alert the crew to appropriate action to reduce the engine compartment temperature. The second-level response is at a level above that attainable by a leaking hot gas and is the fire warning.

Temperature Trend Indication The analog signal produced by the sensing element loop as its temperature changes is converted to signals suitable for flight deck display to indicate engine bay temperature increases from normal. A comparison of the readings from each loop system also provides a check on the condition of the fire detection system, because the two loops should normally read alike.

System Test The integrity of the continuous-loop fire detection system may be tested by actuating a test switch in the flight deck that switches one end of the sensing element loop from its control circuit to a test circuit built into the control unit, which simulates the sensing element resistance change due to fire. If the sensing element loop is unbroken, the resistance detected by the control circuit is that of the simulated fire, and the alarm is activated. The test demonstrates, in addition to the continuity of the sensing element loop, the integrity of the alarm indicator circuit and the proper functioning of the control circuits. The thermistic properties of the sensing element remain unchanged for the life of the element (no irreversible changes take place when heated); the element functions properly as long as it is electrically connected to the control unit.

Fault Indication Provision is made in the control unit to output a fault signal which activates a fault indicator whenever the short discriminator circuit detects a short in the sensing element loop. This is a requirement for transport category aircraft because such a short disables the fire detection system.

Dual-Loop Systems Dual-loop systems are two complete basic fire detection systems with their output signals connected so that both must signal to result in a fire warning. This arrangement, called AND logic, results in greatly increased reliability against false fire warnings from any cause. Should one of the two loops be found inoperative at the preflight integrity test, a flight deck selector switch disconnects that loop and allows the signal from the other loop alone to activate the fire warning. Since the single operative loop meets all fire detector requirements, the aircraft can be safely dispatched and maintenance deferred to a more convenient time. However, should one of the two loops become inoperative in flight and a fire subsequently occur, the fire signaling loop activates a flight deck fault signal that alerts the flight crew to select single-loop operation to confirm the possible occurrence of fire.

Automatic Self-Interrogation Dual-loop systems automatically perform the loop switching and decision-making function required of the flight crew upon appearance of the fault indication in the flight deck, a function called automatic self-interrogation. Automatic self-interrogation eliminates the fault indication and assures the immediate appearance of the fire indication should fire occur while at least one loop of the dual-loop system is operative. Should the control circuit from a single-loop signal fire, the self-interrogation circuit automatically tests the functioning of the other loop. If it tests operative, the circuit suppresses the fire signal because the operative loop would have signaled if a fire existed. If, however, the other loop tests inoperative, the circuit outputs a fire signal. The interrogation and decision takes place in milliseconds, so that no delay occurs if a fire actually exists.

Support Tube Mounted Sensing Elements For those installations where it is desired to mount the sensing elements on the engine, and in some cases, on the aircraft structure, the support tube mounted element solves the problem of providing sufficient element support points and greatly facilitates the removal and reinstallation of the sensing elements for engine or system maintenance.

Most modern installations use the support tube concept of mounting sensing elements for better maintainability, as well as increased reliability. The sensing element is attached to a prebent stainless steel tube by closely spaced clamps and bushings, where it is supported from vibration damage and protected from pinching and excessive bending. The support tube-mounted elements can be furnished with either single or dual sensing elements.

Being prebent to the designed configuration assures its installation in the aircraft precisely in its designed location, where it has the necessary clearance to be free from the possibility of the elements chafing against engine or aircraft structure. The assembly requires only a few attachment points and, should its removal for engine maintenance be necessary, it is quickly and easily accomplished. Should the assembly require repair or maintenance, it is easily replaced with another assembly, leaving the repair for the shop. Should a sensing element be damaged, it is easily replaced in the assembly.

Fire Detection Control Unit (Fire Detection Card) The control unit for the simplest type of system typically contains the necessary electronic resistance monitoring and alarm output circuits housed in a hermetically sealed aluminum case fitted with a mounting bracket and electrical connector. For more sophisticated systems, control modules are employed that contain removable control cards with circuitry for individual hazard areas and/or unique functions. In the most advanced applications, the detection system circuitry controls all aircraft fire protection functions, including fire detection and extinguishing for engines, APUs, cargo bays, and bleed-air systems.

### Pressure Type Sensor Responder Systems

Some smaller turboprop aircraft are outfitted with pneumatic single point detectors. The design of these detectors is based on the principles of gas laws. The sensing element consists of a closed, helium-filled tube connected at one end to a responder assembly. As the element is heated, the gas pressure inside the tube increases until the alarm threshold is reached. At this point, an internal switch closes and reports an alarm to the flight deck. Continuous fault monitoring is included. This type of sensor is designed as a single-sensor detection system and does not require a control unit.

#### Pneumatic Continuous-Loop Systems

The pneumatic continuous-loop systems are also known by their manufacturers’ names Lindberg, Systron-Donner, and Meggitt Safety Systems. These systems are used for engine fire detection of transport type aircraft and have the same function as the Kidde system; however, they work on a different principle. They are typically used in a dual-loop design to increase reliability of the system.

The pneumatic detector has two sensing functions. It responds to an overall average temperature threshold and to a localized discrete temperature increase caused by impinging flame or hot gasses. Both the average and discrete temperature are factory set and are not field adjustable.

Averaging Function The fire/overheat detector serves as a fixed-volume device filled with helium gas. The helium gas pressure inside the detector increases in proportion to the absolute temperature and operates a pressure diaphragm that closes an electrical contact, actuating the alarm circuit. The pressure diaphragm within the responder assembly serves as one side of the electrical alarm contact and is the only moving part in the detector. The alarm switch is preset at an average temperature. Typical temperature ranges for average temperature settings are 200 °F (93 °C) to 850 °F (454 °C).

Discrete Function The fire/overheat detector’s sensor tube also contains a hydrogen-filled core material. Large quantities of hydrogen gas are released from the detector core whenever a small section of the tube is heated to the preset discrete temperature or higher. The core outgassing increases the pressure inside the detector and actuates the alarm switch. Both the averaging and discrete functions are reversible. When the sensor tube is cooled, the average gas pressure is lowered, and the discrete hydrogen gas returns to the core material. The reduction of internal pressure allows the alarm switch to return to its normal position, opening the electrical alarm circuit.

Figure 17-8 shows a typical aircraft fire detection system in which a control module monitors two loops of up to four pneumatic detectors each, connected in parallel. The control module responds directly to an alarm condition and continuously monitors the wiring and integrity of each loop. The normally open alarm switch closes upon an overheat or fire condition, causing a short circuit between terminals A and C. During normal operation, a resistance value is maintained across the terminals by a normally closed integrity switch. Loss of sensor gas pressure opens the integrity switch, creating an open circuit across the terminals of the faulted detector. In addition to the pressure-activated alarm switch, there is a second integrity switch in the detector that is held closed by the averaging gas pressure at all temperatures down to –65 °F (–54 °C). If the detector should develop a leak, the loss of gas pressure would allow the integrity switch to open and signal a lack of detector integrity. The system then does not operate during test.

### Fire Zones

Powerplant compartments are classified into zones based on the airflow through them.

1. Class A zone—area of heavy airflow past regular arrangements of similarly shaped obstructions. The power section of a reciprocating engine is usually of this type.

2. Class B zone—area of heavy airflow past aerodynamically clean obstructions. Included in this type are heat exchanger ducts, exhaust manifold shrouds, and areas where the inside of the enclosing cowling or other closure is smooth, free of pockets, and adequately drained so leaking flammables cannot puddle. Turbine engine compartments may be considered in this class if engine surfaces are aerodynamically clean and all airframe structural formers are covered by a fireproof liner to produce an aerodynamically clean enclosure surface.

3. Class C zone—area of relatively low airflow. An engine accessory compartment separated from the power section is an example of this type of zone.

4. Class D zone—area of very little or no airflow. These include wing compartments and wheel wells where little ventilation is provided.

5. Class X zone—area of heavy airflow and of unusual construction, making uniform distribution of the extinguishing agent very difficult. Areas containing deeply recessed spaces and pockets between large structural formers are of this type. Tests indicate agent requirements to be double those for Class A zones.

## 2. 中文翻译

TODO

## 3. 专业词汇

| 英文 | 词性 | 中文 | 本节语境 |
| --- | --- | --- | --- |
TODO

## 4. 语法解析

TODO
