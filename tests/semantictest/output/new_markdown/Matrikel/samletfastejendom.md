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
            "cardinality": "0..1",
            "description": "angiver om den samlede faste ejendom er en arbejderbolig"
        },
        "erflleslod": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(bool),
            "cardinality": "1..1",
            "description": "angiver, at typen af samlet fast ejendom er fælleslod"
        },
        "geometri": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "1..1",
            "description": "objektets geografiske placering"
        },
        "hovedejendomopdeltiejerlejligheder": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(bool),
            "cardinality": "1..1",
            "description": "angiver, om den pågældende samlede faste ejendom er registreret som hovedejendom og opdelt i ejerlejligheder"
        },
        "landbrugsnotering": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.Matrikel.Landbrugsnotering, str),
            "cardinality": "0..1",
            "description": "angiver hvorvidt ejendommen er noteret som landbrugsejendom og derfor har landbrugspligt"
        },
        "udskiltvej": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(bool),
            "cardinality": "1..1",
            "description": "angiver, om der er tale om en udskilt, offentlig vej med selvstændigt matrikelnummer"
        },
        "jordstykke": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.FK(dk.Matrikel.Jordstykke, str),
            "cardinality": "0..*",
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