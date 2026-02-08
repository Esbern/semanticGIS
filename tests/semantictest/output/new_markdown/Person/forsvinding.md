---
title: Forsvinding
draft: false
type: entity
---

# Forsvinding

oplysning om forsvindinger og genfindinger

### Semantic Template
```python
p.io.declare_input(
    output_name="forsvinding",
    attributes={
        "virkningfra": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(date),
            "cardinality": "1..1",
            "description": "forsvindingsdato"
        },
        "virkningfrausikkerhedsmarkering": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "1..1",
            "description": "angiver at virkningFra er usikker"
        },
        "virkningtil": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(date),
            "cardinality": "0..1",
            "description": "dato for genfinding. Vil altid findes som historisk data, idet det er slut på en forsvinding"
        },
        "virkningtilusikkerhedsmarkering": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "0..1",
            "description": "angiver at virkningTil er usikker"
        },
        "status": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.Person.Status, str),
            "cardinality": "1..1",
            "description": "angiver status for forsvinding"
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