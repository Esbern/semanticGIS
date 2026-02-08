---
title: Separation
draft: false
type: entity
---

# Separation

oplysninger om eventuelle separationer knyttet til ægteskab. Der kan både være aktuelle og historiske separationer

### Semantic Template
```python
p.io.declare_input(
    output_name="separation",
    attributes={
        "virkningfra": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(date),
            "cardinality": "1..1",
            "description": "separation startdato"
        },
        "virkningfrausikkerhedsmarkering": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "1..1",
            "description": "angiver at separation startdato er usikker"
        },
        "virkningtil": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(date),
            "cardinality": "0..1",
            "description": "separation slutdato"
        },
        "status": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.Person.Status, str),
            "cardinality": "1..1",
            "description": "separation status"
        },
        "virkningtilusikkerhedsmarkering": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "0..1",
            "description": "angiver at separation slutdato er usikker"
        },
        "registreringfra": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(datetime),
            "cardinality": "1..1",
            "description": "dato for startoplysninger"
        },
        "civilstand": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.FK(dk.Person.Civilstand, str),
            "cardinality": "1..1",
            "description": ""
        }
    }
)
```