---
title: Ejendomsvurdering
draft: false
type: entity
---

# Ejendomsvurdering

Ingen definition fundet

### Semantic Template
```python
p.io.declare_input(
    output_name="ejendomsvurdering",
    attributes={
        "aar": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(int),
            "description": "Ingen definition fundet"
        },
        "aendringdato": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": "Ingen definition fundet"
        },
        "aendringkode": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.vur.lookups.ejendomsvurderingændringkode, str),
            "description": "Ingen definition fundet"
        },
        "ajourfoeringdato": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(datetime),
            "description": "Ingen definition fundet"
        },
        "antalmedvurderedelejligheder": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(int),
            "description": "Ingen definition fundet"
        },
        "benyttelsekode": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.vur.lookups.ejendomsvurderingbenyttelsekode, str),
            "description": "Ingen definition fundet"
        },
        "daekningsafgiftforskelvaerdi": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(int),
            "description": "Ingen definition fundet"
        },
        "daekningsafgiftpligtkode": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.vur.lookups.ejendomsvurderingdækningsafgiftpligtkode, str),
            "description": "Ingen definition fundet"
        },
        "daekningsafgiftpligttypekode": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.vur.lookups.ejendomsvurderingdækningsafgiftpligttypekode, str),
            "description": "Ingen definition fundet"
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
        "ejendomvaerdibeloeb": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(int),
            "description": "Ingen definition fundet"
        },
        "fkmoderejendomid": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(int),
            "description": ""
        },
        "fkvurderetunderid": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(int),
            "description": ""
        },
        "fkvurderingsejendomid": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(int),
            "description": ""
        },
        "grundvaerdibeloeb": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(int),
            "description": "Ingen definition fundet"
        },
        "id": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(int),
            "description": ""
        },
        "juridiskkategorikode": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(int),
            "description": "Ingen definition fundet"
        },
        "juridiskkategoritekst": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": "Ingen definition fundet"
        },
        "juridiskunderkategorikode": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(int),
            "description": "Ingen definition fundet"
        },
        "juridiskunderkategoritekst": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": "Ingen definition fundet"
        },
        "vurderetareal": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.vur.lookups.area, int),
            "description": "Ingen definition fundet"
        },
        "vurderingskredskode": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.vur.lookups.ejendomsvurderingvurderingskredskode, int),
            "description": "Ingen definition fundet"
        },
        "vurmark": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(int),
            "description": "Ingen definition fundet"
        },
    }
)
```
