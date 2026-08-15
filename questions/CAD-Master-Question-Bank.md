# ServiceNow CAD — Master Question Bank

> **Exam:** Certified Application Developer (mainline) · 60 questions · 90 minutes
> **Blueprint:** Official exam blueprint KB0011498 — six domains at 20/20/20/20/10/10
> **Built:** 2026-08-11 · **Last revised:** 2026-08-14

## How to read this bank

| Marker | Meaning |
|---|---|
| `⭐` | **A sample question ServiceNow publishes in the official exam specification (KB0011498).** Exactly three questions carry this. Nothing else is starred. |
| `⚠️` | Answer could not be fully settled against current docs — read the `Why` before trusting it. |
| `Src` column | Where the question came from. Use it to filter. |

**Src vocabulary:** `v2` · `authored` · `docs` · `web+docs` · `web` · `official`

### Which sources to trust

`v2` is the newest set, written directly from the Australia-release documentation, and **every answer
cites the page that settles it** — the one item that could not be settled says so in its `Why`.
`docs` and `authored` are also documentation-derived. `official` is ServiceNow's own published samples.

`web` is the weak tier: mined from practice sites, which contradict each other constantly and are
wrong often enough that every correction found in this project so far came from that pool. Roughly a
hundred `web` items have never been checked against the documentation — they are *unquestioned*, not
*verified*. Treat a `web` answer as a prompt to think, not as an authority.

---

## Domain 1 — Designing and Creating an Application (20%)

> Determine if an application is a good fit for ServiceNow · Design and implement a data model · Create modules · Use Application scope

**Q1.** You create a new application in ServiceNow Studio and reach the step for defining who can access it. Which roles has Studio already generated for you? *(Choose 2)*
- A. An admin role
- B. An approver role
- C. A user role
- D. A read-only role

**Q3.** A platform developer wants to create app files, edit metadata, and package the application for deployment without leaving a single environment. Which tool is built for that?
- A. Application Repository
- B. ServiceNow Studio
- C. Platform Analytics
- D. Instance Scan

**Q4.** You have an application file open in ServiceNow Studio. Which two pieces of context does the status bar display? *(Choose 2)*
- A. The application scope
- B. The update set the changes are being captured into
- C. The Git branch the application is linked to
- D. The delegated developer assigned to the file

**Q5.** Which two are capabilities of ServiceNow Studio? *(Choose 2)*
- A. Opening and editing files in any scope you have access to, including global
- B. Developing an application while disconnected from the instance
- C. Linking an application to a source control repository
- D. Encrypting scripts so that other developers on the instance cannot read them

**Q8.** ServiceNow Studio gives you one place to do which three things with application files? *(Choose 3)*
- A. Create them
- B. Review them
- C. Update them
- D. Automatically generate test suites for them
- E. Translate them into other languages
- F. Attach them to a change request

**Q10.** Which table stores the definitions of custom many-to-many relationships?
- A. sys_m2m
- B. sys_collection
- C. sys_relationship
- D. sys_m2m_definition

**Q11.** An administrator wants to browse the many-to-many relationships that ship with the base system. What should they enter in the navigation filter?
- A. sys_m2m.list
- B. sys_collection.list
- C. sys_relationship.list
- D. sys_m2m_base.list

---
### Domain 1 — Answers

| Q | Answer | Src | Why |
|---|--------|-----|-----|
| Q1 | A & C | authored | **Admin and user.** `servicenow-studio-classic/create-an-application-in-servicenow-studio.md`: "ServiceNow Studio automatically defines default admin and user roles. You can remove the predefined roles or add more roles." Approver and read-only roles exist only if you author them. Corroborated by `app-engine-studio/app-tutorial-create-an-app.md`. |
| Q3 | B | authored | **ServiceNow Studio.** `servicenow-studio-classic/exploring-servicenow-studio.md` states the point twice: "manage app files, edit metadata, and package changes for deployment **without switching between tools**." Application Repository *distributes* finished apps rather than building them; Platform Analytics and Instance Scan are unrelated. |
| Q4 | A & B | authored | **Scope and update set.** `servicenow-studio-classic/servicenow-studio-user-interface.md`: "When you have an app or file open, the status bar shows the current scope and the update set associated with the application." These are the two settings that silently misfile your work when wrong. |
| Q5 | A & C | authored | **Any-scope editing and source control.** `exploring-servicenow-studio.md` lists "Global and custom scope: Open and edit files of any scope you have access to"; source control has its own page (`link-app-to-source-control.md`). **Trap on D:** a Script Protection Policy genuinely exists (`c_ScriptProtectionPolicy.md`), but it protects scripts in *published store apps* — it is not a Studio feature and does not hide code from developers on your own instance. Studio is browser-based, so B is impossible. |
| Q8 | A, B & C | authored | **Create, review, update.** `exploring-servicenow-studio.md`: "Create, edit, maintain, and deploy custom, globally scoped, and base system apps and app files." Test generation, translation and change-request attachment are other tools' jobs. |
| Q10 | A | authored | **`sys_m2m`.** `platform-administration/table-administration-and-data-management/t_CreateAManyToManyRelationship.md`: "The Many to Many Definitions `[sys_m2m]` table allows administrators to create custom many-to-many relationships." |
| Q11 | B | authored | **`sys_collection.list`.** `r_RefDefaultManyToManyRels.md`: "To reference many-to-many relationships that are available in the base system, administrators can enter `sys_collection.list` in the navigation filter." **Trap:** Q10 and Q11 are a deliberate pair — the same doc adds "Only use this table to view many-to-many relationships in the base system. To create a new relationship, always use the Many-to-Many Definitions table." So `sys_m2m` = create, `sys_collection` = view what already ships. |

---

## Domain 2 — Application User Interface (20%)

> Create, design, and customize forms · Add/remove fields from forms and tables · Client-side scripts for desktop · Server-side scripts · Record Producer as an application's UI

**Q12.** What does a formatter put on a form?
- A. Information that is not a field on the record
- B. A read-only copy of a field from a referenced record
- C. A calculated value derived from two or more fields
- D. A validation message raised when the form fails to save

**Q13.** What does an embedded list let a user do?
- A. View and edit related records without navigating away from the form
- B. Export the form's data to a CSV file
- C. Display a field from a referenced record inline
- D. Attach a document to the record

**Q15.** In the Next Experience navigation, which element do you open to reach any item in the instance?
- A. The contextual application pill
- B. The All menu
- C. The Favorites menu
- D. The History menu

**Q16.** In the Next Experience navigation, which element shows you where you currently are in the instance and lets you favorite the item you are viewing?
- A. The History menu
- B. The All menu
- C. The contextual application pill
- D. The Favorites menu

---
### Domain 2 — Answers

| Q | Answer | Src | Why |
|---|--------|-----|-----|
| Q12 | A | authored | **Information that is not a field on the record.** `platform-administration/c_Formatters.md`: "A formatter is a form element used to display information that is not a field in the record." Activity stream, Approvers and Process Flow are all formatters. Worth knowing: a *custom* formatter is a UI macro plus a formatter record that points at it. |
| Q13 | A | authored | **View and edit related records inline.** `platform-user-interface/configure-use-list-functions.md`: "Some lists may be embedded in forms. Use list controls to work with records in an embedded list within a form" — you can insert, expand and collapse rows without leaving the form. **Trap on C:** displaying a single field from a referenced record is a *derived/dot-walked field*, not an embedded list. |
| Q15 | B | authored | **The All menu.** `platform-user-interface/adoption-services/configure-next-experience-onboarding.md` enumerates the Next Experience elements as Intro/welcome, Pinning, **All menu**, Favorites menu, History and **Application Pill** — so All menu and the pill are distinct things. All menu is the full catalogue of everything in the instance. |
| Q16 | C | authored | **The contextual application pill.** Same source as Q15. Q15/Q16 are a matched pair and cannot share an answer: *reach anything* = All menu; *where am I, and favorite it* = application pill. Favorites and History are for items you already saved or visited. |

---

## Domain 3 — Security and Restricting Access (20%)

> Restrict access to applications and modules · Manually and automatically create, test, and debug Access Controls · GlideSystem methods for script security · Application scope to protect application artifacts

**Q22.** Deny-Unless access controls are evaluated before Allow-If access controls. What does that ordering achieve?
- A. The instance restricts by default, so a failing Deny-Unless blocks the request before anything can grant it
- B. Access control evaluation completes in fewer database queries
- C. Roles assigned directly to a user outrank roles inherited from a group
- D. Idle user sessions are terminated sooner

**Q23.** The access control engine encounters a rule that is empty or invalid. What does it do by default?
- A. Grants access for the remainder of the session
- B. Falls back to a system-supplied default rule
- C. Denies access
- D. Sends an approval request to an administrator

**Q24.** Which statement describes both access control decision types correctly?
- A. Deny-Unless denies access unless its requirements are met; Allow-If grants access if its requirements are met
- B. Deny-Unless denies access unconditionally; Allow-If grants access unconditionally
- C. Deny-Unless grants access by default; Allow-If ignores its conditions entirely
- D. Both grant access as soon as any one requirement is present

**Q25.** An administrator builds an access control but specifies neither a role nor a security attribute. What does the system do?
- A. Prompts them to select a role or an existing security attribute
- B. Saves the record and writes a warning to the system log
- C. Refuses to save the record at all
- D. Assigns the admin role automatically

**Q26.** Which access control decision type is evaluated first?
- A. Allow-If
- B. Deny-Unless
- C. Rules that specify a script
- D. Rules that specify no role

**Q27.** Which of these makes an access control *invalid*, rather than merely restrictive?
- A. It requires a role that exists but is currently inactive
- B. It references a security attribute that has no record in the database
- C. It requires a role that no user currently holds
- D. Its condition evaluates to false for every record on the table

**Q28.** Which two together stop users from reporting on list report columns that hold sensitive data? *(Choose 2)*
- A. The report_view table access control
- B. The add_to_list access control
- C. Setting the glide.report.add_to_list_supported property to true
- D. The read operation access control
- E. Setting the glide.report.report_view.check_published property to true

**Q29.** A manager wants to stop users from picking the caller_name field as a column when they build a new report. Which operation's access control does that?
- A. report_view
- B. add_to_list
- C. list_edit
- D. read

**Q32.** Which two are documented benefits of Access Analyzer? *(Choose 2)*
- A. It provides reporting capabilities for the analyzer's results
- B. It helps you achieve least-privilege when implementing access controls
- C. It encrypts sensitive field data at rest
- D. It records which pages anonymous users were able to reach
- E. It replaces access controls with a role-only permission model

---
### Domain 3 — Answers

| Q | Answer | Src | Why |
|---|--------|-----|-----|
| Q22 | A | authored | **Secure by default.** `platform-security/access-control/acl-denial-behavior.md`: "Deny-Unless ACLs will take priority against Allow-If ACLs in ACL Evaluation, as it will be evaluated first." Putting the restrictive type first means a failing Deny-Unless vetoes the request before any Allow-If gets a chance to grant it. B, C and D invent performance and session rationales. |
| Q23 | C | authored | **Deny.** `exploring-access-control-list.md`: "By default the ACL engine completely denies access if an ACL is empty or invalid." ServiceNow fails closed — the single most reliable access-control principle on this exam. An ACL counts as *empty* when it lacks a role, security attribute, data condition **and** script. |
| Q24 | A | authored | Read it literally. `exploring-access-control-list.md` defines Deny-Unless as "restrict access to resource by explicitly denying access unless conditions are passed" and Allow-If as "allow access to resource if conditions are passed." A restates both; B, C and D each break one half. |
| Q25 | A | authored | **It prompts you.** `exploring-access-control-list.md`: "If the system detects the user creating an ACL it will prompt the user to select a role or an existing security attribute." It neither blocks the save (C) nor silently accepts it (B) nor guesses a role (D). |
| Q26 | B | authored | **Deny-Unless.** Same source as Q22, asked as sequence rather than rationale. C and D are not decision types — they describe what an individual rule contains. |
| Q27 | B | authored | **A security attribute with no database record.** `exploring-access-control-list.md` defines invalid ACLs as those with roles that do not exist, security attributes that do not exist, or a script containing `answer=true` or `true`. **The discrimination:** invalid means *unresolvable*, not *ineffective*. An inactive role, an unheld role and an always-false condition are all valid references that simply grant nobody access. |
| Q28 | B & C | authored | **The add_to_list ACL plus its enabling property.** `now-intelligence/reporting/column-view-access-control-list-reports.md`: "the glide.report.add_to_list_supported system property enables the add_to_list access control list. This access control list (ACL) prevents users from reporting on list report columns with sensitive data." The property is inactive by default, so the ACL alone does nothing. **Trap on E:** `glide.report.report_view.check_published` is a real property (`sc-enable-report-view-acls.md`) but it governs *viewing published reports*, not *building* them. |
| Q29 | B | authored | **add_to_list.** Same doc: "If a table field is restricted for the user, it doesn't appear in the Available column. Users are therefore not able to select it in the reports they create." Learn the split — `add_to_list` = can you pick the field while building; `report_view` = can you see it once built. Two limits worth knowing: the ACL applies only to the top-level table the report is based on, and existing reports are unaffected. |
| Q32 | A & B | authored | Both are listed verbatim under Benefits in `platform-security/access-control/explore-access-analyzer.md`: "Provide reporting capabilities for the analyzer results" and "Achieve the least privilege principals when implementing access controls." Note the tool's current scope — it validates access for resources **and agentic assets** (agentic workflows and AI agents), which is a rebuild from earlier releases. |

---

## Domain 4 — Application Automation (20%)

> Write, test, and debug Workflow and Flow Designer · Create and use Application Properties · Create Events, Scheduled Script Executions (Scheduled Jobs), and Utils (application) Script Includes · Send and receive email

---
### Domain 4 — Answers

| Q | Answer | Src | Why |
|---|--------|-----|-----|

---

## Domain 5 — Working with External Data (10%)

> Import data in CSV or Excel format · Integrate to, including testing and debugging, an external data source using REST

*No questions from local sources yet — this domain is filled in the web-mining and authoring passes.*

---

## Domain 6 — Managing Applications (10%)

> Download and install applications · Use Delegated Development to manage source code and code review · Use the ServiceNow Git integration to manage source code

**Q34.** On an instance where the App Collaboration Component is *not* installed, where do you go to grant someone delegated developer permissions on an application?
- A. The application record, then Manage Developers
- B. The application record, then Roles Required
- C. The role record, then Subscribed Users
- D. The System Applications menu, then Delegated Developers

**Q35.** Which action on a role record makes that role usable as an application-specific administrator?
- A. Add the role to the Application Administrator related list
- B. Select the Application Administrator check box and update the role record
- C. Add the role to an Application Administrator group
- D. Select the Delegated Application Developer check box and update the role record

**Q36.** Which property name sets the minimum number of application administrators an application must retain?
- A. admin_count
- B. num_admin
- C. max_admin_count
- D. min_admin_count

**Q37.** An application requires a minimum of four application administrators. It currently has two. What can be done?
- A. Two or more application administrators can be added
- B. Exactly one application administrator can be added
- C. One application administrator can be removed
- D. All but one application administrator can be removed

**Q38.** In App Engine Studio, which role can assign sharing permissions for the templates that user creates?
- A. sn_app_eng_studio.user
- B. app_template_author
- C. app_template_admin
- D. scan_admin

**Q39.** In App Engine Studio, which role can review templates, activate and deactivate them, and assign sharing permissions across *all* templates?
- A. app_template_author
- B. delegated_developer
- C. app_template_admin
- D. scan_admin

---
### Domain 6 — Answers

