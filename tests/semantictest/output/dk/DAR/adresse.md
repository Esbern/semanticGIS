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
            "description": "en læsbar struktur, som identificerer adressen fuldstændigt"
        },
        "bygning": {
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
        "doerbetegnelse": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": "betegnelse, som angiver den adgangsdør e.l. som adressen identificerer"
        },
        "doerpunkt": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.FK(dk.dar.adressepunkt, str),
            "description": "geografisk punkt, som udpeger beliggenheden af den adgangsdør e.l. som adressen identificerer"
        },
        "etagebetegnelse": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": "betegnelse, som angiver hvilken etage den del af bygningen som adressen identificerer, er beliggende på"
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
