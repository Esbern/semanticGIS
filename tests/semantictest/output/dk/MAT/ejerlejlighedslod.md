---
title: Ejerlejlighedslod
draft: false
type: entity
---

# Ejerlejlighedslod

en ejerlejlighed kan bestå af flere arealer, som er fysisk adskilt fra hinanden. Disse arealer kaldes ejerlejlighedslodder

### Semantic Template
```python
p.io.declare_input(
    output_name="ejerlejlighedslod",
    attributes={
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
        "ejerlejlighedlokalid": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": ""
        },
        "etagebetegnelse": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": "angivelse af hvilken etage ejerlejlighedslodden er beliggende på."
        },
        "feltliste": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": ""
        },
        "forretningshaendelse": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.mat.lookups.matrikulærtelementforretningshændelse, str),
            "description": "den primære begivenhed i virkeligheden som udløste ændringen i data"
        },
        "forretningsomraade": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.mat.lookups.matrikelforretningsområde, str),
            "description": "den del af den offentlige forretning der håndterer hændelsen og derved udvirker ændringen i data"
        },
        "forretningsproces": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.mat.lookups.sagskategori, str),
            "description": "den manuelle eller IT-understøttede proces hvori forretningsområdet håndterer hændelsen"
        },
        "geometri": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.mat.lookups.gm_surface, str),
            "description": "objektets geografiske placering"
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
        "lodareal": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.mat.lookups.area, int),
            "description": "det registrerede areal for det pågældende ejerlejlighedslod"
        },
        "lodbeliggenhedstekst": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": "tekst, der angiver ejerlejlighedsloddens beliggenhed i relation til hovedejendommen."
        },
        "lodlitra": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": "bogstav, der bruges for at angive en underinddeling af en ejerlejlighed i ejerlejlighedslodder"
        },
        "objectid": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(int),
            "description": ""
        },
        "paataenkthandling": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.mat.lookups.påtænkthandling, str),
            "description": "den påtænkte handling for objekter med status 'Foreløbig'"
        },
        "registreringfra": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(datetime),
            "description": "tidspunktet hvor registreringen af versionen af forretningsobjektet er foretaget"
        },
        "registreringsaktoer": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": "den aktør der har foretaget registreringen"
        },
        "registreringtil": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(datetime),
            "description": "tidspunktet hvor versionen af et forretningsobjekt enten er blevet erstattet af en nyere version eller er logisk slettet."
        },
        "senestesaglokalid": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": ""
        },
        "status": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.mat.lookups.matrikulærtelementstatus, str),
            "description": "angivelse af hvor et forretningsobjekt er i sin livscyklus"
        },
        "virkningfra": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(datetime),
            "description": "tidspunktet hvorfra forretningsobjektet har virkning"
        },
        "virkningsaktoer": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": "den aktør der har afstedkommet forretningsobjektets virkning"
        },
        "virkningtil": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(datetime),
            "description": "tidspunktet hvor forretningsobjektets virkning ophører"
        },
    }
)
```
