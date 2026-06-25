---
company: "Quantcast"
slug: "quantcast"
title: "Senior Software Engineer"
start: "2008-09"
end: "2011-09"
location: ""
employment_type: "full-time"
ingested_sources:
  - file: "Resume02-2025 (Google Drive)"
    date: "2026-06-18"
  - file: "Resume 2011 (Google Drive)"
    date: "2026-06-18"
---

# Quantcast — Senior Software Engineer

## Context

Large-scale Hadoop and MapReduce data processing for a web analytics and advertising startup.

## Responsibilities

### Production job optimization and operations
- scope: ongoing mandate to improve performance and scalability of production jobs as datasets grew; re-implemented jobs that could no longer scale

### Production support and on-call
- scope: on-call rotation for production Hadoop pipelines; responsible for keeping the core daily measurement pipeline running reliably

## Contributions

### PipeV3 — Daily Measurement Job
- what: components of the Publisher daily job producing reach counts for all quantified web sites
- stack: Hadoop, MapReduce, HDFS
- impact: core daily measurement pipeline that drove Quantcast's publisher reach product for over 10 years before being retired

### Publisher Geo Job
- what: extension of the daily publisher measurement pipeline to produce geo-level reach counts at city, DMA, state, and national granularity using Bloom filter merging; used MaxMind geo database with long-tail city filtering for tractability; XUnits aggregation hierarchy rolled city-level data up through DMA, state, and national in one pass; multi-threaded multi-output reducers used to fan out aggregated results across granularity levels in a single pass
- stack: Hadoop, MapReduce, HDFS, Bloom filters, MaxMind
- impact: re-implemented the monthly Publisher Geo job after the previous implementation could no longer scale; enabled multi-level geo reach measurement (city/DMA/state/national) for all quantified websites using an efficient rolling 30-day window strategy (5+2-day chunks merged into 7-day windows, released weekly)

### Datacore Framework
- what: Ruby framework for scheduling, executing, monitoring, and managing Quantcast's production Hadoop jobs — with notifications, retry logic, and dependency management
- stack: Ruby, Hadoop
- impact: load-bearing production job scheduler for Quantcast's Hadoop pipelines; early exploration of dependency-based scheduling ideas that later influenced the design of Satisfaction

### Hotdog — RMR Serialization
- what: serialization framework for Quantcast-specific Hadoop POJOs built within the RMR (Relational MapReduce) ecosystem, enabling object-level MapReduce logic without manual ser/de boilerplate; predated or contemporaneous with Kryo
- stack: Java, Hadoop, MapReduce
- impact: reduced serialization overhead in Jerome's own pipelines by a few percentage points; not broadly adopted but a proactive initiative to remove friction he identified himself
