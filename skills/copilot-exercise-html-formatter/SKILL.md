---
name: copilot-exercise-html-formatter
description: |
  Produce and repair the styled HTML handout format used for Microsoft Copilot demo exercises, workshop guides, and enablement session content: brand color resolution, executive handout layout, collapsible left nav rail, copy-to-clipboard prompt blocks, WCAG AA contrast, and ASCII-safe punctuation encoding. Use when the user asks to "format this exercise as an HTML handout", "style the workshop guide", "apply brand colors to the handout", "add copy buttons to the prompts", "fix the contrast in the handout", "clean up the em-dashes and encoding", "rebuild the nav rail", "make the sidebar collapsible", or when another Copilot exercise skill needs its HTML rendered. Do NOT use to invent exercise content (use copilot-exercise-builder or copilot-cowork-exercise-builder), to build general web pages or apps, or to produce Word, PowerPoint, or Excel deliverables.
metadata:
  category: writing
  icon: Code
---

# Copilot Exercise HTML Formatter

This skill owns the presentation layer for Copilot demo and workshop content. It does not decide what an exercise says. It decides how the handout looks, encodes, and behaves.

Two skills call it: `copilot-exercise-builder` and `copilot-cowork-exercise-builder`. It also runs standalone when the user hands over existing exercise content and asks for a handout, or asks to fix an existing one.

## Inline sources at point of use (binding default)

This rule overrides any older requirement for a published source pack, content matrix, file-to-exercise mapping table, inventory, blueprint, or separate source section. Apply it to new content and revisions, in HTML and plain text alike.

- Put exact source filenames or verified links immediately alongside the exercise that requires them, in a concise `Setup`, `Open`, or `Upload` sentence or short bullets. List only the files needed at that point. Use one action verb per instruction: open, upload, or reference; add a short business purpose only when useful. Replace legacy participant-facing `Drop-in Content Pack` tables and published file blueprints with `Inline Sources` within the requiring exercise, or merge them into its existing setup sentence. Do not retain a separate pack heading, add another matrix, or duplicate the setup list. Include a short business purpose for each source without describing its internal anatomy.
- Do not publish a centralized source pack/content matrix, mapping table, inventory section, source blueprint, or navigation link that sends participants elsewhere to discover required inputs. Move legacy entries into the relevant exercise and remove the obsolete section and orphaned nav link, rather than hiding them. This does not prohibit business-result tables or actual business data in source files.
- Reuse the same saved file across exercises. Store it once in its primary exercise folder and reference that same exact path at each point of use; do not generate duplicate copies. Use an exact filename/path when no verified URL is available. Never invent a download, tenant, or sharing link; verify any link against the actual saved artifact or confirmed source.
- Keep any file manifest, source-to-exercise mapping, or detailed blueprint internal for authoring and validation only, never in participant artifacts (including hidden panels, comments, appendices, or notes). Generate only the minimal assets needed for the bounded business task.
- Put ONE concise `Synthetic` provenance attribution near the first exercise that uses the synthetic files, plus one `Synthetic` metadata/header label per file. Do not repeat the handout attribution for later exercises reusing those files, or put provenance in copied prompts. Retain truthful source, author/participants and date identifiers.
- Keep setup business-only: no row/tab anatomy, internal field inventories, or prompt meta-narrative. Preserve bounded evidence and coverage, supported verified analytical paths, draft-only/approval constraints, factual access prerequisites, and minimal assets. Before delivery, verify every required source is named at its point of use and every link resolves to the intended saved source. Formatting changes must preserve the existing nav-width and semantic reading-anchor contracts.
- Audit placement exercise by exercise, using an internal manifest only if useful: reconcile every required input against its inline setup and saved artifact, check exact spelling and any verified link target, and confirm reused sources keep one saved path. Remove conflicting old published-table/file-mapping mandates and obsolete source-section/nav entries rather than relying only on this override. Do not repeat prompt metadata or provenance. For a source-placement-only skill update, preserve the prior nav-width and semantic reading-anchor requirements byte-for-byte; do not edit a handout to demonstrate the change.

## Business-only wording and bounded evidence (binding)

These rules govern authoring and formatting alike and override older examples or section names that conflict. They apply to every participant-facing prompt, instruction, narrative, expected output, and companion source.

