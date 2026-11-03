# Alternators

> 通用 Ch 12 · Alternators · 原文 PDF 第 596 页

## 1. 原文

### Basic Alternators & Classifications

An electrical generator is a machine that converts mechanical energy into electrical energy by electromagnetic induction. A generator that produces alternating current is referred to as an AC generator and, through combination of the words “alternating” and “generator,” the word “alternator” has come into widespread use. In some areas, the word “alternator” is applied only to small AC generators. This handbook treats the two terms synonymously and uses the term “alternator” to distinguish between AC and DC generators.

The major difference between an alternator [Figure 12-317] and a DC generator is the method of connection to the external circuit. The alternator is connected to the external circuit by slip rings, but the DC generator is connected by a commutator.

### Method of Excitation

One means of classification is by the type of excitation system used. In alternators used on aircraft, excitation can be affected by one of the following methods:

1. A direct connected, DC generator. This system consists of a DC generator fixed on the same shaft with the AC generator. A variation of this system is a type of alternator that uses DC from the battery for excitation, after which the alternator is self-excited.

2. By transformation and rectification from the AC system. This method depends on residual magnetism for initial AC voltage buildup, after which the field is supplied with rectified voltage from the AC generator.

3. Integrated brushless type. This arrangement has a DC generator on the same shaft with an AC generator. The excitation circuit is completed through silicon rectifiers rather than a commutator and brushes. The rectifiers are mounted on the generator shaft and their output is fed directly to the AC generator’s main rotating field.

### Number of Phases

Another method of classification is by the number of phases of output voltage. AC generators may be single-phase, two-phase, three-phase, or even six-phase and more. In the Compensating winding Main field Compensating winding Main field motor.

electrical systems of aircraft, the three-phase alternator is by far the most common.

### Armature or Field Rotation

Still another means of classification is by the type of stator and rotor used. From this standpoint, there are two types of alternators: the revolving armature-type and the revolving field-type. The revolving armature alternator is similar in construction to the DC generator in that the armature rotates through a stationary magnetic field. The revolving armature alternator is found only in alternators of low-power rating and generally is not used. In the DC generator, the EMF generated in the armature windings is converted into a unidirectional voltage (DC) by means of the commutator. In the revolving armature-type of alternator, the generated AC voltage is applied unchanged to the load by means of slip rings and brushes.

The revolving field type of alternator has a stationary armature winding (stator) and a rotating field winding (rotor). [Figure 12-318] The advantage of having a stationary armature winding is that the armature can be connected directly to the load without having sliding contacts in the load circuit. A rotating armature would require slip rings and brushes to conduct the load current from the armature to the external circuit. Slip rings have a relatively short service life and arc over is a continual hazard; therefore, high voltage alternators are usually of the stationary armature, rotating field-type. The voltage and current supplied to the rotating field are relatively small, and slip rings and brushes for this circuit are adequate. The direct connection to the armature circuit makes possible the use of large cross-section conductors, adequately insulated for high voltage. Since the rotating field alternator is used almost universally in aircraft systems, this type is explained in detail, as a single-phase, two-phase, and three-phase alternator.

#### Single-Phase Alternator

Since the EMF induced in the armature of a generator is alternating, the same sort of winding can be used on an alternator as on a DC generator. This type of alternator is known as a single-phase alternator, but since the power delivered by a single-phase circuit is pulsating, this type of circuit is objectionable in many applications.

A single-phase alternator has a stator made up of a number of windings in series, forming a single circuit in which an output voltage is generated. [Figure 12-319] The stator has four polar groups evenly spaced around the stator frame. The rotor has four poles with adjacent poles of opposite polarity. As the rotor revolves, AC voltages are induced in the stator windings. Since one rotor pole is in the same position relative to a stator winding as any other rotor pole, all stator polar groups are cut by equal numbers of magnetic lines of force at any time.

