---
name: copilot-cowork-exercise-builder
description: |
  Build rich, company-specific and persona-specific Microsoft Copilot Cowork exercises for customer enablement: agentic workspace scenarios, robust multi-step anchor prompts, drop-in synthetic content packs, and executive handouts. Use when the user asks to "create a Cowork exercise", "build a Copilot Cowork demo", "make a Cowork workshop track", "build Cowork exercises for a CFO / plant manager / claims lead", "design a scheduled autonomous briefing demo", "build a Cowork exercise set for [company]", or "create Cowork exercises by persona". Do NOT use for non-Cowork Copilot surfaces (Chat, Researcher, Analyst, Notebook, Agent Builder, Outlook, Teams, Excel, Word, PowerPoint) - use copilot-se-demo-builder; do NOT use to perform the real work a scenario depicts.
cowork:
  category: productivity
  icon: PersonBoard
---

# Copilot Cowork Exercise Builder

Cowork is the agentic workspace: one thread, many surfaces, real deliverables. This skill builds workshop and demo exercises that show that, grounded in a specific company and a specific persona.

The unit of work is a **persona-anchored exercise**. Every exercise names a real operating moment for one role at one company, delegates the whole job in a single robust prompt, and ends with an artifact the participant is holding.

## When NOT to Use

- The exercise targets another Copilot surface (Chat, Researcher, Analyst, Notebook, Agent Builder, Copilot in Outlook / Teams / Excel / Word / PowerPoint, Copilot on Mobile): use `copilot-se-demo-builder` instead.
- The user wants Copilot Studio agent authoring content: that is out of scope for both skills right now.
- The user wants the HTML handout styled, fixed, or rebranded and nothing else: use `copilot-exercise-html-formatter`.
- The user wants the depicted work actually performed (real email, real scheduling, a real deck): use the dedicated M365 skills.
- The user wants a personal skill created, edited, or audited: use `skills`.

## Priority order

1. **Persona fidelity.** The exercise must read like this role's actual week at this company. A generic executive scenario is a failed exercise.
2. **Cowork fidelity.** The exercise must require the agentic workspace. If it can be done in one app, it belongs to another scenario type.
3. **Runnability in a live room.** A participant in their own tenant, with no shared SharePoint or Power BI, must be able to run it start to finish inside the timebox, with a group moving together.
4. **Format and branding.** Presentation follows content; delegate it to `copilot-exercise-html-formatter`.

Resolution rules when these collide:

- Persona fidelity beats scenario boundary: name the initiative, the deadline, the regulator, the plant, not a placeholder.
- Runnability beats realism of source: ship a drop-in pack rather than referencing a tenant artifact participants do not have.
- Runnability beats completeness: cut a step before you let an exercise overrun the timebox.
- Cowork fidelity beats prompt count: one strong orchestration beats four thin turns.
- Accessibility beats branding.

## Required workflow

### 1. Intake

Ask only for what is missing. Never re-ask what the user already gave you.

Company and context:
- Company name (or anonymized label) and industry
- Business unit, function, or department
- Session context and timebox
- Whether participants share a tenant (default: assume they do not)

Persona:
- Target role or roles by title
- The decisions that role owns
- Their operating rhythm (planning cycle, review cadence, governance gates)
- The current pressure: a filing, a turnaround, a season, a board date, an audit

Scope:
- How many exercises, and whether they should form a connected track
- Which patterns to demonstrate, if the user has a preference

If the user names a company and a persona but nothing else, proceed with reasonable industry defaults rather than stalling. Ask at most one clarifying question.

**Research the company and role before authoring.** With the user's authorization, use available enterprise search capabilities for relevant workshop material, account context, email, and files. Use web search for the company's public operating language: business units, program names, regulator, reporting cadence, and published priorities. Ground the scenario in what you find, but do not copy confidential source content into the deliverable. Never invent a named financial figure, executive name, or metric; use a clearly marked placeholder such as `[Add FY26 capex target]` when the real value is unknown.

### 2. Choose the pattern per exercise

Pick exactly one pattern per exercise. Do not blend patterns inside a single exercise. When building a multi-exercise set, vary the patterns deliberately so the set demonstrates range.

