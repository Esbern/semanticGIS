---
title: "Natural Earth — `ne_10m_populated_places`, `ne_10m_urban_areas` Realisation of Populated Areas and Settlements"
type: realisation
draft: false
leaf: Populated Areas and Settlements
dataset: Natural Earth
tags:
  - realisation/natural_earth
  - leaf/populated-areas
---

**Leaf:** [[Leaves/populated-areas|Populated Areas and Settlements]]
**Dataset:** Natural Earth — `ne_10m_populated_places`, `ne_10m_urban_areas`

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
