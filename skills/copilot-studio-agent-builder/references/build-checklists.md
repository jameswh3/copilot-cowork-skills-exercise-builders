# Build checklists

Doc-grounded baseline (Microsoft Learn, pages last updated 2026). Re-verify before publishing a guide.

Source pages:
- Write agent instructions — https://learn.microsoft.com/en-us/microsoft-copilot-studio/authoring-instructions
- High-quality instructions for generative orchestration — https://learn.microsoft.com/en-us/microsoft-copilot-studio/guidance/generative-mode-guidance
- Knowledge sources summary — https://learn.microsoft.com/en-us/microsoft-copilot-studio/knowledge-copilot-studio
- Add tools to custom agents — https://learn.microsoft.com/en-us/microsoft-copilot-studio/add-tools-custom-agent
- Skills overview (GitHub Copilot harness) — https://learn.microsoft.com/en-us/microsoft-copilot-studio/agents-experience/skills-overview
- Knowledge for GitHub Copilot harness agents — https://learn.microsoft.com/en-us/microsoft-copilot-studio/agents-experience/knowledge-add-existing-copilot
- Publish and deploy your agent — https://learn.microsoft.com/en-us/microsoft-copilot-studio/publication-fundamentals-publish-channels

## 0. Solution (do this before creating the agent)

Source: https://learn.microsoft.com/en-us/microsoft-copilot-studio/authoring-solutions-overview

- [ ] Confirm the security role allows solution management — solution explorer inherits Power Apps privileges (Environment Maker, System Customizer, or System Administrator)
- [ ] Solution explorer: three dots on the side bar, then Solutions
- [ ] New solution; create or select a publisher (the prefix keeps components from different teams distinct)
- [ ] Name the solution for the agent, not the project
- [ ] **Do NOT set a preferred solution** — it redirects where new components are created account-wide and collides when several people share an environment. Create the agent from inside the solution instead
- [ ] Include the participant's name or initials in the solution name; the environment's solution list is shared

## 1. Create

- [ ] Confirm environment, maker permissions, and licensing path
- [ ] Choose the harness deliberately — it can't be changed later
- [ ] Name and describe the agent for its audience; describe it in natural language so generated instructions start close to intent
- [ ] Keep it to a single agent — if the scope needs a second agent, cut the scope instead and log it as a later phase

## 2. Instructions

- [ ] Keep them short and simple; number or bullet ordered steps; Markdown is fine
- [ ] Only instruct behavior the agent can actually perform — instructions can't use tools or knowledge you haven't added
- [ ] Reference specific tools/topics/knowledge with `/` and use the exact object name
- [ ] Add scope guardrails ("only respond to X; otherwise say you can't help")
- [ ] Specify response format where it matters (tables, rich-text email bodies)
- [ ] Skip tone instructions unless the scenario needs a non-default tone
- [ ] **Do not** write instructions that alter citations/references, retrieval logic, Adaptive Card triggering, or the fallback message — use the fallback topic and card config instead
- [ ] Avoid vague UI terms; they cause unpredictable behavior
- [ ] Debug technique: strip instructions, add them back one at a time, test between each

## 3. Knowledge

- [ ] Map each user question type to a source: public website, uploaded documents, SharePoint, Dataverse, connectors (GitHub Copilot harness adds Azure AI Search, Dynamics 365, Salesforce, ServiceNow, Azure SQL in the Add knowledge dialog)
- [ ] Note the source authentication model — SharePoint, Dataverse, and connector sources honor the end user's Entra ID permissions, so users only see what they can already access
- [ ] **Web knowledge — two distinct controls:**
  - *Public website* knowledge source: searches Bing but returns results **only from the URLs you list** (generative mode: up to 25 websites; classic: four public URLs)
  - *Web Search / "Use information from the web"* (Generative AI settings and the Overview page Knowledge section): searches **all** public sites Bing indexes, in parallel with your listed sites, results interleaved; requires generative orchestration; uses Grounding with Bing Search
  - Recommend the default explicitly and state the data-boundary consequence
- [ ] Leave **Allow ungrounded responses** at its default and keep it out of the guide entirely — turning it off makes correct answers disappear intermittently (an answer returns only when it carries a citation, and models omit citations unpredictably). Force grounding with instruction text instead
- [ ] Consider **Tenant graph grounding with semantic search** for SharePoint-heavy agents (requires Authenticate with Microsoft; extra cost; small latency increase)
- [ ] Set content moderation level (default High; topic-level overrides agent-level at runtime)
- [ ] Give every knowledge source an accurate, specific description — generative orchestration filters sources by description when there are many
- [ ] Note channel citation limits (Teams caps citations and truncates titles/snippets; customized answers don't get automatic citations)

## 4. Tools

- [ ] Start from the default shape: **send an email** (Office 365 Outlook connector) and/or **an agent flow** for a multi-step action; add prompt, REST API, MCP server, custom connector, or computer use only when the scenario requires it
- [ ] Write name + description as routing logic — the orchestrator selects on them; add "when not to use this" wording if it fires wrongly
- [ ] Decide per tool: let the agent choose dynamically vs. call only from a topic
- [ ] Decide per tool: **Ask the end user before running** (off by default) — turn it on for consequential actions
- [ ] Choose authentication: end-user credentials (per-user permissions) vs. maker-provided (shared identity)
- [ ] Review inputs — default is dynamic AI fill; override with fixed values or Power Fx where correctness matters
- [ ] Choose completion behavior (don't respond / generative response / specific response / adaptive card)
- [ ] Keep the tool set small — the orchestrator supports many tools (up to 128) but roughly 25-30 per agent is the practical recommendation; for a single-agent design, aim far lower and narrow the scope instead of adding tools
- [ ] For a send-email tool: constrain allowed recipients in the instructions, request rich-text body formatting, and consider requiring end-user confirmation before it runs
- [ ] GitHub Copilot harness only: consider **skills** (Markdown SKILL.md + optional supporting files, portable/shareable) for reusable task behaviors, and **memory** for cross-interaction context

## 5. Test

- [ ] Test in the test pane while building; for GitHub Copilot harness use the Preview tab and the Evaluate tab test sets
- [ ] Write prompts for: happy path, ambiguous routing between two tools, missing input, out-of-scope refusal, and a prompt-injection attempt
- [ ] Test trigger payloads for triggered/autonomous agents
- [ ] Test as a non-maker user to validate permission-trimmed knowledge
- [ ] Re-test after every instruction change

## 6. Publish

- [ ] Publish before anyone can use it; republish after every change
- [ ] Agent authentication defaults to Authenticate with Microsoft — leave it, and keep it out of the lab steps (settings reference only). "No authentication" means the agent can't use tools with user credentials and anyone with the link can chat
- [ ] Add channels only after the first publish; channel availability can be restricted by admins
- [ ] Roll out to yourself → small group → org catalog; the demo website is for stakeholder feedback, not production
- [ ] For agents for Microsoft 365 Copilot: publishing populates the org catalog entry and may require admin approval; distribution is via share link, teammates, org-wide submission, or a downloaded .zip
- [ ] Expect a delay before published changes reach existing sessions

## 7. Govern & monitor

- [ ] Confirm the data boundary the agent creates (who can reach what through it)
- [ ] Harden against prompt injection from untrusted content: constrain which tools may run after reading a source, and constrain tool parameters (e.g., allowed recipients)
- [ ] Set up analytics/monitoring review cadence and a feedback path for wrong answers
- [ ] Define the owner, change process, and re-test trigger for knowledge updates
- [ ] Record known limitations for users (attachments, multilingual behavior, channel rendering differences)
