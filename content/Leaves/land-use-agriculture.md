---

title: Agricultural Land Management
type: leaf
draft: false
sphere: Socio_Technical
subsphere: Socio_technical_resource_utilisation
concept: Agricultural production and land management regimes describing cultivated use classes
question: Which agricultural land-use classes apply in this area?
threads: []
tags:
  - socio_technical_resource_utilisation
  - agriculture
  - land-use
---

> **Cognised existence:** Agricultural land management is the way cultivated surfaces are classified and used over time.

**Question:** Which agricultural land-use classes apply in this area?

**OSM wiki:** [https://wiki.openstreetmap.org/wiki/Key:landuse](https://wiki.openstreetmap.org/wiki/Key:landuse)

---

## Realisations

Instead of hardcoding implementation schemas here, SPHERE separates semantic meaning from dataset implementation. See the following realisations for how to access this data:

- **[[Realisations/OpenStreetMap_land_use_agriculture|OpenStreetMap — `landuse=*`]]**

---

## Geometry Representations

| Rep ID | Source Dataset | Geometry Type | Native CRS | Suitable For | Not Suitable For |
| --- | --- | --- | --- | --- | --- |
| `agri_osm_polygons` | OSM via Geofabrik | Polygon | EPSG:4326 | Area totals, land-use share, overlap with protection zones | Crop-yield modelling and subsidy compliance |

---

## Limitations

- Agricultural classes are broad and not crop-specific.
- Mapping quality depends on local contributors.
- For policy-grade agriculture statistics, use national LPIS or equivalent.
