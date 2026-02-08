---
title: Cprhaendelse
draft: false
type: entity
---

# Cprhaendelse

oplysninger om de hændelser, en person registreret i CPR er berørt af. Fx vielse eller navneændring. Leveres for hver hændelse personen er berørt af i dagens løb

### Semantic Template
```python
p.io.declare_input(
    output_name="cprhaendelse",
    attributes={
        "afledtmarkering": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "1..1",
            "description": "angiver, at hændelsen er sket afledt som følge af en hændelse indrapporteret på en anden person. fx: ved en vielse er hændelsen på kvinden den primære hændelse mens hændelsen på manden er en afledt hændelse"
        },
        "afleveringsdato": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(datetime),
            "cardinality": "1..1",
            "description": "tidspunkt for aflevering af data for personen til datafordeler"
        },
        "forretningsomraade": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "1..1",
            "description": "det forretningsområde hændelsen er sket inden for"
        },
        "rettetden": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(datetime),
            "cardinality": "1..1",
            "description": "tidspunkt for hvornår personen er blevet berørt af hændelsen"
        },
        "forretningshaendelse": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.Person.Forretningshaendelse, str),
            "cardinality": "1..1",
            "description": "angiver forretningshaendelse for haendelsen"
        },
        "cprhaendelse": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.FK(dk.Person.CprHaendelseskode, str),
            "cardinality": "0..*",
            "description": ""
        },
        "person": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.FK(dk.Person.Person, str),
            "cardinality": "1..1",
            "description": ""
        }
    }
)
```