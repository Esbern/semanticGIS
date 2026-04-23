---
title: Leaves
draft: true
tags: []
---

A **leaf** is a **cognised existence** — an abstract concept that exists independently of any particular dataset. Classically, GIS might call these "feature classes", but that is too simplistic. A cognised existence names what something *is* (an address, a building, a service), then describes how it is *realised* by one or more datasets — including the spatial access paths (join chains) needed to reach geometry.

Leaves are the finest-grained navigable unit in the [[SPHERE]] protocol.

## Why Leaves?

The same concept often spans multiple datasets. "Services" can be realised through CVR (filtering on branchekode), OpenStreetMap (amenity tags), or BBR (building use codes). A leaf isolates the concept and maps it to *all* its realisations with the specific entities, join chains, and coordinate representations each provides.

## How to Read a Leaf

Each leaf tells you:

| Section | What it provides |
| --- | --- |
| **Concept** | What this cognised existence *is* — its nature and significance |
| **Question** | What kind of question this leaf answers |
| **Sphere / Subsphere** | Where this concept fits thematically in the SPHERE tree |
| **Realisations** | Which datasets implement this concept |
| **Spatial Access Path** | The join chain from concept to geometry (per realisation) |
| **Alternative Representations** | Different coordinate types for different use cases |
| **Threads** | Other spheres where this concept is also relevant |

## All Cognised Existence Leaves

Every leaf represents a cognised existence — an abstract concept realised by one or more datasets. Each documents the spatial access paths (join chains to geometry) per realisation:

