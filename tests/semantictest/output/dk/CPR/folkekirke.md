---
title: Folkekirke
draft: false
type: entity
---

# Folkekirke

Oplysning om medlemskab af folkekirken, valgmenighed og tillige folkekirken, men fritaget for kirkeskat under udenlandsophold, fordi der betales kirkeskat til Dansk Kirke i Udlandet eller Dansk Sømandskirke eller ikke er medlem af folkekirken.

### Semantic Template
```python
p.io.declare_input(
    output_name="folkekirke",
    attributes={
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
            "description": "Status for oplysningen."
        },
        "tilhoersforhold": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.cpr.lookups.tilhoersforhold, str),
            "description": "Tilhørsforhold for oplysningen."
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
