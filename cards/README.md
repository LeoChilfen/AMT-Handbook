# 学习卡片 · Study Cards

按手册的**二级目录**（每章的直接子条目，如 Ch 01 的 `Shop Safety`、`Fire Protection`）拆出来的学习卡片。
一张卡覆盖一个大节：从该标题之后开始，到下一个二级标题之前结束的**全部原文**（其中更细的小标题按
书签层级渲染成 `###` / `####` / `#####` 的 Markdown 标题，翻译里同样保留、同级别），再配三块学习内容。

卡片里**不放图**：手册原文中所有图号引用（`[Figure 1-4]`）、「如图 1-x 所示」这类句子、以及 PDF 抽出来的
图内文字与表格乱码碎片，一律删除，中英文成对删掉、段落数保持一一对应。

## 卡片长什么样

```markdown
# Shop Safety

> 通用 Ch 01 · Shop Safety · 原文 PDF 第 23 页

## 1. 原文                 ← 手册英文原文，逐段保留（禁止改写）；小标题按目录层级用 ### / ####
## 2. 中文翻译             ← 与原文自然段一一对应的专业翻译，标题层级与英文一致
## 3. 专业词汇             ← 表格：英文 | 词性 | 中文 | 本节语境（10~12 条，优先取 Glossary 词条）
## 4. 语法解析             ← 4~6 个语法点，每个含 原句 / 拆解 / 要点
```

标题层级取 PDF 书签 depth：书签 depth 2 → `###`（17.5px）、depth 3 → `####`（15.5px）、
depth 4 → `#####`（14.5px），由 `tools/build_site.py` 的 `.content h3/h4/h5` 控制字号。

## 目录结构

```
cards/
  general/ch01/01-shop-safety.md
  general/ch01/02-safety-around-compressed-gases.md
  ...
```

`<序号>-<标题 slug>.md`，序号即本节在该章里的先后顺序（来自 PDF 书签顺序）。

## 分段依据

直接读 PDF 的**书签（outline / bookmarks）**：目录树里每一章下面的子条目就是小节标题，
并带目标页。流水线按书签顺序在正文里定位每个标题，两个标题之间的文字即本节原文。

- 卡片粒度取**二级目录**（书签 depth == 1，即章的直接子条目），pdf_sections.py --level 1；--level 0 则是每条书签一张卡（旧版）；
- 父级标题（下面直接跟子标题、自身没有正文）不单独出卡；
- 正文不足 200 字符的标题跳过（多为一句话说明或纯图表页）；
- 段落切分依据「换行行尾是否有空格」：折行有尾空格、段落末行没有。

## 专业词汇取词

`tools/glossary.py` 从手册 Glossary 章（G-1 起）抽条目，生成 `glossary.json`。
出卡时把「本节原文里出现过的 Glossary 词条」写进第 3 节的 TODO 注释，填卡时优先采用。

## 重新生成 / 校验

需要 `pypdf`（`pip install pypdf`）。

```bash
PDF="AMT Handbook-General2023.pdf"

# 1. 导出书签树（标题 + 页码）
python tools/pdf_outline.py "$PDF" outline.json

# 2. 导出每页正文（jsonl，一行一页）
python tools/pdf_pages.py "$PDF" pages.jsonl 1 678

# 3. 按书签把某一章切成小节（输出 paras 列表）
python tools/pdf_sections.py --outline outline.json --pages pages.jsonl \
       --chapter 1 --json sections-ch01.json --level 1

# 4. 抽 Glossary 词条
python tools/glossary.py pages.jsonl glossary.json 657 667

# 5. 出卡片骨架（只有原文 + 三个 TODO）
python tools/gen_cards_pdf.py sections-ch01.json --book general --chapter 01 \
       --root . --glossary glossary.json

# 6. 校验：四节齐全、无 TODO、翻译段数够、词汇表够行、语法点都有原句
python tools/check_cards.py cards/general/ch01
```

站点由 `tools/build_site.py` 自动把 `cards/**/*.md` 渲染成
`docs/cards/<chapter>-<seq>.html`，入口是侧栏的「学习卡片」。含 `TODO` 的未完成卡片不会上站。

> 旧流程（`parse_toc.py` / `locate_headings.py` / `gen_cards.py` / `split_sections.py`）是从
> 纯文本抽取件切节的版本，保留以便换用没有书签的 PDF；有书签时优先用上面的 `pdf_*.py`。
