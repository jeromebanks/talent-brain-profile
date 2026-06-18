# Jerome Banks — Career Profile

This is Jerome's career profile, built and maintained with [Talent Brain](https://github.com/jeromebanks/talent-brain) — a Claude Code plugin for managing career profiles as structured, agent-navigable repositories.

---

## For hiring managers and recruiters

Open this folder in [Claude Code](https://claude.ai/code) and run:

```
/talent-brain:showcase
```

You'll get an interactive presentation of Jerome's background — an opening statement built around his through-line and strongest signals, followed by Q&A where you can ask about anything: specific roles, technical decisions, leadership, fit for a particular problem.

No setup required. The plugin loads automatically.

---

## For Jerome (profile owner)

### Quick reference

| What you want to do | Command |
|---|---|
| Add a new job or resume | `/talent-brain:ingest [file]` |
| Deepen a role with a structured interview | `/talent-brain:excavate` |
| Update career goals and preferences | `/talent-brain:intent` |
| Generate a resume for a job posting | `/talent-brain:generate [jd]` |
| Check fit against a role | `/talent-brain:fit [jd]` |
| Find gaps for a target role | `/talent-brain:gap [jd]` |
| Draft a cover letter | `/talent-brain:cover-letter [jd]` |

### What needs attention now

- **`intent.md`** — not yet filled in. Run `/talent-brain:intent` to capture what you actually want next. This is the most valuable file for job search.
- **`skills.md`** — has an "Ingested (needs review)" section with ~30 skills extracted from your resume. Add depth and recency signals, then move them to the right sections.
- **Experience files** — most have `<!-- not yet captured -->` in Outcomes, Decisions & Tradeoffs, and Team & Scope sections. Use `/talent-brain:excavate` to fill these in for roles you want to highlight.

---

## What's in this repo

```
RESUME.md               Career index — start here
intent.md               What Jerome is looking for (fill this in)
skills.md               Capability taxonomy
llms.txt                Machine-readable manifest for agents

experience/
  onyx-gsk.md           Senior Data Platform Engineer, Onyx GSK (2023–present)
  apixio.md             Staff Software Engineer, Data Platform, Apixio (2022–2023)
  tatari.md             Staff Data Platform Engineer, Tatari (2021–2022)
  demandbase.md         Principal Big Data Engineer, Demandbase (2018–2021)
  jumpshot.md           Senior Software Engineer, Jumpshot/Avast (2016–2018)
  stitchfix.md          Data Platform Engineer, StitchFix (2015–2016)
  ifwe.md               Senior Software Engineer, Tagged.com/if(we) (2014–2015)
  klout.md              Senior Software Engineer, Klout (2011–2014)
  quantcast.md          Senior Software Engineer, Quantcast (2008–2011)
  prior-experience.md   Earlier roles (pre-2008)

projects/
  brickhouse.md         Brickhouse — open-source Hive UDF library
  satisfaction.md       Satisfaction — next-generation Hadoop batch scheduler
```

---

## Background

Jerome is a Senior Data Platform Engineer with 15+ years of experience in Big Data, distributed systems, and cloud data infrastructure. He's worked across ad tech, social media, healthcare, and pharma — at companies including Klout, StitchFix, Demandbase, and currently GSK.

He founded [Brickhouse](http://github.com/klout/brickhouse), a widely-used open-source Hive UDF library, and [Satisfaction](http://github.com/ifwe/satisfaction), a Hadoop batch scheduler. He's an Apache Committer ([Hivemall](https://hivemall.incubator.apache.org/)) and holds a BS in Engineering & Applied Science from Caltech.

---

## Built with Talent Brain

This profile was created using the [Talent Brain plugin](https://github.com/jeromebanks/talent-brain) for Claude Code. Talent Brain is an open plugin — anyone can use it to create and manage their own career profile.
