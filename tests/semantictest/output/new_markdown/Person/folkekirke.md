---
title: Folkekirke
draft: false
type: entity
---

# Folkekirke

oplysning om medlemskab af folkekirken, valgmenighed og tillige folkekirken, men fritaget for kirkeskat under udenlandsophold, fordi der betales kirkeskat til Dansk Kirke i Udlandet eller Dansk Sømandskirke eller ikke er medlem af folkekirken

### Semantic Template
```python
p.io.declare_input(
    output_name="folkekirke",
    attributes={
        "virkningfra": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(date),
            "cardinality": "1..1",
            "description": "gyldighedsstartdato for oplysningen"
        },
        "virkningfrausikkerhedsmarkering": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "1..1",
            "description": "om gyldighedsstartdatoen er usikker"
        },
        "virkningtil": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(date),
            "cardinality": "0..1",
            "description": "gyldighedsslutdato for oplysningen"
        },
        "virkningtilusikkerhedsmarkering": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "0..1",
            "description": "om gyldighedsslutdato er usikker"
        },
        "status": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.Person.Status, str),
            "cardinality": "1..1",
            "description": "status for oplysningen"
        },
        "tilhoersforhold": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.Person.Tilhoersforhold, str),
            "cardinality": "1..1",
            "description": "tilhørsforhold for oplysningen"
        },
        "registreringfra": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(datetime),
            "cardinality": "1..1",
            "description": "dato for startoplysninger"
        }
    }
)
```