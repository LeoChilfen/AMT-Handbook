# -*- coding: utf-8 -*-
"""Dump PDF outline (bookmarks) as a nested list with page numbers."""
import sys, json, io
from pypdf import PdfReader

pdf = sys.argv[1]
out = sys.argv[2] if len(sys.argv) > 2 else None
r = PdfReader(pdf)
n = len(r.pages)
print("pages:", n)
print("has outline:", bool(r.outline))

rows = []

def page_no(dest):
    try:
        return r.get_destination_page_number(dest) + 1
    except Exception:
        return None

def walk(items, depth):
    for it in items:
        if isinstance(it, list):
            walk(it, depth + 1)
        else:
            try:
                title = it.title
            except Exception:
                title = str(it)
            p = page_no(it)
            rows.append({"depth": depth, "title": title, "page": p})

if r.outline:
    walk(r.outline, 0)

print("entries:", len(rows))
for x in rows[:60]:
    print("%s%-70s p%s" % ("  " * x["depth"], x["title"][:70], x["page"]))

if out:
    with io.open(out, "w", encoding="utf-8", newline="\n") as f:
        json.dump(rows, f, ensure_ascii=False, indent=1)
    print("written:", out)
