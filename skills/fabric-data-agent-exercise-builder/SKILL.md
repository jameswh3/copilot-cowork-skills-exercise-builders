---
name: fabric-data-agent-exercise-builder
description: |
  Builds company- and persona-specific hands-on labs that take participants from an empty Fabric workspace to a published Microsoft Fabric data agent: prerequisites, click-path steps, copy-ready agent and data source instructions, validated example SQL, test prompts with computed answers, synthetic CSV data, and a scheduled PySpark ingestion notebook. Use when the user asks to "create a Fabric data agent exercise", "build a Fabric Data Agent workshop", "build a Fabric data agent lab", or "data agent hands-on for [company]". Do NOT use for Copilot Cowork exercises (copilot-cowork-exercise-builder), Copilot Studio agents (copilot-studio-exercise-builder), other Copilot surfaces (copilot-exercise-builder), HTML formatting alone (copilot-exercise-html-formatter), or provisioning real Fabric items.
metadata:
  category: productivity
  icon: DatabaseSearch
---

# Fabric Data Agent Exercise Builder

Build a **hands-on lab** that takes a participant from an empty Fabric workspace to a working, tested, published
Fabric data agent, grounded in one company, one persona, and one business scenario. The skill also produces
everything the participant needs to succeed: realistic synthetic data, a scheduled ingestion notebook, and every
piece of text they paste.

The unit of work is **one lab producing one data agent**. Exercises are its dependency-ordered parts, never
standalone labs. Audience: customer makers and analysts following along at a keyboard in their own tenant.

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
- **Service boundary, stated plainly.** Never frame data handling as content leaving the tenant. State the boundary:
  the agent queries under the participant's own Entra ID identity and permissions; Fabric uses a Microsoft-managed
  Azure OpenAI service; when the agent is consumed from Microsoft 365 Copilot or Copilot Studio, that service
  processes the returned responses under its own terms.
- Exercise titles lead with the business task, product in parentheses: "Answer Backlog Questions in Plain English
  (Fabric Data Agent)".

## When NOT to Use

- Copilot Cowork exercises or tracks: use `copilot-cowork-exercise-builder`.
- Copilot Studio agent builds or walkthroughs: use `copilot-studio-exercise-builder`.
- Demos for Copilot Chat, Researcher, Analyst, Agent Builder, or Copilot in Word/Excel/PowerPoint/Outlook/Teams: use
  `copilot-exercise-builder`.
- Styling, rebranding, or repairing an existing handout and nothing else: use `copilot-exercise-html-formatter`.
- Actually creating a workspace, lakehouse, notebook, schedule, or data agent in a live tenant: this skill produces
  the lab, not the items.
- Power BI report authoring, Fabric capacity sizing, licensing quotes, or pricing.

## Build sequence (why this order)

Prerequisites → workspace → lakehouse → upload files → import, attach, run the notebook → schedule it → verify
tables in the SQL analytics endpoint → create the data agent → add the lakehouse and select tables → **baseline
question** → data agent instructions and data source instructions → **same question again** → example queries →
in-scope and out-of-scope tests with the generated SQL inspected → publish → share → optional consumption.

Two positions matter most:

1. **Data lands as tables through a notebook, not "Load to Tables".** The agent answers from lakehouse tables, not
   Files. A notebook with explicit schemas gives typed columns, repeatable overwrite loads, and a run that can be
   scheduled, which is how the data stays current after the lab.
2. **Ask before instructing.** The participant asks the before/after prompt with no instructions, records the answer
   and its SQL, then adds instructions and asks again. Seeing the number change is the lesson; both values are
   computed from the data by code.

Optional advanced exercises (only when requested or the timebox allows): add a second source (warehouse or Power BI
semantic model: semantic models take no example queries and need only Read permission), Refresh the data source after
the scheduled job runs, diagnostics, Git integration and deployment pipelines.

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
row-count query, and the notebook parameter values. Any non-tabular companion (for example a one-page data
dictionary, only if the scenario needs it) is `.docx` in Aptos, never `.txt` or `.md`.

### 7. Render through the formatter (explicit handoff)

Invoke the **`copilot-exercise-html-formatter`** skill and hand it the finished content plus the brand color. Require:
brand color resolution, executive handout layout, collapsible left nav rail, WCAG AA contrast, ASCII-safe
punctuation, sans-serif fonts (Aptos, Segoe UI), and **copy-to-clipboard blocks for every test prompt, the agent
instructions, the data source instructions, each SQL example query, the row-count query, and the notebook parameter
code**. Do not write CSS or HTML styling in this skill; never hand-roll the handout.

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
serif font names. Each hit in participant content is a defect: fix it. Confirm every exercise has Check it worked,
every test prompt has What good looks like with a computed value, and the Prerequisites section and pre-flight
checklist are present with **References:**.

### 10. Summarize in chat

Company, persona, scenario; the traps planted and which instruction line or example handles each; the before/after
values; any **[Verify]** items left; any Learn change since the baseline; file list with paths.

## Things participants must not miss

Call these out in the guide, in one or two plain sentences each at the point of use:
- The agent answers from **tables**, not files; that is why the notebook runs first.
- **Descriptive names** in tables and columns improve the SQL the agent writes.
- **Example queries are used only when valid** and matching the selected tables' schema; an invalid one is ignored.
- Expand the **steps** dropdown to read the generated SQL; that is how to confirm the answer applied the definitions.
- **Clear chat** before an independent test; earlier turns shape later answers and responses are capped at 25 rows.
- **"Why" questions are out of scope**: the agent retrieves and aggregates; it does not do causal inference, advanced
  analytics, or machine learning. Its queries are read-only.
- **Publish** creates a published version to share and keeps a draft to keep improving; the description tells
  colleagues and other agents when to use it. Recipients also need access to the lakehouse.
- Scheduled notebook runs use the identity of whoever created or last updated the schedule.

## Output format (handout section order)

1. **Header strip** - exercise count, products used, and the access the reader must already have. No run-time or
   duration estimates.
2. **The scenario** - two or three sentences in the persona's business terms; what the finished agent answers.
3. **What you will be able to do** - 5-8 capability statements.
4. **Prerequisites**, **Pre-flight checklist**, **References:** - clearly called out, from the template.
5. **Exercises** in build order, each with Goal, Steps, Enter this, Check it worked; one `Synthetic` attribution
   near the first use of the content pack.
6. **Test prompts** - each with **What good looks like** (computed value, filters the SQL should show, or expected
   out-of-scope behavior).
7. **What you built** - checklist of things the participant observed.
8. **Optional advanced exercises** - only those in scope.
9. **References:** - full list, each a live link with the URL visible.

## Pre-delivery checklist

1. Product facts re-verified on Learn today; unverifiable paths carry [Verify].
2. Prerequisites section, pre-flight checklist, and References: present, participant-facing, and accurate.
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
12. Service boundary stated plainly; nothing framed as data leaving the tenant.

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
- "Build a Fabric data agent lab where the notebook runs nightly and the agent answers backlog questions."
