# Autopilot Components

> 机体 Ch 10 · Autopilot Components · 原文 PDF 第 579 页

## 1. 原文

Most autopilot systems consist of four basic elements, plus various switches and auxiliary units. The four basic elements are: sensing elements, computing element, output elements, and command elements. Many advanced autopilot systems contain a fifth element: feedback or follow-up. This refers to signals sent as corrections are being made by the output elements to advise the autopilot of the progress being made.

### Sensing Elements

The attitude (or vertical) and directional gyros, the turn coordinator, and an altitude control are the autopilot sensing elements. These units sense the movements of the aircraft. They generate electric signals that are used by the autopilot to automatically take the required corrective action needed to keep the aircraft flying as intended. The sensing gyros can be located in the flight deck mounted instruments. They can also be remotely mounted. Remote gyro sensors drive the servo displays in the flight deck panel, as well as provide the input signals to the autopilot computer.

Modern digital autopilots may use a variety of different sensors. MEMS gyros may be used or accompanied by the use solid state accelerometers and magnetometers. Rate based systems may not use gyros at all. Various input sensors may be located within the same unit or in separate units that transfer information via digital data bus. Navigation information is also integrated via digital data bus connection to avionics computers.

### Computer & Amplifier

The computing element of an autopilot may be analog or digital. Its function is to interpret the sensing element data, integrate commands and navigational input, and send signals to the output elements to move the flight controls as required to control the aircraft. An amplifier is used to strengthen the signal for processing, if needed, and for use by the output devices, such as servo motors. The amplifier and associated circuitry is the computer of an analog autopilot system. Information is handled in channels corresponding to the axis of control for which the signals are intended (i.e., pitch channel, roll channel, or yaw channel). Digital systems use solid state microprocessor computer technology and typically only amplify signals sent to the output elements.

### Output Elements

The output elements (components) of an autopilot system are the servos that cause actuation of the flight control surfaces. They are independent devices for each of the control channels that integrate into the regular flight control system. Autopilot servo designs vary widely depending on the method of actuation of the flight controls. Cable-actuated systems typically utilize electric servo motors or electro-pneumatic servos. Hydraulic actuated flight control systems use electro-hydraulic autopilot servos. Digital fly-by-wire aircraft utilize the same actuators for carrying out manual and autopilot maneuvers. When the autopilot is engaged, the actuators respond to commands from the autopilot rather than exclusively from the pilot. Regardless, autopilot servos must allow unimpeded control surface movement when the autopilot is not operating.

Aircraft with cable actuated control surfaces use two basic types of electric motor-operated servos. In one, a motor is connected to the servo output shaft through reduction gears. The motor starts, stops, and reverses direction in response to the commands of autopilot computer. The other type of electric servo uses a constantly running motor geared to the output shaft through two magnetic clutches. The clutches are arranged so that energizing one clutch transmits motor torque to turn the output shaft in one direction; energizing the other clutch turns the shaft in the opposite direction. Electro-pneumatic servos can also be used to drive cable flight controls in some autopilot systems. They are controlled by electrical signals from the autopilot amplifier and actuated by an appropriate air pressure source. The source may be a vacuum system pump or turbine engine bleed air. Each servo consists of an electromagnetic valve assembly and an output linkage assembly.

Aircraft with hydraulically actuated flight control systems have autopilot servos that are electro-hydraulic. They are control valves that direct fluid pressure as needed to move the control surfaces via the control surface actuators. They are powered by signals from the autopilot computer. When the autopilot is not engaged, the servos allow hydraulic fluid to flow unrestricted in the flight control system for normal operation. The servo valves can incorporate feedback transducers to update the autopilot of progress during error correction.

### Command Elements

The command unit, called a flight controller, is the human interface of the autopilot. It allows the pilot to tell the autopilot what to do. Flight controllers vary with the complexity of the autopilot system. By pressing the desired function buttons, the pilot causes the controller to send instruction signals to the autopilot computer, enabling it to activate the proper servos to carry out the command(s). Level flight, climbs, descents, turning to a heading, or flying a desired heading are some of the choices available on most autopilots. Many aircraft make use of a multitude of radio navigational aids. These can be selected to issue commands directly to the autopilot computer.

