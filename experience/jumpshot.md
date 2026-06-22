---
company: "Jumpshot/Avast"
slug: "jumpshot"
title: "Senior Software Engineer"
start: "2016-12"
end: "2018-08"
location: ""
employment_type: "full-time"
ingested_sources:
  - file: "Resume02-2025 (Google Drive)"
    date: "2026-06-18"
---

# Jumpshot/Avast — Senior Software Engineer

## Context

Big data infrastructure and pipelines for a marketing analytics startup with access to an extensive unique data panel. Mentored junior engineers on scalable Big Data techniques.

## Contributions

### Cubism
- what: reusable Scala Spark DataFrame library for multidimensional aggregates, with KMV sketches for cardinality estimation, salting for skew handling, and utilities for high-dimensional vectors, event sequences, and time series
- stack: Scala, Apache Spark
- impact: became the basis for multiple internal projects including data monitoring, anomaly detection, and marketing insights

### FunnelCube
- what: e-commerce analytics aggregate pipelines across domain, brand, category, geo, and demographics dimensions using Cubism
- stack: Scala, Apache Spark, Cubism
- impact: provides the basis for Jumpshot's E-commerce Insights product

### Cubism Streaming
- what: extension of Cubism to Spark Streaming for continuous multidimensional aggregate generation, with Kafka data quality monitoring for rapid anomaly detection
- stack: Apache Spark Streaming, Kafka, Scala
- impact: 5–30 minute frequency aggregates with rapid anomaly detection across multiple dimensions

### Pigsicle
- what: Scala Spark library for multi-condition row emission using a PEG SQL parser
- stack: Scala, Apache Spark
- impact: enabled efficient generation of hundreds of cookie-based audiences in a single pass over a massive user-feature dataset

### WillRogers
- what: Hive MetaStore snapshot pipelines and mass DDL operation utilities for HDFS disk usage analysis and monitoring
- stack: Scala, Apache Spark, Hive
- impact: <!-- not yet captured -->
