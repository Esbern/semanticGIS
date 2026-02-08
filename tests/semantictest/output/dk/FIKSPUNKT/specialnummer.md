---
title: Specialnummer
draft: false
type: entity
---

# Specialnummer

datatype med værdien af og systemet for et specialnummer

### Semantic Template
```python
p.io.declare_input(
    output_name="specialnummer",
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
        "nummer": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": "værdien for et specialnummer"
        },
        "nummertype": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.fikspunkt.lookups.nummertypeværdi, str),
            "description": "type af specialnummer ud fra opbygning og anvendelse"
        },
        "objectid": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": ""
        },
    }
)
```
