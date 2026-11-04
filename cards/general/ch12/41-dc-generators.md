# DC Generators

> 通用 Ch 12 · DC Generators · 原文 PDF 第 565 页

## 1. 原文

### Theory of Operation

In the study of alternating current, basic generator principles were introduced to explain the generation of an AC voltage by a coil rotating in a magnetic field. Since this is the basis for all generator operation, it is necessary to review the principles of generation of electrical energy.

When lines of magnetic force are cut by a conductor passing through them, voltage is induced in the conductor. The strength of the induced voltage is dependent upon the speed of the conductor and the strength of the magnetic field. If the ends of the conductor are connected to form a complete circuit, a current is induced in the conductor. The conductor and the magnetic field make up an elementary generator.

This simple generator is illustrated in the figure, together with the components of an external generator Ahrs +28 vdc Ahrs +28 vdc A/p controller +28 vdc +28 vdc +28 vdc +28 vdc +28 vdc +28 vdc +28 vdc +28 vdc +28 vdc Pitch servo valid +28 Roll servo valid +28 Yaw damper valid +28 Trim servo valid +28 Attitude valid +28 Heading valid +28 Attitude/heading reference system (Ahrs)

Autopilot computer (engage circuit)

Autopilot controller Pitch wheel centered Turn knob centered When all input circuits are valid, then the a/p can be engaged Autopilot Engage Logic +28 vdc OR gate input/output Truth table A f = A + B B A 0 1 0 1 B 0 0 1 1 f 0 1 1 1 A B + − A B + − circuit which collect and use the energy produced by the simple generator. The loop of wire is arranged to rotate in a magnetic field. When the plane of the loop of wire is parallel to the magnetic lines of force, the voltage induced in the loop causes a current to flow in the direction indicated by the arrows. The voltage induced at this position is maximum, since the wires are cutting the lines of force at right angles, thus cutting more lines of force per second than in any other position relative to the magnetic field. As the loop approaches the vertical position shown, the induced voltage decreases because both sides of the loop (A and B) are approximately parallel to the lines of force and the rate of cutting is reduced. When the loop is vertical, no lines of force are cut since the wires are momentarily traveling parallel to the magnetic lines of force, and there is no induced voltage. As the rotation of the loop continues, the number of lines of force cut increases until the loop has rotated an additional 90° to a horizontal plane. In the position shown, the number of lines of force cut and the induced voltage once again are maximum. The direction of cutting, however, is in the opposite direction to that occurring in the earlier positions, so the direction (polarity) of the induced voltage is reversed. As rotation of the loop continues, the number of lines of force having been cut again decreases, and the induced voltage becomes zero at the position shown, since the wires A and B are again parallel to the magnetic lines of force.

If the voltage induced throughout the entire 360° of rotation is plotted, the curve shown in the figure results. This voltage is called an alternating voltage because of its reversal from positive to negative value, first in one direction and then in the other.

To use the voltage generated in the loop for producing a current flow in an external circuit, some means must be provided to connect the loop of wire in series with the external circuit. Such an electrical connection can be effected by opening the loop of wire and connecting its two ends to two metal rings, called slip rings, against which two metal or carbon brushes ride. The brushes are connected to the external circuit. By replacing the slip rings of the basic AC generator with two half cylinders, called a commutator, a basic DC generator is obtained. In this illustration, the black side of the coil is connected to the black segment, and the white side of the coil to the white segment. The segments are insulated from each other. The two stationary brushes are placed on opposite sides of the commutator and are so mounted that each brush contacts each segment of the commutator as the latter revolves simultaneously with the loop. The rotating parts of a DC generator (coil and commutator) are called an armature. The generation of an emf by the loop rotating in the magnetic field is the same for both AC and DC generators, but the action of the commutator produces a DC voltage.

### Generation of a DC Voltage

The figure illustrates in an elementary, step-by-step manner, how a DC voltage is generated. This is accomplished by showing a single wire loop rotating through a series of positions within a magnetic field.

The loop starts in position A and is rotating clockwise. However, no lines of force are cut by the coil sides, which means that no emf is generated. The black brush is shown coming into contact with the black segment of the commutator, and the white brush is just coming into contact with the white segment.

X-NOR gate input/output Truth table A f = A + B 0f 0 0 B T0 T1 T2 T3 T4 1 A 0 0 1 1 B 0 1 0 1 f 1 0 0 1 0 A 1 0 T0 T1 T2 T3 T4 1 0 B 0 1 1 X-OR gate input/output Truth table A f 0f 1 0 0B T0 T1 T2 T3 T4 T5 1 A 0 0 1 1 B 0 1 0 1 f 0 1 1 0 0 A 1 0 0 T0 T1 T2 T3 T4 T4 1 0 B 0 0 1 1 NOR gate input/output NOR gate truth table 0 1 0 0 0 1 A 0 0 1 1 B 0 1 0 1 f 1 0 0 0 1 0 0 1 0 1 table.

In position B, the flux is now being cut at a maximum rate, which means that the induced emf is maximum. At this time, the black brush is contacting the black segment, and the white brush is contacting the white segment. The deflection of the meter is toward the right, indicating the polarity of the output voltage.

At position C, the loop has completed 180° of rotation. Like position A, no flux lines are being cut and the output voltage is zero. The important condition to observe at position C is the action of the segments and brushes. The black brush at the 180° angle is contacting both black and white segments on one side of the commutator, and the white brush is contacting both segments on the other side of the commutator. After the loop rotates slightly past the 180° point, the black brush is contacting only the white segment, and the white brush is contacting only the black segment.

Because of this switching of commutator elements, the black brush is always in contact with the coil side moving downward, and the white brush is always in contact with the coil side moving upward. Though the current actually reverses its direction in the loop in exactly the same way as in the AC generator, commutator action causes the current to flow always in the same direction through the external circuit or meter.

At position D, commutator action reverses the current in the external circuit, and the second half cycle has the same waveform as the first half cycle. The process of commutation is sometimes called rectification, since rectification is the converting of AC voltage to DC voltage.

#### The Neutral Plane

