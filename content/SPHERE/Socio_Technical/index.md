---
title: Socio-Technical
draft: false
tags:

  - socio-technical

---

**Description:** This sphere encompasses the human-created systems and organisational structures that shape environments and human activities. It includes infrastructure, services, socioeconomic patterns, governance, digital and movement flows, thematic human perception, informal systems, the quantification of human resource utilisation, and human-centric risk.
**Subclasses (Complexes):**

- **[[SPHERE/Socio_Technical/Infrastructure/index|Socio_technical_infrastructure]]:** Physical and organisational networks enabling urban and rural functions (e.g., transportation networks, utility grids, built environment as infrastructure, water/wastewater/stormwater infrastructure, waste management facilities).
- **[[SPHERE/Socio_Technical/Services/index|Socio_technical_services]]**: Organised activities and institutions providing essential functions (e.g., healthcare, education, public safety, commercial services, water supply/wastewater treatment services, energy generation/distribution).
- **[[SPHERE/Socio_Technical/Socioeconomic/index|Socio_technical_socioeconomic]]**: Data on human populations, their activities, and organization (e.g., demographics, economy, land ownership, consumption patterns, general human population distribution, workforce data, GDP, income levels).
- **[[SPHERE/Socio_Technical/Governance/index|Socio_technical_governance]]**: Administrative boundaries (municipalities, regions, nations), cadastral parcels, addresses, zoning maps, planning maps, national park boundaries, protected areas, political divisions, environmental regulations, resource permits, fishing quotas, Statistical Units (e.g., Census Tracts, Enumeration Areas), and Algorithmic generated Grids (e.g., DGGS indices like H3, S2, DGGAL).
- **[[SPHERE/Socio_Technical/ICT/index|socio_technical_ict_flows]]**: Information and communication technologies and flow traces (e.g., sensor streams, digital platforms, communication infrastructure, movement telemetry).
- **[[SPHERE/Socio_Technical/Perception_Thematics/index|socio_technical_perception_thematics]]**: Human thematic partitioning and cognitive map products (e.g., topographic/thematic maps, zoning interpretation layers, subjective classification views).
- **[[SPHERE/Socio_Technical/Informal_Ephemeral/index|socio_technical_informal_ephemeral]]**: Informal, tactical, and short-lived human systems not consistently registered in formal cadastres or registries.
- **[[SPHERE/Socio_Technical/Contaminants/index|Socio_technical_contaminants]]**: Data related to human-generated sources or pathways of contamination, or human exposure to contaminants and human health impacts (e.g., industrial emission points, hazardous waste sites, pollution regulations, spatial distribution of human disease cases/outbreaks, human exposure assessment data).
- **[[SPHERE/Socio_Technical/Hazard_Vulnerability_Risk/index|Socio_technical_hazard_vulnerability_risk]]**: Data combining natural or anthropocentric hazards with human vulnerability and exposure, leading to comprehensive risk assessments and management strategies. This includes spatial data on population vulnerability, critical infrastructure exposure, and multi-hazard risk mapping. **Note:** This is the _risk_ to humans, not the _natural hazard_ itself.
- **[[SPHERE/Socio_Technical/Resource_Utilisation/index|Socio_technical_resource_utilisation]]**: Data on the direct physical quantification of human resource extraction, harvesting, consumption, and production from natural systems. This includes measured volumes of abstracted water, harvested biomass (e.g., fish catches, timber yields), mineral extraction quantities, and energy production from natural sources.

---

## Leaves

Leaves are purpose-specific semantic aspects of datasets. They answer one kind of question and point to the entities and attributes needed. See [[SPHERE]] for the protocol and [[Leaves/index|all leaves]].

### Socioeconomic and Organisational Leaves

| Leaf | Question | Subsphere |
| --- | --- | --- |
| [[Leaves/firms\\\|Firms]] | What firm is this, as a legal registered entity? | Socio_technical_socioeconomic |
| [[Leaves/economic-activities\\\|Economic Activities]] | What economic activity does a business perform? | Socio_technical_socioeconomic |
| [[Leaves/business-locations\\\|Business Locations]] | Where does a business physically operate? | Socio_technical_infrastructure |
| [[Leaves/corporate-ownership\\\|Ownership and Governance]] | Who owns, controls, or governs a firm? | Socio_technical_socioeconomic |
| [[Leaves/business-financials\\\|Economics and Employment]] | What are the economic and employment characteristics of a firm or establishment? | Socio_technical_socioeconomic |

### Governance, Infrastructure and Services Leaves

| Leaf | Question | Subsphere |
| --- | --- | --- |
| [[Leaves/addresses\\\|Addresses]] | Where is a property located by its official address? | Socio_technical_governance |
| [[Leaves/buildings\\\|Buildings and Housing]] | What buildings exist at a location? | Socio_technical_infrastructure |
| [[Leaves/administrative-units\\\|Administrative Units]] | Which administrative area does a location belong to? | Socio_technical_governance |
| [[Leaves/cadastral-parcels\\\|Cadastral Parcels]] | What are the legal boundaries of land? | Socio_technical_governance |
| [[Leaves/geographical-names\\\|Geographical Names]] | What is the official name of a place? | Socio_technical_governance |
| [[Leaves/populated-areas\\\|Populated Areas and Settlements]] | Where are villages, towns, and cities, and what is their hierarchy? | Socio_technical_socioeconomic |
| [[Leaves/population\\\|Population (Demography)]] | What is the population count, density, and demographic profile in this area? | Socio_technical_socioeconomic |
| [[Leaves/transport-networks\\\|Transport Networks]] | What transport routes and networks exist? | Socio_technical_infrastructure |
| [[Leaves/services\\\|Services and Amenities]] | What services or amenities are available at or near a location? | Socio_technical_services |
