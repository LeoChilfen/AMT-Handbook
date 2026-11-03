# DC Generators

> 通用 Ch 12 · DC Generators · 原文 PDF 第 565 页

## 1. 原文

### Theory of Operation

In the study of alternating current, basic generator principles were introduced to explain the generation of an AC voltage by a coil rotating in a magnetic field. Since this is the basis for all generator operation, it is necessary to review the principles of generation of electrical energy.

When lines of magnetic force are cut by a conductor passing through them, voltage is induced in the conductor. The strength of the induced voltage is dependent upon the speed of the conductor and the strength of the magnetic field. If the ends of the conductor are connected to form a complete circuit, a current is induced in the conductor. The conductor and the magnetic field make up an elementary generator.

This simple generator is illustrated in Figure 12-269 , together with the components of an external generator Ahrs +28 vdc Ahrs +28 vdc A/p controller +28 vdc +28 vdc +28 vdc +28 vdc +28 vdc +28 vdc +28 vdc +28 vdc +28 vdc Pitch servo valid +28 Roll servo valid +28 Yaw damper valid +28 Trim servo valid +28 Attitude valid +28 Heading valid +28 Attitude/heading reference system (Ahrs)

Autopilot computer (engage circuit)

Autopilot controller Pitch wheel centered Turn knob centered When all input circuits are valid, then the a/p can be engaged Autopilot Engage Logic +28 vdc OR gate input/output Truth table A f = A + B B A 0 1 0 1 B 0 0 1 1 f 0 1 1 1 A B + − A B + − circuit which collect and use the energy produced by the simple generator. The loop of wire [Figure 12-269A and B] is arranged to rotate in a magnetic field. When the plane of the loop of wire is parallel to the magnetic lines of force, the voltage induced in the loop causes a current to flow in the direction indicated by the arrows in Figure 12-269. The voltage induced at this position is maximum, since the wires are cutting the lines of force at right angles, thus cutting more lines of force per second than in any other position relative to the magnetic field. As the loop approaches the vertical position shown in Figure 12-270 , the induced voltage decreases because both sides of the loop (A and B) are approximately parallel to the lines of force and the rate of cutting is reduced. When the loop is vertical, no lines of force are cut since the wires are momentarily traveling parallel to the magnetic lines of force, and there is no induced voltage. As the rotation of the loop continues, the number of lines of force cut increases until the loop has rotated an additional 90° to a horizontal plane. As shown in Figure 12-271, the number of lines of force cut and the induced voltage once again are maximum. The direction of cutting, however, is in the opposite direction to that occurring in Figures 12-269 and 12-270, so the direction (polarity) of the induced voltage is reversed. As rotation of the loop continues, the number of lines of force having been cut again decreases, and the induced voltage becomes zero at the position shown in Figure 12-272, since the wires A and B are again parallel to the magnetic lines of force.

If the voltage induced throughout the entire 360° of rotation A F B NAND gate A (1)

F B A F B Equivalent circuit NAND gate input/output 0 1 0 NAND gate input/output NAND gate truth table 0 1 1 1 1 0 1 0 1 A 0 1 0 1 B 0 0 1 1 f 1 1 1 0 OR gate input/output Truth table A f = A + B B A 0 1 0 1 B 0 0 1 1 f 0 1 1 1 Door unsafe Door warn Light on Cabin door not secured Baggage door secured+28 VDC Door unsafe Door warn Light off Cabin door secured Baggage door secured+28 VDC is plotted, the curve shown in Figure 12-273 results. This voltage is called an alternating voltage because of its reversal from positive to negative value, first in one direction and then in the other.

To use the voltage generated in the loop for producing a current flow in an external circuit, some means must be provided to connect the loop of wire in series with the external circuit. Such an electrical connection can be effected by opening the loop of wire and connecting its two ends to two metal rings, called slip rings, against which two metal or carbon brushes ride. The brushes are connected to the external circuit. By replacing the slip rings of the basic AC generator with two half cylinders, called a commutator, a basic DC generator is obtained. [Figure 12-274] In this illustration, the black side of the coil is connected to the black segment, and the white side of the coil to the white segment. The segments are insulated from each other. The two stationary brushes are placed on opposite sides of the commutator and are so mounted that each brush contacts each segment of the commutator as the latter revolves simultaneously with the loop. The rotating parts of a DC generator (coil and commutator) are called an armature. The generation of an emf by the loop rotating in the magnetic field is the same for both AC and DC generators, but the action of the commutator produces a DC voltage.

