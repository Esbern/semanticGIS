---
title: "CVR (CentraleVirksomhedsregister) — DB25 Industry Code Realisation of Economic Activities"
type: realisation
draft: false
leaf: Economic Activities
dataset: CVR
tags:
  - realisation/cvr_centralevirksomhedsregister
  - leaf/economic-activities
---

**Leaf:** [[Leaves/economic-activities|Economic Activities]]
**Dataset:** CVR (CentraleVirksomhedsregister) — DB25 Industry Code

The authoritative per-entity realisation. [[Datasets by Collection/Grunddatamodellen/CentraleVirksomhedsregister/index|CVR]] classifies every registered business via the `Branche` entity.

#### Spatial Access Path

```
Branche (activity code)
  │  FK: CVREnhedsId
  ▼
Virksomhed / Produktionsenhed
  │  FK: → Adressering → DAR join chain
  │       adresse → husnummer → adgangspunkt.position
  ▼
adgangspunkt.position (point geometry via DAR)
```

**No native geometry.** To map activities spatially, join through the business entity to its address, then through the [[Leaves/addresses|Addresses]] join chain to coordinates.

#### Key Entities

| Entity | Role |
| --- | --- |
| **Branche** | Carries the industry code and text. A business may have multiple (primary + secondary) |
| **Virksomhed** | Legal business entity that branches attach to |
| **Produktionsenhed** | Operational establishment — may have its own branch set |

#### Key Attributes

| Attribute | Description | Notes |
| --- | --- | --- |
| `branchekode` | DB25 industry code | Compact form without dots: `561110` not `56.11.10`. Since Jan 2025, CVR uses DB25 (NACE Rev 2.1), replacing DB07 |
| `branchetekst` | Human-readable description | Danish language |
| `hovedbranche` | Primary activity flag | `true` = main activity of the business |

#### DB07 → DB25 Transition

As of January 2025, CVR stores **DB25** codes (Danish implementation of NACE Rev 2.1). Older records may still carry DB07 codes. CVR stores codes **without dots** — strip dots when matching against external references using dotted format (e.g., `56.11.10`).

- [[Datasets by Collection/Grunddatamodellen/CentraleVirksomhedsregister/codebook-and-normalization|CVR Codebook and Normalization]]
- DST conversion table: [DB07-DB25 concordance](https://www.dst.dk/da/Statistik/dokumentation/nomenklaturer/db)

#### Access

- **GraphQL**: [[Data Portals/Datafordeleren/graphql|Datafordeleren GraphQL]] — query `Branche` with filters on `branchekode`
- **File Download**: Bulk `Branche` entity export, join locally to `Virksomhed`
- **Semantic map**: [[Datasets by Collection/Grunddatamodellen/CentraleVirksomhedsregister/semantic-organisation|CVR Semantic Organisation]]

## Temporal Model

Industry classification is **bitemporal** (inherited from [[Datasets by Collection/Grunddatamodellen/Shared Temporal Superclass Contract|Shared Temporal Superclass Contract]]). A business can change its primary industry over time. Historical queries require `virkningFra`/`virkningTil` filtering.
