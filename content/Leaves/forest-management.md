---

title: Forest Cover and Management
type: leaf
draft: false
sphere: Biosphere
subsphere: Terrestrial_Ecosystems
concept: Forest and woodland areas as land cover and ecological resource
question: Where are forests and woodland areas and what type are they?
threads: []
tags:
  - biosphere
  - forest
  - land-cover
---

> **Cognised existence:** Forests are contiguous areas of tree cover that function as ecological systems, carbon stores, and managed resources. Their spatial extent and type are the primary inputs for biodiversity, climate, and land management analysis.

**Question:** Where are forests and woodland areas and what type are they?

**OSM wiki:** [https://wiki.openstreetmap.org/wiki/Tag:landuse%3Dforest](https://wiki.openstreetmap.org/wiki/Tag:landuse%3Dforest) | [https://wiki.openstreetmap.org/wiki/Tag:natural%3Dwood](https://wiki.openstreetmap.org/wiki/Tag:natural%3Dwood)

---

## Realisations

Instead of hardcoding implementation schemas here, SPHERE separates semantic meaning from dataset implementation. See the following realisations for how to access this data:

- **[[Realisations/OpenStreetMap_forest_management|OpenStreetMap — `landuse=forest`, `natural=wood`]]**

---

## Geometry Representations

| Rep ID | Source Dataset | Geometry Type | Native CRS | Suitable For | Not Suitable For |
| --- | --- | --- | --- | --- | --- |
| `forest_osm_polygon` | OSM via Geofabrik | Polygon | EPSG:4326 | Area calculation, fragmentation analysis, map display | Sub-stand classification, age structure, canopy height |

---

## Limitations

- `landuse=forest` vs `natural=wood` distinction is applied inconsistently.
- Species composition and management intensity are not reliably tagged.
- For canopy cover and forest type, consider Global Forest Watch, Copernicus Land Cover, or CORINE Land Cover.
