# Inertial Navigation System (INS)/Inertial Reference System (IRS)

> 机体 Ch 11 · Inertial Navigation System (INS)/Inertial Reference System (IRS) · 原文 PDF 第 672 页

## 1. 原文

An inertial navigation system (INS) is used on some large aircraft for long range navigation. This may also be identified as an inertial reference system (IRS), although the IRS designation is generally reserved for more modern systems. An INS/IRS is a self-contained system that does not require input radio signals from a ground navigation facility or transmitter. The system derives attitude, velocity, and direction information from measurement of the aircraft’s accelerations given a known starting point. The location of the aircraft is continuously updated through calculations based on the forces experienced by INS accelerometers. A minimum of two accelerometers is used, one referenced to north, and the other referenced to east. In older units, they are mounted on a gyro-stabilized platform. This averts the introduction of errors that may result from acceleration due to gravity.

An INS uses complex calculation made by an INS computer to convert applied forces into location information. An interface control head is used to enter starting location position data while the aircraft is stationary on the ground. This is called initializing. From then on, all motion of the aircraft is sensed by the built-in accelerometers and run through the computer. Feedback and correction loops are used to correct for accumulated error as flight time progresses. The amount an INS is off in one hour of flight time is a reference point for determining performance. Accumulated error of less than one mile after one hour of flight is possible. Continuous accurate adjustment to the gyro-stabilized platform to keep it parallel to the Earth’s surface is a key requirement to reduce accumulated error. A latitude/longitude coordinate system is used when giving the location output.

INS is integrated into an airliner’s flight management system and automatic flight control system. Waypoints can be entered for a predetermined flightpath and the INS will guide the aircraft to each waypoint in succession. Integration with other NA V aids is also possible to ensure continuous correction and improved accuracy but is not required.

Modern INS systems are known as IRS. They are completely solid-state units with no moving parts. Three-ring, laser gyros replace the mechanical gyros in the older INS platform systems. This eliminates precession and other mechanical gyro shortcomings. The use of three solid-state accelerometers, one for each plane of movement, also increases accuracy. The accelerometer and gyro output are input to the computer for continuous calculation of the aircraft’s position.

The most modern IRS integration is the satellite GPS. The GPS is extremely accurate in itself. When combined with IRS, it creates one of the most accurate navigation systems available. The GPS is used to initialize the IRS so the pilot no longer needs to do so. GPS also feeds data into the IRS computer to be used for error correction. Occasional service interruptions and altitude inaccuracies of the GPS system pose no problem for IRS/GPS. The IRS functions continuously and is completely self-contained within the IRS unit. Should the GPS falter, the IRS portion of the system continues without it. The latest electronic technology has reduced the size and weight of INS/IRS avionics units significantly. Figure 11-156 shows a modern micro-IRS unit that measures approximately six inches on each side.

### Aircraft Communication Addressing & Reporting System (ACARS)

ACARS is a two-way communication link between an airliner in flight and the airline’s main ground facilities. Data is collected in the aircraft by digital sensors and is transmitted to the ground facilities. Replies from the ground may be printed out so the appropriate flight crewmember can have a hard copy of the response.

## 2. 中文翻译

惯性导航系统（INS）用于部分大型飞机的远程导航。它也可能被称为惯性参考系统（IRS），不过 IRS 这一名称通常保留给更为现代的系统。INS/IRS 是一种自足式系统，不需要来自地面导航设施或发射机的无线电输入信号。该系统在已知起始点的基础上，通过测量飞机的加速度来推导姿态、速度与方向信息。飞机的位置则由 INS 加速度计所感受的力经过计算不断更新。系统至少使用两个加速度计，一个以北为基准，另一个以东为基准。在较老的装置中，它们安装在一个陀螺稳定平台上。这样可以避免重力加速度引入误差。

