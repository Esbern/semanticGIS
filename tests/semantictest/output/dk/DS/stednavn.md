---
title: Stednavn
draft: false
type: entity
---

# Stednavn

egennavn eller betegnelse på en geografisk lokalitet

### Semantic Template
```python
p.io.declare_input(
    output_name="stednavn",
    attributes={
        "aktualitet": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.ds.lookups.aktualitetværdi, str),
            "description": "nutidig eller fortidig virkning for stednavnet"
        },
        "brugsprioritet": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.ds.lookups.brugsprioritetværdi, str),
            "description": "stednavnenes indbyrdes brugsmæssige prioritering på et specifikt NavngivetSted"
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
        "navnefoelgenummer": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(int),
            "description": "nummer der unikt identificerer et stednavn i konteksten af et given navngivet sted"
        },
        "navnestatus": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.ds.lookups.navnestatusværdi, str),
            "description": "stednavnenes indbyrdes prioritering ud fra pålidelighed, på et specifikt NavngivetSted"
        },
        "navngivetsted_objectid": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": ""
        },
        "objectid": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": ""
        },
        "oprettelsesdato": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(datetime),
            "description": "dato for oprettelse af første version af Stednavnet i databasen"
        },
        "skrivemaade": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": "stednavnets skriftlige form"
        },
        "sprog": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.ds.lookups.languagecode, str),
            "description": "sproget som er anvendt i skrivemåden"
        },
    }
)
```
