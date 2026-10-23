---
name: copilot-exercise-builder
description: |
  Create executive-ready Microsoft Copilot demo exercises, workshop scenarios, and prompt sequences for customer enablement sessions. Use when the user asks to "create a Copilot demo", "build a Copilot workshop", "make a Researcher exercise", "build an Agent Builder demo", or "put together a full suite of Copilot exercises" for Copilot Chat, Researcher, Analyst, Notebook, Agent Builder, Copilot in Outlook, Teams, Excel, Word, or PowerPoint, or Copilot on Mobile. Do NOT use for Copilot Cowork exercises (use copilot-cowork-exercise-builder) or for HTML handout formatting alone (use copilot-exercise-html-formatter); do NOT use to actually perform the work a scenario depicts (sending real email, real meeting prep, building real decks) - use the dedicated M365 skills instead; do NOT use to modify built-in system skills.
metadata:
  category: productivity
  icon: SlideText
---

# Copilot Exercise Builder

Use this skill to create customer-facing Copilot demo scenarios. Produce one scenario per request unless the user explicitly requests multiple scenarios and provides both the exact number and the specific scenario types. If either is missing, ask one clarifying question. You may also offer one optional `Writing Assistant` companion exercise after the primary output; only generate it if the user accepts.

## Inline sources at point of use (binding default)

This rule overrides any older requirement for a published source pack, content matrix, file-to-exercise mapping table, inventory, blueprint, or separate source section. Apply it to new content and revisions, in HTML and plain text alike.

- Put exact source filenames or verified links immediately alongside the exercise that requires them, in a concise `Setup`, `Open`, or `Upload` sentence or short bullets. List only the files needed at that point. Use one action verb per instruction: open, upload, or reference; add a short business purpose only when useful. Replace legacy participant-facing `Drop-in Content Pack` tables and published file blueprints with `Inline Sources` within the requiring exercise, or merge them into its existing setup sentence. Do not retain a separate pack heading, add another matrix, or duplicate the setup list. Include a short business purpose for each source without describing its internal anatomy.
- Do not publish a centralized source pack/content matrix, mapping table, inventory section, source blueprint, or navigation link that sends participants elsewhere to discover required inputs. Move legacy entries into the relevant exercise and remove the obsolete section and orphaned nav link, rather than hiding them. This does not prohibit business-result tables or actual business data in source files.
- Reuse the same saved file across exercises. Store it once in its primary exercise folder and reference that same exact path at each point of use; do not generate duplicate copies. Use an exact filename/path when no verified URL is available. Never invent a download, tenant, or sharing link; verify any link against the actual saved artifact or confirmed source.
- Keep any file manifest, source-to-exercise mapping, or detailed blueprint internal for authoring and validation only, never in participant artifacts (including hidden panels, comments, appendices, or notes). Generate only the minimal assets needed for the bounded business task.
- Put ONE concise `Synthetic` provenance attribution near the first exercise that uses the synthetic files, plus one `Synthetic` metadata/header label per file. Do not repeat the handout attribution for later exercises reusing those files, or put provenance in copied prompts. Retain truthful source, author/participants and date identifiers.
- Keep setup business-only: no row/tab anatomy, internal field inventories, or prompt meta-narrative. Preserve bounded evidence and coverage, supported verified analytical paths, draft-only/approval constraints, factual access prerequisites, and minimal assets. Before delivery, verify every required source is named at its point of use and every link resolves to the intended saved source. Formatting changes must preserve the existing nav-width and semantic reading-anchor contracts.
- Audit placement exercise by exercise, using an internal manifest only if useful: reconcile every required input against its inline setup and saved artifact, check exact spelling and any verified link target, and confirm reused sources keep one saved path. Remove conflicting old published-table/file-mapping mandates and obsolete source-section/nav entries rather than relying only on this override. Do not repeat prompt metadata or provenance. For a source-placement-only skill update, preserve the prior nav-width and semantic reading-anchor requirements byte-for-byte; do not edit a handout to demonstrate the change.

## Business-only wording and bounded evidence (binding)

These rules govern authoring and formatting alike and override older examples or section names that conflict. They apply to every participant-facing prompt, instruction, narrative, expected output, and companion source.

