# CAD Trap Sheet

> The confusions that actually cost marks. Each row is a pair people mix up, plus the one rule that separates them.
> Read this the morning of the exam. Companion to `CAD-Master-Question-Bank.md`.

---

## 1. The three highest-value instincts

**① If it isn't enforced server-side, it isn't security.**
UI Policy, Client Script, form layout and list layout are all cosmetic. Only an **ACL** survives REST, import sets, and a curious user with a URL. Any question of the form "hide this field from users…" where the stem mentions API/web service/import → the answer is an ACL.

**② Read multi-answer stems for the *count*, then eliminate.**
ServiceNow multi-select questions almost always include one option that is a real feature from a different product area (Advanced Work Assignment, Agent Affinity, Virtual Agent, Machine Learning). Those are filler. Strike them first.

**③ When two options are the same sentence with one word changed, that word is the question.**
"Turn on the **Application Administrator** field" vs "Turn on the **Delegated Application Developer** field". "`max_admin_count`" vs "`min_admin_count`". "`hasRole`" vs "`hasRoleExactly`" — and note `hasRoleExactly` exists only on `g_user`, never on `gs`. Slow down and read the differing token.

---

## 2. Scripting tier — client vs server

| | Client side | Server side |
|---|---|---|
| User object | `g_user` | `gs` (GlideSystem) |
| Form API | `g_form` | — |
| Record | — | `current`, `previous` |
| Query | — | `GlideRecord` |
| Logging | `jslog()`, `g_form.addInfoMessage()` | `gs.log()`, `gs.info()` |
| Abort | `return false` (onSubmit) | `current.setAbortAction(true)` |

**Rules that follow:**
- `gs.*` in a client script → **always wrong**. `gs.log()` is the stock wrong answer for "client debugging strategy".
- **`GlideRecord` is not the client/server tell — `gs` is.** GlideSystem never appears in the client API listing. A **client-side GlideRecord API does exist** ("enables the use of *some* GlideRecord functionality in client-side scripts, such as client scripts and UI policy scripts"); it is *discouraged* for performance, which is not the same as unavailable. Reach the server with **GlideAjax** + a client-callable Script Include.
- **`GlideDialogWindow` is documented as deprecated.** If a question asks which client API is deprecated, that is the one.
- **The two role APIs are not symmetric.** Client `g_user` has `hasRole()`, `hasRoleExactly()`, `hasRoleFromList()`, `hasRoles()`. Server `gs` has **only `hasRole()`**.
- So `gs.hasRoleExactly()` **does not exist** — in a Business Rule the answer is always `gs.hasRole('admin')`. `g_form` has no role methods at all.
- `g_user.hasRole('x')` returns **true for admin too**; `g_user.hasRoleExactly('x')` does not. `hasRoleOnly` does not exist.
- In an **ACL script**: `gs.hasRole()` and `current.isNewRecord()`. Note **`isNewRecord()`**, not `isNew()`.
- `gs.getUserName()` = login name. `gs.getUserDisplayName()` = First Last. **`gs.getUserID()` = sys_id.**
- **`gs.getUserSysID()` does not exist.** The whole set is `getUser()`, `getUserDisplayName()`, `getUserID()`, `getUserName()` — plus `getUserNameByUserID()` in global scope only. Same species of trap as `gs.hasRoleExactly()`: a name that reads right and was never real.

---

## 3. Business Rule `when`

| when | Runs | Has `previous`? | Signature use |
|---|---|---|---|
| **display** | Before the form is shown to the user | **No** | Populate `g_scratchpad` |
| **before** | After submit, before DB write | Yes | Validate / modify `current`, abort |
| **after** | After DB write, same transaction | Yes | Update related records |
| **async** | After transaction, scheduled | Yes | Heavy work; **cannot trigger on query** |

- `g_scratchpad` flows **server → client**, set in a **display** rule, read in a client script on form load.
- The Business Rule template is a **self-invoking anonymous function** — the trailing `()` is what makes "self-invoking" the keyed answer.
- Multiple rules on the same table/operation run in ascending **Order**.
- No-script Business Rule Actions: **Set field values** and **Add message**. That's it.

---

## 4. ACLs — the deep end

**Order within one ACL:** Role → Security Attribute → Condition → Script.
⚠️ Legacy course material taught "**Conditions, Roles, Script**" and dumps still key it that way. Current docs say role-first. **If a role-first option is offered, take it.**

**Matching order across ACLs:** most specific → most generic. The documented sequences are exact:

