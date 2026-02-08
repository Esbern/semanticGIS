---
title: Husnummer
draft: false
type: entity
---

# Husnummer

betegnelse, som indgår i den samlede adressebetegnelse, idet den identificerer det adgangspunkt, som giver adgang til den eller de pågældende adresser

### Semantic Template
```python
p.io.declare_input(
    output_name="husnummer",
    attributes={
        "adgangsadressebetegnelse": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": "en læsbar struktur, som identificerer husnummeret fuldstændigt"
        },
        "adgangspunkt": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.FK(dk.dar.adressepunkt, str),
            "description": "et geografisk punkt i terrænplan, som repræsenterer en adresses beliggenhed"
        },
        "adgangtilbygning": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": ""
        },
        "adgangtiltekniskanlaeg": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": ""
        },
        "afstemningsomraade": {
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
        "geodanmarkbygning": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": ""
        },
        "husnummerretning": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.dar.lookups.gm_point, str),
            "description": "geografisk punkt, der anvendes til at angive retningen for et husnummer (husnummertekst), i forhold til Adgangspunktet, når det skal vises på et kort"
        },
        "husnummertekst": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": "husnummeret til adressen inklusive evt. bogstav"
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
        "jordstykke": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": ""
        },
        "kommuneinddeling": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": ""
        },
        "menighedsraadsafstemningsomraade": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": ""
        },
        "navngivenvej": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": ""
        },
        "placeretpaaforeloebigtjordstykke": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": ""
        },
        "postnummer": {
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
        "sogneinddeling": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": ""
        },
        "status": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.dar.lookups.livscyklus, str),
            "description": "adresseelementets status i den pågældende version, dvs. elementets tilstand i den samlede livscyklus"
        },
        "supplerendebynavn": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": ""
        },
        "vejmidte": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": "kode for vejmidte for hvilken navngivenvejkommunedel som husnummeret er tilknyttet. Angivet som kommundekode-vejkode"
        },
        "vejpunkt": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.FK(dk.dar.adressepunkt, str),
            "description": "et geografisk punkt, der repræsenterer det sted på den navngivne vej, som er adgangsgivende til et bestemt adgangspunkt"
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
