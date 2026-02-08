---
title: Notat
draft: false
type: entity
---

# Notat

Notater til brug for kommunens forvaltning.

### Semantic Template
```python
p.io.declare_input(
    output_name="notat",
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
        "notatlinie": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": "Tekstfelt, der kan benyttes til fritekst i forbindelse med folkeregisternotater."
        },
        "notatnummer": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.cpr.lookups.number, int),
            "description": "Angiver en notatlinies nummer, idet en person kan have flere notatlinier."
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
            "description": "Status for notat."
        },
        "virkningfra": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": ""
        },
        "virkningtil": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": ""
        },
    }
)
```
