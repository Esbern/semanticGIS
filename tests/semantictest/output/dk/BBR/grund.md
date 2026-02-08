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
        "bestemtfastejendom": {
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
        "forretningshaendelse": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.bbr.lookups.forretningshændelse, str),
            "description": "kode for den forretningshændelse, som afstedkom opdateringen af bygværkselementet til den pågældende version"
        },
        "forretningsomraade": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.bbr.lookups.forretningsområde, str),
            "description": "FORM-kode for det offentlige forretningsområde som har opdateret bygværkselementet til den pågældende version"
        },
        "forretningsproces": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.bbr.lookups.forretningsproces, str),
            "description": "kode for den forretningshændelse, som afstedkom opdateringen af bygværkselementet til den pågældende version"
        },
        "gru009vandforsyning": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.bbr.lookups.vandforsyning, str),
            "description": "angiver forhold omkring vandforsyning for grunden"
        },
        "gru010afloebsforhold": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.bbr.lookups.afløbsforhold, str),
            "description": "angiver afløbsforhold for grunden"
        },
        "gru021udledningstilladelse": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.bbr.lookups.udledningstilladelse, str),
            "description": "angiver status for udledningstilladelse på grunden"
        },
        "gru022medlemskabafspildevandsforsyning": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.bbr.lookups.medlemsskabafsplidevandforsyning, str),
            "description": "angiver om der for grunden er indgået kontraktligt medlemskab af spildevandsforsyningsselskab"
        },
        "gru023paabudvedrspildevandsafledning": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.bbr.lookups.rensningspåbud, str),
            "description": "angiver om der er givet påbud vedr. spildevandsafledning på grunden"
        },
        "gru024fristvedrspildevandsafledning": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(datetime),
            "description": "angiver dato for frist for evt. påbud vedr. spildevandsafledning på grunden"
        },
        "gru025tilladelsetiludtraeden": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.bbr.lookups.tilladelsetiludtræden, str),
            "description": "angiver tilladelse til udtræden af det offentlige kloakfællesskab"
        },
        "gru026datofortilladelsetiludtraeden": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(datetime),
            "description": "angiver dato for tilladelse til udtræden af det offentlige kloakfællesskab"
        },
        "gru027tilladelsetilalternativbortskaffelseellerafledning": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.bbr.lookups.tilladelsetilalternativbortskaffelseellerafledning, str),
            "description": "angiver tilladelse til alternativ bortskaffelse eller afledning af spildevand"
        },
        "gru028datofortilladelsetilalternativbortskaffelseellerafledning": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(datetime),
            "description": "angiver dato for tilladelse til alternativ bortskaffelse eller afledning af spildevand"
        },
        "gru029dispensationfritagelseiftkollektivvarmeforsyning": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.bbr.lookups.dispensationfritagelseiftkollektivvarmeforsyning, str),
            "description": "angiver dispensation eller fritagelse ift kollektiv varmeforsyning"
        },
        "gru030datofordispensationfritagelseiftkollektivvarmeforsyning": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(datetime),
            "description": "angiver dato for dispensation eller fritagelse ift kollektiv varmeforsyning"
        },
        "gru500notatlinjer": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": "beskrivende tekstnotat om særlige forhold for dette BBR-element"
        },
        "husnummer": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": ""
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
        "kommunekode": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.bbr.lookups.kommunekode, str),
            "description": "kode der identificerer den kommune som bygværkselementet hører til"
        },
        "registreringfra": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(datetime),
            "description": "tidspunktet hvor registreringen af den pågældende version af bygværkselementet er foretaget"
        },
        "registreringsaktoer": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": "kode som angiver hvilken aktør der har foretaget registreringen af den pågældende version af bygværkselementet"
        },
        "registreringtil": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(datetime),
            "description": "tidspunktet hvor næste version af bygværkselementet registreres, og hvor denne version således ikke længere er den seneste"
        },
        "status": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.bbr.lookups.livscyklus, str),
            "description": "kode for bygværkselementets status i den pågældende version, dvs. elementets tilstand i den samlede livscyklus"
        },
        "virkningfra": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(datetime),
            "description": "tidspunktet hvor virkningen af den pågældende version af bygværkselementet er startet"
        },
        "virkningsaktoer": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.bbr.lookups.virkningsaktør, str),
            "description": "den aktør der har afstedkommet virkningsegenskaberne for den pågældende version af bygværkselementet"
        },
        "virkningtil": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(datetime),
            "description": "tidspunktet hvor virkningen af den pågældende version af bygværkselementet ophører"
        },
    }
)
```
