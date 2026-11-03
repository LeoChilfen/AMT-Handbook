"""Build the AMT-Handbook static site into docs/.

No third-party dependencies: a small markdown renderer tailored to the note
format (headings, tables, lists, blockquotes, fenced code, bold/italic/inline
code/links) plus a hand-written shell page.

Usage:
    python build_site.py <repo-root>
"""
import hashlib
import io
import json
import os
import re
import sys

BOOKS = [
    ("general", "General", "通用", 15),
    ("airframe", "Airframe", "机体", 18),
    ("powerplant", "Powerplant", "动力装置", 11),
]

# ---------------------------------------------------------------- inline ----

LINK_MAP = {}


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def rewrite_url(url):
    m = re.match(r"^notes/([a-z]+)/(ch[0-9]+[ab]?)\.md$", url)
    if m:
        return "#/" + m.group(1) + "-" + m.group(2)
    if url in ("INDEX.md", "./INDEX.md"):
        return "#/index"
    if url in ("README.md", "./README.md"):
        return "#/"
    if re.match(r"^notes/[a-z]+/?$", url):
        return "#/index"
    return url


def inline(s):
    stash = []

    def put(html):
        stash.append(html)
        return "\x00%d\x00" % (len(stash) - 1)

    s = re.sub(r"`([^`]+)`", lambda m: put("<code>" + esc(m.group(1)) + "</code>"), s)
    s = esc(s)
    s = re.sub(
        r"!\[([^\]]*)\]\(([^)\s]+)\)",
        lambda m: put('<img src="%s" alt="%s">' % (rewrite_url(m.group(2)), esc(m.group(1)))),
        s,
    )
    s = re.sub(
        r"\[([^\]]+)\]\(([^)\s]+)\)",
        lambda m: put('<a href="%s">%s</a>' % (rewrite_url(m.group(2)), m.group(1))),
        s,
    )
    s = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"(?<![\w*])\*([^*\s][^*]*)\*(?![\w*])", r"<em>\1</em>", s)
    s = re.sub(r"(?<!\w)__([^_]+)__(?!\w)", r"<strong>\1</strong>", s)

    def back(m):
        return stash[int(m.group(1))]

    return re.sub(r"\x00(\d+)\x00", back, s)


# ---------------------------------------------------------------- blocks ----

def slugify_heading(text, used):
    base = re.sub(r"[^0-9A-Za-z\u4e00-\u9fff]+", "-", text).strip("-").lower()
    if not base:
        base = "sec"
    slug = base
    n = 2
    while slug in used:
        slug = "%s-%d" % (base, n)
        n += 1
    used.add(slug)
    return slug


def split_row(line):
    line = line.strip()
    if line.startswith("|"):
        line = line[1:]
    if line.endswith("|"):
        line = line[:-1]
    return [c.strip() for c in line.split("|")]