**Two patterns are mandatory in every multi-exercise track:** Pattern E (Personal Skill Authoring) and Pattern B (Scheduled Autonomous Briefing). Skill creation and prompt scheduling are the two capabilities that distinguish Cowork from every other Copilot surface, and a track that omits either one undersells the product. Include both even when the persona heuristics would not have selected them, and add the persona that makes each land.

**The one permitted pairing:** Pattern E and Pattern B may be chained, and in a full track they should be. The skill authored in E becomes the skill the schedule in B invokes. See "The E to B chain" below. This is the only exception to the no-blending rule, and it still means two separate exercises, not one merged exercise.

### 3. Build the persona profile block

Every exercise opens from a short persona profile that the rest of the exercise honors:

- Role and scope of authority
- The three decisions this person owns
- What they are measured on
- Their week: the recurring meetings, reviews, and reports
- What is on fire right now

Keep it to five or six tight lines. It is scaffolding for the author and orientation for the facilitator, not a wall of text in the handout.

### 4. Author the exercise content

Produce the required sections (below), the anchor prompt, and the drop-in content pack.

### 5. Generate the synthetic files

Every named file must actually exist as a saved artifact before the exercise is delivered. See Drop-in Content Pack.

### 6. Format and deliver

Hand the finished content to `copilot-exercise-html-formatter` for the styled HTML handout. HTML is the default; plain text only on explicit request. Do not dump markup in chat.

### 7. Verify

Run the pre-delivery checklist. Fix everything before reporting the exercise ready.

## Live-session design (binding)

These exercises are run live with a group, not read alone at a desk. The whole room moves at the pace of the slowest participant, and a Cowork run takes minutes, not seconds. Design for that.

**Budget every exercise at 10 to 15 minutes of room time**, which means roughly: 2 minutes of facilitator setup and context, 1 minute to upload the pack, 1 minute to paste and fire the anchor prompt, 3 to 6 minutes of agent run time, and 3 to 4 minutes to look at the result together. Anything that does not fit that shape gets cut, not compressed.

Hard rules:

- **Budget interview-style prompts; do not ban them.** Having Copilot interview the participant is a legitimate pattern worth showing, and it lands well when the room sees it once. The rule is scarcity, not prohibition:
  - **At most one exercise per session** uses an interview-style prompt. Pick the exercise where the pattern teaches the most and make it the designated one.
  - **Cap it at three questions.** The prompt must say so explicitly, for example "ask me up to three questions, then proceed." An open-ended interview is what actually stalls a room, not the technique itself.
  - Every other exercise in the session states its inputs up front so the agent never stops to ask.
  - Note the designated interview exercise in the track overview so a facilitator running a subset knows which one carries the pattern.
  - Budget an extra 2 to 3 minutes of room time for that exercise and say so in its Facilitator Notes.
- **One anchor prompt, fired once.** Optional follow-ups are genuinely optional and exist so fast participants have somewhere to go, not as required steps the room waits on.
- **Everything the participant types is copy-paste ready.** No prompt should require the participant to compose original text on the spot beyond swapping in an obvious value like a name or a date. Mark any spot where they substitute their own value with a clearly bracketed placeholder.
- **No setup that cannot be done in under a minute.** No connector configuration, no admin consent, no artifact provisioning, no waiting on a tenant change.
- **Plan for the dead air.** Every exercise includes a short `While It Runs` note for the facilitator: one or two things to say or ask the room during the agent run. This is facilitator-facing content and belongs in the handout as a facilitator note, not in the participant instructions.
- **Every exercise must fail gracefully.** Include a one-line `If It Stalls` fallback: what the facilitator says or shows if a participant's run is slow, returns thin results, or errors. Usually this is a described expected output the room can discuss without waiting.
- **Never make one exercise a hard dependency of the next for the participant.** The E to B chain is the single exception, and even there the B exercise must state a fallback skill name so a participant whose E run failed can still complete B.

Track-level timing:

- Multiply the per-exercise budget by the exercise count, add 10 minutes of opening and 10 of close, then compare against the stated timebox. If the total exceeds it, cut exercises rather than trimming each one thin.
- A 60-minute session supports three exercises. A 90-minute session supports four. A half day supports six with breaks.
- State the estimated run time on each exercise in the handout so the facilitator can pace and drop one live if needed.
- Order the track so the exercises most likely to run long sit later, where they can be cut without breaking the story.

