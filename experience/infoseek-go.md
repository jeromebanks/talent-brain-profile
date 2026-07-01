---
company: "Infoseek / Go.com / Disney Internet Group"
slug: "infoseek-go"
title: "Staff Engineer, E-Commerce Group"
start: "1999-02"
end: "2000-03"
location: ""
employment_type: "full-time"
ingested_sources:
  - file: "Resume 2011 (Google Drive)"
    date: "2026-06-18"
  - file: "Resume-2002 (local)"
    date: "2026-06-29"
  - file: "excavation"
    date: "2026-06-29"
    note: "structured interview"
---

# Infoseek / Go.com / Disney Internet Group — Staff Engineer, E-Commerce Group

## Context

Server-side e-commerce platform and infrastructure for Go.com — Disney's internet portal formed from Starwave + Infoseek. Jerome joined February 1999 as Go.com was ramping up, as part of the platform team supporting e-commerce, auctions, and other verticals. Disney completed its full acquisition of Infoseek in November 1999, at which point the culture shifted from startup to corporate; Jerome left in March 2000. Go.com launched with ~8M users and was shut down by Disney in 2001 at a cost of $878M.

## Contributions

### BxsonMgr
- what: Java package for accessing topic ontology from a remote server over HTTP/XML
- stack: Java, XML, HTTP
- impact: powered topic category navigation on the Go.com portal (Yahoo-style click-through ontology) at ~8M users at launch

### QueryBean
- what: Java JDBC result access package for the proprietary Tea templating language using JavaBeans
- stack: Java, JDBC, Tea
- impact: eliminated boilerplate for e-commerce team developers accessing JDBC results from the Tea templating layer; adopted within the e-commerce group

### JTP-Servlet Bridge
- what: Servlet 2.1 engine bridge for the proprietary JTP application server
- stack: Java, Servlets
- impact: enabled use of standard Servlet 2.1 components within the proprietary JTP server, unlocking compatibility with the broader Java web ecosystem

### MessagePipeline
- what: transactional message queue for application integration, with advocacy for message-based architecture across the org
- stack: Java, JMS
- impact: provided async integration backbone for e-commerce; message-based architecture pattern adopted by the e-commerce team

### CreditCardAuth
- what: credit card authorization package with fraud/not-fraud logic, async authorization via message queues, and cross-system result relay
- stack: Java, JMS, Oracle
- impact: powered payment processing for Go.com's live auction product; handled async authorization and fraud classification (product launched but did not reach expected transaction volume competing with eBay)

### Lego Design Pattern
- what: design pattern for code reuse across web pages, proposed and evangelized org-wide
- stack: Java
- impact: adopted by the e-commerce team, reducing code duplication across web page components

### OMS
- what: Java interface to Order Management System via Oracle stored procedure calls
- stack: Java, JDBC, Oracle
- impact: bridged the e-commerce platform to the Order Management System via a clean Java API over Oracle stored procedures

### CommentLego / ShippingAddressLego
- what: reusable web components for customer service annotation and ECML-standard shipping address processing
- stack: Java, Servlets
- impact: reusable ECML-standard shipping and customer service annotation components for the Go.com e-commerce platform

### Merchant Extranet
- what: merchandizing and product information management system (team contribution)
- stack: Java, Servlets
- impact: team contribution; delivered merchandizing and product information management for Go.com commerce verticals
