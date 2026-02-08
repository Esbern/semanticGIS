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
            "cardinality": "1..1",
            "description": "formatet for udenlandske adresser er forskelligt, hvorfor adresser angives i op til 10 adresselinjer, hvis indhold varierer afhængig af landets standard"
        },
        "landekodenumerisk": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "1..1",
            "description": "entydig numerisk kode for det land, hvor adressen er beliggende"
        },
        "adresselinje2": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "0..1",
            "description": "formatet for udenlandske adresser er forskelligt, hvorfor adresser angives i op til 10 adresselinjer, hvis indhold varierer afhængig af landets standard"
        },
        "adresselinje3": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "0..1",
            "description": "formatet for udenlandske adresser er forskelligt, hvorfor adresser angives i op til 10 adresselinjer, hvis indhold varierer afhængig af landets standard"
        },
        "adresselinje4": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "0..1",
            "description": "formatet for udenlandske adresser er forskelligt, hvorfor adresser angives i op til 10 adresselinjer, hvis indhold varierer afhængig af landets standard"
        },
        "adresselinje5": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "0..1",
            "description": "formatet for udenlandske adresser er forskelligt, hvorfor adresser angives i op til 10 adresselinjer, hvis indhold varierer afhængig af landets standard"
        },
        "adresselinje6": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "0..1",
            "description": "formatet for udenlandske adresser er forskelligt, hvorfor adresser angives i op til 10 adresselinjer, hvis indhold varierer afhængig af landets standard"
        },
        "adresselinje7": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "0..1",
            "description": "formatet for udenlandske adresser er forskelligt, hvorfor adresser angives i op til 10 adresselinjer, hvis indhold varierer afhængig af landets standard"
        },
        "adresselinje8": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "0..1",
            "description": "formatet for udenlandske adresser er forskelligt, hvorfor adresser angives i op til 10 adresselinjer, hvis indhold varierer afhængig af landets standard"
        },
        "adresselinje9": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "0..1",
            "description": "formatet for udenlandske adresser er forskelligt, hvorfor adresser angives i op til 10 adresselinjer, hvis indhold varierer afhængig af landets standard"
        },
        "adresselinje10": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "0..1",
            "description": "formatet for udenlandske adresser er forskelligt, hvorfor adresser angives i op til 10 adresselinjer, hvis indhold varierer afhængig af landets standard"
        },
        "altadrperson": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.FK(dk.Person.Person, str),
            "cardinality": "0..1",
            "description": ""
        },
        "altadrvirksomhed": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.FK(dk.CentraleVirksomhedsregister.Virksomhed, str),
            "cardinality": "0..1",
            "description": ""
        },
        "id_lokalid": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.PK(str),
            "cardinality": "1..1",
            "description": "persistent unik nøgle"
        },
        "behandlingsid": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "1..1",
            "description": "persistent unik nøgle for den Ejerskabshændelse behandling eller Person/Virksomhedshændelse behandling, som objektet senest er ændret ved"
        },
        "forretningshndelse": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.Ejerfortegnelsen.EjerfortegnelseForretningshændelse, str),
            "cardinality": "1..1",
            "description": "den begivenhed i virkeligheden som udløste ændringen i data"
        },
        "forretningsomrade": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.Ejerfortegnelsen.EjerfortegnelseForretningsområde, str),
            "cardinality": "1..1",
            "description": "den del af den offentlige forretning der håndterer hændelsen og derved udvirker ændringen i data"
        },
        "forretningsproces": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.Ejerfortegnelsen.EjerfortegnelseForretningsproces, str),
            "cardinality": "1..1",
            "description": "den manuelle eller IT-understøttede proces hvori forretningsområdet håndterer hændelsen"
        },
        "status": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.LOOKUP(dk.Ejerfortegnelsen.EjerfortegnelsestatusVærdi, str),
            "cardinality": "1..1",
            "description": "angivelse af hvor et forretningsobjekt er i sin livscyklus"
        },
        "registreringfra": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(datetime),
            "cardinality": "1..1",
            "description": "tidspunktet hvor registreringen er foretaget"
        },
        "registreringtil": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(datetime),
            "cardinality": "0..1",
            "description": "tidspunktet hvor en ny registrering er foretaget på objektet, og hvor denne version således ikke længere er den seneste"
        },
        "registreringsaktr": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "1..1",
            "description": "den aktør der har foretaget registreringen"
        },
        "virkningfra": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(datetime),
            "cardinality": "1..1",
            "description": "tidspunktet hvorfra objektet har virkning"
        },
        "virkningtil": {
            "scale": MeasurementScale.INTERVAL,
            "role": sg.DES(datetime),
            "cardinality": "0..1",
            "description": "tidspunktet hvor objektets virkning ophører"
        },
        "virkningsaktr": {
            "scale": MeasurementScale.NOMINAL,
            "role": sg.DES(str),
            "cardinality": "1..1",
            "description": "den aktør der har afstedkommet objektets virkning"
        }
    }
)
```