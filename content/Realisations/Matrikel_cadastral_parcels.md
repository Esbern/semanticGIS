---
title: "Matrikel — Parcel Geometry and Identity Realisation of Cadastral Parcels"
type: realisation
draft: false
leaf: Cadastral Parcels
dataset: Matrikel
tags:
  - realisation/matrikel
  - leaf/cadastral-parcels
---

**Leaf:** [[Leaves/cadastral-parcels|Cadastral Parcels]]
**Dataset:** Matrikel — Parcel Geometry and Identity

[[Datasets by Collection/Grunddatamodellen/Matrikel/index|Matrikel]] is the authoritative cadastral register.

#### Spatial Access Path

```
jordstykke → geometri (polygon — direct, no joins needed)
```

Cadastral parcels carry their own polygon geometry directly. The `jordstykke` entity IS the parcel with its boundary.

#### Entities

| Entity | Role |
| --- | --- |
| **jordstykke** | The parcel: boundary polygon, area, matrikelnummer |
| **ejerlav** | Cadastral district grouping parcels |
| **skelforretning** | Boundary survey event (provenance of the boundary) |

#### Key Attributes

| Attribute | Description |
| --- | --- |
| `matrikelnummer` | Parcel identifier within the ejerlav |
| `ejerlavskode` | Cadastral district code |
| `registreretareal` | Registered area (m²) |
| `geometri` | Parcel boundary polygon |

## Temporal Model

Bitemporal. Parcel boundaries change through subdivision, merger, and resurvey — all tracked with `virkningFra`/`virkningTil`.
