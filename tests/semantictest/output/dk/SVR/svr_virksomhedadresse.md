---
title: svr virksomhedadresse
draft: false
type: entity
---

# svr virksomhedadresse

Ingen definition fundet

### Semantic Template
```python
p.io.declare_input(
    output_name="svr_virksomhedadresse",
    attributes={
        "adresseformat": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.svr.lookups.virksomhedadresseformat, str),
            "description": "Ingen definition fundet"
        },
        "adresseformattekst": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": ""
        },
        "adresselobenummer": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": ""
        },
        "adressetype": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": ""
        },
        "adressetypetekst": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": ""
        },
        "annulleringskode": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(int),
            "description": "Ingen definition fundet"
        },
        "bynavn": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": "Ingen definition fundet"
        },
        "conavn": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": ""
        },
        "datafordeleropdateringstid": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(datetime),
            "description": ""
        },
        "datafordelerregisterimportsequencenumber": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(int),
            "description": ""
        },
        "datafordelerrowid": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": ""
        },
        "datafordelerrowversion": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(int),
            "description": ""
        },
        "dorbetegnelse": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": ""
        },
        "etagebetegnelse": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": "Ingen definition fundet"
        },
        "husbogstavfra": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": ""
        },
        "husbogstavtil": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": ""
        },
        "husnummerfra": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": ""
        },
        "husnummertil": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": ""
        },
        "landenavn": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.svr.lookups.countrycode, str),
            "description": "Ingen definition fundet"
        },
        "landenavnkort": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": ""
        },
        "lokalid": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": ""
        },
        "lokaltstednavn": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": ""
        },
        "namespace": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": ""
        },
        "postboksnummer": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(int),
            "description": ""
        },
        "postnummer": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(int),
            "description": "Ingen definition fundet"
        },
        "registreringfra": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": ""
        },
        "registreringsaktor": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": ""
        },
        "registreringtil": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": ""
        },
        "senummer": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(int),
            "description": ""
        },
        "status": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.svr.lookups.status, str),
            "description": "Ingen definition fundet"
        },
        "supplerendebynavn": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": ""
        },
        "udenlandskadresselinje1": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": ""
        },
        "udenlandskadresselinje2": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": ""
        },
        "vejnavn": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": "Ingen definition fundet"
        },
        "virkningfra": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": ""
        },
        "virkningsaktor": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": ""
        },
        "virkningtil": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": ""
        },
    }
)
```
