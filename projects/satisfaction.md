---
name: "Satisfaction"
slug: "satisfaction"
type: "open-source"
status: "archived"
company: "if(we) (open-sourced)"
start: "2013-01"
end: "2015-07"
url: "http://github.com/ifwe/satisfaction"
ingested_sources:
  - file: "Resume02-2025 (Google Drive)"
    date: "2026-06-18"
  - file: "excavation"
    date: "2026-07-16"
    note: "structured interview — Impact, Technical Decisions, Through-Line"
---

# Satisfaction

## Problem

Hadoop workflow schedulers like Oozie and Jenkins had significant operational deficiencies for dependency-based batch scheduling at scale. Teams needed a more robust, developer-friendly alternative.

## What I Built

A next-generation dependency-based Hadoop workflow scheduler, implemented in Scala. Features a DSL for defining workflow "Goals and Tracks," a Play! framework UI, an Akka-based dependency engine, an embedded Hive driver, and a pluggable architecture for deploying multiple Tracks — extensible to support Spark, Scalding, and other Hadoop technologies. Took it from prototype at Klout to a robust production system at if(we). Open-sourced, documented, and presented at meetups.

## Impact

Deployed as a greenfield solution — it wasn't replacing a failing system, but filling the gap left by Oozie/Jenkins-era scheduling deficiencies. In production at if(we), Satisfaction managed roughly a dozen distinct Tracks, including Ramblas (all application events across a 300M-member platform, half-hour cadence) and Pinkman (demographic aggregates across millions of segments). Remained in production after Jerome's departure from if(we); duration past that point wasn't tracked. The asset-based dependency model it introduced predated Dagster's similar approach by roughly 3–5 years (Satisfaction: 2013–2015; Dagster: 2018).

## Technical Decisions

The core design departure from Oozie and Jenkins — the dominant workflow schedulers at the time — was an asset-based model: Satisfaction tracked which data assets were already satisfied and rebuilt only the unsatisfied dependencies on failure or partial completion, rather than re-running or restarting an entire DAG. Satisfaction predates Airflow's general availability (prototyped at Klout in 2013, in if(we) production by 2014–2015, versus Airflow's 2015 open-source release) — the two share the goal of programmatic, dependency-aware workflow orchestration, but Satisfaction's asset-based approach was a different model from Airflow's DAG-of-tasks design. That same asset-centric approach was independently arrived at years later by Dagster (2018), roughly 3–5 years after Satisfaction. Akka's actor model powered the dependency engine specifically because it let the scheduler distribute and parallelize workload evaluation in a way that suited the asset-based approach — tracking many independent assets' satisfaction state concurrently — better than a simpler sequential dependency walker would have.

## Through-Line

The name itself is a deliberate analogy to logical satisfiability: rather than treating a workflow as an imperative sequence of steps, Satisfaction treats it as a goal-seeking constraint-satisfaction problem — find what's unsatisfied, build only that. This "data engineering through goal-seeking" instinct — solve for the minimal necessary work rather than re-deriving everything — is a throughline that resurfaces in Brickhouse's declarative-SQL-over-procedural-MapReduce pattern and later in nf-forge's reuse of existing pipeline logic rather than rebuilding from scratch.
