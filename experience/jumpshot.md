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
  - file: "Resume-2018 (Google Drive)"
    date: "2026-06-25"
  - file: "excavation"
    date: "2026-06-25"
    note: "structured interview"
---

# Jumpshot/Avast — Senior Software Engineer

## Context

Big data infrastructure and pipelines for a marketing analytics startup with access to an extensive opt-in clickstream data panel sourced from the Avast browser plugin — approximately 100M devices and 435M monthly active users. Jerome worked on the "Data Processing" team of 3–4 San Francisco engineers, serving as de facto technical lead. The team collaborated closely with a San Francisco data analyst group and a larger engineering group in Czech Republic. Mentored junior engineers and educated SF data analysts on Hive query best practices.

## Responsibilities

### Pipeline and job optimization
- scope: ongoing performance tuning and scalability improvements to production Big Data pipelines

### Data engineering best practices
- scope: introducing and advocating scalable data engineering patterns and approaches across the team

### Mentoring junior engineers
- scope: guidance on scalable Big Data techniques and engineering craft

### Educating data analysts
- scope: teaching SF data analysts Hive query best practices and scalable data access patterns on the Avast clickstream dataset

## Contributions

### Cubism
- what: reusable Scala Spark DataFrame library for multidimensional aggregates, with KMV sketches for cardinality estimation and set similarity, salting for skew handling, and utilities for high-dimensional vectors, event sequences, and time series
- stack: Scala, Apache Spark
- impact: adopted by both the San Francisco and Czech Republic engineering teams; served as the basis for FunnelCube, WillRogers, and streaming browser-type aggregates; KMV sketches enabled audience overlap analysis (set similarity) in addition to cardinality estimation; Cubism itself formed the basis for data monitoring, anomaly detection, and marketing insights infrastructure; used in both internal analytics and customer-facing products

### FunnelCube
- what: e-commerce analytics aggregate pipelines across domain, brand, category, geo, and demographics dimensions using Cubism; metrics include interaction, add-to-cart, start-checkout, and conversion counts, funnel sessions, estimated reach, time to conversion, cross-site and cross-brand interactions, upstream keywords, and dimensional ranking
- stack: Scala, Apache Spark, Cubism
- impact: powered Jumpshot's E-commerce Insights SaaS product, used by brand marketers and e-commerce sites to track cross-site consumer journeys (browse Walmart → purchase on Amazon; abandon Adidas cart → purchase at Nike)

### Cubism Streaming
- what: extension of Cubism to Spark Streaming for continuous multidimensional aggregation of browser-type metrics from the Avast clickstream at 5-30 minute intervals, with Kafka-based data quality monitoring for rapid anomaly detection
- stack: Apache Spark Streaming, Kafka, Scala
- impact: served as a sentinel against Avast browser plugin deployment misconfigurations — enabled the Data Processing team to detect data quality anomalies within minutes and halt downstream processing before corrupted data could propagate; without it, a silent misconfiguration in an Avast deployment could poison the entire pipeline

### Pigsicle
- what: Scala Spark library for multi-condition row emission using a PEG SQL parser
- stack: Scala, Apache Spark
- impact: enabled efficient generation of hundreds of cookie-based audiences in a single pass over a massive user-feature dataset

### WillRogers
- what: Hive MetaStore snapshot pipelines and mass DDL operation utilities for HDFS disk usage analysis and monitoring on fixed-capacity on-premises clusters; tooling to identify deletable files and predict resource usage
- stack: Scala, Apache Spark, Hive
- impact: tracked data access, lineage, and delivery times daily; provided analytics of Hadoop cluster usage and Hive metadata; supported the legally-mandated migration of the on-prem cluster from Amsterdam to Czech Republic (data governance requirement; secondary benefits: hardware upgrade and cost reduction)
