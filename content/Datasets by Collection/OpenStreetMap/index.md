---
title: OpenStreetMap
draft: false
tags:
  - collection
  - osm
  - global
  - vector
---

OpenStreetMap (OSM) is a global collaborative map dataset covering roads, buildings, land use, waterways, points of interest, administrative boundaries, and more. It is available freely under the Open Database Licence (ODbL).

**Portal page:** [[Data Portals/OpenStreetMap/index|OpenStreetMap Portal]] — service types, access patterns, osmnx usage, Geofabrik downloads.

**OSM wiki Map Features:** [https://wiki.openstreetmap.org/wiki/Map_features](https://wiki.openstreetmap.org/wiki/Map_features)

---

## Coverage by Leaf

| Leaf | OSM Feature Class | Primary Tags | Geometry | Geofabrik Layer |
| --- | --- | --- | --- | --- |
| [[Leaves/buildings\|Buildings]] | Buildings | `building=*` | Polygon | `gis_osm_buildings_a_free_1` |
| [[Leaves/transport-networks\|Transport Networks]] | Roads / Railways | `highway=*`, `railway=*` | LineString | `gis_osm_roads_free_1`, `gis_osm_railways_free_1` |
| [[Leaves/administrative-units\|Administrative Units]] | Boundaries | `boundary=administrative` | Polygon (relation) | — (use Overpass/osmnx) |
| [[Leaves/freshwater-bodies\|Freshwater Bodies]] | Waterways / Water | `waterway=*`, `natural=water` | LineString, Polygon | `gis_osm_waterways_free_1`, `gis_osm_water_a_free_1` |
| [[Leaves/geographical-names\|Geographical Names]] | Places | `place=*`, `name=*` | Point | `gis_osm_places_free_1` |
| [[Leaves/nature-protection-areas\|Nature Protection Areas]] | Protected areas | `boundary=protected_area` | Polygon | — (use Overpass) |
| [[Leaves/forest-management\|Forest Cover]] | Natural / Land use | `landuse=forest`, `natural=wood` | Polygon | `gis_osm_landuse_a_free_1`, `gis_osm_natural_a_free_1` |
| [[Leaves/land-use-agriculture\|Land Use / Agriculture]] | Land use | `landuse=farmland`, `landuse=meadow` | Polygon | `gis_osm_landuse_a_free_1` |
| [[Leaves/business-locations\|Business Locations]] | POIs | `amenity=*`, `shop=*`, `office=*` | Point, Polygon | `gis_osm_pois_free_1` |
| [[Leaves/energy-infrastructure\|Energy Infrastructure]] | Power | `power=*` | Point, LineString | — (use Overpass) |
| [[Leaves/habitat-extent\|Habitat Extent]] | Natural areas | `natural=wetland`, `natural=heath` | Polygon | `gis_osm_natural_a_free_1` |
| [[Leaves/population\|Population / Settlements]] | Places | `place=city\|town\|village\|hamlet` | Point | `gis_osm_places_free_1` |

---

## OSM Tag Schema

OSM uses a flat key–value tagging system. Key references:

- **Map Features wiki:** [https://wiki.openstreetmap.org/wiki/Map_features](https://wiki.openstreetmap.org/wiki/Map_features) — master tag index
- **TagInfo:** [https://taginfo.openstreetmap.org](https://taginfo.openstreetmap.org) — tag usage statistics globally
- **Overpass Turbo:** [https://overpass-turbo.eu](https://overpass-turbo.eu) — interactive query builder and visualiser

---

## Access Methods Summary

| Method | Best For | Tool |
| --- | --- | --- |
| Geofabrik `.shp.zip` | Bulk regional extract, offline analysis | Direct download |
| Geofabrik `.osm.pbf` | Full-fidelity extract for processing | `osmium`, `pyosmium` |
| osmnx (Overpass under hood) | Python network/feature queries | `osmnx` |
| Raw Overpass query | Low-level debugging, reproducibility | `curl`, `requests` |
| XYZ tile service | Basemap rendering | Leaflet, QGIS, MapLibre |
