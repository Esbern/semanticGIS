---
title: UdrejseIndrejse
draft: false
type: entity
---

# UdrejseIndrejse

oplysning om førstegangsindrejse, udrejse og eventuel genindrejse

### Semantic Template
```python
p.io.declare_input(
    output_name="udrejseindrejse",
    attributes={
        "virkningfra": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(date),
            "cardinality": "0..1",
            "description": "dato for personens udrejse"
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
            "cardinality": "0..1",
            "description": "dato for personens genindrejse"
        },
        "virkningtilusikkerhedsmarkering": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "0..1",
            "description": "angiver at virkningTil er usikker"
        },
        "udlandsadresselinje1": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "0..1",
            "description": "ikke krævet og ikke nogen krav til specifikt indhold"
        },
        "status": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.Person.Status, str),
            "cardinality": "1..1",
            "description": "angiver status for UdrejseIndrejse"
        },
        "udlandsadresselinje2": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "0..1",
            "description": "ikke krævet og ikke nogen krav til specifikt indhold"
        },
        "registreringfra": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(datetime),
            "cardinality": "1..1",
            "description": "dato for startoplysninger"
        },
        "udlandsadresselinje3": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "0..1",
            "description": "ikke krævet og ikke nogen krav til specifikt indhold"
        },
        "udlandsadresselinje4": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "0..1",
            "description": "ikke krævet og ikke nogen krav til specifikt indhold"
        },
        "udlandsadresselinje5": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "0..1",
            "description": "ikke krævet og ikke nogen krav til specifikt indhold"
        },
        "cprlandudrejse": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.FK(dk.Person.AdministrativEnhed, str),
            "cardinality": "0..1",
            "description": ""
        },
        "cprlandindrejse": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.FK(dk.Person.AdministrativEnhed, str),
            "cardinality": "0..1",
            "description": ""
        }
    }
)
```