- **Table rules:** `incident` → parent table `task` → `*`
- **Field rules:** `incident.number` → `task.number` → `*.number` → `incident.*` → `task.*` → `*.*`

So **`table.*` is a *field* rule** — the catch-all for fields on that table, evaluated *fourth*, after
`*.field`. The record-level rule is `table` on its own (shown as `.None`).

**The first successful field ACL stops field-level processing.** Once a field rule passes, no other
field rule is consulted for that field.

**Both must pass:** the matching table-level rule **and** the matching field-level rule. Fail the
table rule and you are denied **every** field, even ones whose field rule you would have passed.
That single sentence is what separates Q107 from Q217 — check whether a `table.*` row exists before
working out which fields are readable.

**Operation is `write`, not `update`.** Full documented record-operation list: `create`, `read`,
`write`, `delete`, `execute` (client-callable script includes and REST endpoints), `list_edit`,
`report_on`, `report_view`, `add_to_list`, `personalize_choices`, `save_as_template`, `query_match`,
`query_range`, `edit_task_relations`, `edit_ci_relations`. Note **`add_to_list` supports neither
conditions nor scripts.**

| Situation | Result |
|---|---|
| ACL is **empty or invalid** | **Denied** |
| **No matching ACL at all** | **Granted** (rare in practice — default rules exist) |
| Required roles list is **empty** | Role check evaluates **true** |
| Deny-Unless passes, no Allow-If matches | **Granted by default** |

**Invalid ACL** = role that doesn't exist · security attribute that doesn't exist · script that is just `answer=true`/`true`.
An **inactive** role is still a *valid* reference — valid but ineffective. Not the same thing.

**Decision types:** Deny-Unless is evaluated **first** (secure by default). Deny-Unless = denied *unless* conditions met. Allow-If = allowed *if* conditions met.

**Naming:** `table.None` = table/record level. `table.*` = all rows **and** all fields.

**Auto-created on a new custom table:** read, create, **write**, delete — **four**, one per CRUD operation. (`execute` is not generated for a data table.)

**Pre-query check = roles only** (no record data yet). Post-query = roles + conditions + script.

**`glide.sm.default_mode`** controls wildcard-table deny/allow. Once set to **Deny Access it cannot be reverted**. Doesn't affect report_on / personalize_choices.

**Report ACLs — the pair that trips everyone:**
- `add_to_list` → can the user **pick this field as a report column**
- `report_view` → can the user **see the report once built**
- A report *grouped by* a restricted field is blocked entirely — you can't just hide a grouping column.

---

## 5. Scope and cross-scope

| Concept | Table | What it is |
|---|---|---|
| Cross-scope **privilege** | `sys_scope_privilege` | Runtime: can this script touch that resource |
| **Restricted caller access** | `sys_restricted_caller_access` | Tracks/approves cross-scope callers |

