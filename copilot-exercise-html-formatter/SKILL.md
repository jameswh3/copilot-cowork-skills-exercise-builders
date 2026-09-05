---
name: copilot-exercise-html-formatter
description: |
  Produce and repair the styled HTML handout format used for Microsoft Copilot demo exercises, workshop guides, and enablement session content: brand color resolution, executive handout layout, collapsible left nav rail, copy-to-clipboard prompt blocks, WCAG AA contrast, and ASCII-safe punctuation encoding. Use when the user asks to "format this exercise as an HTML handout", "style the workshop guide", "apply brand colors to the handout", "add copy buttons to the prompts", "fix the contrast in the handout", "clean up the em-dashes and encoding", "rebuild the nav rail", "make the sidebar collapsible", or when another Copilot exercise skill needs its HTML rendered. Do NOT use to invent exercise content (use copilot-se-demo-builder or copilot-cowork-exercise-builder), to build general web pages or apps, or to produce Word, PowerPoint, or Excel deliverables.
metadata:
  category: writing
  icon: Code
---

# Copilot Exercise HTML Formatter

This skill owns the presentation layer for Copilot demo and workshop content. It does not decide what an exercise says. It decides how the handout looks, encodes, and behaves.

Two skills call it: `copilot-se-demo-builder` and `copilot-cowork-exercise-builder`. It also runs standalone when the user hands over existing exercise content and asks for a handout, or asks to fix an existing one.

## When NOT to Use

- The user needs exercise content authored, not styled: use `copilot-se-demo-builder` (scenario exercises) or `copilot-cowork-exercise-builder` (Cowork exercises).
- The user wants a general-purpose web page, landing page, or interactive app: use the `create` skill instead.
- The user wants a Word, PowerPoint, Excel, or PDF deliverable: use `docx`, `pptx`, `xlsx`, or `pdf` instead.
- The user wants synthetic sample data files generated: that belongs to the calling exercise skill.

## Required workflow

1. **Confirm the output format.** HTML (styled handout) is the default for all Copilot exercise content. Only produce plain text when the user explicitly asks for it. Do not ask which format; assume HTML.
2. **Resolve brand colors** (see Brand resolution below). Never emit `[accent]`, `[accentTint]`, or `[accentText]` placeholders into a finished file.
3. **Build the handout** using the layout, punctuation, accessibility, and copy-button rules below.
4. **Sweep before delivery** (see Pre-delivery sweep). This step is mandatory, not optional.
5. **Save the HTML as a downloadable `.html` file.** Never dump the markup into chat as a code block.

## Brand resolution

Resolve brand colors before generating any HTML when a company is named.

- Use a brand color only when it comes from an authoritative public brand source or user-provided brand guidance. Do not infer a company's color from memory.
- Derive `[accentTint]` as the accent blended with white at roughly 10% opacity (for example `#0078D4` becomes `#e6f2fb`).
- Derive `[accentText]` as a darkened variant of `[accent]` reaching at least 4.5:1 contrast against both `#ffffff` and `#fafafa`. Bright brand colors (orange, magenta, gold, lime) typically need 40-50% darkening to meet AA.
  - Worked examples: `#F36F21` becomes `#8C3D11`; `#FF6600` becomes `#B23A00`; `#E20074` becomes `#8C0048`.
  - For colors already dark enough (`#0078D4`, `#003087`), `[accentText]` can equal `[accent]`.
- If the company's brand colors are not known, ask one brief question: "Do you have a primary brand color or company website I should use for styling?"
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
- Two-column layout: a left-hand navigation rail plus a right-side main content area (`flex: 1`, `max-width: 980px`, left padding around 24px).
- **Use `position: fixed` for the nav rail, never `position: sticky`.** Sticky inside a flex row breaks page scrolling in M365 and Cowork preview panes. Give the fixed nav `max-height: calc(100vh - 32px); overflow-y: auto;` and offset the main content with a left margin around 288px.
- **The nav rail is collapsible, and the toggle is pure CSS.** Build it with the checkbox pattern in "Collapsible left nav" below. Never drive the collapse from JavaScript.
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

## Collapsible left nav (pure CSS, no JavaScript)

Every handout with a fixed left nav rail gets a toggle button that collapses the rail and lets the main content reclaim the freed width. Build it with the checkbox pattern below, never with a script. Some renderers and preview panes strip or block inline scripts, and a collapse that depends on JavaScript silently stops working in exactly the viewers the handout is written for. The copy buttons still use JavaScript because copy has no CSS-only equivalent; the collapse does, so it uses it.