| Q | Answer | Src | Why |
|---|--------|-----|-----|
| Q34 | A | authored | **Application record → Manage Developers.** `delegated-development-and-deployment/t_AddADeveloper.md` walks it: All > System Applications > My Company Applications, open the application, "Select **Manage Developers**. **Note:** If the App Collaboration Component is installed, the link appears as **Manage Collaborators**." Two facts worth carrying: developer permissions exist **only for scoped apps, not global**, and if Application administration is enabled only an application administrator can delegate. **Trap on B:** Roles Required governs who can *use* the app, not who can *develop* it. |
| Q35 | B | authored | **Select the Application Administrator check box.** `application-administration.md`: "You can make any role an application-specific administrator by selecting the **Application Administrator** check box in Role Configuration." `enable-application-administration.md` adds that this check box replaced the older **Assignable by** field. D is the same sentence with a fabricated field name — read these options word by word. |
| Q36 | D | authored | **`min_admin_count`**, namespaced to the application's scope — e.g. `sn_uni_task.min_admin_count`, documented as ensuring "a minimum number of scoped administrators are active at any given time for managing the application" (`employee-service-management/universal-task/assign-ut-admin-role.md`). `max_admin_count` is the mirror-image trap; there is no cap, only a floor. |
| Q37 | A | authored | **Add two or more.** The count is *below* the configured minimum, so the only permitted direction is up, and it takes at least two to reach four. Every removal option is blocked — the whole point of the property is that the application cannot be locked out by losing its administrators. **Trap on B:** "exactly one" misreads a floor as a quota. |
| Q38 | B | authored | **app_template_author** — authors control sharing for the templates *they* create. `app-engine-studio/manage-template-access.md`. |
| Q39 | C | authored | **app_template_admin** — admins review, activate/deactivate, and control sharing across **all** templates. Same doc. Q38/Q39 are a scope pair: author = own templates, admin = every template. |

---

## Provenance summary

| Src | Questions | Notes |
|---|---|---|
| `web` | 117 | Mined from practice sites. The weak tier — see "Which sources to trust" above |
| `authored` | 95 | Written against the ADF course structure and the Australia-release docs |
| `v2` | 39 | Newest set, written from the documentation; every answer cites its source page |
| `docs` | 15 | Written directly from the Australia-release documentation |
| `web+docs` | 11 | Mined, then corrected against the documentation |
| `official` | 3 | Sample questions ServiceNow publishes in KB0011498 — the only `⭐` items |
| **Total** | **280** | |

**No question in this bank is taken from a ServiceNow exam**, and none should be added. Where a topic
is worth testing, the question is written from the documentation page that defines it, and the answer
cites that page. See `SOURCES.md`.

---

## Domain 1 — Designing and Creating an Application (Practice)

**Q40.** A developer creates a new scoped application with the namespace `x_acme_fleet`. They then create a table named `vehicle` inside that application. What will the actual table name be?
- A. `u_vehicle`
- B. `vehicle`
- C. `x_acme_fleet_vehicle`
- D. `sys_x_acme_fleet_vehicle`

**Q41.** Which statement about the `u_` and `x_` table-name prefixes is correct?
- A. `u_` marks a table created in a scoped application; `x_` marks one created in the global scope
- B. `u_` marks a custom table created in the global scope; `x_` marks a table created in a scoped application
- C. Both prefixes mean the same thing and are assigned at random
- D. `u_` is applied to all custom tables regardless of scope, and `x_` is applied only to tables from the ServiceNow Store

**Q42.** A requirement states that a new Vehicle Request record must be assignable, have a state, carry an SLA, and appear in existing task reporting. What is the best data-model decision?
- A. Create a brand-new table with no parent and manually add assignment and state fields
- B. Extend the Task [task] table
- C. Extend the Configuration Item [cmdb_ci] table
- D. Add the fields directly to the Task table itself

**Q43.** Which is the strongest indicator that a business requirement is a good fit for building on ServiceNow?
- A. The process is entirely computational with no human participants and needs sub-millisecond latency
- B. The work is task-based, moves through states, needs approvals, and involves people across teams
- C. The requirement is to store and stream large binary media files to external consumers
- D. The requirement is to render a high-frame-rate 3D graphics interface

**Q44.** In a many-to-many relationship between two tables, what does ServiceNow actually create to store the relationship?
- A. A reference field on each of the two tables
- B. A new table that holds a reference to each of the two related tables
- C. A related list definition only, with no underlying table
- D. A Document ID field on the parent table

**Q45.** Which two are true of a module in an application menu? *(Choose 2)*
- A. A module can open a list, a form, a URL, or a separate script
- B. A module must always point to a table
- C. A module's visibility can be restricted with roles
- D. A module can only be created by the System Administrator and cannot be scoped

**Q46.** What does setting Runtime access tracking to Enforcing on an application do?
- A. Logs cross-scope access attempts but permits all of them
- B. Permits only cross-scope runtime requests that have a valid cross-scope privilege record
- C. Disables all cross-scope access unconditionally
- D. Automatically creates and approves any cross-scope privilege record on demand

**Q47.** Which table stores cross-scope privilege records?
- A. `sys_scope`
- B. `sys_scope_privilege`
- C. `sys_app_privilege`
- D. `sys_cross_scope`

**Q48.** In a cross-scope privilege record, which operations are supported for a script include target?
- A. read, write, create, delete
- B. execute API only
- C. read and execute only
- D. All CRUD operations plus execute API

**Q49.** A developer wants other developers to see the logic inside their published script include but not modify it. Which script protection policy should they choose?
- A. None
- B. Read-only
- C. Protected
- D. Restricted

**Q50.** Which script protection policy prevents other application developers from changing your intellectual property?
- A. None
- B. Read-only
- C. Protected
- D. Private

**Q51.** An application is published with Can Edit Application in Studio set to false. What is the consequence for someone who downloads it?
- A. They cannot install the application at all
- B. They cannot edit the application in Studio, but retain access to Source Control integration features inside Studio
- C. They can edit the application freely; the setting only affects the publishing instance
- D. They can edit the application only after requesting access from the publisher

**Q52.** Which statement about the global scope is correct?
- A. Global applications cannot access tables in scoped applications under any circumstance
- B. Global applications can alter data you do not intend to alter, so scoped apps are preferred for new tables
- C. Global scope automatically applies a namespace prefix to all new tables
- D. Global scope is required in order to use Delegated Development

**Q53.** By default, what access does a scoped application have to its own tables and business logic?
- A. None until explicitly granted
- B. Read-only
- C. Full access to read and change them
- D. Access only through cross-scope privilege records

**Q54.** Which two places let an administrator specify what parts of an application are accessible to other applications? *(Choose 2)*
- A. The Custom application record
- B. Each application Table record
- C. The Update Set record
- D. The Application Menu record

**Q55.** A developer creates a table that extends Task. Which statement about the resulting fields is correct?
- A. The child table gets a private copy of the Task fields that can be renamed freely
- B. The child table inherits the Task fields, and records appear in Task-level lists and reports
- C. The child table inherits no fields; extension only affects ACLs
- D. The child table inherits fields but its records do not appear in Task queries

**Q56.** What is the effect of the Application Access setting "Can read" on a scoped table when accessed from another scope?
- A. It grants read access to all users regardless of ACLs
- B. It permits other applications to read the table, still subject to ACLs
- C. It replaces the need for ACLs entirely
- D. It only affects REST API access

**Q57.** Which tool is designed to walk a developer through creating an application by defining the app record, roles, and data tables in a guided sequence?
- A. ServiceNow Studio
- B. Guided Application Creator
- C. Table Builder
- D. Update Set Manager

**Q58.** Which statement best distinguishes App Engine Studio from ServiceNow Studio?
- A. They are the same product under two names
- B. App Engine Studio is a low-code guided experience; ServiceNow Studio is the full IDE for application files
- C. App Engine Studio is the full IDE; ServiceNow Studio is the low-code guided experience
- D. App Engine Studio can only edit existing apps and never create new ones

**Q59.** A developer needs a field that stores one of a fixed list of values chosen by the user. Which field type is appropriate?
- A. String with a Choice list defined
- B. Reference
- C. Document ID
- D. Glide List

**Q60.** What distinguishes a Reference field from a Glide List field?
- A. Reference points to exactly one record; Glide List can point to multiple records on the same table
- B. Reference points to multiple records; Glide List points to one
- C. Reference works only on Task tables; Glide List works anywhere
- D. There is no functional difference

**Q61.** Which statement about the Document ID field type is correct?
- A. It references a single fixed table chosen at design time
- B. It references a record on a table determined at runtime by a companion table-name field
- C. It stores a URL to an external document
- D. It stores an attachment sys_id

**Q62.** An application must be installable on other instances and versioned over time. Which is the appropriate distribution mechanism?
- A. Update Set exported to XML
- B. Publish the application to the Application Repository
- C. Copy and paste the scripts manually
- D. A scheduled data export

**Q63.** Which two statements about application scope and naming conflicts are correct? *(Choose 2)*
- A. The namespace identifier prevents naming conflicts between applications
- B. Scope allows the contextual development environment to determine which changes are permitted
- C. Scope guarantees that two applications can never reference the same table
- D. Scope removes the need for unique field names within a single table

**Q64.** A developer is working in Studio and notices the status bar shows a different application than the one they intend to edit. What is the risk if they proceed?
- A. No risk; Studio automatically reassigns files on save
- B. New application files will be created in the wrong scope
- C. The instance will reject the save with an error
- D. The files will be created correctly but placed in the wrong update set only

---
### Domain 1 — Practice Answers

| Q | Answer | Src | Why |
|---|--------|-----|-----|
| Q40 | C | authored | Scoped tables are prefixed with the application namespace: `x_acme_fleet_vehicle`. `u_` is the global-scope custom prefix, so A is the classic wrong answer. `sys_` is reserved for platform tables. |
| Q41 | B | authored | `u_` = custom table in global scope. `x_` = table in a scoped app. Seeing `u_` on a table tells you immediately it is global. |
| Q42 | B | authored | Assignment, state, SLA and task reporting are all Task behaviours — extend Task and inherit them. D is the trap: adding fields to Task itself pollutes every task-derived table platform-wide. |
| Q43 | B | authored | ServiceNow fits task-based, stateful, approval-driven, cross-team work. A, C and D are the canonical poor fits (real-time compute, media streaming, heavy graphics). |
| Q44 | B | authored | M2M creates an intermediate table holding one reference to each side. A describes one-to-many done twice; C and D describe unrelated constructs. |
| Q45 | A & C | authored | Modules can open lists, forms, URLs, or run a script, and can be role-restricted. B is false (a module need not target a table) and D is false (modules are scoped like any app file). |
| Q46 | B | authored | Enforcing = only requests with a valid cross-scope privilege record run. Tracking is the log-but-allow mode described in A — that is the distinction being tested. |
| Q47 | B | authored | `sys_scope_privilege`. The other three are invented table names. |
| Q48 | B | authored | Script includes and script objects support execute API only. Tables are the ones supporting read/write/create/delete — do not swap them. |
| Q49 | B | authored | Read-only = others can see the logic but not change it. |
| Q50 | C | authored | Protected = IP protection, logic not changeable. Q49/Q50 are a pair: Read-only exposes the code, Protected does not. "Restricted"/"Private" are not policy values. |
| Q51 | B | authored | They lose Studio editing but keep Source Control integration features inside Studio. The setting has no effect on apps still in development on the publishing instance. |
| Q52 | B | authored | Straight from the docs: global apps can alter data you do not intend to alter, so use scoped apps for new tables. Global scope does not add a namespace prefix (C), and Delegated Development does not require global (D). |
| Q53 | C | authored | A scoped app has full access to its own tables and logic by default; it is other applications that need explicit permission. |
| Q54 | A & B | authored | The Custom application record and each application Table record. Update sets and application menus have nothing to do with cross-application accessibility. |
| Q55 | B | authored | Extension inherits fields and makes records visible at the parent level — that is exactly why Q42's answer is "extend Task". |
| Q56 | B | authored | Application Access controls cross-scope reachability; ACLs still apply on top. A and C both wrongly treat it as an ACL bypass. |
| Q57 | B | authored | Guided Application Creator — app record, roles, data tables (see Q7). Studio is the IDE, not a guided sequence. |
| Q58 | B | authored | AES = low-code guided app building; Studio = full IDE over application files. D is a distortion of a real fact: AES User Limited group members can only edit existing apps. |
| Q59 | A | authored | A String field with a Choice list. Reference points at records in another table, which is a different requirement. |
| Q60 | A | authored | Reference = one record. Glide List = many records on one table. |
| Q61 | B | authored | Document ID resolves its target table at runtime via a companion table field — that is what makes it different from Reference. |
| Q62 | B | authored | The Application Repository handles versioned install/upgrade across instances. Update sets move changes between dev/test/prod, not distribute a versioned product. |
| Q63 | A & B | authored | Namespace prevents conflicts; scope drives what the contextual development environment permits. C overstates it (cross-scope references are possible when granted) and D is unrelated. |
| Q64 | B | authored | Files land in whatever scope is active — Studio will not stop you. This is why Q4/Q6 (scope in the status bar and browser tab) are worth knowing. |

---

## Domain 2 — Application User Interface (Practice)

**Q65.** Which script type runs in the user's browser and can respond to a field value changing without a round trip to the server?
- A. Business Rule
- B. Client Script
- C. Script Include
- D. Scheduled Script Execution

**Q66.** Which client script type runs when a form is loaded and the fields are populated?
- A. onChange
- B. onSubmit
- C. onLoad
- D. onCellEdit

**Q67.** Which client script type runs when a value is changed in a list view rather than on a form?
- A. onChange
- B. onCellEdit
- C. onSubmit
- D. onLoad

**Q68.** A requirement is to make a field mandatory and read-only based on the value of another field, with no scripting. What should be used?
- A. Client Script
- B. UI Policy
- C. Business Rule
- D. Data Policy

**Q69.** What is the key difference between a UI Policy and a Data Policy?
- A. UI Policy enforces rules on the form only; Data Policy enforces rules on data regardless of entry point, including imports and web services
- B. Data Policy applies to the form only; UI Policy applies everywhere
- C. They are identical but Data Policy is deprecated
- D. UI Policy runs on the server; Data Policy runs on the client

**Q70.** Which two statements about UI Policies versus Client Scripts are correct? *(Choose 2)*
- A. UI Policies run after Client Scripts on form load
- B. UI Policies are the preferred no-code way to set mandatory, read-only, and visible
- C. Client Scripts should be preferred over UI Policies for simple field-state changes
- D. Client Scripts run only on the server

**Q71.** Which method correctly retrieves the value of a field in a client script?
- A. `current.getValue('short_description')`
- B. `g_form.getValue('short_description')`
- C. `gs.getValue('short_description')`
- D. `g_scratchpad.short_description`

**Q72.** A developer needs data computed on the server made available to a client script when a form loads, without an extra server call. What should they use?
- A. A display business rule writing to `g_scratchpad`
- B. An after business rule writing to `g_scratchpad`
- C. GlideAjax from an onLoad client script
- D. A before business rule writing to `current`

**Q73.** Which two statements about `g_scratchpad` are correct? *(Choose 2)*
- A. It is populated on the server and read on the client
- B. It is populated on the client and read on the server
- C. It is typically set in a display business rule
- D. It is typically set in an after business rule

**Q74.** A client script must call server-side logic and use the result. What is the correct mechanism?
- A. Call the script include directly by name from the client script
- B. Use GlideAjax against a script include marked Client callable
- C. Use `gs.include()` in the client script
- D. Use a before business rule

