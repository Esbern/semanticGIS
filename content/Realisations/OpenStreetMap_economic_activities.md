---
title: "OpenStreetMap — Tag Families Realisation of Economic Activities"
type: realisation
draft: false
leaf: Economic Activities
dataset: OpenStreetMap
tags:
  - realisation/openstreetmap
  - leaf/economic-activities
---

**Leaf:** [[Leaves/economic-activities|Economic Activities]]
**Dataset:** OpenStreetMap — Tag Families

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

## Temporal Model

Industry classification is **bitemporal** (inherited from [[Datasets by Collection/Grunddatamodellen/Shared Temporal Superclass Contract|Shared Temporal Superclass Contract]]). A business can change its primary industry over time. Historical queries require `virkningFra`/`virkningTil` filtering.
