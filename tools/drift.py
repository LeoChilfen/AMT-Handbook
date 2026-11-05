# -*- coding: utf-8 -*-
"""检查一轮改稿后，哪些卡片的「非英文部分」需要跟着改。

用法：
  python drift.py <cards/general/chNN 目录>
输出每张卡的漂移项：
  - ZH≠EN：中文段数与英文段数不一致（需要拆/并段）
  - HEAD：小标题 (#) 与英文不同位（需要搬标题）
  - QUOTE：第 4 节里的 **原句** 在第 1 节原文里找不到了（英文改过后引用失效）
  - VOCAB：第 3 节词条表里，英文列的词在第 1 节原文里出现 0 次（英文改过后可能已无此词）
"""
import io
import os
import re
import sys


def split_sections(text):
    """按 ## 1./2./3./4. 切四节，返回 dict。"""
    marks = [(m.start(), m.group(0)) for m in re.finditer(r"^## [1-4]\. .*$", text, re.M)]
    out = {}
    for i, (pos, title) in enumerate(marks):
        end = marks[i + 1][0] if i + 1 < len(marks) else len(text)
        out[title[3:4]] = text[pos:end]
    return out


def paras(block):
    """去掉节标题后的段落列表。"""
    body = block.split("\n", 1)[1] if "\n" in block else ""
    return [p.strip() for p in body.split("\n\n") if p.strip()]


def norm(s):
    return re.sub(r"[^a-z0-9]", "", s.lower())


def check(path):
    text = io.open(path, encoding="utf-8").read()
    sec = split_sections(text)
    if not all(k in sec for k in "1234"):
        return ["STRUCT: 四节不全"]
    en, zh, vo, gr = (paras(sec[k]) for k in "1234")
    issues = []

    # 中文段数与英文段数
    if len(en) != len(zh):
        issues.append("ZH≠EN: 英文 %d 段 / 中文 %d 段" % (len(en), len(zh)))
    else:
        for i, (a, b) in enumerate(zip(en, zh)):
            ha, hb = a.startswith("#"), b.startswith("#")
            if ha != hb:
                issues.append("HEAD: 第 %d 段 英文%s标题、中文%s标题" % (i + 1, "" if ha else "不是", "" if hb else "不是"))
                break

    # 语法点「原句」是否仍在原文里
    en_join = norm(" ".join(en))
    gr_text = "\n".join(gr)
    for m in re.finditer(r"\*\*原句\*\*[：:]\s*([^\n]+)", gr_text):
        q = norm(m.group(1))
        if q and q not in en_join:
            issues.append("QUOTE: 失效 → %s" % m.group(1)[:60])

    # 词汇表里的词在原文是否还出现（按词逐个匹配，容忍词形变化）
    rows = [ln for ln in "\n".join(vo).split("\n") if ln.strip().startswith("|") and "---" not in ln]
    for ln in rows[1:]:  # 跳过表头
        cells = [c.strip() for c in ln.strip().strip("|").split("|")]
        if not cells:
            continue
        term = cells[0]
        head = re.split(r"[（(]", term)[0].strip()
        words = [w for w in re.findall(r"[A-Za-z]{3,}", head) if len(w) >= 3]
        if not words:
            continue
        if not all(norm(w)[:6] in en_join for w in words):
            issues.append("WARN-VOCAB: 原文未逐字出现 %s" % head)
    return issues


def main():
    root = sys.argv[1]
    files = sorted(os.listdir(root))
    total = 0
    warns = 0
    for name in files:
        if not name.endswith(".md"):
            continue
        issues = check(os.path.join(root, name))
        fatal = [x for x in issues if not x.startswith("WARN-")]
        warns += len(issues) - len(fatal)
        issues = fatal
        if issues:
            total += 1
            print("%s" % name)
            for it in issues:
                print("    " + it)
    print("---")
    print("%d 张卡需要跟改" % total)


if __name__ == "__main__":
    main()
