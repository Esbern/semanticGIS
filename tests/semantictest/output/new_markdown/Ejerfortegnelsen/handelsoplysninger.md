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
        "afstaelsesdato": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(date),
            "cardinality": "0..1",
            "description": "dato for ejerens afståelse af ejendommen"
        },
        "betalingsforpligtelsesdato": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(date),
            "cardinality": "0..1",
            "description": "dato for ny ejers overtagelse af betalingsforpligtigelser"
        },
        "kbsaftaledato": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(date),
            "cardinality": "0..1",
            "description": "dato for underskrift af købsaftale (kaldes også for slutseddel)"
        },
        "entreprisesum": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(float),
            "cardinality": "0..1",
            "description": "angiver beløbet for en entreprise"
        },
        "husdyrbestningsum": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(float),
            "cardinality": "0..1",
            "description": "værdi af husdyr som indgår i handlen"
        },
        "lsresum": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(float),
            "cardinality": "0..1",
            "description": "aktiver, der overtages udenfor købesummen"
        },
        "kontantkbesum": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(float),
            "cardinality": "0..1",
            "description": "den pris i rede penge, der skal betales ved køb af en fast ejendom"
        },
        "samletkbesum": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(float),
            "cardinality": "0..1",
            "description": "det samlede beløb, som den eller de ejerskiftede ejendomme er blevet købt for"
        },
        "valutakode": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "0..1",
            "description": "angiver hvilken type valuta købesummen er beregnet i"
        },
        "bygningeromfattet": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "0..1",
            "description": "angivelse af, om anmeldelsen omfatter bygninger"
        },
        "skdetekst": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "0..1",
            "description": "fri tekst, der kan følge med anmeldelsen"
        },
        "ejerskifte": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.FK(dk.Ejerfortegnelsen.Ejerskifte, str),
            "cardinality": "1..*",
            "description": ""
        },
        "id_lokalid": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.PK(str),
            "cardinality": "1..1",
            "description": "persistent unik nøgle"
        },
        "behandlingsid": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "1..1",
            "description": "persistent unik nøgle for den Ejerskabshændelse behandling eller Person/Virksomhedshændelse behandling, som objektet senest er ændret ved"
        },
        "forretningshndelse": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.Ejerfortegnelsen.EjerfortegnelseForretningshændelse, str),
            "cardinality": "1..1",
            "description": "den begivenhed i virkeligheden som udløste ændringen i data"
        },
        "forretningsomrade": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.Ejerfortegnelsen.EjerfortegnelseForretningsområde, str),
            "cardinality": "1..1",
            "description": "den del af den offentlige forretning der håndterer hændelsen og derved udvirker ændringen i data"
        },
        "forretningsproces": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.Ejerfortegnelsen.EjerfortegnelseForretningsproces, str),
            "cardinality": "1..1",
            "description": "den manuelle eller IT-understøttede proces hvori forretningsområdet håndterer hændelsen"
        },
        "status": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.Ejerfortegnelsen.EjerfortegnelsestatusVærdi, str),
            "cardinality": "1..1",
            "description": "angivelse af hvor et forretningsobjekt er i sin livscyklus"
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
        }
    }
)
```