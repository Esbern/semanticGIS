---
title: Handelsoplysninger
draft: false
type: entity
---

# Handelsoplysninger

oplysninger som relaterer sig til Ejerskabshændelser der beskriver en ejendomshandel

### Semantic Template
```python
p.io.declare_input(
    output_name="handelsoplysninger",
    attributes={
        "afstaaelsesdato": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": "dato for ejerens afståelse af ejendommen"
        },
        "behandlingsid": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": "persistent unik nøgle for den Ejerskabshændelse behandling eller Person/Virksomhedshændelse behandling, som objektet senest er ændret ved"
        },
        "betalingsforpligtelsesdato": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": "dato for ny ejers overtagelse af betalingsforpligtigelser"
        },
        "bygningeromfattet": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": "angivelse af, om anmeldelsen omfatter bygninger"
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
        "entreprisesum": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(float),
            "description": "angiver beløbet for en entreprise"
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
        "husdyrbesaetningsum": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(float),
            "description": "værdi af husdyr som indgår i handlen"
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
        "koebsaftaledato": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": "dato for underskrift af købsaftale (kaldes også for slutseddel)"
        },
        "kontantkoebesum": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(float),
            "description": "den pris i rede penge, der skal betales ved køb af en fast ejendom"
        },
        "loesoeresum": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(float),
            "description": "aktiver, der overtages udenfor købesummen"
        },
        "objectid": {
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
        "samletkoebesum": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(float),
            "description": "det samlede beløb, som den eller de ejerskiftede ejendomme er blevet købt for"
        },
        "skoedetekst": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": "fri tekst, der kan følge med anmeldelsen"
        },
        "status": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.ejf.lookups.ejerfortegnelsestatusværdi, str),
            "description": "angivelse af hvor et forretningsobjekt er i sin livscyklus"
        },
        "valutakode": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.ejf.lookups.uomcurrency, str),
            "description": "angiver hvilken type valuta købesummen er beregnet i"
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
