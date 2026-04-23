---
title: Geographical Names
type: leaf
draft: false
sphere: Socio_Technical
subsphere: Socio_technical_governance
concept: Named places and topographic features as spatial identifiers
question: What is the name and location of a place or topographic feature?
realisations:
  - OpenStreetMap
  - Natural Earth
  - places
primary_collection: OpenStreetMap
services: {}
---

> **Cognised existence:** Geographical names are the human identifiers for places — cities, villages, mountains, rivers, regions. They are the primary keys for geocoding and the spatial anchors for most human communication about place.

**Question:** What is the name and location of a place or topographic feature?

**OSM wiki:** [https://wiki.openstreetmap.org/wiki/Key:place](https://wiki.openstreetmap.org/wiki/Key:place) | [https://wiki.openstreetmap.org/wiki/Key:name](https://wiki.openstreetmap.org/wiki/Key:name)

---

## Realisations

### OpenStreetMap — `place=*`, `name=*`

OSM contains named place points globally, from cities to hamlets, plus named topographic features. It is the primary open dataset for geocoding and place labelling.

#### osmnx access

```python
import osmnx as ox
ox.settings.cache_folder = ".cache/"

# All named places in an area
places = ox.features_from_place(
    "Denmark",
    tags={"place": ["city", "town", "village", "hamlet", "suburb"]}
)

# Geocode a place name to coordinates + boundary polygon
gdf = ox.geocode_to_gdf("Aarhus, Denmark")
```

#### Geofabrik layer

`gis_osm_places_free_1.shp` — point layer, fields: `osm_id`, `code`, `fclass` (city/town/village/hamlet/suburb/island…), `name`, `population`.

#### Key OSM tags

| Tag | Meaning |
| --- | --- |
| `place=city` | City (typically > 100k pop.) |
| `place=town` | Town |
| `place=village` | Village |
| `place=hamlet` | Hamlet |
| `place=suburb` | Suburb or named neighbourhood |
| `place=island` | Island |
| `place=locality` | Named uninhabited location |
| `name=*` | Primary name (local language) |
| `name:en=*` | English name |
| `population=*` | Population estimate (sparse) |

### Natural Earth — `ne_10m_populated_places`

Natural Earth provides a curated point dataset of globally significant populated places, cross-referenced to multiple authoritative gazetteer sources. It includes ADM0 (country) and ADM1 (first-level) name associations and a `scalerank` field for symbol filtering.

#### Python load

```python
import geopandas as gpd

places = gpd.read_file("ne_10m_populated_places.shp")

# Filter by rank for display
major = places[places["scalerank"] <= 5]
```

#### Key attributes

| Field | Meaning |
| --- | --- |
| `NAME` | Primary place name |
| `NAME_EN` | English name |
| `FEATURECLA` | Feature class (Populated place) |
| `SCALERANK` | Display prominence (0 = most prominent) |
| `POP_MAX` | Maximum population estimate |
| `ADM0NAME` | Country name |
| `ADM1NAME` | First-level administrative unit name |
| `SOV0NAME` | Sovereignty name |

---

## Geometry Representations

| Rep ID | Source Dataset | Geometry Type | Native CRS | Suitable For | Not Suitable For |
| --- | --- | --- | --- | --- | --- |
| `names_osm_points` | OSM via Geofabrik | Point | EPSG:4326 | Geocoding, labelling, proximity search | Area-based aggregation (use admin boundary polygons instead) |
| `names_ne_10m_points` | Natural Earth 10m populated places | Point | EPSG:4326 | Global reference labelling, settlement hierarchy maps, continental-scale geocoding | Sub-national name coverage, local gazetteers |

---

## Limitations

- Population data is very sparse and not reliably maintained.
- City/town/village classification is inconsistent across countries.
- For authoritative national gazetteers, prefer official national datasets.

## Realised By Links

- [[Datasets by Collection/OpenStreetMap/index|OpenStreetMap]] (collection)
- [[Datasets by Collection/Natural Earth/index|Natural Earth]] (collection)