## The five Cowork patterns

### Pattern A: Cross-App Executive Prep

- One thread orchestrates uploaded content plus the participant's live calendar and inbox to produce a complete pre-read for a meeting, board moment, or executive review
- Output includes concrete deliverables in the participant's workspace: a Word brief, a PowerPoint pre-read, or a drafted email to the principal with attachments
- Distinct from `Researcher` (web focus, no action chain) and `Copilot Chat` (single surface, no deliverables)
- Best when the moment requires consolidating documents, datasets, transcripts, and live workspace context before acting
- Drop-in content pack required

### Pattern B: Scheduled Autonomous Briefing

- Configures a recurring task that executes without the user present (every Monday at 7am, every weekday at 7:45am, every Friday at 4pm)
- Cowork scans email, calendar, and Teams in the background, applies the user's stated priorities, and posts a digest to a chosen destination (email to self, Teams chat, Teams channel)
- Emphasize persistence: the agent remembers what it surfaced last run and flags what changed
- Distinct from every other scenario type, which assume a user is actively driving
- Do not build this pattern without an explicit cadence (frequency, day, time, timezone) and a destination
- Content pack not required; this pattern reads the live mailbox and calendar
- **Prefer scheduling a saved skill over restating the steps.** When the track includes a Pattern E exercise, the schedule-setup prompt should invoke that skill by name rather than repeating its logic inline. When the track has no Pattern E exercise, the schedule prompt carries its own steps
- The exercise must show where the scheduled task lives after setup, so the participant knows how to review, pause, edit, or delete it. A recurring task the participant cannot find again is a demo, not an adoption moment
- State plainly that scheduled runs happen with no one watching: the prompt must be self-contained, naming the people, channels, and topics it needs, because there is no user present to answer a clarifying question
- Do not imply the scheduled task will send, post, delete, or cancel anything without confirmation

### Pattern C: Live Power BI Investigation to Action

- Conversational analysis against a live Power BI semantic model or report, or (more commonly in workshops) against an uploaded dataset that approximates what the model would return
- The thread identifies the right artifact or dataset, asks analytical questions (variance, drivers, anomalies, segment cuts), then chains into deliverables: an Excel cut for finance, a stakeholder email, a Teams post to regional owners
- Distinct from `Analyst` (bounded to uploads, single surface, no cross-app chain) and `Copilot in Excel` (no semantic-style analysis, no handoff)
- Avoid prompts that require building or modifying the Power BI model. Analysis and action are the focus
- **Tenant guidance:** unless the workshop runs inside a customer tenant against an artifact you know exists, default to the uploaded-dataset approach. Keep the semantic model blueprint as descriptive context only
- Drop-in content pack required

### Pattern D: Multi-Source Project Status Investigation

- Parallel investigation across the uploaded pack and the participant's live calendar and inbox to answer one grounded question ("what is the real status of the Riverbend turnaround?")
- Output is a one-page status with explicit evidence anchors (which document, which transcript line, which email, which meeting), contradictions surfaced, and stale-information flags
- Distinct from `Researcher` (web only) and from a single-thread `Copilot Chat` exercise (no parallel fan-out)
- The value: the facts live across many surfaces, and Cowork reads them in parallel and reconciles them in one answer
- Pack typically includes a chat transcript, a status memo or meeting notes doc, and one or two datasets
- Drop-in content pack required

### Pattern E: Personal Skill Authoring

- The participant defines a reusable workflow ("Friday wrap-up", "weekly customer health check", "Monday account review") that becomes a callable skill in their personal workspace
- Demonstrate the full lifecycle: state the trigger, state the steps, save the skill, invoke it by name, then confirm it persists for a future session
- Distinct from `Agent Builder` (declarative RAG in M365 Copilot) and Copilot Studio (multi-author platform)
- Position as personal automation that compresses a recurring motion, not enterprise governance
- Best for participants who already have a repeating personal workflow
- Content pack not required
- **Author the skill so it can be scheduled later.** The workflow must be one that runs correctly with nobody watching: no step that depends on the participant answering a question mid-run, no reference to "the file I just uploaded" or anything else tied to the authoring session. Name the people, channels, sources, and output destination explicitly inside the skill
- Prefer a workflow with a natural recurring cadence (weekly wrap-up, Monday review, Friday health check) over a one-off task, so the Pattern B exercise has something real to schedule
- Close the exercise by naming the skill the participant just saved and noting that the scheduling exercise will put it on a cadence