In addition to an on/off switch on the autopilot controller, most autopilots have a disconnect switch located on the control wheel(s). This switch, operated by thumb pressure, can be used to disengage the autopilot system should a malfunction occur in the system or any time the pilot wishes to take manual control of the aircraft.

### Feedback or Follow-up Element

As an autopilot maneuvers the flight controls to attain a desired flight attitude, it must reduce control surface correction as the desired attitude is nearly attained so the controls and aircraft come to rest on course. Without doing so, the system would continuously overcorrect. Surface deflection would occur until the desired attitude is attained. But movement would still occur as the surface(s) returned to pre-error position. The attitude sensor would once again detect an error and begin the correction process all over again. Various electric feedback, or follow-up signals, are generated to progressively reduce the error message in the autopilot so that continuous over correction does not take place. This is typically done with transducers on the surface actuators or in the autopilot servo units. Feedback completes a loop as illustrated in Figure 10-111 . This is called a closed-loop system.

A rate system receives error signals from a rate gyro that are of a certain polarity and magnitude that cause the control surfaces to be moved. As the control surfaces counteract the error and move to correct it, follow-up signals of opposite polarity and increasing magnitude counter the error signal until the aircraft’s correct attitude is restored. A displacement follow-up system uses control surface pickups to cancel the error message when the surface has been moved to the correct position.

### Autopilot Functions

The following autopilot system description is presented to show the function of a simple analog autopilot. Most autopilots are far more sophisticated; however, many of the operating fundamentals are similar.

The automatic pilot system flies the aircraft by using electrical signals developed in gyro-sensing units. These units are connected to flight instruments that indicate direction, rate of turn, bank, or pitch. If the flight attitude or magnetic heading is changed, electrical signals are developed in the gyros. These signals are sent to the autopilot computer/ amplifier and are used to control the operation of servo units.

A servo for each of the three control channels converts electrical signals into mechanical force, which moves the control surface in response to corrective signals or pilot commands. The rudder channel receives two signals that determine when and how much the rudder moves. The first signal is a course signal derived from a compass system. As long as the aircraft remains on the magnetic heading it was on when the autopilot was engaged, no signal develops. But, any deviation causes the compass system to send a signal to the rudder channel that is proportional to the angular displacement of the aircraft from the preset heading.

The second signal received by the rudder channel is the rate signal that provides information anytime the aircraft is turning about the vertical axis. This information is provided by the turn-and-bank indicator gyro. When the aircraft attempts to turn off course, the rate gyro develops a signal proportional to the rate of turn, and the course gyro develops a signal proportional to the amount of displacement. The two signals are sent to the rudder channel of the amplifier, where they are combined, and their strength is increased. The amplified signal is then sent to the rudder servo. The servo turns the rudder in the proper direction to return the aircraft to the selected magnetic heading.

As the rudder surface moves, a follow-up signal is developed that opposes the input signal. When the two signals are equal in magnitude, the servo stops moving. As the aircraft arrives on course, the course signal reaches a zero value, and the rudder is returned to the streamline position by the follow-up signal.

The aileron channel receives its input signal from a transmitter located in the gyro horizon indicator. Any movement of the aircraft about its longitudinal axis causes the gyro-sensing unit to develop a signal to correct for the movement. This signal is amplified, phase detected, and sent to the aileron servo, which moves the aileron control surfaces to correct for the error. As the aileron surfaces move, a follow-up signal builds up in opposition to the input signal. When the two signals are equal in magnitude, the servo stops moving. Since the ailerons are displaced from the streamline, the aircraft now starts moving back toward level flight with the input signal becoming smaller and the follow-up signal driving the control surfaces back toward the streamline position. When the aircraft has returned to level flight roll attitude, the input signal is again zero. At the same time, the control surfaces are streamlined, and the follow-up signal is zero.

