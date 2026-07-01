---
company: "Onyx GSK"
slug: "onyx-gsk"
title: "Senior Data Platform Engineer"
start: "2023-07"
end: "2026-06"
location: ""
employment_type: "full-time"
ingested_sources:
  - file: "Resume02-2025 (Google Drive)"
    date: "2026-06-18"
  - file: "user excavation"
    date: "2026-06-30"
  - file: "excavation"
    date: "2026-07-01"
    note: "structured interview — AI/ML work (MCP tools, LangGraph, Claude Code SDLC skills, org mindmap), team context, departure date"
---

# Onyx GSK — Senior Data Platform Engineer

## Context

Data Platform Engineering (DPE) team building data and pipeline infrastructure for GSK's scientists, engineers, and decision makers — ingesting large scientific datasets, migrating bioinformatics and imaging workflows to Nextflow/GCP Batch, and supporting production genomics pipelines. Team of roughly 7–9: two senior platform engineers (Jerome plus one peer), 2–3 mid-level engineers, 2–3 junior engineers, occasional contractors, managed by Qi. Despite the "platform engineer" title, the role was closer to a generalist applying deep data-engineering and distributed-systems background to genomics, bioinformatics, and ML workloads — not classic Kubernetes/DevOps platform work. Jerome acquired working domain knowledge in genomics and bioinformatics on the job, and worked closely with ML engineers (on the phenomics pipeline) and with oncologists and research scientists (on HRD and Cellpose3D) to gather requirements and validate results. Later in the role, the team began engaging with GSK's broader AI Scientist / Lab-in-the-loop (LIAL) initiative — the MCP-based Nextflow pipeline API work and Jerome's personal LIAL org mindmap grew out of that direction. Left GSK June 2026.

## Responsibilities

### Production support and operations
- scope: no formal on-call rotation (production issues typically waited for business hours), but ongoing responsibility for fixing production issues and providing workarounds; handling ad hoc data transfer requests from users; running onboarding workshops/labs for new DPE team members; staffing office hours for data engineers with general questions

### Stakeholder collaboration with scientists and ML engineers
- scope: ongoing collaboration with ML engineers on the phenomics pipeline to maintain consistency across codebases they both touched; ongoing engagement with oncologists and research scientists on the HRD and Cellpose3D pipelines to gather and solidify requirements and validate scientific results

## Contributions

### Large Dataset HTTP Ingestion Tool
- what: generic Spark/Dataproc tool for transferring large public datasets over HTTP using range request headers for chunked parallel transfer; recursively scanned source folder structures in a scalable manner to build file manifests, handling datasets with many small files as well as large individual files; used for ingesting public scientific datasets when GCP-native S3 and HTTP transfer services were not yet approved for use within GSK; instrumental for nf-forge development, providing large well-known public datasets for validation and scaling of nf-core pipelines
- stack: Apache Spark, GCP Dataproc, HTTP range requests, GCS
- impact: enabled ingestion of large public scientific datasets into GSK's GCP environment under enterprise transfer constraints; provided the dataset foundation for pipeline validation and scale testing during nf-forge development

### Broad Institute JUMP-CP Cell Painting Ingestion
- what: GCP Dataflow pipeline for ingesting 150TB+ of Cell Painting image data (100B+ files) from the Broad Institute's JUMP-CP dataset from S3 to GCP, with manifest capture of all transferred files
- stack: GCP Dataflow, Apache Beam, GCS, S3
- impact: ingested the full JUMP-CP Cell Painting dataset (150TB+, 100B+ files) — the world's largest public Cell Painting dataset, covering 1B+ cells across 140,000+ chemical and genetic perturbations — into GSK's GCP environment, providing the imaging foundation for downstream phenomics analysis pipelines

### BigQuery Table Metadata
- what: Dataflow pipeline gathering BigQuery table metadata (storage size, partitioning) for analysis and optimization of on-premise Hadoop to GCP migration
- stack: GCP Dataflow, Apache Beam, BigQuery
- impact: <!-- not yet captured -->