As a result, the voltages induced in all the windings have the same amplitude, or value, at any given instant. The four stator windings are connected to each other so that the AC voltages are in phase or “series adding.” Assume that rotor pole 1, a South pole, induces a voltage in the direction indicated by the arrow in stator winding 1. Since rotor pole 2 is a North pole, it induces a voltage in the opposite direction in stator coil 2 with respect to that in coil 1. For the two induced voltages to be in series addition, the two coils are connected as shown in Figure 12-319 . Applying the same reasoning, the voltage induced in stator coil 3 (clockwise rotation of the field) is the same direction (counterclockwise) as the voltage induced in coil 1.

A B P9 P8 P7 P6 P5 P4 P3 P2 P1 aircraft.

Similarly, the direction of the voltage induced in winding 4 is opposite to the direction of the voltage induced in coil 1. All four stator coil groups are connected in series so that the voltages induced in each winding add to give a total voltage that is four times the voltage in any one winding.

#### Two-Phase Alternator

Two-phase alternators have two or more single-phase windings spaced symmetrically around the stator. In a two-phase alternator, there are two single-phase windings spaced physically so that the AC voltage induced in one is 90° out of phase with the voltage induced in the other. The windings are electrically separate from each other. When one winding is being cut by maximum flux, the other is being cut by no flux. This condition establishes a 90° relation between the two phases.

#### Three-Phase Alternator

A three-phase, or polyphase circuit, is used in most aircraft alternators, instead of a single or two-phase alternator. The three-phase alternator has three single-phase windings spaced so that the voltage induced in each winding is 120° out of phase with the voltages in the other two windings. A schematic diagram of a three-phase stator showing all the coils becomes complex and difficult to see what is actually happening.

A simplified schematic diagram showing each of three phases is illustrated in Figure 12-320. The rotor is omitted for simplicity. The waveforms of voltage are shown to the right of the schematic. The three voltages are 120° apart and are similar to the voltages that would be generated by three single-phase alternators whose voltages are out of phase by angles of 120°. The three phases are independent of each other.

### Wye Connection (Three-Phase)

Rather than have six leads from the three-phase alternator, one of the leads from each phase may be connected to form a common junction. The stator is then called wye or star connected. The common lead may or may not be brought out of the alternator. If it is brought out, it is called the neutral lead. The simplified schematic shows a wye connected stator with the common lead not brought out. [Figure 12-321A] Each load is connected across two phases in series. Thus, RAB is connected across phases A and B in series; RAC is connected across phases A and C in series; and RBC is connected across phases B and C in series. Therefore, the voltage across each load is larger than the voltage across a single phase. The total voltage, or line voltage, across any two phases is the vector sum of the individual phase voltages. For balanced conditions, the line voltage is 1.73 times the phase voltage. Since there is only one path for current in a line wire and the phase to which it is connected, the line current is equal to the phase current.

### Delta Connection (Three-Phase)

A three-phase stator can also be connected so that the phases are connected end to end. [Figure 12-321B] This arrangement is called a delta connection. In a delta connection, the voltages are equal to the phase voltages; the line currents are equal to the vector sum of the phase currents; and the line current is equal to 1.73 times the phase current when the loads are balanced. For equal loads (equal output), the delta connection supplies increased line current at a value of line voltage equal to phase voltage, and the wye connection supplies increased line voltage at a value of line current equal to phase current.

### Alternator Rectifier Unit

A type of alternator used in the electrical system of many aircraft weighing less than 12,500 pounds is shown in a DC generator, since it is used in DC systems. Although its output is a DC voltage, it is an alternator rectifier unit. This type of alternator rectifier is a self-excited unit but does not contain a permanent magnet. The excitation for starting is 0 +e Time axis –e N N S S 113 3 2 2 4 4 Rotating field S N Armature Circuit Slip rings To exciter– + field.

obtained from the battery; immediately after starting, the unit is self-exciting. Cooling air for the alternator is conducted into the unit by a blast air tube on the air inlet cover.

