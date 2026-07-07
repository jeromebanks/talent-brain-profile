---
schema_version: "1.1"
name: "Jerome Banks"
current_title: "Senior Data Platform Engineer"
location: ""
emails:
  - "jerome_banks@yahoo.com"
  - "jerome.banks@gmail.com"
linkedin: "https://www.linkedin.com/in/jerome-banks-8320771"
github: "http://github.com/jeromebanks"
websites:
  - url: "https://brickhouseconfessions.wordpress.com"
    label: "blog"
  - url: "https://github.com/jeromebanks/talent-brain-profile"
    label: "talent-brain profile"
updated: "2026-06-25"
---

# Jerome Banks

> This is a Talent Brain profile. Navigate using the links below and fetch detail files on demand. See [SCHEMA.md](SCHEMA.md) for the agent contract.

_Senior Data Platform Engineer with deep roots in Hadoop/Spark ecosystems and a track record of building foundational open-source infrastructure. Currently focused on cloud-scale data platform work at the intersection of Big Data and ML/AI pipelines._

## Summary

Staff-level data platform engineer with over 15 years building large-scale distributed data infrastructure — from early Hadoop/MapReduce through Apache Spark, cloud-native streaming, and now AI-assisted pipeline engineering. Founded and open-sourced Brickhouse and Satisfaction, infrastructure libraries still used across the data engineering community, and has repeatedly been brought in as the senior technical IC to stand up big data capability from scratch, across ad tech, marketing analytics, and most recently pharma. At GSK, migrated genomics and cell-imaging pipelines to Nextflow/GCP Batch and built AI-assisted tooling — including an approach for generating Nextflow pipelines from legacy scientific code and MCP servers for pipeline operations — to modernize scientific workflow delivery. Currently deepening AI/ML platform expertise while applying distributed-systems fundamentals to large-scale scientific and genomic data.

## Interests & Intent

Targeting Staff+ hands-on IC roles at the intersection of AI/ML and large-scale data engineering — ideally biotech, but any domain involving AI and big data. High autonomy, small collaborative team, SF Bay Area (hybrid).

→ [Full detail](intent.md)

## Core Competencies

Big Data & Distributed Systems Architecture · Data Pipeline Engineering (Batch & Streaming) · Multidimensional Aggregation & Analytics Engineering · Open Source Infrastructure Libraries · Agentic Engineering (Claude Code, MCP, LangGraph) · Mentoring & Technical Evangelism

→ [Full taxonomy with depth/recency signals](skills.md)

## Experience

### Onyx GSK — Senior Data Platform Engineer (2023–2026)
Data platform and pipeline engineering for GSK's scientific and bioinformatics workloads — GCP Dataflow ingestion of 150TB+ cell imaging data, and Nextflow/GCP Batch migrations for the phenomics and 3D cell-segmentation pipelines. Built nf-forge, an AI-assisted approach for generating Nextflow pipelines from existing scientific code (first proven by migrating an HRD-determination workflow in ~4–5 days), plus MCP tooling for GCP operations (adopted by the team for pipeline debugging) and a POC exposing Nextflow pipeline APIs to AI agents. Also built internal Claude Code skills for PR review, JIRA automation, and adversarial code review to raise engineering rigor across the team.
→ [Deep dive](experience/onyx-gsk.md)

### Apixio — Staff Software Engineer, Data Platform (2022–2023)
Stabilized a healthcare document processing pipeline for a small data platform team. Resolved chronic daily pipeline failures by rearchitecting Delta Lake telemetry writes through Kafka; built a zombie-process detector that caught silently stalled Spark jobs before they missed time-critical deadlines; and introduced Prometheus/Grafana observability where none had existed.
→ [Deep dive](experience/apixio.md)

### Tatari — Staff Data Platform Engineer (2020–2022)
Brought in to introduce Big Data to a TV AdTech company with no Spark experience and no budget for managed services. Stood up production Spark on Kubernetes as a zero-cost on-ramp; built multi-dimensional aggregation tooling for combined linear and streaming TV campaign metrics; and shipped a SparkSQL UDF library before the company eventually moved to Databricks.
→ [Deep dive](experience/tatari.md)

### Demandbase — Principal Big Data Engineer (2018–2020)
Built and owned the core data pipelines behind Demandbase's intent signal product — web crawling at millions-of-URLs scale, multi-dimensional engagement aggregates re-architected with the Cubism pattern (adding geo, substantially faster and cheaper), and a streaming sync layer bridging cloud-scale processing with federated per-customer instances from an acquisition. Primary developer on most projects, from conception through production support.
→ [Deep dive](experience/demandbase.md)

