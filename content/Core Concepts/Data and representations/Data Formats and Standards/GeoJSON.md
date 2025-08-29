---
title: GeoJSON
draft: false
tags:
---
 **GeoJSON** is a widely-used format for encoding a variety of geographic data structures using JavaScript Object Notation (**JSON**). It is designed to represent simple geospatial features and their non-spatial attributes, making it a popular choice for web services, data exchange, and lightweight geospatial applications.

### **Key Features of GeoJSON**

1. **GeoJSON Structure**:
   - **Geometry**: GeoJSON supports several geometry types as defined by the [[Open Geospatial Consortium (OGC)]] in the [[Simple Feature Access (SFA)]] standard, including Point, Line String, Polygon, MultiPoint, Multiline String`, and `MultiPolygon`. Each geometry type is represented as a JSON object with specific coordinate data.
   - **Feature**: A GeoJSON Feature object represents a spatially bounded entity with a geometry and associated properties (attributes). Each feature is a combination of a geometry and properties stored in a dictionary-like structure.
   - **FeatureCollection**: This is a collection of Feature objects, allowing multiple features to be grouped together in a single GeoJSON file.

   Example:
   ```json
   {
     "type": "FeatureCollection",
     "features": [
       {
         "type": "Feature",
         "geometry": {
           "type": "Point",
           "coordinates": [12.4924, 41.8902]
         },
         "properties": {
           "name": "Colosseum"
         }
       }
     ]
   }
   ```

2. **GeoJSON Creation and Editing**:
   - **Online Creation**: You can create and edit GeoJSON files directly in your web browser using tools like [geojson.io](https://geojson.io). This online tool provides a simple interface for drawing points, lines, and polygons, and it allows you to export the resulting GeoJSON file.
   - **Using QGIS**: QGIS, a popular open-source GIS platform, also supports the creation and editing of GeoJSON files. You can import data into QGIS, edit it, and then export it as a GeoJSON file, making it a versatile tool for managing geospatial data.

3. **GitHub and GeoJSON**:
   - **Native Support**: GitHub natively supports GeoJSON files. When you upload a GeoJSON file to a GitHub repository, it will automatically render the data as an interactive map, allowing viewers to visualize the geospatial data directly within the GitHub interface.

4. **GeoJSON in Web Services**:
   - **Exchange Format**: GeoJSON is frequently used as an exchange format for simple geospatial data in web services. It is lightweight, easy to parse, and well-suited for web applications.
   - **Example Web Service Call**: A typical example of a GeoJSON response from a web service is the following API call:
     ```
     https://api.dataforsyningen.dk/adresser?kommunekode=0360&format=geojson
     ```
     This URL requests all addresses for the municipality of Lolland (code 0360) in Denmark, returning the data in GeoJSON format. This demonstrates how GeoJSON is often used to provide spatial data in a web-friendly format, making it ideal for web mapping applications.

### **Advantages of GeoJSON**

- **Human-Readable**: Like JSON, GeoJSON is human-readable, making it easy to understand and debug.
- **Lightweight**: It is a lightweight format, which is beneficial for web applications where data transfer efficiency is crucial.
- **Interoperability**: GeoJSON is supported by many GIS software packages and web mapping platforms, making it an excellent format for data exchange.
- **Flexibility**: With support for a variety of geometries and the ability to store properties, GeoJSON is versatile for different types of geospatial data.

### **Conclusion**

GeoJSON is a powerful and flexible format for representing simple geospatial data. Its integration with web services, native support in platforms like GitHub, and ease of creation through tools like QGIS and [geojson.io](https://geojson.io) make it a go-to format for many geospatial applications. Whether you're sharing geospatial data on the web or integrating it into a mapping application, GeoJSON provides a straightforward and effective solution.

For more information on the underlying structure, you can refer to the   [[JSON]] note that provides a foundational understanding of the JSON format on which GeoJSON is based.