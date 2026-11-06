# Principles of Gyroscopic Instruments

> 机体 Ch 10 · Principles of Gyroscopic Instruments · 原文 PDF 第 570 页

## 1. 原文

### Mechanical Gyros

Three of the most common flight instruments, the attitude indicator, heading indicator, and turn needle of the turn-and-bank indicator, are controlled by gyroscopes. To understand how these instruments operate, knowledge of gyroscopic principles and instrument power systems is required.

A mechanical gyroscope, or gyro, is comprised of a wheel or rotor with its mass concentrated around its perimeter. The rotor has bearings to enable it to spin at high speeds.

Different mounting configurations are available for the rotor and axle, which allow the rotor assembly to rotate about one or two axes perpendicular to its axis of spin. To suspend the rotor for rotation, the axle is first mounted in a supporting ring called a gimbal. If brackets are attached 90° around the supporting ring from where the spin axle attached, the supporting ring and rotor can both move freely 360°. When in this configuration, the gyro is said to be a captive gyro. It can rotate about only one axis that is perpendicular to the axis of spin.

The supporting ring can also be mounted inside an outer ring. The bearing points are the same as the bracket just described, 90° around the supporting ring from where the spin axle attached. Attachment of a bracket to this outer ring allows the rotor to rotate in two planes while spinning. Both of these are perpendicular to the spin axis of the rotor. The plane that the rotor spins in due to its rotation about its axle is not counted as a plane of rotation.

A gyroscope with this configuration, two rings plus the mounting bracket, is said to be a free gyro because it is free to rotate about two axes that are both perpendicular to the rotor’s spin axis. As a result, the supporting ring with spinning gyro mounted inside is free to turn 360° inside the outer ring.

Unless the rotor of a gyro is spinning, it has no unusual properties; it is simply a wheel universally mounted. When the rotor is rotated at a high speed, the gyro exhibits a couple of unique characteristics. The first is called gyroscopic rigidity, or rigidity in space. This means that the rotor of a free gyro always points in the same direction no matter which way the base of the gyro is positioned.

Gyroscopic rigidity depends upon several design factors:

1. Weight—for a given size, a heavy mass is more resistant to disturbing forces than a light mass.

2. Angular velocity—the higher the rotational speed, the greater the rigidity or resistance is to deflection.

3. Radius at which the weight is concentrated— maximum effect is obtained from a mass when its principal weight is concentrated near the rim, rotating at high speed.

4. Bearing friction—any friction applies a deflecting force to a gyro. Minimum bearing friction keeps deflecting forces at a minimum.

This characteristic of gyros to remain rigid in space is exploited in the attitude-indicating instruments and the directional indicators that use gyros. The spinning gyro remains fixed in space and the airplane moves around it. It acts as a reference to allow measurement of changes in attitude or direction.

Precession is a second important characteristic of gyroscopes. By applying a force to the horizontal axis of the gyro, a unique phenomenon occurs. The applied force is resisted. Instead of responding to the force by moving about the horizontal axis, the gyro moves in response about its vertical axis. Stated another way, an applied force to the axis of the spinning gyro does not cause the axis to tilt. Rather, the gyro responds as though the force was applied 90° around in the direction of rotation of the gyro rotor. The gyro rotates rather than tilts. This predictable controlled precession of a gyroscope is utilized in a turn and bank instrument.

### Solid State Gyros & Related Systems

Improved attitude and direction information is always a goal in aviation. Modern aircraft make use of highly accurate solid-state attitude and directional devices with no moving parts. This results in very high reliability and low maintenance.

#### Ring Laser Gyros (RLG)

The ring laser gyro (RLG) is widely used in commercial aviation. The basis for RLG operation is that it takes time for light to travel around a stationary, nonrotating circular path. Light takes longer to complete the journey if the path is rotating in the same direction as the light is traveling. And, it takes less time for the light to complete the loop if the path is rotating in the direction opposite to that of the light. Essentially, the path is made longer or shorter by the rotation of the path. This is known as the Sagnac effect.

A laser is light amplification by stimulated emission of radiation. A laser operates by exciting atoms in plasma to release electromagnetic energy, or photons. A ring laser gyro produces laser beams that travel in opposite directions around a closed triangular cavity. The wavelength of the light traveling around the loop is fixed. As the loop rotates, the path the lasers must travel lengthens or shortens. The light wavelengths compress or expand to complete travel around the loop as the loop changes its effective length. As the wavelengths change, the frequencies also change. By examining the difference in the frequencies of the two counter-rotating beams of light, the rate at which the path is rotating can be measured. A piezoelectric dithering motor in the center of the unit vibrates to prevent lock-in of the output signal at low rotational speeds. It causes units installed on aircraft to hum when operating.