The elevator channel circuits are similar to those of the aileron channel, with the exception that the elevator channel detects and corrects changes in pitch attitude of the aircraft. For altitude control, a remotely mounted unit containing an altitude pressure diaphragm is used. Similar to the attitude and directional gyros, the altitude unit generates error signals when the aircraft has moved from a preselected altitude. This is known as an altitude hold function. The signals control the pitch servos, which move to correct the error. An altitude select function causes the signals to continuously be sent to the pitch servos until a preselected altitude has been reached. The aircraft then maintains the preselected altitude using altitude hold signals.

### Yaw Dampening

Many aircraft have a tendency to oscillate around their vertical axis while flying a fixed heading. Near continuous rudder input is needed to counteract this effect. A yaw damper is used to correct this motion. It can be part of an autopilot system or a completely independent unit. A yaw damper receives error signals from the turn coordinator rate gyro. Oscillating yaw motion is counteracted by rudder movement, which is made automatically by the rudder servo(s) in response to the polarity and magnitude of the error signal.

## 2. 中文翻译

大多数自动驾驶仪系统由四个基本环节加上各种开关和辅助组件构成。这四个基本环节是：传感元件、计算元件、输出元件和指令元件。许多先进的自动驾驶仪系统还含有第五个环节：反馈或随动。它指的是在输出元件进行修正的过程中所发出的信号，用来把修正的进展告知自动驾驶仪。

### 传感元件

姿态（或垂直）陀螺和方向陀螺、转弯协调器以及高度控制装置，就是自动驾驶仪的传感元件。这些组件感受飞机的运动。它们产生电信号，自动驾驶仪利用这些信号自动采取所需的修正动作，使飞机按预期状态飞行。传感陀螺可以装在驾驶舱仪表内部，也可以远距安装。远距陀螺传感器驱动驾驶舱面板上的伺服显示器，同时向自动驾驶仪计算机提供输入信号。

现代数字式自动驾驶仪可能使用多种不同的传感器。可以使用 MEMS 陀螺，或将其与固态加速度计和磁强计配合使用。速率式系统可能完全不用陀螺。各种输入传感器可以装在同一组件内，也可装在分开的组件中，通过数字数据总线传递信息。导航信息也通过与航空电子计算机的数字数据总线连接而实现集成。

### 计算机与放大器

自动驾驶仪的计算元件可以是模拟式或数字式的。其功能是解读传感元件数据，综合指令与导航输入，并向输出元件发送信号，按要求移动飞行操纵面以控制飞机。放大器用于在需要时增强信号以便处理，并供伺服电动机等输出装置使用。在模拟式自动驾驶仪系统中，放大器及相关电路就是计算机。信息按信号所针对的操纵轴分通道处理（即俯仰通道、横滚通道或偏航通道）。数字式系统采用固态微处理器计算机技术，通常只放大送往输出元件的信号。

### 输出元件

自动驾驶仪系统的输出元件（组件）是驱动飞行操纵面动作的舵机。它们按各操纵通道分别设置，是独立装置，并接入常规飞行操纵系统。自动驾驶仪舵机的设计因飞行操纵的驱动方式不同而差异很大。钢索驱动系统通常采用电动舵机或电动气动舵机。液压驱动的飞行操纵系统采用电动液压自动驾驶仪舵机。数字式电传飞机在人工操纵和自动驾驶仪操纵时使用同一套作动器。自动驾驶仪接通时，作动器响应来自自动驾驶仪的指令，而不再只响应飞行员的输入。无论如何，自动驾驶仪未工作时，其舵机必须允许操纵面不受阻碍地运动。

操纵面为钢索驱动的飞机，使用两种基本类型的电动机式舵机。一种是电动机通过减速齿轮与舵机输出轴相连，电动机按自动驾驶仪计算机的指令启动、停止和换向。另一种电动舵机使用持续运转的电动机，通过两个磁离合器与输出轴啮合。离合器的布置使激励其中一个时把电动机扭矩传给输出轴，使其朝一个方向转动；激励另一个时则使轴朝相反方向转动。某些自动驾驶仪系统也可用电动气动舵机驱动钢索式飞行操纵。它们由自动驾驶仪放大器的电信号控制，由适当的气压源驱动。气源可以是真空系统泵或涡轮发动机引气。每个舵机由一个电磁活门组件和一个输出连杆组件组成。

