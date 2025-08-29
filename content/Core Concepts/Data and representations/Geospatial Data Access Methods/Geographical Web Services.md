---
title: Geographical Web Services
draft: false
tags:
---
## What is a Web Service in general?

A web service is a method of communication between two electronic devices over a network. It allows various applications from different sources to communicate with each other without time-consuming custom coding. They are platform-independent and enable seamless integration of various services.

## What is a Geographical Web Service?

Geographical web services are specialised web services that handle spatial data. These services are crucial for applications requiring geographic information, such as mapping, location-based services, and spatial analysis. Let's explore two main examples of geographical web services: geocoding services and Web Feature Services (WFS).

#### Geocoding Services

Geocoding is the process of converting addresses (like "Universitetsvej 1 4000") into geographic coordinates (like latitude 55.65168685 and longitude 12.1366598). T

Popular examples of international geocoding web services include Google Maps Geocoding API, but most countries also have their own national services that typically are more up to date and deliver more detailed feedback. In calling https://api.dataforsyningen.dk/adresser?vejnavn=Universitetsvej&husnr=1&postnr=4000 will, for instance, return information relating to the address "Universitetsvej 1 4000", including the coordinates. You can try this by simply clicking on the link above.

Behind-the-scenes web services are what drive much of what we do when working with geospatial data, especially supplying background maps.

The key web-services types you brobsbly will come across when working with geospatial data are: 
- [[WFS]]
- WMS
- XYZ tiles



