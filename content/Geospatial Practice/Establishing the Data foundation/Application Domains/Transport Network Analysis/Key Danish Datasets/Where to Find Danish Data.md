---
title: Where to Find Danish Data
draft: true
tags:
---
 Before looking for Danish Data, please remember that there are at least three different ways of accessing data See the note [[Geospatial Data Acces Methods]]:
1. Web services where you access central data collection over the internet; see the note on [[Geographical Web Services]]
2. Remote Database server connection (This is typically used within an organisation to ensure that all members of the organisation have access to the same version of a given dataset). This is typically implemented as a [[Postgres]] server connection.
3. Data for download. Many smaller organisation as well as larger organisations that give access to data primarily used for analysis exposes the ability to download an entire dataset for use on your local computer. Data will often be in one of the [[Common Data Formats for Sharing Data]]. 

Also, remember that the same data can be served as both Raster and Vector Data. See the note on [[Key differences between Raster and Vector representation]]


It is relevant to distinguish between two types of data portals, namely:
- Metadata portals 
- Data warehouse portals. 
In a Metadata portal, you only find the description of data (i.e. the metadata) and a link to where the data is located (the data warehouse where the data is stored). In contrast, the data warehouse portals are primarily concerned with storing and giving access to the data but also contains meta data for search and description purposes.

In Denmark, there are two main metadata services
- "Datavejviseresn" contains "all public data" where some is geospatial data and some are not. websit: http://www.datavejviser.dk/
- "Geo-data.info.dk": only focuses on geospatial data. Website : https://geodata-info.dk/

Data warehouse portals are a bit more complicated. In principle, there is one national public data warehouse portal, "Datafordeleren" (https://datafordeler.dk/), which contains access to all the so-called "Grunddata" (Basic public data). Datafordeleren is primarily geared towards the professional user who accesses data regularly. For the more infrequent users, much of the geospatial data found on "Datafordeleren" can, with less effort, be accessed through the "Dataforsyning" portal (https://dataforsyningen.dk/). In order to use "Dataforsyning," you need to create a user on the portal, which is rather straightforward if you understand Danish.  For Non-Danish speakers, I have created a guide for "[[Creating a user on Dataforsyningen]]". In addition to the portals that give access to "the Basic public data", there are several sector/ministerial special sites.
- Planning data (Plandata.dk) : https://www.planinfo.dk/
- Environmental data ("Danmarks Miljøportal") : https://miljoeportal.dk/it-systemer-udvikling-og-webservices/it-systemer and its data search sub site  https://arealdata.miljoeportal.dk/
- Traffic and mobility data ([Dataudveksleren](https://du-portal-ui.dataudveksler.app.vd.dk/)) : https://du-portal-ui.dataudveksler.app.vd.dk/
- Agricultural data (LandbrugsGIS): https://landbrugsgeodata.fvm.dk/

