# Electrical System Components

> 机体 Ch 09 · Electrical System Components · 原文 PDF 第 511 页

## 1. 原文

### Switches

Switches are devices that open and close circuits. They consist of one or more pair of contacts. The current in the circuit flows when the contacts are closed. Switches with momentary contacts actuate the circuit temporarily, and they return to the normal position with an internal spring when the switch is released. Switches with continuous contacts remain in position when activated. Hazardous errors in switch operation can be avoided by logical and consistent installation. Two-position on/off switches should be mounted so that the on position is reached by an upward or forward movement of the toggle. When the switch controls movable aircraft elements, such as landing gear or flaps, the toggle should move in the same direction as the desired motion. Inadvertent operation of a switch can be prevented by mounting a suitable guard over the switch. A specifically designed switch should be used in all circuits where a switch malfunction would be hazardous. Such switches are of rugged construction and have sufficient contact capacity to break, make, and carry continuously the connected load current. Snap action design is generally preferred to obtain rapid opening and closing of contacts regardless of the speed of the operating toggle or plunger, thereby minimizing contact arcing. The nominal current rating of the conventional aircraft switch is usually stamped on the switch housing. This rating represents the continuous current rating with the contacts closed. Switches should be derated from their nominal current rating for the following types of circuits:

1. High rush-in circuits—contain incandescent lamps that can draw an initial current 15 times greater than the continuous current. Contact burning or welding may occur when the switch is closed.

2. Inductive circuits—magnetic energy stored in solenoid coils or relays is released and appears as an arc when the control switch is opened.

3. Motors—DC motors draw several times their rated current during starting, and magnetic energy stored in their armature and field coils is released when the control switch is opened.

Figure 9-166 is used for selecting the proper nominal switch rating when the continuous load current is known. This selection is essentially a derating to obtain reasonable switch efficiency and service life.

#### Type of Switches

Single-pole single-throw (SPST)—opens and closes a single circuit. Pole indicates the number of separate circuits that can be activated, and throw indicates the number of current paths.

Double-pole single-throw (DPST)—turn two circuits on and off with one lever.

Single-pole double-throw (SPDT)—route circuit current to either of two paths. The switch is ON in both positions. For example, switch turns on red lamp in one position and turns on green lamp in the other position.

Double-pole double-throw (DPDT)—activates two separate circuits at the same time.

Double-throw switches—have either two or three positions.

Two-position switch—pole always connected to one of the two throws. Three-position switches have a center OFF position that disconnects the pole from both throws.

Spring-loaded switches—available in two types: 1) normally open (NO) and 2) normally closed (NC). The contacts of the NO switch are disconnected in the normal position and become closed when the switch is activated. The switch returns to the normal position when the applied force to the switch is released. The contacts of the NC switch are connected in the normal position and become open when the switch is activated. The switch returns to the normal position when the applied force to the switch is released.

#### Toggle & Rocker Switches

Toggle and rocker switches control most of aircraft’s electrical components. Aircraft that are outfitted with a glass flight deck often use push buttons to control electrical components.

#### Rotary Switches

Rotary switches are activated by twisting a knob or shaft and are commonly found on radio control panels. Rotary switches are utilized for controlling more than two circuits.

#### Precision (Micro) Switches

Micro switches require very little pressure to activate. These types of switches are spring loaded, once the pressure is removed, the contacts return to the normal position. These types of switches are typically single-pole double-throw (SPDT) or double-pole double-throw (DPDT) and have three contacts: normally open, normally closed, and common. Micro switches are used to detect position or to limit travel of moving parts, such as landing gear, flaps, spoilers, etc.

### Relays & Solenoids (Electromagnetic Switches)

Relays are used to control the flow of large currents using a small current. A low-power DC circuit is used to activate the relay and control the flow of large AC currents. They are used to switch motors and other electrical equipment on and off and to protect them from overheating. A solenoid is a special type of relay that has a moving core. The electromagnet core in a relay is fixed. Solenoids are mostly used as mechanical actuators but can also be used for switching large currents. Relays are only used to switch currents.

#### Solenoids

