# Talent Brain Profile - Codex Instructions

This repository is a Talent Brain career profile. Use the existing profile
documents as the source of truth instead of duplicating their contents here.

## Start Here

1. Read [CLAUDE.md](CLAUDE.md) for the profile structure, available commands,
   and agent orientation.
2. Read [RESUME.md](RESUME.md) first for any profile or candidate question.
   It is the career index and links to detail files.
3. Read detail files only as needed:
   - [intent.md](intent.md) for career preferences and constraints
   - [skills.md](skills.md) for capability taxonomy
   - [llms.txt](llms.txt) for the machine-readable file manifest
   - `experience/*.md` for employer-specific evidence
   - `projects/*.md` for project-specific evidence
4. Use [SCHEMA.md](SCHEMA.md) as the contract for profile file structure.

## Talent Brain Skills

The canonical workflow is defined by the bundled skills in [.claude/skills](.claude/skills).
When a user asks for one of these workflows, follow the matching skill
instructions:

- `/showcase` - present the profile to a recruiter or hiring manager
- `/ingest [file]` - add source material additively
- `/excavate` - conduct a structured interview before editing profile files
- `/intent` - capture career intent directly from the owner
- `/generate [jd]` - produce ATS-safe resume HTML/PDF
- `/resume-review [resume] [jd]` - review a resume through evidence, parser, recruiter, hiring-manager, technical, editorial, and authenticity perspectives
- `/fit [jd]` - assess fit against a job description
- `/gap [jd]` - classify hard, profile, framing, and intent gaps
- `/cover-letter [jd]` - draft a grounded cover letter
- `/publish` - refresh generated artifacts and publish the profile

If the local bundled skills differ from the plugin source, prefer the bundled
profile copy unless the user explicitly asks to update from the plugin.

## Hard Rules

- Never invent profile claims, metrics, preferences, credentials, or intent.
- Do not infer `intent.md` from resumes, LinkedIn exports, or experience files.
  Career intent must come directly from Jerome through `/intent`.
- Preserve evidence links. Claims in generated resumes, fit assessments,
  showcase answers, and cover letters must trace back to profile files.
- Treat `<!-- not yet captured -->` as a real placeholder, not as permission to
  fill from guesswork. Suggest `/excavate` or `/intent` as appropriate.
- Do not read or publish `intent-private.md` unless the user is explicitly
  updating private compensation notes. It is not resume, showcase, or publish
  material.
- Source files such as `source/`, resume PDFs, and LinkedIn exports may contain
  private data. Do not add them to generated public material unless the profile
  content already captures the relevant fact.

## Editing Guidance

- For normal profile questions, work read-only.
- For writing workflows, show proposed content before editing when the relevant
  skill requires approval.
- `/ingest` is additive only: create missing files, fill placeholders, or append
  supplementary blocks. Do not overwrite human-written sections.
- `/excavate` and `/intent` are conversational workflows. Ask one question at a
  time, synthesize after the conversation, then get approval before writing.
- `/generate` may overwrite the canonical `resume.html` and `resume.pdf` (plus
  the identical `<name-slug>-resume.pdf` copy) for a general resume. Tailored
  resumes use `resumes/<name-slug>-resume-<slug>.*`.
- `/publish` may update generated artifacts and commit/push profile changes, but
  should still run the review pass described in the skill instructions.

## Command Usage

Follow the repository-level shell convention from the user instructions: prefix
shell commands with `rtk` when available. If debugging requires raw command
output, use the raw command deliberately.