The alternator is directly coupled to the aircraft engine by means of a flexible drive coupling. The output of the alternator portion of the unit is three-phase alternating current, derived from a three-phase, delta connected system incorporating a three-phase, full-wave bridge rectifier. [Figure 12-323] This unit operates in a speed range from 2,100 to 9,000 rpm, with a DC output voltage of 26–29 volts and 125 amperes.

### Brushless Alternator

This design is more efficient because there are no brushes to wear down or to arc at high altitudes. This generator consists of a pilot exciter, an exciter, and the main generator system. The need for brushes is eliminated by using an integral exciter with a rotating armature that has its AC output rectified for the main AC field, which is also of the rotating type. [Figure 12-324]

The pilot exciter is an 8-pole, 8,000 rpm, 533 cps, AC generator. The pilot exciter field is mounted on the main generator rotor shaft and is connected in series with the main generator field. The pilot exciter armature is mounted on the main generator stator. The AC output of the pilot exciter is supplied to the voltage regulator, where it is rectified and controlled, and is then impressed on the exciter field winding to furnish excitation for the generator.

The exciter is a small AC generator with its field mounted on the main generator stator and its three-phase armature mounted on the generator rotor shaft. Included in the exciter field are permanent magnets mounted on the main generator stator between the exciter poles.

The exciter field resistance is temperature compensated by a thermistor. This aids regulation by keeping a nearly constant resistance at the regulator output terminals. The exciter output is rectified and impressed on the main generator field and the pilot exciter field. The exciter stator has a stabilizing field, which is used to improve stability and to prevent voltage regulator over-corrections for changes in generator output voltage.

The AC generator shown in Figure 12-324 is a 6-pole, 8,000 rpm unit having a rating of 31.5 kilovoltamperes (kV A), 115⁄200 volts, 400 cps. This generator is three-phase, 4 wire, wye connected with grounded neutrals. By using an integral AC exciter, the necessity for brushes within the generator has been eliminated. The AC output of the rotating exciter armature is fed directly into the three-phase, full-wave, rectifier bridge located inside the rotor shaft, which uses high-temperature silicon rectifiers. The DC output from the rectifier bridge is fed to the main AC generator rotating field.

V oltage regulation is accomplished by varying the strength of the AC exciter stationary fields. Polarity reversals of the AC generator are eliminated and radio noise is minimized by the absence of the brushes. A noise filter mounted on the alternator further reduces any existing radio noise. The rotating pole structure of the generator is laminated from steel punchings, containing all six poles and a connecting hub section. This provides optimum magnetic and mechanical properties.

Some alternators are cooled by circulating oil through steel tubes. The oil used for cooling is supplied from the constant speed drive assembly. Ports located in the flange connecting the generator and drive assemblies make oil flow between the constant speed drive and the generator possible.

A B C A 0 +e –e B C Wye connection Delta connection RB RAAC B RC RBC RABAC B RAC A B output waveforms.

V oltage is built up by using permanent magnet interpoles in the exciter stator. The permanent magnets assure a voltage buildup, precluding the necessity of field flashing. The rotor of the alternator may be removed without causing loss of the alternator’s residual magnetism.

### Alternator Frequency

The frequency of the alternator voltage depends upon the speed of rotation of the rotor and the number of poles. The faster the speed, the higher the frequency; the lower the speed, the lower the frequency. The more poles on the rotor, the higher the frequency for a given speed. When a rotor has rotated through an angle so that two adjacent rotor poles (a North and a South pole) have passed one winding, the voltage induced in that winding has varied through one complete cycle. For a given frequency, the greater the number of pairs of poles, the lower the speed of rotation. A two-pole alternator rotates at twice the speed of a four-pole alternator for the same frequency of generated voltage. The frequency of the alternator in cycles per minute (cpm) is related to the number of poles and the speed, as expressed by the equation:

F = × = P N PNN 60 120 Where: P is the number of poles per phase f is the frequency in cps N is the rated speed in rpm For example, a 2-pole, 3,600 rpm alternator has a frequency of:

