# Jerome Banks

For over 15 years, Jerome has been the engineer companies bring in when a large-scale data problem needs to become production infrastructure — from Hadoop-era batch pipelines at web-audience-measurement scale, through Spark and cloud-native streaming, to today's AI-assisted scientific workflow engineering at GSK. He's repeatedly stood up big data capability from nothing (Tatari, Demandbase, Jumpshot/Avast), and his open-source infrastructure — Brickhouse and Satisfaction, both founded over a decade ago — is still in active use across the data engineering community. That same instinct — spot the missing infrastructure layer, build it as composable tooling others can pick up — is what produced this profile itself: an agentic system he designed and built end to end.

**Strongest signals:**
- Founded [Brickhouse](http://github.com/klout/brickhouse), a Hive UDF library forked and cloned by hundreds of data teams industry-wide, still active more than a decade later
- Designed and built [Talent Brain](https://github.com/jeromebanks/talent-brain) — a twelve-skill agentic system, running on Claude Code, that turns a career history into a navigable knowledge graph and generates targeted resumes, fit assessments, and live recruiter Q&A; open-sourced and the tool that built this profile
- At GSK, migrated a phenomics image-processing pipeline from Vertex AI to Nextflow/GCP Batch, driving GPU utilization from ~1.75% to ~100% and cutting single-barcode runtime roughly 3x (~2h11m → ~43m32s)
- Built nf-forge, an AI-assisted approach for generating Nextflow pipelines from legacy scientific code — first proven by migrating an HRD-determination workflow to production in ~4–5 days
- Repeatedly brought in as the senior technical IC to build big data capability from scratch with no existing team or budget — most notably standing up production Spark on Kubernetes at Tatari with zero managed-service spend

---

## For hiring managers and recruiters

Open this folder in [Claude Code](https://claude.ai/code) and run:

```
/showcase
```

Or just ask questions directly — Claude will navigate the profile and answer:

- "What has Jerome built that's most relevant to a Staff+ engineer role at a data-heavy company?"
- "Walk me through his most complex infrastructure project."
- "Has he led or mentored engineers?"
- "How does his background compare to what we need for [describe the problem]?"

No setup required. The skills are bundled in this folder and load automatically.

---

## For Jerome

| What you want to do | Command |
|---|---|
| Add a new resume or job | `/ingest [file]` |
| Deepen a role with a structured interview | `/excavate` |
| Update career goals and preferences | `/intent` |
| Generate a resume for a job posting | `/generate [jd]` |
| Check fit against a role | `/fit [jd]` |
| Find gaps for a target role | `/gap [jd]` |
| Draft a cover letter | `/cover-letter [jd]` |
| Publish updates to the repo | `/publish` |

---

Built with [Talent Brain](https://github.com/jeromebanks/talent-brain).