### Generation of a DC Voltage

Figure 12-275 illustrates in an elementary, step-by-step manner, how a DC voltage is generated. This is accomplished by showing a single wire loop rotating through a series of positions within a magnetic field.

The loop starts in position A and is rotating clockwise. However, no lines of force are cut by the coil sides, which means that no emf is generated. The black brush is shown coming into contact with the black segment of the commutator, and the white brush is just coming into contact with the white segment.

X-NOR gate input/output Truth table A f = A + B 0f 0 0 B T0 T1 T2 T3 T4 1 A 0 0 1 1 B 0 1 0 1 f 1 0 0 1 0 A 1 0 T0 T1 T2 T3 T4 1 0 B 0 1 1 X-OR gate input/output Truth table A f 0f 1 0 0B T0 T1 T2 T3 T4 T5 1 A 0 0 1 1 B 0 1 0 1 f 0 1 1 0 0 A 1 0 0 T0 T1 T2 T3 T4 T4 1 0 B 0 0 1 1 NOR gate input/output NOR gate truth table 0 1 0 0 0 1 A 0 0 1 1 B 0 1 0 1 f 1 0 0 0 1 0 0 1 0 1 table.

In position B, the flux is now being cut at a maximum rate, which means that the induced emf is maximum. At this time, the black brush is contacting the black segment, and the white brush is contacting the white segment. The deflection of the meter is toward the right, indicating the polarity of the output voltage.

At position C, the loop has completed 180° of rotation. Like position A, no flux lines are being cut and the output voltage is zero. The important condition to observe at position C is the action of the segments and brushes. The black brush at the 180° angle is contacting both black and white segments on one side of the commutator, and the white brush is contacting both segments on the other side of the commutator. After the Typical integrated logic circuit 0.280" max 0.200" max 0.785" max 16 15 14 13 12 11 10 9 1 2 3 4 5 6 7 8 4Y 4A 4B GND 3A 3B 3Y 1Y 1A 1B VCC 2A 2B 2Y 14 13 12 11 10 9 8 1 2 3 4 5 6 7 Quad exclusive-OR circuit Input Output A 0 0 1 1 Y 0 1 1 0 B 0 1 0 1 1Q 2Q 2Q Enable Gnd 3Q 3Q 4Q 1Q 1D 2D Enable Vcc 3D 4D 4Q 16 15 14 13 12 11 10 9 1 2 3 4 5 6 7 8 DQ G Q QD Q G DQ G Q QD Q G D-register loop rotates slightly past the 180° point, the black brush is contacting only the white segment, and the white brush is contacting only the black segment.

Because of this switching of commutator elements, the black brush is always in contact with the coil side moving downward, and the white brush is always in contact with the coil side moving upward. Though the current actually reverses its direction in the loop in exactly the same way as in the AC generator, commutator action causes the current to flow always in the same direction through the external circuit or meter.

At position D, commutator action reverses the current in the external circuit, and the second half cycle has the same waveform as the first half cycle. The process of commutation is sometimes called rectification, since rectification is the converting of AC voltage to DC voltage.

#### The Neutral Plane

At the instant that each brush is contacting two segments on the commutator [Figure 12-275A, C, and E], a direct short circuit is produced. If an emf were generated in the loop at this time, a high current would flow in the circuit, causing an arc and thus damaging the commutator. For this reason, the brushes must be placed in the exact position where the short occurs when the generated emf is zero. This position is called the neutral plane. If the brushes are installed properly, no sparking occurs between the brushes and the commutator. Sparking is an indication of improper brush placement, which is the main cause of improper commutation.

The voltage generated by the basic DC generator in Figure 12-275 varies from zero to its maximum value twice for each revolution of the loop. This variation of DC voltage is called “ripple,” and may be reduced by using more loops, or coils, as shown in Figure 12-276A. As the number of loops is increased, the variation between maximum and minimum values of voltage is reduced [Figure 12-276B], and the output voltage of the generator approaches a steady DC value. In Figure 12-276A, the number of commutator segments is increased in direct proportion to the number of loops; that N S A B N S B A direction.

N S A Armature B Load Slip ring Pole piece Brush N S A B generator.

is, there are two segments for one loop, four segments for two loops, and eight segments for four loops.

