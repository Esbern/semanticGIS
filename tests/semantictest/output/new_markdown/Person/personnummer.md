---
title: Personnummer
draft: false
type: entity
---

# Personnummer

entydig Identifikation af en person i CPR. Indeholder information om fødselsdato, køn og århunderede. Et personnummer kan ændres, hvis data i nummeret ændres, eller når der konstateres at en person har flere personnumre

### Semantic Template
```python
p.io.declare_input(
    output_name="personnummer",
    attributes={
        "personnummer": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "1..1",
            "description": "indeholder information om fødselsdato, køn og århundrede"
        },
        "virkningfra": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(date),
            "cardinality": "1..1",
            "description": "dato for tildeling af personnummer"
        },
        "virkningfrausikkerhedsmarkering": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "1..1",
            "description": "angiver at virkningFra er usikker"
        },
        "virkningtil": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(date),
            "cardinality": "1..1",
            "description": "dato for, at personnummeret ikke længere er gyldigt. Ved ændring af fødselsdato, køn eller dobbeltnummer (personen er tildelt 2 personnumre ved en fejl)"
        },
        "virkningtilusikkerhedsmarkering": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "1..1",
            "description": "angiver at virkningTil er usikker"
        },
        "status": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.Person.Status, str),
            "cardinality": "1..1",
            "description": "status på cprnummer"
        },
        "registreringfra": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(datetime),
            "cardinality": "0..0",
            "description": "dato for startoplysninger"
        }
    }
)
```