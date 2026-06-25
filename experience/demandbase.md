---
company: "Demandbase"
slug: "demandbase"
title: "Principal Big Data Engineer"
start: "2018-09"
end: "2021-02"
location: ""
employment_type: "full-time"
ingested_sources:
  - file: "Resume02-2025 (Google Drive)"
    date: "2026-06-18"
  - file: "excavation"
    date: "2026-06-24"
    note: "structured interview"
---

# Demandbase — Principal Big Data Engineer

## Context

Account-based marketing platform with a core IP-to-company mapping technology. Jerome worked across two team configurations: a small 3-person SF team and a larger group co-located with a Seattle engineering org. For most contributions, he was the primary developer, owning projects from conception through design, development, and production support.

## Responsibilities

### On-call and production support
- scope: Big Data ETL pipelines serving critical business processes

### Compute efficiency and resource management
- scope: ongoing BigQuery slot optimization, Spark tuning, and Airflow DAG reliability across team pipelines

## Contributions

### EngagementQube
- what: aggregate pipeline for multi-dimensional web engagement events, with reach estimation and time-series analytics
- stack: Scala, Apache Spark
- impact: replaced a spaghetti implementation with a clean re-architecture applying the Cubism design pattern; added geo as a new dimension (roughly doubling the computation), substantially faster and cheaper than the original pipeline; aggregates surfaced to clients via a BigQuery-backed insights product for campaign performance tracking

### Nutch Crawler
- what: web crawler for processing millions of URLs daily, with crawl metrics framework
- stack: Apache Nutch
- impact: stood up production web crawling for intent signal extraction at millions-of-URLs scale; instrumentation revealed that a significant portion of crawl time was spent on irrelevant or paywall-blocked sites, ruling out the crawler itself as a bottleneck and clarifying the signal quality ceiling

### Windmill Document Parser
- what: text extraction pipeline from HTML with Named Entity Recognition and keyword extraction
- stack: Apache Beam, GCP Dataflow, Spotify Scio, Stanford NLP
- impact: exploratory prototype — full pipeline ran on GCP Dataflow with Stanford NLP for more sophisticated topic extraction than bag-of-words; positioned as a strategic hedge if the primary intent approach lost signal; did not reach production

### Intent Pipeline
- what: optimization and extension of legacy BigQuery pipelines on Airflow to reduce slot usage and meet critical SLAs
- stack: BigQuery, Apache Airflow
- impact: drastically reduced BigQuery slot usage; DAGs met critical business SLAs

### Bumblebee Processing Framework
- what: streaming synchronization framework for distributed tenant instances, with near real-time updates and Pulsar-to-PubSub bridge
- stack: Apache Beam, Spotify Scio, GCP Dataflow, Apache Pulsar, GCP Pubsub, Prometheus, Grafana
- impact: enabled real-time synchronization between Demandbase's cloud-scale pipeline and the federated per-customer instances (each with local in-memory data) acquired from a startup; kept keyword updates in sync and triggered downstream processing jobs across both systems
