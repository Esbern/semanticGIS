---
title: AlternativAdresse
draft: false
type: entity
---

# AlternativAdresse

adresse som, hvis den er angivet, skal anvendes ved kommunikation med person eller virksomhed via post

### Semantic Template
```python
p.io.declare_input(
    output_name="alternativadresse",
    attributes={
        "adresselinje1": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": "formatet for udenlandske adresser er forskelligt, hvorfor adresser angives i op til 10 adresselinjer, hvis indhold varierer afhængig af landets standard"
        },
        "adresselinje10": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": "formatet for udenlandske adresser er forskelligt, hvorfor adresser angives i op til 10 adresselinjer, hvis indhold varierer afhængig af landets standard"
        },
        "adresselinje2": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": "formatet for udenlandske adresser er forskelligt, hvorfor adresser angives i op til 10 adresselinjer, hvis indhold varierer afhængig af landets standard"
        },
        "adresselinje3": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": "formatet for udenlandske adresser er forskelligt, hvorfor adresser angives i op til 10 adresselinjer, hvis indhold varierer afhængig af landets standard"
        },
        "adresselinje4": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": "formatet for udenlandske adresser er forskelligt, hvorfor adresser angives i op til 10 adresselinjer, hvis indhold varierer afhængig af landets standard"
        },
        "adresselinje5": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": "formatet for udenlandske adresser er forskelligt, hvorfor adresser angives i op til 10 adresselinjer, hvis indhold varierer afhængig af landets standard"
        },
        "adresselinje6": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": "formatet for udenlandske adresser er forskelligt, hvorfor adresser angives i op til 10 adresselinjer, hvis indhold varierer afhængig af landets standard"
        },
        "adresselinje7": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": "formatet for udenlandske adresser er forskelligt, hvorfor adresser angives i op til 10 adresselinjer, hvis indhold varierer afhængig af landets standard"
        },
        "adresselinje8": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": "formatet for udenlandske adresser er forskelligt, hvorfor adresser angives i op til 10 adresselinjer, hvis indhold varierer afhængig af landets standard"
        },
        "adresselinje9": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": "formatet for udenlandske adresser er forskelligt, hvorfor adresser angives i op til 10 adresselinjer, hvis indhold varierer afhængig af landets standard"
        },
        "altadrpersonpersonnr": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": ""
        },
        "altadrvirksomhedcvrnr": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(int),
            "description": ""
        },
        "behandlingsid": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": "persistent unik nøgle for den Ejerskabshændelse behandling eller Person/Virksomhedshændelse behandling, som objektet senest er ændret ved"
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
            "role": sg.LOOKUP(dk.ejf.lookups.ejerfortegnelseforretningshændelse, str),
            "description": "den begivenhed i virkeligheden som udløste ændringen i data"
        },
        "forretningsomraade": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.ejf.lookups.ejerfortegnelseforretningsområde, str),
            "description": "den del af den offentlige forretning der håndterer hændelsen og derved udvirker ændringen i data"
        },
        "forretningsproces": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.ejf.lookups.ejerfortegnelseforretningsproces, str),
            "description": "den manuelle eller IT-understøttede proces hvori forretningsområdet håndterer hændelsen"
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
        "landekodenumerisk": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.ejf.lookups.countrycode, str),
            "description": "entydig numerisk kode for det land, hvor adressen er beliggende"
        },
        "objectid": {
            "scale": MeasurementScale.RATIO,
            "role": sg.DES(int),
            "description": ""
        },
        "registreringfra": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(datetime),
            "description": "tidspunktet hvor registreringen er foretaget"
        },
        "registreringsaktoer": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": "den aktør der har foretaget registreringen"
        },
        "registreringtil": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(datetime),
            "description": "tidspunktet hvor en ny registrering er foretaget på objektet, og hvor denne version således ikke længere er den seneste"
        },
        "status": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.ejf.lookups.ejerfortegnelsestatusværdi, str),
            "description": "angivelse af hvor et forretningsobjekt er i sin livscyklus"
        },
        "virkningfra": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(datetime),
            "description": "tidspunktet hvorfra objektet har virkning"
        },
        "virkningsaktoer": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "description": "den aktør der har afstedkommet objektets virkning"
        },
        "virkningtil": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(datetime),
            "description": "tidspunktet hvor objektets virkning ophører"
        },
    }
)
```
