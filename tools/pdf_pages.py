# -*- coding: utf-8 -*-
"""Extract per-page text from the PDF to jsonl (one {"page":N,"text":...} per line)."""
import sys, io, json
from pypdf import PdfReader

pdf = sys.argv[1]
out = sys.argv[2]
lo = int(sys.argv[3]) if len(sys.argv) > 3 else 1
hi = int(sys.argv[4]) if len(sys.argv) > 4 else 10 ** 9

r = PdfReader(pdf)
n = len(r.pages)
hi = min(hi, n)
with io.open(out, "w", encoding="utf-8", newline="\n") as f:
    for i in range(lo - 1, hi):
        try:
            t = r.pages[i].extract_text() or ""
        except Exception as e:
            t = ""
        f.write(json.dumps({"page": i + 1, "text": t}, ensure_ascii=False) + "\n")
        if (i + 1) % 50 == 0:
            print("...", i + 1, flush=True)
print("done %d-%d of %d" % (lo, hi, n))
