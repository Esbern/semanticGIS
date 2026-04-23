---
title: Natural Earth
draft: false
tags:
  - data-portal
  - natural-earth
  - global
  - vector
  - raster
---

[Natural Earth](https://www.naturalearthdata.com/downloads/) provides free public-domain global basemap data for small-scale mapping and analytics.

It is organized by:

- **Scale:** `1:10m`, `1:50m`, `1:110m`
- **Theme:** **Cultural**, **Physical**, **Raster**
- **Format:** zipped shapefiles (vector) and raster relief products

**Collection page:** [[Datasets by Collection/Natural Earth/index|Natural Earth Collection]]
**Owner page:** [[Datasets by Owner/Natural Earth/index|Natural Earth (owner)]]

---

## Access Pattern

1. Open [Natural Earth Downloads](https://www.naturalearthdata.com/downloads/).
2. Select scale (`10m`, `50m`, `110m`) by intended zoom/analysis detail.
3. Select theme (Cultural/Physical/Raster).
4. Download zipped package and load in GIS/Python.

Typical Python load flow:

```python
import geopandas as gpd

gdf = gpd.read_file("ne_10m_admin_0_countries.shp")
```

---

## Leaf Coverage Matrix

| Natural Earth Theme Family | Example Layers | Mapped Leaves | New Leaf Required? |
| --- | --- | --- | --- |
| Administrative boundaries | `admin_0_*`, `admin_1_*` | [[Leaves/administrative-units\|Administrative Units]] | No |
| Populated places and urban areas | `populated_places`, `urban_areas` | [[Leaves/geographical-names\|Geographical Names]], [[Leaves/populated-areas\|Populated Areas and Settlements]] | No |
| Roads / rail / airports / ports | `roads`, `railroads`, `airports`, `ports` | [[Leaves/transport-networks\|Transport Networks]], [[Leaves/nautical-traffic\|Nautical Traffic]] | No |
| Lakes, rivers, basins | `lakes`, `rivers_lake_centerlines`, `geography_marine_polys` | [[Leaves/freshwater-bodies\|Surface Freshwater Bodies]], [[Leaves/hydrological-basin-delineations\|Hydrological Basin Delineations]], [[Leaves/marine-waters\|Marine and Coastal Waters]] | No |
| Coastline and ocean/land masks | `coastline`, `ocean`, `land` | [[Leaves/coastline\|Coastline]], [[Leaves/marine-waters\|Marine and Coastal Waters]], [[Leaves/coastal-erosion-risk\|Coastal Erosion Risk]] | No — Coastline leaf created |
| Elevation/bathymetry context | `sr_w/e`, shaded relief, bathymetry rasters | [[Leaves/elevation\|Elevation Models]] | No |
| Land cover and natural areas proxies | `land`, `glaciated_areas`, `reefs` | [[Leaves/habitat-extent\|Habitat Extent]], [[Leaves/nature-protection-areas\|Nature Protection Areas]] | No (proxy use) |
| Sovereignty and map units variants | `admin_0_map_units`, `admin_0_countries`, disputed variants | [[Leaves/administrative-units\|Administrative Units]] | No |

---

## Geometry and CRS Notes

- Natural Earth vectors are distributed in geographic coordinates (`EPSG:4326`).
- Use `10m` for analysis where shape fidelity matters.
- Use `50m`/`110m` for continental/global visualization and fast overlays.
- Treat Natural Earth as **small-scale reference/cartographic baseline**, not legal authority.

---

## Implementation Decision

- **MVP decision:** start with existing leaves only.
- **New leaves required now:** none.
- **Future optional leaf candidate:** dedicated coastline morphology leaf, only if shoreline-structure workflows become a recurring requirement.
