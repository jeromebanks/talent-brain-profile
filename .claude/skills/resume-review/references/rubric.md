# Resume Review Rubric

Use this rubric after extracting the resume once. Keep factual support separate from presentation quality: a statement may be supported yet still be generic, awkward, misleadingly framed, or over-tailored.

## Review packet

Build and reuse one compact packet containing:

1. Extracted resume text and structural-checker JSON
2. Job requirements matrix, when a job description exists
3. Claim/evidence ledger
4. Profile sources actually consulted

Do not load the whole profile once per persona. Add a profile file only when needed to verify a claim, resolve a requirement, or understand the career through-line.

## Job requirements matrix

Use this table when a job description is available:

| ID | Requirement | Priority | Kind | Evidence status | Profile sources | Exact wording useful? |
|---|---|---|---|---|---|---|
| R1 | Concise requirement text | must-have / preferred / contextual | standard term / employer phrase / broad capability / marketing-cultural | strong / adjacent / unsupported / unknown or not yet captured | file and section | yes/no, with reason |

Rules:

- Do not treat repeated wording as proof that exact wording belongs in the resume.
- Use exact standard technology or domain terms when accurate.
- Translate employer-specific phrases into conventional industry language unless the phrase is independently meaningful.
- Preserve unsupported requirements as honest gaps.

## Claim/evidence ledger

Record important claims using this schema:

| Resume claim | Profile source and section | Ownership | Team contribution | Scope/scale | Outcome/adoption | Maturity | Confidence | Qualification needed | Explainable in depth? |
|---|---|---|---|---|---|---|---|---|---|

Allowed maturity values:

- production
- operational or internal
- pilot
- proof of concept
- exploratory
- historical
- unclear

Evidence rules:

- Distinguish work personally performed from systems supported and team outcomes.
- Preserve scale units and metric context exactly.
- Do not combine separate source metrics into a larger implied outcome.
- Do not call a technology production experience merely because it appears in `skills.md`; connect it to actual work.
- Mark absent evidence `unsupported`; mark plausible but uncaptured evidence `unknown or not yet captured` only when the profile contains a genuine placeholder or nearby evidence that makes the distinction warranted.
- Ask whether the candidate could explain each claim naturally, including technical decisions, constraints, and tradeoffs.

## Persona decisions

Complete these in order before synthesizing the overall result.

### 1. ATS/parser auditor

Decision: `PASS`, `PASS WITH WARNINGS`, or `FAIL`.

Evaluate:

- Whether useful text, contact information, roles, companies, and dates are visible
- Conventional section structure and reading order
- Date-format consistency and conservative chronology warnings
- Important supported standard terminology
- Nonstandard or job-description-derived classifications

Do not optimize keyword density. Do not produce a numeric ATS score. Treat structural-checker findings as proxies, not guarantees about a proprietary parser.

### 2. Technical recruiter

Decision: `FORWARD`, `BORDERLINE`, or `DO NOT FORWARD`.

Answer:

- Can level and domain be understood quickly?
- Are must-have qualifications visible without keyword hunting?
- What are the three strongest forwarding signals?
- What creates hesitation?
- Can the recruiter explain the fit to the hiring manager in two sentences?

### 3. Hiring manager

Decision: `INTERVIEW`, `BORDERLINE`, or `PASS`.

Do not decide whether to hire from the resume alone. Evaluate:

- Relevant ownership and scope
- Outcomes, adoption, and operational consequences
- Architectural depth and technical leadership
- Career progression and through-line
- Evidence strong enough to justify an interview slot
- Important evidence that is missing, buried, or obscured

### 4. Skeptical senior engineer

Decision: `DEFENSIBLE`, `DEFENSIBLE WITH EDITS`, or `NOT DEFENSIBLE`.

Identify:

- Inflated, vague, or technically awkward claims
- Production/prototype confusion
- Unsupported technologies
- Statements that require immediate interview qualification
- True claims framed in a misleading way

For each concern, quote the minimum exact language, cite evidence, and recommend the smallest honest correction.

### 5. Human resume editor

Decision: `READY`, `REVISE`, or `REWRITE`.

Identify:

- Artificial or job-description-parroting language
- Nonstandard headings or invented skills categories
- Generic filler and overloaded skills sections
- Bullets that declare capability without evidence
- Important accomplishments displaced by keywords
- Repetitive accomplishment formulas or cadence
- Loss of the candidate's distinctive career narrative

### 6. Authenticity and career-coherence reviewer

Decision: `DISTINCTLY AUTHENTIC`, `CREDIBLE BUT OVER-PROCESSED`, `SYNTHETIC-SOUNDING`, or `CREDIBILITY CONCERNS`.

This is not AI-authorship detection. Evaluate whether the document is a credible account of one real person's career.

#### Evidence authenticity

- Trace every significant claim to Talent Brain evidence.
- Check ownership, scope, maturity, adoption, outcomes, and metric context.
- Distinguish personal work from team accomplishments.
- Connect technologies to where and why they were used.
- Flag invented, suspiciously perfected, unsupported, or overstated claims.
- Ask whether the candidate can explain the bullet naturally and in technical depth.

