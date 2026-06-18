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

Developed big data infrastructure components and pipelines for a marketing analytics startup with access to an extensive unique data panel. Mentored and educated junior engineers on scalable Big Data techniques.

## Contributions

- **FunnelCube** – Developed Scala Spark libraries and pipelines for efficiently generating aggregates of e-commerce analytics across domain, brand, category, geo, and demographics dimensions, using the Cubism library. These metrics provide the basis of Jumpshot's E-commerce Insights product.
- **Cubism** – Developed and supported a reusable Scala Spark DataFrame library for efficiently generating multidimensional aggregates ("cubes"). Developed efficient Scala implementation of KMV sketches for cardinality estimation and set similarity. Developed utilities for handling skew data with "salting," and for aggregating high-dimensional vectors, event sequences, and time series data. This library became the basis for multiple projects including data monitoring, anomaly detection, and marketing insights.
- **Cubism Streaming** – Extended Cubism to Apache Spark Streaming, enabling generation of multidimensional aggregates on an ongoing basis at 5–30 minute frequency. Implemented a Kafka data quality monitoring system for rapid anomaly detection across multiple dimensions.
- **Pigsicle** – Designed a Scala Spark library for emitting rows based on multiple conditions using a fast PEG SQL parser. Enabled the efficient generation of hundreds of different cookie-based audiences during a single pass over a massive user-feature dataset.
- **WillRogers** – Developed Scala libraries and pipelines for taking snapshots of the Hive MetaStore into Hive tables, to enable analysis and monitoring of HDFS disk usage. Developed Spark/Hive UDFs for performing mass Hive DDL operations.

## Outcomes

<!-- not yet captured -->

## Decisions & Tradeoffs

<!-- not yet captured -->

## Tools & Methods

- Scala, Apache Spark, Spark Streaming
- Hive, HDFS
- Kafka
- KMV sketches

## Team & Scope

<!-- not yet captured -->
