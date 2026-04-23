---
title: Populated Areas and Settlements
type: leaf
draft: false
sphere: Socio_Technical
subsphere: Socio_technical_socioeconomic
concept: Cognised settlement entities such as villages, towns, and cities, including hierarchy and urban footprint
question: Where are villages, towns, and cities, and what is their settlement hierarchy?
realisations:
  - OpenStreetMap
  - Natural Earth
primary_collection: OpenStreetMap
services: {}
---

> **Cognised existence:** Populated areas are settlement entities (city, town, village, hamlet, urban area) represented as points or polygons.

**Question:** Where are villages, towns, and cities, and what is their settlement hierarchy?

**OSM wiki:** [https://wiki.openstreetmap.org/wiki/Key:place](https://wiki.openstreetmap.org/wiki/Key:place)

---

## Realisations

### OpenStreetMap — settlement entities via `place=*`

OSM models settlements directly using `place` tags. This is suitable for settlement hierarchy mapping and nearest-settlement analysis.

#### osmnx access

```python
import osmnx as ox
ox.settings.cache_folder = ".cache/"

settlements = ox.features_from_place(
    "Denmark",
    tags={"place": ["city", "town", "village", "hamlet", "suburb"]},
)
```

#### Geofabrik layer

`gis_osm_places_free_1.shp` — place points with optional attributes such as `population`.

#### Key OSM tags

| Tag | Meaning |
| --- | --- |
| `place=city` | Major settlement |
| `place=town` | Town |
| `place=village` | Village |
| `place=hamlet` | Hamlet |
| `place=suburb` | Suburb/neighborhood |
| `population=*` | Optional settlement population estimate |

### Natural Earth — `ne_10m_populated_places`, `ne_10m_urban_areas`

Natural Earth provides globally consistent settlement points and generalized urban area polygons for small-scale mapping.

#### Python load

```python
import geopandas as gpd

places = gpd.read_file("ne_10m_populated_places.shp")
urban_areas = gpd.read_file("ne_10m_urban_areas.shp")

major_cities = places[places["SCALERANK"] <= 2]
```

#### Key attributes

| Field | Meaning |
| --- | --- |
| `NAME` | Settlement name |
| `FEATURECLA` | Feature class |
| `SCALERANK` | Cartographic prominence rank |
| `POP_MAX` | Maximum population estimate |
| `ADM0NAME` | Country name |

---

## Geometry Representations

| Rep ID | Source Dataset | Geometry Type | Native CRS | Suitable For | Not Suitable For |
| --- | --- | --- | --- | --- | --- |
| `settlements_osm_points` | OSM via Geofabrik | Point | EPSG:4326 | Settlement hierarchy mapping, nearest settlement analysis | Official census totals or demographic structure |
| `settlements_ne_10m_points` | Natural Earth populated places | Point | EPSG:4326 | Global city hierarchy maps, small-scale settlement context | Local-level settlement completeness |
| `settlements_ne_10m_urban_areas` | Natural Earth urban areas | Polygon | EPSG:4326 | Broad urban footprint context at global scale | Legal urban boundaries or municipal planning precision |

---

## Limitations

- OSM and Natural Earth settlement layers are not official census registers.
- Settlement class definitions vary by country and mapping conventions.
- Use statistical population grids or census datasets for demography and density metrics.

## Related Leaves

- [[Leaves/population\|Population]]
- [[Leaves/geographical-names\|Geographical Names]]
- [[Leaves/administrative-units\|Administrative Units]]

## Realised By Links

- [[Datasets by Collection/OpenStreetMap/index|OpenStreetMap]] (collection)
- [[Datasets by Collection/Natural Earth/index|Natural Earth]] (collection)
- [[Datasets by Owner/Natural Earth/index|Natural Earth]] (owner)