### JDBC Ingestion
- what: separate repo and Dataproc Spark job for multi-source JDBC ingestion into BigQuery and GCS (Parquet); handled column-type impedance mismatch across SQL dialects; refactored to include unit tests and docker-compose integration tests running real database engines (Oracle, Postgres, MySQL, SQLServer) in Docker containers
- stack: GCP Workflows, Dataproc, Apache Spark, BigQuery, GCS, JDBC, Docker, docker-compose, Oracle, Postgres, MySQL, SQLServer, Parquet
- impact: established repeatable test model for multi-backend SQL ingestion; docker-compose test harness enabled validation against real DB engines without external dependencies; type casting and impedance mismatch logic verified across all four SQL backends; output to both Parquet and BigQuery supported

### DPE Frameworks — GCP Workflows SDLC
- what: built complete software engineering discipline around GSK's GCP Workflow development, starting from a baseline of versioned YAML templates with no testing, no versioning, and manual deploys; delivered WFLinter (pre-commit YAML validation tool), pytest integration test suite per workflow, WireMock-based error simulation for Google and internal service failures, end-to-end test framework with canned inputs and expected pass/fail outcomes, semantic versioning (feat/fix/chore → MAJOR.MINOR.PATCH via commitizen), and multi-environment CI/CD pipeline (dev → UAT → prod) with ServiceNow change management and Confluence release documentation; scaled to ~12+ workflow templates with a contractor, including support for a new metadata sync process
- stack: GCP Workflows, Terraform, Python, pytest, WireMock, pre-commit, semantic-release, GitHub Actions, ServiceNow, Confluence
- impact: transformed GCP Workflow development from unconstrained YAML file commits to a governed engineering discipline with automated validation, per-workflow test coverage, error-condition simulation, and a full multi-environment release and change management process; team went from zero testing to integration tests + end-to-end harness across ~12+ workflows

### nf-forge
- what: built and applied an early AI-assisted workflow-engineering approach for generating and refining Nextflow pipelines from existing scientific code; first application was migration of an HRD-determination workflow from cHPC-based execution to a running Nextflow pipeline in approximately 4–5 days; subsequent work explored structured scientific PRDs, schema-driven requirements, golden datasets, and nf-core-aware reuse as durable artifacts for reproducible AI-assisted pipeline delivery; longer-term vision was a repeatable system to accelerate creation, migration, and validation of many GSK Nextflow pipelines
- stack: Nextflow, Claude Code Skills, Codex, Gemini LLMs, cHPC
- impact: migrated HRD-determination workflow from legacy cHPC code to a functioning Nextflow pipeline in approximately 4–5 days; created a concrete internal proof point for AI-assisted scientific workflow modernization; demonstrated a practical path from HPC-oriented execution toward cloud-based Nextflow delivery

#### Problem

Scientific and bioinformatics workflows were being developed and run through a mixture of existing cHPC code, manually assembled pipeline logic, and informal requirements. Moving an established scientific calculation onto a modern cloud-oriented workflow platform could require substantial time to understand the existing code, reconstruct its behavior, map execution dependencies, and validate that the migrated workflow produced usable results.

The immediate opportunity was to determine whether AI-assisted workflow generation, combined with structured engineering guidance and Nextflow expertise, could materially shorten that migration cycle while still producing a working scientific pipeline.

#### What I Built

Built and applied an early version of nf-forge, an AI-assisted workflow-engineering approach for generating and refining Nextflow pipelines from existing scientific code. Used Claude Code Skills, Codex, and Gemini LLMs as generation and investigation accelerators, paired with hands-on workflow design, implementation, debugging, and validation.

The first meaningful application was the migration of an HRD-determination workload from cHPC-based execution to a running Nextflow pipeline in approximately 4–5 days.

Subsequent investigation explored structured scientific PRDs, schema-driven requirements, golden datasets, nf-core-aware reuse, staged testing, and reusable lessons learned — moving away from chat-session context toward durable, reviewable artifacts.

The HRD migration was intended as an early proof point for a broader direction: using nf-forge to accelerate, standardize, and eventually automate substantial portions of GSK's Nextflow pipeline development lifecycle — potentially changing the economics and delivery model for scientific workflow development across the organization.

#### Technical Decisions

