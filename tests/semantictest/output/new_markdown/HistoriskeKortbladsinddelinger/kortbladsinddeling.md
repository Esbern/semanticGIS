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
        "id_lokalid": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.PK(str),
            "cardinality": "1..1",
            "description": "persistent unik nøgle"
        },
        "virkningfra": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(datetime),
            "cardinality": "1..1",
            "description": "tidspunktet hvorfra objektet har virkning"
        },
        "virkningtil": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(datetime),
            "cardinality": "0..1",
            "description": "tidspunktet hvor objektets virkning ophører"
        },
        "virkningsaktr": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "1..1",
            "description": "den aktør der har afstedkommet objektets virkning"
        },
        "forretningshndelse": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.HistoriskeKortbladsinddelinger.KortbladsinddelingForretningshændelseVærdi, str),
            "cardinality": "1..1",
            "description": "den begivenhed i virkeligheden som udløste ændringen i data"
        },
        "registreringfra": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(datetime),
            "cardinality": "1..1",
            "description": "tidspunktet hvor registreringen er foretaget"
        },
        "registreringtil": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(datetime),
            "cardinality": "0..1",
            "description": "tidspunktet hvor en ny registrering er foretaget på objektet, og hvor denne version således ikke længere er den seneste"
        },
        "registreringsaktr": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "1..1",
            "description": "den aktør der har foretaget registreringen"
        },
        "forretningsomrade": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.HistoriskeKortbladsinddelinger.KortbladsinddelingForretningsområdeVærdi, str),
            "cardinality": "1..1",
            "description": "den del af den offentlige forretning der håndterer hændelsen og derved udvirker ændringen i data"
        },
        "status": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.HistoriskeKortbladsinddelinger.KortbladsinddelingStatusVærdi, str),
            "cardinality": "1..1",
            "description": "angivelse af hvor et forvaltningsobjekt er i sin livscyklus"
        },
        "forretningsproces": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.HistoriskeKortbladsinddelinger.KortbladsinddelingForretningsprocesVærdi, str),
            "cardinality": "1..1",
            "description": "den manuelle eller IT-understøttede proces hvori forretningsområdet håndterer hændelsen"
        },
        "dkningomrade": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.HistoriskeKortbladsinddelinger.DækningsområdeVærdi, str),
            "cardinality": "1..1",
            "description": "dækningsområde for kortværket"
        },
        "kortvrk": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.HistoriskeKortbladsinddelinger.KortværkVærdi, str),
            "cardinality": "1..1",
            "description": "navn på et historisk kortværk"
        },
        "navn": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "1..1",
            "description": "egennavn for den administrative inddeling"
        },
        "geometri": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "1..1",
            "description": "objektets geografiske placering"
        },
        "orginalkortprojektion": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "1..1",
            "description": "projektion det oprindelige kort blev defineret i"
        },
        "originalehjrnekoordinater": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "1..1",
            "description": "hjørnekoordinaterne i den oprindelige kortprojektion"
        },
        "kode": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "0..1",
            "description": "versionsnummer for kortet"
        },
        "malestok": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.HistoriskeKortbladsinddelinger.MålestokVærdi, str),
            "cardinality": "1..1",
            "description": "størrelsesforholdet mellem landskabet og kortets repræsentation heraf"
        },
        "malt": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "0..1",
            "description": "opmålingsår for kortet. Kortet kan senere være nymålt eller rettet"
        },
        "kortbladnummer": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "1..1",
            "description": "nummerering eller benævnelse for kortbladet. Kortbladsnummeret angiver et geografisk område indenfor kortbladsinddelingen"
        },
        "sidstrettet": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "0..1",
            "description": "årstal for seneste rettelse af kortet"
        },
        "udgivet": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "0..1",
            "description": "udgivelsesår eller trykkeår for kortet"
        },
        "bemrkning": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "0..1",
            "description": "kommentarer til en version af kortet"
        },
        "hkpnlink": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "0..1",
            "description": "hyperlink til kortet på Historiske Kort På Nettet (hkpn.dk)"
        }
    }
)
```