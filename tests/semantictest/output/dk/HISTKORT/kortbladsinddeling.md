---
title: Kortbladsinddeling
draft: false
type: entity
---

# Kortbladsinddeling

geografisk afgrænsning af tegnede eller trykte kort. Kortbladsinddelingen er unik for hvert kortværk

### Semantic Template
```python
p.io.declare_input(
    output_name="kortbladsinddeling",
    attributes={
        "bemaerkning": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": "kommentarer til en version af kortet"
        },
        "daekningomraade": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.histkort.lookups.dækningsområdeværdi, str),
            "description": "dækningsområde for kortværket"
        },
        "datafordeleropdateringstid": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(datetime),
            "description": ""
        },
        "forretningshaendelse": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.histkort.lookups.kortbladsinddelingforretningshændelseværdi, str),
            "description": "den begivenhed i virkeligheden som udløste ændringen i data"
        },
        "forretningsomraade": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.histkort.lookups.kortbladsinddelingforretningsområdeværdi, str),
            "description": "den del af den offentlige forretning der håndterer hændelsen og derved udvirker ændringen i data"
        },
        "forretningsproces": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.histkort.lookups.kortbladsinddelingforretningsprocesværdi, str),
            "description": "den manuelle eller IT-understøttede proces hvori forretningsområdet håndterer hændelsen"
        },
        "geometri": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.histkort.lookups.gm_surface, str),
            "description": "objektets geografiske placering"
        },
        "gmlid": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": ""
        },
        "hkpnlink": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.histkort.lookups.uri, str),
            "description": "hyperlink til kortet på Historiske Kort På Nettet (hkpn.dk)"
        },
        "id_lokalid": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.PK(str),
            "description": ""
        },
        "id_namespace": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": ""
        },
        "kode": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": "versionsnummer for kortet"
        },
        "kortbladnummer": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": "nummerering eller benævnelse for kortbladet. Kortbladsnummeret angiver et geografisk område indenfor kortbladsinddelingen"
        },
        "kortvaerk": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.histkort.lookups.kortværkværdi, str),
            "description": "navn på et historisk kortværk"
        },
        "maalestok": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.histkort.lookups.målestokværdi, str),
            "description": "størrelsesforholdet mellem landskabet og kortets repræsentation heraf"
        },
        "maalt_aar": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(int),
            "description": ""
        },
        "navn": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": "egennavn for den administrative inddeling"
        },
        "objectid": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": ""
        },
        "orginalkortprojektion": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": "projektion det oprindelige kort blev defineret i"
        },
        "originalehjoernekoordinater": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": "hjørnekoordinaterne i den oprindelige kortprojektion"
        },
        "registreringfra": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(datetime),
            "description": "tidspunktet hvor registreringen er foretaget"
        },
        "registreringsaktoer": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": "den aktør der har foretaget registreringen"
        },
        "registreringtil": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(datetime),
            "description": "tidspunktet hvor en ny registrering er foretaget på objektet, og hvor denne version således ikke længere er den seneste"
        },
        "sidstrettet_aar": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(int),
            "description": ""
        },
        "status": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.histkort.lookups.kortbladsinddelingstatusværdi, str),
            "description": "angivelse af hvor et forvaltningsobjekt er i sin livscyklus"
        },
        "udgivet_aar": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(int),
            "description": ""
        },
        "virkningfra": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(datetime),
            "description": "tidspunktet hvorfra objektet har virkning"
        },
        "virkningsaktoer": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": "den aktør der har afstedkommet objektets virkning"
        },
        "virkningtil": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(datetime),
            "description": "tidspunktet hvor objektets virkning ophører"
        },
    }
)
```
