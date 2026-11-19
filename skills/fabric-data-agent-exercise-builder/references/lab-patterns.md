# Lab patterns: click paths, copy-ready text, and test design

Facts and URLs live in [fabric-grounding.md](fabric-grounding.md). This file says *how to write them as steps*.
Anything marked [Verify] must be re-checked against Learn before it ships; if it still can't be verified, keep the
[Verify] marker in the handout.

## The step shape (every exercise)

- **Title** - carries the goal (business task, product in parentheses). No separate Goal line.
- **Steps** - numbered; each starts with a UI verb (Select, Open, Paste, Enter, Upload, Run) and names the page and
  control. Never "decide", "consider", "ensure", "review", "make sure".
- **Enter this** - copy blocks holding only literal text the participant pastes: agent instructions, data source
  instructions, example question + SQL, test prompts, publish description, names to enter. Never UI
  navigation inside a copy block.
- **Check it worked** - what appears on screen (table names in Explorer, the notebook's row counts, the generated SQL
  in the steps dropdown, the exact expected number). Omit it when it would only restate a step or point to What good
  looks like.

No "If it didn't", "If it stalls", wait-time, or troubleshooting blocks. Factual prerequisites stay.

## Exercise sequence (dependency order)

**Lab Setup** (stands up a lakehouse that mirrors the customer's production lakehouse; not part of the story and not
counted as exercises; see "Lab setup vs. the story" in SKILL.md):

| # | Setup step | Ends with on screen |
|---|---|---|
| S1 | Open your workspace and create the lakehouse | Empty lakehouse with Tables and Files |
| S2 | Upload the lab files to Files | CSVs listed under Files/<folder> |
| S3 | Import the notebook, attach the lakehouse, run it once | Exit value shows `succeeded`; tables listed under Tables |
| S4 | See where a notebook schedule is configured (do not create one) | Scheduler panel opened, then closed with the schedule off |
| S5 | Verify the tables in the SQL analytics endpoint | Row counts match the expected counts |

**Exercises** (the story; they start from the lakehouse as if it were production):

| # | Exercise | Ends with on screen |
|---|---|---|
| 1 | Create the data agent and add the lakehouse | Agent opens with lakehouse in Explorer; tables checked |
| 2 | Ask a baseline question (before instructions) | Baseline answer and its SQL recorded |
| 3 | Add data agent instructions and data source instructions | Same question returns the defined answer |
| 4 | Add example queries | Examples validate; matched question reuses the logic |
| 5 | Test in-scope and out-of-scope prompts | Each answer matches "What good looks like" |
| 6 | Publish and share | Published version exists; description visible |
| 7 | Optional: consume from Microsoft Copilot (Publish to Agent Store, then @mention the agent) or Copilot Studio | Agent answers from the other surface |
| A1-A3 | Optional advanced: second source, diagnostics, Git / deployment pipelines | Per exercise |

Prerequisites and the pre-flight checklist come before Lab Setup. Exercises 2 and 3 together are the **before/after test**: the same prompt, asked before and after instructions,
with the two different expected values computed from the data.

## Verified click paths (re-check at build time)

### Workspace and lakehouse
1. Open Fabric and select **Workspaces** in the left rail; open a workspace assigned to a paid Fabric capacity (or
   select **+ New workspace**, name it, and under Advanced choose a Fabric capacity license mode [Verify]).
2. Select **+ New item**, search **Lakehouse**, select it, enter the lakehouse name, select **Create**.

### Upload files
1. In the lakehouse explorer, select **Files** > **...** > **New subfolder**; enter the folder name from the notebook
   parameters cell (for example `maintenance_export`) [Verify].
2. Select the folder > **...** > **Upload** > **Upload files**; select every CSV from the content pack; select
   **Upload** [Verify]. The pre-flight checklist has already had participants close the files in Excel; do not
   repeat it here.
Check it worked: each CSV is listed in the folder. The participant does not use "Load to Tables"; the notebook owns
ingestion.

### Import, attach, run
The notebook ships as a standard `.ipynb` and is imported in the browser. Never require VS Code or any local tool,
and never ask participants to copy and paste notebook code; the workspace import supports `.ipynb` directly.
1. In the workspace toolbar, select **Import** > **Notebook** > **From this computer**, select the `.ipynb`, select
   **Upload**.
2. Open the notebook. In **Lakehouse explorer**, select **Add lakehouse** > **Existing lakehouse**, select the
   lakehouse, and pin it as the default if it is not already.
3. Select **Run all**.
Check it worked: the last cell shows a table of row counts and the exit value contains `"status": "succeeded"`; the
lakehouse **Tables** node lists every table (select **Refresh** on Tables if needed).

### Where a schedule is configured (no schedule created)
1. In the workspace, hover the notebook > **...** > **Schedule**.
2. Leave the schedule **Off** and close the panel.
Title such as "See Where a Notebook Schedule Is Set (Job Scheduler)". No Check it worked (the steps say it all), and
nothing about why the lab does not schedule it.

### SQL analytics endpoint check
1. In the lakehouse, switch the view selector (top right) from **Lakehouse** to **SQL analytics endpoint** [Verify].
2. Select **New SQL query**, paste the row-count query from the guide, select **Run**.
Copy block: one `SELECT 'table' AS table_name, COUNT(*) AS row_count FROM table UNION ALL ...` statement generated
from the manifest. Check it worked: counts equal the manifest counts.

### Create the data agent and add data
1. In the workspace, select **+ New item**, search **Fabric data agent**, select it, enter the agent name, select
   **Create**.