= 60 cps 2 × 3,600120 A 4-pole, 1,800 rpm alternator has the same frequency; a 6-pole, 500 rpm alternator has a frequency of:

= 25 cps 6 × 500120 A 12-pole, 4,000 rpm alternator has a frequency of:

= 400 cps12 × 4,000120

### Starter Generator

Many turbine-powered aircraft use a starter generator that acts like a starter during the start of the engine and when the engine is online it acts like a Generator. [Figure 12-325] The main advantage of the starter generator is saving weight by eliminating a separate starter that is only used during the start. Initially used on small turboprops and light jets but large units are now installed on the B787 aircraft engines to power the main engines and power the electrical system.

### Alternator Rating

The maximum current that can be supplied by an alternator depends upon the maximum heating loss (I2R power loss) that can be sustained in the armature and the maximum heating loss that can be sustained in the field. The armature current of an alternator varies with the load. This action is similar to that of A 12 pole, 4,000 rpm alternator has a frequency of DC generators. In AC generators, however, lagging power factor loads tend to demagnetize the field of an alternator, and terminal voltage is maintained only by increasing DC field current. For this reason, AC generators are usually rated according to kV A, power factor, phases, voltage, and frequency. One generator, for example, may be rated at 40 kV A, 208 volts, 400 cycles, three phase, at 75 percent power factor. The kV A indicates the apparent power. This is the kV A output, or the relationship between the current and voltage at which the generator is intended to operate. The power factor is the expression of the E B A G1 L1 C3 C2 CR4 CR5 CR6 CR1 CR2 CR3 + + + – ratio between the apparent power (volt-amperes) and the true or effective power (watts). The number of phases is the number of independent voltages generated. Three-phase generators generate three voltages 120 electrical degrees apart.

### Alternator Maintenance

Maintenance and inspection of alternator systems is similar to that of DC systems. Check the exciter brushes for wear and surfacing. On most large aircraft with two or four alternator systems, each power panel has three signal lights, one connected to each phase of the power bus, so the lamp lights when the panel power is on. The individual buses throughout the airplane can be checked by operating equipment from that particular bus. Consult the manufacturer’s instructions on operation of equipment for the method of testing each bus.

Alternator test stands are used for testing alternators and constant speed drives in a repair facility. They are capable of supplying power to constant speed drive units at input speeds varying from 2,400 rpm to 9,000 rpm.

A typical test stand motor uses 220/440 volt, 60 cycle, three-phase power. Blowers for ventilation, oil coolers, and necessary meters and switches are integral parts of the test stand. A load bank supplies test circuits. An AC motor generator set for ground testing is shown in Figure 12-326.

A typical, portable, AC electrical system test set is an analyzer, consisting of a multirange ohmmeter, a multirange combination AC DC voltmeter, an ammeter with a clip-on current transformer, a vibrating reed type frequency meter, and an unmounted continuity light.

A portable load bank unit furnishes a load similar to that on the airplane for testing alternators, either while mounted in the airplane or on the shop test stand. A complete unit consists of resistive and reactive loads controlled by selector switches and test meters mounted on a control panel. This load unit is compact and convenient, eliminating the difficulty of operating large loads on the airplane while testing and adjusting the alternators and control equipment.

Proper maintenance of an alternator requires that the unit be kept clean and that all electrical connections are tight and in good repair. If the alternator fails to build up voltage as designated by applicable manufacturer’s technical instructions, test the voltmeter first by checking the voltages of other alternators, or by checking the voltage in the suspected alternator with another voltmeter and comparing the results. If the voltmeter is satisfactory, check the wiring, the brushes, and the drive unit for faults. If this inspection fails to reveal the trouble, the exciter may have lost its residual magnetism. Residual magnetism is restored to the exciter by flashing the field. Follow the applicable manufacturer’s instructions when flashing the exciter field. If, after flashing the field, no voltage is indicated, replace the alternator, since it is probably faulty.

