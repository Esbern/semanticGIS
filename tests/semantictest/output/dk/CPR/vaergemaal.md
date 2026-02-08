---
title: Vaergemaal
draft: false
type: entity
---

# Vaergemaal

Oplysninger om personer under værgemål efter værgemålslovens paragraf 6. Kan indeholde oplysning om relation til værge personnummer eller adressat.

### Semantic Template
```python
p.io.declare_input(
    output_name="vaergemaal",
    attributes={
        "adresselinie1": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": ""
        },
        "adresselinie2": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": ""
        },
        "adresselinie3": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": ""
        },
        "adresselinie4": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": ""
        },
        "adresselinie5": {
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
            "description": "Status for oplysningen."
        },
        "vaergemaalstype": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.cpr.lookups.vaergemaalstype, str),
            "description": "Angiver vaergemaalstype for Vaergemaal"
        },
        "vaergenavn": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": "Navn på værge hvis det er en virksomhed"
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
    }
)
```
