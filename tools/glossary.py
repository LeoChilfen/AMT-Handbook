# -*- coding: utf-8 -*-
"""Extract the Glossary entries (term + definition) from the pages jsonl."""
import sys, io, json, re

pages_path = sys.argv[1]
out_path = sys.argv[2]
lo = int(sys.argv[3]) if len(sys.argv) > 3 else 657
hi = int(sys.argv[4]) if len(sys.argv) > 4 else 667

pages = {}
for line in io.open(pages_path, encoding="utf-8"):
    if line.strip():
        r = json.loads(line)
        pages[r["page"]] = r["text"]

raw = "\n".join(pages.get(p, "") for p in range(lo, hi + 1))

paras = []
buf = []
for line in raw.split("\n"):
    core = line.strip()
    wrapped = line.endswith(" ")
    if not core:
        if buf:
            paras.append(" ".join(buf))
            buf = []
        continue
    if re.match(r"^G-\d+$", core) or re.match(r"^[A-Z]$", core):
        if buf:
            paras.append(" ".join(buf))
            buf = []
        continue
    buf.append(core)
    if not wrapped:
        paras.append(" ".join(buf))
        buf = []
if buf:
    paras.append(" ".join(buf))

entries = []
for p in paras:
    p = re.sub(r"\s+", " ", p).strip()
    m = re.match(r"^([A-Z][^.]{1,80}?)\.\s+(.{10,})$", p)
    if m:
        entries.append({"term": m.group(1).strip(), "def": m.group(2).strip()})
    elif entries and len(p) > 0:
        # continuation of the previous entry
        entries[-1]["def"] = (entries[-1]["def"] + " " + p).strip()

json.dump(entries, io.open(out_path, "w", encoding="utf-8", newline="\n"),
          ensure_ascii=False, indent=1)
print("glossary entries:", len(entries))
for e in entries[:8]:
    print(" -", e["term"], "|", e["def"][:70])