def render_markdown(text):
    lines = text.splitlines()
    out = []
    headings = []
    used = set()
    i = 0
    n = len(lines)

    while i < n:
        line = lines[i]
        stripped = line.strip()

        if not stripped:
            i += 1
            continue

        # fenced code
        if stripped.startswith("```"):
            lang = stripped[3:].strip()
            i += 1
            buf = []
            while i < n and not lines[i].strip().startswith("```"):
                buf.append(lines[i])
                i += 1
            i += 1
            cls = ' class="language-%s"' % esc(lang) if lang else ""
            out.append("<pre><code%s>%s</code></pre>" % (cls, esc("\n".join(buf))))
            continue

        # heading
        m = re.match(r"^(#{1,6})\s+(.*)$", stripped)
        if m:
            level = len(m.group(1))
            text_ = m.group(2).strip()
            hid = slugify_heading(re.sub(r"`", "", text_), used)
            if level == 2:
                headings.append((hid, text_))
            out.append('<h%d id="%s">%s</h%d>' % (level, hid, inline(text_), level))
            i += 1
            continue

        # horizontal rule
        if re.match(r"^(-{3,}|\*{3,}|_{3,})$", stripped):
            out.append("<hr>")
            i += 1
            continue

        # table
        if stripped.startswith("|") and i + 1 < n and re.match(
            r"^\|?\s*:?-{2,}", lines[i + 1].strip()
        ):
            header = split_row(stripped)
            aligns = []
            for cell in split_row(lines[i + 1]):
                if cell.startswith(":") and cell.endswith(":"):
                    aligns.append("center")
                elif cell.endswith(":"):
                    aligns.append("right")
                else:
                    aligns.append("left")
            i += 2
            rows = []
            while i < n and lines[i].strip().startswith("|"):
                rows.append(split_row(lines[i]))
                i += 1
            out.append('<div class="table-wrap"><table>')
            out.append("<thead><tr>")
            for k, cell in enumerate(header):
                al = aligns[k] if k < len(aligns) else "left"
                out.append('<th style="text-align:%s">%s</th>' % (al, inline(cell)))
            out.append("</tr></thead><tbody>")
            for row in rows:
                out.append("<tr>")
                for k, cell in enumerate(row):
                    al = aligns[k] if k < len(aligns) else "left"
                    out.append('<td style="text-align:%s">%s</td>' % (al, inline(cell)))
                out.append("</tr>")
            out.append("</tbody></table></div>")
            continue

        # blockquote
        if stripped.startswith(">"):
            buf = []
            while i < n and lines[i].strip().startswith(">"):
                buf.append(lines[i].strip()[1:].strip())
                i += 1
            out.append("<blockquote>%s</blockquote>" % inline(" ".join(buf)))
            continue

        # lists
        if re.match(r"^([-*+])\s+", stripped):
            items = []
            while i < n and re.match(r"^([-*+])\s+", lines[i].strip()):
                items.append(re.sub(r"^([-*+])\s+", "", lines[i].strip()))
                i += 1
            out.append("<ul>%s</ul>" % "".join("<li>%s</li>" % inline(t) for t in items))
            continue

        if re.match(r"^\d+[.)]\s+", stripped):
            items = []
            start = int(re.match(r"^(\d+)[.)]\s+", stripped).group(1))
            while i < n and re.match(r"^\d+[.)]\s+", lines[i].strip()):
                items.append(re.sub(r"^\d+[.)]\s+", "", lines[i].strip()))
                i += 1
            attr = ' start="%d"' % start if start > 1 else ""
            out.append("<ol%s>%s</ol>" % (attr, "".join("<li>%s</li>" % inline(t) for t in items)))
            continue

        # paragraph
        buf = []
        while i < n:
            cur = lines[i].strip()
            if not cur:
                break
            if re.match(r"^(#{1,6})\s", cur) or cur.startswith("```") or cur.startswith("|") \
                    or cur.startswith(">") or re.match(r"^([-*+])\s+", cur) or re.match(r"^\d+[.)]\s+", cur) \
                    or re.match(r"^(-{3,}|\*{3,}|_{3,})$", cur):
                break
            buf.append(cur)
            i += 1
        if buf and buf[0].startswith("•"):
            # 项目符号段落：后续紧跟的行是该条目的续行，换行但保持悬挂缩进
            out.append('<p class="bullet">%s</p>' % "<br>".join(inline(x) for x in buf))
        else:
            out.append("<p>%s</p>" % inline(" ".join(buf)))

    return "\n".join(out), headings


# ----------------------------------------------------------------- data -----

def chapter_key(num):
    m = re.match(r"^(\d+)([ab]?)$", num)
    return (int(m.group(1)), m.group(2))


def read(path):
    with io.open(path, encoding="utf-8") as f:
        return f.read()


def parse_title(text, fallback):
    """Return (part, english_title, chinese_title).

    Handles both "# Ch 12 · Title（中文）" and "# Ch 12（上） · Title（中文）".
    """
    for line in text.splitlines():
        if line.startswith("# "):
            raw = line[2:].strip()
            m = re.match(r"^Ch\s*(\d+)\s*([（(][^）)]*[）)])?\s*[·・]\s*(.*)$", raw)
            if m:
                part = (m.group(2) or "").strip("（）() ")
                rest = m.group(3)
            else:
                part, rest = "", raw
            # trailing "（…）" may itself contain nested parens, e.g.
            # "Aircraft Fabric Covering（飞机蒙布（织物）覆盖）"
            open_at = -1
            if rest and rest[-1] in "）)":
                depth = 0
                for i in range(len(rest) - 1, -1, -1):
                    ch = rest[i]
                    if ch in "）)":
                        depth += 1
                    elif ch in "（(":
                        depth -= 1
                        if depth == 0:
                            open_at = i
                            break
            if open_at > 0:
                return part, rest[:open_at].strip(), rest[open_at + 1:-1].strip()
            return part, rest.strip(), ""
    return "", fallback, ""


