---
title: Grund
draft: false
type: entity
---

# Grund

en grund er et sammenhængende areal, som består af et eller flere jordstykker (dvs. matrikelnumre), som udgør eller indgår i den samme samlede faste ejendom, jf. § 2 i lov om udstykning og anden registrering i matriklen

### Semantic Template
```python
p.io.declare_input(
    output_name="grund",
    attributes={
        "gru009vandforsyning": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.BygningerOgBoliger.Vandforsyning, str),
            "cardinality": "1..1",
            "description": "angiver forhold omkring vandforsyning for grunden"
        },
        "gru010aflbsforhold": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.BygningerOgBoliger.Afløbsforhold, str),
            "cardinality": "1..1",
            "description": "angiver afløbsforhold for grunden"
        },
        "gru021udledningstilladelse": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.BygningerOgBoliger.Udledningstilladelse, str),
            "cardinality": "1..1",
            "description": "angiver status for udledningstilladelse på grunden"
        },
        "gru022medlemskabafspildevandsforsyning": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.BygningerOgBoliger.MedlemsskabAfSplidevandforsyning, str),
            "cardinality": "1..1",
            "description": "angiver om der for grunden er indgået kontraktligt medlemskab af spildevandsforsyningsselskab"
        },
        "gru023pabudvedrspildevandsafledning": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.BygningerOgBoliger.Rensningspåbud, str),
            "cardinality": "1..1",
            "description": "angiver om der er givet påbud vedr. spildevandsafledning på grunden"
        },
        "gru024fristvedrspildevandsafledning": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(datetime),
            "cardinality": "1..1",
            "description": "angiver dato for frist for evt. påbud vedr. spildevandsafledning på grunden"
        },
        "gru025tilladelsetiludtrden": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.BygningerOgBoliger.TilladelseTilUdtræden, str),
            "cardinality": "1..1",
            "description": "angiver tilladelse til udtræden af det offentlige kloakfællesskab"
        },
        "gru026datofortilladelsetiludtrden": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(datetime),
            "cardinality": "1..1",
            "description": "angiver dato for tilladelse til udtræden af det offentlige kloakfællesskab"
        },
        "gru027tilladelsetilalternativbortskaffelseellerafledning": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.BygningerOgBoliger.TilladelseTilAlternativBortskaffelseEllerAfledning, str),
            "cardinality": "1..1",
            "description": "angiver tilladelse til alternativ bortskaffelse eller afledning af spildevand"
        },
        "gru028datofortilladelsetilalternativbortskaffelseellerafledning": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(datetime),
            "cardinality": "1..1",
            "description": "angiver dato for tilladelse til alternativ bortskaffelse eller afledning af spildevand"
        },
        "gru029dispensationfritagelseiftkollektivvarmeforsyning": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.BygningerOgBoliger.DispensationFritagelseIftKollektivVarmeforsyning, str),
            "cardinality": "1..1",
            "description": "angiver dispensation eller fritagelse ift kollektiv varmeforsyning"
        },
        "gru030datofordispensationfritagelseiftkollektivvarmeforsyning": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(datetime),
            "cardinality": "1..1",
            "description": "angiver dato for dispensation eller fritagelse ift kollektiv varmeforsyning"
        },
        "gru500notatlinjer": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "1..1",
            "description": "beskrivende tekstnotat om særlige forhold for dette BBR-element"
        },
        "husnummer": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.FK(dk.DanmarksAdresser.Husnummer, str),
            "cardinality": "0..1",
            "description": ""
        },
        "bestemtfastejendom": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.FK(dk.BygningerOgBoliger.Ejendomsrelation, str),
            "cardinality": "1..1",
            "description": ""
        },
        "jordstykker": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.FK(dk.Matrikel.Jordstykke, str),
            "cardinality": "0..*",
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