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
  - file: "excavation"
    date: "2026-06-24"
    note: "structured interview"
---

# Quantcast — Senior Software Engineer

## Context

Quantcast is a web audience measurement and adtech company, founded in 2006 and among the first to apply machine learning to real-time audience insights at scale. Jerome joined in 2008 — early in the company's history, before its publisher measurement service received MRC accreditation in 2010. His team functioned as what would today be called a data platform team: developing and maintaining core measurement pipelines (including the Publisher daily reach job that drove Quantcast's flagship product), building job scheduling infrastructure, and carrying an on-call responsibility to react to pipeline failures. Team size varied over time — a small 2-person team in the early years, growing to 4–6 engineers later.

## Responsibilities

### Production job optimization and operations
- scope: ongoing mandate to improve performance and scalability of production jobs as datasets grew; re-implemented jobs that could no longer scale

### Production support and on-call
- scope: on-call rotation for production Hadoop pipelines; responsible for keeping the core daily measurement pipeline running reliably

## Contributions

### PipeV3 — Daily Measurement Job
- what: key development and maintenance of the Publisher daily job producing daily reach counts for all sites with the Quantcast pixel; optimized jobs to meet scale and delivery requirements as the publisher base grew
- stack: Hadoop, MapReduce, HDFS
- impact: calculated daily reach for all quantified web sites — the core output driving Quantcast's flagship publisher reach product, which ran for over 10 years

### Publisher Geo Job
- what: extension of the daily publisher measurement pipeline to produce geo-level reach counts at city, DMA, state, and national granularity using Bloom filter merging; used MaxMind geo database with long-tail city filtering for tractability; XUnits aggregation hierarchy rolled city-level data up through DMA, state, and national in one pass; multi-threaded multi-output reducers used to fan out aggregated results across granularity levels in a single pass
- stack: Hadoop, MapReduce, HDFS, Bloom filters, MaxMind
- impact: re-implemented the monthly Publisher Geo job after the previous implementation could no longer scale; enabled multi-level geo reach measurement (city/DMA/state/national) for all quantified websites using an efficient rolling 30-day window strategy (5+2-day chunks merged into 7-day windows, released weekly)

### Datacore Framework
- what: Ruby framework for scheduling, executing, monitoring, and managing Quantcast's production Hadoop jobs — with notifications, retry logic, and dependency management
- stack: Ruby, Hadoop
- impact: automated the management and monitoring of Quantcast's production Hadoop cluster jobs — scheduling, execution, notifications, retry, and dependency management in one system; early exploration of dependency-based scheduling ideas that later influenced the design of Satisfaction

### Hotdog — RMR Serialization
- what: serialization framework for Quantcast-specific Hadoop POJOs, implemented using bytecode modification (Javassist) to dynamically enable dependency injection, SEDA buffering, Mapper chaining, and multi-threaded multi-output reducers — object-level MapReduce logic without manual ser/de boilerplate; predated or contemporaneous with Kryo
- stack: Java, Hadoop, MapReduce, Javassist
- impact: reduced serialization overhead in Jerome's own pipelines by a few percentage points; not broadly adopted but a proactive initiative to remove friction he identified himself