| Leaf | Question it answers | Realisations |
| --- | --- | --- |
| [[Leaves/addresses\\\|Addresses]] | Where is a property located by its official address? | DAR, OSM |
| [[Leaves/buildings\\\|Buildings]] | What buildings exist at a location? | BBR, GeoDanmark, OSM |
| [[Leaves/administrative-units\\\|Administrative Units]] | Which administrative area does a location belong to? | DAGI, OSM |
| [[Leaves/cadastral-parcels\\\|Cadastral Parcels]] | What are the legal boundaries of land? | Matrikel, EJF |
| [[Leaves/geographical-names\\\|Geographical Names]] | What is the official name of a place? | Stednavne, OSM |
| [[Leaves/elevation\\\|Elevation]] | What is the elevation at a given location? | DHM |
| [[Leaves/coastline\\\|Coastline]] | Where is the land-sea boundary and what is its large-scale geometry? | Natural Earth |
| [[Leaves/orthoimagery\\\|Orthoimagery]] | What does the Earth's surface look like? | GeoDanmark, Copernicus |
| [[Leaves/populated-areas\\\|Populated Areas and Settlements]] | Where are villages, towns, and cities, and what is their hierarchy? | OSM, Natural Earth |
| [[Leaves/population\\\|Population]] | What is the population count, density, and demographic profile in this area? | Census grids, GEOSTAT, GHSL, WorldPop |
| [[Leaves/transport-networks\\\|Transport Networks]] | What transport routes and networks exist? | GeoDanmark, OSM |
| [[Leaves/services\\\|Services and Amenities]] | What services or amenities are available at or near a location? | CVR, OSM, BBR |
| [[Leaves/bathing-water-quality\\\|Bathing Water Quality]] | Is bathing water suitable and safe for human recreational use at this location and time? | Badevand analyse, kontrolstation, and stamdata datasets |
| [[Leaves/freshwater-bodies\\\|Surface Freshwater Bodies]] | Which river, lake, wetland, or catchment is this location part of? | VP3 freshwater delimitation and hydrography datasets |
| [[Leaves/flood-hazard-inundation\\\|Flood Hazard and Inundation]] | Which areas are exposed to flooding or inundation here, and under what scenario or return period? | Coastal inundation and flood directive datasets |
| [[Leaves/groundwater-bodies\\\|Groundwater Bodies]] | Which groundwater body or aquifer is present here, and what status applies? | VP3 groundwater delimitation datasets |
| [[Leaves/groundwater-chemistry\\\|Groundwater Chemistry]] | What is the chemical status of groundwater in this area, and which substances drive trends or exceedances? | VP3 substance-specific groundwater chemistry and trends datasets |
| [[Leaves/marine-waters\\\|Marine and Coastal Waters]] | Which coastal or marine water body is this location part of, and what condition applies? | VP3 kystvande and marine ecology datasets |
| [[Leaves/aquaculture-sites\\\|Aquaculture Sites]] | Where are aquaculture activities located, and what production or discharge characteristics are reported there? | Akvakultur and akvakulturanlæg datasets |
| [[Leaves/species-observations\\\|Species Observations]] | Which species have been observed at this location, and when were they recorded? | Arter.dk and Naturdatabasen observation datasets |
| [[Leaves/habitat-extent\\\|Habitat Extent]] | Which habitat and nature-type areas are mapped at this location? | Naturdatabasen, Biodiversitetskortet, and marine habitat extent datasets |
| [[Leaves/habitat-condition\\\|Habitat Condition]] | What ecological condition or quality is reported for the habitat at this location? | Naturtilstand and biodiversity condition indicator datasets |
| [[Leaves/nature-protection-areas\\\|Nature Protection Areas]] | Which nature protection designations or restrictions apply at this location? | Protected nature, watercourse, and protection-line datasets |
| [[Leaves/land-use-agriculture\\\|Land Use and Agriculture]] | How is this area used agriculturally, and which land-use restrictions or management classes apply? | Land-use and agricultural management datasets |
| [[Leaves/fisheries-intensity\\\|Fisheries Intensity]] | What fishing effort and gear activity occur in this marine area, and how does it relate to ecosystem pressure and regulation? | VP3 and NP3 fisheries effort datasets |
| [[Leaves/nautical-traffic\\\|Nautical Traffic]] | What vessel traffic patterns are present here, and how intense is maritime movement over time? | Maritime traffic intensity and harbor traffic datasets |
| [[Leaves/energy-infrastructure\\\|Energy Infrastructure]] | Which energy infrastructures are present here, and what operational or planning constraints apply to them? | Wind, solar, electricity transmission, and gas infrastructure datasets |
| [[Leaves/planning-zoning-decisions\\\|Planning and Zoning Decisions]] | Which planning or zoning decisions apply here, and what constraints do they impose? | Fingerplan and landzone planning datasets |
| [[Leaves/spill-pollution-incidents\\\|Spill and Pollution Incidents]] | Which spill, contamination, or hazardous discharge signals are reported for this area? | Marine hazard and pollution indicator datasets |
| [[Leaves/coastal-erosion-risk\\\|Coastal Erosion Risk]] | Where is coastal erosion risk highest, and how severe is the expected shoreline impact? | Coastal erosion and shoreline protection datasets |
| [[Leaves/hydrological-basin-delineations\\\|Hydrological Basin Delineations]] | Which basin or sub-basin does this location belong to in water-management planning? | VP3 basin and coastal catchment delineation datasets |
| [[Leaves/surface-flow-systems\\\|Surface Flow Systems]] | How does water move and accumulate on the surface here, including depressions, flooding, and catchment context? | Bluespot, flooding, and catchment delineation datasets |
| [[Leaves/biodiversity-priority-indicators\\\|Biodiversity Priority Indicators]] | How is this area prioritized for biodiversity action, and which indicators drive that priority? | Biodiversitetskortet prioritization and pressure indicator datasets |
| [[Leaves/species-conservation-concern\\\|Species of Conservation Concern]] | Which protected or conservation-priority species are documented here? | Habitat directive and conservation-species datasets |
| [[Leaves/marine-spatial-infrastructure\\\|Marine Spatial Infrastructure]] | Which marine installations or constrained-use structures are present in this sea area? | Sea-territory installation and marine constraints datasets |
| [[Leaves/protected-water-use-zones\\\|Protected Water Use Zones]] | Which protected-use water zones apply here, and what protection objective do they represent? | Drinking-water and shellfish protected-zone datasets |
| [[Leaves/subsurface-freshwater\\\|Subsurface Freshwater]] | What do boreholes reveal about subsurface freshwater chemistry and aquifer behavior here? | Borehole and groundwater chemistry datasets |
| [[Leaves/soil-properties\\\|Soil Properties]] | What soil types and near-surface soil properties characterize this area? | Soil type and texture mapping datasets |
| [[Leaves/geological-strata\\\|Geological Strata]] | Which geological strata and subsurface structures are present here, and how do they frame subsurface interpretation? | Geological strata and subsurface structure datasets |
| [[Leaves/atmospheric-deposition-emissions\\\|Atmospheric Deposition and Emissions]] | What atmospheric emissions and deposition loads are modeled for this area? | Gridded atmospheric deposition and emission datasets |
| [[Leaves/firms\\\|Firms]] | What firm is this, as a legal registered entity? | CVR |
| [[Leaves/economic-activities\\\|Economic Activities]] | What economic activity does a business perform? | CVR, OSM, DST |
| [[Leaves/business-locations\\\|Business Locations]] | Where does a business physically operate? | CVR, OSM, BBR |
| [[Leaves/corporate-ownership\\\|Ownership and Governance]] | Who owns, controls, or governs a firm? | CVR |
| [[Leaves/business-financials\\\|Economics and Employment]] | What are the economic and employment characteristics of a firm or establishment? | CVR, DST || [[Leaves/property-valuation\\\|Property Valuation]] | What is the official assessed value of a property? | Ejendomsvurdering, Matrikel |
| [[Leaves/geodetic-control-points\\\|Geodetic Control Points]] | Where are the geodetic control points, and what coordinates and accuracy do they define? | Fikspunkter |
| [[Leaves/historical-map-sheets\\\|Historical Map Sheets]] | Which historical map sheet covers this location, and what cartographic source does it represent? | HistoriskeKortbladsinddelinger |

