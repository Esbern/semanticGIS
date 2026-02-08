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
        "sag001byggesagsnummer": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": "angiver byggesagens journalnummer"
        },
        "sag002byggesagsdato": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(datetime),
            "description": "angiver  byggesagens dato"
        },
        "sag003byggetilladelsesdato": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(datetime),
            "description": "dato for byggetilladelse"
        },
        "sag004forventetpaabegyndelsesdato": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(datetime),
            "description": "dato for forventet påbegyndelse af byggeri"
        },
        "sag005paabegyndelsesdato": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(datetime),
            "description": "dato for påbegyndelse af byggeri"
        },
        "sag006ibrugtagningstilladelse": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(datetime),
            "description": "angiver dato for ibrugtagning"
        },
        "sag007henlaeggelse": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(datetime),
            "description": "angiver dato for henlæggelse af sag"
        },
        "sag008faerdigtbygningsareal": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(int),
            "description": "angiver det færdiggjorte bygningsareal"
        },
        "sag009forventetfuldfoertdato": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(datetime),
            "description": "angiver dato for forventet fuldførelse af byggeri"
        },
        "sag010fuldfoerelseafbyggeri": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(datetime),
            "description": "dato for fuldførelse af byggeri"
        },
        "sag012byggesagskode": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.bbr.lookups.byggesagskode, str),
            "description": "angiver koden for sagen"
        },
        "sag013anmeldelseafbyggearbejde": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(datetime),
            "description": "dato for anmeldelse af byggearbejde"
        },
        "sag016delvisibrugtagningstilladelse": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(datetime),
            "description": "dato for delvis tilladelse ibrugtagningstilladelse"
        },
        "sag017foreloebigfaerdiggjortbygningsareal": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(int),
            "description": "foreløbigt færdiggjort bygningsareal"
        },
        "sag018foreloebigfaerdiggjortantallejligheder": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(int),
            "description": "angiver foreløbigt færdiggjort antal lejligheder"
        },
        "sag019bygherreforhold": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.bbr.lookups.bygherreforhold, str),
            "description": "angiver hvem der er bygherre"
        },
        "sag024datoformodtagelseafansoegningombyggetilladelse": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(datetime),
            "description": "angiver dato for modtagelse af ansøgning om byggetilladelse"
        },
        "sag025datoforfyldestgoerendeansoegning": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(datetime),
            "description": "angiver dato for fyldestgørende ansøgning om byggetilladelse"
        },
        "sag026datofornaboorientering": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(datetime),
            "description": "angiver dato for igangsættelse af naboorientering"
        },
        "sag027datoforfaerdigbehandlingafnaboorientering": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(datetime),
            "description": "angiver dato for færdigbehandling af naboorientering"
        },
        "sag032litra": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": "angiver litra under byggesagen"
        },
        "sag033foreloebigfaerdiggjortantallejlighederudenkoekken": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(int),
            "description": "angiver antal færdiggjorte  lejligheder"
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