1. **Business-only copy blocks.** Write only the work request the persona would actually give: the decision, selected inputs, substantive business constraints, and requested output. Never put demo, simulation, illustrative, teaching, or authoring labels in prompts. Exclude "this exercise", product comparisons, test controls, generation commentary, and explanations such as "This is illustrative IT ...". Keep draft-only instructions, unknown-value handling, citation/evidence requirements, uncertainty, and approval constraints: these protect the business work and are not meta-narrative.
2. **Provenance once, in the right place.** Put ONE concise `Synthetic` label in each companion source's metadata/header and ONE concise handout attribution near the first exercise using the synthetic files. Retain source/author/participants/date identifiers. Do not repeat the label in business prose, prompt directives, table rows, or expected outputs; exclude all other demo/simulation/illustrative/teaching/authoring narrative. Do not remove truthful provenance or factual product availability, permissions, licensing, or access prerequisites. Product names and necessary setup/click paths remain; explanatory product comparisons do not.
3. **Bound the actual evidence workload.** Use a short, explicitly selected file set, authored small enough for the timebox, and a bounded business question or decision-gate scope. Name the files, business scope and timeframe in the work request; keep internal row/table selection out of participant-facing content. For live M365 retrieval, bound topics, people/meetings, dates and returned evidence; report what was actually found/read and what remains unknown. Chat, Notebook, Agent Builder and search-based M365 retrieval are not exhaustive per-account/per-record audit engines. Never promise search-wide completeness, full-population validation, or an all-clear from retrieved snippets or a sample.
4. **Population is not analyzed records.** A business rollout may cover hundreds of accounts, devices, employees, or sites without the run analyzing each one. Keep that population as business context; state the much smaller source set, summary/gate workload, and coverage actually analyzed separately. Prefer supplied aggregates to hundreds of enumerated items. Do not turn a rollout count such as 600 into 600 individual checks. Choose workload sizes for the timebox and actual source granularity, not an unsupported universal numeric product limit.
5. **Use the right analytical path.** Quantitative scans and computations belong in Analyst over uploaded data or in Excel for appropriate formulas, tables and light analysis. In Cowork, use an explicitly available computational tool or supported model query for that leg before synthesizing or creating deliverables. Keep inputs small enough for the timebox and verify the computed output. If exact comprehensive validation is required, use a genuinely exhaustive tool-supported path with a defined dataset, full row/page coverage, explicit rules and verification; when unavailable, narrow the task or state the gap instead of promising completeness. No fabricated all-clear, totals, percentages, or probabilities from a sample.
6. **Coverage belongs in the business result.** Require the sources/rows/gates actually considered, missing or stale evidence, contradictions, and unresolved questions. Distinguish source-reported aggregates from independently computed results and inferences. A sampled finding applies only to its evidence, not the whole population; missing evidence is unknown, not passed. Keep any message, approval or recommendation a draft where appropriate.
7. **Audit before delivery.** Read the literal text copied by EVERY copy button, not just the visible wrapper, plus all visible/hidden narrative, source metadata, document notes and workbook tabs. Remove excluded wording rather than hiding it. Check actual source granularity, files/rows/gates touched, computational path and timebox; reconcile every prompt and claimed result with the companion files. Preserve participant setup, truthful provenance and business evidence guards. Delete orphaned navigation links. Fix conflicts before declaring ready; keep audit/generation commentary in chat only.

## Business source language, not file anatomy (binding)

This overriding rule applies to all participant-facing setup and selected-source content, steps, inline source instructions, copied prompts, and expected outputs. Where older wording asks for source selection or summary/gate scope, express that scope in business terms, not workbook anatomy.

- Name the workbook or file and the business question, date period, service, vendor, or metric relevant to the decision. Do not ask participants to find named tabs/sheets, count sheets, locate row/column numbers or A1 ranges, copy exact formulas, select ranges, exclude metadata rows, or map sheets. Do not publish internal table/field inventories as participant setup requirements.
- Have participants open or upload the file, then ask naturally for the result. Ask Copilot to identify the relevant table and fields, check stored units and number formats, preserve source values, and provide a traceable result. Do not claim that opening/uploading a file guarantees the entire file is read or exhaustive coverage. Missing, inaccessible, ambiguous, or unread evidence must be reported honestly, not inferred as complete or passed.
- Bound workloads by authoring genuinely small files and specifying a business scope and date period, not by teaching participants to select a small set of rows or hunt for sheets. Keep source-reported aggregates distinct from computed values and inference; retain evidence checks, missing-data handling and the appropriate verified analytical path. Do not move numerical work into unsupported Chat arithmetic.
- Internal authoring validation remains required: inspect source structure, tables, fields, rows, formulas, units, metadata, and expected calculations to ensure the files support the request. Keep that anatomy internal. Row/cell citations or other precise source anchors may appear in generated results as evidence; they are not a participant setup burden or an expected-output instruction to navigate manually.
- A genuine product prerequisite may be stated plainly: "Use a formatted table if your Excel experience requires one." Never attach hardcoded ranges or sheet-hunting directions to it. Preserve truthful access prerequisites and product navigation, without confusing them with file-internal selection.
- Before delivery, sweep all setup, steps, inline source instructions, prompt text (including literal clipboard content), and expected outputs for file-anatomy micromanagement. Rewrite it as file name plus business scope; keep the units, evidence and computation guards. Do not silently alter business figures or invent inaccessible evidence.

Example business prompt: "Using the workbook, chart weekly availability by service for September 11 through October 16; flag Workplace Access below 99.90%; check stored units; preserve source values and cite the evidence."

## Participant-only published content (binding)

Every published HTML handout and companion file must stand alone for a participant who has never seen the authoring chat. This rule takes precedence over any older output-section, workflow, or companion-reference instruction requiring delivery notes or troubleshooting blocks.

- Exclude meta-narrative and authoring rationale: no explanation of how the material was drafted, revised, selected, validated, or packaged; no internal process commentary or validation results.
- Exclude chat-history extensions: no "as you requested", "updated/rebuilt", feedback acknowledgments, discussion of inferred scope or session counts, or future optional-extension offers copied from assistant chat. Keep any required planning statements and offers in chat only, never in an artifact.
- Exclude facilitator, speaker, delivery-team, and run-room notes, including "While It Runs", "If It Stalls", wait-time filler, troubleshooting advice, and what someone should say or show to the room. Remove these sections rather than hiding them in comments, collapsed panels, appendices, document notes, or workbook tabs.
- Preserve genuine participant scenario context, product setup and click paths, copy-ready prompts, expected outputs, evidence checks, and essential factual availability, access, permissions, and reference information. Business context and product constraints are not authoring commentary. Do not remove participant instructions merely because they address the reader directly.
- Synthetic material must read like original source material: use the single `Synthetic` source-metadata label and first-use handout attribution specified above, plus appropriate source, participants or author, and date identifiers. Follow with business content only, without repeated labeling, author conversation, or exercise-construction commentary.
- Before publishing or revising, inspect all handout sections and every companion file for these excluded categories, including hidden text and notes. Delete excluded material and any orphaned navigation links; confirm required participant steps, prompts, source evidence, and factual prerequisites remain intact.

