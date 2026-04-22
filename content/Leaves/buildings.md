---
title: Buildings
type: leaf
draft: true
sphere: Socio_Technical
subsphere: Socio_technical_infrastructure
concept: Cognised physical structures sheltering human activity
question: What buildings exist at a location and what are their characteristics?
realisations: []
threads: []
tags: []
primary_collection:
entities: []
key_attributes: []
services: {}
---

> **Cognised existence:** A building is a roofed, permanent physical structure that shelters human activity. It has use, age, size, and technical characteristics — and it occupies space, but its *geometry* may come from different sources than its *attributes*.

**Question:** What buildings exist at a location and what are their characteristics?

## What is a Building?

A building combines two kinds of data: **registry attributes** (what it is, when it was built, how it's used) and **geometric footprint** (its shape on the ground). These often come from different datasets. Understanding which to query depends on what you need.

---

## Realisations

### 1. BygningerOgBoliger (BBR) — Attributes

[[Datasets by Collection/Grunddatamodellen/BygningerOgBoliger/index|BBR]] is the national building and housing register. It carries detailed attributes but **no native geometry**. Geometry arrives via joins.

#### Spatial Access Path

```
bygning (building with attributes)
  │  FK: bygning → grund → jordstykke (via Matrikel)
  │  OR: bygning → adresse → husnummer → adgangspunkt (via DAR)
  ▼
Two routes to geometry:
  Route A: grund → jordstykke.geometri (parcel footprint — approximate)
  Route B: husnummer → adgangspunkt.position (point — geocoded)
  Route C: Join to GeoDanmark bygning via shared identifier (precise footprint)
```

#### Entity Hierarchy

| Entity | Role |
| --- | --- |
| **bygning** | The building: use code, construction year, area, floors, heating |
| **enhed** | Dwelling or commercial unit within a building |
| **etage** | Floor level |
| **opgang** | Staircase / entrance |
| **grund** | Ground parcel the building sits on |
| **tekniskanlæg** | Technical installations (heating plants, solar panels) |

#### Key Attributes

| Attribute | Description |
| --- | --- |
| `byg_anvendelse` | Building use code (residential, commercial, industrial, public) |
| `byg_opfoerelsesaar` | Year of construction |
| `byg_areal` | Area in m² (footprint, gross, net variants) |
| `byg_antal_etager` | Number of floors |
| `byg_varmeinstallation` | Heating type (district heating, gas, electric) |

### 2. GeoDanmark — Geometry

[[Datasets by Collection/Grunddatamodellen/GeoDanmark/index|GeoDanmark]] provides the authoritative **building footprint polygons** as part of the national topographic dataset. These are photogrammetrically measured outlines.

#### Spatial Access Path

```
GeoDanmark.bygning → polygon geometry (direct, no joins needed)
```

**Join to BBR**: Match GeoDanmark footprints to BBR buildings via shared spatial location or building identifier to combine attributes + geometry.

### 3. OpenStreetMap

OSM contains building footprints with basic attributes.

| OSM Tag | BBR Equivalent |
| --- | --- |
| `building=yes/residential/commercial/...` | byg_anvendelse |
| `building:levels` | byg_antal_etager |
| `start_date` | byg_opfoerelsesaar |

**Spatial access**: Direct polygon geometry on the `building` way. Less detailed attributes than BBR but openly available.

---

## Geometry Representations

A building query must declare which geometric encoding is used. These representations are not interchangeable.

| Rep ID | Source Dataset | Geometry Type | Native CRS | Field Path | Suitable For | Not Suitable For |
|---|---|---|---|---|---|---|
| `buildings_bbr_centroid` | BBR (`BBR_Bygning`) | Point | EPSG:25832 | `byg404Koordinat.wkt` | Density mapping, point-in-polygon queries, proximity counts | Area statistics, footprint overlap, spatial join to polygon layers |
| `buildings_geodanmark_footprint` | GeoDanmark | Polygon | EPSG:25832 | `geometri` | Area calculation, footprint overlap, visual representation, join to BBR attributes | Network routing |
| `buildings_dar_address_point` | DAR (`husnummer.adgangspunkt`) | Point | EPSG:25832 | `adgangspunkt.position` | Geocoding, address-level mapping | Building-specific attributes (requires join back to BBR via husnummer) |
| `buildings_osm_footprint` | OpenStreetMap | Polygon | WGS84 | `way` geometry | General mapping, open-data contexts | Official Danish register accuracy, bitemporal analysis |

**Default assumption is wrong:** BBR centroid is the easiest geometry to extract but is not suitable for area statistics, shadow/solar analysis, or any operation requiring the building outline. If the question involves shape, size, or spatial overlap — select `buildings_geodanmark_footprint` and join to BBR for attributes.

---

## Classical Theme References

| Standard | Theme | Link |
| --- | --- | --- |
| ISO 19115 | Structure | [[Classical Classifications/ISO 19115/structure\\\|Structure]] |
| INSPIRE | Buildings | [[Classical Classifications/INSPIRE/buildings\\\|Buildings]] |
| UN-GGIM | Buildings and Settlements | [[Classical Classifications/UN-GGIM/buildings-and-settlements\\\|Buildings and Settlements]] |

## Temporal Model

Bitemporal in BBR. GeoDanmark footprints are updated periodically (annual campaign). Historical building states via `virkningFra`/`virkningTil` in BBR.

## Realised By Links

- [[Datasets by Collection/Grunddatamodellen/BygningerOgBoliger/index.md|Bygninger og boliger]] (collection)
- [[Datasets by Collection/Grunddatamodellen/GeoDanmark/index.md|GeoDanmark]] (collection)

### Unmatched Realisations

- OpenStreetMap
## Realised By Links

- [[Datasets by Collection/Grunddatamodellen/BygningerOgBoliger/index.md|Bygninger og boliger]] (collection)
- [[Datasets by Collection/Grunddatamodellen/GeoDanmark/index.md|GeoDanmark]] (collection)

### Unmatched Realisations

- OpenStreetMap
