---
name: copilot-se-demo-builder
description: |
  Create executive-ready Microsoft Copilot demo exercises, workshop scenarios, and prompt sequences for customer enablement sessions. Use when the user asks to "create a Copilot demo", "build a Copilot workshop", "make a Researcher exercise", "build an Agent Builder demo", or "put together a full suite of Copilot exercises" for Copilot Chat, Researcher, Analyst, Notebook, Agent Builder, Copilot in Outlook, Teams, Excel, Word, or PowerPoint, or Copilot on Mobile. Do NOT use for Copilot Cowork exercises (use copilot-cowork-exercise-builder) or for HTML handout formatting alone (use copilot-exercise-html-formatter); do NOT use to actually perform the work a scenario depicts (sending real email, real meeting prep, building real decks) - use the dedicated M365 skills instead; do NOT use to modify built-in system skills.
cowork:
  category: productivity
  icon: SlideText
---

# Copilot SE Demo Builder

Use this skill to create customer-facing Copilot demo scenarios. Produce one scenario per request unless the user explicitly requests multiple scenarios and provides both the exact number and the specific scenario types. If either is missing, ask one clarifying question. You may also offer one optional `Writing Assistant` companion exercise after the primary output; only generate it if the user accepts.

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

Context that is part of the exercise itself (for example Scenario Overview, decision pressure, and why a prompt matters at that step) is required and is not treated as meta-narrative.

**In the exercise output, do not include:**
- Explanations of your approach
- Rationale for structure or design
- Meta-framing phrases like "this exercise is designed to..." or "the goal here is..."

**Note:** The non-overlap check (workflow step 3) is a brief planning statement outside the exercise output and is exempt from this rule.

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
   - In 1-2 sentences, state how this exercise is distinct from other exercises mentioned.

3. **Capability boundary enforcement**
   - Write a "What This Exercise Demonstrates" section that frames scope in terms of outcome and decision value.
   - Example: "This exercise demonstrates how to surface priorities and reshape Copilot's tone through custom instructions."
   - Focus on what participants will see work, grounded in decision value.

4. **Produce the exercise content**
   - Include only the sections relevant to the selected scenario.

5. **Generate synthetic files**
   - Generate every named file the exercise references, per the synthetic data rules below, before delivering.

6. **Format and deliver**
   - Hand the finished content to `copilot-exercise-html-formatter` for brand resolution and the styled HTML handout. Save the HTML as a downloadable `.html` file; do not output it as a code block in chat.
   - If output format is plain text: return as formatted text in chat.

7. **Offer optional companion exercise**
   - After delivering the requested scenario(s), offer one optional additional `Writing Assistant` companion exercise.
   - If the user accepts, generate the companion exercise in the same output format and with the same customer context.
   - If the user declines or does not answer, stop after the requested scenario(s).
   - If the user explicitly requested standalone `Writing Assistant`, treat that as the requested output and skip the companion-offer step.

## Required output sections

For `Copilot Chat` scenarios, prepend a `System of Work: Think, Plan, Do, Evaluate` section before the standard sections below.

1. `Scenario Overview`
2. `What This Exercise Demonstrates`
3. `Setup / Priming Content`
4. `Participant-Facing Instructions`
5. `Prompt Sequence` (4-5 prompts maximum; never exceed 5). One exception: `Researcher` (one Chat framing prompt plus one Researcher run). See that scenario section for the exact structure.

Context depth expectations for every exercise:

- `Scenario Overview` is **1-2 plain sentences** of scenario context, in the shape "You need to prepare X for Y, with [constraint]." Do NOT use bold mini-labels (no "The moment / Why now / Pressure / Who needs to act" structure). Capture the current moment, why it matters now, and the core decision pressure in plain prose. **OMIT "who needs to act."** The reader is the target persona, so naming an owner is redundant. Keep the "Scenario Overview" section heading itself.
- `Setup / Priming Content` should be lean: only include 2-3 concrete anchors directly relevant to the first prompt (active initiatives, named risks, specific cadence); avoid verbose background
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
  - A short framing paragraph that states this is a hands-on system of work for delegating complex work to AI and evaluating outputs with leader-level rigor.
  - Four concise phase callouts in this exact sequence:
    - **Think - Frame the Problem**
    - **Plan - Design the Delegation**
    - **Do - Execute with the Right Tool**
    - **Evaluate - Judge the Output**
  - A closing line with this exact wording: **Accountability stays with the leader at every step.**
  - Include a TPDE mapping table when it improves clarity. If included, it must be adapted to the specific customer and business unit for the current exercise.
  - Treat the maritime mapping table pattern as an example only, never as default reusable text.
  - Build customer-specific rows by mapping each TPDE phase to the customer's real operating rhythm (for example: planning cycle, execution cadence, governance gates, and review motions) and then to what participants do in the exercise.
  - A one-sentence transition into the Copilot Chat exercise.

