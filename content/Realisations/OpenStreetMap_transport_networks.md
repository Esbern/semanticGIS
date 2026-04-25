---
title: "OpenStreetMap — `highway=*`, `railway=*`, `aeroway=*` Realisation of Transport Infrastructure Networks"
type: realisation
draft: false
leaf: Transport Infrastructure Networks
dataset: OpenStreetMap
tags:
  - realisation/openstreetmap
  - leaf/transport-networks
---

**Leaf:** [[Leaves/transport-networks|Transport Infrastructure Networks]]
**Dataset:** OpenStreetMap — `highway=*`, `railway=*`, `aeroway=*`

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
