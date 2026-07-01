---
company: "Pulse Entertainment / Veepers.com"
slug: "pulse-veepers"
title: "Lead Java Developer"
start: "2007-05"
end: "2008-09"
location: "San Francisco, CA"
employment_type: "full-time"
ingested_sources:
  - file: "Resume 2008 (Google Drive)"
    date: "2026-06-18"
  - file: "excavation"
    date: "2026-06-25"
    note: "structured interview + web research"
---

# Pulse Entertainment / Veepers.com — Lead Java Developer

## Context

Pulse Entertainment was a San Francisco mobile multimedia startup whose Veepers Media System (VMS) converted static 2D photos into animated 3D speaking avatar characters, delivered as compact video-like files to mobile handsets. Major customers included Verizon Wireless, AT&T, KDDI, and American Greetings, with commercial deployments across the US, Japan, and several other countries. Jerome was the primary backend engineer on a team of ~10–15 people, responsible for backend service development, maintenance, scalability, and on-call production support across three consumer products.

## Responsibilities

### Backend Services
- scope: primary backend engineer across three consumer mobile products; development, maintenance, performance tuning, on-call production support, and direct customer interaction to resolve production issues

### Engineering Practices
- scope: introduced rigorous development practices to a small team with significant technical debt

## Contributions

### ImageFactory
- what: designed and implemented scalable web services for a custom mobile wallpaper product — content repository, caching, streaming architecture, storefront, and service clustering
- stack: Java, Spring, Jackrabbit JCR, ehcache, RMI, Struts2, BREW
- impact: launched and in production; wallpaper purchases via carrier mobile app; did not achieve significant commercial traction

### VMS (Veepers Media System)
- what: backend maintenance and performance work on legacy avatar video generation service — diagnosed bottlenecks, proposed vertical-clustering for multi-core scalability, resolved memory corruption in video encoding library, added QCELP audio codec support for CDMA carrier compatibility
- stack: Java, C++, FFMPEG
- impact: production service delivering personalized video messages to Verizon Wireless, AT&T, and KDDI customers across multiple countries; QCELP support was required for CDMA network delivery (Verizon, Sprint)

### E-card Service
- what: backend scalability work on legacy e-card greeting card service to sustain holiday traffic spikes
- stack: Java
- impact: service remained operational through peak holiday load (Mother's Day and similar); American Greetings was a key customer

### BREW JSON Parser
- what: implemented optimized JSON parser for BREW mobile client to enable REST calls to backend services
- stack: C++, BREW
- impact: no existing library available for the platform; written to run within severe memory and CPU constraints of early mobile hardware
