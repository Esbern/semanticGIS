---
title: svr skatteforvaltningvirksomhed
draft: false
type: entity
---

# svr skatteforvaltningvirksomhed

Ingen definition fundet

### Semantic Template
```python
p.io.declare_input(
    output_name="svr_skatteforvaltningvirksomhed",
    attributes={
        "annulleringskode": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(int),
            "description": "Ingen definition fundet"
        },
        "bibranche1": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.svr.lookups.branche, str),
            "description": "Ingen definition fundet"
        },
        "bibranche2": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.svr.lookups.branche, str),
            "description": "Ingen definition fundet"
        },
        "bibranche3": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.svr.lookups.branche, str),
            "description": "Ingen definition fundet"
        },
        "cvrnummer": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(int),
            "description": ""
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
        "hovedbranche": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.svr.lookups.branche, str),
            "description": "Ingen definition fundet"
        },
        "lokalid": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": ""
        },
        "namespace": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": ""
        },
        "registreringfra": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": ""
        },
        "registreringsaktor": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": ""
        },
        "registreringtil": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": ""
        },
        "senummer": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(int),
            "description": ""
        },
        "status": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.svr.lookups.status, str),
            "description": "Ingen definition fundet"
        },
        "virkningfra": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": ""
        },
        "virkningsaktor": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": ""
        },
        "virkningtil": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": ""
        },
        "virksomhedstype": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.svr.lookups.virksomhedtype, str),
            "description": "Ingen definition fundet"
        },
        "virksomhedstypetekst": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": ""
        },
    }
)
```
