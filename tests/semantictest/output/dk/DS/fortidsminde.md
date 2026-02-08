---
title: Fortidsminde
draft: false
type: entity
---

# Fortidsminde

menneskeskabt bygværk eller efterladenskaber af menneskelig aktivitet fra forhistorisk tid

### Semantic Template
```python
p.io.declare_input(
    output_name="fortidsminde",
    attributes={
        "dataansvarligmyndighed": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": "den myndighed, der afgør, til hvilket formål og med hvilke hjælpemidler der må foretages behandling af data"
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
        "forretningshaendelse": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.ds.lookups.stednavneforretningshændelseværdi, str),
            "description": "den begivenhed i 'virkeligheden' som udløser en ændring i data"
        },
        "forretningsomraade": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.ds.lookups.stednavneforretningsområdeværdi, str),
            "description": "den del af den offentlige forretning der håndterer hændelsen og derved udvirker ændringen i data"
        },
        "forretningsproces": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.ds.lookups.stednavneforretningsprocesværdi, str),
            "description": "den manuelle eller it-understøttede proces, hvori forretningsområdet håndterer hændelsen"
        },
        "fortidsmindetype": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.ds.lookups.fortidsmindeværdi, str),
            "description": "underinddeling af Fortidsminde på baggrund af historisk periode og mindets karakteristik"
        },
        "geometri": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.ds.lookups.gm_multipoint, str),
            "description": "opbygning af punkter og/eller linjer og/eller flader der tilsammen udgør en geografisk udstrækning"
        },
        "gmlid": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": ""
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
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
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
            "description": "den aktør der har foretaget en registrering"
        },
        "registreringtil": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(datetime),
            "description": "tidspunktet hvor en ny registrering er foretaget på objektet, og hvor denne version således ikke længere er den seneste"
        },
        "status": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.ds.lookups.navngivetstedstatusværdi, str),
            "description": "angivelse af hvor et forvaltningsobjekt er i sin livscyklus"
        },
        "virkningfra": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(datetime),
            "description": "tidspunktet hvorfra forvaltningsobjektet har virkning"
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