1. **Business-only copy blocks.** Write only the work request the persona would actually give: the decision, selected inputs, substantive business constraints, and requested output. Never put demo, simulation, illustrative, teaching, or authoring labels in prompts. Exclude "this exercise", product comparisons, test controls, generation commentary, and explanations such as "This is illustrative IT ...". Keep draft-only instructions, unknown-value handling, citation/evidence requirements, uncertainty, and approval constraints: these protect the business work and are not meta-narrative.
2. **Provenance once, in the right place.** Put ONE concise `Synthetic` label in each companion source's metadata/header and ONE concise handout attribution near the first exercise using the synthetic files. Retain source/author/participants/date identifiers. Do not repeat the label in business prose, prompt directives, table rows, or expected outputs; exclude all other demo/simulation/illustrative/teaching/authoring narrative. Do not remove truthful provenance or factual product availability, permissions, licensing, or access prerequisites. Product names and necessary setup/click paths remain; explanatory product comparisons do not.
3. **Bound the actual evidence workload.** Use a short, explicitly selected file set, authored small enough for the timebox, and a bounded business question or decision-gate scope. Name the files, business scope and timeframe in the work request; keep internal row/table selection out of participant-facing content. For live M365 retrieval, bound topics, people/meetings, dates and returned evidence; report what was actually found/read and what remains unknown. Chat, Notebook, Agent Builder and search-based M365 retrieval are not exhaustive per-account/per-record audit engines. Never promise search-wide completeness, full-population validation, or an all-clear from retrieved snippets or a sample.
4. **Population is not analyzed records.** A business rollout may cover hundreds of accounts, devices, employees, or sites without the run analyzing each one. Keep that population as business context; state the much smaller source set, summary/gate workload, and coverage actually analyzed separately. Prefer supplied aggregates to hundreds of enumerated items. Do not turn a rollout count such as 600 into 600 individual checks. Choose workload sizes for the timebox and actual source granularity, not an unsupported universal numeric product limit.
5. **Use the right analytical path.** Quantitative scans and computations belong in Analyst over uploaded data or in Excel for appropriate formulas, tables and light analysis. In Cowork, use an explicitly available computational tool or supported model query for that leg before synthesizing or creating deliverables. Keep inputs small enough for the timebox and verify the computed output. If exact comprehensive validation is required, use a genuinely exhaustive tool-supported path with a defined dataset, full row/page coverage, explicit rules and verification; when unavailable, narrow the task or state the gap instead of promising completeness. No fabricated all-clear, totals, percentages, or probabilities from a sample.
6. **Coverage belongs in the business result.** Require the sources/rows/gates actually considered, missing or stale evidence, contradictions, and unresolved questions. Distinguish source-reported aggregates from independently computed results and inferences. A sampled finding applies only to its evidence, not the whole population; missing evidence is unknown, not passed. Keep any message, approval or recommendation a draft where appropriate.
7. **Audit before delivery.** Read the literal text copied by EVERY copy button, not just the visible wrapper, plus all visible/hidden narrative, source metadata, document notes and workbook tabs. Remove excluded wording rather than hiding it. Check actual source granularity, files/rows/gates touched, computational path and timebox; reconcile every prompt and claimed result with the companion files. Preserve participant setup, truthful provenance and business evidence guards. Delete orphaned navigation links. Fix conflicts before declaring ready; keep audit/generation commentary in chat only.

## Business source language, not file anatomy (binding)

This overriding rule applies to all participant-facing setup and selected-source content, steps, inline source instructions, copied prompts, and expected outputs. Where older wording asks for source selection or summary/gate scope, express that scope in business terms, not workbook anatomy.

- Name the workbook or file and the business question, date period, service, vendor, or metric relevant to the decision. Do not ask participants to find named tabs/sheets, count sheets, locate row/column numbers or A1 ranges, copy exact formulas, select ranges, exclude metadata rows, or map sheets. Do not publish internal table/field inventories as participant setup requirements.
- Have participants open or upload the file, then ask naturally for the result. Ask Copilot to identify the relevant table and fields, check stored units and number formats, preserve source values, and provide a traceable result. Do not claim that opening/uploading a file guarantees the entire file is read or exhaustive coverage. Missing, inaccessible, ambiguous, or unread evidence must be reported honestly, not inferred as complete or passed.
- Bound workloads by authoring genuinely small files and specifying a business scope and date period, not by teaching participants to select a small set of rows or hunt for sheets. Keep source-reported aggregates distinct from computed values and inference; retain evidence checks, missing-data handling and the appropriate verified analytical path. Do not move numerical work into unsupported Chat arithmetic.
- Internal authoring validation remains required: inspect source structure, tables, fields, rows, formulas, units, metadata, and expected calculations to ensure the files support the request. Keep that anatomy internal. Row/cell citations or other precise source anchors may appear in generated results as evidence; they are not a participant setup burden or an expected-output instruction to navigate manually.
- A genuine product prerequisite may be stated plainly: "Use a formatted table if your Excel experience requires one." Never attach hardcoded ranges or sheet-hunting directions to it. Preserve truthful access prerequisites and product navigation, without confusing them with file-internal selection.
- Before delivery, sweep all setup, steps, inline source instructions, prompt text (including literal clipboard content), and expected outputs for file-anatomy micromanagement. Rewrite it as file name plus business scope; keep the units, evidence and computation guards. Do not silently alter business figures or invent inaccessible evidence.

Example business prompt: "Using the workbook, chart weekly availability by service for September 11 through October 16; flag Workplace Access below 99.90%; check stored units; preserve source values and cite the evidence."

