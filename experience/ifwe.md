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
---

# Tagged.com / if(we) — Senior Software Engineer, Analytics Infrastructure

## Context

Analytics infrastructure for a large social website. Small data-engineering and analytics team working with large HDFS datasets. Provided guidance to business analysts and presented at internal and external meetups.

## Contributions

### Ramblas — Event Ingestion
- what: event ingestion system from Kafka queues into HDFS with continuous scheduling and job monitoring via Satisfaction
- stack: Kafka, Avro, Camus, Hive, HDFS, Satisfaction
- impact: <!-- not yet captured -->

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
