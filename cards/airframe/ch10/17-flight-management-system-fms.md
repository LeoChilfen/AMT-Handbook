# Flight Management System (FMS)

> 机体 Ch 10 · Flight Management System (FMS) · 原文 PDF 第 591 页

## 1. 原文

The highest level of automated flight system is the flight FMS. Companies flying aircraft for hire have special results they wish to achieve. On-time performance, fuel conservation, and long engine and component life all contribute to profitability. An FMS helps achieve these results by operating the aircraft with greater precision than possible by a human pilot alone.

A FMS can be thought of as a master computer system that has control over all other systems, computerized and otherwise. As such, it coordinates the adjustment of flight, engine, and airframe parameters either automatically or by instructing the pilot how to do so. Literally, all aspects of the flight are considered, from preflight planning to pulling up to the jet-way upon landing, including in-flight amendments to planned courses of action.

The main component of an FMS is the flight management computer (FMC). It communicates with the EICAS or ECAM, the ADC, the thrust management computer that controls the autothrottle functions, the EIFIS symbol generators, the automatic flight control system, the inertial reference system, collision avoidance systems, and all of the radio navigational aids via data busses.

The interface to the system is a control display unit (CDU) that is normally located forward on the center pedestal in the flight deck. It contains a full alphanumeric keypad, a CRT or LCD display/work screen, status and condition annunciators, and specialized function keys.

The typical FMS uses two FMS FMCs that operate independently as the pilot’s unit and the copilot’s unit. However, they do crosstalk through the data busses. In normal operation, the pilot and copilot divide the workload, with the pilot’s CDU set to supervise and interface with operational parameters and the copilot’s CDU handling navigational chores. This is optional at the flightcrew’s discretion. If a main component fails (e.g., an FMC or a CDU), the remaining operational units continue to operate with full control and without system compromise.

Each flight of an aircraft has vertical, horizontal, and navigational components, which are maintained by manipulating the engine and airframe controls. While doing so, numerous options are available to the pilot. Rate of climb, thrust settings, EPR levels, airspeed, descent rates, and other terms can be varied. Commercial air carriers use the FMC to establish guidelines by which flights can be flown. Usually, these promote the company’s goals for fuel and equipment conservation. The pilot need only enter variables as requested and respond to suggested alternatives as the FMC presents them.

The FMC has stored in its database literally hundreds of flight plans with predetermined operational parameters that can be selected and implemented. Integration with NA V-COM aids allows the FMS to change radio frequencies as the flight plan is enacted. Internal computations using direct input from fuel flow and fuel quantity systems allow the FMC to carry out lean operations or pursue other objectives, such as high performance operations if making up time is paramount on a particular flight. Weather and traffic considerations are also integrated. The FMS can handle all variables automatically but communicates via the CDU screen to present its planned action, gain consensus, or ask for an input or decision.

As with the monitoring systems, FMS includes BITE. The FMC continuously monitors its entire systems and inputs for faults during operation. Maintenance personal can retrieve system generated and pilot recorded fault messages. They may also access maintenance pages that call out line replaceable units (LRUs) to which faults have been traced by the BITE system. Follow manufacturers’ procedures for interfacing with maintenance data information.

## 2. 中文翻译

自动化飞行系统的最高层级就是飞行管理系统（FMS）。以出租方式运营飞机的公司，有其希望达成的特定目标。准点率、燃油节约，以及发动机和部件的长寿命，都有助于提高盈利能力。FMS 以远超人类飞行员单独操作所能达到的精度来操纵飞机，从而帮助实现这些目标。

FMS 可以看作一套主控计算机系统，对包括计算机化和非计算机化的所有其他系统实施控制。因此，它以自动方式，或通过指示飞行员如何操作，来协调飞行、发动机和机体参数的调整。可以说，飞行的方方面面都被纳入考虑，从飞行前计划，到落地时滑靠登机廊桥，还包括飞行中对既定行动方案的修改。

FMS 的主要部件是飞行管理计算机（FMC）。它通过数据总线与 EICAS 或 ECAM、ADC、控制自动油门功能的推力管理计算机、EIFIS 符号发生器、自动飞行控制系统、惯性基准系统、防撞系统以及所有无线电导航设备进行通信。