The voltage induced in a single turn loop is small. Increasing the number of loops does not increase the maximum value of generated voltage, but increasing the number of turns in each loop increases this value. Within narrow limits, the output voltage of a DC generator is determined by the product of the number of turns per loop, the total flux per pair of poles in the machine, and the speed of rotation of the armature.

An AC generator, or alternator, and a DC generator are identical as far as the method of generating voltage in the rotating loop is concerned. However, if the current is taken from the loop by slip rings, it is an alternating current, and the generator is called an AC generator, or alternator. If the current is collected by a commutator, it is direct current, and the generator is called a DC generator.

### Construction Features of DC Generators

Generators used on aircraft may differ somewhat in design, since various manufacturers make them. All, however, are of the same general construction and operate similarly. The major parts, or assemblies, of a DC generator are a field frame (or yoke), a rotating armature, and a brush assembly. The parts of a typical aircraft generator are shown in Figure 12-277.

The field frame is also called the yoke, which is the foundation or frame for the generator. The frame has two functions: It completes the magnetic circuit between the poles and acts as a mechanical support for the other parts of the generator. In Figure 12-278A, the frame for a two-pole generator is shown in a cross-sectional view. A four-pole generator frame is shown in Figure 12-278B.

– Voltage + Voltage Maximum Minimum 0° Maximum 90° 270° 360° 360° 1 cycle 180° S N Induced EMF 1 Revolution A EB C D In small generators, the frame is made of one piece of iron, but in larger generators, it is usually made up of two parts bolted together. The frame has high magnetic properties and, together with the pole pieces, forms the major part of the magnetic circuit. The field poles are bolted to the inside of the frame and form a core on which the field coil windings are mounted. [Figure 12-278] The poles are usually laminated to reduce eddy current losses and serve the same purpose as the iron core of an electromagnet; that is, they concentrate the lines of force produced by the field coils. The entire frame, including field poles, is made from high-quality magnetic iron or sheet steel.

A practical DC generator uses electromagnets instead of permanent magnets. To produce a magnetic field of the necessary strength with permanent magnets would greatly increase the physical size of the generator.

The field coils are made up of many turns of insulated wire and are usually wound on a form that fits over the iron core of the pole to which it is securely fastened. [Figure 12-279] The exciting current, which is used to produce the magnetic field and which flows through the field coils, is obtained from an external source or from the generated DC of the machine. No electrical connection exists between the windings of the field coils and the pole pieces.

Most field coils are connected so that the poles show alternate polarity. Since there is always one North pole for each South pole, there must always be an even number of poles in any generator.

Note that the pole pieces in Figure 12-278 project from the frame. Because air offers a great amount of reluctance to the magnetic field, this design reduces the length of the air gap between the poles and the rotating armature and increases the efficiency of the generator. When the pole pieces are made to project they are called salient poles. [Figure 12-278]

A B C D E 0 1/4 1/2 3/4 1Induced EMF Revolutions S N A B in the voltage.

The armature assembly of a generator consists of many armature coils wound on an iron core, a commutator, and associated mechanical parts. These additional loops of wire are actually called windings and are evenly spaced around the armature so that the distance between each winding is the same. Mounted on a shaft, it rotates through the magnetic field produced by the field coils. The core of the armature acts as an iron conductor in the magnetic field and, for this reason, is laminated to prevent the circulation of eddy currents.

#### Gramme-Ring Armature

There are two general kinds of armatures: the ring and the drum. Figure 12-280 shows a ring-type armature made up of an iron core, an eight-section winding, and an eight-segment commutator. The disadvantage of this arrangement is that the windings, located on the inner side of the iron ring, cut few lines of flux. As a result, they have very little voltage induced in them. For this reason, the Gramme ring armature is not widely used.

#### Drum-Type Armature

A drum-type armature is shown in Figure 12-281 . The armature core is in the shape of a drum and has slots cut into it where the armature windings are placed. The advantage is that each winding completely surrounds the core so that the entire length of the conductor cuts through the magnetic flux. The total induced voltage in this arrangement is far greater than that of the Gramme ring-type armature.

Drum-type armatures are usually constructed in one of two methods: lap winding and the wave winding. Each method having its own advantage. Lap windings are used in generators that are designed for high current. The windings are connected in parallel paths and for this reason require several brushes. The wave winding is used in generators that are designed for high voltage outputs. The two ends of each coil are connected to commutator segments separated by the distance between poles. This results in a series arrangement of the coils and is additive of all the induced voltages.

