---
title: PlanfikspunktFO plandesc
draft: false
type: entity
---

# PlanfikspunktFO plandesc

Ingen definition fundet

### Semantic Template
```python
p.io.declare_input(
    output_name="planfikspunktfo_plandesc",
    attributes={
        "datafordeleropdateringstid": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(datetime),
            "description": ""
        },
        "datafordelerregisterimportsequencenumber": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(int),
            "description": ""
        },
        "datafordelerrowid": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": ""
        },
        "datafordelerrowversion": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(int),
            "description": ""
        },
        "plandesc": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.fikspunkt.lookups.plandescriptorværdi, str),
            "description": "afmærkningstype (afmærkningsform) og fysisk status"
        },
        "planfikspunktfoobjectid": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": ""
        },
    }
)
```
