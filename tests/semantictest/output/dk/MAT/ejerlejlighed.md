---
title: Ejerlejlighed
draft: false
type: entity
---

# Ejerlejlighed

lejlighed i en beboelsesejendom hvor hver enkelt lejlighed ejes særskilt og betragtes som selvstændig fast ejendom, mens de fælles dele og faciliteter ejes i fællesskab af en ejerforening

### Semantic Template
```python
p.io.declare_input(
    output_name="ejerlejlighed",
    attributes={
        "b_bygningpaafremmedgrundfladel": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": ""
        },
        "b_bygningpaafremmedgrundpunktl": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": ""
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
        "ejerlejlighedskort": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.mat.lookups.uri, str),
            "description": "sagsbilag hvorpå geometrien for ejerlejligheden og eventuelle ejerlejlighedslodder er illustreret"
        },
        "ejerlejlighedsnummer": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": "identifikation af den enkelte ejerlejlighed der ligger i en hovedejendom"
        },
        "feltliste": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": ""
        },
        "fordelingstalnaevner": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(int),
            "description": "udgør sammen med fordelingstalTæller ejerlejlighedens andel af ejendomsretten af den hovedejendom som ejerlejligheden indgår i"
        },
        "fordelingstaltaeller": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(int),
            "description": "udgør sammen med fordelingstalNævner ejerlejlighedens andel af ejendomsretten af den hovedejendom som ejerlejligheden indgår i"
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
        "ibygningpaafremmedgrund": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(bool),
            "description": "angiver, om ejerlejligheden er beliggende i en bygning på fremmed grund"
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
        "samletareal": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.mat.lookups.area, int),
            "description": "angiver det aktuelle, samlede areal for ejerlejligheden i kvadratmeter"
        },
        "samletfastejendomlokalid": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": ""
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
        "stedbestemmelsesgeometri": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": ""
        },
        "stedbestemmelsesreference": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": ""
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