## Companion skills (delegate, do not duplicate)

- **HTML handout formatting** is owned by `copilot-exercise-html-formatter`: brand color resolution, layout, nav rail, copy-to-clipboard prompt blocks, accessibility contrast, punctuation and encoding rules, and the pre-delivery sweep. Hand finished exercise content to that skill to render the handout. Do not re-derive those rules here.
- **Copilot Cowork exercises** are owned by `copilot-cowork-exercise-builder`. If the user asks for a Cowork exercise, a Cowork track, or persona-based Cowork content, route there. Do not author Cowork scenarios in this skill.
- **Copilot Studio Agents** exercises are out of scope. If the user asks for one, say plainly that Copilot Studio exercise authoring is not currently supported and offer `Agent Builder` instead.
- **Custom instructions belong to `Copilot Chat` only.** They are a Copilot Chat construct set under Settings, Customize, Custom instructions. Do not carry the custom-instructions setup step, the Settings path, or the before-and-after comparison into any other scenario type, and never into a Cowork exercise.

## Priority categories

1. **Executive content quality:** Every demo must be decision-focused, grounded in real business moments, and free of hype.
2. **Scenario-specific boundaries:** Stay within each scenario's defined scope and constraints.
3. **Output format and branding:** Apply consistent styling and brand alignment through `copilot-exercise-html-formatter`. The default HTML output is chosen because it best supports executive readability and portability; it does not conflict with content quality.

When conflicts arise, apply the following resolution rules in order:

1. **Executive quality vs. scenario boundary:** If a scenario boundary suggests generic setup text but executive-ready context requires specificity, choose specificity (for example: name the initiative, deadline, or business pressure instead of a placeholder).
2. **Executive quality vs. output format:** If output format rules conflict with a complete executive prompt sequence, keep the full sequence and apply formatting within it.
3. **Branding vs. readability:** If branding reduces readability or contrast, prioritize accessibility and adjust accent usage.
4. **Synthetic data scope vs. decision value:** If synthetic data scope conflicts with decision value, provide a decision-focused summary format instead of a large file.
5. **Participant practice vs. time:** If participant practice may exceed the available time, prioritize the first 3-4 prompts for clarity over full prompt count.
6. **Multiple scenario ordering** (applies only when multiple scenarios are explicitly requested):
   - Place agent scenarios near the end of the sequence regardless of request order.
   - If a `Copilot Cowork` exercise is part of the same session, it belongs last as the capstone integration story; build it through `copilot-cowork-exercise-builder` and reference it in the sequence.
   - Connect scenarios with handoff cues.

Detailed rules later in this file explain each category, but they do not change the priority order above.

## Supported scenario types

- `Copilot Chat`
- `Researcher`
- `Analyst`
- `Notebook`
- `Agent Builder`
- `Copilot in Outlook`
- `Copilot in Teams`
- `Copilot on Mobile (Voice Mode)`
- `Copilot in Excel`
- `Copilot in Word`
- `Copilot in PowerPoint`

`Writing Assistant` is not a primary scenario type in this list. It may be offered as an optional companion exercise after requested scenario output, or generated as standalone only when explicitly requested.

`Copilot Cowork` is not built here. Route it to `copilot-cowork-exercise-builder`.

If the request does not specifically name one of the supported scenario types from the list provided (e.g., "Create a Copilot Chat demo"), ask one brief clarifying question before proceeding. Exception: if the user explicitly requests standalone `Writing Assistant`, proceed without requiring scenario-type clarification.

## When NOT to Use

This skill builds demo and workshop content (exercises, prompt sequences, synthetic sample files). It does not perform the real work a scenario depicts. Route elsewhere when:

- The user wants a `Copilot Cowork` exercise, a Cowork track, or persona-based Cowork content: use `copilot-cowork-exercise-builder` instead.
- The user only wants the HTML handout built, restyled, rebranded, or repaired: use `copilot-exercise-html-formatter` instead.
- The user wants a Copilot Studio agent exercise: not currently supported; offer `Agent Builder` instead.
- The user wants to run the task for real, not demo it: use the appropriate email, meeting, or scheduling capability instead.
- The user wants a real business document rather than a demo asset: use docx, pptx, or xlsx instead.
- The user wants to create, edit, validate, or audit a personal skill: use the host's personal-skill management capability instead.
- The user wants deep external research as the deliverable, not a Researcher exercise: use the host's research capability instead.
- The request names no Copilot surface and is not about demos or workshops: answer directly instead.

## Core operating rules

Follow the priority order defined above. Treat the detailed rules later in this file as refinements within that order, not as exceptions that can change it.

### 1. Scenario output scope

The default behavior is to produce **one scenario per request**. Only produce multiple exercises when the user explicitly states the number of scenarios or lists the requested scenario types.

