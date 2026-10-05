---
name: generate
description: Generate a tailored resume for a specific job description, or a general-purpose resume if no JD is provided. Pulls from the full profile depth and positions the candidate's experience for the target role. Outputs an ATS-safe HTML file, auto-converted to PDF via whatever CLI tool is available (headless Chrome/Chromium, wkhtmltopdf, or pandoc), no manual steps required. Use when a candidate needs a resume document to send or upload.
---

# Talent Brain — Generate Resume

You are generating a resume document from the candidate's Talent Brain profile. The output is tailored to a specific role if a JD is provided, or optimized as a strong general-purpose resume if not.

**ATS-legibility beats cosmetics.** This tool exists partly to fight the failure mode where AI screeners misparse a visually "designed" resume and lose the signal in it. Every choice in this skill — layout, formatting, the conversion pipeline — optimizes for a parser reading the text cleanly, not for a human admiring the typography. Plain and correct beats polished and fragile.

## Inputs

- `/generate` — generate a general-purpose resume
- `/generate "senior ML engineer at fintech startup"` — generate tailored to a context description
- `/generate [file or URL]` — generate tailored to a specific job description

If a JD is provided as a file path or URL, read/fetch it first.

## Phase 1 — Load the full profile

Read all of the following before generating anything:
1. `RESUME.md` — index, summary, experience list
2. `intent.md` — direction and preferences (informs the summary and objective). Only "Most Important Factors," "What I'm Not Interested In," and "Where I'm Going" are resume material — never pull from "Reasons for the Move," "Availability & Job Search Activity," or "Work Authorization" into resume text. Those sections don't belong on a resume regardless of source.
3. `skills.md` — full capability taxonomy
4. **All** `experience/*.md` files — you need the depth, not just summaries
5. **All** `projects/*.md` files — select the most relevant

Unlike other skills, generate reads everything upfront. A resume that only draws from summaries will be generic and weak.

## Phase 2 — If a JD was provided: run fit mapping

Before generating, identify:
- Which requirements from the JD are strongly met → lead with these
- Which experience files are most relevant → feature more prominently
- Which projects are most relevant → include; deprioritize others
- Which skills should be surfaced → map accurate standard terminology to the stable taxonomy in `skills.md`; do not turn unusual JD wording into resume taxonomy
- What the 2-line summary should emphasize → the candidate's strongest fit signal for this role
- Which adoption, reusable abstractions, scope, technical leadership, and identity-bearing details make the candidate's case distinctive → preserve these even when the JD does not name them

Treat ATS parseability and keyword matching as separate concerns. Prefer a coherent career argument over exhaustive requirement-by-requirement mirroring. Exact JD wording is useful only when it is standard industry terminology that accurately represents the candidate's evidence.

If no JD: identify the top 3 signals from the profile overall and build the summary around them.

## Phase 3 — Generate the content

### Content rules

- Target length: 1 page for < 10 years experience, 2 pages for longer careers. Flag if the output is running long.
- Contact line at top: name | location | email | linkedin | github (omit blanks). If `RESUME.md` frontmatter lists multiple emails, use the first one listed as primary — don't guess or default to whichever looks more "professional."
- Use the candidate's exact company names and titles from the profile — never paraphrase or invent.
- Dates: `MM/YYYY – MM/YYYY` or `MM/YYYY – Present`. Consistent format throughout.
- Consistent tense: past tense for past roles, present tense for the current role, throughout.
- Keep production, operational/internal, pilot, proof-of-concept, and exploratory work explicitly distinguishable.
- Use standard industry terminology. Never copy an unusual JD phrase into a heading, category, title, or claim merely to increase lexical overlap.

### Summary / Professional Profile (3–4 sentences)

Lead with the through-line: what this person is, what they're known for, what they're heading toward. If a JD was provided, open with the fit signal. Do not use generic filler ("results-driven professional", "dynamic leader"). Every sentence must contain a specific claim.

For targeted resumes: the summary should make the fit obvious in the first two sentences.

Before rendering, check whether the summary could describe hundreds of interchangeable candidates after swapping names and technologies. If so, replace generic framing with supported identity-bearing details and a recognizable career through-line.

### Skills section

Pull from `skills.md` and preserve its stable skills taxonomy. For targeted resumes, reorder, select, or omit existing categories as needed, but do not invent categories from JD wording. Use the JD's vocabulary only when it is both accurate and a conventional industry term. Do not list skills the candidate doesn't have just because the JD asks for them.

Group by domain. Keep depth signals (`expert`, `proficient`) if the format allows; drop them if space is tight. Omit `historical` skills unless directly relevant.

