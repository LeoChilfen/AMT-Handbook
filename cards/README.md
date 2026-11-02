# 学习卡片 · Study Cards

按「手册的每一节」拆出来的学习卡片。每张卡对应手册里一段红色标题小节：
从该标题之后开始，到下一个标题之前结束的**全部原文**，配三块学习内容。

## 卡片长什么样

```markdown
# Shop Safety

> 通用 Ch 01 · Shop Safety · 原文 PDF 第 23 页

## 1. 原文                 ← 手册英文原文，逐段保留（禁止改写）
## 2. 中文翻译             ← 与原文自然段一一对应的专业翻译
## 3. 专业词汇             ← 表格：英文 | 词性 | 中文 | 本节语境（4~9 条）
## 4. 语法解析             ← 2~4 个语法点，每个含 原句 / 拆解 / 要点
```

样板：`cards/general/ch01/01-shop-safety.md`。

## 目录结构

```
cards/
  general/ch01/01-shop-safety.md
  general/ch01/02-physiological-safety.md
  ...
```

`<序号>-<标题 slug>.md`，序号即本节在该章目录（TOC）中的先后顺序。

## 分段依据

手册 PDF 没有保留字体颜色，无法程序化取出「红色标题」。因此改用**书前目录（TOC）**：
目录里逐条列出每章的小节标题与印刷页码（如 `Shop Safety ............ 1-1`），
这就是权威的节序表。流水线把目录标题按顺序在正文里定位，两个标题之间的文字即本节原文。

- 父级标题（下面直接跟子标题、自身没有正文）不单独出卡；
- 正文不足 220 字符的标题跳过（多为一句话说明或纯图表页）。

## 重新生成 / 校验

素材（PDF 纹理后的按章 txt）默认读 `C:\Users\Admin\.dsh\docs-index\amt\_src`，
可用 `--root` 指向别处。

```bash
# 1. 解析书前目录，得到每章的权威小节标题表
python tools/parse_toc.py --json toc.json

# 2. 把标题按顺序定位到章节正文里（输出带行号/页码的 JSON）
python tools/locate_headings.py general 01 --toc toc.json --json heads-general-ch01.json

# 3. 按定位结果切出卡片骨架（只有原文 + 三个 TODO）
python tools/gen_cards.py general 01 --headings heads-general-ch01.json --skip-first

# 4. 校验：四节齐全、无 TODO、翻译段数够、词汇表够行、语法点都有原句
python tools/check_cards.py cards/general/ch01
```

站点由 `tools/build_site.py` 自动把 `cards/**/*.md` 渲染成
`docs/cards/<chapter>-<seq>.html`，入口是首页侧栏的「学习卡片」。