该系统的接口是控制显示组件（CDU），通常位于驾驶舱中央操纵台的前部。它包含完整的字母数字键盘、CRT 或 LCD 显示屏/工作屏、状态与状况信号牌，以及专用功能键。

典型的 FMS 装有两台 FMC，分别作为机长单元和副驾驶单元独立工作。不过，它们确实通过数据总线相互对话。正常运行时，机长与副驾驶分担工作量：机长的 CDU 设置为监控运行参数并与之交互，副驾驶的 CDU 则处理导航事务。这种分工由机组自行决定，属可选项。若某个主要部件失效（例如一台 FMC 或一个 CDU），其余可用单元仍能继续工作，保持完全控制，系统不受影响。

飞机的每一次飞行都包含垂直、水平和导航三个方面的内容，这些内容通过操纵发动机和机体操纵装置来维持。在此过程中，飞行员有多种选择。爬升率、推力设定、EPR 值、空速、下降率及其他参数都可以改变。商业航空公司利用 FMC 制定飞行所依据的准则，这些准则通常服务于公司在燃油与设备节约方面的目标。飞行员只需按要求输入变量，并对 FMC 提出的备选方案作出回应。

FMC 的数据库中存储着数以百计的飞行计划，每份都带有预定的运行参数，可供选择和执行。与 NAV-COM 导航/通信设备的整合，使 FMS 能在飞行计划实施过程中切换无线电频率。利用燃油流量与燃油量系统的直接输入进行内部计算，FMC 可以执行经济（贫油）运行，或追求其他目标——例如在某一航班上赶时间成为首要考虑时，执行高性能运行。天气与交通因素也被纳入其中。FMS 能自动处理所有变量，但会通过 CDU 屏幕进行沟通，以呈报其计划动作、取得一致意见，或请求输入或决策。

与监控系统一样，FMS 也包含机内测试设备（BITE）。FMC 在运行中持续监视其整个系统与各项输入，以发现故障。维修人员可以调取系统生成的以及飞行员记录的故障信息。他们还可以进入维护页面，页面会列出 BITE 系统追踪到故障所对应的航线可更换组件（LRU）。与维护数据信息交互时，须遵循制造商的程序。

## 3. 专业词汇

| 英文 | 词性 | 中文 | 本节语境 |
| --- | --- | --- | --- |
| flight management computer (FMC) | n. | 飞行管理计算机 | FMS 的核心计算部件，存储飞行计划并计算飞行剖面 |
| control display unit (CDU) | n. | 控制显示组件 | 驾驶舱中央操纵台上的 FMS 人机接口，含键盘与显示屏 |
| data bus | n. | 数据总线 | FMC 与 EICAS、ADC、惯导等各系统交换数据的通道 |
| autothrottle | n. | 自动油门 | 由推力管理计算机控制、自动调节推力的功能 |
| thrust management computer | n. | 推力管理计算机 | 接受 FMC 指令并控制自动油门动作的计算机 |
| inertial reference system | n. | 惯性基准系统 | 为 FMS 提供姿态、航向与位置信息的自主导航系统 |
| symbol generator | n. | 符号发生器 | EFIS 中把显示数据转换成电子显示符号的部件 |
| EICAS | n. | 发动机指示与机组警告系统 | 波音机型上集中显示发动机参数与警告的系统 |
| ECAM | n. | 电子中央飞机监控系统 | 空客机型上对应的集中显示与警告系统 |
| built-in test equipment (BITE) | n. | 机内测试设备 | FMC 内持续监视系统与输入、隔离故障的自检装置 |
| line replaceable unit (LRU) | n. | 航线可更换组件 | 可在停机线整体拆换的单元，BITE 将故障定位到它 |
| engine pressure ratio (EPR) | n. | 发动机压比 | 飞行员可设定的一种推力参数，受 FMC 准则约束 |
| center pedestal | n. | 中央操纵台 | 驾驶舱两座椅之间的台体，CDU 通常装在其前部 |
| flight plan | n. | 飞行计划 | FMC 数据库中预存、可供选择执行的航路与参数方案 |

