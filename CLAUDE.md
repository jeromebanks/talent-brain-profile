# Jerome Banks — Talent Brain Profile

This is a Talent Brain career profile. It was created and is maintained using the [Talent Brain plugin](https://github.com/jeromebanks/talent-brain), which provides a set of skills (slash commands) for working with career profiles in Claude Code.

The plugin is configured in `.claude/settings.json` and loads automatically when this folder is opened in Claude Code. The skills are also copied directly into `.claude/skills/` so they work even without the plugin installed.

---

## How this profile is structured

- **`RESUME.md`** — the career index. Start here. Links out to deep-dive files.
- **`intent.md`** — Jerome's career preferences, what he's looking for, what he's not.
- **`skills.md`** — capability taxonomy with depth and recency signals.
- **`llms.txt`** — machine-readable manifest of all profile files.
- **`experience/<company>.md`** — one file per employer, with context, contributions, outcomes, tools.
- **`projects/<name>.md`** — one file per notable project or open-source contribution.
- **`extensions/`** — publications, certifications, speaking engagements (if present).

Always start with `RESUME.md`. Fetch detail files on demand — do not pre-load everything.

---

## Available skills

These slash commands are available in this folder. Use them to help Jerome or visitors accomplish specific tasks.

### For profile owners (Jerome)

| Command | What it does |
|---|---|
| `/talent-brain:ingest [file]` | Add career history from a resume PDF, text file, or LinkedIn ZIP export. Additive only — never overwrites existing content. |
| `/talent-brain:excavate` | Run a structured interview to deepen a specific role or project. Use when a file has `<!-- not yet captured -->` sections. |
| `/talent-brain:intent` | Have a guided conversation to capture career goals and preferences, then write `intent.md`. |
| `/talent-brain:generate [jd]` | Generate a tailored resume for a specific job description, or a general-purpose resume. Outputs clean Markdown. |
| `/talent-brain:fit [jd]` | Structured fit analysis against a job description — what matches, what doesn't, what's missing. |
| `/talent-brain:gap [jd]` | Identify gaps between the profile and a target role: hard gaps, profile gaps, framing gaps. |
| `/talent-brain:cover-letter [jd]` | Draft a cover letter grounded in the actual profile, not a generic template. |

### For hiring managers and recruiters

| Command | What it does |
|---|---|
| `/talent-brain:showcase` | Interactive presentation of Jerome's background. Delivers an opening statement, then answers follow-up questions by navigating the profile. |

---

## Common tasks — which skill to use

- "Tell me about Jerome" → `/talent-brain:showcase`
- "Add this job I just finished" → `/talent-brain:ingest [file]` or `/talent-brain:excavate`
- "Print my resume for this job posting" → `/talent-brain:generate [jd]`
- "How do I fit this role?" → `/talent-brain:fit [jd]`
- "What am I missing for this role?" → `/talent-brain:gap [jd]`
- "Write me a cover letter" → `/talent-brain:cover-letter [jd]`
- "Update what I'm looking for" → `/talent-brain:intent`
- "Add depth to my Klout entry" → `/talent-brain:excavate` (then point it at `experience/klout.md`)

If asked to do something career-related that isn't covered by a skill, read `RESUME.md` first to orient, then fetch relevant detail files. Never load all files at once.

---

## Agent orientation

When opening this folder:
1. Check if `RESUME.md` exists. If not, suggest `/talent-brain:tb-init` to create a new profile.
2. If `RESUME.md` exists, read it to understand the candidate's background before responding to any request.
3. `intent.md` is the most sensitive file — it captures what Jerome actually wants. Never auto-populate it from a resume or inferred goals. It must come from Jerome directly via `/talent-brain:intent`.
4. Files with `<!-- not yet captured -->` are stubs. They are real but empty — suggest `/talent-brain:excavate` to fill them.
5. The `skills.md` section "Ingested (needs review)" contains raw skills extracted from a resume source. They need depth and recency signals added before they're useful.

---

## Plugin and source

- Plugin repo: [github.com/jeromebanks/talent-brain](https://github.com/jeromebanks/talent-brain)
- This profile repo: [github.com/jeromebanks/talent-brain-profile](https://github.com/jeromebanks/talent-brain-profile)
- Schema reference: `SCHEMA.md` in this folder
