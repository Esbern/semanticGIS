---
title: "CVR (CentraleVirksomhedsregister) — Per-Entity Reports Realisation of Economics and Employment"
type: realisation
draft: false
leaf: Economics and Employment
dataset: CVR
tags:
  - realisation/cvr_centralevirksomhedsregister
  - leaf/business-financials
---

**Leaf:** [[Leaves/business-financials|Economics and Employment]]
**Dataset:** CVR (CentraleVirksomhedsregister) — Per-Entity Reports

The authoritative per-company realisation. [[Datasets by Collection/Grunddatamodellen/CentraleVirksomhedsregister/index|CVR]] stores annual accounts and employment data per entity.

#### Spatial Access Path

```
regnskab / Beskaeftigelse
  │  FK: CVREnhedsId → Virksomhed / Produktionsenhed
  ▼
Virksomhed / Produktionsenhed
  │  FK: → Adressering → DAR join chain
  │       adresse → husnummer → adgangspunkt.position
  ▼
adgangspunkt.position (point geometry via DAR)
```

**No native geometry.** Financial data attaches to the legal entity. To map it spatially, join through the entity to its address, then through the [[Leaves/addresses|Addresses]] join chain. For production-unit-level employment, use `Produktionsenhed` addresses (see [[Leaves/business-locations|Business Locations]]).

#### Key Entities

| Entity | Role |
| --- | --- |
| **[[Datasets by Collection/Grunddatamodellen/CentraleVirksomhedsregister/regnskab\\\|regnskab]]** | Annual financial accounts (balance sheet, income statement) |
| **[[Datasets by Collection/Grunddatamodellen/CentraleVirksomhedsregister/revision\\\|revision]]** | Audit information |
| **[[Datasets by Collection/Grunddatamodellen/CentraleVirksomhedsregister/revisorrelation\\\|revisorrelation]]** | Auditor assignments |
| **[[Datasets by Collection/Grunddatamodellen/CentraleVirksomhedsregister/finansiel\\\|finansiel]]** | Financial classification data |
| **[[Datasets by Collection/Grunddatamodellen/CentraleVirksomhedsregister/stadfæstelse\\\|stadfæstelse]]** | Account confirmation/approval |
| **Beskaeftigelse** | Employment figures (headcount, FTE) |
| **Kreditoplysninger** | Credit status indicators |

#### Key Attributes

| Attribute | Description | Notes |
| --- | --- | --- |
| `omsaetning` | Revenue | Annual, DKK. Not all companies report this |
| `bruttofortjeneste` | Gross profit | May be reported instead of revenue for smaller firms |
| `resultatfoerskat` | Profit before tax | Key profitability indicator |
| `balancesum` | Total assets (balance sum) | End-of-year balance |
| `ansatte` | Employee count | Headcount at reporting date |
| `aarsvaerk` | Full-time equivalents (FTE) | Better measure of actual workforce size |

#### Reporting Obligations

Not all businesses report the same detail:

| Class | Size | Detail Level |
| --- | --- | --- |
| **A** | Smallest | Minimal — may only show `bruttofortjeneste` |
| **B** | Small/medium | Revenue, profit, balance |
| **C** | Large | Full financial statements with notes |
| **D** | Largest/public interest | Full statements, extended notes, segment reporting |

**Missing fields usually mean the company is exempt from reporting, not that the value is zero.**

#### Employment Data Sources

| Source | Granularity | Frequency |
| --- | --- | --- |
| `Beskaeftigelse` entity | Per-entity headcount + FTE intervals | Quarterly |
| `regnskab` | Annual employment figures in financial report | Annual |

These can differ. `Beskaeftigelse` is more granular (quarterly) while `regnskab` is annual.

#### Access

- **GraphQL**: [[Data Portals/Datafordeleren/graphql|Datafordeleren GraphQL]] — `regnskab` and employment entities queryable
- **File Download**: Bulk export of `regnskab`, `Beskaeftigelse`, join by `CVREnhedsId`
- **Note**: Financial data may have publication delays (annual accounts filed months after year-end)

## Temporal Model

Financial data is inherently **periodic** in addition to being bitemporal. Each `regnskab` record covers a specific accounting period (typically a fiscal year). Employment data (`Beskaeftigelse`) may have quarterly intervals. DST tables are versioned by publication year.