Used the existing cHPC implementation as the behavioral reference rather than treating the migration as a syntax translation exercise. Scientific logic, execution order, input/output behavior, and expected results had to be reconstructed and preserved in the Nextflow implementation.

Used AI as an engineering accelerator rather than an autonomous author. Generated material was reviewed, adapted, and tested rather than accepted as authoritative.

Focused first on demonstrating value through a real workflow migration rather than building a framework description. Later work moved toward structured artifact models — requirements, validation plans, and lessons learned — to make the approach reproducible and reviewable without relying on ephemeral chat context.

#### Through-Line

nf-forge extends a recurring pattern: taking complex, domain-heavy systems with accumulated operational knowledge and turning them into more reproducible, scalable, and engineerable platforms. Its larger ambition was to make scientific workflow delivery more like a platform capability than a series of bespoke engineering engagements. The project reflects a practical view of agentic engineering: AI is most useful when paired with explicit artifacts, domain constraints, executable validation, and an engineer who can turn generated ideas into working systems.

### Phenomics Nextflow Pipeline
- what: migrated a phenomics image-processing and embedding-generation workflow from a Vertex AI / HPC implementation (one barcode per run, SLURM-style task graph) to a Nextflow DSL2 pipeline on GCP Batch with Seqera Tower; redesigned GPU featurization from ~1.75% GPU utilization on mostly-idle A100s to streaming PyTorch IterableDataset with controlled batching, driving utilization to nearly 100% on T4 GPUs; pipeline active in production
- stack: Nextflow DSL2, GCP Batch, Seqera Tower, Vertex AI, GPU (A100, T4), Docker, Python, PyTorch, HDF5, GCSFuse, n1-standard-8
- impact: reduced single-barcode runtime from ~2h11m (Vertex AI) to ~43m32s (GCP Batch) — roughly 3× faster; scaled from 1 barcode per run to 15; drove GPU utilization from ~1.75% to ~100%; representative run cost ~$1.04 across 45 tasks in 4 Batch jobs

#### Problem

A phenomics image-analysis workflow existed as a Vertex AI implementation that mirrored the original HPC / SLURM execution model — one barcode per run, a granular one-to-one task graph, and GPU featurization running on A100s with approximately 1.75% GPU utilization and 3.29% GPU-memory use, leaving seven of eight GPUs effectively idle.

The workflow needed to be migrated to a reproducible, cloud-scalable platform that could handle multi-barcode runs, replace the fine-grained Vertex orchestration with proper dataflow-oriented execution, and fix the inference data path so that expensive GPU capacity was actually used.

#### What I Built

Migrated the workflow to a Nextflow DSL2 pipeline running on GCP Batch, with Seqera Tower for orchestration, observability, and run management. The prior Vertex implementation processed one barcode per run using a SLURM-style task graph. The Nextflow design used channels, process-level parallelism, task arrays, and job packing to support 15-barcode execution with fewer Batch jobs and better concurrency.

Pipeline stages: TIFF-to-HDF5 conversion, illumination correction factor calculation and application, image and channel combination, tiling large microscopy images into model-ready tiles, GPU-based featurization and embedding generation, structured feature-output generation.

Refactored the GPU featurization stage from memory-heavy bulk loading to a streaming architecture: PyTorch IterableDataset, manifest-driven reads, controlled batch size (256) and worker count (6), incremental CSV output, error tracking and finalization behavior for long-running jobs.

Addressed GCSFuse stale-handle behavior, POSIX assumptions in workflow components, Nextflow work-directory behavior, Tower work-directory overrides, large intermediate artifact handling, and GCP Batch API read quota issues as first-class engineering concerns.

#### Technical Decisions

Replaced Vertex-style fine-grained orchestration with Nextflow dataflow and Batch task arrays. The prior Vertex AI implementation preserved much of the original HPC task structure, resulting in a granular one-barcode execution model. Nextflow channels and job packing enabled 15-barcode execution and reduced representative single-barcode runtime from ~2h11m to ~43m32s.

Matched GPU capacity to the actual inference data path. Initial instrumentation showed A100s were largely idle because the inference path was constrained by data delivery and pipeline structure, not GPU computation. Streaming inputs, worker and batch tuning, and incremental output writing drove GPU utilization to ~100%. T4 GPUs completed featurization in under 30 minutes, eliminating dependence on expensive underutilized A100 capacity.