Demonstrate a requirement through evidence-backed accomplishments before declaring it as a capability in the skills section. For example, never create a `Production Python` category because a JD uses that phrase; keep supported items under conventional categories such as `Languages`, `Frameworks`, `Data and Platform`, or an existing `skills.md` heading, and show production experience in the relevant bullets.

### Experience section (reverse chronological)

For each role:
1. Read the full `experience/<slug>.md` — do not rely on the RESUME.md summary alone
2. For each `### Initiative` sub-section in Contributions, generate one resume bullet
3. For targeted resumes: select the most relevant initiatives first; omit or compress less relevant ones
4. Each bullet is synthesized from the atom fields: lead with `impact` if present, then `what`, with `stack` woven in naturally. The LLM picks the right verb from the nature of the work — do not force "developed" or any single verb
5. Use numbers wherever `impact` contains them. Do not invent metrics.
6. For `Responsibilities` sub-sections: generate a brief bullet describing the ongoing operational scope
7. If `impact` is `<!-- not yet captured -->`: generate from `what` and `stack` alone — omit "improved X" framing since you have no number to back it
8. Preserve role-specific constraints, decisions, adoption, and maturity instead of forcing every bullet into the same accomplishment formula
9. Do not rewrite historical roles in the vocabulary of the current JD; preserve natural differences among companies, domains, and periods

For roles more than 15 years old: 2–3 bullets maximum, summary-level only, unless the role has specific high-relevance to the target.

### Projects section

Include 2–3 projects maximum. For targeted resumes: pick the most relevant. For general: pick the highest-signal.

Each project: name, type, 1-sentence description, 2 bullets with outcomes.

### Education

Institution, degree, year. One line per entry. No GPA unless exceptional and recent.

### Extensions

If the profile has extensions (publications, patents, open source, speaking): include a brief section if relevant to the target role. Omit if not.

## Phase 4 — Render as ATS-safe HTML

Write a single, self-contained HTML file. This is the step that determines whether a parser can read the resume, so follow it exactly — do not add anything in the name of making it "look nicer."

**Structure:**
- One column. No CSS grid/flexbox columns, no sidebars, no tables for layout.
- Semantic tags only: `<h1>` for name, `<p>` for the contact line, `<h2>` for section headers (Summary, Experience, Skills, Projects, Education), `<h3>` for role/company headers, `<ul><li>` for bullets.
- Reading order in the HTML source must match visual reading order — no absolute positioning, no CSS that reorders content.
- Real text only. No text embedded in images, no icons, no emoji standing in for words.
- No headers/footers, no page-numbering tricks, no decorative borders or background colors/shading.

**Minimal CSS budget** (inline `<style>` in `<head>`, nothing else): font stack, font size, line-height, margins, and heading weight. That's it. Something like:

```html
<style>
  body { font-family: Georgia, 'Times New Roman', serif; font-size: 11pt; line-height: 1.4; color: #000; max-width: 7.5in; margin: 0.5in auto; }
  h1 { font-size: 18pt; margin-bottom: 0.1em; }
  h2 { font-size: 13pt; border-bottom: 1px solid #000; margin-top: 1em; }
  h3 { font-size: 11.5pt; margin-bottom: 0.1em; }
  ul { margin-top: 0.2em; padding-left: 1.2em; }
  @page { margin: 0.6in; }
</style>
```

Adjust font size/margins only as needed to hit the target page count — never by cutting content in a way that omits real experience.

## Phase 5 — Advisor review (tailored resumes only)

If a JD was provided (a tailored resume), call the `advisor` tool once the HTML is written, before converting to PDF. Skip this phase for general-purpose resumes (no JD) — advisor review is for the higher-stakes, JD-specific case.

