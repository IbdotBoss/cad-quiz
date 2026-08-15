# CAD Question Bank

Practice questions and a self-contained quiz app for the **ServiceNow Certified Application Developer (CAD)** exam.

**▶ [Open the quiz](https://ibdotboss.github.io/cad-quiz/)**

The real exam is 60 questions in 90 minutes. ServiceNow does **not** publish the cut score and states it is **not always 70%**, so treat any percentage here as a working target, not a pass mark. Multi-select questions give **no partial credit**.

---

## What's here

| | |
|---|---|
| [`index.html`](index.html) | The quiz app. One file, no build step, no dependencies — works offline by double-clicking. |
| [`questions/CAD-Master-Question-Bank.md`](questions/CAD-Master-Question-Bank.md) | 280 questions across the six blueprint domains, each with an explanation of why the distractors are wrong. |
| [`questions/CAD-Trap-Sheet.md`](questions/CAD-Trap-Sheet.md) | The X-vs-Y confusions that actually cost marks, with the one rule that separates each pair. Read this last. |
| [`questions/SOURCES.md`](questions/SOURCES.md) | Provenance, plus a log of every answer dispute and how it was resolved. |
| [`build-questions.py`](build-questions.py) | Parses the markdown bank into the app. Fails loudly on malformed data. |

## Modes

- **Study** — everything matching your filters, immediate feedback
- **Exam simulation** — 60 questions, 90-minute timer, drawn to blueprint weight, no feedback until the end
- **New questions** — the newest set (39), written from the ServiceNow documentation to cover the blueprint topics the older bank was thin on. Kept out of Study and Exam by default so it can be drilled on its own; turn on the **new (v2)** source chip to mix it in
- **My wrong answers** — accumulates as you drill, clears as you get them right

Filter by domain and by source, and choose **Bank order** or **Shuffled** (Study only — the other
modes always shuffle). Progress persists in `localStorage`, and an unfinished run shows a
**resume banner** on the setup screen with Resume / Discard, so opening settings never bins an
exam you are part way through.

**Keyboard:** `1`–`7` select · `←`/`→` navigate · `Enter` submit · `A` ask AI · `S` toggle sidebar

**Answer options are shuffled by default** (Settings → Answer options). Without this, re-drilling
teaches you *"the answer is B"* rather than the material, and the real exam reorders them. The order
is fixed for the life of a run and survives a reload.

**Trap sheet** is built into the app — the X-vs-Y confusions with a filter box, so you can look up
`coalesce` or `ACL` mid-drill.

Results list **every question you missed**, with your answer against the correct one, so you don't
have to re-drill just to find out what went wrong.

## Ask AI

Stuck on a question? **Ask AI** copies the full question — stem, options, keyed answer and the bank's
reasoning — and opens it in Claude, ChatGPT, Perplexity or Gemini, so you can ask *why*.

The prompt also points the model at ServiceNow's **own documentation**
([ServiceNow/ServiceNowDocs](https://github.com/ServiceNow/ServiceNowDocs), `australia` branch),
including the [`llms.txt`](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/llms.txt)
index and the publication index most relevant to that question's domain — so it verifies against
source rather than from memory, and is explicitly asked to say so if the key looks wrong.

Prefill support is uneven, so the question is **always copied to your clipboard** as well:

| Platform | Prompt via URL |
|---|---|
| Claude | yes |
| ChatGPT | yes (auto-submits) |
| Perplexity | yes |
| Gemini | **no** — accepts no prompt by link, so paste from the clipboard |

**Private chat** uses each platform's own temporary-chat mode. Only Claude and ChatGPT expose one by
URL, so Perplexity and Gemini are disabled while it is on — Perplexity's incognito is an in-app
shortcut (`Ctrl ;`) that no link can reach. A web page **cannot** force a browser incognito window;
that is a browser security restriction available only to extensions.

When the platform can't take the prompt by link, a dialog appears **before** the tab opens — with the
question in a selectable box, a Copy button, and a "Don't show this again" option — so the instruction
to paste isn't lost behind the new tab.

## Coverage

| Domain | Weight | Questions |
|---|---|---|
| 1 · Designing and Creating an Application | 20% | 50 |
| 2 · Application User Interface | 20% | 45 |
| 3 · Security and Restricting Access | 20% | 46 |
| 4 · Application Automation | 20% | 55 |
| 5 · Working with External Data | 10% | 35 |
| 6 · Managing Applications | 10% | 23 |

Weights are the **official blueprint** (KB0011498), confirmed against the published exam specification. Several prep sites advertise a different split; they are wrong.

## Two things to know about the answers

**Answers were verified, not copied.** Practice sites frequently disagree with each other on the *same* question — the same item turned up keyed three different ways for UI Action types, source-control roles, and ACL evaluation order. Every conflict was adjudicated against the official ServiceNow product documentation, and the reasoning is logged in `SOURCES.md`. Where a conflict could not be resolved, the question was **dropped rather than guessed**.

**No question is marked “real exam” on a website's say-so.** Several sites advertise “actual exam
questions”; a dedicated search for genuine first-person recall found none, and those sites' keys were
measurably *worse* than average — one keyed “what do you install to add functionality” as *Patch/Update
Pack/App Package* rather than *Plugin*. The ACL evaluation-order question alone has now been keyed all
four possible ways by four different sources. `SOURCES.md` has the receipts.

**Every answer in the newest set cites the documentation page that settles it**, and the one item that could *not* be settled from the docs says so in its explanation rather than quietly asserting an answer.

`⭐` marks the three sample questions ServiceNow publishes in the exam specification.

## Rebuilding

Edit `questions/CAD-Master-Question-Bank.md`, then:

```bash
python build-questions.py
```

This regenerates `_questions.js` **and** inlines the questions into `index.html` between the `QUESTIONS:START` / `QUESTIONS:END` markers, so the app stays a single self-contained file. The script exits non-zero on any missing answer row, orphaned answer, out-of-range answer index, duplicate question number, or question without a domain heading.

## Contributing a question

Add the question and its answer row to the bank, then rebuild. Format:

```markdown
**Q42.** Which roles are created by default for a new application? *(Choose 2)*
- A. User role
- B. Customer role
- C. Admin role
- D. Approver role
```

```markdown
| Q | Answer | Src | Why |
|---|--------|-----|-----|
| Q42 | A & C | authored | Studio scaffolds `<scope>_user` and `<scope>_admin`. B and D are never generated. |
```

Answer rows may live anywhere in the domain. `Src` drives the app's source filter; `⭐` after the number marks one of the three official exam-specification samples.

The bank and its companion documents are authored in a working folder and **copied forward** into `questions/` by the build, so the two copies cannot drift. The build **fails** if any file under `questions/` contains a local filesystem path, because that folder is published.

---

## Disclaimer

Study aid, unofficial, not affiliated with or endorsed by ServiceNow. ServiceNow, and the certification and release names used here, belong to ServiceNow, Inc.

Questions are either written for this project, derived from public product documentation, or drawn from publicly reachable practice sites. **No question here is taken from a ServiceNow exam.** The three starred items are the sample questions ServiceNow publishes in its own exam specification.

The ServiceNow certification agreement prohibits disclosing exam content — **do not add exam questions to this repository**, and note that paraphrasing one still discloses it; rewording is not a workaround. Where a topic is worth testing, write the question from the documentation page that defines it and cite that page. Use this to learn the material, not to shortcut it.
