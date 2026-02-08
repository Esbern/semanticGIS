---
title: Formkurve0 5
draft: false
type: entity
---

# Formkurve0 5

generaliserede kurver med ækvidistance på 0.5m der giver et indtryk af terrænet ved repræsentation i mindre målestok

### Semantic Template
```python
p.io.declare_input(
    output_name="formkurve0_5",
    attributes={
        "datafordeleropdateringstid": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(datetime),
            "description": ""
        },
        "forretningshaendelse": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.dhmhoejdekurver.lookups.højdekurveforretningshændelseværdi, str),
            "description": "den begivenhed i virkeligheden som udløste ændringen i data"
        },
        "forretningsomraade": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.dhmhoejdekurver.lookups.højdekurveforretningsområdeværdi, str),
            "description": "den del af den offentlige forretning, som håndterer hændelsen og derved udvirker ændringen i data"
        },
        "forretningsproces": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.dhmhoejdekurver.lookups.højdekurveforretningsprocesværdi, str),
            "description": "den manuelle eller IT-understøttede proces hvori forretningsområdet håndterer hændelsen"
        },
        "geometri": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.dhmhoejdekurver.lookups.gm_curve, str),
            "description": "objektets geografiske placering"
        },
        "gmlid": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": ""
        },
        "hjaelpekurve": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(bool),
            "description": "visuel hjælp til at skabe sammenhæng i kurvebilledet. Værdien true er en hjælpekurve"
        },
        "hoejde": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.dhmhoejdekurver.lookups.real, float),
            "description": "kotens højde over terrænmodellens definerede 0"
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
        "kurveid": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(int),
            "description": "nøgle, som binder de opklippede kurver sammen (ModerID for højdekurve)"
        },
        "objectid": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": ""
        },
        "objektnavn": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": "navn på 10x10kmm celle i henhold til Det danske Kvadretnet"
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
        "status": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.dhmhoejdekurver.lookups.højdekurvestatusværdi, str),
            "description": "angivelse af hvor et forvaltningsobjekt er i sin livscyklus"
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
