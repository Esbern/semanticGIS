---
title: HoejdefikspunktGL kotedesc
draft: false
type: entity
---

# HoejdefikspunktGL kotedesc

Ingen definition fundet

### Semantic Template
```python
p.io.declare_input(
    output_name="hoejdefikspunktgl_kotedesc",
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
        "hoejdefikspunktglobjectid": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": ""
        },
        "kotedesc": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.fikspunkt.lookups.kotedecriptorværdi, str),
            "description": "fysisk etablering og administrative status i det aktuelle kotesystem"
        },
    }
)
```
