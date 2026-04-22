---
title: OpenStreetMap
draft: false
tags:
  - data-portal
  - osm
  - vector
  - global
---

[OpenStreetMap](https://www.openstreetmap.org/) (OSM) is a collaborative, freely editable global map. All data is available under the [Open Database Licence (ODbL)](https://opendatacommons.org/licenses/odbl/). It is the primary global source for roads, buildings, land use, waterways, points of interest, and administrative boundaries.

**OSM wiki Map Features reference:** [https://wiki.openstreetmap.org/wiki/Map_features](https://wiki.openstreetmap.org/wiki/Map_features)

OSM data is tag-based. Every feature is described by key–value pairs (e.g. `highway=residential`, `building=yes`, `amenity=school`). The Map Features page is the canonical reference for which tags exist and what they mean.

---

## Service Types

### 1. Tile Services (Raster Basemaps)

OSM provides raster map tiles via the standard XYZ/slippy map scheme. Use for basemaps in interactive web maps.

| Endpoint | Format | CRS | Auth |
| --- | --- | --- | --- |
| `https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png` | PNG raster tiles | EPSG:3857 (Web Mercator) | None |

**Usage notes:**

- Tile usage policy requires a valid `User-Agent` header and attribution: © OpenStreetMap contributors.
- For heavy production use, self-host tiles or use a tile provider (Mapbox, Stamen, CartoDB, etc.) rather than hammering the OSM tile CDN.
- In Leaflet: `L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', { attribution: '© OpenStreetMap contributors' })`

**Service family:** `wmts` (XYZ tiles)
**Auth mode:** None

---

### 2. Geofabrik Downloads (Bulk Vector Data)

[Geofabrik](https://download.geofabrik.de/) provides regularly updated OSM extract downloads by region (continent → country → sub-region). Recommended for bulk analysis of a specific area.

| Resource | URL |
| --- | --- |
| Download index | [https://download.geofabrik.de](https://download.geofabrik.de) |
| Europe index | [https://download.geofabrik.de/europe.html](https://download.geofabrik.de/europe.html) |

**Available formats:** `.osm.pbf` (recommended), `.osm.bz2`, `.shp.zip` (pre-split by feature type)

**Shapefile layers in the `.shp.zip` package:**

| Layer | Feature Type | Key OSM Tags |
| --- | --- | --- |
| `gis_osm_roads_free_1` | LineString | `highway=*` |
| `gis_osm_buildings_a_free_1` | Polygon | `building=*` |
| `gis_osm_landuse_a_free_1` | Polygon | `landuse=*` |
| `gis_osm_waterways_free_1` | LineString | `waterway=*` |
| `gis_osm_water_a_free_1` | Polygon | `natural=water`, `waterway=*` |
| `gis_osm_natural_free_1` | Point | `natural=*` |
| `gis_osm_natural_a_free_1` | Polygon | `natural=*` |
| `gis_osm_places_free_1` | Point | `place=*` |
| `gis_osm_pofw_free_1` | Point | `amenity=place_of_worship` |
| `gis_osm_pois_free_1` | Point | `amenity=*`, `shop=*`, `tourism=*` |
| `gis_osm_pois_a_free_1` | Polygon | same as above |
| `gis_osm_railways_free_1` | LineString | `railway=*` |
| `gis_osm_traffic_free_1` | Point | traffic features |
| `gis_osm_transport_free_1` | Point | public transport stops |

**CRS:** WGS84 (EPSG:4326)
**Auth mode:** None — free download
**Service family:** `filedownload`

---

### 3. Overpass API (Query-Based Feature Extraction)

The [Overpass API](https://overpass-api.de/) allows querying specific OSM features by tag, bounding box, or named area. Use for targeted feature extraction rather than bulk download.

**Recommended approach: use OSMnx and let it manage the endpoint.**

Per the project template workflow preference (`workflow-preferences.yaml: osm.preferred_fetch_library: osmnx`):

- Use `osmnx` as the default Python library for OSM queries.
- Configure caching: `ox.settings.cache_folder = ".cache/"`.
- Do not hardcode an Overpass endpoint — let osmnx choose based on its defaults.
- Use raw Overpass queries only as a fallback or for reproducible low-level debugging.

**osmnx quick reference:**

```python
import osmnx as ox
ox.settings.cache_folder = ".cache/"

# Road network
G = ox.graph_from_place("Copenhagen, Denmark", network_type="drive")

# Building footprints
buildings = ox.features_from_place("Copenhagen, Denmark", tags={"building": True})

# Administrative boundary
area = ox.geocode_to_gdf("Copenhagen Municipality, Denmark")

# Custom tag query (e.g. parks)
parks = ox.features_from_place("Copenhagen, Denmark", tags={"leisure": "park"})
```

**Direct Overpass query (fallback):**

```ql
[out:json][timeout:60];
area["name"="Copenhagen"]["admin_level"="7"]->.searchArea;
(
  way["building"](area.searchArea);
  relation["building"](area.searchArea);
);
out body; >; out skel qt;
```

**Public Overpass endpoints:**

| Endpoint | Notes |
| --- | --- |
| `https://overpass-api.de/api/interpreter` | Main public endpoint (osmnx default) |
| `https://overpass.kumi.systems/api/interpreter` | Mirror |

**Service family:** `overpass` (treat as API query)
**Auth mode:** None

---

## CRS Summary

| Context | CRS |
| --- | --- |
| Vector data (downloaded / Overpass) | EPSG:4326 (WGS84) |
| Raster tiles | EPSG:3857 (Web Mercator) |
| osmnx graph nodes | EPSG:4326 (lat/lng stored as node attributes) |

Transform to local CRS (e.g. EPSG:25832 for Denmark) using GeoPandas: `gdf.to_crs("EPSG:25832")`.

---

## Attribution

All OSM data must be attributed: **© OpenStreetMap contributors**, licensed under [ODbL](https://opendatacommons.org/licenses/odbl/). Derived databases must also be released under ODbL.

---

## Covered Leaves (semanticgis.org)

| Leaf | Primary OSM Tag(s) |
| --- | --- |
| [[Leaves/buildings\|Buildings]] | `building=*` |
| [[Leaves/transport-networks\|Transport Networks]] | `highway=*`, `railway=*`, `aeroway=*` |
| [[Leaves/administrative-units\|Administrative Units]] | `boundary=administrative` + `admin_level=*` |
| [[Leaves/freshwater-bodies\|Freshwater Bodies]] | `waterway=*`, `natural=water` |
| [[Leaves/geographical-names\|Geographical Names]] | `name=*`, `place=*` |
| [[Leaves/nature-protection-areas\|Nature Protection Areas]] | `boundary=protected_area`, `leisure=nature_reserve` |
| [[Leaves/forest-management\|Forest Cover]] | `landuse=forest`, `natural=wood` |
| [[Leaves/land-use-agriculture\|Land Use / Agriculture]] | `landuse=farmland`, `landuse=meadow`, `landuse=*` |
| [[Leaves/business-locations\|Business Locations]] | `amenity=*`, `shop=*`, `office=*` |
| [[Leaves/energy-infrastructure\|Energy Infrastructure]] | `power=*` |
| [[Leaves/habitat-extent\|Habitat Extent]] | `natural=wetland`, `natural=heath`, `natural=scrub` |
| [[Leaves/population\|Population / Settlements]] | `place=city\|town\|village\|hamlet` |
