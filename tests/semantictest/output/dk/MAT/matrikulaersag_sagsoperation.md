---
title: MatrikulaerSag sagsoperation
draft: false
type: entity
---

# MatrikulaerSag sagsoperation

type med kode og betegnelse for en sagsoperation

### Semantic Template
```python
p.io.declare_input(
    output_name="matrikulaersag_sagsoperation",
    attributes={
        "betegnelse": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": "betegnelse for sagsoperationen"
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
        "kode": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": "kode for sagsoperationen"
        },
        "matrikulaersagobjectid": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(int),
            "description": ""
        },
        "objectid": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(int),
            "description": ""
        },
    }
)
```
