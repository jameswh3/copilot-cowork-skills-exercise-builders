# Build checklists

Two checklists: the participant-facing **Prerequisites + pre-flight checklist** that every handout carries, and the
**coverage checklist** the author uses to confirm each exercise is complete. Facts come from
[fabric-grounding.md](fabric-grounding.md); re-verify before publishing.

## Participant-facing Prerequisites section (template)

Render as its own clearly called-out section before Lab Setup, with the heading **Prerequisites**, followed by
**Pre-flight checklist**. Say which exercise each item blocks. References go once, at the end of the handout.

**Prerequisites**

| You need | Why | Blocks |
|---|---|---|
| A workspace on a paid Fabric capacity (F2 or higher) or Power BI Premium per capacity (P1 or higher) with Microsoft Fabric enabled. A Fabric trial capacity does not support the data agent. | The data agent runs only on supported capacity | Lab Setup and all exercises |
| Tenant setting *Users can use Copilot and other features powered by Azure OpenAI* enabled (tenant or capacity level) | Powers the data agent | Exercise 1 onward |
| Tenant setting *Capacities can be designated as Fabric Copilot capacities* enabled | Required by the data agent | Exercise 1 onward |
| If your capacity region is outside the US and the EU data boundary: the two cross-geo settings for processing and storing data sent to Azure OpenAI | Required in those regions | Exercise 1 onward |
| [Only if Learn lists one at build time: the named data agent tenant switch] | | |
| Workspace role Contributor or higher | Create the lakehouse, notebook, and data agent | Lab Setup and all exercises |
| Read access to each data source you add | The agent queries under your identity | Exercise 1 onward |

One statement follows the table (the only one; do not add statements about what is not required or product limits):
- Tenant settings are changed by a Fabric administrator at OneLake catalog > Govern > Configurations > Tenant
  settings and can take up to one hour to take effect.

**Pre-flight checklist** (tick each before Lab Setup; only checks that are not already a Prerequisites row)
- [ ] In my workspace, **+ New item** lists **Fabric data agent**.
- [ ] The lab files are saved in one folder on my computer, and none are open in Excel or another app: the CSV files
      [and the workbook] and the notebook. (An open CSV is locked by Excel and can fail to upload.) Write only the
      first sentence in the handout.

**References:** (end of the handout only)
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
- [ ] Workspace, lakehouse, upload, import, attach default lakehouse, run once, show where a schedule is configured
      (none created), SQL analytics endpoint check
- [ ] Data agent created via + New item > Fabric data agent; lakehouse added from OneLake catalog; tables checked
- [ ] Before/after prompt with both values computed by code
- [ ] Data agent instructions (character count shown to author, under 15,000) and data source instructions supplied
      literally
- [ ] 3-6 example queries, each validated by the generator against the schema
- [ ] 6-10 test prompts incl. two out of scope; every one has "What good looks like" with computed values
- [ ] Steps dropdown / generated SQL inspection step present
- [ ] Publish with the supplied description; draft vs published explained in one sentence; Share step
- [ ] Optional: Microsoft Copilot / Copilot Studio consumption (for Microsoft Copilot: Publish to Agent Store, then @mention the agent; no data-handling statement unless asked)
- [ ] Optional advanced exercises only if requested or the timebox allows: second source (warehouse or semantic
      model; semantic models take no example queries and need only Read), diagnostics, Git integration / deployment pipelines
- [ ] Every exercise has Steps; Enter this and Check it worked only where they add something; nothing is said twice
