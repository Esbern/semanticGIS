---

title: Surface Freshwater Bodies
type: leaf
draft: false
sphere: Hydrosphere
subsphere: Freshwater_Surface
concept: Lakes, rivers, streams, and other surface freshwater features
question: What surface freshwater bodies exist at a location and how do they flow?
---

> **Cognised existence:** Surface freshwater bodies are the visible hydrological features of the landscape — rivers, streams, lakes, ponds, reservoirs, and canals. They are both ecological habitats and infrastructure.

**Question:** What surface freshwater bodies exist at a location and how do they flow?

**OSM wiki:** [https://wiki.openstreetmap.org/wiki/Key:waterway](https://wiki.openstreetmap.org/wiki/Key:waterway) | [https://wiki.openstreetmap.org/wiki/Tag:natural%3Dwater](https://wiki.openstreetmap.org/wiki/Tag:natural%3Dwater)

---

## Realisations

Instead of hardcoding implementation schemas here, SPHERE separates semantic meaning from dataset implementation. See the following realisations for how to access this data:

- **[[Realisations/OpenStreetMap_freshwater_bodies|OpenStreetMap — `waterway=*`, `natural=water`]]**
- **[[Realisations/Natural_Earth_freshwater_bodies|Natural Earth — Lakes and Rivers]]**

---

## Geometry Representations

| Rep ID | Source Dataset | Geometry Type | Native CRS | Suitable For | Not Suitable For |
| --- | --- | --- | --- | --- | --- |
| `freshwater_osm_lines` | OSM via Geofabrik | LineString | EPSG:4326 | Network tracing, flow direction, river mapping | Catchment area calculation |
| `freshwater_osm_polygons` | OSM via Geofabrik | Polygon | EPSG:4326 | Surface area, shoreline mapping | Flow routing, upstream/downstream analysis |
| `freshwater_ne_10m_lakes` | Natural Earth 10m lakes | Polygon | EPSG:4326 | Global lake context, continental overview | Small or sub-regional lake detail |
| `freshwater_ne_10m_rivers` | Natural Earth 10m rivers and lake centerlines | LineString | EPSG:4326 | Global/continental river context, atlas mapping | Tributary-level hydrological analysis |

**Important:** For catchment / drainage basin analysis, a DEM-derived hydrological network (e.g. Copernicus DEM + SAGA/WhiteboxTools) is more reliable than OSM waterways.

---

## Limitations

- Small streams are under-mapped in many regions.
- Flow direction is implied by way direction but not always correct.
- For hydrological modelling, supplement with DEM-derived data.
