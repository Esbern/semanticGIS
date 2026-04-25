---
title: "Danmarks Statistik — NACE Aggregates Realisation of Economic Activities"
type: realisation
draft: false
leaf: Economic Activities
dataset: Danmarks Statistik
tags:
  - realisation/danmarks_statistik
  - leaf/economic-activities
---

**Leaf:** [[Leaves/economic-activities|Economic Activities]]
**Dataset:** Danmarks Statistik — NACE Aggregates

DST publishes sectoral statistics (employment, revenue, firm counts) coded by NACE sector and geographic area via [Statistikbanken](https://www.statistikbanken.dk/).

#### Spatial Access Path

```
Statistical table (NACE sector × municipality/region)
  │  FK: municipality/region code
  ▼
DAGI administrative polygon (via kommune/region geometry)
```

**1 join** to geometry — aggregate figures are keyed to administrative areas realised by [[Leaves/administrative-units|Administrative Units]].

#### Limitations

- **Aggregated only** — no per-entity data, only counts/sums per area × sector
- **Delayed** — statistics published with months-to-years lag
- **Useful for** — sectoral comparison, time series, regional economic profiles

## Temporal Model

Industry classification is **bitemporal** (inherited from [[Datasets by Collection/Grunddatamodellen/Shared Temporal Superclass Contract|Shared Temporal Superclass Contract]]). A business can change its primary industry over time. Historical queries require `virkningFra`/`virkningTil` filtering.