2. **Scenario Context** - Provide a specific, plainly-worded setup grounded in your industry, role, and current moment (a pending board meeting, an active regulatory process, a seasonal pressure like fire season or budget cycle). Keep it to 1-2 sentences; this context anchors all prompts and makes the scenario feel real, not generic.

3. **Quick Priority Check** - Start with: "What are my top 3 priorities for today?" Copilot will scan your live mail, calendar, and Teams to surface what needs attention. **Why this first:** You're establishing what matters in your current moment. Copilot sees your calendar and inbox but doesn't yet know your values, context, or what "high-impact" means to you. It's offering an initial read based on activity and recency, not on your actual strategic focus.

4. **Custom Instructions Builder** - Open a new chat, then run this prompt: "Do not interview me. Use my Microsoft 365 work signals to figure out how I work, then write my custom instructions for me. Look across my email, calendar, meetings, Teams chats, and files from the last 60 to 90 days and determine: my role and the scope I own; the people and teams I work with most and how I relate to each; the recurring meetings and cadences that structure my week; the projects, accounts, and priorities absorbing most of my time; the decisions I actually make; the audiences I write for; and the tone, length, format, and level of detail in the messages and documents I produce. Where the evidence is thin, make a reasonable inference and label it clearly so I can correct it. Return the finished custom instructions as a single copyable code block, written in first person, under 1,500 characters, followed by a short list of what you based each part on." Once Copilot drafts your custom instructions, review the inferences, then apply them: Settings -> Customize -> Custom instructions -> paste -> Save. **Why this step matters:** Do NOT build the instructions "based on what we just explored." The Quick Priority Check step deliberately shows that Copilot's read without custom instructions is shallow and disconnected, so anchoring the instructions to that result would carry the weakness forward. Start a NEW chat instead, so the disconnected read does not prime the model. The point of the inference approach is that Copilot already has the evidence: rather than asking you to describe your job, it reads your real working patterns and shows you what it can already see. That reveal is the demo moment. Participants correct what it got wrong instead of composing from scratch, which is faster and produces sharper instructions than self-report.

5. **Before / After Demonstration** - Open a fresh chat and re-run the opening prompt: "What are my top 3 priorities for today?" **What to notice:** Compare this response to the first one. You'll see differences in tone, framing, and *what* surfaces to the top. The same query now reflects your strategic context, not just activity. This shows how custom instructions reshape every interaction going forward.

6. **Executive Productivity Prompts** - Run these prompts in sequence and pause after each to absorb the insight:
  - "Based on my previous interactions with [/person], identify five topics they are likely to prioritize in our next meeting."
  - "Create a project update from the emails, chats, and meetings in [/series]. Cover progress against targets, wins and losses, risks, competitive developments, and likely questions with proposed answers."
  - "Assess whether the [Product] launch is on track for [date]. Review engineering progress, pilot results, and key risks, then provide a confidence estimate and explain it."
  - "Analyze my calendar and email from the past month. Group my work into five to seven project categories, estimate the share of time spent on each, and briefly describe them."
  - "Use [/select email] and prior manager and team discussions to prepare me for the next meeting in [/series]."

7. **Participant Practice** - Draft at least one custom instruction specific to your own function (rate case strategy, treasury, accounting, FP&A). Apply it, then re-run one of the executive productivity prompts. Notice how your new instruction shapes the response differently.

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
- Label the two phases clearly (for example `Phase 1: Frame in Chat` and `Phase 2: Run Researcher once`) so the facilitator knows when to toggle Researcher on.

### `Analyst`

- Keep analysis strictly bounded to uploaded data

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
- Include brief handoff cues between phases so the facilitator knows when to switch apps
- Synthetic content (if needed) should carry consistent terminology and data through all phases
- Label each phase clearly in the output: `Phase 1`, `Phase 2`, etc.

## Synthetic content rules

Use this table to determine whether synthetic content is allowed and what form it takes:

| Scenario | Synthetic content allowed | Blueprint required | Brand-aligned |
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

When synthetic content is allowed, provide a concise blueprint with:

- file name
- purpose
- key sections or tables
- optional sample rows or excerpts

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
- Always keep synthetic content clearly illustrative and labeled as synthetic; do not present it as real customer or tenant data.
- This skill produces demo content only. It does not send email, post to Teams, schedule or cancel meetings, or delete or overwrite files. When the user wants a real action taken, hand off to the dedicated M365 skill instead.
- Never modify built-in system skills; only the user's own personal skills may be edited, and only through the host's personal-skill management capability.
- Always review before delivering: sweep for em-dashes and en-dashes, confirm brand color placeholders are resolved, and confirm every named synthetic file was actually generated.
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
