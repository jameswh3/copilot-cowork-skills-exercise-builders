# Fabric data agent grounding baseline

Baseline verified against Microsoft Learn on 2026-10-22. **Re-verify at build time** with `web_fetch` (see the Hard
Grounding Rule in SKILL.md). Treat any line older than the current quarter as needing a re-check, and mark a detail
you could not re-verify as **[Verify]** in the handout rather than guessing.

## Source pages (cite these under "References:")

| Topic | URL | Learn "last updated" at baseline |
|---|---|---|
| Create a Fabric data agent | https://learn.microsoft.com/en-us/fabric/data-science/how-to-create-data-agent | 2026-05-20 |
| Data agent tenant settings | https://learn.microsoft.com/en-us/fabric/data-science/data-agent-tenant-settings | 2026-09-28 |
| Data agent concepts (limits, how it works) | https://learn.microsoft.com/en-us/fabric/data-science/concept-data-agent | 2026-05-11 |
| Job scheduler (schedule a notebook) | https://learn.microsoft.com/en-us/fabric/fundamentals/job-scheduler | re-check |
| Develop and run notebooks (parameters cell) | https://learn.microsoft.com/en-us/fabric/data-engineering/author-execute-notebook | 2026-08-07 |
| How to use notebooks (import, default lakehouse, run identity) | https://learn.microsoft.com/en-us/fabric/data-engineering/how-to-use-notebook | 2026-04-24 |
| Notebook activity in a pipeline | https://learn.microsoft.com/en-us/fabric/data-factory/notebook-activity | re-check |
| Features by SKU (trial support) | https://learn.microsoft.com/en-us/fabric/enterprise/fabric-features | 2026-06-30 |
| Consume a data agent from Microsoft Copilot (preview) | https://learn.microsoft.com/en-us/fabric/data-science/data-agent-microsoft-365-copilot | re-check |

## Prerequisites (participant-facing, verified)

- **Capacity:** a paid F2 or higher Fabric capacity, or Power BI Premium per capacity (P1 or higher) with Microsoft
  Fabric enabled.
- **Trial capacity:** the Features by SKU page lists Fabric data agent for F and P SKUs and states that, unless
  noted, a trial capacity does not support the listed features; the data agent row carries no trial footnote. State
  plainly: *a Fabric trial capacity does not support the data agent; use a paid F2+ or P1+ capacity.* Re-check this
  at every build, since it is the line most likely to change.
- **Tenant settings** (admin; Fabric > OneLake catalog > Govern > Configurations > Tenant settings; changes can take
  up to one hour to take effect):
  - *Users can use Copilot and other features powered by Azure OpenAI* (manageable at tenant and capacity level).
  - *Capacities can be designated as Fabric Copilot capacities.*
  - *Data sent to Azure OpenAI can be processed outside your capacity's geographic region, compliance boundary, or
    national cloud instance* and *Data sent to Azure OpenAI can be stored outside your capacity's geographic region,
    compliance boundary, or national cloud instance*: required only when the capacity region is outside the EU data
    boundary and the US.
  - **Dedicated data agent switch:** the tenant settings page as of 2026-09-28 lists no separate data agent switch;
    the data agent is governed by the Copilot and Azure OpenAI settings above. Older material names a switch such as
    "Users can create and share Fabric data agent item types". Re-check the page; include a named switch only if the
    page lists it at build time.
- **Workspace role:** Contributor or higher to create the lakehouse, notebook, schedule, and data agent (the job
  scheduler requires at least Contributor, or Write on the item, to create or edit a schedule).
- **Data access:** read access to every data source added to the agent. A Power BI semantic model needs only Read
  permission on the model (no Build, no workspace role); Write is needed only to modify the model or use Prep for AI.
- **No keys:** no Azure OpenAI key or access token is needed. Fabric uses a Microsoft-managed Azure OpenAI Assistant
  and handles authentication. Queries run under the user's Microsoft Entra ID identity and workspace/data permissions.
- **Region:** the agent can't query a source whose workspace capacity is in a different region from the agent's
  workspace capacity.
