---
title: AdministrativEnhed
draft: false
type: entity
---

# AdministrativEnhed

En myndighed eller et land som det er registreret i CPR.

### Semantic Template
```python
p.io.declare_input(
    output_name="administrativenhed",
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
        "kode": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": "Den administrative enheds kode, der består af op til 4 cifre."
        },
        "landekode": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": "Hvis den administrative enhed er et land, udfyldes denne med landets landekode i formatet: ISO 3166-1 alpha-3."
        },
        "navn": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": "Den administrative enheds navn."
        },
        "typekode": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": ""
        },
    }
)
```
