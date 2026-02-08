---
title: HoejdefikspunktDK foto
draft: false
type: entity
---

# HoejdefikspunktDK foto

Ingen definition fundet

### Semantic Template
```python
p.io.declare_input(
    output_name="hoejdefikspunktdk_foto",
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
        "foto": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.fikspunkt.lookups.uri, str),
            "description": "fotografi af punktet, dele af punktet og/eller dets omgivelser"
        },
        "hoejdefikspunktdkobjectid": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": ""
        },
    }
)
```
