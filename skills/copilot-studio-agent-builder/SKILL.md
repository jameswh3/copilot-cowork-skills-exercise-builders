---
name: copilot-studio-agent-builder
description: |
  Picks the right harness for a single Microsoft Copilot Studio agent, then produces a styled HTML hands-on
  walkthrough taking a participant from an empty environment to a working agent: numbered click-path exercises,
  copy-ready instruction text, knowledge (including web knowledge), tools, test prompts, and publishing.
  Use when the user asks to "build a Copilot Studio agent", "which harness should I use", "add knowledge to my
  agent", "add tools to my agent", "write agent instructions", or "publish my agent to Microsoft 365 Copilot".
  Do NOT use for Copilot Cowork exercises (use copilot-cowork-exercise-builder), other Copilot surface demos
  (use copilot-se-demo-builder), or to provision the agent — this produces the guide, not the agent.
metadata:
  category: automation
  icon: BotSparkle
---

# Copilot Studio Agent Builder

Decide the harness internally, then produce a **hands-on walkthrough** that takes a participant from an empty
Copilot Studio environment to a working, tested, published agent. Audience: customer makers building their own
agent, following along at a keyboard.

**This is a lab, not a briefing.** The participant should never have to decide what to type. Every step names a
UI element and an action; every configuration value is supplied literally; every lab ends with something the
participant can see on screen to confirm it worked.

