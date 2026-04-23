---
title: Administrative Units
type: leaf
draft: false
sphere: Socio_Technical
subsphere: Socio_technical_governance
concept: Cognised territorial divisions for governance and statistical aggregation
question: Which administrative area does a location belong to?
realisations:
  - OpenStreetMap
  - Natural Earth
threads: []
tags:
  - socio_technical_governance
  - administrative
primary_collection: OpenStreetMap
services: {}
---

> **Cognised existence:** Administrative units are territorial divisions defined by governance acts. They exist because a political authority declared them. Their boundaries determine jurisdiction, statistical aggregation, electoral geography, and service responsibility.

**Question:** Which administrative area does a location belong to?

**OSM wiki:** [https://wiki.openstreetmap.org/wiki/Tag:boundary%3Dadministrative](https://wiki.openstreetmap.org/wiki/Tag:boundary%3Dadministrative)

---

## Realisations

### OpenStreetMap — `boundary=administrative`

OSM carries administrative boundary relations globally, tagged with `admin_level=*`. The numeric level indicates hierarchical tier but the meaning varies by country.

**Global `admin_level` conventions (varies by country):**

| admin_level | Common use |
| --- | --- |
| 2 | National boundary |
| 4 | State / region / province |
| 6 | County / department |
| 7–8 | Municipality / district |
| 9–10 | Sub-municipal (ward, parish) |

Per-country mappings: [https://wiki.openstreetmap.org/wiki/Tag:boundary%3Dadministrative](https://wiki.openstreetmap.org/wiki/Tag:boundary%3Dadministrative)

#### osmnx access (recommended)

```python
import osmnx as ox
ox.settings.cache_folder = ".cache/"

# Geocode a named area to its boundary polygon
gdf = ox.geocode_to_gdf("Copenhagen Municipality, Denmark")

# Get all municipalities in a country
municipalities = ox.features_from_place(
    "Denmark",
    tags={"boundary": "administrative", "admin_level": "7"}
)
```

#### Overpass (fallback)

```ql
[out:json][timeout:120];
(
  relation["boundary"="administrative"]["admin_level"="7"]["ISO3166-1"="DK"];
);
out body; >; out skel qt;
```

#### Key OSM tags

| Tag | Meaning |
| --- | --- |
| `boundary=administrative` | Administrative boundary relation |
| `admin_level=*` | Hierarchy level (country-specific meaning) |
| `name=*` | Official name |
| `name:en=*` | English name |
| `ISO3166-1=*` | ISO country code (level 2) |
| `ISO3166-2=*` | ISO sub-national code |
| `ref=*` | Official code reference |

### Natural Earth — `ne_10m_admin_0_countries`, `ne_10m_admin_1_states_provinces`

Natural Earth provides national (ADM0) and first-level (ADM1) boundaries in Polygon form at three scales. Attributes include ISO codes, country names, and GeoUnit identifiers.

#### Python load

```python
import geopandas as gpd

# National boundaries
countries = gpd.read_file("ne_10m_admin_0_countries.shp")

# First-level administrative units
regions = gpd.read_file("ne_10m_admin_1_states_provinces.shp")

# Filter to a single country
dk = countries[countries["ISO_A2"] == "DK"]
```

#### Key attributes (ADM0)

| Field | Meaning |
| --- | --- |
| `NAME` | Country name |
| `ISO_A2` | ISO 3166-1 alpha-2 code |
| `ISO_A3` | ISO 3166-1 alpha-3 code |
| `ADMIN` | Full administrative name |
| `CONTINENT` | Continent |
| `POP_EST` | Population estimate |

#### De facto vs. de jure — Natural Earth layer selection

Natural Earth separates the question "who administers this territory?" (de facto) from "who claims sovereign authority?" (de jure) through a deliberate layer family. **Always choose the layer that matches your analytical question.**

| Layer | Represents | Use when |
| --- | --- | --- |
| `ne_10m_admin_0_sovereignty` | De jure sovereign states only — the internationally recognised legal claim | Diplomatic analysis, treaty coverage, UN membership, international law contexts |
| `ne_10m_admin_0_countries` | De facto administrative units — how territory is actually governed on the ground today | Operational mapping, routing, administrative statistics, population attribution |
| `ne_10m_admin_0_map_units` | Further subdivisions of countries for cartographic clarity (e.g. Alaska shown separately) | Cartographic display, atlas-style maps |
| `ne_10m_admin_0_disputed_areas` | Areas where sovereignty or administration is actively contested | Conflict mapping, geopolitical analysis — **never use as authoritative boundary** |
| `ne_10m_admin_0_boundary_lines_land` | Boundary lines with a `status` attribute (`Definite`, `Indefinite`, `Disputed`, `Breakaway`, etc.) | Displaying boundary certainty and legal status |

**Key principle:** `admin_0_countries` may include territories administered by a state that does not hold de jure sovereignty over them (e.g. occupied territories, dependencies, breakaway regions). `admin_0_sovereignty` will attribute those same polygons to the legally recognised sovereign instead.

```python
import geopandas as gpd

# De facto — who governs the ground
countries = gpd.read_file("ne_10m_admin_0_countries.shp")

# De jure — who holds sovereign legal claim
sovereignty = gpd.read_file("ne_10m_admin_0_sovereignty.shp")

# Disputed areas — use only for display/analysis of contested status
disputed = gpd.read_file("ne_10m_admin_0_disputed_areas.shp")

# Boundary lines with status attribute
boundaries = gpd.read_file("ne_10m_admin_0_boundary_lines_land.shp")
print(boundaries["status"].value_counts())
# -> Definite, Indefinite, Disputed, Breakaway, Claim boundary, ...
```

**OSM note:** OSM encodes the on-the-ground situation (de facto) by convention. Disputed boundaries are tagged with `disputed=yes` and/or `border_type=*`. OSM does not carry a parallel de jure geometry — for legal claim boundaries use Natural Earth `admin_0_sovereignty` or `admin_0_disputed_areas`.

---

## Geometry Representations

| Rep ID | Source Dataset | Geometry Type | Native CRS | Suitable For | Not Suitable For |
| --- | --- | --- | --- | --- | --- |
| `admin_osm_polygon` | OSM via osmnx / Overpass | Polygon (relation) | EPSG:4326 | Area queries, point-in-polygon, map display, aggregation | Legal boundary disputes — OSM may lag official updates |
| `admin_ne_10m_countries` | Natural Earth 10m — de facto countries | Polygon | EPSG:4326 | Operational global maps, statistics attribution, population linkage | Legal sovereignty disputes |
| `admin_ne_10m_sovereignty` | Natural Earth 10m — de jure sovereignty | Polygon | EPSG:4326 | Diplomatic/legal contexts, treaty and international law framing | Operational routing or services in disputed territories |
| `admin_ne_10m_disputed` | Natural Earth 10m — disputed areas | Polygon | EPSG:4326 | Visualising contested zones, geopolitical analysis | Any authoritative administrative attribution |
| `admin_ne_50m_polygon` | Natural Earth 50m | Polygon | EPSG:4326 | World-view context mapping | Regional or local detail |

---

## Limitations

- OSM administrative boundaries may lag official updates (elections, boundary changes).
- `admin_level` values are country-specific — always check the OSM wiki for the country in question.
- Boundary quality is highest in Europe and North America; variable elsewhere.
- Natural Earth `admin_0_countries` represents de facto administration, not de jure sovereignty — they diverge for ~20–30 territories globally (occupied areas, breakaway states, dependencies). Always confirm which layer is appropriate for the analytical context before use.

## Realised By Links

- [[Datasets by Collection/OpenStreetMap/index|OpenStreetMap]] (collection)
- [[Datasets by Collection/Natural Earth/index|Natural Earth]] (collection)
