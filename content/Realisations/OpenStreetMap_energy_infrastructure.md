---
title: "OpenStreetMap — `power=*` Realisation of Energy Infrastructure"
type: realisation
draft: false
leaf: Energy Infrastructure
dataset: OpenStreetMap
tags:
  - realisation/openstreetmap
  - leaf/energy-infrastructure
---

**Leaf:** [[Leaves/energy-infrastructure|Energy Infrastructure]]
**Dataset:** OpenStreetMap — `power=*`

OSM contains global energy-network features: plants, substations, transmission towers, and power lines.

#### osmnx access

```python
import osmnx as ox
ox.settings.cache_folder = ".cache/"

power_features = ox.features_from_place(
    "Denmark",
    tags={"power": True},
)
```

#### Key OSM tags

| Tag | Meaning |
| --- | --- |
| `power=line` | Transmission/distribution overhead line |
| `power=cable` | Underground/submarine cable |
| `power=substation` | Substation polygon or point |
| `power=plant` | Power plant area |
| `power=generator` | Single generator (wind turbine, solar, etc.) |
| `generator:source=*` | Source type (wind, solar, gas, hydro, etc.) |
