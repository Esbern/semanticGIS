---
title: Jordstykke stormfald
draft: false
type: entity
---

# Jordstykke stormfald

registrering af udbetalt tilskud til oprydning eller gentilplantning af private fredskove, der er væltet som følge af storme.

### Semantic Template
```python
p.io.declare_input(
    output_name="jordstykke_stormfald",
    attributes={
        "betalingsdato": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": "tidspunkt hvor udbetaling af stormfaldstilskud er startet"
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
        "feltliste": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": ""
        },
        "jordstykkeobjectid": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(int),
            "description": ""
        },
        "objectid": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(int),
            "description": ""
        },
        "omfang": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.mat.lookups.omfang, str),
            "description": "angiver hvor stor en del af jordstykket der er omfattet af registreringen"
        },
        "ophoersdato": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": "tidspunkt hvor udbetaling af stormfaldstilskud er ophørt"
        },
        "snsjournalnummer": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": "det af Naturstyrelsen angivne journalnummer på en stormfaldssag"
        },
        "tilskudstype": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.mat.lookups.tilskudstype, str),
            "description": "typen af tilskud det registrerede stormfald er omfattet af"
        },
    }
)
```
