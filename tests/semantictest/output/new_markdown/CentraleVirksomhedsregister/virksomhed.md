---
title: Virksomhed
draft: false
type: entity
---

# Virksomhed

Ingen definition tilgængelig.

### Semantic Template
```python
p.io.declare_input(
    output_name="virksomhed",
    attributes={
        "cvrnummer": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(int),
            "cardinality": "1..1",
            "description": ""
        },
        "stiftetfr1900": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.FK(dk.CentraleVirksomhedsregister.StiftetFør1900, str),
            "cardinality": "0..1",
            "description": ""
        },
        "stifterrelation": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.FK(dk.CentraleVirksomhedsregister.StifterRelation, str),
            "cardinality": "1..*",
            "description": ""
        },
        "fondsmyndighedtilladelse": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.FK(dk.CentraleVirksomhedsregister.FondsmyndighedTilladelse, str),
            "cardinality": "0..1",
            "description": ""
        },
        "formal": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.FK(dk.CentraleVirksomhedsregister.Formål, str),
            "cardinality": "0..1",
            "description": ""
        },
        "virksomhedstatus": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.FK(dk.CentraleVirksomhedsregister.Virksomhedstatus, str),
            "cardinality": "1..1",
            "description": ""
        },
        "kapitalforhold": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.FK(dk.CentraleVirksomhedsregister.Kapitalforhold, str),
            "cardinality": "0..1",
            "description": ""
        },
        "virksomhedform": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.FK(dk.CentraleVirksomhedsregister.Virksomhedform, str),
            "cardinality": "1..1",
            "description": ""
        },
        "finansiel": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.FK(dk.CentraleVirksomhedsregister.Finansiel, str),
            "cardinality": "0..1",
            "description": ""
        },
        "tegningsregel": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.FK(dk.CentraleVirksomhedsregister.Tegningsregel, str),
            "cardinality": "0..1",
            "description": ""
        },
        "hjemmeside": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.FK(dk.CentraleVirksomhedsregister.Hjemmeside, str),
            "cardinality": "0..1",
            "description": ""
        },
        "fuldtansvarligdeltagerrelation": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.FK(dk.CentraleVirksomhedsregister.FuldtAnsvarligDeltagerRelation, str),
            "cardinality": "0..*",
            "description": ""
        },
        "ansvarligdataleverandr": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.FK(dk.CentraleVirksomhedsregister.AnsvarligDataleverandør, str),
            "cardinality": "1..1",
            "description": ""
        },
        "beskftigelse": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.FK(dk.CentraleVirksomhedsregister.Beskæftigelse, str),
            "cardinality": "0..*",
            "description": ""
        },
        "hvidvaskrelation": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.FK(dk.CentraleVirksomhedsregister.HvidvaskRelation, str),
            "cardinality": "0..*",
            "description": ""
        },
        "koncession": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.FK(dk.CentraleVirksomhedsregister.Koncession, str),
            "cardinality": "0..1",
            "description": ""
        },
        "stadfstelse": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.FK(dk.CentraleVirksomhedsregister.Stadfæstelse, str),
            "cardinality": "0..1",
            "description": ""
        },
        "revision": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.FK(dk.CentraleVirksomhedsregister.Revision, str),
            "cardinality": "0..1",
            "description": ""
        },
        "hovedselskabrelation": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.FK(dk.CentraleVirksomhedsregister.HovedselskabRelation, str),
            "cardinality": "0..1",
            "description": ""
        },
        "binavn": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.FK(dk.CentraleVirksomhedsregister.Navn, str),
            "cardinality": "0..*",
            "description": ""
        },
        "kreditoplysning": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.FK(dk.CentraleVirksomhedsregister.Kreditoplysning, str),
            "cardinality": "0..1",
            "description": ""
        },
        "ledelse": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.FK(dk.CentraleVirksomhedsregister.Ledelse, str),
            "cardinality": "0..1",
            "description": ""
        },
        "socialkonomiskvirksomhed": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.FK(dk.CentraleVirksomhedsregister.SocialØkonomiskVirksomhed, str),
            "cardinality": "0..1",
            "description": ""
        },
        "produktionsenhedrelation": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.FK(dk.CentraleVirksomhedsregister.ProduktionsenhedRelation, str),
            "cardinality": "1..*",
            "description": ""
        },
        "myndighedanden": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.FK(dk.CentraleVirksomhedsregister.MyndighedAnden, str),
            "cardinality": "0..1",
            "description": ""
        },
        "brsnoteret": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.FK(dk.CentraleVirksomhedsregister.Børsnoteret, str),
            "cardinality": "0..1",
            "description": ""
        },
        "hvidvaskogterrorfinansiering": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.FK(dk.CentraleVirksomhedsregister.HvidvaskOgTerrorfinansiering, str),
            "cardinality": "0..1",
            "description": ""
        },
        "ejerforhold": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.FK(dk.CentraleVirksomhedsregister.Ejerforhold, str),
            "cardinality": "1..1",
            "description": ""
        },
        "statslig": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.FK(dk.CentraleVirksomhedsregister.Statslig, str),
            "cardinality": "0..1",
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