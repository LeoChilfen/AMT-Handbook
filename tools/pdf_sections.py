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


def _norm_text(s):
    """lowercase, map every non [a-z0-9] run to a single space (both sides)."""
    return re.sub(r"[^a-z0-9]+", " ", s.lower()).strip()


def norm_map(raw):
    """normalised text + map back to raw indices.

    Punctuation is folded to spaces exactly like _norm_text() so that bookmark
    titles containing em dashes / semicolons still match the page text.
    """
    out = []
    idx = []
    prev_space = True
    for i, ch in enumerate(raw):
        low = ch.lower()
        if low.isalnum() and low.isascii():
            out.append(low)
            idx.append(i)
            prev_space = False
        else:
            if prev_space:
                continue
            out.append(" ")
            idx.append(i)
            prev_space = True
    return "".join(out), idx


def find_title(raw, norm, idx, title, start):
    """Find a bookmark title in the normalised text, preferring a line start.

    Two wrinkles of this PDF:
    * the chapter heading line itself often contains words that are also
      section titles (e.g. "…, Maintenance Forms, Records, & Publications"), so
      a plain substring hit must be rejected — real headings start a line;
    * the reader re-ordered pages by hand, so bookmark order and page order do
      not always agree. Therefore: first look at/after `start`, and only if that
      fails fall back to the first line-start hit anywhere (out-of-order page).
    """
    nt = _norm_text(title)
    if not nt:
        return None
    candidates = [nt]
    words = nt.split()
    if len(words) > 6:
        candidates.append(" ".join(words[:6]))
    if len(words) > 3:
        candidates.append(" ".join(words[-3:]))
    for c in candidates:
        first_any = None
        pos = 0
        while True:
            p = norm.find(c, pos)
            if p == -1:
                break
            rp = idx[p]
            if rp == 0 or raw[rp - 1] == "\n":
                if first_any is None:
                    first_any = (p, p + len(c))
                if p >= start:
                    return p, p + len(c)
            pos = p + 1
        if first_any is not None:
            return first_any
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
    # chapter boundaries: a numbered depth-0 entry starts a chapter, but the
    # chapter ends at the *next* depth-0 entry of any kind (Glossary / Index are
    # not numbered — without this the last chapter swallows them).
    top = [x for x in rows if x["depth"] == 0]
    numbered = [x for x in top if re.match(r"^\d+\.\s", x["title"])]
    cur = None
    nxt = None
    for i, c in enumerate(numbered):
        if c["title"].startswith(a.chapter + "."):
            cur = c
            j = top.index(c)
            nxt = top[j + 1] if j + 1 < len(top) else None
            break
    if not cur:
        sys.exit("chapter not found")

    p0 = cur["page"]
    p1 = (nxt["page"] if nxt and nxt["page"] > p0 else max(pages) + 1)
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
        r = find_title(raw, norm, idx, h["title"], cursor)
        if not r:
            found.append({"title": h["title"], "page": h["page"], "depth": h["depth"],
                          "start": None, "end": None})
            continue
        s, e = r
        found.append({"title": h["title"], "page": h["page"], "depth": h["depth"],
                      "start": idx[s], "end": idx[e]})
        cursor = e

    miss = [h["title"] for h in found if h["start"] is None]

    # Document order, not bookmark order: the pages were re-ordered by hand, and
    # a section body may only ever run from its own heading to the *nearest*
    # following heading in the text. Sorting also removes overlaps that the
    # out-of-order fallback in find_title() can introduce.
    located = [h for h in found if h["start"] is not None]
    located.sort(key=lambda h: (h["start"], h["end"]))

    # drop duplicate hits (same start) — keep the first, but never two headings
    # starting at the same offset
    dedup = []
    for h in located:
        if dedup and h["start"] <= dedup[-1]["end"]:
            continue
        dedup.append(h)
    located = dedup

    # which located headings get their own card?
    kept = [h for h in located if not a.level or h["depth"] == a.level]

    out = []
    seq = 0
    for pos, h in enumerate(kept):
        body_end = kept[pos + 1]["start"] if pos + 1 < len(kept) else len(raw)
        subs = [s for s in located
                if h["end"] <= s["start"] < body_end and s is not h]
        paras = []
        cur = h["end"]
        for s in subs:
            if s["start"] < cur:
                continue
            paras += clean_body(raw[cur:s["start"]])
            paras.append("#" * min(s["depth"] + 1, 6) + " " + s["title"].strip())
            cur = max(cur, s["end"])
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