At the instant that each brush is contacting two segments on the commutator at these points, a direct short circuit is produced. If an emf were generated in the loop at this time, a high current would flow in the circuit, causing an arc and thus damaging the commutator. For this reason, the brushes must be placed in the exact position where the short occurs when the generated emf is zero. This position is called the neutral plane. If the brushes are installed properly, no sparking occurs between the brushes and the commutator. Sparking is an indication of improper brush placement, which is the main cause of improper commutation.

The voltage generated by the basic DC generator varies from zero to its maximum value twice for each revolution of the loop. This variation of DC voltage is called “ripple,” and may be reduced by using more loops, or coils, as shown in the figure. As the number of loops is increased, the variation between maximum and minimum values of voltage is reduced, and the output voltage of the generator approaches a steady DC value. In the figure, the number of commutator segments is increased in direct proportion to the number of loops; that is, there are two segments for one loop, four segments for two loops, and eight segments for four loops.

The voltage induced in a single turn loop is small. Increasing the number of loops does not increase the maximum value of generated voltage, but increasing the number of turns in each loop increases this value. Within narrow limits, the output voltage of a DC generator is determined by the product of the number of turns per loop, the total flux per pair of poles in the machine, and the speed of rotation of the armature.

An AC generator, or alternator, and a DC generator are identical as far as the method of generating voltage in the rotating loop is concerned. However, if the current is taken from the loop by slip rings, it is an alternating current, and the generator is called an AC generator, or alternator. If the current is collected by a commutator, it is direct current, and the generator is called a DC generator.

### Construction Features of DC Generators

Generators used on aircraft may differ somewhat in design, since various manufacturers make them. All, however, are of the same general construction and operate similarly. The major parts, or assemblies, of a DC generator are a field frame (or yoke), a rotating armature, and a brush assembly. The parts of a typical aircraft generator are shown in the figure.

The field frame is also called the yoke, which is the foundation or frame for the generator. The frame has two functions: It completes the magnetic circuit between the poles and acts as a mechanical support for the other parts of the generator. In the figure, the frame for a two-pole generator is shown in a cross-sectional view. A four-pole generator frame is shown in the figure.

In small generators, the frame is made of one piece of iron, but in larger generators, it is usually made up of two parts bolted together. The frame has high magnetic properties and, together with the pole pieces, forms the major part of the magnetic circuit. The field poles are bolted to the inside of the frame and form a core on which the field coil windings are mounted. The poles are usually laminated to reduce eddy current losses and serve the same purpose as the iron core of an electromagnet; that is, they concentrate the lines of force produced by the field coils. The entire frame, including field poles, is made from high-quality magnetic iron or sheet steel.

A practical DC generator uses electromagnets instead of permanent magnets. To produce a magnetic field of the necessary strength with permanent magnets would greatly increase the physical size of the generator.

The field coils are made up of many turns of insulated wire and are usually wound on a form that fits over the iron core of the pole to which it is securely fastened. The exciting current, which is used to produce the magnetic field and which flows through the field coils, is obtained from an external source or from the generated DC of the machine. No electrical connection exists between the windings of the field coils and the pole pieces.

Most field coils are connected so that the poles show alternate polarity. Since there is always one North pole for each South pole, there must always be an even number of poles in any generator.

Note that the pole pieces project from the frame. Because air offers a great amount of reluctance to the magnetic field, this design reduces the length of the air gap between the poles and the rotating armature and increases the efficiency of the generator. When the pole pieces are made to project they are called salient poles.

The armature assembly of a generator consists of many armature coils wound on an iron core, a commutator, and associated mechanical parts. These additional loops of wire are actually called windings and are evenly spaced around the armature so that the distance between each winding is the same. Mounted on a shaft, it rotates through the magnetic field produced by the field coils. The core of the armature acts as an iron conductor in the magnetic field and, for this reason, is laminated to prevent the circulation of eddy currents.

#### Gramme-Ring Armature

There are two general kinds of armatures: the ring and the drum. The figure shows a ring-type armature made up of an iron core, an eight-section winding, and an eight-segment commutator. The disadvantage of this arrangement is that the windings, located on the inner side of the iron ring, cut few lines of flux. As a result, they have very little voltage induced in them. For this reason, the Gramme ring armature is not widely used.

#### Drum-Type Armature

A drum-type armature is shown in the figure. The armature core is in the shape of a drum and has slots cut into it where the armature windings are placed. The advantage is that each winding completely surrounds the core so that the entire length of the conductor cuts through the magnetic flux. The total induced voltage in this arrangement is far greater than that of the Gramme ring-type armature.

Drum-type armatures are usually constructed in one of two methods: lap winding and the wave winding. Each method having its own advantage. Lap windings are used in generators that are designed for high current. The windings are connected in parallel paths and for this reason require several brushes. The wave winding is used in generators that are designed for high voltage outputs. The two ends of each coil are connected to commutator segments separated by the distance between poles. This results in a series arrangement of the coils and is additive of all the induced voltages.

The figure shows a cross-sectional view of a typical commutator. The commutator is located at the end of an armature and consists of wedge shaped segments of hard drawn copper, insulated from each other by thin sheets of mica. The segments are held in place by steel V-rings or clamping flanges fitted with bolts. Rings of mica insulate the segments from the flanges. The raised portion of each segment is called a riser, and the leads from the armature coils are soldered to the risers. When the segments have no risers, the leads are soldered to short slits in the ends of the segments.

The brushes ride on the surface of the commutator, forming the electrical contact between the armature coils and the external circuit. A flexible, braided copper conductor, commonly called a pigtail, connects each brush to the external circuit. The brushes, usually made of high-grade carbon and held in place by brush holders insulated from the frame, are free to slide up and down in their holders in order to follow any irregularities in the surface of the commutator. The brushes are usually adjustable so that the pressure of the brushes on the commutator can be varied and the position of the brushes with respect to the segments can be adjusted.