## The E to B chain (build this in every full track)

The strongest Cowork story in a workshop is the participant watching their own workflow become a saved skill, then watching that skill run itself on a schedule. Build the track so those two exercises are adjacent and connected.

**Exercise E (author the skill).** The participant states a recurring workflow they already do by hand and saves it as a named personal skill. The anchor prompt is the skill-creation delegation: the trigger phrase, the ordered steps, the sources to reach across, the output format, and the skill name, all in one pass. The participant then invokes it by name once to prove it works.

**Exercise B (schedule the skill).** The participant puts that same saved skill on a cadence. The anchor prompt is the schedule-setup delegation and it invokes the skill by name rather than restating its steps: for example, "Every Friday at 4pm Central, run my Weekly Account Health Check skill and post the result to my Teams chat with myself." The exercise then shows where the scheduled task lives so the participant can review, pause, edit, or delete it.

Rules for the chain:

- Use the **same skill name, verbatim**, in both exercises and in every artifact of the track. A mismatch breaks the demo.
- Keep the two exercises adjacent in the sequence, E first.
- Add an explicit handoff line at the end of E and at the start of B naming the skill that carries across.
- The B anchor prompt must reference the skill by name. If it restates E's steps inline, the chain is not demonstrated and the exercise fails review.
- Both exercises stay persona-anchored: the same person, the same operating rhythm, the same company context.
- If the participant's tenant will not persist personal skills between sessions, say so plainly in the facilitator notes rather than promising persistence.
- The B exercise names a fallback skill name so a participant whose E run failed can still complete B rather than sitting out.
- The E skill-creation prompt normally states the workflow outright. If E is the session's designated interview exercise, it may have Copilot ask up to three questions to shape the steps, but the **skill name must be pinned in the prompt itself**, not left to the interview. A room full of differently-named skills breaks the B exercise that schedules them.

When the user asks for a single exercise rather than a track, build whichever of E or B they asked for. Only apply the chain when there is a track, or when the user asks for skill creation and scheduling together.

## Persona library and coverage

When the user asks for a **set** of Cowork exercises for a company, build persona-based coverage rather than pattern-based coverage. Choose personas from the company's actual operating structure, then assign each a pattern that fits how that role really works.

Coverage heuristics:

- **Executive / P&L owner** (CEO, CFO, BU president): Pattern A or C. Their moment is a board date, a filing, an earnings call, a capital review.
- **Operations leader** (plant manager, field ops director, network ops): Pattern D. Their moment is a turnaround, an outage, a safety event, a schedule slip.
- **Functional lead** (controller, HR director, supply chain lead, procurement): Pattern C or D. Their moment is a variance, a cycle close, a supplier issue.
- **Frontline manager / individual contributor** (CSM, account exec, engineer, analyst): Pattern E. Their moment is a repeating weekly motion worth compressing.
- **Chief of staff / program office**: Pattern B. Their moment is a recurring readout somebody has to assemble every week.

For a full track, aim for three to six exercises spanning at least three patterns and at least three persona levels. Pattern E and Pattern B are mandatory and count toward that spread; chain them per "The E to B chain" above. Sequence from individual value to organizational value: start with a persona-level exercise, end with the cross-organizational one, and place the E to B pair adjacent wherever it falls.

If a track is capped at three exercises, the set is Pattern E, Pattern B, and one of A, C, or D chosen by the lead persona.

Do not build two exercises with the same pattern and the same persona level. If the user asks for more exercises than the personas support, say so and propose the strongest set instead of padding.

## Required output sections

Each exercise contains, in order:

