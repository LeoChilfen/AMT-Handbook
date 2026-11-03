# -*- coding: utf-8 -*-
"""Split a chapter of the PDF into sections using the PDF outline (bookmarks).

Usage:
  python pdf_sections.py --outline outline.json --pages pages.jsonl \
         --chapter 1 --json ch01-sections.json [--min-chars 200]

Output JSON: [{"seq","title","depth","page","text"}]
"""
import sys, io, json, re, argparse

PAGE_NUM = re.compile(r"^\s*\d+-\d+\s*$")
FIGCAP = re.compile(r"^Figure\s+\d+-\d+\.", re.I)


def norm_map(raw):
    """lowercase + collapse whitespace, keeping a map back to raw indices."""
    out = []
    idx = []
    prev_space = True
    for i, ch in enumerate(raw):
        if ch in " \t\r\n":
            if prev_space:
                continue
            out.append(" ")
            idx.append(i)
            prev_space = True
        else:
            out.append(ch.lower())
            idx.append(i)
            prev_space = False
    return "".join(out), idx


def find_title(norm, title, start):
    nt = re.sub(r"\s+", " ", title.strip().lower())
    nt = re.sub(r"[^a-z0-9 &/(),.'\-:]", " ", nt)
    nt = re.sub(r"\s+", " ", nt).strip()
    if not nt:
        return None
    candidates = [nt]
    words = nt.split()
    if len(words) > 6:
        candidates.append(" ".join(words[:6]))
    if len(words) > 3:
        candidates.append(" ".join(words[-3:]))
    for c in candidates:
        p = norm.find(c, start)
        if p != -1:
            return p, p + len(c)
    return None


def clean_body(raw):
    """Return paragraph list.

    In this PDF a *wrapped* line ends with a trailing space; a paragraph's last
    line does not. That is the only reliable paragraph signal available.
    """
    paras = []
    buf = []

    def flush():
        if buf:
            paras.append(re.sub(r"\s+", " ", " ".join(buf)).strip())
            del buf[:]

    for line in raw.split("\n"):
        core = line.strip()
        wrapped = line.endswith(" ")
        if not core:
            flush()
            continue
        if PAGE_NUM.match(core) or FIGCAP.match(core):
            flush()
            continue
        if core.startswith(("•", "·")):
            flush()
            buf.append(core)
            flush()
            continue
        buf.append(core)
        if not wrapped:
            flush()
    flush()
    merged = []
    for p in paras:
        if not p:
            continue
        if merged and not re.search(r"[.!?:;”\"')\]]$", merged[-1]) \
                and not p.startswith(("•", "·")):
            merged[-1] = merged[-1] + " " + p
        else:
            merged.append(p)
    return merged


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--outline", required=True)
    ap.add_argument("--pages", required=True)
    ap.add_argument("--chapter", required=True)
    ap.add_argument("--json", required=True)
    ap.add_argument("--min-chars", type=int, default=200)
    ap.add_argument("--level", type=int, default=0, help="1 = only second-level entries (chapter's direct children)")
    a = ap.parse_args()

    rows = json.load(io.open(a.outline, encoding="utf-8"))
    pages = {}
    for line in io.open(a.pages, encoding="utf-8"):
        if line.strip():
            r = json.loads(line)
            pages[r["page"]] = r["text"]

    # chapter boundaries from depth-0 entries that look like "N. Title"
    chapters = []
    for x in rows:
        if x["depth"] == 0 and re.match(r"^\d+\.\s", x["title"]):
            chapters.append(x)
    cur = None
    nxt = None
    for i, c in enumerate(chapters):
        if c["title"].startswith(a.chapter + "."):
            cur = c
            nxt = chapters[i + 1] if i + 1 < len(chapters) else None
            break
    if not cur:
        sys.exit("chapter not found")

    p0 = cur["page"]
    p1 = (nxt["page"] if nxt else max(pages) + 1)
    last = max(pages)
    p1 = min(p1, last + 1)

    # headings belonging to this chapter, in outline order
    heads = []
    inside = False
    for x in rows:
        if x["depth"] == 0:
            inside = (x is cur) or (x["title"] == cur["title"] and x["page"] == p0)
            continue
        if inside and x["page"] and p0 <= x["page"] < p1:
            # relative depth under the chapter
            heads.append({"title": x["title"], "page": x["page"], "depth": x["depth"]})

    raw = "\n".join(pages.get(p, "") for p in range(p0, p1))
    offsets = []
    off = 0
    for p in range(p0, p1):
        offsets.append(off)
        off += len(pages.get(p, "")) + 1
    norm, idx = norm_map(raw)

    found = []
    cursor = 0
    for h in heads:
        r = find_title(norm, h["title"], cursor)
        if not r:
            found.append({"title": h["title"], "page": h["page"], "depth": h["depth"],
                          "start": None, "end": None})
            continue
        s, e = r
        found.append({"title": h["title"], "page": h["page"], "depth": h["depth"],
                      "start": idx[s], "end": idx[e]})
        cursor = e

    miss = [h["title"] for h in found if h["start"] is None]
    # which located headings become their own card?
    kept = [i for i, h in enumerate(found)
            if h["start"] is not None and (not a.level or h["depth"] == a.level)]

    out = []
    seq = 0
    for pos, i in enumerate(kept):
        h = found[i]
        nxt_i = kept[pos + 1] if pos + 1 < len(kept) else None
        body_end = found[nxt_i]["start"] if nxt_i is not None else len(raw)
        # deeper headings inside this section -> bold separators
        subs = [found[j] for j in range(i + 1, nxt_i if nxt_i is not None else len(found))
                if found[j]["start"] is not None and h["end"] <= found[j]["start"] < body_end]
        paras = []
        cur = h["end"]
        for s in subs:
            if s["start"] < cur:
                continue
            paras += clean_body(raw[cur:s["start"]])
            paras.append("**%s**" % s["title"].strip())
            cur = s["end"]
        paras += clean_body(raw[cur:body_end])
        total = sum(len(p) for p in paras)
        if total < a.min_chars:
            continue
        seq += 1
        out.append({"seq": seq, "title": h["title"].strip(), "depth": h["depth"],
                    "page": h["page"], "paras": paras})

    json.dump(out, io.open(a.json, "w", encoding="utf-8", newline="\n"),
              ensure_ascii=False, indent=1)
    print("chapter pages: %d-%d" % (p0, p1 - 1))
    print("outline entries: %d, located: %d, missing: %d, sections kept: %d"
          % (len(found), len([f for f in found if f["start"] is not None]),
             len(miss), len(out)))
    if miss:
        print("MISS:", "; ".join(miss[:12]))
    for s in out[:12]:
        print("  %2d  p%-4s %-58s %d paras %d chars"
              % (s["seq"], s["page"], s["title"][:58], len(s["paras"]),
                 sum(len(p) for p in s["paras"])))


if __name__ == "__main__":
    main()
