---
title: Geographical Names
type: leaf
draft: true
sphere: Socio_Technical
subsphere: Socio_technical_governance
concept: Cognised place identifiers enabling natural-language geographic reference
question: What is the official name of a place or feature?
realisations: []
threads: []
tags: []
primary_collection:
primary_collection_path: /Datasets-by-Collection/Grunddatamodellen/Stednavne/
entities: []
key_attributes: []
services: {}
---

> **Cognised existence:** A geographical name is a human-assigned label for a location or feature — a city, an island, a forest, a lake. Names are how humans refer to places in natural language, making them essential for search and discovery.

**Question:** What is the official name of a place or feature?

---

## Realisations

### 1. Stednavne

[[Datasets by Collection/Grunddatamodellen/Stednavne/index|Stednavne]] is the authoritative Danish gazetteer.

#### Spatial Access Path

```
stednavn → geometri (point or polygon — direct, no joins needed)
```

Each place name carries its own geometry directly — a point for small features, a polygon for areas.

#### Key Attributes

| Attribute | Description |
| --- | --- |
| `navn` | Place name text |
| `stednavntype` | Feature type (by, ø, skov, sø, å, ...) |
| `geometri` | Point or polygon geometry |
| `sprog` | Language (Danish, Greenlandic) |

### 2. OpenStreetMap

OSM carries `name` tags on all named features (places, natural features, administrative areas).

**Spatial access**: Direct geometry on the named node/way/relation.

---

## Role in Data Discovery

A gazetteer enables **natural-language geographic search** — "find data near Roskilde" requires resolving "Roskilde" to coordinates. This leaf is a bridge from human queries to spatial operations.

## Classical Theme References

| Standard | Theme | Link |
| --- | --- | --- |
| INSPIRE | Geographical Names | [[Classical Classifications/INSPIRE/geographical-names\\\|Geographical Names]] |
| UN-GGIM | Geographical Names | [[Classical Classifications/UN-GGIM/geographical-names\\\|Geographical Names]] |

## Realised By Links

- [[Datasets by Collection/Grunddatamodellen/Stednavne/index.md|Stednavne]] (collection)

### Unmatched Realisations

- OpenStreetMap
## Realised By Links

- [[Datasets by Collection/Grunddatamodellen/Stednavne/index.md|Stednavne]] (collection)

### Unmatched Realisations

- OpenStreetMap
