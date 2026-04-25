---

title: Population
type: leaf
draft: false
sphere: Socio_Technical
subsphere: Socio_technical_socioeconomic
concept: Cognised demographic magnitude over space, including counts, density, and composition by area
question: What is the population count, density, and demographic profile in this area?
---

> **Cognised existence:** Population is the measured quantity and density of inhabitants across space and time.

**Question:** What is the population count, density, and demographic profile in this area?

Population is typically represented as raster grids or statistical polygons, not as settlement place points.

---

## Realisations

Instead of hardcoding implementation schemas here, SPHERE separates semantic meaning from dataset implementation. See the following realisations for how to access this data:

- **[[Realisations/Global_population_grids_population|Global population grids]]**
- **[[Realisations/EU_population_grids_population|EU population grids]]**
- **[[Realisations/Census_and_administrative_statistics_population|Census and administrative statistics]]**

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
