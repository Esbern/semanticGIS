
**Description:** This sphere is the gaseous envelope surrounding the Earth, encompassing its composition, dynamics, and energy exchanges. It drives weather patterns and influences climate.
- **Subclasses (Complexes):**
    - `atmosphere_climate`: Long-term weather patterns and trends (e.g., temperature projections, historical climate data, climate zones, greenhouse gas concentrations affecting climate).
    - `atmosphere_weather`: Short-term atmospheric conditions and phenomena (e.g., temperature, precipitation, wind speed, atmospheric pressure, forecasts, severe weather events like storms and hurricanes).
    - `atmosphere_composition`: Data related to the general gaseous and particulate composition of the air (e.g., major atmospheric gases, aerosols, background trace gases not considered pollutants).
    - `atmosphere_contaminants`: Data related to the presence and distribution of pollutants in the atmosphere (e.g., NO2 levels, particulate matter (PM2.5), ozone-depleting substances, industrial emissions, air quality indices).
- **Common Overlaps & Distinctions:**
    - **Precipitation:** While precipitation originates in the atmosphere, actual rainfall/snowfall data that interacts with the ground or water bodies is typically found under `hydrosphere_atmosphericwater`.
    - **Surface Temperature:** Air temperature is `atmosphere_weather`, but the temperature of the land or sea _surface_ is `toposphere_surface_radiative_thermal`.
    - **Climate Change:** The _causes_ (GHG emissions from human activity) are `socio_technical_contaminants` or `socio_technical_resource_utilization`. The _atmospheric manifestations_ (temperature trends, changes in weather patterns) are `atmosphere_climate`. The _impacts_ can span all other spheres.