Solenoids are used as switching devices where a weight reduction can be achieved or electrical controls can be simplified. The foregoing discussion of switch ratings is generally applicable to solenoid contact ratings. Solenoids have a movable core/armature that is usually made of steel or iron, and the coil is wrapped around the armature. The solenoid has an electromagnetic tube and the armature moves in and out of the tube.

#### Relays

The two main types of relays are electromechanical and solid state. Electromechanical relays have a fixed core and a moving plate with contacts on it, while solid-state relays work similar to transistors and have no moving parts. Current flowing through the coil of an electromechanical relay creates a magnetic field that attracts a lever and changes the switch contacts. The coil current can be on or off so relays have two switch positions. These can be made as a single throw or double throw switch. Residual magnetism is a common problem and the contacts may stay closed or are opened by a slight amount of residual magnetism. A relay is an electrically operated switch and is therefore subject to dropout under low system voltage conditions. Relays allow one circuit to switch a second circuit that can be completely separate from the first. For example, a low voltage DC battery circuit can use a relay to switch a 110-volt three-phase AC circuit. There is no electrical connection inside the relay between the two circuits; the link is magnetic and mechanical.

### Current Limiting Devices

Conductors should be protected with circuit breakers or fuses located as close as possible to the electrical power source bus. Normally, the manufacturer of the electrical equipment specifies the fuse or circuit breaker to be used when installing equipment. The circuit breaker or fuse should open the circuit before the conductor emits smoke. To accomplish this, the time current characteristic of the protection device must fall below that of the associated conductor. Circuit protector characteristics should be matched to obtain the maximum utilization of the connected equipment. Figure 9-171 shows a chart used in selecting the circuit breaker and fuse protection for copper conductors. This limited chart is applicable to a specific set of ambient temperatures and wire bundle sizes and is presented as typical only. It is important to consult such guides before selecting a conductor for a specific purpose. For example, a wire run individually in the open air may be protected by the circuit breaker of the next higher rating to that shown on the chart.

#### Fuses

A fuse is placed in series with the voltage source and all current must flow through it. The fuse consists of a strip of metal that is enclosed in a glass or plastic housing. The metal strip has a low melting point and is usually made of lead, tin, or copper. When the current exceeds the capacity of the fuse the metal strip heats up and breaks. As a result of this, the flow of current in the circuit stops.

There are two basic types of fuses: fast acting and slow blow. The fast-acting type opens very quickly when their particular current rating is exceeded. This is important for electric devices that can quickly be destroyed when too much current flows through them for even a very small amount of time. Slow blow fuses have a coiled construction inside. They are designed to open only on a continued overload, such as a short circuit.

#### Circuit Breakers

A circuit breaker is an automatically operated electrical switch designed to protect an electrical circuit from damage caused by an overload or short circuit. Its basic function is to detect a fault condition and immediately discontinue electrical flow. Unlike a fuse that operates once and then has to be replaced, a circuit breaker can be reset to resume normal operation. All resettable circuit breakers should open the circuit in which they are installed regardless of the position of the operating control when an overload or circuit fault exists. Such circuit breakers are referred to as trip-free. Automatic reset circuit breakers automatically reset themselves. They should not be used as circuit protection devices in aircraft. When a circuit breaker trips, the electrical circuit should be checked and the fault removed before the circuit breaker is reset. Sometimes circuit breakers trip for no apparent reason, and the circuit breaker can be reset one time. If the circuit breaker trips again, there exists a circuit fault and the technician must troubleshoot the circuit before resetting the circuit breaker.

Some new aircraft designs use a digital circuit protection architecture. This system monitors the amperage through a particular circuit. When the maximum amperage for that circuit is reached, the power is rerouted away from the circuit. This system reduces the use of mechanical circuit breakers. The advantages are weight savings and the reduction of mechanical parts.

## 2. 中文翻译

### 开关