**The hand-waving test.** Read any instruction you wrote and ask: *could someone do this without knowing anything
I haven't told them?* "Add a scope guardrail" fails. "Paste this into the Instructions box: `Only respond to
questions about ...`" passes. If a step tells the reader to *decide, consider, ensure, review, map, assess,
determine, think about,* or *make sure* — it is not a step, it is a topic heading with no content. Rewrite it as
an action, or move it to the settings table where a recommendation belongs.

## When NOT to Use

- Cowork exercises / workshop tracks → `copilot-cowork-exercise-builder`
- Demos for Copilot Chat, Researcher, Analyst, Agent Builder, Word/Excel/PowerPoint → `copilot-se-demo-builder`
- Multi-agent designs — connected agents, parent/child agent hierarchies, agent-to-agent handoff. This skill
  designs **one** agent. If a scenario seems to need a second agent, narrow the scope of the first instead and
  note it as an open question for later.
- Azure AI Foundry / Agent Framework / pro-code agent development
- Actually provisioning, configuring, or publishing the agent in a live tenant
- Licensing quotes, pricing negotiation, or credit forecasting (point to the billing docs instead)

## Build Sequence (why this order)

The eight exercises are ordered by dependency, not by topic. Two positions are the ones people get wrong:

1. **Solution first, before the agent exists.** Every Copilot Studio agent is created inside a solution, and
   anything created outside one lands in the *default* solution. An agent there cannot be exported and moved
   between environments as a unit, and its components scatter among unrelated ones. So: create the solution in
   exercise one, then **create the agent from inside that solution** in exercise two.
   **Never tell participants to set a preferred solution.** It works for a lone maker and breaks down in a
   shared environment: "preferred solution" redirects where *new components* are created, so a room of people
   each setting their own produces collisions and confusion. Creating the agent from within the solution
   achieves the same placement without touching a shared setting. For the same reason, have participants put
   their own name or initials in the solution and agent names — the environment's lists are shared.
   Note the security-role dependency (Environment Maker or System Customizer) in "Before you start", and give
   participants without it a way to continue in the default solution rather than a dead end.
   **Keep it shallow.** Create the solution, build in it, move on. Publisher prefixes, managed versus
   unmanaged, solution layers and pipelines are ALM topics that belong to a later curriculum, not to a
   participant's first agent. Two or three sentences of why, then the clicks.
2. **Boundaries before capability.** Scope and grounding rules (instructions) come before knowledge; the web
   boundary comes before tools; testing comes before publishing. The failure mode of an agent is not a clumsy
   sentence, it is a confident wrong action against a real system — so the guide constrains what the agent may
   do *before* connecting it to anything that can act.

Everything else follows from those: create → instructions → knowledge → web boundary → tools → test → publish.

Deeper capabilities (agent flows and automation, event triggers, adaptive cards, multi-modal prompts, Dataverse
grounding, MCP servers, connected agents) sit **outside** a first build. Name them in "Where to go next" rather
than folding them in — a first lab that ends with a working, tested, published agent beats one that covers more
and finishes nothing.

## Further Training: Agent Academy

**Copilot Studio Agent Academy** (https://microsoft.github.io/agent-academy/) is Microsoft's free, open-source,
hands-on training program. Every guide ends by linking it as the next step. Two things to keep straight:

- **It is a teaching resource, not a product authority.** Microsoft Learn remains the only source for product
  behavior, limits, setting names, and UI paths under the Hard Grounding Rule. Never cite Agent Academy for a
  fact about how the product works — link it as a place to go and keep learning.
- **What to link:** [Recruit](https://microsoft.github.io/agent-academy/recruit/) is the entry course, one IT
  support scenario end to end, in two paths (a 13-mission topic-based path, and a 10-mission instruction-driven
  path). [Special Ops](https://microsoft.github.io/agent-academy/special-ops/) are standalone single-topic labs
  (MCP servers, RAG with Azure AI Search, custom skills) taken in any order. Always include the caveat that
  Agent Academy supplies no environments or licenses, and that some missions need Dataverse, solution import
  rights, or admin permissions.

**Borrow its structure, never its voice.** What transfers is the construction: one scenario carried across the
whole sequence, dependency-ordered steps, prerequisites stated before anyone starts, capability-based objectives,
and an end-state checklist of things the participant observed. What does NOT transfer is its presentation — no
codenames, mission numbering, difficulty ratings, badges, rank language, or emoji-led headings. Those belong to
Agent Academy. Guides from this skill use the customer's own voice and the standard handout format defined by the companion formatter skill.

## Hard Grounding Rule

Copilot Studio changes fast. **Never assert a product behavior, limit, setting name, or UI location from memory.**
Before writing the guide, re-verify anything version-sensitive against `learn.microsoft.com` with `web_fetch` /
`web_search` — especially: harness capability differences, knowledge source limits, orchestration settings, tool
counts, and publishing paths. [references/harness-matrix.md](references/harness-matrix.md) is the doc-grounded baseline; treat entries older
than the current quarter as needing a re-check. If a check fails, say the detail is unverified rather than guessing.

## Workflow

1. **Resolve the scenario.** Capture: business outcome, users, where they'll use the agent, what data grounds it,
   what actions it must take, and whether it runs on request or on a trigger. With the user's authorization, use
   available Microsoft 365 search and file-reading capabilities when the user references a customer, meeting, or
   document. Ask at most one focused question when the harness choice is genuinely blocked.
2. **Pick the harness — an internal decision, reported in chat only.** Use
   [references/harness-matrix.md](references/harness-matrix.md). In your chat reply give the pick, the one-line
   reason, the trade-off given up, and the warning that GitHub Copilot and standard harness agents **cannot be
   converted to each other** after creation. **None of this goes in the guide** (see Artifact Voice). The pick
   still shapes the guide — it determines which capabilities and settings you document — it just isn't narrated
   to the reader. Scope the design to a **single agent**: one set of instructions, one knowledge set, one tool set.
3. **Write ONE lab made of eight exercises.** The deliverable is a single lab producing a single working
   agent; the exercises are its parts, never eight standalone labs. Each adds one capability to the **same**
   agent, in this order — the sequence is load-bearing, see Build Sequence below:
   solution → create agent → instructions → knowledge → web boundary → tools → test → publish.
   Keep each exercise to what the participant must *do*. Platform machinery they are not configuring (publisher
   prefixes, solution layers, managed vs unmanaged, ALM pipelines) is a distraction inside a first build — one
   sentence of rationale, then the steps.
   Use the click paths and copy-ready text in [references/lab-patterns.md](references/lab-patterns.md) and the
   coverage checklist in [references/build-checklists.md](references/build-checklists.md) — the checklist says
   *what must be covered*, the lab patterns say *how to write it as steps*. Every exercise carries Goal, Steps,
   Enter this, and **Check it worked** — an exercise missing that last one is not finished. Add "If it didn't"
   only where the failure is likely and fixable from the keyboard; omit it rather than padding.
   Write the agent's actual instruction text, knowledge source names and descriptions, and tool names for the
   scenario — do not tell the participant to compose their own. The instructions exercise always includes the
   Microsoft 365 Copilot refinement prompt from the lab patterns, with its caution about leaving citation and
   formatting rules alone.
4. **Verify** every product claim and every UI path against Microsoft Learn (Hard Grounding Rule). A click path
   you cannot verify gets written as a step and marked **[Verify]** — never invented. Collect the **full URLs**
   you actually fetched, not just page titles; every lab carries at least one, and the Sources table links them.
5. **Render the guide.** Invoke `copilot-exercise-html-formatter` and hand it the content; save to
   `output/<agent-name>-build-guide.html`. Never hand-roll the HTML. Confirm with `Glob output/**/*` before
   telling the user it's ready.
   **Then run both sweeps on the rendered file:**
   - *Voice:* grep for `harness`, `credit`, `facilitat`, `the room`, `workshop`, `agenda`, `Day One`, `Day Two`,
     `we `, `I `, `you asked`, `as discussed`. `harness` and `credit` must return **zero** hits.
   - *Hand-waving:* grep for `consider`, `decide`, `ensure`, `make sure`, `review the`, `map each`, `assess`,
     `determine`, `think about`, `as appropriate`, `as needed`. Each hit inside a lab step is a defect — rewrite
     it as an action or move it to the settings table. Then confirm every lab has a "Check it worked" and that
     every instruction, description, or configuration value the participant must enter appears literally in a
     copy block. Do not add a "If it didn't" block for a failure the participant cannot act on.

   A guide that reads like chat output, or that tells the participant to figure something out, is a failed
   deliverable even if every fact in it is correct.
6. **Summarize in chat**: harness pick + reason, the 3-5 decisions that most affect quality, and open questions
   the customer must answer (data access, authentication, admin approvals). This is also where any critique of
   the customer's existing materials goes — never in the artifact.

## Things Builders Must Not Miss

Call these out explicitly in every guide — they are the common failure points:

- **Web knowledge is two different things.** A *public website knowledge source* restricts results to URLs you
  list; the separate *Web Search / "Use information from the web"* setting searches everything Bing indexes and
  interleaves those results. Recommend a default per scenario and state the data-boundary implication.
- **Grounding is done through instructions, not the ungrounded-responses toggle.** Tell the agent in its
  instructions to answer only from its configured sources, always cite, and say so when the sources don't cover
  the question. **Never put "turn off Allow ungrounded responses" in a guide** — with it off an answer is
  returned only when it carries a citation, and because models omit citations unpredictably, correct answers
  vanish intermittently. That is an unteachable failure: it looks like a broken agent, it is not reproducible on
  demand, and diagnosing it derails a session. Leave the setting alone and keep it out of the settings table.
- **Explain retrieval before configuring it.** The knowledge exercise opens with a short plain-language account
  of how the agent actually answers: rewrite the query, retrieve roughly the top three results per source,
  summarize with citations, validate. Then the distinction people get wrong — documents return passages, while
  structured sources (Dataverse, Azure SQL) turn the question into a query over rows, which is the only way a
  "how many / total / top five" question is answerable. Both are knowledge and both are read-only: **knowledge
  informs the answer, a tool takes the action.** See references/lab-patterns.md for the wording.
- **Descriptions are routing logic.** Tool, knowledge, topic, and agent *names and descriptions* are what the
  orchestrator reads to choose. A vague description is a routing bug, not a cosmetic one.
- **Instructions can't do everything.** Instructions steer summarization and conversational flow — not citation
  format, retrieval logic, Adaptive Card triggering, or the fallback message. Route those to the right surface.
- **Tool count discipline.** Keep the tool set small and purposeful — a handful of well-described tools
  outperforms a long list. If the scope keeps growing, narrow the agent rather than adding tools.
- **Tool authentication is a design decision** and belongs in a lab step: end-user credentials preserve per-user
  permissions, maker-provided credentials share one identity. **Agent-level authentication is not** — it already
  defaults to Authenticate with Microsoft, so a step confirming that is a stop with no action behind it. Put it
  in the settings reference as "leave at the default" and move on.
- **Untrusted content is an attack surface.** Agents that read email, tickets, or web content can be prompt-
  injected. Constrain which tools may run after reading a knowledge source and which recipients/parameters are
  allowed; consider requiring confirmation before consequential tools run.
- **Publish is a separate step from build**, and channel availability may be admin-gated.

## Default Tool Shape

Most single-agent scenarios need one or two actions, not a toolbox. Start here and justify anything beyond it:

- **Send an email** — the Office 365 Outlook connector is the common case. Pair it with an explicit recipient
  constraint in the instructions, rich-text formatting for the body, and confirmation before running when the
  message goes to anyone outside a known list.
- **An agent flow** — for a multi-step or system-of-record action (create a record, look something up, chain a
  couple of steps) that shouldn't be left to the model.
- Then, only if the scenario demands it: prompt, REST API, MCP server, custom connector, or computer use.

Name each tool for the action it performs and describe when the agent should use it — that description is what
the orchestrator routes on. **Supply the actual name and description text in the guide**; a participant should
paste them, not invent them.

## Artifact Voice (binding)

The HTML guide is a **standalone document for the customer**. It must read as though it were written for them
from scratch, with no trace of the conversation that produced it and no delivery-team scaffolding.

Keep OUT of the artifact — put these in the chat reply instead:

- **Facilitator and delivery notes.** No "say this out loud", "give the room", "before the room clicks", no
  references to sessions, days, agendas, blocks, rungs, breaks, or who presents what.
- **Chat echo.** No "as we discussed", "you asked", "here's what I found", "this test run", no first person
  (I / we / let's), no addressing the requester rather than the reader.
- **Review commentary on the customer's own materials.** Findings about *their* deck, agenda, or plan are
  chat-reply content. Only product constraints a builder must act on belong in the artifact, stated as
  constraints, never as critique of their document, and never framed around a harness.
- **Process narration.** No mention of tools used, files read, folders, searches, or how the guide was built.
- **Harness selection content.** No harness names, no comparison table, no "recommended harness", no
  convertibility or credit-consumption warnings, and no harness-titled sources. The harness is decided before
  the guide exists; the guide documents the agent that decision produced. Write settings and capabilities
  plainly ("skills are not available for this agent") rather than attributing them to a harness.

Second person addressed to **the builder** ("add the source you want the agent to search") is correct and
expected — that is how product documentation reads. Second person addressed to **the requester** is not.

Every heading must survive the test: *would this heading make sense to someone who has never seen the request?*
"Open Questions for the Customer" fails; "Decisions Required Before Build" passes.

## Output Format

The HTML guide, in this order:

1. **Header strip** — a small table: time estimate, exercise count, products used, and **what access the reader
   must already have**. "You need" means entitlements and permissions that can block them (environment, licence,
   role) — never audience notes like "no prior experience", which cannot block anyone and waste the column
2. **The scenario** — the business problem in two or three sentences, then what the finished agent does
3. **What you will be able to do** — 5-8 capability statements, each an ability gained ("diagnose why the agent
   is not finding what you expect"), never a topic covered
4. **Before you start** — split in two: **access and licensing** (the environment, the licences, the security
   role) and **content and test material**. Name the *specific* entitlements, not a general "access to the
   product": tenant-level access and access inside a given environment are different things, and conflating
   them strands people on the day. Say which exercise each item blocks, and give a fallback where one exists
5. **Exercises**, in build order, each with:
   - **Goal** — one sentence
   - **Steps** — numbered, each starting with a UI verb, naming the page and control
   - **Enter this** — copy blocks holding the literal text: agent description, instruction text, knowledge source
     names and descriptions, tool names and descriptions
   - **Check it worked** — what appears on screen
   - **If it didn't** — likeliest cause and fix, where the failure is likely and fixable
6. **What you built** — a checklist restating each capability as something the participant *observed*, plus the
   instruction to return to the exercise that produced any line that is not true
7. **Settings reference** — setting, where it lives, recommended value, what the other value does. This is where
   recommendations belong, so the exercises stay imperative
8. **Test prompts** — 5-8 to run against the finished agent, at least two the agent should refuse
9. **Before you share it** — auth, data boundary, admin dependencies, monitoring, publish sequence
10. **Decisions required before build** — what the owning organization must confirm (data scope, connectors,
   approved recipients, publishing permissions, review owner). Not harness or licensing choices.
11. **Sources** — a two-column table: which exercise used it, and the page as a **live hyperlink** plus the bare
   URL in visible text (printed handouts lose the anchor). Titled by topic rather than by harness. Never a bare
   list of page titles — a reader whose screen doesn't match needs the authoritative page in one click.
12. **Where to go next** — link Copilot Studio Agent Academy (https://microsoft.github.io/agent-academy/) with a
   one-line description of Recruit and Special Ops, and the caveat that it supplies no environments or licenses

There is no harness section. The harness decision lives in the chat reply.

**Copy blocks carry only what the participant pastes into Copilot Studio** — instruction text, descriptions,
prompts. Never put UI navigation inside a copy block.

Mark anything unverified as **[Verify]**. Use placeholders like `[Customer to confirm]` — never invent tenant
details, limits, license entitlements, or numbers.

## Guardrails

- Ground every product claim in a fetched Microsoft Learn page; no memory-sourced specifics.
- Do not fabricate customer names, data sources, connector availability, or licensing.
- Recommend one harness in chat; do not hedge across all three.
- Never let harness names, comparisons, convertibility warnings, or credit-consumption notes reach the guide;
  a `harness` or `credit` hit in the rendered file is a blocking defect, not a wording preference.
- Every lab step is an action a participant performs, not a decision they must make. Recommendations live in the
  settings reference; steps stay imperative.
- Never ship a lab without a "Check it worked", and never tell a participant to write text the guide could have
  supplied.
- Never write a step that assumes an empty field. Where the product has already populated something — generated
  instructions, a default topic, a suggested source — say so, say whether to replace or keep it, and say why.
- Every source is a clickable link with its URL also visible as text. A source list without URLs is a dead end.
- **Assume a shared environment.** Multiple participants build in the same Power Platform environment, so never
  instruct a step that changes environment-wide or account-level defaults (preferred solution being the main
  one). Prefer per-object placement, and name objects with the participant's own initials so shared lists stay
  navigable.
- Never create, modify, or publish a live agent — this skill produces guidance only.
- Include the security/prompt-injection and authentication items in every guide, even short ones.
- The artifact never references the conversation, the requester, the delivery team, or how it was produced.
  Ship a document, not a transcript.
