# The Binary Number System

> 通用 Ch 03 · The Binary Number System · 原文 PDF 第 123 页

## 1. 原文

The binary number system has only two digits: 0 and 1. The prefix in the word “binary” is a Latin root for the word “two” and its use was first published in the late 1700s. The use of the binary number system is based on the fact that switches or valves have two states: open or closed (on/off).

Currently, one of the primary uses of the binary number system is in computer applications. Information is stored as a series of 0s and 1s, forming strings of binary numbers. An early electronic computer, ENIAC ( Electronic Numerical Integrator and Calculator), was built in 1946 at the University of Pennsylvania and contained 17,000 vacuum tubes, along with 70,000 resistors, 10,000 capacitors, 1,500 relays, 6,000 manual switches and 5 million soldered joints. Computers obviously have changed a great deal since then, but are still based on the same binary number system. The binary number system is also useful when working with digital electronics because the two basic conditions of electricity, on and off, can be represented by the two digits of the binary number system. When the system is on, it is represented by the digit 1, and when it is off, it is represented by the digit 0.

The binary number system is a Base-2 system. That is, the place values in the binary number system are based on powers of 2. An 8-bit binary number system is shown below.

### Converting Binary Numbers to Decimal Numbers

To convert a binary number to a decimal number, add up the place values that have a 1 (place values that have a zero do not contribute to the decimal number conversion).

Example: Convert the binary number 10110011 to a decimal number. Using the place value chart, add up the place values of the ‘1s’ in the binary number (ignore the place values with a zero in the binary number).

The binary number 10110011 = 128 + 0 + 32 + 16 + 0 + 0 + 2 + 1 = 179 in the decimal number system

### Converting Decimal Numbers to Binary Numbers

To convert a decimal number to a binary number, the place values in the binary system are used to create a sum of numbers that equal the value of the decimal number being converted. Start with the largest binary place value and subtract from the decimal number. Continue this process until all of the binary digits are determined.

Example: Convert the decimal number 233 to a binary number. Start by subtracting 128 (the largest place value from the 8-bit binary number) from 233.

233 – 128 = 105 A “1” is placed in the first binary digit space: 1XXXXXXX.

Continue the process of subtracting the binary number place values:

105 – 64 = 41 A “1” is placed in the second binary digit space: 11XXXXXX.

41 – 32 = 9 A “1” is placed in the third binary digit space: 111XXXXX.

Place Value 27 or 128 26 or 64 25 or 32 24 or 16 23 or 8 22 or 4 21 or 2 20 or 1 1 0 0 1 1 0 0 1 0 0 1 0 1 0 1 1 10011001 shown as 00101011 shown as =153 =43 Place Value 27 or 128 26 or 64 25 or 32 24 or 16 23 or 8 22 or 4 21 or 2 20 or 1 1 0 1 1 0 0 1 1 128 + 0 + 32 + 16 + 0 + 0 + 2 + 1 10110011 shown as =179 Place Value 27 or 128 26 or 64 25 or 32 24 or 16 23 or 8 22 or 4 21 or 2 20 or 1 0 0 1 0 0 0 1 1 0 1 1 1 1 1 0 0 0 1 1 0 0 0 0 0 1 1 1 1 1 1 1 1 1 1 1 0 1 0 0 1 35 shown as 124 shown as 96 shown as 255 shown as 233 shown as Since 9 is less than 16 (the next binary place value), a “0” is placed in the fourth binary digit space, 1110XXXX.

9 – 8 = 1 A “1” is placed in the fifth binary digit space: 11101XXX Since 1 is less than 4 (the next binary place value), a 0 is placed in the sixth binary digit space: 111010XX.

Since 1 is less than 2 (the next binary place value), a 0 is placed in the seventh binary digit space: 1110100X.

1 – 1 = 0 A “1” is placed in the eighth binary digit space: 11101001.

