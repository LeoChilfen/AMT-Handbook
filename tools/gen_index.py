"""Regenerate INDEX.md with English chapter names as the link text."""
import io
import os
import re

ROOT = r"F:\AMT-Handbook"
BOOKS = [("general", "General", "通用"), ("airframe", "Airframe", "机体"),
         ("powerplant", "Powerplant", "动力装置")]

H1 = re.compile(r"^#\s+Ch\s*(\d+)\s*([（(][^）)]*[）)])?\s*[·・]\s*(.*?)\s*(?:[（(](.*)[）)])?\s*$")


def read(path):
    with io.open(path, encoding="utf-8") as f:
        return f.read()


def chapter(path):
    text = read(path)
    lines = text.splitlines()
    h1 = H1.match(lines[0].strip())
    if not h1:
        raise SystemExit("bad H1: %s -> %s" % (path, lines[0]))
    num, part, en, zh = h1.group(1), (h1.group(2) or ""), h1.group(3), (h1.group(4) or "")
    # 一句话 = first non-empty line after "## 1."
    summary = ""
    for i, line in enumerate(lines):
        if line.startswith("## 1."):
            for nxt in lines[i + 1:]:
                if nxt.strip():
                    summary = nxt.strip()
                    break
            break
    part_en = {"（上）": " (Part 1)", "（下）": " (Part 2)", "（前半）": " (Part 1)", "（后半）": " (Part 2)"}.get(part, part)
    title = "Ch %s · %s%s" % (num, en, part_en)
    return num, title, summary


def main():
    out = ["# AMT Handbook 中文笔记总索引", "",
           "每章一份笔记，按 8 个小节写；第 7 节是 **TECC 式英语完形填空**（10 题 + 答案中文解析）。"
           "点章节名看全文，或看带目录的在线站点：<https://leochilfen.github.io/AMT-Handbook/>。", ""]
    total = 0
    for slug, en, zh in BOOKS:
        folder = os.path.join(ROOT, "notes", slug)
        files = sorted(os.listdir(folder))
        files = [f for f in files if f.endswith(".md")]
        files.sort(key=lambda f: (int(re.search(r"\d+", f).group()), f))
        total += len(files)
        out.append("## %s %s（%d 份）" % (en, zh, len(files)))
        out.append("")
        out.append("| 章节 | 一句话 |")
        out.append("|---|---|")
        for f in files:
            num, title, summary = chapter(os.path.join(folder, f))
            out.append("| [%s](notes/%s/%s) | %s |" % (title, slug, f, summary))
        out.append("")
    text = "\n".join(out).rstrip() + "\n"
    while "\n\n\n" in text:
        text = text.replace("\n\n\n", "\n\n")
    with io.open(os.path.join(ROOT, "INDEX.md"), "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    print("chapters: %d" % total)


if __name__ == "__main__":
    main()