## 4. 语法解析

### ① 比较结构 + by 动名词方式状语
**原句**：An FMS helps achieve these results by operating the aircraft with greater precision than possible by a human pilot alone.
**拆解**：主语 An FMS；谓语 helps，宾语 achieve these results（help 后接省略 to 的不定式）；by operating the aircraft 为方式状语，operating 的宾语是 the aircraft；with greater precision 为程度状语；than possible by a human pilot alone 为比较状语，省略了 it is。
**要点**：help 后接不带 to 的不定式，不要补 to。than 后面是省略结构，完整为 than (it is) possible (to operate) by a human pilot alone；不要把 than possible 误当成修饰 precision 的定语。

### ② either ... or 并列状语 + how to do 宾语
**原句**：As such, it coordinates the adjustment of flight, engine, and airframe parameters either automatically or by instructing the pilot how to do so.
**拆解**：As such 为连接性状语；主语 it，谓语 coordinates，宾语 the adjustment of flight, engine, and airframe parameters；either automatically or by instructing... 为并列的方式状语；instructing 后接宾语 the pilot 和宾语从句 how to do so。
**要点**：either ... or 连接的是两个方式状语（副词 automatically 与介词短语 by...），不是两个宾语。how to do so 是“疑问词 + 不定式”作宾语，so 指代前面所说的参数调整。

### ③ 长宾语并列 + 定语从句 + via 方式状语
**原句**：It communicates with the EICAS or ECAM, the ADC, the thrust management computer that controls the autothrottle functions, the EIFIS symbol generators, the automatic flight control system, the inertial reference system, collision avoidance systems, and all of the radio navigational aids via data busses.
**拆解**：主语 It，谓语 communicates with，后面是多个并列宾语；其中 the thrust management computer 带 that 引导的定语从句；句末 via data busses 为方式状语，修饰整个 communicate with。
**要点**：communicate with 的宾语被拉得很长，读到 via data busses 时要回到谓语，理解成“通过数据总线与……通信”。that 从句只修饰紧邻的 computer，不修饰前面所有并列项。

### ④ with 复合结构（两个独立主格并列）
**原句**：In normal operation, the pilot and copilot divide the workload, with the pilot’s CDU set to supervise and interface with operational parameters and the copilot’s CDU handling navigational chores.
**拆解**：主句 the pilot and copilot divide the workload；逗号后 with 引出复合结构，内含两套“名词 + 分词”：the pilot’s CDU set（过去分词，表状态）与 the copilot’s CDU handling（现在分词，表主动），中间用 and 并列。
**要点**：同一个 with 结构里可以并列两个独立主格，判断依据是“名词 + 分词”成对出现。set 是过去分词而非谓语，否则会与前面的 divide 冲突。

### ⑤ 宾语后置 + that 定语从句
**原句**：The FMC has stored in its database literally hundreds of flight plans with predetermined operational parameters that can be selected and implemented.
**拆解**：主语 The FMC，谓语 has stored，宾语 literally hundreds of flight plans 因过长而后置到 in its database 之后；with predetermined operational parameters 为介词短语修饰 flight plans；that can be selected and implemented 为定语从句。
**要点**：正常语序是 has stored hundreds of flight plans in its database，作者把地点状语提前以平衡句子。that 从句用被动语态，说明这些计划“可被选取和执行”。

### ⑥ 分词短语作定语 + allow sb. to do + if 条件从句
**原句**：Internal computations using direct input from fuel flow and fuel quantity systems allow the FMC to carry out lean operations or pursue other objectives, such as high performance operations if making up time is paramount on a particular flight.
**拆解**：主语中心词 Internal computations，using direct input... 为现在分词短语作后置定语；谓语 allow，宾语 the FMC，宾补 to carry out ... or pursue ...（两个不定式并列）；such as 举例；if 引导条件状语从句，从句主语是动名词短语 making up time。
**要点**：allow sb. to do sth. 的宾补必须带 to；or 连接 carry out 与 pursue 两个动词原形，共用一个 to。if 从句的主语是动名词短语，谓语 is paramount，不要误把 time 当主语。
