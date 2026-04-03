---
title: "Design Rationale (DR-01): Copenhagen Case Study"
draft: false
tags:
---


### 0. The Wild Brief

**Source:** Copenhagen City Council, Dept. of Culture & Leisure

**Date:** 29 March 2026

**The Request:** > "We have a growing problem with noise and litter in the city centre during weekends. We need to identify 'Party Zones' so we can better coordinate our street-cleaning teams and noise-monitoring officers. We have access to the business register (CVR), but it doesn’t seem to tell the whole story. Can you provide a data-driven map of these hotspots?"._

## 1. Deconstruction Log
### 1.1 Defining Core Questions & Semantic Analysis

**The Refined Question:** _"What is the spatial intensity of nightlife activity in Copenhagen, and how does this correlate with reported urban friction (noise)?"_

**Semantic Analysis (The Intent):**
-To answer this, we must define the "Party Zone" not as a legal boundary, but as a **Vibrancy Gradient**.

- **Primary Entity:** "The Venue" (Bars, Clubs, Pubs).
    
- **Proxy Entity:** "The Friction Point" (Noise complaints).
    
- **Gateway Entity:** "The Transit Node" (Metro/Bus stops).
    

### 1.2 Epistemological Nature: Hybrid (Heuristic → Teleological)

- **Heuristic Phase (The Discovery):** We must first explore the correlation between CVR/OSM venue data and noise complaints to see if a "Party Zone" can be reliably detected.
    
- **Teleological Phase (The Prescription):** Once the detection model is validated, we will reverse-engineer a **Prescriptive Pipeline** for the Council.

### 1.3 Addressing Spatial Omission and Bias

**The "Unseen" Reality:**

- **The Register Gap:** Official business registers (CVR) miss informal socialisation. We must manually include polygons for "Public Social Space" (e.g., Islands Brygge harbour-front, Fælledparken).
    
- **The Seasonal Mask:** _Kolonihavehuse_ (allotments) and pop-up bars are "Semantic Chameleons"—their legal address rarely matches their spatial impact.
    
- **Mobile Entities:** Food trucks will be treated as "Temporal Points" rather than static venues.
    

## 2. Operational Context Log

- **2.1 Stakeholders:** City Council (Client), IT Dept (Gatekeeper), Cleaning Crews (End-User).
    
- **2.2 Tech Stack:** QGIS and VS Code/Copilot.
    
- **2.3 Data Delivery:** The Client is providing an export from the `Københavner-vink` system (public complaint forms) as a CSV with address strings.
    
- **2.4 Business Rules & Constraints:** * **NO OSM/Google:** The Client's legal department forbids the use of crowdsourced or commercial proprietary maps for official resource allocation due to liability and "Digital Sovereignty" concerns.
    
    - **Mandate:** Only official CVR and Danish SDFI (Agency for Data Supply) data may be used.
        
- **2.5 Ethics:** Data will be aggregated to a 100m grid to protect resident privacy (GDPR Compliance).
