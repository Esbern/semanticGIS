---
title: Toposphere
draft: true
tags:

  - toposphere

aliases:

  - toposphere

---

- **Description:** This sphere describes the **geometric and physical properties of the Earth's solid and liquid surfaces**, serving as the **primary interface** where the atmosphere, hydrosphere, pedosphere, lithosphere, and biosphere interact. It focuses on the surface itself, including its raw observable characteristics and high-resolution visual representations.
- **Subclasses (Complexes):**
  - [[SPHERE/Toposphere/CRS/index|toposphere_geospatial_reference_framework]]: The mathematical and legal substrate of the SPHERE Protocol — coordinate reference systems (CRS) that allow all delineations to be placed accurately in 2D/3D/4D space. Each CRS (e.g., EPSG:25832) is treated as a Leaf and is mandated by a responsible authority in Governance.
  - [[SPHERE/Toposphere/Topography/index|toposphere_topography_bathymetry]]: Data related to the shape and elevation of the Earth's land surface and ocean/lake floors (e.g., Digital surface Models (DSM's), Digital Terrain Models (DTM's), bathymetry charts, derived slope, aspect, and curvature maps, geomorphological features).
  - [[SPHERE/Toposphere/Surface_Radiative_Thermal/index|toposphere_surface_radiative_thermal]]: Data describing the energy exchange properties of the Earth's surface (e.g., Albedo (surface reflectivity), Land Surface Temperature (LST), Sea Surface Temperature (SST), surface emissivity, surface net radiation).
  - [[SPHERE/Toposphere/Surface_Physical/index|toposphere_surface_physical]]: Other physical characteristics of the surface that influence interactions (e.g., surface roughness (aerodynamic or hydrological), aerodynamic resistance, surface infiltration capacity _as an interface property_).
  - [[SPHERE/Toposphere/RS/index|toposphere_remote_sensed_observations]]: Raw or processed aerial/satellite photography and other image-based products that serve as direct remote-sensed evidence of the Earth's surface (e.g., raw satellite bands, orthophotos, imagery mosaics, and visual basemaps).
- **Common Overlaps & Distinctions:**
  - **The Ultimate Interface:** This sphere is defined by being the boundary. Its properties influence all other spheres.
  - **Evidence vs. Interpretation:** [[SPHERE/Toposphere/RS/index|toposphere_remote_sensed_observations]] stores raw evidence, while thematic human interpretation belongs to `socio_technical_perception_thematics`.
  - **Terrain vs. Geology/Soil:** [[SPHERE/Toposphere/Topography/index|toposphere_topography_bathymetry]] describes the _shape_ of the land, distinct from the _geological composition_ (`Lithosphere`) or _soil properties_ (`Pedosphere`).
  - **Surface Temperature vs. Air/Water Temp:** [[SPHERE/Toposphere/Surface_Radiative_Thermal/index|toposphere_surface_radiative_thermal]] holds the temperature of the _surface_, distinct from air temperature (`atmosphere_weather`) or water body temperature (`Hydrosphere`).

---

---

## Leaves

| Leaf | Question | Subsphere |
| --- | --- | --- |
| [[Leaves/elevation\\\|Elevation Models]] | What is the elevation at a given location? | toposphere_topography_bathymetry |
| [[Leaves/orthoimagery\\|Orthoimagery]] | What does the Earth's surface look like? | toposphere_remote_sensed_observations |
| CRS Leaves | Which coordinate system frames this dataset? | toposphere_geospatial_reference_framework |

## Cross-Domain Leaves (Threads)

These [[Leaves/index|leaves]] belong to other spheres but connect here via [[SPHERE]] threads:

| Leaf | Primary sphere | Why it connects here |
| --- | --- | --- |
| [[Leaves/business-locations\\\|Business Locations]] | Socio-Technical | Business locations relate to terrain and elevation context (e.g., flood-exposure analysis for operational sites) |