The advisor sees the full conversation, including the JD and the resume HTML just written. Ask it to check two things explicitly:
1. **Correctness** — every claim, number, and framing term traces back to the profile with no exaggeration, unit inflation, double-counting, or misapplied terminology (e.g., don't call a multidimensional-aggregation library a "lakehouse pattern"). Flag anything that reads as keyword-padding echoing the JD's language without profile backing.
2. **Persuasiveness** — does the resume make the strongest honest case for this specific role? Is the summary's opening claim the right one? Are the most JD-relevant bullets surfaced first per role?

Apply correctness fixes to the HTML before moving on — these aren't optional. Treat persuasiveness notes as advisory; use judgment on whether to act on them. If a flagged number or fact traces back to the profile's own source files rather than something introduced during generation, don't silently edit it — that's a profile data question, not a resume-wording one. Surface it to the user instead.

This is one bounded preflight, not a repeated review/rewrite loop. Do not repeatedly call the advisor or automatically rerun generation until it approves. A resume can be sentence-by-sentence defensible and still need revision if it reads as generic, over-processed, implausibly perfect for the JD, or synthetic-sounding.

## Phase 6 — Convert to PDF automatically

Detect an available converter and use it — never ask the user to open a browser or convert anything by hand. Check in this order and use the first match:

```bash
detect_pdf_tool() {
  for c in chromium chromium-browser google-chrome google-chrome-stable; do
    command -v "$c" >/dev/null 2>&1 && { echo "$c"; return; }
  done
  for p in "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
           "/Applications/Chromium.app/Contents/MacOS/Chromium"; do
    [ -x "$p" ] && { echo "$p"; return; }
  done
  command -v wkhtmltopdf >/dev/null 2>&1 && { echo "wkhtmltopdf"; return; }
  command -v pandoc >/dev/null 2>&1 && { echo "pandoc"; return; }
  echo ""
}
```

Conversion command depends on which tool was found:
- **Chrome/Chromium** (binary or app path): `"$TOOL" --headless --disable-gpu --no-pdf-header-footer --print-to-pdf="<output>.pdf" "file://$(pwd)/<output>.html"`
- **wkhtmltopdf**: `wkhtmltopdf "<output>.html" "<output>.pdf"`
- **pandoc**: `pandoc "<output>.html" -o "<output>.pdf"`
- **Nothing found**: skip conversion, keep the HTML file, and tell the user plainly which tool would unlock automatic PDF export (e.g., "Install Chrome or run `brew install pandoc` to get an automatic PDF next time — for now, open `resume.html` in any browser and use Print → Save as PDF"). This is a fallback for a machine with no converter, not the default path.

After conversion, confirm the PDF actually has a real text layer, not a raster image — spot-check by noting the file was produced via a tool that renders live HTML/text (all of the above do); no separate verification step needed beyond confirming the command exited successfully and the file exists with nonzero size.

## Output

**Name in the filename.** Every PDF a recipient sees must carry the candidate's name, so it doesn't get lost among other `resume.pdf` downloads. Build `<name-slug>` from `RESUME.md`'s frontmatter `name`: lowercase, spaces and punctuation collapsed to single hyphens (e.g. `"Jerome Banks"` → `jerome-banks`). Never hard-code a name.

- **No JD (general-purpose):** write `resume.html` and `resume.pdf` to the profile root, overwriting any existing versions, then copy `resume.pdf` byte-for-byte to `<name-slug>-resume.pdf` (`cp resume.pdf <name-slug>-resume.pdf` — copy, don't re-render, so the two are guaranteed identical). `resume.pdf` stays as the stable path referenced by `/publish`, `llms.txt`, and links already shared; `<name-slug>-resume.pdf` is the one to attach or send.
- **JD provided (tailored):** write to `resumes/<name-slug>-resume-<company-or-role-slug>.html` / `.pdf` (create the `resumes/` directory if it doesn't exist) — do not overwrite the canonical root files, and do not commit these to the profile repo; they're one-off artifacts for a specific application.

Print a short summary:

```
✓ Generated

  HTML → [path]
  PDF  → [path]  (via [tool used])
  PDF  → [<name-slug>-resume.pdf path]  (identical copy — general-purpose only)

ATS notes: [any concerns, or "none identified"]

To regenerate with a different target: /generate [new jd]
To run the evidence-grounded persona review: /resume-review [resume] [jd]
```

## Hard invariants

1. **Never invent.** Every bullet, metric, and claim must come from the profile. If the profile is thin on a role, the resume will be thin on it too. The fix is `/excavate`, not fabrication.
2. **Use actual titles and company names.** Do not paraphrase, improve, or modernize them.
3. **Do not include skills the candidate doesn't have** even if the JD asks for them.
4. **Read the full experience files, not just summaries.** The depth is there for a reason.
5. **ATS-safety overrides visual preference.** Single column, semantic HTML, minimal CSS, real text — no exceptions for a "nicer-looking" layout.
6. **Writes only resume output files** (`resume.html`/`resume.pdf`/`<name-slug>-resume.pdf` at the profile root, or their job-specific variants under `resumes/`) — never touches `RESUME.md`, `intent.md`, `skills.md`, or any `experience/`/`projects/` file.
7. **JD language is not resume taxonomy.** Preserve conventional headings and the stable `skills.md` categories; lexical overlap never justifies artificial wording.
8. **Preserve a recognizable career.** Keep identity-bearing details, honest limitations, and work-maturity boundaries; do not make every role or bullet sound uniform.
