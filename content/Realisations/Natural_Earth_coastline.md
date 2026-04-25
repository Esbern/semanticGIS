---
title: "Natural Earth — Coastline and Land/Ocean masks Realisation of Coastline"
type: realisation
draft: false
leaf: Coastline
dataset: Natural Earth
tags:
  - realisation/natural_earth
  - leaf/coastline
---

**Leaf:** [[Leaves/coastline|Coastline]]
**Dataset:** Natural Earth — Coastline and Land/Ocean masks

Natural Earth provides the most widely used public-domain global coastline at three generalisation levels. It is appropriate for global-to-regional mapping and spatial analysis at scales where high-precision coastal surveys are not required.

#### Scale selection guide

| Scale | Shapefile | Use case |
| --- | --- | --- |
| `1:10m` | `ne_10m_coastline.shp` | Regional analysis, national-level maps, coastal context overlays |
| `1:50m` | `ne_50m_coastline.shp` | Continental overview, medium-scale thematic maps |
| `1:110m` | `ne_110m_coastline.shp` | Global visualisation, small-scale reference maps |

#### Python load

```python
import geopandas as gpd

# Coastline as LineString (all scales follow same pattern)
coastline = gpd.read_file("ne_10m_coastline.shp")

# Land as Polygon (useful for land/sea masking)
land = gpd.read_file("ne_10m_land.shp")

# Ocean as Polygon
ocean = gpd.read_file("ne_10m_ocean.shp")

# Clip to a bounding box
bbox = (5.0, 54.0, 16.0, 58.0)  # roughly Denmark + neighbours
coastline_clip = coastline.cx[bbox[0]:bbox[2], bbox[1]:bbox[3]]
```

#### Key attributes (`ne_10m_coastline`)

| Field | Meaning |
| --- | --- |
| `featurecla` | Feature class (`Coastline`) |
| `scalerank` | Visibility rank (lower = more prominent) |
| `min_zoom` | Suggested minimum display zoom level |

#### Available companion layers

| Layer | Geometry | Use |
| --- | --- | --- |
| `ne_10m_land` | Polygon | Land mask |
| `ne_10m_ocean` | Polygon | Ocean mask |
| `ne_10m_coastline` | LineString | Coastline line |
| `ne_10m_minor_islands` | Polygon | Small islands not in main land polygon |
| `ne_10m_reefs` | LineString | Reef features near coast |
