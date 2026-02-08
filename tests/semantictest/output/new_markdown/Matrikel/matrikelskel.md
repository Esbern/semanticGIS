---
title: Matrikelskel
draft: false
type: entity
---

# Matrikelskel

en linje eller en polylinje (cirkelbue), der – sammen med mindst ét andet matrikelskel - afgrænser et jordstykke

### Semantic Template
```python
p.io.declare_input(
    output_name="matrikelskel",
    attributes={
        "administrativgrnsekode": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.Matrikel.Grænsekode, str),
            "cardinality": "1..1",
            "description": "angivelse af hvilke administrative inddelinger, der er sammenfaldende med skellet"
        },
        "geometri": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "1..1",
            "description": "objektets geografiske placering"
        },
        "oprindelsejournalnummer": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "0..1",
            "description": "identifikation af den sag, via journalnummer, som indeholder de måloplysninger der er brugt til at angive objektets placering"
        },
        "produktionsmetode": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.Matrikel.Produktionsmetode, str),
            "cardinality": "1..1",
            "description": "angivelse af hvilken metode og baggrundsmateriale, som matrikelskellet er produceret ved hjælp af"
        },
        "skeltype": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.Matrikel.Skeltype, str),
            "cardinality": "1..1",
            "description": "klassifikation af skellet ud fra skelhierarki"
        },
        "transformationsid": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(int),
            "cardinality": "0..1",
            "description": "transformationsID er en fortløbende nummerering af transformationerne inden for det enkelte ejerlav"
        },
        "venstrejordstykke": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.FK(dk.Matrikel.Jordstykke, str),
            "cardinality": "0..1",
            "description": ""
        },
        "matrikulrsagsomharndretmatrikelskel": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.FK(dk.Matrikel.MatrikulærSag, str),
            "cardinality": "0..1",
            "description": ""
        },
        "matrikulrsagsomfastlggermatrikelskel": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.FK(dk.Matrikel.MatrikulærSag, str),
            "cardinality": "0..1",
            "description": ""
        },
        "skelpunkt": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.FK(dk.Matrikel.Skelpunkt, str),
            "cardinality": "2..2",
            "description": ""
        },
        "hjrejordstykke": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.FK(dk.Matrikel.Jordstykke, str),
            "cardinality": "0..1",
            "description": ""
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