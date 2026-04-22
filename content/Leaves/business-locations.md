---
title: Business Locations
type: leaf
draft: true
sphere: Socio_Technical
subsphere: Socio_technical_infrastructure
concept: Cognised physical operating locations where enterprises conduct activity
question: Where does a business physically operate?
realisations: []
threads:
  - business-locations-to-topography
  - business-locations-to-perception-thematics
tags:
  - toposphere_topography_bathymetry
  - socio_technical_perception_thematics
flow_mode: ant
temporal_mmu: episodic
primary_collection:
primary_collection_path: /Datasets-by-Collection/Grunddatamodellen/CentraleVirksomhedsregister/
entities: []
key_attributes: []
services: {}
  graphql: >-
    /assets/source-manifests/datafordeler/datafordeler.graphql.services.manifest.v1.json
  source_manifest: /assets/source-manifests/datafordeler/cvr.source.manifest.v1.json
  semantic_map: >-
    /assets/source-manifests/datafordeler/cvr.semantic.entity-attribute-map.v1.json
---

> **Cognised existence:** A business location is the physical place where an enterprise conducts its activity — a shop, a factory floor, an office. It is not the business itself (that's legal registration), not the building (that's [[Leaves/buildings|Buildings]]), and not the service provided (that's [[Leaves/services|Services]]). It is the *operational presence* of economic activity at a point in space.

**Question:** Where does a business physically operate?

## What is a Business Location?

A business location answers "where is this enterprise, physically?" This is deceptively complex because a single company can have one registered office but dozens of production sites. Many national business registries separate these two concepts — and choosing the wrong one produces misleading maps.

---

## Critical Distinction: Firm Address vs Production Unit

| Address Type | Entity | Meaning | Use When |
| --- | --- | --- | --- |
| **Firm address** | `Virksomhed` → `Adressering` | Legal/administrative presence (registered office) | "Where is the company registered?" |
| **Production unit address** | `Produktionsenhed` → `Adressering` | Physical operational location | "Where are the restaurants/factories/shops?" |

**Always decide which address type matches your question before geocoding.** For "where are the restaurants?", you want production unit addresses. For "where is the company registered?", you want firm addresses.

---

## Realisations

### 1. CVR (CentraleVirksomhedsregister) — Registered Addresses

The authoritative realisation. [[Datasets by Collection/Grunddatamodellen/CentraleVirksomhedsregister/index|CVR]] records addresses for both firms and production units.

#### Spatial Access Path

```
Produktionsenhed (or Virksomhed)
  │  FK: → Adressering (text-based address components)
  │         kommunekode + vejnavn + husnummer + postnummer
  │
  │  Geocode via DAR match:
  │  FK: adresse → husnummer → adgangspunkt.position
  ▼
adgangspunkt.position (point geometry via DAR)
```

**3+ levels of joins** to geometry. CVR addresses are **text-based** — they store `kommunekode`, `vejnavn`, `husnummer`, `postnummer` as separate fields. Coordinates require joining to [[Leaves/addresses|Addresses (DAR)]]:

1. Normalize CVR address components (strip whitespace, standardise case)
2. Match to DAR using `kommunekode` + `vejnavn` + `husnummer`
3. DAR resolves to `husnummer` → `adgangspunkt.position` (entrance point) or `vejpunkt.position` (road centreline point)

| Level | Entity | Role | Cardinality |
| --- | --- | --- | --- |
| 1 | **Produktionsenhed** | Operational location record | — |
| 2 | **Adressering** | Text address fields | 1..1 per P-enhed |
| 3 | **DAR husnummer** | Matched via address components | 1..1 (when matched) |
| 4a | **adgangspunkt** | Entrance coordinate | 1..1 per husnummer |
| 4b | **vejpunkt** | Road centreline coordinate | 1..1 per husnummer |

#### Key Attributes

| Attribute | Description | Notes |
| --- | --- | --- |
| `kommunekode` | Municipality code | 4-digit, zero-padded (e.g., `0101` for Copenhagen) |
| `vejnavn` | Street name | Danish characters |
| `husnummer` | House number | May include letter suffix (e.g., `12A`) |
| `postnummer` | Postal code | 4-digit |
| `bynavn` | City/town name | May differ from municipality name |

#### Access

- **GraphQL**: [[Data Portals/Datafordeleren/graphql|Datafordeleren GraphQL]] — query `Produktionsenhed` or `Virksomhed` with address subfields
- **File Download**: Bulk `Produktionsenhed` + `Adressering` exports, join locally
- **Semantic map**: [[Datasets by Collection/Grunddatamodellen/CentraleVirksomhedsregister/semantic-organisation|CVR Semantic Organisation]]

### 2. OpenStreetMap — Commercial POIs

OSM records business locations as tagged features with direct geometry.

#### Spatial Access Path

```
OSM node/way with commercial tags → direct point/polygon geometry
```

**No joins needed** — the mapped feature IS the business location and carries its own geometry.

#### Relevant Tags

| OSM Tag | Meaning |
| --- | --- |
| `shop=*` | Retail premises |
| `office=*` | Office locations |
| `craft=*` | Workshop/trade premises |
| `industrial=*` | Industrial sites |
| `amenity=restaurant\|cafe\|bar` | Food/drink premises |
| `building=commercial\|industrial\|retail` | Building-level classification |

OSM coverage is volunteer-driven — complete in urban areas, patchy in rural zones. No authoritative provenance.

### 3. BBR (BygningerOgBoliger) — Buildings by Use Code

When the business location *is* the building, BBR's `byg_anvendelse` (building use code) identifies commercial/industrial premises.

#### Spatial Access Path

```
bygning (building with use code filter)
  │  FK: → GeoDanmark footprint polygon (via building ID)
  │  or: → grund (plot) → DAR adgangspunkt
  ▼
GeoDanmark building footprint polygon / DAR adgangspunkt
```

**1–2 joins** to geometry. See [[Leaves/buildings|Buildings]] for the full BBR spatial access path.

#### Relevant Use Codes

| `byg_anvendelse` range | Meaning |
| --- | --- |
| `300–399` | Commercial buildings (offices, shops) |
| `400–499` | Industrial buildings (factories, warehouses) |
| `500–599` | Cultural and institutional buildings |
| `210–219` | Production-related agricultural buildings |

---

## Combining Realisations

| Need | Best Realisation | Why |
| --- | --- | --- |
| Authoritative business registry with attributes | CVR | Complete, official, includes P-enheder |
| Quick geocoded point map | OSM | Direct geometry, no joins |
| Building-level analysis (area, age, type) | BBR | Physical structure attributes |
| Complete picture | CVR + DAR + BBR | Business attributes + coordinates + building characteristics |

## Cross-Domain Relevance (Threads)

- **Toposphere**: Business locations relate to terrain and elevation context (e.g., flood-exposure analysis for operational sites).
- **Socio-Technical Perception & Thematics**: Business density and spatial distribution directly shape thematic urban interpretation layers — retail corridors, industrial zones, office districts.

## Classical Theme References

| Standard | Theme | Link |
| --- | --- | --- |
| INSPIRE | Production and Industrial Facilities | [[Classical Classifications/INSPIRE/production-and-industrial-facilities\\\|Production and Industrial Facilities]] |
| INSPIRE | Utility and Governmental Services | [[Classical Classifications/INSPIRE/utility-and-governmental-services\\\|Utility and Governmental Services]] |

## Temporal Model

Business locations are **bitemporal**. A business can move. Historical spatial analysis requires `virkningFra`/`virkningTil` filtering to reconstruct location at a given point in time. Both `Adressering` and `Produktionsenhed` carry their own temporal fields.

## Realised By Links

- [[Datasets by Collection/Grunddatamodellen/CentraleVirksomhedsregister/index.md|CentraleVirksomhedsregister]] (collection)
- [[Datasets by Collection/Grunddatamodellen/BygningerOgBoliger/index.md|Bygninger og boliger]] (collection)
- [[Datasets by Collection/Grunddatamodellen/SkatteforvaltningensVirksomhedsregister/index.md|Skatteforvaltningens Virksomhedsregister]] (collection)

### Unmatched Realisations

- OpenStreetMap
## Realised By Links

- [[Datasets by Collection/Grunddatamodellen/CentraleVirksomhedsregister/index.md|CentraleVirksomhedsregister]] (collection)
- [[Datasets by Collection/Grunddatamodellen/BygningerOgBoliger/index.md|Bygninger og boliger]] (collection)
- [[Datasets by Collection/Grunddatamodellen/SkatteforvaltningensVirksomhedsregister/index.md|Skatteforvaltningens Virksomhedsregister]] (collection)

### Unmatched Realisations

- OpenStreetMap