Clean the alternator exterior with an approved fluid; smooth a rough or pitted exciter commutator or slip ring with 000 sandpaper; then clean and polish with a clean, dry cloth. Check the brushes periodically for length and general condition. Consult the applicable manufacturer’s instructions on the specific alternator to obtain information on the correct brushes.

### Regulation of Generator Voltage

Efficient operation of electrical equipment in an airplane depends on a constant voltage supply from the generator. Among the factors, which determine the voltage output of a generator, only one, the strength of the field current, can be conveniently controlled. To illustrate this control, refer to the diagram in Figure 12-327, showing a simple generator with a rheostat in the field circuit. If the rheostat is set to increase the resistance in the field circuit, less current flows through the field winding and the strength of the magnetic field in which the armature rotates decreases. Consequently, the voltage output of the generator decreases. If the resistance in the field circuit is decreased with the rheostat, more current flows through the field windings, the magnetic field becomes stronger, and the generator produces a greater voltage.

### Voltage Regulation with a Vibrating-Type Regulator

Refer to Figure 12-328 . With the generator running at normal speed and switch K open, the field rheostat is adjusted so that the terminal voltage is about 60 percent of Stator Terminal block Terminal block Oil inlet cover Rotor Filter assembly Ball bearing F S N S Stabilizing field Radio noise filter Thermistor Exciter field E1E2T1T4T3 T6 T5 Main AC generator stator windings Main AC generator field Rotor Pilot exciter armature Exciter armature 3 phase bridge rectifier Pilot exciter field normal. Solenoid S is weak and contact B is held closed by the spring. When K is closed, a short circuit is placed across the field rheostat. This action causes the field current to increase and the terminal voltage to rise.

When the terminal voltage rises above a certain critical value, the solenoid downward pull exceeds the spring tension and contact B opens, thus reinserting the field rheostat in the field circuit and reducing the field current and terminal voltage.

When the terminal voltage falls below a certain critical voltage, the solenoid armature contact B is closed again by the spring, the field rheostat is now shorted, and the terminal voltage starts to rise. The cycle repeats with a rapid, continuous action. Thus, an average voltage is maintained with or without load change.

The dashpot P provides smoother operation by acting as a damper to prevent hunting. The capacitor C across contact B eliminates sparking. Added load causes the field rheostat to be shorted for a longer period of time and, thus, the solenoid armature vibrates more slowly. If the load is reduced and the terminal voltage rises, the armature vibrates more rapidly and the regulator holds the terminal voltage to a steady value for any change in load, from no load to full load, on the generator.

Vibrating-type regulators cannot be used with generators, which require a high-field current, since the contacts pit or burn. Heavy-duty generator systems require a different type of regulator, such as the carbon pile voltage regulator.

### Three Unit Regulators

Many light aircraft employ a three unit regulator for their generator systems. [Figure 12-329] This type of regulator includes a current limiter and a reverse current cut-out in addition to a voltage regulator. The action of the voltage regulator unit is similar to the vibrating-type regulator described earlier. The second of the three units is a current regulator to limit the output current of the generator. The third unit is a reverse current cut-out that disconnects the battery from the generator. If the battery is not disconnected, it discharges through the generator armature when the generator voltage falls below that of the battery, thus driving the generator as a motor. This action is called “motoring” the generator and, unless it is prevented, it discharges the battery in a short time.

The operation of a three unit regulator is described in the following paragraphs. [Figure 12-330]

The action of vibrating contact C1 in the voltage regulator unit causes an intermittent short circuit between points R1 and L2. When the generator is not operating, spring S1 holds C1 closed; C2 is also closed by S2. The shunt field is connected directly across the armature.

When the generator is started, its terminal voltage rises as the generator comes up to speed, and the armature supplies the field with current through closed contacts C2 and C1.

