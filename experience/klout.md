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
---

# Klout — Senior Software Engineer

## Context

Technical leadership in Hadoop, Hive, and Big Data for a social influence scoring company. Processing large social media datasets with MapReduce ETL pipelines. Part of on-call support. Mentored junior engineers; provided advice to Operations for cluster management and optimization.

## Responsibilities

### On-call and production support
- scope: Hadoop cluster and production ETL pipelines for Klout score computation

### Pipeline optimization and SLA management
- scope: ongoing mandate to investigate inefficiencies and optimize production jobs as data volumes grew

## Contributions

### Maxwell — Next-Gen Klout Score
- what: Hadoop ETL pipeline for feature generation and calculation of the Klout score and moments, optimized for high data volumes and skewed input via KMV sketches for reach estimation
- stack: Hadoop, MapReduce, Hive, KMV sketches
- impact: met required SLA at scale; KMV sketches introduced as org-wide solution for scalable reach estimation

### Topic Thunder — Topic Assignment
- what: pipelines for topic assignment, topical leaderboards, and topical scores from social media features using Bayesian classification
- stack: Hadoop, MapReduce, Hive
- impact: <!-- not yet captured -->

### Brickhouse — Useful Hive UDFs
- what: open-sourced common internal Hive UDFs as github.com/klout/brickhouse, with community evangelism, tech meetup presentations, and a public blog on Hadoop/Hive patterns
- stack: Hive, Hadoop
- impact: widely adopted open-source project; continues to be used across the industry

### Analytics Warehouse
- what: Hadoop pipelines supporting internal analytics warehouse
- stack: Hadoop, MapReduce, Hive
- impact: <!-- not yet captured -->

### Satisfaction — Next-Gen Batch Scheduler
- what: initial implementation of backward-chaining Hadoop scheduler to replace operational deficiencies in Oozie and Jenkins
- stack: Scala, Akka, Play! Framework
- impact: <!-- not yet captured -->