The mechanism is the checkbox hack: a hidden checkbox holds the state, CSS reacts through `:checked`, and a `<label for="...">` is the clickable button. Labels toggle their associated checkbox natively.

### Structure (this exact order, all siblings under the same parent)

1. A hidden `<input type="checkbox" id="nav-toggle">`. Visually hidden through `opacity: 0`, a 1px box, and `pointer-events: none`, but present and never `display: none`, so it stays in the accessibility and interaction tree.
2. A `<label for="nav-toggle" id="nav-toggle-btn">` styled as the visible button: fixed position, small rounded square, an arrow glyph such as `&lsaquo;`, `cursor: pointer`, and an `aria-label` of "Toggle navigation".
3. The nav rail container, `<div id="side-nav">`: fixed position, fixed width (typically 264px).
4. The main content container, `<div id="main-content">`: the offsetting `margin-left` that clears the rail.

```html
<input type="checkbox" id="nav-toggle" style="position: fixed; opacity: 0; width: 1px; height: 1px; pointer-events: none;" />
<label for="nav-toggle" id="nav-toggle-btn" aria-label="Toggle navigation" style="position: fixed; top: 16px; left: 240px; z-index: 20; width: 26px; height: 26px; border-radius: 6px; background: #ffffff; border: 1px solid [accentText]; color: [accentText]; text-align: center; line-height: 24px; font-size: 16px; cursor: pointer;">&lsaquo;</label>
<div id="side-nav" style="position: fixed; width: 264px; max-height: calc(100vh - 32px); overflow-y: auto;">...</div>
<div id="main-content" style="margin-left: 288px; max-width: 980px;">...</div>
```

### CSS (in the single `<style>` block)

```css
#side-nav, #main-content, #nav-toggle-btn {
  transition: transform 0.2s ease, opacity 0.2s ease, margin-left 0.2s ease, max-width 0.2s ease, left 0.2s ease;
}
#nav-toggle:checked ~ #side-nav {
  transform: translateX(-280px);
  opacity: 0;
  pointer-events: none;
}
#nav-toggle:checked ~ #main-content {
  margin-left: 24px !important;
  max-width: none !important;
}
#nav-toggle:checked ~ #nav-toggle-btn {
  left: 16px !important;
  transform: scaleX(-1);
}
```

`transform: scaleX(-1)` flips the arrow glyph so it points the other way when collapsed. Keep the collapsed `translateX` value at least as large as the rail width plus its left offset, so no sliver of the rail remains visible.

### Two things that are easy to get wrong

- **The checkbox must come first in the DOM.** The general sibling combinator (`~`) only reaches elements that appear after the checkbox at the same nesting level. A checkbox placed after the rail, or nested one level deeper, matches nothing and the toggle does nothing.
- **Inline styles beat these selectors, so add `!important` where they collide.** This skill styles layout inline, so `margin-left`, `max-width`, and `left` are typically set as inline attributes on the rail, the content, and the button. An inline declaration wins over any stylesheet rule regardless of specificity. Put `!important` on exactly the properties that conflict with an inline style, and on nothing else.

Net effect: clicking the label toggles the checkbox, CSS reacts to `:checked`, the rail slides out and fades, the content margin collapses to reclaim the space, and the button slides to the left edge with its arrow flipped, with zero JavaScript.

Hide the toggle button when printing by adding `#nav-toggle-btn` to the `@media print` rules alongside `.copy-btn` and `.copy-confirm`.

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
7. The collapse toggle is present and wired: the hidden `#nav-toggle` checkbox is the first of the four siblings, the `<label for="nav-toggle">` follows it, and `#side-nav` and `#main-content` come after both. No JavaScript drives the collapse.
8. Every `:checked ~` rule carries `!important` on each property that is also set inline (`margin-left`, `max-width`, `left`), and on no other property.
9. Every `<pre>` prompt block reserves at least 72px right padding when its copy button is absolutely positioned.
10. Every named file referenced in the handout actually exists as a saved artifact.
11. The brand comment is present at the top of the output.

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
- "Add a button that collapses the sidebar so the content gets the full width."
- "Sweep this handout for em-dashes and encoding problems before I send it."
- "Apply the supplied brand colors to this exercise guide and check the contrast."
