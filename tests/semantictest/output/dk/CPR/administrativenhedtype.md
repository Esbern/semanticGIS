---
title: AdministrativEnhedType
draft: false
type: entity
---

# AdministrativEnhedType

AdministrativEnhedType indeholder typekode og typenavn for den administrative enhed.

### Semantic Template
```python
p.io.declare_input(
    output_name="administrativenhedtype",
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
        "typekode": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": "CPR's typekode for den administrative enhed."
        },
        "typenavn": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": "Typenavnet for den administrative enhed."
        },
    }
)
```