An RLG is remotely mounted so the cavity path rotates around one of the axes of flight. The rate of frequency phase shift detected between the counter-rotating lasers is proportional to the rate that the aircraft is moving about that axis. On aircraft, an RLG is installed for each axis of flight. Output can be used in analog instrumentation and autopilot systems. It is also easily made compatible for use by digital display computers and for digital autopilot computers.

RLGs are very rugged and have a long service life with virtually no maintenance due to their lack of moving parts. They measure movement about an axis extremely quickly and provide continuous output. They are extremely accurate and generally are considered superior to mechanical gyroscopes.

On aircraft, microelectromechanical systems (MEMS) devices save space and weight. Through the use of solid-state MEMS devices, reliability is increased primarily due to the lack of moving parts. The development of MEMS technology for use in aviation instrumentation integrates with the use of ADCs. This newest improvement in technology is low cost and promises to proliferate through all forms of aviation.

MEMS for gyroscopic applications are used in small, general aviation aircraft, as well as larger commercial aircraft. Tiny vibration-based units with resistance and capacitance measuring pick-offs are accurate and reliable and only a few millimeters in length and width. They are normally integrated into a complete micro-electronic solid-state chip designed to yield an output after various conditioning processes are performed. The chips, which are analogous to tiny circuit boards, can be packaged for installation inside a dedicated computer or module that is installed on the aircraft.

While a large mechanical gyroscope spins in a plane, its rigidity in space is used to observe and measure the movement of the aircraft. The basis of operation of many MEMS gyroscopes is the same despite their tiny size. The difference is that a vibrating or oscillating piezoelectric device replaces the spinning, weighted ring of the mechanical gyro. Still, once set in motion, any out-of-plane motion is detectable by varying microvoltages or capacitances detected through geometrically arranged pickups. Since piezoelectric substances have a relationship between movement and electricity, microelectrical stimulation can set a piezoelectric gyro in motion and the tiny voltages produced via the movement in the piezo can be extracted. They can be input as the required variables needed to compute attitude or direction In modern aircraft, attitude heading and reference systems (AHRS) have taken the place of the gyroscope and other individual instruments. While MEMS devices provide part of the attitude information for the system, GPS, solid state magnetometers, solid state accelerometers, and digital air data signals are all combined in an AHRS to compute and output highly reliable information for display on a flight deck panel.

#### Other Attitude & Directional Systems

## 2. 中文翻译

### 机械陀螺

三种最常见的飞行仪表——姿态指示器、航向指示器以及转弯侧滑仪的转弯指针——都由陀螺仪控制。要理解这些仪表如何工作，需要掌握陀螺原理和仪表动力系统的知识。

机械陀螺仪（简称陀螺）由一个质量集中于轮缘的轮子或转子构成。转子装有轴承，使其能高速旋转。

转子和轴有不同的安装方式，可使转子组件绕一条或两条垂直于自转轴的轴线转动。为使转子能悬挂着转动，先把轴装在一个称为常平环（gimbal）的支承环中。若在支承环上距自转轴连接点 90° 处装上支架，支承环和转子便都能自由地做 360° 运动。处于这种构型时，该陀螺称为受限陀螺（captive gyro），它只能绕一条垂直于自转轴的轴线转动。

支承环也可以装在一个外环之内。轴承位置与刚才所说的支架相同，即在支承环上距自转轴连接点 90° 处。把支架装到这个外环上，转子在旋转时便可在两个平面内转动，这两个平面都垂直于转子的自转轴。转子绕其轴自转所形成的平面不计为一个转动平面。

具有这种构型（两个环加安装支架）的陀螺称为自由陀螺，因为它可绕两条都垂直于转子自转轴的轴线自由转动。因此，内装旋转陀螺的支承环能在外部环内自由做 360° 转动。

除非陀螺的转子在旋转，否则它并没有什么特殊性质，只不过是一个万向安装的轮子。当转子高速旋转时，陀螺会表现出两个独特特性。第一个称为陀螺刚性，或称空间刚性。这意味着无论陀螺的基座怎样放置，自由陀螺的转子始终指向同一方向。

陀螺刚性取决于几个设计因素：

1. 重量——在给定尺寸下，重的质量比轻的质量更能抵抗干扰力。

2. 角速度——转速越高，刚性或抗偏转能力越大。

3. 重量集中的半径——当质量的主要部分集中在轮缘附近并高速旋转时，可获得最大效果。

4. 轴承摩擦——任何摩擦都会对陀螺施加偏转力。轴承摩擦最小，偏转力才能保持在最低限度。

陀螺在空间中保持刚性的这一特性，被用于姿态指示仪表和采用陀螺的方向指示器。旋转的陀螺在空间保持固定，飞机则绕它运动。它作为一个基准，用来测量姿态或方向的变化。

