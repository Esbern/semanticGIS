---
title: Jordstykke
draft: false
type: entity
---

# Jordstykke

areal på jordoverfladen som er afgrænset af matrikelskel

### Semantic Template
```python
p.io.declare_input(
    output_name="jordstykke",
    attributes={
        "arealberegningsmetode": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.Matrikel.Arealberegningsmetode, str),
            "cardinality": "1..1",
            "description": "angivelse af beregningsmetoden for arealet på det pågældende jordstykke"
        },
        "arealbetegnelse": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "0..1",
            "description": "tekstlig beskrivelse af arealets art eller type"
        },
        "arealtype": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.Matrikel.Arealtype, str),
            "cardinality": "0..1",
            "description": "den registrerede type for arealet"
        },
        "brugsretsareal": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(bool),
            "cardinality": "0..1",
            "description": "et areal, der er stiftet en brugsret over for højest 30 år, såfremt arealet udgør en del af en samlet fast ejendom, eller for højest 10 år, såfremt arealet udgør en del af en umatrikuleret ejendom"
        },
        "delnummer": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "0..1",
            "description": "midlertidigt nummer tildelt jordstykket inden det får tildelt det endelige matrikelnummer"
        },
        "faelleslod": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(bool),
            "cardinality": "1..1",
            "description": "angiver om jordstykket er et fælleslod og dermed indgår i flere faste ejendomme"
        },
        "matrikelnummer": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "0..1",
            "description": "entydig identifikation af et jordstykke inden for et ejerlav"
        },
        "registreretareal": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "1..1",
            "description": "jordstykkets registrerede areal i Matriklen"
        },
        "vandarealinkludering": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.Matrikel.Vandarealinkludering, str),
            "cardinality": "1..1",
            "description": "angivelse af om et eventuelt vandareal indenfor jordstykket indgår i det registrerede areal for jordstykket."
        },
        "vejareal": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "0..1",
            "description": "det i matriklen registrerede areal for en ikke udskilt vej på jordstykket"
        },
        "vejarealberegningsstatus": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.Matrikel.Vejarealberegningsstatus, str),
            "cardinality": "1..1",
            "description": "angiver hvorvidt et eventuelt vejareal på jordstykket er beregnet"
        },
        "fredskov": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "0..1",
            "description": "registrering af om der er fredskovspligt, på et jordstykke der er skov"
        },
        "jordrente": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "0..1",
            "description": "registrering af om der på jordstykket hviler jordrenteforpligtigelse i henhold til Bekendtgørelse om statshusmandsbrug m.m. og jordrente"
        },
        "klitfredning": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "0..1",
            "description": "registrering af, om der på jordstykket er klitfredning jf. naturbeskyttelsesloven"
        },
        "majoratsskov": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "0..1",
            "description": "registrering af, om den fredskov som er registreret på jordstykket er noteret som majoratsskov i henhold til Skovloven"
        },
        "stormfald": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "0..*",
            "description": "registrering af, om der for jordstykket er udbetalt tilskud til oprydning eller gentilplantning af private fredskove, der er væltet som følge af storme."
        },
        "strandbeskyttelse": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "0..1",
            "description": "registrering af, om der på jordstykket er strandbeskyttelse jf. Naturbeskyttelsesloven"
        },
        "matrikulrsagsomharndretjordstykkevedsupplerendemaling": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.FK(dk.Matrikel.MatrikulærSag, str),
            "cardinality": "0..1",
            "description": ""
        },
        "samletfastejendomsomersamletafjordstykker": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.FK(dk.Matrikel.SamletFastEjendom, str),
            "cardinality": "1..1",
            "description": ""
        },
        "matrikulrsagsomharndretjordstykkevedskelforretning": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.FK(dk.Matrikel.MatrikulærSag, str),
            "cardinality": "0..1",
            "description": ""
        },
        "kommune": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.FK(dk.Matrikel.MatrikelKommune, str),
            "cardinality": "1..1",
            "description": ""
        },
        "region": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.FK(dk.Matrikel.MatrikelRegion, str),
            "cardinality": "1..1",
            "description": ""
        },
        "sogn": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.FK(dk.Matrikel.MatrikelSogn, str),
            "cardinality": "1..1",
            "description": ""
        },
        "ejerlav": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.FK(dk.Matrikel.Ejerlav, str),
            "cardinality": "1..1",
            "description": ""
        },
        "oprindelig": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.FK(dk.Matrikel.Jordstykke, str),
            "cardinality": "0..1",
            "description": ""
        },
        "forretningshndelse": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.Matrikel.MatrikulærtElementForretningshændelse, str),
            "cardinality": "1..1",
            "description": "den primære begivenhed i virkeligheden som udløste ændringen i data"
        },
        "sekundrforretningshndelse": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.Matrikel.MatrikulærtElementForretningshændelse, str),
            "cardinality": "0..*",
            "description": "de begivenheder i virkeligheden som udløste ændringen i data"
        },
        "forretningsomrade": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.Matrikel.MatrikelForretningsområde, str),
            "cardinality": "1..1",
            "description": "den del af den offentlige forretning der håndterer hændelsen og derved udvirker ændringen i data"
        },
        "forretningsproces": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.Matrikel.Sagskategori, str),
            "cardinality": "1..1",
            "description": "den manuelle eller IT-understøttede proces hvori forretningsområdet håndterer hændelsen"
        },
        "id_lokalid": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.PK(str),
            "cardinality": "1..1",
            "description": "unik identifikation af objektet"
        },
        "patnkthandling": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.Matrikel.PåtænktHandling, str),
            "cardinality": "0..1",
            "description": "den påtænkte handling for objekter med status 'Foreløbig'"
        },
        "registreringfra": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(datetime),
            "cardinality": "1..1",
            "description": "tidspunktet hvor registreringen af versionen af forretningsobjektet er foretaget"
        },
        "registreringsaktr": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "1..1",
            "description": "den aktør der har foretaget registreringen"
        },
        "registreringtil": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(datetime),
            "cardinality": "0..1",
            "description": "tidspunktet hvor versionen af et forretningsobjekt enten er blevet erstattet af en nyere version eller er logisk slettet."
        },
        "status": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.Matrikel.MatrikulærtElementStatus, str),
            "cardinality": "1..1",
            "description": "angivelse af hvor et forretningsobjekt er i sin livscyklus"
        },
        "virkningfra": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(datetime),
            "cardinality": "1..1",
            "description": "tidspunktet hvorfra forretningsobjektet har virkning"
        },
        "virkningsaktr": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "1..1",
            "description": "den aktør der har afstedkommet forretningsobjektets virkning"
        },
        "virkningtil": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(datetime),
            "cardinality": "0..1",
            "description": "tidspunktet hvor forretningsobjektets virkning ophører"
        },
        "senestesag": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.FK(dk.Matrikel.MatrikulærSag, str),
            "cardinality": "1..1",
            "description": ""
        }
    }
)
```