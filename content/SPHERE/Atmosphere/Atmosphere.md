---
tags:

  - atmosphere

---

**Description:** This sphere is the gaseous envelope surrounding the Earth, encompassing its composition, dynamics, and energy exchanges. It drives weather patterns and influences climate.

- **Subclasses (Complexes):**
  - [[SPHERE/Atmosphere/Climate/index|atmosphere_climate]]: Long-term weather patterns and trends (e.g., temperature projections, historical climate data, climate zones, greenhouse gas concentrations affecting climate).
  - [[SPHERE/Atmosphere/Weather/index|atmosphere_weather]]: Short-term atmospheric conditions and phenomena (e.g., temperature, precipitation, wind speed, atmospheric pressure, forecasts, severe weather events like storms and hurricanes).
  - [[SPHERE/Atmosphere/Composition/index|atmosphere_composition]]: Data related to the general gaseous and particulate composition of the air (e.g., major atmospheric gases, aerosols, background trace gases not considered pollutants).
  - [[SPHERE/Atmosphere/Contaminants/index|atmosphere_contaminants]]: Data related to the presence and distribution of pollutants in the atmosphere (e.g., NO2 levels, particulate matter (PM2.5), ozone-depleting substances, industrial emissions, air quality indices).
- **Common Overlaps & Distinctions:**
  - **Precipitation:** While precipitation originates in the atmosphere, actual rainfall/snowfall data that interacts with the ground or water bodies is typically found under [[SPHERE/Hydrosphere/Atmospheric_Water/index|hydrosphere_atmosphericwater]].
  - **Surface Temperature:** Air temperature is [[SPHERE/Atmosphere/Weather/index|atmosphere_weather]], but the temperature of the land or sea _surface_ is [[SPHERE/Toposphere/Surface_Radiative_Thermal/index|toposphere_surface_radiative_thermal]].
  - **Climate Change:** The _causes_ (GHG emissions from human activity) are `socio_technical_contaminants` or `socio_technical_resource_utilization`. The _atmospheric manifestations_ (temperature trends, changes in weather patterns) are [[SPHERE/Atmosphere/Climate/index|atmosphere_climate]]. The _impacts_ can span all other spheres.
