---
title: "BBR (BygningerOgBoliger) — By Building Use Code Realisation of Services and Amenities"
type: realisation
draft: false
leaf: Services and Amenities
dataset: BBR
tags:
  - realisation/bbr_bygningerogboliger
  - leaf/services
---

**Leaf:** [[Leaves/services|Services and Amenities]]
**Dataset:** BBR (BygningerOgBoliger) — By Building Use Code

When the building *is* the service, BBR's `byg_anvendelse` code can be filtered to identify service facilities.

#### Spatial Access Path

```
bygning (building with use code)
  │  Filter: byg_anvendelse ∈ [service-relevant codes]
  │  → geometry via GeoDanmark footprint or DAR adgangspunkt
  ▼
(see Buildings leaf for full join chain)
```