#### Voice and career authenticity

- Identify a recognizable trajectory across roles and projects.
- Preserve specific systems, constraints, choices, tradeoffs, adoption, and consequences.
- Retain useful continuity from older experience.
- Check that tailoring has not made the candidate implausibly perfect for the target.
- Preserve natural differences among companies, domains, and periods.
- Test whether the summary could describe hundreds of other senior engineers after swapping names and technologies.

Potential synthetic-writing signals include:

- Repeated bullet structure or cadence
- Uniformly polished accomplishment formulas
- Abstract nouns such as leadership, innovation, scalability, and impact without concrete evidence
- Buzzwords or job-description phrases without operational meaning
- Adjectives such as robust, production-grade, seamless, cutting-edge, or highly scalable standing in for evidence
- An implausibly tidy metric or outcome in every bullet
- Technologies listed without showing where or why they were used
- Generic claims that erase actual technical decisions
- Every historical role rewritten as if it anticipated the current job description
- Claims that sound impressive but require immediate qualification
- Compression that removes the complications and boundaries of real work
- Suspicious uniformity across unrelated companies, domains, and periods

Do not penalize:

- Clear, polished writing by itself
- Standard technical terminology or concise bullets
- Natural overlap with the job description
- Missing metrics when trustworthy metrics were never captured
- Honest gaps, prototypes, failed approaches, or qualified outcomes
- Uneven detail when some roles are better documented than others

For every authenticity concern provide:

| Exact resume language | Why it is questionable | Talent Brain evidence | Issue type | Minimal correction | Confidence |
|---|---|---|---|---|---|

Issue type must be `factual`, `framing-related`, `stylistic`, or `uncertain`. Confidence must be `high`, `medium`, or `low`.

Identify three identity-bearing details: accomplishments, decisions, named projects, recurring patterns, or career connections that make the resume recognizably belong to this candidate. Recommend preserving or strengthening them.

Never label a resume fabricated because it is polished or appears AI-assisted. Reserve fabrication for an actual conflict with, or absence of support from, the Talent Brain evidence. Otherwise name the exact issue: generic, over-tailored, synthetic-sounding, unsupported, overstated, or uncertain.

## Veto rules

Reject or flag proposed language when it:

- Merely repeats a job-description phrase
- Creates a nonstandard section or skills category from job-description wording
- Is unsupported by profile evidence
- Obscures production versus prototype status
- Converts adjacent familiarity into deep expertise
- Requires immediate backtracking in an interview
- Replaces a concrete accomplishment with a generic capability claim
- Makes the prose sound less like an experienced human engineer
- Removes high-signal older work solely because it is older
- Narrates an explicit comparison to the job description instead of presenting work naturally
- Makes the candidate implausibly perfect for the position
- Erases role-specific differences through uniform accomplishment formulas
- Weakens the recognizable career through-line

Regression rule:

> `Production Python: FastAPI, Pydantic, MCP servers, internal APIs, evaluation harnesses, pytest`

Flag `Production Python` as a nonstandard, likely job-description-derived heading. Keep supported items under stable categories such as `Languages`, `Frameworks`, `Data and Platform`, or the existing `skills.md` taxonomy. Show production experience primarily through evidence-backed bullets.

## Overall synthesis

Set an overall decision of `ready`, `revise`, or `rewrite`. A factual error, unsupported major claim, material maturity inflation, or parser failure is blocking. Generic phrasing, buried evidence, or minor taxonomy drift is normally nonblocking but can still justify `revise` when it materially weakens interview signal or authenticity.

Do not classify unsupported language as merely synthetic-sounding. `Unsupported` is an evidence-integrity finding. `Synthetic-sounding` is a presentation finding and may apply even when every claim is supported. Keep both labels when both are true.

## Report format

Write sections in this order:

1. Overall decision
2. Persona decisions
3. Three strongest signals
4. Blocking problems
5. Important but nonblocking improvements
6. Claims requiring qualification
7. Missing or obscured Talent Brain evidence
8. ATS/parser observations
9. Artificial or keyword-stuffed language
10. Authenticity and career-coherence assessment
11. Identity-bearing details that should be preserved
12. Material that should not be added
13. Prioritized minimal revision brief
14. Evidence references to profile files
15. Limitations

Include this machine-readable summary near the top, using lowercase kebab-case values:

```yaml
overall:
  decision: revise
  interview_signal: borderline
  evidence_integrity: pass-with-concerns

personas:
  ats_parser: pass
  technical_recruiter: forward
  hiring_manager: borderline
  skeptical_engineer: defensible-with-edits
  human_editor: revise

authenticity:
  decision: credible-but-over-processed
  evidence_integrity: pass-with-concerns
  career_coherence: strong
  distinctive_voice: weak
  synthetic_signals: []
  credibility_concerns: []
  identity_bearing_details: []
  confidence: medium
```

End the limitations section with both statements:

- This review is a parser-safety proxy, not a proprietary ATS simulation.
- This review evaluates evidence and writing signals; it is not an AI-authorship detector.
