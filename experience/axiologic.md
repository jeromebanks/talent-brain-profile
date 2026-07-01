---
company: "Axiologic Corporation (Independent Contractor)"
slug: "axiologic"
title: "Independent Contractor"
start: "1995-02"
end: "1997-10"
location: "New York, NY"
employment_type: "contract"
ingested_sources:
  - file: "Resume 2011 (Google Drive)"
    date: "2026-06-18"
  - file: "Resume-2002 (local)"
    date: "2026-06-29"
  - file: "excavation"
    date: "2026-06-29"
    note: "structured interview"
---

# Axiologic Corporation — Independent Contractor

## Context

Consulting to Wall Street financial firms via a personal S-corporation billed corp-to-corp (1099). Three sequential client engagements: NatWest and Deutsche-Morgan Grenfell were true consulting engagements — embedded directly with trading desks, educating on technologies and introducing best practices in a semi-casual, collaborative environment alongside traders who sometimes wrote their own code. Citibank was a more formal enterprise engagement focused on delivery.

## Contributions

### NatWest Markets — Equity Proprietary Trading (August 1996–October 1997)

Front-office trading applications for equity arbitrage strategies.

#### PairMonitor
- what: real-time analytic tool for monitoring hundreds of securities pairs for trading signals, with sorting, filtering, and historical graphing
- stack: C++, X/Motif, Xrt Table Widget
- impact: used by the trading desk to monitor hundreds of securities pairs in real-time for pairs trading signals; supported a strategy with millions of dollars under management

#### Formula / Depends / DataService Libraries
- what: C++ computational infrastructure for real-time calculation of arbitrary complex analytic expressions from tiered data sources
- stack: C++
- impact: used across multiple projects in the group

#### TimeSeries Library
- what: C++ template class library for time-related data containers supporting multiple time frequencies and holiday schedules
- stack: C++
- impact: foundational data structure supporting time-frequency-aware analytics across the group's trading tools

#### Screening Universe
- what: periodic Sybase database of stocks meeting market cap and traded value criteria, generated from multiple data sources
- stack: C++, Sybase, FAME, shell scripting, SQL
- impact: automated periodic stock filtering for the desk's investment universe selection

#### FameClasses
- what: C++ class library for object-oriented access to FAME time-series databases
- stack: C++, FAME
- impact: simplified access to FAME time-series data across the group's tools, abstracting the FAME API into an OO interface

#### PairTrader
- what: decision support tool for pairs trading with real-time position analytics and Reuters news integration
- stack: C++, X/Motif, Xrt Table Widget
- impact: powered the trading desk's live pairs trading strategy — buying and shorting correlated stocks to capture price convergence on shared news; used by Sam Glassman and the traders on positions with millions of dollars under management; integrated into the firm's position management system

### Responsibilities (NatWest)

#### Desk Consulting & Technology Advocacy
- scope: NatWest equity proprietary trading desk
- Embedded directly with the trading desk in a semi-casual, collaborative working relationship; translated trading strategies into software requirements
- Consulted in the true sense: educated traders and the group on software technologies and introduced engineering best practices alongside the delivery work

### Deutsche-Morgan Grenfell — Equity Arbitrage (October 1995–August 1996)

Front-office trading applications supporting the equity arbitrage desk directly.

#### Edgar Expression Scanning
- what: Perl/Expect scripts to analyze SEC Edgar filings, auto-generate web pages with keyword expressions, and notify traders of filings for companies on their watchlists
- stack: Perl, Expect
- impact: surfaced arbitrage opportunities by detecting specific phrases in SEC filings (e.g., "opening up" indicating capital raises) before the market could price them in; identified multiple actionable opportunities for the desk

#### RPC Proxy Libraries
- what: Windows DLL proxy libraries that remotely invoked functions on another machine via ONC RPC
- stack: ONC RPC, Windows DLL, C++
- impact: enabled cross-machine function calls from Windows trading workstations to remote servers, supporting distributed system architecture on the desk

#### FAME Database Wrapper
- what: C++ class library making FAME time-series database appear like a relational database
- stack: C++, FAME
- impact: simplified access to FAME price data for the desk's C++ applications by abstracting the FAME API into a familiar relational-style interface

#### Monte Carlo Pricing Library
- what: C++ library for Monte Carlo pricing of derivative securities, extensible to increasingly complex derivative types
- stack: C++
- impact: provided extensible C++ pricing infrastructure for a desk where some traders wrote their own code and needed a foundation for complex derivative types

#### Financing Model
- what: modification of existing applications to incorporate a stock-loan financing model for comparison with back-office calculations
- stack: C++, Sybase
- impact: enabled the desk to compare stock-loan financing costs against back-office P&L calculations for more accurate position accounting

#### Treasury Note Conversion Factors
- what: automated self-updating database of Treasury Note conversion factors for cheapest-to-deliver calculation
- stack: C++, Sybase
- impact: automated cheapest-to-deliver calculation for treasury note arbitrage strategies; self-updating from source data

### Responsibilities (Deutsche-Morgan Grenfell)

#### Desk Consulting & Technology Advocacy
- scope: Deutsche-Morgan Grenfell equity arbitrage desk
- Embedded directly with the desk in an informal, collaborative working relationship alongside Tracy Fu and quant traders who wrote their own code; worked shoulder-to-shoulder on trading strategies and tooling
- Consulted in the true sense: educated the desk on software technologies and introduced engineering best practices

### Citibank — Global Derivatives (February 1995–October 1995)

Development on CDS, a large-scale global derivative trading system.

#### Data Conversion
- what: led three-person team to convert data from legacy swap trading systems to CDS for the production release
- stack: C++, Sybase
- impact: led successful migration of trading data from the legacy Clipper system to CDS, unblocking the production release of Citibank's new global swaps trading platform

#### Database Security System
- what: C++ library and Sybase stored procedures extending the CDS security mechanism for finer-grained data access control
- stack: C++, Sybase
- impact: extended CDS security model to support finer-grained data access control across desks and users of a large-scale global derivatives platform

#### ReportWriter
- what: support and extension of a GUI report writer application
- stack: Teleuse, Sybase SQR
- impact: maintained reporting capability for the global derivatives desk on CDS