As the terminal voltage rises, the current flow through L1 increases and the iron core becomes more strongly magnetized. At a certain speed and voltage, when the magnetic attraction on the movable arm becomes strong enough to overcome the tension of spring S1, contact points C1 are separated. The field current now flows through R1 and L2. Because resistance is added to the field circuit, the field is momentarily weakened and the rise in terminal voltage is checked. Also, since the L2 winding is opposed to the L1 winding, the magnetic pull of L1 against S1 is partially neutralized, and spring S1 closes contact C1. Therefore, R1 and L2 are again shorted out of the circuit, and the field current again increases; the output voltage increases, and C1 is opened because of the action of L1. The cycle is rapid and occurs many times per second. The terminal voltage of the generator varies slightly, but rapidly, above and below an average value determined by the tension of spring S1, which may be adjusted.

The purpose of the vibrator-type current limiter is to limit the output current of the generator automatically to its maximum rated value in order to protect the generator. As shown in Figure 12-330, L3 is in series with the main line and load. Thus, the amount of current flowing in the line determines when C2 is opened and R2 placed in series with the generator field. By contrast, the voltage regulator is actuated by line voltage, whereas the current limiter is actuated by line current. Spring S2 holds contact C2 closed until the current through the main line and L3 exceeds a certain value, as determined by the tension of spring S2, and causes C2 to be opened. The increase in current is due to an increase in load. This action inserts R2 into the field circuit of the generator and decreases the field current and the generated voltage. When the generated voltage is decreased, the generator current is reduced. The core of L3 is partly demagnetized and the spring closes the contact points. This causes the generator voltage and current to rise until the current reaches a value sufficient to start the cycle again. A certain minimum value of load current is necessary to cause the current limiter to vibrate.

The purpose of the reverse current cut-out relay is to automatically disconnect the battery from the generator when the generator voltage is less than the battery voltage. If this device were not used in the generator circuit, the battery would discharge through the generator. This would tend to make the generator operate as a motor, but because the generator is coupled to the engine, it could not rotate such a heavy load. Under this condition, the generator windings may be severely damaged by excessive current.

There are two windings, L4 and L5, on the soft iron core. The current winding, L4, consisting of a few turns of heavy wire, is in series with the line and carries the entire line current.

Voltage control Start-stop pushbutton Reset button VM5W V A W AM 5W Alternator Motor starting panel Alternator control panel Input terminal Output terminal Motor Terminal connections Current flow Load Shunt field Rheostat B + – A E The voltage winding, L5, consisting of a large number of turns of fine wire, is shunted across the generator terminals.

When the generator is not operating, the contacts, C3 are held open by the spring S3. As the generator voltage builds up, L5 magnetizes the iron core. When the current (as a result of the generated voltage) produces sufficient magnetism in the iron core, contact C3 is closed, as shown. The battery then receives a charging current. The coil spring, S3, is so adjusted that the voltage winding does not close the contact points until the voltage of the generator is in excess of the normal voltage of the battery. The charging current passing through L4 aids the current in L5 to hold the contacts tightly closed. Unlike C1 and C2, contact C3 does not vibrate. When the generator slows down or, for any other cause, the generator voltage decreases to a certain value below that of the battery, the current reverses through L4 and the ampere turns of L4 oppose those of L5. Thus, a momentary discharge current from the battery reduces the magnetism of the core and C3 is opened, preventing the battery from discharging into the generator and motoring it. C3 does not close again until the generator terminal voltage exceeds that of the battery by a predetermined value.

### Differential Relay Switch

Aircraft electrical systems normally use some type of reverse current relay switch, which acts not only as a reverse current relay cut-out but also serves as a remote control switch by which the generator can be disconnected from the electrical system at any time. One type of reverse current relay switch operates on the voltage level of the generator, but the type most commonly used on large aircraft is the differential relay switch, which is controlled by the difference in voltage Load P K C B S Voltage regulator Armature Shunt field Storage battery Current limiter Reverse current cut-out Loads + – + – S3 L4L3L1 L2 C1 C2 C3 S1 S2R1 R2 L5 A between the battery bus and the generator.

