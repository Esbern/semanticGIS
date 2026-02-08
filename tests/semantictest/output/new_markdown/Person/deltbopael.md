---
title: DeltBopael
draft: false
type: entity
---

# DeltBopael

oplysning om barnet har delt bopæl

### Semantic Template
```python
p.io.declare_input(
    output_name="deltbopael",
    attributes={
        "registreringfra": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(datetime),
            "cardinality": "1..1",
            "description": "delt bopæl er blevet registreret i systemet denne dato"
        },
        "virkningfra": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(date),
            "cardinality": "1..1",
            "description": "delt bopæl gyldighedsstartdato"
        },
        "virkningfrausikkerhedsmarkering": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "1..1",
            "description": "om gyldighedsstartdatoen er usikker"
        },
        "status": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.Person.Status, str),
            "cardinality": "1..1",
            "description": "status for DeltBopael"
        },
        "virkningtil": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(date),
            "cardinality": "0..0",
            "description": "delt bopæl gyldighedsslutdato"
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