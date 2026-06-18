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
---

# StitchFix — Data Platform Engineer, Algorithms and Analytics

## Context

Architected, designed, and developed platform components for a fashion recommendation e-commerce retailer.

## Contributions

- **Otherworld — AWS Event Ingestion** – Developed a framework to ingest events into AWS S3 from HTTP REST and AMQP endpoints, with Kinesis as an intermediate persistence layer. Utilized the Akka reactive streams framework in Scala to handle bursts of traffic and error conditions gracefully. Developed Akka Reactive Streams connectors for AWS Kinesis, S3, Cloudwatch, and DynamoDB.
- **Brule's Rules — Rules Engine** – Developed lightweight reactive rules engine in Scala to be embedded in various components like Spark or AWS Lambda functions. Developed an inner Scala DSL for rule definition, as well as a PEG Parser for an external DSL.
- **Ponderosa — Rule evaluation at scale** – Implemented Spark Jobs and Hive UDFs to evaluate state changes via dynamic rules developed with the Brule's Rules DSL.
- **Spark DynamoDB Connector** – Prototyped a Spark DataSource to read/write data from DynamoDB in a scalable distributed manner.
- **Ginsberg — REST Service exposing Hive MetaStore** – Developed a REST microservice using Finagle and Finch with Scala to expose Hive database and table information. Evangelized "your service is a function" design for microservices.

## Outcomes

<!-- not yet captured -->

## Decisions & Tradeoffs

<!-- not yet captured -->

## Tools & Methods

- Scala, Akka, Akka Reactive Streams
- Apache Spark, Hive
- AWS (Kinesis, S3, DynamoDB, CloudWatch, Lambda)
- Finagle, Finch
- AMQP

## Team & Scope

<!-- not yet captured -->
