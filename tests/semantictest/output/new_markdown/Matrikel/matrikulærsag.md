---
title: MatrikulærSag
draft: false
type: entity
---

# MatrikulærSag

helheden af de faktorer og omstændigheder der knytter sig til en matrikulær sag

### Semantic Template
```python
p.io.declare_input(
    output_name="matrikulærsag",
    attributes={
        "id_lokalid": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.PK(str),
            "cardinality": "1..1",
            "description": "unik fortløbende nummer, der identificerer en sag."
        },
        "sagsoperation": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "0..*",
            "description": "angiver hvilke typer af forandringer sagen indeholder"
        },
        "forretningshndelse": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.Matrikel.MatrikulærSagForretningshændelse, str),
            "cardinality": "1..1",
            "description": "den begivenhed i virkeligheden som udløste ændringen i data"
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
        "journaliseringsdato": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(date),
            "cardinality": "0..1",
            "description": "dato for den dag, hvor sagen er journaliseret af matrikelmyndigheden."
        },
        "kommune": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "0..1",
            "description": "den kommune matrikelnummeret hører til og som er blevet brugt til at stedfæste sagen"
        },
        "matrikelmyndighedensjournalnummer": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "0..1",
            "description": "det unikke sagsnummer som er tildelt af matrikelmyndigheden."
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
        "rekvirentref": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "0..1",
            "description": "den sagsansvarliges (ofte landinspektørens) eget journalnummer for sagen"
        },
        "sagstitel": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "0..1",
            "description": "den repræsentative tekst, der beskriver sagen"
        },
        "status": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.Matrikel.Sagsstatus, str),
            "cardinality": "1..1",
            "description": "angivelse af hvor sagen er i sin livscyklus"
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
            "description": "den aktør der har afstedkommet forvaltningsobjektets virkning"
        },
        "virkningtil": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(datetime),
            "cardinality": "0..1",
            "description": "tidspunktet hvor forretningsobjektets virkning ophører"
        },
        "geometri": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "0..1",
            "description": "objektets geografiske placering"
        },
        "ejerlav": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.FK(dk.Matrikel.Ejerlav, str),
            "cardinality": "0..1",
            "description": ""
        },
        "jordstykkesomstedfstermatrikulrsag": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.FK(dk.Matrikel.Jordstykke, str),
            "cardinality": "0..1",
            "description": ""
        },
        "skelpunktsomerfastlagtimatrikulrsag": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.FK(dk.Matrikel.Skelpunkt, str),
            "cardinality": "0..*",
            "description": ""
        },
        "skelpunktsomerndretvedsupplerendemalingimatrikulrsag": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.FK(dk.Matrikel.Skelpunkt, str),
            "cardinality": "0..*",
            "description": ""
        }
    }
)
```