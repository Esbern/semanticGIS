---
title: Punktoprindelse
draft: false
type: entity
---

# Punktoprindelse

identifikation af oprindelse for punkter for et givent område

### Semantic Template
```python
p.io.declare_input(
    output_name="punktoprindelse",
    attributes={
        "datafordeleropdateringstid": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(datetime),
            "description": ""
        },
        "flyvedato": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": "dato for registrering af data"
        },
        "forretningshaendelse": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.dhmoprindelse.lookups.lidarforretningshændelseværdi, str),
            "description": "den begivenhed i virkeligheden som udløste ændringen i data"
        },
        "forretningsomraade": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.dhmoprindelse.lookups.lidarforretningsområdeværdi, str),
            "description": "den del af den offentlige forretning der håndterer hændelsen og derved udvirker ændringen i data"
        },
        "forretningsproces": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.dhmoprindelse.lookups.lidarforretningsprocesværdi, str),
            "description": "den manuelle eller IT-understøttede proces hvori forretningsområdet håndterer hændelsen"
        },
        "geometri": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.dhmoprindelse.lookups.gm_surface, str),
            "description": "objektets geografiske placering"
        },
        "hoejdenoejagtighed": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.dhmoprindelse.lookups.real, float),
            "description": "angivelse af nøjagtighed af data"
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
        "linjeid": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": "unik ID for den flyvelinje hvorfra data stammer"
        },
        "objectid": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": ""
        },
        "plannoejagtighed": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.dhmoprindelse.lookups.real, float),
            "description": "angivelse af plan nøjagtighed"
        },
        "produktionid": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": "en identifikation af hvilken produktion data stammer fra"
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
        "sensortype": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": "angivelse af hvilket udstyr der er anvendt til dataindsamling"
        },
        "status": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.dhmoprindelse.lookups.lidarstatusværdi, str),
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
