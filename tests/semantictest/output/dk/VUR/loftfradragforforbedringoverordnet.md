---
title: LoftFradragForForbedringOverordnet
draft: false
type: entity
---

# LoftFradragForForbedringOverordnet

Ingen definition fundet

### Semantic Template
```python
p.io.declare_input(
    output_name="loftfradragforforbedringoverordnet",
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
        "fkloftansaettelseid": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(int),
            "description": ""
        },
        "foerstegangaar": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(int),
            "description": "Ingen definition fundet"
        },
        "loftfradragforforbedringoverordnetid": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(int),
            "description": ""
        },
        "vaerdisum": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(int),
            "description": "Ingen definition fundet"
        },
    }
)
```