**Q75.** For a script include to be callable via GlideAjax, what must be true? *(Choose 2)*
- A. The Client callable checkbox must be selected
- B. It must extend `AbstractAjaxProcessor`
- C. It must be in the global scope
- D. It must be marked as a Scheduled Job

**Q76.** Which statement about a Record Producer is correct?
- A. It is a report format for catalog data
- B. It is a Service Catalog item that presents a friendly form and creates a record on a target table
- C. It can only create records on the Incident table
- D. It replaces the need for ACLs on the target table

**Q77.** In a Record Producer script, which variable represents the record being created?
- A. `g_form`
- B. `producer`
- C. `current`
- D. `g_scratchpad`

**Q78.** In a Record Producer script, how do you access the value a user entered into a producer variable?
- A. `current.variable_name`
- B. `producer.variablename`
- C. `g_form.getValue('variable_name')`
- D. `gs.getProperty('variable_name')`

**Q79.** Which client-side scripts apply to Record Producers?
- A. Catalog Client Scripts and Catalog UI Policies
- B. UI Scripts and UI Actions
- C. UI Scripts and Record Producer Scripts
- D. Client Scripts and UI Policies

**Q80.** What is the fastest way to create and configure a Record Producer for an existing table?
- A. Create a Catalog Category and select Add New Record Producer
- B. Use the Record Producer module and add every variable manually
- C. Open the table in Tables and select the Add to Service Catalog related link
- D. Right-click the form header and select Create Record Producer

**Q81.** Which two are legitimate uses of a UI Action? *(Choose 2)*
- A. Add a button to a form that runs server-side script
- B. Add a context-menu item to a list
- C. Enforce a field as mandatory on import
- D. Schedule a script to run nightly

**Q82.** Which of the following is NOT a UI Action type?
- A. List choice
- B. Form button
- C. List banner button
- D. Form choice

**Q83.** Which statement about form Views is correct?
- A. A view is a named arrangement of fields and sections that can differ by role or device
- B. A view changes the underlying table schema
- C. Only one view can exist per table
- D. Views are stored as separate physical tables

**Q84.** What is the purpose of a Related List on a form?
- A. To display records from another table that reference this record
- B. To display a read-only copy of the current record's fields
- C. To create a many-to-many relationship automatically
- D. To restrict which fields a user can edit

**Q85.** Which two are true of the `g_form` API? *(Choose 2)*
- A. `g_form.setMandatory()` makes a field required on the form
- B. `g_form.showFieldMsg()` displays a message beside a specific field
- C. `g_form.query()` runs a database query directly from the client
- D. `g_form.setAbortAction()` deletes the current record

**Q86.** Which client script would you use to stop a form from being submitted when a validation fails?
- A. onLoad
- B. onChange
- C. onSubmit returning false
- D. onCellEdit

**Q87.** What is the correct way to abort a record operation from a before business rule?
- A. `return false;`
- B. `current.setAbortAction(true);`
- C. `g_form.setAbortAction(true);`
- D. `gs.abort();`

**Q88.** Which two are recommended debugging strategies for client-side scripts? *(Choose 2)*
- A. `g_form.addInfoMessage()`
- B. `jslog()`
- C. `gs.log()`
- D. `gs.addErrorMessage()`

**Q89.** A field must be hidden from users without a specific role, and the restriction must hold even if the record is accessed through the REST API. What is the correct mechanism?
- A. UI Policy
- B. Client Script
- C. ACL on the field
- D. Form layout

**Q90.** In Form Designer, if you edit the label of a field on a child table, which table is updated?
- A. The base table
- B. The parent table
- C. The child table only
- D. All tables in the hierarchy

**Q91.** Which statement about the Form Designer is correct?
- A. To add a field to the form layout, drag it from the Fields tab to the form
- B. To add a section to the form layout, drag it from the Field Types tab
- C. Removing a field from the form layout deletes it from the database table
- D. New fields cannot be created from the Form Designer

**Q92.** What happens to the List view when a new field is added to an existing table?
- A. The new field is added at the end of the list
- B. A new list view is created containing the new field
- C. The new field is added at the start of the list
- D. The new field is not added to the list view

**Q93.** Can inherited fields be deleted from a child table?
- A. Yes, using the red X in the table definition
- B. Yes, but only text fields
- C. No, inherited fields cannot be deleted from a child table
- D. Yes, but only if no data has ever been saved

**Q94.** Which field type would you select to query records from another table on a form?
- A. Date
- B. Phone Number
- C. String
- D. Reference

**Q95.** Which is a good practice for adding instructions to a form?
- A. Annotations
- B. Related links to wiki pages
- C. A context menu UI Action
- D. A populated read-only field

**Q96.** If the Create module option is selected when creating a table, what is the new module's default behavior?
- A. Open an empty form so new records can be created
- B. Open a link to a wiki article
- C. Display an empty homepage for the application
- D. Display a list of all records from the table

**Q97.** Which class is NOT part of the client-side scoped APIs?
- A. GlideDialogWindow
- B. GlideAjax
- C. GlideRecord
- D. GlideForm

---
### Domain 2 — Practice Answers

| Q | Answer | Src | Why |
|---|--------|-----|-----|
| Q65 | B | authored | Client Scripts are the browser-side tier. Business rules and script includes are server-side; scheduled executions have no form context at all. |
| Q66 | C | authored | onLoad runs once as the form renders, after fields are populated. Contrast the four types: onLoad (form opens), onChange (a field value changes), onSubmit (form is saved), onCellEdit (value changed in a list). |
| Q67 | B | authored | onCellEdit is the list-view type. Candidates routinely answer onChange here — onChange is the form equivalent. |
| Q68 | B | authored | UI Policy is the declarative way to set mandatory/read-only/visible. Reaching for a Client Script here is the classic over-engineering trap. |
| Q69 | A | authored | UI Policy = form only. **Data Policy = enforced regardless of entry point**, including import sets and web services. The most testable UI-vs-Data distinction there is. |
| Q70 | A & B | authored | UI Policies run after client scripts on load and are the preferred declarative option. C inverts best practice; D is false. |
| Q71 | B | authored | `g_form.getValue()`. `current` and `gs` are server-side; `g_scratchpad` is a data carrier, not an accessor. |
| Q72 | A | authored | A **display** business rule runs before the form is presented and can populate `g_scratchpad`. An after rule (B) is too late. GlideAjax (C) works but costs the extra server call the question excludes. |
| Q73 | A & C | authored | Server writes it, client reads it, set in a display business rule. B reverses the direction; D names the wrong rule type. |
| Q74 | B | authored | GlideAjax + a Client callable script include. Client scripts cannot invoke server code directly (A), and `gs` does not exist on the client (C). |
| Q75 | A & B | authored | Client callable checked **and** extends `AbstractAjaxProcessor`. Scope is irrelevant (C); Scheduled Job is a different artifact (D). |
| Q76 | B | authored | A catalog item that produces a record on a target table — that is how it serves as an application UI. Works with any table (C false); does not affect ACLs (D false). |
| Q77 | C | authored | `current` is the record being created. |
| Q78 | B | authored | Producer variables are read from the `producer` object. Q77/Q78 pair up: `current` = the record, `producer` = the user's input. Mixing them is the intended error. |
| Q79 | A | web | Record Producers are catalog artifacts, so they use **Catalog** Client Scripts and **Catalog** UI Policies — not the ordinary form-based ones. |
| Q80 | C | web | Open the table record and use the **Add to Service Catalog** related link — it generates the producer and its variables for you. |
| Q81 | A & B | authored | Form buttons and list context-menu items are both UI Actions. C is a Data Policy job; D is a Scheduled Script Execution. |
| Q82 | D | web+docs | **Form choice** is not a UI Action type. List choice, Form button and List banner button all are. ⚠️ Heavily contested: mined sources keyed this as "List choice" and also listed "Form choice" as *valid* in a different item. The `sys_ui_action` table has List choice; it has no Form choice. |
| Q83 | A | authored | Views are named field/section arrangements and can vary by role or device. They are presentation only — the schema is untouched. |
| Q84 | A | authored | A related list shows records from another table that reference this one. |
| Q85 | A & B | authored | `setMandatory` and `showFieldMsg` are real. `g_form.query()` does not exist, and `setAbortAction` belongs to server-side `current`, never deletes anything. |
| Q86 | C | authored | onSubmit returning false halts submission. |
| Q87 | B | authored | `current.setAbortAction(true)` on the server. `return false` is the *client* onSubmit idiom — mixing the tiers is exactly what Q86/Q87 test. |
| Q88 | A & B | web | `g_form.addInfoMessage()` and `jslog()` are client-side. **`gs.*` is server-side and unavailable in a client script** — that is why gs.log() is the stock wrong answer in every version of this item. |
| Q89 | C | authored | Only an **ACL** enforces server-side and therefore survives REST access. UI Policy, Client Script and form layout are cosmetic — the highest-value security instinct on the exam. |
| Q90 | C | web | The **child table only**. Labels are per-table overrides, so the parent and its other children are unaffected. |
| Q91 | A | web | Fields are dragged from the **Fields** tab; new fields are created by dragging a data type from the **Field Types** tab. Sections also come from Field Types, but the keyed correct statement across sources is the Fields-tab drag. Removing a field from the layout never deletes it from the table (C). |
| Q92 | D | web | Adding a field to a table does **not** add it to the list view — list layout is configured separately. |
| Q93 | C | web | Inherited fields cannot be deleted from a child table; they belong to the parent. Compare Q42/Q55 — inheritance is a benefit and a constraint. |
| Q94 | D | web | Reference field. |
| Q95 | A | web | **Annotations** are the supported way to put instructional text on a form. |
| Q96 | D | web | The generated module displays a **list of all records** from the table. |
| Q97 | C | web | **GlideRecord is server-side.** GlideDialogWindow, GlideAjax and GlideForm are all client-side. Using GlideRecord in a client script is both a wrong answer here and a real-world anti-pattern. |

---

## Domain 3 — Security and Restricting Access (Practice)

**Q98.** Within a single ACL, in what order are the elements evaluated?
- A. Conditions, Roles, Script
- B. Script, Conditions, Roles
- C. Role, Security Attribute, Condition, Script
- D. Conditions, Script, Roles

**Q99.** Which three conditions make an ACL invalid? *(Choose 3)*
- A. An ACL with a role that does not exist in the database
- B. An ACL with a Security Attribute that does not exist
- C. An ACL whose script contains only `answer=true` or `true`
- D. An ACL with a role that exists but is inactive
- E. An ACL that references a deprecated API

**Q100.** When ServiceNow evaluates Access Controls for a requested object, in what order does it search for matching rules?
- A. Only for matches on the current table
- B. Only for matches on the current field
- C. From the most specific match to the most generic match
- D. From the most generic match to the most specific match

**Q101.** For a record operation, which statement about table-level and field-level ACL rules is correct?
- A. Only the field-level rule needs to evaluate to true
- B. Only the table-level rule needs to evaluate to true
- C. The matching table-level and field-level rules must both evaluate to true
- D. Whichever rule is evaluated first determines the outcome

**Q102.** An ACL rule has an empty Required roles list. How does the role portion of that ACL evaluate?
- A. It always fails, denying access
- B. It evaluates to true
- C. It prompts the administrator to add a role
- D. It grants access only to admin

**Q103.** If the system finds no matching access control rules at all for a requested object and operation, what happens by default?
- A. Access is denied
- B. Access is granted
- C. The request is queued for administrator approval
- D. The system throws an error

**Q104.** Which system property controls whether the wildcard table ACL rules deny or allow read, write, create, and delete across all tables?
- A. `glide.security.default_deny`
- B. `glide.sm.default_mode`
- C. `glide.acl.wildcard_mode`
- D. `glide.security.manager.deny`

**Q105.** An administrator sets `glide.sm.default_mode` to Deny Access. What is true afterwards?
- A. The setting can be reverted to Allow Access at any time
- B. The setting cannot be reset to Allow Access once applied
- C. All operations including report_on and personalize_choices are restricted
- D. Only the admin role is affected

**Q106.** An ACL rule is created with the name `customer.*`. What does it secure?
- A. The customer table record only, with no field access
- B. All rows and all fields on the customer table
- C. Only fields that have no explicit ACL
- D. Only the customer table's related lists

**Q107.** On table MyTable with field1, field2 and field3: `MyTable.None` grants read to admin and itil; `MyTable.field3` grants read to admin only. What can a user with only the itil role read?
- A. field2 and field3
- B. field1 and field3
- C. field1, field2 and field3
- D. field1 and field2

**Q108.** Which two methods are useful inside an Access Control script? *(Choose 2)*
- A. `gs.hasRole()`
- B. `current.isNewRecord()`
- C. `g_user.hasRole()`
- D. `g_form.getValue()`

**Q109.** In a Business Rule, which call returns true if the currently logged-in user has the admin role?
- A. `g_form.hasRoleExactly('admin')`
- B. `gs.hasRole('admin')`
- C. `g_form.hasRole('admin')`
- D. `gs.hasRoleExactly('admin')`

**Q110.** What is true of the client-side call `g_user.hasRole('x_my_app_user')`?
- A. It returns true if the user has the x_my_app_user role or the admin role
- B. It returns false only if the user has the x_my_app_user role
- C. There is no `g_user.hasRole()` method
- D. It returns true only if the user has the x_my_app_user role

**Q111.** Which method returns true only if the logged-in user has the catalog_admin role and no other role?
- A. `g_user.hasRole('catalog_admin')`
- B. `g_user.hasRoleExactly('catalog_admin')`
- C. `g_user.hasRoleOnly('catalog_admin')`
- D. `g_user.hasRoleFromList('catalog_admin')`

**Q112.** Which statement about client-side scripted security is correct?
- A. Client-side scripts have access to both GlideSystem (gs) and GlideUser (g_user) methods
- B. Client-side scripts have access to the GlideUser (g_user) methods
- C. Client-side scripts have no access to user methods
- D. Client-side scripts have access to the GlideSystem (gs) user methods

**Q113.** Which ACL operation enables users to execute client callable script includes and REST endpoints?
- A. read
- B. write
- C. execute
- D. query_match

**Q114.** When a custom table is created, which Access Control rules are automatically generated? *(Choose 4)*
- A. read
- B. create
- C. delete
- D. write
- E. execute

**Q115.** During a pre-query ACL check, which parts of the ACL are evaluated?
- A. Roles only
- B. Roles, conditions and scripts
- C. Conditions and scripts only
- D. Nothing; all checks happen post-query

**Q116.** A Deny-Unless ACL passes and no Allow-If ACL matches the request. What happens?
- A. Access is denied because no Allow-If explicitly permitted it
- B. The system grants access by default
- C. The request is escalated to the table owner
- D. The Deny-Unless ACL is ignored

**Q117.** Which statement about a table with the "Allow configuration" Application Access option selected is true?
- A. Only the in-scope application's scripts can create Business Rules for the table
- B. Any user with the application's user role can modify the application's scripts
- C. Out-of-scope applications can create Business Rules for the table
- D. Out-of-scope applications can add new tables to the scoped application

**Q118.** For Application Access, the "Allow access to this table via web services" option is selected. Which statement is true?
- A. Any user can now query the table through web services
- B. The user performing the query must still have the correct permissions to access the table's records
- C. It restricts access to SOAP only and does not apply to REST
- D. It permits reads but always blocks deletes

**Q119.** Which Application Access options become unavailable if "Can read" is NOT selected?
- A. Access via web services
- B. Can create, Can update and Can delete
- C. None; Can read does not affect the other fields
- D. Allow configuration

**Q120.** What are the default runtime access permissions for a new application data table? *(Choose 2)*
- A. Accessible from is set to All application scopes
- B. Can read is enabled
- C. Can create, update and delete are all enabled
- D. Access via web services is disabled

