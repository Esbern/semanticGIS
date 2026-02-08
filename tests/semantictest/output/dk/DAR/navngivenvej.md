---
title: NavngivenVej
draft: false
type: entity
---

# NavngivenVej

et samlet færdselsareal, uafhængigt af kommunegrænser, for hvilket der er fastsat ét vejnavn

### Semantic Template
```python
p.io.declare_input(
    output_name="navngivenvej",
    attributes={
        "administreresafkommune": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.dar.lookups.kommunekode, str),
            "description": "angivelse af den kommune som registreringsansvarlig for vejnavn og geometri for den navngivne vej"
        },
        "beskrivelse": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": "kort beskrivelse af vejnavnets oprindelse eller betydning"
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
        "udtaltvejnavn": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": "vejnavnet skrevet fuldt ud, således som det udtales"
        },
        "vejadresseringsnavn": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": "forkortet udgave af vejnavnet på højst 20 tegn"
        },
        "vejnavn": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": "det fulde vejnavn defineret som: Et egennavn, som udpeger og benævner en del af vej- eller stinettet eller lignende færdselsarealer og områder"
        },
        "vejnavnebeliggenhed_oprindelse_kilde": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": ""
        },
        "vejnavnebeliggenhed_oprindelse_noejagtighedsklasse": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": ""
        },
        "vejnavnebeliggenhed_oprindelse_registrering": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(datetime),
            "description": ""
        },
        "vejnavnebeliggenhed_oprindelse_tekniskstandard": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": ""
        },
        "vejnavnebeliggenhed_vejnavnelinje": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": ""
        },
        "vejnavnebeliggenhed_vejnavneomraade": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": ""
        },
        "vejnavnebeliggenhed_vejtilslutningspunkter": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": ""
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
