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
  - file: "Resume-2002 (local)"
    date: "2026-06-29"
  - file: "excavation"
    date: "2026-06-29"
    note: "structured interview"
---

# diCarta — Sr. Staff Engineer

## Context

Key infrastructure components for a contract management/CRM software vendor.

## Contributions

### XMLAPI Integration Framework
- what: XML-based EAI integration framework for connecting diCarta with ERP/CRM systems (I2, Ariba, Siebel) — includes XML message broker, streaming adaptor (HTTP/EJB/JMS/SMTP), authentication framework (password/cert/shared-secret with LDAP module), and XML-BO mapping service with code generation
- stack: Java, J2EE, EJB, XML, SAX, JAXP, JMS, HTTP, SMTP, LDAP, JNDI, M4
- impact: enabled Professional Services and partner SIs to build customer EAI integrations with ERP/CRM systems (I2, Ariba, Siebel) without one-off custom work; deployed across multiple customer accounts

### Linkin Single Sign-On
- what: SSO solution for launching diCarta from external applications, bypassing the login page securely
- stack: Java, J2EE
- impact: enabled Ariba Buyer and I2 users to launch diCarta Negotiator in a single click with automatic authentication; removed the separate login step for users of both procurement platforms

### Ariba Integration Toolkit
- what: toolkit for integrating diCarta Negotiator with Ariba Buyer, with documentation, sample scenarios, and technical customer support
- stack: Java, XML
- impact: supported key technical customers

### Electronic Signatures
- what: legally-binding digital signing solution for PDF contracts using Java Cryptography Extensions, with XML signing ceremony record stored in PDF trailer
- stack: Java Cryptography Extensions (JCE), Adobe PDF, XML
- impact: shipped as a key differentiating product feature at a time when legally-binding e-signatures were newly viable (ESIGN Act, June 2000); customers executed negotiated contracts with full legal authority in electronic form

### Jabber Chat Prototype
- what: prototype IM/chat applet to evaluate adding in-application chat capabilities
- stack: Java, Swing, Jabber XML protocol
- impact: prototype implemented and delivered; productization and adoption beyond this tenure unknown