The decimal number 233 is equivalent to the binary number 11101001.

Three additional decimal number to binary number conversions are shown below.

## 2. 中文翻译

二进制数制只有两个数字：0 和 1。“binary”一词里的词头是拉丁语中表示“二”的词根，这种用法最早发表于 18 世纪晚期。二进制数制的应用基于这样一个事实：开关或阀门有两种状态——断开或闭合（关/开）。

目前，二进制数制的主要用途之一是计算机应用。信息以一连串的 0 和 1 存储，形成二进制数串。早期的电子计算机 ENIAC（Electronic Numerical Integrator and Calculator，电子数值积分计算机）于 1946 年在宾夕法尼亚大学建成，装有 17,000 只真空管，以及 70,000 个电阻、10,000 个电容、1,500 个继电器、6,000 个手动开关和 500 万个焊接点。此后计算机显然发生了巨大的变化，但依然基于同一套二进制数制。二进制数制在处理数字电子设备时也很有用，因为电的两种基本状态（通与断）可以用二进制数制的两个数字来表示。系统处于“通”的状态时用数字 1 表示，处于“断”的状态时用数字 0 表示。

二进制数制是以 2 为基数的数制。也就是说，二进制数制中的位值以 2 的幂为基础。8 位二进制数制如下所示。

### 把二进制数转换为十进制数

要把二进制数转换为十进制数，就把位值为 1 的那些位值加起来（位值为零的位不计入十进制换算）。

例：把二进制数 10110011 转换为十进制数。利用位值表，把该二进制数中“1”所对应的各位值相加（忽略该二进制数中为零的位）。

二进制数 10110011 = 128 + 0 + 32 + 16 + 0 + 0 + 2 + 1 = 十进制数制中的 179

### 把十进制数转换为二进制数

要把十进制数转换为二进制数，就用二进制数制的各位值去凑出一个等于被转换十进制数的和。先从最大的二进制位值开始，从十进制数中减去它。一直进行下去，直到所有二进制位都确定。

例：把十进制数 233 转换为二进制数。先从 233 中减去 128（8 位二进制数中最大的位值）。

233 – 128 = 105 把“1”放在第一个二进制位上：1XXXXXXX。

继续按二进制各位值进行相减：

105 – 64 = 41 把“1”放在第二个二进制位上：11XXXXXX。

41 – 32 = 9 把“1”放在第三个二进制位上：111XXXXX。

（原文此处为位值表与多组换算的碎片：Place Value、27 or 128 至 20 or 1 的位值栏，以及 10011001 shown as =153、00101011 shown as =43、10110011 shown as =179、35 shown as、124 shown as、96 shown as、255 shown as、233 shown as 等成串数字，原文无完整句子。）由于 9 小于 16（下一个二进制位值），在第四个二进制位上放“0”，即 1110XXXX。

9 – 8 = 1 把“1”放在第五个二进制位上：11101XXX 由于 1 小于 4（下一个二进制位值），在第六个二进制位上放 0，即 111010XX。

由于 1 小于 2（下一个二进制位值），在第七个二进制位上放 0，即 1110100X。

1 – 1 = 0 把“1”放在第八个二进制位上：11101001。

十进制数 233 等价于二进制数 11101001。

下面再给出三个十进制数到二进制数的换算。

## 3. 专业词汇

