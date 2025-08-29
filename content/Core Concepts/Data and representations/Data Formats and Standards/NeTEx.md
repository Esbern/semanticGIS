---
title: Network Timetable Exchange
draft: false
tags:
---
**NeTEx (Network Timetable Exchange)** is a standardised data format specifically designed for the exchange of complex public transportation information. It is part of a broader family of standards developed under the European Committee for Standardization (CEN) and is primarily used across Europe. NeTEx is a powerful and flexible format that supports a wide range of public transport data, making it suitable for detailed modelling and analysis of transit systems.


**Key Features of NeTEx**

1. **Comprehensive Data Coverage**: NeTEx is designed to handle a broad spectrum of public transport information, including:
	- **Timetables**: Detailed scheduling information for various modes of transport, including buses, trains, trams, and ferries.
	- **Routes and Stops**: Information on the routes that vehicles take and the locations of stops and stations along these routes.
	- **Fares and Ticketing**: Complex fare structures, including pricing, fare zones, ticket types, and rules.
	- **Operational Information**: Data on vehicle types, schedules, and operational constraints such as service frequencies and service calendars.

2. **Flexibility and Extensibility**:
   NeTEx is highly flexible, allowing for the inclusion of detailed information tailored to specific needs. Its extensible nature means that new elements can be added to the format as needed, making it adaptable to various public transport systems and requirements.

3. **Advanced Features**:
   NeTEx supports advanced features that go beyond basic timetable and route data:
	- **Flexible Service Areas**: NeTEx can model areas where services are demand-responsive (e.g., buses that can be hailed outside of regular stops).
	- **Accessibility Information**: Detailed data on the accessibility of services for people with disabilities, including information about facilities at stops and stations.
	- **Operational Planning**: Support for operational planning aspects such as vehicle scheduling, crew rostering, and resource allocation.

4. **Compatibility with Other Standards**:
   NeTEx is designed to be interoperable with other European public transport standards, such as SIRI (Service Interface for Real-time Information) and IFOPT (Identification of Fixed Objects in Public Transport). This interoperability ensures that NeTEx can be used effectively in conjunction with real-time data feeds and infrastructure management systems.

**Advantages of Using NeTEx**

- **Rich Data Modeling**: NeTEx’s ability to model complex fare structures, flexible services, and detailed operational information makes it an ideal choice for sophisticated public transport planning and analysis.
- **European Standardization**: As a CEN standard, NeTEx is widely accepted across Europe, facilitating cross-border data exchange and integration within international transportation networks.
- **Future-Proofing**: The extensible nature of NeTEx ensures that it can adapt to future needs, incorporating new types of data and supporting emerging public transport technologies.

**Challenges and Considerations**
- **Complexity**: The richness and flexibility of NeTEx come with a level of complexity that can be challenging to implement and manage, especially for organizations that are new to the format.
- **Adoption and Support**: While NeTEx is widely used in Europe, its adoption outside of Europe is more limited. Additionally, not all GIS and public transport planning tools fully support NeTEx, which can limit its usability in some contexts.

**NeTEx vs. GTFS**
While **[[GTFS]] (General Transit Feed Specification)** is a simpler and more widely adopted format, especially in North America, NeTEx offers a much richer and more detailed data model. [[GTFS]] is often preferred for basic public transport applications due to its simplicity and ease of use, but NeTEx provides the depth needed for advanced applications, such as detailed fare modelling, operational planning, and multi-modal integration.

Accessing NeTEx for Denmark, see [[Traffic and Mobility data (Dataudveksleren)#Rejseplanen NeTEx|Rejseplanen NeTEx]]
