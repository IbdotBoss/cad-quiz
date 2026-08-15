# Sources and Answer-Dispute Log

Built 2026-08-11. Last revised 2026-08-15. Companion to `CAD-Master-Question-Bank.md`.

---

## Where the 282 questions came from

| Src tag | Count | Origin |
|---|---|---|
| `web` | 102 | Free/preview tiers of practice sites (list below) — the weak tier |
| `authored` | 95 | Written against the ADF course structure and the local ServiceNow docs |
| `v2` | 41 | **Newest set** — written directly from the Australia-release documentation to fill measured blueprint gaps |
| `web+docs` | 26 | Mined from the web, then adjudicated against the documentation |
| `docs` | 18 | Written directly from the documentation, including the three sample questions published in the exam specification (KB0011498) |

The three sample questions ServiceNow publishes in the exam specification are tagged `docs` like any
other documentation-derived item, and keep ServiceNow's own keys.

### The standing rule for this bank

**No question here is taken from a ServiceNow exam**, and none should ever be added. ServiceNow's
certification agreement does not permit disclosing exam content, and paraphrasing a question you saw
still discloses it — rewording is not a workaround.

Where a topic is worth testing, the question is written **from the documentation page that defines
it**, and the answer cites that page. That is the only route by which material enters this bank.

### Web sources mined

pass4success.com · open-exam-prep.com · actual4test.com · dumpsbase.com (parts 1–3) · marks4sure.com · processexam.com · itexams.com · pass4test.com · cciedump.spoto.net · interviewquestions.guru · basicoservicenowlearning.in · snready.com · pass4future.com · exams4sure.com · study4exam.com · passleader.com · dumpspedia.com · examgo.com · brainscape.com (Flow Designer deck)

Blocked / unreachable: examtopics.com, validexamdumps.com, quizlet.com, certshero.com, trustedinstitute.com (all 403 or gated).

---

## Documentation used for verification

Local clone: `<ServiceNow>/ServiceNowDocs/markdown/` (Australia release).

### The Fluent API pages are the best adjudicator for "which types/fields exist"

`application-development/servicenow-sdk/fluent-*-api.md` gives **field-level references** for UI Action,
UI Policy, Script Include, Script Action, Email Notification, Import Sets, Service Catalog, SLA and UI
Page. This class of question was previously written off as unsettleable from the local clone — it is
not. `fluent-ui-action-api.md` settled Q82, the item flagged in the last handoff as the weakest in the
bank, by enumerating the placement flags:

| form object | list object |
|---|---|
| `showButton`, `showLink` (Related Links), `showContextMenu`, `showSaveWithFormButton` | `showButton`, `showLink`, `showContextMenu`, `showListChoice`, `showBannerButton` |

**Choice is a list-only placement. There is no Form choice.** Q82's key was right; it now has a citation.

### Other files that settled disputes

- `application-development/servicenow-studio-classic/` — `exploring-servicenow-studio.md`, `servicenow-studio-user-interface.md`, `create-an-application-in-servicenow-studio.md`, `r_AvailableSourceControlOperations.md`
- `application-development/low-vs-pro-code.md` — enumerates the five builders
- `application-development/business-rules-and-script-includes.md`
- `application-development/guided-application-creator/guided-app-creator.md` — deprecation notice
- `application-development/automated-test-framework-atf/` — `atf-run-test.md`, `atf-build-overview.md`, `atf-breakpoints-rollback.md`
- `application-development/delegated-development-and-deployment/t_AddADeveloper.md`
- `application-development/application-administration.md`, `enable-application-administration.md`
- `platform-security/access-control/` — `exploring-access-control-list.md`, `acl-denial-behavior.md`, `explore-access-analyzer.md`, `access-analyzer.md`, `acl-rule-types.md`, `c_DefaultDenyProperty.md`
- `platform-administration/` — `t_CreateAUIPolicy.md`, `t_ConvertAUIPolicyToADataPolicy.md`, `c_Formatters.md`, `c_EmailNotifications.md`, `system-events/c_EventRegistry.md`, `time-configuration/c_ScheduledJobs.md`, `table-administration-and-data-management/t_CreateAManyToManyRelationship.md`, `r_RefDefaultManyToManyRels.md`
- `platform-user-interface/configure-use-list-functions.md`, `adoption-services/configure-next-experience-onboarding.md`
- `now-intelligence/reporting/column-view-access-control-list-reports.md`
- `servicenow-platform/service-catalog/c_RecordProducer.md`
- `api-reference/server-api-reference/c_GlideSystemScopedAPI.md`
- Earlier passes: `r_TableApplicationAccessFields.md`, `c_DefaultRuntimeAccessPermissions.md`, `c_ScriptProtectionPolicy.md`, `c_ApplicationScope.md`, `c_CrossScopePrivilegeRecord.md`, `restricted-caller-access-privilege.md`, `app-engine-studio/manage-template-access.md`