## Participant-only published content (binding)

Every published HTML handout and companion file must stand alone for a participant who has never seen the authoring chat. This rule takes precedence over any older output-section, workflow, or companion-reference instruction requiring delivery notes or troubleshooting blocks.

- Exclude meta-narrative and authoring rationale: no explanation of how the material was drafted, revised, selected, validated, or packaged; no internal process commentary or validation results.
- Exclude chat-history extensions: no "as you requested", "updated/rebuilt", feedback acknowledgments, discussion of inferred scope or session counts, or future optional-extension offers copied from assistant chat. Keep any required planning statements and offers in chat only, never in an artifact.
- Exclude facilitator, speaker, delivery-team, and run-room notes, including "While It Runs", "If It Stalls", wait-time filler, troubleshooting advice, and what someone should say or show to the room. Remove these sections rather than hiding them in comments, collapsed panels, appendices, document notes, or workbook tabs.
- Preserve genuine participant scenario context, product setup and click paths, copy-ready prompts, expected outputs, evidence checks, and essential factual availability, access, permissions, and reference information. Business context and product constraints are not authoring commentary. Do not remove participant instructions merely because they address the reader directly.
- Synthetic material must read like original source material: use the single `Synthetic` source-metadata label and first-use handout attribution specified above, plus appropriate source, participants or author, and date identifiers. Follow with business content only, without repeated labeling, author conversation, or exercise-construction commentary.
- Before publishing or revising, inspect all handout sections and every companion file for these excluded categories, including hidden text and notes. Delete excluded material and any orphaned navigation links; confirm required participant steps, prompts, source evidence, and factual prerequisites remain intact.

## When NOT to Use

- The user needs exercise content authored, not styled: use `copilot-exercise-builder` (scenario exercises) or `copilot-cowork-exercise-builder` (Cowork exercises).
- The user wants a general-purpose web page, landing page, or interactive app: use the `create` skill instead.
- The user wants a Word, PowerPoint, Excel, or PDF deliverable: use `docx`, `pptx`, `xlsx`, or `pdf` instead.
- The user wants synthetic sample data files generated: that belongs to the calling exercise skill.

## Required workflow

1. **Confirm the output format.** HTML (styled handout) is the default for all Copilot exercise content. Only produce plain text when the user explicitly asks for it. Do not ask which format; assume HTML.
2. **Resolve brand colors** (see Brand resolution below). Never emit `[accent]`, `[accentTint]`, or `[accentText]` placeholders into a finished file.
3. **Build the handout** using the layout, punctuation, accessibility, and copy-button rules below. Convert legacy pack tables, matrices, inventories, and published blueprints into concise point-of-use source sentences or bullets alongside each requiring exercise, using only supplied exact filenames/paths or verified links. Remove obsolete source sections and their nav links; do not invent links, duplicate files, repeat provenance, or add a replacement matrix. Keep an internal manifest only for validation. Preserve the nav-width and semantic reading-anchor contracts below. Apply the participant-only, business-only wording and business-source-language rules to incoming content: rewrite file-internal participant instructions as file name plus business question/date period/service/vendor/metric, preserving units, evidence and verified analytical-path requirements; strip excluded material from actual copied prompt text as well as narrative; keep substantive business guards, participant actions, concise provenance and factual prerequisites. Rename legacy "What This Exercise Demonstrates" headings to "Business Outcome" and retain only their business substance. If analysis scope exceeds the actual sources or surface, return that content to the calling authoring skill for a bounded rewrite; do not invent evidence, silently change business figures, or merely style an impossible completeness claim.
4. **Sweep before delivery** (see Pre-delivery sweep). This step is mandatory, not optional.
5. **Save the HTML as a downloadable `.html` file.** Never dump the markup into chat as a code block.

## Brand resolution

Resolve brand colors before generating any HTML when a company is named.

- Research the organization's primary brand color using authoritative public sources. Prefer its official brand guide or design system, then its official website. Use a third-party palette only when an official source corroborates it.
- Do not infer a brand color from memory. Record the source used, and treat conflicting or unverifiable values as unknown.
- Derive `[accentTint]` as the accent blended with white at roughly 10% opacity (for example `#0078D4` becomes `#e6f2fb`).
- Derive `[accentText]` as a darkened variant of `[accent]` reaching at least 4.5:1 contrast against both `#ffffff` and `#fafafa`. Bright brand colors (orange, magenta, gold, lime) typically need 40-50% darkening to meet AA.
  - Worked examples: `#F36F21` becomes `#8C3D11`; `#FF6600` becomes `#B23A00`; `#E20074` becomes `#8C0048`.
  - For colors already dark enough (`#0078D4`, `#003087`), `[accentText]` can equal `[accent]`.
- If the brand color cannot be verified, ask one brief question: "Do you have a primary brand color or official website I should use for styling?"
- At the top of every HTML output, include a comment identifying the resolved colors: `<!-- Brand: [accent] / tint: [accentTint] -->`.

