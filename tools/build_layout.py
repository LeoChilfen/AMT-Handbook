# -*- coding: utf-8 -*-
"""把 PDF 每页按两栏正确阅读顺序重建为纯文本，供“段落顺序校准”使用。"""
import io, re, json, sys
from pypdf import PdfReader

PDF = r"D:\Documents\1常用\2工作\广州飞机维修工程有限公司\TECC\资料\AMT Handbook-General2023.pdf"
OUT = r"C:\Users\Admin\.dsh\whale-work\tmp\layout_pages.jsonl"
GAP = re.compile(r"[ \t]{3,}")

def deinterleave(text):
    left, right, full = [], [], []
    for ln in text.split("\n"):
        raw = ln.rstrip()
        if not raw.strip():
            continue
        indent = len(raw) - len(raw.lstrip())
        chunks = [c for c in GAP.split(raw.strip()) if c.strip()]
        if len(chunks) >= 2:
            left.append(chunks[0])
            right.append(chunks[-1])
        elif indent >= 20:
            right.append(raw.strip())
        else:
            full.append(raw.strip())
    return left, right, full

r = PdfReader(PDF)
n = len(r.pages)
out = io.open(OUT, "w", encoding="utf-8", newline="\n")
for i in range(n):
    try:
        lay = r.pages[i].extract_text(extraction_mode="layout") or ""
    except Exception as e:
        lay = ""
    left, right, full = deinterleave(lay)
    body = "\n".join(full + left + right)
    out.write(json.dumps({"page": i + 1, "text": body}, ensure_ascii=False) + "\n")
    if (i + 1) % 50 == 0:
        print("page", i + 1, "/", n, file=sys.stderr)
out.close()
print("done", n)