The constant making and breaking of connections to the coils in which a voltage is being induced necessitates the use of material for brushes, which has a definite contact resistance. Also, this material must be such that the friction between the commutator and the brush is low, to prevent excessive wear. For these reasons, the material commonly used for brushes is high-grade carbon. The carbon must be soft enough to prevent undue wear of the commutator and yet hard enough to provide reasonable brush life. Since the contact resistance of carbon is fairly high, the brush must be quite large to provide a large area of contact. The commutator surface is highly polished to reduce friction as much as possible. Oil or grease must never be used on a commutator, and extreme care must be used when cleaning it to avoid marring or scratching the surface.

Connector ligs Field frame Drive end frame Sealed ball bearings Drive shaft Field windingScrewPole shoeBrush and holder Steel ring Commutator Brush connector bars Air scoop Armature Drive end Field frame Commutator end frame

A B C D E 0 1/4 1/2 3/4 1Induced EMF Revolutions S N A B in the voltage.

### Armature Reaction

Current flowing through the armature sets up electromagnetic fields in the windings. These new fields tend to distort or bend the magnetic flux between the poles of the generator from a straight-line path. Since armature current increases with load, the distortion becomes greater with an increase in load. This distortion of the magnetic field is called armature reaction.

Armature windings of a generator are spaced so that, during rotation of the armature, there are certain positions when the brushes contact two adjacent segments, thereby shorting the armature windings to these segments. When the magnetic field is not distorted, there is usually no voltage being induced in the shorted windings, and therefore no harmful results occur from the shorting of the windings. However, when the field is distorted, a voltage is induced in these shorted windings, and sparking takes place between the brushes and the commutator segments. Consequently, the commutator becomes pitted, the wear on the brushes becomes excessive, and the output of the generator is reduced. To correct this condition, the brushes are set so that the plane of the coils, which are shorted by the brushes, is perpendicular to the distorted magnetic field, which is accomplished by moving the brushes forward in the direction of rotation. This operation is called shifting the brushes to the neutral plane or plane of commutation. The neutral plane is the position where the plane of the two opposite coils is perpendicular to the magnetic field in the generator. On a few generators, the brushes can be shifted manually ahead of the normal neutral plane to the neutral plane caused by field distortion. On nonadjustable brush generators, the manufacturer sets the brushes for minimum sparking.

### Compensating Windings

Compensating windings or interpoles may be used to counteract some of the effects of field distortion, since shifting the brushes is inconvenient and unsatisfactory, especially when the speed and load of the generator are changing constantly.

Compensating Windings The compensating windings consist of a series of coils embedded in slots in the pole faces. These coils are also connected in series with the armature. Consequently, this series connection with the armature produces a magnetic field in the compensating windings that varies directly with the armature current. The compensating windings are wound in such a manner that the magnetic field produced by them counteracts the magnetic field produced by the armature. As a result, the neutral plane remains stationary any magnitude of armature current. With this design, once the brushes are set correctly, they do not need to be moved again. The figure illustrates how the windings are set into the pole faces.

N S N S N N S S A B Flux Pole Field winding Frame Flux Pole Field winding Frame

An interpole is a pole placed between the main poles of a generator. An example of interpole placement is shown in the figure. This is a simple two-pole generator with two interpoles.

An interpole has the same polarity as the next main pole in the direction of rotation. The magnetic flux produced by an interpole causes the current in the armature to change direction as an armature winding passes under it. This cancels the electromagnetic fields about the armature windings. The magnetic strength of the interpoles varies with the load on the generator; and since field distortion varies with the load, the magnetic field of the interpoles counteracts the effects of the field set up around the armature windings and minimizes field distortion. Thus, the interpole tends to keep the neutral plane in the same position for all loads on the generator; therefore, field distortion is reduced by the interpoles, and the efficiency, output, and service life of the brushes are improved.

### Types of DC Generators

There are three types of DC generators: series wound, shunt wound, and shunt series or compound wound. The difference in type depends on the relationship of the field winding to the external circuit.

#### Series Wound DC Generators

The field winding of a series generator is connected in series with the external circuit called the load. The field coils are composed of a few turns of large wire; the magnetic field strength depends more on the current flow rather than the number of turns in the coil. Series generators have very poor voltage regulation under changing load, since the greater the current through the field coils to the external circuit, the greater the induced emf and the greater the terminal or output voltage. Therefore, when the load is increased, the voltage increases; likewise, when the load is decreased, the voltage Mica V-ring Front V-ring Commutator bar Mica Iron shell Back V-ring with mica inner and outer rings for insulationSlots Tightening nut Iron ring Commutator bars Mica insulation between bars Commutator Slots Shaft Coils decreases. The output voltage of a series wound generator may be controlled by a rheostat in parallel with the field windings. Since the series wound generator has such poor regulation, it is never employed as an airplane generator. Generators in airplanes have field windings, which are connected either in shunt or in compound.

#### Shunt Wound DC Generators

A generator having a field winding connected in parallel with the external circuit is called a shunt generator. The field coils of a shunt generator contain many turns of small wire; the magnetic strength is derived from the large number of turns rather than the current strength through the coils. If a constant voltage is desired, the shunt wound generator is not suitable for rapidly fluctuating loads. Any increase in load causes a decrease in the terminal or output voltage, and any decrease in load causes an increase in terminal voltage; since the armature and the load are connected in series, all current flowing in the external circuit passes through the armature winding. Because of the resistance in the armature winding, there is a voltage drop (IR drop = current × resistance). As the load increases, the armature current increases and the IR drop in the armature increases. The voltage delivered to the terminals is the difference between the induced voltage and the voltage drop; therefore, there is a decrease in terminal voltage. This decrease in voltage causes a decrease in field strength, because the current in the field coils decreases in proportion to the decrease in terminal voltage; with a weaker field, the voltage is further decreased. When the load decreases, the output voltage increases accordingly, and a larger current flows in the windings. This action is cumulative, so the output voltage continues to rise to a point called field saturation, after which there is no further increase in output voltage.

The terminal voltage of a shunt generator can be controlled by means of a rheostat inserted in series with the field windings. As the resistance is increased, the field current is reduced; consequently, the generated voltage is reduced also. For a given setting of the field rheostat, the terminal voltage at the armature brushes is approximately equal to the generated voltage minus the IR N S Rotation + + + + a b Neutral plane Rotation ++ + + + + + + + ++ S N N S Rotation + + + + + + + + + + + ++++ a b A B C Field excited, armature unexcited Armature excited, field unexcited Both field and armature excited drop produced by the load current in the armature; thus, the voltage at the terminals of the generator drops as the load is applied. Certain voltage sensitive devices are available that automatically adjust the field rheostat to compensate for variations in load. When these devices are used, the terminal voltage remains essentially constant.

