---
title: Economics and Employment
type: leaf
draft: true
sphere: Socio_Technical
subsphere: Socio_technical_socioeconomic
concept: >-
  Cognised economic scale, financial performance, and workforce characteristics
  of firms and establishments
question: >-
  What are the economic and employment characteristics of a firm or
  establishment?
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

> **Cognised existence:** Economics and employment describe the measurable scale of a firm's activity — revenue, profit, assets, employment, and workforce intensity. The concept exists whether you read it from a company's filed annual report or from an aggregated statistical table. The granularity and access differ dramatically between sources.

**Question:** What are the economic and employment characteristics of a firm or establishment?

## What are Economics and Employment?

Economics and employment are not the firm itself (that's [[Leaves/firms|Firms]]). They are the *measurable scale and performance* of the firm or establishment — how much money flows in, how many people work there, how large the asset base is, and how labor is distributed over time. Understanding which sources carry what level of detail, and what reporting obligations apply, is critical for avoiding false zeroes (missing ≠ zero).

---

## Realisations

### 1. CVR (CentraleVirksomhedsregister) — Per-Entity Reports

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

### 2. Danmarks Statistik — Aggregated Statistics

DST publishes sectoral financial and employment statistics via [Statistikbanken](https://www.statistikbanken.dk/).

#### Spatial Access Path

```
Statistical table (NACE sector × municipality/region)
  │  FK: municipality/region code
  ▼
DAGI administrative polygon (via kommune/region geometry)
```

**1 join** to geometry — aggregated figures are keyed to administrative areas realised by [[Leaves/administrative-units|Administrative Units]].

#### Key Tables

| Table | Content |
| --- | --- |
| `FIRSTAT` | Firm demographics by sector and municipality |
| `LBESK` | Employment by industry and municipality |
| `REGN` | Financial aggregates (revenue, profit) by sector |
| `GF` | General firm statistics by region |

#### Limitations

- **Aggregated only** — no per-entity data, only counts/sums per area × sector
- **Delayed** — published with months-to-years lag
- **Disclosure rules** — cells with few firms are suppressed to prevent identification
- **Useful for** — benchmarking, time series, regional economic profiles, cross-sector comparison

---

## Combining Realisations

| Need | Best Realisation | Why |
| --- | --- | --- |
| Per-company financial detail | CVR | Individual annual accounts |
| Employment by area | CVR or DST | CVR for per-entity, DST for aggregated time series |
| Sectoral benchmarking | DST | Aggregated averages and totals by NACE |
| Spatial financial heatmap | CVR + DAR | Geocode entities, aggregate by grid/area |
| Long-term economic trends | DST | Multi-year time series by sector and region |

## Classical Theme References

| Standard | Theme | Link |
| --- | --- | --- |
| INSPIRE | Production and Industrial Facilities | [[Classical Classifications/INSPIRE/production-and-industrial-facilities\\\|Production and Industrial Facilities]] |

## Temporal Model

Financial data is inherently **periodic** in addition to being bitemporal. Each `regnskab` record covers a specific accounting period (typically a fiscal year). Employment data (`Beskaeftigelse`) may have quarterly intervals. DST tables are versioned by publication year.

## Realised By Links

- [[Datasets by Collection/Grunddatamodellen/CentraleVirksomhedsregister/index.md|CentraleVirksomhedsregister]] (collection)
- [[Datasets by Collection/Grunddatamodellen/SkatteforvaltningensVirksomhedsregister/index.md|Skatteforvaltningens Virksomhedsregister]] (collection)

### Unmatched Realisations

- DanmarksStatistik
## Realised By Links

- [[Datasets by Collection/Grunddatamodellen/CentraleVirksomhedsregister/index.md|CentraleVirksomhedsregister]] (collection)
- [[Datasets by Collection/Grunddatamodellen/SkatteforvaltningensVirksomhedsregister/index.md|Skatteforvaltningens Virksomhedsregister]] (collection)

### Unmatched Realisations

- DanmarksStatistik
