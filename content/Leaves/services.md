---
title: Services and Amenities
type: leaf
draft: true
sphere: Socio_Technical
subsphere: Socio_technical_services
concept: >-
  Cognised facilities, institutions, and amenities providing functions to the
  public
question: What services or amenities are available at or near a location?
realisations: []
threads: []
tags:
  - socio_technical_services
primary_collection:
primary_collection_path: /Datasets-by-Collection/Grunddatamodellen/CentraleVirksomhedsregister/
entities: []
key_attributes: []
services: {}
---

> **Cognised existence:** A service or amenity is a facility, institution, or establishment that provides a function to the public — healthcare, education, dining, retail, emergency response, recreation, or everyday convenience. The same concept is captured differently across datasets: as a business with an industry code, as a map point with an amenity tag, or as a building with a use code.

**Question:** What services or amenities are available at or near a location?

## What is a Service or Amenity?

A service or amenity is not a building (that's [[Leaves/buildings|Buildings]]). It is not the legal business entity behind it (that's [[Leaves/firms|Firms]]). It is the *function provided at a place*. A hospital provides healthcare. A school provides education. A restaurant provides dining. A playground provides recreation. The same physical building may house multiple services, and the same service type may appear across very different data sources.

---

## Realisations

### 1. CVR (CentraleVirksomhedsregister) — By Industry Code

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

### 2. OpenStreetMap — By Amenity Tag

OSM tags services directly on map features using the `amenity`, `shop`, `tourism`, and `healthcare` tag families.

#### Spatial Access Path

```
OSM node/way with amenity=* tag → direct point/polygon geometry
```

**No joins needed** — the tagged feature IS the service and carries its own geometry.

#### Service Type Mapping (OSM → Service Category)

| OSM Tag | Service Category | Examples |
| --- | --- | --- |
| `amenity=hospital` | Hospital services | |
| `amenity=clinic`, `amenity=doctors` | Healthcare | GP clinics |
| `amenity=dentist` | Healthcare | |
| `amenity=school` | Education | Primary/secondary |
| `amenity=university` | Education | Higher education |
| `amenity=restaurant` | Restaurants | |
| `amenity=cafe` | Dining | |
| `amenity=bar`, `amenity=pub` | Bars and pubs | |
| `shop=supermarket` | Retail | |
| `tourism=hotel` | Accommodation | |
| `amenity=pharmacy` | Healthcare | |
| `amenity=fire_station` | Emergency | |
| `amenity=police` | Public safety | |

### 3. BBR (BygningerOgBoliger) — By Building Use Code

When the building *is* the service, BBR's `byg_anvendelse` code can be filtered to identify service facilities.

#### Spatial Access Path

```
bygning (building with use code)
  │  Filter: byg_anvendelse ∈ [service-relevant codes]
  │  → geometry via GeoDanmark footprint or DAR adgangspunkt
  ▼
(see Buildings leaf for full join chain)
```

---

## Combining Realisations

The power of multi-source realisations: CVR gives you **business attributes** (opening year, employee count, revenue). OSM gives you **direct coordinates and opening hours**. BBR gives you **physical building characteristics**. An agent assembling a complete picture of "healthcare services in Copenhagen" can draw from all three.

| Need | Best Realisation | Why |
| --- | --- | --- |
| Comprehensive business list | CVR | Most complete, authoritative |
| Quick geocoded point map | OSM | Direct geometry, no joins |
| Building characteristics of service facilities | BBR | Physical attributes (area, age, heating) |
| Combined analysis | CVR + OSM + BBR | Full picture via address-based join |

## Classical Theme References

| Standard | Theme | Link |
| --- | --- | --- |
| INSPIRE | Utility and Governmental Services | [[Classical Classifications/INSPIRE/utility-and-governmental-services\\\|Utility and Governmental Services]] |

## Realised By Links

- [[Datasets by Collection/Grunddatamodellen/CentraleVirksomhedsregister/index.md|CentraleVirksomhedsregister]] (collection)
- [[Datasets by Collection/Grunddatamodellen/BygningerOgBoliger/index.md|Bygninger og boliger]] (collection)
- [[Datasets by Collection/Grunddatamodellen/GeoDanmark/index.md|GeoDanmark]] (collection)
- [[Datasets by Collection/Grunddatamodellen/SkatteforvaltningensVirksomhedsregister/index.md|Skatteforvaltningens Virksomhedsregister]] (collection)

### Unmatched Realisations

- OpenStreetMap
## Realised By Links

- [[Datasets by Collection/Grunddatamodellen/CentraleVirksomhedsregister/index.md|CentraleVirksomhedsregister]] (collection)
- [[Datasets by Collection/Grunddatamodellen/BygningerOgBoliger/index.md|Bygninger og boliger]] (collection)
- [[Datasets by Collection/Grunddatamodellen/GeoDanmark/index.md|GeoDanmark]] (collection)
- [[Datasets by Collection/Grunddatamodellen/SkatteforvaltningensVirksomhedsregister/index.md|Skatteforvaltningens Virksomhedsregister]] (collection)

### Unmatched Realisations

- OpenStreetMap
