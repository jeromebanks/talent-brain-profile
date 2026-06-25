---
company: "Tagged.com / if(we)"
slug: "ifwe"
title: "Senior Software Engineer, Analytics Infrastructure"
start: "2014-03"
end: "2015-07"
location: ""
employment_type: "full-time"
ingested_sources:
  - file: "Resume02-2025 (Google Drive)"
    date: "2026-06-18"
  - file: "excavation"
    date: "2026-06-24"
    note: "structured interview"
---

# Tagged.com / if(we) — Senior Software Engineer, Analytics Infrastructure

## Context

Analytics infrastructure for a large social website. Small team of 3–4 data engineers embedded within a larger analytics org of ~5–6 data scientists and analysts. Working with large HDFS datasets. Provided guidance to business analysts and presented at internal and external meetups.

## Responsibilities

### Pipeline and job optimization
- scope: ongoing performance tuning and scalability improvements to production Hadoop and Hive pipelines

### Data engineering best practices
- scope: guidance to business analysts and engineers on data tools, scalable patterns, and open-source contributions; presented internally and at meetups

### Mentoring junior engineers
- scope: guidance on scalable Big Data techniques and engineering craft

## Contributions

### Ramblas — Event Ingestion
- what: event ingestion system from Kafka queues into HDFS with continuous scheduling and job monitoring via Satisfaction
- stack: Kafka, Avro, Camus, Hive, HDFS, Satisfaction
- impact: ingested all application events from Tagged.com — a platform with 300M registered members and tens of millions of monthly active users — into HDFS at half-hour cadence; reliable, continuous production pipeline feeding downstream Pinkman aggregation

### Pinkman — Small Batch Event Aggregation
- what: user-session generation and demographic aggregate pipelines producing reach, session, and action counts for millions of demographic segments (geo, device, gender, age, etc.) at hourly and multi-day rollup frequencies
- stack: Hive, HBase, Brickhouse, HDFS
- impact: daily aggregate coverage across millions of demographic segments for reach, retention, engagement, and spammer activity metrics

### Satisfaction — Next-Gen Batch Scheduler
- what: dependency-based Hadoop workflow scheduler with Scala DSL, Play! UI, Akka engine, and embedded Hive driver — taken from prototype to production and open-sourced
- stack: Scala, Play! Framework, Akka, Hive
- impact: moved from prototype to robust production system; open-sourced and presented at meetups

### Brickhouse — Useful Hive UDFs
- what: curation and extension of open-source Hive UDF library — merged PRs, community support, new HBase UDFs, demographic XUnits, and sessionization UDFs
- stack: Hive, HBase, HDFS
- impact: widely adopted by data companies; forked and cloned by a large number of organizations