INS 利用 INS 计算机进行复杂运算，把施加的力转换成位置信息。飞机静止在地面时，用接口控制头输入起始位置数据，这一过程称为初始化。此后，飞机的一切运动都由内置加速度计感知，并送入计算机运算。随着飞行时间增加，系统用反馈与校正回路修正累积误差。INS 每一小时飞行时间的偏差量是衡量其性能的基准。飞行一小时后累积误差小于 1 英里是可以做到的。持续、准确地把陀螺稳定平台调整到与地球表面平行，是减小累积误差的关键要求。输出位置时采用纬度/经度坐标系。

INS 被集成到客机的飞行管理系统和自动飞行控制系统中。可以为预定航路输入航路点，INS 会依次把飞机引导到每个航路点。它也可以与其他导航设备集成，以保证持续修正并提高精度，但这并非必需。

现代 INS 系统称为 IRS。它们是完全固态的装置，没有运动部件。三环激光陀螺取代了老式 INS 平台系统中的机械陀螺。这消除了进动以及其他机械陀螺的缺点。使用三个固态加速度计（每个运动平面一个）也提高了精度。加速度计和陀螺的输出送入计算机，用于连续计算飞机的位置。

最现代的 IRS 集成方式是卫星 GPS。GPS 本身极为精确。GPS 与 IRS 组合，就构成了现有最精确的导航系统之一。GPS 用于对 IRS 进行初始化，飞行员因而不再需要手动初始化。GPS 还把数据送入 IRS 计算机用于误差修正。GPS 系统偶尔的业务中断和高度不准确，对 IRS/GPS 都不成问题。IRS 连续工作，且完全自足于 IRS 组件内部。即使 GPS 失效，系统中的 IRS 部分仍可继续工作。最新的电子技术已显著减小 INS/IRS 电子组件的尺寸和重量。图 11-156 所示为一台现代微型 IRS 组件，每边尺寸约 6 英寸。

### 飞机通信寻址与报告系统（ACARS）

ACARS 是飞行中的客机与航空公司地面主设施之间的双向通信链路。数据由数字传感器在飞机上采集，并传送至地面设施。地面的回复可以打印出来，使相应的机组成员得到一份回复的硬拷贝。

## 3. 专业词汇

| 英文 | 词性 | 中文 | 本节语境 |
| --- | --- | --- | --- |
| inertial navigation system (INS) | n. | 惯性导航系统 | 靠自身测量的加速度推算位置、不依赖地面台的大型飞机远程导航系统 |
| inertial reference system (IRS) | n. | 惯性参考系统 | 现代固态化 INS 的称呼，通常指较新、无运动部件的型号 |
| self-contained | adj. | 自足式的 | 描述 INS/IRS 不接收地面发射机信号，全部解算在机内完成 |
| accelerometer | n. | 加速度计 | 感受飞机各方向加速度的敏感元件，至少两个（北向、东向） |
| gyro-stabilized platform | n. | 陀螺稳定平台 | 老式 INS 中承载加速度计、保持水平基准的机械平台 |
| initializing | n. | 初始化 | 飞机静止时输入起始位置数据，使 INS 建立初始基准的过程 |
| precession | n. | 进动 | 机械陀螺受外力矩产生的漂移现象，激光陀螺可将其消除 |
| laser gyro | n. | 激光陀螺 | 三环式固态角速度传感器，取代老式 INS 的机械陀螺 |
| solid-state | adj. | 固态的 | 描述 IRS 无运动部件、全部由电子器件构成 |
| waypoint | n. | 航路点 | 预先输入 INS 的地理坐标点，飞机依次被引导通过 |
| flight management system | n. | 飞行管理系统 | 与 INS 集成、按预定航路自动引导飞机的机载系统 |
| latitude/longitude coordinate system | n. | 纬度/经度坐标系 | INS 输出位置时采用的地理坐标表示方式 |
| feedback and correction loop | n. | 反馈与校正回路 | 随飞行时间累积误差而不断修正解算结果的闭环环节 |
| ACARS | n. | 飞机通信寻址与报告系统 | 客机与航空公司地面设施之间传送数据的双向通信链路 |

## 4. 语法解析