开关是用于接通和断开电路的器件。开关由一对或多对触点组成。触点闭合时，电流即在电路中流通。带瞬动触点的开关只在操作时短暂接通电路，松开开关后靠内部弹簧返回正常位置。带持续触点的开关在操作后保持原位。通过合理而一致的安装方式，可以避免开关操作中的危险性差错。双位通/断开关的安装，应使“接通”位可由拨杆向上或向前动作达到。当开关控制起落架、襟翼等活动部件时，拨杆的运动方向应与所需运动的方向一致。在开关上加装合适的护罩，可以防止误操作。凡开关失效会造成危险的电路，都应使用专门设计的开关。此类开关结构坚固，触点容量足以接通、断开并连续承载所接的负载电流。通常优先采用瞬动（snap action）设计，使触点的断开与闭合不受拨杆或推杆动作速度的影响，从而把触点起弧降到最低。常规飞机开关的额定电流通常压印在开关壳体上。该额定值指的是触点闭合时的连续电流额定值。对于下列各类电路，开关应在额定电流的基础上降额使用：

1. 高浪涌电路——含有白炽灯，其起始电流可达连续电流的15倍。开关闭合时可能发生触点烧蚀或熔焊。

2. 感性电路——控制开关断开时，储存在电磁线圈或继电器中的磁能释放出来，形成电弧。

3. 电动机——直流电动机起动时的电流可达额定值的数倍；控制开关断开时，储存在电枢和励磁线圈中的磁能也会释放。

在已知连续负载电流的情况下，可用图9-166选择恰当的开关额定值。这种选择实质上就是降额，以获得合理的开关效率和使用寿命。

#### 开关的类型

单刀单掷（SPST）——接通和断开一个电路。刀（pole）表示可被接通的独立电路数目，掷（throw）表示电流通路的数目。

双刀单掷（DPST）——用一个手柄同时接通和断开两个电路。

单刀双掷（SPDT）——把电路电流引向两条通路中的任意一条。开关在两个位置均为接通。例如，开关在一个位置点亮红灯，在另一个位置点亮绿灯。

双刀双掷（DPDT）——同时接通两个独立的电路。

双掷开关——有两个或三个位置。

双位开关——刀始终与两个掷中的一个相连。三位开关有一个居中的“断”位，使刀与两个掷都断开。

弹簧复位开关——有两种：1）常开（NO），2）常闭（NC）。常开开关的触点在正常位置是断开的，操作开关时闭合；撤去施加在开关上的力后，开关返回正常位置。常闭开关的触点在正常位置是接通的，操作开关时断开；撤去施加在开关上的力后，开关返回正常位置。

#### 拨杆开关与翘板开关

飞机的多数电气部件由拨杆开关和翘板开关控制。配备玻璃驾驶舱（glass flight deck）的飞机则常用按钮来控制电气部件。

#### 旋转开关

旋转开关通过转动旋钮或转轴来操作，常见于无线电控制面板。旋转开关用于控制两个以上的电路。

#### 精密（微型）开关

微型开关只需很小的压力即可动作。这类开关装有弹簧，一旦卸去压力，触点即返回正常位置。这类开关通常为单刀双掷（SPDT）或双刀双掷（DPDT），有三个触点：常开、常闭和公共端。微型开关用于检测位置或限制运动部件的行程，如起落架、襟翼、扰流板等。

### 继电器与电磁线圈（电磁开关）

继电器用小电流控制大电流的通断。它由一个小功率直流电路来激励，从而控制大交流电流的通断。继电器用于接通和断开电动机及其他电气设备，并保护它们免于过热。电磁线圈是一种特殊型式的继电器，其铁芯是可动的；而继电器中的电磁铁芯是固定的。电磁线圈多用作机械作动器，但也可用于通断大电流。继电器则只用于通断电流。

#### 电磁线圈

在能够减轻重量或简化电气控制的场合，电磁线圈被用作开关器件。前面关于开关额定值的讨论，一般也适用于电磁线圈的触点额定值。电磁线圈有一个可动的铁芯/衔铁，通常由钢或铁制成，线圈绕在衔铁上。电磁线圈有一个电磁管，衔铁在管内进出移动。

#### 继电器

