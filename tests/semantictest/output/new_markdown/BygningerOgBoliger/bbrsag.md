---
title: BBRSag
draft: false
type: entity
---

# BBRSag

en BBR sag indeholder de fælles oplysninger om et procesforløb, fx en byggesag, som berører en eller flere BBR-entiteter

### Semantic Template
```python
p.io.declare_input(
    output_name="bbrsag",
    attributes={
        "sag001byggesagsnummer": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "1..1",
            "description": "angiver byggesagens journalnummer"
        },
        "sag002byggesagsdato": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(datetime),
            "cardinality": "1..1",
            "description": "angiver byggesagens dato"
        },
        "sag003byggetilladelsesdato": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(datetime),
            "cardinality": "1..1",
            "description": "dato for byggetilladelse"
        },
        "sag004forventetpabegyndelsesdato": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(datetime),
            "cardinality": "1..1",
            "description": "dato for forventet påbegyndelse af byggeri"
        },
        "sag005pabegyndelsesdato": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(datetime),
            "cardinality": "1..1",
            "description": "dato for påbegyndelse af byggeri"
        },
        "sag006ibrugtagningstilladelse": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(datetime),
            "cardinality": "1..1",
            "description": "angiver dato for ibrugtagning"
        },
        "sag007henlggelse": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(datetime),
            "cardinality": "1..1",
            "description": "angiver dato for henlæggelse af sag"
        },
        "sag008frdigtbygningsareal": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(int),
            "cardinality": "1..1",
            "description": "angiver det færdiggjorte bygningsareal"
        },
        "sag009forventetfuldfrtdato": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(datetime),
            "cardinality": "1..1",
            "description": "angiver dato for forventet fuldførelse af byggeri"
        },
        "sag010fuldfrelseafbyggeri": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(datetime),
            "cardinality": "1..1",
            "description": "dato for fuldførelse af byggeri"
        },
        "sag012byggesagskode": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.BygningerOgBoliger.Byggesagskode, str),
            "cardinality": "1..1",
            "description": "angiver koden for sagen"
        },
        "sag013anmeldelseafbyggearbejde": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(datetime),
            "cardinality": "1..1",
            "description": "dato for anmeldelse af byggearbejde"
        },
        "sag016delvisibrugtagningstilladelse": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(datetime),
            "cardinality": "1..1",
            "description": "dato for delvis tilladelse ibrugtagningstilladelse"
        },
        "sag017forelbigfrdiggjortbygningsareal": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(int),
            "cardinality": "1..1",
            "description": "foreløbigt færdiggjort bygningsareal"
        },
        "sag018forelbigfrdiggjortantallejligheder": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(int),
            "cardinality": "1..1",
            "description": "angiver foreløbigt færdiggjort antal lejligheder"
        },
        "sag019bygherreforhold": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.BygningerOgBoliger.Bygherreforhold, str),
            "cardinality": "1..1",
            "description": "angiver hvem der er bygherre"
        },
        "sag024datoformodtagelseafansgningombyggetilladelse": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(datetime),
            "cardinality": "1..1",
            "description": "angiver dato for modtagelse af ansøgning om byggetilladelse"
        },
        "sag025datoforfyldestgrendeansgning": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(datetime),
            "cardinality": "1..1",
            "description": "angiver dato for fyldestgørende ansøgning om byggetilladelse"
        },
        "sag026datofornaboorientering": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(datetime),
            "cardinality": "1..1",
            "description": "angiver dato for igangsættelse af naboorientering"
        },
        "sag027datoforfrdigbehandlingafnaboorientering": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(datetime),
            "cardinality": "1..1",
            "description": "angiver dato for færdigbehandling af naboorientering"
        },
        "sag032litra": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "1..1",
            "description": "angiver litra under byggesagen"
        },
        "sag033forelbigfrdiggjortantallejlighederudenkkken": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(int),
            "cardinality": "1..1",
            "description": "angiver antal færdiggjorte lejligheder"
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