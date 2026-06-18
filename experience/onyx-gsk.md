---
company: "Onyx GSK"
slug: "onyx-gsk"
title: "Senior Data Platform Engineer"
start: "2023-07"
end: "present"
location: ""
employment_type: "full-time"
ingested_sources:
  - file: "Resume02-2025 (Google Drive)"
    date: "2026-06-18"
---

# Onyx GSK — Senior Data Platform Engineer

## Context

Building next generation data experiences for GSK's scientists, engineers and decision makers.

## Contributions

- **Broad Data Institute Ingestion** – Wrote GCP Dataflow job for the ingestion of over 150TB of cell imaging data (contained in over 100 billion files) from S3 to GCP. Wrote Dataflow job to capture manifest of all transferred files, and shepherded job to completion.
- **BigQuery Table Metadata** – Wrote Dataflow job to gather BigQuery table metadata (like storage size and partitioning information) and store in BigQuery, for analysis and optimization of migration from Hadoop on-premise cluster to GCP BigQuery.
- **JDBC Ingestion** – Refactored GCP Workflow and Dataproc Spark Job for ingesting from multiple JDBC Sources (including Oracle, Postgres, MySQL and SQLServer) into BigQuery and GCS. Provided model for good practices in Spark development, and introduced unit and integration tests for Spark jobs into the organization.
- **WFLinter** – Developed a git pre-commit tool for validating GCP Workflow YAML files before submission into CI/CD pipelines. Proposed SDLC development model for writing GCP Workflows, along with a testing framework for validating GCP Workflow logic.

## Outcomes

<!-- not yet captured -->

## Decisions & Tradeoffs

<!-- not yet captured -->

## Tools & Methods

- GCP Dataflow, Apache Beam
- BigQuery, GCS
- GCP Workflows, Dataproc
- Apache Spark
- JDBC (Oracle, Postgres, MySQL, SQLServer)
- Git pre-commit hooks

## Team & Scope

<!-- not yet captured -->
