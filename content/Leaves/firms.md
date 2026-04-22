---
title: Firms
type: leaf
draft: true
sphere: Socio_Technical
subsphere: Socio_technical_socioeconomic
concept: >-
  Cognised legally registered business entities with stable identity, legal
  form, and lifecycle status
question: 'What firm is this, as a legal registered entity?'
realisations: []
threads: []
tags: []
primary_collection:
primary_collection_path: /Datasets-by-Collection/Grunddatamodellen/CentraleVirksomhedsregister/
entities: []
key_attributes: []
services:
  graphql: >-
    /assets/source-manifests/datafordeler/datafordeler.graphql.services.manifest.v1.json
  source_manifest: /assets/source-manifests/datafordeler/cvr.source.manifest.v1.json
  semantic_map: >-
    /assets/source-manifests/datafordeler/cvr.semantic.entity-attribute-map.v1.json
---

> **Cognised existence:** A firm is a legally recognized business entity that can own assets, incur obligations, report accounts, appoint management, and persist through time even as its activities, addresses, or establishments change.

**Question:** What firm is this, as a legal registered entity?

## What is a Firm?

A firm is not an economic activity, not an establishment, and not a service. It is the **legal business actor** behind those other concepts. It has a stable identity, a legal form, a registration status, and a lifecycle. A single firm may operate many establishments, perform several activities, and hold ownership stakes in other firms.

This leaf is the right starting point when the user wants to identify a company, understand its legal structure, or anchor joins to other business-related concepts.

---

## Realisations

### 1. CVR (CentraleVirksomhedsregister) — Legal Business Entity

The authoritative Danish realisation. [[Datasets by Collection/Grunddatamodellen/CentraleVirksomhedsregister/index|CVR]] models the firm through `Virksomhed`, `CVREnhed`, `Navn`, and `Virksomhedsform`.

#### Spatial Access Path

```
Virksomhed (legal entity)
  │  FK: → CVRAdresse
  ▼
CVRAdresse (registered office / legal address)
  │  normalize address components
  │  → DAR address / house-number match
  ▼
adgangspunkt.position (point geometry via DAR)
```

**Registered office, not operational footprint.** The geometry reached through the firm address represents legal or administrative presence. For where activity happens on the ground, use [[Leaves/business-locations|Business Locations]].

#### Key Entities

| Entity | Role |
| --- | --- |
| **[[Datasets by Collection/Grunddatamodellen/CentraleVirksomhedsregister/virksomhed\\\|virksomhed]]** | Legal business anchor |
| **CVREnhed** | Stable business-side identity |
| **Navn** | Official and alternative names |
| **Virksomhedsform** | Legal form |
| **[[Datasets by Collection/Grunddatamodellen/CentraleVirksomhedsregister/cvradresse\\\|cvradresse]]** | Registered address components |

#### Key Attributes

| Attribute | Description | Notes |
| --- | --- | --- |
| `cvrnummer` | Official firm number | Public business identifier |
| `navn` | Official name | May coexist with trade names / aliases |
| `virksomhedsform` | Legal form | Sole proprietorship, ApS, A/S, foundation, association, etc. |
| `virksomhedstatus` | Registry status | Active, dissolved, under liquidation, etc. |
| `registreringfra` / `registreringtil` | System registration interval | Audit trail |
| `virkningfra` / `virkningtil` | Legal validity interval | Real-world effect |

#### Access

- **GraphQL**: best for targeted firm lookup by CVR number, name, legal form, or status
- **File Download**: best for full business registers and repeatable local joins
- **Semantic bridge**: [[Datasets by Collection/Grunddatamodellen/CentraleVirksomhedsregister/semantic-organisation|CVR Semantic Organisation]]

---

## Realised By Links

- [[Datasets by Collection/Grunddatamodellen/CentraleVirksomhedsregister/index.md|CentraleVirksomhedsregister]] (collection)
- [[Datasets by Collection/Grunddatamodellen/SkatteforvaltningensVirksomhedsregister/index.md|Skatteforvaltningens Virksomhedsregister]] (collection)
## Related Leaves

| Leaf | Relation |
| --- | --- |
| [[Leaves/economic-activities\\\|Economic Activities]] | What the firm does |
| [[Leaves/business-locations\\\|Business Locations]] | Where the firm operates |
| [[Leaves/corporate-ownership\\\|Ownership and Governance]] | Who controls the firm |
| [[Leaves/business-financials\\\|Economics and Employment]] | Financial and workforce characteristics |

## Temporal Model

Firm identity is **bitemporal**. The legal entity can persist while name, legal form, address, activity, and ownership change over time. Historical queries should use `virkning*` for legal state and `registrering*` for system history.
