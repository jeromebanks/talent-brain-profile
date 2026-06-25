---
company: "Apixio"
slug: "apixio"
title: "Staff Software Engineer, Data Platform"
start: "2022-08"
end: "2023-07"
location: ""
employment_type: "full-time"
ingested_sources:
  - file: "Resume02-2025 (Google Drive)"
    date: "2026-06-18"
  - file: "excavation"
    date: "2026-06-23"
    note: "structured interview"
---

# Apixio — Staff Software Engineer, Data Platform

## Context

Data platform for healthcare document processing. Small team of 4–5 engineers responsible for maintaining and shepherding the main document ingestion and processing pipeline. Jerome joined as a Staff IC, the most senior individual contributor role on the team.

## Responsibilities

### Production pipeline monitoring and support
- scope: Spark ETL pipelines for healthcare document processing

### Pipeline and job optimization
- scope: ongoing diagnosis and improvement of Spark pipeline performance, memory, and reliability

### Data engineering best practices
- scope: evangelizing observability, Delta Lake patterns, and Spark best practices as most senior IC on the team

## Contributions

### Trace Hardening
- what: refactor of Spark ETL telemetry pipeline to resolve Delta Lake write contention via Kafka as an intermediate buffer, with mentorship on Delta Lake silver/gold patterns
- stack: Apache Spark, Delta Lake, Kafka
- impact: eliminated daily pipeline failures caused by Delta Lake write contention; pipeline ran stably for the remainder of the engagement after the Kafka buffer was introduced

### Spark Canary
- what: Python scripts to detect and diagnose Spark zombie processes via Spark Monitoring REST API
- stack: Python, Spark Monitoring REST API
- impact: caught zombie Spark processes in production that would otherwise stall pipelines for hours or days undetected; critical for time-sensitive processing deadlines with direct monetary consequences if missed

### Spark Prometheus Grafana Charts
- what: Grafana/Prometheus observability for production Spark ETL pipelines, with ongoing monitoring and evangelism of observability practices
- stack: Prometheus, Grafana, Apache Spark
- impact: introduced observability where none existed before; enabled the team to predict pipeline completion times and surface failures faster

### OCR Improvements
- what: diagnosis of memory corruption in Spark OCR pipelines and optimization of executor and memory settings
- stack: Apache Spark
- impact: resolved memory corruption and increased pipeline throughput