#### Compound Wound DC Generators

A compound wound generator combines a series winding and a shunt winding in such a way that the characteristics of each are used to advantage. The series field coils are made of a relatively small number of turns of large copper conductor, either circular or rectangular in cross section, and are connected in series with the armature circuit. These coils are mounted on the same poles on which the shunt field coils are mounted and, therefore, contribute a magnetomotive force which influences the main field flux of the generator. A diagrammatic and a schematic illustration of a compound wound generator is shown in the figure.

If the ampere turns of the series field act in the same direction as those of the shunt field, the combined magnetomotive force is equal to the sum of the series and shunt field components. Load is added to a compound generator in the same manner in which load is added to a shunt generator, by increasing the number of parallel paths across the generator terminals. Thus, the decrease in total load resistance with added load is accompanied by an increase in armature circuit and series field circuit current. The effect of the additive series field is that of increased field flux with increased load. The extent of the increased field flux depends on the degree of saturation of the field as determined by the shunt field current. Thus, the terminal voltage of the generator may increase or decrease with load, depending on the influence of the series field coils. This influence is referred to as the degree of compounding. A flat compound generator is one in which the no load and full load voltages have the same value; whereas an under compound generator has a full load voltage less than the no load value, and an over compound generator has a full load voltage which is higher than the no load value. Changes in terminal voltage with increasing load depend upon the degree of compounding.

If the series field aids the shunt field, the generator is said to be cumulative compounded. If the series field opposes the shunt field, the machine is said to be differentially compounded or is called a differential generator. Compound generators are usually designed to be overcompounded. This feature permits varied degrees of compounding by connecting a variable shunt across the series field. Such a shunt is sometimes called a diverter. Compound generators are used where voltage regulation is of prime importance.

Differential generators have somewhat the same characteristics as series generators in that they are essentially constant current generators. However, they generate rated voltage at no load, the voltage dropping materially as the load current increases. Constant current generators are ideally suited as power sources for electric arc welders and are used almost universally in electric arc welding.

If the shunt field of a compound generator is connected across both the armature and the series field, it is known as a long shunt connection, but if the shunt field is connected across the armature alone, it is called a short shunt connection. These connections produce essentially the same generator characteristics. A summary of the characteristics of the various types of generators discussed is shown in the figure.

### Generator Ratings

A generator is rated in power output. Since a generator is designed to operate at a specified voltage, the rating usually is given as the number of amperes the generator can safely supply at its rated voltage. Generator rating and performance data are stamped on the nameplate attached to the generator. When replacing a generator, it is important to choose one of the proper rating.

The rotation of generators is termed either clockwise or counterclockwise, as viewed from the driven end. Usually, the direction of rotation is stamped on the data plate. If no direction is stamped on the plate, the rotation may be marked by an arrow on the cover plate of the brush housing. It is important that a generator with the correct direction of rotation be used; otherwise, the voltage is reversed.

The speed of an aircraft engine varies from idle rpm to takeoff rpm; however, during the major portion of a flight, it is at a constant cruising speed. The generator drive is usually geared to revolve the generator between 11⁄8 and 11⁄2 times the engine crankshaft speed. Most aircraft generators have a speed at which they begin to produce their normal voltage. Termed the “coming in” speed, it is usually about 1,500 rpm.

### Generator Terminals

On most large 24-volt generators, electrical connections are made to terminals marked B, A, and E. The positive armature lead in the generator connects to the B terminal. The negative armature lead connects to the E terminal. The positive end of the shunt field winding connects to terminal A, and the opposite end connects to the negative terminal brush. Terminal A receives current from the negative generator brush through the shunt field winding. This current passes through the voltage regulator and back to the armature through the positive brush. Load current, which leaves the armature through the negative brushes, comes out of the E lead and passes through the load before returning to the armature through the positive brushes.

## 2. 中文翻译

### 工作原理

在学习交流电时曾介绍过发电机的基本原理，用来说明线圈在磁场中旋转如何产生交流电压。由于这是所有发电机工作的基础，因此有必要复习电能产生的原理。

当磁力线被穿过它们的导体切割时，导体中就会感应出电压。感应电压的大小取决于导体的速度和磁场的强度。如果把导体的两端连接成闭合回路，导体中就会感应出电流。导体和磁场就构成了一台最基本的发电机。

这台最简单的发电机如图所示，并连同外电路的各个组成部分一起（原文此处为图注碎片：generator Ahrs +28 vdc … Attitude/heading reference system Ahrs，混入正文，无对应正文）。

（原文此处为图注碎片：Autopilot computer 的接通电路，无对应正文）

（原文此处为图注碎片：Autopilot controller … Both field and armature excited，混入正文，无对应正文）电路，用来收集并使用这台简单发电机所产生的电能。导线回路安排在磁场中旋转。当导线回路的平面与磁力线平行时，回路中感应的电压使电流沿箭头所示的方向流动。这一位置感应的电压最大，因为导线与磁力线成直角切割，相对于磁场的任何其他位置每秒切割的磁力线都更多。当回路转到竖直位置时，感应电压减小，因为回路的两边（A 和 B）都大致与磁力线平行，切割速率降低。当回路处于竖直位置时，不切割任何磁力线，因为导线此时暂时平行于磁力线运动，没有感应电压。随着回路继续旋转，切割的磁力线条数增加，直到回路又转过 90° 到达水平面。在所示位置，切割的磁力线条数和感应电压再次达到最大。不过切割方向与此前的各个位置相反，因此感应电压的方向（极性）也反了过来。随着回路继续旋转，已切割的磁力线条数再次减少，在所示位置感应电压为零，因为导线 A 和 B 又平行于磁力线了。

如果把整个 360° 旋转过程中感应的电压绘制成曲线，就得到图中所示的曲线。这种电压称为交流电压，因为它先从正变到负，先朝一个方向，再朝另一个方向。