- Each scenario stays within its own boundaries
- Do not blend content from different scenario types within a single scenario section
- Do not compare scenario types within a scenario section
- **Never produce exercises for scenarios that were not explicitly requested.** If the user asks for a Copilot Chat demo, produce only the Copilot Chat exercise - do not generate Researcher, Analyst, or any other scenario alongside it unless asked.
- **Optional companion exception:** After delivering the requested scenario output, you may offer one optional additional `Writing Assistant` companion exercise. Generate it only if the user explicitly accepts.
- **Standalone exception:** If the user explicitly requests standalone `Writing Assistant`, generate it as the primary output.
- **When multiple scenarios are explicitly requested:** Always place agent scenarios near the end of the sequence regardless of request order. If a `Copilot Cowork` exercise is in the requested set, it goes last as the capstone integration story and is built through `copilot-cowork-exercise-builder`. This positions the agent experiences as integration points after participants have explored Copilot across chat, apps, and workflows.

### 2. No meta-narrative

Within the exercise output, return content directly without explaining structure or design choices.

Business context (Scenario Overview, decision pressure, and the substantive decision supported by a step) remains required. Explanations about the exercise, teaching goals, product comparisons, and generation process are excluded everywhere except concise provenance and factual access prerequisites.

**In the exercise output, do not include:**
- Explanations of your approach
- Rationale for structure or design
- Meta-framing phrases like "this exercise is designed to..." or "the goal here is..."

**Note:** The non-overlap check (the named workflow step below) may be a brief planning statement in chat only. It must never enter the HTML, any companion file, or participant-facing plain-text output.

### 3. Executive prompt style

Focus first on executive-ready and decision-focused content, then ensure it is reusable and free of hype.

All prompts must:

- Sound like something an executive would naturally type
- Be conversational, concise, and decision-oriented
- Avoid prompt-engineering, tool-operation, or system-style language

Examples:

- "What actually needs my attention right now?"
- "What's changed since last quarter that matters?"
- "Where are we exposed or unclear going into this?"

**Favor tight, non-dramatic executive prose throughout the narrative, not just the prompts.** Scenario overviews, context notes, and "why this matters" lines should be short and plainly worded. Cut theatrical build-up, hype, and marketing phrasing (for example "the scarcest thing in the building," "stops being a feature and becomes a workspace," "the only experience that...," "read it as a leader, not a spectator"). State each point in one crisp clause. Executives want signal, not theater. Default to aggressively short on the first build rather than expecting to trim later.

### 4. Punctuation

Never use em-dashes or en-dashes anywhere in the output, in any artifact, including synthetic content files. Use a colon, comma, period, spaced hyphen, or parentheses instead. Apply the substitution as you write, not afterward.

The full punctuation, entity-encoding, and sweep rules live in `copilot-exercise-html-formatter`. Follow them for every artifact this skill produces.

Also: do not generate `.md` or `.txt` files as synthetic data deliverables. Documents are `.docx`, tabular data is `.xlsx` (see "Favor realistic file types" under Synthetic data and file generation).

## Required workflow

1. **Intake (scenario-bounded)**
   - Ask only for inputs the user has not already provided and that are relevant to the chosen scenario. Do not ask for all inputs every time; use what is already known and ask only for what is missing:
     - customer name or anonymized label
     - industry
     - department or function
     - target role
     - audience level
     - session context
     - timebox
     - has the participant already completed prior exercises in this session? (yes/no)
     - for `Copilot Chat` only: has the participant already configured Copilot custom instructions? (yes/no)
     - other exercises in the same session
     - output format: **Always produce HTML (styled handout) unless the user explicitly requests plain text.** Do not ask; HTML is the default.
   - Scenario minimums:
     - `Copilot Chat`, `Copilot in Outlook`, `Copilot in Teams`, `Copilot on Mobile (Voice Mode)`: ask for role, current moment, and timebox if missing.
     - `Analyst`, `Notebook`, `Copilot in Excel`, `Copilot in Word`, `Copilot in PowerPoint`: also confirm the data or source content context if missing.
     - `Agent Builder`: also confirm business trigger, knowledge sources, and action scope if missing.

2. **Non-overlap check (concise)**
   - In chat only, state in 1-2 sentences how this exercise is distinct from other exercises mentioned. Do not publish this planning statement in the exercise or its files.

3. **Capability boundary enforcement**
   - Write a "Business Outcome" section naming the business deliverable and decision it supports.
   - Example: "A focused priority list aligned to your operating responsibilities."
   - Keep capability-boundary planning internal; do not publish demonstration framing or explanatory product comparisons.

4. **Produce the exercise content**
   - Include only the sections relevant to the selected scenario.

5. **Generate synthetic files**
   - Generate every named file the exercise references, per the synthetic data rules below, before delivering.

6. **Format and deliver**
   - Hand the finished content to `copilot-exercise-html-formatter` for brand resolution and the styled HTML handout. Save the HTML as a downloadable `.html` file; do not output it as a code block in chat.
   - If output format is plain text: return as formatted text in chat.

7. **Offer optional companion exercise**
   - After delivering the requested scenario(s), offer one optional additional `Writing Assistant` companion exercise in chat only. Never add the offer to the handout or source files.
   - If the user accepts, generate the companion exercise in the same output format and with the same customer context.
   - If the user declines or does not answer, stop after the requested scenario(s).
   - If the user explicitly requested standalone `Writing Assistant`, treat that as the requested output and skip the companion-offer step.

## Required output sections

For `Copilot Chat` scenarios, prepend a `System of Work: Think, Plan, Do, Evaluate` section before the standard sections below.

1. `Scenario Overview`
2. `Business Outcome`
3. `Setup / Priming Content`
4. `Participant-Facing Instructions`
5. `Prompt Sequence` (4-5 prompts maximum; never exceed 5). One exception: `Researcher` (one Chat framing prompt plus one Researcher run). See that scenario section for the exact structure.

