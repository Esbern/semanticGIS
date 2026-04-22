---
tags:

  - hydrosphere

---

- **Description:** This sphere includes all of Earth's water, whether in liquid, solid (ice), or gaseous (water vapor) form, focusing on the water body or phenomenon itself.
- **Subclasses (Complexes):**
  - [[SPHERE/Hydrosphere/Freshwater_Surface/index|hydrosphere_freshwater_surface]]: Data related to freshwater bodies on the Earth's surface (e.g., rivers, lakes, ponds, wetlands, estuaries, streamflow, lake levels).
  - [[SPHERE/Hydrosphere/Groundwater/index|hydrosphere_groundwater]]: Information about water found beneath the Earth's surface in soil pores and fractures (e.g., groundwater levels, aquifer characteristics, groundwater flow).
  - [[SPHERE/Hydrosphere/Marine/index|hydrosphere_marine]]: Data related to oceans, seas, and coastal waters (e.g., sea surface temperature (water mass), ocean currents, salinity, marine water column temperature, tides, waves, bathymetry of water column).
  - [[SPHERE/Hydrosphere/Cryosphere/index|hydrosphere_cryosphere]]: Data related to frozen water bodies (e.g., glaciers, ice sheets, sea ice extent and thickness, permafrost distribution).
  - [[SPHERE/Hydrosphere/Atmospheric_Water/index|hydrosphere_atmosphericwater]]: Information about water in the atmosphere (e.g., precipitation totals, humidity, cloud properties, water vapor content).
  - [[SPHERE/Hydrosphere/Contaminants/index|hydrosphere_contaminants]]: Data related to the presence and distribution of pollutants within water bodies (e.g., water quality measurements for specific pollutants, chemical spills in rivers or oceans, microplastic concentrations in water).
- **Common Overlaps & Distinctions:**
  - **Ice/Snow as Surface Interpretation:** While [[SPHERE/Hydrosphere/Cryosphere/index|hydrosphere_cryosphere]] describes the physical properties of ice bodies, interpreted thematic surface partitioning belongs in [[SPHERE/Socio_Technical/Perception_Thematics/index|socio_technical_perception_thematics]].
  - **Water Utilization:** Data on the _amount of water extracted or used_ (e.g., cubic meters of water abstracted) is in `socio_technical_resource_utilization`.
  - **Flooding/Tsunamis:** The _hazard itself_ (e.g., flood extent maps, tsunami wave height) belongs here. The _risk to human assets/populations_ is in `socio_technical_hazard_vulnerability_risk`.
  - **Life in Water:** The water body is `Hydrosphere`, but the fish and other aquatic organisms are `biosphere_fauna`.
