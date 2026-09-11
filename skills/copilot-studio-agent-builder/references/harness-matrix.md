# Harness selection matrix

Baseline verified against Microsoft Learn (pages last updated Aug 2026). **Re-verify before use** — see the
Hard Grounding Rule in SKILL.md.

Source pages:
- Agents overview — https://learn.microsoft.com/en-us/microsoft-copilot-studio/agents-overview
- Harnesses in Copilot Studio — https://learn.microsoft.com/en-us/microsoft-copilot-studio/harnesses-overview
- GitHub Copilot harness overview — https://learn.microsoft.com/en-us/microsoft-copilot-studio/agents-experience/overview
- Extend M365 Copilot with the Copilot chat harness — https://learn.microsoft.com/en-us/microsoft-copilot-studio/microsoft-365-copilot-extend-with-agents

## What a harness is

The harness is the runtime between your agent design and the model: it decides when to call the model, what to
send it, how to interpret the result, and which tools to call. Everything built in Copilot Studio runs on one of
three harnesses, and the harness affects billing, features, and capabilities.

## Comparison

| Consideration | GitHub Copilot harness | Standard harness | Copilot chat harness |
|---|---|---|---|
| Best for | Complex, multi-step business processes | Rule-based agents, structured conversations | Extending M365 Copilot Chat with org knowledge |
| How it works | Reasons through a goal step by step; breaks goals into steps and adapts | Follows the topics and rules you define | Connects enterprise knowledge to M365 Copilot Chat |
| Error recovery | Retries and finds alternative paths automatically | Follows the paths you built | Not a focus |
| Files | Natively creates/edits/reasons over Word, Excel, PowerPoint, PDF | Not a focus | Not a focus |
| Skills & memory | Yes (native) | Not a focus | Not a focus |
| Authoring style | Natural-language-first, single Build tab (Instructions, Knowledge, Tools & skills, Model, Memory; connected agents also live here but are out of scope for this skill) | Topics, trigger phrases, branching flows, generative or classic orchestration | Instructions + knowledge + capabilities + suggested prompts |
| Orchestration | Enhanced orchestration for all agents; not configurable | Generative orchestration (default) or classic | M365 Copilot chat models |
| Publishing | Internal teams or external customers | Internal teams or external customers | Internal teams |
| Billing | Copilot Credits (usage-based, including building/testing/evaluating) | Copilot Studio capacity model | Consumption-based or included in an M365 Copilot license |

## Decision shortcuts

- Needs judgment across several steps, files, or many tools → **GitHub Copilot harness**
- Needs the same answer every time on a well-understood question set → **standard harness**
- Goal is grounded answers inside M365 Copilot Chat and nothing more → **Copilot chat harness**

## Non-negotiable warnings

- **Not convertible.** Agents created on the GitHub Copilot harness can't be transferred to the standard
  harness, or vice versa. The harness is chosen at creation.
- **Building costs money on the GitHub Copilot harness.** Using, building, testing, and evaluating can consume
  Copilot Credits — factor this into workshop and pilot planning.
- **Two different M365 Copilot paths.** A *custom agent* published to the Teams + Microsoft 365 channel is not
  the same as an *agent for Microsoft 365 Copilot* (a declarative agent authored from the Microsoft 365 Copilot
  page). The latter is not automatically deployed on publish — it goes to availability options / the org
  catalog, and an admin may gate it.