### Toposphere

- [[Leaves/elevation|Elevation Models]]
- [[Leaves/orthoimagery|Orthoimagery]]

## All Leaves by Sphere

### Socio-Technical

- [[Leaves/firms|Firms]]
- [[Leaves/economic-activities|Economic Activities]]
- [[Leaves/business-locations|Business Locations]]
- [[Leaves/corporate-ownership|Ownership and Governance]]
- [[Leaves/business-financials|Economics and Employment]]
- [[Leaves/addresses|Addresses]]
- [[Leaves/buildings|Buildings and Housing]]
- [[Leaves/administrative-units|Administrative Units]]
- [[Leaves/cadastral-parcels|Cadastral Parcels]]
- [[Leaves/geographical-names|Geographical Names]]
- [[Leaves/populated-areas|Populated Areas and Settlements]]
- [[Leaves/population|Population (Demography)]]
- [[Leaves/transport-networks|Transport Networks]]
- [[Leaves/services|Services and Amenities]]
- [[Leaves/planning-zoning-decisions|Planning and Zoning Decisions]]
- [[Leaves/marine-spatial-infrastructure|Marine Spatial Infrastructure]]
- [[Leaves/nautical-traffic|Nautical Traffic]]
- [[Leaves/energy-infrastructure|Energy Infrastructure]]
- [[Leaves/spill-pollution-incidents|Spill and Pollution Incidents]]
- [[Leaves/property-valuation|Property Valuation]]
- [[Leaves/geodetic-control-points|Geodetic Control Points]]
- [[Leaves/historical-map-sheets|Historical Map Sheets]]

### Socio-Technical Resource Utilisation

- [[Leaves/aquaculture-sites|Aquaculture Sites]]
- [[Leaves/land-use-agriculture|Agricultural Land Management]]
- [[Leaves/fisheries-intensity|Fisheries Intensity]]

### Atmosphere

- [[Leaves/atmospheric-deposition-emissions|Atmospheric Deposition and Emissions]]

### Toposphere

- [[Leaves/elevation|Elevation Models]]
- [[Leaves/orthoimagery|Orthoimagery]]

### Hydrosphere

- [[Leaves/bathing-water-quality|Bathing Water Quality]]
- [[Leaves/freshwater-bodies|Surface Freshwater Bodies]]
- [[Leaves/flood-hazard-inundation|Flood Hazard and Inundation]]
- [[Leaves/hydrological-basin-delineations|Hydrological Basin Delineations]]
- [[Leaves/surface-flow-systems|Surface Flow Systems]]
- [[Leaves/groundwater-bodies|Groundwater Bodies]]
- [[Leaves/groundwater-chemistry|Groundwater Chemistry]]
- [[Leaves/subsurface-freshwater|Subsurface Freshwater]]
- [[Leaves/marine-waters|Marine and Coastal Waters]]
- [[Leaves/protected-water-use-zones|Protected Water Use Zones]]

### Biosphere

- [[Leaves/species-observations|Species Observations]]
- [[Leaves/habitat-extent|Habitat Extent]]
- [[Leaves/habitat-condition|Habitat Condition]]
- [[Leaves/biodiversity-priority-indicators|Biodiversity Priority Indicators]]
- [[Leaves/species-conservation-concern|Species of Conservation Concern]]
- [[Leaves/nature-protection-areas|Nature Protection Areas]]

### Lithosphere

- [[Leaves/coastal-erosion-risk|Coastal Erosion Risk]]
- [[Leaves/soil-properties|Soil Properties]]
- [[Leaves/geological-strata|Geological Strata]]

---

*See [[SPHERE]] for the protocol definition and architecture.*