进动是陀螺的第二个重要特性。对陀螺的水平轴施加一个力，会出现一种独特现象：施加的力受到抵抗，陀螺并不绕水平轴运动来响应这个力，而是绕其垂直轴运动来响应。换句话说，对旋转陀螺的轴施加力，并不会使该轴倾斜；陀螺的响应方式，就好像力是施加在沿陀螺转子旋转方向前方 90° 处一样。陀螺是转动而不是倾斜。这种可预测、受控的陀螺进动被用于转弯侧滑仪。

### 固态陀螺及相关系统

改善姿态与方向信息始终是航空追求的目标。现代飞机采用无运动部件的高精度固态姿态与方向装置，因而可靠性很高、维护量很低。

#### 环形激光陀螺（RLG）

环形激光陀螺（RLG）在商用航空中广泛使用。RLG 工作的基本原理是：光沿一条静止不转的圆形路径行进需要时间；如果路径沿光的行进方向转动，光走完一圈所需时间就更长；如果路径沿与光相反的方向转动，光走完一圈所需时间就更短。实质上是路径的转动使路径变长或变短。这称为萨格纳克效应（Sagnac effect）。

激光（laser）是“受激辐射光放大”的缩写。激光器通过激发等离子体中的原子释放电磁能（即光子）来工作。环形激光陀螺产生两束沿封闭三角形腔体反向传播的激光。绕环路行进的光的波长是固定的。当环路转动时，激光必须行进的路径变长或变短。随着环路有效长度改变，光波长压缩或伸长，以完成绕环路的行程。波长改变时频率也随之改变。通过检测两束反向旋转光的频率差，即可测出路径转动的速率。组件中心的一个压电抖动马达会振动，以防止低转速时输出信号“锁定”。这使装在飞机上的组件工作时发出嗡鸣声。

RLG 采用远程安装，使其腔体路径绕飞行的一条轴转动。两束反向旋转激光之间检测到的频率相移速率，与飞机绕该轴运动的速率成正比。飞机上，每条飞行轴各装一个 RLG。其输出可用于模拟式仪表和自动驾驶仪系统，也很容易做到与数字显示计算机和数字自动驾驶仪计算机兼容。

RLG 非常坚固，使用寿命长，由于没有运动部件，几乎无需维护。它们能极快地测量绕轴的转动并提供连续输出。其精度极高，通常被认为优于机械陀螺。

飞机上，微机电系统（MEMS）器件可节省空间与重量。通过采用固态 MEMS 器件，可靠性得以提高，主要原因是没有运动部件。用于航空仪表的 MEMS 技术的发展，与大气数据计算机（ADC）的使用相结合。这项最新的技术进步成本低，有望在所有航空领域普及。

用于陀螺应用的 MEMS 既用于小型通用航空飞机，也用于大型商用飞机。微小的、基于振动的器件配以电阻和电容测量拾取装置，精确可靠，长度和宽度仅几毫米。它们通常集成在一个完整的微电子固态芯片中，芯片经各种调理处理后给出输出。这些芯片类似于微型电路板，可封装起来装入安装在飞机上的专用计算机或模块内。

大型机械陀螺在一个平面内旋转，利用其空间刚性来观测和测量飞机的运动。许多 MEMS 陀螺尽管体积很小，其工作原理却相同。区别在于，用振动的压电装置取代了机械陀螺中旋转的配重环。同样，一旦使它运动起来，任何平面外运动都可通过按几何布置的拾取装置检测到的微小电压变化或电容变化而测得。由于压电材料在运动与电之间具有对应关系，微电激励可使压电陀螺运动起来，并可提取压电体因运动产生的微小电压。这些电压可作为计算姿态或方向所需的变量输入。在现代飞机上，姿态航向基准系统（AHRS）已取代陀螺仪和其他单个仪表。MEMS 器件为该系统提供部分姿态信息，而 GPS、固态磁强计、固态加速度计和数字大气数据信号都在 AHRS 中综合起来，计算并输出高度可靠的信息，供驾驶舱面板显示。

#### 其他姿态与方向系统

## 3. 专业词汇

