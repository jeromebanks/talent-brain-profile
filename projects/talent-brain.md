---
name: "Talent Brain"
slug: "talent-brain"
type: "open-source"
status: "active"
company: "independent"
start: "2026-06"
url: "https://github.com/jeromebanks/talent-brain"
---

# Talent Brain

## Problem

Resumes are lossy by construction — every rewrite compresses real decisions, tradeoffs, and impact into bullet fragments, and years of that compression leaves most of a career's actual depth unrecoverable. At the same time, both sides of hiring are increasingly agent-mediated: candidates use AI to tailor applications, recruiters and hiring managers use AI to screen them. Neither side had a structured, agent-readable source of truth to work from — just the same flattened PDF.

## What I Built

An agentic system, built as a Claude Code plugin, that turns a career history into a navigable knowledge graph instead of a static document: a markdown schema (`SCHEMA.md`) for experience, projects, skills, and intent, plus twelve composable skills that operate on it — `ingest` (resumes, LinkedIn exports) and `excavate` (structured interview to recover detail resumes strip out) to build the profile; `intent` to capture what a candidate actually wants next, including disinterest signals no resume format has room for; `fit`, `gap`, `generate`, and `cover-letter` to produce targeted outputs against a specific job description; and `showcase`, which opens a live agent-mediated Q&A session (via Claude Cowork) so a recruiter can interrogate the profile directly instead of reading a document. `publish` keeps the generated resume and README in sync with the underlying profile.

## Impact

Used to build and maintain my own profile — this repository is the reference implementation and primary consumer. Released publicly and MIT-licensed on GitHub for others to adopt.

## Technical Decisions

Chose plain markdown files over a database or proprietary format so the profile stays portable, diffable, and readable by both humans and agents without a runtime dependency. Made ingestion strictly additive — never overwriting existing content — so multiple source documents (old resumes, LinkedIn exports) can be merged without losing whichever one had the most detail. Structured the system as independent, composable skills rather than one monolithic flow, so each capability (excavate, fit, generate, showcase) can be invoked and extended on its own. Skills are symlinked into the profile repo itself so a cloned profile is self-contained and runs anywhere Claude Code opens it — no separate plugin install required.

## Through-Line

Same pattern as Brickhouse and Satisfaction: notice a missing infrastructure layer, build it as composable open tooling, let others adopt and extend it — this time applied to the career-tooling problem created by agentic AI itself, rather than to Hadoop-era data infrastructure. It's also the most direct, hands-on evidence of agentic engineering ability in the profile: not a description of working with LLM agents, but a working multi-skill agent system designed, built, and shipped end to end.
