# -*- coding: utf-8 -*-
"""按 PDF 书签顺序 + 两栏阅读顺序重排卡片段落（中英同步，索引守恒）。"""
import io, json, re, os, glob

PAGES = [json.loads(l) for l in io.open(r"C:\Users\Admin\.dsh\whale-work\tmp\layout_pages.jsonl", encoding="utf-8")]
OUTLINE = json.load(io.open(r"C:\Users\Admin\.dsh\whale-work\tmp\outline-general2023.json", encoding="utf-8"))
ROOT = r"F:\AMT-Handbook\cards\general"
APPLY = False

def norm(s):
    return re.sub(r"[^a-z0-9]", "", s.lower())

def part_no(s):
    m = re.search(r"part\s*(\d{1,3})", s, re.I)
    return m.group(1) if m else None

def window_text(lo, hi):
    return norm("\n".join(p["text"] for p in PAGES if lo <= p["page"] <= hi))

def key_of(t):
    k = re.sub(r"^#+\s*", "", t).strip()
    k = re.sub(r"^\d{1,2}\.\s*", "", k)
    return norm(k)

def candidates(nt, k):
    out, start = [], 0
    if len(k) < 12:
        return out
    while len(out) < 8:
        j = nt.find(k[:60], start)
        if j < 0:
            j = nt.find(k[:30], start)
        if j < 0:
            break
        out.append(j)
        start = j + 1
    return out

def order_within(items, nt):
    """items: [(原索引, 文本)] -> 按版面位置排序后的原索引列表"""
    cursor, pos = 0, []
    for _, t in items:
        cs = candidates(nt, key_of(t))
        if not cs:
            pos.append(None); continue
        nxt = [c for c in cs if c >= cursor]
        brief = bool(re.match(r"^(#|\d{1,2}\.|•)", t.strip()))
        limit = 1500 if brief else 6000
        cand = None
        for c in nxt:
            if c - cursor <= limit:
                cand = c
                break
        if cand is None and nxt and not brief:
            cand = nxt[0]
        if cand is None:
            pos.append(None); continue
        cursor = max(cursor, cand)
        pos.append(cand)
    filled, last = [], -1.0
    for p in pos:
        if p is None:
            last += 0.0001
            filled.append(last)
        else:
            filled.append(p); last = float(p)
    order = sorted(range(len(items)), key=lambda x: (filled[x], x))
    return [items[x][0] for x in order], sum(1 for p in pos if p is not None)

def outline_titles(lo, hi):
    out = []
    for it in OUTLINE:
        pg = it.get("page")
        if pg is None or not (lo <= pg <= hi):
            continue
        if it.get("depth", 0) >= 1:
            out.append(it["title"])
    return out

def rank_of(head, titles):
    if not head:
        return None
    h = re.sub(r"^#+\s*", "", head)
    pn = part_no(h)
    if pn:
        for n, t in enumerate(titles):
            if part_no(t) == pn:
                return n
    key = norm(h)
    for n, t in enumerate(titles):
        ot = norm(t)
        if key and (key == ot or key in ot or ot in key):
            return n
    return None

def reorder(path, lo, hi):
    t = io.open(path, encoding="utf-8").read()
    i, j, k = t.find("## 1. "), t.find("## 2. "), t.find("## 3. ")
    if min(i, j, k) < 0:
        return ("NOSTRUCT", path)
    head, en, zh, tail = t[:i], t[i:j], t[j:k], t[k:]
    en_p = [x.strip() for x in en.split("\n\n") if x.strip()][1:]
    zh_p = [x.strip() for x in zh.split("\n\n") if x.strip()][1:]
    if len(en_p) != len(zh_p):
        return ("PARITY", path, len(en_p), len(zh_p))

    blocks, cur = [], None
    for idx, x in enumerate(en_p):
        if x.startswith("#"):
            cur = {"head": (idx, x), "items": []}
            blocks.append(cur)
        else:
            if cur is None:
                cur = {"head": None, "items": []}
                blocks.append(cur)
            cur["items"].append((idx, x))

    titles = outline_titles(lo, hi)
    ranks, last = [], -0.5
    for b in blocks:
        r = rank_of(b["head"][1] if b["head"] else None, titles)
        if r is None:
            last += 0.5
            ranks.append(last)
        else:
            last = float(r)
            ranks.append(last)

    nt = window_text(lo, hi)
    new_idx, known, total = [], 0, 0
    for x in sorted(range(len(blocks)), key=lambda n: (ranks[n], n)):
        b = blocks[x]
        if b["head"]:
            new_idx.append(b["head"][0])
        if b["items"]:
            o, kn = order_within(b["items"], nt)
            known += kn; total += len(b["items"])
            new_idx.extend(o)
    if len(new_idx) != len(en_p) or sorted(new_idx) != list(range(len(en_p))):
        return ("BADIDX", path, len(new_idx), len(en_p))
    if new_idx == list(range(len(en_p))):
        return ("SAME", path)
    if APPLY:
        new = (head + "## 1. 原文\n\n" + "\n\n".join(en_p[x] for x in new_idx) + "\n\n"
               + "## 2. 中文翻译\n\n" + "\n\n".join(zh_p[x] for x in new_idx) + "\n\n" + tail.lstrip("\n"))
        io.open(path, "w", encoding="utf-8", newline="\n").write(new)
    return ("MOVED", path, known, total)
