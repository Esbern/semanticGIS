---
title: "Census and administrative statistics Realisation of Population"
type: realisation
draft: false
leaf: Population
dataset: Census and administrative statistics
tags:
  - realisation/census_and_administrative_statistics
  - leaf/population
---

**Leaf:** [[Leaves/population|Population]]
**Dataset:** Census and administrative statistics

Population can also be represented as areal totals linked to administrative units (municipality, region, census tract, etc.).

#### Python load (example pattern)

```python
import geopandas as gpd
import rasterio

# Raster grid example (population count per cell)
with rasterio.open("population_grid.tif") as src:
    pop_grid = src.read(1)
    transform = src.transform

# Polygon example (population per statistical unit)
admin_pop = gpd.read_file("population_by_admin_units.gpkg")
admin_pop["pop_density"] = admin_pop["population"] / admin_pop.to_crs(3857).area * 1_000_000
```
