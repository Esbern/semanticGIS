---
title: Ejerskifte
draft: false
type: entity
---

# Ejerskifte

overdragelse af et eller flere Ejerskaber fra en ejerkreds til en anden

### Semantic Template
```python
p.io.declare_input(
    output_name="ejerskifte",
    attributes={
        "anmeldelsesdato": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(datetime),
            "description": "dato for anmeldelse til tinglysning"
        },
        "anmeldelsesidentifikator": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": "unik identifikation af en tinglysningsanmeldelse"
        },
        "behandlingsid": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": "persistent unik nøgle for den Ejerskabshændelse behandling eller Person/Virksomhedshændelse behandling, som objektet senest er ændret ved"
        },
        "bestemtfastejendombfenr": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(int),
            "description": ""
        },
        "betinget": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(bool),
            "description": "angivelse af, om Ejerskiftet er betinget"
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
        "forretningshaendelse": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.ejf.lookups.ejerfortegnelseforretningshændelse, str),
            "description": "den begivenhed i virkeligheden som udløste ændringen i data"
        },
        "forretningsomraade": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.ejf.lookups.ejerfortegnelseforretningsområde, str),
            "description": "den del af den offentlige forretning der håndterer hændelsen og derved udvirker ændringen i data"
        },
        "forretningsproces": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.ejf.lookups.ejerfortegnelseforretningsproces, str),
            "description": "den manuelle eller IT-understøttede proces hvori forretningsområdet håndterer hændelsen"
        },
        "fristdato": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": "dato for frist oplyst i tinglysningsmeddelelser, som er afsendt som følge af en tinglysning med frist"
        },
        "handelsoplysningerlokalid": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": ""
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
        "objectid": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(int),
            "description": ""
        },
        "overdragelsesmaade": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.ejf.lookups.overdragelsesmådeværdi, str),
            "description": "angiver på hvilken måde overdragelsen er foretaget"
        },
        "overtagelsesdato": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(datetime),
            "description": "dato for købers overtagelse af den købte andel af ejendommen"
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
        "status": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.ejf.lookups.ejerfortegnelsestatusværdi, str),
            "description": "angivelse af hvor et forretningsobjekt er i sin livscyklus"
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
