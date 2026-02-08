---
title: SamletFastEjendom
draft: false
type: entity
---

# SamletFastEjendom

en vedvarende forening af et eller flere jordstykker som tilsammen udgør én ejendom

### Semantic Template
```python
p.io.declare_input(
    output_name="samletfastejendom",
    attributes={
        "arbejderbolig": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(bool),
            "description": "angiver om den samlede faste ejendom er en arbejderbolig"
        },
        "bfenummer": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(int),
            "description": "unikt fortløbende identifikation tildelt den specifikke bestemte fast ejendom"
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
        "erfaelleslod": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(bool),
            "description": "angiver, at typen af samlet fast ejendom er fælleslod"
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
            "role": sg.LOOKUP(dk.mat.lookups.gm_multisurface, str),
            "description": "objektets geografiske placering"
        },
        "hovedejendomopdeltiejerlejligh": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(bool),
            "description": "angiver, om den pågældende samlede faste ejendom er registreret som hovedejendom og opdelt i ejerlejligheder"
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
        "landbrugsnotering": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.mat.lookups.landbrugsnotering, str),
            "description": "angiver hvorvidt ejendommen er noteret som landbrugsejendom og derfor har landbrugspligt"
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
        "stedbestemmelsesreference": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": ""
        },
        "udskiltvej": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(bool),
            "description": "angiver, om der er tale om en udskilt, offentlig vej med selvstændigt matrikelnummer"
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
