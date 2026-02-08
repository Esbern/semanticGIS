---
title: KorrektionEgne register
draft: false
type: entity
---

# KorrektionEgne register

Ingen definition fundet

### Semantic Template
```python
p.io.declare_input(
    output_name="korrektionegne_register",
    attributes={
        "datafordeleropdateringstid": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(datetime),
            "description": ""
        },
        "korrektionegneobjectid": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": ""
        },
        "register": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.dhmoprindelse.lookups.registerværdi, str),
            "description": "de datasæt som berøres af en rettelse"
        },
    }
)
```
