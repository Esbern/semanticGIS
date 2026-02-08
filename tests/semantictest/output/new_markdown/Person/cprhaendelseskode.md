---
title: CprHaendelseskode
draft: false
type: entity
---

# CprHaendelseskode

oplysninger om de hændelseskoder, en person registreret i CPR er berørt af. Fx vielse eller navneændring. Leveres for hver hændelse personen er berørt af i dagens løb

### Semantic Template
```python
p.io.declare_input(
    output_name="cprhaendelseskode",
    attributes={
        "registreringfra": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(datetime),
            "cardinality": "1..1",
            "description": "tidspunkt for hvornår personen er blevet berørt af hændelsen"
        },
        "virkningfra": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(date),
            "cardinality": "1..1",
            "description": "startdato for hændelsen"
        },
        "afledtmrk": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "0..1",
            "description": "angiver en værdimængde, der beskriver at hændelsen er sket afledt som følge af en hændelse indrapporteret på en anden person. fx: ved en vielse er hændelsen på kvinden den primære hændelse mens hændelsen på manden er en afledt hændelse"
        },
        "kode": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "1..1",
            "description": "angiver en kode der definerer hændelsen"
        },
        "cprhaendelseskode": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.FK(dk.Person.Cprhaendelse, str),
            "cardinality": "0..*",
            "description": ""
        },
        "person": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.FK(dk.Person.Person, str),
            "cardinality": "0..*",
            "description": ""
        }
    }
)
```