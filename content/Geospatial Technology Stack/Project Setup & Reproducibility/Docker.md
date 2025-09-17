---
title: Docker
draft: false
tags:
---
 
Docker containers give you a fully isolated environment, which can be easily shared and deployed across different systems. This means that a docker container can be sent from one organisation to another, and it will still run, e.g  it is almost independent of the underlying hardware.  The key exception is if a docker container relies on the use of CUDA acceleration; this will only work if the underlying hardware supports CUDA. This is primarily an issue with containers that optimise AI models but also rely on CUDA support at some "[[point cloud]]" tools.
In my experience with code-based geospatial data processing, there are two distinct scenarios for the use of containerisation:
- **[[Developing and deploying a service]]**: This could be a front end for a database backend, enabling web-based visualisation and analysis. Here the task in the development face is to connect to the container from an IDE, such as vs. code on your host computer but running on the environment within the container (so-called remote development). When deploying the service, all that is needed is to set a variable to production rather than development when starting the container
- **Deploying and running a prebuilt web app**: This could, for instance, be a web GIS server such as GeoNode see (https://geonode.org/). A typical example of this scenario is to deploy a web-based development environment such as [[JupyterLab]]. 
One of the significant advantages of using containerisation tools like docker is the ability to isolate services in individual containers and have them communicate on internal secure networks that are not accessible outside the containers. Multiple containers and their network and run parameters can be oriented using co-called docker-compose files.

Docker can either be run as a command line tool or from a desktop app see (https://www.docker.com/)