继电器主要有两种型式：机电式和固态式。机电式继电器有一个固定铁芯和一块带触点的可动衔铁板；固态继电器的工作方式类似晶体管，没有运动部件。电流流过机电式继电器的线圈时产生磁场，吸引衔铁杆并使开关触点换位。线圈电流可以接通或断开，因此继电器有两个开关位置，可做成单掷或双掷开关。剩磁是常见问题，触点可能保持闭合，或因少量剩磁而保持断开。继电器是一种由电操作的开关，因此在系统电压过低的条件下会出现释放（dropout）。继电器可以让一个电路去切换另一个与之完全分开的电路。例如，低压直流电池电路可用继电器切换110伏三相交流电路。继电器内部两个电路之间没有电气连接，其联系是磁性的和机械的。

### 限流装置

导线应使用尽可能靠近电源汇流条的断路器或保险丝加以保护。通常，电气设备的制造商在安装设备时会规定应使用的保险丝或断路器。断路器或保险丝应在导线冒烟之前断开电路。为此，保护装置的时间—电流特性必须低于所关联导线的特性。应使电路保护装置的特性与之匹配，以充分利用所接的设备。图9-171给出一张用于为铜导线选择断路器和保险丝保护的图表。这张有限的图表只适用于特定的一组环境温度和线束规格，仅作典型示例。在为特定用途选择导线之前，查阅此类指南是很重要的。例如，单独敷设在开阔空气中的导线，可以由额定值比图表所示高一级的断路器来保护。

#### 保险丝

保险丝与电源串联，所有电流都必须流过它。保险丝由一条金属片构成，封装在玻璃或塑料壳体内。金属片熔点低，通常由铅、锡或铜制成。当电流超过保险丝的容量时，金属片发热并熔断，于是电路中的电流停止。

保险丝有两种基本类型：快熔式和慢熔式。快熔式保险丝在超过其特定额定电流时迅速熔断。对于那些电流稍大且时间极短就会被迅速烧毁的电气设备，这一点很重要。慢熔式保险丝内部为线圈结构，设计上只在持续过载（如短路）时才熔断。

#### 断路器

断路器是一种自动操作的电气开关，用于保护电路免受过载或短路造成的损坏。其基本功能是检测故障状态并立即切断电流。与熔断一次后必须更换的保险丝不同，断路器可以复位以恢复正常工作。所有可复位断路器在存在过载或电路故障时，无论操作手柄处于什么位置，都应断开其所在电路。这类断路器称为自由脱扣（trip-free）式。自动复位断路器会自行复位，不得在飞机上用作电路保护装置。断路器跳开后，应先检查电路并排除故障，然后再复位。有时断路器会无明显原因地跳开，此时可将断路器复位一次；若再次跳开，则说明存在电路故障，技术人员必须在复位前对电路进行排故。

一些新机型采用数字式电路保护架构。该系统监测通过某一特定电路的电流值。当达到该电路的最大电流时，电源即被改接到该电路之外。这种系统减少了机械式断路器的使用，其优点是减轻重量和减少机械部件。

## 3. 专业词汇

| 英文 | 词性 | 中文 | 本节语境 |
| --- | --- | --- | --- |
| momentary contact | n. | 瞬动触点 | 只在操作瞬间接通、松手后靠内部弹簧复位的触点形式 |
| continuous contact | n. | 持续触点 | 操作后保持位置、不自动复位的触点 |
| toggle | n. | 拨杆 | 双位开关上向上或向前扳动的操作杆，其运动方向要求与所控部件的运动一致 |
| snap action | n. | 瞬动（快跳）机构 | 使触点迅速开合、不受拨动速度影响的设计，用于抑制起弧 |
| contact arcing | n. | 触点起弧 | 触点开合瞬间产生的电弧，是开关降额与选用瞬动设计的原因 |
| derating | n. | 降额 | 按低于额定电流的档次选用开关，以兼顾效率与使用寿命 |
| rush-in current | n. | 浪涌电流 | 白炽灯冷态起动时可达连续电流15倍的初始电流 |
| pole / throw | n. | 刀/掷 | 刀指可接通的独立电路数，掷指电流通路数，二者构成SPST等代号 |
| armature | n. | 衔铁（电枢） | 电磁线圈中可动的铁芯，也是直流电动机储存磁能的部分 |
| residual magnetism | n. | 剩磁 | 断电后铁芯残留的磁性，会使触点误保持闭合或误断开 |
| dropout | n. | 释放（脱扣） | 系统电压过低时继电器吸力不足而自行释放 |
| trip-free | adj. | 自由脱扣的 | 存在故障时无论操作手柄位置如何都强制断开电路 |
| circuit breaker | n. | 断路器 | 可复位的过流保护开关，跳开后须先排故再复位 |
| fuse | n. | 保险丝 | 与电源串联、过流即熔断的一次性保护元件 |