## Punctuation and encoding (binding)

**Never use em-dashes or en-dashes anywhere in the output.** This covers body text, headings, callouts, table cells, HTML, plain text, and any synthetic content file, in both literal form and as `&mdash;` / `&ndash;` entities.

Em-dashes render unreliably across encodings (they surface as garbled characters when a file is re-decoded as Latin-1) and are a strong tell that content is machine-generated. Substitute as you write, not afterward:

- A colon, when introducing or expanding: "The moment: fire season is approaching."
- A comma or period, when separating clauses.
- A hyphen with spaces, when a visual break is needed: "Three connected sessions - one agent that grows with each exercise."
- Parentheses, for parenthetical context.

Use ASCII-safe entity encoding for every punctuation mark that needs a non-ASCII glyph. Some enterprise viewers re-decode files as Latin-1 and garble raw UTF-8 punctuation.

| Character | Use instead |
|---|---|
| middle dot | `&middot;` (never raw) |
| right single quote or apostrophe | `&rsquo;` |
| left and right double quotes | `&ldquo;` and `&rdquo;` |
| ellipsis | `&hellip;` or `...` |
| right and left arrows | `&rarr;` and `&larr;` |
| non-breaking space | `&nbsp;` |

Apply the same rule to every artifact shipped alongside the handout.

## Layout rules

- Return a single self-contained `<div>` with nested elements. Do not return `<html>`, `<head>`, or `<body>` tags.
- Include exactly one `<style>` block at the end of that `<div>`, holding only the `@media print` rules that hide `.copy-btn` and `.copy-confirm`, plus the collapsible nav rules from the section below.
- Use inline styles for all other layout and visual styling.
- Font: `Arial, Helvetica, sans-serif`. Text color: `#1a1a1a`. `line-height: 1.6` or `1.7`.
- No height, max-height, overflow, or scrolling styles on the main content area.
- Two-column layout: a fixed left-hand navigation rail plus a right-side main content area. Start with an explicit expanded responsive width (for example `width: calc(100% - 312px); max-width: 980px; box-sizing: border-box; flex: none`). Enhanced desktop collapse must reclaim actual reading width, with semantic text-position restoration; expanded layout is restored on opening. Only the no-script desktop fallback and mobile overlay keep width invariant between nav states. Avoid unintended flex growth/shrinkage; use explicit state geometry.
- **Use `position: fixed` for the nav rail, never `position: sticky`.** Sticky inside a flex row breaks page scrolling in M365 and Cowork preview panes. Give the fixed nav `max-height: calc(100vh - 32px); overflow-y: auto;` and offset the main content with a left margin around 288px.
- **The nav rail is collapsible: CSS owns checkbox/rail state; JavaScript progressively enhances desktop width and reading position.** Use the checkbox pattern below. Scripts blocked: retain the invariant-width CSS fallback. Mobile: keep an overlay with no content reflow in either mode.
- Include at minimum these nav anchors when the sections are present: `#session-slides`, `#system-of-work`, and each active exercise section (for example `#copilot-chat`).
- For multi-section outputs, add divider separators in the nav between foundational sections and exercise sections.
- Navigation labels use a shortened form of the exercise title with the product still in parentheses (for example "Draft Business Case (Word)").

Executive handout look:

- Small badge at the top for the exercise or scenario type
- Prominent title with a muted subtitle for the company or use case
- Section headings with a bottom border in the accent color
- Rounded overview and callout panels with soft tinted backgrounds
- Setup, configuration, and starter-prompt content in lightly bordered cards
- Consistent spacing, subtle dividers, restrained visual hierarchy
- Use `<h2>`, `<h3>`, `<h4>`, `<p>`, `<ul><li>`, `<ol><li>`, `<table>`, `<strong>`, `<em>`, `<pre>`, and `<hr />` where they help

Apply the accent color to badge backgrounds, heading underlines and dividers, left borders on callout and prompt blocks, and light background fills for overview or tip cards. Keep accent usage limited and whitespace generous.

## Collapsible left nav (CSS state with progressive JavaScript enhancement)

Every fixed-rail handout gets a keyboard-accessible toggle. **Default enhanced desktop behavior: collapsing the rail widens the reading content into the released space; opening restores the rail layout.** In both directions, preserve the same visible text position at the same vertical viewport offset. Translation alone is not width reclamation. CSS owns the checkbox/rail state; inline JavaScript enhances desktop content geometry and reading-position restoration. If scripts are blocked, the checkbox remains functional with an invariant-width fallback. On mobile, the rail is an overlay and never reflows content.

### Three explicit layout contracts (binding)

