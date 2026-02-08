---
title: Ejendomsbeliggenhed
draft: false
type: entity
---

# Ejendomsbeliggenhed

Ingen definition tilgængelig.

### Semantic Template
```python
p.io.declare_input(
    output_name="ejendomsbeliggenhed",
    attributes={
        "adressemanueltangivet": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "1..1",
            "description": ""
        },
        "betegnelse": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "0..1",
            "description": ""
        },
        "esdhreferencekommune": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "0..1",
            "description": ""
        },
        "esdhreferenceadresse": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "0..1",
            "description": ""
        },
        "kommunemanueltangivet": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "1..1",
            "description": ""
        },
        "id_lokalid": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.PK(str),
            "cardinality": "1..1",
            "description": ""
        },
        "virkningfra": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(datetime),
            "cardinality": "1..1",
            "description": ""
        },
        "virkningtil": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(datetime),
            "cardinality": "0..1",
            "description": ""
        },
        "virkningsaktr": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "1..1",
            "description": ""
        },
        "forretningshndelse": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.Ejendomsbeliggenhed.EjendomsbeliggenhedForretningshændelsesVærdi, str),
            "cardinality": "1..1",
            "description": ""
        },
        "registreringfra": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(datetime),
            "cardinality": "1..1",
            "description": ""
        },
        "registreringtil": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(datetime),
            "cardinality": "0..1",
            "description": ""
        },
        "registreringsaktr": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "1..1",
            "description": ""
        },
        "forretningsomrade": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.Ejendomsbeliggenhed.EjendomsbeliggenhedForretningsområde, str),
            "cardinality": "1..1",
            "description": ""
        },
        "status": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.Ejendomsbeliggenhed.EjendomsbeliggenhedStatusVærdi, str),
            "cardinality": "1..1",
            "description": ""
        },
        "forretningsproces": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.Ejendomsbeliggenhed.EjendomsbeliggenhedForretningsprocesVærdi, str),
            "cardinality": "1..1",
            "description": ""
        },
        "bestemtfastejendom": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.FK(dk.Matrikel.BestemtFastEjendom, str),
            "cardinality": "1..1",
            "description": ""
        },
        "husnummer": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.FK(dk.DanmarksAdresser.Husnummer, str),
            "cardinality": "0..1",
            "description": ""
        },
        "adresse": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.FK(dk.DanmarksAdresser.Adresse, str),
            "cardinality": "0..1",
            "description": ""
        },
        "kommuneinddeling": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.FK(dk.Matrikel.MatrikelKommune, str),
            "cardinality": "1..1",
            "description": ""
        }
    }
)
```