---
title: Civilstand
draft: false
type: entity
---

# Civilstand

oplysninger om en persons civilstand og evt. ægteskabsoplysninger

### Semantic Template
```python
p.io.declare_input(
    output_name="civilstand",
    attributes={
        "virkningfra": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(date),
            "cardinality": "1..1",
            "description": "gyldighedsstart for en civilstandsoplysning"
        },
        "virkningfrausikkerhedsmarkering": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "1..1",
            "description": "angiver om civilstandens gyldighedsstartdato er usikker"
        },
        "virkningtil": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(date),
            "cardinality": "0..1",
            "description": "gyldighedsslut for en civilstandsoplysning"
        },
        "virkningtilusikkerhedsmarkering": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "1..1",
            "description": "angiver om civilstandens gyldighedsslutdato er usikker"
        },
        "status": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.Person.Status, str),
            "cardinality": "1..1",
            "description": "angiver civilstandens status"
        },
        "civilstandstype": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.Person.Civilstandstype, str),
            "cardinality": "1..1",
            "description": "angiver typen af civilstanden"
        },
        "registreringfra": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(datetime),
            "cardinality": "1..1",
            "description": "dato for startoplysninger"
        },
        "ikkevalidrelationsaegtefaelde": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.FK(dk.Person.IkkeValidRelationsPerson, str),
            "cardinality": "0..1",
            "description": ""
        },
        "andenaegtefaelle": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.FK(dk.Person.PersonUdenCpr, str),
            "cardinality": "0..1",
            "description": ""
        },
        "separation": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.FK(dk.Person.Separation, str),
            "cardinality": "0..*",
            "description": ""
        },
        "aegtefaelle": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.FK(dk.Person.Person, str),
            "cardinality": "1..2",
            "description": ""
        }
    }
)
```