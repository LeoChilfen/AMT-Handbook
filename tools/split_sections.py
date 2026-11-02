"""Split a chapter .txt (from the AMT PDF extraction) into sections.

The PDF marks section headings in red; the text extraction keeps them as
standalone short title-case lines that are followed by running text.  This
module rebuilds those sections so the card generator has clean input.

Usage:
    python split_sections.py <book> <ch> [--root SRC] [--json out.json]
"""
import io
import json
import os
import re
import sys

PAGE = re.compile(r"^===\s*PDF\s*(\d+)\s*.*===$")
PAGENUM = re.compile(r"^\d+-\d+$")
DEFAULT_ROOT = r"C:\Users\Admin\.dsh\docs-index\amt\_src"


def read_lines(path):
    return io.open(path, encoding="utf-8", errors="replace").read().splitlines()


def is_body_line(line):
    s = line.rstrip()
    return 30 <= len(s.strip()) <= 64 and not PAGENUM.match(s.strip())


def heading_indices(lines):
    """Indices of lines that look like a red section heading."""
    n = len(lines)
    out = []
    for i in range(n):
        s = lines[i]
        if not s or s != s.strip():
            continue
        if len(s) < 3 or len(s) > 46:
            continue
        if PAGE.match(s) or PAGENUM.match(s) or re.match(r"^(Figure|Table)\b", s):
            continue
        if not re.match(r"^[A-Z]", s):
            continue
        if s.endswith((".", ",", ";", ":", "-")):
            continue
        if s.isupper() and len(s.split()) <= 3:
            continue
        j = i + 1
        while j < n and not lines[j].strip():
            j += 1
        if j >= n or PAGE.match(lines[j].strip()):
            continue
        follow_ok = False
        k = j
        for _ in range(3):
            if k >= n:
                break
            if is_body_line(lines[k]):
                follow_ok = True
                break
            k += 1
        if not follow_ok:
            continue
        p = i - 1
        while p >= 0 and not lines[p].strip():
            p -= 1
        if p >= 0:
            prev = lines[p].strip()
            if not (prev.endswith((".", ":", "!", "?")) or len(prev) <= 46):
                continue
        out.append(i)
    return out


def paragraphs(body_lines):
    """Rebuild paragraphs from soft-wrapped lines."""
    paras = []
    buf = []
    for ln in body_lines:
        s = ln.rstrip()
        if not s.strip():
            if buf:
                paras.append(" ".join(buf))
                buf = []
            continue
        buf.append(s.strip())
        if not ln.endswith(" ") and s.strip().endswith((".", ":", "!", "?", ")", "]", '"', "'")):
            paras.append(" ".join(buf))
            buf = []
    if buf:
        paras.append(" ".join(buf))
    cleaned = []
    for p in paras:
        p = re.sub(r"\s+", " ", p).strip()
        if p:
            cleaned.append(p)
    return cleaned


def page_of(lines, idx):
    pg = None
    for i in range(idx, -1, -1):
        m = PAGE.match(lines[i])
        if m:
            pg = int(m.group(1))
            break
    return pg


def split(book, ch, root=DEFAULT_ROOT):
    path = os.path.join(root, "%s-ch%s.txt" % (book, ch))
    lines = read_lines(path)
    heads = heading_indices(lines)
    sections = []
    for k, i in enumerate(heads):
        end = heads[k + 1] if k + 1 < len(heads) else len(lines)
        raw = [l for l in lines[i + 1:end] if not PAGE.match(l.strip())]
        paras = paragraphs(raw)
        text = "\n\n".join(paras)
        sections.append({
            "index": len(sections) + 1,
            "title": lines[i].strip(),
            "page": page_of(lines, i),
            "chars": len(text),
            "paragraphs": paras,
        })
    return sections


def keep(sections, min_chars=200):
    out = []
    for s in sections:
        if s["chars"] < min_chars:
            continue
        if len(s["paragraphs"]) < 2 and s["chars"] < 320:
            continue
        out.append(s)
    for n, s in enumerate(out, 1):
        s["index"] = n
    return out


def main(argv):
    book, ch = argv[1], argv[2]
    root = DEFAULT_ROOT
    if "--root" in argv:
        root = argv[argv.index("--root") + 1]
    secs = keep(split(book, ch, root))
    print("%s ch%s: %d sections" % (book, ch, len(secs)))
    for s in secs:
        print("%3d p%-4s %5d  %s" % (s["index"], s["page"], s["chars"], s["title"]))
    if "--json" in argv:
        out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "sections.json")
        with io.open(out, "w", encoding="utf-8", newline="\n") as f:
            f.write(json.dumps(secs, ensure_ascii=False, indent=1))
        print("wrote", out)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
