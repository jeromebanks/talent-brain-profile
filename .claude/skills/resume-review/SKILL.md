---
name: resume-review
description: Review a generated or existing resume against a job description and a Talent Brain profile using ATS/parser, recruiter, hiring-manager, senior-engineer, human-editor, and authenticity perspectives. Use when evaluating whether a PDF, HTML, Markdown, or text resume is evidence-grounded, persuasive, technically defensible, naturally written, and coherent without letting job-description keywords take over the candidate's voice.
---

# Talent Brain — Resume Review

Review the resume; do not rewrite it by default. Use one bounded host-agent pass for every perspective. Do not spawn persona agents, call an external model or API, recursively invoke this skill, or run a review/rewrite loop. Make at most one revision pass, and only when the user explicitly requests it.

Read [references/rubric.md](references/rubric.md) completely before making semantic judgments. Use [scripts/check_resume_structure.py](scripts/check_resume_structure.py) only for deterministic extraction and parser-safety proxies; the active host agent performs all evidence, persuasion, and authenticity analysis.

## Inputs

Accept:

- A resume in PDF, HTML, Markdown, or plain text
- A job description as a file or pasted text
- The current Talent Brain profile as the evidence source

If no resume path is supplied, inspect the current directory for obvious resume artifacts. Prefer an exact job-specific stem when one exists. If several plausible resumes remain, ask which one to use. Do not silently choose among ambiguous inputs.

If no job description is supplied, continue and state that job-specific fit, priority, and terminology coverage were not evaluated. Never infer a job description from the resume.

Treat `RESUME.md`, `skills.md`, `llms.txt`, and relevant files under `experience/`, `projects/`, and `extensions/` as profile evidence. Read `intent.md` only when target direction or constraints matter. Never read `intent-private.md`. Do not modify profile evidence files.

## Python environment

Use the profile-root `.venv` for every Python checker, test, and validation command. Do not install packages into the system Python or run this skill's code with bare `python` or `python3` after bootstrap.

If `.venv/bin/python` does not exist, initialize the environment from the profile root and install the declared development dependencies:

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements-dev.txt
```

If the environment already exists, reuse it. Do not recreate it or reinstall dependencies on every review.

## Phase 1 — Extract and inspect

Run the checker with the profile virtual environment. Resolve the checker path relative to this `SKILL.md`; this profile's canonical path is shown below:

```bash
.venv/bin/python .claude/skills/resume-review/scripts/check_resume_structure.py <resume-path> --pretty
```

Run that command from the profile root. If the skill is installed at a different location, keep `.venv/bin/python` rooted in the profile and substitute the actual skill directory for `.claude/skills/resume-review`. Keep the JSON result in the working context; do not upload the resume. Describe the result as a parser-safety proxy, never as a proprietary ATS simulation or universal ATS score.

If PDF extraction fails because `pdftotext` is unavailable, report the exact limitation and ask for an HTML, Markdown, or text version, or for local installation of Poppler. Do not substitute OCR, cloud extraction, or a model API silently.

## Phase 2 — Analyze the job description

When a job description exists, build one compact requirements matrix using the schema in the rubric. Separate must-have, preferred, and contextual requirements. Classify each item as a standard term, employer-specific phrase, broad capability, or marketing/cultural language. Decide whether exact wording is useful; repetition in the job description is not sufficient reason to copy it.

## Phase 3 — Build the evidence ledger

Extract the important resume claims once. Load only the profile files needed to verify those claims and the highest-priority job requirements. Reuse this ledger for all personas; do not reread the profile separately for each perspective.

For each significant claim, record its source and distinguish personal ownership, supported systems, team results, scale, outcome, and maturity. Use `unknown or not yet captured` when evidence is absent or a placeholder is present. Do not turn adjacent familiarity into deep expertise or a prototype into production work.

## Phase 4 — Review sequentially

Complete these perspectives in order, keeping each decision logically distinct while using the same review packet:

1. ATS/parser auditor
2. Technical recruiter
3. Hiring manager
4. Skeptical senior engineer
5. Human resume editor
6. Authenticity and career-coherence reviewer

The personas diagnose; they do not independently rewrite. Follow each decision scale and required questions in the rubric. A polished resume is not evidence of AI authorship. Call language fabricated only when it conflicts with, or lacks support from, the profile; otherwise use precise terms such as generic, over-tailored, synthetic-sounding, unsupported, overstated, or uncertain.

## Phase 5 — Apply vetoes

Flag language that merely parrots the job description, invents a resume taxonomy, obscures work maturity, erases ownership boundaries, replaces evidence with capability claims, makes every role sound alike, or weakens the recognizable career through-line.

Always flag a skills label such as `Production Python` when it was derived from job-description wording. Preserve supported Python tools under the profile's stable conventional taxonomy, and demonstrate production use in evidence-backed accomplishment bullets.

Preserve honest gaps and high-signal older work. Prefer the smallest correction that keeps the underlying accomplishment.

## Phase 6 — Write the report

Write `<resume-stem>-review.md` beside a job-specific resume unless the repository already uses a clearer application-artifact location for that stem. Do not overwrite the resume. Follow the report order and structured summary in the rubric, including file-and-section evidence references.

Conclude with a prioritized minimal revision brief. Do not produce a wholesale rewrite unless the user explicitly asks for one. State both limitations:

- This is a parser-safety proxy, not a proprietary ATS simulation.
- This evaluates evidence and writing signals; it does not detect AI authorship.

## Hard invariants

1. Ground every substantive recommendation in the resume, job description, or named profile evidence.
2. Never invent claims, metrics, technologies, intent, or missing evidence.
3. Keep production, operational/internal, pilot, proof-of-concept, exploratory, historical, and unclear work distinguishable.
4. Treat ATS parseability and keyword matching as separate concerns.
5. Prefer coherent career evidence over exhaustive requirement mirroring.
6. Do not modify `RESUME.md`, `intent.md`, `skills.md`, `experience/`, `projects/`, or `extensions/`.
7. Do not require an OpenAI or Anthropic API key and do not invoke `codex`, `claude`, or another model process.
8. Use the profile-root `.venv/bin/python` for all Python execution after environment bootstrap.
