---
title: "Natural Earth — `ne_10m_admin_0_countries`, `ne_10m_admin_1_states_provinces` Realisation of Administrative Units"
type: realisation
draft: false
leaf: Administrative Units
dataset: Natural Earth
tags:
  - realisation/natural_earth
  - leaf/administrative-units
---

**Leaf:** [[Leaves/administrative-units|Administrative Units]]
**Dataset:** Natural Earth — `ne_10m_admin_0_countries`, `ne_10m_admin_1_states_provinces`

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
