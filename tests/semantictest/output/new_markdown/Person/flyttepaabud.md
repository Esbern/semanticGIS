---
title: Flyttepaabud
draft: false
type: entity
---

# Flyttepaabud

oplysninger, der angiver at der for personen er påbud om at fraflytte en ulovlig beboelse

### Semantic Template
```python
p.io.declare_input(
    output_name="flyttepaabud",
    attributes={
        "bemaerkninger": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "0..1",
            "description": "fritekstfelt til bemærkninger i tilknytning til oplysninger om flyttepåbud"
        },
        "virkningfra": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(date),
            "cardinality": "1..1",
            "description": "startdato for flyttepåbud"
        },
        "virkningtil": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(date),
            "cardinality": "0..0",
            "description": "slutdato for flyttepåbud"
        },
        "status": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.Person.Status, str),
            "cardinality": "1..1",
            "description": "status for oplysningen"
        },
        "registreringfra": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(datetime),
            "cardinality": "0..0",
            "description": "dato for startoplysninger"
        }
    }
)
```