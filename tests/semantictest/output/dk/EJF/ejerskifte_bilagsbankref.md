---
title: Ejerskifte bilagsbankRef
draft: false
type: entity
---

# Ejerskifte bilagsbankRef

Ingen definition fundet

### Semantic Template
```python
p.io.declare_input(
    output_name="ejerskifte_bilagsbankref",
    attributes={
        "bilagsbankref": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": "reference til bilag i Bilagsbanken hos Tinglysningsretten"
        },
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
        "ejerskifteobjectid": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(int),
            "description": ""
        },
    }
)
```
