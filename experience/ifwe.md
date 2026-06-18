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

Architected, designed, and developed systems for calculating web-analytics for a large social website. Managed large amounts of data in HDFS with Hadoop technologies in a small data-engineering and analytics team. Provided guidance to business analysts on the use of data tools. Presented before audiences internally and at meetups about technical projects and open-source contributions.

## Contributions

- **Ramblas — Event Ingestion** – Developed system for ingestion of large amounts of events from Kafka queues into HDFS, based on Avro, Camus, and Hive. Developed tracks in Satisfaction for continuous scheduling and job monitoring.
- **Pinkman — Small Batch Event Aggregation** – Developed pipelines for generating user-sessions from events, and produced aggregates of reach, session and action counts for millions of demographics segments, including combinations of geo, device, gender, age, and other user dimensions. Generated aggregates per event for a large number of event types. Aggregates calculated hourly, then aggregated to produce daily results for 1, 3, 7, 14, and 30 days. Aggregates batch-put into HBase using HBase UDFs developed in Brickhouse. Developed pipelines for other core metrics like user retention, engagement, and spammer activity.
- **Satisfaction — Next-Gen Batch Scheduler** – Designed and developed the robust dependency-based Hadoop workflow scheduler. Implemented in Scala with a DSL for workflow "Goals and Tracks," a Play! framework UI, an Akka-based dependency-engine, an embedded Hive driver, and pluggable architecture for deploying multiple Tracks. Took it from prototype to a robust production system. Open-sourced, documented, presented, and evangelized internally and at meetups.
- **Brickhouse — Useful Hive UDFs** – Continued to support and curate this popular Hive UDF library, forked and cloned by a large number of data companies. Merged pull-requests, fielded questions and bug reports. Answered related questions on stackoverflow.com and wrote relevant blogs at brickhouseconfessions.wordpress.com. Contributed new UDFs including HBase-related UDFs, demographic XUnits, and user sessionization.

## Outcomes

<!-- not yet captured -->

## Decisions & Tradeoffs

<!-- not yet captured -->

## Tools & Methods

- Scala, Akka, Play! Framework
- Hive, HDFS, HBase, Hadoop
- Kafka, Avro, Camus
- Satisfaction (scheduler)
- Brickhouse (Hive UDFs)

## Team & Scope

<!-- not yet captured -->
