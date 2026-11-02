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

<!-- TODO: 逐段对应翻译，术语按行业惯例（如 tie-down 系留、fireguard 消防警戒员） -->

## 3. 专业词汇

<!-- TODO: 表格 | 英文 | 词性 | 中文 | 本节语境 |，4~8 条 -->

## 4. 语法解析

<!-- TODO: 2~4 个语法点，每条写「原句 / 拆解 / 要点」 -->
