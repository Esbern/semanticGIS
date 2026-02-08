---
title: Vurderingsejendom
draft: false
type: entity
---

# Vurderingsejendom

Ingen definition fundet

### Semantic Template
```python
p.io.declare_input(
    output_name="vurderingsejendom",
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
        "esrejendomsnummer": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(int),
            "description": "Ingen definition fundet"
        },
        "esrkommunenummer": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(int),
            "description": "Ingen definition fundet"
        },
        "vurderingsejendomid": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(int),
            "description": "Ingen definition fundet"
        },
        "vurejendomsid": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(int),
            "description": "Ingen definition fundet"
        },
    }
)
```