### Jumpshot/Avast — Senior Software Engineer (2016–2018)
Built big data infrastructure for a marketing analytics company with exclusive access to opt-in clickstream data from the Avast browser plugin — approximately 100M devices and 435M monthly active users. Key output: Cubism, a multidimensional aggregation library adopted across the San Francisco and Czech Republic engineering teams, which powered FunnelCube (the pipeline behind the E-commerce Insights SaaS product tracking cross-site consumer journeys — browse Walmart, buy on Amazon) and a Spark Streaming sentinel that detected Avast deployment misconfigurations within minutes before they could corrupt downstream pipelines. Also built WillRogers, HDFS disk usage and lineage tooling that supported a legally-mandated cluster migration from Amsterdam to Czech Republic.
→ [Deep dive](experience/jumpshot.md)

### StitchFix — Data Platform Engineer, Algorithms & Analytics (2015–2016)
Platform team of ~6 supporting a large data science and algorithms org. Built production web event ingestion into AWS S3 via Kinesis; a Spark DataSource for reading and writing ML model weights to DynamoDB; a rules engine for customer cohort assignment for targeted marketing; and a Hive MetaStore REST service for internal tooling.
→ [Deep dive](experience/stitchfix.md)

### Tagged.com / if(we) — Senior Software Engineer, Analytics Infrastructure (2014–2015)
Completed and shipped Satisfaction — the asset-based batch orchestrator started at Klout — in production at Tagged, running Ramblas (all application events from a 300M-member platform at half-hour cadence) and Pinkman (demographic aggregates across millions of segments for reach, retention, and engagement). Continued development of Brickhouse open-source UDF library and presented at internal and external meetups.
→ [Deep dive](experience/ifwe.md)

### Klout — Senior Software Engineer (2011–2014)
Technical leader for Big Data at a 50–100 person social influence startup. Built the pipelines behind Klout's topical influence scores — 10,000+ topics across hundreds of millions of users daily, with work contributing to two published research papers. Open-sourced Brickhouse (github.com/klout/brickhouse), a widely-adopted Hive UDF library that originated in an internal analytics warehouse. Designed Satisfaction, an asset-based batch orchestrator that predated Airflow and was later completed and open-sourced at Tagged/if(we).
→ [Deep dive](experience/klout.md)

### Quantcast — Senior Software Engineer (2008–2011)
Hadoop/MapReduce pipelines for web analytics and advertising. Publisher daily measurement job, job scheduling framework in Ruby, cluster job performance optimization.
→ [Deep dive](experience/quantcast.md)

### Pulse Entertainment / Veepers.com — Lead Java Developer (2007–2008)
Primary backend engineer at a San Francisco mobile multimedia startup whose Veepers Media System (VMS) delivered animated speaking avatar characters to Verizon Wireless, AT&T, and KDDI customers across multiple countries. Built scalable Java services for three consumer products — personalized video messaging, custom mobile wallpapers, and a holiday-spiking e-card service — plus a custom C++ JSON parser for the BREW mobile client where no library existed.
→ [Deep dive](experience/pulse-veepers.md)

### BEA BID Division / Plumtree Software — Sr. Software Engineer (2004–2007)
Backend and developer platform engineer at Plumtree Software (acquired by BEA for ~$200M in 2005) across three teams: designed and evangelized the org-wide Spring/JMS remoting stack adopted by enterprise customers' engineering teams, extended the Publisher CMS into a public Enterprise Developer Kit, and implemented the CMS workflow notification service — while advocating Spring dependency injection and unit testing culture across the engineering org.
→ [Deep dive](experience/bea-plumtree.md)

### Lawson Software — Technical Lead (2004)
Six-month engagement at an enterprise ERP vendor; analyzed performance of a Budgeting and Planning application, identified JVM thread contention and database bottlenecks, and delivered architectural recommendations — engagement too short to implement changes.
→ [Deep dive](experience/lawson.md)

### Cyanea Systems — Sr. Software Engineer (2002–2004)
Early APM startup (pre-New Relic era) whose product Cyanea/One was resold by IBM as WebSphere Studio Application Monitor and later acquired by IBM outright; independently developed a bytecode modification instrumentation agent (Asprobe) to profile customer J2EE apps without source changes — the same approach Lew Cirne's Wily Technology was pioneering at the same time. Also built the SNMP monitoring integration and delivered order-of-magnitude performance improvements to the core backend.
→ [Deep dive](experience/cyanea.md)

### diCarta — Sr. Staff Engineer (2000–2002)
Contract management/CRM vendor; architected the XMLAPI integration framework — an XML-based EAI layer with streaming adaptors (HTTP, JMS, EJB, SMTP), pluggable auth, and XML-BO mapping — used by Professional Services and partner SIs to deploy customer integrations with I2, Ariba, and Siebel. Also built Linkin SSO (single-click launch from Ariba Buyer and I2 into diCarta with automatic auth) and an early legally-binding electronic signature feature for PDF contracts — a key product differentiator at the newly-viable e-signature era (ESIGN Act, 2000). Company later acquired by Emptoris (2006), then IBM (2012).
→ [Deep dive](experience/dicarta.md)

