---
title: UdrejseIndrejse
draft: false
type: entity
---

# UdrejseIndrejse

Oplysning om førstegangsindrejse, udrejse og eventuel genindrejse.

### Semantic Template
```python
p.io.declare_input(
    output_name="udrejseindrejse",
    attributes={
        "cprlandekodeindrejse": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": ""
        },
        "cprlandekodeudrejse": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
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
        "personid": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": ""
        },
        "registreringfra": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(datetime),
            "description": ""
        },
        "status": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.cpr.lookups.status, str),
            "description": "Angiver status for UdrejseIndrejse"
        },
        "udenlandsadresselinie1": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": ""
        },
        "udenlandsadresselinie2": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": ""
        },
        "udenlandsadresselinie3": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": ""
        },
        "udenlandsadresselinie4": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": ""
        },
        "udenlandsadresselinie5": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": ""
        },
        "virkningfra": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": ""
        },
        "virkningfrausikkerhedsmarkering": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(bool),
            "description": ""
        },
        "virkningtil": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": ""
        },
        "virkningtilusikkerhedsmarkering": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(bool),
            "description": ""
        },
    }
)
```
