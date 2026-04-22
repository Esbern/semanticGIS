---
title: Cadastral Parcels
type: leaf
draft: true
sphere: Socio_Technical
subsphere: Socio_technical_governance
concept: Cognised legal boundaries of land ownership
question: What are the legal boundaries and ownership of land?
realisations: []
threads: []
tags: []
primary_collection:
primary_collection_path: /Datasets-by-Collection/Grunddatamodellen/Matrikel/
entities: []
key_attributes: []
services: {}
---

> **Cognised existence:** A cadastral parcel is the legal unit of land ownership. It exists because a surveyor measured it and a governance authority registered it. It has a boundary, an identifier, an area, and an owner.

**Question:** What are the legal boundaries and ownership of land?

## What is a Cadastral Parcel?

Each cadastral system defines unique parcel identifiers within one or more cadastral districts. The parcel boundary is the legal division of land, independent of what grows on it or what buildings sit on it.

---

## Realisations

### 1. Matrikel — Parcel Geometry and Identity

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

### 2. Ejerfortegnelsen — Ownership

[[Datasets by Collection/Grunddatamodellen/Ejerfortegnelsen/index|Ejerfortegnelsen]] links parcels to their owners (persons and organisations).

#### Spatial Access Path

```
ejerforhold (ownership record)
  │  FK: → jordstykke (via BFE-nummer or matrikelnummer + ejerlavskode)
  ▼
jordstykke.geometri (from Matrikel)
```

Ownership itself has no geometry — it inherits from the parcel. **2 levels of joins** to get from ownership to space.

---

## Classical Theme References

| Standard | Theme | Link |
| --- | --- | --- |
| ISO 19115 | Planning/Cadastre | [[Classical Classifications/ISO 19115/planningCadastre\\\|Planning/Cadastre]] |
| INSPIRE | Cadastral Parcels | [[Classical Classifications/INSPIRE/cadastral-parcels\\\|Cadastral Parcels]] |
| UN-GGIM | Land Parcels | [[Classical Classifications/UN-GGIM/land-parcels\\\|Land Parcels]] |

## Temporal Model

Bitemporal. Parcel boundaries change through subdivision, merger, and resurvey — all tracked with `virkningFra`/`virkningTil`.

## Realised By Links

- [[Datasets by Collection/Grunddatamodellen/Matrikel/index.md|Matrikel]] (collection)
- [[Datasets by Collection/Grunddatamodellen/Ejerfortegnelsen/index.md|Ejerfortegnelsen]] (collection)
- [[Datasets by Collection/Grunddatamodellen/BygningerOgBoliger/index.md|Bygninger og boliger]] (collection)
## Realised By Links

- [[Datasets by Collection/Grunddatamodellen/Matrikel/index.md|Matrikel]] (collection)
- [[Datasets by Collection/Grunddatamodellen/Ejerfortegnelsen/index.md|Ejerfortegnelsen]] (collection)
- [[Datasets by Collection/Grunddatamodellen/BygningerOgBoliger/index.md|Bygninger og boliger]] (collection)
