---
title: Feature Extraction
draft: false
tags:
aliases:
  - Feature Extraction
---
 
# From Observation to Data: A Framework for Capturing Reality

Disclaimer:
According to [Immanuel Kant](https://da.wikipedia.org/wiki/Immanuel_Kant), we can never observe reality as "Ding an sich" or [noumenon](https://en.wikipedia.org/wiki/Noumenon). Our process always begins with **Observation**: the act of perceiving **phenomena**—the objects, events, or signals that appear to our senses or instruments, _before_ we have assigned them a formal meaning.

## From Observation to Recording
While we can **observe** countless phenomena, we cannot map, enumerate, or analyse them in a structured way without an **Ontology** defined as as Domain of Discource (DoD) as descriptive in the article on the [[Data Modelling|Data Modelling]] phase of a GIS project. DoD is the formal "rulebook" that allows us to move from "unstructured" observation to "structured" **[[Field Surveys|Recording]]**—the process of creating data.

The concepts of "unstructured" observation and "structured" Recording are at each end of a continuum defined by how well-defined (scoped) our ontology is. In practice, we rarely operate at the extreme ends of this continuum, but rather somewhere in between, depending on the project's purpose and current state.

Large projects with many participants, running over more extended periods, typically require more well-defined ontologies to ensure consistency between individuals and over time, compared to a single-person, one-off survey. Strictly speaking, we are not even able to verbalise our observations without a loose, culturally defined ontology. In projects where the fieldwork is caried out by several people it is common to include "training" recordings where the individuals interpretation if the DoD are synchronised.

Even a well-thought-through ontology (DoD), rarely survives contact with the complexity of observed phenomena. This is why a pilot study is essential. It is an iterative process where you test your recording rules in the field, discovering ambiguities and refining your schema. This crucial step ensures that your final ontology is not only theoretically sound but also practically robust, enabling a consistent and meaningful recording of your observations. Far too many projects suffer from having to change their ontology after data recording has started, and find themselves in the dilemma of having to scrap and redo the first part of the data recording or try (seldom successfully to modify the observations to match the new ontology.)

The SemanticGIS approach to generating New data 
1. **Precompilng** a ontology: Desktop work where a preliminary ontology is created based on a priori knowledge and literature studies. 
2. **Pilot registration**: The purpose is to test the the registration based on the preliminary ontology on “reality” in the Area Of Interest. We often use “unstructured” registration tools using paper and notebooks to ensure maximum flexibility in the registration.
3. **Finalising the Ontology**: Modifying the preliminary ontology to match “reality”
4. **Creating a data schema**: Specifying how data is to be stored in a computer system
5. **Final Registration**: A new registration using a more structures tools i.e. apps preprinted forms etc.
 
In SemanticGIS **Design** the Preliminary Ontology is  as part of the Project scoping and Data Modelling phases og the project and documented in  ( step 1 and 2) of [[Concepts/Framework/Design rational]]. The following steps all belong to the Data Sourcing and Preparation phase of the of the project..
In both the **Pilot** and the **Final Registration**, the same four fundamental methods of data capture are used. The crucial difference lies in the **goal** of the work, the **tools** you employ, and the **level of rigor** you apply. The pilot is an exploratory test of your ontology using flexible tools, while the final registration is a systematic execution of your finalized rules using structured tools to produce clean, consistent data.

New top text:
### Feature Extraction vs. Data Analysis

The distinction between these two phases is determined by the project's **primary ontology**, not the specific tool being used.

- **Feature Extraction:** This is the process of creating the **primary subjects** of a study. If your project's goal is to analyze "park neighborhoods," then creating those features via a buffer is `Feature Extraction`. Similarly, if "hilltops" are a primary feature, then creating them from a TPI raster is `Feature Extraction`. The output is a foundational dataset that directly represents the core entities being investigated.
    
- **Data Analysis:** This is the process of using or creating **derivative data** to investigate the properties of, or relationships between, primary features. If your primary features are "parks," then using a buffer as a temporary tool to count the population nearby is `Data Analysis`. Calculating a TPI raster from a DEM to serve as an input for a subsequent extraction is also a `Data Analysis` step.
    

---

### First-Order and Second-Order Extraction

We've distinguished two hierarchical levels of `Feature Extraction`, which is crucial for handling complex subjects like those in landscape ecology.

- **First-Order Feature Extraction:** This is the creation of features directly from a raw or semi-structured source, such as an image or field survey. It's about delineating the basic elements of the landscape (e.g., individual forest patches, buildings, or rivers).
    
- **Second-Order Feature Extraction:** This is the creation of higher-order features that are defined by the **spatial pattern and arrangement** of existing first-order features. It's about delineating features that are themselves patterns (e.g., a "fragmented forest landscape" polygon derived from the arrangement of many smaller forest patches).
    

---

### The Methods of Feature Extraction

Our final list of fundamental methods is organized by the core logic of the operation.

#### First-Order Methods:

- **Manual Delineation:** The creation of features through direct **human interpretation** and digitization, either in the field or at a desktop.
    
- **Pixel-Based Classification:** An automated method that classifies features on a **pixel-by-pixel** basis according to their spectral values.
    
- **Object-Based Delineation:** An automated method that first groups pixels into **meaningful objects (segments)** and then classifies those objects.
    

#### Second-Order Method:

- **Pattern-Based Extraction:** An automated method that delineates features based on the **spatial arrangement** and context of a mosaic of existing first-order features.