液压驱动飞行操纵系统的飞机，其自动驾驶仪舵机为电动液压式。它们是控制活门，按需引导液压压力，通过操纵面作动器使操纵面运动。它们由自动驾驶仪计算机的信号驱动。自动驾驶仪未接通时，舵机允许液压油在飞行操纵系统中不受限制地流动，以保证正常操作。伺服活门内可装入反馈传感器，在误差修正过程中向自动驾驶仪更新进展。

### 指令元件

指令组件称为飞行控制器，是自动驾驶仪的人机接口。它让飞行员告诉自动驾驶仪该做什么。飞行控制器随自动驾驶仪系统的复杂程度而异。飞行员按下所需的功能按钮，控制器便向自动驾驶仪计算机发出指令信号，使其启动相应的舵机来执行指令。平飞、爬升、下降、转向某航向或飞向期望航向，是多数自动驾驶仪提供的部分选择。许多飞机使用多种无线电导航设备，这些设备可被选来直接向自动驾驶仪计算机发出指令。

除自动驾驶仪控制器上的通/断开关外，多数自动驾驶仪在驾驶盘上还设有断开开关。该开关由拇指按压操作，可在系统发生故障时、或飞行员任何时候想改为人工操纵飞机时，用来断开自动驾驶仪系统。

### 反馈或随动环节

自动驾驶仪操纵飞行操纵面以达到期望飞行姿态时，必须在接近达到该姿态时减小操纵面修正量，使操纵面和飞机稳定在航向上。否则，系统会持续过修正：操纵面偏转直到达到期望姿态，但当操纵面回到误差前位置时运动仍会发生；姿态传感器会再次检测到误差，又重新开始修正过程。系统产生各种电反馈（随动）信号，逐步减小自动驾驶仪中的误差信号，使持续的过修正不会发生。这通常由装在操纵面作动器上或自动驾驶仪舵机组件内的传感器完成。反馈构成一个回路，如图 10-111 所示。这称为闭环系统。

速率式系统从速率陀螺接收具有一定极性和大小的误差信号，使操纵面产生动作。当操纵面抵消误差并朝修正方向运动时，极性相反、大小递增的随动信号会抵消误差信号，直到飞机恢复正确姿态。位移随动系统则利用操纵面位置传感器，在操纵面移动到正确位置时消除误差信号。

### 自动驾驶仪功能

下面介绍自动驾驶仪系统，是为了说明一台简单模拟式自动驾驶仪的功能。多数自动驾驶仪要复杂得多，但许多基本工作原理是相似的。

自动驾驶仪系统利用陀螺传感组件产生的电信号来驾驶飞机。这些组件与指示方向、转弯速率、坡度或俯仰的飞行仪表相连。若飞行姿态或磁航向发生变化，陀螺中便产生电信号。这些信号送往自动驾驶仪计算机/放大器，用来控制舵机组的工作。

三个操纵通道各有一个舵机，把电信号转换为机械力，驱动操纵面响应修正信号或飞行员指令。方向舵通道接收两个信号，决定方向舵何时动作、动作多少。第一个信号是由罗盘系统引出的航向信号。只要飞机保持在自动驾驶仪接通时所处的磁航向上，就不产生信号。但一旦出现任何偏差，罗盘系统便向方向舵通道发出信号，其大小与飞机偏离预选航向的角度成正比。

方向舵通道接收的第二个信号是速率信号，只要飞机绕垂直轴转弯，它就提供信息。该信息由转弯倾斜仪陀螺提供。当飞机试图偏离航线转弯时，速率陀螺产生与转弯速率成正比的信号，航向陀螺产生与偏离量成正比的信号。这两个信号送往放大器的方向舵通道，在那里合并并增强。放大后的信号再送往方向舵舵机。舵机朝正确方向偏转方向舵，使飞机回到所选磁航向。