- **Enhanced desktop, above 760px:** collapsed main content has a strictly larger computed width than expanded content at the same viewport. Change width and left margin together, remove the expanded cap for the collapsed state, and reset any fallback transform. Opening restores the original expanded width and margin. Text wrapping and document height may change; the semantic anchor must not move vertically by more than 1 CSS pixel after settling.
- **No-script desktop:** keep width, max-width, margins, padding, font metrics, wrapping and block heights invariant across toggle states. Horizontal translation into the free space is allowed; blank space is a fallback only, not the enhanced default.
- **Mobile at or below 760px:** use identical content width, margin, padding and transform in both states, with or without scripts. The drawer overlays content. A viewport resize may change layout; a mobile nav toggle may not.

Keep main content in normal vertical flow. Do not add a height, max-height or scrolling style to main content to disguise a jump. Support an existing host/preview scrolling ancestor rather than imposing a new one. No width, margin, padding, max-width or content-transform transition in enhanced mode: reflow is discrete, followed by a bounded anchor restoration, never an animation with repeated scroll corrections.

### Structure (this order, all siblings under one handout root)

Use unique identifiers per handout when several are embedded. The following assumes one instance. The hidden checkbox remains focusable, has an accessible name and controls the rail; Space toggles it natively. The visible label is the pointer target and shows a clear focus indicator when the checkbox has keyboard focus. Do not give the label a second keyboard tab stop or introduce double activation.

```html
<div class="exercise-handout">
  <input type="checkbox" id="nav-toggle" aria-label="Collapse navigation" aria-controls="side-nav" style="position: fixed; opacity: 0; width: 1px; height: 1px;" />
  <label for="nav-toggle" id="nav-toggle-btn" aria-label="Toggle navigation" style="position: fixed; top: 16px; left: 240px; z-index: 20; width: 26px; height: 26px; border-radius: 6px; background: #ffffff; border: 1px solid [accentText]; color: [accentText]; text-align: center; line-height: 24px; font-size: 16px; cursor: pointer;">&lsaquo;</label>
  <div id="side-nav" style="position: fixed; width: 264px; max-height: calc(100vh - 32px); overflow-y: auto;">...</div>
  <div id="main-content" style="margin-left: 288px; width: calc(100% - 312px); max-width: 980px; box-sizing: border-box; flex: none;">...</div>
  <!-- Include the inline enhancement/copy script and the single style block here. -->
</div>
```

### CSS (in the single style block)

```css
#nav-toggle:focus-visible ~ #nav-toggle-btn {
  outline: 2px solid currentColor;
  outline-offset: 3px;
}
#side-nav { transition: transform 0.2s ease, opacity 0.2s ease; }
#nav-toggle-btn { transition: left 0.2s ease, transform 0.2s ease; }
#nav-toggle:checked ~ #side-nav {
  transform: translateX(-280px);
  opacity: 0;
  visibility: hidden;
  pointer-events: none;
}
/* Script-free desktop fallback: move, but do not resize, content. */
#nav-toggle:checked ~ #main-content { transform: translateX(-264px); }
#nav-toggle:checked ~ #nav-toggle-btn {
  left: 16px !important;
  transform: scaleX(-1);
}
@media (min-width: 761px) {
  /* JS commits this class ONLY after capturing the reading anchor. */
  .exercise-handout.nav-enhanced #main-content {
    transform: none !important;
    transition: none !important;
  }
  .exercise-handout.nav-enhanced.nav-wide #main-content {
    margin-left: 24px !important;
    width: calc(100% - 48px) !important;
    max-width: none !important;
  }
}
@media (max-width: 760px) {
  .exercise-handout #main-content,
  .exercise-handout #nav-toggle:checked ~ #main-content {
    margin-left: 16px !important;
    width: calc(100% - 32px) !important;
    max-width: 980px !important;
    padding-top: 38px;
    transform: none !important;
    transition: none !important;
  }
  #nav-toggle-btn,
  #nav-toggle:checked ~ #nav-toggle-btn {
    top: 8px !important;
    left: 8px !important;
  }
}
@media (prefers-reduced-motion: reduce) {
  #side-nav, #main-content, #nav-toggle-btn { transition: none; }
}
@media print {
  #side-nav, #nav-toggle, #nav-toggle-btn, .copy-btn, .copy-confirm {
    display: none !important;
  }
  .exercise-handout #main-content {
    margin-left: 0 !important;
    width: 100% !important;
    max-width: none !important;
    transform: none !important;
    transition: none !important;
  }
}
```

The enhanced width class is deliberately NOT a `:checked` width rule: native checkbox activation changes `:checked` before its `change` handler runs. Keeping geometry behind the committed `.nav-wide` class lets the handler capture the old layout first, then apply the new width. Install the enhancement only after its anchor/scroll helpers and event handlers are ready. Initial activation, including a restored checked checkbox, must use the same capture-before-reflow transaction. Without successful setup, leave CSS fallback intact.

### Semantic reading-position transaction (required inline JavaScript)

Implement these helpers in the handout's inline script; this is an implementation contract, not a claim that the illustrative CSS alone implements anchoring:

