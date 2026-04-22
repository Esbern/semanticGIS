---
title: Economic Activities
type: leaf
draft: true
sphere: Socio_Technical
subsphere: Socio_technical_socioeconomic
concept: Cognised classification of what economic function an enterprise performs
question: What economic activity does a business perform?
realisations: []
threads:
  - economic-activities-to-biosphere-ecosystems
  - economic-activities-to-perception-thematics
tags:
  - biosphere_ecosystems
  - socio_technical_perception_thematics
flow_mode: ant
temporal_mmu: episodic
primary_collection:
primary_collection_path: /Datasets-by-Collection/Grunddatamodellen/CentraleVirksomhedsregister/
entities: []
key_attributes: []
services:
  graphql: >-
    /assets/source-manifests/datafordeler/datafordeler.graphql.services.manifest.v1.json
  source_manifest: /assets/source-manifests/datafordeler/cvr.source.manifest.v1.json
  semantic_map: >-
    /assets/source-manifests/datafordeler/cvr.semantic.entity-attribute-map.v1.json
---

> **Cognised existence:** An economic activity is the classified function an enterprise performs — what it *does* in the economy. This concept exists independent of any particular register: a restaurant is a restaurant whether you read it from an industry code, an OSM amenity tag, or a statistical table.

**Question:** What economic activity does a business perform?

## What is an Economic Activity?

An economic activity is not a business (that's a legal entity). It is the *type of work* performed. A single enterprise may have multiple activities (primary + secondary). The classification enables sectoral analysis, economic diversity mapping, and filtering businesses by function.

For the legal business entity behind the activity, use [[Leaves/firms|Firms]].

Different data sources encode this concept using incompatible taxonomies — business registries use industry code systems, OSM uses tag families, and statistics systems use aggregated sector classes. A leaf-level understanding lets an agent translate between them.

---

## Realisations

### 1. CVR (CentraleVirksomhedsregister) — DB25 Industry Code

The authoritative per-entity realisation. [[Datasets by Collection/Grunddatamodellen/CentraleVirksomhedsregister/index|CVR]] classifies every registered business via the `Branche` entity.

#### Spatial Access Path

```
Branche (activity code)
  │  FK: CVREnhedsId
  ▼
Virksomhed / Produktionsenhed
  │  FK: → Adressering → DAR join chain
  │       adresse → husnummer → adgangspunkt.position
  ▼
adgangspunkt.position (point geometry via DAR)
```

**No native geometry.** To map activities spatially, join through the business entity to its address, then through the [[Leaves/addresses|Addresses]] join chain to coordinates.

#### Key Entities

| Entity | Role |
| --- | --- |
| **Branche** | Carries the industry code and text. A business may have multiple (primary + secondary) |
| **Virksomhed** | Legal business entity that branches attach to |
| **Produktionsenhed** | Operational establishment — may have its own branch set |

#### Key Attributes

| Attribute | Description | Notes |
| --- | --- | --- |
| `branchekode` | DB25 industry code | Compact form without dots: `561110` not `56.11.10`. Since Jan 2025, CVR uses DB25 (NACE Rev 2.1), replacing DB07 |
| `branchetekst` | Human-readable description | Danish language |
| `hovedbranche` | Primary activity flag | `true` = main activity of the business |

#### DB07 → DB25 Transition

As of January 2025, CVR stores **DB25** codes (Danish implementation of NACE Rev 2.1). Older records may still carry DB07 codes. CVR stores codes **without dots** — strip dots when matching against external references using dotted format (e.g., `56.11.10`).

- [[Datasets by Collection/Grunddatamodellen/CentraleVirksomhedsregister/codebook-and-normalization|CVR Codebook and Normalization]]
- DST conversion table: [DB07-DB25 concordance](https://www.dst.dk/da/Statistik/dokumentation/nomenklaturer/db)

#### Access

- **GraphQL**: [[Data Portals/Datafordeleren/graphql|Datafordeleren GraphQL]] — query `Branche` with filters on `branchekode`
- **File Download**: Bulk `Branche` entity export, join locally to `Virksomhed`
- **Semantic map**: [[Datasets by Collection/Grunddatamodellen/CentraleVirksomhedsregister/semantic-organisation|CVR Semantic Organisation]]

### 2. OpenStreetMap — Tag Families

OSM encodes economic activity through multiple tag families directly on map features.

#### Spatial Access Path

```
OSM node/way with activity tags → direct point/polygon geometry
```

**No joins needed** — the tagged feature carries its own geometry.

#### Activity Tag Mapping (OSM → DB25 Approximate Equivalents)

| OSM Tag Family | Activity Domain | DB25 Range |
| --- | --- | --- |
| `shop=*` | Retail trade | `47xxxx` |
| `amenity=restaurant\|cafe` | Food service | `5611xx` |
| `amenity=bar\|pub` | Drinking establishments | `5630xx` |
| `craft=*` | Skilled trades | `43xxxx` (construction trades) |
| `office=*` | Professional services | `69–74xxxx` |
| `industrial=*` | Manufacturing/industry | `10–33xxxx` |
| `tourism=hotel\|hostel` | Accommodation | `55xxxx` |
| `amenity=school\|university` | Education | `85xxxx` |
| `amenity=hospital\|clinic` | Healthcare | `86xxxx` |

OSM classifications are **not hierarchical** — they are flat tags. Mapping to NACE/DB25 is approximate and context-dependent.

### 3. Danmarks Statistik — NACE Aggregates

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

---

## Cross-Domain Relevance (Threads)

- **Biosphere**: Industry codes signal environmental impact. Agriculture (`01xxxx`), fishing (`03xxxx`), and extraction industries directly affect ecosystems.
- **Socio-Technical Perception & Thematics**: Industry type correlates with thematic human partitioning of space. Retail clusters, industrial zones, and agricultural activities shape mapped interpretation layers.

## Classical Theme References

| Standard | Theme | Link |
| --- | --- | --- |
| INSPIRE | Production and Industrial Facilities | [[Classical Classifications/INSPIRE/production-and-industrial-facilities\\\|Production and Industrial Facilities]] |

## Temporal Model

Industry classification is **bitemporal** (inherited from [[Datasets by Collection/Grunddatamodellen/Shared Temporal Superclass Contract|Shared Temporal Superclass Contract]]). A business can change its primary industry over time. Historical queries require `virkningFra`/`virkningTil` filtering.

## Realised By Links

- [[Datasets by Collection/Grunddatamodellen/CentraleVirksomhedsregister/index.md|CentraleVirksomhedsregister]] (collection)
- [[Datasets by Collection/Grunddatamodellen/SkatteforvaltningensVirksomhedsregister/index.md|Skatteforvaltningens Virksomhedsregister]] (collection)

### Unmatched Realisations

- OpenStreetMap
- DanmarksStatistik
## Realised By Links

- [[Datasets by Collection/Grunddatamodellen/CentraleVirksomhedsregister/index.md|CentraleVirksomhedsregister]] (collection)
- [[Datasets by Collection/Grunddatamodellen/SkatteforvaltningensVirksomhedsregister/index.md|Skatteforvaltningens Virksomhedsregister]] (collection)

### Unmatched Realisations

- OpenStreetMap
- DanmarksStatistik