**Q121.** Which records track cross-scope applications or scripts that request access to an application resource or event?
- A. Restricted caller access records
- B. Caller tracking records
- C. Access control level records
- D. Cross-scope access records

**Q122.** Which is NOT a valid Caller access field option?
- A. Caller Tracking
- B. Caller Restriction
- C. None
- D. Caller Permission

**Q123.** A developer hides a sensitive field using a Client Script and reports the field as secured. Why is that assessment wrong?
- A. Client scripts run only for users with the admin role
- B. Client scripts affect only the browser and do not enforce server-side access
- C. Client scripts disable all ACLs on the table
- D. Client scripts run only after the record is deleted

**Q124.** A module is restricted to the `x_app.user` role, but the table behind it has no read ACL for that role. What does the user experience?
- A. Records open normally because the module role is sufficient
- B. The user reaches the list but cannot read any records
- C. The module role is copied automatically into a table ACL
- D. The table becomes readable by all application users

**Q125.** When configuring a module, what does the "Override application menu roles" option do?
- A. Users with the module role but without access to the application menu can access the module
- B. Self-Service users can access the module even without roles
- C. Admin is given access even if Access Controls would prevent it
- D. Users with application menu access see the module even without the module role

**Q126.** Which two database operations can be controlled with an Access Control? *(Choose 2)*
- A. Create
- B. Update
- C. Compile
- D. Index

**Q127.** Which feature limits who can contribute to or read articles within a knowledge base?
- A. Roles
- B. Groups
- C. Categories
- D. User Criteria

---
### Domain 3 — Practice Answers

| Q | Answer | Src | Why |
|---|--------|-----|-----|
| Q98 | C | web+docs | Current documentation is explicit: within an ACL the hierarchy is **Role → Security Attribute → Condition → Script**. ⚠️ **Read the options carefully on exam day.** Older course material taught "Conditions, Roles, Script" and dump sites still key it that way — the two most-copied dumps contradict each other on this exact item. Prefer a role-first option when one is offered. |
| Q99 | A, B & C | docs | Documented invalid-ACL definition: non-existent role, non-existent security attribute, or a script containing just `answer=true`/`true`. **D is the trap** — an inactive role still exists, so the ACL is valid but ineffective. Compare Q27. |
| Q100 | C | web | Most specific → most generic. This is why a field ACL is found before the table wildcard. |
| Q101 | C | docs | Both must evaluate to true. A field is only readable if the table-level rule **and** the field-level rule pass. |
| Q102 | B | docs | An empty roles list evaluates to **true** — it imposes no role requirement. Candidates routinely assume empty means deny. |
| Q103 | B | docs | Documented behaviour: no matching rules → **access is granted**. The platform ships default rules so this is rare in practice, which is why the intuition "no ACL means denied" feels right and is wrong. Contrast Q23: an *empty or invalid* ACL denies; *no matching* ACL grants. |
| Q104 | B | docs | `glide.sm.default_mode`. |
| Q105 | B | docs | Once set to Deny Access it **cannot be reset** to Allow Access. C is wrong — report_on and personalize_choices are explicitly unaffected. |
| Q106 | B | web | B is the best of the four, but **be precise about what `table.*` actually is**: `platform-security/access-control/acl-rule-types.md` lists it in the **field** ACL ordering — "Match the table and any field (\*). For example, `incident.*`" — at position 4 of 6, *after* `table.field`, `parent.field` and `*.field`. So `customer.*` is the catch-all **field** rule for that table, not a record rule; the record rule is `customer` (shown as `.None`). ⚠️ Option C ("only fields with no explicit ACL") is closer to the runtime behaviour than it looks, because a more specific field rule matches first and "the first successful field ACL evaluation stops ACL rule processing at the field level" — but C is wrong as written, since a rule like `*.name` also outranks `customer.*`. Read the option set, not the wildcard alone. |
| Q107 | D | web | itil passes the table rule, so field1 and field2 are readable; field3 carries its own admin-only rule that itil fails. ⚠️ One mined source keyed "field1 and field3" — wrong, field3 is precisely the restricted one. |
| Q108 | A & B | web | ACL scripts are **server-side**: `gs.hasRole()` and `current.isNewRecord()`. `g_user` is client-side and `g_form` is a form API. Note the method is `isNewRecord()`, not `isNew()`. |
| Q109 | B | web+docs | `gs.hasRole('admin')`. **`gs.hasRoleExactly()` does not exist.** The official Scripting Security reference splits the two APIs: client-side **GlideUser (`g_user`)** has `hasRole()`, `hasRoleExactly()`, `hasRoleFromList()`, `hasRoles()`; server-side **GlideSystem (`gs`)** has only `hasRole()` — plus `getUser()`, `getUserID()`, `getUserName()`, `isLoggedIn()`, `isInteractive()`, `getSession()`. So D is not a weaker answer, it is **not a real method**. A and C fail twice over: `g_form` is client-side *and* has no role methods at all. |
| Q110 | A | web | `g_user.hasRole()` returns true for the named role **or admin**, because admin is treated as holding every role. Q110/Q111 pair: `hasRole` includes admin, `hasRoleExactly` does not. |
| Q111 | B | web+docs | `g_user.hasRoleExactly()` — true only when that is the user's sole role. ⚠️ **Correction:** an earlier version of this note claimed `hasRoleFromList` does not exist. **It does** — the official Scripting Security reference lists `hasRole()`, `hasRoleExactly()`, `hasRoleFromList()` and `hasRoles()` on `g_user`. `hasRoleFromList()` is real but answers a different question (does the user hold *any* of these roles). Only **`hasRoleOnly`** is invented. |
| Q112 | B | web | Client scripts get **g_user only**. `gs` is server-side. |
| Q113 | C | docs | The `execute` operation covers client callable script includes and REST endpoint execution — which is why those artifact types appear in access-analysis questions (Q31). |
| Q114 | A, B, C & D | web | **read, create, write, delete** — four rules, one per CRUD operation. `execute` is not generated for a data table. ⚠️ An earlier draft of this bank keyed only three (omitting write); three independent sources key four, and a separate mined item phrases it as "which **four** Access Controls are created". Four is correct. |
| Q115 | A | docs | Pre-query checks **roles only**, because no record data exists yet. Roles, conditions and scripts are all evaluated post-query. |
| Q116 | B | docs | Documented explicitly: if the Deny-Unless passes and no Allow-If matches, the system **grants access by default**. A is the intuitive-but-wrong reading. |
| Q117 | C | web | "Allow configuration" is design-time access — it lets **out-of-scope applications create configuration records** (such as Business Rules) against the table. |
| Q118 | B | docs | Verbatim from the docs: the user must still have correct permissions even when the box is selected. The setting opens the door; ACLs still guard it. |
| Q119 | B | docs | Can write, create and delete are each available **only when Can read is selected** — "You must first select read access to grant any other API record operation." Web services access is independent, so A is the trap. |
| Q120 | A & B | docs | Default is Accessible from = **All application scopes**, Can read = **Enabled**, create/update/delete disabled, web services **enabled**. ⚠️ A widely-copied dump claims the baseline is "only in-scope artifacts can read" — the documentation says otherwise. |
| Q121 | A | docs | Restricted caller access `[sys_restricted_caller_access]` records. Distinguish from `sys_scope_privilege` (Q47), the runtime cross-scope privilege table. |
| Q122 | D | web | The options are Caller Tracking, Caller Restriction and None. "Caller Permission" does not exist. |
| Q123 | B | web | Browser-only. Same principle as Q89 — if it is not enforced server-side, it is not security. |
| Q124 | B | web | Module roles govern **navigation**, ACLs govern **data**. The user reaches an empty list. This split is worth internalising: a visible module is not an accessible record. |
| Q125 | A | web | It lets users holding the **module** role in without the application-menu role. |
| Q126 | A & B | web | Creating and updating records are both controllable; "Compile" and "Index" are not operations ACLs govern. **But note the naming trap:** the operation is called **`write`**, not "update" — `acl-rule-types.md` defines `write` as "Enables users to update records in a table." If an option offers *write* and *update* side by side, **write** is the operation name. The full documented record-operation list is longer than most sources admit: `create`, `read`, `write`, `delete`, `execute`, `list_edit`, `report_on`, `report_view`, `add_to_list`, `personalize_choices`, `save_as_template`, `query_match`, `query_range`, `edit_task_relations`, `edit_ci_relations`. |
| Q127 | D | web | **User Criteria** governs knowledge base contribute/read. Roles and groups are the generic mechanisms; user criteria is the knowledge-specific one. |

---

## Domain 4 — Application Automation (Practice)

**Q128.** Which is NOT a trigger type in Flow Designer?
- A. Outbound Email
- B. Schedule
- C. Application
- D. Record

**Q129.** In Flow Designer, where is the output of an action stored so it can be used by subsequent actions?
- A. Data Element
- B. Field Value
- C. Data Trigger
- D. Data Pill

**Q130.** What is a scoped application that contains Flow Designer actions tailored to a specific application or record type called?
- A. Bundle
- B. Action
- C. Spoke
- D. Flow

**Q131.** Which two ways can an application respond to an Event generated by `gs.eventQueue()`? *(Choose 2)*
- A. Script Action
- B. Scheduled Script Execution
- C. UI Policy
- D. Email Notification

**Q132.** Which object CANNOT be used in a Script Action script?
- A. previous
- B. GlideRecord
- C. event
- D. current

**Q133.** Which two objects are available in a Scheduled Script Execution script? *(Choose 2)*
- A. GlideSystem
- B. GlideRecord
- C. current
- D. g_form

**Q134.** Which four objects are available in an Inbound Email Action script? *(Choose 4)*
- A. `current`
- B. `event`
- C. `email`
- D. `logger`
- E. `previous`
- F. `producer`

**Q135.** How does ServiceNow match an inbound email to an existing record?
- A. sys_id in the body
- B. Watermark
- C. Subject line text
- D. Sender address

**Q136.** In an Email Notification, which syntax references a property of the event that triggered the notification?
- A. `${event.<property name>}`
- B. `${current.<property name>}`
- C. `${<property name>.getDisplayValue()}`
- D. `${gs.<property name>}`

**Q137.** Regarding the Weight field on an Email Notification, which statement is NOT true?
- A. The Weight value defaults to zero
- B. Only the highest-weight notifications for the same record and recipients are sent
- C. A Weight of zero means the notification is always sent when criteria are met
- D. A Weight of zero means no email should be sent

**Q138.** Which three elements are configured in an Email Notification? *(Choose 3)*
- A. Who receives the notification
- B. The content of the notification
- C. When to send the notification
- D. Which database indexes to rebuild

**Q139.** Which module is used to create a new email notification?
- A. System Properties > Email > Settings
- B. User Preferences > Email > Notifications
- C. System Notification > Email > Notifications
- D. Administration > Notification Overview

**Q140.** Which two actions can a Business Rule take without any scripting? *(Choose 2)*
- A. Set field values
- B. Add a message
- C. Query an external REST endpoint
- D. Rebuild the table index

**Q141.** Which Business Rule "when" option runs before the record is presented to the user and is used to populate `g_scratchpad`?
- A. before
- B. after
- C. async
- D. display

**Q142.** Which object does a Display Business Rule NOT have access to?
- A. previous
- B. GlideSystem
- C. g_scratchpad
- D. current

**Q143.** For an Async Business Rule, which database operation CANNOT be configured as a trigger?
- A. Query
- B. Insert
- C. Update
- D. Delete

**Q144.** What happens when multiple Business Rules apply to the same table and operation?
- A. They trigger in random order
- B. They trigger in ascending Order field sequence
- C. Only the first rule triggers
- D. They trigger simultaneously

**Q145.** What is `g_scratchpad` used for?
- A. To pass data from a client script back to the server
- B. To pass data from a server-side script to a client-side script when a form loads
- C. To store persistent data between user sessions
- D. To define constructors for a table class

**Q146.** What is a benefit of creating an Application Properties page?
- A. It provides a common landing page for an application
- B. It overrides application properties inherited from ServiceNow
- C. It tells users where to change the application's appearance
- D. It allows changes to application behavior without modifying application artifacts

**Q147.** Which Module Link type is used to access an Application Properties page?
- A. URL (from Arguments)
- B. HTML (from Arguments)
- C. Script (from Arguments)
- D. Single Record

**Q148.** When creating a Utils Script Include, which step does NOT belong?
- A. Identify the table
- B. Script the functions
- C. Create a class
- D. Create a prototype object from the new class

**Q149.** Which two are benefits of storing server-side logic in a Script Include? *(Choose 2)*
- A. It runs only when called from a script
- B. It makes every script on the instance execute faster
- C. It gives one place to edit shared application logic
- D. It automatically exposes the logic to client scripts

**Q150.** What type of JavaScript function is the standard Business Rule script template?
- A. Constructor
- B. Scoped
- C. Anonymous
- D. Self-invoking

**Q151.** Which server-side object provides methods for working with dates in a privately scoped application?
- A. GlideDateTime
- B. GlideRecord
- C. GlideSystem
- D. current

**Q152.** In a Business Rule, which call returns the sys_id of the logged-in user?
- A. `g_form.getUserID()`
- B. `g_form.getUserSysID()`
- C. `gs.getUserSysID()`
- D. `gs.getUserID()`

**Q153.** Which GlideSystem method returns the first and last name of the logged-in user concatenated together?
- A. `gs.getUserName()`
- B. `gs.getUserID()`
- C. `gs.getUserDisplayName()`
- D. `gs.getUser()`

**Q154.** Which feature tracks how long a task has been open to ensure it is completed within an allotted time?
- A. Inactivity Monitor
- B. Business Time Remaining
- C. Service Level Agreements
- D. Response Time Clock

**Q155.** Which testing framework is used to test ServiceNow applications?
- A. Selenium
- B. Test Driven Framework (TDF)
- C. Automated Test Framework (ATF)
- D. JUnit

**Q156.** Which ATF test step sets up a specific user profile for testing purposes?
- A. Impersonation
- B. Create a role
- C. Create a user
- D. Create a group

**Q157.** Which script always executes on the server side?
- A. Business Rule
- B. UI Action
- C. Client Script
- D. UI Policy

**Q158.** What is a workflow context?
- A. The checked-out workflow version being edited
- B. An instance generated from a workflow version that executes activities and follows transitions
- C. The table plus the conditions that start the workflow
- D. The business reason documented for the workflow design

---
### Domain 4 — Practice Answers

