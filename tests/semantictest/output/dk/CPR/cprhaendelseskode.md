---
title: CprHaendelseskode
draft: false
type: entity
---

# CprHaendelseskode

Oplysninger om de hændelseskoder, en person registreret i CPR er berørt af. Fx vielse eller navneændring. Leveres for hver hændelse personen er berørt af i dagens løb.

### Semantic Template
```python
p.io.declare_input(
    output_name="cprhaendelseskode",
    attributes={
        "afledtmrk": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(bool),
            "description": "Angiver en værdimængde, der beskriver at hændelsen er sket afledt som følge af en hændelse indrapporteret på en anden person. fx: ved en vielse er hændelsen på kvinden den primære hændelse mens hændelsen på manden er en afledt hændelse."
        },
        "cprhaendelseskodeid": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": ""
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
        "kode": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": "Angiver en kode der definerer hændelsen."
        },
        "personid": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": ""
        },
        "registreringfra": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(datetime),
            "description": ""
        },
        "virkningfra": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": ""
        },
    }
)
```
