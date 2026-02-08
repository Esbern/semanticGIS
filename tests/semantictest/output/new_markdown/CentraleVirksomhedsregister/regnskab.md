---
title: Regnskab
draft: false
type: entity
---

# Regnskab

Ingen definition tilgængelig.

### Semantic Template
```python
p.io.declare_input(
    output_name="regnskab",
    attributes={
        "omlgningsperiodeslut": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.FK(dk.CentraleVirksomhedsregister.OmlægningsperiodeSlut, str),
            "cardinality": "0..1",
            "description": ""
        },
        "frsteregnskabsperiodestart": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.FK(dk.CentraleVirksomhedsregister.FørsteRegnskabsperiodeStart, str),
            "cardinality": "1..1",
            "description": ""
        },
        "regnskabsarstart": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.FK(dk.CentraleVirksomhedsregister.RegnskabsårStart, str),
            "cardinality": "1..1",
            "description": ""
        },
        "tilsynkategori": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.FK(dk.CentraleVirksomhedsregister.TilsynKategori, str),
            "cardinality": "0..1",
            "description": ""
        },
        "omlgningsperiodestart": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.FK(dk.CentraleVirksomhedsregister.OmlægningsperiodeStart, str),
            "cardinality": "0..1",
            "description": ""
        },
        "regnskabsarfritekst": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.FK(dk.CentraleVirksomhedsregister.RegnskabsårFritekst, str),
            "cardinality": "0..1",
            "description": ""
        },
        "regnskabsarslut": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.FK(dk.CentraleVirksomhedsregister.RegnskabsårSlut, str),
            "cardinality": "1..1",
            "description": ""
        },
        "frsteregnskabsperiodeslut": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.FK(dk.CentraleVirksomhedsregister.FørsteRegnskabsperiodeSlut, str),
            "cardinality": "1..1",
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