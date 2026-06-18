---
updated: "2026-06-18"
---

# Skills & Capabilities

<!--
Format per entry:
**Skill** — expert|proficient|familiar — active|recent|historical
1–2 sentences on what you've done with it, at what scale or in what context.
_Used at:_ [Company](../experience/slug.md), ...
_Reference:_ [Name](url)
-->

## Core Strengths

These are the areas Jerome consistently operates in across roles — not just tools used, but problems owned.

**Big Data & Distributed Systems Architecture** — expert — active  
Designing and operating large-scale data pipelines across the full lifecycle: ingestion, transformation, aggregation, delivery. Experience from MapReduce-era Hadoop through modern Spark and cloud-native Beam/Dataflow, across ad tech, social media, healthcare, and pharma.  
_Throughout:_ [Quantcast](../experience/quantcast.md), [Klout](../experience/klout.md), [if(we)](../experience/ifwe.md), [StitchFix](../experience/stitchfix.md), [Demandbase](../experience/demandbase.md), [Jumpshot](../experience/jumpshot.md), [Tatari](../experience/tatari.md), [Apixio](../experience/apixio.md), [Onyx GSK](../experience/onyx-gsk.md)

**Data Pipeline Engineering — Batch & Streaming** — expert — active  
Building and operating ETL/ELT pipelines at scale: daily batch jobs, near-real-time streaming, and hybrid architectures. Consistent track record of optimizing for SLA compliance, skew handling, and cost reduction.  
_Throughout:_ most roles

**Multidimensional Aggregation & Analytics Engineering** — expert — recent  
Specialist in generating aggregates across high-cardinality, multi-dimensional datasets efficiently — a recurring theme from Klout Score computation to FunnelCube to Tatari's TV metrics. Inventor of the Cubism library and the Flexible Aggregator.  
_Used at:_ [Klout](../experience/klout.md), [Jumpshot](../experience/jumpshot.md), [Tatari](../experience/tatari.md)

**Open Source Infrastructure Libraries** — expert — recent  
Founded and maintained widely-used open-source projects: Brickhouse (Hive UDFs, forked/cloned by hundreds of data teams), Satisfaction (Hadoop scheduler). Apache Committer on Hivemall.  
_Projects:_ [Brickhouse](../projects/brickhouse.md), [Satisfaction](../projects/satisfaction.md)

---

## Languages

**Scala** — expert — active  
Primary language for production data engineering work since ~2011. Used for Spark jobs, streaming pipelines, Akka-based systems, DSL design, and open-source libraries.  
_Used at:_ [Klout](../experience/klout.md), [if(we)](../experience/ifwe.md), [StitchFix](../experience/stitchfix.md), [Demandbase](../experience/demandbase.md), [Jumpshot](../experience/jumpshot.md), [Tatari](../experience/tatari.md)

**Python** — proficient — active  
Used for scripting, tooling, and data pipeline work. Built Spark Canary (zombie detection) and WFLinter (GCP Workflow validation) in Python.  
_Used at:_ [Apixio](../experience/apixio.md), [Onyx GSK](../experience/onyx-gsk.md)

**Java** — proficient — historical  
Primary language for early career work in enterprise software and e-commerce infrastructure.  
_Used at:_ [prior-experience](../experience/prior-experience.md)

**Ruby** — familiar — historical  
Built Datacore, Quantcast's production job scheduling and monitoring framework, in Ruby.  
_Used at:_ [Quantcast](../experience/quantcast.md)

**C++** — familiar — historical  
Used in earlier engineering roles.  
_Used at:_ [prior-experience](../experience/prior-experience.md)

**Bash / Zsh** — proficient — active  
Shell scripting for automation, tooling, and DevOps tasks throughout career.

---

## Big Data & Distributed Systems

