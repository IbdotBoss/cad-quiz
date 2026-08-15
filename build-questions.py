#!/usr/bin/env python3
"""Parse CAD-Master-Question-Bank.md -> JS question array for index.html.

Format contract
---------------
Question block:
    **Q42. Stem text? *(Choose 2)*
    - A. option
    - B. option

Answer row (Src column is new vs the CSA parser):
    | Q42 | A & C | v2 | explanation |

Unlike the CSA version there is no `in_answers` state flag: question headers
start with `**Q` and answer rows start with `| Q`, so the two are unambiguous
and practice sections can be appended anywhere in a domain.
"""
import re
import json
import sys
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent

# Two copies of the bank exist by design: the working folder is authored in, and
# questions/ is what ships in the public repo. Prefer the working folder when it is
# present (this machine) and copy forward, so the two can never drift; fall back to
# questions/ so a bare clone of the repo still builds.
WORKING = HERE.parent / "CAD-questions"
SHIPPED = HERE / "questions"

# Kept in sync automatically. SOURCES.md is written with <ServiceNow>/... placeholders rather than
# absolute paths precisely so that it can be mirrored; the leak check below is the backstop.
MIRRORED = ("CAD-Master-Question-Bank.md", "CAD-Trap-Sheet.md", "SOURCES.md")

if (WORKING / MIRRORED[0]).exists():
    SHIPPED.mkdir(exist_ok=True)
    for name in MIRRORED:
        src = WORKING / name
        if src.exists():
            dst = SHIPPED / name
            new = src.read_text(encoding="utf-8")
            if not dst.exists() or dst.read_text(encoding="utf-8") != new:
                dst.write_text(new, encoding="utf-8")
                print(f"Synced {name} -> questions/", file=sys.stderr)

# questions/ is published, so a local path reaching it would be disclosed. Fail loudly rather
# than scrub silently: an auto-scrub quietly misses any pattern it was not taught.
LEAKS = ("C:\\Users\\", "C:/Users/")
for doc in sorted(SHIPPED.glob("*.md")):
    text = doc.read_text(encoding="utf-8")
    for pat in LEAKS:
        if pat in text:
            sys.exit(f"ERROR: {doc.name} contains a local path ({pat!r}) and would publish it. "
                     f"Scrub it to <ServiceNow>/... before building.")

SRC = SHIPPED / "CAD-Master-Question-Bank.md"
OUT = HERE / "_questions.js"
HTML = HERE / "index.html"

with open(SRC, encoding="utf-8") as f:
    lines = f.read().splitlines()

# ---- Pass 1: answer rows -> qid -> (letters, src, why) ----
answers = {}
ans_row = re.compile(
    r'^\|\s*Q(\d+)\s*\|\s*([^|]+?)\s*\|\s*([^|]*?)\s*\|\s*(.+?)\s*\|\s*$'
)
for ln in lines:
    m = ans_row.match(ln)
    if not m:
        continue
    qid = int(m.group(1))
    letters = re.findall(r'\b([A-G])\b', m.group(2).strip())
    if not letters:
        continue
    src = m.group(3).strip().lower() or "unknown"
    why = m.group(4).strip().replace('**', '')
    answers[qid] = (letters, src, why)

# ---- Pass 2: question blocks ----
domain_hdr = re.compile(r'^##\s+Domain\s+(\d+)\b')
q_hdr = re.compile(r'^\*\*Q(\d+)\.\*\*\s*(.*)$')
opt_line = re.compile(r'^\s*-\s*([A-G])\.\s+(.*)$')

questions = []
cur_domain = None
i, n = 0, len(lines)
while i < n:
    ln = lines[i]
    dm = domain_hdr.match(ln)
    if dm:
        cur_domain = int(dm.group(1))
        i += 1
        continue
    qm = q_hdr.match(ln)
    if qm:
        qid = int(qm.group(1))
        stem = qm.group(2).strip()
        opts, letters = [], []
        j = i + 1
        while j < n:
            l2 = lines[j]
            om = opt_line.match(l2)
            if om:
                letters.append(om.group(1))
                opts.append(om.group(2).strip())
                j += 1
                continue
            if not l2.strip():
                if opts:
                    break
                j += 1
                continue
            if l2.startswith('**Q') or l2.startswith('#') or l2.startswith('---') or l2.startswith('|'):
                break
            if not opts:
                stem += ' ' + l2.strip()      # stem wrapped onto next line
                j += 1
                continue
            break
        stem = re.sub(r'\s*\*?\(Choose[^)]*\)\*?\s*$', '', stem).strip()
        stem = stem.replace('**', '').strip()
        questions.append({
            'qid': qid, 'd': cur_domain, 'stem': stem,
            'opts': opts, 'letters': letters,
        })
        i = j
        continue
    i += 1