1. **Identify the actual scrolling context.** Walk ancestors for scrollable overflow and scroll height, falling back to `document.scrollingElement`. Include outer scrollable ancestors if needed. Compute the content's visible vertical intersection with the host scroller and viewport. Never assume `window.scrollY` is the reading position; embedded previews often scroll an ancestor element. Preserve scrollLeft too.
2. **Capture BEFORE any geometry mutation.** In the old content layout, select visible main-content text near a stable reading line inside that intersection. Use `caretPositionFromPoint` or `caretRangeFromPoint` where supported, with a TreeWalker/Range-rectangle fallback. Save the text node and exact character offset (plus a stable block identifier/text-offset recovery path), a one-character DOM Range covering that character, and its rectangle's top relative to the visible scrollport. For prose, table cells and wrapped prompts, use the text range's rendered line, NOT just a heading or block's top: block-top anchoring loses the passage within long text. Do not clone, replace or rewrite text nodes during the toggle. If no text is visible, use a stable visible element rectangle as a fallback and report that limitation; if no anchor can be captured, retain invariant-width behavior for that toggle rather than guessing.
3. **Prevent competing scroll mechanisms.** Temporarily set `overflow-anchor: none` on the actual scroll owners and relevant content/ancestors, and `scroll-behavior: auto` on scroll owners, preserving previous inline values and priorities. Do this before applying width changes. Do not autofocus the rail, change fragments, invoke `scrollIntoView`, or run a competing smooth-scroll routine. Honor user-initiated wheel/touch/navigation during the transaction by cancelling pending restoration, not dragging the user back.
4. **Commit the new geometry.** In a `change` handler the checkbox continues to own rail state. Capture while `.nav-wide` still represents the old width, then set `.nav-enhanced` and toggle `.nav-wide` to match `checkbox.checked` on desktop. The desktop expanded state removes `.nav-wide`; inline expanded values then apply again. Mobile never commits width changes or performs scroll compensation. Keep checkbox accessible naming/state current and ensure hidden rail links cannot receive focus; do not steal focus from the toggle.
5. **Wait for layout to settle, then restore once.** Wait for relevant fonts/media to be ready (or reserve their dimensions) and for two animation frames with stable main width and anchor rectangle. Use a bounded timeout and transaction generation token, cancelling stale callbacks on rapid toggles, resize, navigation, print or user scrolling. Measure the SAME character Range in the new wrapping; compute `delta = newAnchorOffset - savedAnchorOffset`, then adjust the actual scroll owner's scrollTop by delta with instant behavior. For nested scrolling contexts, compensate in the nearest context with available scroll range and distribute residual to outer scroll owners only if needed; use the same viewport-relative anchor and remeasure after each bounded correction. Raw old scrollTop/scrollY, scroll percentage, and heading-only anchors are not substitutes for this delta.
6. **Verify and clean up.** After the correction frame, measure anchor error; allow at most one residual correction for rounding/settling, not a perpetual animation-frame/observer loop. Restore anchoring and scroll-behavior styles in `finally`, including cancellation/error paths, after the correction settles. Both collapsing and opening use the identical algorithm. At document/scroll-container boundaries, scroll clamping can make the requested offset impossible: do not claim a pass; retain/roll back to invariant-width geometry if feasible, or disclose the boundary limitation in chat. The accepted default must pass the mid-document matrix below.

Bind pointer and keyboard activation through the native checkbox `change` event, not separate handlers that toggle it twice. Use scoped event listeners for each handout. Rail transforms can animate; enhanced main-content dimensions cannot. Do not store raw scrollY as the only anchor, loop on `scrollTo`, or continuously fight the reader's scrolling. Responsive/print cleanup must not leave stale `.nav-wide` work running.

### Mandatory mid-document regression matrix

Before delivering a rendered handout, execute the following on a runnable sample, in BOTH collapse and expand directions. Record viewport, script mode, scroll owner, text-node/character anchor, its old/new vertical offset and error, plus old/new computed main width. Include long prose, table-cell text and a wrapped prompt at several mid-document locations, plus an embedded scrolling preview when available.

| Mode | Viewports | Required assertions |
|---|---|---|
| Enhanced desktop | Wide (for example 1440px) and just above the breakpoint (761px and 800px) | Collapse strictly increases main width, including when the expanded 980px cap is active; expansion restores original width/margin. Wrapping may change. SAME visible character stays within 1 CSS pixel of its original offset after settling in both directions. |
| No-script desktop | Same wide and near-breakpoint widths; scripts disabled/stripped | Checkbox still toggles rail. Main width, wrapping and vertical geometry are unchanged; anchor error is at most 1 CSS pixel. Translation/blank space is expected fallback. |
| Mobile overlay | At 760px and narrow (for example 390px), scripts on AND off | Both states have identical main width, margins, wrapping and vertical geometry, with anchor error at most 1 CSS pixel. Drawer opening never triggers desktop compensation. |

