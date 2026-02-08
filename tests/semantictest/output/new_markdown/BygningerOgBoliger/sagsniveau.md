---
title: Sagsniveau
draft: false
type: entity
---

# Sagsniveau

sagsniveau samler oplysninger om en BBR-entitets relation til den BBR Sag de indgår i

### Semantic Template
```python
p.io.declare_input(
    output_name="sagsniveau",
    attributes={
        "niveautype": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.BygningerOgBoliger.Niveautype, str),
            "cardinality": "1..1",
            "description": "angiver typen af sags- go stamdata"
        },
        "sagstype": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.BygningerOgBoliger.Sagstype, str),
            "cardinality": "1..1",
            "description": "angiver sagstypen"
        },
        "stamdataenhed": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.FK(dk.BygningerOgBoliger.Enhed, str),
            "cardinality": "0..1",
            "description": ""
        },
        "sagsdatagrund": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.FK(dk.BygningerOgBoliger.Grund, str),
            "cardinality": "0..1",
            "description": ""
        },
        "stamdatatekniskanlg": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.FK(dk.BygningerOgBoliger.TekniskAnlæg, str),
            "cardinality": "0..1",
            "description": ""
        },
        "stamdataetage": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.FK(dk.BygningerOgBoliger.Etage, str),
            "cardinality": "0..1",
            "description": ""
        },
        "sagsdataenhed": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.FK(dk.BygningerOgBoliger.Enhed, str),
            "cardinality": "0..1",
            "description": ""
        },
        "stamdatagrund": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.FK(dk.BygningerOgBoliger.Grund, str),
            "cardinality": "0..1",
            "description": ""
        },
        "sagsdatatekniskanlg": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.FK(dk.BygningerOgBoliger.TekniskAnlæg, str),
            "cardinality": "0..1",
            "description": ""
        },
        "sagsdataetage": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.FK(dk.BygningerOgBoliger.Etage, str),
            "cardinality": "0..1",
            "description": ""
        },
        "byggesag": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.FK(dk.BygningerOgBoliger.BBRSag, str),
            "cardinality": "0..1",
            "description": ""
        },
        "sagsdataopgang": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.FK(dk.BygningerOgBoliger.Opgang, str),
            "cardinality": "0..1",
            "description": ""
        },
        "sagsdatabygning": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.FK(dk.BygningerOgBoliger.Bygning, str),
            "cardinality": "0..1",
            "description": ""
        },
        "stamdataopgang": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.FK(dk.BygningerOgBoliger.Opgang, str),
            "cardinality": "0..1",
            "description": ""
        },
        "stamdatabygning": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.FK(dk.BygningerOgBoliger.Bygning, str),
            "cardinality": "0..1",
            "description": ""
        },
        "forretningshndelse": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.BygningerOgBoliger.Forretningshændelse, str),
            "cardinality": "1..1",
            "description": "kode for den forretningshændelse, som afstedkom opdateringen af bygværkselementet til den pågældende version"
        },
        "forretningsomrade": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.BygningerOgBoliger.Forretningsområde, str),
            "cardinality": "1..1",
            "description": "FORM-kode for det offentlige forretningsområde som har opdateret bygværkselementet til den pågældende version"
        },
        "status": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.BygningerOgBoliger.Livscyklus, str),
            "cardinality": "1..1",
            "description": "kode for bygværkselementets status i den pågældende version, dvs. elementets tilstand i den samlede livscyklus"
        },
        "forretningsproces": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.BygningerOgBoliger.Forretningsproces, str),
            "cardinality": "1..1",
            "description": "kode for den forretningshændelse, som afstedkom opdateringen af bygværkselementet til den pågældende version"
        },
        "id_lokalid": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.PK(str),
            "cardinality": "1..1",
            "description": "unik og uforanderlig identifikation af bygværkselementet igennem hele dets livscyklus"
        },
        "kommunekode": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.BygningerOgBoliger.Kommunekode, str),
            "cardinality": "1..1",
            "description": "kode der identificerer den kommune som bygværkselementet hører til"
        },
        "registreringfra": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(datetime),
            "cardinality": "1..1",
            "description": "tidspunktet hvor registreringen af den pågældende version af bygværkselementet er foretaget"
        },
        "registreringsaktr": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "1..1",
            "description": "kode som angiver hvilken aktør der har foretaget registreringen af den pågældende version af bygværkselementet"
        },
        "registreringtil": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(datetime),
            "cardinality": "0..1",
            "description": "tidspunktet hvor næste version af bygværkselementet registreres, og hvor denne version således ikke længere er den seneste"
        },
        "virkningfra": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(datetime),
            "cardinality": "1..1",
            "description": "tidspunktet hvor virkningen af den pågældende version af bygværkselementet er startet"
        },
        "virkningsaktr": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.BygningerOgBoliger.Virkningsaktør, str),
            "cardinality": "1..1",
            "description": "den aktør der har afstedkommet virkningsegenskaberne for den pågældende version af bygværkselementet"
        },
        "virkningtil": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(datetime),
            "cardinality": "0..1",
            "description": "tidspunktet hvor virkningen af den pågældende version af bygværkselementet ophører"
        }
    }
)
```