---
title: VirksomhedEjer
draft: false
type: entity
---

# VirksomhedEjer

Ingen definition tilgængelig.

### Semantic Template
```python
p.io.declare_input(
    output_name="virksomhedejer",
    attributes={
        "ejernavn": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "1..1",
            "description": ""
        },
        "ejernummer": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "1..1",
            "description": ""
        },
        "ejerrolle": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.SkatteforvaltningensVirksomhedsregister.VirksomhedEjerRolle, str),
            "cardinality": "1..1",
            "description": ""
        },
        "ejerrolletekst": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "1..1",
            "description": ""
        },
        "ejertype": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.SkatteforvaltningensVirksomhedsregister.VirksomhedEjerType, str),
            "cardinality": "1..1",
            "description": ""
        },
        "ejertypetekst": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "1..1",
            "description": ""
        },
        "annulleringskode": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "1..1",
            "description": ""
        },
        "id_lokalid": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.PK(str),
            "cardinality": "1..1",
            "description": ""
        },
        "registreringfra": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(date),
            "cardinality": "1..1",
            "description": ""
        },
        "registreringsaktr": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "1..1",
            "description": ""
        },
        "registreringtil": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(date),
            "cardinality": "1..1",
            "description": ""
        },
        "status": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.SkatteforvaltningensVirksomhedsregister.Status, str),
            "cardinality": "1..1",
            "description": ""
        },
        "virkningfra": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(date),
            "cardinality": "1..1",
            "description": ""
        },
        "virkningsaktr": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "1..1",
            "description": ""
        },
        "virkningtil": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(date),
            "cardinality": "1..1",
            "description": ""
        }
    }
)
```