Figure 12-282 shows a cross-sectional view of a typical commutator. The commutator is located at the end of an armature and consists of wedge shaped segments of hard drawn copper, insulated from each other by thin sheets of mica. The segments are held in place by steel V-rings or clamping flanges fitted with bolts. Rings of mica insulate the segments from the flanges. The raised portion of each segment is called a riser, and the leads from the armature coils are soldered to the risers. When the segments have no risers, the leads are soldered to short slits in the ends of the segments.

The brushes ride on the surface of the commutator, forming the electrical contact between the armature coils and the external circuit. A flexible, braided copper conductor, commonly called a pigtail, connects each brush to the external circuit. The brushes, usually made of high-grade carbon and held in place by brush holders insulated from the frame, are free to slide up and down in their holders in order to follow any irregularities in the surface of the commutator. The brushes are usually adjustable so that the pressure of the brushes on the commutator can be varied and the position of the brushes with respect to the segments can be adjusted.

The constant making and breaking of connections to the coils in which a voltage is being induced necessitates the use of material for brushes, which has a definite contact resistance. Also, this material must be such that the friction between the commutator and the brush is low, to prevent excessive wear. For these reasons, the material commonly used for brushes is high-grade carbon. The carbon must be soft enough to prevent undue wear of the commutator and yet hard enough to provide reasonable brush life. Since the contact resistance of carbon is fairly high, the brush must be quite large to provide a large area of contact. The commutator surface is highly polished to reduce friction as much as possible. Oil or grease must never be used on a commutator, and extreme care must be used when cleaning it to avoid marring or scratching the surface.

Connector ligs Field frame Drive end frame Sealed ball bearings Drive shaft Field windingScrewPole shoeBrush and holder Steel ring Commutator Brush connector bars Air scoop Armature Drive end Field frame Commutator end frame

### Armature Reaction

Current flowing through the armature sets up electromagnetic fields in the windings. These new fields tend to distort or bend the magnetic flux between the poles of the generator from a straight-line path. Since armature current increases with load, the distortion becomes greater with an increase in load. This distortion of the magnetic field is called armature reaction. [Figure 12-283]

Armature windings of a generator are spaced so that, during rotation of the armature, there are certain positions when the brushes contact two adjacent segments, thereby shorting the armature windings to these segments. When the magnetic field is not distorted, there is usually no voltage being induced in the shorted windings, and therefore no harmful results occur from the shorting of the windings. However, when the field is distorted, a voltage is induced in these shorted windings, and sparking takes place between the brushes and the commutator segments. Consequently, the commutator becomes pitted, the wear on the brushes becomes excessive, and the output of the generator is reduced. To correct this condition, the brushes are set so that the plane of the coils, which are shorted by the brushes, is perpendicular to the distorted magnetic field, which is accomplished by moving the brushes forward in the direction of rotation. This operation is called shifting the brushes to the neutral plane or plane of commutation. The neutral plane is the position where the plane of the two opposite coils is perpendicular to the magnetic field in the generator. On a few generators, the brushes can be shifted manually ahead of the normal neutral plane to the neutral plane caused by field distortion. On nonadjustable brush generators, the manufacturer sets the brushes for minimum sparking.

### Compensating Windings

or interpoles may be used to counteract some of the effects of field distortion, since shifting the brushes is inconvenient and unsatisfactory, especially when the speed and load of the generator are changing constantly.

Compensating Windings The compensating windings consist of a series of coils embedded in slots in the pole faces. These coils are also connected in series with the armature. Consequently, this series connection with the armature produces a magnetic field in the compensating windings that varies directly with the armature current. The compensating windings are wound in such a manner that the magnetic field produced by them counteracts the magnetic field produced by the armature. As a result, the neutral plane remains stationary any magnitude of armature current. With this design, once the brushes are set correctly, they do not need to be moved again. Figure 12-284A illustrates how the windings are set into the pole faces.

N S N S N N S S A B Flux Pole Field winding Frame Flux Pole Field winding Frame

An interpole is a pole placed between the main poles of a generator. An example of interpole placement is shown in Figure 12-284B. This is a simple two-pole generator with two interpoles.

An interpole has the same polarity as the next main pole in the direction of rotation. The magnetic flux produced by an interpole causes the current in the armature to change direction as an armature winding passes under it. This cancels the electromagnetic fields about the armature windings. The magnetic strength of the interpoles varies with the load on the generator; and since field distortion varies with the load, the magnetic field of the interpoles counteracts the effects of the field set up around the armature windings and minimizes field distortion. Thus, the interpole tends to keep the neutral plane in the same position for all loads on the generator; therefore, field distortion is reduced by the interpoles, and the efficiency, output, and service life of the brushes are improved.