### ① 省略 if 的倒装条件句
**原句**：Should the GPS falter, the IRS portion of the system continues without it.
**拆解**：Should the GPS falter 是省略 if 的虚拟条件状语从句，情态动词 Should 提到主语 the GPS 之前形成倒装；主句 the IRS portion of the system continues without it，主语中心词 portion，of the system 作后置定语，without it 为条件状语。
**要点**：正式技术英语常用 “Should + 主语 + 动词原形” 代替 “If … should …”，表示“万一、倘若”。识别时把 Should 放回 if 之后还原成 If the GPS should falter 就通了；此处 falter 是原形，不是第三人称单数，别误读成疑问句。

### ② 长名词短语作主语 + 不定式作后置定语
**原句**：Continuous accurate adjustment to the gyro-stabilized platform to keep it parallel to the Earth’s surface is a key requirement to reduce accumulated error.
**拆解**：主语中心词 adjustment，前置定语 Continuous accurate，介词短语 to the gyro-stabilized platform 说明调整对象，不定式 to keep it parallel to the Earth’s surface 说明调整目的；谓语 is，表语 a key requirement，不定式 to reduce accumulated error 作后置定语。
**要点**：主语由 15 个词构成，谓语 is 一直拖到 platform 之后才出现。keep it parallel to … 是 “keep + 宾语 + 形容词” 的复合宾语结构，parallel 是宾语补足语，不能换成副词 parallelly。整句译成中文时习惯拆成“把平台持续准确地调整到与地表平行，是……的关键要求”。

### ③ 省略关系词的定语从句嵌在主语里
**原句**：The amount an INS is off in one hour of flight time is a reference point for determining performance.
**拆解**：主语中心词 The amount，其后 an INS is off in one hour of flight time 是省略了关系副词 that（或 by which）的定语从句，修饰 amount；主句谓语 is，表语 a reference point，介词短语 for determining performance 作后置定语。
**要点**：amount 后面直接跟主谓结构，中间没有关系词，容易误把 an INS 当成主句主语。判断依据是：is a reference point 这一套主谓只能属于 The amount。be off 在此表示“偏差、偏离”，不是“关闭”。

### ④ 被动语态 + while 引导的时间状语从句
**原句**：An interface control head is used to enter starting location position data while the aircraft is stationary on the ground.
**拆解**：主句为被动语态 An interface control head is used，不定式 to enter starting location position data 作目的状语（说明该控制头的用途）；while 引导时间状语从句，主语 the aircraft，系动词 is，表语 stationary，介词短语 on the ground 作地点状语。
**要点**：be used to do 中的 to 是不定式符号，与 be used to doing（习惯于）结构形似而意义完全不同。while 在此强调“在……期间”，从句用一般现在时表状态，不用进行时，因为 stationary 本身就是持续状态。

### ⑤ 过去分词短语作条件状语
**原句**：The system derives attitude, velocity, and direction information from measurement of the aircraft’s accelerations given a known starting point.
**拆解**：主语 The system，谓语 derives，宾语 attitude, velocity, and direction information，介词短语 from measurement of the aircraft’s accelerations 作来源状语；given a known starting point 是过去分词短语作条件状语，相当于 if a known starting point is given。
**要点**：given 在此不是谓语动词的过去式，而是“在……已知/给定的条件下”的分词用法，逻辑主语是整句所述的计算过程。它与介词 given（“考虑到”）同形，需按其后是否带名词短语来判断；本句中 given 后接名词短语，属分词。

### ⑥ 现在完成时 + 程度状语后置
**原句**：The latest electronic technology has reduced the size and weight of INS/IRS avionics units significantly.
**拆解**：主语 The latest electronic technology，谓语 has reduced（现在完成时，强调至今的结果），宾语 the size and weight of INS/IRS avionics units，副词 significantly 作程度状语后置。
**要点**：宾语由 and 连接的两个并列名词共用 of 短语，of 只出现一次，还原为 the size of … and the weight of …。significantly 放在句末是为了避免打断 has reduced 与长宾语，中文习惯把它提到动词前译作“显著减小了”。
