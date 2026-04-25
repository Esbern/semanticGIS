---
title: "Natural Earth — `ne_10m_populated_places` Realisation of Geographical Names"
type: realisation
draft: false
leaf: Geographical Names
dataset: Natural Earth
tags:
  - realisation/natural_earth
  - leaf/geographical-names
---

**Leaf:** [[Leaves/geographical-names|Geographical Names]]
**Dataset:** Natural Earth — `ne_10m_populated_places`

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
