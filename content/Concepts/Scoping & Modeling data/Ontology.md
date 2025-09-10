---
title: Ontology
draft: false
tags:
---

An **ontology** in the context of SemanticGIS is a structured framework that defines how we represent and categorise the world of observation. It is a crucial component in defining the **[[world of discourse]]**—the specific way in which we interpret and organise the phenomena we observe ([[world of observation]]), tailored to the goals of the project.

### **Starting Simple: Basic Ontology Components**

In many cases, a basic ontology for a GIS project may be as simple as specifying that it includes "Buildings" as defined in a national building dataset. This approach leverages existing standards to ensure consistency and compatibility, allowing the project to align with established definitions without needing to create new ones from scratch.

For example, if your project uses a national building dataset, you can define the "Building" entity type according to the criteria set by that dataset, such as the inclusion of structures intended for human occupancy or use. This helps ensure that all relevant data fits seamlessly into the project's framework, while also allowing for meaningful analysis and comparisons.

### **Ontology and the Concept of Existence**

At a deeper level, ontology is about defining what "exists" within the world of discourse. This ties back to the metaphysical origins of the term ontology, which concerns the nature of being and existence. In the context of a GIS project, the ontology determines what entities and phenomena are recognized as part of the project’s scope. It essentially dictates the "reality" of the project by defining what is considered to exist within its analytical framework.

For instance, in one project, "Buildings" and "Roads" might be the primary entities recognized in the ontology, while natural features like "Forests" or "Rivers" might be excluded. This decision shapes the entire analysis and visualization process, focusing the project’s efforts on specific elements of the world of observation.

### **Incorporating Temporality into the Ontology**

One often neglected but critical aspect of ontology in GIS projects is **temporality**—the consideration of time in defining and analyzing entities. Temporality plays a significant role, especially in fields like urban planning and environmental management, where changes over time are essential to understanding and managing spaces.

For example, in urban planning, a "Building" might have temporal attributes such as construction date, renovation history, or anticipated lifespan. These temporal aspects allow the ontology to capture not just the current state of the entity, but also its history and projected future. This is crucial for analyzing trends, forecasting future developments, and making informed decisions about resource allocation and policy.

Similarly, in environmental management, the temporality of features like "Wetlands" or "Forests" is key to understanding ecological changes, such as seasonal variations or long-term shifts due to climate change. An ontology that incorporates temporality enables more dynamic and responsive models, capable of supporting adaptive management strategies.

### **Refining the Ontology: Adhering to Existing Standards**

As we refine the ontology, we often align it with existing datasets or standards. When working with established datasets, the ontology is often implicitly defined by the data specifications. For example, using a national building dataset means adopting its definitions, such as what constitutes a "Building" and the associated properties like height, footprint, and usage.

While these specifications guide the ontology, they may also include implementation-specific details (e.g., using a 16-bit integer to store building height). These details are necessary for technical compatibility but are more related to the data's storage and format than to the conceptual framework of the ontology itself.

### **The Role of Ontology in Defining the World of Discourse**

The ontology is not just a list of categories and properties; it shapes the entire [[world of discourse]] for the [[GIS project]]. By defining what entities (see [[Entity-based modelling]]) and properties (see [[Field-based modelling]]) are relevant, the ontology determines how we view and interpret the [[world of observation]]. For example, one project might define a "Building" primarily by its usage (residential, commercial, industrial), while another might focus on its architectural style or historical significance. The ontology directs these choices, influencing everything from data collection to analysis and visualization.

The ontology also plays a crucial role in deciding whether existing data can be used or if new data collection is required. If the existing dataset’s ontology aligns with the project’s needs, it can be integrated directly. If not, adjustments to the ontology or new data collection may be necessary.

### **Conclusion**

Understanding and developing a clear ontology is fundamental to the success of a [[GIS project]]. It not only defines the structure of the data you will use but also shapes the entire analytical framework of your project. By starting with simple entity types and properties, aligning with existing standards, and incorporating crucial elements like temporality, you can ensure that your GIS project has a solid conceptual foundation. This foundation supports effective data analysis and decision-making, ensuring that the world of discourse accurately reflects the needs and goals of the project. The ontology should always play a central role in the [[Design rational]] of the [[GIS project]].


