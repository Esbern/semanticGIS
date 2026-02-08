---
title: Foraeldremyndighedsoplysning
draft: false
type: entity
---

# Foraeldremyndighedsoplysning

oplysninger og hvem der har forældremyndighed over et barn

### Semantic Template
```python
p.io.declare_input(
    output_name="foraeldremyndighedsoplysning",
    attributes={
        "virkningfra": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(date),
            "cardinality": "1..1",
            "description": "forældremyndighedens gyldighedsstart"
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
            "cardinality": "0..0",
            "description": "forældremyndighedens gyldighedsslut"
        },
        "foraeldremyndighedsindehaverrolle": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.Person.Foraeldremyndighedshaverrolle, str),
            "cardinality": "1..1",
            "description": "forældremyndighedsindehaveren relation til Personen"
        },
        "status": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.Person.Status, str),
            "cardinality": "1..1",
            "description": "status for Foraeldremyndighedsoplysning"
        },
        "registreringfra": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(datetime),
            "cardinality": "0..0",
            "description": "foraeldremyndighedsoplysning er blevet registreret i systemet denne dato"
        },
        "foraeldremyndighedshaver": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.FK(dk.Person.Person, str),
            "cardinality": "0..1",
            "description": ""
        },
        "foraeldremyndighedover": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.FK(dk.Person.Person, str),
            "cardinality": "1..1",
            "description": ""
        }
    }
)
```