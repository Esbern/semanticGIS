---
title: Classical Classifications
draft: false
tags: []
---

This section maps three widely-used geospatial metadata classification systems into the [[SPHERE]] tree. Each classical theme gets a page with its original definition, its location in the SPHERE hierarchy, and harvesting hints for discovering relevant datasets in metadata catalogs.

## Why This Mapping Exists

Classical metadata standards (ISO 19115, INSPIRE, UN-GGIM) use **flat lists** of topic categories. This works for basic catalog search but breaks down when:

- A theme spans multiple domains (e.g., "Environment" monitors *all* physical spheres)
- Themes mix abstraction levels (orthophoto imagery at the same level as land use classification)
- There is no hierarchy to navigate — you must know the keyword to find the data

The SPHERE tree provides the missing hierarchy. Each classical theme maps to a **sphere** (branch), a **subsphere** (twig), and optionally **threads** (cross-domain connections). An agent harvesting a metadata catalog can use this mapping to route datasets into the right part of the tree.

## The Three Classification Systems

| Standard | Themes | Purpose | Scope |
| --- | --- | --- | --- |
| [[Classical Classifications/ISO 19115/index\\\|ISO 19115 Topic Categories]] | 19 | General-purpose metadata keywords for any geospatial dataset | Global |
| [[Classical Classifications/INSPIRE/index\\\|INSPIRE Themes]] | 34 | Legally mandated data themes for European SDI interoperability | EU / EEA |
| [[Classical Classifications/UN-GGIM/index\\\|UN-GGIM Fundamental Themes]] | 14 | Core geospatial data themes identified by the UN for national SDIs | Global |

## Cross-Standard Concordance

Many themes appear in multiple standards. Notable equivalences:

| Concept | ISO 19115 | INSPIRE | UN-GGIM |
| --- | --- | --- | --- |
| Addresses | Location | Addresses | Addresses |
| Elevation | Elevation | Elevation | Elevation and Depth |
| Buildings | Structure | Buildings | Buildings and Settlements |
| Transport | Transportation | Transport Networks | Transport Networks |
| Land Cover/Use | Imagery/BaseMaps/EarthCover | Land Cover and Use | Land Cover and Land Use |
| Population | Society | Population Distribution | Population Distribution |
| Geology | GeoscientificInformation | Geology | Geology and Soils |
| Orthoimagery | Imagery/BaseMaps/EarthCover | Orthoimagery | Orthoimagery |
| Water | InlandWaters + Oceans | Hydrography + Sea Regions | Water |
| Soil | GeoscientificInformation | Soil | Geology and Soils |

## Key Threads (Themes That Cross Spheres)

These themes are inherently cross-domain — they are the "wind through the branches" of the SPHERE tree:

1. **Land Cover and Land Use** (all 3 standards) → Socio-Technical Perception & Thematics primary, thread to Toposphere Imagery & Evidence
2. **Natural Risk Zones** (INSPIRE) → Physical hazards (Lithosphere/Hydrosphere) + human vulnerability (Socio-Technical)
3. **Environment / Environmental Monitoring** (ISO + INSPIRE) → Monitoring infrastructure (Socio-Technical) observing across all physical spheres
4. **Planning/Cadastre / Area Management** (ISO + INSPIRE) → Human governance intent wrapped around physical space
5. **Farming / Agriculture** (ISO + INSPIRE) → Resource utilisation (Socio-Technical) + Biosphere organisms
6. **Geology and Soils** (UN-GGIM) → Lithosphere ↔ Pedosphere bridge
7. **Energy Resources** (INSPIRE) → Lithosphere resources + Socio-Technical infrastructure

---

*See [[SPHERE]] for the full protocol definition. See [[Leaves/index|Leaves]] for purpose-specific dataset entry points.*