为了利用回路中产生的电压在外电路中形成电流，必须提供某种手段，把导线回路与外电路串联起来。这种电连接可以通过把导线回路断开、将其两端分别接到两个金属环上来实现，这种金属环称为滑环，两只金属或碳质电刷压在滑环上。电刷与外电路相连。把基本交流发电机的滑环换成两个半圆柱体（称为换向器），就得到一台基本的直流发电机。在这幅图中，线圈的黑色一侧接到黑色换向片，白色一侧接到白色换向片。各换向片之间相互绝缘。两个固定电刷放在换向器的相对两侧，其安装方式使换向片随回路一起旋转时每个电刷都与每个换向片接触。直流发电机的旋转部分（线圈和换向器）称为电枢。回路在磁场中旋转产生电动势的过程，对交流发电机和直流发电机来说是相同的，但换向器的作用产生了直流电压。

### 直流电压的产生

图中以基本的、分步的方式说明了直流电压是如何产生的。做法是让一个单匝导线回路在磁场中依次转过一系列位置。

回路从位置 A 开始顺时针旋转。不过线圈边没有切割任何磁力线，因此不产生电动势。图中黑色电刷正开始与换向器的黑色换向片接触，白色电刷正开始与白色换向片接触。

（原文此处为图注碎片：X-NOR gate input/output、Truth table、T0 T1 T2 T3 T4、NOR gate truth table 等，无对应正文）

在位置 B，磁通以最大速率被切割，这意味着感应电动势最大。此时黑色电刷与黑色换向片接触，白色电刷与白色换向片接触。表针向右偏转，指示出输出电压的极性。

在位置 C，回路已转过 180°。与位置 A 一样，没有磁通线被切割，输出电压为零。在位置 C 需要注意的重要情况是换向片与电刷的作用。处于 180° 角位置的黑色电刷与换向器一侧的黑色和白色换向片同时接触，白色电刷则与换向器另一侧的两个换向片同时接触。回路稍转过 180° 之后，黑色电刷只与白色换向片接触，白色电刷只与黑色换向片接触。

由于换向器件的这种切换作用，黑色电刷始终与向下运动的线圈边接触，白色电刷始终与向上运动的线圈边接触。尽管电流在回路中的实际换向方式与交流发电机完全相同，换向器的作用却使电流在外电路或表计中始终沿同一方向流动。

在位置 D，换向器作用使外电路中的电流反向，后半个周期的波形与前半个周期相同。换向过程有时称为整流，因为整流就是把交流电压转换为直流电压。

#### 中性面

当每个电刷同时接触换向器上的两个换向片时，就会产生直接短路。如果此时回路中产生了电动势，电路中就会流过很大的电流，产生电弧，从而损坏换向器。因此，电刷必须放在短路恰好发生在感应电动势为零的位置。这个位置称为中性面。如果电刷安装正确，电刷与换向器之间不会发生火花。火花是电刷位置不当的迹象，而电刷位置不当是换向不良的主要原因。

基本直流发电机产生的电压每转一周两次从零变到最大值。这种直流电压的变化称为“纹波”，可以通过使用更多的回路（线圈）来减小，如图所示。随着回路数增加，电压最大值与最小值之间的变化减小，发电机的输出电压趋近于稳定的直流值。回路数越多，换向片数按比例增加；也就是说，一个回路有两片换向片，两个回路有四片，四个回路有八片。

单匝回路感应出的电压很小。增加回路数并不提高发电机电压的最大值，但增加每个回路的匝数可以提高这个值。在较窄的范围内，直流发电机的输出电压由每个回路的匝数、电机每对磁极的总磁通以及电枢转速三者的乘积决定。

就旋转回路中产生电压的方法而言，交流发电机（或交流电机）与直流发电机完全相同。但是，如果电流通过滑环从回路引出，那就是交流电，该发电机称为交流发电机。如果电流通过换向器收集，那就是直流电，该发电机称为直流发电机。

### 直流发电机的结构特点

飞机上使用的发电机因各制造商不同，在设计上可能有所差异。但所有发电机的总体结构相同，工作方式也相似。直流发电机的主要部件（或组件）有磁场机架（或称磁轭）、旋转电枢和电刷组件。典型飞机发电机的零件如图所示。

磁场机架也称为磁轭，是发电机的底座或骨架。机架有两个作用：它构成磁极之间的磁路，并作为发电机其他部件的机械支撑。图中以横截面视图给出了两极发电机的机架。四极发电机的机架如图所示。

在小发电机中，机架由一整块铁制成，而在较大的发电机中，机架通常由用螺栓连在一起的两部分组成。机架具有良好的磁性能，与磁极铁心一起构成磁路的主要部分。磁场磁极用螺栓固定在机架内侧，形成安装励磁线圈绕组的铁心。磁极通常做成叠片，以减少涡流损耗，其作用与电磁铁的铁心相同，即集中励磁线圈产生的磁力线。整个机架（包括磁场磁极）由优质磁性铁或薄钢板制成。

实际的直流发电机使用电磁铁而不是永久磁铁。要用永久磁铁产生所需强度的磁场，会使发电机的物理尺寸大大增加。

励磁线圈由许多匝绝缘导线绕成，通常绕在套于磁极铁心上的骨架上，并牢固地固定在该铁心上。用来产生磁场的励磁电流流过励磁线圈，它由外部电源或电机自身发出的直流电提供。励磁线圈的绕组与磁极铁心之间没有电连接。

大多数励磁线圈的连接方式使各磁极呈现交替的极性。由于每一个南极总对应一个北极，因此任何发电机的磁极数必定是偶数。

注意，磁极铁心从机架上凸出。由于空气对磁场呈现很大的磁阻，这种设计缩短了磁极与旋转电枢之间的气隙长度，提高了发电机的效率。磁极铁心做成凸出形状时称为凸极。

发电机的电枢组件由绕在铁心上的许多电枢线圈、换向器以及相关的机械部件组成。这些附加的导线回路实际上称为绕组，它们沿电枢均匀分布，使各绕组之间的间距相同。电枢装在轴上，在励磁线圈产生的磁场中旋转。电枢铁心在磁场中起铁导体作用，因此做成叠片式，以防止涡流环流。

