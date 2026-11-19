---
name: fabric-data-agent-exercise-builder
description: |
  Builds company- and persona-specific hands-on labs that take participants from an empty Fabric workspace to a published Microsoft Fabric data agent: prerequisites, click-path steps, copy-ready agent and data source instructions, validated example SQL, test prompts with computed answers, synthetic CSV data, and a one-time PySpark ingestion notebook. Use when the user asks to "create a Fabric data agent exercise", "build a Fabric Data Agent workshop", "build a Fabric data agent lab", or "data agent hands-on for [company]". Do NOT use for Copilot Cowork exercises (copilot-cowork-exercise-builder), Copilot Studio exercises (copilot-studio-exercise-builder), other Copilot surfaces (copilot-exercise-builder), HTML formatting alone (copilot-exercise-html-formatter), or provisioning real Fabric items.
metadata:
  category: productivity
  icon: DatabaseSearch
---

# Fabric Data Agent Exercise Builder

Build a **hands-on lab** that takes a participant from an empty Fabric workspace to a working, tested, published
Fabric data agent, grounded in one company, one persona, and one business scenario. The skill also produces
everything the participant needs to succeed: realistic synthetic data, a one-time ingestion notebook, and every
piece of text they paste.

The unit of work is **one lab producing one data agent**. Exercises are its dependency-ordered parts, never
standalone labs. Audience: customer makers and analysts following along at a keyboard in their own tenant.

## Lab setup vs. the story (binding)

The lakehouse is the star: it **stands in for the customer's production lakehouse** (curated tables a data team
already refreshes nightly). The CSV files, the upload, and the ingestion notebook are **only the mechanism
that stands that lakehouse up for the lab**, run once. Keep them out of the story.

- **No scheduled job.** The import runs once. Lab Setup shows where a notebook schedule is configured (open the
  scheduler, then close it with the schedule off) and never has the participant turn one on, set a recurrence, or
  check Monitor for scheduled runs.
- **Browser only.** The notebook is imported as `.ipynb` from the workspace toolbar (Import > Notebook > From this
  computer). Never require VS Code or other local tools, and never have participants paste notebook code.
- **Closed files.** The pre-flight checklist has participants save the lab files in one folder with none open in
  Excel or another app, so uploads are not blocked by a file lock.

- Put the data load in a clearly labeled **Lab Setup** section (steps S1-S5) after Prerequisites and before
  Exercise 1. Open it with one sentence: these steps stand up a lakehouse that mirrors the production HR (or
  domain) lakehouse; in a real deployment it already exists and the data team keeps it current. Setup steps use
  the same Steps / Enter this / Check it worked shape, but they are not numbered exercises and do not appear
  in "What you will be able to do", the scenario, or the exercise count.
