---
title: PlanfikspunktFO specialnr
draft: false
type: entity
---

# PlanfikspunktFO specialnr

Ingen definition fundet

### Semantic Template
```python
p.io.declare_input(
    output_name="planfikspunktfo_specialnr",
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
        "specialnummerobjectid": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": ""
        },
    }
)
```