### Types of DC Generators

There are three types of DC generators: series wound, shunt wound, and shunt series or compound wound. The difference in type depends on the relationship of the field winding to the external circuit.

#### Series Wound DC Generators

The field winding of a series generator is connected in series with the external circuit called the load. [Figure 12-285] The field coils are composed of a few turns of large wire; the magnetic field strength depends more on the current flow rather than the number of turns in the coil. Series generators have very poor voltage regulation under changing load, since the greater the current through the field coils to the external circuit, the greater the induced emf and the greater the terminal or output voltage. Therefore, when the load is increased, the voltage increases; likewise, when the load is decreased, the voltage Mica V-ring Front V-ring Commutator bar Mica Iron shell Back V-ring with mica inner and outer rings for insulationSlots Tightening nut Iron ring Commutator bars Mica insulation between bars Commutator Slots Shaft Coils decreases. The output voltage of a series wound generator may be controlled by a rheostat in parallel with the field windings. [Figure 12-285A] Since the series wound generator has such poor regulation, it is never employed as an airplane generator. Generators in airplanes have field windings, which are connected either in shunt or in compound.

#### Shunt Wound DC Generators

A generator having a field winding connected in parallel with the external circuit is called a shunt generator. [Figure 12-286A and B] The field coils of a shunt generator contain many turns of small wire; the magnetic strength is derived from the large number of turns rather than the current strength through the coils. If a constant voltage is desired, the shunt wound generator is not suitable for rapidly fluctuating loads. Any increase in load causes a decrease in the terminal or output voltage, and any decrease in load causes an increase in terminal voltage; since the armature and the load are connected in series, all current flowing in the external circuit passes through the armature winding. Because of the resistance in the armature winding, there is a voltage drop (IR drop = current × resistance). As the load increases, the armature current increases and the IR drop in the armature increases. The voltage delivered to the terminals is the difference between the induced voltage and the voltage drop; therefore, there is a decrease in terminal voltage. This decrease in voltage causes a decrease in field strength, because the current in the field coils decreases in proportion to the decrease in terminal voltage; with a weaker field, the voltage is further decreased. When the load decreases, the output voltage increases accordingly, and a larger current flows in the windings. This action is cumulative, so the output voltage continues to rise to a point called field saturation, after which there is no further increase in output voltage.

The terminal voltage of a shunt generator can be controlled by means of a rheostat inserted in series with the field windings. [Figure 12-286A] As the resistance is increased, the field current is reduced; consequently, the generated voltage is reduced also. For a given setting of the field rheostat, the terminal voltage at the armature brushes is approximately equal to the generated voltage minus the IR N S Rotation + + + + a b Neutral plane Rotation ++ + + + + + + + ++ S N N S Rotation + + + + + + + + + + + ++++ a b A B C Field excited, armature unexcited Armature excited, field unexcited Both field and armature excited drop produced by the load current in the armature; thus, the voltage at the terminals of the generator drops as the load is applied. Certain voltage sensitive devices are available that automatically adjust the field rheostat to compensate for variations in load. When these devices are used, the terminal voltage remains essentially constant.

#### Compound Wound DC Generators

A compound wound generator combines a series winding and a shunt winding in such a way that the characteristics of each are used to advantage. The series field coils are made of a relatively small number of turns of large copper conductor, either circular or rectangular in cross section, and are connected in series with the armature circuit. These coils are mounted on the same poles on which the shunt field coils are mounted and, therefore, contribute a magnetomotive force which influences the main field flux of the generator. A diagrammatic and a schematic illustration of a compound wound generator is shown in Figure 12-287A and B.

If the ampere turns of the series field act in the same direction as those of the shunt field, the combined magnetomotive force is equal to the sum of the series and shunt field components. Load is added to a compound generator in the same manner in which load is added to a shunt generator, by increasing the number of parallel paths across the generator terminals. Thus, the decrease in total load resistance with added load is accompanied by an increase in armature circuit and series field circuit current. The effect of the additive series field is that of increased field flux with increased load. The extent of the increased field flux depends on the degree of saturation of the field as determined by the shunt field current. Thus, the terminal voltage of the generator may increase or decrease with load, depending on the influence of the series field coils. This influence is referred to as the degree of compounding. A flat compound generator is one in which the no load and full load voltages have the same value; whereas an under compound generator has a full load voltage less than the no load value, and an over compound generator has a full load voltage which is higher than the no load value. Changes in terminal voltage with increasing load depend upon the degree of compounding.

