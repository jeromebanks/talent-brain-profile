---
company: "BEA BID Division / Plumtree Software"
slug: "bea-plumtree"
title: "Sr. Software Engineer"
start: "2004-10"
end: "2007-05"
location: "San Francisco, CA"
employment_type: "full-time"
ingested_sources:
  - file: "Resume 2011 (Google Drive)"
    date: "2026-06-18"
  - file: "excavation"
    date: "2026-06-25"
    note: "structured interview + web research"
---

# BEA BID Division / Plumtree Software — Sr. Software Engineer

## Context

Plumtree Software was an enterprise portal pioneer (founded 1996) whose product connected enterprise workgroups, IT systems, and business processes via a cross-platform Java EE and .NET portal. BEA Systems acquired Plumtree for ~$200M in October 2005; Jerome joined pre-acquisition and stayed through the BEA integration. He contributed across multiple teams — developer platform, portal standards, and content management.

## Responsibilities

### Engineering Practices
- scope: advocated dependency injection with Spring Framework and a culture of unit testing across the engineering org; added extensive test coverage to codebases that had little; communicated technologies and techniques to developers through wiki entries, email, and internal presentations — these were emerging practices in enterprise software at the time (2004–2007)

## Contributions

### Remoting Framework
- what: designed and evangelized IoC/POJO remoting solution for SOA environment — investigated and certified an open-source stack, built streaming large-file transfer over JMS (brought to parity with JAX-WS), added JMX monitoring via Spring AOP interceptors, prototyped SAML security integration, contributed reconnect logic and queue limits back to upstream open-source projects; built a custom Spring namespace handler for convenient exposure of remote services and a Spring MacroBean to encapsulate common wiring patterns for developer ergonomics
- stack: Spring Framework, Spring AOP, JMS, Lingo, ActiveMQ, JMX, OpenCounters, ACEGI, OpenSAML
- impact: adopted as the organizational remoting standard across Plumtree/BEA's engineering org

### Publisher / EDK (Enterprise Developer Kit)
- what: extended internal Publisher CMS APIs into a public Enterprise Developer Kit for external developers; added extensive unit test coverage
- stack: Java
- impact: customer-facing developer infrastructure for enterprise engineering teams building on Plumtree

### Notification Server
- what: designed and implemented email notification service for CMS publishing workflow — content approval, change requests, and publish events trigger email with MIME attachments, using templating and job scheduling
- stack: Java, Velocity, Quartz
- impact: enabled workflow notification across Plumtree's Publisher CMS product

### .NET Web Accelerator
- what: ported .NET Web Accelerator (tool for displaying .NET apps as Plumtree Portlets) from .NET 1.1 to .NET 2.0
- stack: .NET (C#), JavaScript
- impact: maintained .NET portlet compatibility for enterprise customers upgrading to .NET 2.0

### JSR-168 and WSRP Containers
- what: support and defect fixing for Plumtree's JSR-168 portlet container and WSRP standard implementation
- stack: Java, JSR-168, WSRP
- impact: maintained portlet standards compliance for enterprise customers
