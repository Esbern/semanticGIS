---
title: Naturareal
draft: false
type: entity
---

# Naturareal

geografisk miljø, primært kendetegnet ud fra ensartede bevoksnings- og jordbundsforhold

### Semantic Template
```python
p.io.declare_input(
    output_name="naturareal",
    attributes={
        "areal": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.ds.lookups.area, str),
            "description": "geografisk horisontal udstrækning af et Naturareal som flade"
        },
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
        "geometri": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.ds.lookups.gm_surface, str),
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
        "naturarealtype": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.ds.lookups.naturarealværdi, str),
            "description": "underinddeling af Naturareal på baggrund af mere botaniske og geologiske forhold"
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