#### 环形电枢（Gramme 环）

电枢一般有两种：环形和鼓形。图中给出一个环形电枢，它由铁心、八段绕组和八片换向器组成。这种结构的缺点是，位于铁环内侧的绕组切割的磁力线很少，因此其中感应的电压很小。由于这个原因，Gramme 环形电枢没有得到广泛应用。

#### 鼓形电枢

鼓形电枢如图所示。电枢铁心呈鼓形，上面开有槽，电枢绕组嵌在槽中。其优点是每个绕组都完全包围铁心，因此导体的全长都切割磁通。这种结构感应的总电压远大于 Gramme 环形电枢。

鼓形电枢通常采用两种绕制方法之一：叠绕组和波绕组，每种方法各有优点。叠绕组用于设计为大电流的发电机。绕组接成并联支路，因此需要多个电刷。波绕组用于设计为高电压输出的发电机。每个线圈的两端接到相隔一个极距的换向片上，这样就使线圈形成串联，各个感应电压相加。

图中给出典型换向器的横截面视图。换向器位于电枢一端，由硬拉铜制成的楔形换向片组成，各片之间用薄云母片绝缘。换向片由钢制 V 形环或带螺栓的夹紧凸缘固定。云母环把换向片与凸缘绝缘。每个换向片凸起的部分称为升高片，电枢线圈的引线焊在升高片上。换向片没有升高片时，引线焊在换向片端部的短槽中。

电刷在换向器表面上滑行，在电枢线圈与外电路之间形成电接触。一根柔软的编织铜导体（通常称为辫线）把每个电刷与外电路连接起来。电刷通常由优质碳制成，装在用绝缘材料与机架隔开的刷握中，可以在刷握中自由上下移动，以跟随换向器表面的任何不平整。电刷通常可以调整，以便改变电刷对换向器的压力，并调整电刷相对于换向片的位置。

电刷与正在感应电压的线圈之间不断接通和断开，这就要求电刷材料具有一定的接触电阻。同时，这种材料的摩擦还必须小，以防止过度磨损。因此，电刷常用的材料是优质碳。碳必须足够软，以防换向器过度磨损，但又必须足够硬，以保证电刷有合理的使用寿命。由于碳的接触电阻相当高，电刷必须做得相当大，以提供较大的接触面积。换向器表面经过高度抛光，以尽可能减小摩擦。换向器上绝不可使用油或润滑脂，清洁时必须格外小心，以免损伤或划伤表面。

（原文此处为图注碎片：Connector ligs、Field frame、Drive end frame、Commutator end frame 等零件标注，无对应正文）

（原文此处为图注碎片：A B C D E、Induced EMF、Revolutions，无对应正文）

### 电枢反应

流过电枢的电流在绕组中建立起电磁场。这些新磁场会使发电机磁极之间的磁通偏离直线路径而发生畸变或弯曲。由于电枢电流随负载增大，畸变也随负载增加而加剧。磁场的这种畸变称为电枢反应。

发电机的电枢绕组按一定间隔分布，使电枢旋转过程中会出现电刷同时接触两个相邻换向片的某些位置，从而把这些换向片之间的电枢绕组短路。磁场未畸变时，被短路的绕组中通常没有感应电压，因此短路绕组不会产生有害后果。然而，当磁场畸变时，这些被短路的绕组中就会感应出电压，电刷与换向片之间便产生火花。于是换向器被烧蚀出麻点，电刷磨损过度，发电机的输出降低。为纠正这种情况，要调整电刷位置，使被电刷短路的线圈平面垂直于畸变后的磁场，做法是把电刷沿旋转方向向前移动。这一操作称为把电刷移到中性面或换向面。中性面是两个相对线圈的平面垂直于发电机磁场的位置。在少数发电机上，电刷可以手动从正常中性面向前移到由磁场畸变造成的中性面。在电刷不可调的发电机上，制造厂把电刷设定在火花最小的位置。

### 补偿绕组

由于移动电刷很不方便且效果不理想（尤其是在发电机转速和负载不断变化时），可以采用补偿绕组或换向极来抵消磁场畸变的部分影响。

补偿绕组　补偿绕组由嵌入磁极面槽中的一系列线圈组成。这些线圈也与电枢串联。因此，这种与电枢的串联连接使补偿绕组中产生的磁场随电枢电流成正比变化。补偿绕组的绕制方式使其产生的磁场抵消电枢产生的磁场。结果，无论电枢电流大小如何，中性面都保持不动。采用这种设计，电刷一旦调好，就无需再移动。图中说明了绕组的嵌放方式。

（原文此处为图注碎片：N S N S、Flux、Pole、Field winding、Frame，无对应正文）

换向极是装在发电机主磁极之间的磁极。图中给出换向极布置的一个例子。这是一台带两个换向极的简单两极发电机。

换向极的极性与旋转方向上相邻的主磁极相同。换向极产生的磁通使电枢绕组经过其下方时电枢中的电流改变方向。这抵消了电枢绕组周围的电磁场。换向极的磁性强弱随发电机负载变化；由于磁场畸变随负载变化，换向极的磁场抵消电枢绕组周围建立的磁场的影响，使磁场畸变减到最小。因此，换向极在所有负载下都趋向于使中性面保持同一位置；所以换向极减小了磁场畸变，提高了效率、输出和电刷的使用寿命。

### 直流发电机的类型

直流发电机有三种类型：串励、并励以及并串联（复励）。类型的区别取决于励磁绕组与外电路的关系。

#### 串励直流发电机

串励发电机的励磁绕组与外电路（称为负载）串联。励磁线圈由少量大截面导线的匝组成；磁场强度更多取决于电流大小，而不是线圈的匝数。串励发电机在负载变化时电压调整率很差，因为通过励磁线圈流向外部电路的电流越大，感应电动势越大，端电压或输出电压也越高。因此，负载增加时电压升高；同样，负载减小时电压（原文此处为图注碎片：Mica V-ring、Commutator bar、Tightening nut、Coils，混入正文，无对应正文）降低。串励发电机的输出电压可以用与励磁绕组并联的变阻器来控制。由于串励发电机的电压调整率很差，它从不作为飞机发电机使用。飞机上的发电机都带励磁绕组，绕组接成并励或复励。

