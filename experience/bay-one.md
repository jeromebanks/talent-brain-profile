---
company: "Bay One Technologies"
slug: "bay-one"
title: "Senior Software Engineer, Server Group"
start: "1997-10"
end: "1999-02"
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

# Bay One Technologies — Senior Software Engineer, Server Group

## Context

Bay One Technologies was the software subsidiary originally built inside Lombard Securities to power their online trading platform. Dean Witter acquired Lombard and renamed it Discover Brokerage Direct (1997); after Dean Witter merged with Morgan Stanley, Bay One was kept operationally separate within the larger Morgan Stanley Dean Witter organization. Jerome joined October 1997, immediately after the Discover Brokerage Direct rename, during the explosive growth of retail online trading (competing with E*Trade and Schwab).

## Contributions

### BrokerSiteManager
- what: CORBA server for distributing requests to multiple brokers with role-based priority queues
- stack: Java, CORBA (Iona OrbixWeb)
- impact: compliance-critical backend routing layer for regulated trade approval — distributed pending trades to available Series 7-licensed brokers via role-based priority queues to satisfy regulatory requirement that certain sales and options contracts be human-approved before execution

### Unit Testing Strategy
- what: unit testing strategy for JavaWebServer applications, decoupled from the app server via record/replay of business use cases
- stack: Java, JavaWebServer
- impact: introduced unit testing practices to the team at a time when the discipline was new; adopted across the engineering org to varying degrees

### Distributed Testing Framework
- what: distributed testing framework for concurrency defect detection (deadlock, resource starvation) with runtime metrics
- stack: Java
- impact: provided tooling to surface concurrency defects in a distributed trading system where such failures could be costly; exposed runtime metrics (queue lengths, memory usage) during test runs

### QuoteServer
- what: extension of QuoteServer for bond quote display and real-time heartbeat to guarantee timeliness of bond quote data
- stack: Java
- impact: enabled bond trading capability on the platform, expanding from equities into fixed income; real-time heartbeat guaranteed timeliness of bond quote data

### BrokerApp
- what: maintenance and enhancements to Java AWT client application
- stack: Java, AWT
- impact: the tool through which Series 7-licensed brokers reviewed and clicked to approve regulated trades before execution — effectively turned what had been a client-facing advisory career into a compliance button-pushing role; directly supported regulatory compliance for the platform
