---
title: SocialØkonomiskVirksomhed
draft: false
type: entity
---

# SocialØkonomiskVirksomhed

Ingen definition tilgængelig.

### Semantic Template
```python
p.io.declare_input(
    output_name="socialøkonomiskvirksomhed",
    attributes={
        "ieftilsyn": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.FK(dk.CentraleVirksomhedsregister.IEFTilsyn, str),
            "cardinality": "1..1",
            "description": ""
        },
        "ieftilsyntekst": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.FK(dk.CentraleVirksomhedsregister.IEFTilsynTekst, str),
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