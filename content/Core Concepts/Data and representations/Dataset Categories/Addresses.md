---
title: Adresses
draft: false
tags:
---
Addresses serve a vital role in various aspects of geospatial data management and analysis, extending far beyond simply indicating where people live. They are key elements in numerous applications, including geocoding, transportation analysis, logistics, membership lists for organizations, and much more. In the context of Geographic Information Systems (GIS), an address is more than just a point on a map—it is a critical piece of data that connects to a wide range of other information and services.

#### **Addresses in Broader Applications**

1. **Geocoding**:
   - Addresses are used to convert textual location descriptions into geographic coordinates. This process, known as geocoding, is fundamental in mapping services, route planning, and location-based services. Accurate geocoding enables organisations to analyze the spatial distribution of customers, resources, or incidents.

2. **Firm and Membership Lists**:
   - Businesses and organisations use addresses to maintain records of locations where services are provided, members are located, or products are delivered. Addresses in these lists can be analysed to optimise routes, assess market coverage, or plan new services.

3. **Transport Network Analysis**:
   - In transportation and logistics, addresses are crucial for route planning and optimization. Addresses are linked to transport networks to model how people and goods move through a city or region. Accurate address data ensures that routes are efficient and cost-effective.

#### **Danish Addresses: Unique Identifiers and Availability**

In Denmark, the significance of addresses is underscored by their unique integration into national registers and their accessibility through public APIs.

1. **Nationwide Unique GUID**:
   - Every address in Denmark is assigned a nationwide unique Global Unique Identifier (GUID). This identifier is used across multiple national databases, including the **Dwelling and Buildings Register (BBR)** and the **Central Business Register (CVR)**. The use of GUIDs ensures that each address can be uniquely identified and consistently referenced across different datasets and systems.

