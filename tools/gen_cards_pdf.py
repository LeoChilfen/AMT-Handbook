# -*- coding: utf-8 -*-
"""Generate study-card skeletons from sections JSON (PDF-outline based).

Usage:
  python gen_cards_pdf.py sections-ch01.json --book general --chapter 01 \
         --root F:\\AMT-Handbook --glossary glossary.json [--min-chars 200]
"""
import sys, io, json, re, os, argparse

CARD = u"""# {title}

> 通用 Ch {num} · {title} · 原文 PDF 第 {page} 页

## 1. 原文

{body}

## 2. 中文翻译

<!-- TODO: 逐段翻译，段数与上面严格一一对应（{nparas} 段）。专业术语按行业惯例，数字与缩写保留。 -->

## 3. 专业词汇

<!-- TODO: 用表格 | 英文 | 词性 | 中文 | 本节语境 |，4~8 行。优先选下面 Glossary 里的词（本节原文出现过的）：
{hints}
-->

## 4. 语法解析

<!-- TODO: 2~4 个语法点，格式：
### ① 语法点名称
**原句**：<必须逐字来自第 1 节原文>
**拆解**：主/谓/宾、从句、非谓语等成分分析
**要点**：为什么这样用、易错点、可迁移的搭配
-->
"""


def slug(title):
    s = title.lower()
    s = re.sub(r"&", " and ", s)
    s = re.sub(r"[^a-z0-9]+", "-", s)
    return s.strip("-")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("sections")
    ap.add_argument("--book", default="general")
    ap.add_argument("--chapter", required=True)
    ap.add_argument("--root", default=r"F:\AMT-Handbook")
    ap.add_argument("--glossary")
    ap.add_argument("--min-chars", type=int, default=200)
    a = ap.parse_args()

    secs = json.load(io.open(a.sections, encoding="utf-8"))
    gl = json.load(io.open(a.glossary, encoding="utf-8")) if a.glossary else []

    outdir = os.path.join(a.root, "cards", a.book, "ch" + a.chapter)
    if not os.path.isdir(outdir):
        os.makedirs(outdir)

    made = 0
    skipped = []
    for s in secs:
        paras = [p for p in s["paras"] if len(p) >= 20]
        total = sum(len(p) for p in paras)
        if total < a.min_chars:
            skipped.append((s["title"], total))
            continue
        body = "\n\n".join(paras)
        # glossary terms that actually appear in this section
        low = body.lower()
        hints = []
        for g in gl:
            key = g["term"].split("(")[0].strip().lower()
            if len(key) < 5:
                continue
            pat = r"\b" + r"\s+".join(re.escape(w) for w in key.split()) + r"\b"
            if re.search(pat, low):
                hints.append(u"- %s —— %s" % (g["term"], g["def"][:160]))
        hints = hints[:8]
        if not hints:
            hints = [u"-（本节原文没有直接命中 Glossary 的词，按专业术语自选）"]
        fn = "%02d-%s.md" % (s["seq"], slug(s["title"])[:70] or "section")
        with io.open(os.path.join(outdir, fn), "w", encoding="utf-8", newline="\n") as f:
            f.write(CARD.format(title=s["title"], num=a.chapter, page=s["page"],
                                body=body, nparas=len(paras),
                                hints="\n".join(hints)))
        made += 1

    print("root:", a.root)
    print("written:", made, "->", outdir)
    if skipped:
        print("skipped (<%d chars):" % a.min_chars)
        for t, n in skipped:
            print("   %-58s %d" % (t[:58], n))


if __name__ == "__main__":
    main()
