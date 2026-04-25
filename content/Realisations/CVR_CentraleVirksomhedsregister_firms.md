---
title: "CVR (CentraleVirksomhedsregister) — Legal Business Entity Realisation of Firms"
type: realisation
draft: false
leaf: Firms
dataset: CVR
tags:
  - realisation/cvr_centralevirksomhedsregister
  - leaf/firms
---

**Leaf:** [[Leaves/firms|Firms]]
**Dataset:** CVR (CentraleVirksomhedsregister) — Legal Business Entity

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

## Temporal Model

Firm identity is **bitemporal**. The legal entity can persist while name, legal form, address, activity, and ownership change over time. Historical queries should use `virkning*` for legal state and `registrering*` for system history.