2. **Address API**:
   - Danish addresses are publicly accessible through the API provided by **Dataforsyningen**. This API allows users to retrieve detailed address information, including geographic coordinates, administrative details, and additional metadata.
   - Example: The API endpoint `https://api.dataforsyningen.dk/adresser?kommunekode=0360&format=geojson` returns all addresses in the Lolland municipality in **GeoJSON** format. This is particularly useful for applications requiring geospatial analysis or integration with mapping services.

   Here's an example of an address record from the API:

   ```json
   {
     "type": "Feature",
     "geometry": {
       "type": "Point",
       "coordinates": [
         11.13267357,
         54.83416531
       ]
     },
     "properties": {
       "id": "7cba20da-ff01-4caa-9457-dcaafef2496c",
       "status": 1,
       "darstatus": 3,
       "oprettet": "2014-05-05T19:07:48.577",
       "ændret": "2014-05-05T19:07:48.577",
       "ikrafttrædelse": "2014-05-05T19:07:48.577",
       "nedlagt": null,
       "vejkode": "0001",
       "vejnavn": "A. E. Hansensvej",
       "adresseringsvejnavn": "A. E. Hansensvej",
       "husnr": "9C",
       "etage": null,
       "dør": null,
       "supplerendebynavn": null,
       "postnr": "4900",
       "postnrnavn": "Nakskov",
       "stormodtagerpostnr": null,
       "stormodtagerpostnrnavn": null,
       "kommunekode": "0360",
       "kommunenavn": "Lolland",
       "ejerlavkode": 2002852,
       "ejerlavnavn": "Nakskov Markjorder",
       "matrikelnr": "7ap",
       "esrejendomsnr": "0",
       "etrs89koordinat_øst": 636975.46,
       "etrs89koordinat_nord": 6078422.15,
       "wgs84koordinat_bredde": 54.83416531,
       "wgs84koordinat_længde": 11.13267357,
       "nøjagtighed": "A",
       "kilde": 5,
       "tekniskstandard": "UF",
       "tekstretning": 200,
       "ddkn_m100": "100m_60784_6369",
       "ddkn_km1": "1km_6078_636",
       "ddkn_km10": "10km_607_63",
       "adressepunktændringsdato": "2013-10-23T23:59:00.000",
       "adgangsadresseid": "00a9a3dd-5794-4b1a-bcee-4e2351a09de4",
       "adgangsadresse_status": 1,
       "adgangsadresse_darstatus": 3,
       "adgangsadresse_oprettet": "2009-11-24T01:50:11.000",
       "adgangsadresse_ændret": "2018-07-04T18:00:00.000",
       "adgangsadresse_ikrafttrædelse": "2013-10-23T15:27:26.583",
       "adgangsadresse_nedlagt": null,
       "regionskode": "1085",
       "regionsnavn": "Region Sjælland",
       "jordstykke_ejerlavnavn": "Nakskov Markjorder",
       "jordstykke_ejerlavkode": 2002852,
       "jordstykke_matrikelnr": "7ap",
       "jordstykke_esrejendomsnr": "0",
       "højde": 1.9,
       "adgangspunktid": "ff0995dc-2ee9-453d-b4cf-453559f8e022",
       "vejpunkt_x": 11.13270812,
       "vejpunkt_y": 54.83417856,
       "vejpunkt_id": "11604f69-af45-11e7-847e-066cff24d637",
       "vejpunkt_kilde": "Ekstern",
       "vejpunkt_nøjagtighed": "B",
       "vejpunkt_tekniskstandard": "V0",
       "vejpunkt_ændret": "2018-05-03T14:08:02.125",
       "sognekode": "7670",
       "sognenavn": "Sankt Nikolaj",
       "politikredskode": "1466",
       "politikredsnavn": "Sydsjællands og Lolland-Falsters Politi",
       "retskredskode": "1131",
       "retskredsnavn": "Retten i Nykøbing Falster",
       "opstillingskredskode": "0029",
       "opstillingskredsnavn": "Lolland",
       "zone": "Byzone",
       "afstemningsområdenummer": "20",
       "afstemningsområdenavn": "Nakskov Vest",
       "menighedsrådsafstemningsområdenummer": 47,
       "menighedsrådsafstemningsområdenavn": "Sankt Nikolaj",
       "brofast": true,
       "supplerendebynavn_dagi_id": null,
       "navngivenvej_id": "0e75c7b0-c641-4682-b72f-b0c66fc9c88e",
       "storkredsnummer": "5",
       "storkredsnavn": "Sjælland",
       "valglandsdelsbogstav": "B",
       "valglandsdelsnavn": "Sjælland-Syddanmark",
       "landsdelsnuts3": "DK022",
       "landsdelsnavn": "Vest- og Sydsjælland",
       "kvhx": "03600001__9C_______",
       "kvh": "03600001__9C",
       "betegnelse": "A. E. Hansensvej 9C, 4900 Nakskov"
     }
   }
   ```

#### **Special Features of Danish Addresses for Network Analysis**

One of the unique aspects of Danish address data is the presence of two coordinates associated with each address:

1. **Entrance Coordinate**:
   - This coordinate represents the physical entrance to the property or building. It is crucial for pinpointing the exact location where people enter or leave a building.

2. **Road Network Coordinate (Vejpunkt)**:
   - The **Vejpunkt** is the coordinate on the centerline of the nearest road to the address. This is particularly important for transport network analysis, as it provides a connection between the address and the road network, facilitating accurate route calculations and transport modeling.

### **Conclusion**

Addresses are indispensable components of geospatial data systems, serving as the nexus between physical locations and a wide array of spatial analyses. In Denmark, the integration of addresses with nationwide unique identifiers (GUIDs) and their accessibility through a public API further enhances their utility. Whether for geocoding, transport analysis, or managing organizational records, understanding and utilizing address data effectively is key to unlocking valuable insights and improving decision-making in various fields.

The availability of detailed address information through services like the Danish Dataforsyningen API allows for sophisticated spatial analyses, such as network modeling, logistical planning, and resource allocation. The inclusion of multiple coordinates (e.g., entrance and road network points) adds depth to the data, enabling precise calculations and more accurate models.

Overall, addresses are more than just simple location indicators—they are critical elements in the broader geospatial data ecosystem, supporting a wide range of applications from everyday navigation to complex urban planning and beyond. As the need for accurate, high-quality geospatial data continues to grow, the role of addresses in linking and contextualizing this information will only become more important.