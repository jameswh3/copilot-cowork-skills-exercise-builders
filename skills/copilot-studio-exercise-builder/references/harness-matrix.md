# Harness selection matrix

Baseline verified against Microsoft Learn (verified 2026-11-18). **Re-verify before use** — see the
Hard Grounding Rule in SKILL.md.

Source pages:
- Agents overview — https://learn.microsoft.com/en-us/microsoft-copilot-studio/agents-overview
- Harnesses in Copilot Studio — https://learn.microsoft.com/en-us/microsoft-copilot-studio/harnesses-overview
- Microsoft Copilot harness overview — https://learn.microsoft.com/en-us/microsoft-copilot-studio/agents-experience/overview
- Extend Microsoft Copilot with the Copilot chat harness — https://learn.microsoft.com/en-us/microsoft-copilot-studio/microsoft-365-copilot-extend-with-agents

## What a harness is

The harness is the runtime between your agent design and the model: it decides when to call the model, what to
send it, how to interpret the result, and which tools to call. Everything built in Copilot Studio runs on one of
three harnesses, and the harness affects billing, features, and capabilities.

## Comparison

| Consideration | Microsoft Copilot harness | Customer Conversation harness (preview) | Standard harness |
|---|---|---|---|
| Best for | Complex, multi-step business processes | Customer-facing, contact-center-style scenarios over voice and chat | Rule-based agents, structured conversations |
| How it works | Reasons through a goal step by step; breaks goals into steps and adapts | Multi-agent architecture with specialized sub-agents that can escalate to a human representative | Follows the topics and rules you define |
| Error recovery | Retries and finds alternative paths automatically | Escalates to a human representative through a defined path | Follows the paths you built |
| Files | Natively creates/edits/reasons over Word, Excel, PowerPoint, PDF | Not a focus | Not a focus |
| Skills & memory | Yes (native) | Yes | Not a focus |
| Authoring style | Natural-language-first; tabs Build, Preview, Evaluate, Monitor. Build components: Instructions, Knowledge, Tools, Skills, Model, Connected agents (out of scope for this skill), Memory | [Verify] | Instructions, knowledge, tools, and topics for wording that must not vary; generative orchestration by default |
| Orchestration | Enhanced orchestration for all agents; not configurable | [Verify] | Generative orchestration (default) or classic |
| Publishing | Internal teams or external customers | Website chat or a phone number | Internal teams or external customers |
| Billing | Copilot Credits (usage-based) | Copilot Credits (usage-based) | Licensing for agents powered by the standard harness |

Billing source: Harnesses in Copilot Studio. Whether building, testing and evaluating also consume Copilot
Credits on the Microsoft Copilot harness is **[Verify]** — not stated on that page.

**Agents for Microsoft Copilot (declarative agents)** run on the Copilot chat harness, authored from the
Microsoft Copilot page: instructions, knowledge, capabilities and suggested prompts, published to internal teams.
Use this path only when the goal is grounded answers inside Microsoft Copilot Chat and nothing more.

## Computation and files

| | Microsoft Copilot harness | Standard harness |
|---|---|---|
| Exact computation over data | **Code interpreter, native**: each task runs in a secure sandbox (isolated Linux/Python workspace) governed by Copilot Studio, no single-file limit, multi-turn. pandas/numpy/matplotlib/openpyxl preinstalled. Used automatically when a task needs exact computation, parsing, validation or file creation. No outbound internet | **Code interpreter, opt-in**: one file per prompt, no multi-turn, no system commands, timeouts on large datasets, admin-enabled per environment, not callable from a topic |
| Generated artifacts | Charts, Word/Excel/PowerPoint/PDF, cleaned datasets, images | Not a focus |

This is the single biggest practical difference for any scenario involving numbers or files, and it is the one
most often got wrong in guidance written before the Microsoft Copilot harness went GA (Aug 3, 2026).

## Decision shortcuts

- Needs judgment across several steps, files, or many tools → **Microsoft Copilot harness**
- Customer-facing over website chat or phone, with escalation to a human → **Customer Conversation harness (preview)**
- Needs the same answer every time on a well-understood question set → **standard harness**
- Goal is grounded answers inside Microsoft Copilot Chat and nothing more → **agent for Microsoft Copilot** (Copilot chat harness)

Note on the standard harness: generative orchestration is the default there too. A topic gives you authored
wording, not authored routing — the agent still selects the topic from its name and trigger description. Trigger
phrases belong to classic orchestration and only appear once orchestration is turned off.

On the Microsoft Copilot harness, prompts are replaced by **skills**, and topics and system triggers are replaced
by **hooks**.

Do **not** decide on authoring style. Topics are a standard-harness technique, not a reason to choose it:
migration guidance translates authored conversational paths into instructions and skills. Decide on how much of
the path is mappable before runtime, volume and billing model, and whether the work needs files or computation.

## Non-negotiable warnings

- **One-way only.** Agents can't move from the Microsoft Copilot harness back to the standard harness. Copilot
  Studio can create a Microsoft Copilot harness agent from a standard agent with **Upgrade (preview)**. Choose
  the harness at creation.
- **Billing.** Microsoft Copilot harness agents use Copilot Credits — factor this into workshop and pilot
  planning (credit use while building, testing and evaluating: [Verify]).
- **Two different Microsoft Copilot paths.** A *custom agent* published to the Teams + Microsoft 365 channel is not
  the same as an *agent for Microsoft Copilot* (a declarative agent authored from the Microsoft Copilot
  page). The latter is not automatically deployed on publish — it goes to availability options / the org
  catalog, and an admin may gate it.