# ---- Merge + validate ----
LET2IDX = {c: k for k, c in enumerate('ABCDEFG')}
out, errors = [], []
seen = set()
for q in sorted(questions, key=lambda x: x['qid']):
    qid = q['qid']
    if qid in seen:
        errors.append(f"Q{qid}: duplicate question number")
        continue
    seen.add(qid)
    if qid not in answers:
        errors.append(f"Q{qid}: no answer row found")
        continue
    letters, src, why = answers[qid]
    ans_idx = sorted(LET2IDX[c] for c in letters)
    if len(q['opts']) < 2:
        errors.append(f"Q{qid}: only {len(q['opts'])} options")
    for a in ans_idx:
        if a >= len(q['opts']):
            errors.append(f"Q{qid}: answer index {a} >= option count {len(q['opts'])}")
    if q['d'] is None:
        errors.append(f"Q{qid}: no domain header above it")
    out.append({
        'id': qid, 'd': q['d'], 'q': q['stem'], 'opts': q['opts'],
        'ans': ans_idx, 'multi': len(ans_idx) > 1,
        'src': src, 'exp': why,
    })

orphans = set(answers) - seen
for qid in sorted(orphans):
    errors.append(f"Q{qid}: answer row with no question block")

# ---- Report ----
print(f"Parsed {len(out)} questions", file=sys.stderr)
dc = Counter(o['d'] for o in out)
for d in range(1, 7):
    print(f"  D{d}: {dc.get(d, 0)}", file=sys.stderr)
sc = Counter(o['src'] for o in out)
print("  by src: " + ", ".join(f"{k}={v}" for k, v in sorted(sc.items())), file=sys.stderr)
print(f"  multi:   {sum(1 for o in out if o['multi'])}", file=sys.stderr)
if errors:
    print("ERRORS:", file=sys.stderr)
    for e in errors:
        print("  " + e, file=sys.stderr)
    sys.exit(1)
print("  no validation errors", file=sys.stderr)

# ---- Emit ----
parts = [
    "{id:%d,d:%d,q:%s,opts:%s,ans:%s,multi:%s,src:%s,exp:%s}" % (
        o['id'], o['d'],
        json.dumps(o['q'], ensure_ascii=False),
        json.dumps(o['opts'], ensure_ascii=False),
        json.dumps(o['ans']),
        'true' if o['multi'] else 'false',
        json.dumps(o['src']),
        json.dumps(o['exp'], ensure_ascii=False),
    )
    for o in out
]
js = "const QS = [\n" + ",\n".join(parts) + "\n];\n"
with open(OUT, "w", encoding="utf-8") as f:
    f.write(js)
print(f"Wrote {OUT}", file=sys.stderr)

# Inline the data into index.html between the markers. Keeping the questions inside
# index.html makes the file genuinely self-contained: it opens with a double-click over
# file:// (where fetch() is CORS-blocked) and can never serve a stale cached copy.
START = "/* QUESTIONS:START"
END = "/* QUESTIONS:END */"
try:
    with open(HTML, encoding="utf-8") as f:
        html = f.read()
    i, j = html.find(START), html.find(END)
    if i == -1 or j == -1 or j < i:
        print("  WARN: markers not found in index.html; left untouched", file=sys.stderr)
    else:
        head = START + " — generated by build-questions.py, do not edit by hand */\n"
        html = html[:i] + head + js + html[j:]
        with open(HTML, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"Inlined {len(out)} questions into {HTML}", file=sys.stderr)
except FileNotFoundError:
    print(f"  WARN: {HTML} not found; skipped inlining", file=sys.stderr)
