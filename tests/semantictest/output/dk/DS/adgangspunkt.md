---
title: Adgangspunkt
draft: false
type: entity
---

# Adgangspunkt

udpeger en adgang ind på eller ind i det relaterede objekt

### Semantic Template
```python
p.io.declare_input(
    output_name="adgangspunkt",
    attributes={
        "adgangsbeskrivelse": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": "adgangsvejens funktion i daglig drift"
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
        "geometri": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.ds.lookups.gm_point, str),
            "description": "opbygning af punkter og/eller linjer og/eller flader der tilsammen udgør en geografisk udstrækning"
        },
        "navngivetsted_objectid": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": ""
        },
        "objectid": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": ""
        },
    }
)
```