- **Runtime access tracking:** *Tracking* = log but allow. *Enforcing* = only allow with a valid privilege record.
- Cross-scope operations: **tables** support read/write/create/delete; **script includes and script objects support `execute API` only.**
- Caller access options: Caller Tracking, Caller Restriction, None. ("Caller Permission" doesn't exist.)

**Application Access defaults for a new table:** Accessible from = *All application scopes*, **Can read = enabled**, create/update/delete = disabled, **web services = enabled**.
⚠️ A widely-copied dump claims the baseline is "only in-scope artifacts can read". The documentation says otherwise.

- **Can write / create / delete are each only available once Can read is selected.** Web services access is independent of Can read.
- "Allow access via web services" still requires the user to have proper permissions.
- **"Allow configuration"** = out-of-scope applications may create configuration records (e.g. Business Rules) against your table.

**Script protection policy:** None (editable) · **Read-only** (visible, not editable) · **Protected** (IP hidden).

**Prefixes:** `u_` = custom table in **global** scope. `x_<namespace>_` = table in a **scoped** app.

---

## 6. Client-side artifact chooser

| Requirement | Use |
|---|---|
| Mandatory / read-only / visible, no code | **UI Policy** |
| Same rules enforced on **import and web services** too | **Data Policy** |
| React to a field change on a **form** | Client Script `onChange` |
| React to a change in a **list** | Client Script `onCellEdit` |
| Block submission | `onSubmit` returning **false** |
| Call server logic from the client | **GlideAjax** + script include with **Client callable** ✓ **and** extends `AbstractAjaxProcessor` |
| Server data available at form load without a round trip | **display BR → `g_scratchpad`** |

- UI Policies run **after** client scripts on load. Within a UI Policy, **Scripts execute before Actions**.
- **Record Producers use *Catalog* Client Scripts and *Catalog* UI Policies** — not the ordinary form ones.
- In a Record Producer script: **`current`** = the record being created; **`producer.<variable>`** = what the user typed.
- Fastest way to build a Record Producer for an existing table: the table record's **Add to Service Catalog** related link.
- **UI Action types include "List choice". There is no "Form choice."**

---

## 7. Automation

- **Flow triggers:** Record, Schedule, Application, Inbound Email, MetricBase, inbound API. **Outbound Email is NOT a trigger** — it's an action.
- Action output is stored in a **Data Pill**.
- A scoped app bundling flow actions = **Spoke**. Action = one step; Flow = the sequence.
- Workflow **version** = the design. Workflow **context** = the running instance.
- `gs.eventQueue()` events are consumed by **Script Actions** and **Email Notifications**. *Not* Scheduled Script Executions, *not* UI Policies.
- **Script Action:** no `previous`. **Scheduled Script Execution:** no `current` (nothing triggered it) — you get GlideSystem and GlideRecord.
- **Inbound Email Action:** **four** objects — `current`, `event`, `email`, `logger`. (A common exam item asks you to pick one *pair*; the docs list all four, so watch for a flawed question.)
- Inbound email is matched to a record by **watermark**.
- Email Notification event property syntax: `${event.<property>}`.
- **Weight = 0 means the notification is ALWAYS sent** when criteria are met. Only the highest-weight notification is sent for the same record+recipients. Default is 0.
- A **Utils Script Include** is table-agnostic — "identify the table" is *not* one of its steps.
- **Run Trigger options** (record trigger): *For each unique change* · *Once* · *Only if not currently running* · *For every update*. **"Always" is the old name for *Only if not currently running***, so a stale question offering "Always" means that one. Fires on **every** update regardless of running contexts = *For every update*.
- Application Properties exist so you can change behaviour **without modifying artifacts**. Reached via a module of link type **URL (from Arguments)**.

---

## 8. Data model

- Extending Task inherits fields **and** behaviour, and records show up in Task-level lists/reports. Parent ACLs are evaluated.
- **Records are NOT copied** to the child table when you extend.
- **Inherited fields cannot be deleted** from a child table.
- Editing a field **label** on a child table affects the **child only**.
- Many-to-many creates an **intermediate table**. Details live in **`sys_m2m`**; browse base-system ones at **`sys_collection.list`**.
- **Reference** = one record. **Glide List** = many records, one table. **Document ID** = target table resolved at runtime by a companion field.
- Adding a field to a table does **not** add it to the list view.
- Schema map = graphical view of table relationships.
- Table creation methods: upload a spreadsheet · extend a table · create a custom table.

---

## 9. Data in / integration

- Three steps: **Load data → Create Transform Map → Run Transform.** (Loading is always first — you can't select an import set that doesn't exist.)
- **Data Source** = where data comes from. **Import Set table** = staging. **Transform Map** = field mapping.
- **Coalesce** = match field. Match → **update**. No match → **insert**.
- **No coalesce field → every run inserts duplicates.**
- ServiceNow requesting data from outside = **consumer**. Serving data = **provider**.
- REST Message **Endpoint** = the URI of the data.
- **REST API Explorer** builds sample code for *ServiceNow's own* REST requests — it is not a sandbox for third-party APIs.
- Custom inbound endpoint with custom logic = **Scripted REST API**.
- **Dot walking** pulls fields from a related table onto a report.

---

## 10. Managing applications

- **Update Set** = move config between environments. **Application Repository** = distribute a versioned app. **Store** = third-party. **Share** = community.
- There is **no "Copy button"** install method.
- To see what ships with an app: the **Application Files** related list on the application record.
- App **data** ships only when records are added via **Create Application Files**.
- Git link needs **user name + password + URL**. **Application name is not required.** Behind a firewall → **MID Server**.
- **Stash** = shelve local changes. Branch = parallel line. Tag = marker.
- Delegated developers package changes with the **Publish** button.
- Without App Collaborator, add delegated developers at **Application record > Manage Developers**.
- Make a role eligible as Application Administrator: turn on the **Application Administrator** field on the role record.
- **`min_admin_count`** sets the floor. Below the floor you can only **add**.
- Application Picker shows **all custom scopes plus Global**, and selecting one **sets the scope**.
- Application scoping does **not** track who developed an app.

---

## 11. Studio, navigation and templates

- **Studio defaults:** a new app gets a **user role** and an **admin role**. Nothing else is generated.
- **Studio status bar** shows the two things that silently misfile your work: **current scope** and **update set**. (An earlier version of this sheet also claimed scope appears in the **browser tab title** — that is not in the documentation and has been removed.)
- **Studio is one environment for create / review / update** of app files, in **any scope you can access**, with **source control** and **code search**. It is browser-based, so "offline development" is always wrong.
- **Five builders, all real** — Creator Studio (no-code) · App Engine Studio (low-code) · ServiceNow Studio (mid-code) · ServiceNow IDE + SDK (pro-code). "Workflow Studio" and "Creator Studio" are **not** invented names. If a stem asks which one is "an IDE", note that **ServiceNow IDE** is now its own product, so treat any Studio-vs-IDE item with suspicion.
- **Next Experience:** **All menu** = reach any item · **contextual application pill** = where you are, and favorite it. Favorites and History are for things you already saved or visited.
- **AES template roles:** `app_template_author` = share **their own** templates. `app_template_admin` = review/activate/deactivate/share **all** templates.
- **Formatter** = shows something on a form that is **not a field**. **Embedded list** = view and edit related records inline.
- **`sys_m2m`** = the Many to Many Definitions table, where you **create** relationships. **`sys_collection.list`** = where you **browse the ones that ship in the base system**. One creates, one views.
- **Delegated developers** are added from the application record via **Manage Developers** (it reads **Manage Collaborators** when the App Collaboration Component is installed), and only for **scoped** apps — never global.

---

## 12. Form logic, testing and automation

- **UI Policy vs Client Script:** both can make a field read-only, mandatory or hidden. The documented tie-breaker is **prefer the UI policy, for faster load times**. A UI policy condition **evaluates fields that are not on the form layout at all**.
- **UI Policy vs Data Policy:** a UI policy guards the **form**; a data policy guards the **data whichever route it arrives by**, including import sets and SOAP. Converting a UI policy to a data policy **deactivates the UI policy** — tick **Use as UI Policy on client** to keep it working on the form. Conversion requires Run scripts **off**, Global **on**, and every action's Visible set to **Leave Alone**.
- **ATF vs flow testing — the pair to memorise.** An ATF test **rolls back the data it creates**. Testing a flow **does not** — it "creates or changes records on the instance". Both belong on a non-production instance; only one cleans up after itself.
- **Record Producer vs Catalog Item:** a record producer creates a **task-based record** (an incident). A catalog item creates a **requested item**. Never use a record producer for requested items, or the standard catalog workflows will not run.
- **Event vs Scheduled Script Execution:** an event is **consumed** by **Script Actions and Email Notifications**, and only once it has been **registered** in the event registry. A scheduled job runs **on a clock** — it never subscribes to the event queue, so it is never the answer to "what responds to this event".
- **Scheduled job states:** **Ready** = will run at the next interval · **Queued** = already in the scheduler queue, waiting · Running · Error. Ready and Queued are the pair that gets swapped.
- **`gs.getProperty()` returns a String.** A property holding the text `"false"` is a **non-empty string, therefore truthy** — `if (gs.getProperty('x'))` runs the block. Compare with `=== 'true'`.
- **Never call `current.update()` in a Business Rule** — it forces an extra database write, causing duplicate notifications and recursive loops. In a *before* rule, just set the field.
- **Script Include over global Business Rule.** When a UI Action and a Scripted REST API need the same logic, put it in a **Script Include** and call it from both — never chain one artifact to the other.
- **Display Business Rule** is the one that populates **`g_scratchpad`** for client scripts — and the one with **no `previous` object**, because nothing has been saved yet.
- **Reporting on sensitive columns:** `add_to_list` ACL (plus the `glide.report.add_to_list_supported` property, which is **off by default**) stops a field being **picked** as a report column. `report_view` controls whether you can **see** it once the report exists.

---

## 13. Final 60 seconds

- Multi-answer? Count the required answers and make sure you selected exactly that many.
- "NOT" / "EXCEPT" in the stem? Re-read — you're looking for the false one.
- Security question? Ask "would this survive a REST call?"
- Two near-identical options? The differing word is the answer.
- Genuinely unsure on an ACL question? **Deny / most-restrictive** is the better guess — except for "no matching ACL", which grants.
