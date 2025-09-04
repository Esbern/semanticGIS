---
title: Relational Database (Concept)
draft: false
tags:
---
 

# Relational Database Concepts

A **relational database** is a type of database that organizes data into tables, also known as **relations**. Each table consists of rows and columns, where:

- **Tuples** (or rows) represent individual records in the table.
- **Attributes** (or columns) define the properties or fields of the data stored in the table.

## Tables (Relations)
A table is the primary structure within a relational database where data is stored. Each table contains a set of attributes, and each tuple in the table represents a single data entry or record.

For example, a table representing a collection of users might look like this:

| UserID | FirstName | LastName  | Email            |
|--------|-----------|-----------|------------------|
| 1      | Alice     | Smith     | alice@email.com  |
| 2      | Bob       | Johnson   | bob@email.com    |

In this example:
- The **attributes** are `UserID`, `FirstName`, `LastName`, and `Email`.
- Each **tuple** corresponds to a single user, containing information across those attributes.

## Primary Keys
A **primary key** is an attribute (or a set of attributes) that uniquely identifies each tuple in a table. This ensures that no two rows in the table have the same primary key, making each record unique. In the example above, the `UserID` attribute is the primary key because it uniquely identifies each user.

## Foreign Keys
A **foreign key** is an attribute in one table that refers to the primary key of another table, establishing a relationship between the two tables. Foreign keys help maintain referential integrity between related data stored in different tables.

For instance, if we have another table called **Orders**, which tracks orders placed by users, it might look like this:

| OrderID | UserID | Product      | Quantity |
|---------|--------|--------------|----------|
| 101     | 1      | Laptop       | 1        |
| 102     | 2      | Smartphone   | 2        |

In this table:
- `OrderID` is the primary key for the **Orders** table.
- `UserID` is a foreign key that refers to the `UserID` primary key in the **Users** table, establishing a link between the two tables. This link allows us to associate orders with the users who placed them.

## Relationships Between Tables
Tables in a relational database can be related in various ways, including:
- **One-to-one relationships**: Each tuple in one table corresponds to one tuple in another.
- **One-to-many relationships**: A single tuple in one table relates to multiple tuples in another (e.g., a user placing multiple orders).
- **Many-to-many relationships**: Tuples in one table can relate to multiple tuples in another and vice versa. This usually requires an intermediary table.

## Database Management Systems (DBMS)
A **Database Management System (DBMS)** is the software that manages the creation, storage, and querying of relational databases. DBMSs offer various features that enhance data management, including:

- **User Management**: Most DBMSs include user management features, allowing administrators to control access to the database. This involves assigning roles and permissions, enabling multi-user collaboration, and maintaining data security.
- **Scalability**: Relational databases are designed to handle increasing amounts of data efficiently. Some DBMSs are optimized for large-scale, multi-user applications, while others are suited for smaller, single-user projects.

### Server-based vs. Serverless Databases
Relational databases come in two main types based on how they are deployed and accessed:

1. **Server-based Databases**: These databases require a dedicated server to host the DBMS. They are designed for multi-user environments and can handle large amounts of data with high availability, performance, and security. Examples include:
   - **[[PostgreSQL]]**: A powerful, open-source, server-based relational database that supports advanced features such as geospatial data processing (with the PostGIS extension).
   - **MySQL** and **Microsoft SQL Server**: Other examples of server-based relational DBMSs that offer enterprise-level features, including user management and scalability.

   Server-based databases are ideal for large applications, such as web platforms, multi-user systems, or any scenario where scalability, performance, and concurrency are critical.

2. **Serverless (Embedded) Databases**: These databases do not require a dedicated server to run. They are typically embedded within an application and are designed for local, single-user environments. A key example is:
   - **SQLite**: A serverless, lightweight database that is embedded in applications. It is commonly used in mobile apps and local desktop applications. SQLite is also the foundation for the **[[GeoPackage]]** format, widely used in GIS applications like [[Tools/QGIS/index|QGIS]]] to store geospatial data in a portable, self-contained file.

   Serverless databases are often used in scenarios where simplicity and portability are more important than scalability. They are easy to deploy and ideal for local data storage.

##  [[SQL]]
The structure of relational databases is managed and queried through **Structured Query Language (SQL)**. [[SQL]] is the standard language for interacting with relational databases, allowing users to insert, query, update, and manage data. While this note focuses on the core concepts of relational databases, a more detailed exploration of SQL, especially in the context of geospatial processing, will be provided in a separate note. That note will also discuss how standard SQL can be extended with spatial operators for handling geographic data.

