---
title: PlanfikspunktFO punktdesc
draft: false
type: entity
---

# PlanfikspunktFO punktdesc

Ingen definition fundet

### Semantic Template
```python
p.io.declare_input(
    output_name="planfikspunktfo_punktdesc",
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
        "planfikspunktfoobjectid": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": ""
        },
        "punktdesc": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.fikspunkt.lookups.punktdescriptorværdi, str),
            "description": "afmærkningstype (afmærkningsform) og fysisk tilstand og status"
        },
    }
)
```
