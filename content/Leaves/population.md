---
title: Population
type: leaf
draft: true
sphere: Socio_Technical
subsphere: Socio_technical_socioeconomic
concept: Cognised spatial distribution of human inhabitants
question: How is the population distributed and what are its characteristics?
realisations: []
threads: []
tags: []
primary_collection:
entities: []
key_attributes: []
services: {}
---

> **Cognised existence:** Population is the spatial distribution of people — where they live, how many, their age, gender, household composition. It is the denominator for nearly every per-capita indicator.

**Question:** How is the population distributed and what are its characteristics?

---

## Realisations

### 1. Person Register (CPR)

[[Datasets by Collection/Grunddatamodellen/Person/index|Person]] records every individual with legal residence in Denmark.

#### Spatial Access Path

```
person (individual record)
  │  FK: person → adresse (registered address)
  │       └─ see Addresses leaf for the address → geometry join chain
  ▼
adresse → husnummer → adgangspunkt.position
```

**3+ levels of joins** to get from a person to coordinates:
person → adresse → husnummer → adgangspunkt

This realisation is **restricted** — individual-level data requires authorisation. Aggregated to administrative units, it becomes freely available.

#### Key Attributes

| Attribute | Description |
| --- | --- |
| `foedselsdato` | Date of birth → age derivation |
| `koen` | Gender |
| `civilstand` | Marital status |
| `kommunekode` | Municipality of residence → [[Leaves/administrative-units\\\|Administrative Units]] |

### 2. Danmarks Statistik (DST)

Pre-aggregated population statistics at municipal, parish, and 100m grid levels.

#### Spatial Access Path

```
DST population table (aggregated counts)
  │  Key: kommunekode, sognekode, or grid cell ID
  │  Join to: DAGI (for kommune/sogn polygon) or statistical grid
  ▼
DAGI.kommune.geometri  OR  statistisk_gridcelle.geometri
```

**1 level of join** — aggregated statistics join directly to administrative or grid geometries.

---

## Access Restrictions

| Realisation | Access level | What you get |
| --- | --- | --- |
| CPR (individual) | Restricted (authorisation required) | Individual records with address FK |
| DST (aggregated) | Open | Counts by municipality/parish/grid |
| DST (microdata) | Research authorisation | Anonymised individual records |

## Classical Theme References

| Standard | Theme | Link |
| --- | --- | --- |
| ISO 19115 | Society | [[Classical Classifications/ISO 19115/society\\\|Society]] |
| INSPIRE | Population Distribution | [[Classical Classifications/INSPIRE/population-distribution\\\|Population Distribution]] |
| UN-GGIM | Population Distribution | [[Classical Classifications/UN-GGIM/population-distribution\\\|Population Distribution]] |

## Realised By Links

- [[Datasets by Collection/Grunddatamodellen/Person/index.md|Person]] (collection)

### Unmatched Realisations

- DanmarksStatistik
## Realised By Links

- [[Datasets by Collection/Grunddatamodellen/Person/index.md|Person]] (collection)

### Unmatched Realisations

- DanmarksStatistik
