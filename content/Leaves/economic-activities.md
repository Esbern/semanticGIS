---

title: Economic Activities
type: leaf
draft: true
sphere: Socio_Technical
subsphere: Socio_technical_socioeconomic
concept: Cognised classification of what economic function an enterprise performs
question: What economic activity does a business perform?
threads:
  - economic-activities-to-biosphere-ecosystems
  - economic-activities-to-perception-thematics
tags:
  - biosphere_ecosystems
  - socio_technical_perception_thematics
flow_mode: ant
temporal_mmu: episodic
---

> **Cognised existence:** An economic activity is the classified function an enterprise performs — what it *does* in the economy. This concept exists independent of any particular register: a restaurant is a restaurant whether you read it from an industry code, an OSM amenity tag, or a statistical table.

**Question:** What economic activity does a business perform?

## What is an Economic Activity?

An economic activity is not a business (that's a legal entity). It is the *type of work* performed. A single enterprise may have multiple activities (primary + secondary). The classification enables sectoral analysis, economic diversity mapping, and filtering businesses by function.

For the legal business entity behind the activity, use [[Leaves/firms|Firms]].

Different data sources encode this concept using incompatible taxonomies — business registries use industry code systems, OSM uses tag families, and statistics systems use aggregated sector classes. A leaf-level understanding lets an agent translate between them.

---

## Realisations

Instead of hardcoding implementation schemas here, SPHERE separates semantic meaning from dataset implementation. See the following realisations for how to access this data:

- **[[Realisations/CVR_CentraleVirksomhedsregister_economic_activities|CVR (CentraleVirksomhedsregister) — DB25 Industry Code]]**
- **[[Realisations/OpenStreetMap_economic_activities|OpenStreetMap — Tag Families]]**
- **[[Realisations/Danmarks_Statistik_economic_activities|Danmarks Statistik — NACE Aggregates]]**

---

## Cross-Domain Relevance (Threads)

- **Biosphere**: Industry codes signal environmental impact. Agriculture (`01xxxx`), fishing (`03xxxx`), and extraction industries directly affect ecosystems.
- **Socio-Technical Perception & Thematics**: Industry type correlates with thematic human partitioning of space. Retail clusters, industrial zones, and agricultural activities shape mapped interpretation layers.

## Classical Theme References

| Standard | Theme | Link |
| --- | --- | --- |
| INSPIRE | Production and Industrial Facilities | [[Classical Classifications/INSPIRE/production-and-industrial-facilities\\\|Production and Industrial Facilities]] |
