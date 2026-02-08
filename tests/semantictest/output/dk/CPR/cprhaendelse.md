---
title: Cprhaendelse
draft: false
type: entity
---

# Cprhaendelse

Oplysninger om de hændelser, en person registreret i CPR er berørt af. Fx vielse eller navneændring. Leveres for hver hændelse personen er berørt af i dagens løb.

### Semantic Template
```python
p.io.declare_input(
    output_name="cprhaendelse",
    attributes={
        "afledtmarkering": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.cpr.lookups.discretetruth, bool),
            "description": "Angiver, at hændelsen er sket afledt som følge af en hændelse indrapporteret på en anden person. fx: ved en vielse er hændelsen på kvinden den primære hændelse mens hændelsen på manden er en afledt hændelse."
        },
        "afleveringsdato": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(datetime),
            "description": "Tidspunkt for aflevering af data for personen til datafordeler."
        },
        "cprkommunekodenuvaerende": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": ""
        },
        "cprkommunekodetidligere": {
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
        "forretningshaendelse": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.cpr.lookups.forretningshaendelse, str),
            "description": "Angiver forretningshaendelse for haendelsen"
        },
        "forretningshaendelseid": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": ""
        },
        "forretningsomraade": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": "Det forretningsområde hændelsen er sket inden for."
        },
        "personid": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": ""
        },
        "rettetden": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(datetime),
            "description": "Tidspunkt for hvornår personen er blevet berørt af hændelsen."
        },
    }
)
```
