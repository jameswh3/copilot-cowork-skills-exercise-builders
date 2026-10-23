# Lab patterns: click paths, copy-ready text, and test design

Facts and URLs live in [fabric-grounding.md](fabric-grounding.md). This file says *how to write them as steps*.
Anything marked [Verify] must be re-checked against Learn before it ships; if it still can't be verified, keep the
[Verify] marker in the handout.

## The step shape (every exercise)

- **Goal** - one sentence naming the capability the participant gains.
- **Steps** - numbered; each starts with a UI verb (Select, Open, Paste, Enter, Upload, Run) and names the page and
  control. Never "decide", "consider", "ensure", "review", "make sure".
- **Enter this** - copy blocks holding only literal text the participant pastes: agent instructions, data source
  instructions, example question + SQL, test prompts, publish description, notebook parameter values. Never UI
  navigation inside a copy block.
- **Check it worked** - what appears on screen (table names in Explorer, the run status in Monitor, the generated SQL
  in the steps dropdown, the exact expected number).

No "If it didn't", "If it stalls", wait-time, or troubleshooting blocks. Factual prerequisites stay.

## Exercise sequence (dependency order)

| # | Exercise | Ends with on screen |
|---|---|---|
| 0 | Prerequisites and pre-flight checklist | Every checklist line ticked |
| 1 | Open your workspace and create the lakehouse | Empty lakehouse with Tables and Files |
| 2 | Upload the source files to Files | CSVs listed under Files/<folder> |
| 3 | Import the notebook, attach the lakehouse, run it once | Exit value shows `succeeded`; tables listed under Tables |
| 4 | Schedule the notebook | Schedule saved; a run appears in Monitor / Recent runs |
| 5 | Verify the tables in the SQL analytics endpoint | Row counts match the expected counts |
| 6 | Create the data agent and add the lakehouse | Agent opens with lakehouse in Explorer; tables checked |
| 7 | Ask a baseline question (before instructions) | Baseline answer and its SQL recorded |
| 8 | Add data agent instructions and data source instructions | Same question returns the defined answer |
| 9 | Add example queries | Examples validate; matched question reuses the logic |
| 10 | Test in-scope and out-of-scope prompts | Each answer matches "What good looks like" |
| 11 | Publish and share | Published version exists; description visible |
| 12 | Optional: consume from Microsoft 365 Copilot or Copilot Studio | Agent answers from the other surface |
| A1-A4 | Optional advanced: second source, Refresh after scheduled run, diagnostics, Git / deployment pipelines | Per exercise |

Exercises 7 and 8 together are the **before/after test**: the same prompt, asked before and after instructions,
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
   **Upload** [Verify].
Check it worked: each CSV is listed in the folder. The participant does NOT use "Load to Tables"; the notebook owns
ingestion so it can be scheduled.

### Import, attach, run
1. In the workspace, select **Import** > **Notebook** > **From this computer**, select the `.ipynb`, select
   **Upload** [Verify].
2. Open the notebook. In **Lakehouse explorer**, select **Add lakehouse** > **Existing lakehouse**, select the
   lakehouse, and pin it as the default if it is not already.
3. Confirm the parameters cell holds the same folder name used in the upload step; edit only that value if needed.
4. Select **Run all**.
Check it worked: the last cell shows a table of row counts and the exit value contains `"status": "succeeded"`; the
lakehouse **Tables** node lists every table (select **Refresh** on Tables if needed).

### Schedule
1. In the notebook, select the **Run** tab > **Schedule** [Verify]; or in the workspace, hover the notebook > **...**
   > **Schedule**.
2. Turn the schedule **On**; set **Repeat** (for example Daily), **Time**, **Start date and time**, **End date and
   time**, and **Time zone**; select **Apply**.
3. Optionally add yourself under **Failure notifications**.
Check it worked: the schedule shows as on with the next run time; after the first scheduled run, **Monitor** (left
rail) or the notebook's **...** > **Recent runs** lists the run as Succeeded.
State in the guide: scheduled runs use the identity of whoever created or last updated the schedule.
Optional alternative (one paragraph, no full lab): a **Data pipeline** with a **Notebook** activity that selects this
notebook, passes `source_folder` under **Base parameters**, then **Home** > **Schedule**.

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
Check it worked: Explorer lists the lakehouse with the selected tables checked.

### Instructions
1. Select **Data agent instructions**; paste the agent instructions copy block (stays well under 15,000 characters).
2. Open the lakehouse source's **Data source instructions** [Verify label and location]; paste the data source
   instructions copy block.
3. Select **Clear chat**, then ask the before/after prompt again.

### Example queries
1. Select **Example queries**; for the lakehouse, select **Add** (or **Edit**); paste each question and its SQL.
Check it worked: each example shows as valid; an example flagged invalid is ignored by the agent, so fix it against
the schema before moving on.

### Test
1. Select **Clear chat** before each independent test.
2. Paste the prompt; when the answer appears, expand the **steps** dropdown and read the generated SQL.
Check it worked: the value matches "What good looks like".

### Publish and share
1. Select **Publish**; paste the publish description copy block; confirm.
2. Select **Share**, add a colleague, and remind them they also need access to the lakehouse [Verify Share location].
Check it worked: the agent shows a published version; the draft remains editable.

## Copy-ready text templates

Number lines under each heading, restarting per heading. No labeling scheme, no codes. Every "never" is a guardrail.
Write business terms exactly as the synthetic data encodes them.

### Data agent instructions (shape)

```
## Purpose
You answer questions from <persona team> at <company> about <domain> using the <lakehouse name> lakehouse.

## Business definitions
1. "Backlog" means work orders on their current revision whose status is open, in progress, or waiting approval. Cancelled work orders are never backlog.
2. "Downtime" without a qualifier means unplanned downtime.
3. Report labor in hours. Some labor is recorded in minutes; convert it before adding.
4. "Last quarter" means the most recent completed calendar quarter.

## How to answer
1. State the number first, then the filters you applied in one sentence.
2. Show results as a table when there is more than one row.
3. When a question asks why something happened, return the related figures and say that cause analysis is outside what you answer.
4. Mark a value as unknown when the data has no record for it.
```

### Data source instructions (shape)

```
1. Use work_orders.is_current_revision = 1 for every count or total; earlier revisions are superseded.
2. Status codes vary in spelling. Treat OPEN and Open as open; INPR and In Progress as in progress; WAPPR as waiting approval; COMP, COMPLETED, COMPLETE as completed; CLOSE, CLOSED, CLSD as closed; CAN, CANC, Cancelled as cancelled. Compare with UPPER(status_code).
3. labor_unit is HR or MIN. Divide MIN values by 60.0 before summing hours.
4. Join work_orders and downtime_events to sites on site_id and to assets on asset_id.
5. downtime_category values UNPLANNED, Unplanned, and UNPL all mean unplanned.
6. record_loaded_date is when a record arrived, not when work happened; filter periods on opened_date or event_start_ts.
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
Answers questions about <domain> at <company>: <three or four concrete question types>. Uses the <lakehouse> lakehouse tables <list>. Applies the business definitions for <terms>. Does not explain causes; returns the related figures instead. Read-only.
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
