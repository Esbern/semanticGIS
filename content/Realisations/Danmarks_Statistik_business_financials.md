---
title: "Danmarks Statistik — Aggregated Statistics Realisation of Economics and Employment"
type: realisation
draft: false
leaf: Economics and Employment
dataset: Danmarks Statistik
tags:
  - realisation/danmarks_statistik
  - leaf/business-financials
---

**Leaf:** [[Leaves/business-financials|Economics and Employment]]
**Dataset:** Danmarks Statistik — Aggregated Statistics

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

## Temporal Model

Financial data is inherently **periodic** in addition to being bitemporal. Each `regnskab` record covers a specific accounting period (typically a fiscal year). Employment data (`Beskaeftigelse`) may have quarterly intervals. DST tables are versioned by publication year.
