---

title: Geographical Names
type: leaf
draft: false
sphere: Socio_Technical
subsphere: Socio_technical_governance
concept: Named places and topographic features as spatial identifiers
question: What is the name and location of a place or topographic feature?
---

> **Cognised existence:** Geographical names are the human identifiers for places — cities, villages, mountains, rivers, regions. They are the primary keys for geocoding and the spatial anchors for most human communication about place.

**Question:** What is the name and location of a place or topographic feature?

**OSM wiki:** [https://wiki.openstreetmap.org/wiki/Key:place](https://wiki.openstreetmap.org/wiki/Key:place) | [https://wiki.openstreetmap.org/wiki/Key:name](https://wiki.openstreetmap.org/wiki/Key:name)

---

## Realisations

Instead of hardcoding implementation schemas here, SPHERE separates semantic meaning from dataset implementation. See the following realisations for how to access this data:

- **[[Realisations/OpenStreetMap_geographical_names|OpenStreetMap — `place=*`, `name=*`]]**
- **[[Realisations/Natural_Earth_geographical_names|Natural Earth — `ne_10m_populated_places`]]**

---

## Geometry Representations

| Rep ID | Source Dataset | Geometry Type | Native CRS | Suitable For | Not Suitable For |
| --- | --- | --- | --- | --- | --- |
| `names_osm_points` | OSM via Geofabrik | Point | EPSG:4326 | Geocoding, labelling, proximity search | Area-based aggregation (use admin boundary polygons instead) |
| `names_ne_10m_points` | Natural Earth 10m populated places | Point | EPSG:4326 | Global reference labelling, settlement hierarchy maps, continental-scale geocoding | Sub-national name coverage, local gazetteers |

---

## Limitations

- Population data is very sparse and not reliably maintained.
- City/town/village classification is inconsistent across countries.
- For authoritative national gazetteers, prefer official national datasets.
