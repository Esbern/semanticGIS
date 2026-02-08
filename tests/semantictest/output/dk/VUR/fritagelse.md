---
title: Fritagelse
draft: false
type: entity
---

# Fritagelse

Ingen definition fundet

### Semantic Template
```python
p.io.declare_input(
    output_name="fritagelse",
    attributes={
        "artkode": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.vur.lookups.fritagelseartkode, str),
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
        "ejendomtypekode": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.vur.lookups.fritagelseejendomtypekode, str),
            "description": "Ingen definition fundet"
        },
        "fkejendomsvurderingid": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(int),
            "description": ""
        },
        "fritagelseid": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(int),
            "description": ""
        },
        "loebenummer": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(int),
            "description": "Ingen definition fundet"
        },
        "omfangkode": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.vur.lookups.fritagelseomfangkode, str),
            "description": "Ingen definition fundet"
        },
    }
)
```
