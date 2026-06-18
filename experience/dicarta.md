---
company: "diCarta"
slug: "dicarta"
title: "Sr. Staff Engineer"
start: "2000-06"
end: "2002-01"
location: ""
employment_type: "full-time"
ingested_sources:
  - file: "Resume 2011 (Google Drive)"
    date: "2026-06-18"
---

# diCarta — Sr. Staff Engineer

## Context

Designed and developed key infrastructure components for this contract management/CRM software vendor.

## Contributions

- **XMLAPI Integration Framework** – Architected, designed, and developed an XML-based integration framework for EAI integrations of the diCarta application with ERP/CRM systems (I2, Ariba, Siebel). Comprised several sub-components:
  - **XML Message Broker** – Core XML message-handling framework: header processing, security checking, message routing, and action invocation. Extensible CRUD message format for importing business objects with support for parent-child relations.
  - **Streaming Adaptor Framework** – Single stream-based interface to the XMLAPI with protocol adaptors for HTTP, EJB/IIOP, JMS, and SMTP. Supported various deployment architectures (3-tier, HTTP-to-EJB, message-based) via configuration.
  - **Authentication Framework** – User authentication supporting multiple credential types (password, certificate, shared-secret) with pluggable mechanisms. Developed an LDAP authentication module with brute-force protection.
  - **XML-BO Mapping Service** – Orthogonal XML-based serialization for Java objects using SAX/JAXP. Supports XML validation, versioning, case-insensitive mode, and message enveloping. Automated code generation with M4.
- **"Linkin" Single Sign-On** – Architected, designed, and developed a Single Sign-On solution to launch the diCarta application from an external application, bypassing the login page securely.
- **Ariba Integration Toolkit** – Designed, developed, and documented a toolkit for integrating diCarta Negotiator with Ariba Buyer. Provided sample scenarios and code; supported key technical customers.
- **Electronic Signatures** – Implemented a legally-binding solution to digitally sign negotiated contracts stored as Adobe PDF files, using Java Cryptography Extensions. Stored an XML representation of the signing ceremony in the PDF trailer.
- **Jabber Chat Prototype** – Implemented a Swing/Applet chat applet to investigate adding IM capabilities to the application. Evaluated chat/IM solutions and studied the Jabber XML protocol.

## Outcomes

<!-- not yet captured -->

## Decisions & Tradeoffs

<!-- not yet captured -->

## Tools & Methods

- Java, J2EE, EJB
- XML, SAX, JAXP, JAXM, JAXB
- JMS, HTTP, SMTP
- LDAP, JNDI
- JDBC, Oracle
- Java Cryptography Extensions (JCE)
- M4 (code generation)
- Adobe PDF

## Team & Scope

<!-- not yet captured -->
