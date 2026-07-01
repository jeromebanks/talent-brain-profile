---
company: "Tatari"
slug: "tatari"
title: "Staff Data Platform Engineer"
start: "2020-02"
end: "2022-07"
location: ""
employment_type: "full-time"
ingested_sources:
  - file: "Resume02-2025 (Google Drive)"
    date: "2026-06-18"
  - file: "excavation"
    date: "2026-06-23"
    note: "structured interview"
---

# Tatari — Staff Data Platform Engineer

## Context

Helped transition this TV AdTech company off of Postgres and Redshift and onto Spark and Databricks for data processing. Small data platform team of 5–6 engineers; Jerome joined as the most senior IC and provided technical leadership through a period of management transition.

## Responsibilities

### Pipeline and job optimization
- scope: ongoing performance tuning and scalability improvements to Spark and Databricks pipelines during the Postgres/Redshift migration

### Data engineering best practices
- scope: technical leadership as most senior IC; introducing scalable Big Data patterns during a period of management transition

## Contributions

### Spark on Kubernetes
- what: deployment of Apache Spark onto AWS EKS with custom Helm charts and Docker images, with Livy fork bug fixes and new features
- stack: Apache Spark, Kubernetes (AWS EKS), Helm, Docker, Apache Livy
- impact: stood up production Spark compute from scratch with no budget, enabling the company's first real Big Data pipelines on existing Kubernetes infrastructure; ran in production for approximately a year until management signed a Databricks contract

### Flexible Aggregator
- what: multi-dimensional aggregate tool in Spark with OLAP-style schema-less flexibility, deployed via Airflow ETL DAGs for combined linear and streaming TV metrics
- stack: Apache Spark, Apache Airflow, Databricks
- impact: designed to precompute OLAP-style rollups for linear and streaming TV campaign metrics, reducing ad-hoc query load on the Postgres backend; full impact unrealized due to a deployment decision made without coordination that reintroduced the Postgres bottleneck

### Zippo SparkSQL UDF Library
- what: Scala Spark UDF and UDAF library for data engineering use cases including KMV cardinality estimation and ArgMax TopN
- stack: Scala, Apache Spark
- impact: shipped and available for team adoption; tenure ended before broader uptake
