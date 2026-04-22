---
title: Addresses
type: leaf
draft: true
sphere: Socio_Technical
subsphere: Socio_technical_governance
concept: Cognised spatial identifiers for locatable dwellings and premises
question: Where is a property located by its official address?
realisations: []
threads: []
tags: []
primary_collection:
primary_collection_path: /Datasets-by-Collection/Grunddatamodellen/DanmarksAdresser/
entities: []
key_attributes: []
services: {}
---

> **Cognised existence:** An address is a structured spatial identifier that connects a human activity — dwelling, business, service — to a point in geographic space. It is a universal join key in many geospatial data ecosystems.

**Question:** Where is a property located by its official address?

## What is an Address?

An address is not a coordinate. It is a **layered set of identifiers** (street name, house number, floor, door) that can collapse to one or more coordinate representations depending on purpose. In most data ecosystems, many registries reference addresses. Understanding the join chain from address entities to geometry is fundamental.

---

## Realisations

### 1. DanmarksAdresser (DAR)

The authoritative realisation. [[Datasets by Collection/Grunddatamodellen/DanmarksAdresser/index|DAR]] is the national address register.

#### Spatial Access Path

```
adresse (dwelling: floor + door)
  │  FK: adresseHarHusnummer (1..1)
  ▼
husnummer (building entrance level: "12A")
  │
  ├──► adgangspunkt (1..1)  → entrance point in terrain plane
  │       └─ position: GM_Point (ETRS89/UTM32N)
  │       └─ Use: "where is this building?" — geocoding, proximity analysis
  │
  └──► vejpunkt (1..1)      → road centreline point
          └─ position: GM_Point (ETRS89/UTM32N)
          └─ Use: network analysis, routing, snapping to road graph
```

**3 levels of joins, 2 alternative coordinate points:**

| Level | Entity | Role | Cardinality |
| --- | --- | --- | --- |
| 1 | **adresse** | Dwelling-level address (etage + dør) | — |
| 2 | **husnummer** | Building entrance (house number on a named road) | 1..1 per adresse |
| 3a | **adgangspunkt** | Entrance coordinate (terrain plane) | 1..1 per husnummer |
| 3b | **vejpunkt** | Road centreline coordinate (for network analysis) | 1..1 per husnummer |

Both `adgangspunkt` and `vejpunkt` are instances of the `Adressepunkt` superclass, stored in the **adressepunkter** table. Each carries:

- `position` — the GM_Point geometry
- `oprindelse` — provenance and quality metadata (source, accuracy class, technical standard)

#### Supporting Entities

| Entity | Role | Join |
| --- | --- | --- |
| **navngivenvej** | Street name | husnummer → navngivenVej (0..1) |
| **postnummer** | Postal code area | husnummer → postnummer (1..1) |
| **supplerendebynavn** | Supplementary city name | husnummer → supplerendebynavn (0..1) |

#### Key Attributes

| Attribute | On | Description |
| --- | --- | --- |
| `adressebetegnelse` | adresse | Full formatted address text |
| `husnummertekst` | husnummer | House number including letter suffix ("12A") |
| `etage` | adresse | Floor number |
| `doer` | adresse | Door identifier ("tv", "th", "mf", or number) |
| `postnr` | postnummer | 4-digit postal code |
| `postnrnavn` | postnummer | Postal district name |

#### Access

- **GraphQL**: `adresse` with joins to `husnummer`, `adgangspunkt`, `vejpunkt`
- **File Download**: Bulk exports of all DAR entities
- **DAWA**: Free API at `https://api.dataforsyningen.dk/adresser`

### 2. OpenStreetMap

Secondary realisation. OSM stores addresses as `addr:*` tags on nodes and building polygons.

| OSM Tag | DAR Equivalent |
| --- | --- |
| `addr:street` | navngivenvej.vejnavn |
| `addr:housenumber` | husnummer.husnummertekst |
| `addr:postcode` | postnummer.postnr |
| `addr:city` | postnummer.postnrnavn |

**Spatial access**: Direct — the node/polygon itself carries the geometry. No join chain needed. But OSM addresses lack the dwelling-level precision (no floor/door) and have no authoritative provenance.

---

## Classical Theme References

| Standard | Theme | Link |
| --- | --- | --- |
| ISO 19115 | Location | [[Classical Classifications/ISO 19115/location\\\|Location]] |
| INSPIRE | Addresses | [[Classical Classifications/INSPIRE/addresses\\\|Addresses]] |
| UN-GGIM | Addresses | [[Classical Classifications/UN-GGIM/addresses\\\|Addresses]] |

## Temporal Model

Bitemporal (from [[Datasets by Collection/Grunddatamodellen/Shared Temporal Superclass Contract|Shared Temporal Superclass Contract]]). Address lifecycle: created → active → retired. Historical queries on `virkningFra`/`virkningTil`.

## Realised By Links

- [[Datasets by Collection/Grunddatamodellen/DanmarksAdresser/index.md|DanmarksAdresser]] (collection)
- [[Datasets by Collection/Grunddatamodellen/BygningerOgBoliger/index.md|Bygninger og boliger]] (collection)

### Unmatched Realisations

- OpenStreetMap
## Realised By Links

- [[Datasets by Collection/Grunddatamodellen/DanmarksAdresser/index.md|DanmarksAdresser]] (collection)
- [[Datasets by Collection/Grunddatamodellen/BygningerOgBoliger/index.md|Bygninger og boliger]] (collection)

### Unmatched Realisations

- OpenStreetMap
