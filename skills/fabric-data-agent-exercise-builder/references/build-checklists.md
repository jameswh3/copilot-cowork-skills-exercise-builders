# Build checklists

Two checklists: the participant-facing **Prerequisites + pre-flight checklist** that every handout carries, and the
**coverage checklist** the author uses to confirm each exercise is complete. Facts come from
[fabric-grounding.md](fabric-grounding.md); re-verify before publishing.

## Participant-facing Prerequisites section (template)

Render as its own clearly called-out section before Exercise 1, with the heading **Prerequisites**, followed by
**Pre-flight checklist**, then **References:**. Say which exercise each item blocks.

**Prerequisites**

| You need | Why | Blocks |
|---|---|---|
| A workspace on a paid Fabric capacity (F2 or higher) or Power BI Premium per capacity (P1 or higher) with Microsoft Fabric enabled. A Fabric trial capacity does not support the data agent. | The data agent runs only on supported capacity | Exercises 1-12 |
| Tenant setting *Users can use Copilot and other features powered by Azure OpenAI* enabled (tenant or capacity level) | Powers the data agent | Exercise 6 onward |
| Tenant setting *Capacities can be designated as Fabric Copilot capacities* enabled | Required by the data agent | Exercise 6 onward |
| If your capacity region is outside the US and the EU data boundary: the two cross-geo settings for processing and storing data sent to Azure OpenAI | Required in those regions | Exercise 6 onward |
| [Only if Learn lists one at build time: the named data agent tenant switch] | | |
| Workspace role Contributor or higher | Create the lakehouse, notebook, schedule, and data agent | Exercises 1-12 |
| Read access to each data source you add | The agent queries under your identity | Exercise 6 onward |
| The content pack downloaded and unzipped on your computer | Files to upload and the notebook to import | Exercises 2-3 |

Plain statements that follow the table (participant-facing, not editorial):
- Tenant settings are changed by a Fabric administrator at OneLake catalog > Govern > Configurations > Tenant
  settings and can take up to one hour to take effect.
- No Azure OpenAI key or token is required. Fabric handles authentication, and the agent's queries run under your
  Microsoft Entra ID identity and permissions.
- An agent can use up to five data sources. Its queries are read-only.

**Pre-flight checklist** (tick each before Exercise 1)
- [ ] I can open my workspace and its license shows a paid Fabric or Premium capacity.
- [ ] In my workspace, **+ New item** lists **Fabric data agent**.
- [ ] My role in the workspace is Contributor, Member, or Admin.
- [ ] I have the content pack folder open: the CSV files [and the workbook] and the notebook.
- [ ] I know the folder name the notebook expects (shown in the notebook's parameters cell).

**References:**
- https://learn.microsoft.com/en-us/fabric/data-science/how-to-create-data-agent
- https://learn.microsoft.com/en-us/fabric/data-science/data-agent-tenant-settings
- https://learn.microsoft.com/en-us/fabric/data-science/concept-data-agent
- https://learn.microsoft.com/en-us/fabric/fundamentals/job-scheduler

Each reference is a live hyperlink with the full URL visible as text.

## Coverage checklist (author, per build)

### Data and notebook
- [ ] Spec written; `generate_synthetic_data.py --check` exits 0 (no orphan keys, every answer and example query runs)
- [ ] Table and column names are descriptive business names (`work_orders.opened_date`, not `wo.dt1`)
- [ ] 3-5 traps from the trap menu, each handled by a named instruction line or example query
- [ ] CSVs written; optional single workbook written; no `.txt` / `.md` data files; any document is `.docx` in Aptos
- [ ] `build_ingest_notebook.py` run from the same manifest; parameters cell folder equals the upload folder in the guide
- [ ] Authoring files (`manifest.json`, `expected_answers.json`) kept out of the participant package

### Exercises
- [ ] Prerequisites section + pre-flight checklist + References: present and re-verified today
- [ ] Workspace, lakehouse, upload, import, attach default lakehouse, run once, schedule, Monitor / Recent runs, SQL
      analytics endpoint check
- [ ] Data agent created via + New item > Fabric data agent; lakehouse added from OneLake catalog; tables checked
- [ ] Before/after prompt with both values computed by code
- [ ] Data agent instructions (character count shown to author, under 15,000) and data source instructions supplied
      literally
- [ ] 3-6 example queries, each validated by the generator against the schema
- [ ] 6-10 test prompts incl. two out of scope; every one has "What good looks like" with computed values
- [ ] Steps dropdown / generated SQL inspection step present
- [ ] Publish with the supplied description; draft vs published explained in one sentence; Share step
- [ ] Optional: Microsoft 365 Copilot / Copilot Studio consumption with the service boundary stated plainly
- [ ] Optional advanced exercises only if requested or the timebox allows: second source (warehouse or semantic
      model; semantic models take no example queries and need only Read), Refresh after the scheduled run,
      diagnostics, Git integration / deployment pipelines
- [ ] Every exercise has Goal, Steps, Enter this, Check it worked
