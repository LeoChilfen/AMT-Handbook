"""Validate study cards: structure, translation coverage, glossary, grammar."""
import io
import os
import re
import sys

REQ = ["## 1. 原文", "## 2. 中文翻译", "## 3. 专业词汇", "## 4. 语法解析"]


def split_sections(text):
    marks = [m.start() for m in re.finditer(r"^## \d\. ", text, re.M)]
    parts = {}
    for i, pos in enumerate(marks):
        end = marks[i + 1] if i + 1 < len(marks) else len(text)
        chunk = text[pos:end]
        head = chunk.splitlines()[0].strip()
        parts[head] = chunk
    return parts


def check(path):
    text = io.open(path, encoding="utf-8").read()
    problems = []
    for r in REQ:
        if r not in text:
            problems.append("缺少小节 " + r)
    if "TODO" in text:
        problems.append("仍有 TODO 未填")
    if problems:
        return problems, {}

    parts = split_sections(text)
    orig = parts.get("## 1. 原文", "")
    trans = parts.get("## 2. 中文翻译", "")
    orig_paras = [p for p in orig.split("\n\n")[1:] if p.strip()]
    trans_paras = [p for p in trans.split("\n\n")[1:] if p.strip()]
    if len(trans_paras) < max(1, len(orig_paras) - 1):
        problems.append("翻译段落 %d < 原文段落 %d" % (len(trans_paras), len(orig_paras)))

    gloss = parts.get("## 3. 专业词汇", "")
    rows = [l for l in gloss.splitlines() if l.strip().startswith("|") and "---" not in l]
    rows = [r for r in rows if not re.match(r"^\|\s*英文\s*\|", r)]
    if len(rows) < 4:
        problems.append("词汇表 %d 行（需 >= 4）" % len(rows))

    gram = parts.get("## 4. 语法解析", "")
    items = re.findall(r"^### ", gram, re.M)
    if len(items) < 2:
        problems.append("语法点 %d 个（需 >= 2）" % len(items))
    if gram.count("原句") < len(items):
        problems.append("语法点缺「原句」")

    stats = {
        "orig_paras": len(orig_paras),
        "trans_paras": len(trans_paras),
        "terms": len(rows),
        "grammar": len(items),
    }
    return problems, stats


def main(argv):
    root = argv[1] if len(argv) > 1 else "cards"
    total, bad = 0, 0
    for dirpath, _dirs, files in os.walk(root):
        for f in sorted(files):
            if not f.endswith(".md"):
                continue
            total += 1
            path = os.path.join(dirpath, f)
            rel = os.path.relpath(path, root)
            problems, stats = check(path)
            if problems:
                bad += 1
                print("FAIL %s" % rel)
                for p in problems:
                    print("   - " + p)
            else:
                print("OK   %s  (%d 段原文 / %d 词条 / %d 语法点)" % (
                    rel, stats["orig_paras"], stats["terms"], stats["grammar"]))
    print("---")
    print("%d/%d cards pass" % (total - bad, total))
    return 0 if bad == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
