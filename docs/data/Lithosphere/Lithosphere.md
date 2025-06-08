- **Description:** This sphere encompasses the Earth's solid, rocky outer part, including the crust and upper mantle. It deals with the physical structure, composition, and processes of the Earth's bedrock geology and subsurface geological features.
- **Subclasses (Complexes):**
    - `lithosphere_geology`: Information about the rocks, minerals, and geological formations (e.g., geological maps of bedrock, borehole data, subsurface stratigraphy, structural geology, geochemistry of bedrock).
    - `lithosphere_tectonics`: Data related to crustal movements, earthquakes, and volcanic activity (e.g., fault lines, seismic activity maps, volcanic hazard zones, plate boundaries).
    - `lithosphere_resources`: Data concerning geological resources (e.g., mineral deposits, fossil fuel reserves, geothermal energy potential locations).
    - `lithosphere_hazards`: Data specifically on lithospheric hazards (e.g., landslide susceptibility, ground stability, sinkhole locations, fault rupture zones).
    - `lithosphere_contaminants`: Data related to geological materials or processes that naturally contain pollutants or act as pollution sources within the lithosphere (e.g., naturally occurring heavy metals in rock formations, radon mapping, contaminated bedrock).
- **Common Overlaps & Distinctions:**
    - **Terrain/Topography:** While shaped by geological processes, the explicit geometric description of the surface (elevation, slope) is in `toposphere_topography`.
    - **Soil:** The bedrock (Lithosphere) is often the parent material for soil (`Pedosphere`), but the soil layer itself is distinct.
    - **Resource Extraction:** The _natural occurrence_ of minerals/fuels is `lithosphere_resources`, but the _quantity extracted_ is `socio_technical_resource_utilization`.
    - **Natural Hazards:** The _hazard itself_ (e.g., an earthquake epicenter) is here, but the _risk to human populations/assets_ is in `socio_technical_hazard_vulnerability_risk`.


