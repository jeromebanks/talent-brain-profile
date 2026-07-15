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

A collection of useful Hive UDFs, packaged and open-sourced at github.com/klout/brickhouse. Founded at Klout, continued and expanded at if(we). Includes UDFs for: KMV sketch-based cardinality estimation, HBase batch reads/writes, user sessionization, demographic XUnit explosion, and time-series utilities. Evangelized through tech meetups, blog posts at brickhouseconfessions.wordpress.com, and stackoverflow answers. Widely forked and cloned across the data engineering community.

## Impact

Adopted well beyond Klout: 573 forks and 33 external contributors on GitHub, published to Maven Central as `com.klout:brickhouse` (through version 0.6.0+), and evangelized through a four-year blog run (brickhouseconfessions.wordpress.com, 2013–2017, including at least one external guest post) and a talk hosted on the Apache Software Foundation's own wiki ("Building the Brickhouse — Enhancing Hive with our UDF Library"). Known to have been carried by former Klout engineers to companies including Apple Music and Lyft, and anecdotally used at Facebook; a confirmed external fork exists from chaordic, a Brazilian e-commerce personalization company. The KMV sketch-based reach estimator solved a real production failure: Klout's Maxwell pipeline computing the Klout Score hit OOM crashes processing "whale" accounts (e.g. One Direction) because the naive approach — collecting all unique retweeter IDs into an in-memory array — couldn't scale past a certain follower count no matter the memory settings. The sketch approach became the org-wide solution at Klout and continued in production use at Tagged/if(we). The library's core ideas outlived Hive itself: XUnit-style multidimensional aggregation and reach-estimation sketches were re-implemented a few years later as Cubism, a Spark-based, more functional successor built at Jumpshot and Demandbase, once the industry moved past Hive UDFs. The original `klout/brickhouse` GitHub repo went offline after Klout's 2018 shutdown; Jerome has maintained it under his own account since, though active demand for new Hive UDFs has faded.

## Technical Decisions

Chose KMV (K-Minimum Values) sketches over HyperLogLog for reach/cardinality estimation — not because KMV is theoretically superior, but because Jerome had already used the approach at Quantcast (PipeV3) and judged it far simpler to implement correctly as a Hive UDAF, with less risk of the subtle correctness bugs a from-scratch HLL implementation invites (retaining the 5,000 lowest MD5 hashes per key). An HLL implementation was added to Brickhouse later, based on an existing open-source implementation, once a solid one was available to adopt rather than build. `collect`/`collect_max` were designed to avoid two idiomatic Hive anti-patterns — self-joins and unnecessary UDTFs — by aggregating related fields into an array/map directly. `distributed_map` used Hive's distributed cache to broadcast small lookup tables into mappers, an early manual analog of what later became broadcast joins. The `union_max`/salting technique ("Defeat the Titans with salt") addressed data skew directly: randomly salting high-cardinality keys to spread aggregation across more reducers, then merging partial results — later generalized into `union_sketch` for merging sketch sets. HBase UDFs (`hbase_batch_put`/`hbase_cached_get`) let Bayesian document classification (Topic Thunder) scale past what fit in a single Hive job by using HBase as an external key-value store for millions of features. Brickhouse itself originated as an internal Klout UDF library called "warehouse," open-sourced once it proved broadly useful. The contributor community was deliberately loose — "stone soup" style, in Jerome's words — with contributors adding whatever capability they personally needed rather than the project being centrally managed or curated.

## Through-Line

The same pattern recurs across Jerome's whole career: notice a missing infrastructure layer inside a production system, generalize the fix into something composable, and let it outlive the original problem. The KMV reach-estimation and XUnit-style multidimensional aggregation techniques in Brickhouse were carried over from work at Quantcast, then reborn again a few years later as Cubism — a Spark-based, more functional successor built at Jumpshot and Demandbase once the ecosystem moved past Hive. Brickhouse is the earliest evidence in this profile of the instinct that later produced nf-forge and Talent Brain: build the missing tool as reusable infrastructure, open it up, and let others take what they need.
