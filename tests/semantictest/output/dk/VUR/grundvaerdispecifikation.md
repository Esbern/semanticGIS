---
title: Grundvaerdispecifikation
draft: false
type: entity
---

# Grundvaerdispecifikation

Ingen definition fundet

### Semantic Template
```python
p.io.declare_input(
    output_name="grundvaerdispecifikation",
    attributes={
        "areal": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.vur.lookups.area, int),
            "description": "Ingen definition fundet"
        },
        "beloeb": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(int),
            "description": "Ingen definition fundet"
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
        "enhedbeloeb": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(int),
            "description": "Ingen definition fundet"
        },
        "fkejendomsvurderingid": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(int),
            "description": ""
        },
        "grundvaerdispecifikationid": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(int),
            "description": ""
        },
        "loebenummer": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(int),
            "description": "Ingen definition fundet"
        },
        "priskode": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.vur.lookups.grundværdispecifikationpriskode, str),
            "description": "Ingen definition fundet"
        },
        "tekst": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": "Ingen definition fundet"
        },
    }
)
```
