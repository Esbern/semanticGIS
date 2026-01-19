---
title: Geocoding
draft: false
tags:
---
 Geocoding (Semantic Translation) is the process of translating **human-defined references** (street addresses, place names, postal codes) into **spatial coordinates** (Latitude/Longitude).

**The Lookup Service Model** Because human language is ambiguous and the physical world is vast, Geocoding is rarely performed "locally" on your machine. Instead, it is implemented as a **Lookup Service** (Web Service).

- **Data Volume:** A global address database (Gazetteer) is too large to store in a typical project.
    
- **Currency:** Roads change, and new buildings are constructed daily. A web service ensures you are querying the most up-to-date reality.
    
- **Fuzzy Logic:** Addresses are often misspelled or incomplete. Geocoding services employ complex "fuzzy matching" algorithms to interpret intent (e.g., knowing that "Main St" and "Main Street" are the same).
    

**The Reproducibility Challenge** In the context of **SemanticGIS**, Geocoding represents a specific risk to reproducibility. Because the external service acts as a "Black Box" and the underlying database changes over time, sending the exact same address today might yield a slightly different coordinate next year.

- **Best Practice:** Always record the **Service Name** (e.g., Nominatim, Google API), the **Date of Query**, and the **Original Input String** in your dataset. This ensures that the origin of your coordinates remains traceable.

You can find links to geocoding under the [[Global data/Datasets by Sphere/Socio_Technical/Governance/Addresses|addressee data section]]  