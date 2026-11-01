"""Validate that a note's section 7 is a well-formed 10-item English cloze test.

Usage:
    python check_cloze.py <note.md> [more notes...]

Checks per file:
  1. section heading "## 7. 高频考点" exists and section 8 still follows
  2. exactly 10 items numbered **1.** .. **10.** in order
  3. every item is followed by an options line containing A) B) C) D)
  4. "### 答案与解析" present with exactly 10 entries "**n. X**"
  5. stems and option lines contain no CJK characters
  6. at least 3 distinct answer letters (no AAAA...)
"""
import io
import re
import sys

CJK = re.compile(r"[\u3400-\u9fff]")
Q = re.compile(r"^\*\*(\d+)\.\*\*\s*(.+)$")
A = re.compile(r"^\*\*(\d+)\.\s*([A-D])\*\*")


def check(path):
    with io.open(path, encoding="utf-8") as f:
        lines = f.read().splitlines()

    errs = []
    heads = [i for i, l in enumerate(lines) if l.startswith("## 7.")]
    if not heads:
        return ["missing section ## 7."], 0
    start = heads[0]
    ends = [i for i, l in enumerate(lines) if i > start and l.startswith("## 8.")]
    if not ends:
        errs.append("section ## 8. not found after section 7")
        end = len(lines)
    else:
        end = ends[0]
    body = lines[start:end]

    ans_idx = [i for i, l in enumerate(body) if l.startswith("### 答案与解析")]
    if not ans_idx:
        errs.append("missing '### 答案与解析'")
        qpart, apart = body, []
    else:
        qpart, apart = body[: ans_idx[0]], body[ans_idx[0] + 1 :]

    numbers, stems = [], []
    qpos = [i for i, l in enumerate(qpart) if Q.match(l)]
    for i in qpos:
        m = Q.match(qpart[i])
        numbers.append(int(m.group(1)))
        stems.append(m.group(2))
        nxt = qpart[i + 1] if i + 1 < len(qpart) else ""
        optline = nxt
        if not re.search(r"A\)", optline):
            for j in range(i + 1, min(i + 4, len(qpart))):
                if re.search(r"A\)", qpart[j]):
                    optline = qpart[j]
                    break
        if not all(re.search(p, optline) for p in (r"A\)", r"B\)", r"C\)", r"D\)")):
            errs.append("item %s: options line missing A)/B)/C)/D)" % m.group(1))
        if CJK.search(m.group(2)):
            errs.append("item %s: stem contains Chinese" % m.group(1))
        if CJK.search(optline):
            errs.append("item %s: options contain Chinese" % m.group(1))

    if numbers != list(range(1, 11)):
        errs.append("item numbers are %s, expected 1..10" % numbers)

    answers = []
    for l in apart:
        m = A.match(l)
        if m:
            answers.append((int(m.group(1)), m.group(2)))
    if [a[0] for a in answers] != list(range(1, 11)):
        errs.append("answer keys are %s, expected 1..10" % [a[0] for a in answers])
    if len(set(a[1] for a in answers)) < 3:
        errs.append("answer letters too uniform: %s" % "".join(a[1] for a in answers))

    return errs, len(numbers)


def main():
    bad = 0
    for path in sys.argv[1:]:
        errs, n = check(path)
        name = path.replace("\\", "/").split("/notes/")[-1]
        if errs:
            bad += 1
            print("FAIL %-28s %s" % (name, "; ".join(errs)))
        else:
            print("OK   %-28s %d items" % (name, n))
    print("---")
    print("%d/%d files pass" % (len(sys.argv) - 1 - bad, len(sys.argv) - 1))
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
