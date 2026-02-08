---
title: SkatteforvaltningVirksomhed
draft: false
type: entity
---

# SkatteforvaltningVirksomhed

Ingen definition tilgængelig.

### Semantic Template
```python
p.io.declare_input(
    output_name="skatteforvaltningvirksomhed",
    attributes={
        "bibranche1": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "0..1",
            "description": ""
        },
        "bibranche2": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "0..1",
            "description": ""
        },
        "bibranche3": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "0..1",
            "description": ""
        },
        "cvrnummer": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "0..1",
            "description": ""
        },
        "hovedbranche": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "0..1",
            "description": ""
        },
        "senummer": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "1..1",
            "description": ""
        },
        "virksomhedstype": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.SkatteforvaltningensVirksomhedsregister.VirksomhedType, str),
            "cardinality": "1..1",
            "description": ""
        },
        "virksomhedstypetekst": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "1..1",
            "description": ""
        },
        "virksomhedejer": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.FK(dk.SkatteforvaltningensVirksomhedsregister.VirksomhedEjer, str),
            "cardinality": "1..*",
            "description": ""
        },
        "virksomhednavn": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.FK(dk.SkatteforvaltningensVirksomhedsregister.VirksomhedNavn, str),
            "cardinality": "1..1",
            "description": ""
        },
        "virksomhedledelse": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.FK(dk.SkatteforvaltningensVirksomhedsregister.VirksomhedLedelse, str),
            "cardinality": "1..*",
            "description": ""
        },
        "virksomhedregistreringsstatus": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.FK(dk.SkatteforvaltningensVirksomhedsregister.VirksomhedRegistreringStatus, str),
            "cardinality": "1..1",
            "description": ""
        },
        "virksomheddriftform": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.FK(dk.SkatteforvaltningensVirksomhedsregister.VirksomhedDriftform, str),
            "cardinality": "1..1",
            "description": ""
        },
        "virksomhedhenvisning": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.FK(dk.SkatteforvaltningensVirksomhedsregister.VirksomhedHenvisning, str),
            "cardinality": "0..*",
            "description": ""
        },
        "adresse": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.FK(dk.DanmarksAdresser.Adresse, str),
            "cardinality": "0..*",
            "description": ""
        },
        "myndighed": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.FK(dk.SkatteforvaltningensVirksomhedsregister.Myndighed, str),
            "cardinality": "1..*",
            "description": ""
        },
        "virksomhed": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.FK(dk.CentraleVirksomhedsregister.Virksomhed, str),
            "cardinality": "0..1",
            "description": ""
        },
        "virksomhedtelefon": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.FK(dk.SkatteforvaltningensVirksomhedsregister.VirksomhedTelefon, str),
            "cardinality": "0..*",
            "description": ""
        },
        "virksomhedstatus": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.FK(dk.SkatteforvaltningensVirksomhedsregister.VirksomhedKreditStatus, str),
            "cardinality": "0..*",
            "description": ""
        },
        "e_mailadresse": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.FK(dk.SkatteforvaltningensVirksomhedsregister.E-mailadresse, str),
            "cardinality": "0..*",
            "description": ""
        },
        "virksomhedadresse": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.FK(dk.SkatteforvaltningensVirksomhedsregister.VirksomhedAdresse, str),
            "cardinality": "0..*",
            "description": ""
        },
        "annulleringskode": {
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
        "registreringfra": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(date),
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
            "role": sg.DES(date),
            "cardinality": "1..1",
            "description": ""
        },
        "status": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.SkatteforvaltningensVirksomhedsregister.Status, str),
            "cardinality": "1..1",
            "description": ""
        },
        "virkningfra": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(date),
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
            "role": sg.DES(date),
            "cardinality": "1..1",
            "description": ""
        }
    }
)
```