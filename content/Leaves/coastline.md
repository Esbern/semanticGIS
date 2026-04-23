---
title: Coastline
type: leaf
draft: false
sphere: Toposphere
subsphere: toposphere_coastline
concept: The physical boundary between land and sea as a mappable linear or polygon feature
question: Where is the land-sea boundary and what is its large-scale geometry?
realisations:
  - Natural Earth
  - OpenStreetMap
threads:
  - coastline-to-hydrosphere-marine
tags:
  - toposphere_coastline
  - coastline
  - land-sea-boundary
primary_collection: Natural Earth
services: {}
---

> **Cognised existence:** The coastline is the land-sea boundary — the line or polygon edge that separates terrestrial from marine space. It is foundational for any analysis that requires knowing what is land, what is water, or which areas are coastal.

**Question:** Where is the land-sea boundary and what is its large-scale geometry?

**Natural Earth downloads:** [https://www.naturalearthdata.com/downloads/](https://www.naturalearthdata.com/downloads/)

---

## Realisations

### Natural Earth — Coastline and Land/Ocean masks

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

---

### OpenStreetMap — `natural=coastline` (pre-processed derivatives)

OSM encodes the coastline using the tag `natural=coastline` on open ways. **Land is always on the left side of the way direction; sea is on the right.**

**Do you need a line or a polygon?** The answer determines which product to use:

| Use case | Geometry needed | Approach |
| --- | --- | --- |
| Display the coastline on a map | LineString | Use `ne_10m_coastline` (Natural Earth) or the OSM coastlines line file (below) |
| Distance to coast, buffer zone, proximity analysis | LineString | Either source above |
| Coastal length measurement | LineString | Either source above |
| Land/sea masking, point-in-polygon (is this point on land?) | Polygon | OSM land-polygons or NE `ne_10m_land` |
| Clip a dataset to land only | Polygon | OSM land-polygons or NE `ne_10m_land` |

**For the line case** osmdata.openstreetmap.de also publishes a pre-assembled coastlines-as-lines file alongside the polygon products:

**Download:** [https://osmdata.openstreetmap.de/data/coastlines.html](https://osmdata.openstreetmap.de/data/coastlines.html)

| Package | Geometry | Description |
| --- | --- | --- |
| `coastlines-split-4326.zip` | LineString | Assembled, consistent-direction coastline segments, EPSG:4326 |
| `land-polygons-split-4326.zip` | Polygon | Land polygons for masking, EPSG:4326 |
| `water-polygons-split-4326.zip` | Polygon | Ocean / sea water polygons |
| `simplified-land-polygons-complete-3857.zip` | Polygon | Simplified for tile rendering, EPSG:3857 |

#### OSM coastline — Python load

```python
import geopandas as gpd

# Line form — for display, distance, proximity
coastline = gpd.read_file("coastlines-split-4326/lines.shp")

# Polygon form — for masking / point-in-polygon
land = gpd.read_file("land-polygons-split-4326/land_polygons.shp")

# Clip to a bounding box (e.g. Denmark + surrounding sea)
bbox = (7.0, 54.0, 16.0, 58.5)
coastline_dk = coastline.cx[bbox[0]:bbox[2], bbox[1]:bbox[3]]
land_dk = land.cx[bbox[0]:bbox[2], bbox[1]:bbox[3]]
```

#### Why raw Overpass / osmnx ways are problematic

Raw `natural=coastline` ways from Overpass or osmnx are disconnected partial segments with inconsistent direction. They are **not** pre-assembled into a continuous line and cannot be used directly for either display or analysis without a join step.

| Approach | Problem |
| --- | --- |
| `ox.features_from_place(..., tags={"natural": "coastline"})` | Returns disconnected, inconsistently oriented segments |
| Overpass `way["natural"="coastline"]` | Same — partial segments, no topological join |
| `osmcoastline` (local) | Correct but requires full planet `.osm.pbf` and the tool |

For sub-national detail (e.g. Danish fjords, harbour inlets) OSM-derived coastline at full resolution surpasses Natural Earth. Use the `coastlines-split-4326` (line) or `land-polygons-split-4326` (polygon) product clipped to the area of interest.

---

## Geometry Representations

| Rep ID | Source Dataset | Geometry Type | Native CRS | Suitable For | Not Suitable For |
| --- | --- | --- | --- | --- | --- |
| `coastline_ne_10m_line` | Natural Earth 10m | LineString | EPSG:4326 | Display, distance to coast, coastal length, overlay reference | Sub-kilometre precision, legal disputes |
| `coastline_ne_10m_land` | Natural Earth 10m | Polygon | EPSG:4326 | Land/sea masking, point-in-polygon, clip to land | Cadastral or legal precision |
| `coastline_ne_50m_line` | Natural Earth 50m | LineString | EPSG:4326 | Continental-scale mapping | Any sub-regional detail |
| `coastline_osm_lines` | OSM coastlines-split-4326 (assembled) | LineString | EPSG:4326 | High-resolution display, distance-to-coast, proximity analysis, coastal length | Not suitable as-is for land masking (use polygon form instead) |
| `coastline_osm_land_polygons` | OSM land-polygons-split-4326 (assembled) | Polygon | EPSG:4326 | Land/sea masking, point-in-polygon, clip to land, fjord and inlet detail | Requires pre-downloaded file; not streamed from Overpass |

---

## Limitations

- Natural Earth coastline is generalised — not suitable for precise coastal engineering, legal shoreline disputes, or sub-kilometre coastal modelling.
- Island coverage at `10m` is extensive but not exhaustive for very small or remote islands.
- For authoritative national coastlines, use official surveying agency products (e.g. GeoDanmark for Denmark, Ordnance Survey for UK).
- Raster relief products from Natural Earth include bathymetry shading but are not bathymetric data for depth analysis.
- Raw OSM `natural=coastline` ways **cannot be used directly** — always use the pre-processed `land-polygons-split-4326` product from osmdata.openstreetmap.de.

## Realised By Links

- [[Datasets by Collection/Natural Earth/index|Natural Earth]] (collection)
- [[Datasets by Owner/Natural Earth/index|Natural Earth]] (owner)
- [[Datasets by Collection/OpenStreetMap/index|OpenStreetMap]] (collection via osmdata land-polygons)

## Related Leaves

- [[Leaves/marine-waters|Marine and Coastal Waters]]
- [[Leaves/coastal-erosion-risk|Coastal Erosion Risk]]
- [[Leaves/elevation|Elevation Models]]