### Infoseek / Go.com / Disney Internet Group — Staff Engineer (1999–2000)
E-commerce platform engineer at Go.com (Disney's ~8M-user internet portal, formed from Starwave + Infoseek). Built the topic ontology navigation layer for the portal, payment processing for Go.com's live auctions product, async transaction messaging infrastructure, and a reusable component pattern (Lego) adopted by the e-commerce team. Left after the full Disney acquisition shifted the culture from startup to corporate.
→ [Deep dive](experience/infoseek-go.md)

### Bay One Technologies — Senior Software Engineer (1997–1999)
Software subsidiary powering Discover Brokerage Direct (Lombard Securities, acquired by Dean Witter → Morgan Stanley). Built BrokerSiteManager, the CORBA-based compliance routing layer that distributed pending trades to Series 7-licensed brokers for mandatory human approval before execution. Also added bond trading capability to the platform, introduced unit testing practices to the team, and built a distributed concurrency testing framework for a system where deadlocks had real financial consequences.
→ [Deep dive](experience/bay-one.md)

### Axiologic Corporation (contractor) — NatWest / Deutsche-Morgan Grenfell / Citibank (1995–1997)
Corp-to-corp consultant at three Wall Street firms. At NatWest and Deutsche-Morgan Grenfell, embedded directly with the trading desk — educating on technologies and introducing best practices alongside the delivery work. Built PairTrader and PairMonitor for NatWest's live pairs trading strategy (millions under management, used by traders in production); surfaced multiple arbitrage opportunities at Deutsche-Morgan Grenfell by scanning SEC Edgar filings for keyword signals. At Citibank, led the data migration from a legacy Clipper system to CDS for the production release of a new global swaps trading platform.
→ [Deep dive](experience/axiologic.md)

### Lehman Brothers — Senior Programmer Analyst (1993–1995)
Built and deployed a real-time risk management system for equity traders across multiple desks — calculating Greek option metrics (delta, gamma, theta, etc.) from live price and position changes, displayed in a flashing spreadsheet-like X Windows interface. Event-based distributed C++ architecture, scalable to firm-wide level, ahead of its time for 1993.
→ [Deep dive](experience/lehman.md)

### OFI Corp. — Software Engineer (1993)
Project contracting firm ("Office of the Future") whose major engagement was with General Motors on CAFE fuel efficiency standards software. Implemented foundational C++ container and iterator libraries (pre-STL era — binary search had to be written by hand), a window-based help system, and Oracle database performance improvements via array fetch reimplementation.
→ [Deep dive](experience/ofi.md)

### Timber Hill — Programmer/Analyst / Tech Lead (1991–1993)
Back-office systems for Thomas Peterffy's options trading firm (predecessor to Interactive Brokers). Tech lead for a 3-person team responsible for ensuring all trades cleared. Built an OO security modeling framework in C++, a domain-specific language (Element Description Language) for representing exotic financial instruments with a Lex/Yacc interpreter, an OO persistent-object interface to Ingress, and foundational ADT libraries — all pre-STL.
→ [Deep dive](experience/timber-hill.md)

### AT&T — Consultant via Zyga (1989–1991)
First job out of Caltech, employed by Zyga (a small boutique consulting firm focused on AT&T). Built an early Oracle/Unix commission calculation pipeline for AT&T's hardware sales org, then embedded within an AT&T team building customer support and telemarketing applications on AT&T's proprietary windowing workstations (pre-Windows, pre-Mac, pre-X Windows) and reimplementing the hardware repair tracking system for larger data volumes.
→ [Deep dive](experience/att.md)

## Selected Projects

### Brickhouse
A collection of useful Hive UDFs, widely adopted across the data engineering community. Founded at Klout, maintained through if(we). Includes cardinality estimation (KMV sketches), HBase I/O, user sessionization, and demographic aggregation utilities.
→ [Project detail](projects/brickhouse.md)

### Satisfaction
A next-generation dependency-based Hadoop batch scheduler built in Scala, with a DSL for workflow definitions, a Play! UI, and an Akka dependency engine. Open-sourced at if(we).
→ [Project detail](projects/satisfaction.md)

## Education

### California Institute of Technology
Bachelor of Science, Engineering & Applied Science — emphasis in Computer Science

## Skills

Big Data & Distributed Systems (Spark, Hadoop, Beam/Dataflow, Kafka) · Cloud (GCP, AWS) · AI/Agentic Engineering (MCP, LangGraph, Claude Code Skills) · Scala/Python/Java · Orchestration & DevOps (Airflow, Nextflow, Kubernetes, Terraform)

→ [Full taxonomy](skills.md)

## Extensions

→ [Publications](extensions/publications.md) — acknowledged contributor on two published research papers (LASTA, KDD '14; Klout Topics, K-CAP '17)
→ [Patents](extensions/patents.md) — co-inventor on four granted US patents from Cyanea Systems/IBM application performance monitoring work, plus a Klout patent filing (unissued)
