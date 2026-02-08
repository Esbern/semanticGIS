---
title: LegalEjerRelation
draft: false
type: entity
---

# LegalEjerRelation

Ingen definition tilgængelig.

### Semantic Template
```python
p.io.declare_input(
    output_name="legalejerrelation",
    attributes={
        "legalejerandelsompantstemmeretprocent": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.FK(dk.CentraleVirksomhedsregister.LegalEjerAndelSomPantStemmeretProcent, str),
            "cardinality": "0..1",
            "description": ""
        },
        "legalejerandelprocentsompant": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.FK(dk.CentraleVirksomhedsregister.LegalEjerAndelProcentSomPant, str),
            "cardinality": "0..1",
            "description": ""
        },
        "legalejerandelmeddelelsedato": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.FK(dk.CentraleVirksomhedsregister.LegalEjerAndelMeddelelseDato, str),
            "cardinality": "0..1",
            "description": ""
        },
        "legalejerandelkapitalklasse": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.FK(dk.CentraleVirksomhedsregister.LegalEjerAndelKapitalklasse, str),
            "cardinality": "0..1",
            "description": ""
        },
        "legalejerandelprocent": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.FK(dk.CentraleVirksomhedsregister.LegalEjerAndelProcent, str),
            "cardinality": "0..1",
            "description": ""
        },
        "legalejerandelstemmeretprocent": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.FK(dk.CentraleVirksomhedsregister.LegalEjerAndelStemmeretProcent, str),
            "cardinality": "0..1",
            "description": ""
        },
        "cvrenhed": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.FK(dk.CentraleVirksomhedsregister.CVREnhed, str),
            "cardinality": "1..*",
            "description": ""
        },
        "id_lokalid": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.PK(str),
            "cardinality": "1..1",
            "description": ""
        },
        "registreringfra": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(datetime),
            "cardinality": "1..1",
            "description": ""
        },
        "registreringsaktr": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "1..1",
            "description": ""
        },
        "registreringtil": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(datetime),
            "cardinality": "0..1",
            "description": ""
        },
        "status": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.CentraleVirksomhedsregister.StatusType, str),
            "cardinality": "1..1",
            "description": ""
        },
        "virkningfra": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(datetime),
            "cardinality": "1..1",
            "description": ""
        },
        "virkningsaktr": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "1..1",
            "description": ""
        },
        "virkningtil": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(datetime),
            "cardinality": "0..1",
            "description": ""
        }
    }
)
```