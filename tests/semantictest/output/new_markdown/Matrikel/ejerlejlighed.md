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
        "bygningpafremmedgrundlokalid": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "0..1",
            "description": "unik identifikation af den bygning på fremmed grund som er hovedejendom for den pågældende ejerlejlighed"
        },
        "ejerlejlighedskort": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "0..1",
            "description": "sagsbilag hvorpå geometrien for ejerlejligheden og eventuelle ejerlejlighedslodder er illustreret"
        },
        "ejerlejlighedsnummer": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "1..1",
            "description": "identifikation af den enkelte ejerlejlighed der ligger i en hovedejendom"
        },
        "fordelingstalnvner": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(int),
            "cardinality": "1..1",
            "description": "udgør sammen med fordelingstalTæller ejerlejlighedens andel af ejendomsretten af den hovedejendom som ejerlejligheden indgår i"
        },
        "fordelingstaltller": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(int),
            "cardinality": "1..1",
            "description": "udgør sammen med fordelingstalNævner ejerlejlighedens andel af ejendomsretten af den hovedejendom som ejerlejligheden indgår i"
        },
        "ibygningpafremmedgrund": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(bool),
            "cardinality": "1..1",
            "description": "angiver, om ejerlejligheden er beliggende i en bygning på fremmed grund"
        },
        "samletareal": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "1..1",
            "description": "angiver det aktuelle, samlede areal for ejerlejligheden i kvadratmeter"
        },
        "ejendom": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.FK(dk.Matrikel.SamletFastEjendom, str),
            "cardinality": "0..1",
            "description": ""
        },
        "bygning": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.FK(dk.Matrikel.BygningPåFremmedGrund, str),
            "cardinality": "0..1",
            "description": ""
        },
        "bfenummer": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(int),
            "cardinality": "1..1",
            "description": "unikt fortløbende identifikation tildelt den specifikke bestemte fast ejendom"
        },
        "forretningshndelse": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.Matrikel.MatrikulærtElementForretningshændelse, str),
            "cardinality": "1..1",
            "description": "den primære begivenhed i virkeligheden som udløste ændringen i data"
        },
        "sekundrforretningshndelse": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.Matrikel.MatrikulærtElementForretningshændelse, str),
            "cardinality": "0..*",
            "description": "de begivenheder i virkeligheden som udløste ændringen i data"
        },
        "forretningsomrade": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.Matrikel.MatrikelForretningsområde, str),
            "cardinality": "1..1",
            "description": "den del af den offentlige forretning der håndterer hændelsen og derved udvirker ændringen i data"
        },
        "forretningsproces": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.Matrikel.Sagskategori, str),
            "cardinality": "1..1",
            "description": "den manuelle eller IT-understøttede proces hvori forretningsområdet håndterer hændelsen"
        },
        "id_lokalid": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.PK(str),
            "cardinality": "1..1",
            "description": "unik identifikation af objektet"
        },
        "patnkthandling": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.Matrikel.PåtænktHandling, str),
            "cardinality": "0..1",
            "description": "den påtænkte handling for objekter med status 'Foreløbig'"
        },
        "registreringfra": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(datetime),
            "cardinality": "1..1",
            "description": "tidspunktet hvor registreringen af versionen af forretningsobjektet er foretaget"
        },
        "registreringsaktr": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "1..1",
            "description": "den aktør der har foretaget registreringen"
        },
        "registreringtil": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(datetime),
            "cardinality": "0..1",
            "description": "tidspunktet hvor versionen af et forretningsobjekt enten er blevet erstattet af en nyere version eller er logisk slettet."
        },
        "status": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.Matrikel.MatrikulærtElementStatus, str),
            "cardinality": "1..1",
            "description": "angivelse af hvor et forretningsobjekt er i sin livscyklus"
        },
        "virkningfra": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(datetime),
            "cardinality": "1..1",
            "description": "tidspunktet hvorfra forretningsobjektet har virkning"
        },
        "virkningsaktr": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "1..1",
            "description": "den aktør der har afstedkommet forretningsobjektets virkning"
        },
        "virkningtil": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(datetime),
            "cardinality": "0..1",
            "description": "tidspunktet hvor forretningsobjektets virkning ophører"
        },
        "senestesag": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.FK(dk.Matrikel.MatrikulærSag, str),
            "cardinality": "1..1",
            "description": ""
        }
    }
)
```