Established stable operating parameters empirically: batch size 512 / 8 workers caused failures; batch size 256 / 6 workers was stable.

#### Through-Line

Demonstrates the practical engineering required to turn scientific image-analysis code into a cloud-executable workflow — not just translating logic into a new orchestration language, but redesigning data delivery, execution topology, and GPU utilization so the system actually performs at scale.

### Cellpose3D Distributed Segmentation Pipeline
- what: designed and investigated a distributed 3D cell segmentation pipeline for multi-hundred-gigabyte microscopy volumes; used streamed TIFF-to-Zarr conversion, spatial block partitioning with halo overlap, GPU-based Cellpose-SAM inference, and controlled merge logic; identified and fixed a major merge-correctness bug from concurrent writes to shared Zarr chunks; pipeline slated to run against ~100 real patient tissue samples
- stack: Nextflow, GCP Batch, Cellpose-SAM, Zarr, TIFF, GPU, Python, 3D segmentation, Docker
- impact: established viable distributed architecture for Cellpose-SAM 3D segmentation on volumes too large for in-memory execution; demonstrated streamed ingestion of multi-hundred-GB TIFF volumes; corrected lost-update correctness issue in distributed Zarr merge stage; defined validation matrix for boundary-crossing cells, label collisions, and halo-only objects

#### Problem

Very large three-dimensional microscopy image files needed cell segmentation at a scale that could not be handled safely as a single in-memory job. Typical source images were hundreds of gigabytes and contained thousands of Z-slices. A single image volume could exceed available memory and create impractical runtime characteristics for a conventional Cellpose execution model.

The objective was to investigate a distributed Nextflow-based approach for running Cellpose-SAM 3D segmentation over large image volumes while preserving segmentation quality at block boundaries and producing a correct merged output.

#### What I Built

Designed and investigated a distributed 3D segmentation pipeline: streamed TIFF-to-Zarr conversion with chunk shape aligned to segmentation block dimensions, generation of a block manifest with spatial coordinates (Z/Y/X start and end) for each segmentation task, spatial partitioning into independent 3D blocks, halo overlap between blocks for boundary context, GPU-based Cellpose-SAM inference in 3D mode, and a controlled merge stage to reconcile block outputs into final segmentation labels.

Development ongoing as of mid-2026; pipeline is slated to run against approximately 100 real patient tissue samples.

#### Technical Decisions

Used streaming TIFF-to-Zarr conversion to avoid materializing multi-hundred-GB volumes in memory. Chunk shape was treated as a key design decision affecting storage efficiency, block reads, merge behavior, and concurrent-write safety.

Included halo overlap between blocks so Cellpose-SAM could see neighboring context during inference, reducing truncated or missed objects at spatial boundaries. Merge stage required distinguishing core-region labels from overlap-region labels.

Identified and corrected a major merge-stage correctness issue: multiple merge tasks writing to the same Zarr chunks concurrently caused lost updates even when tasks targeted logically different spatial regions. Fix: align chunk boundaries with block boundaries, eliminate uncontrolled concurrent writes, use a controlled sequential final-write stage. Correctness-first — distributed throughput was secondary.

Identified that GPU acceleration applied to model inference while flow-following and final reconciliation remained CPU-bound, affecting the expected performance profile and future scaling design.

Defined a deliberate validation matrix: cells crossing block and halo boundaries, thin structures spanning multiple blocks, multi-channel volumes, label collisions between neighboring blocks, halo-only objects, low-contrast regions, varying halo widths, and uneven object-density distributions.

#### Through-Line

Extends distributed-systems background into scientific imaging workloads where correctness depends on spatial data partitioning, storage layout, and safe reconciliation of parallel results. The central challenge was not running a segmentation model on a GPU — it was making a very large 3D scientific dataset decomposable, distributable, and mergeable without silently corrupting the final result.