#### 并励直流发电机

励磁绕组与外电路并联的发电机称为并励发电机。并励发电机的励磁线圈包含许多匝细导线；磁场强度来自匝数多，而不是线圈中电流大。如果要求电压恒定，并励发电机不适合快速波动的负载。负载的任何增加都会使端电压或输出电压下降，负载的任何减小都会使端电压上升；由于电枢与负载串联，外电路中的全部电流都流过电枢绕组。由于电枢绕组有电阻，会产生电压降（IR 降 = 电流 × 电阻）。负载增加时，电枢电流增大，电枢中的 IR 降增大。送到端钮的电压是感应电压与电压降之差；因此端电压下降。这个电压下降又使磁场强度减弱，因为励磁线圈中的电流随端电压下降而成比例减小；磁场变弱，电压又进一步降低。负载减小时，输出电压相应升高，绕组中流过更大的电流。这种作用是累积性的，所以输出电压继续上升，直到称为磁场饱和的一点，此后输出电压不再增加。

并励发电机的端电压可以通过串接在励磁绕组中的变阻器来控制。电阻增大时，励磁电流减小，于是产生的电压也随之降低。对于磁场变阻器的某一给定位置，电枢电刷处的端电压大致等于产生的电压减去负载电流在电枢中产生的 IR 降（原文此处为图注碎片：Neutral plane、Both field and armature excited，混入正文，无对应正文）；因此，加上负载时发电机的端电压下降。有一些电压敏感器件可以自动调节磁场变阻器，以补偿负载变化。使用这些器件时，端电压基本保持恒定。

#### 复励直流发电机

复励发电机把串励绕组和并励绕组组合起来，使两者的特性都能得到有利利用。串励磁场线圈由数量相对较少的几匝大截面铜导体绕成（截面可为圆形或矩形），并与电枢电路串联。这些线圈装在并励磁场线圈所在的同一磁极上，因此产生一个磁动势，影响发电机的主磁场磁通。图中给出了复励发电机的原理图和接线图。

如果串励磁场的安匝与并励磁场方向相同，则合成的磁动势等于串励与并励磁场分量之和。给复励发电机加负载的方式与给并励发电机加负载相同，即增加跨接在发电机端钮上的并联支路数。因此，随着负载增加，总负载电阻减小，同时电枢电路和串励磁场电路中的电流增大。附加串励磁场的作用是使磁场磁通随负载增加而增加。磁场磁通增加的幅度取决于并励电流所决定的磁场饱和程度。因此，发电机的端电压可能随负载升高或降低，取决于串励磁场线圈的影响。这种影响称为复励程度。平复励发电机是空载电压与满载电压相同的一种发电机；而欠复励发电机的满载电压低于空载值，过复励发电机的满载电压则高于空载值。端电压随负载增加的变化取决于复励程度。

如果串励磁场助磁并励磁场，则称该发电机为积复励。如果串励磁场去磁并励磁场，则称该电机为差复励，或称为差复励发电机。复励发电机通常设计成过复励。这一特点允许通过在串励磁场上并联可变分流器来获得不同的复励程度。这种分流器有时称为分流电阻。复励发电机用于电压调整率至关重要的场合。

差复励发电机具有与串励发电机大致相同的特性，因为它们本质上都是恒流发电机。不过，它们在空载时就能产生额定电压，而随着负载电流增加，电压显著下降。恒流发电机非常适合作电弧焊机的电源，几乎普遍用于电弧焊接。

如果复励发电机的并励磁场跨接在电枢和串励磁场两端，则称为长并励连接；如果并励磁场仅跨接在电枢两端，则称为短并励连接。这两种连接产生的发电机特性基本相同。图中给出了所讨论的各种发电机特性的汇总。

### 发电机的额定值

发电机的额定值按输出功率表示。由于发电机设计在规定的电压下工作，额定值通常用发电机在额定电压下能安全提供的安培数来表示。发电机的额定值和性能数据打在发电机附带的铭牌上。更换发电机时，重要的是选择额定值合适的发电机。

发电机的旋转方向，从驱动端看，有顺时针和逆时针两种说法。通常旋转方向打在数据牌上。如果数据牌上没有标明方向，则可在电刷罩的盖板上用箭头标出旋转方向。必须使用旋转方向正确的发电机，否则电压会反向。

飞机发动机的转速从慢车转速到起飞转速变化；不过，在飞行的大部分时间里，发动机处于恒定的巡航转速。发电机传动装置通常设计成使发电机的转速为发动机曲轴转速的 1 1/8 到 1 1/2 倍。大多数飞机发电机都有一个开始产生正常电压的转速，称为“切入”转速，通常约为 1,500 rpm。

### 发电机端钮

在大多数大型 24 伏发电机上，电气连接接到标有 B、A 和 E 的端钮上。发电机中正电枢引线接到 B 端钮，负电枢引线接到 E 端钮。并励绕组的正端接到 A 端钮，另一端接到负电刷。A 端钮通过并励绕组接收来自发电机负电刷的电流。该电流经过电压调节器，再经正电刷回到电枢。负载电流从负电刷离开电枢，经 E 引线流出，通过负载后再经正电刷回到电枢。

## 3. 专业词汇

