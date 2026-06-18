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
---

# Cyanea Systems — Sr. Software Engineer

## Context

Designed and developed infrastructure components for an enterprise J2EE application management software startup.

## Contributions

- **Application Traps** – Designed and developed a subsystem for application-level traps using an event bus architecture. When specified application-level events occur (e.g., a request exceeding a time threshold), email is sent to monitoring users. Implemented front-end JSP/Servlet screens for trap management, introducing an MVC architecture to the organization. Developed an SNMP adaptor for traps to integrate with other system monitoring packages.
- **Performance Improvements** – Implemented order-of-magnitude performance improvements in the "Publish Server" backend component. Improved scalability by reducing thread contention and avoiding unneeded synchronization.
- **Aspect-Oriented Data Collector** – Designed and developed a prototype "Data Collector" component using aspect-oriented techniques. Used BCEL to bytecode-modify customer enterprise applications to include profiling instrumentation — without requiring source changes.
- **Memory Leak Detector** – Designed and developed a prototype memory leak detector using bytecode modification to track "staleness" of objects in Java collections classes.
- **UUID Generator** – Implemented a high-speed, scalable component for generating UUIDs according to the IETF standard.
- **Installer** – Developed and maintained an installer that deploys and updates J2EE applications using WebSphere and WebLogic JMX APIs.

## Outcomes

<!-- not yet captured -->

## Decisions & Tradeoffs

<!-- not yet captured -->

## Tools & Methods

- Java, J2EE
- JSP, Servlets (MVC)
- SNMP
- BCEL (bytecode modification), AspectJ
- WebSphere, WebLogic (JMX)
- Event bus architecture

## Team & Scope

<!-- not yet captured -->
