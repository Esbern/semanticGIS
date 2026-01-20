---
title: Establishing the Data foundation
draft: false
tags:
aliases:
  - Establishing the Data foundation
order: "3"
---
# Establishing the Data Foundation

Until this point, the GIS project has been focused on the intellectual process of ensuring a sound conceptual foundation. We now come to the practical phase where we must "grab tools and shovel bytes" to establish the physical material of our project.

## 1. The Technical Environment

**The "Project Document" vs. The Database**

Before we acquire data, we need a container. We must distinguish between the **Data Structure** (where bytes live) and the **Project Document** (where logic lives).

- **The Project Document:** In desktop GIS (QGIS, ArcGIS Pro), this is a file (`.qgz`, `.aprx`) that stores _references_ to data, styling rules, and print layouts. In Python, this is your setup script.
    
- **The Connection:** The project document establishes a named connection between the processing environment and the physical data. It does _not_ contain the data itself.
    

> **⚠️ Stewardship Alert:** Never rely on the Project Document to store your data schema. Your data must exist in a robust format (like GeoPackage or PostGIS) independent of the software used to view it.

---

## 2. Acquiring and Creating Data

Having defined your **Domain of Discourse (DoD)** in Phase 2, you must now populate your schema. In SemanticGIS, we distinguish between three fundamental origins of data:

### A. [[Geospatial Practice/Establishing the Data Foundation/Sourcing Existing Data/index|Sourcing Existing Data]]

**The "Found" World.** You are not creating new data, but integrating data that already exists—whether it is a ready-made map layer (Geospatial Infrastructure) or a raw Excel list (Register Data).

- **Workflow:** Download, Document Provenance, and Transform (Filter/Clip/Join).
    
- **Key Task:** See [[Geospatial Practice/Establishing the Data Foundation/Sourcing Existing Data/Handling Address and Contact Data|Handling Address and Contact Data]] for a guide on cleaning tabular registers.
    

### B. [[Geospatial Practice/Establishing the Data Foundation/Sensor-Based Capture/index|Sensor-Based Capture]]

**The "Measured" World.** Data created by machines measuring physical reality. This is resource-intensive and requires strict calibration.

- **Field Data Collection:** Using GPS/GNSS or mobile apps (QField/Mergin) to record location and attributes in the field.
    
- **Remote Sensing:** Using drones, satellites, or LiDAR to capture raw sensor readings that must be processed into geometry.
    

### C. [[Geospatial Practice/Establishing the Data Foundation/Human-Led Creation/index|Human-Led Creation]]

**The "Interpreted" World.** Data created by the human mind interpreting a source.

- **Heads-up Digitizing:** The manual process of tracing features (e.g., forests, roads) from an orthophoto or historical map.
    
- **AI-Assisted Extraction:** Using algorithms to segment images, followed by human verification.
    

---

## 3. The Outcome: A Clean Database

Regardless of the path taken, this phase concludes when you have a **final, documented project database**. This database is the "frozen" state of your inputs and serves as the official starting point for **[[Geospatial Practice/Analytical Modelling/index|Phase 4: Analytical Modelling]]**.