| 英文 | 词性 | 中文 | 本节语境 |
| --- | --- | --- | --- |
| armature | n. | 电枢 | 直流发电机的旋转部分，由线圈和换向器组成 |
| commutator | n. | 换向器 | 由两个半圆柱或楔形铜片构成，使回路输出变为直流 |
| brush | n. | 电刷 | 压在滑环或换向器上、与外电路相连的碳质导电件 |
| slip ring | n.phr. | 滑环 | 交流发电机集流用的金属环；换成换向器即成直流发电机 |
| yoke | n. | 磁轭 | 又称 field frame，构成磁路并支撑其他部件的机架 |
| field coil | n.phr. | 励磁线圈 | 绕在磁极铁心上、通励磁电流以产生磁场的线圈 |
| neutral plane | n.phr. | 中性面 | 电刷短路的线圈平面垂直于磁场、感应电动势为零的位置 |
| armature reaction | n.phr. | 电枢反应 | 电枢电流磁场使磁极间磁通发生畸变的现象 |
| interpole | n. | 换向极 | 装在主磁极之间、抵消电枢反应以改善换向的磁极 |
| compensating winding | n.phr. | 补偿绕组 | 嵌入磁极面槽中、与电枢串联以抵消电枢磁场的绕组 |
| salient pole | n.phr. | 凸极 | 从机架凸出、缩短气隙以增大效率的磁极 |
| ripple | n. | 纹波 | 直流电压每转两次波动的现象，增多回路可减小 |
| compounding | n. | 复励（程度） | 串励磁场对并励磁场助磁或去磁的强弱程度 |
| field saturation | n.phr. | 磁场饱和 | 输出电压随负载升高到一定程度后不再增加的极限点 |
| voltage regulation | n.phr. | 电压调整率 | 负载变化时端电压保持稳定的能力 |

## 4. 语法解析

### ① since 原因从句 + it 形式主语 + necessary to
**原句**：Since this is the basis for all generator operation, it is necessary to review the principles of generation of electrical energy.
**拆解**：Since this is the basis for all generator operation 为原因状语从句（this 指前句所说的线圈在磁场中旋转发电的原理）；主句 it 为形式主语，真正主语是不定式 to review the principles of generation of electrical energy，is necessary 为系表结构。
**要点**：since 在此表“由于”，比 because 语气弱，多置于句首。It is necessary to do sth 是技术文本高频句型，译作“有必要……”。注意 principles of generation of electrical energy 中三个 of 层层限定，翻译时应由后向前逐层剥开：“电能产生的原理”，不能顺译成“原理的产生”。
### ② when 时间状语从句（被动）+ 现在分词短语作后置定语
**原句**：When lines of magnetic force are cut by a conductor passing through them, voltage is induced in the conductor.
**拆解**：When 引导时间状语从句，从句主语 lines of magnetic force，谓语为被动 are cut by a conductor；passing through them 为现在分词短语作后置定语修饰 conductor（them 指 the lines of magnetic force）；主句 voltage is induced in the conductor 为被动结构。
**要点**：科技英语大量使用被动语态以突出动作承受者，本句主从句均为被动，译成汉语时可转为主动“导体切割磁力线时，导体中就会感应出电压”。现在分词后置定语与被修饰词是主动关系（导体切割磁力线），过去分词则表被动；判断主动/被动关系是分词题的核心。
### ③ since 原因从句 + thus + 现在分词结果状语 + 比较结构
**原句**：The voltage induced at this position is maximum, since the wires are cutting the lines of force at right angles, thus cutting more lines of force per second than in any other position relative to the magnetic field.
**拆解**：主句 The voltage induced at this position is maximum（induced at this position 为过去分词短语作后置定语）；since 引导原因状语从句 the wires are cutting the lines of force at right angles；thus cutting … 为现在分词短语作结果状语；than in any other position 为比较结构，省略了重复的谓语和主语。
**要点**：thus + 现在分词表示“从而……”，是结果状语的常见形式，不能写成 thus cut。比较结构 than in any other position 后省略了 the wires cut lines of force，补全后才能看清比较对象；than 后接介词短语时比较的是状语，注意不要误把 than 当连词接完整从句。at right angles 意为“成直角”，是固定搭配，不可写 at right angle。
### ④ 与现在事实相反的虚拟语气 + 现在分词结果状语
**原句**：If an emf were generated in the loop at this time, a high current would flow in the circuit, causing an arc and thus damaging the commutator.
**拆解**：If 引导的虚拟条件从句用 were generated（与现在事实相反，从句谓语用过去式/were + 过去分词），主句用 would flow；causing an arc and thus damaging the commutator 为现在分词短语作结果状语，两个分词由 and 并列。
**要点**：与现在事实相反的虚拟：从句 were/did，主句 would/could/might + 动词原形。emf 是 electromotive force 的缩写，作单数。分词结果状语 causing … 的逻辑主语是前面整句所述情况（高电流流动），不是 a high current 本身，翻译时应译成“从而产生电弧、损坏换向器”。
### ⑤ 被动语态 + product of 三项并列
**原句**：Within narrow limits, the output voltage of a DC generator is determined by the product of the number of turns per loop, the total flux per pair of poles in the machine, and the speed of rotation of the armature.
**拆解**：介词短语 Within narrow limits 作状语；主语 the output voltage of a DC generator；谓语为被动 is determined by；宾语 the product of A, B, and C 中 A、B、C 为三项并列：the number of turns per loop、the total flux per pair of poles in the machine、the speed of rotation of the armature。
**要点**：be determined by 后接 product of 时，三项并列由逗号与 and 分隔，最后一项前的逗号不可省（三项以上并列的牛津逗号）。翻译时“由……三者的乘积决定”，注意每项内部的 of 短语要整体译，如 the number of turns per loop 是“每个回路的匝数”而非“匝数的数量”。Within narrow limits 表示结论有适用范围，译作“在较窄的范围内”。
### ⑥ 过去分词短语作插入定语 + be free to do + in order to
**原句**：The brushes, usually made of high-grade carbon and held in place by brush holders insulated from the frame, are free to slide up and down in their holders in order to follow any irregularities in the surface of the commutator.
**拆解**：主语 The brushes 后接两个并列过去分词短语 usually made of high-grade carbon 与 held in place by brush holders（insulated from the frame 为过去分词短语修饰 holders）作插入式后置定语；谓语 are free to slide up and down；in order to follow … 为目的状语。
**要点**：be free to do 意为“可以自由地做”，不要译成“免费”。insulated from the frame 中的 insulated 是过去分词作定语，与 brush holders 是被动关系（刷握被绝缘）。插入定语较长时，汉语宜拆成独立短句“电刷通常由优质碳制成，装在……刷握中”。in order to 表目的，可与 so as to 互换，但 so as to 不置于句首。