def main():
    root = sys.argv[1] if len(sys.argv) > 1 else "."
    notes_dir = os.path.join(root, "notes")
    docs = os.path.join(root, "docs")
    pages = os.path.join(docs, "pages")
    assets = os.path.join(docs, "assets")
    for d in (docs, pages, assets):
        if not os.path.isdir(d):
            os.makedirs(d)
    for f in os.listdir(pages):
        if f.endswith(".html"):
            os.remove(os.path.join(pages, f))

    manifest = []
    for book_slug, book_en, book_zh, _count in BOOKS:
        folder = os.path.join(notes_dir, book_slug)
        files = [f for f in os.listdir(folder) if f.endswith(".md")]
        files.sort(key=lambda f: chapter_key(f[2:-3]))
        for fname in files:
            num = fname[2:-3]
            path = os.path.join(folder, fname)
            text = read(path)
            part, title_en, title_zh = parse_title(text, fname)
            if part:
                part_en = {"上": "Part 1", "下": "Part 2", "前半": "Part 1", "后半": "Part 2"}.get(part, part)
                title_en = (title_en + " (" + part_en + ")").strip()
            slug = "%s-ch%s" % (book_slug, num)
            body, headings = render_markdown(text)
            manifest.append(
                {
                    "slug": slug,
                    "book": book_slug,
                    "bookEn": book_en,
                    "bookZh": book_zh,
                    "num": num,
                    "titleEn": title_en,
                    "titleZh": title_zh,
                    "headings": [{"id": h, "text": t} for h, t in headings],
                }
            )
            with io.open(os.path.join(pages, slug + ".html"), "w", encoding="utf-8", newline="\n") as f:
                f.write(body)

    # ---- index page content (parsed from INDEX.md summaries) ----
    index_md = read(os.path.join(root, "INDEX.md")) if os.path.exists(os.path.join(root, "INDEX.md")) else ""
    summaries = {}
    for line in index_md.splitlines():
        m = re.search(r"\]\(notes/([a-z]+/ch[0-9]+[ab]?)\.md\)", line)
        if not m or not line.strip().startswith("|"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        summaries[m.group(1)] = cells[-1] if cells else ""
    for item in manifest:
        item["summary"] = summaries.get("%s/ch%s" % (item["book"], item["num"]), "")

    groups = []
    for book_slug, book_en, book_zh, _c in BOOKS:
        chapters = [it for it in manifest if it["book"] == book_slug]
        groups.append(
            {"slug": book_slug, "en": book_en, "zh": book_zh, "count": len(chapters), "chapters": chapters}
        )

    # ---- study cards (cards/<book>/ch<NN>/<seq>-<slug>.md) ----
    cards_root = os.path.join(root, "cards")
    cards_dir = os.path.join(docs, "cards")
    if not os.path.isdir(cards_dir):
        os.makedirs(cards_dir)
    for f in os.listdir(cards_dir):
        if f.endswith(".html"):
            os.remove(os.path.join(cards_dir, f))

    card_sets = []
    if os.path.isdir(cards_root):
        for book_slug, book_en, book_zh, _c in BOOKS:
            book_dir = os.path.join(cards_root, book_slug)
            if not os.path.isdir(book_dir):
                continue
            chdirs = [d for d in os.listdir(book_dir) if os.path.isdir(os.path.join(book_dir, d))]
            chdirs.sort(key=lambda d: chapter_key(d[2:]))
            for chname in chdirs:
                num = chname[2:]
                chapter_slug = "%s-ch%s" % (book_slug, num)
                src_dir = os.path.join(book_dir, chname)
                files = [f for f in os.listdir(src_dir) if f.endswith(".md")]
                files.sort()
                cards = []
                for fname in files:
                    text = read(os.path.join(src_dir, fname))
                    # 未填完的卡片（还有 TODO 占位）先不上站
                    if "TODO" in text:
                        continue
                    first = ""
                    for line in text.splitlines():
                        if line.startswith("# "):
                            first = line[2:].strip()
                            break
                    seq = fname.split("-")[0]
                    slug = "%s-%s" % (chapter_slug, seq)
                    body, _h = render_markdown(text)
                    with io.open(os.path.join(cards_dir, slug + ".html"), "w", encoding="utf-8", newline="\n") as f:
                        f.write(body)
                    cards.append({"slug": slug, "seq": seq, "title": first or fname, "file": fname})
                if not cards:
                    continue
                chapter = next((it for it in manifest if it["slug"] == chapter_slug), None)
                if chapter is None:
                    # split chapters (ch12a / ch12b) live in one card folder
                    chapter = next((it for it in manifest
                                    if it["slug"].startswith(chapter_slug + "a")
                                    or it["slug"].startswith(chapter_slug + "b")), None)
                title_en = chapter["titleEn"] if chapter else "Ch " + num
                if chapter and chapter["slug"] != chapter_slug:
                    # split chapter (ch12 -> ch12a): the card folder spans both parts
                    title_en = re.sub(r"\s*\(Part\s*\d+\)\s*$", "", title_en)
                card_sets.append({
                    "chapter": chapter_slug,
                    "book": book_slug,
                    "bookEn": book_en,
                    "bookZh": book_zh,
                    "num": num,
                    "titleEn": title_en,
                    "count": len(cards),
                    "cards": cards,
                })

    with io.open(os.path.join(docs, "data.js"), "w", encoding="utf-8", newline="\n") as f:
        f.write("window.AMT_DATA = " + json.dumps(groups, ensure_ascii=False, indent=1) + ";\n")
        f.write("window.AMT_CARDS = " + json.dumps(card_sets, ensure_ascii=False, indent=1) + ";\n")

    write_assets(assets)
    write_shell(docs, groups)

    total = len(manifest)
    print("chapters: %d" % total)
    for g in groups:
        print("  %-12s %2d" % (g["slug"], g["count"]))
    print("pages: %d files" % len(os.listdir(pages)))
    return 0


def write_assets(assets):
    with io.open(os.path.join(assets, "style.css"), "w", encoding="utf-8", newline="\n") as f:
        f.write(CSS)
    with io.open(os.path.join(assets, "app.js"), "w", encoding="utf-8", newline="\n") as f:
        f.write(JS)


def _asset_version(path):
    """Short content hash used as a cache-busting query string."""
    h = hashlib.md5()
    with io.open(path, "rb") as f:
        h.update(f.read())
    return h.hexdigest()[:8]


def write_shell(docs, groups):
    assets = os.path.join(docs, "assets")
    html = HTML_SHELL
    html = html.replace("__CSS__", _asset_version(os.path.join(assets, "style.css")))
    html = html.replace("__DATA__", _asset_version(os.path.join(docs, "data.js")))
    html = html.replace("__APP__", _asset_version(os.path.join(assets, "app.js")))
    with io.open(os.path.join(docs, "index.html"), "w", encoding="utf-8", newline="\n") as f:
        f.write(html)
    with io.open(os.path.join(docs, ".nojekyll"), "w", encoding="utf-8", newline="\n") as f:
        f.write("")


HTML_SHELL = r"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>AMT Handbook · 中文笔记</title>
<meta name="description" content="FAA AMT Handbook 三册 44 份中文笔记，含 TECC 式英语完形填空练习。">
<link rel="stylesheet" href="assets/style.css?v=__CSS__">
</head>
<body>
<header class="topbar">
  <button class="menu-btn" id="menuBtn" aria-label="目录">☰</button>
  <a class="brand" href="#/">AMT Handbook<span class="brand-sub">中文笔记</span></a>
  <input class="search" id="search" type="search" placeholder="搜索章节（按 / 聚焦）" autocomplete="off">
</header>
<div class="shell">
  <aside class="sidebar" id="sidebar">
    <div class="side-note">三册 44 份 · 每章 8 节</div>
    <nav id="nav"></nav>
  </aside>
  <main class="content" id="content">
    <div class="loading">加载中…</div>
  </main>
</div>
<footer class="foot">
  <a href="https://github.com/LeoChilfen/AMT-Handbook" target="_blank" rel="noopener">GitHub 仓库</a>
  <span>·</span>
  <span>笔记原文件为 Markdown，可用 Obsidian / VS Code 打开</span>
</footer>
<script src="data.js?v=__DATA__"></script>
<script src="assets/app.js?v=__APP__"></script>
</body>
</html>
"""

CSS = r"""*{box-sizing:border-box}
html,body{margin:0;padding:0}
body{
  font-family:-apple-system,BlinkMacSystemFont,"Segoe UI","PingFang SC","Hiragino Sans GB","Microsoft YaHei",sans-serif;
  color:#1f2328;background:#fbfbfa;line-height:1.75;font-size:16px;
}
.topbar{position:sticky;top:0;z-index:20;display:flex;align-items:center;gap:14px;
  padding:10px 18px;background:rgba(255,255,255,.92);backdrop-filter:blur(8px);
  border-bottom:1px solid #e6e6e3}
.brand{font-weight:700;text-decoration:none;color:#1f2328;font-size:16px;letter-spacing:.2px;white-space:nowrap}
.brand-sub{margin-left:8px;font-weight:400;font-size:13px;color:#6b7280}
.search{margin-left:auto;width:280px;max-width:45vw;padding:7px 12px;border:1px solid #d9d9d6;border-radius:999px;
  font-size:14px;outline:none;background:#fff}
.search:focus{border-color:#9aa0a6;box-shadow:0 0 0 3px rgba(0,0,0,.04)}
.menu-btn{display:none;border:1px solid #d9d9d6;background:#fff;border-radius:8px;width:36px;height:34px;font-size:16px;cursor:pointer}
.shell{display:flex;align-items:flex-start;max-width:1400px;margin:0 auto;gap:0}
.sidebar{position:sticky;top:57px;height:calc(100vh - 57px);overflow-y:auto;width:300px;flex:0 0 300px;
  padding:16px 10px 40px 18px;border-right:1px solid #ececea}
.side-note{font-size:12px;color:#8a8f98;margin:0 0 10px 6px}
.nav-group{margin-bottom:14px}
.nav-group h3{margin:0 0 6px;padding:0 6px;font-size:12.5px;letter-spacing:.06em;text-transform:uppercase;color:#6b7280}
.nav-link{display:block;padding:6px 8px;border-radius:7px;text-decoration:none;color:#2b3138;font-size:13.5px;line-height:1.4}
.nav-link .row{display:grid;grid-template-columns:32px 1fr;align-items:start;gap:2px;min-width:0}
.nav-link .ttl{flex:1 1 auto;min-width:0;overflow:hidden;display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;line-height:1.32}
.nav-link .num{flex:0 0 32px;color:#9aa0a6;font-variant-numeric:tabular-nums}
.nav-link:hover{background:#f1f1ef}
.nav-link.active{background:#1f2328;color:#fff}
.nav-link.active .num{color:#c9cdd2}

.content{flex:1 1 auto;min-width:0;padding:28px 40px 90px;max-width:900px}
.content h1{font-size:26px;line-height:1.4;margin:6px 0 18px;letter-spacing:.2px}
.content h2{scroll-margin-top:72px;font-size:20px;margin:36px 0 12px;padding-top:10px;border-top:1px solid #ececea}
.content h3{font-size:17.5px;margin:26px 0 8px;line-height:1.45}
.content h4{font-size:15.5px;margin:20px 0 6px;line-height:1.5;color:#1f2328}
.content h5{font-size:14.5px;margin:16px 0 5px;line-height:1.5;color:#333b43}
.content h6{font-size:13.5px;margin:14px 0 4px;line-height:1.5;color:#4a525b}
.content p{margin:10px 0}
.content p.bullet{padding-left:1.15em;text-indent:-1.15em}
.content ul,.content ol{margin:10px 0;padding-left:22px}
.content li{margin:4px 0}
.content code{background:#f3f3f1;padding:1.5px 5px;border-radius:5px;font-size:.9em;
  font-family:ui-monospace,SFMono-Regular,Consolas,"Liberation Mono",monospace}
.content pre{background:#f6f6f4;border:1px solid #e8e8e5;border-radius:10px;padding:14px 16px;overflow:auto}
.content pre code{background:none;padding:0;font-size:13px;line-height:1.6}
.content blockquote{margin:14px 0;padding:10px 14px;background:#f7f7f5;border-left:3px solid #c9cdd2;color:#4b5563;border-radius:0 8px 8px 0}
.table-wrap{overflow-x:auto;margin:14px 0}
.content table{border-collapse:collapse;width:100%;font-size:14px}
.content th,.content td{border:1px solid #e6e6e3;padding:7px 10px;vertical-align:top}
.content th{background:#f6f6f4;font-weight:600;text-align:left;white-space:nowrap}
.content a{color:#0b63c5;text-decoration:none}
.content a:hover{text-decoration:underline}
.content hr{border:none;border-top:1px solid #ececea;margin:26px 0}
.crumb{font-size:12.5px;color:#8a8f98;letter-spacing:.04em;margin-bottom:6px}
.toc{background:#f7f7f5;border:1px solid #ececea;border-radius:10px;padding:12px 16px;margin:0 0 22px;font-size:13.5px}
.toc b{font-size:12px;color:#6b7280;letter-spacing:.06em;display:block;margin-bottom:6px}
.toc a{display:inline-block;margin:3px 14px 3px 0;color:#2b3138}
.pager{display:flex;justify-content:space-between;gap:14px;margin-top:56px;padding-top:18px;border-top:1px solid #ececea;font-size:14px}
.pager a{color:#0b63c5;text-decoration:none}
.pager .grow{flex:1}
.hero h1{font-size:30px;margin:4px 0 8px}
.hero .lead{color:#4b5563;font-size:15.5px;margin:0 0 22px}
.cards{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:14px;margin:18px 0 8px}
.card{display:block;text-decoration:none;color:inherit;border:1px solid #e6e6e3;border-radius:12px;padding:16px 18px;background:#fff}
.card:hover{border-color:#c9cdd2;box-shadow:0 2px 10px rgba(0,0,0,.04)}
.card .k{font-size:11.5px;letter-spacing:.08em;text-transform:uppercase;color:#8a8f98}
.card .t{font-size:19px;font-weight:650;margin:4px 0 2px}
.card .d{font-size:13px;color:#6b7280}
.idx-book{margin:34px 0}
.idx-book h2{margin-top:30px}
.idx-item{display:block;padding:10px 0;border-bottom:1px solid #f0f0ee}
.idx-item a{font-weight:600;text-decoration:none;color:#0b63c5}
.idx-item a .idx-num{color:#9aa0a6;font-weight:500;margin-right:8px;font-variant-numeric:tabular-nums}
.idx-item > span{display:block;color:#4b5563;font-size:14px;margin-top:3px;line-height:1.6}
.loading{color:#8a8f98;padding:40px 0}
.foot{max-width:1400px;margin:0 auto;padding:18px 40px 40px;color:#8a8f98;font-size:12.5px;display:flex;gap:8px;flex-wrap:wrap}
.foot a{color:#6b7280}
@media (max-width:900px){
  .menu-btn{display:block}
  .search{width:180px}
  .sidebar{position:fixed;left:0;top:57px;bottom:0;z-index:15;background:#fbfbfa;transform:translateX(-100%);
    transition:transform .18s ease;box-shadow:2px 0 12px rgba(0,0,0,.08);height:auto}
  .sidebar.open{transform:translateX(0)}
  .content{padding:20px 18px 70px}
  .foot{padding:18px}
}
.card-list{margin:14px 0 0;padding-left:24px;line-height:2.1}
.card-list a{color:#1a73e8;text-decoration:none}
.card-list a:hover{text-decoration:underline}
.idx-book{margin:30px 0 4px;font-size:17px;border-bottom:1px solid #eee;padding-bottom:6px}
.content h2 a{color:inherit;text-decoration:none}
"""

JS = r"""(function(){
  var data = window.AMT_DATA || [];
  var cardsData = window.AMT_CARDS || [];
  var cardsByChapter = {};
  cardsData.forEach(function(s){ cardsByChapter[s.chapter] = s; });
  var bySlug = {};
  var order = [];
  data.forEach(function(g){ g.chapters.forEach(function(c){ c.group = g; bySlug[c.slug] = c; order.push(c); }); });

  var nav = document.getElementById('nav');
  var content = document.getElementById('content');
  var search = document.getElementById('search');
  var sidebar = document.getElementById('sidebar');
  var menuBtn = document.getElementById('menuBtn');

  function pad2(n){ var m = String(n).match(/^(\d+)([ab]?)$/); if (!m) return n; return (m[1].length < 2 ? '0' + m[1] : m[1]) + m[2]; }

  function buildNav(){
    var html = '';
    if (cardsData.length){
      html += '<div class="nav-group"><h3>学习卡片 · Study cards</h3>' +
        '<a class="nav-link" href="#/cards" data-slug="__cards__">' +
        '<span class="row"><span class="num">★</span><span class="ttl">全部学习卡片</span></span></a></div>';
    }
    data.forEach(function(g){
      html += '<div class="nav-group" data-group="' + g.slug + '"><h3>' + g.en + ' · ' + g.zh + '</h3>';
      g.chapters.forEach(function(c){
        html += '<a class="nav-link" href="#/' + c.slug + '" data-slug="' + c.slug + '">' +
          '<span class="row"><span class="num">' + pad2(c.num) + '</span>' +
          '<span class="ttl">' + esc(c.titleEn || ('Ch ' + c.num)) + '</span></span></a>';
      });
      html += '</div>';
    });
    nav.innerHTML = html;
  }

  function esc(s){ return String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;'); }

  function markActive(slug){
    [].forEach.call(nav.querySelectorAll('.nav-link'), function(a){
      a.classList.toggle('active', a.getAttribute('data-slug') === slug);
    });
  }

  function setTitle(t){ document.title = t ? (t + ' · AMT Handbook 中文笔记') : 'AMT Handbook · 中文笔记'; }

  function renderHome(){
    var total = order.length;
    var html = '<div class="hero"><h1>AMT Handbook 中文笔记</h1>' +
      '<p class="lead">FAA《Aviation Maintenance Technician Handbook》三册全书的中文精读笔记，共 ' + total +
      ' 份，每章 8 个小节。第 7 节已改为 <strong>TECC 式英语完形填空</strong>：题干与选项取自本章英文术语，答案后附中文语法 / 词义解析。</p>' +
      '<div class="cards">';
    data.forEach(function(g){
      html += '<a class="card" href="#/index"><span class="k">' + g.en + '</span>' +
        '<div class="t">' + g.zh + ' · ' + g.count + ' 份</div>' +
        '<div class="d">点开总索引，逐章阅读</div></a>';
    });
    html += '</div></div>' +
      '<h2>怎么用</h2>' +
      '<ul>' +
      '<li>左侧目录按三册分组，点章节即可打开；顶部搜索框按章节标题过滤（快捷键 <code>/</code>）。</li>' +
      '<li>每章固定 8 节：一句话 → 要点 → 术语对照 → 关键数字 → 结构部件 → 检查维修 → <b>高频考点（完形填空）</b> → 易混点。</li>' +
      '<li>完形填空先自己做，答案与解析在每条题目的「答案与解析」小节里。</li>' +
      '</ul>' +
      '<p style="color:#8a8f98;font-size:14px">原始 Markdown 文件在仓库 <code>notes/</code> 目录，可直接用 Obsidian 或 VS Code 打开。</p>';
    content.innerHTML = html;
    markActive(null);
    setTitle('');
  }

  function renderIndex(){
    var html = '<div class="crumb">总索引</div><h1>44 章总索引</h1>' +
      '<p style="color:#4b5563;font-size:14.5px;margin-top:-8px">每章一句话概括，点标题进入全文。</p>';
    data.forEach(function(g){
      html += '<section class="idx-book"><h2>' + g.en + ' · ' + g.zh + '（' + g.count + ' 份）</h2>';
      g.chapters.forEach(function(c){
        html += '<div class="idx-item"><a href="#/' + c.slug + '">' +
          '<span class="idx-num">Ch ' + c.num + '</span>' + esc(c.titleEn || ("Ch " + c.num)) + '</a>' +
          '<span>' + esc(c.summary || c.titleZh || "") + '</span></div>';
      });
      html += '</section>';
    });
    content.innerHTML = html;
    markActive(null);
    setTitle('总索引');
  }

  function renderChapter(slug, anchor){
    var c = bySlug[slug];
    if (!c){ content.innerHTML = '<div class="loading">没有找到这一章。<a href="#/">回到首页</a></div>'; return; }
    var idx = order.indexOf(c);
    var prev = idx > 0 ? order[idx - 1] : null;
    var next = idx < order.length - 1 ? order[idx + 1] : null;

    fetch('pages/' + slug + '.html').then(function(r){
      if (!r.ok) throw new Error('HTTP ' + r.status);
      return r.text();
    }).then(function(html){
      var toc = '';
      if (c.headings && c.headings.length){
        toc = '<div class="toc"><b>本页目录</b>' + c.headings.map(function(h){
          return '<a href="#/' + slug + '/' + h.id + '">' + esc(h.text) + '</a>';
        }).join('') + '</div>';
      }
      var pager = '<div class="pager">' +
        '<div class="grow">' + (prev ? '<a href="#/' + prev.slug + '">← Ch ' + prev.num + ' ' + esc(prev.titleEn) + '</a>' : '') + '</div>' +
        '<div class="grow" style="text-align:right">' + (next ? '<a href="#/' + next.slug + '">Ch ' + next.num + ' ' + esc(next.titleEn) + ' →</a>' : '') + '</div>' +
        '</div>';
      var crumb = '<div class="crumb">' + c.bookEn + ' · ' + c.bookZh + ' / Ch ' + c.num + '</div>';
      var h1end = html.indexOf('</h1>');
      if (toc && h1end > -1){ html = html.slice(0, h1end + 5) + toc + html.slice(h1end + 5); }
      content.innerHTML = crumb + html + pager;
      markActive(slug);
      setTitle('Ch ' + c.num + ' ' + (c.titleEn || ''));
      if (anchor){
        var el = document.getElementById(anchor);
        if (el){ el.scrollIntoView({block: 'start'}); } else { window.scrollTo(0, 0); }
      } else {
        window.scrollTo(0, 0);
      }
    }).catch(function(err){
      content.innerHTML = '<div class="loading">这一页加载失败（' + err.message + '）。请刷新重试。</div>';
    });
  }

  function renderCardsIndex(){
    var total = 0;
    cardsData.forEach(function(s){ total += s.count; });
    var html = '<div class="hero"><h1>学习卡片</h1>' +
      '<p class="lead">按每章<b>二级目录</b>拆分的学习卡片：每张覆盖一个大节（含其下的小标题），包含 <b>手册原文</b>、<b>专业翻译</b>、<b>专业词汇解析</b> 与 <b>语法解析</b>。' +
      (total ? '当前共 ' + total + ' 张，覆盖 ' + cardsData.length + ' 章。' : '') + '</p></div>';
    var curBook = '';
    cardsData.forEach(function(s){
      if (s.book !== curBook){
        curBook = s.book;
        html += '<h2 class="idx-book">' + esc(s.bookEn) + ' · ' + esc(s.bookZh) + '</h2>';
      }
      html += '<div class="idx-item">' +
        '<a class="idx-num" href="#/cards/' + s.chapter + '">Ch ' + pad2(s.num) + '</a>' +
        '<div class="idx-main"><a class="idx-title" href="#/cards/' + s.chapter + '">' + esc(s.titleEn) + '</a>' +
        '<div class="idx-sum">' + s.count + ' 张卡片</div></div></div>';
    });
    content.innerHTML = html;
    markActive('__cards__');
    setTitle('学习卡片');
    window.scrollTo(0, 0);
  }

  function renderCardSet(chapterSlug){
    var s = cardsByChapter[chapterSlug];
    if (!s){ content.innerHTML = '<div class="loading">没有找到这组卡片。<a href="#/cards">返回卡片目录</a></div>'; return; }
    var html = '<div class="crumb"><a href="#/cards">学习卡片</a> / ' + esc(s.bookEn) + ' · ' + esc(s.bookZh) + '</div>' +
      '<h1>Ch ' + pad2(s.num) + ' · ' + esc(s.titleEn) + '</h1>' +
      '<p class="lead">共 ' + s.count + ' 张卡片，按节顺序排列。</p><ol class="card-list">' +
      s.cards.map(function(c){
        return '<li><a href="#/card/' + c.slug + '">' + esc(c.title) + '</a></li>';
      }).join('') + '</ol>';
    content.innerHTML = html;
    markActive(chapterSlug);
    setTitle('学习卡片 · Ch ' + s.num);
    window.scrollTo(0, 0);
  }

  function renderCard(slug){
    var set = null, idx = -1;
    cardsData.forEach(function(s){
      s.cards.forEach(function(c, i){ if (c.slug === slug){ set = s; idx = i; } });
    });
    if (!set){ content.innerHTML = '<div class="loading">没有找到这张卡片。<a href="#/cards">返回卡片目录</a></div>'; return; }
    var prev = idx > 0 ? set.cards[idx - 1] : null;
    var next = idx < set.cards.length - 1 ? set.cards[idx + 1] : null;
    fetch('cards/' + slug + '.html').then(function(r){
      if (!r.ok) throw new Error('HTTP ' + r.status);
      return r.text();
    }).then(function(html){
      var crumb = '<div class="crumb"><a href="#/cards">学习卡片</a> / <a href="#/cards/' + set.chapter + '">' +
        esc(set.bookEn) + ' Ch ' + pad2(set.num) + '</a> / 第 ' + (idx + 1) + ' 节</div>';
      var pager = '<div class="pager">' +
        '<div class="grow">' + (prev ? '<a href="#/card/' + prev.slug + '">← ' + esc(prev.title) + '</a>' : '') + '</div>' +
        '<div class="grow" style="text-align:right">' + (next ? '<a href="#/card/' + next.slug + '">' + esc(next.title) + ' →</a>' : '') + '</div>' +
        '</div>';
      content.innerHTML = crumb + html + pager;
      markActive(set.chapter);
      setTitle((set.cards[idx] ? set.cards[idx].title : '') + ' · 学习卡片');
      window.scrollTo(0, 0);
    }).catch(function(err){
      content.innerHTML = '<div class="loading">卡片加载失败（' + err.message + '）。</div>';
    });
  }

  function route(){
    var h = location.hash.replace(/^#\/?/, '');
    var parts = h.split('/');
    var slug = parts[0];
    if (!slug){ renderHome(); }
    else if (slug === 'index'){ renderIndex(); }
    else if (slug === 'cards'){
      if (parts[1]){ renderCardSet(parts[1]); } else { renderCardsIndex(); }
    }
    else if (slug === 'card' && parts[1]){ renderCard(parts[1]); }
    else {
      var anchor = parts[1] ? decodeURIComponent(parts[1]) : '';
      renderChapter(slug, anchor);
    }
    sidebar.classList.remove('open');
  }

  search.addEventListener('input', function(){
    var q = search.value.trim().toLowerCase();
    [].forEach.call(nav.querySelectorAll('.nav-link'), function(a){
      var c = bySlug[a.getAttribute('data-slug')];
      var hay = (c.titleEn + ' ' + c.titleZh + ' ' + c.num + ' ' + c.bookZh + ' ' + c.bookEn).toLowerCase();
      a.style.display = (!q || hay.indexOf(q) > -1) ? '' : 'none';
    });
    [].forEach.call(nav.querySelectorAll('.nav-group'), function(g){
      var vis = [].some.call(g.querySelectorAll('.nav-link'), function(a){ return a.style.display !== 'none'; });
      g.style.display = vis ? '' : 'none';
    });
  });

  document.addEventListener('keydown', function(e){
    if (e.key === '/' && document.activeElement !== search){ e.preventDefault(); search.focus(); }
    if (e.key === 'Escape' && document.activeElement === search){ search.value = ''; search.dispatchEvent(new Event('input')); search.blur(); }
  });

  menuBtn.addEventListener('click', function(){ sidebar.classList.toggle('open'); });
  window.addEventListener('hashchange', route);

  buildNav();
  route();
})();
"""

if __name__ == "__main__":
    sys.exit(main())
