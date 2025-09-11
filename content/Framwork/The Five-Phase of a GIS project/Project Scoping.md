---
title: Project Scoping
draft: false
tags:
aliases:
  - Project Scoping
order: "1"
---
The first phase of any project is to define its **purpose, boundaries, and real-world context**. All projects exist within an organisational framework of rules, resources, and requirements. The first and most critical step is to understand this framework, as it defines the practical limits and directs the intellectual focus of your work.

---
### The Organisational Framework: Understanding Your Constraints

Before defining your specific research goals, you must identify and document the external factors that will shape your project. These are often non-negotiable constraints imposed by clients, employers, or legal bodies.

- **The Brief:** You must begin by analysing the project brief from the client (or teacher). This document dictates the entire structure of your project. Your first task is to determine which of two primary workflows it requires:
    
    - **Exploitative Workflow:** The brief poses an open-ended question (e.g., "Investigate the relationship between green space and property values"). Your process will be iterative, and the final output may not be known at the start.
        
    - **Reverse Engineering Workflow:** The brief demands hard deliverables (e.g., "Produce a map of all land parcels suitable for urban agriculture"). Here, your process is determined by working backward from the required output to identify the necessary data and analytical steps. 
	It is always a best practice to **reformulate the brief** in your own words, clarifying the workflow and deliverables, and have it approved by the client to ensure a shared understanding. Also note that a brief can seldom be answered through a  enticingly **Exploitative workflow** or a enticingly **Reverse Engineering Workflow:** often the two work in tandem. This articel presents the phases in the order of a **Exploitative workflow** since this is the simplest. At the end of the articel we wil discuss how to modify the proces for a more **Reverse Engineering Workflow:**
	
- **The Stakeholder Landscape**: Beyond the primary client (or teacher) who provides the brief, most projects have a wider network of **stakeholders**. You should identify who they are and what their interests or requirements might be.
	- **Who are they?** Stakeholders could include the **IT department** that controls data access and software, the **end-users** who will interact with your final map, a **communications team** that must approve public-facing materials, or even **community groups** affected by the analysis.
    - **Why does it matter?** A brilliant analysis that the IT department can't support or that the end-users find confusing is a failed project. Mapping these stakeholders early helps you anticipate needs and manage expectations.
        
- **Resources:** You need to assess the practical resources available. This includes the **time** allocated for the project, the **budget**, and your access to crucial, task-specific **data**, software, or expertise within the organisation. **The Technical Infrastructure** This is a more specific aspect of "Resources." It's not just about what you have access to, but what you are _required_ to use.
	- **What is it?** This includes constraints like a mandatory software ecosystem (e.g., "This organization works exclusively with ESRI products"), required database formats (e.g., "All data must be stored in the central PostgreSQL/PostGIS database"), or specific programming languages for scripts (e.g., "All automation must be done in Python 3.9").
	- **Why does it matter?** These constraints dictate your tool choices from the very beginning. Knowing them prevents you from building a solution in QGIS and R when the client can only support ArcGIS Pro and its proprietary tools.
	
- **Project Management:** Document any formal project management requirements. This includes **deadlines** and **milestones**, but also any specific formats for external documentation or reporting. While you must meet these external demands, your **`semanticGIS` Design Rationale remains your non-negotiable internal tool** for ensuring analytical rigour.
    
- **Legislation and Compliance:** You must identify any legal or regulatory constraints, such as privacy regulations (GDPR), data protection laws, or copyright on data that govern how you can acquire, store, and use information. In addition to the Legislation you should also consider  **Ethical Guidelines**. This goes beyond strict "Legislation and Compliance." Even if an analysis is legal, it may have significant ethical implications that you must consider.
	- **What is it?** This involves assessing the potential social impact of your work. For example, will a crime hotspot analysis unintentionally stigmatise a neighbourhood and reinforce social biases? Does a site suitability analysis for a new waste facility fairly consider the impact on all communities?
	- **Why does it matter?** As a researcher and consultant, you have a professional responsibility to "do no harm." Documenting your consideration of these ethical dimensions is a hallmark of a mature and responsible analytical process.
    
- **Design and Branding:** Identify any constraints on your final visualisations. Your client or organisation may have a **design manual** with specific rules for fonts, colours, and logos that you must follow.
    

---

### Defining Your Intellectual Core: Your Analytical Goals

Now that you have established the practical boundaries of your project, you can define its specific intellectual core. This involves translating the brief into a focused, actionable, and achievable research plan that fits within the identified constraints.

Your task is to:

- **Frame the Problem:** In your own words, write a clear statement of the research question or problem you will address.
    
- **Define Objectives:** List the specific, measurable goals you will achieve to answer that question.
    
- **Establish Scope:** Clearly define what is included and excluded from your analysis, including your geographical study area and any thematic or temporal limits.
    

The deliverable for this phase is a formal **project scope** that clearly outlines the external constraints and your specific analytical goals. This will be the first chapter in your Design Rationale.