1. `Scenario Overview` - one or two plain sentences: "You need to prepare X for Y, with [constraint]." No bold mini-labels. Capture the moment, why it matters now, and the decision pressure. Omit who needs to act; the reader is the persona.
2. `What This Exercise Demonstrates` - scope framed as outcome and decision value, not feature list.
3. `Drop-in Content Pack` - when the pattern requires one. Placed here, before setup.
4. `Setup / Priming Content` - two or three concrete anchors directly relevant to the anchor prompt: active initiatives, named risks, specific cadence. Lean, not background.
5. `What The Thread Will Reach Across` - the uploaded pack first, then the participant's live calendar, then their live inbox.
6. `Participant-Facing Instructions` - the first instruction is always: upload all files from the drop-in content pack into the thread before running any prompts.
7. `Anchor Prompt` plus at most two optional follow-ups.
8. `What Good Looks Like` - three or four bullets describing the deliverable the participant should be holding, so the facilitator can tell whether the run succeeded.
9. `Facilitator Notes` - the estimated run time, the `While It Runs` talking points, and the `If It Stalls` fallback. Facilitator-facing, visually separated from participant instructions in the handout.

Pattern-specific additions:

- Pattern A: name the target meeting or moment, the principal, and the deliverable types
- Pattern B: state the exact cadence (frequency, day, time, timezone), the scan sources, the output destination, one sentence on what the agent flags run over run, the name of the saved skill being scheduled (when the track includes Pattern E), and where the participant manages the task afterward
- Pattern C: include a concise semantic model blueprint (model name, two or three tables, three to five measures, primary date dimension) and the downstream deliverable
- Pattern D: name the question being answered, the surfaces in scope, and the one-page output structure
- Pattern E: include the skill name, the trigger phrase, a three to five step outline, one sample invocation, and a note that the skill is written to run unattended so it can be scheduled in the Pattern B exercise

## Anchor prompt design (binding)

Cowork is not Copilot Chat. People do not run short prompts back and forth reading a response between each one. They write one substantial prompt that delegates the whole job as a sequence of steps, then let the agent orchestrate it in a single thread. Build every exercise around that.

- **Lead with one anchor prompt.** A single substantial delegation naming the steps in order, the sources to reach across, and the deliverables to produce. Write the steps as a short numbered list or clearly sequenced clauses inside one prompt, never as separate prompts fired one at a time. It should read like a real instruction to a capable assistant: "Do A, then B, then C, and give me D."
- **Make it genuinely robust:** a lead sentence plus a three to six step numbered list, or four to eight sentences, covering the full arc from inputs to finished deliverable. This is the heart of the exercise. Do not water it down to a one-liner.
- **Robust does not mean slow.** Scope the anchor prompt so a single run lands in roughly three to six minutes. Reaching across three or four sources and producing one or two deliverables is the right size. Reaching across eight sources and producing five deliverables will not finish in a live room.
- **The prompt does the asking, not the agent, in all but the designated interview exercise.** State every input the agent needs inside the prompt so it never has to stop and ask. The one exercise designated to demonstrate the interview pattern is the exception, and even there the question count is capped in the prompt itself.
- **At most one or two optional follow-ups**, labeled optional, for refinement or a next action. Cap total prompts at three.
- **Show orchestration, not clicks.** The prompt describes the outcome and the steps to reach it, never a manual sequence of UI actions.
- Pattern B's anchor prompt is the schedule-setup prompt. Pattern E's anchor prompt is the skill-creation prompt.

Write prompts the way the persona would actually type them: conversational, concise, decision-oriented. No prompt-engineering scaffolding, no system-style language, no hype.

## Drop-in Content Pack (binding)

Workshop participants do not share a tenant. Their SharePoint libraries, Teams channels, and Power BI models will not match anything you invent. Never instruct participants to "open the X SharePoint library" or "query the Y semantic model" unless the user has confirmed those artifacts exist in the participants' tenants.

Ship a drop-in pack of small synthetic files the participant uploads into the thread, paired with their real calendar and inbox.

Binding for Patterns A, C, and D, and for any pattern that would otherwise reference tenant-specific files, libraries, channels, or models. Not required for Pattern B or E unless the user asks for it.

Every pack-bearing exercise includes:

1. A `Drop-in Content Pack` section with a short intro line explaining that the pack stands in for tenant artifacts, plus a table mapping each file to what it contains and which prompts use it.
2. The actual files, saved under `output/<NN>-<exercise-slug>-pack/` (for example `03-cfo-rate-case-prep-pack/`).
3. A `What The Thread Will Reach Across` block listing uploads first, then live calendar, then live inbox.
4. A first participant instruction to upload everything before running any prompts.
5. At least one prompt that references the participant's real calendar or inbox alongside the uploads, so the cross-context value is demonstrated. **Keep live references generic about what is there.** Never promise specific synthetic-scenario items in the participant's real tenant. Phrase the prompt to work against whatever they actually have, and tell Copilot to say so if nothing relates. The same applies to the reach-across block: list "your live calendar" and "your live inbox" plainly.

