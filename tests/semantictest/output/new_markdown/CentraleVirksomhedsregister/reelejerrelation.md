---
title: ReelEjerRelation
draft: false
type: entity
---

# ReelEjerRelation

Ingen definition tilgængelig.

### Semantic Template
```python
p.io.declare_input(
    output_name="reelejerrelation",
    attributes={
        "begunstigetgruppe": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.FK(dk.CentraleVirksomhedsregister.BegunstigetGruppe, str),
            "cardinality": "0..1",
            "description": ""
        },
        "srligeejerforhold": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.FK(dk.CentraleVirksomhedsregister.SærligeEjerforhold, str),
            "cardinality": "0..*",
            "description": ""
        },
        "begunstigetretskrav": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.FK(dk.CentraleVirksomhedsregister.BegunstigetRetskrav, str),
            "cardinality": "0..1",
            "description": ""
        },
        "betydeligindflydelseviarolle": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.FK(dk.CentraleVirksomhedsregister.BetydeligIndflydelseViaRolle, str),
            "cardinality": "0..*",
            "description": ""
        },
        "srligeejerforholdbeskrivelse": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.FK(dk.CentraleVirksomhedsregister.SærligeEjerforholdBeskrivelse, str),
            "cardinality": "0..1",
            "description": ""
        },
        "reelejerandelstemmeretprocent": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.FK(dk.CentraleVirksomhedsregister.ReelEjerAndelStemmeretProcent, str),
            "cardinality": "0..1",
            "description": ""
        },
        "reelejerandelkapitalklasse": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.FK(dk.CentraleVirksomhedsregister.ReelEjerAndelKapitalklasse, str),
            "cardinality": "0..1",
            "description": ""
        },
        "reelejerandelprocent": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.FK(dk.CentraleVirksomhedsregister.ReelEjerAndelProcent, str),
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