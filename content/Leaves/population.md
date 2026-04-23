---
title: Population
type: leaf
draft: false
sphere: Socio_Technical
subsphere: Socio_technical_socioeconomic
concept: Cognised demographic magnitude over space, including counts, density, and composition by area
question: What is the population count, density, and demographic profile in this area?
realisations:
  - Official Census and Statistical Units
  - Global Population Grids
  - EU Population Grids
primary_collection: Statistical Offices and Population Grid Products
services: {}
---

> **Cognised existence:** Population is the measured quantity and density of inhabitants across space and time.

**Question:** What is the population count, density, and demographic profile in this area?

Population is typically represented as raster grids or statistical polygons, not as settlement place points.

---

## Realisations

### Global population grids

Global gridded datasets estimate population counts and density on regular cells (for example 1 km or 100 m depending on product/version).

Representative products:

| Product | Geometry | Typical Resolution | Scope |
| --- | --- | --- | --- |
| GHSL Population Grid (GHS-POP) | Raster grid | 250 m to 1 km | Global |
| WorldPop | Raster grid | ~100 m (country dependent) | Global (modelled) |
| GPWv4 (CIESIN) | Raster grid | ~1 km | Global |

### EU population grids

For Europe, population is commonly distributed in harmonized grid systems for comparable regional analysis.

Representative products:

| Product | Geometry | Typical Resolution | Scope |
| --- | --- | --- | --- |
| GEOSTAT population grid | Grid polygon / raster equivalent | 1 km | Europe |
| National statistical population grids | Grid polygon / raster | 100 m to 1 km | Country-specific |

### Census and administrative statistics

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

---

## Geometry Representations

| Rep ID | Source Dataset | Geometry Type | Native CRS | Suitable For | Not Suitable For |
| --- | --- | --- | --- | --- | --- |
| `population_grid_global` | GHSL / WorldPop / GPW | Raster grid | Product-specific | Density surfaces, exposure modelling, regional comparisons | Household-level counts, legal reporting |
| `population_grid_eu` | GEOSTAT / national EU grids | Grid polygon or raster | Product-specific | Harmonized European population comparisons, density analysis | Fine-grained individual-level inference |
| `population_admin_units` | Census by admin area | Polygon | National statistical CRS | Official reporting, demographic indicators by area | Within-unit spatial heterogeneity |

---

## Limitations

- Gridded population products are modelled estimates, not exact headcounts per cell.
- Census polygons introduce the modifiable areal unit problem (MAUP).
- Temporal mismatch across products is common; always check reference year.
- Settlement point datasets should be treated as populated-area proxies, not full population measures.

## Related Leaves

- [[Leaves/populated-areas\|Populated Areas and Settlements]]
- [[Leaves/administrative-units\|Administrative Units]]
- [[Leaves/geographical-names\|Geographical Names]]

## Realised By Links

- [[Classical Classifications/INSPIRE/population-distribution|INSPIRE Population Distribution]] (classification)
- [[Classical Classifications/UN-GGIM/population-distribution|UN-GGIM Population Distribution]] (classification)
