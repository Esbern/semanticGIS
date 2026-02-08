---
title: Jordstykke sekundaerForretning
draft: false
type: entity
---

# Jordstykke sekundaerForretning

Ingen definition fundet

### Semantic Template
```python
p.io.declare_input(
    output_name="jordstykke_sekundaerforretning",
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
        "jordstykkeobjectid": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(int),
            "description": ""
        },
        "sekundaerforretningshaendelse": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.mat.lookups.matrikulærtelementforretningshændelse, str),
            "description": "de begivenheder i virkeligheden som udløste ændringen i data"
        },
    }
)
```
