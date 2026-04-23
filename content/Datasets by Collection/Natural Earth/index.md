---
title: Natural Earth
draft: false
tags:
  - collection
  - natural-earth
  - global
  - vector
  - raster
---

Natural Earth is a global small-scale cartographic dataset family for boundaries, hydrography, transport context, places, and physical reference layers.

**Portal page:** [[Data Portals/Natural Earth/index|Natural Earth Portal]]

---

## Dataset Families

| Family | Representative Layers | Primary Geometry |
| --- | --- | --- |
| Cultural boundaries | `admin_0_*`, `admin_1_*` | Polygon / LineString |
| Human geography | `populated_places`, `urban_areas` | Point / Polygon |
| Transport | `roads`, `railroads`, `airports`, `ports` | LineString / Point |
| Hydrography | `lakes`, `rivers_lake_centerlines` | Polygon / LineString |
| Marine and coast | `coastline`, `ocean`, `geography_marine_polys` | LineString / Polygon |
| Physical reference | `land`, `glaciated_areas`, relief/bathymetry rasters | Polygon / Raster |

---

## Coverage by Leaf

| Leaf | Natural Earth Coverage |
| --- | --- |
| [[Leaves/administrative-units\|Administrative Units]] | Country and first-level admin boundaries |
| [[Leaves/geographical-names\|Geographical Names]] | Named populated places and selected named features |
| [[Leaves/populated-areas\|Populated Areas and Settlements]] | Populated places and generalized urban area polygons |
| [[Leaves/population\|Population]] | Place population proxy attributes only (`POP_MAX`, `POP_MIN`) |
| [[Leaves/transport-networks\|Transport Networks]] | Generalized global road and rail context |
| [[Leaves/freshwater-bodies\|Surface Freshwater Bodies]] | Lakes and river centerlines |
| [[Leaves/marine-waters\|Marine and Coastal Waters]] | Marine polygons, coastline, ocean/land context |
| [[Leaves/coastline\|Coastline]] | Global coastline at 10m/50m/110m scale |
| [[Leaves/hydrological-basin-delineations\|Hydrological Basin Delineations]] | Basin/catchment context (small-scale support) |
| [[Leaves/elevation\|Elevation Models]] | Global relief and bathymetric raster context |
| [[Leaves/habitat-extent\|Habitat Extent]] | Broad physical/ecological proxy extents |

---

## Limitations

- Not suitable for cadastral, legal, or municipal-precision boundary decisions.
- Transport and hydrography are generalized and not routing-grade.
- Use as global baseline; pair with local authoritative datasets for operational decisions.