方向舵面移动时会产生随动信号，与输入信号相对抗。当两个信号大小相等时，舵机停止动作。当飞机回到航向上时，航向信号降为零值，方向舵随动信号使其回到顺流（中立）位置。

副翼通道从装在陀螺地平仪内的发送器接收输入信号。飞机绕纵轴的任何运动都会使陀螺传感组件产生信号以修正该运动。该信号经放大、鉴相后送往副翼舵机，由舵机带动副翼操纵面修正误差。副翼面移动时，随动信号逐步建立，与输入信号相对抗。当两个信号大小相等时，舵机停止动作。由于副翼已偏离顺流位置，飞机此时开始向平飞状态回返，输入信号逐渐减小，随动信号则驱动操纵面回到顺流位置。当飞机回到平飞横滚姿态时，输入信号再次为零；同时操纵面处于顺流位置，随动信号也为零。

升降舵通道的电路与副翼通道相似，不同之处在于升降舵通道检测并修正飞机俯仰姿态的变化。高度控制使用一个远距安装、内含高度压力膜盒的组件。与姿态陀螺和方向陀螺类似，高度组件在飞机偏离预选高度时产生误差信号。这称为高度保持功能。信号控制俯仰舵机动作以修正误差。高度选择功能则使信号持续送往俯仰舵机，直到达到预选高度；此后飞机利用高度保持信号维持该预选高度。

### 偏航阻尼

许多飞机在按固定航向飞行时，有绕垂直轴摆动的趋势，需要几乎连续地输入方向舵来抵消这种效应。偏航阻尼器用于修正这种运动。它可以是自动驾驶仪系统的一部分，也可以是完全独立的组件。偏航阻尼器从转弯协调器的速率陀螺接收误差信号。摆动的偏航运动由方向舵动作抵消，该动作由方向舵舵机根据误差信号的极性和大小自动完成。

## 3. 专业词汇

| 英文 | 词性 | 中文 | 本节语境 |
| --- | --- | --- | --- |
| sensing element | n. | 传感元件 | 感受飞机姿态与航向变化、并产生电信号的陀螺等组件 |
| turn coordinator | n. | 转弯协调器 | 提供转弯速率与侧滑信息、内含速率陀螺的仪表 |
| directional gyro | n. | 方向陀螺 | 提供航向基准的陀螺，属于自动驾驶仪的传感元件之一 |
| follow-up signal | n. | 随动信号 | 操纵面动作后反馈回来、与输入信号相抗以停止舵机的信号 |
| closed-loop system | n. | 闭环系统 | 反馈把输出送回输入端、构成回路的控制系统 |
| servo | n. | 舵机 | 把电信号转换为机械力、驱动操纵面动作的输出元件 |
| actuator | n. | 作动器 | 电传飞机上执行人工与自动驾驶仪指令的驱动装置 |
| reduction gear | n. | 减速齿轮 | 电动机与舵机输出轴之间降低转速、增大扭矩的齿轮组 |
| magnetic clutch | n. | 磁离合器 | 常转电动机与输出轴之间的电磁啮合装置，决定转向 |
| electro-pneumatic servo | n. | 电动气动舵机 | 由电信号控制、以真空泵或发动机引气为动力的钢索式舵机 |
| electro-hydraulic servo | n. | 电动液压舵机 | 液压操纵系统上按计算机信号引导压力的伺服活门 |
| fly-by-wire | n. | 电传操纵 | 以电信号取代机械连杆、共用同一套作动器的操纵方式 |
| yaw damper | n. | 偏航阻尼器 | 抑制飞机绕垂直轴摆动的装置，可独立或并入自动驾驶仪 |
| altitude hold | n. | 高度保持 | 偏离预选高度时产生误差信号、由俯仰舵机修正的功能 |

## 4. 语法解析