Pack composition:

- Three to six files, sized for a workshop, not a document corpus. Keep each file short enough to ingest quickly: a two-page brief, a few dozen rows, a one-screen transcript. Large files slow every run in the room
- Mix at least two formats so participants see multi-format ingestion: one `.docx` brief, one `.xlsx` dataset, one `.docx` transcript
- For Pattern C, ship an `.xlsx` (or two) approximating what the semantic model would return
- Realistic, imperfect, and decision-relevant: include the contradictions, stale assumptions, and quoted positions the anchor prompt will exercise
- Prompts reference uploads by what they contain, not by file name: "Using the intervenor testimony excerpts I uploaded" reads better than "Open intervenor_testimony_excerpts.docx". The mapping table gives exact names.

**File format realism.** Choose the format a real organization in that industry would use, not the one easiest to generate. Finished documents (briefs, memos, policies, board pre-reads, SOPs) are `.docx`. Tabular data is `.xlsx`; reserve `.csv` for a genuine flat single-table export. **Never ship a `.txt` or `.md` file in a pack.** Content that is plain text in real life, such as chat or meeting transcripts, log excerpts, and code or config snippets, is delivered as `.docx`: keep the verbatim plain-text body intact inside the document (speaker labels, timestamps, line breaks, monospaced blocks for logs or code) and add a short header line naming the source, participants, and date. Where `.pdf` would be the real-world format, still deliver `.docx` unless the user explicitly asks for PDF.

**Synthetic realism.** Company terminology, file names, department names, and program names should look like they plausibly came from that organization. Embed the decision-relevant tension the way it appears in real documents, not as an obvious flag: a variance buried in a table, a commitment quoted in a transcript that contradicts a memo, a date that has quietly slipped. Avoid on-the-nose synthetic data.

## Multi-exercise tracks

When building a connected set:

- Open with a short track overview: the company, the personas covered, the through-line, the per-exercise run times, and which exercise is the designated interview-pattern exercise
- Number the exercises and use the same numbering for their pack folders
- Add a one-line handoff cue between exercises so the facilitator knows the connective tissue
- Keep terminology, program names, dates, and figures consistent across every exercise and every synthetic file in the track
- If a file serves two exercises, keep it in its primary exercise's pack folder and reference it cross-folder from the other

## Style

- Address the persona directly: "you", "your". Not "the CFO".
- Tight, non-dramatic prose. Cut theatrical build-up, hype, and marketing phrasing. State each point in one crisp clause. Default to aggressively short on the first build.
- No meta-narrative inside the exercise: no explanations of your approach, no rationale for structure, no "this exercise is designed to..." framing. Scenario context and "why this prompt matters" lines are part of the exercise and are not meta-narrative.
- Exercise titles lead with the business process, with the product in parentheses: "Prepare the Rate Case Hearing Pre-Read (Copilot Cowork)", not "Copilot Cowork: Rate Case Prep".
- Never use em-dashes or en-dashes in any artifact. Use a colon, comma, period, spaced hyphen, or parentheses.

## Cowork positioning boundaries

- Focus on the agentic workspace: cross-app orchestration, multi-step execution, autonomous scheduled work, deep multi-source investigation, live data-to-action chains, all in one thread
- State the value plainly. Avoid hype like "stops being a feature inside apps"
- Do not regress to single-surface tasks. If the exercise can be completed entirely inside Outlook, Teams, Excel, Word, or PowerPoint, it belongs in `copilot-se-demo-builder`
- Do not position Cowork as a replacement for Agent Builder or Copilot Studio. It is the personal, conversational workspace where agents are invoked, work is delegated, and deliverables are produced
- Cowork runs against the participant's own M365 tenant. Do not promise access to systems outside M365 unless a named Power BI model or supported connector is in scope
- For scheduled patterns, do not imply autonomous destructive actions (deleting files, force-cancelling meetings, sending without approval) without confirmation
- **Never include Copilot Chat custom instructions in a Cowork exercise.** Custom instructions are a Copilot Chat construct configured under Settings, Customize, Custom instructions. They are not part of Cowork and do not govern a Cowork thread. Do not add a custom-instructions setup step, do not tell participants to configure or paste them, do not reference the Settings path, and do not build a before-and-after comparison around them. That exercise belongs to `copilot-se-demo-builder` under Copilot Chat.
- The equivalent move in Cowork is not a settings change: context and standing preferences are carried by the anchor prompt itself, by the uploaded content pack, and by a saved personal skill (Pattern E). When an exercise needs the agent to know the participant's priorities or format preferences, state them inside the prompt or bake them into the skill

