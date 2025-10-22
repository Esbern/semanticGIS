---
title: Project Scoping
draft: false
tags:
aliases:
  - Project Scoping
order: "1"
---
The first and most critical phase of any `semanticGIS` project is the **project scoping**, which produces a **Project Outline**. This document is not mere bureaucracy; it is the strategic blueprint that prevents "technical drift" and ensures every line of code we write serves a clear, agreed-upon purpose. It synthesises the project's core question with its operational realities.

---
### 1. Defining the Core Question & Deliverables

This is the "why" of the project. We start by deconstructing the client's brief to define a precise, answerable question and the tangible outputs required.

- **Deconstruct the Brief**: Your first step is correct: analyse the brief. The goal is to translate a business or research need into a geospatial question.
    
- **Define the Analytical Workflow**: You've identified two primary types. Let's refine the terminology for clarity, as "Exploitative" can have unintended connotations.
    
    - **Exploratory Workflow**: The brief poses an open-ended question where the outcome is unknown (e.g., "Investigate the relationship between green space and property values"). The goal is **discovery**. The process is iterative, and the primary deliverable might be a report, a set of statistical summaries, and visualizations that reveal patterns.
        
    - **Prescriptive Workflow**: The brief requires a definitive, actionable output (e.g., "Produce a map of all land parcels suitable for urban agriculture"). The goal is **prescription** or creation. This workflow is often, characterised by, "reverse engineered" the outputs from the required deliverable. ^Prescriptive-Workflow
    
- **Clarify the Spectrum**: It's crucial to state that most projects exist on a **spectrum** between these two poles. A prescriptive project might require an exploratory phase to determine the suitability criteria first. We must document which parts of the project fall where.
    
- **State the Key Deliverables**: The Core Question must be tied to concrete outputs. This is non-negotiable. What will be handed over?
    - A set of GeoPackage files with specific layers?    
    - A printed A0-format map?  
    - A web map application?   
    - A reproducible technical report with figures and tables?   
    - A  pipeline/automation that can be re-run by the client?

This section answers: **"What are we trying to find out, and what will we produce?"**

---
### 2. Mapping the Operational Context (The Framework)

This section documents the non-negotiable constraints and resources. It defines the "rules of the game." Your list is excellent; I've grouped them for better logical flow.

- **Stakeholders & Roles**: Who is involved?
    
    - **Client**: The primary authority who signs off on the brief and deliverables.
    - **End-Users**: The people who will actually use the final product. Their needs are paramount.
    - **Gatekeepers**: IT departments, data owners, legal teams. We need their buy-in.
    - **Collaborators**: Other teams or experts we depend on.
        
- **Resources & [[Geospatial Technology Stack/Platforms & Applications/index|Geospatial Technology Stack]]**: What tools and assets do we have?
    - **Time & Budget**: The ultimate constraints.
    - **Data Access**: What data can we use? Is it readily available or does it need to be acquired?
    - **Mandated Technology**: The required software (e.g., ArcGIS Pro vs. QGIS), databases (PostgreSQL/PostGIS), and programming languages (Python version, specific libraries). This dictates our implementation choices from the start.
        
- **Governance**: What rules must we follow?
    - **Legislation & Compliance**: GDPR, data privacy, copyright, and licensing. This is a hard boundary.
    - **Ethical Considerations**: Beyond the law, we must document potential societal impacts. Will our analysis reinforce bias? Could it be misinterpreted in a harmful way? Acknowledging this is a sign of professional integrity.
        
- **Project Management & Communication**: How will we work and report?
    - **Deadlines & Milestones**: The required schedule for delivery.
    - **Documentation Standards**: Any specific formats for reports.
    - **Design & Branding**: Required visual guidelines (fonts, colors, logos) for any outputs.

This section answers: **"What are the boundaries, rules, and resources that shape our work?"**

---
### The Synthesis: **Project Outline**

The output of this phase is the finalised **Project Outline**, a concise document summarising the points above. It should be written in plain language and formally approved by the client or project lead.

This **Project Outline** is our **"source of truth."** When challenges or requests for changes arise mid-project ("scope creep"), we refer back to this document to make informed decisions.

Crucially, this Project Outline provides the narrative framework for the rest of the project, which is essential for our semanticGIS process. With this **narrative framework** in hand, we are ready to move to the next phase: [[Geospatial Practice/Data Modelling/index]], where we start establishing the cast (the data).