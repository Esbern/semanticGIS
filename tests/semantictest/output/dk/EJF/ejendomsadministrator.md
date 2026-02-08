---
title: Ejendomsadministrator
draft: false
type: entity
---

# Ejendomsadministrator

en Person eller Virksomhed (herunder udlændinge og andre uden et CPR/CVR-nummer) som administrerer betalinger og andre forhold vedr. én Bestemt Fast Ejendom

### Semantic Template
```python
p.io.declare_input(
    output_name="ejendomsadministrator",
    attributes={
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
        "feltliste": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
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
        "personellervirksomhedlokalid": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": ""
        },
        "personpersonnr": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": ""
        },
        "produktionsenhedpnr": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(int),
            "description": ""
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
        "stedbestemmelsesreference": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
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
        "virksomhedcvrnr": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(int),
            "description": ""
        },
    }
)
```