| Q | Answer | Src | Why |
|---|--------|-----|-----|
| Q128 | A | web | Flow triggers include Record, Schedule, Application, Inbound Email and inbound API. **Outbound Email is not a trigger** — sending outbound email is something a flow *does*, not something that starts it. |
| Q129 | D | web | A **Data Pill** is the draggable token representing an action's output. "Data Element" and "Data Trigger" are invented terms — Flow Designer's vocabulary is trigger, action, flow logic, and data pill. |
| Q130 | C | web | A **Spoke** is a scoped app bundling Flow Designer actions for one system (the Slack spoke, the Microsoft spoke). An *Action* is a single step inside it; a *Flow* is the sequence you build from actions. |
| Q131 | A & D | web | Events are consumed by **Script Actions** and **Email Notifications**. ⚠️ Mined sources keyed this as "UI Policy" and as a single answer — both wrong. A Scheduled Script Execution runs on a clock; it does not subscribe to the event queue. |
| Q132 | A | web+docs | **`previous`.** A Script Action runs off the event queue, decoupled from the transaction that fired it, so there is no prior record state to compare. The closest documented statement is in `api-reference/business-rules-classic/c_BusinessRules.md`, which says `previous` is "Available on update and delete operations only. **Not available on async operations.**" — the same decoupling. `current`, `event` and `GlideRecord` are all available. |
| Q133 | A & B | web | GlideSystem and GlideRecord. There is **no `current`** in a scheduled job: nothing is "current" without a triggering record. That is the whole point. |
| Q134 | A, B, C & D | docs | **All four**: `current` (the record the email refers to), `event` (`event.parm1`, `event.parm2`), `email` (`email.subject` — the inbound message), `logger` (writes to the email log). Straight from the script template in `platform-administration/t_CreatingAnInboundEmailAction.md`. ⚠️ **This replaces a broken question.** The mined version asked to pick one pair from "current and email" vs "current and event" — but the docs list both, so it had two correct answers and was unanswerable. `previous` belongs to Business Rules and `producer` to Record Producers. |
| Q135 | B | web+docs | **The watermark.** `platform-administration/c_EmailNotifications.md`: "a unique watermark label will be generated at the bottom of each notification email to allow matching incoming email to existing records", and `c_InboundEmailActions.md`: "An inbound email action checks the email for a watermark that associates it with a task." **Worth carrying:** with no identifiable watermark the action *creates* a record; with the watermark of an existing record it *updates* that record. |
| Q136 | A | web | `${event.<property name>}`. |
| Q137 | D | web | The question asks which is NOT true. Weight zero means the notification is **always sent** when criteria are met, so "zero means no email" is the false statement. ⚠️ Mined sources keyed this three different ways because the option order was scrambled — read the options, not the letter. |
| Q138 | A, B & C | web | Who, what, when. Index rebuilding is unrelated. |
| Q139 | C | web | System Notification > Email > Notifications. |
| Q140 | A & B | web | The no-script Business Rule Actions are **Set field values** and **Add message**. |
| Q141 | D | web | The **display** business rule. See Q72/Q73. |
| Q142 | A | web | `previous`. ⚠️ One mined source keyed `g_scratchpad` — backwards: populating `g_scratchpad` is the display rule's signature use. A display rule reads a record for presentation, so there is no prior version to compare. |
| Q143 | A | web+docs | **Query.** `api-reference/business-rules-classic/c_BusinessRules.md` states it flatly for async rules: "**Insert**, **Update**, and **Delete** database operations. **You cannot select Query.**" Async work is scheduled off a write; a read does not schedule anything. |
| Q144 | B | web | Ascending **Order** value. Lower numbers run first. |
| Q145 | B | web | Server → client, on form load. |
| Q146 | D | web | Properties let you change behaviour **without modifying artifacts** — the point of externalising configuration. A and C describe a homepage, not a properties page. |
| Q147 | A | web+docs | **URL (from Arguments)** — a documented Link type, used exactly this way in `platform-administration/platform-performance/t_CreateAConnectionTestModule.md` ("**Link type**: **URL (from Arguments)**"). The Arguments field carries `system_properties.do?sysparm_title=…&sysparm_category=…`. ⚠️ That argument string is **not** in the local docs clone — it comes from the course material, so treat the exact syntax as unverified. **The discriminator is documented, though, and is the likely trap:** a module that opens the *properties page* uses **URL (from Arguments)**; a module that lists the property *records* uses **List of Records** with Table = System Properties [sys_properties] (`r_AvailableSystemProperties.md`). Read whether the stem says page or list. |
| Q148 | A | web | "Identify the table" does not belong — a Utils Script Include is **table-agnostic** reusable logic. Its steps: create a class, create a prototype object, script the functions. |
| Q149 | A & C | web | Runs only when called, and centralises shared logic. B is false (no blanket speed gain); D is false — client access needs **Client callable** plus GlideAjax (Q75). |
| Q150 | D | web | The template is a **self-invoking** anonymous function: `(function executeRule(current, previous) { ... })(current, previous);`. Both "anonymous" and "self-invoking" describe it, but self-invoking is keyed because the trailing `()` is the distinguishing feature. |
| Q151 | A | web | GlideDateTime. |
| Q152 | D | web+docs | **`gs.getUserID()`** — `api-reference/server-api-reference/c_GlideSystemScopedAPI.md`: "Scoped GlideSystem - getUserID() — Gets the sys_id of the current user." ⚠️ **Corrected: this bank previously keyed `gs.getUserSysID()` and called `getUserID()` a deprecated alternate. That was backwards — `getUserSysID()` does not exist at all.** The complete `getUser*` set is `getUser()`, `getUserDisplayName()`, `getUserID()`, `getUserName()` (global scope adds `getUserNameByUserID()`). Same trap as `gs.hasRoleExactly()`: a plausible-looking method name that was never real. `g_form` is client-side and has no such method either. |
| Q153 | C | web | `gs.getUserDisplayName()` = first + last name. `gs.getUserName()` returns the **login** user name — the classic confusion. |
| Q154 | C | web | Service Level Agreements. |
| Q155 | C | web | Automated Test Framework. |
| Q156 | A | web+docs | The **Impersonation** step — confirmed in `automated-test-framework-atf/atf-use-basic-form.md`, whose worked example opens with "Test step 1 - Impersonate". ⚠️ A site advertising "actual exam questions" keyed *Create a user*; it is wrong. Creating a user makes a record; impersonation is what runs the test *as* that user. |
| Q157 | A | web | A Business Rule is always server-side. A **UI Action can be either** — the Client checkbox decides — which makes it the intended distractor. |
| Q158 | B | web | A context is the **running instance** generated from a published workflow version. Distinguish: version = the design, context = the execution. |

---

## Domain 5 — Working with External Data (Practice)

**Q159.** What tool imports data from various data sources and maps that data into ServiceNow tables?
- A. Update Set
- B. Transform Set
- C. Data Pack
- D. Import Set

**Q160.** Which platform feature determines the relationship between fields in an Import Set table and fields in the target table?
- A. Business Service Management Map
- B. Data Source
- C. Transform Map
- D. Schema Map

**Q161.** What are the three steps to import new data into ServiceNow from a spreadsheet?
- A. Select Data Source, Schedule Transform, Review
- B. Load Data, Create Transform Map, Run Transform
- C. Define Data Source, Select Transform Map, Schedule Import
- D. Select Import Set, Create Data Pack, Run Transform

**Q162.** What is the purpose of the coalesce setting on a field map?
- A. It merges two source columns into one target field
- B. It is the match field: if a record with that value exists it is updated, otherwise a new record is inserted
- C. It deletes target records that are absent from the source
- D. It converts the field's data type during transform

**Q163.** A developer runs an import repeatedly with no coalesce field defined. What is the result?
- A. Existing records are updated each time
- B. A new record is inserted on every run, creating duplicates
- C. The import fails with a validation error
- D. Only the first row is processed

**Q164.** When a ServiceNow instance requests information from an external web service, ServiceNow is acting as the web service:
- A. Publisher
- B. Specialist
- C. Provider
- D. Consumer

**Q165.** When configuring a REST Message, the Endpoint is:
- A. The command telling the REST script to stop execution
- B. The URI of the data to be accessed, queried, or modified
- C. Information about the format of the returned data
- D. The provider's response indicating there is no data to send back

**Q166.** What is the REST API Explorer used for?
- A. Practising REST interaction with public data providers
- B. Finding web resources for learning REST
- C. Converting SOAP methods to REST methods
- D. Creating sample code for ServiceNow REST requests

**Q167.** In a SOAP Message, which syntax indicates a variable to be passed when the function is called?
- A. `current.variable_name`
- B. `${variable_name}`
- C. `<variable_name>`
- D. `<variable_name>.do?WSDL`

**Q168.** Which HTTP method would an Outbound REST Message use to retrieve data without modifying it?
- A. GET
- B. POST
- C. PUT
- D. DELETE

**Q169.** A developer needs to expose a custom ServiceNow endpoint that external systems can call with a custom URL and custom logic. What should they build?
- A. An Outbound REST Message
- B. A Scripted REST API
- C. A Transform Map
- D. An Import Set

**Q170.** Which two statements distinguish inbound from outbound integration? *(Choose 2)*
- A. Inbound means an external system calls ServiceNow
- B. Outbound means ServiceNow calls an external system
- C. Inbound means ServiceNow calls an external system
- D. Outbound integrations are configured with Import Sets

**Q171.** Which ServiceNow feature includes data from a secondary, related table on a report?
- A. Joins
- B. SQL
- C. Dot walking
- D. Outer join

**Q172.** Which statement about a Data Source record is correct?
- A. It defines where the import data comes from, such as a file, JDBC connection, or attachment
- B. It maps import fields to target fields
- C. It stores the transformed records
- D. It schedules the ACL evaluation for imported records

**Q173.** During a transform, which script runs before each row is transformed?
- A. onBefore
- B. onAfter
- C. onStart
- D. onComplete

---
### Domain 5 — Practice Answers

| Q | Answer | Src | Why |
|---|--------|-----|-----|
| Q159 | D | web | Import Set. |
| Q160 | C | web | Transform Map. Distinguish the three: **Data Source** = where data comes from, **Import Set table** = the staging area, **Transform Map** = how staged fields land on the target. |
| Q161 | B | web+docs | **Load Data → Create Transform Map → Run Transform.** ⚠️ A mined source keyed "Select Import Set, Select Transform Map, Run Transform" — wrong; you cannot select an import set that does not exist yet. Loading the data is always step one. |
| Q162 | B | authored | Coalesce is the **match field**. Match found → update; no match → insert. |
| Q163 | B | authored | With no coalesce field every row is treated as new, so each run **inserts duplicates**. This is the single most common real-world import mistake and a recurring exam item. |
| Q164 | D | web | ServiceNow is the **consumer** when it requests data. Consumer = calls out; provider = serves. |
| Q165 | B | web | The URI of the data to be accessed. |
| Q166 | D | web | It generates **sample code for ServiceNow REST requests** and lets you test them. A is the tempting misread — it is not a sandbox for third-party APIs. |
| Q167 | B | web | `${variable_name}`. |
| Q168 | A | authored | GET is the read-only verb. |
| Q169 | B | authored | A **Scripted REST API** — custom endpoint, custom logic. An Outbound REST Message goes the other direction. |
| Q170 | A & B | authored | Inbound = they call us; outbound = we call them. Anchor it to Q164: consumer/outbound is ServiceNow reaching out. |
| Q171 | C | web | **Dot walking** reaches through a reference field to pull in fields from the related table. |
| Q172 | A | authored | The Data Source defines the origin — file, JDBC, attachment, REST. |
| Q173 | A | authored | onBefore runs per row before the transform; onAfter runs per row after. onStart/onComplete bracket the whole transform. |

---

## Domain 6 — Managing Applications (Practice)

**Q174.** Which of the following is NOT a way to install an application on a ServiceNow instance?
- A. Install an application from the Application Repository
- B. Select the Copy button on the application record
- C. Download and install an application from ServiceNow Share
- D. Download and install a third-party application from the ServiceNow Store

**Q175.** Where can an application be published once it is ready to share? *(Choose 3)*
- A. To the ServiceNow Store
- B. To a local drive
- C. To an application repository
- D. To an Update Set
- E. To a spreadsheet

**Q176.** What is the ServiceNow Application Repository?
- A. A database for logging application errors
- B. A database for tracking user permissions
- C. A database containing custom ServiceNow applications
- D. A collection of files in a Git database

**Q177.** How can you see which artifacts will be included in a published application?
- A. Enter the application name in Global search
- B. Open the Update Sets list
- C. Examine the Application Files related list on the application record
- D. Open every artifact record individually

**Q178.** What contains the configuration changes made in an instance and helps move those changes from Dev to another environment?
- A. Import sets
- B. Update sets
- C. Transform maps
- D. System dictionaries

**Q179.** What is required to link a ServiceNow application to a Git repository? *(Choose 3)*
- A. User name
- B. URI
- C. Password
- D. ACL
- E. URL
- F. Application name

**Q180.** How can an application link to a repository that sits behind a firewall?
- A. This option is not supported
- B. Link the application to source control through a MID Server
- C. Link the application to source control through an access token
- D. Link the application to source control with multi-factor authentication

**Q181.** What is the source control operation that stores local changes so they can be applied later?
- A. Branch
- B. Tag
- C. Stash
- D. Update set

**Q182.** You are developing MyApp, which has Table A. You want Table A's records installed as part of the application. Table A's records will be installed when:
- A. Table A is active and extends the Task table
- B. Table A's records are added to the application record using the Create Application Files feature
- C. Table A has an automatic number counter for new records
- D. Table A is not in the System Clone > Exclude Tables list

**Q183.** Which statement about Delegated Development is INCORRECT?
- A. Administrators can specify which application file types a developer may access
- B. Administrators can grant access to script fields
- C. Administrators can grant access to security records
- D. Administrators can grant non-admin users the ability to develop global applications

**Q184.** What is displayed to delegated developers so they can package changes for deployment in ServiceNow Studio?
- A. Tools tab
- B. Update Set Picker
- C. Export to XML
- D. Publish button

**Q185.** Which statement is true for the Application Picker?
- A. All custom application scopes and the Global scope appear in the Application Picker
- B. All applications including baseline applications like Incident appear in the Application Picker
- C. Only custom applications appear in the Application Picker
- D. Only downloaded applications appear in the Application Picker

**Q186.** How does the Application Picker interact with Application Scope?
- A. Global is reserved and does not appear in the picker
- B. Selecting Global sets the Application Scope to Incident
- C. Selecting an application does not set the Application Scope
- D. Selecting an application sets the Application Scope

**Q187.** Which two features are available to Global applications? *(Choose 2)*
- A. Automated Test Framework
- B. Flow Designer
- C. Delegated Development
- D. Application scope protection policies

**Q188.** Which business requirements should be documented as part of the application development plan? *(Choose 4)*
- A. Data input and output
- B. Business problem
- C. Project schedule
- D. Process steps
- E. Database capacity
- F. Users and stakeholders
- G. Available licenses

**Q189.** Which is NOT a purpose of application scoping?
- A. Provide a relationship between application artifacts
- B. Provide a way of tracking which user developed an application
- C. Provide a namespace to prevent cross-application name collisions
- D. Provide controls for how scripts from another scope can alter tables in a scoped application

---
### Domain 6 — Practice Answers

| Q | Answer | Src | Why |
|---|--------|-----|-----|
| Q174 | B | web | There is **no Copy button** that installs an application. Repository, Share and Store are all real distribution routes. |
| Q175 | A, C & D | web | Store, application repository, and update set. Local drives and spreadsheets are not publication targets. |
| Q176 | C | web | A database containing **custom** applications — your organisation's own apps, as distinct from the Store (third-party). |
| Q177 | C | web | The **Application Files** related list on the application record is the definitive artifact inventory. |
| Q178 | B | web | Update sets. Contrast with the Application Repository (Q62), which distributes versioned applications rather than moving config between environments. |
| Q179 | A, C & E | web | User name, password, URL. **Application name is not required** — that is the distractor, and it is also the answer to the inverted "which is NOT required" phrasing. Note "URI" is offered as a near-miss for "URL". |
| Q180 | B | web | Through a **MID Server**. |
| Q181 | C | web | **Stash** parks uncommitted local changes so you can switch context and reapply them later. A *branch* is a parallel line of development and a *tag* marks a point in history — neither shelves work in progress. |
| Q182 | B | web | Records are shipped with an application only when added via **Create Application Files**. Table extension, numbering and clone-exclusion have nothing to do with it. |
| Q183 | D | web+docs | **Confirmed against the docs:** "Developer permissions are available only for scoped apps, **not global apps**" (`delegated-development-and-deployment/t_AddADeveloper.md`). So granting non-admins the ability to develop *global* applications is the incorrect statement. The other three are documented controls. A dump keyed A; it is wrong. |
| Q184 | D | web | The **Publish** button. |
| Q185 | A | web | All custom scopes **plus Global**. B is wrong because baseline apps like Incident are not scoped applications in the picker sense. |
| Q186 | D | web | Selecting an application **sets the Application Scope** — which is exactly why Q64 (wrong scope in the status bar) is a real hazard. |
| Q187 | A & B | web+docs | ATF and Flow Designer work with global applications. **Delegated Development is documented as scoped-only** — "Developer permissions are available only for scoped apps, not global apps" (`t_AddADeveloper.md`) — and scope protection policies are scoped by definition, so C and D are both out. |
| Q188 | A, B, D & F | web | Business problem, data in/out, process steps, users/stakeholders. Project schedule, database capacity and licensing are project-management concerns, not application design inputs. |
| Q189 | B | web | Scoping does **not** track who developed an application. It provides namespacing, artifact relationships and cross-scope controls. |

