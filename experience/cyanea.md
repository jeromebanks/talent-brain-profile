---
company: "Cyanea Systems"
slug: "cyanea"
title: "Sr. Software Engineer"
start: "2002-03"
end: "2004-04"
location: ""
employment_type: "full-time"
ingested_sources:
  - file: "Resume 2011 (Google Drive)"
    date: "2026-06-18"
  - file: "excavation"
    date: "2026-06-25"
    note: "structured interview + web research"
---

# Cyanea Systems — Sr. Software Engineer

## Context

Cyanea Systems was an Oakland-based J2EE application performance management (APM) startup — conceptually similar to what New Relic would later become — building tools to monitor and manage enterprise J2EE applications. Its flagship product, Cyanea/One, was resold by IBM as WebSphere Studio Application Monitor. IBM acquired Cyanea in July 2004 (three months after Jerome left), integrating it into the Tivoli systems management portfolio. Lew Cirne's Wily Technology was the primary competitor, also built on bytecode instrumentation.

## Contributions

### Aspect-Oriented Data Collector (Asprobe)
- what: replaced expensive JNI-based method interception with aspect-oriented profiling instrumentation — prototyped with AspectJ, then reimplemented as a custom bytecode modification agent to instrument customer enterprise apps without source changes; renamed "Asprobe" after sales concerns around BCM competitive positioning
- stack: Java, AspectJ, BCEL
- impact: shipped to customers via IBM channel; production use confirmed via IBM support site bug reports

### Memory Leak Detector
- what: bytecode modification tool to detect memory leaks by tracking object staleness in Java collections, without requiring source changes
- stack: Java, BCEL
- impact: shipped as part of the Asprobe bytecode feature set

### Application Traps
- what: application-level event trap subsystem using event bus architecture — email notifications on threshold events, JSP/Servlet management UI, and SNMP adaptor for integration with enterprise monitoring tools
- stack: Java, JSP, Servlets, SNMP
- impact: enabled integration with enterprise monitoring infrastructure (HP OpenView, Tivoli, etc.) via standard SNMP; also introduced an MVC architecture to Cyanea's engineering org in the process of building the management UI

### Performance Improvements
- what: performance and scalability improvements to the Publish Server backend via reduced thread contention and synchronization
- stack: Java
- impact: order-of-magnitude performance improvement

### UUID Generator
- what: high-speed scalable UUID generator per IETF standard
- stack: Java
- impact: supporting infrastructure component used across the product

### Installer
- what: installer for deploying and updating J2EE applications via WebSphere and WebLogic JMX APIs
- stack: Java, WebSphere, WebLogic (JMX)
- impact: customer-facing deployment tooling for enterprise J2EE environments