Context depth expectations for every exercise:

- `Scenario Overview` is **1-2 plain sentences** of scenario context, in the shape "You need to prepare X for Y, with [constraint]." Do NOT use bold mini-labels (no "The moment / Why now / Pressure / Who needs to act" structure). Capture the current moment, why it matters now, and the core decision pressure in plain prose. **OMIT "who needs to act."** The reader is the target persona, so naming an owner is redundant. Keep the "Scenario Overview" section heading itself.
- `Setup / Priming Content` should be lean: include exact required filenames or verified links inline with a concise open/upload/reference action, plus only 2-3 concrete business anchors directly relevant to the first prompt (active initiatives, named risks, specific cadence); avoid verbose background or a separate source inventory.
- Prompt-level context: Each prompt in the sequence should include a brief explanation of why that prompt matters at that point and what to expect before running it. Keep these to one short clause; do not stack multiple sentences.
- Avoid generic setup text; context should read like a real operating moment for that role and function
- Address the executive directly ("you", "your"), not in third person ("the CFO", "the executive")
- Keep all narrative tight and non-dramatic (see Executive prompt style above).

### Exercise and scenario titles: business-first, product in parentheses

Name every exercise for the business process or scenario the participant works through, and put the Microsoft product or surface in parentheses at the end. Lead with the outcome in the customer's language, not the tool.

- Correct: "Draft the Interim Business Case (Copilot in Word)", "Screen the Opportunity List (Analyst)".
- Wrong: "Copilot in Word: Draft the Interim Business Case", "Analyst: Screen the Opportunity List" (product leads, the business scenario is buried).

Apply this consistently in all three places so the whole handout reads business-first:
- the exercise section headings (`<h2>`),
- the left-hand navigation labels (a shorter form of the same name, product still in parentheses, for example "Draft Business Case (Word)"),
- the agenda and session-slides segment names.

When an exercise is foundational setup rather than a domain task (for example the Copilot Chat foundations exercise), still lead with the participant's activity (for example "Reframe How You Work") and keep the product in parentheses.

## Synthetic data and file generation

**This applies only to scenarios where synthetic content is allowed** (see the Synthetic content rules table). For scenarios marked "No" in that table (such as `Copilot Chat`, `Researcher`, `Copilot in Outlook`, `Copilot in Teams`, and `Copilot on Mobile`), do not generate synthetic files even if the scenario context references named items.

For scenarios where synthetic content is allowed: when an exercise references named files (e.g., "2026 Capital Plan finalization"), **you MUST generate the actual content.** Do not skip this step.

**Favor realistic file types.** Choose the format a real organization in that industry would actually use, not the format that is easiest to generate or parse. Finished business documents (handbooks, policies, SOPs, playbooks, briefs, memos, reports, board pre-reads) should be `.docx`. Tabular data should be `.xlsx` (a real workbook); reserve `.csv` for cases where a flat single-table export is genuinely the right artifact or the exercise specifically calls for CSV ingestion. **Never ship a `.txt` or `.md` synthetic file.** Content that is genuinely plain text in real life, such as chat or meeting transcripts, log or system excerpts, and code or config snippets, is delivered as `.docx`: preserve the verbatim plain-text body inside the document (speaker labels, timestamps, line breaks, and a monospaced block for logs or code) and add a short header line naming the source, participants, and date. Where `.pdf` would be the real-world format, still deliver `.docx` unless the user explicitly asks for PDF. If realism and tool-friendliness genuinely conflict, choose realism and note the tradeoff to the user.

For every named file, generate and provide as a downloadable artifact:

- **For spreadsheets** (.xlsx preferred): Generate a realistic workbook with a formatted header row, sample rows, and representative data that fits the scenario. Default to `.xlsx`; use `.csv` only when a flat single-table export is genuinely the right artifact or the exercise specifically calls for CSV ingestion. Save as a downloadable file.
- **For documents** (`.docx`): Generate a brief, template, or outline that participants can use during the exercise. Always `.docx`, including genuinely plain-text artifacts such as transcripts, logs, and code or config, which keep their verbatim body inside the document. Save as a downloadable file.
- **For datasets** (.xlsx preferred; .csv only if a flat single-table export genuinely fits): Provide a small, representative sample with actual values, not placeholders. Save as a downloadable file.
- **For email/Teams threads**: Generate realistic snippets with actual business language and decision-relevant information. Include in the exercise content or as a downloadable `.docx` file if extensive, with each message keeping its sender, timestamp, and body.

Every synthetic file must:
- Match the scenario's industry, terminology, and timeline
- Include realistic but representative data (not generic placeholders)
- Be immediately usable by the participant without additional preparation

**Organize files into per-exercise folders.** When a build produces sample files for multiple exercises, save each exercise's files under `output/<NN>-<exercise-slug>/` (for example `03-analyst-finance/`, `09-copilot-in-office-operations/`), where NN is the exercise number in the handout. A file shared by more than one exercise lives in its primary exercise's folder; reference it cross-folder from the others (a Notebook synthesis exercise, for instance, may pin sources from several folders). Update the handout's file references to the folder paths so each exercise points at its folder. A `Copilot Cowork` drop-in content pack follows this same numbered convention with a `-pack` suffix; that rule is owned by `copilot-cowork-exercise-builder`.

## Scenario boundaries

### `Copilot Chat`

- Focus on communication, prioritization, and attention management only
- Do not perform deep analysis, multi-source research, or dataset-based insight generation

