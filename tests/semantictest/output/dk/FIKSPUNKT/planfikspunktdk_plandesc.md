---
title: PlanfikspunktDK plandesc
draft: false
type: entity
---

# PlanfikspunktDK plandesc

Ingen definition fundet

### Semantic Template
```python
p.io.declare_input(
    output_name="planfikspunktdk_plandesc",
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
        "planfikspunktdkobjectid": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": ""
        },
    }
)
```
