"""Generate study-card skeletons from a chapter's PDF-extracted text.

Input : _src/<book>-ch<NN>.txt  +  a heading list JSON produced by
        locate_headings.py
        [{"line": 26, "page": 23, "print_page": "1-1", "title": "Shop Safety"}, ...]
Output: cards/<book>/ch<NN>/<seq>-<slug>.md
        Each card keeps the original English text and leaves three TODO
        blocks (translation / glossary / grammar) to be filled in.

Usage:
    python gen_cards.py <book> <ch> --headings heads-general-ch01.json [--root SRC] [--out CARDS]
"""
import io
import json
import os
import re
import sys

DEFAULT_SRC = r"C:\Users\Admin\.dsh\docs-index\amt\_src"
PAGE = re.compile(r"^===\s*PDF\s*(?:第\s*)?(\d+)")
PAGENUM = re.compile(r"^\d+-\d+$")
FIGCAP = re.compile(r"^Figure\s+\d+-\d+\.")
RUNHEAD = re.compile(r"\s+Chapter\s+\d+\s*$")
LEADHEAD = re.compile(r"^.{0,45}?\s+Chapter\s+\d+\s+")

BOOK_CN = {"general": "通用", "airframe": "机体", "powerplant": "动力装置"}


def read_lines(path):
    return io.open(path, encoding="utf-8", errors="replace").read().splitlines()


def norm(s):
    s = s.lower()
    s = re.sub(r"[^a-z0-9]+", " ", s)
    return re.sub(r"\s+", " ", s).strip()


def page_at(lines, idx):
    for i in range(idx, -1, -1):
        m = PAGE.match(lines[i])
        if m:
            return int(m.group(1))
    return None


def body_paragraphs(lines, start, end, running, tails=()):
    """Rebuild paragraphs, dropping page furniture and repeated headers."""
    raw = []
    for ln in lines[start:end]:
        s = ln.strip()
        if not s:
            raw.append("")
            continue
        if PAGE.match(s) or PAGENUM.match(s) or FIGCAP.match(s):
            continue
        # running header: "<section> Chapter N" or a bare repeat of a title
        if len(s) <= 70 and (RUNHEAD.search(s) or norm(s) in running):
            continue
        # page top repeats only the last words of a long wrapped heading
        if len(s) <= 40 and norm(s) and norm(s) in tails:
            continue
        s = LEADHEAD.sub("", s)
        raw.append(s)

    paras, buf = [], []
    for ln in raw:
        s = ln.rstrip()
        if not s.strip():
            if buf:
                paras.append(" ".join(buf))
                buf = []
            continue
        buf.append(s.strip())
        tail = s.strip()[-1:]
        if not ln.endswith(" ") and tail in ".:!?)]\"'":
            paras.append(" ".join(buf))
            buf = []
    if buf:
        paras.append(" ".join(buf))

    out = []
    for p in paras:
        p = re.sub(r"\s+", " ", p).strip()
        if len(p) >= 20:
            out.append(p)
    return out


def slugify(text):
    s = text.lower()
    s = re.sub(r"[^0-9a-z]+", "-", s)
    return s.strip("-") or "section"


CARD = u"""# {title}

> {book_cn} Ch {ch} · {title} · 原文 PDF 第 {page} 页

## 1. 原文

{original}

## 2. 中文翻译

<!-- TODO: 逐段对应翻译，术语按行业惯例（如 tie-down 系留、fireguard 消防警戒员） -->

## 3. 专业词汇

<!-- TODO: 表格 | 英文 | 词性 | 中文 | 本节语境 |，4~8 条 -->

## 4. 语法解析

<!-- TODO: 2~4 个语法点，每条写「原句 / 拆解 / 要点」 -->
"""


def main(argv):
    book, ch = argv[1], argv[2]
    src = DEFAULT_SRC
    if "--root" in argv:
        src = argv[argv.index("--root") + 1]
    heads_path = argv[argv.index("--headings") + 1]
    out_root = r"F:\AMT-Handbook\cards"
    if "--out" in argv:
        out_root = argv[argv.index("--out") + 1]

    lines = read_lines(os.path.join(src, "%s-ch%s.txt" % (book, ch)))
    heads = json.load(io.open(heads_path, encoding="utf-8"))
    heads.sort(key=lambda h: h["line"])
    if "--skip-first" in argv and heads:
        heads = heads[1:]
    running = set(norm(h["title"]) for h in heads)

    outdir = os.path.join(out_root, book, "ch%s" % ch)
    if not os.path.isdir(outdir):
        os.makedirs(outdir)
    for f in os.listdir(outdir):
        if f.endswith(".md"):
            os.remove(os.path.join(outdir, f))

    made, skipped = 0, []
    for k, h in enumerate(heads):
        start = h["line"] + 1
        end = heads[k + 1]["line"] if k + 1 < len(heads) else len(lines)
        tails = set()
        words = norm(h["title"]).split()
        for k in (2, 3, 4):
            if len(words) >= k:
                tails.add(" ".join(words[-k:]))
        paras = body_paragraphs(lines, start, end, running, tails)
        text = "\n\n".join(paras)
        if len(text) < 220:
            skipped.append((h["title"], len(text)))
            continue
        made += 1
        title = h["title"].strip()
        page = h.get("page") or page_at(lines, h["line"])
        fname = "%02d-%s.md" % (made, slugify(title))
        with io.open(os.path.join(outdir, fname), "w", encoding="utf-8", newline="\n") as f:
            f.write(CARD.format(
                title=title,
                book_cn=BOOK_CN.get(book, book),
                ch=ch,
                page=page,
                original=text,
            ))
    print("%s ch%s -> %d cards, %d skipped" % (book, ch, made, len(skipped)))
    for t, n in skipped:
        print("  skip %-46s %d chars" % (t, n))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
