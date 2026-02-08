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
            "role": sg.LOOKUP(dk.DanmarksAdresser.Kommunekode, str),
            "cardinality": "1..1",
            "description": "angivelse af den kommune som registreringsansvarlig for vejnavn og geometri for den navngivne vej"
        },
        "beskrivelse": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "0..1",
            "description": "kort beskrivelse af vejnavnets oprindelse eller betydning"
        },
        "udtaltvejnavn": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "0..1",
            "description": "vejnavnet skrevet fuldt ud, således som det udtales"
        },
        "vejadresseringsnavn": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "0..1",
            "description": "forkortet udgave af vejnavnet på højst 20 tegn"
        },
        "vejnavn": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "0..1",
            "description": "det fulde vejnavn defineret som: Et egennavn, som udpeger og benævner en del af vej- eller stinettet eller lignende færdselsarealer og områder"
        },
        "vejnavnebeliggenhed": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "1..1",
            "description": "beskrivelse af den navngivne vejs omtrentlige geografiske beliggenhed. Vejnavnebeliggenheden er udtrykt enten ved en vejnavnelinje eller et vejnavneområde samt oprindelses- og kvalitetsoplysninger for stedfæstelsen af vejnavnebeliggenheden"
        },
        "postnummer": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.FK(dk.DanmarksAdresser.Postnummer, str),
            "cardinality": "1..*",
            "description": ""
        },
        "supplerendebynavn": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.FK(dk.DanmarksAdresser.SupplerendeBynavn, str),
            "cardinality": "0..*",
            "description": ""
        },
        "forretningshndelse": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.DanmarksAdresser.Forretningshændelse, str),
            "cardinality": "1..1",
            "description": "den forretningshændelse, som afstedkom opdateringen af adresseelementet til den pågældende version"
        },
        "forretningsomrade": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.DanmarksAdresser.Forretningsområde, str),
            "cardinality": "1..1",
            "description": "det forretningsområde som har opdateret adresseelementet til den pågældende version"
        },
        "forretningsproces": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.DanmarksAdresser.Forretningsproces, str),
            "cardinality": "1..1",
            "description": "den forretningsproces, som afstedkom opdateringen af adresseelementet til den pågældende version"
        },
        "id_lokalid": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.PK(str),
            "cardinality": "1..1",
            "description": "identifikation af adresseelementet igennem hele dets livscyklus"
        },
        "registreringfra": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(datetime),
            "cardinality": "1..1",
            "description": "tidspunktet hvor registreringen af den pågældende version af adresseelementet er foretaget"
        },
        "registreringsaktr": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "1..1",
            "description": "den aktør der har foretaget registreringen af den pågældende version af adresseelementet"
        },
        "registreringtil": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(datetime),
            "cardinality": "0..1",
            "description": "tidspunktet hvor en ny registrering på adresseelementet er foretaget, og hvor denne version således ikke længere er den seneste"
        },
        "status": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.DanmarksAdresser.Livscyklus, str),
            "cardinality": "1..1",
            "description": "adresseelementets status i den pågældende version, dvs. elementets tilstand i den samlede livscyklus"
        },
        "virkningfra": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(datetime),
            "cardinality": "1..1",
            "description": "tidspunktet hvorfra den pågældende version af adresseelementet har virkning"
        },
        "virkningsaktr": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.DanmarksAdresser.Virkningsaktør, str),
            "cardinality": "1..1",
            "description": "den aktør der har afstedkommet virkningsegenskaberne for den pågældende version af adresseelementet"
        },
        "virkningtil": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(datetime),
            "cardinality": "0..1",
            "description": "tidspunktet hvor virkningen af den pågældende version af adresseelementet ophører"
        }
    }
)
```