**Required content for every Copilot Chat scenario:**

Every Copilot Chat exercise must include the following elements in this order:

1. **System of Work Prefix** - Before the Copilot Chat exercise content, include a section titled **System of Work: Think, Plan, Do, Evaluate** that frames the exercise as a repeatable delegation method, not a feature tour. Use this structure:
  - A short business framing paragraph about defining the decision, delegating the work, and checking evidence before acting; no hands-on, demo or teaching narrative.
  - Four concise phase callouts in this exact sequence:
    - **Think - Frame the Problem**
    - **Plan - Design the Delegation**
    - **Do - Execute with the Right Tool**
    - **Evaluate - Judge the Output**
  - A closing line with this exact wording: **Accountability stays with the leader at every step.**
  - Include a TPDE mapping table when it improves clarity. If included, it must be adapted to the specific customer and business unit for the current exercise.
  - Treat the maritime mapping table pattern as an example only, never as default reusable text.
  - Build customer-specific rows by mapping each TPDE phase to the customer's real operating rhythm (for example: planning cycle, execution cadence, governance gates, and review motions) and then to the business task and evidence check.
  - A one-sentence transition into the Copilot Chat exercise.

2. **Scenario Context** - Provide a specific, plainly-worded setup grounded in your industry, role, and current moment (a pending board meeting, an active regulatory process, a seasonal pressure like fire season or budget cycle). Keep it to 1-2 sentences; this context anchors all prompts and makes the scenario feel real, not generic.

3. **Quick Priority Check** - Start with: "What are my top 3 priorities for today?" Copilot will scan your live mail, calendar, and Teams to surface what needs attention. **Why this first:** You're establishing what matters in your current moment. Copilot sees your calendar and inbox but doesn't yet know your values, context, or what "high-impact" means to you. It's offering an initial read based on activity and recency, not on your actual strategic focus.

4. **Custom Instructions Builder** - Open a new chat, then run this prompt: "Do not interview me. Draft my custom instructions from the recent work signals you can retrieve for [named project or topic] during [date range], prioritizing [selected meeting series] and [selected email thread]. Infer my role, recurring decisions, audiences, and writing preferences only where those selected sources support them. Distinguish evidence from inference and leave unsupported details unknown. Return first-person instructions under 1,500 characters as one copyable block, followed by the sources actually considered and gaps for me to correct." Review the evidence and inferences, then apply the corrected text: Settings -> Customize -> Custom instructions -> paste -> Save. Do not claim a complete profile or measured time allocation from retrieval.

5. **Compare Priority Summaries** - Open a fresh chat and re-run "What are my top 3 priorities for today?" Check whether the response reflects your stated responsibilities, and review cited evidence and gaps. Do not promise that personalization guarantees better priorities or complete retrieval.

6. **Selected Work Prompts** - Use the prompts relevant to the current decision; keep the whole sequence within the prompt-count and timebox rules. These bounded versions take precedence over any earlier requirement to reproduce broad prompts verbatim:
  - "Based on [selected prior thread] with [/person] during [date range], identify likely discussion topics for our next meeting. Cite the evidence and flag assumptions."
  - "Draft a project update from [/selected email], [/selected chat] and [/selected meeting]: source-reported KPIs versus targets, decisions, risks, and open questions. State which sources were considered and leave unsupported metrics unknown."
  - "Using [selected launch status memo] and [selected pilot summary], summarize the readiness gates for the [Product] launch in November. Flag gaps and conflicting evidence; do not infer whole-launch readiness or assign an unsupported probability."
  - "Using [selected calendar entries] and [selected email thread] from [date range], suggest the main work themes. Describe coverage and uncertainty; do not claim measured percentages of total time from this selection."
  - "Review [/select email] and [/selected meeting notes] to draft a brief for the next meeting in [/series], with evidence, unresolved issues and questions for the team."

7. **Participant Practice** - Draft one custom instruction specific to your function (rate case strategy, treasury, accounting, FP&A), apply it, then re-run a selected work prompt. Check whether it reflects your responsibilities without inventing evidence.

### `Researcher`

- Focus on discovery and synthesis only
- No forecasting or official guidance
- Assume zero user-provided inputs
- Do not ask for uploads, decks, memos, KPIs, transcripts, or source lists
- At most, ask one clarifying question about leadership focus or timeframe
- **Favor the "frame in Chat, then bring Researcher into the thread" pattern.** Researcher is invoked from inside Copilot Chat, and each Researcher run is long. In an executive or any time-boxed session, do NOT stack multiple sequential Researcher prompts: several deep runs back to back will stall a live room. Instead structure the exercise in two phases:
  - **Phase 1 (Copilot Chat, fast and interactive):** frame the problem and plan the research in one or two quick Chat turns. Use Chat to pin down the decision at stake, the specific questions worth researching, and the scope/timeframe. This costs seconds, not minutes.
  - **Phase 2 (Researcher, same thread, one run):** switch Researcher on in that same chat and fire a single consolidated, well-scoped prompt that asks for the synthesized, decision-ready deliverable in one pass. One run, one output.
- **Researcher Prompt Sequence is the exception to the 4-5 prompt rule:** target one Chat framing prompt plus exactly one Researcher invocation (two prompts total). Do not author three-to-five standalone Researcher prompts. If a refine is truly needed, note it as optional rather than as a second required run.
- Label the two phases clearly (for example `Phase 1: Frame in Chat` and `Phase 2: Run Researcher once`) so the participant knows when to switch to Researcher.

### `Analyst`

