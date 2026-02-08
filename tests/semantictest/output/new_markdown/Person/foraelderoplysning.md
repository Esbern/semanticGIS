---
title: Foraelderoplysning
draft: false
type: entity
---

# Foraelderoplysning

oplysninger om relationer mellem forældre og børn

### Semantic Template
```python
p.io.declare_input(
    output_name="foraelderoplysning",
    attributes={
        "virkningfra": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(date),
            "cardinality": "0..1",
            "description": "slægtskabets gyldighedsstartdato"
        },
        "virkningfrausikkerhedsmarkering": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "0..1",
            "description": "om gyldighedsstartdatoen er usikker"
        },
        "foraelderrolle": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.Person.Foraelderrolle, str),
            "cardinality": "1..1",
            "description": "angiver om forælder er mor/far/medfar eller far/medmor"
        },
        "status": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.Person.Status, str),
            "cardinality": "1..1",
            "description": "status for Foraelderoplysning"
        },
        "virkningtil": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(date),
            "cardinality": "0..0",
            "description": "slægtskabets gyldighedsslutdato"
        },
        "registreringfra": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(datetime),
            "cardinality": "0..0",
            "description": "foraelderoplysning er blevet registreret i systemet denne dato"
        },
        "foraelder": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.FK(dk.Person.GeneriskBasePerson, str),
            "cardinality": "1..1",
            "description": ""
        },
        "barn": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.FK(dk.Person.Person, str),
            "cardinality": "1..1",
            "description": ""
        }
    }
)
```