- The scenario, header strip, and core exercises speak only about the lakehouse and its tables ("the HR lakehouse,
  refreshed nightly from the HR system"), never about CSVs, an export, file uploads, or the notebook. Exercise 1 is
  creating the data agent over the lakehouse.
- Data quirks are framed as **what a production lakehouse really looks like** (history rows, mixed codes, mixed units,
  late-arriving records), not as quirks of a file.
- Agent instructions, data source instructions, and descriptions describe the lakehouse tables, never "the export" or
  files. Use the as-of date as "data current through <date>".
- The `Synthetic` attribution sits once in Lab Setup, where the files are uploaded.


**The hand-waving test.** Read every step and ask: *could someone do this without knowing anything I haven't told
them?* "Add instructions for status codes" fails. "Paste this into Data source instructions: `Status codes vary in
spelling...`" passes. A step that tells the reader to *decide, consider, ensure, review, map, assess, determine,
think about,* or *make sure* is not a step: rewrite it as an action.

## Participant-only published content (binding)

Every published HTML handout and companion file must stand alone for a participant who has never seen the authoring
chat. This rule takes precedence over any older output-section or workflow instruction.

- Exclude meta-narrative and authoring rationale: how the material was drafted, validated, or packaged; validation
  results; generator names, seeds, or spec files.
- Exclude chat echo: "as you requested", "updated/rebuilt", feedback acknowledgments, optional-extension offers.
- Exclude facilitator, speaker, and run-room notes: no facilitator notes, run times for the room, "While It Runs",
  "If it stalls", wait-time filler, troubleshooting advice, ground rules, pairings, or what to say to the room.
  Leave them out entirely; never hide them in comments, collapsed panels, appendices, notes, or workbook tabs.
- Preserve scenario context, product click paths, copy-ready text, expected outputs, evidence checks, and factual
  prerequisites, permissions, availability, and references.
- Synthetic material reads like an original export: one concise `Synthetic` label in the handout near the first use
  of the content pack and one in each `.docx`/`.xlsx` header or properties; never inside CSV rows (CSVs stay a clean
  flat export) and never in copied prompts.

## House style (binding)

- **US English.** Sans-serif fonts only (Aptos, then Segoe UI) everywhere, including any `.docx` or `.xlsx`.
- Never write the phrase "failure mode". No candor or editorial commentary ("honestly", "to be fair", "the catch
  is"). Reference lists are headed **References:**, never "Learn more:".
- No em-dashes or en-dashes in any artifact; use a colon, comma, period, spaced hyphen, or parentheses.
- **Minimal file count:** one HTML handout, one notebook, consolidated data files (one CSV per table, 3-5 tables,
  plus at most one optional `.xlsx` with a tab per table). A ZIP is only a convenience copy of the same files.
- Test prompts are realistic, concise human questions as the persona would type them. They never restate setup,
  table names, file names, or the instructions.
- Data agent instructions, data source instructions, and test prompts say what to do: the task, the tables and
  filters, the output, and how to handle out-of-scope questions or missing data. Write a needed limit as the
  action ("Return aggregated results only"); keep a negative only for a hard privacy or security line that no
  affirmative form can carry.
- **No noise (binding).** Include only what the participant must have, do, paste, or see. Leave out statements about
  what is not required ("no key or token is required"), background on how the product works, limits the lab never
  reaches (five-source limit, 25-row cap), run-identity and notification trivia, alternative approaches, and
  sentences that explain why a step matters. If a sentence can be deleted without the participant missing an action,
  a value, or an expected result, delete it. Keep each Check it worked to what appears on screen.
- **No redundancy (binding).** Say each thing once. A Check it worked that restates a step or points back to What good
  looks like is deleted; a Goal that restates the exercise title is deleted (titles carry the goal); a prompt already
  in a copy block is referred to, not repeated ("ask the headcount question again"); a step that confirms what Check
  it worked already shows is cut. No recap sections ("What you built"); References appear once, at the end; the
  pre-flight checklist holds only checks that are not already a row in the Prerequisites table.
- **Data handling.** Never frame data handling as content leaving the tenant. Do not add data-handling or service
  boundary statements by default; include one plain sentence only when the user asks or the scenario requires it.
- Exercise titles lead with the business task, product in parentheses: "Answer Backlog Questions in Plain English
  (Fabric Data Agent)".

## When NOT to Use

- Copilot Cowork exercises or tracks: use `copilot-cowork-exercise-builder`.
- Copilot Studio exercises: use `copilot-studio-exercise-builder`.
- Demos for Copilot Chat, Researcher, Analyst, Agent Builder, or Copilot in Word/Excel/PowerPoint/Outlook/Teams: use
  `copilot-exercise-builder`.
- Styling, rebranding, or repairing an existing handout and nothing else: use `copilot-exercise-html-formatter`.
- Actually creating a workspace, lakehouse, notebook, schedule, or data agent in a live tenant: this skill produces
  the lab, not the items.
- Power BI report authoring, Fabric capacity sizing, licensing quotes, or pricing.

## Build sequence (why this order)

Prerequisites → **Lab Setup** (S1 workspace and lakehouse → S2 upload files → S3 import, attach, run the notebook →
S4 see where a schedule is configured, without creating one → S5 verify tables in the SQL analytics endpoint) → **Exercises**: create the data agent over the
lakehouse and select tables → **baseline question** → data agent instructions and data source instructions →
**same question again** → example queries → in-scope and out-of-scope tests with the generated SQL inspected →
publish and share → optional consumption.

Two positions matter most:

1. **Setup lands data as tables through a notebook, not "Load to Tables".** The agent answers from lakehouse tables,
   not Files. A notebook with explicit schemas gives typed columns in one run. This is setup, not the lesson (see Lab setup vs. the story).
2. **Ask before instructing.** The participant asks the before/after prompt with no instructions, records the answer
   and its SQL, then adds instructions and asks again. Seeing the number change is the lesson; both values are
   computed from the data by code.

Optional advanced exercises (only when requested or the timebox allows): add a second source (warehouse or Power BI
semantic model: semantic models take no example queries and need only Read permission), diagnostics, Git integration
and deployment pipelines.

## Hard Grounding Rule

Fabric changes fast. **Never assert a product behavior, limit, setting name, or UI location from memory.** At build
time, re-fetch the pages in [references/fabric-grounding.md](references/fabric-grounding.md) with `web_fetch`
(minimum: create-data-agent, tenant settings, concepts, job scheduler) and reconcile: capacity and trial support,
tenant setting names, the five-source limit, the 15,000-character instruction limit, example-query validation, and
the scheduling path. A click path you cannot verify is written as a step and marked **[Verify]**, never invented.
Update the baseline file in your build notes when Learn has moved; report the change in chat.

## Workflow

### 1. Intake (never block)

Gather, defaulting anything missing without asking: company (default: a clearly fictional company in the stated
industry), industry (default: manufacturing maintenance), persona (default: the role closest to the data, such as a
reliability or operations manager), business scenario, number of exercises (default: the core sequence 0-11 plus
the optional consumption exercise), brand color (default: the formatter's neutral palette). Ask at most one
question, and only when the scenario is genuinely ambiguous. If the user references a customer, meeting, or file,
look it up (`m365_search-SearchM365`, `sharepoint_onedrive-ReadFileContent`) rather than asking. Use `web_search`
for the company's public operating vocabulary. Never invent a real company's figures or executive names.

### 2. Verify the product facts

Apply the Hard Grounding Rule. Collect the full URLs fetched; they feed the **References:** lists.

### 3. Design the data scenario

Write a spec JSON in `working/<slug>/spec.json` following [scripts/sample_spec.json](scripts/sample_spec.json) and
the generator kinds documented in `scripts/generate_synthetic_data.py`:
- 3-5 tables with **descriptive table and column names** (the agent relies on them), consistent keys across tables
  (`fk` and `lookup` kinds), and realistic volumes (tens to a few hundred rows per table).
- 3-5 traps from the trap menu in [references/lab-patterns.md](references/lab-patterns.md): inconsistent unit or
  status codes, nulls, superseded or late-arriving records, business-term ambiguity. Opaque: plausible codes a real
  export would carry; never on-the-nose names.
- `answers`: SQL for every expected value, including both halves of the before/after pair.
- `example_queries`: 3-6 question + T-SQL pairs encoding the business definitions.

### 4. Generate data and compute expected answers (script, deterministic)

```bash
python scripts/generate_synthetic_data.py --spec working/<slug>/spec.json --check
python scripts/generate_synthetic_data.py --spec working/<slug>/spec.json \
  --out working/<slug>/package/content-pack --meta working/<slug>/authoring [--xlsx <Company>_<Domain>_Export.xlsx]
```
`--check` must exit 0: no orphan keys, every answer and example query executes, and every example query's tables and
columns exist. Every "What good looks like" value comes from `authoring/expected_answers.json`. Never estimate a
number. If a value looks implausible, change the spec and regenerate; never hand-edit a CSV.

### 5. Generate the ingestion notebook (script, deterministic)

```bash
python scripts/build_ingest_notebook.py --manifest working/<slug>/authoring/manifest.json \
  --out working/<slug>/package/content-pack/<Company>_Ingest.ipynb --title "<Business title>"
```
The notebook has a tagged parameters cell (`source_folder`, `validate_row_counts`), explicit typed schemas, Delta
overwrite with `saveAsTable`, a row-count check against the generated counts, and a JSON summary via
`mssparkutils.notebook.exit`. The upload folder in the guide must equal `source_folder`.

### 6. Author the lab content

Follow the step shape and click paths in [references/lab-patterns.md](references/lab-patterns.md) and the
Prerequisites template and coverage list in [references/build-checklists.md](references/build-checklists.md).
Write every pasted value literally: agent instructions (show the character count to yourself; stay well under
15,000), data source instructions, example queries, test prompts, publish description, the SQL analytics endpoint
row-count query, and the names the participant enters. Show notebook parameter values only if the participant must
change them. Any non-tabular companion (for example a one-page data
dictionary, only if the scenario needs it) is `.docx` in Aptos, never `.txt` or `.md`.

### 7. Render through the formatter (explicit handoff)

Invoke the **`copilot-exercise-html-formatter`** skill and hand it the finished content plus the brand color. Require:
brand color resolution, executive handout layout, collapsible left nav rail, WCAG AA contrast, ASCII-safe
punctuation, sans-serif fonts (Aptos, Segoe UI), and **copy-to-clipboard blocks for every test prompt, the agent
instructions, the data source instructions, each SQL example query, the row-count query, and each name the participant
enters**. Do not write CSS or HTML styling in this skill; never hand-roll the handout.

### 8. Package and deliver

Final layout (build in `working/<slug>/package/`, then save to `output/<slug>/`; if a direct write to `output/`
fails, publish the folder with `CopyArtifact(surface="output", ...)` and verify the copied count):
```
output/<slug>/
  <Company>-Fabric-Data-Agent-Lab.html
  content-pack/<table>.csv ... [<one workbook>.xlsx] <Company>_Ingest.ipynb
  <slug>-content-pack.zip        (optional convenience copy of content-pack/)
```
`authoring/` (spec, manifest, expected answers) stays in `working/` and never ships. Confirm with a directory listing
before reporting ready.

### 9. Sweep the rendered handout and files

grep the HTML (including the literal text behind every copy button) and every companion for: `facilitat`, `the room`,
`If it stalls`, `While it runs`, `ground rules`, `pair up`, `run time`, `failure mode`, `Learn more`, `we `, `I `,
`as requested`, `honestly`, `consider`, `ensure`, `make sure`, `decide`, `as needed`, em-dashes and en-dashes, and
serif font names. Each hit in participant content is a defect: fix it. Confirm every test prompt has What good looks like with
a computed value, the Prerequisites section and pre-flight checklist are present, and **References:** appears once at
the end. Then read the handout top to bottom for anything said twice (a Goal that repeats the title, a Check it worked
that repeats a step or What good looks like, a repeated prompt, a recap) and delete the second occurrence.

### 10. Summarize in chat

Company, persona, scenario; the traps planted and which instruction line or example handles each; the before/after
values; any **[Verify]** items left; any Learn change since the baseline; file list with paths.

## Things participants must not miss

Build these into steps or Check it worked, not into explanatory paragraphs:
- A step to expand the **steps** dropdown and read the generated SQL.
- A **Clear chat** step before each independent test.
- Example queries must show as valid; an invalid one is fixed against the schema.
- The Share step gives colleagues access to the lakehouse as well as the agent.

## Output format (handout section order)

1. **Header strip** - exercise count, products used, and the access the reader must already have. No run-time or
   duration estimates.
2. **The scenario** - two or three sentences in the persona's business terms; what the finished agent answers.
3. **What you will be able to do** - 5-8 capability statements.
4. **Prerequisites** and **Pre-flight checklist** - clearly called out, from the template.
5. **Lab Setup** (S1-S5) - stands up the lakehouse that mirrors production; one `Synthetic` attribution where the
   files are uploaded. Not counted as exercises.
6. **Exercises** in build order starting with creating the data agent, each with Steps, Enter this when there is
   text to paste, and Check it worked only when it adds an on-screen result the steps do not already state.
7. **Test prompts** - each with **What good looks like** (computed value, filters the SQL should show, or expected
   out-of-scope behavior).
8. **Optional advanced exercises** - only those in scope.
9. **References:** - the only reference list, each a live link with the URL visible.

## Pre-delivery checklist

1. Product facts re-verified on Learn today; unverifiable paths carry [Verify].
2. Prerequisites section and pre-flight checklist present, participant-facing, accurate, and not duplicating each
   other; References: appears once, at the end.
3. `generate_synthetic_data.py --check` exit 0; every expected value traces to `expected_answers.json`.
4. Notebook generated from the same manifest; `source_folder` equals the upload folder named in the guide.
5. Before/after pair shows two different computed values and names the SQL change to look for.
6. Every example query validated against the schema; 3-6 of them; none for a semantic model source.
7. 6-10 test prompts, at least two out of scope (one causal "why").
8. Every pasted value is in a copy block; no UI navigation inside a copy block.
9. The handout came from `copilot-exercise-html-formatter`, saved as a file.
10. File count minimal: one HTML, one notebook, one CSV per table, at most one workbook; no `.txt`/`.md` data.
11. Sweep clean: no facilitator content, run-room timing, editorial commentary, "failure mode", "Learn more", dashes,
    or serif fonts; US English.
12. No noise: no statements of what is not required, product background, unreached limits, run-identity or
    notification trivia, alternative approaches, or why-this-matters sentences; nothing framed as data leaving the
    tenant.
13. Data load is confined to Lab Setup: the scenario, header, core exercises, instructions, and publish description
    mention the lakehouse and its tables, never CSVs, an export, uploads, or the notebook.

## Guardrails

- Ground every product claim in a fetched Microsoft Learn page; no memory-sourced limits, settings, or UI paths.
- Never fabricate real customer facts, figures, or names; use a fictional company or a bracketed placeholder such
  as `[Customer to confirm]`.
- Every expected value is computed by the generator from the synthetic data; never estimated, rounded by eye, or
  typed from memory.
- Never execute the participant notebook against a real tenant, and never create, modify, schedule, or publish live
  Fabric items. This skill produces lab content only.
- Never include secrets, keys, connection strings, or real tenant, workspace, or capacity IDs in any file.
- Keep `authoring/` files out of the participant package.
- Respect copyright: write original scenario text; never copy third-party lab content.
- Never modify built-in system skills or the other exercise skills.

## Example requests

- "Create a Fabric data agent exercise for a reliability manager at a chemicals company."
- "Build a Fabric Data Agent workshop for Contoso Retail's merchandising team, brand color #0F6CBD."
- "Data agent hands-on for a regional utility's outage analysts, with a warehouse as a second source."
- "Build a Fabric data agent lab where the agent answers maintenance backlog questions."
