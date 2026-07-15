---
name: "Brickhouse"
slug: "brickhouse"
type: "open-source"
status: "archived"
company: "Klout (open-sourced)"
start: "2012-01"
end: "2015-07"
url: "https://github.com/jeromebanks/brickhouse"
ingested_sources:
  - file: "Resume02-2025 (Google Drive)"
    date: "2026-06-18"
  - file: "excavation"
    date: "2026-07-15"
    note: "structured interview plus web research (GitHub, Maven Central, Apache wiki, brickhouseconfessions.wordpress.com)"
---

# Brickhouse

## Problem

Hadoop/Hive ecosystems lacked a reusable, community-curated library of UDFs for common data engineering patterns — reach estimation, sessionization, HBase I/O, demographic aggregation, and more. Each team was reinventing these tools in isolation.

## What I Built

A collection of Hive UDFs, packaged and open-sourced at github.com/klout/brickhouse. Founded at Klout, continued and expanded at if(we). The core idea was letting engineers express complex data pipeline patterns declaratively in SQL instead of hand-writing MapReduce jobs — collapsing multi-step, procedural pipeline logic into a single Hive query. Includes UDFs for: aggregating rows into maps/arrays to replace self-joins (`collect`/`collect_max`), broadcasting small lookup tables into mappers to avoid joins (`distributed_map`), salting to handle skewed keys, KMV sketch-based cardinality estimation, HBase batch reads/writes, user sessionization, demographic XUnit explosion, and time-series utilities. Evangelized through tech meetups, blog posts at brickhouseconfessions.wordpress.com, and stackoverflow answers. Widely forked and cloned across the data engineering community.

## Impact

Brickhouse's declarative UDFs became core production infrastructure at Klout: the sketch-based reach estimator, for instance, replaced a naive approach (collecting unique retweeter IDs into an in-memory array) that hit OOM crashes on high-follower "whale" accounts (e.g. One Direction) in the Maxwell pipeline computing the Klout Score — expressible in SQL instead, it became the org-wide solution and continued in production use at Tagged/if(we). Adoption went well beyond Klout: 573 forks and 33 external contributors on GitHub, published to Maven Central as `com.klout:brickhouse` (through version 0.6.0+), and evangelized through a four-year blog run (brickhouseconfessions.wordpress.com, 2013–2017, including at least one external guest post) and a talk hosted on the Apache Software Foundation's own wiki ("Building the Brickhouse — Enhancing Hive with our UDF Library"). Known to have been carried by former Klout engineers to companies including Apple Music and Lyft, and anecdotally used at Facebook; a confirmed external fork exists from chaordic, a Brazilian e-commerce personalization company. The library's core ideas outlived Hive itself: the declarative-pipeline instinct, and specific techniques like XUnit-style multidimensional aggregation, were re-implemented a few years later as Cubism, a Spark-based, more functional successor built at Jumpshot and Demandbase, once the industry moved past Hive UDFs. The original `klout/brickhouse` GitHub repo went offline after Klout's 2018 shutdown; Jerome has maintained it under his own account since, though active demand for new Hive UDFs has faded.

## Technical Decisions

The central design principle: give Hive engineers UDFs that let a single SQL query express a pipeline pattern that would otherwise take several procedural MapReduce/Spark stages to write correctly. `collect`/`collect_max` aggregate related fields into an array/map directly, replacing the expensive self-join anti-pattern (join a table to itself on ID to combine rows) with a single group-by. `distributed_map` used Hive's distributed cache to broadcast small lookup tables into mappers, avoiding a join against a large table for what was really just a lookup — an early manual analog of what later became broadcast joins. The `union_max`/salting technique ("Defeat the Titans with salt") addressed data skew directly in SQL: randomly salting high-cardinality keys to spread aggregation across more reducers, then merging partial results in a second query — later generalized into `union_sketch` for merging sketch sets. That same "push more into declarative SQL" instinct also produced the sketch-based UDFs: reach/cardinality estimation (KMV, and later HyperLogLog, added based on an existing open-source implementation once a solid one existed to adopt) let a `SELECT ... GROUP BY` compute approximate uniques instead of requiring a bespoke job, and HBase UDFs (`hbase_batch_put`/`hbase_cached_get`) let a Hive query read/write an external key-value store directly, scaling Bayesian document classification (Topic Thunder) past what fit in one job. Brickhouse itself originated as an internal Klout UDF library called "warehouse," open-sourced once it proved broadly useful. The contributor community was deliberately loose — "stone soup" style, in Jerome's words — with contributors adding whatever capability they personally needed rather than the project being centrally managed or curated.

## Through-Line

The same pattern recurs across Jerome's whole career: notice that a class of production problem is being solved with brittle, hand-written procedural code, and build a declarative, composable abstraction that lets people express the same intent more simply — then open it up and let others extend it. Brickhouse did this for Hive pipelines; the same instinct, applied to Spark a few years later at Jumpshot and Demandbase, produced Cubism. It's the earliest evidence in this profile of the pattern that later produced nf-forge and Talent Brain: build the missing tool as reusable infrastructure rather than a one-off fix.