- Keep analysis strictly bounded to uploaded data. Use a timebox-sized dataset and an explicit business scope/date period, naming the file and relevant service, vendor or metric rather than table/row coordinates; compute and verify requested aggregates with the analytical tool. Let Copilot identify the relevant table and fields, check units, and report actual coverage, missing values and business exclusions in the result, with precise source anchors where available. A complete scan of an uploaded table is not completeness across the wider business population.

### `Notebook`

- Focus on analysis and synthesis only

### `Agent Builder`

- Focus on declarative agent design only
- Do not imply runtime or behavioral guarantees
- Propose scenarios that are a strong fit for retrieval-grounded question answering over documents, policies, FAQs, playbooks, SOPs, and other reference content
- Prefer use cases such as knowledge lookup, policy guidance, onboarding help, process guidance, and internal reference assistance
- Do not position Agent Builder as a tool for deep analytics, trend analysis, forecasting, or reasoning over large tabular datasets
- Do not use long Excel or CSV files as the primary knowledge example unless they are framed as simple reference lookup only, not analytical reasoning
- Explicitly set expectations that the agent's RAG behavior is best for retrieval, summarization, and grounded answers from source content rather than analyst-style data exploration
- For `Agent Builder` outputs, `Writing Assistant` may be offered as the optional companion add-on described in the global workflow rules
- Treat `Writing Assistant` as an extension exercise, not a standalone scenario type, unless the user explicitly requests it as standalone
- If included, position `Writing Assistant` after the core Agent Builder exercise and connect it with a handoff cue that explains how retrieved grounded content is transformed into executive-ready writing output
- Include:
  - `Describe` text
  - `Instructions`
  - `Capability boundaries`
  - Executive-style starter prompts
  - Optional synthetic knowledge source design
  - Optional `Writing Assistant` add-on block (when requested)

### `Copilot in Outlook`

- Focus on email drafting, thread summarization, follow-up generation, and meeting scheduling
- Demo prompts should simulate real inbox scenarios: catching up on a thread, drafting a response, or preparing for a meeting
- Do not demo deep analytics or multi-source research
- Avoid generic "summarize this email" prompts; focus on decision-relevant communication and next actions

### `Copilot in Teams`

- Focus on meeting recap, action item extraction, chat summarization, and meeting preparation
- Demo prompts should reflect post-meeting or in-meeting use: "What did I miss?", "What are my action items?", "Prepare me for this call"
- Do not demo document creation or data analysis
- Keep prompts grounded in collaboration and follow-through

### `Copilot on Mobile (Voice Mode)`

- Focus on voice-driven, on-the-go use: quick summaries, task capture, status checks, and brief communications
- Prompts should be short, natural, and hands-free in tone - as if spoken aloud
- Do not demo complex analytical tasks or long-form document creation
- Emphasize the ambient and contextual nature of mobile Copilot: catching up during a morning workout (exercise bike, on a walk) or while getting ready, quick task triage, voice-to-action
- Do NOT frame voice exercises around driving or commuting in a car. Many customers (utilities especially) treat talking on the phone while driving as a safety violation. Use a safe hands-free context instead: on the exercise bike, on a walk, getting ready at home, or between meetings.

### `Copilot in Excel`

- Focus on formula assistance, data pattern recognition, chart generation, and conditional formatting guidance
- Synthetic data is allowed; frame it as a realistic business spreadsheet (budget, pipeline, ops metrics)
- Do not position Excel Copilot as a substitute for Python analytics or Power BI reporting
- Keep prompts grounded in what a business user - not a data engineer - would naturally ask
- Light analysis is acceptable: highlight outliers, apply conditional formatting, generate a chart, or surface a trend visible in the data
- Do not suggest correlation analysis, regression, statistical modeling, multi-variable analysis, or any prompt that requires Python or advanced reasoning over large datasets; route those use cases to the `Analyst` scenario instead
- If a prompt would feel at home in a Jupyter notebook or a data science workflow, it belongs in `Analyst`, not here

### `Copilot in Word`

- Focus on document drafting, rewriting, summarizing, and expanding existing content
- Typical entry point: content produced by a prior `Researcher` or `Copilot Chat` session, carried through a Loop page
- Demo prompts should show Copilot acting on that content: refining tone, adding an executive summary, restructuring for a specific audience
- Do not demo document creation from scratch without a prior content source unless explicitly requested
- See the linked flow section below for the full Page to Word to PowerPoint sequence

### `Copilot in PowerPoint`

- Focus on Copilot's editing capabilities within PowerPoint: creating a presentation from a Word document, adding slides, applying Designer, and refining content
- Typical entry point: a Word document produced from the Page to Word step in the linked flow
- When the value is simply generating the deck from existing content, a single well-scoped prompt is enough; do not pad with extra iteration prompts the participant does not need
- Demo prompts should show: generating a deck from a document, adding a summary or risk slide, applying a theme
- Do not demo PowerPoint features unrelated to Copilot's editing capabilities
- See the linked flow section below for the full Page to Word to PowerPoint sequence

### Linked flow: Researcher / Copilot Chat to Page to Word to PowerPoint

Use this flow when demoing the full document creation chain. Treat it as a single multi-step scenario with clearly labeled phases.

1. **Generate source content** - Run a `Researcher` or `Copilot Chat` scenario to produce a substantive response. For `Copilot Chat`, the output should be long enough to anchor a document.
2. **Convert to a Page** - Show converting the Copilot response to a Loop page. Demonstrate a brief inline collaboration moment (e.g., a colleague edits or comments).
3. **Export to Word** - Show the page exported to a Word document. Transition into `Copilot in Word` to refine the content for the target audience.
4. **Generate PowerPoint** - From the Word document, use Copilot in PowerPoint's editing capabilities to generate a presentation.