## 4. 语法解析

### ① so that 引导的目的/结果状语从句 + 被动语态
**原句**：Two-position on/off switches should be mounted so that the on position is reached by an upward or forward movement of the toggle.
**拆解**：主句为被动语态 should be mounted（主语 Two-position on/off switches）；so that 引导从句，从句主语 the on position，谓语 is reached（被动），by an upward or forward movement of the toggle 为方式状语。
**要点**：so that 既可表目的也可表结果，此处是“安装成……以便……”的目的意味。从句仍用被动，是因为“接通位”是被人为扳到的；汉语习惯转成主动“由拨杆向上或向前扳到”。

### ② where 引导的定语从句 + 情态动词被动
**原句**：A specifically designed switch should be used in all circuits where a switch malfunction would be hazardous.
**拆解**：主句 A specifically designed switch should be used in all circuits（被动）；where 引导定语从句修饰 circuits，从句主语 a switch malfunction，谓语 would be hazardous（系表结构）。
**要点**：where 在此等于 in which，先行词是 circuits 而非 switch；从句本身是主动的系表结构，不要误以为整句都是被动。翻译时 where 常处理成“凡……的电路”。

### ③ be of + 抽象名词 与并列谓语后的不定式定语
**原句**：Such switches are of rugged construction and have sufficient contact capacity to break, make, and carry continuously the connected load current.
**拆解**：主语 Such switches 带两个并列谓语：are of rugged construction（be of + 名词，表性质）和 have sufficient contact capacity；不定式 to break, make, and carry 作 capacity 的后置定语，continuously 修饰 carry，宾语 the connected load current 后置。
**要点**：be of + 抽象名词相当于该名词对应的形容词（of rugged construction = ruggedly constructed）。to break, make, and carry 三个动词共用一个宾语，宾语因太长而后置，别把 continuously 误当成修饰 break。

### ④ 不定式目的状语 + regardless of + thereby 分词结果状语
**原句**：Snap action design is generally preferred to obtain rapid opening and closing of contacts regardless of the speed of the operating toggle or plunger, thereby minimizing contact arcing.
**拆解**：主句为被动 is generally preferred；to obtain... 为不定式作目的状语；regardless of 引导让步性介词短语修饰整个动作；thereby + 现在分词 minimizing 作结果状语，其逻辑主语是前面整件事。
**要点**：thereby doing 是书面语中表示“由此产生的结果”的固定结构，不另起分句，因此前面只用逗号。regardless of 后接名词短语，不能接从句。

### ⑤ 并列句 + when 时间状语从句 + with 方式状语
**原句**：Switches with momentary contacts actuate the circuit temporarily, and they return to the normal position with an internal spring when the switch is released.
**拆解**：and 连接两个分句；前句主语 Switches，with momentary contacts 为介词短语作后置定语；后句主语 they（指开关），谓语 return，with an internal spring 为方式状语，when 引导时间状语从句（被动 is released）。
**要点**：with momentary contacts 修饰 Switches 而不是作状语，判断依据是它紧跟名词且不能移到句末。when 从句用被动，是因为“开关被松开”，汉语可译成主动“松开开关后”。

### ⑥ the same ... as 比较结构 + when 状语从句中的插入语
**原句**：When the switch controls movable aircraft elements, such as landing gear or flaps, the toggle should move in the same direction as the desired motion.
**拆解**：When 引导时间状语从句；such as landing gear or flaps 为插入的同位成分，举例说明 elements；主句 the toggle should move in the same direction as the desired motion，其中 the same ... as 构成比较。
**要点**：the same direction as 中 as 是关系代词性质的连接词，后面跟一个名词短语而非完整从句。such as 的插入语用一对逗号隔开，去掉后句子依然完整。