### MCP Tools for GCP
- what: FastMCP-based MCP server (~12 tools) exposing GCP Batch, Cloud Run, GCP Workflows, and GCS operations for debugging Nextflow-pipeline job failures and reacting to production incidents, as an alternative to Claude Code writing ad hoc gcloud CLI invocations; included unit tests, an eval framework, and a feedback mechanism where agents could request tool improvements by filing markdown requests (e.g., "return field X so this becomes one call instead of two")
- stack: Python, FastMCP, GCP Batch, Cloud Run, GCP Workflows, GCS, gcloud
- impact: reduced reliance on ad hoc/hallucination-prone gcloud CLI scripting during pipeline debugging; adopted by Jerome and several DPE teammates; not yet presented to the wider AI Scientist org before departure

### MCP Strategy for Domain-Specific Nextflow Pipeline APIs
- what: designed the MCP interface layer for GSK's Nextflow pipelines (run via Seqera Tower behind a governance-mandated WFMS REST gateway) as part of the AI Scientist / lab-in-the-loop (LIAL) direction; each pipeline exposed a hand-written, Pydantic-modeled domain-specific API for validation and ergonomics (with a Claude Code skill in progress to generate these from a template repo); iterated the MCP design from "generate one FastMCP tool per API/OpenAPI endpoint" (which caused context bloat and discoverability problems) to a single generic MCP tool backed by a searchable SKILL-file registry (keyword and hierarchical/type search, e.g. "image processing"), letting an AI Scientist agent discover and invoke the right domain-specific pipeline API without enumerating dozens of tools
- stack: FastMCP, Python, Pydantic, OpenAPI, Nextflow, Seqera Tower, Claude Code Skills
- impact: working POC covering 3–4 pipelines (phenomics, Cellpose3D, one or two nf-core pipelines including rna-seq), with the intent to extend to nearly every nf-core pipeline plus internal ones; under evaluation with other LIAL/platform teams at time of departure

### LangGraph Agent Integration
- what: took over a non-functional LangChain/LangGraph proof-of-concept (built by a contractor in 2025) intended to let researchers trigger pipeline runs via chat (e.g., "run cell-processing on this barcode"); wired in the GCP MCP tools and the Nextflow pipeline-API MCP tools, and added support for the agent reading SKILL files mounted on GCS, aiming to make the LangGraph agent behave as close to Claude Code as possible so local (Claude Code) and cloud (LangGraph) agent environments stayed consistent
- stack: LangChain, LangGraph, Python, MCP, GCS
- impact: got the previously non-working integration functional; handed off to a teammate supporting the LangGraph agent; not deployed before departure due to unrelated UI-side issues

### Claude Code Skills for SDLC and Ergonomics
- what: built a set of internal Claude Code skills to codify and evangelize engineering rigor across the DPE team: a PR review/explanation skill that generated plain-language explanations of large AI-generated PRs, proposed splitting oversized PRs into smaller cohesive ones, and generated comprehension quizzes for junior reviewers; a JIRA skill that authored and groomed tickets to program management's required format (story points, parent linkage, sprint assignment) and checked sprint-review readiness; a skill-documentation generator (javadoc/pydoc-style) that read a repo's skill/command files and produced human-readable docs plus a state-transition graph of the agentic workflow (built to explain nf-forge internally; Jerome may open-source a version of this); and a Gemini adversarial-review skill that had Gemini critique a PR or architectural plan, let Claude respond with fixes, and could loop suggest→fix→review until Gemini approved or a turn limit forced human intervention
- stack: Claude Code Skills, Gemini API, JIRA API, Python
- impact: adopted to varying degrees across a small team that was itself new to Claude Code, within a period of a few months; drove Jerome's own productivity directly; intended primarily as a leadership/mentorship vehicle to raise team-wide engineering rigor

### LIAL Org Mindmap (Obsidian + LightRAG)
- what: personal knowledge-graph tool built to gain visibility into the sprawling AI Scientist / LIAL initiative at GSK — used MCP to spider Confluence wiki pages and GitHub repos into Obsidian, with LightRAG layered on top to unify related concepts across disconnected sources (e.g., recognizing that two teams' documents were both describing the same underlying project)
- stack: Obsidian, LightRAG, MCP
- impact: personal-use only, not adopted by others; helped Jerome understand competing/overlapping projects and identify who to contact on unfamiliar initiatives, in an organization too large and siloed for a single IC to track through normal channels
