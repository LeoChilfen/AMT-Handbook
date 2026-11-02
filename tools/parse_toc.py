"""Parse the handbook table of contents out of general.pages.jsonl.

The TOC pages give, per chapter, the exact list of red section headings in
reading order plus the printed page (e.g. "Shop Safety ....... 1-1").

Usage:
    python parse_toc.py [--json out.json]
"""
import io
import json
import re
import sys

PAGES = r"C:\Users\Admin\.dsh\docs-index\amt\general.pages.jsonl"
ENTRY = re.compile(r"^(?P<title>.+?)[\s.]*?(?:\.{3,}|…{2,})\s*\.?\s*(?P<page>\d+-\d+)\s*$")
CHAPTER = re.compile(r"^Chapter\s+(\d+)\s*$")


def clean(t):
    t = t.replace("\u2026", "...")
    t = re.sub(r"\s+", " ", t).strip(" .")
    # strip a stray roman front-matter page number glued to the title
    t = re.sub(r"^[ivxlc]{1,5}\s+(?=[A-Z])", "", t)
    return t.strip()


def split_two_column(title, page):
    """The extractor sometimes glues two TOC entries onto one line:
    'Conductors, Insulators, and Semiconductors 12-2 Conductors 12-3'."""
    m = re.search(r"\s(\d+-\d+)\s+(?=[A-Z])", title)
    if not m:
        title = re.sub(r"\.(\d+-\d+)\s+", r" \1 ", title)
        m = re.search(r"\s(\d+-\d+)\s+(?=[A-Z])", title)
    if not m:
        return [(title, page)]
    head = title[:m.start()]
    first_page = m.group(1)
    rest = title[m.end():]
    out = [(head, first_page)]
    m2 = ENTRY.match(rest + " " + page) if not ENTRY.match(rest) else ENTRY.match(rest)
    if m2:
        out.extend(split_two_column(m2.group("title"), m2.group("page")))
    else:
        out.append((rest, page))
    return out


def parse():
    recs = [json.loads(l) for l in io.open(PAGES, encoding="utf-8") if l.strip()]
    by_page = {r["page"]: r["text"] for r in recs}
    chapters = {}
    current = None
    pending = ""
    for pg in sorted(by_page):
        if pg > 24:
            break
        for raw in by_page[pg].splitlines():
            line = raw.rstrip()
            if not line.strip():
                continue
            m = CHAPTER.match(line.strip())
            if m:
                current = int(m.group(1))
                chapters.setdefault(current, [])
                pending = ""
                continue
            if current is None:
                continue
            text = line.strip()
            # rejoin titles wrapped by the extractor: no dot leader => continuation
            if not re.search(r"(\.{3,}|…{2,})", text):
                if pending:
                    text = pending + " " + text
                    pending = ""
                else:
                    pending = text
                    continue
            elif pending:
                text = pending + " " + text
                pending = ""
            m2 = ENTRY.match(text)
            if not m2:
                continue
            chunks = split_two_column(m2.group("title"), m2.group("page"))
            for title, page in chunks:
                title = clean(title)
                if not title or re.match(r"^FAA-H-", title):
                    continue
                chapters[current].append({"title": title, "print_page": page})
    return chapters


def main(argv):
    chs = parse()
    for ch in sorted(chs):
        print("Chapter %d: %d headings" % (ch, len(chs[ch])))
    if "--json" in argv:
        out = argv[argv.index("--json") + 1]
        with io.open(out, "w", encoding="utf-8", newline="\n") as f:
            f.write(json.dumps(chs, ensure_ascii=False, indent=1))
        print("wrote", out)
    ch1 = chs.get(1, [])
    print("--- chapter 1 ---")
    for h in ch1:
        print("  %-60s %s" % (h["title"], h["print_page"]))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