When producing this linked flow:

- Produce a connected prompt sequence that flows naturally across each phase
- Include brief participant-facing handoff cues between phases naming the next app and action
- Synthetic content (if needed) should carry consistent terminology and data through all phases
- Label each phase clearly in the output: `Phase 1`, `Phase 2`, etc.

## Synthetic content rules

Use this table to determine whether synthetic content is allowed and what form it takes:

| Scenario | Synthetic content allowed | Internal validation required | Brand-aligned |
|---|---|---|---|
| `Copilot Chat` | No | - | - |
| `Researcher` | No | - | - |
| `Analyst` | Yes | Yes | Yes, if company named |
| `Notebook` | Yes | Yes | Yes, if company named |
| `Agent Builder` | Yes | Yes | Yes, if company named |
| `Copilot in Outlook` | No | - | - |
| `Copilot in Teams` | No | - | - |
| `Copilot on Mobile (Voice Mode)` | No | - | - |
| `Copilot in Excel` | Yes | Yes | Yes, if company named |
| `Copilot in Word` | Yes, if no prior content source | Yes | Yes, if company named |
| `Copilot in PowerPoint` | Yes, if no prior content source | Yes | Yes, if company named |

When synthetic content is allowed, validate sections, tables, fields, sample rows, formulas, units and evidence support internally before delivery. A detailed blueprint or manifest is optional internal scaffolding, not a required published deliverable. Participant-facing setup names only the needed files immediately alongside the exercise, using a concise open/upload/reference sentence or short bullets and, when useful, a short business purpose. Include relevant business scope or date period naturally. Do not publish a file/pack table, source mapping matrix, inventory section, or blueprint.

Do not publish tab names, sheet maps/counts, row/column coordinates, ranges, exact formulas or metadata-row exclusions as participant preparation. Participants open/upload the file and ask naturally for the result.

For `Agent Builder`, prefer synthetic knowledge sources such as policy documents, handbooks, SOPs, FAQ content, support guides, product documentation, and internal playbooks. Generate these as `.docx`, never `.txt` or `.md`.

Avoid proposing synthetic knowledge sources that depend on large spreadsheet analytics, KPI interpretation, trend modeling, or multi-tab Excel reasoning.

When describing `Agent Builder` scenarios, make the expected value proposition retrieval-focused: finding the right answer, grounding the response in source content, and guiding the user to the relevant policy or procedure.

Make the synthetic content realistic, imperfect, and decision-relevant.

When generating synthetic content for a named company, align file names, department names, product names, and internal terminology to the company's industry and known brand identity. Synthetic content should feel like it plausibly came from that organization.

## Output format

Produce HTML output unless the user explicitly requests plain text.

All HTML handout rules (brand resolution, layout, nav rail, copy-to-clipboard prompt blocks, accessibility contrast, entity encoding, and the pre-delivery sweep) are owned by `copilot-exercise-html-formatter`. Hand the finished exercise content to that skill rather than re-deriving the rules here. Save the result as a downloadable `.html` file; never paste the markup into chat.

## Quality bar

All outputs must be:

- Executive-ready
- Decision-focused
- Grounded in risks, trade-offs, and implications
- Free of hype or marketing language
- Tight and plainly worded (short scenario overviews, no theatrical phrasing)
- Reusable without added explanation

## Guardrails

- Never fabricate facts in exercise content or synthetic data: names, numbers, quotes, dates, or metrics. When a real value is unknown, use a clearly marked placeholder (for example [Add Q3 revenue]).
- Keep synthetic provenance truthful using only the concise `Synthetic` source-metadata label and first-use handout attribution; do not present it as real customer or tenant data or repeat illustrative narrative in prompts or content.
- This skill produces demo content only. It does not send email, post to Teams, schedule or cancel meetings, or delete or overwrite files. When the user wants a real action taken, hand off to the dedicated M365 skill instead.
- Never modify built-in system skills; only the user's own personal skills may be edited, and only through the host's personal-skill management capability.
- Always review before delivering: sweep for em-dashes and en-dashes, confirm brand color placeholders are resolved, and confirm every named synthetic file was actually generated. Also run the business-only wording and bounded-evidence audit on every copy block, narrative section and companion source: verify actual source granularity, workload, numerical path, coverage and consistency, not just the headline scope.
- If required inputs are missing (customer, industry, target role, or scenario type), ask one focused question rather than guessing; when a specific detail cannot be found, use a clearly marked placeholder instead of inventing it.
- Respect copyright: never reproduce third-party copyrighted text in synthetic content; summarize or create original substitutes instead.

## Example requests

- "Create a `Copilot Chat` demo for a retail COO preparing for a weekly ops review."
- "Draft an `Analyst` exercise for a manufacturing finance lead using uploaded spend data."
- "Build an `Agent Builder` demo for an HR knowledge assistant for employee policy questions."
- "Create `Copilot in Outlook` and `Copilot in Teams` demos for a financial services VP."
- "Build the full `Researcher` to `Copilot in Word` to `Copilot in PowerPoint` flow for a healthcare strategy team."
- "Make a `Notebook` exercise for a pharma regulatory team synthesizing submission documents."
- "Create a `Copilot on Mobile (Voice Mode)` exercise for a field operations director."
