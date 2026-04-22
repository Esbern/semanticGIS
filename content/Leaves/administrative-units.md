---
title: Administrative Units
type: leaf
draft: true
sphere: Socio_Technical
subsphere: Socio_technical_governance
concept: Cognised territorial divisions for governance and statistical aggregation
question: Which administrative area does a location belong to?
realisations: []
threads: []
tags: []
primary_collection:
primary_collection_path: /Datasets-by-Collection/Grunddatamodellen/DAGI/
entities: []
key_attributes: []
services: {}
---

> **Cognised existence:** Administrative units are territorial divisions defined by governance acts. They exist because a political authority declared them. Their boundaries determine jurisdiction, statistical aggregation, electoral geography, and service responsibility.

**Question:** Which administrative area does a location belong to?

## What is an Administrative Unit?

An administrative unit is an area with a name, a code, and a polygon boundary that groups other spatial objects (addresses, parcels, people, businesses) for governance purposes. Most countries have nested hierarchies (for example region → municipality → local district), often with parallel divisions for judicial, police, health, or electoral purposes.

---

## Realisations

### 1. DAGI (Danmarks Administrative Geografiske Inddeling)

[[Datasets by Collection/Grunddatamodellen/DAGI/index|DAGI]] is the authoritative realisation.

#### Spatial Access Path

```
All DAGI entities carry direct polygon geometry — no joins needed.
  kommune.geometri  → municipality boundary (polygon)
  region.geometri   → region boundary (polygon)
  sogn.geometri     → parish boundary (polygon)
  ...etc.
```

#### Entity Hierarchy

| Entity | Count | Code | Use |
| --- | --- | --- | --- |
| **region** | 5 | `regionskode` | Healthcare, spatial planning |
| **kommune** | 98 | `kommunekode` | Primary governance unit, most statistics |
| **sogn** | ~2,200 | `sognekode` | Church parishes, historical aggregation |
| **retskreds** | 24 | `retskredskode` | Judicial districts |
| **politikreds** | 12 | `politikredskode` | Police districts |
| **opstillingskreds** | 92 | — | Electoral constituencies |
| **afstemningsomraade** | ~1,400 | — | Polling districts (finest electoral unit) |

#### Key Attributes

| Attribute | Description |
| --- | --- |
| `kommunekode` | 4-digit municipality code (the most commonly used key in Danish data) |
| `regionskode` | 4-digit region code |
| `navn` | Name of the administrative unit |
| `geometri` | Polygon boundary |

**`kommunekode` is the universal aggregation key** — most Danish registers store it as a foreign key. Point-in-polygon queries against DAGI are the standard way to assign data to municipalities.

### 2. OpenStreetMap

OSM carries `admin_level` boundaries for Denmark, with `admin_level=4` for regions and `admin_level=7` for municipalities.

**Spatial access**: Direct polygon geometry on `boundary=administrative` relations.

---

## Classical Theme References

| Standard | Theme | Link |
| --- | --- | --- |
| ISO 19115 | Boundaries | [[Classical Classifications/ISO 19115/boundaries\\\|Boundaries]] |
| INSPIRE | Administrative Units | [[Classical Classifications/INSPIRE/administrative-units\\\|Administrative Units]] |

## Temporal Model

Bitemporal. Municipal mergers (last major reform: 2007) are tracked historically.

## Realised By Links

- [[Datasets by Collection/Grunddatamodellen/DAGI/index.md|DAGI]] (collection)
- [[Datasets by Collection/Grunddatamodellen/GeoDanmark/index.md|GeoDanmark]] (collection)

### Unmatched Realisations

- OpenStreetMap
## Realised By Links

- [[Datasets by Collection/Grunddatamodellen/DAGI/index.md|DAGI]] (collection)
- [[Datasets by Collection/Grunddatamodellen/GeoDanmark/index.md|GeoDanmark]] (collection)

### Unmatched Realisations

- OpenStreetMap
