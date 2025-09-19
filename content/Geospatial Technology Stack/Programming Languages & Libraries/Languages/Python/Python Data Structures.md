---
title: Python Data Structures
draft: false
tags:
---
 
In [[Geospatial Technology Stack/Programming Languages & Libraries/Languages/Python/index]], data is managed using both **simple data types** and **complex data structures**. Simple data types, such as integers, floats, and strings, represent single values and are the building blocks of more complex structures. Complex data structures, on the other hand, are used to store and organise multiple values, often of different types, in a single, cohesive unit. These complex structures are essential for effectively managing, analysing, and visualising data in various applications, including geospatial data and [[Frameworks & Context/GIS]]. 

### **1. Lists**

**Lists** are ordered, mutable collections of items. They are one of the most versatile data structures in Python, capable of holding elements of any data type, including other lists.

- **Example in Geospatial Data**: A list might be used to store a sequence of latitude and longitude coordinates representing a path or route.
  ```python
  coordinates = [(40.7128, -74.0060), (34.0522, -118.2437), (51.5074, -0.1278)]
  ```

**Key Characteristics**:
- Ordered: Items are stored in a specific sequence.
- Mutable: Items can be added, removed, or modified.
- Flexible: Can store elements of different types.

### **2. Tuples**

**Tuples** are similar to lists but are immutable, meaning that once a tuple is created, its elements cannot be changed. Tuples are useful for storing fixed collections of items.

- **Example in Geospatial Data**: A tuple might represent the immutable coordinates of a specific point.
  ```python
  point = (40.7128, -74.0060)
  ```

**Key Characteristics**:
- Ordered: Items are stored in a specific sequence.
- Immutable: Once created, elements cannot be modified.
- Useful for fixed data collections.

### **3. Dictionaries**

**Dictionaries** (dicts) are collections of [[Key-Value Pairs]], where each key is unique. They are ideal for storing and accessing data that is associated with a specific identifier.

- **Example in GIS**: A dictionary might be used to store attributes of a geographic feature, such as a building.
  ```python
  building_attributes = {
      "name": "Empire State Building",
      "height_m": 381,
      "location": (40.748817, -73.985428)
  }
  ```

**Key Characteristics**:
- Unordered: No inherent order to the elements.
- Key-Value Pairs: Access data by unique keys.
- Mutable: Items can be added, modified, or removed.

### **4. Sets**

**Sets** are collections of unique elements, making them ideal for operations that involve membership testing, deduplication, or mathematical set operations.

- **Example in Geospatial Data**: A set might be used to store unique IDs of geographic features, ensuring that no duplicates exist.
  ```python
  feature_ids = {101, 102, 103, 104}
  ```

**Key Characteristics**:
- Unordered: No inherent order to the elements.
- Unique Elements: No duplicate entries.
- Mutable: Elements can be added or removed.

### **5. Strings**

**Strings** are immutable sequences of characters, commonly used to store and manipulate text data.

- **Example in GIS**: A string might represent a well-known text (WKT) format of a geometric shape.
  ```python
  wkt_string = "POINT (40.748817 -73.985428)"
  ```

**Key Characteristics**:
- Immutable: Cannot be modified after creation.
- Sequence of Characters: Supports indexing and slicing.

### **6. Arrays (Using NumPy)**

While Python's native lists can store arrays of elements, **NumPy arrays** offer more efficient storage and manipulation, especially for numerical data.

- **Example in Geospatial Data**: A NumPy array might store raster data (such as elevation values) in a grid format.
  ```python
  import numpy as np
  elevation_data = np.array([[200, 210, 215], [190, 200, 205], [180, 195, 200]])
  ```

**Key Characteristics**:
- Fixed Size: Once created, the size of the array cannot change.
- Efficient: Optimized for numerical operations.
- Supports multidimensional data.

### **7. DataFrames (Using Pandas)**

**DataFrames** are a two-dimensional, tabular data structure provided by the Pandas library. They are especially useful for handling structured data, such as attribute tables in GIS.

- **Example in GIS**: A DataFrame might represent an attribute table with columns for feature IDs, names, and coordinates.
  ```python
  import pandas as pd
  data = {
      "FeatureID": [1, 2, 3],
      "Name": ["River", "Mountain", "Forest"],
      "Coordinates": [(40.7128, -74.0060), (34.0522, -118.2437), (51.5074, -0.1278)]
  }
  df = pd.DataFrame(data)
  ```

**Key Characteristics**:
- Tabular Data: Rows and columns, similar to a spreadsheet or database table.
- Flexible: Supports complex data manipulations and operations.
- Integration: Works well with other data structures like lists and dictionaries.

### **8. Objects**

**Objects** are instances of classes in Python, which serve as blueprints for creating complex data structures that bundle both data and behavior (methods). Objects are essential in object-oriented programming (OOP), allowing for the creation of reusable and modular code.

- **Example in [[Frameworks & Context/Geospatial data]]**: An object might represent a geographic feature, such as a `Building`, with attributes (e.g., height, location) and methods (e.g., calculating area).
  ```python
  class Building:
      def __init__(self, name, height, location):
          self.name = name
          self.height = height
          self.location = location
      
      def get_area(self):
          # Example method to calculate area
          pass
  
  empire_state = Building("Empire State Building", 381, (40.748817, -73.985428))
  ```

**Key Characteristics**:
- Encapsulation: Bundles data and methods that operate on the data within a single structure.
- Reusability: Classes can be reused to create multiple objects with the same structure but different data.
- Modularity: Helps in organizing code into logical blocks, making it easier to maintain and extend.

### **Conclusion**

Python's complex data structures, including lists, tuples, dictionaries, sets, strings, arrays, DataFrames, and objects, provide a robust toolkit for managing and processing data, particularly in geospatial contexts. These structures, built on simple data types, enable the creation of sophisticated data models and workflows that can handle the complexities of geospatial analysis and GIS applications. Understanding the appropriate use of each data structure, including objects, is key to optimising your workflows and achieving effective results in your geospatial projects.