The differential type relay switch connects the generator to the main bus bar in the electrical system when the generator voltage output exceeds the bus voltage by 0.35 to 0.65 volt. It disconnects the generator when a nominal reverse current flows from the bus to the generator. The differential relays on all the generators of a multiengine aircraft do not close when the electrical load is light. For example, in an aircraft having a load of 50 amperes, only two or three relays may close. If a heavy load is applied, the equalizing circuit lowers the voltage of the generators already on the bus and, at the same time, raise the voltage of the remaining generators, allowing their relays to close. If the generators have been paralleled properly, all the relays stay closed until the generator control switch is turned off or until the engine speed falls below the minimum needed to maintain generator output voltage.

The differential generator control relay shown in Figure 12-331 is made up of two relays and a coil-operated contactor. One relay is the voltage relay and the other is the differential relay. Both relays include permanent magnets that pivot between the pole pieces of temporary magnets wound with relay coils. V oltages of one polarity set up fields about the temporary magnets with polarities that cause the permanent magnet to move in the direction necessary to close the relay contacts; voltages of the opposite polarity establish fields that cause the relay contacts to open. The differential relay has two coils wound on the same core. The coil-operated contactor, called the main contactor, consists of movable contacts that are operated by a coil with a movable iron core.

Closing the generator switch on the control panel connects the generator output to the voltage relay coil. When generator voltage reaches 22 volts, current flows through the coil and closes the contacts of the voltage relay. This action completes a circuit from the generator to the battery through the differential coil.

When the generator voltage exceeds the bus voltage by 0.35 volt, current flows through the differential coil, the differential relay contact closes and, thus, completes the main contractor coil circuit. The contacts of the main contactor close and connect the generator to the bus.

When the generator voltage drops below the bus (or battery) voltage, a reverse current weakens the magnetic field about the temporary magnet of the differential relay. The weakened field permits a spring to open the differential relay contacts, breaking the circuit to the coil of the main contactor relay, opening its contacts, and disconnecting the generator from the bus. The generator battery circuit may also be broken by opening the flight deck control switch, which opens the contacts of the voltage relay, causing the differential relay coil to be de-energized.

### Overvoltage & Field Control Relays

Two other items used with generator control circuits are the overvoltage control and the field control relay. As its name implies, the overvoltage control protects the system when excessive voltage exists. The overvoltage relay is closed when the generator output reaches 32 volts and completes a circuit to the trip coil of the field control relay. The closing of the field control relay trip circuit opens the shunt field circuit and completes it through a resistor, causing generator voltage to drop; also, the generator switch circuit and the equalizer circuit (multiengine aircraft) are opened. An indicator light circuit is completed, warning that an overvoltage condition exists. A “reset” position of the flight deck switch is used to complete a reset coil circuit in the field control relay, returning the relay to its normal position.

## 2. 中文翻译

<!-- TODO: 逐段翻译，段数与上面严格一一对应（89 段）。专业术语按行业惯例，数字与缩写保留。 -->

## 3. 专业词汇

<!-- TODO: 用表格 | 英文 | 词性 | 中文 | 本节语境 |，4~8 行。优先选下面 Glossary 里的词（本节原文出现过的）：
- Addition —— The process in which the value of one number is added to the value of another.
- Alternating current —— An electric current that reverses direction in a circuit at regular intervals.
- Ammeter —— An instrument for measuring electric current in amperes.
- Ampere —— A unit of measure of the rate of electron flow or current in an electrical conductor. One ampere of current represents one coulomb of electrical charge (6.24 × 
- Apparent power —— That power apparently available for use in an AC circuit containing a reactive component. It is the product of effective voltage times the effective current, ex
- Capacitor —— An electrical component that stores an electric charge.
- Current —— The flow of electrical charge.
- Difference —— The answer to a subtraction problem.
-->

## 4. 语法解析

<!-- TODO: 2~4 个语法点，格式：
### ① 语法点名称
**原句**：<必须逐字来自第 1 节原文>
**拆解**：主/谓/宾、从句、非谓语等成分分析
**要点**：为什么这样用、易错点、可迁移的搭配
-->