2. The OneLake catalog opens: select the lakehouse > **Add**.
3. In **Explorer** (left pane), expand the lakehouse and check only the exercise tables.
No Check it worked (it would restate step 3).

### Instructions
1. Select **Data agent instructions**; paste the agent instructions copy block (stays well under 15,000 characters).
2. Open the lakehouse source's **Data source instructions** [Verify label and location]; paste the data source
   instructions copy block.
3. Select **Clear chat**, then ask the before/after prompt again (refer to it; do not repeat its copy block).

### Example queries
1. Select **Example queries**; for the lakehouse, select **Add** (or **Edit**); paste each question and its SQL.
Check it worked: each example shows as valid. Do not add a separate "confirm each is valid" step.

### Test
1. Select **Clear chat** before each independent test.
2. Paste the prompt; when the answer appears, expand the **steps** dropdown and read the generated SQL.
Each prompt has its own What good looks like; no Check it worked for the exercise.

### Publish and share
1. Select **Publish**; paste the publish description copy block; confirm.
2. Select **Share**, add a colleague, and remind them they also need access to the lakehouse [Verify Share location].
Check it worked: the agent shows a published version; the draft remains editable.

## Copy-ready text templates

Number lines under each heading, restarting per heading. No labeling scheme, no codes. Write each line as what the
agent does (see House style in SKILL.md). Write business terms exactly as the synthetic data encodes them.

Copy-ready text describes the lakehouse tables as production data ("data current through <date>"), never files, an
export, or the notebook.

### Data agent instructions (shape)

```
## Purpose
You answer questions from <persona team> at <company> about <domain> from the <table list> tables in the <lakehouse name> lakehouse, data current through <date>.

## Business definitions
1. "Backlog" means work orders on their current revision whose status is open, in progress, or waiting approval.
2. "Downtime" without a qualifier means unplanned downtime.
3. Report labor in hours. Some labor is recorded in minutes; convert it before adding.
4. "Last quarter" means the most recent completed calendar quarter.

## How to answer
1. State the number first, then the filters you applied in one sentence.
2. Show results as a table when there is more than one row.

## Questions the data doesn't answer
1. When a question asks why something happened, return the related figures and say that cause analysis is outside what you answer.
2. When a question needs data outside these tables, say which data would answer it.
3. Mark a value as unknown when the data has no record for it.
```

### Data source instructions (shape)

```
1. Use work_orders.is_current_revision = 1 for every count or total; earlier revisions are superseded.
2. Status codes vary in spelling. Treat OPEN and Open as open; INPR and In Progress as in progress; WAPPR as waiting approval; COMP, COMPLETED, COMPLETE as completed; CLOSE, CLOSED, CLSD as closed; CAN, CANC, Cancelled as cancelled. Compare with UPPER(status_code).
3. labor_unit is HR or MIN. Divide MIN values by 60.0 before summing hours.
4. Join work_orders and downtime_events to sites on site_id and to assets on asset_id.
5. downtime_category values UNPLANNED, Unplanned, and UNPL all mean unplanned.
6. Filter time periods on opened_date or event_start_ts; record_loaded_date is the date a record arrived.
```

### Example queries
- Each is a natural question plus T-SQL that runs on the SQL analytics endpoint and matches the selected tables.
- Encode the business definitions (current revision, status normalization, unit conversion) so the agent learns
  them by example.
- Cover different shapes: a grouped count, a time-bounded sum, a filtered single value.
- Keep them portable (date literals as `'YYYY-MM-DD'`, `UPPER`, `CASE`, `ROUND`) so `generate_synthetic_data.py` can
  execute them; give a separate `sqlite` form in the spec only when T-SQL syntax (TOP, DATEADD) is unavoidable.

### Publish description (shape)

```
Answers questions about <domain> at <company>: <three or four concrete question types>. Uses the <lakehouse> lakehouse tables <list>. Applies the business definitions for <terms>. For questions about causes, returns the related figures. Answers with read-only queries.
```

## Test prompt design

- Short, realistic human questions as the persona would type them: "How big is our maintenance backlog right now?"
  Never restate setup, table names, file names, or instructions in the prompt.
- 6-10 prompts: at least one before/after pair, two or three in-scope aggregates touching different traps, one
  multi-table join, one that should hit an example query, and **two out of scope**: one causal "why" question and one
  that asks for something the data does not contain.
- **What good looks like** for each: the exact expected value or top rows from `expected_answers.json`, the filters
  the generated SQL should show (current revision, status normalization, unit conversion), and for out-of-scope
  prompts, the expected behavior (returns related figures and says cause analysis is outside scope; or says the data
  does not cover it).
- Before/after: the "before" value is the naive reading (for example `status_code = 'OPEN'` on all revisions); the
  "after" value applies the definitions. Both come from code. Say what the participant should see change in the SQL.

## Synthetic data trap menu (choose 3-5 per scenario)

| Trap | How it looks in the data | What handles it |
|---|---|---|
| Inconsistent codes | `COMP`, `Completed`, `COMPLETE` for one status | Data source instructions + example query |
| Mixed units | labor in HR with some rows in MIN | Data source instructions |
| Nulls | missing cost or cause code | Agent instructions: unknown, not zero |
| Superseded records | revision rows with `is_current_revision` | Data source instructions + example query |
| Late-arriving records | load date weeks after event date | Data source instructions: filter on event date |
| Business-term ambiguity | "backlog", "downtime", "active customer" | Agent instructions: definitions |

Keep traps opaque: plausible codes and columns that a real export would carry, never names like `bad_flag`,
`trap_unit`, or `DUPLICATE`.