| 英文 | 词性 | 中文 | 本节语境 |
| --- | --- | --- | --- |
| binary number system | n.phr. | 二进制数制 | 只有 0 和 1 两个数字的计数制，本节主题 |
| digit | n. | 数字；数位 | 组成二进制数的 0 或 1，也指某一个二进制位 |
| decimal number system | n.phr. | 十进制数制 | 换算的目标数制，如 10110011 换成 179 |
| place value | n.phr. | 位值 | 每一位所代表的数值，二进制中为 27、26 … 20 |
| base-2 | n.phr. | 以 2 为基数 | 说明二进制位值按 2 的幂递增 |
| powers of 2 | n.phr. | 2 的幂 | 二进制位值的来源，如 128、64、32 … 1 |
| switch | n. | 开关 | 例中具有通/断两种状态的元件 |
| valve | n. | 阀门 | 与开关并列的两种状态元件，对应 0 与 1 |
| vacuum tube | n.phr. | 真空管 | ENIAC 时代计算机所用元件，共 17,000 只 |
| relay | n. | 继电器 | ENIAC 所用元件，共 1,500 个 |
| 8-bit | adj. | 8 位的 | 本节位值表与例题所用的二进制位宽 |
| sum | n. | 和 | 十进制转二进制时用各位值凑出的总和 |

## 4. 语法解析

### ① 冒号列举 + only 限定
**原句**：The binary number system has only two digits: 0 and 1.
**拆解**：主语 The binary number system；谓语 has；宾语 two digits 被 only 限定；冒号后 0 and 1 是对 two digits 的具体列举，不是独立分句。
**要点**：冒号后列举成分用逗号/and 连接即可，不必写成完整句；only 要紧贴被限定的 two，若说 has two digits only 则限定对象变成谓语。

### ② be based on the fact that 同位语从句
**原句**：The use of the binary number system is based on the fact that switches or valves have two states: open or closed (on/off).
**拆解**：主干 The use of the binary number system is based on the fact；that 引导同位语从句，解释 fact 的内容；从句主语 switches or valves，谓语 have，宾语 two states，冒号后 open or closed (on/off) 作补充。
**要点**：the fact that 中 that 不能换成 which（同位语从句不作成分）；be based on 后接名词或动名词，表示“以……为依据”。

### ③ 两个并列 when 从句 + 被动语态
**原句**：When the system is on, it is represented by the digit 1, and when it is off, it is represented by the digit 0.
**拆解**：and 连接两个并列分句，各由 when 时间状语从句开头；两个主句都是 it is represented by …（被动，by 引出表示手段的数字）。
**要点**：英语用 is on / is off 表示“处于开/关状态”，此处 on、off 是形容词；被动句 by 后的 digit 1 表示“用数字 1 来表示”，并非施动者，翻译要还原成主动。

### ④ That is 插入语 + be based on
**原句**：That is, the place values in the binary number system are based on powers of 2.
**拆解**：That is 是插入语（意为“也就是说”），用逗号与后文隔开；主干 the place values … are based on powers of 2，in the binary number system 作定语修饰 place values。
**要点**：That is 后必须加逗号，与 i.e. 意思相当；powers of 2 用复数表示“若干个 2 的幂”，不能写成 power of 2。

### ⑤ 目的不定式 + 祈使句 + 定语从句
**原句**：To convert a binary number to a decimal number, add up the place values that have a 1 (place values that have a zero do not contribute to the decimal number conversion).
**拆解**：To convert … 为目的状语置于句首；主句是祈使句 add up the place values；that have a 1 为定语从句修饰 place values；括号内另是一个完整句，含 that have a zero 定语从句。
**要点**：convert A to B 表示“把 A 换算成 B”，to 也可换为 into；祈使句无主语，技术说明中常用来给操作步骤；括号补充说明在翻译中可保留括号形式。

### ⑥ 被动 + 定语从句 + being converted 分词后置
**原句**：To convert a decimal number to a binary number, the place values in the binary system are used to create a sum of numbers that equal the value of the decimal number being converted.
**拆解**：目的状语 To convert … 置前；主句 the place values … are used to create a sum of numbers（被动 + 目的不定式）；that equal the value of the decimal number being converted 是定语从句修饰 numbers，其中 being converted 是现在分词被动式后置修饰 decimal number。
**要点**：be used to do 中的 to 是不定式符号（不是介词），别与 be used to doing（习惯于）混淆；being converted 表示“正在被转换的”，强调动作进行且为被动。
