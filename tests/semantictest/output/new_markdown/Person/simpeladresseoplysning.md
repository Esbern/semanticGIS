---
title: SimpelAdresseoplysning
draft: false
type: entity
---

# SimpelAdresseoplysning

adresse i klartekst

### Semantic Template
```python
p.io.declare_input(
    output_name="simpeladresseoplysning",
    attributes={
        "virkningfra": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(date),
            "cardinality": "1..1",
            "description": "startdato for kontaktadressen"
        },
        "virkningtil": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(date),
            "cardinality": "0..0",
            "description": "slutdato for adresseoplysningen"
        },
        "adresselinje1": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "0..1",
            "description": "ikke krævet og ikke nogen krav til specifikt indhold"
        },
        "adresselinje2": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "0..1",
            "description": "ikke krævet og ikke nogen krav til specifikt indhold"
        },
        "adresselinje3": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "0..1",
            "description": "ikke krævet og ikke nogen krav til specifikt indhold"
        },
        "adresselinje4": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "0..1",
            "description": "ikke krævet og ikke nogen krav til specifikt indhold"
        },
        "status": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.Person.Status, str),
            "cardinality": "1..1",
            "description": "status for oplysningen"
        },
        "adresselinje5": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "0..1",
            "description": "ikke krævet og ikke nogen krav til specifikt indhold"
        },
        "registreringfra": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(datetime),
            "cardinality": "0..0",
            "description": "dato for startoplysninger"
        },
        "startmyndighed": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.FK(dk.Person.AdministrativEnhed, str),
            "cardinality": "1..1",
            "description": ""
        }
    }
)
```