### A caution about this docs clone

The `servicenow-studio-classic/` folder mixes **current** ServiceNow Studio documentation with pages
explicitly titled `Legacy - …`, which carry their own notice that the legacy version of Studio is
being prepared for future deprecation. Read the page title before trusting a Studio detail — the
folder name is misleading, because the product itself is current.

---

## The v2 set (41 questions)

Written to fill the sub-objectives KB0011498 names explicitly but the bank barely tested. Counts before:

| Sub-objective | Was | Added |
|---|---:|---:|
| UI Policy / client-vs-server form logic (D2) | 1 | 8 |
| Record Producer as application UI (D2) | 6 | 4 |
| ATF (D2) | 2 | 6 |
| Application Properties (D4) | 2 | 6 |
| Events + Scheduled Script Executions (D4) | 3 | 6 |
| Script Includes (D4) | 6 | 5 |
| Send and receive email (D4) | 7 | 4 |
| Client-side API surface (D2) — added after the audit found the bank's GlideRecord claim wrong | — | 2 |

**Rule for this set: every answer cites the documentation file that settles it**, either directly or by
chaining to the row above ("Same doc: …"). A build-time check enforces this.

**One item is not doc-settled and says so: Q276** (why use a property rather than a hard-coded value).
The clone documents the property *API* and the `sys_properties` table but carries no page stating the
rationale. It is flagged `⚠️` in the bank and should be answered by eliminating the distractors, both
of which are independently false. It was kept rather than dropped because the distractors *are*
refutable from the docs; it is the answer's positive justification that is not.

**Not in the docs clone at all:** the properties-page module configuration (Link type, and the
`system_properties.do?sysparm_title=…&sysparm_category=…` arguments). No question was written about it,
rather than guess.

---

## Answer disputes and how they were resolved

Dump sites frequently disagree with each other on the *same* question. Every case below was adjudicated
against the documentation where possible. **These are also the best questions in the bank to study** —
sources disagree precisely where the material is confusing.

