---
company: "Timber Hill"
slug: "timber-hill"
title: "Programmer/Analyst"
start: "1991-09"
end: "1993-03"
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

# Timber Hill — Programmer/Analyst

## Context

Timber Hill was Thomas Peterffy's options trading firm — already doing electronic options trading before Jerome joined, and later the foundation for Interactive Brokers. Jerome focused on the backend and back-office: ensuring all trades cleared and processed correctly. Served as tech lead and manager for a 3-person back-office development team while primarily working as an IC.

## Contributions

### Security Framework
- what: object-oriented C++ framework modeling financial securities for back-office use
- stack: C++
- impact: core back-office model for the financial securities Timber Hill traded; foundation for the Element Description Language's pricing and margin virtual dispatch

### Element Description Language
- what: recursive language for describing financial securities, with a Lex/Yacc interpreter
- stack: C++, Lex, Yacc
- impact: DSL for representing exotic financial instruments of the era; solved a compatibility/interoperability problem between systems by providing a common declarative representation with virtual dispatch for per-security pricing and margin calculations

### OO DBMS Interface
- what: object-oriented C++ interface to the Ingress relational database
- stack: C++, Ingress
- impact: enabled C++ application code to treat Ingress database records as persistent objects; clean OO abstraction over the relational layer for the back-office codebase

### Utility Base Class Libraries
- what: C++ base class libraries with fundamental abstract data types — Stacks, Queues, BTrees, Bags, ReferenceCounters, Tries
- stack: C++
- impact: foundational ADT library for ongoing back-office development — pre-STL era, these had to be built from scratch

## Responsibilities

### Tech Lead & Back-Office Operations
- scope: back-office development team, Timber Hill
- Managed a 3-person back-office development team as tech lead; primarily worked as IC
- Responsible for ensuring all trades cleared correctly on an options trading desk running Thomas Peterffy's personal account