- **Language:** questions, instructions, and example queries in English.

## Product facts the exercises depend on

- Up to **five data sources** per agent, any combination of lakehouse, warehouse, Power BI semantic model, KQL
  database, ontology, Microsoft Graph. Each is added individually from the OneLake catalog.
- Lakehouse sources answer from **tables**, not Files. CSVs must be ingested into tables first (the notebook does
  this). Unstructured files (.pdf, .docx, .txt) are not supported as data.
- Explorer checkboxes control which tables are available to the AI; selecting a parent selects all children.
- **Descriptive table and column names** materially improve query generation (Learn: `SalesData` over `TableA`,
  `IsCustomerActive` over `C1`).
- **Data agent instructions:** up to 15,000 characters of plain English; use them for routing between sources and for
  defining business terms, acronyms, and jargon.
- **Data source instructions:** per-source guidance on tables, joins, filters, and value conventions. [Verify the
  current UI label and location at build time.]
- **Example queries:** question/SQL (or KQL) pairs per source; up to 100 per source. The agent only uses examples
  whose SQL/KQL is **valid and matches the schema of the selected tables**; it ignores examples that have not passed
  validation. Power BI semantic models and ontologies do not support example queries.
- **Read-only:** the agent generates only read queries; no create, update, or delete.
- **Out of scope:** causal or "why" questions ("Why is productivity lower in Q2?", "What is the root cause of the
  spike?"). The agent does not perform advanced analytics, machine learning, or causal inference.
- **Response cap:** responses are capped at 25 rows and 25 columns; earlier chat turns influence later answers, so
  start a new chat (Clear chat) before a fresh test.
- **Transparency:** each answer has a steps dropdown showing the steps and the generated query.
- **Refresh:** in Explorer, hover a source > three dots > Refresh to resync after the source changes; Remove is in the
  same menu.
- **Publish:** Publish asks for a description; write a detailed one, since colleagues and other orchestrators use it
  to decide when to invoke the agent. Publishing creates a **draft** version (keep editing) and a **published**
  version (shared).
- **Share:** recipients need access to the agent and to the underlying data sources.
- **Consumption:** Microsoft 365 Copilot (preview at baseline), Copilot Studio, Microsoft Foundry, or as an MCP
  server. Service boundary, stated plainly: when the agent is consumed from one of these services, that service
  processes and stores the returned responses under its own terms and data handling policies.
- **ALM:** diagnostics, Git integration (instructions, example queries, data source selections), deployment pipelines.
- **Governance:** Purview DLP and access restriction policies can block or truncate results; interactions can be
  audited.

## Notebook and scheduling facts

- Import: workspace toolbar > Import > Notebook > From this computer; Fabric accepts standard `.ipynb`. [Verify the
  exact menu labels.]
- Default lakehouse: in the notebook's Lakehouse explorer, add the lakehouse and pin it as default; restart the
  session after pinning a new default. Relative paths like `Files/<folder>/<file>.csv` resolve against it.
- Parameters cell: cell toolbar ... > **Toggle parameter cell**. A pipeline Notebook activity overrides its values
  under Settings > Base parameters. Scheduled runs don't support parameterized session configuration.
- Run identity: an interactive run uses the current user; a scheduled run uses the identity of the user who created
  or last updated the schedule; a pipeline run uses the pipeline's last modified user.
- Schedule: from the notebook (Run tab > **Schedule** [Verify]) or the item's contextual menu > **Schedule**
  (verified). Configure on/off, repeat frequency, time, start and end date, and time zone; optionally add Failure
  notifications (scheduled runs only). Multiple schedules per item are supported.
- Monitor: the **Monitor** hub lists runs; the item's ... menu > **Recent runs** shows its history. [Verify labels.]
- `mssparkutils.notebook.exit(value)` returns an exit value that pipelines can read. `notebookutils` is the newer
  name for the same utilities; `mssparkutils` remains supported. [Verify at build time.]
- Pipeline alternative: Data pipeline > Notebook activity > Settings: select the workspace and notebook, set Base
  parameters, then Home > Schedule.
