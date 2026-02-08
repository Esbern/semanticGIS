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
            "cardinality": "1..1",
            "description": "en læsbar struktur, som identificerer husnummeret fuldstændigt"
        },
        "vejmidte": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "0..1",
            "description": "kode for vejmidte for hvilken navngivenvejkommunedel som husnummeret er tilknyttet. Angivet som kommundekode-vejkode"
        },
        "adgangspunkt": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "1..1",
            "description": "et geografisk punkt i terrænplan, som repræsenterer en adresses beliggenhed"
        },
        "husnummerretning": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "1..1",
            "description": "geografisk punkt, der anvendes til at angive retningen for et husnummer (husnummertekst), i forhold til Adgangspunktet, når det skal vises på et kort"
        },
        "husnummertekst": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "0..1",
            "description": "husnummeret til adressen inklusive evt. bogstav"
        },
        "vejpunkt": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "1..1",
            "description": "et geografisk punkt, der repræsenterer det sted på den navngivne vej, som er adgangsgivende til et bestemt adgangspunkt"
        },
        "sogneinddeling": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.FK(dk.DAGI.Sogneinddeling, str),
            "cardinality": "1..1",
            "description": ""
        },
        "geodanmarkbygning": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.FK(dk.GeoDanmark.Bygning, str),
            "cardinality": "0..1",
            "description": ""
        },
        "placeretpaforelbigtjordstykke": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.FK(dk.Matrikel.Jordstykke, str),
            "cardinality": "0..1",
            "description": ""
        },
        "adgangtiltekniskanlg": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.FK(dk.BygningerOgBoliger.TekniskAnlæg, str),
            "cardinality": "0..1",
            "description": ""
        },
        "jordstykke": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.FK(dk.Matrikel.Jordstykke, str),
            "cardinality": "0..1",
            "description": ""
        },
        "kommuneinddeling": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.FK(dk.DAGI.Kommuneinddeling, str),
            "cardinality": "1..1",
            "description": ""
        },
        "postnummer": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.FK(dk.DanmarksAdresser.Postnummer, str),
            "cardinality": "1..1",
            "description": ""
        },
        "menighedsradsafstemningsomrade": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.FK(dk.DanmarksAdresser.menighedsrådsafstemningsområde, str),
            "cardinality": "0..1",
            "description": ""
        },
        "navngivenvej": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.FK(dk.DanmarksAdresser.NavngivenVej, str),
            "cardinality": "0..1",
            "description": ""
        },
        "supplerendebynavn": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.FK(dk.DanmarksAdresser.SupplerendeBynavn, str),
            "cardinality": "0..1",
            "description": ""
        },
        "afstemningsomrade": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.FK(dk.DAGI.Afstemningsområde, str),
            "cardinality": "1..1",
            "description": ""
        },
        "adgangtilbygning": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.FK(dk.BygningerOgBoliger.Bygning, str),
            "cardinality": "0..1",
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