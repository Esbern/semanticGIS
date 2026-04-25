---

title: Populated Areas and Settlements
type: leaf
draft: false
sphere: Socio_Technical
subsphere: Socio_technical_socioeconomic
concept: Cognised settlement entities such as villages, towns, and cities, including hierarchy and urban footprint
question: Where are villages, towns, and cities, and what is their settlement hierarchy?
---

> **Cognised existence:** Populated areas are settlement entities (city, town, village, hamlet, urban area) represented as points or polygons.

**Question:** Where are villages, towns, and cities, and what is their settlement hierarchy?

**OSM wiki:** [https://wiki.openstreetmap.org/wiki/Key:place](https://wiki.openstreetmap.org/wiki/Key:place)

---

## Realisations

Instead of hardcoding implementation schemas here, SPHERE separates semantic meaning from dataset implementation. See the following realisations for how to access this data:

- **[[Realisations/OpenStreetMap_populated_areas|OpenStreetMap — settlement entities via `place=*`]]**
- **[[Realisations/Natural_Earth_populated_areas|Natural Earth — `ne_10m_populated_places`, `ne_10m_urban_areas`]]**

---

## Geometry Representations

| Rep ID | Source Dataset | Geometry Type | Native CRS | Suitable For | Not Suitable For |
| --- | --- | --- | --- | --- | --- |
| `settlements_osm_points` | OSM via Geofabrik | Point | EPSG:4326 | Settlement hierarchy mapping, nearest settlement analysis | Official census totals or demographic structure |
| `settlements_ne_10m_points` | Natural Earth populated places | Point | EPSG:4326 | Global city hierarchy maps, small-scale settlement context | Local-level settlement completeness |
| `settlements_ne_10m_urban_areas` | Natural Earth urban areas | Polygon | EPSG:4326 | Broad urban footprint context at global scale | Legal urban boundaries or municipal planning precision |

---

## Limitations

- OSM and Natural Earth settlement layers are not official census registers.
- Settlement class definitions vary by country and mapping conventions.
- Use statistical population grids or census datasets for demography and density metrics.

## Related Leaves

- [[Leaves/population\|Population]]
- [[Leaves/geographical-names\|Geographical Names]]
- [[Leaves/administrative-units\|Administrative Units]]
