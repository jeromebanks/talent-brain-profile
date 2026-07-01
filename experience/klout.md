---
company: "Klout"
slug: "klout"
title: "Senior Software Engineer"
start: "2011-09"
end: "2014-02"
location: ""
employment_type: "full-time"
ingested_sources:
  - file: "Resume02-2025 (Google Drive)"
    date: "2026-06-18"
  - file: "Resume-2014 (local)"
    date: "2026-06-29"
  - file: "excavation"
    date: "2026-06-24"
    note: "structured interview"
---

# Klout — Senior Software Engineer

## Context

Technical leadership in Hadoop, Hive, and Big Data for a social influence scoring company. Small startup of 50–100 employees at peak; Jerome worked on teams of 3–6 with close collaboration across the org. Processing large social media datasets with MapReduce and Hive ETL pipelines. Part of on-call support. Mentored junior engineers; provided advice to Operations for cluster management and optimization.

## Responsibilities

### On-call and production support
- scope: Hadoop cluster and production ETL pipelines for Klout score computation

### Pipeline optimization and SLA management
- scope: ongoing mandate to investigate inefficiencies and optimize production jobs as data volumes grew

### Hive and common UDF evangelism
- scope: evangelized use of Hadoop Hive and common UDFs across the engineering org; introduced a common programming model for data development that replaced one-off MapReduce approaches

## Contributions

### Maxwell — Next-Gen Klout Score
- what: Hadoop ETL pipeline for feature generation and calculation of the Klout score and moments, optimized for high data volumes and skewed input via KMV sketches for reach estimation
- stack: Hadoop, MapReduce, Hive, KMV sketches
- impact: met required SLA at scale — computing Klout scores across Klout's full user base (~750M users, ~45B daily social interactions at peak); KMV sketches resolved otherwise-intractable reach estimation bottlenecks and were adopted as the org-wide solution

### Topic Thunder — Topic Assignment
- what: investigation of social media features for topic relevance, leading to a Bayesian classification approach; pipelines for topic assignment, topical leaderboards, and topical scores
- stack: Hadoop, MapReduce, Hive, HBase, Brickhouse UDFs
- impact: shipped customer-facing topical influence scores and leaderboards at scale — 10,000+ topics across hundreds of millions of users, processed daily; work contributed to two published research papers (LASTA, 2014; Klout Topics, 2017) with Jerome acknowledged as contributor

### Brickhouse — Useful Hive UDFs
- what: open-sourced common internal Hive UDFs as github.com/klout/brickhouse, with community evangelism, tech meetup presentations, and a public blog on Hadoop/Hive patterns
- stack: Hive, Hadoop
- impact: widely adopted open-source project; continues to be used across the industry

### Analytics Warehouse
- what: Hadoop pipelines supporting internal analytics warehouse
- stack: Hadoop, MapReduce, Hive
- impact: internal BI reporting warehouse for klout.com web analytics; notable as the origin of the Hive UDF collection that was later open-sourced as Brickhouse — first adoption of SQL-based Hive pipelines at Klout in place of explicit MapReduce

### Satisfaction — Next-Gen Batch Scheduler
- what: initial implementation of backward-chaining Hadoop scheduler to replace operational deficiencies in Oozie and Jenkins
- stack: Scala, Akka, Play! Framework
- impact: prototype asset-based orchestrator (backward-chaining from target Hive tables) built to replace Oozie/Jenkins error recovery nightmare; not production-ready before Klout downsized; carried to Tagged/if(we) with agreement, where it completed and ran production pipelines; ultimately open-sourced before being eclipsed by Airflow
