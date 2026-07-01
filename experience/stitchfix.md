---
company: "StitchFix"
slug: "stitchfix"
title: "Data Platform Engineer, Algorithms and Analytics"
start: "2015-08"
end: "2016-10"
location: ""
employment_type: "full-time"
ingested_sources:
  - file: "Resume02-2025 (Google Drive)"
    date: "2026-06-18"
  - file: "excavation"
    date: "2026-06-24"
    note: "structured interview"
---

# StitchFix — Data Platform Engineer, Algorithms and Analytics

## Context

Platform components for a fashion recommendation e-commerce retailer. Small platform team of ~6 engineers supporting a large data science and algorithms org.

## Responsibilities

### On-call and production support
- scope: broader data platform — ingestion pipelines, Spark jobs, and supporting infrastructure for the algorithms and analytics org

### Pipeline and job optimization
- scope: ongoing performance tuning and scalability improvements to data platform components

### Data engineering best practices
- scope: evangelizing scalable data engineering patterns; "your service is a function" design; Akka Reactive Streams adoption across the platform team

## Contributions

### Otherworld — AWS Event Ingestion
- what: framework for ingesting events from HTTP REST and AMQP endpoints into AWS S3 via Kinesis, with Akka Reactive Streams connectors for AWS services
- stack: Scala, Akka, Akka Reactive Streams, AWS Kinesis, S3, DynamoDB, CloudWatch, AMQP
- impact: production web analytics event ingestion pipeline for StitchFix.com — HTTP and AMQP events into AWS S3 via Kinesis using Akka Reactive Streams specifically to handle bursts of traffic and error conditions gracefully

### Brule's Rules — Rules Engine
- what: lightweight reactive rules engine with inner Scala DSL and PEG parser external DSL, embeddable in Spark or Lambda functions
- stack: Scala
- impact: built for customer cohort assignment to drive targeted marketing campaigns (e.g. re-engagement emails based on purchase recency); production status unclear at time of departure

### Ponderosa — Rule Evaluation at Scale
- what: Spark jobs and Hive UDFs for evaluating state changes via dynamic Brule's Rules DSL rules
- stack: Apache Spark, Hive, Scala
- impact: Spark-scale evaluation layer for Brule's Rules cohort logic, enabling dynamic rule updates without redeployment; production status unclear at time of departure

### Spark DynamoDB Connector
- what: Spark DataSource for scalable distributed read/write from DynamoDB
- stack: Apache Spark, DynamoDB
- impact: enabled Spark jobs to read and write ML model weights stored in DynamoDB at distributed scale; used in production by the algorithms team

### Ginsberg — REST Service for Hive MetaStore
- what: REST microservice exposing Hive database and table metadata using "your service is a function" microservice design
- stack: Scala, Finagle, Finch
- impact: provided REST access to Hive MetaStore metadata for internal tooling; in production