| 英文 | 词性 | 中文 | 本节语境 |
| --- | --- | --- | --- |
| gyroscope | n. | 陀螺仪 | 高速旋转的转子，具有空间刚性和进动两大特性 |
| rotor | n. | 转子 | 质量集中于轮缘的轮子，靠轴承支承高速旋转 |
| gimbal | n. | 常平环 | 支承转子轴的环，使转子可绕自转轴以外的轴转动 |
| captive gyro | n. | 受限陀螺 | 只能绕一条垂直于自转轴的轴线转动的陀螺构型 |
| free gyro | n. | 自由陀螺 | 两环加支架、可绕两条轴自由转动 360° 的陀螺 |
| gyroscopic rigidity | n. | 陀螺刚性（空间刚性） | 转子指向在空间中保持不变的特性，是姿态仪表的基础 |
| precession | n. | 进动 | 对自转轴施力时陀螺绕垂直轴转动的可预测响应 |
| ring laser gyro (RLG) | n. | 环形激光陀螺 | 无运动部件的固态陀螺，靠反向激光的频率差测角速率 |
| Sagnac effect | n. | 萨格纳克效应 | 光路随腔体转动而变长变短、引起频率差的物理现象 |
| dithering motor | n. | 抖动马达 | RLG 中心的压电马达，抖动以防低转速时信号锁定 |
| MEMS | n. | 微机电系统 | 毫米级固态传感器件，无运动部件、可靠性高 |
| AHRS | n. | 姿态航向基准系统 | 综合 MEMS、GPS、磁强计与大气数据算出姿态航向 |
| pick-off | n. | 拾取装置 | 按几何布置、把微小位移转成电压或电容变化的元件 |
| piezoelectric | adj. | 压电的 | 受力产生电压、通电产生形变的材料特性，用作振动陀螺驱动 |

## 4. 语法解析

### ① 不定式短语作目的状语 + 被动谓语
**原句**：To understand how these instruments operate, knowledge of gyroscopic principles and instrument power systems is required.
**拆解**：句首不定式短语 To understand how these instruments operate 作目的状语，其中 how 引导宾语从句作 understand 的宾语；主句主语 knowledge of gyroscopic principles and instrument power systems（介词短语作后置定语），谓语 is required 为被动。
**要点**：目的状语提到句首是为了承接上文，主干其实只有 knowledge ... is required 五个词。knowledge 是不可数名词，故谓语用 is；of 引出的两层并列成分（gyroscopic principles / instrument power systems）共同修饰 knowledge。

### ② 条件状语从句 + from where 引导的宾语从句
**原句**：If brackets are attached 90° around the supporting ring from where the spin axle attached, the supporting ring and rotor can both move freely 360°.
**拆解**：If 引导条件状语从句，从句为被动 are attached，90° around the supporting ring 为地点/角度状语，from where the spin axle attached 为介词 from + 关系副词 where 引导的从句；主句主语 the supporting ring and rotor，谓语 can move，freely 360° 为方式与程度状语。
**要点**：from where 相当于“从……的位置”，where 指代 the point on the supporting ring，不能换成 from which（which 不能直接指地点）。attached 在此是过去分词作后置定语（轴被连接的部位），与前面的 are attached 不是同一结构，读时不要重复理解成两个谓语。

### ③ unless 条件从句 + 分号并列 + 过去分词后置定语
**原句**：Unless the rotor of a gyro is spinning, it has no unusual properties; it is simply a wheel universally mounted.
**拆解**：Unless 引导否定条件状语从句（= if ... not），从句用现在进行时 is spinning 表状态；主句 it has no unusual properties；分号后为并列分句，it is simply a wheel，universally mounted 为过去分词短语作后置定语。
**要点**：unless 本身含否定，从句不能再加 not。universally mounted 是“被万向安装的”，过去分词表被动；若写成 mounting 则变成轮子去安装别的东西，逻辑不通。

### ④ no matter which 引导让步状语从句
**原句**：This means that the rotor of a free gyro always points in the same direction no matter which way the base of the gyro is positioned.
**拆解**：主句主语 This，谓语 means，宾语为 that 引导的宾语从句；宾语从句中主语 the rotor of a free gyro，谓语 points，in the same direction 为方向状语；no matter which way 引导让步状语从句，从句 the base of the gyro is positioned 为被动。
**要点**：no matter which way = however the base is positioned，语序必须是“疑问词 + 名词 + 陈述语序”，不能写成 no matter which way is the base positioned。that 从句里再套让步从句，共三层，翻译时先把主干“转子总指向同一方向”拎出来。

### ⑤ by + 动名词作方式状语 + 定语从句 + 被动谓语
**原句**：By examining the difference in the frequencies of the two counter-rotating beams of light, the rate at which the path is rotating can be measured.
**拆解**：By + 动名词短语 examining the difference... 作方式状语；主句主语 the rate，后接 at which 引导的定语从句 the path is rotating（at the rate 为固定搭配）；谓语 can be measured 为被动。
**要点**：定语从句的介词 at 提到 which 之前，是因为先行词 the rate 与 at 搭配（at the rate of...）。主句谓语是 can be measured，主语 the rate 被定语从句隔开，找主干时要跳过 at which ... 这一整段。
