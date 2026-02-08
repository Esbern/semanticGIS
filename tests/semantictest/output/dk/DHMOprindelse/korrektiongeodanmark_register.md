---
title: KorrektionGeoDanmark register
draft: false
type: entity
---

# KorrektionGeoDanmark register

Ingen definition fundet

### Semantic Template
```python
p.io.declare_input(
    output_name="korrektiongeodanmark_register",
    attributes={
        "datafordeleropdateringstid": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(datetime),
            "description": ""
        },
        "korrektiongeodanmarkobjectid": {
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