### ① 过去分词后置定语 + as 时间状语从句 + 不定式表目的
**原句**：This refers to signals sent as corrections are being made by the output elements to advise the autopilot of the progress being made.
**拆解**：主语 This，谓语 refers to，宾语 signals；sent as corrections are being made by the output elements 为过去分词短语作后置定语，其中 as 引导时间状语从句、用现在进行时的被动语态；to advise the autopilot of the progress being made 为不定式短语作目的状语，being made 为现在分词被动式修饰 progress。
**要点**：sent 的逻辑主语是 signals（信号被发出），故用过去分词。as 从句里的 are being made 强调“修正正在进行”。advise sb. of sth. 意为“把某事告知某人”，不是“建议”。

### ② 定语从句中的被动 + 过去分词作后置定语
**原句**：They generate electric signals that are used by the autopilot to automatically take the required corrective action needed to keep the aircraft flying as intended.
**拆解**：主句主语 They，谓语 generate，宾语 electric signals；that are used by the autopilot 为定语从句（被动语态），to automatically take the required corrective action 为不定式作目的状语；needed to keep the aircraft flying as intended 为过去分词短语作后置定语修饰 action，其中 keep sb./sth. doing 为复合宾语。
**要点**：needed 修饰的是 action 而非 autopilot，找逻辑主语要看紧邻的名词。keep the aircraft flying 中 flying 是宾语补足语，as intended 意为“按预期”。

### ③ so that 结果从句 + 动名词作主语 + 分号并列
**原句**：The clutches are arranged so that energizing one clutch transmits motor torque to turn the output shaft in one direction; energizing the other clutch turns the shaft in the opposite direction.
**拆解**：主句 The clutches are arranged 为被动；so that 引导结果状语从句，从句主语是动名词短语 energizing one clutch，谓语 transmits，宾语 motor torque，to turn... 为目的状语；分号后为并列从句，主语同样是动名词短语 energizing the other clutch。
**要点**：so that 在此表结果（“从而”），与表目的的用法要靠上下文区分。两个从句都用动名词短语作主语，谓语用第三人称单数 transmits/turns。分号连接两个结构对称的分句，比 and 更能突出对照。

### ④ 三个从句连环：as 时间 + as 时间 + so 结果
**原句**：As an autopilot maneuvers the flight controls to attain a desired flight attitude, it must reduce control surface correction as the desired attitude is nearly attained so the controls and aircraft come to rest on course.
**拆解**：句首 As 引导时间状语从句，主语 an autopilot，谓语 maneuvers；主句主语 it，谓语 must reduce，宾语 control surface correction；第二个 as 再引导时间状语从句（随着姿态接近达到）；so 引导结果状语从句，主语 the controls and aircraft，谓语 come to rest。
**要点**：同一个 as 在句中两次出现，功能都是“随着/当……时”，不要与表原因的 as 混淆。so 在此是连词而非 so that，直接跟句子表结果。come to rest 意为“静止下来、稳定”。

### ⑤ since 原因状语从句 + with 复合结构（两个独立主格并列）
**原句**：Since the ailerons are displaced from the streamline, the aircraft now starts moving back toward level flight with the input signal becoming smaller and the follow-up signal driving the control surfaces back toward the streamline position.
**拆解**：Since 引导原因状语从句；主句主语 the aircraft，谓语 starts moving；with 复合结构作伴随状语，内部有两个并列的“名词 + 现在分词”：the input signal becoming smaller 与 the follow-up signal driving the control surfaces...
**要点**：with 后面挂了两个独立主格，第二个省略了 with，靠 and 与第一个并列，不要误读成 driving 与 becoming 并列。streamline position 指操纵面与气流平行的中立位置。

### ⑥ cause sth. to be done + until 时间状语从句
**原句**：An altitude select function causes the signals to continuously be sent to the pitch servos until a preselected altitude has been reached.
**拆解**：主语 An altitude select function，谓语 causes，宾语 the signals，宾补 to continuously be sent（不定式的被动式，split infinitive：副词插在 to 与 be 之间）；until 引导时间状语从句，用现在完成时的被动语态。
**要点**：causes 的宾补用带 to 的不定式，且信号是“被发送”，故用被动式 to be sent。until 从句用现在完成时，强调“到达预选高度”这一动作完成之前信号持续发送。