| # | Question | Conflicting keys seen | Resolution | Basis |
|---|---|---|---|---|
| 1 | Order of elements evaluated within an ACL (Q98) | "Conditions, Roles, Script" vs "Roles, Conditions, Script" | **Role → Security Attribute → Condition → Script** | `access-analyzer-logs.md` states the hierarchy explicitly. The Conditions-first version is legacy course material. **Kept flagged — read the options on exam day.** |
| 2 | Baseline access for a privately-scoped table (Q120) | "Only in-scope artifacts can read" vs "All scopes can read" | **All application scopes, Can read enabled** | `c_DefaultRuntimeAccessPermissions.md` table |
| 3 | Which options are unavailable if Can read is off (Q119) | "All web services access" vs "Can create/update/delete" | **Can create, update, delete** | `r_TableApplicationAccessFields.md` — each is "available only when Can read is selected"; web services is independent |
| 4 | Object a Display Business Rule lacks (Q142) | `g_scratchpad` vs `previous` | **`previous`** | `business-rules-and-script-includes.md` — the Display row's documented use *is* writing to `g_scratchpad`, so it cannot be the missing object |
| 6 | `hasRole` vs `hasRoleExactly` for admin in a BR (Q109) | Both keyed in different dumps | **`gs.hasRole('admin')`** | `hasRoleExactly` does not exist on `gs` at all (see #22) |
| 7 | Which is NOT a UI Action type (Q82) | "List choice" vs "Form choice" | **Form choice** — ⚠️ **now settled** | `fluent-ui-action-api.md` enumerates the placement flags; choice exists only on the list object |
| 8 | Responses to `gs.eventQueue()` (Q131) | "UI Policy" vs single answer vs "Script Action + Email Notification" | **Script Action and Email Notification** | Independently confirmed by `c_EventRegistry.md`: registration lets "Email and SMS notifications and Script Actions… react to the event" |
| 9 | Three steps to import a spreadsheet (Q161) | "Select Import Set, Select Transform Map, Run Transform" vs "Load Data, Create Transform Map, Run Transform" | **Load Data → Create Transform Map → Run Transform** | You cannot select an import set that does not exist yet |
| 10 | Email Notification Weight field (Q137) | Keyed three different ways | **Weight 0 = always send** (so "zero means no email" is the false statement) | Option order was scrambled between sources; the underlying fact is stable |
| 11 | itil read access with a field-level ACL (Q107) | "field1 and field3" vs "field1 and field2" | **field1 and field2** | field3 carries the admin-only rule |
| 12 | Source control roles | `source_control`+`source_control_admin` vs `source_control_admin`+`git_admin` vs `source_control`+`admin` | **Still excluded** | Three-way conflict, no documentation found. Not worth memorising a guess |
| 13 | Which source control op is available from both Studio and the Git repository | "Create Branch" vs "Apply Remote Changes" | **Create Branch** (and Create Tag) — ⚠️ **previously excluded, now settled** | `r_AvailableSourceControlOperations.md`: only **Create Branch** and **Create Tag** list both Studio and GIT repository. Apply Remote Changes is Studio-only. Note the page is `Legacy -` prefixed |
| 14 | Features available to Global applications (Q187) | "ATF + Source Control" vs "ATF + Flow Designer" | **ATF + Flow Designer**, flagged ⚠️ | Delegated Development and scope protection are scoped-app features; the other two are the defensible pair |
| 15 | Incorrect statement about Delegated Development (Q183) | "grants security record access" vs "non-admins develop global apps" | **Non-admins developing global apps**, flagged ⚠️ | Corroborated: `t_AddADeveloper.md` states "Developer permissions are available only for scoped apps, not global apps" |
| 16 | Cross-scope access on by default for which file type | Script Include vs REST message vs Table | **Excluded from the bank** | Three-way conflict |
| 17 | Table creation methods | Included "Using Flow Designer" | **Excluded** | Flow Designer does not create tables; the dump key is wrong |
| 18 | Form Designer true/false statements (Q91) | Four mutually contradictory keys across five sources | **Kept one defensible version only** | The rest were dropped rather than guessed |
| 19 | Which is NOT supported by Flow Designer (Q194) | "MetricBase Trigger" vs "Test a flow with rollback" | **Testing with rollback** — this bank originally keyed MetricBase and was **wrong** | `flow-test.md`: "Because testing a flow creates or changes records on the instance, flow designers should always test flows on a non-production instance." MetricBase is a documented, supported trigger with its own page |
| 20 | Objects in an Inbound Email Action (Q134) | "current and email" vs "current and event" | **Question replaced.** The docs list **four** objects, so both pairs were correct and the item was unanswerable | `t_CreatingAnInboundEmailAction.md` script template: `runAction(current, event, email, logger)` |
| 21 | Run Trigger "Always" (Q204) | Keyed "Always" | **Question replaced.** "Always" is the *previous-release* name for "Only if not currently running", so two options were the same thing | `flow-triggers.md`: "This behavior is the same as the **Always** option in previous releases." |
| 22 | `gs.hasRoleExactly()` (Q109) | Two dumps keyed it as the answer | Answer unchanged (`gs.hasRole`), but **the reasoning was wrong**: `gs.hasRoleExactly()` **does not exist** | Scripting Security reference: `g_user` has hasRole/hasRoleExactly/hasRoleFromList/hasRoles; `gs` has only `hasRole()` |
| 23 | Preventing reports on sensitive list columns (Q28/Q29) | Two readings: the `report_view` ACL, or the `add_to_list` ACL plus its property | **`add_to_list` plus the property** | `column-view-access-control-list-reports.md`: "the **glide.report.add_to_list_supported** system property enables the **add_to_list** access control list. This access control list (ACL) prevents users from reporting on list report columns with sensitive data" — and, for the field-selection case, "If a table field is restricted for the user, it doesn't appear in the **Available** column" |
| 24 | "Workflow Studio" and "Creator Studio" are invented names (was in Q2's reasoning) | Asserted by this bank | **False on both counts** | `build-workflows/workflow-studio/` and `application-development/creator-studio/` are both current products; `low-vs-pro-code.md` lists five distinct builders. The bank cited the Workflow Studio path elsewhere while calling it invented |

### On sources that advertise "real exam" questions

A dedicated search was run for genuine first-person exam recall — Reddit "I just passed" threads,
ServiceNow Community experience posts, blog writeups. **It found none.** What it found instead were
dump sites whose *marketing copy* says "actual exam questions" while serving the same recycled pool as
everyone else, with **worse** answer keys. Concretely, from one such "verified actual questions" site:

| Their question | Their key | Actual answer |
|---|---|---|
| "What do you install to add applications or functionality?" | Patch, Update Pack, App Package | **Plugin** |
| "When evaluating Access Controls, ServiceNow searches and evaluates:" | Only for matches on the current table | **Most specific to most generic** |
| "Which ATF test step sets up a specific user profile?" | Create a user | **Impersonation** (every other source agrees) |

The single clearest illustration is the ACL debug-order question. Across sources it has been keyed
**all four possible ways**:

| Source | Keyed answer |
|---|---|
| marks4sure | Conditions, Roles, Script |
| cciedump | Roles, Conditions, Script |
| study4exam | Roles, Conditions, Script |
| pass4success ("actual exam questions") | Script, Conditions, Roles |
| **Official ServiceNow documentation** | **Role → Security Attribute → Condition → Script** |

That is not a question with a disputed answer; it is a question whose answer has been copied wrong
repeatedly. This bank keys it from the documentation and flags it (Q98).

---

## Blueprint: resolved

The official CAD exam specification (KB0011498) confirms the six domains at
**20 / 20 / 20 / 20 / 10 / 10**, with exactly the domain names used here. The alternative split
(5/20/10/20/20/25) circulated by several prep sites is **wrong**.

Three further facts from the official spec that change how this bank should be read:

1. **The cut score is not 70%.** The spec states the score "is not publicly shared and is not always
   70%". Any pass/fail framing based on 70% is wrong. The app reports a raw score with 80% as a stated
   *working target*, not a pass line.
2. **Multi-select gives no partial credit**, which matches this bank's all-or-nothing scoring.
3. **ServiceNow explicitly says study material posted elsewhere online is not official and should not
   be used to prepare.** That includes every dump site mined here. It is the strongest argument for the
   verification passes in this document, and for preferring `v2`, `authored` and `docs` over `web`.

The spec also publishes **four sample questions**. Three are reproduced with ServiceNow's own keys and
tagged `docs`. The fourth was published without its answer options, so it appears as an `authored`
question on the same topic rather than a guess.

## Coverage against the blueprint

| Domain | Weight | Questions | Exam sim draw |
|---|---|---|---|
| 1 Designing and Creating an Application | 20% | 46 | 12 |
| 2 Application User Interface | 20% | 59 | 12 |
| 3 Security and Restricting Access | 20% | 44 | 12 |
| 4 Application Automation | 20% | 75 | 12 |
| 5 Working with External Data | 10% | 35 | 6 |
| 6 Managing Applications | 10% | 23 | 6 |

The bank is deliberately **not** quota'd to the blueprint — it is a study pool, and depth is worth more
in the domains with the most script detail. The **exam simulation** is what enforces the weighting, and
it draws 12/12/12/12/6/6 regardless of how the pool is distributed.

## Known gap — the largest remaining risk

All questions originally mined from practice sites start as `web`. As each is adjudicated against the
documentation it is retagged **`web+docs`** — so the two counts are a progress bar:

| | Count |
|---|---|
| `web+docs` — checked against the documentation | 26 |
| `web` — **not yet checked** | 102 |

The 102 are *unquestioned*, not *verified*. They are concentrated in **Domain 4 (43)** and
**Domain 3 (19)**. **Every answer correction found in this project so far came from that pool** —
three outright wrong keys, plus several correct answers carrying false reasoning, which is the more
insidious failure. Working through the remainder is the highest-value job left on this bank.

---

## Rebuilding

```bash
python "<ServiceNow>/cad-quiz/build-questions.py"
```

The bank and trap sheet are authored in `<ServiceNow>/CAD-questions/` and **copied forward** into
`cad-quiz/questions/` by the build, so the two copies cannot drift. `SOURCES.md` is mirrored too, which
is why this file uses `<ServiceNow>/…` placeholders rather than absolute paths — the build **fails** if
any file under `questions/` contains a local path, because that folder is published.

The build regenerates `cad-quiz/_questions.js` **and inlines the questions directly into
`cad-quiz/index.html`** between the `QUESTIONS:START` / `QUESTIONS:END` markers, so the app stays a
single self-contained file that opens by double-click and can never serve a stale cached copy. It exits
non-zero on any validation error: missing answer row, orphaned answer, out-of-range answer index,
duplicate question number, question with no domain heading, or a local path in a published file.
