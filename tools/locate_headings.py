"""Locate the TOC section headings inside a chapter's extracted text.

TOC (from parse_toc.py) gives the authoritative heading list in order.
This script finds the line offset of each heading in the chapter .txt,
searching forward from the previous hit so duplicates stay ordered.

Usage:
    python locate_headings.py <book> <ch> --toc toc.json [--json out.json]
"""
import io
import json
import os
import re
import sys

DEFAULT_SRC = r"C:\Users\Admin\.dsh\docs-index\amt\_src"
PAGE = re.compile(r"^===\s*PDF\s*(\d+)\s*.*===$")


def norm(s):
    s = s.replace("\u2019", "'").replace("\u201c", '"').replace("\u201d", '"')
    s = s.lower()
    s = re.sub(r"[^a-z0-9]+", " ", s)
    return re.sub(r"\s+", " ", s).strip()


def read_lines(path):
    return io.open(path, encoding="utf-8", errors="replace").read().splitlines()


def find_heading(lines, title, start):
    """Return (index, matched_text) or (None, None)."""
    target = norm(title)
    n = len(lines)
    # 1) single line exact
    for i in range(start, n):
        if norm(lines[i]) == target:
            return i, lines[i].strip()
    # 2) two-line join exact
    for i in range(start, n - 1):
        if norm(lines[i] + " " + lines[i + 1]) == target:
            return i, (lines[i].rstrip() + " " + lines[i + 1].strip())
    # 3) single line starts with the heading's first 6 words and is short
    head_words = target.split()
    if len(head_words) >= 3:
        probe = " ".join(head_words[:6])
        for i in range(start, n):
            line = norm(lines[i])
            if len(lines[i]) > 60:
                continue
            if line and (line == probe or line.startswith(probe)):
                return i, lines[i].strip()
    # 4) last three words of the heading on a short line
    if len(head_words) >= 3:
        tail = " ".join(head_words[-3:])
        for i in range(start, n):
            line = norm(lines[i])
            if len(lines[i]) > 60:
                continue
            if line.endswith(tail):
                return i, lines[i].strip()
    return None, None


def page_at(lines, idx):
    for i in range(idx, -1, -1):
        m = PAGE.match(lines[i])
        if m:
            return int(m.group(1))
    return None


def main(argv):
    book, ch = argv[1], argv[2]
    src = DEFAULT_SRC
    if "--root" in argv:
        src = argv[argv.index("--root") + 1]
    toc_path = argv[argv.index("--toc") + 1]
    toc = json.load(io.open(toc_path, encoding="utf-8"))
    key = str(int(ch[:2])) if ch[:2].isdigit() else ch
    heads = toc.get(key) or toc.get(ch) or []
    if "--start-index" in argv:
        heads = heads[int(argv[argv.index("--start-index") + 1]):]
    lines = read_lines(os.path.join(src, "%s-ch%s.txt" % (book, ch)))

    out, missing = [], []
    pos = 0
    consumed = 0
    stop_at_miss = "--stop-at-miss" in argv
    for h in heads:
        idx, matched = find_heading(lines, h["title"], pos)
        if idx is None:
            # fallback: the TOC wording may differ a little; look anywhere
            idx, matched = find_heading(lines, h["title"], 0)
        if idx is None:
            missing.append(h["title"])
            if stop_at_miss:
                break
            consumed += 1
            continue
        pos = idx + 1
        consumed += 1
        out.append({
            "line": idx,
            "page": page_at(lines, idx),
            "print_page": h.get("print_page"),
            "title": h["title"],
            "matched": matched,
        })
    # de-duplicate by line, keep reading order
    seen = set()
    uniq = []
    for o in out:
        if o["line"] in seen:
            continue
        seen.add(o["line"])
        uniq.append(o)
    uniq.sort(key=lambda o: o["line"])
    out = uniq
    print("%s ch%s: %d/%d headings located (consumed %d)" % (book, ch, len(out), len(heads), consumed))
    for m in missing:
        print("  MISS  " + m)
    if "--json" in argv:
        path = argv[argv.index("--json") + 1]
        with io.open(path, "w", encoding="utf-8", newline="\n") as f:
            f.write(json.dumps(out, ensure_ascii=False, indent=1))
        print("wrote", path)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
