---
title: "OpenStreetMap — `shop=*`, `amenity=*`, `office=*` Realisation of Business Locations"
type: realisation
draft: false
leaf: Business Locations
dataset: OpenStreetMap
tags:
  - realisation/openstreetmap
  - leaf/business-locations
---

**Leaf:** [[Leaves/business-locations|Business Locations]]
**Dataset:** OpenStreetMap — `shop=*`, `amenity=*`, `office=*`

OSM provides global point and polygon features for businesses and services. Coverage is strongest in dense urban areas.

#### osmnx access

```python
import osmnx as ox
ox.settings.cache_folder = ".cache/"

businesses = ox.features_from_place(
    "Copenhagen, Denmark",
    tags={
        "shop": True,
        "amenity": ["restaurant", "cafe", "bank", "pharmacy", "hospital", "school"],
        "office": True,
    },
)
```

#### Geofabrik layers

| Layer | Content |
| --- | --- |
| `gis_osm_pois_free_1.shp` | Point POIs including shops and amenities |
| `gis_osm_pois_a_free_1.shp` | Polygon POIs |

#### Key OSM tags

| Tag | Meaning |
| --- | --- |
| `shop=*` | Retail business class |
| `amenity=*` | Public/commercial service class |
| `office=*` | Office function |
| `name=*` | Business name |
| `brand=*` | Brand chain |
| `opening_hours=*` | Opening schedule |
