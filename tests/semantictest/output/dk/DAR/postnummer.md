---
title: Postnummer
draft: false
type: entity
---

# Postnummer

postnummer med tilhørende navn som indgår i det landsdækkende postnummersystem

### Semantic Template
```python
p.io.declare_input(
    output_name="postnummer",
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
        "forretningshaendelse": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.dar.lookups.forretningshændelse, str),
            "description": "den forretningshændelse, som afstedkom opdateringen af adresseelementet til den pågældende version"
        },
        "forretningsomraade": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.dar.lookups.forretningsområde, str),
            "description": "det forretningsområde som har opdateret adresseelementet til den pågældende version"
        },
        "forretningsproces": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.dar.lookups.forretningsproces, str),
            "description": "den forretningsproces, som afstedkom opdateringen af adresseelementet til den pågældende version"
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
        "navn": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": "navn på by, bydel e.l., som postnummeret omfatter"
        },
        "postnr": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": "kode på fire cifre som identificerer postnummeret"
        },
        "postnummerinddeling": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.dar.lookups.postnummerinddeling, str),
            "description": "reference til DAGI's objekt for dette postnummer"
        },
        "registreringfra": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(datetime),
            "description": "tidspunktet hvor registreringen af den pågældende version af adresseelementet er foretaget"
        },
        "registreringsaktoer": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": "den aktør der har foretaget registreringen af den pågældende version af adresseelementet"
        },
        "registreringtil": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(datetime),
            "description": "tidspunktet hvor en ny registrering på adresseelementet er foretaget, og hvor denne version således ikke længere er den seneste"
        },
        "status": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.dar.lookups.livscyklus, str),
            "description": "adresseelementets status i den pågældende version, dvs. elementets tilstand i den samlede livscyklus"
        },
        "virkningfra": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(datetime),
            "description": "tidspunktet hvorfra den pågældende version af adresseelementet har virkning"
        },
        "virkningsaktoer": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.dar.lookups.virkningsaktør, str),
            "description": "den aktør der har afstedkommet virkningsegenskaberne for den pågældende version af adresseelementet"
        },
        "virkningtil": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(datetime),
            "description": "tidspunktet hvor virkningen af den pågældende version af adresseelementet ophører"
        },
    }
)
```
