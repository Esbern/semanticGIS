---
title: Adresse
draft: false
type: entity
---

# Adresse

en struktureret betegnelse som angiver en særskilt adgang til et areal, en bygning eller en del af en bygning, efter reglerne i adressebekendtgørelsen

### Semantic Template
```python
p.io.declare_input(
    output_name="adresse",
    attributes={
        "adressebetegnelse": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "1..1",
            "description": "en læsbar struktur, som identificerer adressen fuldstændigt"
        },
        "drbetegnelse": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "0..1",
            "description": "betegnelse, som angiver den adgangsdør e.l. som adressen identificerer"
        },
        "drpunkt": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "0..1",
            "description": "geografisk punkt, som udpeger beliggenheden af den adgangsdør e.l. som adressen identificerer"
        },
        "etagebetegnelse": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "0..1",
            "description": "betegnelse, som angiver hvilken etage den del af bygningen som adressen identificerer, er beliggende på"
        },
        "bygning": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.FK(dk.BygningerOgBoliger.Bygning, str),
            "cardinality": "0..1",
            "description": ""
        },
        "husnummer": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.FK(dk.DanmarksAdresser.Husnummer, str),
            "cardinality": "1..1",
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