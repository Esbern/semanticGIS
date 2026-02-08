---
title: Beskyttelse
draft: false
type: entity
---

# Beskyttelse

en persons beskyttelse mod videregivelse af adresse- og navneoplysninger

### Semantic Template
```python
p.io.declare_input(
    output_name="beskyttelse",
    attributes={
        "virkningfra": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(datetime),
            "cardinality": "1..1",
            "description": "gyldighedsstart"
        },
        "virkningtil": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(datetime),
            "cardinality": "0..1",
            "description": "gyldighedsslut"
        },
        "status": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.Person.Status, str),
            "cardinality": "1..1",
            "description": "angiver beskyttelse status"
        },
        "beskyttelsestype": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.Person.Beskyttelsestype, str),
            "cardinality": "1..1",
            "description": "angiver typen af beskyttelsen"
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