Also test keyboard Space and pointer activation, visible focus, rapid repeated toggles/cancellation, reduced motion, rail anchors, copy of the complete prompt, and print with controls hidden and full-width content. Neither direction resets the reader to the top. Clipboard availability is separate from the no-script nav test. Validate no width transition, no repeated scroll fight, and no stale restoration after user scrolling or fragment navigation.

A source sweep is not a browser test. If no runnable sample or interactive test surface is available, label these tests **not run**, name the limitation in chat, and do not claim the handout's behavior is verified. Never place testing/implementation commentary in participant artifacts. When modifying this skill alone, add/maintain the regression requirements but do not create or edit a handout just to claim a test pass.

### Narrow viewports: the toggle is an icon, never a labelled pill

At narrow widths the rail becomes an overlay drawer and the toggle is the only thing left sitting on top of the
content. Keep it to a **30px square or smaller, icon only**. A button carrying a word next to its glyph
("Contents", "Menu") is roughly 110px wide, and because it is `position: fixed` it stays there through the whole
scroll, covering the start of a heading or a table row on every screen.

- Icon only. The accessible name lives in `aria-label`, not in a visible span, so nothing is lost by dropping
  the word.
- Offset it 6 to 8px from the top and left corner, and give the main content just enough top padding to clear
  it (around 38px for a 30px button). More padding than that is a visible gap at the top of every page.
- A slightly translucent white background (`rgba(255,255,255,0.92)`) keeps text readable if it does pass
  underneath during a scroll.
- Check it against the longest heading in the handout, not against the top of the page. The overlap shows up
  mid-document, which is why it survives a quick look at the first screen.

## Accessibility: text color and contrast (binding)

Enterprise viewers (Outlook, Teams, in-app preview panes) silently override or fail to inherit text colors, which produces white-on-light cells that cannot be read.

- **Explicit text color on table cells.** Set `color: #1a1a1a` directly on every `<th>`, `<td>`, and any nested `<strong>`, `<em>`, or `<code>` inside a table. Do not rely on inheritance from the parent `<div>`.
- **Explicit text color on code and pre blocks.** Set `color: #1a1a1a` directly on every `<pre>` and `<code>`.
- **Brand color text contrast (WCAG AA, 4.5:1 for normal text).** Use `[accent]` only for decorative elements and large fills (heading underlines, left borders, dividers, 3px or thicker strokes). Use `[accentText]` for all small text: section eyebrows, prompt labels, copy button text and border, and badge backgrounds that carry white text.

## Prompt copy-to-clipboard buttons

Every prompt shown in a `<pre>` block gets a copy-to-clipboard button, immediately above or to the right of the prompt.

- Inline styles for appearance, matching the handout look: small, rounded, subtle accent border, hover effect
- Accessible text ("Copy prompt") and an aria-label
- A clipboard icon or the word "Copy"
- On click, copy the prompt text and show a brief confirmation ("Copied!")
- Each button uniquely bound to its prompt via a data attribute or unique id
- Button and confirmation hidden when printing, via the `@media print` block
- All JavaScript inline within the main `<div>`; no external files
- **Never overlap the prompt text.** When the button is absolutely positioned inside the prompt block, the `<pre>` must reserve at least `72px` of right padding so wrapped lines never run under it. If that padding cannot be guaranteed, place the button on its own line above the `<pre>` with `text-align: right`.

Reference pattern:

```html
<div style="position: relative; margin-bottom: 18px;">
  <button class="copy-btn" data-target="prompt-1" aria-label="Copy prompt" style="position: absolute; top: 8px; right: 8px; background: #ffffff; border: 1px solid [accentText]; color: [accentText];">Copy</button>
  <span class="copy-confirm" id="confirm-prompt-1" style="display:none; position:absolute; top:10px; right:64px; color:#0d7a3a; font-size:12px;">Copied!</span>
  <pre id="prompt-1" style="background: #f2f2f2; padding: 14px 72px 14px 16px; color: #1a1a1a; border-left: 3px solid [accent]; white-space: pre-wrap; word-wrap: break-word; margin: 0;">Prompt text here</pre>
</div>
```

The `padding: 14px 72px 14px 16px;` on the `<pre>` is required, not optional. Without the 72px right padding, long prompt lines clip behind the Copy button in viewers that wrap at narrower widths.

At the end of the main `<div>`, include a `<script>` block handling all copy button clicks and confirmations, plus the `<style>` block with `@media print` rules hiding `.copy-btn` and `.copy-confirm`.

Do not place Copilot UI instructions inside `<pre>` blocks. Those blocks are reserved for prompt text the participant copies.

## Naming conventions carried into the HTML

Exercise and section titles lead with the business process or scenario, with the Microsoft product or surface in parentheses at the end.

- Correct: "Draft the Interim Business Case (Copilot in Word)", "Screen the Opportunity List (Analyst)"
- Wrong: "Copilot in Word: Draft the Interim Business Case" (product leads, the business scenario is buried)

