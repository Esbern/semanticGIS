---
title: Formkurve0_5
draft: false
type: entity
---

# Formkurve0_5

generaliserede kurver med ækvidistance på 0.5m der giver et indtryk af terrænet ved repræsentation i mindre målestok

### Semantic Template
```python
p.io.declare_input(
    output_name="formkurve0_5",
    attributes={
        "geometri": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "1..1",
            "description": "objektets geografiske placering"
        },
        "kurveid": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(int),
            "cardinality": "1..1",
            "description": "nøgle, som binder de opklippede kurver sammen (ModerID for højdekurve)"
        },
        "objektnavn": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "1..1",
            "description": "navn på 10x10kmm celle i henhold til Det danske Kvadretnet"
        },
        "hjlpekurve": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(bool),
            "cardinality": "1..1",
            "description": "visuel hjælp til at skabe sammenhæng i kurvebilledet. Værdien true er en hjælpekurve"
        },
        "hjde": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(float),
            "cardinality": "1..1",
            "description": "kotens højde over terrænmodellens definerede 0"
        },
        "forretningshndelse": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.Højdekurver.HøjdekurveForretningshændelseVærdi, str),
            "cardinality": "1..1",
            "description": "den begivenhed i virkeligheden som udløste ændringen i data"
        },
        "forretningsomrade": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.Højdekurver.HøjdekurveForretningsområdeVærdi, str),
            "cardinality": "1..1",
            "description": "den del af den offentlige forretning, som håndterer hændelsen og derved udvirker ændringen i data"
        },
        "forretningsproces": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.Højdekurver.HøjdekurveForretningsprocesVærdi, str),
            "cardinality": "1..1",
            "description": "den manuelle eller IT-understøttede proces hvori forretningsområdet håndterer hændelsen"
        },
        "id_lokalid": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.PK(str),
            "cardinality": "1..1",
            "description": "persistent unik nøgle"
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
        "status": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.Højdekurver.HøjdekurveStatusVærdi, str),
            "cardinality": "1..1",
            "description": "angivelse af hvor et forvaltningsobjekt er i sin livscyklus"
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