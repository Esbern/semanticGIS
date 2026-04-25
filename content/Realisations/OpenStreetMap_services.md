---
title: "OpenStreetMap — By Amenity Tag Realisation of Services and Amenities"
type: realisation
draft: false
leaf: Services and Amenities
dataset: OpenStreetMap
tags:
  - realisation/openstreetmap
  - leaf/services
---

**Leaf:** [[Leaves/services|Services and Amenities]]
**Dataset:** OpenStreetMap — By Amenity Tag

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
