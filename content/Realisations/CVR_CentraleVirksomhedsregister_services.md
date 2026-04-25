---
title: "CVR (CentraleVirksomhedsregister) — By Industry Code Realisation of Services and Amenities"
type: realisation
draft: false
leaf: Services and Amenities
dataset: CVR
tags:
  - realisation/cvr_centralevirksomhedsregister
  - leaf/services
---

**Leaf:** [[Leaves/services|Services and Amenities]]
**Dataset:** CVR (CentraleVirksomhedsregister) — By Industry Code

[[Datasets by Collection/Grunddatamodellen/CentraleVirksomhedsregister/index|CVR]] realises services and amenities through **branchekode** filtering, usually anchored on the operational unit (`Produktionsenhed`) rather than only the legal firm.

#### Spatial Access Path

```
Produktionsenhed (preferred) / Virksomhed
  │  Filter: branchekode ∈ [service-relevant codes]
  │  FK: → adresse → husnummer → adgangspunkt.position
  ▼
adgangspunkt.position (point geometry via DAR)
```

**3 levels of joins** to geometry (same as [[Leaves/addresses|Addresses]]):
entity → adresse → husnummer → adgangspunkt

#### Service Type Mapping (DB25 → Service Category)

| DB25 Range | Service Category | Examples |
| --- | --- | --- |
| `8610*` | Hospital services | Hospitals, psychiatric hospitals |
| `8621*`–`8690*` | Healthcare | GP clinics, dentists, physiotherapy |
| `8510*`–`8560*` | Education | Primary schools, secondary, universities |
| `5611*` | Restaurants | Restaurants, cafés |
| `5630*` | Bars and pubs | Bars, nightclubs |
| `4711*`–`4799*` | Retail | Supermarkets, shops |
| `5510*`–`5590*` | Accommodation | Hotels, hostels, camping |

Use `hovedbranche = true` to get primary activity. For regional geography and service availability studies, start from `Produktionsenhed` whenever possible. See [[Leaves/economic-activities|Economic Activities]] for the full codebook.
