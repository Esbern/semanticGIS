---
title: "Natural Earth — Lakes and Rivers Realisation of Surface Freshwater Bodies"
type: realisation
draft: false
leaf: Surface Freshwater Bodies
dataset: Natural Earth
tags:
  - realisation/natural_earth
  - leaf/freshwater-bodies
---

**Leaf:** [[Leaves/freshwater-bodies|Surface Freshwater Bodies]]
**Dataset:** Natural Earth — Lakes and Rivers

Natural Earth includes `ne_10m_lakes`, `ne_10m_rivers_lake_centerlines`, and related ocean basin polygon variants at three scales. Best used for continental or global overview contexts.

#### Python load

```python
import geopandas as gpd

lakes = gpd.read_file("ne_10m_lakes.shp")
rivers = gpd.read_file("ne_10m_rivers_lake_centerlines.shp")

# Optional: filter to major rivers only
major_rivers = rivers[rivers["scalerank"] <= 4]
```

#### Key attributes

| Field | Meaning |
| --- | --- |
| `featurecla` | Feature class (`Lake`, `River`) |
| `name` | Feature name |
| `scalerank` | Prominence rank (lower = larger/more important) |
| `min_zoom` | Suggested minimum display zoom |
