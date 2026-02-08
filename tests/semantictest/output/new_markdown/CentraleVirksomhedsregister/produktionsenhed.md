---
title: Produktionsenhed
draft: false
type: entity
---

# Produktionsenhed

Ingen definition tilgængelig.

### Semantic Template
```python
p.io.declare_input(
    output_name="produktionsenhed",
    attributes={
        "pnummer": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(int),
            "cardinality": "1..1",
            "description": ""
        },
        "beskftigelse": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.FK(dk.CentraleVirksomhedsregister.Beskæftigelse, str),
            "cardinality": "0..*",
            "description": ""
        },
        "telefax": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.FK(dk.CentraleVirksomhedsregister.Telefax, str),
            "cardinality": "0..1",
            "description": ""
        },
        "reklamebeskyttet": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.FK(dk.CentraleVirksomhedsregister.Reklamebeskyttet, str),
            "cardinality": "1..1",
            "description": ""
        },
        "cvradresse": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.FK(dk.CentraleVirksomhedsregister.CVRAdresse, str),
            "cardinality": "0..1",
            "description": ""
        },
        "telefon": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.FK(dk.CentraleVirksomhedsregister.Telefon, str),
            "cardinality": "0..1",
            "description": ""
        },
        "email": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.FK(dk.CentraleVirksomhedsregister.Email, str),
            "cardinality": "0..1",
            "description": ""
        },
        "navn": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.FK(dk.CentraleVirksomhedsregister.Navn, str),
            "cardinality": "1..1",
            "description": ""
        },
        "branche": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.FK(dk.CentraleVirksomhedsregister.Branche, str),
            "cardinality": "0..3",
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