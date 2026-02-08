---
title: Vaergemaal
draft: false
type: entity
---

# Vaergemaal

oplysninger om personer under værgemål efter værgemålslovens paragraf 6. Kan indeholde oplysning om relation til værge personnummer eller adressat

### Semantic Template
```python
p.io.declare_input(
    output_name="vaergemaal",
    attributes={
        "vaergenavn": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "0..1",
            "description": "navn på værge hvis det er en virksomhed"
        },
        "virkningfra": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(date),
            "cardinality": "1..1",
            "description": "dato for værgemål"
        },
        "virkningfrausikkerhedsmarkering": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "0..1",
            "description": "angiver at virkningFra er usikker"
        },
        "virkningtil": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(date),
            "cardinality": "0..0",
            "description": "slutdato for værgemål"
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
        "adresselinje5": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "0..1",
            "description": "ikke krævet og ikke nogen krav til specifikt indhold"
        },
        "vaergemaalstype": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.Person.Vaergemaalstype, str),
            "cardinality": "1..1",
            "description": "angiver vaergemaalstype for Vaergemaal"
        },
        "status": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.Person.Status, str),
            "cardinality": "1..1",
            "description": "status for oplysningen"
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