---

## Domain 4 — Application Automation (Practice, set 2)

**Q190.** Which module would you use to create a new automation of business logic such as approvals, tasks, and notifications?
- A. Process Automation > Workflow Editor
- B. Process Automation > Active Flows
- C. Process Automation > Process Flow
- D. Process Automation > Flow Designer
- E. Process Automation > Flow Administration

**Q191.** Where do Business Rules execute in the ServiceNow architecture?
- A. Client-side only
- B. Server-side only
- C. Both client and server-side
- D. Neither client nor server-side

**Q192.** Which are types of Business Rule based on when they execute in the transaction lifecycle?
- A. Before insert and Before update
- B. After insert and After update
- C. Display
- D. All of the above

**Q193.** Which two logging methods are available in a privately scoped application? *(Choose 2)*
- A. `gs.log()`
- B. `gs.info()`
- C. `gs.error()`
- D. `gs.print()`

**Q194.** Which is NOT supported by Flow Designer?
- A. Calling a subflow from a flow
- B. Testing a flow with rollback
- C. Using a Delegated Developer
- D. Running a flow from a MetricBase Trigger

---
### Domain 4 — Practice set 2 Answers

| Q | Answer | Src | Why |
|---|--------|-----|-----|
| Q190 | D | web | **Process Automation > Flow Designer.** "Active Flows", "Process Flow" and "Flow Administration" are invented module names; Workflow Editor is the legacy tool, not the one for new automation. |
| Q191 | B | web | Business Rules are **server-side only**. Contrast Q157: a UI Action can run either side. |
| Q192 | D | web | before, after **and** display are all "when" values (plus async). A question offering "All of the above" where each listed item is genuinely valid is usually keying "All of the above". |
| Q193 | B & C | web+docs | Scoped applications use `gs.info()`, `gs.warn()`, `gs.error()` and `gs.debug()`. ⚠️ **`gs.log()` is global-scope only and is the trap here** — one mined source keyed `gs.log()`, which is wrong for a *privately scoped* app. `gs.print()` does not exist. |
| Q194 | B | web+docs | **Testing does not roll back.** The docs say it outright: "Because testing a flow creates or changes records on the instance, flow designers should always test flows on a non-production instance" (`build-workflows/workflow-studio/flow-test.md`). ⚠️ **Corrected — this bank previously keyed D.** MetricBase *is* a supported trigger and has its own page (`create-mb-flow.md`), though it needs a separate subscription; `delegated_developer` appears throughout Workflow Studio; subflows are core. Two dump sites split between C and D, and the one this bank followed was the wrong one. |

---

## Domain 3 — Security and Restricting Access (Practice, set 2)

**Q195.** What setting allows users to view a Knowledge Base article even if they are not logged in?
- A. The ESS role
- B. The Allow All role
- C. The Public setting
- D. The View All setting

---
### Domain 3 — Practice set 2 Answers

| Q | Answer | Src | Why |
|---|--------|-----|-----|
| Q195 | C | web | The **Public** setting. Pairs with Q127: *User Criteria* controls who can read/contribute within a knowledge base for logged-in users; *Public* is what exposes an article to anonymous visitors. |

---

## Domain 1 — Designing and Creating an Application (Practice, set 2)

**Q196.** Which ServiceNow utility provides a modern interactive graphical interface to visualise configuration items and their relationships?
- A. Class Map
- B. Flow Design
- C. Dependency View
- D. Business Service Map

**Q197.** What do you click when you have made modifications to a report and want to see the results without saving?
- A. Execute
- B. Preview
- C. Run
- D. Test

**Q198.** What provides a graphical view of the relationships among tables?
- A. Schema map
- B. Dependency view
- C. Business Service Map
- D. Map source report

**Q199.** Which is the base table of the configuration management database hierarchy?
- A. `cmdb_rel_ci`
- B. `ucmdb`
- C. `cmdb_ci`
- D. `cmdb`

---
### Domain 1 — Practice set 2 Answers

| Q | Answer | Src | Why |
|---|--------|-----|-----|
| Q196 | C | web | **Dependency View** — configuration items and their relationships. |
| Q197 | B | web | **Preview** renders the modified report without committing the change. |
| Q198 | A | web | **Schema map** — *table* relationships in the data model. Q196/Q198 are the pair that catches people: both stems say "graphical view of relationships", so read whether it says **configuration items** (dependency view) or **tables** (schema map). |
| Q199 | C | web | **`cmdb_ci`** is the base configuration-item class that every CI table extends. `cmdb_rel_ci` stores CI *relationships*, and `ucmdb` is a different vendor's product. |

---

## Domain 4 — Application Automation (Flow Designer deep dive)

**Q200.** What role does the trigger play in a flow?
- A. It specifies where the flow should execute
- B. It specifies what the flow should execute
- C. It specifies when the flow should execute
- D. It specifies why the flow should execute

**Q201.** What is an action responsible for in a flow?
- A. Specifying when the flow should execute
- B. Specifying why the flow should execute
- C. Specifying where the flow should execute
- D. Specifying what the flow should execute

**Q202.** What is the main purpose of flow logic?
- A. It allows the system scheduler to determine execution timing
- B. It provides users manual time selection for flow launch
- C. It is a programming structure for decisions and logical choices
- D. It enables developers to keep flows organised

**Q203.** Which three are valid Flow Designer trigger types? *(Choose 3)*
- A. Record-based
- B. Notification-based
- C. Application-based
- D. Schedule-based
- E. Condition-based

**Q204.** On a record trigger, which Run Trigger option fires the flow on **every** update, even if a context for that flow is already running?
- A. Only if not currently running
- B. Once
- C. For every update
- D. For each unique change

**Q205.** Which three are components of an action? *(Choose 3)*
- A. Transitions
- B. Outputs
- C. Inputs
- D. Activities
- E. Steps

**Q206.** What are action outputs?
- A. Data variables representing the results of the action
- B. Data variables the action requires to begin processing
- C. Data variables used only within the action
- D. Data variables available to a parent flow after a subflow completes

**Q207.** What occurs when an action is added to a flow?
- A. The data pane is emptied
- B. The data pill picker selects fields via reference lookup
- C. Data pills are created to capture runtime variables
- D. The end user receives an email notification

**Q208.** What is used to pass data between a flow and a subflow?
- A. Inputs and outputs
- B. Activities
- C. An action
- D. The scratchpad

**Q209.** What are subflow inputs responsible for?
- A. The timing details of subflow execution
- B. Specifying the data available to the subflow when it launches
- C. The execution details of subflow operations
- D. Specifying the data available to the parent flow after the subflow completes

**Q210.** Which two are characteristics of a subflow? *(Choose 2)*
- A. It provides customers with self-service opportunities
- B. It contains inputs and outputs that pass data to and from the subflow
- C. It sequences reusable actions that can be started from a flow, subflow, or script
- D. It organises configuration activities into categories

**Q211.** Which step is NOT performed when a flow is processed?
- A. The system creates an entry in the event queue
- B. The system builds a process plan from the flow
- C. The system stores execution details in the syslog table
- D. The system runs the process plan using the triggering record

**Q212.** Which two roles grant full access to all Flow Designer features? *(Choose 2)*
- A. admin
- B. flow_operator
- C. flow_designer
- D. workflow_admin

**Q213.** Which three are reasons to create Flow Designer content in a scoped application rather than in Global? *(Choose 3)*
- A. Scoped apps can be shared via the application repository
- B. Scope helps categorise content for maintenance
- C. Scope protects applications from damage by others
- D. Scope limits access to Flow Designer itself

**Q214.** Which is NOT an example of when an application would use a Scheduled Script Execution?
- A. The application needs to send weekly email reminders for all records on a table
- B. The application needs to run a clean-up script on the last day of every month
- C. The application needs to query the database every day for unassigned records
- D. The application needs to run a client-side script at the same time every day

**Q215.** What is the Event Registry?
- A. A table containing a record for every Event known to the system, which allows ServiceNow to react when Events are generated
- B. A workflow launched every time an Event is generated, used to debug Events
- C. The method used in server-side scripts to generate Events and pass parameters
- D. The Event Log listing every Event that has been generated

**Q216.** Which three script types execute on the server? *(Choose 3)*
- A. Business Rule
- B. Client Script
- C. UI Policy
- D. Script Action
- E. Scheduled Job

---
### Domain 4 — Flow Designer deep dive Answers