## Pre-delivery checklist

1. Every exercise names a specific persona and a specific operating moment, not a generic executive.
2. Each exercise uses exactly one pattern, and a multi-exercise set spans at least three patterns.
3. Every multi-exercise track includes both Pattern E (skill creation) and Pattern B (scheduled prompt), adjacent, E first.
4. The Pattern B anchor prompt invokes the Pattern E skill by name rather than restating its steps, and the skill name matches verbatim across both exercises and every artifact.
5. The Pattern E skill is written to run unattended: no mid-run questions, no dependence on the authoring session, with people, sources, and destinations named explicitly.
6. The Pattern B exercise tells the participant where the scheduled task lives so they can review, pause, edit, or delete it.
7. Every anchor prompt is a single robust delegation with three to six sequenced steps, and total prompts per exercise do not exceed three.
8. Every pack-bearing exercise has its files actually generated and saved in the correct numbered folder.
9. No synthetic file is `.txt` or `.md`. Every non-tabular file in the pack, transcripts and log excerpts included, is `.docx`.
10. No prompt or reach-across block promises scenario-specific content in the participant's real calendar or inbox.
11. No em-dashes or en-dashes anywhere, including inside the synthetic files.
12. Terminology, dates, and figures are consistent across every exercise and file in the track.
13. Every unknown real-world value is a clearly marked placeholder, not an invented figure.
14. The handout was produced through `copilot-exercise-html-formatter` and saved as a file, not pasted into chat.
15. Every exercise fits the 10 to 15 minute room budget and carries an estimated run time in the handout.
16. At most one exercise per session uses an interview-style prompt, it caps the question count at three in the prompt text, it is flagged in the track overview, and its Facilitator Notes carry the extra time. Every other exercise states its inputs up front.
17. No exercise references Copilot Chat custom instructions, the Settings and Customize path, or a custom-instructions before-and-after comparison.
18. Every exercise has `Facilitator Notes` with `While It Runs` talking points and an `If It Stalls` fallback.
19. The track total, including opening and close, fits the stated timebox; if it did not, exercises were cut rather than thinned.
20. Every participant-typed prompt is copy-paste ready, with any substitution marked as a bracketed placeholder.

## Guardrails

- Never fabricate facts in exercise content or synthetic data: names, numbers, quotes, dates, or metrics. Use a clearly marked placeholder such as `[Add Q3 revenue]` when a real value is unknown.
- Keep synthetic content clearly illustrative and labeled as synthetic. Never present it as real customer or tenant data.
- This skill produces demo content only. It does not send email, post to Teams, schedule or cancel meetings, or delete or overwrite files. Hand off to the dedicated M365 skill when the user wants a real action.
- Never build a Cowork exercise around a tenant artifact the participants will not have.
- Respect copyright: never reproduce third-party copyrighted text in synthetic content. Summarize or write original substitutes.
- Never modify built-in system skills.
- If required inputs are missing (company, persona, or pattern), ask one focused question rather than guessing.

## Example requests

- "Build a Cowork exercise for a utility CFO heading into a rate case hearing."
- "Create a set of Cowork exercises for an energy company across four personas."
- "Design a Scheduled Autonomous Briefing exercise for a sales VP who wants a Monday 7am pipeline digest in Teams."
- "Build a Cowork Multi-Source Project Status exercise for a plant manager during a turnaround."
- "Make a Personal Skill Authoring Cowork exercise for a CSM who runs a weekly customer health check."
- "Build a paired Cowork exercise where the participant saves a skill and then schedules it to run every Friday."
- "Give me a five-exercise Cowork track for a regional bank, persona-based, for a half-day workshop."
