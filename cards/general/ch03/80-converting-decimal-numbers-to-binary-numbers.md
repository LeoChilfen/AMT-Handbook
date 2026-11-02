# Converting Decimal Numbers to Binary Numbers

> 通用 Ch 03 · Converting Decimal Numbers to Binary Numbers · 原文 PDF 第 123 页

## 1. 原文

To convert a decimal number to a binary number, the place values in the binary system are used to create a sum of numbers that equal the value of the decimal number being converted. Start with the largest binary place value and subtract from the decimal number. Continue this process until all of the binary digits are determined.

Example: Convert the decimal number 233 to a binary number.

Start by subtracting 128 (the largest place value from the 8-bit binary number) from 233.

233 – 128 = 105 A “1” is placed in the first binary digit space: 1XXXXXXX.

Continue the process of subtracting the binary number 105 – 64 = 41 A “1” is placed in the second binary digit space: 11XXXXXX.

41 – 32 = 9 A “1” is placed in the third binary digit space: 111XXXXX.

Place Value 27 or 128 26 or 64 25 or 32 24 or 16 23 or 8 22 or 4 21 or 2 20 or 1 1 0 0 1 1 0 0 1 0 0 1 0 1 0 1 1 10011001 shown as 00101011 shown as =153 =43 Place Value 27 or 128 26 or 64 25 or 32 24 or 16 23 or 8 22 or 4 21 or 2 20 or 1 1 0 1 1 0 0 1 1 128 + 0 + 32 + 16 + 0 + 0 + 2 + 1 10110011 shown as =179 Place Value 27 or 128 26 or 64 25 or 32 24 or 16 23 or 8 22 or 4 21 or 2 20 or 1 0 0 1 0 0 0 1 1 0 1 1 1 1 1 0 0 0 1 1 0 0 0 0 0 1 1 1 1 1 1 1 1 1 1 1 0 1 0 0 1 35 shown as 124 shown as 96 shown as 255 shown as 233 shown as Since 9 is less than 16 (the next binary place value), a “0” is placed in the fourth binary digit space, 1110XXXX.

9 – 8 = 1 A “1” is placed in the fifth binary digit space: 11101XXX Since 1 is less than 4 (the next binary place value), a 0 is placed in the sixth binary digit space: 111010XX.

Since 1 is less than 2 (the next binary place value), a 0 is placed in the seventh binary digit space: 1110100X.

1 – 1 = 0 A “1” is placed in the eighth binary digit space: 11101001.

The decimal number 233 is equivalent to the binary number 11101001, as shown in Figure 3-36.

Three additional decimal number to binary number conversions are shown in Figure 3-36.

## 2. 中文翻译

要把十进制数换算成二进制数，可利用二进制数制的各数位值，凑出一组和等于待换算十进制数的数值。从最大的二进制数位值开始，从十进制数中减去它，一直重复这一过程，直到确定全部二进制位。

例：把十进制数 233 换算为二进制数。

先从 233 中减去 128（8 位二进制数中最大的数位值）。

233 – 128 = 105，在第一个二进制位的位置上记「1」：1XXXXXXX。

继续做减法 105 – 64 = 41，在第二个二进制位的位置上记「1」：11XXXXXX。

41 – 32 = 9，在第三个二进制位的位置上记「1」：111XXXXX。

（原文此处为图 3-36 的数位值表与多组换算示例被 OCR 压平后的残片，可辨认者有：数位值 2⁷ 或 128、2⁶ 或 64、2⁵ 或 32、2⁴ 或 16、2³ 或 8、2² 或 4、2¹ 或 2、2⁰ 或 1；以及示例结果 153、43、179、35、124、96、255、233，各组 0/1 阵列因错行无法与算式一一对应，此处略。）由于 9 小于 16（下一个二进制数位值），在第四个二进制位的位置上记「0」，得 1110XXXX。

9 – 8 = 1，在第五个二进制位的位置上记「1」：11101XXX。由于 1 小于 4（下一个二进制数位值），在第六个二进制位的位置上记 0：111010XX。

由于 1 小于 2（下一个二进制数位值），在第七个二进制位的位置上记 0：1110100X。

1 – 1 = 0，在第八个二进制位的位置上记「1」：11101001。

十进制数 233 等于二进制数 11101001，如图 3-36 所示。

图 3-36 还给出了另外三组十进制数换算为二进制数的示例。

## 3. 专业词汇

| 英文 | 词性 | 中文 | 本节语境 |
| --- | --- | --- | --- |
| place value | n. phr. | 数位值 | 2 的幂：128、64、32……1 |
| binary digit space | n. phr. | 二进制位（数位空位） | 从左到右 8 个空位，用 X 占位待填 |
| subtract | v. | 减、减去 | subtract 128 from 233，注意 from 引出的方向 |
| equivalent to | phr. | 等于、相当于 | 233 is equivalent to 11101001 |
| 8-bit | adj. | 8 位的 | the 8-bit binary number，本例的位数框架 |
| conversion | n. | 换算 | decimal to binary conversions |
| bit | n. | 位（二进制位） | 由 8-bit 派生，binary digit 的缩合 |
| decimal number | n. phr. | 十进制数 | 待换算的原始数值，如 233 |

## 4. 语法解析

### ① 目的状语 + 被动句 + being converted

**原句**：To convert a decimal number to a binary number, the place values in the binary system are used to create a sum of numbers that equal the value of the decimal number being converted.

**拆解**：To convert … 是不定式短语作目的状语；主句为被动 the place values … are used to create …；that equal the value … 是定语从句修饰 a sum of numbers；being converted 是现在分词被动式，作后置定语修饰 the decimal number。

**要点**：这是「方法定义句」，用被动是因为重点在方法与对象而非执行者。being converted 强调「正在被换算的那个数」，与 converted（已完成）不同；它也可看作 the decimal number (which is) being converted 的省略形式。

### ② A is placed in …：操作类被动句

**原句**：A “1” is placed in the first binary digit space: 1XXXXXXX.

**拆解**：被动语态 is placed；in the first binary digit space 是地点状语；冒号后 1XXXXXXX 用 X 占位，表示尚未确定的低位。

**要点**：操作类被动句「A is placed in …」译作「在……上记 A」即可，中文不必保留被动。X 是占位符（placeholder），不是字母 X 的读音；书写时 X 的个数应等于尚未确定的位数，本例第一个空位记 1 后还剩 7 个 X。

### ③ since 表原因 + less than 比较

**原句**：Since 9 is less than 16 (the next binary place value), a “0” is placed in the fourth binary digit space, 1110XXXX.

**拆解**：Since 9 is less than 16 是原因状语从句（此处 since = because，不是「自从」）；括号内 the next binary place value 是 16 的同位语；主句为被动 a “0” is placed …，末尾 1110XXXX 是结果说明。

**要点**：since 有两义——「自从」（主句配现在完成时）与「因为」（配原因从句），这里从句用一般现在时 is，只能是「因为」。数值比较一律用 less than，可数名词的「更少」才用 fewer than；这是机务换算中容易混的一对。