| Q | Answer | Src | Why |
|---|--------|-----|-----|
| Q200 | C | web | Trigger = **when**. Q200/Q201 are a deliberate pair: trigger answers *when*, action answers *what*. Memorise the pairing, not the sentence. |
| Q201 | D | web | Action = **what**. |
| Q202 | C | web | Flow logic is the decision/branching structure (If, Else, For Each, Do Until). D describes annotations, not logic. |
| Q203 | A, C & D | web | Record, Application, Schedule. "Notification-based" and "Condition-based" do not exist as trigger types — a condition is part of a *record* trigger, not a type of its own. |
| Q204 | C | docs | **For every update** — "every time that the record is updated, regardless of whether there has already been or currently are any running contexts". The current four options are *For each unique change*, *Once*, *Only if not currently running*, *For every update*. ⚠️ **This replaces a broken question.** The mined version offered **Always**, which the docs say is the *previous-release name* for **Only if not currently running** — so two of its four options were the same thing under different names. If a stale exam item offers "Always", it means today's *Only if not currently running*. |
| Q205 | B, C & E | web | Inputs, Outputs, Steps. **Transitions and Activities belong to legacy Workflow**, not Flow Designer — that is the trap in this item. |
| Q206 | A | web | Outputs = the action's **results**. B describes inputs; D describes subflow outputs. |
| Q207 | C | web | **Data pills** are generated to represent the action's runtime values. See Q129. |
| Q208 | A | web | Inputs and outputs. Note `g_scratchpad` is a *form* mechanism (Q145) and has nothing to do with flows — D is the cross-topic trap. |
| Q209 | B | web | Subflow **inputs** define what goes in at launch; subflow **outputs** define what comes back to the parent (which is option D, and the answer to Q206's distractor). |
| Q210 | B & C | web | Inputs/outputs, and reusable action sequences callable from a flow, subflow, or script. |
| Q211 | C | web | Flow execution details are **not** written to `syslog`; they go to the flow execution/context records. The other three all happen. |
| Q212 | A & C | web | `admin` and `flow_designer`. `flow_operator` is read/run-only; `workflow_admin` belongs to legacy Workflow. |
| Q213 | A, B & C | web | Repository sharing, maintenance categorisation, and protection. D is false — scoping does not restrict access to Flow Designer as a tool. |
| Q214 | D | web | Scheduled jobs are **server-side**; there is no such thing as scheduling a client-side script. Recurring server work (A, B, C) is exactly what they are for. |
| Q215 | A | web | A table of every known Event, letting the system react when one is queued. C describes `gs.eventQueue()`; D describes the Event Log. |
| Q216 | A, D & E | web | Business Rules, Script Actions and Scheduled Jobs are all server-side. Client Scripts and UI Policies are browser-side. |

---

## Domain 3 — Security and Restricting Access (Practice, set 3)

**Q217.** A table has three fields: field1, field2, field3. The Access Control list is: `table.None` read for admin and itil; `table.*` read for admin only; `table.field3` read for itil. Which field or fields can a user with only the itil role read?
- A. field1, field2 and field3
- B. field3 only
- C. field1 and field3
- D. All fields except field3

**Q218.** How must Application Access be configured to prevent all other private application scopes from creating configuration records on an application's data tables?
- A. Create Access Controls instead; Application Access cannot do this
- B. Set Accessible from to All application scopes and clear Can create
- C. Set Accessible from to This application scope only and clear the web services option
- D. Set Accessible from to This application scope only

**Q219.** A customer requires that Incident numbers are read-only on all lists and forms for all users, and that Short description is mandatory on insert across all applications. Which type of policy meets this?
- A. Dictionary Design Policy
- B. Field Criteria Policy
- C. Data Quality Policy
- D. Data Policy

**Q220.** Which tab on a knowledge base record identifies the sets of users able to read articles in that knowledge base?
- A. Access List
- B. Can Access
- C. Accessible to
- D. Can Read

---
### Domain 3 — Practice set 3 Answers

| Q | Answer | Src | Why |
|---|--------|-----|-----|
| Q217 | B | web | **field3 only.** Work it field by field: field1 and field2 have no field-specific rule, so they fall back to `table.*` — which is **admin only**, so itil fails. field3 has its own itil rule, so it passes. ⚠️ Compare Q107, which looks almost identical but has **no `table.*` rule** and therefore answers "field1 and field2". The presence or absence of the wildcard row flips the answer completely — read the ACL list, not the shape of the question. |
| Q218 | D | web | **Accessible from = This application scope only.** That single setting closes design-time access from every other scope; you do not also need to touch web services (C) and clearing Can create (B) does not stop *configuration* records. |
| Q219 | D | web | **Data Policy** — the giveaway is "across all applications" and "on insert", i.e. enforcement independent of the form. A UI Policy could not satisfy either clause. Reinforces Q69. |
| Q220 | D | web | The **Can Read** tab. |

---

## Domain 5 — Working with External Data (Practice, set 2)

**Q221.** What is the purpose of the coalesce field when importing data?
- A. When a match is found, a new record is inserted
- B. To determine whether a record matches an existing record or is a new record
- C. If a match is not found, the existing record is updated
- D. To identify and merge duplicate records

**Q222.** Which of the following is NOT a method used by the ServiceNow REST API?
- A. COPY
- B. POST
- C. GET
- D. DELETE

**Q223.** Application developers can specify which page a user sees after submitting a record through a Record Producer. How is that page specified?
- A. An after Business Rule on the target table setting `window.redirect`
- B. An application property storing the URL
- C. A script in the Record Producer's Script field setting `producer.redirect = "<URL>"`
- D. Configuration on the module that opens the Record Producer

**Q224.** Which one allows the creation of a task-based record from the Service Catalog?
- A. UI Builder
- B. Flow Designer
- C. Assignment Rule
- D. Record Producer

---
### Domain 5 — Practice set 2 Answers

| Q | Answer | Src | Why |
|---|--------|-----|-----|
| Q221 | B | web | Coalesce = the **match test**. A and C state the behaviour backwards (match → update, no match → insert), which is exactly how this item is made hard. See Q162/Q163. |
| Q222 | A | web | **COPY** is not a REST verb here. GET, POST, PUT, PATCH and DELETE are. |
| Q223 | C | web+docs | **`producer.redirect = "<URL>";`** in the Record Producer's Script field. ⚠️ The mined source keyed "an application property" — that is wrong; a property stores a value, it does not perform a redirect. Note this uses the same `producer` object as Q78. |
| Q224 | D | web | **Record Producer** — a catalog front end that creates a task-based record. See Q76. |

---

## Domain 1 — Designing and Creating an Application (Practice, set 3)

**Q225.** When designing a form, what do you create to organise fields on the form?
- A. Related lists
- B. Tabs
- C. Sections
- D. Buttons

**Q226.** What is the name of the string that displays the filter criteria on a list?
- A. Breadcrumb
- B. Choice
- C. Menu
- D. Topic

**Q227.** On a form, which field type shows an icon that can be clicked to preview the associated record?
- A. Reference
- B. Lookup
- C. Quickview
- D. Drilldown

**Q228.** Which three tables are available by default in a ServiceNow instance? *(Choose 3)*
- A. Task
- B. Item
- C. User
- D. Incident
- E. Project

**Q229.** What is the ServiceNow Store?
- A. The source for ServiceNow Community created developer content
- B. A marketplace for free and paid certified ServiceNow applications and integrations
- C. A downloadable ServiceNow script archive
- D. An alternate name for the ServiceNow Developer Share site

**Q230.** What is the best practice regarding the Default update set for moving customisations between instances?
- A. Submit the Default update set to the application repository
- B. You should not use the Default update set for moving between instances
- C. Keep the Default update set to a maximum of 20 records for troubleshooting
- D. Merge Default update sets before moving between instances

---
### Domain 1 — Practice set 3 Answers

| Q | Answer | Src | Why |
|---|--------|-----|-----|
| Q225 | C | web | **Sections**. Tabs are how sections are *displayed*, but the thing you create is a section. |
| Q226 | A | web | The **breadcrumb** shows and lets you unwind filter conditions. |
| Q227 | A | web | **Reference** fields carry the preview (ⓘ) icon. "Lookup", "Quickview" and "Drilldown" are not field types. |
| Q228 | A, C & D | web | Task, User (`sys_user`) and Incident ship with the platform. "Item" and "Project" are not baseline tables in this sense. |
| Q229 | B | web | A **marketplace for certified apps and integrations**, free and paid. A/D describe **Share**, the community site — Store vs Share is the distinction being tested (see Q174). |
| Q230 | B | web | **Never use the Default update set to move changes.** It is the catch-all for work done outside a named set; always create and select your own update set first. |

---

## Domain 1 — Designing and Creating an Application (Practice, set 4)

**Q231.** The Task table is an example of which two of the following? *(Choose 2)*
- A. Legacy class
- B. Child class
- C. Base class
- D. Parent class

**Q232.** Tables that extend another table do what?
- A. Sometimes inherit the parent's fields
- B. Automatically update the application scope
- C. Do not inherit the parent's fields
- D. Inherit the parent's fields

**Q233.** What do you install when you want to add applications or functionality within your development instance?
- A. Patch
- B. Update Pack
- C. App Package
- D. Plugin

**Q234.** Which one of the following is NOT true for Modules?
- A. Access to Modules is controlled with roles
- B. Modules open content pages
- C. Every Module must be associated with a table
- D. Every Module must be part of an Application Menu

---
### Domain 1 — Practice set 4 Answers

| Q | Answer | Src | Why |
|---|--------|-----|-----|
| Q231 | C & D | web | Task is the **base** class of the task hierarchy and the **parent** of Incident, Problem, Change and so on. It is never a child — nothing sits above it. |
| Q232 | D | web | Extension **inherits the parent's fields** — unconditionally, not "sometimes". Reinforces Q42/Q55. |
| Q233 | D | web | A **Plugin**. ⚠️ The source keyed this as "Patch, Update Pack, App Package" — that is wrong, and a good example of why these keys need checking. Patches and update packs are *upgrade* artifacts; plugins are what you activate to add functionality. |
| Q234 | C | web | A module need **not** be tied to a table — it can open a URL, a content page, or run a script. ⚠️ One source keyed D instead ("must be part of an Application Menu"), but modules do live under an application menu, so D is a true statement and cannot be the answer to a NOT question. |

---

## Domain 2 — Application User Interface (Practice, set 2)

**Q235.** You are looking at a list of Active Incidents and want to exclude Incidents with the State of Resolved. How might you do that?
- A. On the State column title, right-click and select Filter Out > Resolved
- B. On the list of records, locate and right-click the Resolved value, then select Exclude
- C. Click the funnel icon, click AND, select Resolved, Is Not, State, then click Run
- D. On the list of records, locate and right-click the Resolved value, then select Filter Out

---
### Domain 2 — Practice set 2 (cont.) Answers

| Q | Answer | Src | Why |
|---|--------|-----|-----|
| Q235 | D | web | Right-click the **value** in the list and choose **Filter Out**. A is wrong because you right-click the value, not the column title; B invents an "Exclude" item; C has the condition operands in the wrong order. |

---

## Domain 2 — Application User Interface (Official sample items)

> These come from the **official ServiceNow CAD exam specification** (KB0011498, "Sample Questions").
> They are published by ServiceNow as representative of the real exam — the highest-authority items in
> this bank. Keys are ServiceNow's own.

**Q236. ⭐** Which method is valid for `GlideUser()`?
- A. `getUserName()`
- B. `getFullName()`
- C. `getRole()`
- D. `getRoleExactly()`

---
### Domain 2 — Official sample Answers

| Q | Answer | Src | Why |
|---|--------|-----|-----|
| Q236 ⭐ | B | official | `getFullName()` is a real GlideUser method. **Trap:** `hasRole()` and `hasRoleExactly()` exist, but `getRole()` / `getRoleExactly()` do not — the verb is `has`, not `get`. And the login name is the **property** `g_user.userName`, not a `getUserName()` method. Compare Q110/Q111. |

---

## Domain 4 — Application Automation (Official sample items)

**Q237. ⭐** How do you configure a Scheduled Job to execute on the last day of every month?
- A. Set the Run field value to Periodically and the Repeat Interval value to 31
- B. Set the Run field value to Periodically and the Repeat Interval value to Last Day
- C. Set the Run field value to Monthly and the Day field value to 31
- D. Set the Run field value to Monthly and the Day field value to Last Day

---
### Domain 4 — Official sample Answers

| Q | Answer | Src | Why |
|---|--------|-----|-----|
| Q237 ⭐ | C | official | **Monthly + Day 31.** ServiceNow clamps the day to the end of shorter months, so 31 means "last day" for every month. **Trap:** D reads more naturally in English, but the Day field takes a number — there is no "Last Day" value. Periodically counts a fixed interval and drifts against calendar months. |

---

## Domain 6 — Managing Applications (Official sample items)

**Q238. ⭐** When managing global application files, which action is allowed?
- A. Moving application files into or out of the scoped application
- B. Adding files from global scope to a global application
- C. Changing the scope of a global application
- D. Removing an application's scope

---
### Domain 6 — Official sample Answers

| Q | Answer | Src | Why |
|---|--------|-----|-----|
| Q238 ⭐ | B | official | Global-to-global file moves are permitted. **The other three are all things scope exists to prevent:** you cannot drag files across a scope boundary (A), cannot re-scope an existing application (C), and cannot strip an application's scope (D). Useful anchor — scope is assigned at creation and is effectively permanent. |

---

## Domain 5 — Working with External Data (Practice, set 3)

**Q239.** Which utility determines whether field names in an Import Set match the field names on the target table?
- A. Auto Map Matching Fields
- B. Schema Map
- C. Mapping Assist
- D. Field Watcher

**Q240.** Which two statements about the Import Set table are correct? *(Choose 2)*
- A. It is a staging table that holds the raw imported rows
- B. It is the final destination of the imported data
- C. Its rows are transformed onto the target table by a Transform Map
- D. It must be created manually before every import

**Q241.** During a transform, which script runs once before the entire transform begins?
- A. onStart
- B. onBefore
- C. onAfter
- D. onComplete

**Q242.** A Transform Map field map needs to derive the target value from several source columns. What should be used?
- A. A coalesce field
- B. A source script on the field map
- C. A Data Policy
- D. A Business Rule on the import set table

**Q243.** Two field maps on the same Transform Map are both marked as coalesce. What is the effect?
- A. Only the first coalesce field is used
- B. The import fails validation
- C. A record matches only when both values match
- D. A record matches when either value matches

**Q244.** Which Data Source format options are available for a file-based import? *(Choose 2)*
- A. CSV
- B. Excel (XLSX)
- C. DOCX
- D. PPTX

**Q245.** A scheduled import needs to pull a file from an external server behind the customer's firewall. What is required?
- A. A MID Server
- B. A Scripted REST API
- C. An Outbound REST Message
- D. A Data Policy

**Q246.** Which statement about the `sys_import_set_row` table is correct?
- A. It stores the Transform Map definitions
- B. It stores the raw staged rows for an import set
- C. It stores the transformed target records
- D. It stores the data source connection details

**Q247.** In an Outbound REST Message, where do you define a value that will be supplied at call time?
- A. A variable substitution such as `${record_number}`
- B. A coalesce field
- C. A data policy
- D. A UI policy

**Q248.** Which two are true of a Scripted REST API? *(Choose 2)*
- A. It defines a custom inbound endpoint that external systems call
- B. It is used by ServiceNow to call an external system
- C. Each resource specifies an HTTP method and a relative path
- D. It replaces the need for authentication

**Q249.** Which HTTP status code family indicates the request succeeded?
- A. 2xx
- B. 3xx
- C. 4xx
- D. 5xx

**Q250.** A REST call from ServiceNow returns HTTP 401. What does that indicate?
- A. The endpoint does not exist
- B. Authentication failed or was not supplied
- C. The server encountered an internal error
- D. The request was malformed

**Q251.** Which object is used in a script to send an outbound REST request in a scoped application?
- A. `sn_ws.RESTMessageV2`
- B. `GlideRecord`
- C. `GlideAjax`
- D. `sn_import.ImportSet`

**Q252.** After running a transform, where do you look to see which source rows failed and why?
- A. The Import Set Run history and the transform log
- B. The System Log > Emails
- C. The Update Set list
- D. The Schema Map

**Q253.** Which two are valid ways to bring spreadsheet data into ServiceNow? *(Choose 2)*
- A. Load Data from an attached CSV or Excel file
- B. Create a Data Source pointing to a file, then schedule the import
- C. Paste the rows into a UI Page
- D. Attach the file to an Update Set

**Q254.** What does the Run Transform step actually do?
- A. Uploads the file into the import set table
- B. Applies the Transform Map to move staged rows onto the target table
- C. Deletes the import set table
- D. Publishes the application

---
### Domain 5 — Practice set 3 Answers

| Q | Answer | Src | Why |
|---|--------|-----|-----|
| Q239 | A | authored | **Auto Map Matching Fields** matches source columns to target fields by name. This item appears in the official sample list but ServiceNow published it without its options, so the options here are authored. Schema Map shows table relationships (Q198); Mapping Assist is the manual drag-and-drop mapper; Field Watcher is a debugging tool. |
| Q240 | A & C | authored | The import set table is a **staging** table; a Transform Map moves its rows to the target. It is created automatically by the load, so D is false, and it is never the final destination (B). |
| Q241 | A | authored | **onStart** runs once at the beginning; **onComplete** once at the end. onBefore/onAfter run **per row** (Q173). Learn the pair: Start/Complete bracket the run, Before/After bracket each row. |
| Q242 | B | authored | A **source script** on the field map computes the value. Coalesce is for matching, not deriving. |
| Q243 | C | authored | Multiple coalesce fields form a **composite key** — all must match for the row to be treated as an update. A common real-world surprise: adding a second coalesce field makes matching *stricter*, so previously-updating rows start inserting. |
| Q244 | A & B | authored | CSV and Excel. Word and PowerPoint are not import formats. |
| Q245 | A | authored | A **MID Server** reaches resources behind the firewall — the same answer as the source-control case in Q180. If a question says "behind a firewall", the answer is almost always MID Server. |
| Q246 | B | authored | `sys_import_set_row` holds the **staged rows**. |
| Q247 | A | authored | Variable substitution `${...}` in the endpoint or body, supplied at call time. Same syntax family as the SOAP case in Q167. |
| Q248 | A & C | authored | Scripted REST API = **inbound**, with resources defined by HTTP method plus relative path. B describes an Outbound REST Message — the direction is the whole distinction (Q169/Q170). D is never true of anything. |
| Q249 | A | authored | 2xx = success, 3xx = redirect, 4xx = client error, 5xx = server error. |
| Q250 | B | authored | **401 = unauthorised**, i.e. credentials missing or rejected. 404 is "does not exist", 500 is server error, 400 is malformed. Worth knowing 401 vs 403: 401 means "who are you?", 403 means "I know who you are and you still can't." |
| Q251 | A | authored | `sn_ws.RESTMessageV2` is the scoped outbound REST API. The `sn_ws` namespace is the tell. |
| Q252 | A | authored | The Import Set Run history plus the transform log record row-level errors. |
| Q253 | A & B | authored | Load Data (ad hoc) or a Data Source plus schedule (repeatable). Update sets carry configuration, not data (Q178). |
| Q254 | B | authored | Run Transform applies the map from staging to target — the third of the three steps in Q161. |

---

## Domain 2 — Application User Interface (New questions, v2)

> Gap-filling set written directly from the Australia-release documentation. Every answer row cites the file that settles it.

**Q255.** According to ServiceNow's guidance, how do UI policies compare with client scripts for showing, hiding, or requiring a field?
- A. Client scripts load faster, so they are preferred
- B. Both can perform these actions, but UI policies are preferred because they load faster
- C. Only client scripts can make a field mandatory
- D. UI policies run only on form load; client scripts run on change

**Q256.** A UI policy's condition references a field that is not on the form layout. What happens?
- A. The condition is skipped because the field is not on the form
- B. The condition still evaluates — UI policy conditions evaluate all fields whether or not they appear on the form
- C. The UI policy deactivates itself
- D. The form raises a client-side error

**Q257.** Which role is required to create a UI policy?
- A. ui_policy_admin
- B. personalize_form
- C. ui_admin
- D. form_admin

**Q258.** A UI policy needs to do something more complex than making fields visible, mandatory, or read-only. What do you use?
- A. Convert it to a data policy
- B. Select the Run scripts option on the UI policy
- C. Replace it with an access control
- D. Add a Business Rule on the same table

**Q259.** Which three conditions must hold before a UI policy can be converted to a data policy? *(Choose 3)*
- A. The Run scripts check box must be cleared
- B. The Global check box must be selected
- C. Every UI policy action must have Visible set to Leave Alone
- D. The UI policy must already be inactive
- E. The policy must affect exactly one field
- F. The table must be in the global scope

**Q260.** What happens to the UI policy when you convert it to a data policy?
- A. Nothing — both stay active independently
- B. The UI policy is deactivated; to keep enforcing it on the form, select Use as UI Policy on client on the data policy
- C. The UI policy is deleted
- D. The new data policy is created read-only

**Q261.** Why choose a data policy over a UI policy to make a field mandatory?
- A. Data policies render faster on the form
- B. A data policy also applies to import sets and data arriving via SOAP web services, not just the form
- C. Data policies can run client-side scripts
- D. Data policies apply only to the desktop UI

**Q262.** Where are UI policies not supported?
- A. Forms in the Content Management System
- B. Search screens
- C. Lists in the Content Management System
- D. Forms on extended tables

**Q263.** What does a record producer create?
- A. A requested item in the Service Catalog
- B. A task-based record, such as an incident
- C. An import set row
- D. A catalog item definition

**Q264.** A developer wants users to raise a requested item through the catalog. Should they build a record producer for it?
- A. Yes — record producers are the standard way to create requested items
- B. No — record producers should create task-based records only; use a catalog item so standard catalog processes such as workflows run as expected
- C. Yes, provided the table is in the same scope
- D. No, requested items can only be created by an import

**Q265.** For which tables can you create a record producer? *(Choose 2)*
- A. Tables and database views in the same scope as the record producer
- B. Tables in other scopes that allow create access from other applications
- C. Any table on the instance, regardless of scope or access
- D. Only tables that extend Task in the global scope

**Q266.** Which of these should a record producer script avoid?
- A. Calling current.update()
- B. Reading values from the producer object
- C. Setting field values on current
- D. Redirecting the user after submission

**Q267.** An automated test creates records while it runs. What happens to that data when the test finishes?
- A. It stays on the instance and must be removed manually
- B. The system rolls the data back once all steps in the test complete
- C. It is copied to an archive table
- D. It is committed only if every step passed

**Q268.** How does running an ATF test differ from testing a flow in Flow Designer?
- A. ATF rolls back the data it creates; testing a flow creates or changes records on the instance
- B. Testing a flow rolls back; ATF does not
- C. Neither one creates records
- D. Both roll back automatically

**Q269.** Where should automated tests be run?
- A. On a non-production instance
- B. On production, outside business hours
- C. On any instance, because ATF is read-only
- D. Only inside a scoped application

**Q270.** Which ATF feature lets you pause a test part-way through a run in order to troubleshoot it?
- A. Breakpoints
- B. Step templates
- C. Parameterized data
- D. Test suites

**Q271.** Several tests need the same opening sequence of steps. What saves rebuilding it each time?
- A. Copy the whole test and rename it
- B. Add a predefined list of steps — a template — to the test
- C. Move the steps into a Script Include
- D. Group the tests into a test suite

**Q272.** Which two are true of automated test steps? *(Choose 2)*
- A. Data can be passed from one test step to another
- B. Form steps can produce results screenshots
- C. Each step is isolated and cannot see anything an earlier step did
- D. Test steps can only run server-side

---
### Domain 2 — New questions (v2), answers

| Q | Answer | Src | Why |
|---|--------|-----|-----|
| Q255 | B | v2 | `platform-administration/t_CreateAUIPolicy.md` states both halves: UI policies "dynamically change the behavior of information on a form", and "You can also use client scripts to perform all of these actions, but **for faster load times use UI policies when possible**." The capability overlaps; the tie-breaker is performance. **Trap on A:** the preference runs the other way. |
| Q256 | B | v2 | `t_CreateAUIPolicy.md`: "A UI policy condition evaluates all fields even if they are not visible on the form. This function removes the requirement that a field must be on a form for it to be evaluated." The field does not need to be on the layout. |
| Q257 | A | v2 | **`ui_policy_admin`**, stated under Before you begin in `t_CreateAUIPolicy.md`. The others are invented. Navigation is All > System UI > UI Policies. |
| Q258 | B | v2 | `t_CreateAUIPolicy.md`: "Basic UI policies do not require any scripting, however for more advanced actions, use the **Run scripts** option." Note the knock-on for Q259 — turning Run scripts on makes the policy ineligible for conversion to a data policy. |
| Q259 | A, B & C | v2 | `t_ConvertAUIPolicyToADataPolicy.md` lists exactly these three: Run scripts cleared, Global selected, and no action with Visible set to True or False — Visible must be Leave Alone. The policy does **not** need to be inactive first. |
| Q260 | B | v2 | Same doc: "Converting a UI policy to a data policy deactivates the UI policy. To retain the policy in the UI, ensure that the **Use as UI Policy on client** check box is selected on the data policy record." An easy mark lost by assuming both keep running. |
| Q261 | B | v2 | Same doc: "You can also apply a UI policy to import sets or to data imported by SOAP web services when you convert it to a data policy." **The discrimination:** a UI policy guards the form; a data policy guards the data whichever route it arrives by. |
| Q262 | B | v2 | `t_CreateAUIPolicy.md`: "UI policies are not supported on search screens." The same note rules out the distractors — "UI Policies also apply to forms and lists displayed within Content Management System application." |
| Q263 | B | v2 | `servicenow-platform/service-catalog/c_RecordProducer.md`: "A record producer is a specific type of catalog item that allows end users to create task-based records, such as incident records, from the service catalog... the record producer generates a task record such as incident, **instead of a requested item**." |
| Q264 | B | v2 | Same doc, stated as a rule: "Use a record producer to create task-based records only" and "To ensure that standard service catalog processes are followed, such as initiating workflows as expected, **do not create requested item records from record producers**. Instead, create requested item using catalog items." |
| Q265 | A & B | v2 | Same doc: "You can create a record producer for tables and database views that are in the same scope as the record producer. You can also create a record producer for tables that allow create access from applications in other scopes." C ignores scope; D invents a Task-only limit. |
| Q266 | A | v2 | Same doc: "Do not call the update, setAbortAction method, or set the sys_class_name on current record to avoid unexpected behavior." Setting fields and redirecting are the record producer's normal job. Related fact: if the script aborts generation, no row is written to Item Produced Record [sc_item_produced_record]. |
| Q267 | B | v2 | `automated-test-framework-atf/atf-run-test.md`: "If your test creates data, the system rolls back that data after all steps in the test complete." |
| Q268 | A | v2 | **The pair to memorise.** ATF rolls back (`atf-run-test.md`); flow testing does not — `build-workflows/workflow-studio/flow-test.md` says "Because testing a flow creates or changes records on the instance, flow designers should always test flows on a non-production instance." Both advise a sub-production instance, but only one cleans up after itself. |
| Q269 | A | v2 | `atf-run-test.md` says it twice, including in the page description: "After creating an automated test, run it on a non-production instance." Rollback covers data the test creates, not every side effect it triggers. |
| Q270 | A | v2 | `atf-breakpoints-rollback.md`: "Breakpoints allow you to pause your test at any step of a test run in order to troubleshoot and test authoring." |
| Q271 | B | v2 | `atf-build-overview.md`: "Some steps frequently occur in the same sequence in many different tests, so you can add a predefined list of steps (template) to an automated test." **Trap on D:** a test suite groups whole tests; it does not share steps between them. |
| Q272 | A & B | v2 | `atf-build-overview.md` names both: "Passing data from one automated test step to another", and for tests involving form steps, "View results screenshots from an automated test." C contradicts A directly. |

---

## Domain 4 — Application Automation (New questions, v2)

> Gap-filling set written directly from the Australia-release documentation. Every answer row cites the file that settles it.

**Q273.** Which method reads a system property in a scoped application and returns a fallback when the property does not exist?
- A. gs.getProperty(key, alt)
- B. gs.getValue(key, alt)
- C. gs.property(key, alt)
- D. gs.readProperty(key, alt)

**Q274.** Which call sets a property's value together with a description?
- A. gs.setProperty(key, value, description)
- B. gs.putProperty(key, value, description)
- C. gs.property.set(key, value, description)
- D. gs.updateProperty(key, value, description)

**Q275.** Which table stores system properties?
- A. sys_properties
- B. sys_config
- C. sys_app_property
- D. sys_settings

**Q276.** Why store a configurable value as an application property instead of hard-coding it in a script?
- A. Properties are encrypted at rest
- B. An administrator can change the value without editing the script
- C. Properties are evaluated faster than variables
- D. Properties are the only way to share a value between scopes

**Q277.** What type does gs.getProperty() return?
- A. String
- B. Boolean
- C. GlideRecord
- D. Whatever type the property was declared as

**Q278.** A property holds the text "false". A script runs `if (gs.getProperty('my.flag')) { ... }`. What happens?
- A. The block is skipped, because the value is false
- B. The block runs, because the returned value is the non-empty string "false", which is truthy
- C. The script throws a type error
- D. The block runs only in the global scope

**Q279.** You have created a new event and a business rule that fires it. What must you do so notifications and script actions can respond to it?
- A. Register the event in the event registry
- B. Restart the instance
- C. Attach the event to a scheduled job
- D. Nothing — events are discovered automatically

**Q280.** What does registering an event make possible? *(Choose 2)*
- A. Email and SMS notifications can see it in their list of available events
- B. Script Actions can react to it when it occurs
- C. The event is written to the syslog table automatically
- D. The event runs immediately instead of being queued

**Q281.** Which of these is NOT something a scheduled job is used for?
- A. Generating and distributing a report automatically
- B. Generating records from a template on a recurring schedule
- C. Running a script at the end of the month
- D. Reacting to a record the moment a user saves it

**Q282.** A scheduled job has been added to the scheduler queue and is waiting to run. Which state is it in?
- A. Ready
- B. Queued
- C. Running
- D. Error

**Q283.** Which scheduled job state means the job will run at its next scheduled interval?
- A. Ready
- B. Queued
- C. Running
- D. Waiting

**Q284.** Where do you monitor both event processing and scheduled job processing?
- A. The System Events and Jobs Dashboard
- B. The System Log
- C. The flow execution list
- D. The Transaction Log

**Q285.** What does a Script Include define?
- A. Either an object class or a function, reusable by server-side scripts
- B. A client-side library loaded on every form
- C. A recurring unit of scheduled work
- D. A REST endpoint

**Q286.** Which recommendation appears in ServiceNow's guidance on Business Rules?
- A. Use global Business Rules instead of Script Includes
- B. Use Script Includes instead of global Business Rules
- C. Run Business Rules without conditions so they never miss a change
- D. Finish every Business Rule with current.update()

**Q287.** Which of these should be avoided inside a Business Rule?
- A. current.update()
- B. Setting a field on current in a before rule
- C. Using a condition to control when the rule runs
- D. Calling a Script Include

**Q288.** The same logic is needed by a UI Action and by a Scripted REST API. What is the recommended structure?
- A. Call the Business Rule from the UI Action
- B. Put the logic in a Script Include and call it from both
- C. Duplicate the code in each place
- D. Call the UI Action from the Scripted REST API

**Q289.** Which Business Rule type is used to make server-side objects available to client-side scripts through g_scratchpad?
- A. Before
- B. After
- C. Async
- D. Display

**Q290.** Which four things does an email notification let an administrator specify? *(Choose 4)*
- A. When to send the notification
- B. Who receives it
- C. What content it contains
- D. Whether it can be delivered in an email digest
- E. Which mail server relays it
- F. The recipient's time zone

**Q291.** Which format do new email notifications use by default?
- A. Rich HTML
- B. Plain text
- C. Raw HTML source
- D. Markdown

**Q292.** What does the rich HTML format do to links that point at instance records?
- A. Converts relative URLs to absolute links so they do not break
- B. Shortens them to save space
- C. Strips them for security
- D. Forces them to open in a new tab

**Q293.** An email notification can also go out as an SMS. What does the system use as the SMS text by default?
- A. The subject line of the email notification
- B. The first line of the email body
- C. The name of the notification record
- D. A separate SMS-only notification record

---
### Domain 4 — New questions (v2), answers

| Q | Answer | Src | Why |
|---|--------|-----|-----|
| Q273 | A | v2 | `api-reference/server-api-reference/c_GlideSystemScopedAPI.md` documents `getProperty(String key, Object alt)` — "Gets the value of a Glide property. If the property is not found, returns an alternate value." The other three method names do not exist. |
| Q274 | A | v2 | Same reference, shown in its own example: `gs.setProperty("glide.foo","bar","foo")` — key, value, description. |
| Q275 | A | v2 | **`sys_properties`.** Confirmed by the configuration reference in `platform-security/instance-security-hardening-settings/sc-enable-report-view-acls.md`, which gives Configuration type as "System Properties (/sys_properties_list.do)". |
| Q276 | B | v2 | ⚠️ **The one v2 item not settled by a documentation quote.** The docs clone covers the property *API* (`c_GlideSystemScopedAPI.md`) and the `sys_properties` table, but has no page stating why you would prefer a property over a hard-coded value. B is the standard rationale — configuration separated from code, changeable without editing and re-testing a script. Answer it by elimination rather than by trusting B on its own: ordinary properties are **not** encrypted (A), and cross-scope sharing is governed by application access and cross-scope privileges, not properties (D). |
| Q277 | A | v2 | `c_GlideSystemScopedAPI.md` gives the return type as **String** — "The value of the Glide property, or the alternate object defined above." This is the fact behind Q278. |
| Q278 | B | v2 | Follows directly from Q277: the call returns the **string** "false", and every non-empty string is truthy in JavaScript, so the block runs. This is the most common application-property bug. Compare explicitly, e.g. `gs.getProperty('my.flag') === 'true'`. |
| Q279 | A | v2 | `platform-administration/system-events/c_EventRegistry.md`: "After you create a new event and a business rule that uses the event, you must register it." |
| Q280 | A & B | v2 | Same doc: "Registration lets other parts of the system, such as Email and SMS notifications and Script Actions, see the event in their list of available events and react to the event when it occurs." This is also why a Scheduled Script Execution is never the answer to "what consumes an event" — it runs on a clock, it does not subscribe. |
| Q281 | D | v2 | `platform-administration/time-configuration/c_ScheduledJobs.md` defines scheduled jobs as "automated pieces of work that can be performed at a specific time or on a recurring schedule" and lists A, B and C among the tasks they automate. Reacting the instant a record is saved is a Business Rule's job — that is the discrimination being tested. |
| Q282 | B | v2 | **Queued** — "Job has been added to the scheduler queue and is waiting to run" (`c_ScheduledJobs.md`). Paired deliberately with Q283; Ready and Queued are the two that get swapped. |
| Q283 | A | v2 | **Ready** — same doc as Q282: "Job is ready to run at the next scheduled interval." The four documented states are Ready, Running, Queued and Error; "Waiting" is invented. |
| Q284 | A | v2 | `c_ScheduledJobs.md`: "Use the System Events and Jobs Dashboard to monitor the system event processing system and the scheduled jobs processing system." One dashboard covers both. |
| Q285 | A | v2 | `application-development/business-rules-and-script-includes.md`: "Each Script Include defines either an object class or a function that can be reused among any server-side scripts." |
| Q286 | B | v2 | Same doc's good-practice list includes "Use Script Includes instead of global Business Rules" and "Always use a condition with Business Rules" — which also rules out C ("Business Rules rarely run with no conditions"). |
| Q287 | A | v2 | Same doc: "current.update() should not be used in any Business Rules. Using current.update() triggers an additional database operation, which could cause duplicate notifications, recursive loops, etc." Setting a field on current in a *before* rule is the documented normal pattern, so B is correct practice. |
| Q288 | B | v2 | Same doc, almost verbatim: "Instead of calling a Business Rule from a UI Action or a UI Action from a Scripted REST API, put the code in a Script Include and call the Script Include from both places." It also notes this lets you test the function before deploying it elsewhere. |
| Q289 | D | v2 | **Display.** Same doc's Business Rule timing table: Display runs "every time the corresponding form is displayed" and is "used to make server-side objects available to client-side scripts", with the worked example writing to `g_scratchpad`. Compare Q142 — a display rule has no `previous` object, because nothing has been saved yet. |
| Q290 | A, B, C & D | v2 | `platform-administration/c_EmailNotifications.md` lists exactly these four: when to send it, who receives it, what content it holds, and whether it can go in an email digest. Mail relay and recipient time zone are not part of the notification record. |
| Q291 | A | v2 | Same doc: "The rich HTML format is the default for all new email notifications." |
| Q292 | A | v2 | Same doc: "To avoid broken links, items like images and incidents, that are linked with URLs relative to an instance are converted to absolute links." |
| Q293 | A | v2 | Same doc: "The system uses the subject line of the email notification and converts it to an SMS message." An administrator can override this with an alternate SMS message on the email template or notification form. |