Apply this in all three places so the handout reads business-first: the `<h2>` section headings, the left-hand nav labels (shorter form, product still in parentheses), and any agenda or session-slides segment names.

## Pre-delivery sweep (mandatory)

Before telling the user the handout is ready, check every item:

1. No em-dash or en-dash characters, and no `&mdash;` or `&ndash;` entities, anywhere in the file.
2. No raw non-ASCII punctuation: sweep for the middle dot, curly apostrophe, curly double quotes, ellipsis, and arrow glyphs, and replace each with its entity.
3. No unresolved `[accent]`, `[accentTint]`, or `[accentText]` placeholders.
4. Every `<td>`, `<th>`, `<strong>`, `<code>`, and `<pre>` carries an explicit `color:` style.
5. No `color: [accent]` or `background: [accent]; color: #fff` pattern applied to small text; those convert to `[accentText]`.
6. The nav rail uses `position: fixed`, with `max-height` and `overflow-y: auto` set, and the main content carries the offsetting left margin.
7. The collapse toggle is present and wired: the focusable, accessibly named `#nav-toggle` checkbox is the first of the four siblings, its label follows, and rail/main content follow both. CSS owns rail state; keyboard Space and pointer activation work. Inline JavaScript owns enhanced desktop width commits and semantic anchor restoration, not a competing rail toggle.
8. Enhanced desktop collapse increases computed main width and opening restores expanded geometry, with capture of visible text node/character Range and scrollport offset BEFORE reflow, settling then bounded instant restoration in both directions. Disable competing automatic anchoring during adjustment; support existing embedded scroll owners. No width/margin transition or repeated scroll fight. Only no-script desktop and mobile assert invariant width/wrapping; mobile overlay geometry is identical in both states. Necessary inline overrides use `!important`.
9. Every `<pre>` prompt block reserves at least 72px right padding when its copy button is absolutely positioned.
10. Audit source placement for each exercise against the supplied files or internal manifest. Every required file is named immediately alongside the exercise using it, with an exact filename/path or verified link, concise open/upload/reference action and short business purpose. Replace legacy Drop-in Content Pack tables and published file blueprints with Inline Sources or merge their entries into existing setup, not a separate source section. Only needed files appear; shared sources use the same saved path, never duplicate copies. Every referenced file actually exists. No centralized source pack/content matrix, mapping table, inventory section, published blueprint, or source-navigation link remains, and no attribution repeats in later exercises or prompts.
11. The brand comment is present at the top of the output.
12. All visible and hidden content passes the participant-only published-content rule. No chat echo, authoring rationale, facilitator/speaker notes, wait/stall/troubleshooting advice, extension offers, or internal validation commentary remains; removed sections have no orphaned nav links.
13. Participant scenario context, setup/click paths, prompts, expected outputs, evidence checks, and essential access/availability information remain intact. Audit literal clipboard text for excluded labels, product comparisons, test controls and generation commentary. Keep only the single `Synthetic` source-metadata label and first-use handout attribution, never prompt directives or repeated narrative. Companion-file cleanup is handed to the authoring skill if outside this formatter's HTML scope.
14. Execute the mandatory mid-document regression matrix in BOTH directions for long prose, table text and wrapped prompts: wide/near-760 desktop enhanced width increases on collapse and restores on open, with SAME character-anchor error at most 1 CSS pixel; no-script desktop and mobile scripts-on/off keep width/wrapping invariant with the same anchor tolerance. Include embedded scroll contexts, keyboard focus, anchors, copy and print. If no runnable sample or interactive surface is available, state tests not run in chat; do not imply a browser pass from source inspection.
15. Check selected-source granularity and actual files/rows/gates against prompts, claimed coverage, run size and timebox. A rollout population is not an analyzed record count; retrieval is not an exhaustive audit. Quantitative claims need the appropriate verified analytical path. Return content mismatches to the authoring skill before delivery; do not mask them with formatting.

Fix any failure before delivering. Do not report the file as ready with an open item.

## Guardrails

- This skill formats and repairs handout HTML. It does not author exercise content, invent scenario facts, or generate synthetic data files.
- Never fabricate company brand colors as fact. If a color is unknown and the user cannot supply one, use a neutral professional palette and say so plainly.
- Never place raw markup in chat as the deliverable. Save the `.html` file and name it.
- Preserve accessibility over branding. When a brand color reduces contrast below AA, darken it rather than shipping the brand value.
- Never modify built-in system skills.

## Example requests

- "Format this Copilot workshop content as a branded HTML handout."
- "The copy buttons in this handout are covering the prompt text, fix it."
- "Rebuild the left nav on this exercise guide, it stopped scrolling in Teams."
- "Collapse the sidebar to widen the reading content, then reopen it without losing my place in the text."
- "Fix the nav collapse: it only shrinks the rail instead of expanding the content, and keep my reading position."
- "Sweep this handout for em-dashes and encoding problems before I send it."
- "Apply the supplied brand colors to this exercise guide and check the contrast."
