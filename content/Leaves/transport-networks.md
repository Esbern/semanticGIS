---
title: Transport Infrastructure Networks
type: leaf
draft: false
sphere: Socio_Technical
subsphere: Socio_technical_infrastructure
concept: Road, rail, and other transport corridors including routing geometry and access classification
question: What transport networks exist at a location and how are they classified?
realisations:
  - OpenStreetMap
  - Natural Earth
threads: []
tags:
  - socio_technical_infrastructure
  - transport
  - connectivity
primary_collection: OpenStreetMap
services: {}
---

> **Cognised existence:** Transport networks are the physical corridors along which people and goods move. Their geometry and classification determine routing, accessibility analysis, and connectivity modelling.

**Question:** What transport networks exist at a location and how are they classified?

**OSM wiki:** [https://wiki.openstreetmap.org/wiki/Key:highway](https://wiki.openstreetmap.org/wiki/Key:highway) | [https://wiki.openstreetmap.org/wiki/Key:railway](https://wiki.openstreetmap.org/wiki/Key:railway)

---

## Realisations

### OpenStreetMap — `highway=*`, `railway=*`, `aeroway=*`

OSM is the primary global open source for road and transport network geometry. It is the standard input for routing and network analysis via osmnx.

#### osmnx access (recommended)

osmnx builds a routable NetworkX graph from OSM transport data, handling topology, directionality, and simplification automatically.

```python
import osmnx as ox
ox.settings.cache_folder = ".cache/"

# Drive network
G_drive = ox.graph_from_place("Copenhagen, Denmark", network_type="drive")

# Walk network
G_walk = ox.graph_from_place("Copenhagen, Denmark", network_type="walk")

# Cycle network
G_bike = ox.graph_from_place("Copenhagen, Denmark", network_type="bike")

# Convert graph to GeoDataFrame for inspection
nodes, edges = ox.graph_to_gdfs(G_drive)
```

**`network_type` values:** `drive`, `walk`, `bike`, `all`, `all_private`

#### Geofabrik layers

| Layer | Content |
| --- | --- |
| `gis_osm_roads_free_1.shp` | All roads + paths, LineString, field `fclass` for type |
| `gis_osm_railways_free_1.shp` | Rail lines, LineString |
| `gis_osm_transport_free_1.shp` | Public transport stop points |

#### Key OSM tags

| Tag | Meaning |
| --- | --- |
| `highway=motorway` | Motorway / freeway |
| `highway=trunk` | Major non-motorway road |
| `highway=primary` | Primary road |
| `highway=secondary` | Secondary road |
| `highway=residential` | Residential street |
| `highway=cycleway` | Dedicated cycle path |
| `highway=footway` | Footpath |
| `railway=rail` | Main line railway |
| `railway=subway` | Urban metro |
| `oneway=yes` | Directed edge |
| `maxspeed=*` | Speed limit (sparse — verify before use) |

---

### Natural Earth — roads, railroads, airports, ports

Natural Earth provides small-to-medium scale transport infrastructure layers covering the entire globe. These are suitable for continental overview mapping and context layers, not for routing or sub-national analysis.

**Download:** [https://www.naturalearthdata.com/downloads/](https://www.naturalearthdata.com/downloads/) → Cultural

| Layer | Scale | Geometry | Content |
| --- | --- | --- | --- |
| `ne_10m_roads` | 1:10m | LineString | Major roads globally, field `type` (Major Highway, Secondary Highway, etc.) |
| `ne_50m_roads` | 1:50m | LineString | Generalised road network |
| `ne_10m_railroads` | 1:10m | LineString | Main line rail, field `type` (Rail, Ferry) |
| `ne_10m_airports` | 1:10m | Point | Major civilian airports, field `iata_code`, `name`, `scalerank` |
| `ne_10m_ports` | 1:10m | Point | Major seaports, field `name`, `website`, `scalerank` |

#### Python load

```python
import geopandas as gpd

roads      = gpd.read_file("ne_10m_roads.zip")
railroads  = gpd.read_file("ne_10m_railroads.zip")
airports   = gpd.read_file("ne_10m_airports.zip")
ports      = gpd.read_file("ne_10m_ports.zip")

# Filter to major airports only (scalerank 0–2 are the largest)
major_airports = airports[airports["scalerank"] <= 2]
major_ports    = ports[ports["scalerank"] <= 2]
```

**Important:** Natural Earth transport layers are context reference data. Do not use them for routing — they carry no topology. For routing, use OSM via osmnx.

---

## Geometry Representations

| Rep ID | Source Dataset | Geometry Type | Native CRS | Suitable For | Not Suitable For |
| --- | --- | --- | --- | --- | --- |
| `transport_osm_graph` | OSM via osmnx | NetworkX graph (LineString edges) | EPSG:4326 | Routing, isochrones, accessibility, network analysis | Simple visual mapping without topology |
| `transport_osm_lines` | OSM via Geofabrik | LineString | EPSG:4326 | Visual mapping, length statistics, buffer analysis | Turn-by-turn routing without topology processing |
| `transport_ne_10m_roads` | Natural Earth 10m | LineString | EPSG:4326 | Continental overview mapping, context layer | Routing, sub-national road analysis |
| `transport_ne_10m_railroads` | Natural Earth 10m | LineString | EPSG:4326 | Continental overview mapping, rail context | Routing, detailed rail network analysis |
| `transport_ne_10m_airports` | Natural Earth 10m | Point | EPSG:4326 | Airport location mapping, index of major airports | Airport capacity, traffic, or operational data |
| `transport_ne_10m_ports` | Natural Earth 10m | Point | EPSG:4326 | Port location mapping, index of major seaports | Port throughput or vessel traffic intensity |

**Important:** Select `transport_osm_graph` (osmnx) for any routing or accessibility analysis. Raw line features do not carry topological connectivity.

---

## Limitations

- Speed limits (`maxspeed`) are inconsistently tagged in OSM — validate before use in routing models.
- Turn restrictions exist in OSM but require explicit processing.
- Natural Earth transport layers cover only major infrastructure and are not suitable for local or sub-national analysis.
- For legally authoritative road classification, prefer national datasets.

## Realised By Links

- [[Datasets by Collection/OpenStreetMap/index|OpenStreetMap]] (collection)
- [[Datasets by Collection/Natural Earth/index|Natural Earth]] (collection)
- [[Datasets by Owner/Natural Earth/index|Natural Earth]] (owner)