**Apache Spark** — expert — active  
Deep expertise: Spark SQL, DataFrames, Datasets, UDFs/UDAFs, streaming, Kubernetes deployment, performance tuning (executor sizing, skew handling, memory). Used in production across 7+ companies.  
_Used at:_ [StitchFix](../experience/stitchfix.md), [Demandbase](../experience/demandbase.md), [Jumpshot](../experience/jumpshot.md), [Tatari](../experience/tatari.md), [Apixio](../experience/apixio.md), [Onyx GSK](../experience/onyx-gsk.md)  
_Reference:_ [spark.apache.org](https://spark.apache.org)

**Spark Streaming / Structured Streaming** — proficient — recent  
Extended Cubism to Spark Streaming for continuous multidimensional aggregation at Jumpshot; Kafka-based streaming pipelines at Apixio.  
_Used at:_ [Jumpshot](../experience/jumpshot.md), [Apixio](../experience/apixio.md)  
_Reference:_ [Spark Streaming docs](https://spark.apache.org/docs/latest/streaming-programming-guide.html)

**Delta Lake** — proficient — recent  
Used for silver/gold aggregate tables; diagnosed and resolved write contention issues at Apixio.  
_Used at:_ [Apixio](../experience/apixio.md), [Tatari](../experience/tatari.md)  
_Reference:_ [delta.io](https://delta.io)

**Databricks** — proficient — recent  
Core compute platform for Tatari's Spark-based data processing after migrating off Postgres/Redshift; used for deploying Spark jobs and the Flexible Aggregator.  
_Used at:_ [Tatari](../experience/tatari.md)  
_Reference:_ [databricks.com](https://databricks.com)

**Apache Hive** — expert — historical  
Deep expertise in Hive UDF/UDAF development (Brickhouse), HiveQL query optimization, and MetaStore management. Wrote REST service exposing MetaStore at StitchFix.  
_Used at:_ [Klout](../experience/klout.md), [Quantcast](../experience/quantcast.md), [if(we)](../experience/ifwe.md), [StitchFix](../experience/stitchfix.md), [Jumpshot](../experience/jumpshot.md)  
_Reference:_ [hive.apache.org](https://hive.apache.org)

**Hadoop / MapReduce / HDFS** — expert — historical  
Hands-on from early MapReduce era through YARN. Deep operational experience including cluster optimization and on-call at Klout and Quantcast.  
_Used at:_ [Quantcast](../experience/quantcast.md), [Klout](../experience/klout.md), [if(we)](../experience/ifwe.md)  
_Reference:_ [hadoop.apache.org](https://hadoop.apache.org)

**Apache HBase** — proficient — historical  
Batch writes using HBase UDFs from Brickhouse; built demographic aggregation pipelines writing into HBase at if(we).  
_Used at:_ [if(we)](../experience/ifwe.md), [Klout](../experience/klout.md)  
_Reference:_ [hbase.apache.org](https://hbase.apache.org)

**Apache Livy** — familiar — recent  
Extended a fork of Apache Livy for bug fixes and new features to support Spark-on-Kubernetes deployment at Tatari.  
_Used at:_ [Tatari](../experience/tatari.md)  
_Reference:_ [livy.apache.org](https://livy.apache.org)

**KMV Sketches (Cardinality Estimation)** — proficient — recent  
Implemented KMV sketch-based cardinality estimation and set similarity in Brickhouse, Cubism (Jumpshot), and Zippo (Tatari). Recurring technique for scalable reach/unique-count estimation at high cardinality without exact counts.  
_Used at:_ [Klout](../experience/klout.md), [if(we)](../experience/ifwe.md), [Jumpshot](../experience/jumpshot.md), [Tatari](../experience/tatari.md)

---

## Streaming & Messaging

**Apache Kafka** — proficient — active  
Used as event ingestion bus, intermediate buffer for write contention, and data quality monitoring. Implemented Kafka-based anomaly detection at Jumpshot.  
_Used at:_ [if(we)](../experience/ifwe.md), [Demandbase](../experience/demandbase.md), [Jumpshot](../experience/jumpshot.md), [Tatari](../experience/tatari.md), [Apixio](../experience/apixio.md)  
_Reference:_ [kafka.apache.org](https://kafka.apache.org)

**Apache Beam / Spotify Scio** — proficient — recent  
Built multiple GCP Dataflow pipelines using Beam with Scio at Demandbase (document parsing, streaming sync) and Onyx GSK (150TB ingestion, metadata).  
_Used at:_ [Demandbase](../experience/demandbase.md), [Onyx GSK](../experience/onyx-gsk.md)  
_Reference:_ [beam.apache.org](https://beam.apache.org) · [Scio on GitHub](https://github.com/spotify/scio)

**Apache Avro** — proficient — historical  
Serialization format for event data ingested from Kafka into HDFS via Camus at if(we)'s Ramblas event ingestion system.  
_Used at:_ [if(we)](../experience/ifwe.md)  
_Reference:_ [avro.apache.org](https://avro.apache.org)

**Apache Camus** — familiar — historical  
Used at if(we) for reliable bulk ingestion of Kafka topic data into HDFS, as part of the Ramblas event ingestion system.  
_Used at:_ [if(we)](../experience/ifwe.md)  
_Reference:_ [github.com/linkedin/camus](https://github.com/linkedin/camus)

**Apache Pulsar** — familiar — historical  
Implemented a Pulsar-to-GCP-Pubsub bridge at Demandbase for the Bumblebee streaming framework.  
_Used at:_ [Demandbase](../experience/demandbase.md)  
_Reference:_ [pulsar.apache.org](https://pulsar.apache.org)

**AWS Kinesis** — familiar — historical  
Used as intermediate persistence layer for event ingestion pipeline at StitchFix; built Akka Reactive Streams connector.  
_Used at:_ [StitchFix](../experience/stitchfix.md)  
_Reference:_ [AWS Kinesis](https://aws.amazon.com/kinesis/)

**AMQP** — familiar — historical  
Used as an event source endpoint in the Otherworld event ingestion framework at StitchFix, alongside HTTP REST.  
_Used at:_ [StitchFix](../experience/stitchfix.md)

---

## Cloud Platforms

**Google Cloud Platform (GCP)** — expert — active  
Deep hands-on with Dataflow, BigQuery, GCS, Workflows, Dataproc, Pubsub, Bigtable. GCP has been the primary cloud for the last ~6 years.  
_Used at:_ [Demandbase](../experience/demandbase.md), [Onyx GSK](../experience/onyx-gsk.md)  
_Reference:_ [cloud.google.com](https://cloud.google.com)

**Google BigQuery** — expert — active  
Designing BigQuery table schemas, optimizing slot usage, partition strategies, metadata analysis, and migration from on-prem Hadoop.  
_Used at:_ [Demandbase](../experience/demandbase.md), [Onyx GSK](../experience/onyx-gsk.md)  
_Reference:_ [cloud.google.com/bigquery](https://cloud.google.com/bigquery)

**GCP Dataflow** — expert — active  
Production pipelines for large-scale ingestion (150TB+), streaming sync, document parsing, and table metadata gathering.  
_Used at:_ [Demandbase](../experience/demandbase.md), [Onyx GSK](../experience/onyx-gsk.md)  
_Reference:_ [cloud.google.com/dataflow](https://cloud.google.com/dataflow)

**GCP Dataproc** — proficient — active  
Managed Spark clusters on Dataproc for JDBC ingestion jobs at Onyx GSK.  
_Used at:_ [Onyx GSK](../experience/onyx-gsk.md)  
_Reference:_ [cloud.google.com/dataproc](https://cloud.google.com/dataproc)

**GCP Pub/Sub** — proficient — recent  
Used as the target for the Pulsar-to-Pubsub bridge in Demandbase's Bumblebee streaming framework.  
_Used at:_ [Demandbase](../experience/demandbase.md)  
_Reference:_ [cloud.google.com/pubsub](https://cloud.google.com/pubsub)

**Amazon Web Services (AWS)** — proficient — historical  
Used EMR, S3, Kinesis, DynamoDB, Lambda, CloudWatch, EKS in production at StitchFix and Tatari.  
_Used at:_ [StitchFix](../experience/stitchfix.md), [Tatari](../experience/tatari.md)  
_Reference:_ [aws.amazon.com](https://aws.amazon.com)

**AWS S3** — proficient — historical  
Primary storage layer for event ingestion pipelines at StitchFix; also used at Tatari for data lake storage.  
_Used at:_ [StitchFix](../experience/stitchfix.md), [Tatari](../experience/tatari.md)  
_Reference:_ [AWS S3](https://aws.amazon.com/s3/)

**AWS Lambda** — familiar — historical  
Used as a runtime for evaluating Brule's Rules DSL-defined rules at StitchFix.  
_Used at:_ [StitchFix](../experience/stitchfix.md)  
_Reference:_ [AWS Lambda](https://aws.amazon.com/lambda/)

**AWS CloudWatch** — familiar — historical  
Built Akka Reactive Streams connector for CloudWatch metrics at StitchFix; used for production monitoring.  
_Used at:_ [StitchFix](../experience/stitchfix.md)  
_Reference:_ [AWS CloudWatch](https://aws.amazon.com/cloudwatch/)

---

## Data Storage & Databases

**PostgreSQL / MySQL / Oracle / SQLServer** — proficient — active  
JDBC ingestion from all four at Onyx GSK; Postgres/Redshift migration at Tatari.  
_Used at:_ [Tatari](../experience/tatari.md), [Onyx GSK](../experience/onyx-gsk.md)

**AWS Redshift** — familiar — historical  
Migrated Tatari's data warehouse off Redshift onto Spark/Databricks.  
_Used at:_ [Tatari](../experience/tatari.md)  
_Reference:_ [AWS Redshift](https://aws.amazon.com/redshift/)

**AWS DynamoDB** — familiar — historical  
Built Spark DataSource connector and Akka Reactive Streams connector at StitchFix.  
_Used at:_ [StitchFix](../experience/stitchfix.md)  
_Reference:_ [AWS DynamoDB](https://aws.amazon.com/dynamodb/)

**Cassandra / MongoDB** — familiar — historical  
Used in supporting roles; not featured in specific project descriptions.

---

## Data Pipeline & Orchestration

**Apache Airflow** — proficient — recent  
Deployed ETL DAGs for TV metrics at Tatari; optimized and extended legacy BigQuery DAGs at Demandbase to meet SLAs.  
_Used at:_ [Demandbase](../experience/demandbase.md), [Tatari](../experience/tatari.md)  
_Reference:_ [airflow.apache.org](https://airflow.apache.org)

**GCP Workflows** — proficient — active  
Refactored JDBC ingestion workflow at Onyx GSK; built WFLinter pre-commit validation tool and SDLC model for Workflow development.  
_Used at:_ [Onyx GSK](../experience/onyx-gsk.md)  
_Reference:_ [cloud.google.com/workflows](https://cloud.google.com/workflows)

**Apache Nutch** — familiar — historical  
Extended Nutch for large-scale URL crawling at Demandbase; built crawl metrics framework.  
_Used at:_ [Demandbase](../experience/demandbase.md)  
_Reference:_ [nutch.apache.org](https://nutch.apache.org)

---

## ML/AI Platform

**Vertex AI** — familiar — active  
Used for ML workloads at Onyx GSK (GCP's primary ML platform).  
_Used at:_ [Onyx GSK](../experience/onyx-gsk.md)  
_Reference:_ [cloud.google.com/vertex-ai](https://cloud.google.com/vertex-ai)

**Kubeflow** — familiar — active  
ML pipeline orchestration; used alongside Vertex AI for workflow management at Onyx GSK.  
_Used at:_ [Onyx GSK](../experience/onyx-gsk.md)  
_Reference:_ [kubeflow.org](https://www.kubeflow.org)

**MLflow** — familiar — recent  
Experiment tracking and model registry; used in data platform work at Apixio.  
_Used at:_ [Apixio](../experience/apixio.md)  
_Reference:_ [mlflow.org](https://mlflow.org)

**Stanford NLP (CoreNLP)** — familiar — historical  
Used for Named Entity Recognition and keyword extraction in the Windmill Document Parser Dataflow pipeline at Demandbase.  
_Used at:_ [Demandbase](../experience/demandbase.md)  
_Reference:_ [stanfordnlp.github.io/CoreNLP](https://stanfordnlp.github.io/CoreNLP/)

---

## DevOps & Infrastructure

**Kubernetes / Helm** — proficient — recent  
Deployed Spark on AWS EKS via custom Helm Charts and Docker images at Tatari; extended Apache Livy fork.  
_Used at:_ [Tatari](../experience/tatari.md)  
_Reference:_ [kubernetes.io](https://kubernetes.io) · [helm.sh](https://helm.sh)

**Docker** — proficient — active  
Container builds for Spark workloads; general DevOps use throughout.  
_Used at:_ [Tatari](../experience/tatari.md)  
_Reference:_ [docker.com](https://www.docker.com)

**Terraform** — familiar — active  
Infrastructure-as-code for cloud environments; used in DPE framework workflows at Onyx GSK.  
_Used at:_ [Onyx GSK](../experience/onyx-gsk.md)  
_Reference:_ [terraform.io](https://www.terraform.io)

**Prometheus / Grafana** — proficient — recent  
Built observability dashboards for production Spark pipelines at Apixio; integrated monitoring with alerts at Demandbase.  
_Used at:_ [Demandbase](../experience/demandbase.md), [Apixio](../experience/apixio.md)  
_Reference:_ [prometheus.io](https://prometheus.io) · [grafana.com](https://grafana.com)

**Git pre-commit hooks** — proficient — active  
Built WFLinter as a git pre-commit hook for validating GCP Workflow YAML files before CI/CD submission at Onyx GSK.  
_Used at:_ [Onyx GSK](../experience/onyx-gsk.md)

---

## Reactive & Async Systems

**Akka / Akka Streams** — proficient — historical  
Used Akka for dependency-engine in Satisfaction scheduler, reactive event ingestion at StitchFix, and initial Klout Score scheduling prototype.  
_Used at:_ [Klout](../experience/klout.md), [if(we)](../experience/ifwe.md), [StitchFix](../experience/stitchfix.md)  
_Reference:_ [akka.io](https://akka.io)

**Play! Framework** — proficient — historical  
Satisfaction scheduler UI built with Play! at Klout and if(we); web framework of choice for Scala-based internal tooling.  
_Used at:_ [Klout](../experience/klout.md), [if(we)](../experience/ifwe.md)  
_Reference:_ [playframework.com](https://www.playframework.com)

**Finagle / Finch** — familiar — historical  
Used Twitter's Finagle and Finch to build Ginsberg, a REST microservice exposing the Hive MetaStore, at StitchFix.  
_Used at:_ [StitchFix](../experience/stitchfix.md)  
_Reference:_ [twitter.github.io/finagle](https://twitter.github.io/finagle/)

---

## Open Source

**Brickhouse** — founder & primary maintainer  
Collection of Hive UDFs widely used in the data engineering community. Forked and cloned by hundreds of teams. Covers: KMV sketches (cardinality estimation), HBase I/O, user sessionization, demographic aggregation.  
_Reference:_ [github.com/klout/brickhouse](http://github.com/klout/brickhouse)

**Satisfaction** — founder  
Next-generation Hadoop batch scheduler with Scala DSL, Akka dependency engine, and Play! UI. Replaced Oozie/Jenkins-based workflows at Klout and if(we).  
_Reference:_ [github.com/ifwe/satisfaction](http://github.com/ifwe/satisfaction)

**Apache Hivemall** — committer  
Apache incubating project for scalable machine learning on Hive.  
_Reference:_ [hivemall.incubator.apache.org](https://hivemall.incubator.apache.org)

---

## Leadership & Collaboration

**Mentoring engineers** — proficient — active  
Explicit mentoring of junior and mid-level engineers at Klout, Jumpshot, and Onyx GSK. Introduced common programming model for data development at Klout; educated junior engineers on Big Data techniques at Jumpshot.  
_Used at:_ [Klout](../experience/klout.md), [Jumpshot](../experience/jumpshot.md), [Onyx GSK](../experience/onyx-gsk.md)

**Technical evangelism & community building** — expert — recent  
Sustained track record of open-source community development (Brickhouse, Satisfaction), technical blogging (brickhouseconfessions.wordpress.com), meetup presentations, and stackoverflow engagement. Not just building tools — building adoption.

**Production operations & on-call** — proficient — historical  
Formal on-call rotation at Klout for Hadoop cluster issues; production pipeline monitoring and incident response across multiple companies.  
_Used at:_ [Klout](../experience/klout.md), [Quantcast](../experience/quantcast.md)

**Startup experience** — expert — active  
Has worked at early-to-growth-stage startups throughout career: Quantcast, Klout, StitchFix, Demandbase, Jumpshot, Tatari. Comfortable with small teams, shifting priorities, and wearing multiple hats.

**Cross-functional technical guidance** — proficient — active  
Provided data platform guidance to business analysts (if(we)), proposed SDLC models and testing practices (Onyx GSK), evangelized observability (Apixio). Bridges engineering and data consumer needs.