If the series field aids the shunt field, the generator is said to be cumulative compounded. If the series field opposes the shunt field, the machine is said to be differentially compounded or is called a differential generator. Compound generators are usually designed to be overcompounded. This feature permits varied degrees of compounding by connecting a variable shunt across the series field. Such a shunt is sometimes called a diverter. Compound generators are used where voltage regulation is of prime importance.

Differential generators have somewhat the same characteristics as series generators in that they are essentially constant current generators. However, they generate rated voltage at no load, the voltage dropping materially as the load current increases. Constant current generators are ideally suited as power sources for electric arc welders and are used almost universally in electric arc welding.

If the shunt field of a compound generator is connected across both the armature and the series field, it is known as a long shunt connection, but if the shunt field is connected across the armature alone, it is called a short shunt connection. These connections produce essentially the same generator characteristics. A summary of the characteristics of the various types of generators discussed is shown in Figure 12-288.

### Generator Ratings

A generator is rated in power output. Since a generator is designed to operate at a specified voltage, the rating usually is given as the number of amperes the generator can safely Generator + − S N SN External load Generator −− − − − − − + + + ++ + ++ − − − − − − − + + + + + + + CompensatingA InterpoleB Main field windings Armature windings Main field windings Compensating windings Compensating windings Interpole windings Interpole windings A B NS Load − + Field rheostat Field coils To load Arm supply at its rated voltage. Generator rating and performance data are stamped on the nameplate attached to the generator. When replacing a generator, it is important to choose one of the proper rating.

The rotation of generators is termed either clockwise or counterclockwise, as viewed from the driven end. Usually, the direction of rotation is stamped on the data plate. If no direction is stamped on the plate, the rotation may be marked by an arrow on the cover plate of the brush housing. It is important that a generator with the correct direction of rotation be used; otherwise, the voltage is reversed.

The speed of an aircraft engine varies from idle rpm to takeoff rpm; however, during the major portion of a flight, it is at a constant cruising speed. The generator drive is usually geared to revolve the generator between 11⁄8 and 11⁄2 times the engine crankshaft speed. Most aircraft generators have a speed at which they begin to produce their normal voltage. Termed the “coming in” speed, it is usually about 1,500 rpm.

### Generator Terminals

On most large 24-volt generators, electrical connections are made to terminals marked B, A, and E. The positive armature lead in the generator connects to the B terminal. The negative armature lead connects to the E terminal. The positive end of the shunt field winding connects to terminal A, and the opposite end connects to the negative terminal brush. Terminal A receives current from the negative generator brush through the shunt field winding. This current passes through the voltage regulator and back to the armature through the positive brush. Load current, which leaves the armature through the negative brushes, comes out of the E lead and passes through the load before returning to the armature through the positive brushes.

## 2. 中文翻译

<!-- TODO: 逐段翻译，段数与上面严格一一对应（71 段）。专业术语按行业惯例，数字与缩写保留。 -->

## 3. 专业词汇

<!-- TODO: 用表格 | 英文 | 词性 | 中文 | 本节语境 |，4~8 行。优先选下面 Glossary 里的词（本节原文出现过的）：
- Alternating current —— An electric current that reverses direction in a circuit at regular intervals.
- Ampere —— A unit of measure of the rate of electron flow or current in an electrical conductor. One ampere of current represents one coulomb of electrical charge (6.24 × 
- Conductor —— A material that will carry electric current.
- Current —— The flow of electrical charge.
- Difference —— The answer to a subtraction problem.
- Direct current (DC) —— Electricity that flows in one direction at all times.
- Electrical energy —— Electrical energy is converted to heat energy when an electric current flows through any form of resistance such as an electric iron, electric light, or an elec
- Energy —— The capacity of a physical system to perform work. There are two types of energy, kinetic and potential.
-->

## 4. 语法解析

<!-- TODO: 2~4 个语法点，格式：
### ① 语法点名称
**原句**：<必须逐字来自第 1 节原文>
**拆解**：主/谓/宾、从句、非谓语等成分分析
**要点**：为什么这样用、易错点、可迁移的搭配
-->
