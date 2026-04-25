---
title: Bathing Water Quality
type: leaf
draft: true
sphere: Hydrosphere
subsphere: hydrosphere_freshwater_surface
concept: Bathing water suitability and public exposure risk from measured water quality
question: >-
  Is bathing water suitable and safe for human recreational use at this location
  and time?
twig_membership:
  - hydrosphere_freshwater_surface
  - hydrosphere_contaminants
  - socio_technical_contaminants
  - socio_technical_hazard_vulnerability_risk
  - socio_technical_services
primary_lens: hydrosphere_freshwater_surface
threads:
  - bathing-water-quality-hydrosphere-freshwater
  - bathing-water-quality-hydrosphere-contaminants
  - bathing-water-quality-socio-contaminants
  - bathing-water-quality-hvr
  - bathing-water-quality-services
tags:
  - hydrosphere_freshwater_surface
  - hydrosphere_contaminants
  - socio_technical_contaminants
  - socio_technical_hazard_vulnerability_risk
  - socio_technical_services
flow_mode: gauge
temporal_mmu: stream
---

> Cognised existence: a monitored bathing location with measured water quality and interpreted suitability for recreational human use.

This leaf is intentionally multi-twig. It combines hydrological context, contamination indicators, exposure interpretation, and risk communication.

## Core Question

Is bathing water suitable and safe for human recreational use at this location and time?

## Why This Leaf Is Cross-Domain

- Hydrosphere: the measured water body and station context
- Hydrosphere Contaminants: pollutant and microbiological measurements in water
- Socio-Technical Contaminants: human exposure interpretation
- Hazard Vulnerability and Risk: suitability classes and public risk signals
- Services: bathing sites as a public recreational service

## Twig Links

- [[SPHERE/Hydrosphere/Freshwater_Surface/index|Hydrosphere -> Freshwater Surface Water]]
- [[SPHERE/Hydrosphere/Contaminants/index|Hydrosphere -> Water Contaminants]]
- [[SPHERE/Socio_Technical/Contaminants/index|Socio-Technical -> Contaminants (Human Exposure)]]
- [[SPHERE/Socio_Technical/Hazard_Vulnerability_Risk/index|Socio-Technical -> Hazard, Vulnerability, and Risk]]
- [[SPHERE/Socio_Technical/Services/index|Socio-Technical -> Services]]

## Indicative Realisation

The Miljoeportalen dataset "Badevand: Analyse- og Maleresultater" is a canonical realisation for this leaf, together with station-level datasets such as control stations.

## Threads

| Thread id | Twig | Relation type | Question support |
| --- | --- | --- | --- |
| `bathing-water-quality-hydrosphere-freshwater` | `hydrosphere_freshwater_surface` | `core_water_body_context` | Which freshwater surface context does this site belong to? |
| `bathing-water-quality-hydrosphere-contaminants` | `hydrosphere_contaminants` | `water_quality_measurement` | Which contamination measurements determine suitability? |
| `bathing-water-quality-socio-contaminants` | `socio_technical_contaminants` | `human_exposure_signal` | What do measurements imply for human exposure? |
| `bathing-water-quality-hvr` | `socio_technical_hazard_vulnerability_risk` | `risk_classification_input` | Should this site be flagged for risk communication? |
| `bathing-water-quality-services` | `socio_technical_services` | `service_suitability` | Is the bathing service usable at this time? |

## Temporal Semantics

- Use sample timestamp as event time.
- Do not merge measurements across seasons without explicit temporal normalization.
- Track both observation time and publication/update time when available.

## Realised By Links

- [[Datasets by Owner/kommunerne/badevand.md|Badevand]] (owner)
- [[Datasets by Owner/kommunerne/badevand.md|Badevand]] (owner)

### Unmatched Realisations

- Badevand: Analyse- og Måleresultater
## Related Leaves

- [[Leaves/services|Services and Amenities]]
- [[Leaves/elevation|Elevation Models]]
