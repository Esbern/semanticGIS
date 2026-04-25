---

title: Services and Amenities
type: leaf
draft: true
sphere: Socio_Technical
subsphere: Socio_technical_services
concept: >-
  Cognised facilities, institutions, and amenities providing functions to the
  public
question: What services or amenities are available at or near a location?
threads: []
tags:
  - socio_technical_services
---

> **Cognised existence:** A service or amenity is a facility, institution, or establishment that provides a function to the public — healthcare, education, dining, retail, emergency response, recreation, or everyday convenience. The same concept is captured differently across datasets: as a business with an industry code, as a map point with an amenity tag, or as a building with a use code.

**Question:** What services or amenities are available at or near a location?

## What is a Service or Amenity?

A service or amenity is not a building (that's [[Leaves/buildings|Buildings]]). It is not the legal business entity behind it (that's [[Leaves/firms|Firms]]). It is the *function provided at a place*. A hospital provides healthcare. A school provides education. A restaurant provides dining. A playground provides recreation. The same physical building may house multiple services, and the same service type may appear across very different data sources.

---

## Realisations

Instead of hardcoding implementation schemas here, SPHERE separates semantic meaning from dataset implementation. See the following realisations for how to access this data:

- **[[Realisations/CVR_CentraleVirksomhedsregister_services|CVR (CentraleVirksomhedsregister) — By Industry Code]]**
- **[[Realisations/OpenStreetMap_services|OpenStreetMap — By Amenity Tag]]**
- **[[Realisations/BBR_BygningerOgBoliger_services|BBR (BygningerOgBoliger) — By Building Use Code]]**

---

## Combining Realisations

The power of multi-source realisations: CVR gives you **business attributes** (opening year, employee count, revenue). OSM gives you **direct coordinates and opening hours**. BBR gives you **physical building characteristics**. An agent assembling a complete picture of "healthcare services in Copenhagen" can draw from all three.

| Need | Best Realisation | Why |
| --- | --- | --- |
| Comprehensive business list | CVR | Most complete, authoritative |
| Quick geocoded point map | OSM | Direct geometry, no joins |
| Building characteristics of service facilities | BBR | Physical attributes (area, age, heating) |
| Combined analysis | CVR + OSM + BBR | Full picture via address-based join |

## Classical Theme References

| Standard | Theme | Link |
| --- | --- | --- |
| INSPIRE | Utility and Governmental Services | [[Classical Classifications/INSPIRE/utility-and-governmental-services\\\|Utility and Governmental Services]] |
